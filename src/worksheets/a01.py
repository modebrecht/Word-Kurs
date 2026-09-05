from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image, ImageDraw, ImageFont

from build_runtime import resolve_font_paths
from course_common import (
    NAVY, TEAL, MID,
    base_doc, block, add_text, add_step, add_workarea, add_tip, add_check,
    add_finish, add_picture, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def toolbar_preview(path: Path):
    reg, bold = resolve_font_paths()
    W, H = 1500, 330
    im = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(im)
    f_tab = ImageFont.truetype(bold, 30)
    f_ui = ImageFont.truetype(reg, 27)
    f_ui_b = ImageFont.truetype(bold, 30)
    f_small = ImageFont.truetype(reg, 23)
    border = '#D3DEE2'
    pale = '#F3F6F7'
    accent = '#237B78'

    d.rounded_rectangle((16, 16, W-16, H-16), radius=18, outline=border, width=3, fill='white')
    d.rectangle((16, 16, W-16, 80), fill=pale)
    d.text((48, 32), 'Start', font=f_tab, fill='#17324D')
    d.line((45, 75, 132, 75), fill=accent, width=5)
    for x, label in [(175, 'Einfügen'), (330, 'Zeichnen'), (480, 'Entwurf'), (625, 'Layout'), (755, 'Referenzen')]:
        d.text((x, 36), label, font=f_small, fill='#667684')

    y1, y2 = 118, 190
    d.text((55, 96), 'Schriftart', font=f_small, fill='#667684')
    d.rounded_rectangle((55, y1, 385, y2), radius=10, outline=accent, width=4, fill='white')
    d.text((78, 136), 'Arial', font=f_ui, fill='#17324D')
    d.polygon([(350, 145), (365, 145), (357, 156)], fill='#17324D')

    d.text((420, 96), 'Grösse', font=f_small, fill='#667684')
    d.rounded_rectangle((420, y1, 565, y2), radius=10, outline=accent, width=4, fill='white')
    d.text((449, 136), '11', font=f_ui, fill='#17324D')
    d.polygon([(530, 145), (545, 145), (537, 156)], fill='#17324D')

    buttons = [
        (610, 'F', True, False),
        (705, 'K', False, True),
    ]
    for x, label, is_bold, is_italic in buttons:
        d.rounded_rectangle((x, y1, x+76, y2), radius=10, outline=accent, width=4, fill='white')
        font = f_ui_b if is_bold else ImageFont.truetype(reg, 32)
        d.text((x+24, 134), label, font=font, fill='#17324D')

    d.text((818, 96), 'Schriftfarbe', font=f_small, fill='#667684')
    d.rounded_rectangle((818, y1, 930, y2), radius=10, outline=accent, width=4, fill='white')
    d.text((850, 130), 'A', font=f_ui_b, fill='#17324D')
    d.line((846, 171, 902, 171), fill='#237B78', width=8)
    d.polygon([(900, 143), (915, 143), (907, 154)], fill='#17324D')

    d.text((985, 104), 'Diese Werkzeuge findest du', font=f_small, fill='#667684')
    d.text((985, 138), 'oben unter «Start».', font=f_ui_b, fill='#17324D')
    d.text((55, 232), 'Markieren: Mit gedrückter Maustaste über den gewünschten Text ziehen.', font=f_ui, fill='#17324D')
    d.text((55, 278), 'Dann Schriftart, Grösse, Fett, Kursiv oder Schriftfarbe wählen.', font=f_small, fill='#667684')

    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, quality=95)


def build_document(out: Path, toolbar_path: Path):
    doc=base_doc('A1','Text formatieren','Die wichtigsten Werkzeuge','Du lernst die Grundwerkzeuge zum Formatieren von Text.','Text markieren und Schriftart, Schriftgrösse, Fett, Kursiv und Farbe einsetzen und eine Änderung rückgängig machen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Formatiere Schritt für Schritt'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Arbeite von A bis E. Markiere immer nur den Text, den der Schritt nennt.',9.4,after=.45)
    add_picture(r, toolbar_path, 11.35)
    add_step(r,'A',[( 'Markiere zuerst den ganzen Rohtext',True,False,NAVY),('  →  Arial  →  11 pt',False,False,None)])
    add_step(r,'B',[('Markiere nur «Mein Lieblingsort»',True,False,NAVY),('  →  20 pt  →  ',False,False,None),('Fett',True,False,NAVY),('  →  Dunkelblau',False,False,NAVY)])
    add_step(r,'C',[('Markiere «Walensee» und danach «Churfirsten»',True,False,NAVY),('  →  ',False,False,None),('Fett',True,False,NAVY)])
    add_step(r,'D',[('Markiere nur «Sommer»',True,False,NAVY),('  →  ',False,False,None),('Blau',True,False,TEAL)])
    add_step(r,'E',[('Markiere den letzten Satz',True,False,NAVY),('  →  ',False,False,None),('Kursiv',False,True,NAVY)])
    add_workarea(doc,'HIER','ARBEITEN 01',['Mein Lieblingsort','Der Walensee liegt in der Ostschweiz. Auf der einen Seite ragen die Churfirsten steil auf, auf der anderen liegt das Glarnerland.','Im Sommer kann man baden, wandern oder einfach am Ufer sitzen.','Besonders schön finde ich den Blick über den See am Abend.'])
    add_tip(doc,'Etwas falsch gemacht? Mit Ctrl + Z machst du den letzten Schritt rückgängig.')
    add_check(doc,'Ist der Titel deutlich anders als der Fliesstext? Sind «Walensee» und «Churfirsten» fett? Ist «Sommer» blau? Ist der letzte Satz kursiv?')
    add_finish(doc); finalise(doc,out,'A1 - Text formatieren')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; prev=sheets/'assets'/'vorlagen'; prev.mkdir(parents=True,exist_ok=True)
    image=prev/'a1_start_werkzeuge.png'; toolbar_preview(image)
    build_document(sheets/'A1_Text_formatieren.docx',image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A1', build)
