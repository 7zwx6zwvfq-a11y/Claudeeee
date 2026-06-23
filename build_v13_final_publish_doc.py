#!/usr/bin/env python3
"""V13 Pre-publish Checklist — PDF version via reportlab."""

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
    Paragraph("NEUROCENTS — VIDEO 13 FINAL · PRE-PUBLISH CHECKLIST", TITLE_S),
    Paragraph("5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)  ·  20:15 España / 14:15 EST", SUB_S),
    hr(),
]

# 1. FILENAME
flow += [
    sec("1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir"),
    lv("ARCHIVO", "5-ways-brain-physically-rewires-stay-broke-neurocents.mp4", GREEN),
    hr(),
]

# 2. TÍTULO
flow += [
    sec("2. TÍTULO — fórmula outlier 181×  ·  validación externa 85×"),
    lv("TÍTULO PRINCIPAL",
       "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)", DARK),
    grn("Fórmula: '[Number] Ways Your Brain [Physical Verb] to Stay Broke (Without Telling You)' — 181× outlier validado."),
    grn("Validación externa: '10 Habits That Physically Rewire Your Brain For Happiness' = 85× outlier, 238K views (it's that simple, 81K subs)."),
    grn("Validación externa adicional: 'These 7 Daily Habits Are Reshaping Your Brain Right Now' = 39× outlier, 396K views."),
    note("Alternativa A considerada: '5 Habits That Physically Rewire Your Brain to Keep You Broke (Without Telling You)' — 'Habits' funciona en outliers pero 'Ways' es más canónico de Neurocents."),
    note("Alternativa B considerada: '5 Ways Your Brain Is Physically Rewiring Itself Right Now (To Keep You Broke)' — 'Right Now' del outlier 39×, presente continuo para urgencia."),
    warn("Mantener el título principal. 181× + doble validación externa = mayor confianza que cualquier alternativa."),
    hr(),
]

