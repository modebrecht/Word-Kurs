from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from course_common import (
    NAVY, TEAL_DARK, MID,
    base_doc, block, add_text, add_step, add_workarea, add_tip, add_check,
    add_finish, finalise, set_run,
)
from course_build_helpers import clear_paragraph as _clear


def build_document(out: Path):
    doc=base_doc('A4','Listen & Nummerierungen','Dinge oder Reihenfolge?','Du lernst, wann du Aufzählungen und wann du Nummerierungen verwendest.','Dinge als Aufzählung und eine Reihenfolge als Nummerierung darstellen.')
    t=block(doc,'01','AUFGABE'); r=t.cell(0,1); p=r.paragraphs[0]; _clear(p); x=p.add_run('Mach aus Zeilen richtige Listen'); set_run(x,size=12.8,bold=True,color=NAVY)
    add_text(r,'Dinge = Aufzählung. Reihenfolge = Nummerierung.',9.5,bold=True,color=MID,after=.25)
    add_text(r,'NEU: Start → Absatz → Aufzählungszeichen oder Nummerierung.',9.2,bold=True,color=TEAL_DARK,after=.55)
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
    sheets=root/'arbeitsblaetter'
    build_document(sheets/'A4_Listen_und_Nummerierungen.docx')


if __name__ == '__main__':
    from worksheet_runtime import run_single
    run_single('A4', build)
