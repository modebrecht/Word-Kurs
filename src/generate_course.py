from __future__ import annotations

import argparse
from pathlib import Path

import build_steckbrief
import build_uebungstest
import build_word_test
from build_runtime import install_deterministic_docx_save, staged_course_root
from validate_build import validate_course_package
from worksheets import a01, a02, a03, a04, a05, a06, a07, a08, a09, a10, a11, a12, a13

ROOT = Path(__file__).resolve().parents[1]

WORKSHEETS = {
    'A1': a01, 'A2': a02, 'A3': a03, 'A4': a04, 'A5': a05,
    'A6': a06, 'A7': a07, 'A8': a08, 'A9': a09, 'A10': a10,
    'A11': a11, 'A12': a12, 'A13': a13,
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


def _build_course_worksheets(root: Path):
    for module in WORKSHEETS.values():
        module.build(root)


def _build_complete_package(root: Path):
    _build_course_worksheets(root)
    build_uebungstest.build_all(root)
    build_steckbrief.build_all(root)
    build_word_test.build_all(root)
    write_readme(root)
    validate_course_package(root)


def _normalise_code(value: str) -> str:
    raw = value.strip().upper()
    if raw.startswith('A'):
        raw = raw[1:]
    try:
        number = int(raw)
    except ValueError as exc:
        raise ValueError(f'Unknown worksheet: {value}') from exc
    code = f'A{number}'
    if code not in WORKSHEETS:
        raise ValueError(f'Unknown worksheet: {value}')
    return code


def build_selected(values: list[str]):
    codes = list(dict.fromkeys(_normalise_code(value) for value in values))
    install_deterministic_docx_save()
    for code in codes:
        WORKSHEETS[code].build(ROOT)
    validate_course_package(ROOT)
    print('Generated', ', '.join(codes), 'in', ROOT / 'arbeitsblaetter')


def build_all():
    install_deterministic_docx_save()
    with staged_course_root(ROOT) as stage_root:
        _build_complete_package(stage_root)
    print('Generated complete Word course package in', ROOT / 'arbeitsblaetter')


def main():
    parser = argparse.ArgumentParser(
        description='Generate the complete Word course or selected worksheets.'
    )
    parser.add_argument(
        'worksheets',
        nargs='*',
        metavar='A7',
        help='Optional worksheet codes (for example A7 A8). Omit to rebuild everything.',
    )
    args = parser.parse_args()
    if args.worksheets:
        try:
            build_selected(args.worksheets)
        except ValueError as exc:
            parser.error(str(exc))
    else:
        build_all()


if __name__ == '__main__':
    main()