# 3. DESCRIPCIÓN
flow.append(sec("3. DESCRIPCIÓN — copia exactamente"))
desc_lines = [
    ("Alex earns more than he did three years ago.", True),
    ("He has less to show for it. Not because of bad investments. Because his brain is running 5 programs he was never told about.", False),
    ("", False),
    ("Here's the full map:", False),
    ("", False),
    ("Way 1: The Anticipation Burn — Wolfram Schultz (Cambridge, Nobel) proved dopamine fires at the", False),
    ("prediction of reward, not the reward itself. By Wednesday, Alex's brain has already spent Friday's salary.", False),
    ("", False),
    ("Way 2: The Balance Blindspot — Galai & Sade (Hebrew University, 2006) documented the ostrich effect:", False),
    ("when financial information is painful, the brain stops seeking it. The money leaves. Alex doesn't see it leave.", False),
    ("", False),
    ("Way 3: The Expertise Trap — Terrance Odean (UC Berkeley) found that investors who traded more", False),
    ("frequently earned less. Daniel Kahneman: 80% believe they're above-average investors. 50% are", False),
    ("mathematically wrong. More vocabulary = more certainty. Not more accuracy.", False),
    ("", False),
    ("Way 4: The Night Drain — Shai Danziger (Ben-Gurion University) studied 8 judges over 10 months.", False),
    ("Morning: 65% parole granted. Afternoon: 11%. Same judges. Same evidence. By 10pm, Alex's resistance", False),
    ("is minimum. The Brain Villain only needs to wait.", False),
    ("", False),
    ("Way 5: The Upgrade Lock — Kent Berridge (University of Michigan, 30 years of research) separated", False),
    ("WANTING (dopamine, increases with exposure) from LIKING (opioid circuits, decreases with repetition).", False),
    ("Every upgrade raises the floor. Alex was satisfied for eleven days.", False),
    ("", False),
    ("None of this is a character flaw. The programs are not broken. They are perfectly designed for", False),
    ("an environment that no longer exists.", False),
    ("", False),
    ("───────────────────────────────", False),
    ("📌 Watch next → [PEGA AQUÍ URL DE V14]", False),
    ("📌 Previous: 3 Reasons Your Brain Spends Every Payday → [PEGA AQUÍ URL DE V12]", False),
    ("───────────────────────────────", False),
    ("", False),
    ("0:00  Alex earns more. Has less.", False),
    ("0:30  Way 1 — Anticipation Burn (Schultz / Cambridge / Nobel)", False),
    ("2:20  Way 2 — Balance Blindspot (Galai & Sade / Hebrew University)", False),
    ("3:40  CTA", False),
    ("3:50  Way 3 — Expertise Trap (Odean / UC Berkeley + Kahneman)", False),
    ("5:20  Way 4 — Night Drain (Danziger / Ben-Gurion)", False),
    ("6:30  Way 5 — Upgrade Lock (Berridge / Michigan)", False),
    ("8:00  System: all 5 running together", False),
    ("9:00  Brain Villain's last trick", False),
    ("10:00 Identity close", False),
    ("", False),
    ("#behavioralfinance #financialpsychology #brainandmoney #cognitivebiases #neurocents", False),
    ("#whyyoustayroke #egodepletion #dopamine #hedonicrewire #psychologyofmoney", False),
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
        "behavioral finance, financial psychology, brain rewires itself, why you stay broke, "
        "cognitive biases money, anticipation burn, balance blindspot, expertise trap, night drain, "
        "upgrade lock, wolfram schultz dopamine, terrance odean, kent berridge, shai danziger, "
        "ostrich effect, ego depletion money, hedonic treadmill, psychology of money, "
        "why your brain keeps you broke, neurocents, human psychology, rewire brain, "
        "wanting vs liking, decision fatigue money, overconfidence bias",
        CODE_S),
    sp(2),
    body("<b>TOP KEYWORDS POR SCORE VIDIQ:</b>"),
]
kw_rows = [
    ("behavioral finance",              "98K/mes",    "24 comp.",  "75 ← primario"),
    ("financial psychology",            "120K/mes",   "27 comp.",  "74.7 ← primario"),
    ("psychology of money",             "731K/mes",   "57 comp.",  "69.5 ← alto vol."),
    ("human psychology",                "295.3K VPH", "+152% trending", "← INCLUIR primeras 200 chars"),
    ("cognitive biases money",          "4.9K/mes",   "33.7 comp.", "59.6"),
    ("brain rewires itself",            "testear",    "—",          "← exact match título"),
    ("why you stay broke",              "testear",    "—",          "← intención búsqueda"),
    ("wanting vs liking",               "testear",    "—",          "← Berridge / nicho fuerte"),
    ("decision fatigue money",          "testear",    "—",          "← Night Drain connection"),
]
for kw, vol, comp, score in kw_rows:
    flow.append(Paragraph(
        f'<font name="Courier">{kw:<42}  {vol:<18}  {comp:<20}  {score}</font>', KW_S))
flow.append(sp(2))
flow.append(warn("'human psychology' trending +152% en VidIQ a 295.3K VPH — incluir en tags Y primeras 200 chars de descripción."))
flow.append(hr())

# 5. MINIATURA
flow += [
    sec("5. MINIATURA — concepto 5 WAYS / YOUR BRAIN / REWIRES ITSELF (fondo blanco Andy/MoneyTom)"),
    lv("CONCEPTO A (primary)",
       "Alex IZQUIERDA, expresión shock (mano apretada contra cabeza), skull transparente mostrando Brain Villain activando 5 circuitos rojos simultáneamente."),
    lv("TEXTO THUMBNAIL",
       '"5 WAYS" grande negro | "YOUR BRAIN" mediano negro | "REWIRES ITSELF" ultra-bold ROJO (#C62828)'),
    lv("FONDO", "BLANCO — estilo Andy/MoneyTom canónico. NO oscuro, NO gradiente.", RED),
    lv("TEXTO POSICIÓN", "DERECHA del frame — personaje ocupa lado izquierdo"),
    note("Expresión de Alex: shock genuino (hand pressed against head), ojos muy abiertos. Villain: dentro del skull, heavy-lidded smirk, activando 5 nodos rojos."),
    note("Los 5 circuitos rojos deben ser visibles dentro del cráneo transparente — no fuera de la cabeza."),
    warn("BLUE t-shirt en Alex — NOT red. Verificar SIEMPRE en Google Flow antes de generar."),
    warn("Brain Villain DENTRO del cráneo transparente — NO flotando fuera. Regla absoluta."),
    hr(),
]

