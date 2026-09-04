# AGENTS.md – Arbeitsweise für den Word-Kurs

Diese Datei beschreibt, wie neue Arbeitsblätter in diesem Repository erstellt und bestehende Blätter geändert werden sollen. Sie ist die technische und didaktische Arbeitsanweisung für weitere Bearbeitung durch Menschen oder Coding-/AI-Agenten.

## 1. Grundprinzip

Die DOCX-Dateien unter `arbeitsblaetter/` sind **generierte Ergebnisse**. Die eigentliche Quelle liegt in `src/`.

Darum gilt:

- Änderungen an einem Arbeitsblatt möglichst **nicht nur direkt in der DOCX-Datei** machen.
- Die Änderung im passenden Python-Builder unter `src/` umsetzen.
- Danach die DOCX-Dateien neu generieren.
- Neue wiederverwendbare Layout-Funktionen gehören nach Möglichkeit in `src/course_common.py`.
- `src/generate_course.py` ist der gemeinsame Einstiegspunkt für den vollständigen Build.

Aktuell ist der Generator aufgeteilt in:

- `src/build_a1_a5.py`
- `src/build_a6_a9.py`
- `src/course_common.py`
- `src/generate_course.py`

Wenn A10–A13 ergänzt werden, kann ein neuer Builder wie `build_a10_a13.py` angelegt und in `generate_course.py` eingebunden werden.

## 2. Ziel des Kurses

Der Kurs ist für eine 8. Sekundarklasse konzipiert. Die Arbeitsblätter sollen nicht wie ein Word-Handbuch wirken.

Bevorzugt werden:

- wenig Erklärungstext
- ein klarer Arbeitsauftrag
- ein sichtbares Resultat
- kurze, konkrete Formulierungen
- direkte Arbeit in Word
- Wiederholung bereits bekannter Funktionen
- zunehmend weniger Hilfestellung

Die zentrale didaktische Regel lautet:

> Schwieriger bedeutet nicht automatisch, mehr Information zu verstecken.

Nur Informationen verstecken oder selbst ableiten lassen, wenn genau diese Ableitung Teil des Lernziels ist. Keine zusätzliche Denkaufgabe einbauen, die mit der eigentlichen Word-Kompetenz nichts zu tun hat.

Bei jedem Blatt prüfen:

- Was ist das eigentliche Lernziel?
- Was müssen die Schülerinnen und Schüler bereits können?
- Welche Informationen sind sichtbar und welche müssen sie selbst ableiten?
- Entsteht unbeabsichtigte Zusatzbelastung?
- Wird aus Versehen mehr als eine neue Kompetenz gleichzeitig geprüft?
- Ist die Progression geführt → teilweise geführt → selbstständig nachvollziehbar?

Siehe zusätzlich `planung/DIDAKTIK.md` und `planung/KURSUEBERSICHT.md`.

## 3. Sprache und Schwierigkeitsgrad

Die Klasse ist eher schwach. Darum:

- keine unnötigen Fachbegriffe
- lieber `Farbe`, `Blau`, `dunkelblau` als Begriffe wie `Akzentfarbe`
- Arbeitsschritte sichtbar und eindeutig formulieren
- bei frühen Blättern konkrete Textstellen nennen
- keine widersprüchlich wirkenden Anweisungen wie zuerst „alles 11 pt“ und danach ohne Reihenfolge „Titel 20 pt“
- neue Funktionen einzeln einführen und später kombinieren

Ein sichtbarer Nachbau nach Vorlage ist in frühen Blättern ausdrücklich erwünscht. Das reduziert Interpretationslast und macht das Ziel kontrollierbar.

## 4. Visuelles System

Alle Arbeitsblätter sollen wie Teile desselben Kurses aussehen.

Wichtige Konstanten:

- Schrift: **Arial** als robuste Standardschrift
- Hauptfarbe Navy: `#17324D`
- Teal: ungefähr `#237B78`
- dunkles Teal: `#1D6765`
- helles Grau: `#F3F6F7`
- helles Teal: `#EAF4F3`
- warmer Tipp-Hintergrund: `#F8F3EA`
- Grau für Sekundärtext: `#667684`
- Linien: ungefähr `#D3DEE2`

Das Hauptlayout arbeitet mit einem festen zweispaltigen Raster:

- linke Labelspalte: ca. `3.2244 cm`
- rechte Inhaltsspalte: ca. `14.1164 cm`
- Gesamtbreite: ca. `17.34 cm`

