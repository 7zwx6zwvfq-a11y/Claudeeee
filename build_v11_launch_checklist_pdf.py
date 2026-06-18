#!/usr/bin/env python3
"""V11 Launch Checklist PDF — 3 Traps That Rewire Your Brain to Stay Broke."""

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
LGREY = colors.HexColor('#DDDDDD')
ORANGE= colors.HexColor('#C05A00')

styles = getSampleStyleSheet()

TITLE_S = ParagraphStyle('T', parent=styles['Title'], fontSize=14, leading=18,
                         alignment=TA_CENTER, textColor=RED, spaceAfter=2)
SUB_S   = ParagraphStyle('S', parent=styles['Normal'], fontSize=9, leading=12,
                         alignment=TA_CENTER, textColor=GREY, spaceAfter=6)
SEC_S   = ParagraphStyle('Sec', parent=styles['Normal'], fontSize=11, leading=14,
                         fontName='Helvetica-Bold', textColor=RED,
                         spaceBefore=10, spaceAfter=4)
CB_S    = ParagraphStyle('Cb', parent=styles['Normal'], fontSize=10, leading=14,
                         leftIndent=5*mm, spaceAfter=3)
NOTE_S  = ParagraphStyle('N', parent=styles['Normal'], fontSize=8, leading=11,
                         leftIndent=5*mm, textColor=GREY, spaceAfter=2)
WARN_S  = ParagraphStyle('W', parent=styles['Normal'], fontSize=8, leading=11,
                         leftIndent=5*mm, textColor=ORANGE, spaceAfter=3)
CODE_S  = ParagraphStyle('C', parent=styles['Normal'], fontSize=8.5, leading=12,
                         leftIndent=5*mm, textColor=DARK, spaceAfter=3,
                         fontName='Courier')
BIG_S   = ParagraphStyle('B', parent=styles['Normal'], fontSize=11, leading=14,
                         leftIndent=5*mm, fontName='Helvetica-Bold',
                         textColor=GREEN, spaceAfter=2)
TIME_S  = ParagraphStyle('Ti', parent=styles['Normal'], fontSize=12, leading=16,
                         fontName='Helvetica-Bold', textColor=DARK,
                         spaceBefore=8, spaceAfter=4)
FOOT_S  = ParagraphStyle('F', parent=styles['Normal'], fontSize=8, leading=11,
                         alignment=TA_CENTER, textColor=GREY)

def sec(t):
    return Paragraph(f"── {t} ──", SEC_S)

def cb(t):
    return Paragraph(f"☐  {t}", CB_S)

def note(t):
    return Paragraph(t, NOTE_S)

def warn(t):
    return Paragraph(f"⚠  {t}", WARN_S)

def code(t):
    return Paragraph(t, CODE_S)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=LGREY,
                      spaceBefore=5, spaceAfter=3)

def sp(h=3):
    return Spacer(1, h*mm)

def time_block(t):
    return Paragraph(t, TIME_S)


flow = []

# ── HEADER ──
flow += [
    Paragraph("NEUROCENTS — VIDEO 11 · LAUNCH CHECKLIST", TITLE_S),
    Paragraph("3 Traps That Rewire Your Brain to Stay Broke  ·  Publicación 20:15 Bali / 12:15 EST", SUB_S),
    hr(),
]

