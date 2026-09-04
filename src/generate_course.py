from pathlib import Path
from build_a1_a5 import build_all as build_a1_a5
from build_a6_a9 import build_all as build_a6_a9
from build_a10_a13 import build_all as build_a10_a13

ROOT = Path(__file__).resolve().parents[1]


def write_readme():
    p = ROOT / 'arbeitsblaetter' / 'README.md'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('''# Arbeitsblätter

Aktueller Arbeitsstand des Word-Kurses.

- A1 – Text formatieren
- A2 – Nach Vorlage gestalten
- A3 – Absätze & Ordnung
- A4 – Listen & Nummerierungen
- A5 – Rette das Chaos-Dokument
- A6 – Seitenlayout
- A7 – Bilder in Word
- A8 – Tabellen
- A9 – Formatvorlagen & Überschriften
- A10 – Kopf- & Fusszeile / Seitenzahlen
- A11 – Dokument nach Vorlage nachbauen
- A12 – Selbstständig gestalten

`assets/` enthält die für Aufgaben benötigten Bilddateien sowie die eingebetteten Zielvorlagen.

Die DOCX-Dateien werden reproduzierbar aus `src/` erzeugt.
''', encoding='utf-8')


def main():
    # Single entry point used locally and by GitHub Actions.
    build_a1_a5(ROOT)
    build_a6_a9(ROOT)
    build_a10_a13(ROOT)
    write_readme()
    print('Generated A1-A12 in', ROOT / 'arbeitsblaetter')


if __name__ == '__main__':
    main()
