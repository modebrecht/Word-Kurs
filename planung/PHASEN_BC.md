# Phase B & C – Werkzeugwahl und Qualitätskontrolle

Status: eigenständige ergänzende Schülerlektionen, keine Änderung an Phase A (A1–A13).

## Ziel und Umfang

- **Phase B (`phase-b.html`):** Die Schülerinnen und Schüler lernen anhand derselben fiktiven Bewerbungsangaben, wann Word, KI oder ein spezialisiertes Dossier-Werkzeug sinnvoll sein könnte. Sichtbarer Vergleich von drei **vereinfachten, ausdrücklich simulierten** Ausgaben (keine echten KI-Antworten und keine Anbindung an CV Cover Charm); anschliessend drei Entscheidungssituationen, kurzer eigener Schreibauftrag und Begründung. Ca. 45 Minuten, ohne Note.
- **Phase C (`phase-c.html`):** Die Schülerinnen und Schüler vergleichen einen absichtlich fehlerhaften, als KI-Entwurf dargestellten Text mit einer Faktenkarte, finden mindestens fünf Fehler, verbessern das Schreiben direkt im Browser, kontrollieren es selbst und übertragen es auf Wunsch nach Word. Ca. 45 Minuten, ohne Note.
- **Inklusion:** B/C sind mit einem Browser und Word auch ohne KI-Zugang oder Benutzerkonto vollständig bearbeitbar. KI-/Dossier-Tools können bei Verfügbarkeit freiwillig ausprobiert werden, sind keine Voraussetzung.
- **Datenschutz durch Gestaltung:** Nur fiktive Bewerberin, fiktives Unternehmen, keine echten Personendaten nötig. Kein Formular-Upload, keine API, keine externen Ressourcen, kein Server-Speichern. Antworten werden nur im aktuellen Browserfenster gehalten; beim Neuladen können sie verloren gehen.
- **Ergebnis/Abgabe:** Phase B: kurze Bewerbung (4–6 Sätze) und drei begründende Antworten im Word-Dokument. Phase C: korrigierter Brief sowie ein Satz zur Qualitätssicherung. Aus dem Browser per Kopieren/Einfügen nach Word; keine ZIP-Dateien.
- **Didaktische Grenze:** Werkzeugwahl ist nicht eine richtige Multiple-Choice-Antwort. Formative Rückmeldungen nennen sinnvolle Vor- und Nachteile. Phase C vergibt ausdrücklich keine automatische Note und behauptet nicht, den Inhalt zuverlässig maschinell beurteilen zu können.

## QA

`python src/validate_phase_bc.py` prüft Struktur, Ressourcenfreiheit, Verknüpfungen und Interaktionen statisch. `python src/browser_qa_phase_bc.py` prüft im Chromium die beiden Seiten bei 1365/820/390/320 px, Klicks, Auswahlsituationen, Kopieren, Checkliste, Reset und horizontale Überläufe; Screenshots/Report nach `qa/browser/`. HTML-Seiten sind als eigenständige Dateien auch lokal nutzbar. Verfügbares Office oder spätere öffentliche Bereitstellung werden damit nicht getestet.

## Abgrenzung

Phase A bleibt vollständig bestehen und unverändert. B/C ersetzen die klassischen Word-Lernziele nicht und erweitern die Bewertung nicht. Keine echte KI-Anbindung und kein Link zu einem Dienst, der ein persönliches Login voraussetzt.