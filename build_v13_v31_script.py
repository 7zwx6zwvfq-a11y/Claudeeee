#!/usr/bin/env python3
"""
VIDEO 13 — BRIEF v3.1 FINAL
5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)
NEUROCENTS · 93 beats · ~1,100 words · ~8 min
Hook strategy: S2 — DATO SIN CONTEXTO (Number Drop)
S17: Thumbnail → "5 WAYS / YOUR BRAIN / REWIRES ITSELF" → Beat 1 = "Five." + 5 circuits on screen
S18 rotation: V12 used S6 → V13 uses S2 ✅
CTA at beats 34-35 = 37% through 93 ✅
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
SUBTITLE = "NEUROCENTS · VIDEO 13 — BRIEF v3.1"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [

    # ── HOOK ── 10 beats (~30 seg)
    # S2 — DATO SIN CONTEXTO (Number Drop)
    # S17: Thumbnail shows "5 WAYS / YOUR BRAIN / REWIRES ITSELF" + Alex shocked + 5 circuits
    # Beat 1 = "Five." on screen. Alex mid-action. 5 red circuits firing in skull. No explanation.
    ("HOOK", [
        "Five.",                                                                              # B1  NUMBER on screen. Alex shocked. 5 circuits lit.
        "That is how many programs your brain is running right now that are keeping you exactly where you are.",  # B2 context arrives
        "Not bad decisions. Not poor discipline.",                                            # B3  eliminate false causes
        "Actual neural circuits — built through repetition — firing without your knowledge.", # B4  mechanism
        "The third one gets worse the more you learn about money.",                           # B5  specificity hook
        "The fifth one is the only financial bias that compounds biologically — not just financially.", # B6 curiosity gap
        "One of them fired this morning. Before you opened this video.",                      # B7  personal
        "We are going to show you all five — in the exact order they fire.",                  # B8  PROMISE
        "Your Brain Villain is already running Program One.",                                 # B9  VILLAIN ACTIVE
        "This is what it looks like.",                                                        # B10 OPEN LOOP → trap 1
    ]),

    # ── TRAP 1 ── 12 beats
    ("TRAP 1 — THE ANTICIPATION BURN", [
        "Wednesday. Alex has not been paid.",
        "He already knows exactly what he will buy when Friday comes.",
        "He has been thinking about it since Monday.",
        "This is not excitement. This is a dopamine schedule.",
        "Wolfram Schultz — Cambridge — won part of the Nobel Prize for discovering this mechanism.",
        "Dopamine does not fire when the reward arrives.",
        "It fires when the brain predicts the reward is coming.",
        "By Wednesday the dopamine peak has already passed.",
        "By Friday — payday — the signal is declining. The brain has moved to the next prediction.",
        "Alex spends on Friday not because he wants to. Because the wanting already happened without him.",
        "His Friday spending is not a decision. It is a receipt for a transaction his brain closed on Tuesday.",
        "Trap One fires first. Trap Two makes the damage invisible.",
    ]),

    # ── TRAP 2 ── 11 beats
    ("TRAP 2 — THE BALANCE BLINDSPOT", [
        "Saturday morning. Alex does not check his balance.",
        "He tells himself he will check next week — when things are calmer.",
        "Over thirty days: six balance checks. All six came after a paycheck. Zero came after a large purchase.",
        "Dan Galai and Orly Sade — Hebrew University, 2006 — called this the ostrich effect.",
        "When financial information is likely to be painful, the brain stops seeking it.",
        "Not a choice. A conditioned reflex — built specifically to reduce cortisol.",
        "Every time Alex looked at a bad number, his brain recorded pain.",
        "After enough repetitions, avoidance became automatic.",
        "The Brain Villain does not need to hide the numbers. Alex does it for him.",
        "Trap One generated the spend. Trap Two buried the evidence.",
        "Trap Three provides the explanation.",
    ]),

    # ── CTA ── beats 34-35 = 37% through 93 ✅
    ("CTA", [
        "If your brain is doing this to you right now — subscribe.",
        "We break down a new bias every week. It's free. And it might save you more than you think.",
    ]),

    # ── TRAP 3 ── 12 beats
    ("TRAP 3 — THE EXPERTISE TRAP", [
        "Alex has been studying behavioral finance for eight months.",
        "He knows the vocabulary. Anchoring. Loss aversion. Mental accounting. He can name his biases in real time.",
        "He feels more in control than ever.",
        "His financial decisions have not improved.",
        "Terrance Odean — UC Berkeley — studied 35,000 investor accounts for seven years.",
        "The investors who traded most frequently earned the lowest returns.",
        "Not because trading is wrong. Because confidence had outpaced competence.",
        "Daniel Kahneman documented the same pattern: eighty percent of investors believe they are above average.",
        "Fifty percent are, by definition, wrong.",
        "The Expertise Trap does not require ignorance. It requires the illusion of knowledge.",
        "The more vocabulary Alex acquires, the more certain he feels. The more certain he feels, the less he questions.",
        "Trap Three rewires in one direction only: more vocabulary, more certainty — not more accuracy.",
    ]),

    # ── TRAP 4 ── 11 beats
    ("TRAP 4 — THE NIGHT DRAIN", [
        "It is 10:47 PM. Alex is tired.",
        "He has made decisions since 7 AM — small ones, large ones, a hundred in between.",
        "He opens his phone. He adds something to his cart.",
        "He tells himself he will decide in the morning.",
        "He buys it before he puts the phone down.",
        "Shai Danziger — Ben-Gurion University — studied eight judges over ten months.",
        "Morning parole decisions: granted sixty-five percent of the time.",
        "Late afternoon: eleven percent.",
        "Same judges. Same cases. Same evidence. Different cognitive reserve.",
        "The Brain Villain does not need to be clever at 11 PM. It only needs to wait.",
        "Impulse purchases peak between nine and midnight — not because people want more at night, but because the override mechanism has run out of fuel.",
    ]),

    # ── TRAP 5 ── 11 beats
    ("TRAP 5 — THE UPGRADE LOCK", [
        "Six months ago, Alex upgraded his apartment.",
        "The first eleven days were different. Genuinely better.",
        "Then it became normal.",
        "He is not unhappy. He is not satisfied either. He is calibrated.",
        "Kent Berridge — University of Michigan — spent thirty years separating two distinct systems.",
        "Wanting. And liking.",
        "Wanting is driven by dopamine. It scales with anticipation and exposure.",
        "Liking is driven by opioid circuits. It decreases with repetition.",
        "Every upgrade strengthens wanting. Every upgrade habituates liking.",
        "The floor does not go back. The ceiling keeps moving.",
        "Trap Five is the only one that compounds biologically — not just financially. Alex does not need to buy more. His brain has already decided he cannot want less.",
    ]),

    # ── SYSTEM CLOSE ── 5 beats
    ("SYSTEM CLOSE", [
        "Five programs. Running simultaneously. Without permission.",
        "Program One generates the impulse before the decision exists.",
        "Program Two hides the evidence so it stays invisible.",
        "Program Three provides the vocabulary to feel in control while losing the same way.",
        "Program Four lowers the override at the exact moment it is needed most. Program Five raises the floor so return is no longer possible.",
    ]),

    # ── BRAIN VILLAIN'S LAST TRICK ── 11 beats (template obligatorio)
    ("BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to this list.",
        "You are feeling it right now.",
        "Not denial. Something quieter.",
        "Something that sounds like self-awareness: 'I already knew about most of these.'",
        "That thought is not insight. Not wisdom. Not progress.",
        "It is the Expertise Trap wearing the costume of self-knowledge.",
        "The programs are not broken.",
        "They are perfectly designed for an environment where pattern recognition and immediate reward were survival.",
        "Knowing the name of a predator kept your ancestors alive.",
        "It does not stop the dopamine from firing on Wednesday.",
        "The Brain Villain was built for that world. Not this one.",
    ]),

    # ── IDENTITY CLOSE ── 8 beats (max 9)
    ("IDENTITY CLOSE", [
        "None of this is a character flaw.",
        "Anticipation Burn kept ancestors motivated through scarcity. Balance Blindspot reduced cortisol when debt meant death.",
        "Night Drain preserved cognitive resources. Expertise Trap protected identity in a world where certainty built coalitions.",
        "Upgrade Lock ensured the tribe kept climbing when climbing was survival.",
        "The programs are not broken. They are perfectly designed for an environment that no longer exists.",
        "The Brain Villain was built for that world. Not this one.",
        "The next video maps the one structural decision that shuts down three of these five simultaneously.",
        "If your brain is doing this to you right now — subscribe. We break down a new bias every week. It's free. And it might save you more than you think.",
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

    note = doc.add_paragraph()
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    nr = note.add_run("Hook: S2 — Dato Sin Contexto · S17 Thumbnail Continuity · S18 Rotation ✅")
    nr.font.size = Pt(9); nr.font.color.rgb = RGBColor(0x44, 0x88, 0x44)

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

    path = "/home/user/Claudeeee/V13_v31_SCRIPT.docx"
    doc.save(path)
    print(f"DOCX: {path} | {total} beats | {wc} words | ~{round(wc/140)} min")
    return all_lines, total, wc


def build_pdf(all_lines, total, wc):
    styles = getSampleStyleSheet()
    H1  = ParagraphStyle('H1',  parent=styles['Title'],  fontSize=14, leading=18, alignment=TA_CENTER)
    SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=10, leading=13,
                         alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                         fontName='Helvetica-Bold')
    NOTE= ParagraphStyle('NOTE',parent=styles['Normal'], fontSize=9, leading=12,
                         alignment=TA_CENTER, textColor=colors.HexColor('#448844'))
    META= ParagraphStyle('META',parent=styles['Normal'], fontSize=9, leading=12,
                         alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    SEC = ParagraphStyle('SEC', parent=styles['Normal'], fontSize=10, leading=13,
                         textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                         spaceBefore=14, spaceAfter=4)
    LINE= ParagraphStyle('LINE',parent=styles['Normal'], fontSize=11, leading=17, spaceAfter=1)

    def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

    pdf_path = "/home/user/Claudeeee/V13_v31_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph("Hook: S2 Dato Sin Contexto · S17 Thumbnail Continuity · CTA beats 34-35 = 37%", NOTE),
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

    pdf_path = "/home/user/Claudeeee/V13_v31_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 13 — BRIEF v3.1", SUB),
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
    print(f"\n✅ V13 BRIEF v3.1 — 3 archivos generados")
    print(f"   {total} beats · {wc} words · ~{round(wc/140)} min")
    print(f"   Hook: S2 Dato Sin Contexto ✅")
    print(f"   Beat 1: Thumbnail continuity — '5' on screen ✅")
    print(f"   CTA: beats 34-35 = {round(34/total*100)}% ✅")
    print(f"   t-shirt: BLUE ✅")
