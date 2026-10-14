# Schülerseite · Word-Kurs Round 3

## Ziel
Eine ruhige, mobil nutzbare `index.html` im etablierten Navy-/Teal-Stil. Schülerinnen und Schüler finden die Reihenfolge A1–A13 visuell statt über GitHub-Ordner.

## Schülersicht
- Desktop: drei Kacheln pro Zeile; Tablets: zwei; Smartphones: eine.
- Kurze Handlungsbeschreibungen und echte Vorlagenbilder, falls vorhanden. Bei A12/A13 nur Bildmaterial, **keine falsche Zielvorlage**.
- **Einzelne Word-Dateien**, **nur bei A7** zusätzlich die einzelne Bilddatei. In A11–A13 sind die Bilder direkt auf der Anleitungsseite des Word-Dokuments eingebettet und kopierbar.
- PLUS 1 / PLUS 2: je Aufgabenblatt und Startdatei als einzelne Word-Downloads.
- **Kein ZIP, kein Entpacken, keine Anmeldung, keine externen Skripte oder CDNs.**
- Lehrerdateien, Übungstest, benoteter Steckbrief und Word-Test werden auf der Startseite nicht verlinkt. Die Lehrperson verteilt Tests selbst.

## Technische Umsetzung
- `index.html` enthält reines, statisches HTML und CSS; echte Vorschaudateien aus `arbeitsblaetter/assets/vorlagen/` und `qa/3rd-round/pages/`.
- Downloadlinks sind relativ zu einem statischen Webserver, der den Repository-Root ausliefert.
- Der Validator `src/validate_student_index.py` prüft die vorhandenen Dateien und verhindert ZIP-/Prüfungslinks; CI führt den Validator nach dem Kursgenerator aus.
- Start-/Muster-Dokumente sind selbständiges Word-Übungsmaterial und erhalten deshalb keinen dekorativen Kurs-Header.
- Die Weboberfläche wurde nicht auf eine bestimmte Plattform deployed.

## Verbindliche Grenze vor Veröffentlichung
Das **Repository ist öffentlich** und enthält auch benotete Prüfungen, Musterlösungen und Lehrerdateien. Das Weglassen von Links in der `index.html` **schützt diese Dateien nicht**. Für Schüler eine getrennte veröffentlichte Website bzw. ein Schulportal mit **ausschliesslich** freigegebenen Schülerdateien verwenden; Prüfungen und Musterlösungen privat halten. Kein öffentliches Hosting des gesamten Repo-Inhalts ohne Bereinigung.

## QA
- Alle 13 Pflichtdateien und zwei optionale Zusatzaufgaben müssen einzeln erreichbar sein.
- Nur die separate A7-PNG muss abrufbar sein. A11–A13 müssen ihre Originalbilder als kopierbare Medien im DOCX enthalten, nicht nur im Vorschau-Screenshot.
- Bilder brauchen beschreibende Alternativtexte.
- Alle Links nur relativ, keine Downloads von Archiven.
- Responsives Layout (3/2/1) und Tastaturfokus; Browser-Sichtprüfung später im gewählten Hosting.
- Schule muss testen, ob die DOCX-Dateien am echten Schul-PC mit Office korrekt heruntergeladen und bearbeitet werden.

## Fix 1 – zweiter Bilddownload entfällt (14.10.2026)

