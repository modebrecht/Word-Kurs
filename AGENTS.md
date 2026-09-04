# AGENTS.md – Arbeitsweise für den Word-Kurs

Diese Datei beschreibt, wie neue Arbeitsblätter, Tests und bestehende DOCX-Dateien in diesem Repository erstellt bzw. geändert werden sollen.

## 1. Source of Truth

Die DOCX-Dateien unter `arbeitsblaetter/` sind **generierte Ergebnisse**. Die eigentliche Quelle liegt in `src/`.

Darum gilt:

- Änderungen nicht nur direkt in einer generierten DOCX vornehmen.
- Änderung im passenden Python-Builder unter `src/` umsetzen.
- Danach den vollständigen Kurs neu generieren.
- Wiederverwendbare Layout-Funktionen gehören nach `src/course_common.py`.
- `src/generate_course.py` ist der gemeinsame Einstiegspunkt.

Aktuelle Builder:

- `src/build_a1_a5.py`
- `src/build_a6_a9.py`
- `src/build_a10_a13.py` – enthält aktuell A10–A12
- `src/build_a13.py`
- `src/build_uebungstest.py`
- `src/course_common.py`
- `src/generate_course.py`

Neue grössere Blöcke dürfen eigene Builder erhalten. Bestehende Builder nicht unnötig zu Monolithen ausbauen.

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

## 6. Vorgehen für neue DOCX-Dateien

### Lernziel festlegen

Zuerst in einem Satz bestimmen, welche Kompetenz gelernt oder überprüft wird.

Alles andere sollte bereits bekannt sein oder sichtbar erklärt werden.

### Aufgabe als Produkt denken

Nicht nur eine Funktion isoliert anklicken lassen, sondern ein kleines sinnvolles Produkt bauen lassen, etwa Flyer, Infoblatt, Reisebericht, Tabelle oder Veranstaltungsankündigung.

### Builder ergänzen

Neue Blattfunktion im passenden Builder anlegen. Gemeinsame Dinge aus `course_common.py` verwenden:

- Farben
- Schrift
- Header/Footer
- Tabellenraster
- Labelzellen
- Absatzformatierung
- Seitenaufbau

Danach den Builder in `src/generate_course.py` einbinden.

### Assets

Aufgabenbilder nach `arbeitsblaetter/assets/`, visuelle Zielvorlagen nach `arbeitsblaetter/assets/vorlagen/`.

Dateinamen:

- klein
- eindeutig
- möglichst mit Blattnummer oder Zweck beginnen
- keine temporären Dateien
- wenn möglich reproduzierbar im Builder erzeugen

## 7. Generieren

Vom Repository-Root:

```bash
pip install -r requirements.txt
python src/generate_course.py
```

Die fertigen Dateien landen unter `arbeitsblaetter/`.

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

Wenn Tabellen geübt werden, genügend freie Dokumentfläche bereitstellen. Keine Schülertabelle in eine Layout-Tabelle des Aufgabenblatts zwängen.

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
```

Danach werden Änderungen unter `arbeitsblaetter/` automatisch zurück ins Repository committed.

Bevorzugter Ablauf:

1. Generator/Quellcode ändern.
2. Lokal generieren.
3. DOCX-Dateien vollständig rendern und prüfen.
4. Quellcode und Planungsdokumente committen.
5. GitHub-Actions-Build abwarten.
6. Prüfen, ob der Build erfolgreich war.
7. Sicherstellen, dass generierte DOCX-Dateien und Assets im Repository vorhanden sind.

Bei erweitertem Kursumfang ebenfalls prüfen:

- `src/generate_course.py`
- `arbeitsblaetter/README.md`
- Root-`README.md`
- `planung/KURSUEBERSICHT.md`
- `.github/workflows/build-word-course.yml`

## 12. Nicht machen

- nur eine generierte DOCX ändern und den Generator veraltet lassen
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
