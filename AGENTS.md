# AGENTS.md – Arbeitsweise für den Word-Kurs

Diese Datei beschreibt, wie neue Arbeitsblätter, Tests und bestehende DOCX-Dateien in diesem Repository erstellt bzw. geändert werden sollen.

## 1. Source of Truth

Die DOCX-Dateien unter `arbeitsblaetter/` sind **generierte Ergebnisse**. Die eigentliche Quelle liegt in `src/`.

Darum gilt:

- Änderungen nicht nur direkt in einer generierten DOCX vornehmen.
- Änderungen am passenden Python-Builder umsetzen.
- **Jedes Arbeitsblatt A1–A13 hat genau einen eigenen Builder** unter `src/worksheets/`.
- Ein einzelnes Blatt darf gezielt neu generiert werden; vor einem Release bzw. nach Änderungen an gemeinsamen Helfern den vollständigen Kurs neu bauen.
- Wiederverwendbare Layout-Funktionen gehören nach `src/course_common.py` bzw. `src/course_build_helpers.py`.
- `src/generate_course.py` ist der gemeinsame Einstiegspunkt.

Arbeitsblatt-Builder:

- `src/worksheets/a01.py`
- `src/worksheets/a02.py`
- `src/worksheets/a03.py`
- `src/worksheets/a04.py`
- `src/worksheets/a05.py`
- `src/worksheets/a06.py`
- `src/worksheets/a07.py`
- `src/worksheets/a08.py`
- `src/worksheets/a09.py`
- `src/worksheets/a10.py`
- `src/worksheets/a11.py`
- `src/worksheets/a12.py`
- `src/worksheets/a13.py`

Weitere Builder und Build-Helfer:

- `src/build_uebungstest.py`
- `src/build_steckbrief.py`
- `src/build_word_test.py`
- `src/course_common.py` – gemeinsames visuelles System und DOCX-Bausteine
- `src/course_build_helpers.py` – Word-spezifische Helfer für Abschnitte, Zellen, XML und Seitenzahlen
- `src/build_runtime.py` – portable Preview-Fonts, deterministische DOCX-Saves und transaktionales Publishing
- `src/worksheet_runtime.py` – direkter Einzelbuild eines Arbeitsblatts
- `src/grading.py` – lineare Schweizer Notenskala mit kaufmännischer Rundung
- `src/validate_build.py` – strukturelle Prüfung der generierten DOCX/PNG und Punktsummen
- `src/generate_course.py` – kompletter oder selektiver Build

Arbeitsblatt-spezifischer Inhalt und Arbeitsblatt-spezifische Assets gehören in den jeweiligen `aXX.py`-Builder. Gemeinsame Mechanik nicht zwischen den 13 Dateien kopieren, sondern in die gemeinsamen Helfer verschieben.

## 2. Kursziel und Didaktik

Zielgruppe ist eine 8. Sekundarklasse. Die Arbeitsblätter sollen nicht wie ein Word-Handbuch wirken.

Bevorzugt werden:

- wenig Erklärungstext
- ein klarer Arbeitsauftrag
- ein sichtbares Resultat
- kurze, konkrete Formulierungen
- direkte Arbeit in Word
- Wiederholung bekannter Funktionen
- zunehmend weniger Hilfestellung

Zentrale Regel:

> Schwieriger bedeutet nicht automatisch, mehr Information zu verstecken.

Nur Informationen verstecken oder selbst ableiten lassen, wenn diese Ableitung Teil des Lernziels ist. Keine zusätzliche Denkaufgabe einbauen, die mit der eigentlichen Word-Kompetenz nichts zu tun hat.

Bei jedem Blatt prüfen:

- Was ist die neue bzw. zentrale Kompetenz?
- Was müssen die Schülerinnen und Schüler schon können?
- Welche Informationen müssen sichtbar bleiben?
- Entsteht unbeabsichtigte Zusatzbelastung?
- Wird aus Versehen mehr als eine neue Kompetenz gleichzeitig geprüft?
- Ist die Progression geführt → teilweise geführt → selbstständig nachvollziehbar?

Siehe zusätzlich `planung/DIDAKTIK.md` und `planung/KURSUEBERSICHT.md`.

## 3. Sprache

Die Klasse ist eher schwach. Darum:

- keine unnötigen Fachbegriffe
- lieber `Farbe`, `Blau`, `dunkelblau` als `Akzentfarbe`
- Arbeitsschritte eindeutig formulieren
- bei frühen Blättern konkrete Textstellen nennen
- keine widersprüchlich wirkenden Vorgaben
- neue Funktionen einzeln einführen und später kombinieren

## 4. Visuelles System

Alle Arbeitsblätter sollen wie Teile desselben Kurses aussehen.

Konstanten:

- Schrift: **Arial**
- Navy: `#17324D`
- Teal: `#237B78`
- dunkles Teal: `#1D6765`
- helles Grau: `#F3F6F7`
- helles Teal: `#EAF4F3`
- warmer Tipp-Hintergrund: `#F8F3EA`
- Sekundärtext: `#667684`
- Linien: `#D3DEE2`

