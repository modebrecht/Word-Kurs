from __future__ import annotations

"""Optionale Transferaufträge V3: keine A14, keine Notenänderung."""
from pathlib import Path

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

from course_common import base_doc, block, add_text, add_step, add_tip, add_check, add_finish, finalise, NAVY


def _raw_style(doc: Document) -> None:
    section = doc.sections[0]
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(2.0)
    section.left_margin = section.right_margin = Cm(2.5)
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15


def _add_link(paragraph, title: str, target: str) -> None:
    """Create a real external Word hyperlink, not blue-looking plain text."""
    rid = paragraph.part.relate_to(target, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), rid)
    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "116C94")
    props.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    props.append(underline)
    run.append(props)
    txt = OxmlElement("w:t")
    txt.text = title
    run.append(txt)
    link.append(run)
    paragraph._p.append(link)


def _instruction_brief(out: Path) -> None:
    doc = base_doc(
        "PLUS 1", "Schnupperlehre", "Ein Brief, der ankommt",
        "Gestalte aus vorgegebenem Rohtext eine professionelle Anfrage.",
        "einen formellen Brief strukturieren, sauber speichern und nur die Briefseite als PDF exportieren.",
    )
    t = block(doc, "01", "VORBEREITEN")
    cell = t.cell(0, 1)
    add_text(cell, "Öffne START_Schnupperlehrbrief.docx. Speichere sofort eine eigene Kopie als Schnupperbrief_Nachname.docx im Ordner IB.", 9.5)
    t = block(doc, "02", "GESTALTEN")
    cell = t.cell(0, 1)
    add_text(cell, "Alle Texte sind bereits vorhanden. Du musst nichts neu erfinden. Die Firma und die Person sind fiktiv. Sende diesen Übungsbrief nicht ab.", 9.3)
    add_step(cell, "A", [("A4 Hochformat, Ränder Normal, Arial 11 pt.", True, False, NAVY)])
    add_step(cell, "B", [("Absender oben, Empfänger darunter, Datum rechts, dann Betreff.", True, False, NAVY)])
    add_step(cell, "C", [("Betreff fett; Anrede, zwei kurze Textabsätze und Grussformel gut lesbar.", True, False, NAVY)])
    add_step(cell, "D", [("Keine Abstände mit vielen Leerzeichen erzeugen. Nutze Absätze und Absatzabstände.", True, False, NAVY)])
    t = block(doc, "03", "EXPORTIEREN")
    cell = t.cell(0, 1)
    add_text(cell, "Kontrolliere in der Druckvorschau: genau 1 Briefseite. Speichere ausserdem eine PDF-Datei, zum Beispiel über Datei → Speichern unter → Dateityp PDF (alternativ Datei → Exportieren). Name: Schnupperbrief_Nachname.pdf.", 9.25)
    add_tip(doc, "DOCX = später bearbeitbar. PDF = zum Weitergeben, ohne dass sich das Layout leicht verschiebt.", "MERKE")
    add_check(doc, "Sind Absender, Empfänger, Datum, Betreff, Anrede und Grussformel vorhanden? Eine Seite? Liegen DOCX und PDF im richtigen Ordner?")
    add_finish(doc, "Gib die DOCX- und die PDF-Datei im Ordner IB ab. Den Brief nicht an ein Unternehmen senden.")
    finalise(doc, out, "Zusatz: Schnupperlehrbrief")


def _starter_brief(out: Path) -> None:
    doc = Document()
    _raw_style(doc)
    doc.core_properties.title = "Rohtext: Schnupperlehrbrief"
    lines = [
        "Sara Muster", "Beispielweg 4", "4500 Solothurn",
        "Pixelwerkstatt AG", "Berufsbildung", "Werkweg 12", "4500 Solothurn",
        "Solothurn, 14. Oktober 2026",
        "Anfrage für eine Schnupperlehre als Informatikerin EFZ",
        "Sehr geehrte Damen und Herren",
        "Ich interessiere mich für den Beruf Informatikerin EFZ. Darum möchte ich gerne einen Einblick in den Berufsalltag erhalten.",
        "Über eine Möglichkeit zum Schnuppern würde ich mich freuen. Ich bin motiviert und lerne gern Neues.",
        "Freundliche Grüsse", "Sara Muster",
    ]
    for item in lines:
        doc.add_paragraph(item)
    doc.save(out)


