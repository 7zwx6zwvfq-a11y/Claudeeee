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
ORANGE= colors.HexColor('#C05A00')

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
                         textColor=ORANGE, spaceAfter=2)
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
    Paragraph("3 Reasons Your Brain Spends Every Payday (Without Telling You)  ·  20:15 España / 14:15 EST", SUB_S),
    hr(),
]

# 1. FILENAME
flow += [
    sec("1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir"),
    lv("ARCHIVO", "3-reasons-brain-spends-every-payday-neurocents.mp4", GREEN),
    hr(),
]

# 2. TÍTULO
flow += [
    sec("2. TÍTULO — VidIQ 85 pts  ·  fórmula outlier 181×"),
    lv("TÍTULO PRINCIPAL",
       "3 Reasons Your Brain Spends Every Payday (Without Telling You)", DARK),
    grn("Fórmula: '[Number] [Things] That [Negative Consequence to Brain/Money] (Without Telling You)' — 181× outlier validado."),
    grn("VidIQ: 85 pts  ·  'reasons' = alta intención + número = expectativa de estructura clara"),
    warn("NO cambiar a título anterior. 85 pts supera 81 pts de 'Why Willpower Fails'. Mantener este."),
    hr(),
]

# 3. DESCRIPCIÓN
flow.append(sec("3. DESCRIPCIÓN — copia exactamente"))
desc_lines = [
    ("Every payday, Alex earns 3,200. By Sunday, 1,200 is already gone.", True),
    ("Not on rent. Not on luxuries. On 3 programs his brain runs automatically.", False),
    ("", False),
    ("He doesn't overspend. His brain does — for 3 specific reasons.", False),
    ("", False),
    ("Reason 1: Roy Baumeister (Florida State, 1998) found that willpower depletes", False),
    ("with every decision you make — not just financial ones.", False),
    ("By payday, after 5 days of micro-choices, you have the least of it", False),
    ("exactly when you need the most.", False),
    ("", False),
    ("Reason 2: Wolfram Schultz (Cambridge, Nobel) proved that dopamine fires", False),
    ("at the moment of expectation — not when you spend.", False),
    ("The decision is already made before the money moves.", False),
    ("", False),
    ("Reason 3: Kahneman and Deaton (Princeton) found that behavioral traps", False),
    ("consume the same percentage of income at $50K as at $150K.", False),
    ("Earning more doesn't fix it. The 3 programs scale with the paycheck.", False),
    ("", False),
    ("Richard Thaler and Shlomo Benartzi tested the only fix that works.", False),
    ("One structural decision — made on a calm Tuesday — took workers", False),
    ("from saving 3.5% to 13.6% in five years. No budgets. No willpower. No spreadsheets.", False),
    ("", False),
    ("In this video:", False),
    ("→ Reason 1 — Ego Depletion: why Friday is the worst day to decide (Baumeister, 1998)", False),
    ("→ Reason 2 — Dopamine at Expectation: why the spend is decided before payday (Schultz)", False),
    ("→ Reason 3 — The Income Trap: why earning more makes the same % disappear (Kahneman/Deaton)", False),
    ("→ The one structural decision that defeats all 3 — before they activate (Thaler &amp; Benartzi)", False),
    ("", False),
    ("───────────────────────────────", False),
    ("📌 Watch next → [PEGA AQUÍ URL DE V13]", False),
    ("📌 Previous: 3 Traps That Rewire Your Brain to Stay Broke → [PEGA AQUÍ URL DE V11]", False),
    ("───────────────────────────────", False),
    ("", False),
    ("0:00  Every payday. Same result.", False),
    ("0:30  Why knowing the traps isn't enough", False),
    ("1:20  Reason 1 — Ego Depletion (Baumeister / radish experiment)", False),
    ("3:10  Reason 2 — Dopamine at Expectation (Schultz / Nobel)", False),
    ("5:00  CTA", False),
    ("5:15  Reason 3 — The Income Trap (Kahneman &amp; Deaton / Princeton)", False),
    ("6:30  The one decision: Save More Tomorrow (Thaler &amp; Benartzi 2004)", False),
    ("8:00  Brain Villain's last trick — Present Bias in disguise", False),
    ("9:00  Identity close + next video", False),
    ("", False),
    ("#behavioralfinance #psychologyofmoney #automaticsavings #egodepletion #neurocents", False),
    ("#savingmoney #presentbias #financialpsychology #cognitivebiases #rewirebrain", False),
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
        "behavioral finance, psychology of money, financial psychology, "
        "automatic savings, ego depletion, save more tomorrow, present bias, "
        "why you spend money, brain and money, baumeister ego depletion, "
        "wolfram schultz dopamine, kahneman deaton, richard thaler, shlomo benartzi, "
        "reasons brain spends, cognitive biases money, neuroscience finance, "
        "rewire brain, standing order savings, decision fatigue money, neurocents",
        CODE_S),
    sp(2),
    body("<b>TOP KEYWORDS POR SCORE VIDIQ:</b>"),
]
kw_rows = [
    ("behavioral finance",              "98K/mes",  "24 comp.", "75 ← primario"),
    ("financial psychology",            "120K/mes", "27 comp.", "74.7 ← primario"),
    ("psychology of money",             "731K/mes", "57 comp.", "69.5 ← alto vol."),
    ("automatic savings",               "~67K/mes", "~31 comp.", "← testear"),
    ("ego depletion",                   "~12K/mes", "~18 comp.", "← gema oculta"),
    ("save more tomorrow",              "~8K/mes",  "~14 comp.", "← nicho fuerte"),
    ("present bias",                    "~15K/mes", "~20 comp.", "← bajo comp."),
    ("reasons brain spends",            "testear",  "—",         "← exact match título"),
    ("why you spend money",             "testear",  "—",         "← intención búsqueda"),
]
for kw, vol, comp, score in kw_rows:
    flow.append(Paragraph(
        f'<font name="Courier">{kw:<42}  {vol:<14}  {comp:<16}  {score}</font>', KW_S))
