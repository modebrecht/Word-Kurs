from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image, ImageDraw, ImageFont

from build_runtime import resolve_font_paths
from course_common import (
    NAVY, TEAL_DARK, PALE,
    base_doc, block, add_text, add_step, add_tip, add_check, add_finish,
    add_picture, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def school_icon(path: Path):
    W,H=420,300
    im=Image.new('RGBA',(W,H),(255,255,255,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((55,95,365,260),radius=12,fill='#EAF4F3',outline='#237B78',width=5)
    d.polygon([(45,105),(210,35),(375,105)],fill='#237B78')
    d.rounded_rectangle((180,170,240,260),radius=6,fill='#17324D')
    for x in (95,275): d.rounded_rectangle((x,145,x+55,195),radius=5,fill='white',outline='#17324D',width=4)
    d.line((210,35,210,2),fill='#17324D',width=5); d.polygon([(210,4),(274,20),(210,36)],fill='#17324D')
    im.save(path)


def source_image(path: Path, icon_path: Path):
    icon=Image.open(icon_path).convert('RGBA')
    canvas=Image.new('RGB',(1100,760),'white')
    icon.thumbnail((650,470)); x=(1100-icon.width)//2; y=(760-icon.height)//2
    canvas.paste(icon.convert('RGB'),(x,y)); d=ImageDraw.Draw(canvas); d.rectangle((1,1,1098,758),outline='#D3DEE2',width=5)
    canvas.save(path,quality=95)


def preview(path: Path, icon_path: Path):
    reg,bold=resolve_font_paths(); W,H=1500,540
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    ft=ImageFont.truetype(bold,46); fb=ImageFont.truetype(reg,27)
    d.rounded_rectangle((18,18,W-18,H-18),radius=18,outline='#D3DEE2',width=3,fill='white')
    d.text((70,48),'UNSER SCHULHAUS',font=ft,fill='#17324D')
    icon=Image.open(icon_path).convert('RGBA'); icon.thumbnail((410,285)); im.paste(icon,(990,132),icon)
    d.text((75,150),'Im Schulhaus Sonnenberg lernen rund 240 Schülerinnen',font=fb,fill='#17324D')
    d.text((75,196),'und Schüler.',font=fb,fill='#17324D')
    d.text((75,270),'Die Bibliothek befindet sich im Erdgeschoss.',font=fb,fill='#17324D')
    d.text((75,445),'In der grossen Pause ist sie geöffnet.',font=fb,fill='#17324D')
    im.save(path,quality=95)


def build_document(out: Path, preview_path: Path):
    doc=base_doc('A7','Bilder in Word','Ein Bild passend einsetzen','Du fügst ein Bild ein und passt es so an, dass Text und Bild zusammenpassen.','ein Bild aus einer Datei einfügen, zuschneiden, auf eine passende Grösse bringen und den Text darum laufen lassen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Baue das Infoblatt nach'); set_run(x,size=12.8,bold=True,color=NAVY); add_text(r,'Bilddatei: a7_schulhaus.png',9.5,bold=True,color=TEAL_DARK); add_picture(r,preview_path,11.1)
    add_text(r,'1 · BILD EINSETZEN',8.8,bold=True,color=TEAL_DARK,after=.1)
    add_step(r,'A',[('Klicke hinter «UNSER SCHULHAUS» und drücke Enter',True,False,NAVY),('  →  Einfügen → Bilder → a7_schulhaus.png',False,False,None)])
    add_step(r,'B',[('Bild zuschneiden',True,False,NAVY),('  →  Bild anklicken → Bildformat → Zuschneiden → grossen weissen Rand entfernen',False,False,None)])
    add_step(r,'C',[('Bildbreite',True,False,NAVY),('  →  Bild anklicken → Bildformat → Grösse → Breite ca. 5,5 cm',False,False,None)])
    add_text(r,'2 · BILD + TEXT',8.8,bold=True,color=TEAL_DARK,after=.1)
    add_step(r,'D',[('Textumbruch',True,False,NAVY),('  →  Quadrat wählen; dann kann der Text am Bild vorbeilaufen',False,False,None)])
    add_step(r,'E',[('Bild anklicken',True,False,NAVY),('  →  mit der Maus rechts neben den Text ziehen',False,False,None)])
    t=block(doc,'HIER','ARBEITEN',fill_left=PALE,fill_right='FBFCFC',label_color=TEAL_DARK,label_size=11.0); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('UNSER SCHULHAUS'); set_run(x,size=18,bold=True,color=NAVY); add_text(r,'Im Schulhaus Sonnenberg lernen rund 240 Schülerinnen und Schüler.',10.6); add_text(r,'Die Bibliothek befindet sich im Erdgeschoss.',10.6); add_text(r,'In der grossen Pause ist sie geöffnet.',10.6)
    add_tip(doc,'Für den Textumbruch: Bild anklicken → kleines Layout-Symbol neben dem Bild → «Quadrat». Dann kann der Text am Bild vorbeilaufen.')
    add_check(doc,'Ist der weisse Rand weg? Ist das Bild ungefähr 5,5 cm breit? Steht es rechts? Läuft der Text links am Bild vorbei und darunter wieder über die ganze Breite?')
    add_finish(doc,'Gib dieses Arbeitsblatt zusammen mit der Bilddatei in deinem Ordner "IB" ab.')
    finalise(doc,out,'A7 - Bilder in Word')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; assets=sheets/'assets'; prev=assets/'vorlagen'; assets.mkdir(parents=True,exist_ok=True); prev.mkdir(parents=True,exist_ok=True)
    icon=assets/'a7_school_icon.png'; source=assets/'a7_schulhaus.png'; image=prev/'a7_schulhaus_vorlage.png'
    school_icon(icon); source_image(source,icon); preview(image,icon)
    build_document(sheets/'A7_Bilder_in_Word.docx',image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A7', build)
