from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

import build_steckbrief
import build_uebungstest
import build_word_test
from build_runtime import install_deterministic_docx_save, staged_course_root
from validate_build import validate_course_package
from worksheets import a01, a02, a03, a04, a05, a06, a07, a08, a09, a10, a11, a12, a13

ROOT = Path(__file__).resolve().parents[1]
_FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)

WORKSHEETS = {
    'A1': a01, 'A2': a02, 'A3': a03, 'A4': a04, 'A5': a05,
    'A6': a06, 'A7': a07, 'A8': a08, 'A9': a09, 'A10': a10,
    'A11': a11, 'A12': a12, 'A13': a13,
}

STUDENT_PACKAGES = {
    'A7': (
        'A7_Bilder_in_Word.zip',
        ('A7_Bilder_in_Word.docx', 'assets/a7_schulhaus.png'),
    ),
    'A11': (
        'A11_Dokument_nach_Vorlage_nachbauen.zip',
        ('A11_Dokument_nach_Vorlage_nachbauen.docx', 'assets/a11_klassenlager_berge.png'),
    ),
    'A12': (
        'A12_Selbststaendig_gestalten.zip',
        ('A12_Selbststaendig_gestalten.docx', 'assets/a12_sommerabend.png'),
    ),
    'A13': (
        'A13_Gesamtauftrag_Pruefungsvorbereitung.zip',
        ('A13_Gesamtauftrag_Pruefungsvorbereitung.docx', 'assets/a13_bern_altstadt.png'),
    ),
    'UEBUNGSTEST': (
        'Uebungstest_Word_Paket.zip',
        ('Uebungstest_Word.docx', 'Uebungstest_Ausgangsdokument.docx', 'assets/uebungstest_greifensee.png'),
    ),
    'WORD_TEST': (
        'Word_Test_Paket.zip',
        ('Word_Test.docx', 'Word_Test_Ausgangsdokument.docx', 'assets/word_test_rheinfall.png'),
    ),
}


def _write_student_package(output: Path, package_name: str, members: tuple[str, ...]) -> None:
    packages = output / 'pakete'
    packages.mkdir(parents=True, exist_ok=True)
    destination = packages / package_name
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for member in members:
            source = output / member
            if not source.is_file():
                raise RuntimeError(f'Cannot build {package_name}; missing {source}')
            info = zipfile.ZipInfo(source.name, date_time=_FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build_student_packages(root: Path, keys: set[str] | None = None) -> None:
    output = root / 'arbeitsblaetter'
    selected = STUDENT_PACKAGES if keys is None else {key: STUDENT_PACKAGES[key] for key in keys if key in STUDENT_PACKAGES}
    for package_name, members in selected.values():
        _write_student_package(output, package_name, members)


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

## Schülerpakete mit Bilddateien

Für Aufgaben, die eine separate Bilddatei benötigen, liegen unter `pakete/` fertige ZIP-Dateien. Im ZIP liegen DOCX und benötigte PNG-Datei(en) direkt nebeneinander.

- `pakete/A7_Bilder_in_Word.zip`
- `pakete/A11_Dokument_nach_Vorlage_nachbauen.zip`
- `pakete/A12_Selbststaendig_gestalten.zip`
- `pakete/A13_Gesamtauftrag_Pruefungsvorbereitung.zip`
- `pakete/Uebungstest_Word_Paket.zip`
- `pakete/Word_Test_Paket.zip`

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
    build_student_packages(root)
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
    build_student_packages(ROOT, set(codes))
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