flow.append(hr())

# 5. MINIATURA
flow += [
    sec("5. MINIATURA — concepto YOUR BRAIN / WINS (fondo blanco Andy/MoneyTom)"),
    lv("CONCEPTO",
       "Alex señalando con el dedo a cartera vacía. Brain Villain dentro del cráneo transparente, brazos cruzados, satisfecho."),
    lv("FONDO", "BLANCO — estilo Andy/MoneyTom. NO oscuro, NO gradiente.", RED),
    lv("TEXTO THUMBNAIL", "YOUR BRAIN / WINS  (máx 5 palabras, bold Impact)"),
    lv("OBJETO", "Cartera vacía con símbolo $ cayendo — arriba Brain Villain victorioso dentro del skull de Alex"),
    note("Expresión de Alex: shock genuino, ojos abiertos, señalando la cartera. Villain: heavy-lidded smug, brazos cruzados."),
    warn("Blue t-shirt en Alex — NO red. Verificar SIEMPRE en Google Flow antes de generar."),
    warn("Brain Villain DENTRO del cráneo transparente — NO flotando fuera. Regla absoluta."),
    hr(),
]

# 6. YOUTUBE STUDIO
flow.append(sec("6. YOUTUBE STUDIO — configuración antes de publicar"))
yt_checks = [
    "Título:         3 Reasons Your Brain Spends Every Payday (Without Telling You)",
    "Descripción:    Pegada completa — 3 razones + timestamps + URLs V11 y V13",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Fondo blanco, Alex shocked, cartera vacía, YOUR BRAIN / WINS",
    "Capítulos:      Activados (timestamps en descripción desde 0:00)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado 20:15 España (CEST = UTC+2) = 14:15 EST",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
]
for c in yt_checks:
    flow.append(cb(c))
flow.append(hr())

# 7. END SCREEN
flow += [
    sec("7. END SCREEN — últimos 20 segundos"),
    cb("Vídeo: seleccionar V13 — NO 'mejor opción automática'"),
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
    cb("Minuto ~1:20 (BAUMEISTER) → card apuntando a V11 (3 Traps — contexto de trampas)"),
    cb("Minuto ~6:30 (THALER) → card apuntando a V5 (Mental Accounting — Thaler conexión)"),
    hr(),
]

# 9. PLAYLIST
flow += [
    sec("9. PLAYLIST"),
    cb("Añadir V12 a playlist 'How Your Brain Costs You Money — Neurocents'"),
    cb("Orden sugerido: V11 → V12 → V13 (secuencia 3 Traps → 3 Reasons → Tax Refund)"),
    cb("Pegar URL de playlist en descripción de V12"),
    hr(),
]

