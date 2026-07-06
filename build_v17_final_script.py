#!/usr/bin/env python3
"""
VIDEO 17 — FORMATO COMPARATIVA (patrón 'Real Estate vs Stocks', 1.5M views)
Two People, Same Salary: Why Only One Stops Working at 45
NEUROCENTS · 74 beats · ~1,000 words · ~7.5 min
Formato: 2 — COMPARATIVA (primera vez) · V16 = Catálogo ✅ rotación S20 (no consecutivo)
Hook strategy: S3 — IN MEDIAS RES (escena dual ya ocurriendo) — última vez V9 ✅ rotación S18
Personajes: LEO y MARC — dos personajes nuevos (patrón Jake/Marcus). Alex descansa este vídeo.
CTA at beats 27-28 = 36-38% ✅ — redacción NUEVA
Sin Villain's Last Trick (Formato 2 no lo pide) — sustituido por 'Why Your Brain Picks Leo' +
      FAIRNESS PIVOT (defender al 'perdedor' — patrón outlier: compra confianza de ambos bandos)
REGLA DE INDEPENDENCIA: cero referencias a otros vídeos ✅ · cero solape con V15 (V15 = automatizar
      el ahorro base; V17 = LA REGLA DE LAS SUBIDAS — bank every raise, upgrade every 5 years)

PATRONES OUTLIERS APLICADOS (S24):
- Dos personajes, un solo variable (mismo sueldo/ciudad/cerebro — solo difiere una regla)
- Checkpoints temporales con re-pregunta implícita '¿quién gana AHORA?' (año 1→5→10→15→20)
- Números hiperespecíficos (34.000 · 126.000 · 318.000 · 640.000)
- Sentimientos vs matemáticas ('Leo looks like the one winning' — social proof vs compounding)
- Fairness pivot ('to be fair to Leo: he didn't lose')
- Cierre que devuelve la pregunta al viewer ('which bet are you currently placing?')
- Honestidad: el precio real de la libertad = 'two decades of looking average'

S17: Thumbnail = split dos figuras (Leo con coche/copa vs Marc gris promedio) + a los 45: Leo
     encadenado al escritorio, Marc libre — texto "SAME SALARY." → Beat 1 = los dos recibiendo
     el mismo email de subida, <5 seg.
BEATS VISUALES: casi todo objetos/split-screens/gráficas de dos curvas — Leo y Marc solo cuando
     la emoción lo pide (regla 'Reducir Alex' aplicada a los personajes nuevos).
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

TITLE    = "Two People, Same Salary: Why Only One Stops Working at 45"
SUBTITLE = "NEUROCENTS · VIDEO 17 — COMPARATIVA"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [

    # ── COLD OPEN ── 5 beats — S3 in medias res: la escena ya está ocurriendo
    ("COLD OPEN", [
        "Leo and Marc get the same email, the same minute: 'Congratulations on your raise.'",  # B1  S3 — dual scene
        "Same company. Same salary. Same city. Same rent.",                # B2  fairness compresa
        "Twenty years later, Marc walks into his boss's office and says he's not coming back. He's forty-five.",  # B3  flash-forward
        "Leo — same age, same career — can't afford to say that sentence. Ever.",  # B4  the gap
        "The difference between their lives fits on a napkin. Here's the napkin.",  # B5  the promise
    ]),

    # ── THE FAIR FIGHT ── 5 beats — eliminar objeciones (patrón outlier)
    ("THE FAIR FIGHT", [
        "Let's keep this brutally fair.",                                  # B6
        "Both are twenty-five. Both earn twenty-eight thousand euros. Both live in the same neighborhood.",  # B7
        "No inheritance. No lottery. No crypto miracle. Neither one is smarter.",  # B8
        "Their brains run the same software — same impulses, same weaknesses, same Friday cravings.",  # B9
        "Only one thing will ever separate them. And it hasn't happened yet.",  # B10 tension
    ]),

    # ── YEAR ONE ── 4 beats — indistinguibles
    ("YEAR ONE", [
        "Year one. Both broke by the twenty-eighth of the month.",         # B11
        "Both check their balance with the same face. Both order the same takeaway they can't quite afford.",  # B12 humor reconocible
        "If you met them at a party, you could not tell them apart.",      # B13
        "Then the first raise lands. Two hundred euros more per month. And the experiment begins.",  # B14 the fork
    ]),

    # ── THE SPLIT ── 6 beats — la divergencia (la única variable)
    ("THE SPLIT", [
        "Leo does what raises are for. He upgrades.",                      # B15
        "A better apartment. A few more dinners out. Nothing crazy — he earned this.",  # B16 razonable, no caricatura
        "Marc does something that looks almost identical from the outside: nothing.",  # B17
        "He keeps living on twenty-eight. The extra two hundred goes somewhere he doesn't look at.",  # B18
        "One rule, made once: 'Every raise is invisible. My life upgrades every five years — on purpose, not by drift.'",  # B19 LA REGLA (el napkin)
        "That's the entire napkin. Now watch what it does to twenty years.",  # B20
    ]),

    # ── YEAR FIVE ── 6 beats — checkpoint 1: Leo parece ganar
    ("YEAR FIVE", [
        "Year five. Both have been promoted twice. Both now earn thirty-six thousand.",  # B21
        "Leo's life is visibly better: nicer flat, nicer car, nicer weekends. He looks like the one winning.",  # B22 feelings vs math
        "Marc still lives like a twenty-five-year-old with a better mattress.",  # B23 humor
        "Leo's savings: about four thousand. Leftovers, mostly.",           # B24
        "Marc's invisible account: thirty-four thousand euros. And it has quietly started earning on its own.",  # B25 número específico
        "Nobody claps for Marc. There is nothing to see. That's the point.",  # B26
    ]),

    # ── CTA ── beats 27-28 = 36-38% ✅ — redacción nueva
    ("CTA", [
        "Quick check: if you already know which of these two you are — subscribe.",  # B27
        "Every Thursday we run the numbers your brain prefers not to look at. Free — and cheaper than finding out at fifty.",  # B28
    ]),

    # ── YEAR TEN ── 4 beats — checkpoint 2: el espejismo continúa
    ("YEAR TEN", [
        "Year ten. Thirty-five years old. Both earn forty-five thousand.", # B29
        "From the outside, Leo is still clearly ahead. Better address. Better car. Better photos.",  # B30
        "Marc's account crosses one hundred and twenty-six thousand — invested, compounding, silent.",  # B31
        "And this is the year something crosses over that neither of them notices.",  # B32 curiosity
    ]),

    # ── THE INVISIBLE LINE ── 4 beats — el cruce
    ("THE INVISIBLE LINE", [
        "Marc's money now earns more per year than his first raise did.",  # B33
        "He has two salaries: his — and his money's.",                     # B34 LAPIDARIA
        "The second one never gets tired, never asks for vacation, and grows every single year.",  # B35
        "Leo still has exactly one worker in his life: Leo. And Leo is getting tired.",  # B36
    ]),

    # ── YEAR FIFTEEN ── 5 beats
    ("YEAR FIFTEEN", [
        "Year fifteen. Forty years old. Both earn fifty-five thousand.",   # B37
        "Leo's lifestyle eats fifty-four of it. Total savings: maybe twenty thousand. Still leftovers.",  # B38
        "Marc: three hundred and eighteen thousand. The curve has stopped being polite.",  # B39
        "Same salary. Same promotions. Same office parking lot.",          # B40 repetition pattern
        "One of them is five years away from never needing it again.",     # B41
    ]),

    # ── YEAR TWENTY ── 6 beats — el final de la carrera
    ("YEAR TWENTY", [
        "Year twenty. Both are forty-five. Both earn sixty-two thousand.", # B42
        "Marc's account: six hundred and forty thousand euros. Invested, it now pays his life by itself.",  # B43
        "That is the entire definition of free: your money's salary covers your living costs.",  # B44
        "He can keep working. Or not. Every Monday is now a choice.",      # B45
        "Leo earns exactly the same sixty-two thousand — and needs every cent of it, until further notice.",  # B46
        "Same career. Same talent. Same luck. Twenty years — one rule apart.",  # B47 LAPIDARIA checkpoint
    ]),

    # ── THE NAPKIN ── 5 beats — la regla, escrita
    ("THE NAPKIN", [
        "Here's the napkin, written out.",                                 # B48
        "Live on your first real salary. Bank every raise, automatically, the month it arrives.",  # B49 LA REGLA
        "Upgrade your life once every five years — on purpose, never by drift.",  # B50
        "That's it. No stock picking. No side hustles. No four a.m. routines.",  # B51
        "The math does the heroics. Your only job is to not interrupt it.",  # B52 LAPIDARIA
    ]),

    # ── WHY YOUR BRAIN PICKS LEO ── 6 beats — el giro Neurocents
    ("WHY YOUR BRAIN PICKS LEO", [
        "Now the honest part: your brain wants Leo's path. Badly.",        # B53
        "A raise screams to be felt. New money reads as permission — and spending it is how your brain celebrates.",  # B54
        "An invisible account gives you nothing to show anyone. No photos. No applause. No proof you're winning.",  # B55
        "Leo got twenty years of small, real pleasures. Marc got a number nobody ever saw.",  # B56
        "That's the actual price of freedom: two decades of looking average.",  # B57 LAPIDARIA
        "Most people can't pay it. Not because of math — because of mirrors.",  # B58 LAPIDARIA doble
    ]),

    # ── TO BE FAIR TO LEO ── 4 beats — fairness pivot (patrón outlier)
    ("TO BE FAIR TO LEO", [
        "And to be fair to Leo: he didn't lose.",                          # B59 compra confianza
        "He had the better wine, the better trips, the better twenties and thirties. Those were real.",  # B60
        "Leo's plan only fails if he ever wants to stop. Or if life makes him stop.",  # B61 la sombra
        "That's the bet he placed — without ever knowing he was betting.", # B62 LAPIDARIA
    ]),

    # ── WHICH BET ARE YOU PLACING ── 4 beats — devolver la pregunta (patrón outlier)
    ("WHICH BET ARE YOU PLACING", [
        "So the real question isn't 'who was right.'",                     # B63
        "It's: which bet are you placing right now?",                      # B64
        "Because you're already on one of these two paths — and never having chosen it doesn't pause it.",  # B65
        "The next raise — the very next one — is the fork.",               # B66
    ]),

    # ── CLOSE ── 5 beats
    ("CLOSE — THE DRAWER", [
        "You don't need to redo your financial life tonight.",             # B67
        "You need one rule, ready in a drawer, for the day the email arrives: 'Congratulations on your raise.'",  # B68
        "Decide now what that email is for. Before it comes. Before it feels like permission.",  # B69
        "Marc didn't beat Leo with discipline. He beat him with a decision that was already made.",  # B70 LAPIDARIA
        "The napkin is yours now. Don't lose it.",                         # B71
    ]),

    # ── NEXT VIDEO TEASE ── 3 beats — V18: 7 Signs (banco)
    ("NEXT VIDEO TEASE", [
        "Next week: seven signs your brain picked Leo's path years ago — without asking you.",  # B72
        "You'll count yours. Number four happens at the supermarket.",     # B73
        "See you Thursday.",                                               # B74
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
    nr = note.add_run("Formato 2 Comparativa (patrón 1.5M) · Hook S3 In Medias Res · Leo vs Marc · Checkpoints año 1→5→10→15→20")
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

    path = "/home/user/Claudeeee/V17_final_SCRIPT.docx"
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

    pdf_path = "/home/user/Claudeeee/V17_final_SCRIPT.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph("Formato 2 Comparativa · Hook S3 · CTA beats 27-28 = 37% · Checkpoints temporales · Independencia total", NOTE),
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

    pdf_path = "/home/user/Claudeeee/V17_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm,
                            topMargin=18*mm, bottomMargin=18*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 17 — COMPARATIVA", SUB),
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
    print(f"\n✅ V17 COMPARATIVA — 3 archivos generados")
    print(f"   {total} beats · {wc} words · ~{round(wc/140)} min · dentro de 70-110 ✅")
    print(f"   Formato 2 (Comparativa) — primera vez ✅ | Hook S3 — última vez V9 ✅")
    print(f"   CTA: beats 27-28 = {round(27/total*100)}% ✅")
    print(f"   Checkpoints 1→5→10→15→20 · Números: 34K/126K/318K/640K ✅")
    print(f"   Fairness pivot + 'which bet are you placing' ✅ · Independencia total ✅")
