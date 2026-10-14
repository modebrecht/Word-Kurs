# 3rd-round-qa — Implementierungs- und QA-Abschlussbericht

Datum: 14.10.2026 · Repository: `modebrecht/Word-Kurs`
Branch: `3rd-round-qa` · Basis: `2nd-rnd-qa` (`5eb899f44567a143743dbca5ea768889dc325202`)

## Entscheidung

**INTERNE QA: PASS (definierte V3-Ergänzungen).**
**GESAMT-RELEASE: NOT YET ACCEPTED.** Der native Microsoft-Word-365-Praxistest auf den Schul-PCs und ein echter Schülerdurchlauf sind noch nicht durchgeführt. Es wurde kein Merge und kein Deployment vorgenommen.

## Leistungsumfang (fest vereinbarte vier Pakete)

| Paket | Ergebnis | Prüfung |
| --- | --- | --- |
| 1 · Unterrichtsblätter | A1: Speicher-/Wiederfindroutine; A7: freiwilliger Alternativtext | Geändert und nach Build auf je einer Seite gerendert; Hauptaufgaben bleiben erhalten |
| 2 · Schnupperlehrbrief/PDF | Zusatzblatt, Rohtextdatei, echte einseitige Musterlösung | DOCX erstellt; Seite gerendert; PDF-Bedienweg anhand Microsoft Support plausibilisiert; nativer Klicktest ausstehend |
| 3 · Links/Quellen | Zusatzblatt, Ausgangsdatei, Word-Musterlösung mit zwei echten externen Hyperlinks | Word-Relationship-Ziele `www.berufsberatung.ch` und `www.sbb.ch` strukturell validiert; Renderseite kontrolliert |
| 4 · Lehrerpaket | `lehrperson/LEHRPERSONENHILFEN_V3.docx` und zwei Musterlösungen | Alle drei gerendert und geprüft; keine Änderung an den bisherigen Prüfungsrubriken |

Die Zusätze sind freiwillig. Es gibt **kein A14**, keine neue Pflichtfunktion im Abschlussauftrag A13 und keinen geänderten Notenschlüssel.

## Evidenz

- Erfolgreicher GitHub-Actions-Workflow: **Run 38530432844** (Source-Commit `0ed8b4a4e521ba64e7f6ee6d116284aab3ad7881`).
- Vollständiger `python src/generate_course.py` inklusive bestehender Prüfungsdateien erfolgreich.
- `python src/validate_build.py` grün; DOCX-ZIP und XML geprüft, Starterpakete vollständig, zwei echte Hyperlinks in der Musterlösung über Beziehungen bestätigt.
- Neun ausgewählte DOCX-Dateien mit LibreOffice und Poppler gerendert: **9 von 9 jeweils 1 Seite**.
- Renderer-Manifest: [qa/3rd-round/manifest.json](../qa/3rd-round/manifest.json).
- Individuelle Seitenbilder: [qa/3rd-round/pages](../qa/3rd-round/pages). Alle neun Seiten wurden anschliessend manuell visuell begutachtet.
- Versionsvergleich mit `2nd-rnd-qa`: Von den Pflichtmodulen wurden nur `A1_Text_formatieren.docx` und `A7_Bilder_in_Word.docx` verändert; das A7-Schüler-ZIP wurde passend neu erzeugt. A2–A6, A8–A13, Steckbrief, Übungstest, benoteter Word-Test und Korrekturblatt bleiben identisch.
- `main` und `2nd-rnd-qa` blieben unverändert.

## Korrekturzyklen

1. Neue DOCX und Lehrpersonenmaterial in generatorbasierte Build-Kette integriert.
2. Schweizer Standarddeutsch verbessert; echte Seitendarstellung ergänzt.
3. Workflow-Fehler beim Git-Commit der Vorschaubilder korrigiert.
4. Visueller Review: doppelte PLUS-Beschriftung in A7, Titelumbruch der Lehrpersonenhilfe und unpassender Zusatztext im Link-Muster entdeckt und korrigiert.
5. Erneuter vollständiger Build und Renderlauf grün; alle neun finalen Seiten nochmals kontrolliert.

## Didaktische Zweitprüfung

- **Clarity:** kurze, ausführbare Arbeitsaufträge; vorhandene Rohtexte statt freier längerer Textproduktion.
- **Cognitive load:** A1 enthält eine geführte Speicherübung, A7 den Alternativtext nur als freiwillige Zusatzaktivität; neue komplexere Aufgaben liegen ausserhalb der A1–A13-Pflichtprogression.
- **Transfer:** Briefaufgabe fordert formellen Aufbau und DOCX→PDF; Linkaufgabe fordert echte Hyperlinks statt bloss gefärbten Texts.
- **Assessment alignment:** Zusatzfähigkeiten erscheinen nicht unangekündigt im Word-Test; vorhandene 30-Punkte- und Steckbrief-Bewertung bleibt unangetastet.
- **Result:** Die definierten Ergänzungen sind intern didaktisch akzeptiert. Kein externer Mensch oder unabhängiger Agent hat sie bestätigt.

## Endstatus

| Gate | Status |
| --- | --- |
| Branch von tatsächlichem Remote-HEAD abgeleitet | PASS |
| Vier begrenzte Pakete implementiert | PASS |
| Reproduzierbarer Generator | PASS |
| DOCX-Integrität / Starters / Muster / Relationen | PASS |
| LibreOffice-Rendering & Seitenzahlen | PASS |
| Visueller Review der neun finalen Seiten | PASS |
| Kurs-Grenzen und Noten unverändert | PASS |
| Native Word 365, Windows-Schul-PC | **UNVERIFIED** |
| Schüler-Praxistest (Zeit, Verständnis, Dateiabgabe) | **UNVERIFIED** |
| Merge nach main | NICHT AUTORISIERT / NICHT AUSGEFÜHRT |

## Offener Schul-PC-Test

1. A1: speichern, schliessen, aus persönlichem Ordner wieder öffnen.
2. A7: Hauptaufgabe und Rechtsklick-/Alternativtext-Option in lokaler Word-Version.
3. PLUS 1: eine DOCX-Briefseite erstellen, PDF speichern, beide visuell vergleichen, beide korrekt ablegen.
4. PLUS 2: zwei Texte via Strg+K zu korrekten Links machen; Links öffnen und Quellenzeile ergänzen.
5. Auf schwächerem Schülerniveau Zeit und Hilfebedarf beobachten. Bei Defekten auf diesem Branch gezielt korrigieren und erneut prüfen.

## Word-Verfahren (Primärreferenzen)

- Microsoft: https://support.microsoft.com/de-de/accessibility/word/keyboard-shortcuts-in-word (Strg+K)
- Microsoft: https://support.microsoft.com/de-de/accessibility/office-accessibility/everything-you-need-to-know-to-write-effective-alt-text
- Microsoft: https://support.microsoft.com/de-de/office/collab-files/save-or-convert-to-pdf-or-xps-in-office-desktop-apps