# 10. PRIMER COMENTARIO
flow += [
    sec("10. PRIMER COMENTARIO — fijar nada más publicar (inmediatamente)"),
    Paragraph(
        "3 reasons. Same result every payday.<br/>"
        "Alex didn't need more willpower. He needed one decision made on a Tuesday — "
        "before the salary arrives, before the dopamine fires, before Reason 1 depletes the tank.<br/>"
        "Which of the 3 reasons costs you the most? Drop the number below.",
        CODE_S),
    hr(),
]

# 11. REDDIT
flow.append(sec("11. REDDIT — publicar 1h después de que el vídeo esté live"))
reddit_rows = [
    ("r/personalfinance",      "Primero — ahorro automático, muy activo"),
    ("r/BehavioralEconomics",  "+30 min — Baumeister + Schultz + Kahneman"),
    ("r/psychology",           "+30 min — ego depletion / radish experiment"),
    ("r/cogsci",               "+30 min — dopamine at expectation / Schultz"),
]
for sub, timing in reddit_rows:
    flow.append(Paragraph(f"<b>{sub}</b>  —  <font color='{GREY.hexval()}'>{timing}</font>", BODY_S))
flow.append(sp(2))
flow.append(body("<b>TÍTULO REDDIT (r/BehavioralEconomics / r/psychology):</b>"))
flow.append(Paragraph(
    "Baumeister (1998) proved willpower depletes with every decision — not just financial ones. "
    "Schultz proved dopamine fires at expectation, not at spend. "
    "Kahneman and Deaton found behavioral traps consume the same % of income at $50K as at $150K. "
    "Three separate findings. One result every payday. "
    "(Short video mapping all three and the only structural fix that works)",
    CODE_S))
flow.append(sp(2))
flow.append(body("<b>TÍTULO REDDIT (r/personalfinance):</b>"))
flow.append(Paragraph(
    "Thaler and Benartzi found that one structural decision — automatic redirect made once — "
    "took workers from saving 3.5% to 13.6% in 5 years. No budgets, no willpower. "
    "The key insight: the decision has to happen on a Tuesday, not a Friday. "
    "Mapped the 3 reasons why Friday never works. (Short video)",
    CODE_S))
flow.append(hr())

# 12. HORA
flow += [
    sec("12. HORA DE PUBLICACIÓN"),
    lv("ESPAÑA (CEST)", "20:15", GREEN),
    lv("EST",  "14:15 (prime time USA East Coast)", GREY),
    lv("UTC",  "18:15", GREY),
    lv("SECUENCIA",
       "V11 publicado antes. V12 = continuidad narrativa. Publicar mismo día si es posible.", GREY),
    warn("Cadencia canal: Lunes y Jueves a las 20:15 España. V12 publica hoy martes — excepción por desplazamiento."),
    hr(),
]

# 13. OUTLIER NOTES
flow.append(sec("13. NOTAS DE OUTLIER — por qué este título y este hook"))
outlier_notes = [
    "TÍTULO: '3 Reasons Your Brain Spends Every Payday' — VIDIQ 85 pts. Fórmula 181× validada por outliers.",
    "FÓRMULA: '[Number] [Things] That [Negative Consequence] (Without Telling You)' — número + curiosity gap.",
    "HOOK BEAT 1: Identity-first — 'Every payday. Same result.' Espectador se reconoce antes de entender el mecanismo.",
    "ESTRUCTURA 3 RAZONES: Baumeister (depletes willpower) → Schultz (dopamine fires early) → Kahneman (scales with income).",
    "VILLAIN INOCULATION: 'Present Bias wearing the costume of caution' — sella el engagement en tiempo real.",
    "IDENTITY CLOSE: 'The programs are not broken' — cierre no moralista = mayor retención hasta el final.",
    "CTR TARGET: >6% en primeras 48h. Retention at 30s: >45%. Retention at midpoint: >50%.",
]
for n in outlier_notes:
    flow.append(Paragraph(f"→  {n}", BODY_S))
flow.append(hr())

# FOOTER
flow += [
    sp(4),
    Paragraph(
        "NEUROCENTS · V12 FINAL · PRE-PUBLISH CHECKLIST · "
        "3 Reasons Your Brain Spends Every Payday (Without Telling You) · 20:15 España",
        FOOT_S),
]

out = "/home/user/Claudeeee/V12_final_Prepublish_Checklist.pdf"
doc = SimpleDocTemplate(out, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)
doc.build(flow)
print(f"Saved: {out}")
