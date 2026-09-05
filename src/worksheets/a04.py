from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image, ImageDraw, ImageFont

from build_runtime import resolve_font_paths
from course_common import (
    NAVY, TEAL_DARK, MID,
    base_doc, block, add_text, add_step, add_workarea, add_tip, add_check,
    add_finish, add_picture, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def preview(path: Path):
    reg,bold=resolve_font_paths(); W,H=1500,390
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    ft=ImageFont.truetype(bold,48); fh=ImageFont.truetype(bold,28); fb=ImageFont.truetype(reg,25)
    d.rounded_rectangle((18,18,W-18,H-18),radius=18,outline='#D3DEE2',width=3,fill='white')
    d.text((60,36),'KLASSENAUSFLUG',font=ft,fill='#237B78')
    d.text((60,112),'Mitnehmen',font=fh,fill='#17324D'); y=155
    for s in ['Trinkflasche','Lunch','Regenjacke']:
        d.text((68,y),'•',font=fb,fill='#237B78'); d.text((105,y),s,font=fb,fill='#17324D'); y+=42
    x=760; d.text((x,112),'So läuft es ab',font=fh,fill='#17324D'); y=155
    for i,s in enumerate(['Treffpunkt beim Schulhaus','Zugfahrt','Wanderung zum Aussichtspunkt'],1):
        d.text((x+4,y),f'{i}.',font=fb,fill='#237B78'); d.text((x+45,y),s,font=fb,fill='#17324D'); y+=42
    im.save(path,quality=95)


def build_document(out: Path, preview_path: Path):
    doc=base_doc('A4','Listen & Nummerierungen','Dinge oder Reihenfolge?','Du lernst, wann du Aufzählungen und wann du Nummerierungen verwendest.','Dinge als Aufzählung und eine Reihenfolge als Nummerierung darstellen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Mach aus Zeilen richtige Listen'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Dinge = Aufzählung. Reihenfolge = Nummerierung.',9.5,bold=True,color=MID)
    add_step(r,'A',[('Markiere die drei Dinge unter «Mitnehmen»',True,False,NAVY),('  →  Aufzählung',False,False,None)])
    add_step(r,'B',[('Markiere die drei Schritte unter «Ablauf»',True,False,NAVY),('  →  Nummerierung',False,False,None)])
    add_step(r,'C',[('Füge unter «Mitnehmen» «Sonnencreme» hinzu',True,False,NAVY),('  →  sie gehört zur Aufzählung',False,False,None)])
    add_workarea(doc,'HIER','ARBEITEN 01',['SPORTTAG','Mitnehmen','Turnschuhe','Trinkflasche','Lunch','Ablauf','Treffpunkt beim Schulhaus','Gemeinsames Aufwärmen','Start der Wettkämpfe'],size=9.8)
    add_tip(doc,'Punkte und Zahlen nicht von Hand tippen. Benutze die Word-Funktion für Aufzählung oder Nummerierung.')
    t=block(doc,'02','NACHBAUEN',fill_left=TEAL_DARK); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Baue die Listen der Vorlage nach'); set_run(x,size=12.8,bold=True,color=NAVY); add_text(r,'Verändere den Text nicht. Entscheide anhand der Vorlage: Punkte oder Zahlen?',9.4); add_picture(r,preview_path,10.5)
    add_check(doc,'Lösche in der Nummerierung den zweiten Schritt. Prüfe, ob Word automatisch neu nummeriert.')
    add_finish(doc); finalise(doc,out,'A4 - Listen und Nummerierungen')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; prev=sheets/'assets'/'vorlagen'; prev.mkdir(parents=True,exist_ok=True)
    image=prev/'a4_ausflug_vorlage.png'; preview(image)
    build_document(sheets/'A4_Listen_und_Nummerierungen.docx',image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A4', build)