# ── T-30 ──
flow += [
    time_block("T − 30 min  (AHORA)"),
    sec("1. ARCHIVO"),
    cb("MP4 renombrado antes de subir:"),
    code("3-traps-rewire-brain-stay-broke-neurocents.mp4"),
    hr(),

    sec("2. YOUTUBE STUDIO — subir como No Listado primero"),
    cb('Título:      3 Traps That Rewire Your Brain to Stay Broke'),
    cb("Categoría:   Education"),
    cb("Miniatura:   Alex shocked · 'REWIRED' + '3 TRAPS' legible en móvil · fondo blanco"),
    warn("El script original decía 'deep red gradient background'. El estándar es FONDO BLANCO (Andy/MoneyTom). Verificar cuál thumbnail tenés listo."),
    warn("BLUE t-shirt en Alex — NO red. Verificar antes de subir."),
    hr(),

    sec("3. DESCRIPCIÓN — pegar exactamente"),
    code("Alex earns 3,200 every month. By Sunday, 1,200 is already gone — not on rent. On traps."),
    code("This video breaks down the 3 behavioral programs your brain runs every payday"),
    code("— and why earning more doesn't fix them."),
    code(""),
    code("In this video:"),
    code("→ Trap 1: The Reward Trap — Wolfram Schultz (Nobel, Cambridge) + hedonic adaptation"),
    code("→ Trap 2: The Safe Money Illusion — Richard Thaler (Nobel 2017, Chicago)"),
    code("→ Trap 3: The Future Is Fake — David Laibson (Harvard) + Kahneman/Deaton (Princeton)"),
    code(""),
    code("───────────────────────────────"),
    code("📌 Watch next → [URL V12 — Why Willpower Fails Every Payday]"),
    code("📌 Previous → [URL V10 — Sunk Cost]"),
    code("───────────────────────────────"),
    code(""),
    code("0:00  Friday: 3,200. Sunday: 1,980."),
    code("1:00  Trap 1 — The Reward Trap (Schultz dopamine)"),
    code("2:20  CTA"),
    code("3:20  Trap 2 — Mental Accounting (Thaler)"),
    code("5:50  Trap 3 — Present Bias (Laibson)"),
    code("8:20  The 3 gears — how they feed each other"),
    code("10:00 Identity close"),
    code(""),
    code("#behavioralfinance #psychologyofmoney #mentaltraps #presentbias"),
    code("#mentalaccounting #rewirebrain #neurocents #cognitivebiases"),
    hr(),

    sec("4. TAGS — pegar todo el bloque"),
    code("behavioral finance, psychology of money, investing psychology, money mindset,"),
    code("cognitive biases, brain and money, neuroscience finance, financial psychology,"),
    code("rewire brain, mental traps, hedonic adaptation, present bias, mental accounting,"),
    code("hyperbolic discounting, reward trap, richard thaler, wolfram schultz, david laibson"),
    hr(),

    sec("5. END SCREEN + CARDS"),
    cb("End screen → apunta a V12 ('Why Willpower Fails Every Payday')"),
    cb("Card ~1:00 → V1 (Three Brain Glitches — contexto de trampas)"),
    cb("Card ~5:50 → V5 (Mental Accounting — Thaler conexión directa)"),
    hr(),

    sec("6. PROGRAMAR PUBLICACIÓN"),
    cb("Visibilidad: Público programado — 20:15 Bali / 12:15 EST"),
    hr(),
]

# ── T-15 ──
flow += [
    time_block("T − 15 min"),
    sec("7. AMIGOS"),
    cb("Enviar link privado/no listado a los 8 amigos"),
    note("Deben ver el video COMPLETO — sin skip, sin background — antes de que sea público"),
    note("Objetivo: señal de retención alta antes de que el algoritmo lo testee"),
    hr(),
]

# ── T+0 ──
flow += [
    time_block("T + 0  (20:15 — video PÚBLICO)"),
    sec("8. COMENTARIO FIJADO — pegar INMEDIATAMENTE después de publicar"),
    code('"Alex earns 3,200. By Sunday, 1,200 is already gone — and he can\'t explain why.'),
    code("Which of the 3 traps costs you the most? Drop your number below."),
    code('Watch the one that fixes it next: [URL V12]"'),
    hr(),
]

# ── T+20 a T+60 ──
flow += [
    time_block("T + 20 a T + 60 min"),
    sec("9. DISTRIBUCIÓN"),
    cb("LinkedIn live — link en el PRIMER COMENTARIO, no en el cuerpo del post"),
    cb("Amigos postean comentarios escalonados — uno cada 3-4 min (no todos a la vez)"),
    cb("Responder a TODOS los comentarios en menos de 30 min"),
    sp(2),
    note("RESPUESTA CANÓNICA para comentarios de amigos:"),
    code('"The gear system is the key insight most financial advice misses.'),
    code("Budgeting apps target Trap 1. Debt consolidation targets Trap 2."),
    code("Savings automation targets Trap 3. But the gears reinforce each other."),
    code("Target the operating system — Present Bias — and the other two become"),
    code('easier to interrupt automatically. That\'s exactly what the next video covers."'),
    hr(),
]

