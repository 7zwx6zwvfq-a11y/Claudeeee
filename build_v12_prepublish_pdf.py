#!/usr/bin/env python3
"""V12 Pre-publish Checklist — PDF version via reportlab."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether

RED   = colors.HexColor('#B02A2A')
DARK  = colors.HexColor('#2C3E50')
GREY  = colors.HexColor('#777777')
GREEN = colors.HexColor('#1A7A3C')
LGREY = colors.HexColor('#CCCCCC')

styles = getSampleStyleSheet()

TITLE_S = ParagraphStyle('TitleS', parent=styles['Title'],
                         fontSize=13, leading=17, alignment=TA_CENTER,
                         textColor=RED, spaceAfter=3)
SUB_S   = ParagraphStyle('SubS', parent=styles['Normal'],
                         fontSize=9, leading=12, alignment=TA_CENTER,
                         textColor=GREY, spaceAfter=8)
SEC_S   = ParagraphStyle('SecS', parent=styles['Normal'],
                         fontSize=11, leading=14, fontName='Helvetica-Bold',
                         textColor=RED, spaceBefore=12, spaceAfter=4)
LBL_S   = ParagraphStyle('LblS', parent=styles['Normal'],
                         fontSize=9, leading=12, spaceAfter=2)
BODY_S  = ParagraphStyle('BodyS', parent=styles['Normal'],
                         fontSize=9, leading=12, leftIndent=5*mm, spaceAfter=2)
NOTE_S  = ParagraphStyle('NoteS', parent=styles['Normal'],
                         fontSize=8, leading=11, leftIndent=5*mm,
                         textColor=GREY, spaceAfter=2)
WARN_S  = ParagraphStyle('WarnS', parent=styles['Normal'],
                         fontSize=8, leading=11, leftIndent=5*mm,
                         textColor=RED, spaceAfter=2)
GRNS    = ParagraphStyle('GrnS', parent=styles['Normal'],
                         fontSize=8, leading=11, leftIndent=5*mm,
                         textColor=GREEN, spaceAfter=2)
CB_S    = ParagraphStyle('CbS', parent=styles['Normal'],
                         fontSize=10, leading=13, leftIndent=8*mm, spaceAfter=3)
CODE_S  = ParagraphStyle('CodeS', parent=styles['Normal'],
                         fontSize=9, leading=13, leftIndent=5*mm,
                         textColor=DARK, spaceAfter=4)
BIG_S   = ParagraphStyle('BigS', parent=styles['Normal'],
                         fontSize=12, leading=15, leftIndent=5*mm,
                         fontName='Helvetica-Bold', textColor=DARK, spaceAfter=3)
KW_S    = ParagraphStyle('KwS', parent=styles['Normal'],
                         fontSize=8, leading=11, leftIndent=5*mm,
                         fontName='Courier', textColor=DARK, spaceAfter=1)
FOOT_S  = ParagraphStyle('FootS', parent=styles['Normal'],
                         fontSize=8, leading=11, alignment=TA_CENTER,
                         textColor=GREY)


def sec(title):
    return Paragraph(f"── {title} ──", SEC_S)

def lv(label, value, color=DARK, size=None):
    sz = f' size="{size}"' if size else ''
    return Paragraph(
        f'<font color="{GREY}" size="9"><b>{label}:</b>  </font>'
        f'<font color="#{color.hexval()[2:]}"{sz}>{value}</font>', LBL_S)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=LGREY,
                      spaceBefore=6, spaceAfter=3)

def cb(text):
    return Paragraph(f"☐  {text}", CB_S)

def note(text):
    return Paragraph(text, NOTE_S)

def warn(text):
    return Paragraph(f"⚠ {text}", WARN_S)

def grn(text):
    return Paragraph(text, GRNS)

def body(text):
    return Paragraph(text, BODY_S)

def sp(h=4):
    return Spacer(1, h*mm)


flow = []

# HEADER
flow += [
    Paragraph("NEUROCENTS — VIDEO 12 FINAL · PRE-PUBLISH CHECKLIST", TITLE_S),
    Paragraph("Why Willpower Fails Every Payday · Baumeister Ego Depletion · Thaler &amp; Benartzi · Save More Tomorrow", SUB_S),
    hr(),
]

# 1. FILENAME
flow += [
    sec("1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir"),
    lv("ARCHIVO", "why-willpower-fails-every-payday-automatic-savings-neurocents.mp4", GREEN),
    hr(),
]

# 2. TÍTULO
flow += [
    sec("2. TÍTULO — testear en VidIQ antes de publicar"),
    lv("TÍTULO PRINCIPAL (outlier-validated)",
       "Why Willpower Fails Every Payday — And the One Decision That Stops It", DARK),
    grn("Justificación: 132.7× outlier pattern. 'Why [X] Fails Every [Trigger]' — identidad + mecanismo + solución en 12 palabras."),
    note("Alternativa A: 'The One Decision That Defeats All Three Brain Traps' — mecanismo-first, menor CTR"),
    note("Alternativa B: 'Why Your Brain Spends Every Payday (And the One Move That Stops It)' — testear score"),
    warn("El título principal tiene outlier pattern validado ('Why Willpower Fails'). Mantener si VidIQ ≥80."),
    hr(),
]

# 3. DESCRIPCIÓN
flow.append(sec("3. DESCRIPCIÓN — copia exactamente"))
desc_lines = [
    ("Alex watched the last video. He took notes. He sent it to his brother.", True),
    ("On Friday, the salary notification arrived — and four hundred euros were gone again.", True),
    ("", False),
    ("Knowing the name of a trap is not the same as escaping it.", True),
    ("The real fix requires removing the decision from Alex's hands entirely — not making it easier to get right.", False),
    ("", False),
    ("Roy Baumeister found that willpower depletes with every decision you make — not just financial ones.", False),
    ("By payday, you have the least of it exactly when you need the most.", False),
    ("In 1998, his radish experiment showed the mechanism clearly: same puzzle, different reserve.", False),
    ("", False),
    ("Richard Thaler and Shlomo Benartzi tested the solution at the University of Chicago in 2004.", False),
    ("Workers who made one structural decision went from saving 3.5% to 13.6% in five years.", False),
    ("No budgets. No willpower. No spreadsheets.", False),
    ("", False),
    ("In this video:", False),
    ("→ Why understanding a bias doesn't stop it from running", False),
    ("→ Roy Baumeister's ego depletion — the radish experiment", False),
    ("→ Why the standing order fires one minute before the Reward Trap", False),
    ("→ Save More Tomorrow (Thaler &amp; Benartzi, 2004) — 3.5% to 13.6% in five years", False),
    ("→ The Brain Villain's last trick — Present Bias wearing the costume of caution", False),
    ("", False),
    ("───────────────────────────────", False),
    ("📌 Watch next → [PEGA AQUÍ URL DE V13 — TAX REFUND]", False),
    ("📌 Previous: 3 Traps That Rewire Your Brain to Stay Broke → [PEGA AQUÍ URL DE V11]", False),
    ("───────────────────────────────", False),
    ("", False),
    ("0:00  You've started a budget at least three times", False),
    ("0:30  Why knowing isn't enough — Alex still spent it", False),
    ("1:45  Roy Baumeister — ego depletion + radish experiment", False),
    ("3:30  The standing order — how it beats all three traps", False),
    ("5:00  The CTA", False),
    ("5:15  Thaler &amp; Benartzi — Save More Tomorrow", False),
    ("6:30  The Brain Villain's last trick (Present Bias in disguise)", False),
    ("7:30  Identity close + next video", False),
    ("", False),
    ("#behavioralfinance #automaticsavings #savingmoney #egodepletion #neurocents", False),
]
for text, bold in desc_lines:
    if text == "":
        flow.append(Spacer(1, 2*mm))
    else:
        s = ParagraphStyle('dl', parent=CODE_S,
                           fontName='Helvetica-Bold' if bold else 'Helvetica')
        flow.append(Paragraph(text, s))
flow.append(hr())

# 4. TAGS
flow += [
    sec("4. TAGS — copia todo el bloque en YouTube Studio"),
    Paragraph(
        "automatic savings, ego depletion, save more tomorrow, willpower and money, "
        "behavioral finance, richard thaler, baumeister ego depletion, present bias, "
        "savings psychology, how to save money automatically, brain bias money, "
        "shlomo benartzi, standing order savings, psychology of saving, "
        "behavioral economics, neuroscience money, decision fatigue, neurocents, "
        "why willpower fails, radish experiment",
        CODE_S),
    sp(2),
    body("<b>TOP KEYWORDS POR SCORE VIDIQ (confirmar en VidIQ antes de publicar):</b>"),
]
kw_rows = [
    ("behavioral finance",              "103K/mes", "27 comp.", "73 ← confirmado"),
    ("automatic savings",               "~67K/mes", "~31 comp.", "← testear"),
    ("how to save money automatically", "~44K/mes", "~29 comp.", "← alto volumen"),
    ("ego depletion",                   "~12K/mes", "~18 comp.", "← gema oculta"),
    ("save more tomorrow",              "~8K/mes",  "~14 comp.", "← nicho fuerte"),
    ("baumeister ego depletion",        "~5K/mes",  "~10 comp.", "← long-tail preciso"),
    ("savings psychology",              "~22K/mes", "~25 comp.", "← testear"),
    ("willpower and money",             "~19K/mes", "~22 comp.", "← testear"),
    ("present bias",                    "~15K/mes", "~20 comp.", "← bajo comp."),
    ("why willpower fails",             "testear",  "—",         "← título exact match"),
]
for kw, vol, comp, score in kw_rows:
    flow.append(Paragraph(
        f'<font name="Courier">{kw:<42}  {vol:<14}  {comp:<16}  {score}</font>', KW_S))
flow.append(hr())

# 5. MINIATURA
flow += [
    sec("5. MINIATURA"),
    lv("CONCEPTO",
       "Alex con expresión de cansancio / revelación. <b>Fondo blanco estilo Andy/MoneyTom.</b>"),
    lv("TEXTO THUMBNAIL", "WILLPOWER FAILS  (máx 5 palabras)"),
    lv("OBJETO", "Villain pequeño vs. standing order (flecha verde) — contraste de tamaño"),
    note("Alternativa A: Alex exhausted (viernes) LEFT | Alex calm (martes) RIGHT — split panel antes/después."),
    note("Alternativa B: Villain durmiendo / vencido, Alex de pie con brazo cruzado. Alex dominante."),
    warn("V11 usó villain activo + 3 trampas. V12: Alex dominante, villain en segundo plano o derrotado."),
    warn("BLUE t-shirt en Alex — NO red. Verificar en Google Flow antes de generar."),
    hr(),
]

# 6. YOUTUBE STUDIO
flow.append(sec("6. YOUTUBE STUDIO — configuración antes de publicar"))
yt_checks = [
    "Título:         Why Willpower Fails Every Payday — And the One Decision That Stops It",
    "Descripción:    Pegada completa con capítulos y URLs de V11 y V13",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — fondo blanco, Alex dominante, texto WILLPOWER FAILS",
    "Capítulos:      Activados (timestamps en descripción)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado 20:00–22:00 hora Bali (12:00–14:00 EST)",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
]
for c in yt_checks:
    flow.append(cb(c))
flow.append(hr())

# 7. END SCREEN
flow += [
    sec("7. END SCREEN — últimos 20 segundos"),
    cb("Vídeo: seleccionar V13 (Tax Refund — €800 disappears 3× faster) — NO 'mejor opción'"),
    cb("Botón suscripción"),
    body("Script end screen: 'Watch this next — Alex gets a tax refund. Eight hundred euros he wasn't expecting. "
         "His brain treats it completely differently. The money disappears three times faster. "
         "The reason is the one nobody expects.'"),
    warn("Después de publicar V12: entrar a V11 y actualizar end screen apuntando a V12 específico."),
    hr(),
]

# 8. CARDS
flow += [
    sec("8. CARDS (tarjetas dentro del vídeo)"),
    cb("Minuto ~1:45 (BAUMEISTER) → card apuntando a V11 (3 Traps — contexto de trampas)"),
    cb("Minuto ~5:30 (THE SCIENCE) → card apuntando a V5 (Mental Accounting — Thaler conexión)"),
    hr(),
]

# 9. PLAYLIST
flow += [
    sec("9. PLAYLIST"),
    cb("Añadir V12 a playlist 'How Your Brain Costs You Money — Neurocents'"),
    cb("Orden sugerido: V11 → V12 → V13 (secuencia 3 Traps → One Decision → Tax Refund)"),
    cb("Pegar URL de playlist en descripción de V12"),
    hr(),
]

# 10. PRIMER COMENTARIO
flow += [
    sec("10. PRIMER COMENTARIO — fijar nada más publicar"),
    Paragraph(
        "Alex didn't need more willpower. He needed fewer decisions.<br/>"
        "One bank transfer, set up on a calm Tuesday — before the salary arrives.<br/>"
        "Drop 🧠 if you felt the discomfort when the standing order was explained. "
        "That was the Brain Villain identifying itself.",
        CODE_S),
    hr(),
]

# 11. REDDIT
flow.append(sec("11. REDDIT — publicar 1h después de que el vídeo esté live"))
reddit_rows = [
    ("r/personalfinance",      "Primero — ahorro automático, muy activo"),
    ("r/BehavioralEconomics",  "+30 min — Thaler &amp; Benartzi + Baumeister"),
    ("r/psychology",           "+30 min — ego depletion / radish experiment"),
    ("r/cogsci",               "+30 min — sistema automático vs willpower"),
]
for sub, timing in reddit_rows:
    flow.append(Paragraph(f"<b>{sub}</b>  —  <font color='{GREY.hexval()}'>{timing}</font>", BODY_S))
flow.append(sp(2))
flow.append(body("<b>TÍTULO REDDIT (r/psychology / r/BehavioralEconomics):</b>"))
flow.append(Paragraph(
    "Baumeister's 1998 radish experiment found that willpower depletes with every decision — not just financial ones. "
    "By payday (after 5 days of choosing), you have the least of it exactly when you need the most. "
    "The only real fix isn't a better budget. (Made a short video on the mechanism + the structural solution)",
    CODE_S))
flow.append(sp(2))
flow.append(body("<b>TÍTULO REDDIT (r/personalfinance):</b>"))
flow.append(Paragraph(
    "Thaler &amp; Benartzi found that one structural decision — automatic redirect on raise day — "
    "took workers from 3.5% to 13.6% savings in 5 years. No budgets, no willpower. "
    "The insight isn't the savings rate — it's why the decision needs to happen on a Tuesday, not a Friday. "
    "(Short video on the mechanism)",
    CODE_S))
flow.append(hr())

# 12. HORA
flow += [
    sec("12. HORA DE PUBLICACIÓN"),
    lv("BALI", "20:00 – 22:00", GREEN),
    lv("EST",  "12:00 – 14:00 (prime time USA)", GREY),
    lv("SECUENCIA",
       "Publicar V12 máximo 7 días después de V11 — son una unidad narrativa", GREY),
    warn("V12 debe publicarse pronto después de V11 para mantener la continuidad narrativa."),
    hr(),
]

# 13. OUTLIER NOTES
flow.append(sec("13. NOTAS DE OUTLIER — por qué este título y este hook"))
outlier_notes = [
    "TÍTULO: 'Why Willpower Fails Every Payday' — Outlier pattern validado (132.7×): 'Why [X] Fails Every [Trigger]'",
    "HOOK BEAT 1: Identity-first — espectador se reconoce antes de hacer clic (3 presupuestos, ninguno sobrevivió)",
    "BAUMEISTER EXPERIMENT: concreto, narrativo, contrastivo — mismo tipo de datos que generan retención alta",
    "VILLAIN INOCULATION (beats 76–86): segunda persona directa en tiempo real — sella el engagement con el concepto",
    "IDENTITY CLOSE: 'The programs are not broken' — cierre no moralista = mayor retención hasta el final",
]
for n in outlier_notes:
    flow.append(Paragraph(f"→  {n}", BODY_S))
flow.append(hr())

# FOOTER
flow += [
    sp(4),
    Paragraph(
        "NEUROCENTS · V12 FINAL · PRE-PUBLISH CHECKLIST · "
        "Why Willpower Fails Every Payday · Tags a confirmar en VidIQ",
        FOOT_S),
]

out = "/home/user/Claudeeee/V12_final_Prepublish_Checklist.pdf"
doc = SimpleDocTemplate(out, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)
doc.build(flow)
print(f"Saved: {out}")
