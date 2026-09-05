# Word-Kurs – Sekundarstufe 8b

Neu konzipierter Word-Kurs für eine 8. Klasse in der Schweiz.

Der bestehende ältere Kurs wird **nicht einfach gekürzt oder modernisiert**, sondern didaktisch neu aufgebaut: kurze Aufträge, wenig Erklärungstext, direktes Arbeiten in Word und zunehmend selbstständige Anwendung.

## Aktueller Stand

Das vollständige Paket ist erstellt:

- Arbeitsblätter **A1–A13** ✅
- vollständiger **unbenoteter Word-Übungstest** ✅
- benoteter **persönlicher Steckbrief mit Foto** inkl. Bewertungsraster ✅
- benoteter **Word-Test** inkl. Ausgangsdokument, Bilddatei und Korrekturblatt ✅

Die fertigen Dateien liegen unter [arbeitsblaetter/](arbeitsblaetter/README.md). Benötigte Bilddateien und visuelle Vorlagen liegen in `arbeitsblaetter/assets/`.

## Bewertungsmodell

Es entstehen drei Noten:

1. **Fleissnote** aus A1–A13
2. **persönlicher Steckbrief** – 20 Punkte
3. **Word-Test** – 30 Punkte

Für Steckbrief und Word-Test gilt die lineare Skala:

`Note = 1 + 5 × (Punkte / Maximalpunkte)`

Die Note wird kaufmännisch auf eine Dezimalstelle gerundet; **60 % entsprechen Note 4.0**. Bei den drei Noten ist eine Streichnote vorgesehen.

## Planungsdokumente

- [Kursübersicht](planung/KURSUEBERSICHT.md)
- [Didaktische Leitlinien](planung/DIDAKTIK.md)
- [Bewertung](planung/BEWERTUNG.md)
- [Persönlicher Steckbrief](planung/STECKBRIEF.md)
- [Offene Punkte / Tests](planung/OFFENE_PUNKTE.md)

## Arbeitsblätter weiterentwickeln

Die DOCX-Dateien werden reproduzierbar aus `src/` erzeugt. **Jedes Arbeitsblatt hat einen eigenen Builder** unter `src/worksheets/` (`a01.py` bis `a13.py`). Dadurch kann ein einzelnes Blatt geändert und neu erzeugt werden, ohne A1–A13 komplett neu zu bauen.

Kompletter Kurs:

```bash
python src/generate_course.py
```

Nur einzelne Arbeitsblätter:

```bash
python src/generate_course.py A7
python src/generate_course.py A7 A8
```

Ein einzelner Builder kann auch direkt gestartet werden:

```bash
python src/worksheets/a07.py
```

Die vollständige Arbeitsanweisung für neue Arbeitsblätter, Layoutregeln, didaktische Leitplanken, Assets, Rendering/QA und den GitHub-Actions-Workflow steht in [AGENTS.md](AGENTS.md).

Wichtig: Generierte DOCX-Dateien nicht isoliert von Hand pflegen. Änderungen sollen im Generator nachvollziehbar bleiben und jede fertige DOCX muss nach dem Erzeugen seitenweise visuell geprüft werden.

## Grundidee

Die Schülerinnen und Schüler sollen Word **durch Benutzung lernen**, nicht durch lange Erklärungen zur Benutzeroberfläche.

Die Progression endet bewusst mit:

- **A11:** komplexere Vorlage nachbauen
- **A12:** selbst gestalten ohne Zielvorlage
- **A13:** zweiseitiger Gesamtauftrag ohne neue Word-Funktion
- **Übungstest:** vollständige testähnliche Situation ohne Note
- **Steckbrief:** persönliche, aber objektiv messbare Anwendungsnote
- **Word-Test:** gleicher Arbeitsmodus wie im Übungstest, aber mit neuem Inhalt
