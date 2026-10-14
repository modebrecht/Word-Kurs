# 3rd-round-qa — gezielte Integration nach Vergleich

Basis: 2nd-rnd-qa, SHA 5eb899f44567a143743dbca5ea768889dc325202.
Branch: 3rd-round-qa. Kein Merge und keine Veraenderung von main oder 2nd-rnd-qa.

## Fixierte Grenzen
- A1–A13 bleiben die 13 Pflichtarbeitsblaetter in derselben Reihenfolge.
- Fleissnote, Steckbrief, Uebungstest und Word-Test behalten ihre Bewertung.
- Keine neue Pflichtfunktion in A13 oder in benoteten Pruefungen.
- Zwei neue Aufgaben sind **freiwillige Zusatzauftraege** und werden nicht fuer die Fleissnote zaehlt.
- Die Rohtexte sind vollstaendig vorhanden und werden nicht ohne Lernziel neu geschrieben.

## Paket 1: Bestehende Blätter
- A1: kurze Speicher-/Wiederfindroutine; nur ein neuer Mini-Ablauf, demonstrierbar.
- A7: freiwilliger Alternativtext mit Beispiel, nach der Bildlayout-Hauptaufgabe.
- A12/A13: unveraendert, um die bestehende Transferfolge nicht aufzuweichen. PDF-Export wird im separaten, einseitigen Brief geuebt.

## Paket 2: Schnupperlehr-Brief
- ZUSATZ_Schnupperlehrbrief.docx: 45 Minuten, ein formeller Brief.
- START_Schnupperlehrbrief.docx: vollstaendiger fiktiver Rohtext, keine eigenen Personendaten noetig.
- MUSTER_Schnupperlehrbrief.docx: eine echte Musterseite.
- DOCX plus einseitiger PDF-Export der fertigen *Briefdatei*, nicht der Aufgabenanleitung.

## Paket 3: Links und Quellen
- ZUSATZ_Links_und_Quellen.docx: 20–25 Minuten.
- START_Links_und_Quellen.docx mit vorhandenem Zieltext.
- MUSTER_Links_und_Quellen.docx mit zwei echten externen Hyperlinks.
- Webadressen: www.berufsberatung.ch und www.sbb.ch. Quellenzeile: Anbieter, Thema, URL, Datum.

## Paket 4: Lehrpersonenmaterial
- lehrperson/LEHRPERSONENHILFEN_V3.docx, zwei Musterdokumente.
- Zusaetzliche Beobachtungskriterien; bestehende Pruefungen und Noten unveraendert.

## QA-Gates
1. Originale Hauptfolge und Bewertungen gegen Basis vergleichen.
2. Vollstaendiger Generator mit 7 neuen DOCX, 2 ZIP-Paketen.
3. DOCX-ZIP-CRC, XML-Parsing, Dokumentlesen, Quellen und Hyperlinks pruefen.
4. DOCX-Seiten rendern und **jede** Seite visuell kontrollieren.
5. Alle Word-Bedienhandlungen gegen Microsoft 365 Windows verifizieren.
6. Didaktischer Zweitdurchgang, besonders kognitive Last und nur optionale Zusatzskills.
7. Schul-PC-Praxistest als externer offener Gate.

Die Renderer-Ausgabe wird unter `qa/3rd-round/pages` als Sichtprüf-Evidenz abgelegt. Render-Erfolg ist ausdrücklich noch kein visueller PASS.

Bis Gates 1–6 mit wirklicher Evidenz belegt sind, bleibt der Branch Status IN PROGRESS / UNVERIFIED.

## Nachbesserung nach unabhängigem Didaktik-Audit (14.10.2026)

Auf demselben Branch werden die sieben festgestellten Schwachstellen geschlossen: (1) A1 Speichern früh und kontrolliert, (2) A7 informatives vs. dekoratives Bild, (3) Briefschema, (4) Brief nach Bearbeitung speichern und PDF erneut mit DOCX vergleichen, (5) Word-Link öffnen (Strg+Klick), (6) belegbarer Fakt statt blosser Quellenabschrift mit variablem Zugriffsdatum, (7) präzisere Lehrpersonenhilfen mit Sek-B-Differenzierung. Automatische Inhalts-/Relationstests ergänzen die bestehende visuelle QA. Keine Änderungen am Notenmodell oder A2–A6/A8–A13.

QA-Bericht wird erst nach einem tatsächlichen erfolgreichen Build und Sichtprüfung aktualisiert. Schul-PC-Word-365 und echte Schülerzeit bleiben UNVERIFIED.