# 6. YOUTUBE STUDIO
flow.append(sec("6. YOUTUBE STUDIO — configuración antes de publicar"))
yt_checks = [
    "Título:         5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)",
    "Descripción:    Pegada completa — 5 Ways + timestamps + URLs V12 y V14",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Fondo blanco, Alex shocked, 5 circuitos rojos, '5 WAYS / YOUR BRAIN / REWIRES ITSELF'",
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
    cb("Vídeo: seleccionar V14 — NO 'mejor opción automática'"),
    cb("Botón suscripción"),
    body("Script end screen: 'Watch this next — Alex tries to budget for the third time. "
         "He has a spreadsheet. He has a system. He has everything — "
         "except the part that actually changes anything.'"),
    warn("Después de publicar V13: entrar a V12 y actualizar end screen apuntando a V13 específico."),
    hr(),
]

# 8. CARDS
flow += [
    sec("8. CARDS (tarjetas dentro del vídeo)"),
    cb("Minuto ~2:20 (SCHULTZ / Anticipation Burn) → card apuntando a V11 (3 Traps — Schultz aparece también)"),
    cb("Minuto ~5:20 (DANZIGER / Night Drain) → card apuntando a V12 (ego depletion connection)"),
    hr(),
]

# 9. PLAYLIST
flow += [
    sec("9. PLAYLIST"),
    cb("Añadir V13 a playlist 'How Your Brain Costs You Money — Neurocents'"),
    cb("Orden: V11 → V12 → V13 → V14 (secuencia narrativa continua)"),
    cb("Pegar URL de playlist en descripción de V13"),
    hr(),
]

# 10. PRIMER COMENTARIO
flow += [
    sec("10. PRIMER COMENTARIO — fijar nada más publicar (inmediatamente)"),
    Paragraph(
        "5 programs. Running simultaneously. Right now.<br/>"
        "Alex didn't know any of their names — and they still cost him the same amount every month.<br/>"
        "Which of the 5 is costing you the most? Drop the number below.<br/>"
        "(The next video shows the structural fix for 3 of them — one decision, set up on a Tuesday.)",
        CODE_S),
    hr(),
]

# 11. REDDIT
flow.append(sec("11. REDDIT — publicar 1h después de que el vídeo esté live"))
reddit_rows = [
    ("r/psychology",           "Primero — Schultz Nobel + Berridge WANTING vs LIKING"),
    ("r/BehavioralEconomics",  "+30 min — Galai & Sade ostrich effect + Odean overconfidence"),
    ("r/personalfinance",      "+30 min — Danziger judges + Night Drain impulse hours"),
    ("r/cogsci",               "+30 min — Berridge 30 years WANTING vs LIKING + Upgrade Lock"),
]
for sub, timing in reddit_rows:
    flow.append(Paragraph(f"<b>{sub}</b>  —  <font color='{GREY.hexval()}'>{timing}</font>", BODY_S))
flow.append(sp(2))

flow.append(body("<b>REDDIT r/psychology (primero):</b>"))
flow.append(Paragraph(
    "Wolfram Schultz proved dopamine fires at the prediction of reward — not the reward itself. "
    "By Wednesday, Alex's brain has already decided how to spend Friday's salary. "
    "The decision is made 48 hours before the money exists. "
    "(Short video mapping all 5 mechanisms and why naming them isn't enough to stop them)",
    CODE_S))
flow.append(sp(2))

flow.append(body("<b>REDDIT r/BehavioralEconomics (+30 min):</b>"))
flow.append(Paragraph(
    "Galai &amp; Sade (Hebrew University, 2006) documented the ostrich effect: when financial information "
    "is painful, the brain stops seeking it. Terrance Odean found that the more investors trade, the less "
    "they earn — not because trading is wrong, but because confidence outpaced competence. "
    "We mapped both effects plus 3 more in the same video. (10 min)",
    CODE_S))
