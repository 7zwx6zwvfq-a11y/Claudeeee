#!/usr/bin/env python3
"""
VIDEO 13 — FINAL SCRIPT
5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)
NEUROCENTS · 77 beats · ~770 words · ~5.5 min
Estructura canonical Creator Brief v3.0
"""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

TITLE    = "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)"
SUBTITLE = "NEUROCENTS · VIDEO 13 — FINAL"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [

    # ── HOOK ── 10 beats (~30 seg) — identity → promesa → dato → loop abierto
    ("HOOK", [
        "Alex earns more than he did three years ago.",                                 # B1  IDENTITY
        "He has less to show for it.",                                                  # B2
        "Not because of bad decisions.",                                                # B3  eliminate A
        "Not because of poor discipline.",                                              # B4  eliminate B
        "Because his brain has been running five programs he was never told about.",    # B5  TWIST
        "We're going to show you all five — in the order they fire.",                  # B6  PROMISE
        "The third one gets worse the more financially educated he becomes.",           # B7  DATA HOOK
        "The fifth one compounds biologically — not just financially.",                 # B8  SPECIFICITY
        "His brain started running Trap One this week.",                                # B9  VILLAIN ACTIVE
        "So did yours.",                                                                # B10 OPEN LOOP
    ]),

    # ── TRAP 1 ── 9 beats
    ("TRAP 1 — THE ANTICIPATION BURN", [
        "It is Wednesday. Alex hasn't been paid.",
        "He already knows what he's going to buy.",
        "Wolfram Schultz — Cambridge — won part of the Nobel Prize for this.",
        "Dopamine does not fire when the reward arrives.",
        "It fires when the brain predicts the reward is coming.",
        "By Wednesday, the dopamine peak has already passed.",
        "By Friday — payday — the signal is declining.",
        "His spending on Friday is not a decision. It is a receipt.",
        "Trap One fires first. Trap Two makes it invisible.",
    ]),

    # ── TRAP 2 ── 8 beats
    ("TRAP 2 — THE BALANCE BLINDSPOT", [
        "Saturday morning. Alex does not check his balance.",
        "He will check next week — when things are calmer.",
        "In thirty days: six balance checks. All six after a paycheck. Zero after a large purchase.",
        "Galai and Sade — Hebrew University, 2006 — called it the ostrich effect.",
        "When financial information is painful, the brain stops seeking it.",
        "Not a choice — a conditioned reflex, built to reduce cortisol.",
        "Every time Alex looked at a bad number, his brain recorded pain.",
        "After enough repetitions, avoidance became automatic.",
    ]),

    # ── CTA ── 2 beats  →  beats 28-29 = 37% through 77  ✅
    ("CTA", [
        "If your brain is doing this to you right now — subscribe.",
        "We break down a new bias every week. It's free. And it might save you more than you think.",
    ]),

    # ── TRAP 3 ── 8 beats
    ("TRAP 3 — THE EXPERTISE TRAP", [
        "Alex has been reading about behavioral finance for eight months.",
        "He knows the vocabulary. He feels more in control than ever.",
        "Terrance Odean — UC Berkeley — studied investors for a decade.",
        "The ones who traded most frequently earned the lowest returns.",
        "Not because trading is wrong. Because confidence outpaced competence.",
        "Daniel Kahneman: eighty percent of investors believe they are above average.",
        "Fifty percent are, by definition, wrong.",
        "The expertise trap rewires in one direction: more vocabulary, more certainty — not more accuracy.",
    ]),

    # ── TRAP 4 ── 8 beats
    ("TRAP 4 — THE NIGHT DRAIN", [
        "It is 10:47pm. Alex is tired.",
        "He has been making decisions since 7am.",
        "He adds something to his cart. He buys it.",
        "Shai Danziger — Ben-Gurion University — studied eight judges over ten months.",
        "Morning: parole granted sixty-five percent of the time.",
        "By late afternoon: eleven percent.",
        "Same judges. Same evidence. Different reserve.",
        "Impulse purchases peak between nine and midnight. The Brain Villain doesn't need to be clever. It only needs to wait.",
    ]),

    # ── TRAP 5 ── 9 beats
    ("TRAP 5 — THE UPGRADE LOCK", [
        "Six months ago, Alex upgraded his apartment.",
        "He was satisfied for eleven days.",
        "Kent Berridge — University of Michigan — spent thirty years separating two systems.",
        "Wanting. And liking.",
        "Wanting is driven by dopamine. It increases with exposure.",
        "Liking is driven by opioid circuits. It decreases with repetition.",
        "Every upgrade strengthens wanting and habituates liking.",
        "The floor cannot go back. The ceiling keeps moving.",
        "Trap Five is the only one that compounds biologically — not just financially.",
    ]),

    # ── SYSTEM CLOSE ── 4 beats
    ("SYSTEM CLOSE", [
        "Five programs. Running simultaneously. Without Alex's permission.",
        "Trap One generates the impulse. Trap Two hides the damage. Trap Three provides the vocabulary to justify it.",
        "Trap Four lowers resistance at the exact moment it's needed most. Trap Five raises the floor so he cannot return.",
        "Kahneman and Deaton — Princeton, 2010 — found these programs consume the same percentage of income at €40,000 as at €140,000. The math adjusts. The programs don't.",
    ]),

    # ── BRAIN VILLAIN'S LAST TRICK ── 11 beats (template obligatorio)
    ("BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to identification.",
        "You're feeling it right now.",
        "Not denial. Something quieter.",
        "Something that sounds like rationality: 'I already know this.'",
        "That thought is not self-awareness. Not wisdom. Not knowledge.",
        "It is the Expertise Trap wearing the costume of insight.",
        "The programs are not broken.",
        "They are perfectly designed for an environment where pattern recognition was survival.",
        "Knowing the name of a predator kept your ancestors alive.",
        "It doesn't stop the dopamine.",
        "The Brain Villain was built for that world. Not this one.",
    ]),

    # ── IDENTITY CLOSE ── 8 beats (max 9)
    ("IDENTITY CLOSE", [
        "None of this is a character flaw.",
        "Anticipation Burn kept ancestors motivated. Balance Blindspot reduced cortisol when debt meant death. Night Drain was adaptive instinct. Upgrade Lock meant survival.",
        "The programs are not broken.",
        "They are perfectly designed for an environment that no longer exists.",
        "The Brain Villain was built for that world. Not this one.",
        "The next video maps the one structural decision that shuts down three of these five simultaneously.",
        "If your brain is doing this to you right now — subscribe.",
        "We break down a new bias every week. It's free. And it might save you more than you think.",
    ]),

]


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run(SUBTITLE)
    r.bold = True; r.font.size = Pt(14)

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run(LABEL)
    r.bold = True; r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run(TITLE)
    r.bold = True; r.italic = True; r.font.size = Pt(14)

    doc.add_paragraph()

    beat_num = 1
    for section_title, lines in SECTIONS:
        sh = doc.add_paragraph()
        sr = sh.add_run(f"— {section_title} —")
        sr.bold = True; sr.font.size = Pt(11)
        sr.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)
        sh.paragraph_format.space_before = Pt(14)
        sh.paragraph_format.space_after = Pt(4)

        for line in lines:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            nr = p.add_run(f"[{beat_num}]  ")
            nr.bold = True; nr.font.size = Pt(9)
            nr.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
            p.add_run(line).font.size = Pt(11)
            beat_num += 1
        doc.add_paragraph()

    all_lines = [line for _, lines in SECTIONS for line in lines]
    wc = sum(len(l.split()) for l in all_lines)
    total = beat_num - 1

    f = doc.add_paragraph()
    f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = f.add_run(f"TOTAL: {total} beats · ~{wc} words · ~{round(wc/140)} min")
    fr.font.size = Pt(9); fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/V13_final_SCRIPT.docx"
    doc.save(path)
    print(f"DOCX: {path} | {total} beats | {wc} words | ~{round(wc/140)} min")
    return all_lines, total, wc


