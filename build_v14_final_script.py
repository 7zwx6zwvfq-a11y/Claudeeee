#!/usr/bin/env python3
"""
VIDEO 14 — BRIEF v3.1 FINAL
5 Things That Drain Your Money Before Payday (No Matter What You Earn)
NEUROCENTS · 95 beats · ~900 words · ~8 min
Hook strategy: S1 — PREGUNTA SIN RESOLVER (Zeigarnik Effect)
S17: Thumbnail → Alex + €0.00 + Brain Villain lit → Beat 1 = pregunta directa al viewer
S18 rotation: V13 used S2 → V14 uses S1 ✅
CTA at beats 36-37 = 38% through 95 ✅
Format: Lista con Ranking (5 → 1) — sector-wide topic — sin datos científicos
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

TITLE    = "5 Things That Drain Your Money Before Payday (No Matter What You Earn)"
SUBTITLE = "NEUROCENTS · VIDEO 14 — BRIEF v3.1"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [

    # ── HOOK ── 8 beats (~25 seg)
    # S1 — PREGUNTA SIN RESOLVER (Zeigarnik Effect)
    # S17: Thumbnail shows Alex + €0.00 balance + Brain Villain lit
    # Beat 1 = pregunta directa. Viewer se reconoce en <5 segundos.
    ("HOOK — PRIMEROS 5 SEGUNDOS", [
        "Why does your money always disappear before payday?",           # B1  S19: pregunta → sentimiento → loop
        "Not sometimes. Every month.",                                   # B2  pattern established
        "It doesn't matter if you earn €2,000 or €6,000.",             # B3  universality
        "Four weeks. Same empty account.",                               # B4  repetition pattern
        "Five things are doing this to you.",                            # B5  promise — list format
        "And number one runs before you even get paid.",                 # B6  curiosity gap
        "Not when you spend it. Before.",                                # B7  contrast beat
        "Here's the list.",                                              # B8  open loop → into list
    ]),

    # ── SETUP ── 4 beats
    ("SETUP", [
        "These aren't budgeting mistakes.",                              # B9
        "They're not discipline failures.",                              # B10
        "They're patterns. And they run automatically.",                 # B11  mechanism
        "Number five is the one everyone knows. And still can't stop.", # B12  hook into ranking
    ]),

    # ── ITEM 5 ── 8 beats
    ("ITEM 5 — THE CARD GAP", [
        "Number five. The Card Gap.",                                    # B13  reveal
        "When you pay with cash, your brain registers loss.",            # B14  mechanism
        "You feel the €40 leave.",                                       # B15  felt experience
        "When you pay with card — tap, done — the pain disappears.",    # B16  contrast
        "Same purchase. Different brain response.",                       # B17  pattern phrase
        "Card users spend 20 to 47% more than cash users.",             # B18  stat
        "Not because they want to. Because the payment doesn't feel like payment.", # B19
        "Your brain is still waiting for the money to actually leave.", # B20  mechanism close
    ]),

    # ── ITEM 4 ── 8 beats
    ("ITEM 4 — THE REWARD DRAIN", [
        "Number four. The Reward Drain.",                                # B21  reveal
        "It's Thursday. You've had a brutal week.",                     # B22  scene
        "Alex has too. Deadlines. A difficult meeting. Late nights.",   # B23  specificity
        "And his brain does something automatic.",                       # B24  mechanism
        "It calculates what he's owed.",                                 # B25  the logic
        "Not the salary. Something extra.",                              # B26  contrast
        "'I worked hard. I deserve this.'",                              # B27  signature phrase
        "That sentence has cost more money than any impulse purchase.", # B28  the real cost
    ]),

    # ── ITEM 3 ── 7 beats
    ("ITEM 3 — THE INVISIBLE DRAIN", [
        "Number three. The Invisible Drain.",                            # B29  reveal
        "Right now, you have at least three subscriptions you've forgotten about.", # B30  direct
        "Apps you haven't opened in four months.",                       # B31
        "Services that auto-renewed in January.",                        # B32
        "Why haven't you cancelled them?",                               # B33  Zeigarnik question
        "Because cancelling requires a decision. And decisions cost energy.", # B34  mechanism
        "Your brain doesn't cancel things. It lets them run.",          # B35  mechanism close
    ]),

    # ── CTA ── beats 36-37 = 38% ✅
    ("CTA", [
        "If your brain is doing this to you right now — subscribe.",
        "We break down a new pattern every week. It's free. And it might save you more than you think.",
    ]),

    # ── ITEM 2 ── 9 beats
    ("ITEM 2 — SOCIAL SPENDING", [
        "Number two. Social Spending.",                                  # B38  reveal
        "You bought something this month for an audience that wasn't watching.", # B39  direct
        "The car that looks good in the parking lot.",                   # B40  example
        "The jacket for the meeting.",                                   # B41  example
        "The upgrade nobody asked for but someone might notice.",        # B42  example
        "Who is that person you're buying for?",                        # B43  Zeigarnik question
        "They don't exist. They're a projection.",                       # B44  reveal
        "The most expensive audience in your life has never spent a single dollar.", # B45
        "They live entirely in your head. And they have expensive taste.", # B46  close
    ]),

    # ── ITEM 1 ── 12 beats
    ("ITEM 1 — THE PRE-SPEND", [
        "Number one. The one nobody names.",                             # B47  build-up
        "The Pre-Spend.",                                                # B48  reveal — one word
        "It's Wednesday. Payday is Friday.",                            # B49  scene
        "Alex hasn't received anything yet.",                            # B50
        "But his brain has already spent it.",                          # B51  the core mechanism
        "Not metaphorically. Neurologically.",                           # B52  elevation
        "The moment you know money is coming — your brain allocates it.", # B53  mechanism
        "The rent. The pending bill. The thing you've been delaying.",  # B54  the logical ones
        "And then — quietly — a few things that feel deserved.",        # B55  the silent add-ons
        "By the time Friday arrives, the money is already gone in your mind.", # B56
        "Friday is just the confirmation.",                              # B57  the reframe
        "You don't spend your salary. You process a transaction your brain closed on Wednesday.", # B58
    ]),

    # ── MECHANISM CONCLUSION ── 5 beats
    ("MECHANISM CONCLUSION", [
        "Five patterns. Running automatically.",                         # B59
        "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.", # B60
        "None of them feel like mistakes when they happen.",             # B61
        "The Card Gap feels convenient.",                                # B62
        "The Reward Drain feels earned. The Social Spend feels reasonable. The Pre-Spend feels like planning.", # B63
    ]),

    # ── THE STRUCTURAL FIX ── 10 beats
    ("THE STRUCTURAL FIX", [
        "The fix isn't 'spend less.'",                                  # B64
        "That's not a system. That's a wish.",                          # B65
        "For the Card Gap: switch one category to cash. Groceries. Restaurants. One category.", # B66
        "You don't need to feel the money leaving everywhere. Just somewhere.", # B67
        "For the Reward Drain: budget it. €80 a month. 'This is my earned money.'", # B68
        "When it's gone, it's gone. The Villain needs a container, not a lecture.", # B69
        "For the Invisible Drain: one audit. Once a year. Not monthly — once.", # B70
        "For Social Spending: one question before every non-essential purchase.", # B71
        "'Who am I buying this for?' If the answer isn't you — pause.", # B72
        "For the Pre-Spend: the salary hits the account. You don't touch it for 24 hours.", # B73
    ]),

    # ── BRAIN VILLAIN'S LAST TRICK ── 11 beats (template obligatorio)
    ("BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to this list.",              # B74
        "You're feeling it right now.",                                  # B75
        "Not resistance. Something quieter.",                            # B76
        "Something that sounds like common sense: 'I already know this.'", # B77
        "That thought is not wisdom. Not self-awareness.",               # B78
        "It is the Invisible Drain wearing the costume of insight.",    # B79
        "The programs are not broken.",                                  # B80
        "They were built for a world where money was physical — coins you could feel, resources you could see leaving.", # B81
        "In that world, the Pre-Spend was planning. The Reward Drain was recovery. The Card Gap didn't exist.", # B82
        "The Brain Villain was built for that world. Not this one.",    # B83
        "These five systems were designed for the world you actually live in.", # B84
    ]),

    # ── IDENTITY CLOSE ── 7 beats (max 9)
    ("IDENTITY CLOSE", [
        "Your money doesn't disappear.",                                 # B85
        "It follows five very predictable routes.",                      # B86
        "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.", # B87
        "Name them. And they lose power.",                               # B88
        "You're not bad with money.",                                    # B89
        "You're running programs that were never designed for a world with direct deposits and one-click payments.", # B90
        "Now you know which five. That's the first thing the Villain didn't want you to have.", # B91
    ]),

    # ── NEXT VIDEO TEASE ── 4 beats
    ("NEXT VIDEO TEASE", [
        "Next week — the one decision that stops all five.",             # B92
        "Not five solutions. One.",                                      # B93
        "Made once. Before the patterns activate.",                      # B94
        "See you Thursday.",                                             # B95
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
    nr = note.add_run("Hook: S1 — Pregunta Sin Resolver · S17 Thumbnail Continuity · S18 Rotation ✅ · Lista con Ranking")
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

    path = "/home/user/Claudeeee/V14_final_SCRIPT.docx"
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

    pdf_path = "/home/user/Claudeeee/V14_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph("Hook: S1 Pregunta Sin Resolver · S17 Thumbnail Continuity · CTA beats 36-37 = 38%", NOTE),
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

    pdf_path = "/home/user/Claudeeee/V14_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 14 — BRIEF v3.1", SUB),
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
    print(f"\n✅ V14 BRIEF v3.1 — 3 archivos generados")
    print(f"   {total} beats · {wc} words · ~{round(wc/140)} min")
    print(f"   Hook: S1 Pregunta Sin Resolver ✅")
    print(f"   Beat 1: Thumbnail continuity — pregunta directa ✅")
    print(f"   CTA: beats 36-37 = 38% ✅")
    print(f"   t-shirt: BLUE ✅")
