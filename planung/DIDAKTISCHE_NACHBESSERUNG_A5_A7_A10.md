# Didaktische Nachbesserung A5, A7 und A10

## Status

**Implementiert und gezielt QA-geprüft auf Branch `didactic-fix-a5-a7-a10`.**

Die Änderungen wurden nach einer erneuten Analyse mit `modebrecht/M/didactic.md` umgesetzt. Dabei gilt als Leitprinzip:

> **Do not assume that “harder” means “hide more information”. Only hide information that belongs to the actual learning objective.**

Die drei betroffenen Builder wurden angepasst, der komplette Kurs wurde danach neu gebaut und mit `src/validate_build.py` erfolgreich validiert. Zusätzlich wurden die geänderten DOCX mit dem kanonischen Renderer gerendert und **jede Seite bei 100 % visuell geprüft**:

- A5: 1 Seite – geprüft
- A7: 1 Seite – geprüft
- A10: 3 Seiten – alle 3 geprüft

Keine Überlappungen, abgeschnittenen Inhalte oder sichtbaren Layoutfehler wurden festgestellt.

**Wichtig:** Damit ist nur die gezielte Nachbesserung von A5, A7 und A10 abgeschlossen. Die vollständige didaktische Enddiagnose des gesamten Kurses A1–A13 plus Übungstest, Steckbrief und Word-Test bleibt ein separates Release-Gate.

---

## Reanalyse nach `modebrecht/M/didactic.md`

Für jedes Blatt wurde getrennt geprüft:

1. Was ist das Lernziel?
2. Was kennen die Schülerinnen und Schüler bereits?
3. Welche Information ist sichtbar?
4. Welche Information ist versteckt?
5. Was müssen die Schülerinnen und Schüler tatsächlich erinnern oder ableiten?
6. Entsteht Schwierigkeit aus der gewünschten Word-Kompetenz oder aus einer unbeabsichtigten Zusatzanforderung?
7. Passt die Hilfe zur Stelle in der Progression?
8. Wird versehentlich mehr als das Lernziel getestet?
9. Ist die Darstellung über die Blätter hinweg konsistent?

Es ging ausdrücklich **nicht** um ein Redesign oder darum, die Blätter ausführlicher zu machen. Geändert wurde nur didaktisch relevante Reibung.

## Kurzurteil

| Blatt | Diagnose vor Änderung | Kernproblem | Umgesetzte Konsequenz |
|---|---|---|---|
| A5 | SHOULD FIX | Das bewusste Mini-Neuziel Bild verkleinern/verschieben war legitim, aber das Verkleinern weniger sichtbar gestützt als das Verschieben. | Bildaufgabe behalten; neue Bedienhandlung klar markieren und Menüweg sichtbar machen. |
| A7 | MUST FIX | Neue Bildfunktionen verlangten teilweise Menüwissen, das noch nicht aufgebaut war; zusätzlich entstand ein unnötiger Platzhalter-Löschschritt. | Neue Funktionen sichtbar verankern; Platzhalter entfernen; keine zusätzliche Umbruch-Theorie einführen. |
| A10 | MUST FIX | Physische DOCX-Seiten 2/3 standen gleichzeitig neben automatischen Seitenzahlen 1/2. | Nur noch von erster/zweiter Übungsseite sprechen; Abschnittstechnik unsichtbar lassen. |

---

# A5 – Rette das Chaos-Dokument

## Lernziel

Hauptziel:

- bekannte Text-, Absatz- und Listenwerkzeuge aus A1–A4 in einem fehlerhaften Dokument erkennen und gezielt einsetzen.

Bewusstes Mini-Neuziel:

- eine **bereits vorhandene** Grafik verkleinern und an die richtige Stelle verschieben.

A5 ist damit keine reine Repetition mit versehentlich eingeschobener Bildaufgabe. Die kleine Bildhandlung war im Kursplan bewusst vorgesehen.

## Problem vor der Änderung

