from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT

from course_common import (
    NAVY, TEAL,
    base_doc, block, add_text, add_step, add_tip, add_check, add_finish,
    new_workspace_section, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def build_document(out: Path):
    doc=base_doc('A6','Seitenlayout','Die Seite passend einstellen','Du arbeitest heute nur am Aufbau der Seite – nicht am Text.','eine Seite auf Querformat stellen, Seitenränder ändern und mit einem Seitenumbruch gezielt eine neue Seite beginnen.')
    t=block(doc,'01','SEITE 2'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Bearbeite nur die Übungsseite'); set_run(x,size=12.8,bold=True,color=NAVY); add_text(r,'Klicke zuerst irgendwo auf Seite 2. Der Text dort ist bereits richtig formatiert.',9.5,after=.7)
    add_step(r,'A',[('Seite 2',True,False,NAVY),('  →  Querformat',False,False,None)])
    add_step(r,'B',[('Seite 2',True,False,NAVY),('  →  Seitenränder «Schmal»',False,False,None)])
    add_step(r,'C',[('Klicke direkt vor «PACKLISTE»',True,False,NAVY),('  →  Ctrl + Enter',False,False,None)])
    add_step(r,'D',[('Kontrolliere',True,False,NAVY),('  →  «PACKLISTE» beginnt jetzt auf einer neuen Seite.',False,False,None)])
    add_tip(doc,'Hochformat = ▯   |   Querformat = ▭   |   Neue Seite = Ctrl + Enter','MERKE')
    add_tip(doc,'Für eine neue Seite nicht viele Male Enter drücken. Ein Seitenumbruch bleibt auch dann richtig, wenn später Text dazukommt.')
    add_check(doc,'Seite 1 bleibt Hochformat. Die Übungsseite ist Querformat. «PACKLISTE» beginnt auf einer neuen Seite.')
    add_finish(doc)
    sec=new_workspace_section(doc,'A6'); sec.orientation=WD_ORIENT.PORTRAIT; sec.page_width=Cm(21); sec.page_height=Cm(29.7)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; x=p.add_run('SCHULAUSFLUG NACH LUZERN'); set_run(x,size=20,bold=True,color=NAVY)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after=Pt(12); x=p.add_run('Dienstag, 22. September'); set_run(x,size=11,bold=True,color=TEAL)
    p=doc.add_paragraph(); x=p.add_run('PROGRAMM'); set_run(x,size=13,bold=True,color=NAVY)
    for tm,txt in [('08.00 Uhr','Treffpunkt beim Schulhaus'),('08.20 Uhr','Abfahrt mit dem Zug'),('10.00 Uhr','Verkehrshaus'),('12.15 Uhr','Mittagspause am See'),('14.00 Uhr','Altstadt-Rundgang'),('16.30 Uhr','Rückfahrt')]:
        p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(4); x=p.add_run(tm+'  –  '); set_run(x,size=11,bold=True,color=NAVY); x=p.add_run(txt); set_run(x,size=11)
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(14); x=p.add_run('PACKLISTE'); set_run(x,size=13,bold=True,color=NAVY)
    for item in ['Trinkflasche','Lunch','Regenjacke','Schreibzeug','Halbtax / Billet falls vorhanden']:
        p=doc.add_paragraph(); p.paragraph_format.left_indent=Cm(.5); x=p.add_run('•  '+item); set_run(x,size=11)
    finalise(doc,out,'A6 - Seitenlayout')


def build(root: Path):
    build_document(root/'arbeitsblaetter'/'A6_Seitenlayout.docx')


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A6', build)
