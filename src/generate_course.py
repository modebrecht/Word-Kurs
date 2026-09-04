from pathlib import Path

import build_a1_a5
import build_a6_a9
import build_a10_a13
import build_a13
import build_uebungstest
import build_steckbrief
import build_word_test
from build_runtime import install_deterministic_docx_save, resolve_font_paths, staged_course_root

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_OUTPUTS = {
    'A1_Text_formatieren.docx',
    'A2_Nach_Vorlage_gestalten.docx',
    'A3_Absaetze_und_Ordnung.docx',
    'A4_Listen_und_Nummerierungen.docx',
    'A5_Rette_das_Chaos_Dokument.docx',
    'A6_Seitenlayout.docx',
    'A7_Bilder_in_Word.docx',
    'A8_Tabellen.docx',
    'A9_Formatvorlagen_und_Ueberschriften.docx',
    'A10_Kopf_Fusszeile_Seitenzahlen.docx',
    'A11_Dokument_nach_Vorlage_nachbauen.docx',
    'A12_Selbststaendig_gestalten.docx',
    'A13_Gesamtauftrag_Pruefungsvorbereitung.docx',
    'Uebungstest_Word.docx',
    'Uebungstest_Ausgangsdokument.docx',
    'Benoteter_Steckbrief.docx',
    'Word_Test.docx',
    'Word_Test_Ausgangsdokument.docx',
    'Word_Test_Korrekturblatt.docx',
    'README.md',
}


def write_readme(root: Path):
    p = root / 'arbeitsblaetter' / 'README.md'
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


def _configure_portable_preview_fonts():
    regular, bold = resolve_font_paths()
    build_a1_a5.fonts = lambda: (regular, bold)
    build_a6_a9.fonts = lambda: (regular, bold)
    build_a10_a13._fonts = lambda: (regular, bold)


def _verify_expected_outputs(root: Path):
    output_dir = root / 'arbeitsblaetter'
    missing = sorted(name for name in EXPECTED_OUTPUTS if not (output_dir / name).is_file())
    if missing:
        raise RuntimeError('Build is incomplete; missing expected outputs: ' + ', '.join(missing))


def _build_into(root: Path):
    build_a1_a5.build_all(root)
    build_a6_a9.build_all(root)
    build_a10_a13.build_all(root)
    build_a13.build_all(root)
    build_uebungstest.build_all(root)
    build_steckbrief.build_all(root)
    build_word_test.build_all(root)
    write_readme(root)
    _verify_expected_outputs(root)


def main():
    install_deterministic_docx_save()
    _configure_portable_preview_fonts()
    with staged_course_root(ROOT) as stage_root:
        _build_into(stage_root)
    print('Generated complete Word course package in', ROOT / 'arbeitsblaetter')


if __name__ == '__main__':
    main()
