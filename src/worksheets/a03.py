from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PIL import Image, ImageDraw, ImageFont

from build_runtime import resolve_font_paths
from course_common import (
    NAVY, TEAL, TEAL_DARK, MID,
    base_doc, block, add_text, add_step, add_workarea, add_tip, add_check,
    add_finish, add_picture, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def preview(path: Path):
    reg,bold=resolve_font_paths(); W,H=1500,470
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    ft=ImageFont.truetype(bold,54); fd=ImageFont.truetype(bold,28); fb=ImageFont.truetype(reg,27)
    d.rounded_rectangle((18,18,W-18,H-18),radius=18,outline='#D3DEE2',width=3,fill='white')
    s='KINOABEND'; box=d.textbbox((0,0),s,font=ft); d.text(((W-(box[2]-box[0]))/2,42),s,font=ft,fill='#237B78')
    s='Freitag, 25. September'; box=d.textbbox((0,0),s,font=fd); d.text((W-70-(box[2]-box[0]),120),s,font=fd,fill='#17324D')
    y=205
    for s in [
        'Wir schauen gemeinsam einen Film in der Aula.',
        'Treffpunkt: 18.15 Uhr vor der Aula.',
        'Ende: ca. 21.00 Uhr.',
        'Bring etwas zu trinken mit.',
    ]:
        d.text((70,y),s,font=fb,fill='#17324D'); y+=58
    im.save(path,quality=95)


def _prepare_kino_workarea(table):
    """Keep font formatting correct so task 02 tests paragraph skills only."""
    r = table.cell(0,1)
    for i,p in enumerate(r.paragraphs):
        if not p.runs:
            continue
        if i == 0:
            set_run(p.runs[0],name='Arial',size=11.2,bold=True,color=TEAL)
        elif i == 1:
            set_run(p.runs[0],name='Arial',size=9.8,bold=True,color=NAVY)
        else:
            set_run(p.runs[0],name='Arial',size=9.8,color=NAVY)


def build_document(out: Path, preview_path: Path):
    doc=base_doc('A3','Absätze & Ordnung','Text braucht Luft','Du lernst, wie du Absätze ausrichtest und Abstände sauber einstellst.','Absätze links, zentriert oder rechts ausrichten und Zeilen- sowie Absatzabstände einstellen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Ordne den Infotext Schritt für Schritt'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Markiere immer genau den Absatz oder die Absätze, die im Schritt genannt werden.',9.4,after=.45)
    add_text(r,'NEU: Ausrichtung + Zeilenabstand → Start → Absatz.  Abstand nach Absatz → Layout → Abstand → Nach.',9.15,bold=True,color=TEAL_DARK,after=.55)
    add_step(r,'A',[('«Bibliothek am Mittag»',True,False,NAVY),('  →  zentriert',False,False,None)])
    add_step(r,'B',[('«Schulhaus Sonnenberg»',True,False,NAVY),('  →  rechts',False,False,None)])
    add_step(r,'C',[('Die drei Textabsätze',True,False,NAVY),('  →  links',False,False,None)])
    add_step(r,'D',[('Die drei Textabsätze',True,False,NAVY),('  →  Zeilenabstand 1,5',False,False,None)])
    add_step(r,'E',[('Die drei Textabsätze',True,False,NAVY),('  →  Abstand nach Absatz: 6 pt',False,False,None)])
    add_workarea(doc,'HIER','ARBEITEN 01',['Bibliothek am Mittag','Schulhaus Sonnenberg','Unsere Bibliothek ist am Dienstag und Donnerstag über Mittag geöffnet.','Du kannst lesen, Hausaufgaben erledigen oder in Ruhe arbeiten.','Bitte stelle Bücher nach dem Lesen zurück und verlasse den Raum ordentlich.'])
    add_tip(doc,'Für Abstand nicht mehrfach Enter drücken. Nutze die Absatz-Einstellungen – so bleibt das Dokument sauber.')

    t=block(doc,'02','ANWENDEN',fill_left=TEAL_DARK); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Baue die Vorlage nach'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Der Text darunter ist schon richtig formatiert. Verändere nur Ausrichtung und Abstände.',9.35,after=.2)
    add_text(r,'Ausrichtung: nach Vorlage. Die vier Textabsätze: Zeilenabstand 1,5 und 6 pt Abstand danach.',9.2,color=MID,after=.25)
    add_picture(r,preview_path,9.7)
    work2=add_workarea(doc,'HIER','ARBEITEN 02',['KINOABEND','Freitag, 25. September','Wir schauen gemeinsam einen Film in der Aula.','Treffpunkt: 18.15 Uhr vor der Aula.','Ende: ca. 21.00 Uhr.','Bring etwas zu trinken mit.'],body_font='Arial',size=9.8)
    _prepare_kino_workarea(work2)
    add_check(doc,'Keine Leerzeilen? Titel zentriert, Datum rechts, Text links? Die vier Textabsätze haben 1,5 Zeilenabstand und 6 pt Abstand danach?')
    add_finish(doc); finalise(doc,out,'A3 - Absätze und Ordnung')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; prev=sheets/'assets'/'vorlagen'; prev.mkdir(parents=True,exist_ok=True)
    image=prev/'a3_kinoabend_vorlage.png'; preview(image)
    build_document(sheets/'A3_Absaetze_und_Ordnung.docx',image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A3', build)
