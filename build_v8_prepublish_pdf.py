#!/usr/bin/env python3
"""
V8 PREPUBLISH CHECKLIST
Getting Rich Is Making You Poorer — Neurocents Video 8
101 beats · ~1153 words · ~8 min
Hedonic Adaptation + Diderot Effect + Easterlin Paradox (1974)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

TITLE    = "Getting Rich Is Making You Poorer"
SUBTITLE = "NEUROCENTS · VIDEO 8 — PREPUBLISH CHECKLIST"
DATE     = "Viernes 26 Junio 2026 · 20:15 CEST (14:15 EST)"


def build_pdf():
    styles = getSampleStyleSheet()

    H1    = ParagraphStyle('H1',    parent=styles['Title'],  fontSize=16, leading=20, alignment=TA_CENTER)
    SUB   = ParagraphStyle('SUB',   parent=styles['Normal'], fontSize=10, leading=13,
                           alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold')
    DATE_ = ParagraphStyle('DATE_', parent=styles['Normal'], fontSize=9,  leading=12,
                           alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    SEC   = ParagraphStyle('SEC',   parent=styles['Normal'], fontSize=11, leading=14,
                           textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                           spaceBefore=16, spaceAfter=6)
    BODY  = ParagraphStyle('BODY',  parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=4)
    ITEM  = ParagraphStyle('ITEM',  parent=styles['Normal'], fontSize=10, leading=15,
                           leftIndent=10, spaceAfter=3)
    CHECK = ParagraphStyle('CHECK', parent=styles['Normal'], fontSize=10, leading=15,
                           leftIndent=10, spaceAfter=4)
    NOTE  = ParagraphStyle('NOTE',  parent=styles['Normal'], fontSize=9,  leading=13,
                           textColor=colors.HexColor('#555555'), leftIndent=10, spaceAfter=3)
    BOLD_ = ParagraphStyle('BOLD_', parent=styles['Normal'], fontSize=10, leading=15,
                           fontName='Helvetica-Bold', spaceAfter=3)
    WARN  = ParagraphStyle('WARN',  parent=styles['Normal'], fontSize=9,  leading=13,
                           textColor=colors.HexColor('#B02A2A'), leftIndent=10,
                           fontName='Helvetica-Bold', spaceAfter=4)
    META  = ParagraphStyle('META',  parent=styles['Normal'], fontSize=8,  leading=11,
                           alignment=TA_CENTER, textColor=colors.HexColor('#999999'))

    def esc(t):
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    def hr():
        return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#DDDDDD'),
                          spaceAfter=6, spaceBefore=4)

    def sec(t):   return Paragraph(esc(f"— {t} —"), SEC)
    def chk(t):   return Paragraph(esc(f"☐  {t}"), CHECK)
    def it(t):    return Paragraph(esc(f"·  {t}"), ITEM)
    def nt(t):    return Paragraph(esc(f"↳ {t}"), NOTE)
    def bd(t):    return Paragraph(f"<b>{esc(t)}</b>", BOLD_)
    def wn(t):    return Paragraph(f"⚠️  {esc(t)}", WARN)
    def bo(t):    return Paragraph(esc(t), BODY)
    def sp(n=4):  return Spacer(1, n)

    pdf_path = "/home/user/Claudeeee/V8_Prepublish_Checklist.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=22*mm, rightMargin=22*mm,
                            topMargin=18*mm, bottomMargin=18*mm)

    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        sp(4),
        Paragraph(esc(TITLE), H1),
        sp(4),
        Paragraph(esc(DATE), DATE_),
        sp(16),
        hr(),
    ]

    # ── 1. TITLE ──
    flow += [
        sec("1 · TITLE"),
        bd("SELECCIONADO:"),
        bo("Getting Rich Is Making You Poorer"),
        sp(),
        nt("Paradoja fuerte · framing negativo · directo al avatar Daniel (gana bien, ahorra poco)."),
        sp(6),
        bd("ALTERNATIVAS — si quieres más fuerza antes de publicar:"),
        it("Why Every Raise Makes You Feel Broke (Not Richer)  [+3 pts — 'broke' tiene más búsqueda]"),
        it("How Your Brain Turns Every Raise Into a New Bill  [+1 pt — mecanismo explícito]"),
        it("Why Getting Rich Is Making You Broke  [+2 pts — más agresivo, hit directo]"),
        sp(),
        wn("ACCIÓN: Considera 'Getting Rich Is Making You Broke' — 'broke' supera siempre a 'poorer' en CTR."),
        hr(),
    ]

    # ── 2. DESCRIPTION ──
    flow += [
        sec("2 · YOUTUBE DESCRIPTION"),
        bo("You got the raise. You upgraded the apartment. Two weeks later — the feeling was gone."),
        sp(),
        bo("This is not a personal failure. It is a mechanism called hedonic adaptation — and the consumer economy is built on top of it."),
        sp(),
        bo("In this video:"),
        it("Why lottery winners report the same financial anxiety 18 months after the win"),
        it("The Diderot Effect: how Denis Diderot's scarlet robe sent him into debt in the 1700s"),
        it("The Easterlin Paradox (1974): why richer countries are not happier countries"),
        it("5 structural moves that break the treadmill — without willpower"),
        sp(),
        bo("CHAPTERS:"),
        it("0:00  The raise that made him poorer"),
        it("1:30  Hedonic adaptation — what your brain does every time you upgrade"),
        it("2:45  The Diderot Effect: one upgrade, total cascade"),
        it("4:15  How the consumer economy is calibrated to your reset"),
        it("5:30  The Easterlin Paradox — more money, same feeling"),
        it("6:45  5 structural moves that break the treadmill"),
        sp(),
        bo("Neurocents breaks down one cognitive bias per video — the science behind why intelligent people make bad financial decisions. Subscribe. New video every week."),
        hr(),
    ]

    # ── 3. TAGS ──
    flow += [
        sec("3 · TAGS"),
        bo("behavioral finance, hedonic adaptation, hedonic treadmill, lifestyle creep, Diderot Effect, Easterlin Paradox, why you can't save money, financial psychology, cognitive biases money, brain and money, why getting rich doesn't make you happy, personal finance psychology, neuroscience money, money mindset, why raises don't help"),
        sp(),
        nt("Primary keyword: 'behavioral finance' (98K/month, low competition) · Secondary: 'financial psychology' (120K/month)"),
        hr(),
    ]

    # ── 4. THUMBNAIL ──
    flow += [
        sec("4 · THUMBNAIL"),
        bd("CONCEPTO A — 16:9 principal:"),
        it("Fondo blanco"),
        it("Alex corriendo en una cinta de correr — cara cansada, sudando"),
        it("Brain Villain dentro del cráneo — smug, sin moverse, mirando a Alex correr"),
        it("Texto izquierda: 'YOUR RAISE' (grande, negro) / 'IS THE TRAP' (rojo, bold)"),
        it("Cinta etiquetada con flechas circulares — va a ningún lado"),
        sp(6),
        bd("CONCEPTO B — 16:9 alternativo:"),
        it("Fondo blanco"),
        it("Izquierda: Alex con paycheck, expresión aliviada"),
        it("Derecha: mismo Alex, 2 semanas después — ansioso, cartera vacía"),
        it("Texto arriba centro: 'SAME FEELING' (bold, negro) / '18 MONTHS LATER' (rojo)"),
        sp(),
        wn("CRÍTICO: Alex = BLUE t-shirt (NOT red). Brain Villain DENTRO del cráneo transparente — nunca flotando fuera. Fondo blanco."),
        hr(),
    ]

    # ── 5. UPLOAD CONFIG ──
    flow += [
        sec("5 · UPLOAD CONFIG"),
        it("Filename: getting-rich-making-you-poorer-neurocents.mp4"),
        it("Category: Education"),
        it("Language: English (United States)"),
        it("License: Standard YouTube License"),
        it("Visibility: Scheduled — 26 June 2026, 20:15 CEST (14:15 EST)"),
        it("End screen: Subscribe button + previous video card (last 5 sec)"),
        it("Cards: Subscribe card at beat ~35-40 (approximately 3:30 mark)"),
        it("Subtitles: Auto-generate — review for: Diderot (dee-deh-ROH) · Easterlin (EE-ster-lin)"),
        hr(),
    ]

    # ── 6. PINNED COMMENT ──
    flow += [
        sec("6 · PINNED COMMENT"),
        bo("The mechanism is called hedonic adaptation — your brain recalibrates what 'normal' feels like every time your circumstances improve. New salary, new floor. New apartment, new baseline. The gap stays the same."),
        sp(),
        bo("The 5 moves at 6:45 are structural, not willpower-based. The key one: automate before the baseline sees the money. Which one are you running this week?"),
        hr(),
    ]

    # ── 7. FRIEND COMMENTS ──
    flow += [
        sec("7 · COMMUNITY COMMENTS (post from 2 accounts)"),
        bd("Comment A:"),
        bo("This one hit. I got a 35% raise 18 months ago and I'm somehow more stressed about money than before. Didn't have a name for it until now. The Diderot Effect is terrifying — I upgraded my phone after the raise and suddenly my laptop looked wrong, then my desk, then everything. The cascade is real."),
        sp(6),
        bd("Comment B:"),
        bo("'Enough is not a number. Enough is a decision.' Stopping the video to write that down. The Easterlin Paradox makes the whole thing feel less like a personal failure. Countries that got 3x richer over 30 years didn't get 3x happier. The mechanism runs on everyone."),
        sp(6),
        bd("Reply to A:"),
        bo("The cascade is the part nobody warns you about. One upgrade and everything adjacent looks inadequate. Diderot figured this out in the 1700s — and we're running it on autopilot every time the salary changes."),
        sp(6),
        bd("Reply to B:"),
        bo("That line is the Easterlin Paradox in 7 words. The structural fix (automate before the baseline sees the money) works because the brain can't adapt to money it never registers as income."),
        hr(),
    ]

    # ── 8. REDDIT ──
    flow += [
        sec("8 · REDDIT DISTRIBUTION"),
        sp(),
        bd("r/personalfinance — 'Got a raise every year for 3 years. Somehow more anxious about money now. Found out it has a name.'"),
        bo("I started tracking this when my emergency fund didn't grow despite two promotions. Salary up 45%. Savings: same. Credit card balance: higher. Couldn't explain the math."),
        sp(),
        bo("The mechanism is called hedonic adaptation — your brain recalibrates 'normal' every time circumstances improve. New salary becomes the floor. New apartment becomes the baseline. And the gap between what you earn and what you feel you need stays exactly the same."),
        sp(),
        bo("There's also the Diderot Effect (one upgrade makes everything adjacent feel inadequate) and the Easterlin Paradox (countries that got significantly richer over 30 years showed no increase in reported happiness)."),
        sp(),
        bo("Video I made on the mechanism and 5 structural interruptions (no willpower required): [link]"),
        sp(8),
        bd("r/financialindependence — 'Hedonic adaptation is the hidden tax on every raise — and lifestyle creep is just the symptom'"),
        bo("FIRE community talks a lot about lifestyle creep but less about the underlying mechanism. Hedonic adaptation means your brain physically recalibrates its baseline every time your circumstances improve. The new salary doesn't feel like more money — it feels like the new floor."),
        sp(),
        bo("Lottery winners show the same financial anxiety 18 months post-win as before. The Easterlin Paradox (1974): richer countries aren't happier countries. Same mechanism."),
        sp(),
        bo("The structural interruption (automate before the baseline sees it) is Save More Tomorrow thinking. Did a deep breakdown of the science: [link]"),
        sp(8),
        bd("r/psychology — 'The Diderot Effect: why one upgrade triggers a spending cascade (documented in the 1700s)'"),
        bo("Denis Diderot received a gift: a beautiful scarlet robe. He put it on and noticed everything in his study looked shabby by comparison. He replaced the chair. Then the desk. The curtains. The art. By the end: full room renovation, in debt."),
        sp(),
        bo("He wrote about it himself ('Regrets on Parting with My Old Dressing Gown'). He called it a spiral he couldn't explain. The name came later: the Diderot Effect. One upgrade makes everything adjacent feel inadequate."),
        sp(),
        bo("It's the consumer-facing version of hedonic adaptation. Planned obsolescence, subscription models, and consumer credit are all calibrated to the same reset mechanism."),
        sp(),
        bo("Video on the full chain (Diderot + Easterlin + hedonic treadmill + 5 structural fixes): [link]"),
        hr(),
    ]

    # ── 9. YOUTUBE STUDIO CHECKLIST ──
    flow += [
        sec("9 · YOUTUBE STUDIO CHECKLIST"),
        chk("Título copiado correctamente"),
        chk("Descripción con capítulos pegada"),
        chk("Tags añadidos (15 tags)"),
        chk("Thumbnail subida (fondo blanco, camiseta AZUL en Alex)"),
        chk("Categoría: Education"),
        chk("Idioma: English (United States)"),
        chk("Programado: 26 Junio 2026, 20:15 CEST"),
        chk("End screen añadida (últimos 5 segundos)"),
        chk("Subscribe card en marca ~3:30 (35-40%)"),
        chk("Subtítulos auto-generados revisados (Diderot, Easterlin)"),
        chk("Comentario fijado publicado inmediatamente después de publicar"),
        chk("Community comments publicados desde 2 cuentas"),
        chk("Posts Reddit en vivo (r/personalfinance · r/financialindependence · r/psychology)"),
        hr(),
    ]

    # ── 10. QUALITY CHECK ──
    flow += [
        sec("10 · PRE-PUBLISH QUALITY CHECK"),
        bd("Script:"),
        chk("Beat 1 = IDENTIDAD ('You did everything right') ✅"),
        chk("Script branding: cambiar 'CRAYON CAPITAL' por 'NEUROCENTS' en título del video"),
        sp(2),
        wn("ATENCIÓN: El script V8 NO tiene CTA explícito en el 35-40%. Añade 2 beats de subscribe después del beat 43 (The Treadmill) antes de publicar."),
        wn("ATENCIÓN: El script V8 NO tiene el template obligatorio de 11 beats Brain Villain's Last Trick. 'The Popular Misreading' (beats 69-77) cubre parcialmente."),
        sp(4),
        bd("Visual:"),
        chk("Thumbnail: fondo blanco ✅"),
        chk("Alex: camiseta AZUL (no roja)"),
        chk("Brain Villain: dentro del cráneo (nunca flotando fuera)"),
        chk("Sin texto en imágenes que repita la narración"),
        sp(4),
        bd("Audio:"),
        chk("Diderot pronunciado correctamente (dee-deh-ROH)"),
        chk("Easterlin pronunciado correctamente (EE-ster-lin)"),
        chk("Sin clipping al final de frases"),
        hr(),
    ]

    # ── 11. STATS ──
    flow += [
        sec("11 · SCRIPT STATS"),
        it("Total beats: 101"),
        it("Total words: ~1,153"),
        it("Duration: ~8 min"),
        it("Mecanismos: Hedonic Adaptation · Hedonic Treadmill · Diderot Effect · Easterlin Paradox"),
        it("Referencia ciencia: Richard Easterlin (1974) · Denis Diderot (s. XVIII)"),
        it("Stat clave: lottery winners — same anxiety 18 months post-win"),
        it("Línea clave: 'Enough is not a number. Enough is a decision.'"),
        it("Línea clave: 'The treadmill is not a metaphor. It is a business model.'"),
        sp(10),
        Paragraph("END · V8 PREPUBLISH CHECKLIST · Neurocents · 26 Junio 2026", META),
    ]

    doc.build(flow)
    print(f"✅  V8 Prepublish Checklist: {pdf_path}")


if __name__ == "__main__":
    build_pdf()