flow.append(sp(2))

flow.append(body("<b>REDDIT r/personalfinance (+30 min):</b>"))
flow.append(Paragraph(
    "Danziger's judge study showed decision quality drops from 65% to 11% by late afternoon. "
    "Same person. Same evidence. Different reserve. Impulse purchases peak between 9-midnight for the same reason. "
    "Mapped 5 specific programs that cost the same % of income at €40K as at €140K. (Short video)",
    CODE_S))
flow.append(sp(2))

flow.append(body("<b>REDDIT r/cogsci (+30 min):</b>"))
flow.append(Paragraph(
    "Kent Berridge spent 30 years separating WANTING (dopamine, increases with exposure) from LIKING "
    "(opioid circuits, decreases with repetition). Every upgrade raises the WANTING threshold. "
    "The LIKING response habituates. The floor cannot go back. "
    "(Video mapping how this interacts with 4 other behavioral programs to create a financial loop)",
    CODE_S))
flow.append(hr())

# 12. HORA
flow += [
    sec("12. HORA DE PUBLICACIÓN"),
    lv("ESPAÑA (CEST)", "20:15", GREEN),
    lv("EST",  "14:15 (prime time USA East Coast)", GREY),
    lv("UTC",  "18:15", GREY),
    lv("SECUENCIA",
       "V11 → V12 publicados. V13 = continuidad narrativa. Publicar 7 días o menos después de V12.", GREY),
    warn("Cadencia canal: Lunes y Jueves a las 20:15 España. Respetar cadencia — V13 en el próximo slot disponible."),
    hr(),
]

# 13. OUTLIER NOTES
flow.append(sec("13. NOTAS DE OUTLIER — por qué este título y este hook"))
outlier_notes = [
    "TÍTULO: '5 Ways Your Brain Physically Rewires Itself to Stay Broke' — fórmula 181× validada por outliers.",
    "VALIDACIÓN EXTERNA 1: '10 Habits That Physically Rewire Your Brain For Happiness' = 85× outlier, 238K views (it's that simple, 81K subs).",
    "VALIDACIÓN EXTERNA 2: 'These 7 Daily Habits Are Reshaping Your Brain Right Now' = 39× outlier, 396K views.",
    "FÓRMULA: '[Number] Ways Your Brain [Physical Verb] to Stay Broke (Without Telling You)' — número + verbo físico + curiosity gap.",
    "HOOK BEAT 1: Identity-first — 'Alex earns more. Has less.' Espectador se reconoce antes de entender el mecanismo.",
    "6 CIENTÍFICOS NOMBRADOS: Schultz (Nobel, Cambridge), Galai &amp; Sade (Hebrew U), Odean (UC Berkeley), Kahneman (Princeton/Nobel), Danziger (Ben-Gurion), Berridge (Michigan) — alta señal de autoridad.",
    "KEYWORD TRENDING: 'human psychology' +152% en VidIQ, 295.3K VPH — incluir en tags y primeras 200 chars.",
    "VILLAIN INOCULATION: 11 beats canónicos — inocula contra resistencia en tiempo real antes del commit.",
    "IDENTITY CLOSE: 'The programs are not broken' — cierre no moralista = mayor retención hasta el final.",
    "CTR TARGET: >6% en primeras 48h. Retention at 30s: >45%. Retention at midpoint: >50%.",
    "VIDIQ Patron de Outlier adicional: 'Specific X That Make You Y' scoring 47.2× y 46.1× — confirma dirección.",
]
for n in outlier_notes:
    flow.append(Paragraph(f"→  {n}", BODY_S))
flow.append(hr())

# FOOTER
flow += [
    sp(4),
    Paragraph(
        "NEUROCENTS · V13 FINAL · PRE-PUBLISH CHECKLIST · "
        "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You) · 20:15 España",
        FOOT_S),
]

out = "/home/user/Claudeeee/V13_final_Prepublish_Checklist.pdf"
doc = SimpleDocTemplate(out, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)
doc.build(flow)
print(f"Saved: {out}")
