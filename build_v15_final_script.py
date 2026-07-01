#!/usr/bin/env python3
"""
VIDEO 15 — BRIEF v3.1 FINAL
Why Smart People Can't Save Money (Do This Once Instead)
NEUROCENTS · 94 beats · ~1,000 words · ~7.5 min
Hook strategy: S4 — AFIRMACION CONTRAINTUITIVA (disonancia en beats 4-6, apertura pregunta S19)
S17: Thumbnail "SMART. STILL BROKE." + Alex con libros finanzas + saldo €140
     → Beat 1 = "You're smart. So why can't you save money?" — misma escena, <5 seg
S18 rotation: V14 used S1 → V15 uses S4 ✅
CTA at beats 37-38 = 39% through 94 ✅
PAGA EL TEASE DE V14: "the one decision that stops all five" — beats 52-58 = payoff anti-5-drains
Ciencia NUEVA: Madrian & Shea (Harvard, 2001) — auto-enrollment 37% → 86%
Diferenciación vs V12: V12 = willpower/ego depletion + Save More Tomorrow.
                       V15 = manual vs automático + defaults + demolición drain por drain.
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

TITLE    = "Why Smart People Can't Save Money (Do This Once Instead)"
SUBTITLE = "NEUROCENTS · VIDEO 15 — BRIEF v3.1"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [

    # ── HOOK ── 10 beats (~30 seg)
    # S4 — AFIRMACION CONTRAINTUITIVA. Apertura en pregunta (S19) que golpea identidad.
    # La disonancia llega en beat 5: "It's because you keep trying."
    # S17: Thumbnail "SMART. STILL BROKE." → Beat 1 = la misma identidad, en pregunta.
    ("HOOK — PRIMEROS 5 SEGUNDOS", [
        "You're smart. So why can't you save money?",                     # B1  S19: pregunta → identidad → loop
        "You've read the books. You understand compound interest. You could explain inflation at a dinner party.",  # B2  identity build — Daniel exacto
        "And your savings account has €140 in it.",                       # B3  the receipt — número específico
        "Here's the uncomfortable part: it's not because you lack discipline.",  # B4  eliminate false cause
        "It's because you keep trying.",                                  # B5  THE TWIST — disonancia S4
        "Trying is manual. And manual always loses to automatic.",        # B6  mechanism in one line
        "Every drain on your money runs automatically. Your defense runs on willpower.",  # B7  the asymmetry
        "That's not a fair fight. It was never a fair fight.",            # B8  repetition pattern
        "One decision ends it. Made once. On a calm morning.",            # B9  PROMISE — paga tease V14
        "Your brain is already listing reasons this won't work. Good. That's the part we dismantle last.",  # B10 VILLAIN ACTIVE + OPEN LOOP
    ]),

    # ── WHY THE COMMON SOLUTION FAILS ── 10 beats
    # Alex lo intentó todo. Cada método murió igual: fade silencioso, no crash.
    ("WHY THE COMMON SOLUTION FAILS", [
        "Alex has tried everything. Watch.",                              # B11 cinematic setup
        "January: a budgeting app. Every expense categorized. Color-coded.",  # B12
        "It lasted nineteen days.",                                       # B13 short beat — the fade
        "March: a no-spend month. He made it to day twelve.",             # B14
        "June: the 50/30/20 rule. The spreadsheet was beautiful.",        # B15
        "The spreadsheet is still beautiful. It just doesn't match reality anymore.",  # B16 irony beat
        "Every method failed the same way. Not with a crash — with a quiet fade.",  # B17
        "Because every method had the same flaw.",                        # B18
        "They all required Alex to make the right decision. Every day. Forever.",  # B19 the flaw named
        "About a hundred and fifty money decisions a month. And he had to win all of them.",  # B20 the impossible math
    ]),

    # ── THE MECHANISM ── 16 beats
    # Manual vs automático. Por qué ser listo no ayuda. Puente a los 5 drains (V14).
    ("THE MECHANISM", [
        "Saying no to a purchase saves money exactly once.",              # B21
        "And you get no points for the nos.",                             # B22
        "Thirty correct nos. One tired yes. The yes wins.",               # B23 the brutal math
        "Now remember the five drains.",                                  # B24 V14 bridge
        "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",  # B25 continuity
        "If you haven't seen that video, it's the one right before this. One detail matters here:",  # B26 cold-viewer rescue
        "All five run automatically. Zero effort. Zero decisions. Zero fatigue.",  # B27
        "The Card Gap doesn't get tired. The Pre-Spend doesn't take weekends off.",  # B28
        "Your drains are machines. Your savings plan is a to-do list.",   # B29 THE frame
        "Machines beat to-do lists. Every time. In every brain.",         # B30
        "This isn't laziness. This is arithmetic.",                       # B31 elevation device (variante)
        "And this is why being smart doesn't help.",                      # B32 title payoff
        "Intelligence improves each decision. It doesn't reduce how many you have to make.",  # B33 the insight
        "A smarter driver still gets tired on a ten-hour drive.",         # B34 analogy
        "So the real question was never: how do I make better money decisions?",  # B35
        "It's: how do I need fewer? Ideally — zero.",                     # B36 pivot question
    ]),

    # ── CTA ── beats 37-38 = 39% ✅
    ("CTA", [
        "If your brain is doing this to you right now — subscribe.",      # B37
        "We break down a new pattern every week. It's free. And it might save you more than you think.",  # B38
    ]),

    # ── MECHANISM CONCLUSION ── 3 beats
    ("MECHANISM CONCLUSION", [
        "So here's the pivot: stop trying to save money.",                # B39 the scandalous line
        "Trying is the strategy that's been failing for years.",          # B40
        "Replace trying with something that doesn't need you.",           # B41 curiosity gap → solution
    ]),

    # ── THE DECISION ── 17 beats
    # La decisión + demolición drain por drain (payoff del tease V14).
    ("THE DECISION", [
        "The one decision.",                                              # B42 two words — reveal
        "The morning your salary arrives, a fixed amount leaves your account. Automatically.",  # B43
        "Before you see it. Before anything can be calculated about it.", # B44
        "A standing transfer. Set up once. Ten minutes on a calm Sunday.",  # B45 specificity
        "Not at the end of the month. There is no end of the month — you've seen your balance.",  # B46 dark humor
        "Hour zero. The morning it lands.",                               # B47
        "Where does it go? A separate account. Different bank. No card attached.",  # B48
        "If reaching the money takes three days and two passwords, your 11 PM brain can't touch it.",  # B49 friction by design
        "How much? Smaller than feels impressive. €100. Even €50.",       # B50
        "The amount is not the point. The automation is the point. You can raise it later.",  # B51
        "Now watch what one transfer does to all five drains.",           # B52 V14 PAYOFF begins
        "The Card Gap: you can't tap money that isn't in the account.",   # B53 drain 5 down
        "The Reward Drain calculates what you deserve from the balance it sees. That balance just got smaller.",  # B54 drain 4 down
        "The Invisible Drain keeps running — but it drains the leftovers now, not your future.",  # B55 drain 3 down (honest)
        "Social Spending: the ghost audience can't order from an account they can't see.",  # B56 drain 2 down
        "And the Pre-Spend? It still runs. Your brain still allocates everything in advance.",  # B57 drain 1 — the twist
        "But the first allocation already happened. You made it months ago. On purpose. You didn't stop the Pre-Spend — you got there first.",  # B58 THE LINE of the video
    ]),

    # ── THE SCIENCE ── 12 beats
    # Madrian & Shea 2001 — auto-enrollment. NUEVA ciencia, formato experimento canónico.
    ("THE SCIENCE", [
        "This is the most replicated finding in savings research. Not a hack. A law.",  # B59
        "Madrian and Shea. Harvard. 2001.",                               # B60 name — institution — year
        "They studied one company that changed one thing about its retirement plan.",  # B61 setup
        "Before: joining required a decision. A form. An enrollment meeting.",  # B62
        "Thirty-seven percent of employees were saving.",                 # B63 number 1
        "After: everyone was enrolled by default. Same plan. Same money. Leaving took one form.",  # B64
        "Eighty-six percent.",                                            # B65 number 2 — short beat
        "Thirty-seven to eighty-six. No raise. No bonus. No motivational seminar.",  # B66
        "Nobody became more disciplined that year.",                      # B67 interpretation
        "The decision moved from 'every payday, forever' to 'once.'",     # B68 the mechanism
        "Defaults beat decisions. In every study since. In every country it's been tested.",  # B69
        "You can't join their plan. But the transfer copies the mechanism exactly.",  # B70 bridge to viewer
    ]),

    # ── BRAIN VILLAIN'S LAST TRICK ── 11 beats (template obligatorio)
    # La objeción: "What if I need that money?" = el Pre-Spend defendiendo su territorio.
    ("BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to this transfer.",           # B71
        "You're feeling it right now.",                                   # B72
        "Not doubt. Something quieter.",                                  # B73
        "Something that sounds like prudence: 'What if I need that money?'",  # B74
        "That thought is not caution. Not planning. Not flexibility.",    # B75
        "It is the Pre-Spend defending its territory — wearing the costume of prudence.",  # B76 continuity kill
        "The programs are not broken.",                                   # B77
        "They were built for a world where every resource had to stay within arm's reach — where an unexpected winter could end you.",  # B78
        "In that world, locking food away from yourself was madness.",    # B79
        "The Brain Villain was built for that world. Not this one.",      # B80
        "The transfer is the first system designed for the world you actually live in — where the threat isn't winter. It's you, on a Tuesday night, with a phone.",  # B81
    ]),

    # ── IDENTITY CLOSE ── 8 beats (max 9)
    ("IDENTITY CLOSE", [
        "You were never bad at saving.",                                  # B82
        "You were playing a manual game against automatic opponents.",    # B83
        "Smart never mattered. Tired always did.",                        # B84
        "One transfer. Set up once. It doesn't need your motivation, your mood, or your Monday.",  # B85
        "It runs while you sleep. It runs on your worst week. It runs.",  # B86 rhythm close
        "Six months from now you'll open that account and feel something unfamiliar.",  # B87
        "Not pride. Evidence.",                                           # B88 short beat
        "Evidence that your brain was never the enemy — it just needed one decision it couldn't argue with.",  # B89
    ]),

    # ── NEXT VIDEO TEASE ── 5 beats — V16: Formato 3 (Señales/Síntomas)
    ("NEXT VIDEO TEASE", [
        "Next week: seven signs your brain is already wired to stay broke.",  # B90
        "Not habits. Signs. Things you do without noticing you do them.",  # B91
        "Number four happens in the supermarket. You probably did it this week.",  # B92
        "If you recognize three or more, that video is going to be uncomfortable.",  # B93
        "See you Thursday.",                                              # B94
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
    nr = note.add_run("Hook: S4 — Afirmación Contraintuitiva · S17 Thumbnail Continuity · S18 Rotation ✅ · Paga tease V14")
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

    path = "/home/user/Claudeeee/V15_final_SCRIPT.docx"
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

    pdf_path = "/home/user/Claudeeee/V15_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph("Hook: S4 Afirmación Contraintuitiva · S17 Thumbnail Continuity · CTA beats 37-38 = 39% · Paga tease V14", NOTE),
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

    pdf_path = "/home/user/Claudeeee/V15_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 15 — BRIEF v3.1", SUB),
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
    print(f"\n✅ V15 BRIEF v3.1 — 3 archivos generados")
    print(f"   {total} beats · {wc} words · ~{round(wc/140)} min")
    print(f"   Hook: S4 Afirmación Contraintuitiva ✅")
    print(f"   Beat 1: Thumbnail continuity — 'You're smart. So why can't you save money?' ✅")
    print(f"   CTA: beats 37-38 = {round(37/total*100)}% ✅")
    print(f"   Paga tease V14: beats 52-58 (demolición 5 drains) ✅")
    print(f"   Ciencia nueva: Madrian & Shea 2001 (37% → 86%) ✅")
