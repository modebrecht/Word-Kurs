from pathlib import Path
from build_a1_a5 import build_all as build_a1_a5
from build_a6_a9 import build_all as build_a6_a9
from build_a10_a13 import build_all as build_a10_a12
from build_a13 import build_all as build_a13
from build_uebungstest import build_all as build_uebungstest
from build_steckbrief import build_all as build_steckbrief
from build_word_test import build_all as build_word_test

ROOT = Path(__file__).resolve().parents[1]


def write_readme():
    p = ROOT / 'arbeitsblaetter' / 'README.md'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('''# Arbeitsblätter

Vollständiger Arbeitsstand des Word-Kurses.

## Kurs

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
- A13 – Gesamtauftrag / Prüfungsvorbereitung

## Üben und Bewerten

- `Uebungstest_Word.docx` – unbenotetes Aufgabenblatt
- `Uebungstest_Ausgangsdokument.docx` – Ausgangsdatei zum Übungstest
- `Benoteter_Steckbrief.docx` – benoteter persönlicher Steckbrief inkl. Bewertungsraster
- `Word_Test.docx` – benoteter Word-Test
- `Word_Test_Ausgangsdokument.docx` – Ausgangsdatei zum Word-Test
- `Word_Test_Korrekturblatt.docx` – Korrekturraster und Notenschlüssel

`assets/` enthält die für Aufgaben und Tests benötigten Bilddateien sowie eingebettete Zielvorlagen.

Die DOCX-Dateien werden reproduzierbar aus `src/` erzeugt.
''', encoding='utf-8')


def main():
    build_a1_a5(ROOT)
    build_a6_a9(ROOT)
    build_a10_a12(ROOT)
    build_a13(ROOT)
    build_uebungstest(ROOT)
    build_steckbrief(ROOT)
    build_word_test(ROOT)
    write_readme()
    print('Generated complete Word course package in', ROOT / 'arbeitsblaetter')


if __name__ == '__main__':
    main()