def _model_brief(out: Path) -> None:
    doc = Document()
    _raw_style(doc)
    doc.core_properties.title = "Musterlösung: Schnupperlehrbrief"
    for s in ["Sara Muster", "Beispielweg 4", "4500 Solothurn"]:
        p = doc.add_paragraph(s)
        p.paragraph_format.space_after = Pt(0)
    p = doc.add_paragraph("")
    p.paragraph_format.space_after = Pt(4)
    for s in ["Pixelwerkstatt AG", "Berufsbildung", "Werkweg 12", "4500 Solothurn"]:
        p = doc.add_paragraph(s)
        p.paragraph_format.space_after = Pt(0)
    p = doc.add_paragraph("Solothurn, 14. Oktober 2026")
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_before = Pt(15)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    r = p.add_run("Anfrage für eine Schnupperlehre als Informatikerin EFZ")
    r.bold = True
    doc.add_paragraph("Sehr geehrte Damen und Herren")
    doc.add_paragraph("Ich interessiere mich für den Beruf Informatikerin EFZ. Darum möchte ich gerne einen Einblick in den Berufsalltag erhalten.")
    doc.add_paragraph("Über eine Möglichkeit zum Schnuppern würde ich mich freuen. Ich bin motiviert und lerne gern Neues.")
    doc.add_paragraph("Freundliche Grüsse")
    doc.add_paragraph("Sara Muster")
    doc.save(out)


def _instruction_links(out: Path) -> None:
    doc = base_doc(
        "PLUS 2", "Links & Quellen", "Links mit Sinn",
        "Verbinde verständliche Linktexte mit richtigen Webseiten und nenne eine Quelle.",
        "einen echten Word-Hyperlink setzen und eine einfache Quellenangabe schreiben.",
    )
    t = block(doc, "01", "ZWEI LINKS")
    cell = t.cell(0, 1)
    add_text(cell, "Öffne START_Links_und_Quellen.docx und speichere eine Kopie im Ordner IB.", 9.5)
    add_step(cell, "A", [("Markiere «Berufsberatung Schweiz» und drücke Strg + K.", True, False, NAVY), ("  Adresse: https://www.berufsberatung.ch/", False, False, None)])
    add_step(cell, "B", [("Markiere «SBB Fahrplan» und drücke Strg + K.", True, False, NAVY), ("  Adresse: https://www.sbb.ch/", False, False, None)])
    t = block(doc, "02", "QUELLE")
    cell = t.cell(0, 1)
    add_text(cell, "Ergänze die vorhandene Zeile «Quelle:» mit diesen Angaben: Berufsberatung Schweiz · Informationen zu Berufen · www.berufsberatung.ch · Zugriffsdatum heute. Die Angabe nennt, wo man Informationen nachlesen kann.", 9.4)
    add_tip(doc, "Ein guter Linktext verrät das Ziel. «Berufsberatung Schweiz» ist besser als «Hier klicken». Die Quelle soll zu der Information passen.", "MERKE")
    add_check(doc, "Sind beide Wörtergruppen wirklich anklickbare Links? Öffnen sich die angegebenen Webseiten? Ist die Quellenzeile ergänzt?")
    add_finish(doc, "Speichere die bearbeitete DOCX im Ordner IB. Dieser Zusatzauftrag ist freiwillig und nicht Teil des Word-Tests.")
    finalise(doc, out, "Zusatz: Links und Quellen")


def _starter_links(out: Path) -> None:
    doc = Document()
    _raw_style(doc)
    doc.core_properties.title = "Rohtext: Links und Quellen"
    doc.add_heading("Hilfreiche Webseiten für Schule und Beruf", 1)
    doc.add_paragraph("Für Berufsinformationen: Berufsberatung Schweiz")
    doc.add_paragraph("Für Zugverbindungen: SBB Fahrplan")
    doc.add_paragraph("Quelle: ")
    doc.save(out)


def _model_links(out: Path) -> None:
    doc = Document()
    _raw_style(doc)
    doc.core_properties.title = "Musterlösung: Links und Quellen"
    doc.add_heading("Hilfreiche Webseiten für Schule und Beruf", 1)
    p = doc.add_paragraph("Für Berufsinformationen: ")
    _add_link(p, "Berufsberatung Schweiz", "https://www.berufsberatung.ch/")
    p = doc.add_paragraph("Für Zugverbindungen: ")
    _add_link(p, "SBB Fahrplan", "https://www.sbb.ch/")
    doc.add_paragraph("Quelle: Berufsberatung Schweiz, Informationen zu Berufen, www.berufsberatung.ch, Zugriff am 14.10.2026.")
    doc.save(out)


