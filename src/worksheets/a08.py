from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image, ImageDraw, ImageFont
from docx.shared import Pt

from build_runtime import resolve_font_paths
from course_common import (
    NAVY, TEAL_DARK,
    base_doc, block, add_text, add_step, add_tip, add_check, add_finish,
    add_picture, new_workspace_section, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def preview(path: Path):
    reg,bold=resolve_font_paths(); W,H=1500,500
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    ft=ImageFont.truetype(bold,32); fh=ImageFont.truetype(bold,23); fb=ImageFont.truetype(reg,22)
    d.rounded_rectangle((20,20,W-20,H-20),radius=18,outline='#D3DEE2',width=3,fill='white')
    x0,y0=70,55; tw=1360; cols=[230,330,520,280]; line='#9FB0B7'
    d.rectangle((x0,y0,x0+tw,y0+60),fill='white',outline=line,width=2)
    s='SPORTTAG – ABLAUF'; box=d.textbbox((0,0),s,font=ft); d.text((x0+(tw-(box[2]-box[0]))/2,y0+11),s,font=ft,fill='#17324D')
    rows=[['Zeit','Ort','Aktivität','Gruppe'],['09.00','Aula','Begrüssung','Alle'],['09.30','Turnhalle','Staffellauf','A'],['09.30','Sportplatz','Fussball','B'],['10.30','Aula','Pause','Alle']]
    y=y0+60
    for ri,row in enumerate(rows):
        x=x0
        for j,(w,val) in enumerate(zip(cols,row)):
            d.rectangle((x,y,x+w,y+54),fill='white',outline=line,width=2); f=fh if ri==0 else fb; c='#237B78' if ri==0 else '#17324D'; box=d.textbbox((0,0),val,font=f); tx=x+(w-(box[2]-box[0]))/2 if ri==0 or j in (0,3) else x+14; d.text((tx,y+13),val,font=f,fill=c); x+=w
        y+=54
    im.save(path,quality=95)


def build_document(out: Path, preview_path: Path):
    doc=base_doc('A8','Tabellen','Infos ins Raster bringen','Du baust eine einfache Tabelle und passt sie Schritt für Schritt an.','eine Tabelle erstellen, Daten in Zellen eintragen, eine Zeile ergänzen und Zellen verbinden.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Baue den Sporttag-Plan nach'); set_run(x,size=12.8,bold=True,color=NAVY); add_text(r,'Arbeite auf Seite 2. Die Daten stehen dort bereits bereit.',9.5); add_picture(r,preview_path,10.9)
    for letter,parts in [
        ('A',[('Unter «HIER TABELLE EINFÜGEN»',True,False,NAVY),('  →  Tabelle mit 4 Spalten und 5 Zeilen einfügen',False,False,None)]),
        ('B',[('Kopfzeile + vier Datenzeilen',True,False,NAVY),('  →  Angaben von oben in die richtigen Zellen übertragen',False,False,None)]),
        ('C',[('Kopfzeile',True,False,NAVY),('  →  fett und zentriert',False,False,None)]),
        ('D',[('Zeit und Gruppe',True,False,NAVY),('  →  zentrieren',False,False,None)]),
        ('E',[('Neue Zeile über der Tabelle einfügen',True,False,NAVY),('  →  alle 4 Zellen dieser Zeile verbinden',False,False,None)]),
        ('F',[('In die verbundene Zelle',True,False,NAVY),('  →  «SPORTTAG – ABLAUF», 16 pt, fett, zentriert',False,False,None)]),
    ]: add_step(r,letter,parts)
    add_tip(doc,'Zellen verbinden: Markiere die vier Zellen der neuen Zeile. Unter Tabellenlayout findest du «Zellen verbinden».')
    add_check(doc,'Hat deine Tabelle 4 Spalten? Sind alle Daten in der richtigen Zeile? Geht der Titel über die ganze Tabelle?')
    add_finish(doc)
    new_workspace_section(doc,'A8')
    p=doc.add_paragraph(); x=p.add_run('DATEN FÜR DIE TABELLE'); set_run(x,size=16,bold=True,color=NAVY)
    for s in ['Zeit | Ort | Aktivität | Gruppe','09.00 | Aula | Begrüssung | Alle','09.30 | Turnhalle | Staffellauf | A','09.30 | Sportplatz | Fussball | B','10.30 | Aula | Pause | Alle']:
        p=doc.add_paragraph(); x=p.add_run(s); set_run(x,size=11)
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(12); x=p.add_run('HIER TABELLE EINFÜGEN'); set_run(x,size=12,bold=True,color=TEAL_DARK)
    finalise(doc,out,'A8 - Tabellen')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; prev=sheets/'assets'/'vorlagen'; prev.mkdir(parents=True,exist_ok=True)
    image=prev/'a8_sporttag_tabelle_vorlage.png'; preview(image)
    build_document(sheets/'A8_Tabellen.docx',image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A8', build)
