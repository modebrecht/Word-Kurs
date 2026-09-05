from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from course_common import (
    NAVY, TEAL, MID,
    base_doc, block, add_text, add_step, add_workarea, add_tip, add_check,
    add_finish, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def build_document(out: Path):
    doc=base_doc('A1','Text formatieren','Die wichtigsten Werkzeuge','Du lernst die Grundwerkzeuge zum Formatieren von Text.','Text markieren und Schriftart, Schriftgrösse, Fett, Kursiv und Farbe einsetzen und eine Änderung rückgängig machen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Formatiere Schritt für Schritt'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Arbeite von A bis E. Markiere immer nur den Text, den der Schritt nennt.',9.4,after=.7)
    p=r.add_paragraph(); x=p.add_run('So sieht es aus:  '); set_run(x,size=9.3,bold=True,color=MID); x=p.add_run('Fett'); set_run(x,size=9.3,bold=True,color=NAVY); x=p.add_run('   ·   '); set_run(x,size=9.3,color=MID); x=p.add_run('Kursiv'); set_run(x,size=9.3,italic=True,color=NAVY); x=p.add_run('   ·   '); set_run(x,size=9.3,color=MID); x=p.add_run('Blau'); set_run(x,size=9.3,bold=True,color=TEAL)
    add_step(r,'A',[( 'Markiere zuerst den ganzen Rohtext',True,False,NAVY),('  →  Arial  →  11 pt',False,False,None)])
    add_step(r,'B',[('Markiere nur «Mein Lieblingsort»',True,False,NAVY),('  →  20 pt  →  ',False,False,None),('Fett',True,False,NAVY),('  →  Dunkelblau',False,False,NAVY)])
    add_step(r,'C',[('Markiere «Walensee» und danach «Churfirsten»',True,False,NAVY),('  →  ',False,False,None),('Fett',True,False,NAVY)])
    add_step(r,'D',[('Markiere nur «Sommer»',True,False,NAVY),('  →  ',False,False,None),('Blau',True,False,TEAL)])
    add_step(r,'E',[('Markiere den letzten Satz',True,False,NAVY),('  →  ',False,False,None),('Kursiv',False,True,NAVY)])
    add_workarea(doc,'HIER','ARBEITEN 01',['Mein Lieblingsort','Der Walensee liegt in der Ostschweiz. Auf der einen Seite ragen die Churfirsten steil auf, auf der anderen liegt das Glarnerland.','Im Sommer kann man baden, wandern oder einfach am Ufer sitzen.','Besonders schön finde ich den Blick über den See am Abend.'])
    add_tip(doc,'Etwas falsch gemacht? Mit Ctrl + Z machst du den letzten Schritt rückgängig.')
    add_check(doc,'Sieht dein Titel deutlich anders aus als der Fliesstext? Sind «Walensee» und «Churfirsten» fett?')
    add_finish(doc); finalise(doc,out,'A1 - Text formatieren')


def build(root: Path):
    build_document(root/'arbeitsblaetter'/'A1_Text_formatieren.docx')


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A1', build)
