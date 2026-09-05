from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image, ImageDraw, ImageFont

from build_runtime import resolve_font_paths
from course_common import (
    NAVY, TEAL_DARK,
    base_doc, block, add_text, add_workarea, add_tip, add_check,
    add_finish, add_picture, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def preview(path: Path):
    reg, bold = resolve_font_paths()
    W,H=1500,540
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    f_title=ImageFont.truetype(bold,66); f_sub=ImageFont.truetype(bold,34)
    f_body=ImageFont.truetype(reg,30); f_body_b=ImageFont.truetype(bold,30); f_small=ImageFont.truetype(reg,28)
    d.rounded_rectangle((18,18,W-18,H-18),radius=18,outline='#D3DEE2',width=3,fill='white')
    x=65; y=52
    d.text((x,y),'Game Night',font=f_title,fill='#237B78'); y+=96
    d.text((x,y),'Freitag, 18. September',font=f_sub,fill='#17324D'); y+=62
    d.text((x,y),'18.30-21.00 Uhr',font=f_body_b,fill='#17324D'); y+=52
    d.text((x,y),'Zimmer 204',font=f_body_b,fill='#237B78'); y+=64
    d.text((x,y),'Bring dein Lieblingsspiel mit.',font=f_body,fill='#17324D'); y+=52
    d.text((x,y),'Getränke stehen bereit. Anmeldung bis Mittwoch bei Frau Keller.',font=f_small,fill='#5E6D78')
    path.parent.mkdir(parents=True, exist_ok=True); im.save(path,quality=95)


def build_document(out: Path, preview_path: Path):
    doc=base_doc('A2','Nach Vorlage gestalten','Schau genau hin','Du nutzt die Werkzeuge aus A1 und baust eine sichtbare Vorlage nach.','an einer Vorlage erkennen, welche Textstellen grösser, fett oder farbig formatiert sind, und diese Formatierung nachbauen.')
    t=block(doc,'01','NACHBAUEN'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Baue die Vorlage genau nach'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Verändere den Text nicht. Verändere nur die Formatierung.',9.5,after=.6); add_picture(r,preview_path,11.7)
    add_workarea(doc,'HIER','ARBEITEN 01',['Game Night','Freitag, 18. September','18.30-21.00 Uhr','Zimmer 204','Bring dein Lieblingsspiel mit.','Getränke stehen bereit. Anmeldung bis Mittwoch bei Frau Keller.'])
    add_tip(doc,'Nicht raten – vergleichen. Schau immer nur auf eine Sache: zuerst Grösse, dann Fett, dann Farbe.')
    add_check(doc,'Vergleiche Zeile für Zeile mit der Vorlage. Findest du noch einen Unterschied?')
    add_finish(doc); finalise(doc,out,'A2 - Nach Vorlage gestalten')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; prev=sheets/'assets'/'vorlagen'; prev.mkdir(parents=True,exist_ok=True)
    image=prev/'a2_game_night_vorlage.png'; preview(image)
    build_document(sheets/'A2_Nach_Vorlage_gestalten.docx',image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A2', build)
