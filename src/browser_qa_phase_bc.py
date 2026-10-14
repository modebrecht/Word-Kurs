"""Playwright checks for phase B/C interactive teaching pages (real Chromium)."""
from __future__ import annotations
import http.server
import json
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/browser"
VIEWPORTS = (("desktop", 1365, 820), ("tablet", 820, 1180),
             ("mobile", 390, 844), ("small-mobile", 320, 720))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, fmt, *args):
        pass

def test_b(page):
    page.locator('[data-tool="ki"]').click()
    assert "Textentwurf" in page.locator("#demo-preview").inner_text()
    assert page.locator('[data-tool="ki"]').get_attribute("aria-pressed") == "true"
    page.locator('[data-tool="dossier"]').click()
    assert "bewerbungsdossier" in page.locator("#demo-preview").inner_text().lower()
    page.locator('[data-tool="word"]').click()
    assert "Word" in page.locator("#demo-preview").inner_text()
    for n, v in [(1, "word"), (2, "ki"), (3, "dossier")]:
        page.locator("#case-" + str(n)).select_option(v)
    page.locator("#compare").click()
    for n in range(1, 4):
        assert len(page.locator("#feedback-" + str(n)).inner_text()) > 25
    page.locator("#choice").select_option("Word")
    page.locator("#reason").fill("Damit ich den Text direkt selbst ändern kann.")
    page.locator("#check").fill("Die Fakten und die Lesbarkeit.")
    page.locator("#copy-b").click()
    page.wait_for_timeout(150)
    assert ("Kopiert" in page.locator("#copy-status").inner_text()
            or "Kopieren nicht möglich" in page.locator("#copy-status").inner_text())

def test_c(page):
    assert not page.locator("#solutions").evaluate("(e) => e.open")
    assert "9. Klasse" in page.locator("#editor").input_value()
    page.locator("#findings").fill("Beruf, Klasse, Enddatum, Erfahrung und Photoshop sind falsch.")
    page.locator("#editor").fill(
        "Lina Berger\nAtelier Nord AG\nSchnupperlehre Mediamatikerin EFZ\n"
        "Guten Tag Frau Widmer\nIch bin in der 8. Klasse. Vom 10. bis 12. März 2027 "
        "würde ich gerne bei Ihnen schnuppern. Ich fotografiere gern und "
        "habe in der Schule ein Plakat gestaltet.\nFreundliche Grüsse\nLina Berger")
    page.locator("#copy-c").click()
    page.wait_for_timeout(150)
    assert "Kopiert" in page.locator("#editor-status").inner_text() or "Strg + C" in page.locator("#editor-status").inner_text()
    for check in page.locator("#checks input[type=checkbox]").all():
        check.check()
    page.locator("#check-c").click()
    assert "Alle fünf Punkte" in page.locator("#check-status").inner_text()
    page.locator("#solutions summary").click()
    assert page.locator("#solutions").evaluate("(e) => e.open")
    page.once("dialog", lambda d: d.accept())
    page.locator("#reset-c").click()
    assert "9. Klasse" in page.locator("#editor").input_value()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    result = {}
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server = threading.Thread(target=httpd.serve_forever, daemon=True)
    server.start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
            try:
                for name, width, height in VIEWPORTS:
                    context = browser.new_context(viewport={"width": width, "height": height},
                                                  base_url="http://127.0.0.1:" + str(httpd.server_address[1]),
                                                  permissions=["clipboard-read", "clipboard-write"],
                                                  reduced_motion="reduce")
                    page = context.new_page()
                    for phase in ("b", "c"):
                        errors = []
                        page.on("pageerror", lambda e: errors.append(str(e)))
                        response = page.goto("/phase-" + phase + ".html", wait_until="networkidle")
                        if response.status != 200:
                            raise AssertionError("Page unavailable " + phase)
                        if page.locator(".section").count() != 4:
                            raise AssertionError("Expected four steps " + phase)
                        if page.locator('a[href="index.html"]').count() < 1:
                            raise AssertionError("Missing phase A navigation")
                        geometry = page.evaluate("""() => ({
                          screen: innerWidth, page: document.documentElement.scrollWidth,
                          sections: document.querySelectorAll('.section').length,
                          clipped: [...document.querySelectorAll('.section,.btn,textarea,select')]
                            .filter(e => {let b=e.getBoundingClientRect();return b.left < -1 || b.right > innerWidth + 1;})
                            .map(e=>e.tagName + '#' + e.id)
                        })""")
                        if geometry["page"] > geometry["screen"] + 1 or geometry["clipped"]:
                            raise AssertionError("Responsive overflow " + name + " phase " + phase + ": " + str(geometry))
                        page.screenshot(path=str(OUT / ("phase-" + phase + "-" + name + ".png")),
                                        full_page=True, animations="disabled")
                        if phase == "b":
                            test_b(page)
                        else:
                            test_c(page)
                        if errors:
                            raise AssertionError("Browser JS errors: " + str(errors))
                        result[phase + "-" + name] = geometry
                    context.close()
            finally:
                browser.close()
    finally:
        httpd.shutdown()
        server.join(timeout=7)
    data = {"status": "PASS", "scope": "localhost Chromium, no live AI/provider integration",
            "viewports": len(VIEWPORTS), "pages": 2, "screenshots": 8, "results": result}
    (OUT / "phase-bc-report.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf8")
    print("Phase B/C real Chromium QA PASS: 2 interactive pages x 4 viewport sizes")

if __name__ == "__main__":
    main()