Hauptraster:

- linke Labelspalte: ca. `3.2244 cm`
- rechte Inhaltsspalte: ca. `14.1164 cm`
- Gesamtbreite: ca. `17.34 cm`

Typischer Aufbau:

1. Kurs-Header
2. Codezeile
3. grosser Titel
4. kurze Unterzeile
5. Lernziel
6. Aufgabe
7. Tipp / Merke / Check nur wenn nötig
8. Abschlusszeile
9. Footer

Grundsätzliche Abschlusszeile:

`FERTIG? Gib dieses Arbeitsblatt in deinem Ordner "IB" ab.`

Bei zusätzlichen Bilddateien darf sie entsprechend erweitert werden.

Keine Name-/Klasse-/Datum-Zeile hinzufügen, ausser sie wird für eine konkrete spätere Aufgabe benötigt.

## 5. Seiten und Arbeitsbereiche

Eine Seite bevorzugen, wenn die Aufgabe sinnvoll darauf Platz hat.

Mehrere Seiten verwenden, wenn dadurch echtes Arbeiten in Word sauberer möglich wird, z. B.:

- Anleitung + separate Übungsseite für Seitenlayout
- Anleitung + freie Seite für eine echte Tabelle
- Anleitung + zweitseitiger Arbeitsbereich für Kopf-/Fusszeilen
- Aufgabenblatt + separate Ausgangsdatei bei testähnlichen Aufgaben

Arbeitsbereiche dürfen in einen eigenen Abschnitt gelegt werden, wenn Schülerinnen und Schüler dort Kopf-/Fusszeilen oder Seiteneinstellungen verändern sollen, ohne das Aufgabenblatt zu zerstören.

## 6. Vorgehen für neue oder geänderte Arbeitsblätter

### Lernziel festlegen

Zuerst in einem Satz bestimmen, welche Kompetenz gelernt oder überprüft wird.

Alles andere sollte bereits bekannt sein oder sichtbar erklärt werden.

### Aufgabe als Produkt denken

Nicht nur eine Funktion isoliert anklicken lassen, sondern ein kleines sinnvolles Produkt bauen lassen, etwa Flyer, Infoblatt, Reisebericht, Tabelle oder Veranstaltungsankündigung.

### Passenden Builder bearbeiten

Für A1–A13 ausschliesslich den entsprechenden Builder `src/worksheets/aXX.py` bearbeiten. Gemeinsame Dinge aus `course_common.py` bzw. `course_build_helpers.py` verwenden:

- Farben
- Schrift
- Header/Footer
- Tabellenraster
- Labelzellen
- Absatzformatierung
- Seitenaufbau
- Arbeitsabschnitte und Seitenzahlen

Ein neues Arbeitsblatt erhält einen eigenen Builder und wird in `WORKSHEETS` in `src/generate_course.py` eingetragen.

### Assets

Aufgabenbilder nach `arbeitsblaetter/assets/`, visuelle Zielvorlagen nach `arbeitsblaetter/assets/vorlagen/`.

Dateinamen:

- klein
- eindeutig
- möglichst mit Blattnummer oder Zweck beginnen
- keine temporären Dateien
- wenn möglich reproduzierbar im jeweiligen Builder erzeugen

## 7. Generieren

Vom Repository-Root:

```bash
pip install -r requirements.txt
```

Komplettes Paket:

```bash
python src/generate_course.py
python src/validate_build.py
```

Einzelnes Arbeitsblatt oder mehrere Arbeitsblätter:

```bash
python src/generate_course.py A7
python src/generate_course.py A7 A8
```

Ein Arbeitsblatt kann auch direkt über seinen Builder erzeugt werden:

```bash
python src/worksheets/a07.py
```

Der vollständige Build baut zunächst in einem Staging-Verzeichnis und veröffentlicht erst nach erfolgreicher Validierung. Selektive Builds ändern nur die Ausgaben der gewählten Arbeitsblätter und validieren danach das bestehende Gesamtpaket.

## 8. Pflicht-QA

Eine DOCX ist **nicht fertig**, nur weil sie erzeugt werden kann.

Nach jeder Erstellung oder Layoutänderung:

1. DOCX mit dem kanonischen Renderer rendern.
2. **Jede Seite** als PNG bei 100 % visuell kontrollieren.
3. Prüfen:
   - abgeschnittener Text
   - Überlappungen
   - falsche Seitenumbrüche
   - schiefe Raster/Spalten
   - zu kleine Schrift
   - unerwartete Leerzeilen
   - Header/Footer
   - Bilder nicht verzerrt
   - Tabellen innerhalb der Seite
4. Fehler im Layout bzw. Generator beheben und erneut rendern.

Für die lokale ChatGPT-Arbeitsumgebung ist der Renderer:

