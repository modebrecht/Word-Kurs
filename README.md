# Word-Kurs – Sekundarstufe 8b

Neu konzipierter Word-Kurs für eine 8. Klasse in der Schweiz.

Der bestehende ältere Kurs wird **nicht einfach gekürzt oder modernisiert**, sondern didaktisch neu aufgebaut: kurze Aufträge, wenig Erklärungstext, direktes Arbeiten in Word und zunehmend selbstständige Anwendung.

## Aktueller Stand

Die Arbeitsblätter **A1–A13** sind erstellt und liegen unter [arbeitsblaetter/](arbeitsblaetter/README.md). Ebenfalls fertig ist der **unbenotete Word-Übungstest** mit Aufgabenblatt, Ausgangsdokument und Bilddatei.

Die benötigten Bilddateien und visuellen Vorlagen liegen in `arbeitsblaetter/assets/`.

## Geplanter Umfang

- 13 Arbeitsblätter (`A1`–`A13`) ✅
- 1 vollständiger **unbenoteter Übungstest** ✅
- 1 benoteter **persönlicher Steckbrief mit Foto**
- 1 benoteter **Word-Test**
- zusätzlich eine **Fleissnote** aus `A1`–`A13`
- bei den drei Noten gilt: **eine Streichnote**

## Planungsdokumente

- [Kursübersicht](planung/KURSUEBERSICHT.md)
- [Didaktische Leitlinien](planung/DIDAKTIK.md)
- [Bewertung](planung/BEWERTUNG.md)
- [Persönlicher Steckbrief](planung/STECKBRIEF.md)
- [Offene Punkte / Tests](planung/OFFENE_PUNKTE.md)

## Arbeitsblätter weiterentwickeln

Die DOCX-Dateien werden reproduzierbar aus `src/` erzeugt. Die vollständige Arbeitsanweisung für neue Arbeitsblätter, Layoutregeln, didaktische Leitplanken, Assets, Rendering/QA und den GitHub-Actions-Workflow steht in [AGENTS.md](AGENTS.md).

Wichtig: Generierte DOCX-Dateien nicht isoliert von Hand pflegen. Änderungen sollen im Generator nachvollziehbar bleiben und jede fertige DOCX muss nach dem Erzeugen seitenweise visuell geprüft werden.

## Grundidee

Die Schülerinnen und Schüler sollen Word **durch Benutzung lernen**, nicht durch lange Erklärungen zur Benutzeroberfläche.

Jedes Arbeitsblatt soll möglichst eine klare Kompetenz, einen sichtbaren Arbeitsauftrag und ein konkretes Resultat haben. Gegen Ende des Kurses werden bekannte Funktionen kombiniert und die Hilfestellungen reduziert.

Die Progression endet bewusst mit:

- **A11:** komplexere Vorlage nachbauen
- **A12:** selbst gestalten ohne Zielvorlage
- **A13:** zweiseitiger Gesamtauftrag ohne neue Word-Funktion
- **Übungstest:** testähnliche Situation mit separater Ausgangsdatei
