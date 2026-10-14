"""Prüft die veröffentlichbare Word-Kurs-Schülerseite ohne externe Abhängigkeiten."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "index.html"
BANNED = ("word_test", "korrekturblatt", "benoteter_steckbrief", "uebungstest", ".zip")
EXPECTED_IMAGES = {
    "a7_schulhaus.png",
}
EXPECTED_DOCX = {
    "A1_Text_formatieren.docx", "A2_Nach_Vorlage_gestalten.docx",
    "A3_Absaetze_und_Ordnung.docx", "A4_Listen_und_Nummerierungen.docx",
    "A5_Rette_das_Chaos_Dokument.docx", "A6_Seitenlayout.docx",
    "A7_Bilder_in_Word.docx", "A8_Tabellen.docx",
    "A9_Formatvorlagen_und_Ueberschriften.docx",
    "A10_Kopf_Fusszeile_Seitenzahlen.docx",
    "A11_Dokument_nach_Vorlage_nachbauen.docx",
    "A12_Selbststaendig_gestalten.docx",
    "A13_Gesamtauftrag_Pruefungsvorbereitung.docx",
    "ZUSATZ_Schnupperlehrbrief.docx", "START_Schnupperlehrbrief.docx",
    "ZUSATZ_Links_und_Quellen.docx", "START_Links_und_Quellen.docx",
}


class IndexLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.downloads = []
        self.assets = []
        self.codes = []
        self.images_without_alt = []
        self.page_lang_ok = False
        self.viewport_ok = False
        self.external = []

    def handle_starttag(self, tag, rawattrs):
        a = dict(rawattrs)
        if tag == "html" and a.get("lang") == "de-CH":
            self.page_lang_ok = True
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport_ok = True
        for key in ("href", "src"):
            value = a.get(key, "")
            if not value or value.startswith("#"):
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or value.startswith("//"):
                self.external.append(value)
                continue
            if not value.startswith("arbeitsblaetter/") and not value.startswith("qa/"):
                raise RuntimeError(f"Unerwarteter Pfad in Schülerseite: {value}")
            path = Path(unquote(url.path))
            if ".." in path.parts or path.is_absolute() or not (ROOT / path).is_file():
                raise RuntimeError(f"Fehlende/verbotene Ressource: {value}")
            self.assets.append(path.as_posix())
            if tag == "a":
                if not a.get("download") or not a.get("aria-label"):
                    raise RuntimeError(f"Unklarer Schülerdownload: {value}")
                self.downloads.append(path)
            if tag == "img" and not a.get("alt", "").strip():
                self.images_without_alt.append(value)


def validate() -> None:
    html = SITE.read_text(encoding="utf-8")
    content = html.lower()
    if any(x in content for x in BANNED):
        raise RuntimeError("Schülerseite enthält Prüfungs-, Lehrer- oder Archivverweise.")
    if "<script" in content or "http://" in content or "https://" in content:
        raise RuntimeError("Die Schülerseite soll ohne externe Dienste und Skripte funktionieren.")
    parser = IndexLinks()
    parser.feed(html)
    parser.close()
    if not parser.page_lang_ok or not parser.viewport_ok:
        raise RuntimeError("Sprache oder responsiver Viewport fehlt.")
    if parser.external or parser.images_without_alt:
        raise RuntimeError(f"Externe Links oder Bilder ohne Alternativtext: {parser.external} / {parser.images_without_alt}")
    docx = [p.name for p in parser.downloads if p.suffix.lower() == ".docx"]
    images = [p.name for p in parser.downloads if p.suffix.lower() == ".png"]
    if set(docx) != EXPECTED_DOCX or len(docx) != len(EXPECTED_DOCX):
        raise RuntimeError(f"Word-Downloads stimmen nicht: {sorted(set(docx)^EXPECTED_DOCX)}")
    if set(images) != EXPECTED_IMAGES or len(images) != len(EXPECTED_IMAGES):
        raise RuntimeError(f"Bild-Downloads stimmen nicht: {images}")
    if len(parser.downloads) != 18:
        raise RuntimeError(f"Erwartet 18 einzelne Downloads, gefunden {len(parser.downloads)}.")
    for i in (11, 12, 13):
        fragment = html.split(f'id="a{i}"', 1)[1].split("</article>", 1)[0]
        if "Bild herunterladen" in fragment:
            raise RuntimeError(f"A{i} darf keinen zweiten Bilddownload benötigen.")
    for i in range(1, 14):
        if not re.search(r'class="task-number">A' + str(i) + r"</span>", html):
            raise RuntimeError(f"A{i} fehlt.")
    for code in ("PLUS 1", "PLUS 2"):
        if f'class="task-number">{code}</span>' not in html:
            raise RuntimeError(f"{code} fehlt.")
    print(f"Student index PASS: 13 Pflichtkacheln + 2 PLUS, {len(docx)} Word- und {len(images)} Bild-Downloads, {len(parser.assets)} überprüfte Pfade, nur A7 mit separatem Bild; keine ZIP/Prüfungen/externen Abhängigkeiten.")


if __name__ == "__main__":
    validate()