```bash
python /home/oai/skills/docx/render_docx.py DATEI.docx --output_dir QA_ORDNER
```

Keine QA-PNGs, PDFs oder temporären Hilfsdateien ins Repository committen.

`src/validate_build.py` ergänzt diese visuelle QA durch automatische Strukturprüfungen: erwartete Dateien, gültige DOCX-ZIPs, lesbare PNGs sowie die definierten 20-/30-Punkte-Schemata.

## 9. Word-spezifische Regeln

### Absätze

Abstände über Absatzformatierung erzeugen, nicht über viele leere Enter-Zeilen.

### Listen

Wenn Aufzählung oder Nummerierung Lernziel/Prüfkriterium ist, echte Word-Listen verwenden bzw. verlangen.

### Seitenumbruch

Für neue Seiten echte Seitenumbrüche (`Ctrl + Enter`) verwenden, nicht viele Enter-Zeichen.

### Formatvorlagen

Wenn Formatvorlagen Lernziel sind, nicht gleichzeitig dieselben Überschriften manuell über Schriftgrösse/Fett nachbauen lassen.

### Bilder

Proportional skalieren. Zuschneiden und Textumbruch nur verlangen, wenn bekannt bzw. Lernziel.

### Tabellen

Wenn Tabellen geübt werden, genügend freie Dokumentfläche bereitstellen. Keine Schülertabelle in eine Layout-Tabelle des Aufgabenblatts zwängen. Freie Fläche nicht durch Ketten leerer Absätze erzeugen.

### Kopf-/Fusszeilen

Bei Arbeitsblättern mit eigenem Kurs-Header für Schüleraufgaben einen separaten Abschnitt oder eine separate Ausgangsdatei verwenden.

### Tabulatoren

Tabulatoren, Lineal und komplexe hängende Einzüge gehören aktuell **nicht zum Pflichtkurs**, weil sie auf den Schulgeräten unzuverlässig waren. Nur wieder aufnehmen, wenn sie vorher lokal auf den tatsächlichen Schulgeräten getestet wurden.

## 10. Progression

Die aktuelle Schlussprogression ist bewusst:

- A10: neue Funktion Kopf-/Fusszeile
- A11: bekannte Werkzeuge anhand einer sichtbaren Vorlage kombinieren
- A12: selbst gestalten, keine Zielvorlage
- A13: Gesamtauftrag, keine neue Word-Funktion
- Übungstest: separate Ausgangsdatei, testähnliche Bedingungen, keine Klickanleitung

Der Übungstest ist unbenotet. Seine Punkte dienen nur zur Orientierung.

## 11. Git- und Build-Workflow

GitHub Actions reagiert auf Änderungen unter `src/**` und führt aus:

```bash
python src/generate_course.py
python src/validate_build.py
```

Danach werden Änderungen unter `arbeitsblaetter/` automatisch zurück ins Repository committed.

Bevorzugter Ablauf bei Änderung eines Arbeitsblatts:

1. Nur den passenden `src/worksheets/aXX.py`-Builder ändern.
2. Das betroffene Blatt selektiv generieren.
3. Automatische Validierung ausführen.
4. Die geänderte DOCX vollständig rendern und visuell prüfen.
5. Quellcode und nötige Planungsdokumente committen.
6. GitHub-Actions-Vollbuild abwarten.
7. Prüfen, ob Build und Validierung erfolgreich waren.
8. Sicherstellen, dass die generierten Dateien im Repository vorhanden sind.

Bei Änderungen an gemeinsamen Helfern oder vor einem Release lokal immer den vollständigen Kurs bauen und alle betroffenen DOCX-Dateien visuell prüfen.

Bei erweitertem Kursumfang ebenfalls prüfen:

- `src/generate_course.py`
- `src/validate_build.py`
- `arbeitsblaetter/README.md`
- Root-`README.md`
- `planung/KURSUEBERSICHT.md`
- `.github/workflows/build-word-course.yml`

## 12. Nicht machen

- nur eine generierte DOCX ändern und den Generator veraltet lassen
- Inhalte mehrerer Arbeitsblätter wieder in einen Sammel-Builder zusammenziehen
- bei jedem Blatt ein neues Design erfinden
- unnötig neue Schriftarten einführen
- Erklärungstext hinzufügen, nur um eine Seite zu füllen
- mehrere unbekannte Word-Funktionen versteckt gleichzeitig prüfen
- Layout mit Leerzeichen oder vielen Enters bauen
- visuelle Fehler ignorieren, weil Python ohne Fehler durchläuft
- QA-, Migrations- oder temporäre Hilfsdateien committen

## 13. Entscheidungskriterium

Wenn unklar ist, ob etwas auf ein Blatt gehört:

**Hilft es den Schülerinnen und Schülern, genau die gewünschte Word-Kompetenz zu lernen bzw. zu zeigen – oder macht es die Aufgabe nur zusätzlich kompliziert?**

Nur Ersteres gehört in den Pflichtteil.