Typischer Aufbau:

1. Header `WORD KURS | SEKUNDARSTUFE I · SEK 8 | ARBEITSBLATT A#`
2. Codezeile
3. grosser Titel
4. kurze Unterzeile
5. Lernziel
6. Aufgabe(n)
7. Tipp / Merke / Check nur wenn didaktisch nötig
8. Abschlusszeile
9. Footer mit Blattnummer und Titel

Die Abschlusszeile lautet grundsätzlich:

`FERTIG? Gib dieses Arbeitsblatt in deinem Ordner "IB" ab.`

Bei Aufgaben mit zusätzlicher Bilddatei darf sie passend erweitert werden.

Keine Name-/Klasse-/Datum-Zeile hinzufügen, sofern dies nicht ausdrücklich für eine spätere Aufgabe verlangt wird.

## 5. Eine oder mehrere Seiten?

**Eine Seite bevorzugen**, wenn die Aufgabe sinnvoll darauf Platz hat.

Mehrere Seiten sind sinnvoll, wenn dadurch die Arbeit in Word sauberer wird. Beispiele:

- Seite 1 = Anleitung, Seite 2 = echte Übungsseite für Seitenlayout
- Seite 1 = Anleitung, Seite 2 = freie Fläche für eine echte Word-Tabelle
- Seite 1 = Anleitung, Seiten 2–3 = mehrseitiges Dokument für Kopf-/Fusszeilen

Nicht künstlich alles auf eine Seite quetschen. Umgekehrt keine zweite Seite nur für zusätzlichen Erklärungstext erzeugen.

## 6. Vorgehen für ein neues Arbeitsblatt

### Schritt 1 – Lernziel festlegen

Zuerst in einem Satz bestimmen, welche **neue** Word-Kompetenz gelernt werden soll.

Beispiele:

- A7: Bild einfügen, zuschneiden, Textumbruch
- A8: Tabelle erstellen und Zellen verbinden
- A9: Formatvorlagen statt manueller Überschriftenformatierung

Alles andere auf dem Blatt sollte entweder bereits bekannt sein oder sichtbar erklärt werden.

### Schritt 2 – Aufgabe als Produkt denken

Nicht „klicke auf Funktion X“, sondern ein kleines sichtbares Produkt bauen lassen:

- Einladung
- Infoblatt
- Sporttag-Plan
- Reisebericht
- Tabelle

Das Produkt soll den Einsatz der Funktion sinnvoll machen.

### Schritt 3 – Builder ergänzen

Neue Blattfunktion im passenden Builder anlegen oder einen neuen Builder für den nächsten Block erstellen.

Gemeinsame Dinge nicht duplizieren, sondern aus `course_common.py` verwenden bzw. dort ergänzen:

- Farben
- Schrift
- Header/Footer
- Tabellenraster
- Labelzellen
- Absatzformatierung
- Seitenaufbau

Danach den neuen Builder in `src/generate_course.py` aufnehmen.

### Schritt 4 – Assets sauber ablegen

Aufgabenbilder und visuelle Zielvorlagen gehören nach `arbeitsblaetter/assets/` bzw. in den passenden Unterordner.

Dateinamen:

- klein
- eindeutig
- mit Blattnummer beginnen, z. B. `a7_schulhaus.png`
- keine temporären Dateien oder kryptischen Namen committen

Wenn eine visuelle Vorlage automatisch erzeugt werden kann, diese ebenfalls reproduzierbar über den Builder erzeugen.

### Schritt 5 – Generieren

Lokal aus dem Repository-Root:

```bash
python src/generate_course.py
```

Abhängigkeiten vorher installieren:

```bash
pip install -r requirements.txt
```

Die fertigen Dateien landen unter `arbeitsblaetter/`.

## 7. Pflicht-QA für jede DOCX-Datei

Eine DOCX ist **nicht fertig**, nur weil sie sich erzeugen lässt.

Nach jeder Erstellung oder Layoutänderung:

1. DOCX rendern bzw. als PDF/PNG ausgeben.
2. **Jede Seite** visuell kontrollieren.
3. Bei 100 % prüfen:
   - abgeschnittener Text
   - überlappende Elemente
   - falsche Seitenumbrüche
   - schiefe Spaltenbreiten
   - unterschiedliche Rasterbreiten
   - zu kleine Schrift
   - unerwartete Leerzeilen
   - Header/Footer korrekt
   - Bilder nicht verzerrt
   - Tabellen nicht über den Seitenrand
