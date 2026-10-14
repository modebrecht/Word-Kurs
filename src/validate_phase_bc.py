"""Static QA for the two independent, student-facing phase pages."""
from __future__ import annotations
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "B": {"file": "phase-b.html", "sections": ("vergleichen", "entscheiden", "ausprobieren", "abgeben"),
          "components": ('data-tool="word"', 'data-tool="ki"', 'data-tool="dossier"',
                         'id="case-1"', 'id="case-2"', 'id="case-3"',
                         'id="choice"', 'id="copy-b"', 'id="compare"',
                         'id="autosave-b"', 'word-kurs.phase-b.v1',
                         'function saveB()', 'function restoreB()')},
    "C": {"file": "phase-c.html", "sections": ("fakten", "entwurf", "verbessern", "kontrolle"),
          "components": ('id="editor"', 'id="findings"', 'id="solutions"',
                         'id="copy-c"', 'id="reset-c"', 'id="checks"', 'id="check-c"',
                         'id="autosave-c"', 'word-kurs.phase-c.v1', 'function saveC()',
                         'function restoreC()', 'NICHT automatisch geprüft')},
}

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.extras = []
        self.sections = 0
        self.html_lang = False
        self.viewport = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang") == "de-CH"
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport = True
        if tag == "section":
            self.sections += 1
        if "id" in a:
            if a["id"] in self.ids:
                raise AssertionError("Duplicate ID: " + a["id"])
            self.ids.add(a["id"])
        if tag == "script" and a.get("src"):
            self.extras.append("external script: " + a["src"])
        if tag == "link" and a.get("href"):
            self.extras.append("external stylesheet: " + a["href"])
        if tag == "img" and a.get("src"):
            self.extras.append("image dependency: " + a["src"])
        if tag == "a":
            self.links.append(a.get("href", ""))

def main():
    for phase, info in PAGES.items():
        p = ROOT / info["file"]
        if not p.exists():
            raise AssertionError("Missing: " + p.name)
        h = p.read_text(encoding="utf8")
        parser = PageParser()
        parser.feed(h)
        parser.close()
        if not parser.html_lang or not parser.viewport:
            raise AssertionError("Wrong language/viewport: " + p.name)
        if parser.extras:
            raise AssertionError("Phase files must be independently usable: " + str(parser.extras))
        if any(x.startswith("http") or "zip" in x.lower() for x in parser.links):
            raise AssertionError("External or archive link: " + p.name)
        if parser.sections != 4 or any(x not in parser.ids for x in info["sections"]):
            raise AssertionError("Missing one of four task steps: " + p.name)
        if any(x not in h for x in info["components"]):
            raise AssertionError("Missing interactive component: " + p.name)
        if "ohne Note" not in h or "ohne Anmeldung" not in h:
            raise AssertionError("Student context unclear: " + p.name)
        if not {"index.html", "phase-b.html", "phase-c.html"}.issubset(parser.links):
            raise AssertionError("Cross-navigation incomplete: " + p.name)
        print(f"Phase {phase} structure PASS: 4 steps, self-contained, three local phase links")
    print("Phase B/C static QA PASS")

if __name__ == "__main__":
    main()
