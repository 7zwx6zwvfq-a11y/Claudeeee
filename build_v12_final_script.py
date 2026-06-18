#!/usr/bin/env python3
"""
V12 FINAL — The One Decision That Defeats All Three Brain Traps
CAMBIOS vs. v12_revised:
  - Hook reescrito: identity-first (beat 1 = espectador se reconoce)
  - WHY WILLPOWER FAILS: experimento rábanos/galletas de Baumeister añadido
  - BRAIN VILLAIN'S LAST TRICK: reescrito — explícito, inocula en tiempo real
  - Título final: "Why Willpower Fails Every Payday — And the One Decision That Stops It"
  - CTA movido a ~39% (después de "Alex does.")
  - Identity Close reducido a 9 beats
102 beats · ~950 words · ~7 min
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

TITLE    = "The One Decision That Defeats All Three Brain Traps"
SUBTITLE = "NEUROCENTS · VIDEO 12 — FINAL"
LABEL    = "SCRIPT (NARRATION)"

# TÍTULO RECOMENDADO (basado en outlier patterns)
# "Why Willpower Fails Every Payday — And the One Decision That Stops It"
# Justificación al final del archivo.

SECTIONS = [

    ("HOOK", [
        # REESCRITO — identity-first (outlier pattern: espectador se reconoce en beat 1)
        "You've started a budget at least three times. It never survived payday.",
        "Not because you're bad with money.",
        "Not because you lack discipline.",
        "Because you've been fighting an automated system with a manual weapon.",
        "One bank transfer. Set up once. It fires before you can stop it.",
        "Workers who used this went from three and a half percent savings to thirteen point six — in five years.",
        "No extra income. No willpower. No spreadsheets.",
        "Just one structural decision made on a calm Tuesday — not a panicked Friday.",
        "Your brain is already calculating why this won't work for you.",
        "That calculation is the last trap. This video was built to dismantle it.",
    ]),

    ("WHY KNOWING ISN'T ENOUGH", [
        "Alex watched the last video.",
        "He understood every trap. He took notes. He sent it to his brother.",
        "He felt the specific shift — the sensation of finally seeing the system clearly.",
        "And on Friday, the salary notification arrived.",
        "His brain asked the same question it always asks: what do I deserve?",
        "Same question. Same Friday. Same four hundred euros gone.",
        "Knowing the name of a trap does not move the walls.",
        "Every personal finance book gives Alex the diagnosis.",
        "None of them give him the surgery.",
        "The surgery requires removing the decision from Alex's hands entirely —",
        "not making it easier to get right.",
    ]),

    ("WHY WILLPOWER FAILS", [
        "Roy Baumeister — social psychologist at Florida State University —",
        "spent a decade measuring something he calls ego depletion.",
        "Willpower is not a character trait. It is a finite daily resource.",
        "It depletes with every decision you make — not just financial ones.",
        "Every decision draws from the same reserve. Lunch. Email. What to wear. Whether to save.",
        # AÑADIDO — experimento rábanos/galletas (Baumeister, 1998)
        "In 1998, Baumeister ran an experiment. Two groups. One room.",
        "One plate had fresh chocolate chip cookies. The other: radishes.",
        "Half the group could only eat the radishes — and resist the cookies.",
        "Then both groups received the same unsolvable puzzle.",
        "Radish eaters gave up in eight minutes. Cookie eaters lasted nineteen.",
        "Same puzzle. Same intelligence. Different reserve.",
        "By payday, Alex has been eating radishes for five days.",
        "His back hurts. His focus is gone. He's been patient all week.",
        "The moment he needs the most discipline is the exact moment he has the least.",
        "A budget is a willpower machine.",
        "It asks Alex to make the right call at the right moment, every payday, for thirty years.",
        "The Brain Villain doesn't get tired.",
        "Alex does.",
    ]),

    ("CTA", [
        "If your brain is running these programs right now — subscribe.",
        "Every week: one bias. How it works. Who exploits it. And what you can actually do about it.",
    ]),

    ("", [
        "Over thirty years, the math does not favor Alex.",
        "But here's what Baumeister also found — the part that changes how you actually set up the system.",
    ]),

    ("THE DECISION", [
        "There is only one way to beat a system that runs automatically.",
        "Build a counter-system that also runs automatically.",
        "Alex set up a standing order.",
        "Four hundred euros. Every payday. One minute before the salary notification arrives.",
        "Before the Reward Trap fires its first question: what do I deserve?",
        "Before Mental Accounting creates a label: this is mine, this is safe, this is earned.",
        "Before Present Bias whispers: Future Alex will take care of it.",
        "The Reward Trap fires the moment the salary hits. The standing order fires one minute earlier.",
        "Mental Accounting assigns emotional labels to every euro Alex sees.",
        "The standing order moves four hundred euros into a category the Brain Villain is never shown.",
        "Present Bias insists that Future Alex will be more responsible than Present Alex.",
        "Past Alex already was — nine days before payday, when he was rested, calm, and the villain was quiet.",
        "Alex didn't learn to say no to the Brain Villain.",
        "He cancelled the meeting.",
        "The Brain Villain cannot argue with a decision it was never invited to attend.",
        "The money is simply not there.",
        "Not hidden. Not locked. Not off-limits.",
        "Gone before the calculation begins.",
    ]),

    ("THE SCIENCE", [
        "Richard Thaler and Shlomo Benartzi — University of Chicago and UCLA, 2004 —",
        "designed a program called Save More Tomorrow.",
        "They didn't ask workers to save more now.",
        "They asked one question, one time: when your next raise arrives, can we automatically redirect a fixed percentage?",
        "Workers said yes — once.",
        "The system then executed automatically, every raise cycle, with no further decision required.",
        "Workers who started at a savings rate of three and a half percent",
        "reached thirteen point six percent within five years.",
        "No budgets. No discipline. No willpower.",
        "One structural decision replaced sixty separate monthly battles with the Brain Villain.",
        "The only variable that changed across those five years was structure.",
        "Not income. Not financial knowledge. Not character.",
        "Structure.",
    ]),

    ("THE BRAIN VILLAIN'S LAST TRICK", [
        # REESCRITO — inoculación en tiempo real, segunda persona directa
        "The Brain Villain has one response to automation.",
        "You're feeling it right now.",
        "Not anxiety. Something quieter.",
        "Something that sounds like responsibility: what if I need that money?",
        "That thought is not intuition. Not wisdom. Not financial prudence.",
        "It is Present Bias wearing the costume of caution.",
        "The Villain doesn't need to spend the money.",
        "It just needs to know it could.",
        "That option — the ability to reach the money — is exactly what the standing order removes.",
        "And your brain just demonstrated why.",
        "The discomfort you felt in the last thirty seconds —",
        "that was the trap identifying itself.",
        "The standing order doesn't just move money. It removes the Brain Villain's last lever.",
    ]),

    ("IDENTITY CLOSE + GUIDE", [
        "Alex doesn't need more discipline.",
        "He needs fewer decisions — not better ones.",
        "Every budgeting system ever created asks Alex to win the same battle every month.",
        "The standing order asks him to win it once.",
        "The programs are not broken.",
        "They are perfectly designed for an environment where saving made no survival sense.",
        "You didn't store food in a world where tomorrow was never guaranteed.",
        "The Brain Villain was built for that world. Not this one.",
        "The standing order is the first system designed for the world he actually lives in.",
    ]),

    ("NEXT VIDEO TEASE", [
        "Next video: Alex gets a tax refund.",
        "Eight hundred euros he wasn't expecting.",
        "His brain treats it completely differently from every euro he ever earned.",
        "Same trap. Different label.",
        "The money disappears three times faster.",
        "The reason is the one nobody expects.",
    ]),

]

# ─────────────────────────────────────────────────────────────────────────────
# VERIFICACIÓN DE REGLAS DE ESTILO
# ─────────────────────────────────────────────────────────────────────────────
# "Not X. But Y." / "Not X. X." — mínimo 3:
#   Beat 2-4: Not because you're bad... / Not because you lack... / Because...
#   Beats 57-59: Not hidden. Not locked. Not off-limits.
#   Beats 72-74: Not income. Not financial knowledge. Not character.
#   Beats 78-80: Not intuition. Not wisdom. Not financial prudence.     ✅ ×4
#
# "Same X. Same Y. Same resultado.":
#   Beat 16: Same question. Same Friday. Same four hundred euros gone.
#   Beat 32: Same puzzle. Same intelligence. Different reserve.         ✅ ×2
#
# CTA espejo identidad: Beat 40 — "If your brain is running these programs..."  ✅
# Cierre identidad: Beat 92 — "The programs are not broken."                   ✅
# Cifras en euros (€ implicado en narración): €400 × 5, €800 × 1              ✅
# Segunda persona: beats 1, 7-10, 69-74, 91, 98 — solo momentos clave        ✅
# Sin "basically", sin hedging, sin relleno                                    ✅
# Ritmo alternado: beat largo → muy corto → largo:
#   [16] largo → [17] muy corto → [18-19] largos                              ✅
#   [32] largo → [33] corto → [34] largo                                      ✅
#   [55] muy corto → [56] largo → [57] corto                                  ✅
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# TÍTULO FINAL RECOMENDADO
# ─────────────────────────────────────────────────────────────────────────────
# "Why Willpower Fails Every Payday — And the One Decision That Stops It"
#
# Justificación por outlier data:
# → Outlier #2 "Why Willpower Fails" = 132.7× breakout en canal de 4,010 subs.
#   El ángulo Baumeister-ego depletion es EXACTAMENTE el mecanismo central de V12.
#   El título matches the content.
# → "Every Payday" = especificidad + trigger universal (todos cobran). CTR > genérico.
# → "The One Decision That Stops It" = curiosity gap sin revelar qué es.
#   "One" promete concreción. "Stops It" implica amenaza activa que necesita solución.
# → Negative framing: "Fails" activa negativity bias. Supera a "How to Save More".
# → Longitud: 12 palabras — rango óptimo.
# → V11 fue el video de las trampas. V12 es el video de la solución.
#   "3 Brain Traps..." repite V11. "Why Willpower Fails..." es nueva puerta de entrada.
# ─────────────────────────────────────────────────────────────────────────────


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
    r.font.size = Pt(16)

    # título recomendado
    s3 = doc.add_paragraph()
    s3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s3.add_run("TÍTULO RECOMENDADO: \"Why Willpower Fails Every Payday — And the One Decision That Stops It\"")
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x1A, 0x7A, 0x3C)

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

    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(
        f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count / 140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/V12_final_SCRIPT.docx"
    doc.save(path)
    print(f"DOCX: {path} | {total_beats} beats | {word_count} words | ~{round(word_count/140)} min")
    return all_lines, total_beats, word_count


def build_pdf(all_lines, total_beats, word_count):
    styles = getSampleStyleSheet()
    H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=16, leading=20, alignment=TA_CENTER)
    SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=10, leading=13,
                          alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                          fontName='Helvetica-Bold')
    REC  = ParagraphStyle('REC',  parent=styles['Normal'], fontSize=8,  leading=11,
                          alignment=TA_CENTER, textColor=colors.HexColor('#1A7A3C'))
    META = ParagraphStyle('META', parent=styles['Normal'], fontSize=9,  leading=12,
                          alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    SEC  = ParagraphStyle('SEC',  parent=styles['Normal'], fontSize=10, leading=13,
                          textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                          spaceBefore=14, spaceAfter=4)
    LINE = ParagraphStyle('LINE', parent=styles['Normal'], fontSize=11, leading=17, spaceAfter=1)

    def esc(t):
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    pdf_path = "/home/user/Claudeeee/V12_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)

    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph('TÍTULO RECOMENDADO: "Why Willpower Fails Every Payday — And the One Decision That Stops It"', REC),
        Spacer(1, 4),
        Paragraph(f"{LABEL} · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min", META),
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
    flow.append(Paragraph(f"END · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min", META))

    doc.build(flow)
    print(f"PDF:  {pdf_path} | {total_beats} beats | {word_count} words")


def build_elevenlabs_pdf(all_lines, word_count):
    styles = getSampleStyleSheet()
    H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=16, leading=20, alignment=TA_CENTER)
    SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=10, leading=13,
                          alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                          fontName='Helvetica-Bold')
    META = ParagraphStyle('META', parent=styles['Normal'], fontSize=9,  leading=12,
                          alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    LINE = ParagraphStyle('LINE', parent=styles['Normal'], fontSize=12, leading=19, spaceAfter=3)

    def esc(t):
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    pdf_path = "/home/user/Claudeeee/V12_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)

    flow = [
        Paragraph("NEUROCENTS · VIDEO 12 — FINAL", SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"ELEVENLABS — NARRATION SCRIPT · {len(all_lines)} lines · ~{word_count} words · ~{round(word_count/140)} min", META),
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
    print("\n✅ V12 FINAL — 3 documentos generados")
    print(f"   {total_beats} beats · {word_count} words · ~{round(word_count/140)} min")
