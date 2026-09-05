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


def list_tools_preview(path: Path):
    reg, bold = resolve_font_paths()
    W, H = 1500, 300
    im = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(im)
    f_tab = ImageFont.truetype(bold, 30)
    f_label = ImageFont.truetype(bold, 27)
    f_small = ImageFont.truetype(reg, 23)
    border = '#D3DEE2'
    pale = '#F3F6F7'
    accent = '#237B78'
    navy = '#17324D'

    d.rounded_rectangle((16, 16, W-16, H-16), radius=18, outline=border, width=3, fill='white')
    d.rectangle((16, 16, W-16, 80), fill=pale)
    d.text((48, 32), 'Start', font=f_tab, fill=navy)
    d.line((45, 75, 132, 75), fill=accent, width=5)
    for x, label in [(175, 'Einfügen'), (330, 'Zeichnen'), (480, 'Entwurf'), (625, 'Layout')]:
        d.text((x, 36), label, font=f_small, fill='#667684')

    d.text((65, 98), 'Absatz', font=f_small, fill='#667684')

    # Aufzählung button: neutral Word-like list icon, no task content shown.
    d.rounded_rectangle((65, 130, 620, 242), radius=12, outline=accent, width=4, fill='white')
    for yy in (154, 180, 206):
        d.ellipse((92, yy-4, 100, yy+4), fill=navy)
        d.line((118, yy, 210, yy), fill=navy, width=4)
    d.text((245, 158), 'Aufzählung', font=f_label, fill=navy)

    # Nummerierung button: shows only the generic tool icon.
    d.rounded_rectangle((665, 130, 1220, 242), radius=12, outline=accent, width=4, fill='white')
    for no, yy in zip(('1.', '2.', '3.'), (154, 180, 206)):
        d.text((690, yy-13), no, font=f_small, fill=navy)
        d.line((735, yy, 827, yy), fill=navy, width=4)
    d.text((860, 158), 'Nummerierung', font=f_label, fill=navy)

    d.text((1260, 142), 'Nur die', font=f_small, fill='#667684')
    d.text((1260, 174), 'Werkzeuge', font=f_label, fill=navy)
    d.text((1260, 210), 'sind gezeigt.', font=f_small, fill='#667684')

    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, quality=95)


def build_document(out: Path, preview_path: Path):
    doc=base_doc('A4','Listen & Nummerierungen','Dinge oder Reihenfolge?','Du lernst, wann du Aufzählungen und wann du Nummerierungen verwendest.','Dinge als Aufzählung und eine Reihenfolge als Nummerierung darstellen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Mach aus Zeilen richtige Listen'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Dinge = Aufzählung. Reihenfolge = Nummerierung.',9.5,bold=True,color=MID,after=.25)
    add_text(r,'NEU: Start → Absatz → Aufzählungszeichen oder Nummerierung.',9.2,bold=True,color=TEAL_DARK,after=.35)
    add_picture(r, preview_path, 11.0)
    add_step(r,'A',[('Markiere die drei Dinge unter «Mitnehmen»',True,False,NAVY),('  →  Aufzählung',False,False,None)])
    add_step(r,'B',[('Markiere die drei Schritte unter «Ablauf»',True,False,NAVY),('  →  Nummerierung',False,False,None)])
    add_step(r,'C',[('Füge unter «Mitnehmen» «Sonnencreme» hinzu',True,False,NAVY),('  →  sie gehört zur Aufzählung',False,False,None)])
    add_workarea(doc,'HIER','ARBEITEN 01',['SPORTTAG','Mitnehmen','Turnschuhe','Trinkflasche','Lunch','Ablauf','Treffpunkt beim Schulhaus','Gemeinsames Aufwärmen','Start der Wettkämpfe'],size=9.8)
    add_tip(doc,'Punkte und Zahlen nicht von Hand tippen. Benutze die Word-Funktion für Aufzählung oder Nummerierung.')

    t=block(doc,'02','ANWENDEN',fill_left=TEAL_DARK); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Entscheide jetzt selbst'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Welche Zeilen sind Dinge? Welche Zeilen sind eine Reihenfolge? Verwende die passende echte Word-Liste.',9.4)
    add_workarea(doc,'HIER','ARBEITEN 02',['KLASSENAUSFLUG','Mitnehmen','Trinkflasche','Lunch','Regenjacke','So läuft es ab','Treffpunkt beim Schulhaus','Zugfahrt','Wanderung zum Aussichtspunkt'],body_font='Arial',size=9.8)

    add_check(doc,'Sind «Mitnehmen» und «So läuft es ab» mit den passenden echten Word-Listen formatiert? Lösche in der Nummerierung den zweiten Schritt, prüfe die automatische Neunummerierung und mache danach mit Ctrl + Z rückgängig.')
    add_finish(doc); finalise(doc,out,'A4 - Listen und Nummerierungen')


def build(root: Path):
    sheets=root/'arbeitsblaetter'; prev=sheets/'assets'/'vorlagen'; prev.mkdir(parents=True, exist_ok=True)
    image=prev/'a4_listen_werkzeuge.png'; list_tools_preview(image)
    build_document(sheets/'A4_Listen_und_Nummerierungen.docx', image)


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A4', build)