# ── COMENTARIOS AMIGOS ──
flow += [
    sec("10. COMENTARIOS DE AMIGOS — queued y listos para pegar"),
]
friend_comments = [
    ("Amigo 1",
     '"The hedonic adaptation part hit me. The 85 euro dinner becoming the new floor —\n'
     ' I thought my spending was stable. It was just adjusting upward every month\n'
     ' without me noticing."'),
    ("Amigo 2",
     '"I have a savings account and credit card debt at the same time. Right now.\n'
     ' The mental accounting section made me uncomfortable in a way I actually needed."'),
    ("Amigo 3",
     '"Future Alex doesn\'t feel like me. That line is going to live in my head for weeks.\n'
     ' Because it\'s true. He really doesn\'t feel like me."'),
    ("Amigo 4",
     '"I always thought the problem was discipline. The \'present bias is the operating\n'
     ' system\' reframe changes everything. It\'s not willpower. It\'s hardware."'),
    ("Amigo 5",
     '"The three gears visual is the moment it clicked. Not three separate problems —\n'
     ' one system. Break one gear and the other two lose power.\n'
     ' I\'d genuinely never thought about it that way."'),
]
for name, comment in friend_comments:
    flow.append(Paragraph(f"<b>{name}:</b>", NOTE_S))
    for line in comment.split('\n'):
        flow.append(code(line))
    flow.append(sp(1))
flow.append(hr())

# ── REDDIT ──
flow += [
    time_block("T + 60 min  (1h después de publicar)"),
    sec("11. REDDIT — staggered, 30 min entre cada uno"),
    cb("r/personalfinance  — primero"),
    cb("r/BehavioralEconomics — +30 min"),
    cb("r/psychology — +30 min (radish experiment / Schultz)"),
    cb("r/cogsci — +30 min"),
    sp(2),
    note("TÍTULO REDDIT (r/psychology / r/BehavioralEconomics):"),
    code('"Wolfram Schultz proved the brain releases dopamine before the money leaves'),
    code("the account. The decision is already made. By payday, after 5 days of"),
    code("micro-choices, you have the least willpower exactly when you need the most."),
    code('(Short video mapping the 3 traps and why they scale with income)"'),
    sp(2),
    note("TÍTULO REDDIT (r/personalfinance):"),
    code('"Researchers at Princeton found that behavioral traps consume the same % of'),
    code("income at 50K as at 150K. It\'s not a salary problem — it\'s a system problem."),
    code("Mapped the 3 specific programs that activate every payday and why naming them"),
    code('isn\'t enough to stop them. (Short video)"'),
    hr(),
]

# ── LINKEDIN ──
flow += [
    sec("12. LINKEDIN POST"),
    code("Most people think they have a spending problem."),
    code(""),
    code("They don't. They have a rewiring problem."),
    code(""),
    code("Every payday, your brain runs 3 programs that were designed for a world"),
    code("that no longer exists — and they consume roughly the same % of your income"),
    code("whether you earn 30K or 150K."),
    code(""),
    code("Wolfram Schultz (Nobel, Cambridge) proved the dopamine fires before you"),
    code("spend a single euro. The decision is already made."),
    code(""),
    code("Richard Thaler (Nobel, Chicago) proved you treat money differently"),
    code("depending on which mental box it's in — even when the math is identical."),
    code(""),
    code("David Laibson (Harvard) proved your future self doesn't feel like you."),
    code("So you don't sacrifice for him."),
    code(""),
    code("We mapped all three in 10 minutes."),
    code(""),
    code("[link to V11 in first comment — NOT in post body]"),
    hr(),
]

# ── SECUENCIA DE LANZAMIENTO ──
flow += [
    sec("SECUENCIA COMPLETA"),
    cb("T+00:00 — 8 amigos reciben link privado · empiezan a ver"),
    cb("T+00:20 — Video pasa a PÚBLICO"),
    cb("T+00:25 — Pegar comentario fijado INMEDIATAMENTE"),
    cb("T+00:35 — LinkedIn live (link en primer comentario)"),
    cb("T+00:35 a T+01:15 — Amigos postean comentarios (uno cada 3-4 min)"),
    cb("T+02:00 — Respondés a TODOS los comentarios"),
    cb("T+01:00 — Reddit: r/personalfinance"),
    cb("T+01:30 — Reddit: r/BehavioralEconomics"),
    cb("T+02:00 — Reddit: r/psychology"),
    cb("T+02:30 — Reddit: r/cogsci"),
    hr(),
]

# ── FOOTER ──
flow += [
    sp(4),
    Paragraph(
        "NEUROCENTS · V11 · LAUNCH CHECKLIST · "
        "3 Traps That Rewire Your Brain to Stay Broke · 20:15 Bali",
        FOOT_S),
]

out = "/home/user/Claudeeee/V11_Launch_Checklist.pdf"
doc = SimpleDocTemplate(out, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)
doc.build(flow)
print(f"Saved: {out}")
