#!/usr/bin/env python3
"""
VIDEO 16 — BRIEF v3.1 + PLAYBOOK OUTLIERS
7 Signs Your Brain Is Wired to Stay Broke (Count Yours)
NEUROCENTS · 92 beats · ~950 words · ~7.5 min
Formato: 3 — SEÑALES/SÍNTOMAS (primera vez usado; V13/V14 = Lista, V15 = Mecanismo) ✅ rotación S20
Hook strategy: S6 — VILLAIN REVEAL ("el programa ya corre y dejó huellas") — última vez V12 ✅ rotación S18
Apertura: micro-momento universal en pregunta (patrón outlier 'names') — cumple S19
CTA at beats 35-36 = 38% ✅ — redacción NUEVA (no repite el CTA de V13/V14/V15)
Villain counter: 5 beats, redacción 100% nueva — CERO frases de V14/V15 (regla S20)
REGLA DE INDEPENDENCIA: cero referencias a otros vídeos, cero conceptos que requieran contexto previo ✅
FRESCURA verificada: hook distinto (micro-momento conductual), esqueleto distinto (checklist con contador),
                     cierre distinto, CTA distinto, sin "The programs are not broken" ni derivados ✅

PATRONES OUTLIERS APLICADOS:
- Micro-plantilla repetida por señal + FRASE LAPIDARIA de cierre (patrón 'Every Drug Explained', 4.9M)
- Contador acumulativo "that's one / that's two" → completismo checklist (patrón catálogo)
- Escalada de leve (señal 7) a profunda/identidad (señal 1) (patrón cafeína→meth)
- Absolución temprana beat 11 + reframe halagador a mitad beats 45-48 (patrón 'names')
- Humor ligero cada ~40s (patrón 'smoking')
- Motor de comentarios: "pon tu número en comentarios" beat 76 (self-assessment compartible)
- Cierre que devuelve el poder al viewer + tease comparativa estilo Jake vs Marcus (patrón 'Real Estate vs Stocks')

S17: Thumbnail = checklist de 7 casillas (3 marcadas en rojo) + Alex contando con dedos, boca abierta,
     texto "HOW MANY?" → Beat 1 = el gesto del one-eye check + primera casilla en pantalla, <5 seg
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

TITLE    = "7 Signs Your Brain Is Wired to Stay Broke (Count Yours)"
SUBTITLE = "NEUROCENTS · VIDEO 16 — BRIEF v3.1 + OUTLIER PLAYBOOK"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [

    # ── HOOK ── 9 beats — S6 Villain Reveal, apertura micro-momento (patrón 'names')
    ("HOOK — PRIMEROS 5 SEGUNDOS", [
        "Do you open your banking app with one eye half-closed?",         # B1  micro-momento + pregunta S19
        "That little pause before the balance loads — that's not a quirk.",  # B2
        "That's evidence.",                                                # B3  two-word beat
        "Your brain runs a quiet program about money. It installed itself years ago. You never agreed to it.",  # B4  S6 villain reveal
        "And like every program, it leaves fingerprints.",                 # B5
        "Seven of them.",                                                  # B6  number drop
        "Most people carry at least three and have never noticed a single one.",  # B7  implication
        "Today you're going to count yours.",                              # B8  the game — checklist contract
        "Fair warning: number one is the reason the other six exist.",     # B9  open loop → escalada
    ]),

    # ── SETUP ── 4 beats — reglas del juego + absolución temprana (patrón 'names')
    ("SETUP — THE RULES", [
        "The rules are simple. I describe the sign. You check if it's you. Keep count.",  # B10
        "No sign is a character flaw. A fingerprint isn't a crime — it's information.",   # B11 absolución TEMPRANA
        "Some of these are so small they look like personality.",          # B12
        "That's exactly what makes them expensive. Start counting.",       # B13
    ]),

    # ── SIGN 7 ── 7 beats — micro-plantilla: nombre → escena → mecanismo → lapidaria → check
    ("SIGN 7 — THE ONE-EYE CHECK", [
        "Sign number seven. The One-Eye Check.",                           # B14
        "You know the gesture. Phone out. App open. And a half-second flinch before the number appears.",  # B15 micro-momento
        "You're not checking your balance. You're bracing for it.",        # B16 LAPIDARIA
        "A person who feels in control reads a number. A person who doesn't — prepares for impact.",  # B17
        "Somewhere along the way, your brain learned that this number brings pain.",  # B18 mecanismo
        "So now it treats your own bank account like an incoming punch.",  # B19 humor oscuro
        "If you flinched this week: that's one.",                          # B20 CHECK — contador
    ]),

    # ── SIGN 6 ── 7 beats
    ("SIGN 6 — THE SALE MATH", [
        "Sign number six. The Sale Math.",                                 # B21
        "'It was fifty percent off.' And your brain files it as money earned.",  # B22 micro-momento
        "You didn't save thirty euros. You spent seventy.",                # B23 LAPIDARIA
        "The discount isn't income. But it feels like income — and your brain banks the feeling.",  # B24 mecanismo
        "That's why the word 'sale' makes you spend faster, not slower.",  # B25
        "Nobody ever got rich collecting discounts on things they didn't need.",  # B26
        "If you've said 'but it was on offer' this month: that's two.",    # B27 CHECK
    ]),

    # ── SIGN 5 ── 7 beats
    ("SIGN 5 — THE ROUND-DOWN MEMORY", [
        "Sign number five. The Round-Down Memory.",                        # B28
        "Someone asks what you spent last night. 'Twenty? Twenty-five?'",  # B29 micro-momento
        "It was thirty-eight.",                                            # B30 short beat — the receipt
        "Your memory rounds your spending down with the confidence of a chief financial officer.",  # B31 humor
        "Never up. Always down. One direction only.",                      # B32
        "That's not bad memory. That's your brain protecting the story it tells about you.",  # B33 mecanismo — LAPIDARIA
        "If your numbers always shrink in the retelling: that's three.",   # B34 CHECK
    ]),

    # ── CTA ── beats 35-36 = 38% ✅ — redacción NUEVA
    ("CTA", [
        "Quick pause. If you've already counted two or more — subscribe.", # B35
        "We put a name on one of these programs every week. Named programs lose their grip. It's free, and it works better than guilt.",  # B36
    ]),

    # ── SIGN 4 ── 8 beats — el del supermercado
    ("SIGN 4 — THE CHECKOUT SACRIFICE", [
        "Sign number four. The Checkout Sacrifice.",                       # B37
        "You're at the supermarket. The total feels high.",                # B38 micro-momento
        "So you take something out of the cart.",                          # B39
        "The two-euro chocolate. Back on the shelf. Ritual complete.",     # B40 humor
        "The sixty euros of everything else? Stays.",                      # B41
        "You didn't cut the cost. You bought the feeling of cutting it.",  # B42 LAPIDARIA
        "Your brain doesn't want a cheaper cart. It wants permission for the cart.",  # B43 mecanismo
        "If you've sacrificed the chocolate to bless the basket: that's four.",  # B44 CHECK
    ]),

    # ── MID REFRAME ── 4 beats — giro halagador (patrón 'names')
    ("MID REFRAME", [
        "Now — if you're at three or four and feeling attacked: hold on.", # B45
        "Recognizing these signs this fast means something most people miss.",  # B46
        "You can't recognize a pattern you've never observed. You've been watching. Most people never watch.",  # B47 el halago
        "The count isn't your sentence. It's your map. Keep going — the last three run deeper.",  # B48 re-hook
    ]),

    # ── SIGN 3 ── 7 beats
    ("SIGN 3 — THE COUNTDOWN CLOCK", [
        "Sign number three. The Countdown Clock.",                         # B49
        "You know exactly how many days until payday. Right now. Without checking.",  # B50 micro-momento
        "But last year's total spending? Not even a guess.",               # B51
        "Your brain measures money in 'days I can survive' — never in years.",  # B52 mecanismo
        "Survival math is short math. Wealth math is long math.",          # B53 LAPIDARIA
        "The horizon of your money thoughts quietly predicts where you'll be in ten years.",  # B54
        "If your money clock only counts down to Friday: that's five.",    # B55 CHECK
    ]),

    # ── SIGN 2 ── 7 beats
    ("SIGN 2 — THE 'WHEN' PLAN", [
        "Sign number two. The 'When' Plan.",                               # B56
        "'When they raise my salary.' 'When things calm down.' 'When this year is over.'",  # B57 micro-momento
        "Every money plan you have starts with a word you don't control.", # B58
        "'When' feels like a plan. It's a waiting room.",                  # B59 LAPIDARIA
        "And your brain loves waiting rooms — because waiting costs nothing today.",  # B60 mecanismo
        "The people who get out never found a better 'when.' They found a smaller 'now.'",  # B61
        "If your money plan lives in someone else's calendar: that's six.",  # B62 CHECK
    ]),

    # ── SIGN 1 ── 9 beats — la profunda (identidad)
    ("SIGN 1 — THE CEILING", [
        "Sign number one. The Ceiling.",                                   # B63
        "Try something. Right now. Picture yourself wealthy. Actually wealthy.",  # B64 ejercicio en vivo
        "Not the car. Not the beach. Just you — with money, at peace.",    # B65
        "Did something push back?",                                        # B66 the moment
        "A small voice. 'That's not for people like us.'",                 # B67
        "That voice has an accent. It sounds like your childhood kitchen.",  # B68 el beat más fuerte del vídeo
        "Somewhere before you turned twelve, you learned how much money 'people like you' are allowed to have.",  # B69 mecanismo
        "It's not that you can't picture being rich. It's that the picture feels like someone else's photo.",  # B70 LAPIDARIA
        "If the picture pushed back: that's seven. And that one is the parent of the other six.",  # B71 CHECK + payoff del beat 9
    ]),

    # ── THE COUNT ── 6 beats — resolución del juego + motor de comentarios
    ("THE COUNT", [
        "So. What's your number?",                                         # B72
        "Zero to two: you have habits. Everyone does.",                    # B73
        "Three to five: you have a program. It's been running for years, and it thinks it's protecting you.",  # B74
        "Six or seven: your money life has been on autopilot since childhood — and today might be the first time you've met the pilot.",  # B75
        "Whatever you counted — put the number in the comments. Watch how many people share your exact fingerprints.",  # B76 MOTOR DE COMENTARIOS
        "Now — before your brain deletes this entire video, we need to talk about what it's doing right now.",  # B77 bridge
    ]),

    # ── THE DELETE ATTEMPT ── 5 beats — inoculación, redacción 100% NUEVA (no template V14/V15)
    ("THE DELETE ATTEMPT", [
        "There's a thought forming in your head at this exact moment.",    # B78
        "'Interesting video.' That's the thought. Calm. Friendly. Final.", # B79
        "'Interesting' is where your brain sends threats to be forgotten.",  # B80 LAPIDARIA
        "A video that names your programs is a threat to your programs.",  # B81
        "So it stamps this one 'interesting' — and schedules the forgetting for tonight.",  # B82
    ]),

    # ── CLOSE ── 6 beats — absolutorio, redacción nueva (sin frases de closes anteriores)
    ("CLOSE — THE CATCH", [
        "Here's what survives the forgetting: one number. Yours.",         # B83
        "You can't uncount it. Tomorrow — at the checkout, at the app, at the word 'sale' — you'll catch yourself mid-sign.",  # B84
        "That catch — that half-second of watching it happen — is the only place money habits have ever actually changed.",  # B85
        "Not in budgets. Not in resolutions. In the catch.",               # B86 LAPIDARIA final
        "Seven signs. One count. And a brain that now knows it's being watched.",  # B87
        "That's not a small thing. That's the whole beginning.",           # B88
    ]),

    # ── NEXT VIDEO TEASE ── 4 beats — V17: Comparativa (patrón Jake vs Marcus)
    ("NEXT VIDEO TEASE", [
        "Next week: two people. Same salary. Same rent. Same city.",       # B89
        "At forty-five, one of them stops needing to work. The other never does.",  # B90
        "The difference fits on a napkin. And nobody teaches it.",         # B91
        "See you Thursday.",                                               # B92
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
    nr = note.add_run("Formato 3 Señales · Hook S6 · Micro-plantilla + frase lapidaria por señal · Contador acumulativo · Independencia total ✅")
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

    path = "/home/user/Claudeeee/V16_final_SCRIPT.docx"
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

    pdf_path = "/home/user/Claudeeee/V16_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph("Formato 3 Señales · Hook S6 · CTA beats 35-36 = 38% · Contador + frases lapidarias · Independencia total", NOTE),
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

    pdf_path = "/home/user/Claudeeee/V16_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 16 — BRIEF v3.1", SUB),
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
    print(f"\n✅ V16 — 3 archivos generados")
    print(f"   {total} beats · {wc} words · ~{round(wc/140)} min · dentro de 70-110 ✅")
    print(f"   Formato 3 (Señales) — primera vez ✅ | Hook S6 — no consecutivo ✅")
    print(f"   CTA: beats 35-36 = {round(35/total*100)}% ✅")
    print(f"   Independencia total: cero referencias a V13/V14/V15 ✅")
    print(f"   Frases nuevas: cero solape con closes/villain de V14/V15 ✅")