def build_pdf(all_lines, total, wc):
    styles = getSampleStyleSheet()
    H1  = ParagraphStyle('H1',  parent=styles['Title'],  fontSize=14, leading=18, alignment=TA_CENTER)
    SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=10, leading=13,
                         alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                         fontName='Helvetica-Bold')
    META= ParagraphStyle('META',parent=styles['Normal'], fontSize=9,  leading=12,
                         alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    SEC = ParagraphStyle('SEC', parent=styles['Normal'], fontSize=10, leading=13,
                         textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                         spaceBefore=14, spaceAfter=4)
    LINE= ParagraphStyle('LINE',parent=styles['Normal'], fontSize=11, leading=17, spaceAfter=1)

    def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

    pdf_path = "/home/user/Claudeeee/V13_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"{LABEL} · {total} beats · ~{wc} words · ~{round(wc/140)} min", META),
        Spacer(1, 14),
    ]
    beat_num = 1
    for section_title, lines in SECTIONS:
        flow.append(Paragraph(f"— {esc(section_title)} —", SEC))
        for line in lines:
            flow.append(Paragraph(
                f'<font color="#888888"><b>[{beat_num}]</b></font>  {esc(line)}', LINE))
            beat_num += 1
        flow.append(Spacer(1, 8))
    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END · {total} beats · ~{wc} words · ~{round(wc/140)} min", META))
    doc.build(flow)
    print(f"PDF:  {pdf_path}")


def build_elevenlabs_pdf(all_lines, wc):
    styles = getSampleStyleSheet()
    H1  = ParagraphStyle('H1',  parent=styles['Title'],  fontSize=14, leading=18, alignment=TA_CENTER)
    SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=10, leading=13,
                         alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                         fontName='Helvetica-Bold')
    META= ParagraphStyle('META',parent=styles['Normal'], fontSize=9,  leading=12,
                         alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    LINE= ParagraphStyle('LINE',parent=styles['Normal'], fontSize=12, leading=20, spaceAfter=3)

    def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

    pdf_path = "/home/user/Claudeeee/V13_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 13 — FINAL", SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"ELEVENLABS — NARRATION ONLY · {len(all_lines)} lines · ~{wc} words · ~{round(wc/140)} min", META),
        Spacer(1, 16),
    ]
    for line in all_lines:
        flow.append(Paragraph(esc(line), LINE))
    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END OF SCRIPT · {len(all_lines)} lines · ~{wc} words", META))
    doc.build(flow)
    print(f"ELEVENLABS: {pdf_path}")


if __name__ == "__main__":
    all_lines, total, wc = build_docx()
    build_pdf(all_lines, total, wc)
    build_elevenlabs_pdf(all_lines, wc)
    print(f"\n✅ V13 FINAL — 3 archivos generados")
    print(f"   {total} beats · {wc} words · ~{round(wc/140)} min")
    print(f"   CTA en beats 28-29 = {round(28/total*100)}% ✅")
