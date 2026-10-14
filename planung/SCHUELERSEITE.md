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
