#!/usr/bin/env python3
"""
VIDEO 13 FINAL — 5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)
Aplica fórmula validada por outliers: [Número] + "Brain" + verbo físico + paréntesis conspiración
181× (Outlier A) · 104× (Outlier B) · 36× (Outlier D)

5 trampas distintas de V11 — nuevos científicos, nuevos mecanismos:
  Trap 1: Anticipation Burn (Schultz / Cambridge / dopamine pre-spend)
  Trap 2: Balance Blindspot (Galai & Sade / Hebrew University / ostrich effect)
  Trap 3: Expertise Trap (Odean / UC Berkeley + Kahneman / overconfidence)
  Trap 4: Night Drain (Danziger / Ben-Gurion / ego depletion × time)
  Trap 5: Upgrade Lock (Berridge / Michigan / wanting vs. liking)

104 beats · FINAL version
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

    ("HOOK", [
        "Alex earns more than he did three years ago.",
        "He has less to show for it.",
        "Not because of bad investments.",
        "Not because of unexpected expenses.",
        "Because his brain has been running five programs he was never told about.",
        "Programs that physically alter neural architecture — every month.",
        "The third one gets worse the more financially educated he becomes.",
        "We're going to show you all five.",
        "The order matters. Trap One fires first — and makes everything else possible.",
        "Your brain started running it this week.",
    ]),

    ("TRAP 1 — THE ANTICIPATION BURN", [
        "It is Wednesday afternoon.",
        "Alex hasn't been paid yet. He already knows what he's going to buy.",
        "The jacket. The dinner. The upgrade he's been putting off.",
        "He hasn't made these decisions. His brain made them 48 hours ago.",
        "Wolfram Schultz — neuroscientist at Cambridge University —",
        "won part of the Nobel Prize for discovering this.",
        "Dopamine does not fire when the reward arrives.",
        "It fires when the brain predicts the reward is coming.",
        "By Wednesday, Alex's dopamine peak has already passed.",
        "By Friday — payday — the signal is declining.",
        "His spending on Friday is not a decision. It is a receipt.",
        "The brain spent the money before the salary existed.",
        "This is not a character flaw. It is a mechanism.",
        "It runs in every brain — including the ones that know it runs.",
        "Trap One fires first. Trap Two makes it invisible.",
    ]),

    ("TRAP 2 — THE BALANCE BLINDSPOT", [
        "Saturday morning. Alex does not check his balance.",
        "He will check next week — when things are calmer.",
        "In the last thirty days, Alex checked his balance six times.",
        "All six were after a paycheck arrived. Zero after a large purchase.",
        "Dan Galai and Orly Sade — Hebrew University — documented this pattern in 2006.",
        "They called it the ostrich effect.",
        "When financial information is painful, the brain stops seeking it.",
        "Not a choice — a conditioned reflex, built to reduce cortisol.",
        "Every time Alex looked at a bad number, his brain recorded pain.",
        "After enough repetitions, avoidance became automatic.",
        "The money leaves. Alex doesn't see it leave.",
        "Trap One runs undisturbed. And Trap Three gives it vocabulary.",
    ]),

    ("CTA", [
        "If your brain is running these programs right now — subscribe.",
        "One bias. Every week. It's free. And it might save you more than you think.",
    ]),

    ("TRAP 3 — THE EXPERTISE TRAP", [
        "Alex started reading about personal finance eight months ago.",
        "He knows the vocabulary. He feels more in control than ever.",
        "Terrance Odean — behavioral economist at UC Berkeley — studied this for a decade.",
        "His finding: investors who traded more frequently earned lower returns.",
        "Not because trading is wrong. Because confidence outpaced competence.",
        "Daniel Kahneman documented the same pattern:",
        "eighty percent of investors believe they are above-average investors.",
        "Fifty percent of them are, by definition, wrong.",
        "The expertise trap rewires the brain in a precise direction:",
        "more vocabulary produces more certainty — not more accuracy.",
        "Alex doesn't know less than he did eight months ago.",
        "He knows just enough to feel like he knows enough.",
        "That gap — between certainty and accuracy — is where Trap Three operates.",
    ]),

    ("TRAP 4 — THE NIGHT DRAIN", [
        "It is 10:47pm on a Tuesday.",
        "Alex is tired. He has been making decisions since 7am.",
        "He adds something to his cart. He's not sure he needs it. He buys it.",
        "Shai Danziger — behavioral scientist at Ben-Gurion University —",
        "studied eight judges over ten months.",
        "At the start of the day, parole was granted sixty-five percent of the time.",
        "By late afternoon: eleven percent.",
        "Same judges. Same evidence. Different reserve.",
        "The same depletion curve runs in Alex's financial decisions.",
        "Impulse purchases peak between nine and midnight.",
        "Ego depletion is maximum. Resistance is minimum.",
        "The Brain Villain doesn't need to be clever at 10pm. It only needs to wait.",
    ]),

    ("TRAP 5 — THE UPGRADE LOCK", [
        "Six months ago, Alex upgraded his apartment.",
        "He estimated it would make him happy for at least a year.",
        "He was satisfied for eleven days.",
        "Kent Berridge — neuroscientist at the University of Michigan —",
        "spent thirty years separating two systems that feel like one.",
        "Wanting. And liking.",
        "Wanting is driven by dopamine. It increases with exposure.",
        "Liking is driven by opioid circuits. It decreases with repetition.",
        "Every upgrade strengthens wanting. And habituates liking.",
        "After six months in the better apartment, Alex doesn't enjoy it more.",
        "He needs the next upgrade.",
        "This is not preference. It is neuroplasticity.",
        "The brain has physically downregulated its response to the current level.",
        "The floor cannot go back. The ceiling keeps moving.",
        "Trap Five is the only one that compounds biologically — not just financially.",
    ]),

    ("SYSTEM CLOSE", [
        "Here is what makes these five programs expensive: they do not run independently.",
        "Trap One generates the impulse. Trap Two makes it invisible.",
        "Trap Three gives Alex the vocabulary to justify what he never examines.",
        "Trap Four lowers resistance at exactly the right moment.",
        "Trap Five raises the floor so he cannot return to where he started.",
        "Kahneman and Deaton — Princeton, 2010 — found that behavioral programs consume the same percentage of income at €40,000 as at €140,000. The math adjusts. The programs don't.",
    ]),

    ("BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to identification.",
        "You're feeling it right now.",
        "Not denial. Something quieter.",
        "Something that sounds like rationality: ‘I already know this.’",
        "That thought is not self-awareness. Not wisdom. Not knowledge.",
        "It is the Expertise Trap wearing the costume of insight.",
        "The programs are not broken.",
        "They are perfectly designed for an environment where pattern recognition was survival.",
        "Knowing the name of a predator kept your ancestors alive. It doesn't stop the dopamine.",
        "The Brain Villain was built for that world. Not this one.",
        "The next video shows the one structural decision that shuts down three of the five simultaneously.",
    ]),

    ("IDENTITY CLOSE", [
        "None of this is a character flaw.",
        "Anticipation Burn kept ancestors motivated to hunt. Balance Blindspot reduced cortisol. Night Drain was instinct. Upgrade Lock meant survival.",
        "The programs are not broken.",
        "They are perfectly designed for an environment that no longer exists.",
        "The Brain Villain was built for that world. Not this one.",
        "Naming them doesn't silence them. But it is the first condition for building a system around them.",
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
    r.bold = True
    r.font.size = Pt(14)

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run(LABEL)
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run(TITLE)
    r.bold = True
    r.italic = True
    r.font.size = Pt(15)

    doc.add_paragraph()

    beat_num = 1
    for section_title, lines in SECTIONS:
        if section_title:
            sh = doc.add_paragraph()
            sr = sh.add_run(f"— {section_title} —")
            sr.bold = True
            sr.font.size = Pt(11)
            sr.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)
            sh.paragraph_format.space_before = Pt(14)
            sh.paragraph_format.space_after = Pt(4)

        for line in lines:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            num_run = p.add_run(f"[{beat_num}]  ")
            num_run.bold = True
            num_run.font.size = Pt(9)
            num_run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
            p.add_run(line).font.size = Pt(11)
            beat_num += 1

        doc.add_paragraph()

    all_lines = [line for _, lines in SECTIONS for line in lines]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = beat_num - 1
    minutes = round(word_count / 140)

    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(
        f"TOTAL: {total_beats} beats · ~{word_count} words · ~{minutes} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/V13_final_SCRIPT.docx"
    doc.save(path)
    print(f"DOCX: {path} | {total_beats} beats | {word_count} words | ~{minutes} min")
    return all_lines, total_beats, word_count


def build_pdf(all_lines, total_beats, word_count):
    styles = getSampleStyleSheet()
    H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=15, leading=19, alignment=TA_CENTER)
    SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=10, leading=13,
                          alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                          fontName='Helvetica-Bold')
    META = ParagraphStyle('META', parent=styles['Normal'], fontSize=9,  leading=12,
                          alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    SEC  = ParagraphStyle('SEC',  parent=styles['Normal'], fontSize=10, leading=13,
                          textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                          spaceBefore=14, spaceAfter=4)
    LINE = ParagraphStyle('LINE', parent=styles['Normal'], fontSize=11, leading=17, spaceAfter=1)

    def esc(t):
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    minutes = round(word_count / 140)
    pdf_path = "/home/user/Claudeeee/V13_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)

    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"{LABEL} · {total_beats} beats · ~{word_count} words · ~{minutes} min", META),
        Spacer(1, 14),
    ]

    beat_num = 1
    for section_title, lines in SECTIONS:
        if section_title:
            flow.append(Paragraph(f"— {esc(section_title)} —", SEC))
        for line in lines:
            flow.append(Paragraph(
                f'<font color="#888888"><b>[{beat_num}]</b></font>  {esc(line)}', LINE))
            beat_num += 1
        flow.append(Spacer(1, 8))

    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END · {total_beats} beats · ~{word_count} words · ~{minutes} min", META))

    doc.build(flow)
    print(f"PDF:  {pdf_path} | {total_beats} beats | {word_count} words")


def build_elevenlabs_pdf(all_lines, word_count):
    styles = getSampleStyleSheet()
    H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=15, leading=19, alignment=TA_CENTER)
    SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=10, leading=13,
                          alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                          fontName='Helvetica-Bold')
    META = ParagraphStyle('META', parent=styles['Normal'], fontSize=9,  leading=12,
                          alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    LINE = ParagraphStyle('LINE', parent=styles['Normal'], fontSize=12, leading=19, spaceAfter=3)

    def esc(t):
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    minutes = round(word_count / 140)
    pdf_path = "/home/user/Claudeeee/V13_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)

    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"ELEVENLABS — NARRATION SCRIPT · {len(all_lines)} lines · ~{word_count} words · ~{minutes} min", META),
        Spacer(1, 16),
    ]

    for line in all_lines:
        flow.append(Paragraph(esc(line), LINE))

    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END OF SCRIPT · {len(all_lines)} lines · ~{word_count} words", META))

    doc.build(flow)
    print(f"ELEVENLABS: {pdf_path} | {len(all_lines)} lines | {word_count} words")


if __name__ == "__main__":
    all_lines, total_beats, word_count = build_docx()
    build_pdf(all_lines, total_beats, word_count)
    build_elevenlabs_pdf(all_lines, word_count)
    minutes = round(word_count / 140)
    print(f"\n✅ VIDEO 13 FINAL — 3 documentos generados")
    print(f"   {total_beats} beats · {word_count} words · ~{minutes} min")