4. Erst danach als fertig betrachten.

Wenn etwas schief sitzt, die Ursache im Layout/Generator korrigieren. Keine pixelweisen kosmetischen Workarounds einbauen, wenn das feste Raster die eigentliche Ursache ist.

Bei einem 2- oder 3-seitigen Blatt müssen **alle Seiten** kontrolliert werden, nicht nur die erste.

## 8. Word-spezifische Regeln

### Absatzabstand statt Enter

Keine Layouts bauen, die viele leere Enter-Zeilen benötigen. Abstand über Absatzformatierung erzeugen.

### Listen

Aufzählungen und Nummerierungen als echte Word-Listen verwenden, nicht als manuell eingetippte Zeichen, wenn die Funktion selbst das Lernziel ist.

### Seitenumbruch

Für eine neue Seite `Ctrl + Enter` bzw. einen echten Seitenumbruch verwenden, nicht viele Enter-Zeichen.

### Formatvorlagen

Wenn Formatvorlagen das Lernziel sind, nicht gleichzeitig verlangen, Schriftgrösse/Fett manuell nachzubauen. Die Formatvorlage ist dann die eigentliche Kompetenz.

### Bilder

Bilder proportional skalieren. Zuschneiden und Textumbruch nur einführen, wenn sie explizit Teil des Lernziels sind.

### Tabellen

Wenn das Erstellen einer Tabelle geübt wird, genügend freie Dokumentfläche geben. Keine echte Schülertabelle innerhalb einer Layout-Tabelle des Arbeitsblatts erzwingen.

### Tabulatoren

Tabulatoren, Lineal und komplexe hängende Einzüge gehören aktuell **nicht zum Pflichtkurs**, weil sie auf den Schulgeräten bereits unzuverlässig waren. Nur wieder aufnehmen, wenn sie vorher lokal auf den tatsächlichen Schulgeräten getestet wurden.

## 9. Repetition und neue Kompetenz trennen

Eine neue Funktion darf bekannte Funktionen wiederholen. Aber nicht gleichzeitig mehrere unbekannte Funktionen voraussetzen.

Beispiel:

- A5 wiederholt A1–A4 und führt nur das Verschieben/Verkleinern einer vorhandenen Grafik als kleine neue Handlung ein.
- A7 führt Bilder gezielt ein.
- A8 führt Tabellen gezielt ein.
- A9 führt Formatvorlagen gezielt ein.

Wenn ein Blatt zu viel enthält, lieber auf zwei Blätter splitten. A1 wurde genau aus diesem Grund in A1 und A2 getrennt.

## 10. Git- und Build-Workflow

GitHub Actions führt bei Änderungen unter `src/**` automatisch aus:

```bash
python src/generate_course.py
```

und committet geänderte generierte Arbeitsblätter unter `arbeitsblaetter/` zurück ins Repository.

Darum bei Änderungen bevorzugt:

1. Generator/Quellcode ändern.
2. Lokal generieren und QA durchführen.
3. Quellcode committen.
4. Prüfen, ob der GitHub-Actions-Build erfolgreich war.
5. Sicherstellen, dass die generierten DOCX-Dateien im Repository dem geprüften Stand entsprechen.

Wenn der Kursumfang erweitert wird, auch prüfen:

- `src/generate_course.py`
- `arbeitsblaetter/README.md`
- Root-`README.md`
- `planung/KURSUEBERSICHT.md`
- Build-Workflow und dessen Commit-Text

## 11. Nicht machen

- nicht nur eine generierte DOCX ändern und den Generator veraltet lassen
- nicht unnötig neue Schriftarten einführen
- nicht bei jedem Blatt ein neues Design erfinden
- nicht mehr Text hinzufügen, nur um ein Blatt „voll“ aussehen zu lassen
- nicht mehrere neue Word-Funktionen auf einmal versteckt prüfen
- nicht mit Leerzeichen oder vielen Enters Layout bauen
- nicht visuelle Probleme ignorieren, weil der Python-Code ohne Fehler durchläuft
- keine temporären QA-, Migrations- oder Hilfsdateien ins Repo committen

## 12. Entscheidungskriterium

Wenn unklar ist, ob etwas auf ein Blatt gehört, gilt diese Frage:

**Hilft es den Schülerinnen und Schülern, genau die gewünschte Word-Kompetenz zu lernen – oder macht es die Aufgabe nur zusätzlich kompliziert?**

Nur Ersteres gehört ins Pflichtblatt.