Das Verschieben wurde sichtbar mit `Ctrl + X` / `Ctrl + V` erklärt. Für die neue Grössenänderung auf ca. 2,2 cm war dagegen weniger deutlich sichtbar, **wo** diese Breite eingestellt wird.

Dadurch konnte neben der eigentlichen neuen Handlung zusätzlich unbekanntes Menüwissen getestet werden.

## Umgesetzt

- Schritt F bleibt bestehen und ist jetzt klar als **`MINI-NEU · Grafik`** markiert.
- Die Grössenänderung wird sichtbar geführt:
  - `Grafik anklicken → Bildformat → Grösse → Breite ca. 2,2 cm`
- Die vorhandene Hilfe zum Verschieben bleibt sichtbar.
- Danach wird die Grafik über den Titel gesetzt und zentriert.
- Keine weiteren Bildfunktionen werden vorgezogen:
  - kein Bild aus Datei einfügen
  - kein Zuschneiden
  - kein Textumbruch
- Zielvorlage und Chaos-Grundidee bleiben unverändert.

## Didaktisches Ergebnis

Wer A1–A4 beherrscht, kann den Wiederholungsteil lösen. Für das eine Mini-Neuziel ist die nötige Bedieninformation sichtbar. Die Schwierigkeit liegt im Anwenden der neuen Grafikhandlung, nicht im Erraten eines Menüwegs.

---

# A7 – Bilder in Word

## Lernziel

Ein Bild aus Datei einfügen und so bearbeiten, dass es passend mit Text zusammenarbeitet:

- einfügen
- zuschneiden
- Grösse ändern
- Textumbruch `Quadrat`
- verschieben

Aus A5 ist bereits bekannt, wie eine vorhandene Grafik angeklickt, in der Grösse verändert und verschoben wird. Neu sind vor allem Einfügen, Zuschneiden und `Quadrat`.

## Probleme vor der Änderung

### Bild einfügen

`a7_schulhaus.png` sollte eingefügt werden, ohne dass für diese neue Funktion ein klarer Menüanker sichtbar war.

### Breite setzen

Die Zielbreite war sichtbar, der Menüweg zur Breite aber weniger klar als andere neue Bildfunktionen.

### Platzhalter löschen

Der Text `[BILD HIER EINFÜGEN]` musste nach dem Einfügen zusätzlich gelöscht werden. Dieser Aufräumschritt prüfte nichts aus dem eigentlichen Lernziel.

## Umgesetzt

Der Auftrag ist jetzt sichtbar in zwei Phasen gegliedert:

### 1 · BILD EINSETZEN

- Cursor hinter `UNSER SCHULHAUS`, Enter
- `Einfügen → Bilder → a7_schulhaus.png`
- `Bild anklicken → Bildformat → Zuschneiden` und weissen Rand entfernen
- `Bild anklicken → Bildformat → Grösse → Breite ca. 5,5 cm`

### 2 · BILD + TEXT

- Textumbruch `Quadrat` wählen
- sichtbarer Zweckanker: **Dann kann der Text am Bild vorbeilaufen.**
- Bild rechts neben den Text verschieben

Zusätzlich:

- Der Platzhalter wurde aus dem Arbeitsbereich entfernt.
- Es wird **keine** zusätzliche Theorie zu weiteren Textumbrucharten eingeführt.
- Die Zielvorlage bleibt sichtbar.
- Neue Bedienwege bleiben sichtbar, weil die Funktionen neu sind.

## Didaktisches Ergebnis

Die Schwierigkeit besteht jetzt darin, die Bildfunktionen korrekt anzuwenden. Die Lernenden müssen nicht zusätzlich erraten, wo eine neue Funktion in Word liegt, und keinen irrelevanten Platzhalter aufräumen.

---

# A10 – Kopf-/Fusszeile und Seitenzahlen

## Lernziel

- Kopfzeile als wiederkehrenden Bereich oben verwenden
- Fusszeile als wiederkehrenden Bereich unten verwenden
- automatische Seitenzahl einsetzen
- erkennen, dass sie auf der nächsten Seite automatisch weiterzählt