- A11, A12 und A13: **ein DOCX reicht**. Das originale, vollständige PNG-Bild ist als eigenständiges, auswählbares Inline-Bild in der Word-Anleitung eingebettet, nicht bloss als Bestandteil eines Vorschaubilds. Per Strg+C / Strg+V auf die Arbeitsseite kopieren; Zuschneiden, Positionieren und Textumbruch bleiben Lernanforderungen. Keine externe Bilddatei mehr nötig.
- A7: unverändert zwei Einzeldateien, weil Bild **aus Datei einfügen** hier ausdrücklich neu eingeführt wird.
- PLUS 1 / PLUS 2: Aufgabenblatt und Startdatei weiterhin separat (beides DOCX). Keine ZIP-Downloads auf der Schülerseite.
- **CI:** [Run 38555065511](https://github.com/modebrecht/Word-Kurs/actions/runs/38555065511) PASS (Generierung, Inhalts-/Bild-Validierung, Schülerseiten-Links, LibreOffice-Rendering). Index: 17 einzelne DOCX-Links und ein A7-PNG-Link, insgesamt 18 Downloads.
- **Visuelle Prüfung:** A11, A12, A13 je zwei Seiten, **6/6 Seiten** kontrolliert. Kein Überlauf, kein fehlendes Bild, keine ungewollte Zusatzseite. Quellbilder sind auch als Medienobjekt im DOCX nachgewiesen.
- **Extern weiterhin UNVERIFIED:** Word 365 auf Schul-PCs; echtes Kopieren/Bildbearbeiten und Schülerzeit. Keine Veröffentlichung.

## Fix 2 — konsistente, ehrliche Miniaturansichten (14.10.2026)

- Alle **15 Kacheln** erhalten exakt denselben Vorschau-Rahmen und eine der drei erklärenden Unterschriften: **SO SOLL ES AUSSEHEN** (konkrete Vorlage), **DAS ÜBST DU** (Werkzeug oder schematische Tätigkeit), **DEIN BILDMATERIAL** (offene Gestaltung ohne Zielvorlage).
- Für A1/A4/A6 werden die vorhandenen tatsächlichen Word-Werkzeugbilder benutzt statt ganzer Dokumentseiten oder erfundener Beispieldokumente. Die Quellen sind die bereits im Kurs vorhandenen PNGs.
- A12/A13 zeigen ausschliesslich Bildmaterial; ausdrücklich **keine Zielvorlage**.
- Die PLUS-Aufgaben zeigen künftig neutrale schematische Ansichten statt der bisher als JPG referenzierten **Lehrpersonen-Musterlösungen**. Dadurch wird der Sachfakt der Quellenrecherche nicht in der Schülerkarte verraten.
- Die Downloadlinks und der Kursstoff bleiben unverändert; kein ZIP. Auch hier gilt: keine öffentliche Auslieferung der vertraulichen Lehrpersonen- und Prüfungsdateien.
- Neuer automatischer QA-Gate in `src/validate_student_index.py`: Vorschau-Typ und Beschriftung aller 15 Kacheln, vorhandene Bilder, keine Lehrpersonenlösung.

## Fix 1 – echte Browser-QA (14.10.2026)

- Playwright / Chromium ruft die echte Schüler-HTML-Seite über einen lokalen HTTP-Server auf und prüft Desktop (1440 px, 3 Spalten), Tablet (820 px, 2 Spalten), Smartphone (390 px, 1 Spalte) und kleines Smartphone (320 px, 1 Spalte).
- Für alle vier Grössen werden 15 Kacheln, 13 geladene Miniaturbilder, 18 sichtbare Downloadlinks, horizontale Überläufe, abgeschnittene Knöpfe, die vier Abschnittsnavigationen und Konsolen-/Netzwerkfehler getestet.
- Unter Desktop werden alle 18 Downloadlinks wirklich angeklickt; Dateinamen und SHA256-Prüfsummen der empfangenen Dateien müssen mit den Originalen übereinstimmen. Mobiler A7-Bilddownload wird zusätzlich geprüft.
- CI schreibt vier echte Screenshots und eine JSON-Auswertung nach `qa/browser/`; **automatische Tests ersetzen die spätere Sichtprüfung nicht**.
- Unverändert: kein Deployment und keine Veröffentlichung des Repository-Inhalts. Native Word 365, Schul-PC-Tests und Schutz der im Repository vorhandenen Prüfungsdateien sind separate Gates.

**Browser-Testpräzisierung:** Ein erster CI-Lauf löste zehn Downloads hintereinander in derselben Chromium-Sitzung aus. Chromium blockierte dann weitere automatische Downloads (Browser-Schutzmechanismus). Die reale Schülernutzung ist ein einzelner Download je Aufgabe. Der vollständige QA-Gate prüft darum jeden der 18 Downloads in einer separaten Inkognito-Browsersitzung: tatsächlicher Klick, Download-Ereignis, Dateiname und SHA256-Dateiintegrität. Der Browserschutz bleibt aktiv und wird nicht abgeschaltet.
