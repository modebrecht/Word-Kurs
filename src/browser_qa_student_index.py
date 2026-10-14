"""Real desktop/tablet/mobile Chromium checks for the Word course start page."""
from __future__ import annotations
import hashlib
import http.server
import json
import re
import threading
from pathlib import Path
from urllib.parse import urlsplit, unquote
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/browser"
CASES = (("desktop", 1440, 900, 3), ("tablet", 820, 1180, 2),
         ("mobile", 390, 844, 1), ("small-mobile", 320, 700, 1))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, fmt, *args):
        pass

class Server(http.server.ThreadingHTTPServer):
    daemon_threads = True

def check(page, name, columns):
    errors, bad = [], []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("requestfailed", lambda r: errors.append(r.url))
    page.on("response", lambda r: bad.append(f"{r.status} {r.url}")
            if r.status >= 400 and not r.url.endswith("favicon.ico") else None)
    res = page.goto("/", wait_until="networkidle")
    if res is None or res.status != 200 or page.title() != "Word-Kurs · Sek 8 | Aufgaben":
        raise AssertionError(f"{name}: failed to load page")
    if page.locator(".task-card").count() != 15 or page.locator(".task-preview").count() != 15:
        raise AssertionError(f"{name}: not 15 cards and previews")
    if page.locator("a[download]").count() != 18:
        raise AssertionError(f"{name}: download count changed")
    if page.locator(".task-preview img").count() != 13:
        raise AssertionError(f"{name}: expected 13 source thumbnails")
    for img in page.locator(".task-preview img").all():
        img.scroll_into_view_if_needed(timeout=10000)
        img.evaluate("""async im => {
            if (!im.complete) await new Promise((ok, fail) => {
                im.addEventListener('load', ok, {once:true});
                im.addEventListener('error', fail, {once:true});
            });
        }""")
        if not img.evaluate("im => im.complete && im.naturalWidth > 0 && im.naturalHeight > 0"):
            raise AssertionError(f"{name}: broken image {img.get_attribute('src')}")
    geometry = page.evaluate("""() => {
        const cards = [...document.querySelectorAll('.task-card')];
        const offenders = [];
        for (const [i, c] of cards.entries()) {
          const r = c.getBoundingClientRect();
          if (r.left < -1 || r.right > innerWidth + 1 || r.width < 240)
            offenders.push('card ' + (i+1));
          const title = c.querySelector('h3');
          if (title.scrollWidth > title.clientWidth + 2)
            offenders.push('title ' + (i+1));
          for (const a of c.querySelectorAll('a[download]')) {
            const b = a.getBoundingClientRect();
            if (b.left < r.left - 1 || b.right > r.right + 1 || a.scrollWidth > a.clientWidth + 3)
              offenders.push('button ' + (i+1));
          }
        }
        const grid = document.querySelector('.grid');
        return {
            viewportWidth: innerWidth,
            documentWidth: document.documentElement.scrollWidth,
            columns: getComputedStyle(grid).gridTemplateColumns.trim().split(/\s+/).length,
            offenders,
            brokenImages: [...document.querySelectorAll('img')]
                .filter(im => !im.complete || !im.naturalWidth).map(im => im.src),
        };
    }""")
    if geometry["documentWidth"] > geometry["viewportWidth"] + 1 or geometry["columns"] != columns or geometry["offenders"] or geometry["brokenImages"]:
        raise AssertionError(f"{name}: visual layout failed: {geometry}")
    if errors or bad:
        raise AssertionError(f"{name}: console/network errors: {errors} {bad}")
    for anchor in ("start", "aufbau", "selbst", "plus"):
        page.locator(f'.nav a[href="#{anchor}"]').click()
        if page.evaluate("x => location.hash", anchor) != "#" + anchor:
            raise AssertionError(f"{name}: navigation #{anchor} failed")
    page.goto("/", wait_until="networkidle")
    page.screenshot(path=str(OUT / f"{name}.png"), full_page=True, animations="disabled")
    return geometry

def check_downloads(page):
    page.goto("/", wait_until="networkidle")
    downloads = []
    links = page.locator(".card-actions a[download]")
    for index in range(links.count()):
        link = links.nth(index)
        href, filename = link.get_attribute("href"), link.get_attribute("download")
        src = (ROOT / unquote(urlsplit(href).path)).resolve()
        if not src.is_relative_to(ROOT.resolve()):
            raise AssertionError(f"Unsafe download path: {href}")
        with page.expect_download(timeout=15000) as ev:
            link.click()
        dl = ev.value
        if dl.failure() or dl.suggested_filename != filename:
            raise AssertionError(f"Download failed or wrong name: {href}")
        a = hashlib.sha256(src.read_bytes()).hexdigest()
        b = hashlib.sha256(Path(dl.path()).read_bytes()).hexdigest()
        if a != b:
            raise AssertionError(f"Corrupt download: {href}")
        downloads.append({"name": filename, "bytes": src.stat().st_size, "sha256": a})
    if len(downloads) != 18:
        raise AssertionError(f"Expected 18 real file downloads, got {len(downloads)}")
    return downloads

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    evidence = {}
    with Server(("127.0.0.1", 0), QuietHandler) as server:
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            port = server.server_address[1]
            with sync_playwright() as pw:
                browser = pw.chromium.launch(headless=True, args=["--no-sandbox"])
                try:
                    for name, width, height, columns in CASES:
                        context = browser.new_context(
                            base_url=f"http://127.0.0.1:{port}",
                            viewport={"width": width, "height": height},
                            device_scale_factor=1, accept_downloads=True,
                            reduced_motion="reduce",
                        )
                        page = context.new_page()
                        details = check(page, name, columns)
                        if name == "desktop":
                            evidence["downloads"] = check_downloads(page)
                        if name == "mobile":
                            page.goto("/", wait_until="networkidle")
                            with page.expect_download() as dl:
                                page.locator('#a7 a[download]').last.click()
                            if dl.value.suggested_filename != "a7_schulhaus.png":
                                raise AssertionError("Mobile A7 picture download failed")
                        evidence[name] = details
                        context.close()
                finally:
                    browser.close()
        finally:
            server.shutdown()
            thread.join(timeout=8)
    report = {
        "status": "BROWSER_QA_PASS",
        "engine": "Playwright / Chromium / localhost",
        "scope": "real browser QA, not deployed hosting or native Word 365",
        "screenshots": [f"{x[0]}.png" for x in CASES],
        "results": evidence,
    }
    (OUT / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("BROWSER QA PASS: 15 cards / 13 preview assets / 18 SHA256-confirmed downloads / four viewport sizes")

if __name__ == "__main__":
    main()