## Problem vor der Änderung

Der Auftrag sprach von den physischen **Seiten 2 und 3** des dreiseitigen DOCX. Gleichzeitig sollten diese beiden Übungsseiten unten automatisch als **Seite 1** und **Seite 2** nummeriert werden.

Damit gab es zwei Zahlenlogiken für dieselben Seiten. Zum Verständnis hätte die interne Abschnittskonstruktion des DOCX mitgedacht werden müssen – obwohl Abschnitte ausdrücklich **nicht** Lernziel von A10 sind.

## Umgesetzt

- Der Aufgabenblock heisst jetzt `ÜBUNGSSEITEN` statt `SEITEN 2–3`.
- Der Auftrag sagt:
  - `Arbeite nur im Reisebericht auf den beiden folgenden Übungsseiten.`
- Danach werden sie konsequent bezeichnet als:
  - `erste Übungsseite`
  - `zweite Übungsseite`
- Die Vorschau trägt ebenfalls die sichtbaren Labels `Übungsseite 1` und `Übungsseite 2`.
- Die interne Abschnittstechnik wird **nicht erklärt**.
- Die sechs sichtbaren Bedienhilfen bleiben erhalten, weil Kopfzeile, Fusszeile und automatische Seitenzahl neue Funktionen sind.
- Der Menüweg für die automatische Zahl bleibt sichtbar:
  - `Einfügen → Seitenzahl → Aktuelle Position`
- Der Konzeptanker beschränkt sich auf das Lernziel:
  - Kopfzeile = Bereich oben
  - Fusszeile = Bereich unten
  - beide wiederholen sich
  - Seitenzahl = automatische Zahl, nicht von Hand tippen

## Didaktisches Ergebnis

Die Lernenden müssen nur noch die drei tatsächlich neuen Konzepte verstehen und anwenden. Die interne technische Konstruktion des Arbeitsblatts erzeugt keine konkurrierende Seitenlogik mehr.

---

# Hidden but important didactic inconsistencies – Ergebnis

Die drei subtilen Probleme waren:

1. **A5:** Nicht die Grafikaufgabe selbst war falsch, sondern die asymmetrische Hilfe zwischen Verschieben und Verkleinern.
2. **A7:** Eine scheinbar vollständige Schrittfolge verlangte trotzdem noch nicht aufgebautes Menüwissen und einen sachfremden Platzhalter-Löschschritt.
3. **A10:** Physische DOCX-Seitenposition und automatische Seitennummerierung benutzten unterschiedliche Zahlen für dieselben Übungsseiten und testeten damit unbeabsichtigt Dokument-Infrastruktur.

Diese drei Punkte sind auf diesem Branch behoben.

---

# QA-Nachweis

## Technisch

- vollständiger Kursbuild erfolgreich
- `src/validate_build.py` erfolgreich
- GitHub Actions Run `33960720643`: **success**
- generierte Kursdateien auf dem Branch aktualisiert

## Visuell

Mit dem kanonischen DOCX-Renderer gerendert und vollständig bei 100 % geprüft:

- `A5_Rette_das_Chaos_Dokument.docx`: 1/1 Seite sauber
- `A7_Bilder_in_Word.docx`: 1/1 Seite sauber
- `A10_Kopf_Fusszeile_Seitenzahlen.docx`: 3/3 Seiten sauber

Geprüft wurden insbesondere:

- kein abgeschnittener Text
- keine Überlappungen
- keine kaputten Tabellen-/Blockgrenzen
- sichtbare Zielvorlagen und Anweisungen vollständig
- A10-Übungsseiten sauber getrennt

## Nicht Teil dieses Nachweises

Diese gezielte QA ersetzt **nicht** die noch offene vollständige didaktische Enddiagnose des gesamten Kurses nach `modebrecht/M/didactic.md` und **nicht** den Praxistest auf den realen Schul-PCs.