def _teacher(out: Path) -> None:
    doc = Document()
    _raw_style(doc)
    doc.core_properties.title = "Lehrpersonenhilfen: Word-Kurs 3rd-round-qa"
    doc.add_heading("Word-Kurs · Ergänzungen V3", 0)
    doc.add_paragraph("Die Pflichtfolge A1–A13 und alle bestehenden Prüfungen bleiben unverändert. Die zwei Zusatzaufträge werden nicht in die Fleissnote aufgenommen.")
    topics = [
        ("A1 · Dateisicherheit (Kurzroutine, 5–8 Min.)",
         "Vorbereitung: Speicherort IB zeigen. Demonstration: Dokument benennen, speichern, schliessen, wieder öffnen. Typischer Fehler: Datei irgendwo in Downloads abgelegt. Formativ: Jedes Kind zeigt die gespeicherte Datei am korrekten Ort. Bei Bedarf später erneut üben."),
        ("A7 · Alternativtext (freiwillig, 5 Min.)",
         "Nach der Hauptaufgabe kurz zeigen: Rechtsklick auf Bild → Alternativtext anzeigen/bearbeiten. Nur Bildinhalt und Zweck beschreiben, nicht 'Bild von'. Alternative: dekorative Bilder als dekorativ kennzeichnen. Keine Pflicht für A7 und keine neue Prüfungsanforderung."),
        ("PLUS 1 · Schnupperlehrbrief (ca. 45 Min.)",
         "Vorbereitung: Aufgabenblatt und START_Schnupperlehrbrief.docx bereitstellen. Einstieg: Absender / Empfänger / Datum / Betreff zeigen. 5 Min Demo, 25 Min gestalten, 10 Min PDF und Rückkontrolle, 5 Min Reserve. Hilfen: markierte Positionen, Musterlösung nur für Lehrperson. Formativ: genau einseitige DOCX und PDF, gleiche Inhalte. Nicht an echte Firmen senden."),
        ("PLUS 2 · Links und Quellen (ca. 20–25 Min.)",
         "Vorbereitung: Aufgabenblatt und START_Links_und_Quellen.docx. 3 Min Demo Strg+K, 12 Min Links, 5 Min Quellenzeile, 5 Min Kontrolle. Technik: Internetzugriff auf zwei offizielle Seiten prüfen. Formativ: zwei echte Hyperlink-Ziele, lesbare Linktexte, Quellenzeile mit Zugriffsdatum."),
        ("A12/A13 & Prüfungen",
         "A12/A13 bleiben im Hauptauftrag ohne neue Pflichtfunktion. Kein PDF oder Hyperlink wird im bestehenden 30-Punkte-Test unangekuendigt verlangt. Die Zusatzaufträge können nach dem Pflichtkurs oder als freiwillige Wahlaufgaben eingesetzt werden."),
    ]
    for heading, body in topics:
        doc.add_heading(heading, level=2)
        doc.add_paragraph(body)
    doc.add_heading("Beobachtungskriterien", level=2)
    for s in [
        "Dateisicherheit: richtiger Speicherort und Dateiname; Datei lässt sich erneut finden.",
        "Brief: Adressblöcke, Datum, Betreff, Abschnitte, Grussformel, 1 Seite, identische PDF-Kopie.",
        "Links: echte anklickbare Beziehungen (nicht nur blau gefärbter Text).",
        "Quellen: Urheber / Anbieter, Seitenthema, Adresse und Zugriffstag.",
        "Bei Problemen zuerst technische Bedienung vormachen; nicht zugleich Textproduktion und neue Word-Funktionen fordern.",
        "Letztes Gate: auf den tatsächlichen Schul-PCs in Word 365 prüfen. LibreOffice- oder CI-Build ist kein Ersatz.",
    ]:
        doc.add_paragraph(s, style="List Bullet")
    doc.save(out)


def build_all(root: Path) -> None:
    output = Path(root) / "arbeitsblaetter"
    teacher = output / "lehrperson"
    teacher.mkdir(parents=True, exist_ok=True)
    _instruction_brief(output / "ZUSATZ_Schnupperlehrbrief.docx")
    _starter_brief(output / "START_Schnupperlehrbrief.docx")
    _model_brief(teacher / "MUSTER_Schnupperlehrbrief.docx")
    _instruction_links(output / "ZUSATZ_Links_und_Quellen.docx")
    _starter_links(output / "START_Links_und_Quellen.docx")
    _model_links(teacher / "MUSTER_Links_und_Quellen.docx")
    _teacher(teacher / "LEHRPERSONENHILFEN_V3.docx")
