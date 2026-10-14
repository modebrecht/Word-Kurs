# 3rd-round-qa — Abschluss nach unabhängigem Didaktik-Audit

**Datum:** 14.10.2026
**Repository/Branch:** modebrecht/Word-Kurs · `3rd-round-qa`
**Basis:** `2nd-rnd-qa` — `5eb899f44567a143743dbca5ea768889dc325202`

## Entscheid

**INTERNE TECHNISCHE UND DIDAKTISCHE NACHPRÜFUNG: PASS für die sieben vereinbarten Fixes.**

**GESAMT-RELEASE: NOT YET ACCEPTED.** Ein nativer Test in Microsoft Word 365 auf den realen Schulgeräten und ein Schülerdurchlauf mit Zeitmessung sind weiterhin **UNVERIFIED**. Kein Merge nach `main`.

## Alle sieben Befunde: korrigiert

| Auditbefund | Nachbesserung | Beleg |
| --- | --- | --- |
| A1 · Dateisicherheit zu spät | *Vor* der Formatierung im Ordner IB speichern; danach Strg+S, schliessen, wieder öffnen; Kompetenz ins Lernziel und CHECK aufgenommen. | `src/worksheets/a01.py`, A1-DOCX, 1 Seite |
| A7 · Alternativtext ohne Unterscheidung | Freiwilliger Auftrag unterscheidet dekorativ (markieren) und informativ (Informationsgehalt beschreiben). Hauptaufgabe unverändert. | `src/worksheets/a07.py`, A7-DOCX, 1 Seite |
| Brief · fehlende visuelle Orientierung | Räumliches, zweispaltiges Briefschema mit Absender, Empfänger, Datum, Betreff, Anrede und Text. | `src/build_ergaenzungen.py`, PLUS-1-Aufgabenblatt, 1 Seite |
| Brief · DOCX/PDF-Mismatch-Risiko | Nach Bearbeitung ausdrücklich Strg+S, aus *Briefdatei* PDF exportieren, beide Dateien erneut öffnen und Text/Seite/Layout vergleichen. | PLUS-1-Aufgabenblatt, CHECK |
| Links · Bedienweg fehlt | Verlinken mit Strg+K, Öffnen in Word gewöhnlich mit Strg+Klick. | PLUS-2-Aufgabenblatt |
| Quellen · Abschrift statt Nachweis; fixes Datum | Schülerinnen und Schüler ermitteln auf der offiziellen «Lehre EFZ»-Seite unter «Dauer» eine konkrete Tatsache (3 oder 4 Jahre) und belegen genau diese. Muster benutzt `[Datum der Bearbeitung]`, kein historisches Abgabedatum. | PLUS-2-Aufgabe, START/MUSTER, echter URL-Link |
| Lehrpersonenmaterial · zu pauschal | Konkrete Zeitstruktur, Sek-B-Hilfen, formative Kriterien, Offline-Fallback und klare Prüfungsgrenzen ergänzt. | `LEHRPERSONENHILFEN_V3.docx`, 2 Seiten |

Die fachliche EFZ-Daueraussage basiert auf https://www.berufsberatung.ch/de/bildungssystem/d/lehre-efz.

## Verifizierte QA-Gates

- **CI:** Workflow [38539756588](https://github.com/modebrecht/Word-Kurs/actions/runs/38539756588), Ergebnis **SUCCESS**, Quellen-Commit `35155a3570113570b8cbaa2e88ab45eb333f9d2b`.
- **Generator:** Vollständiger `python src/generate_course.py` bestanden.
- **Integrität:** `python src/validate_build.py` bestanden, DOCX-ZIP/XML, generierte Dokumente, acht Schülerpakete, benoteter Test/Steckbrief/Notenmodell und neue Didaktik-Regressionsbedingungen.
- **Hyperlinks:** Zwei echte externe DOCX-Hyperlink-Beziehungen mit korrekten Zielen in der Musterlösung bestätigt.
- **Rendering:** Neun betroffene DOCX-Dokumente mit LibreOffice/Poppler zu **insgesamt zehn Seiten** gerendert; alle innerhalb der vorgesehenen Seitenzahlen. Acht Dokumente haben eine Seite, das Lehrpersonenheft zwei.
- **Visuelle Nachprüfung:** Alle zehn Vorschaubilder wurden einzeln kontrolliert. Keine erkennbaren abgeschnittenen Texte, Überlappungen, unlesbaren Blöcke oder ungewollten zusätzlichen Seiten. Dies ist eine AI-Sichtprüfung, kein Word-365-Test.
- **Regression:** A2–A6, A8–A13 sowie die bestehenden Prüfungsdateien wurden in dieser Runde inhaltlich nicht geändert; bestehende Punkte und Streichnote bleiben unverändert.
- **Branch-Schutz:** `main` und `2nd-rnd-qa` unverändert; kein Merge, kein Deployment.

Maschinelles Render-Manifest: `qa/3rd-round/manifest.json`. Das Manifest setzt bewusst nur `RENDERED_NOT_VISUALLY_APPROVED`: Der automatische Renderer selbst kann keine Sichtabnahme behaupten. Die nachträgliche menschlich lesbare AI-Sichtprüfung ist **hier** getrennt protokolliert.

Der automatisch generierte Ergebnis-HEAD vor diesem reinen Berichtscommit ist `ffb205b6890ecaf8bcbfeb532ff784729c1d1f1a`. Die CI lief auf dem letzten Quellenstand; ein separater CI-Lauf auf dem generierten HEAD wurde nicht durchgeführt.

## Weiterhin offen (externe Gates)

1. **Microsoft Word 365 auf tatsächlichen Schul-PCs:** Dateispeicherung, Layout und Seitenzahlen, Alternativtext-/dekorativ-Steuerung, echte Links samt Strg+Klick, Brief-DOCX/PDF identisch.
2. **Schüler-Praxistest:** Mindestens ein geführter Durchlauf mit Sek-B-Niveau; reale Bearbeitungszeiten von PLUS 1/PLUS 2, Verständnis des Schemas, Dateiabgabe, benötigte Hilfen dokumentieren.

Diese externen Gates können nicht durch GitHub Actions oder LibreOffice ersetzt werden. Erst nach deren Abnahme ist der Kurs für den ersten produktiven Einsatz vollständig freizugeben.

**Status: internes QA-Paket abgeschlossen, externe Unterrichtsfreigabe offen.**
