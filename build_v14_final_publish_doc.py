#!/usr/bin/env python3
"""Pre-publish checklist — V14 · 5 Things That Drain Your Money Before Payday (No Matter What You Earn)."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

RED   = RGBColor(0xB0, 0x2A, 0x2A)
DARK  = RGBColor(0x2C, 0x3E, 0x50)
GREY  = RGBColor(0x77, 0x77, 0x77)
GREEN = RGBColor(0x1A, 0x7A, 0x3C)

def add_section(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(f"── {title} ──")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RED

def add_label_value(doc, label, value, value_color=None, value_size=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    lr = p.add_run(f"{label}:  ")
    lr.bold = True
    lr.font.size = Pt(9)
    lr.font.color.rgb = GREY
    vr = p.add_run(value)
    vr.font.size = Pt(value_size)
    if value_color:
        vr.font.color.rgb = value_color

def add_block(doc, text, size=9, color=None, bold=False, indent=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    if indent:
        p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    if color:
        r.font.color.rgb = color

def add_checkbox(doc, text, size=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(f"☐  {text}")
    r.font.size = Pt(size)

def divider(doc):
    p = doc.add_paragraph("─" * 90)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    for r in p.runs:
        r.font.size = Pt(7)
        r.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)

def add_text_block(doc, lines, size=9, indent=True):
    for line in lines:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if indent:
            p.paragraph_format.left_indent = Cm(0.5)
        r = p.add_run(line)
        r.font.size = Pt(size)

# ── DOCUMENT ──
doc = Document()
st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(10)

# ── HEADER ──
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("NEUROCENTS — VIDEO 14 FINAL · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("5 Things That Drain Your Money Before Payday (No Matter What You Earn) · 20:15 España / 14:15 EST")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. NOMBRE ARCHIVO ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO",
    "5-things-drain-money-before-payday-financial-psychology-neurocents.mp4",
    GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — fórmula sector-wide S22 · lista con ranking")
add_label_value(doc,
    "TÍTULO PRINCIPAL",
    "5 Things That Drain Your Money Before Payday (No Matter What You Earn)",
    DARK, 12)
add_block(doc,
    "Fórmula: sector-wide universal (S22) — 'broke before payday' es tema del 99% de la audiencia "
    "financiera, no sub-nicho behavioral finance. El ángulo psicológico es el giro interno, no el gancho.",
    size=8, color=GREY)
add_block(doc,
    "Patrón validado: número + verbo/consecuencia negativa + paréntesis contrapunto "
    "'(No Matter What You Earn)' — elimina la excusa de ingresos antes de que el viewer la piense.",
    size=8, color=GREY)
add_block(doc,
    "NO repite ningún título anterior (V1-V13 revisados). Diferenciado de V13 (rewires/neuroplasticidad) "
    "y de V12 (3 Reasons/Every Payday) — mismo tema payday, ángulo distinto: los 5 drenajes, no las 3 razones.",
    size=8, color=RED)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "Why does your money always disappear before payday? Not sometimes. Every month.",
    "",
    "It doesn't matter if you earn €2,000 or €6,000. Four weeks. Same empty account.",
    "",
    "5 things are draining your money before payday — and none of them feel like mistakes",
    "when they happen. The worst one runs before the money even arrives.",
    "",
    "These aren't budgeting mistakes. They're not discipline failures.",
    "They're patterns. And they run automatically.",
    "",
    "In this video:",
    "→ #5 — The Card Gap: why card payments silence the part of your brain that registers loss",
    "→ #4 — The Reward Drain: the sentence that has cost more than any impulse purchase",
    "→ #3 — The Invisible Drain: why your brain doesn't cancel things, it lets them run",
    "→ #2 — Social Spending: the most expensive audience in your life has never spent a dollar",
    "→ #1 — The Pre-Spend: the one nobody names. It runs before the money arrives.",
    "→ The structural fix for each drain — no willpower required",
    "",
    "───────────────────────────────",
    "📌 Watch next → [PEGA AQUÍ URL DE V15 — 'the one decision that stops all five']",
    "📌 Previous: 5 Ways Your Brain Physically Rewires Itself to Stay Broke → [PEGA AQUÍ URL DE V13]",
    "───────────────────────────────",
    "",
    "0:00 Why your money disappears before payday",
    "0:30 These aren't budgeting mistakes",
    "0:45 #5 — The Card Gap",
    "1:15 #4 — The Reward Drain",
    "1:45 #3 — The Invisible Drain",
    "2:15 CTA",
    "2:25 #2 — Social Spending",
    "2:55 #1 — The Pre-Spend (the one nobody names)",
    "3:40 Five patterns, running automatically",
    "4:00 The structural fix — one per drain",
    "4:40 Brain Villain's last trick",
    "5:20 You're not bad with money",
    "5:45 Next week: the one decision",
    "",
    "(Timestamps aproximados — ajustar a duración real del vídeo montado)",
    "",
    "#behavioralfinance #financialpsychology #psychologyofmoney #personalfinance #neurocents",
]

add_text_block(doc, desc_lines, size=9, indent=True)

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — copia todo el bloque en YouTube Studio")
tags = (
    "behavioral finance, financial psychology, psychology of money, why am I broke before payday, "
    "broke before payday, money psychology, brain and money, cognitive biases money, why money disappears, "
    "neuroscience finance, personal finance psychology, card gap, reward drain, invisible drain, "
    "social spending, pre-spend, money patterns, why you can't save money, financial behavior, "
    "money habits, brain villain, subscription drain, impulsive spending psychology, "
    "payday money gone, neurocents"
)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE:", size=8, bold=True, color=GREY)
kw_rows = [
    ("behavioral finance",           "98K/mes",  "24.2 comp.", "75.0  ← primario"),
    ("financial psychology",         "120K/mes", "27 comp.",   "74.7  ← primario"),
    ("psychology of money",          "731K/mes", "57.5 comp.", "69.5  ← alto volumen"),
    ("why can't I save money",       "11.8K/mes","48.5 comp.", "57.1"),
    ("why am I broke before payday", "testear",  "—",          "exact match título"),
    ("broke before payday",          "testear",  "—",          "sector-wide S22"),
    ("cognitive biases money",       "4.9K/mes", "33.7 comp.", "59.6"),
    ("neuroeconomics",               "6.9K/mes", "27.2 comp.", "63.5"),
]
for kw, vol, comp, score in kw_rows:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<32}")
    r1.font.size = Pt(8)
    r2 = p.add_run(f"{vol:<12}{comp:<14}{score}")
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

divider(doc)

# ── 5. MINIATURA ──
add_section(doc, "5. MINIATURA — concepto BROKE / BEFORE / PAYDAY (fondo blanco, S23 aprobado)")
add_label_value(doc, "CONCEPTO", "Alex sosteniendo teléfono con saldo €0.00, boca abierta en shock genuino. "
                                  "Brain Villain dentro del cráneo transparente, brazos cruzados, satisfecho.")
add_label_value(doc, "FONDO", "BLANCO puro — estilo Andy/MoneyTom. NO oscuro, NO gradiente.")
add_label_value(doc, "TEXTO THUMBNAIL", "BROKE / BEFORE / PAYDAY — stacked, BROKE y BEFORE en negro, PAYDAY en rojo (#C62828)")
add_label_value(doc, "OBJETO", "Teléfono con €0.00 en rojo grande + 'AVAILABLE BALANCE' — prop que confirma S17 continuity")
add_label_value(doc, "EXPRESIÓN ALEX", "Boca ABIERTA en shock/dread genuino, ojos grandes — legible a 200px (S23 regla). "
                                        "Neutral/flat = rechazar y regenerar.")
add_block(doc, "■ Blue t-shirt en Alex — NO red. Verificar SIEMPRE en Google Flow antes de generar.", size=8, color=RED)
add_block(doc, "■ Gray pants — NO jeans, NO blue pants. Corrección de la primera iteración (S23).", size=8, color=RED)
add_block(doc, "■ Brain Villain DENTRO del cráneo transparente — NO flotando fuera. Regla absoluta.", size=8, color=RED)
add_block(doc, "APROBADO tras 2 iteraciones en Google Flow (ver S23 en CLAUDE.md) — variante final con boca "
               "abierta y contraste alto es la que se sube.", size=8, color=GREEN)

doc.add_paragraph()
add_block(doc, "DESCARTADO — variante alternativa 'grid de iconos sin personaje':", size=8, bold=True, color=GREY)
add_block(doc, "Se probó un formato viral tipo listicle (5 iconos de color, sin Alex) inspirado en outliers de "
               "'Cada Droga Explicada' / 'Técnicas de Manipulación'. Test a 200px: las 5 etiquetas y el detalle "
               "de cada icono se volvían ilegibles. Se descarta como miniatura principal — queda como asset "
               "opcional para Reddit o capítulos de descripción, donde sí se ve a tamaño completo.", size=8, color=GREY)

divider(doc)

# ── 6. YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes_yt = [
    "Título:         5 Things That Drain Your Money Before Payday (No Matter What You Earn)",
    "Descripción:    Pegada completa — 5 items + timestamps + URLs V13 y V15",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — Alex shock + €0.00 + BROKE/BEFORE/PAYDAY, fondo blanco",
    "Capítulos:      Activados (timestamps en descripción — ajustar al vídeo real)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado JUEVES 20:15 CEST (= 14:15 EST)",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
]
for cb in checkboxes_yt:
    add_checkbox(doc, cb)

divider(doc)

# ── 7. END SCREEN ──
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: seleccionar V13 (mientras V15 no esté publicado) — NO 'mejor opción automática'")
add_checkbox(doc, "Botón suscripción")

doc.add_paragraph()
add_block(doc, "Script end screen:", size=9, bold=True, color=DARK)
add_block(doc,
    "'Next week — the one decision that stops all five. Not five solutions. One. Made once. "
    "Before the patterns activate. See you Thursday.'",
    size=9, indent=True)
doc.add_paragraph()
add_block(doc, "⚠ CRÍTICO — dependencia con V15: en cuanto V15 esté publicado, entrar aquí y actualizar el "
               "end screen de V14 para que apunte a V15 específicamente. Es el payoff del tease — cerrar el loop.",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~2:15 (CTA) → card apuntando a V13 (contexto de trilogía — 5 Ways Rewires)")
add_checkbox(doc, "Minuto ~4:40 (Brain Villain's Last Trick) → card apuntando a V12 (Why Willpower Fails — tema hermano)")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V14 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden secuencial: V13 → V14 → V15 (trilogía 5 rewires → 5 drains → the one fix)")
add_checkbox(doc, "Pegar URL de playlist en descripción de V14")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar (inmediatamente)")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Which of the 5 hit you hardest?\n\n"
    "For me it's always been number 4 — the Reward Drain.\n"
    "The math the brain does on a brutal Thursday is frighteningly fast.\n"
    "Drop yours below 👇\n\n"
    "(Number 1 — the Pre-Spend — is the one nobody names. That's the one that changed how I see payday.)"
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. REDDIT ──
add_section(doc, "11. REDDIT — publicar 1h después de que el vídeo esté live")

reddit_posts = [
    ("r/personalfinance",       "Primero — ángulo de los 5 patrones automáticos, muy activo"),
    ("r/povertyfinance",        "+30 min — el dato de que la timing no cambia con el ingreso"),
    ("r/psychology",            "+30 min — Card Gap / dolor de pago cash vs card"),
    ("r/cogsci",                "+30 min — Pre-Spend / asignación mental antes del ingreso"),
]
for sub, note in reddit_posts:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<32}")
    r1.font.size = Pt(9)
    r1.bold = True
    r2 = p.add_run(note)
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

doc.add_paragraph()
add_block(doc, "FORMATO REDDIT: 150-200 palabras · aporta valor · menciona el vídeo al final de forma natural · no spam", size=8, color=RED)

doc.add_paragraph()
add_block(doc, "BORRADOR r/personalfinance:", size=9, bold=True, color=DARK)
reddit_draft_1 = [
    "",
    "Title: The reason you're broke before payday isn't what you think",
    "",
    "I spent a while mapping why money disappears before payday — not sometimes, but every",
    "single month — even when income goes up.",
    "",
    "Turned out it wasn't budgeting failures. It was 5 specific patterns that run automatically.",
    "The worst one activates before the money even arrives — your brain allocates the salary",
    "mentally days before it lands, so by payday you're just confirming a decision you already made.",
    "",
    "The five: Card Gap, Reward Drain, Invisible Drain, Social Spending, and the Pre-Spend.",
    "None of them feel like mistakes when they happen. That's what makes them effective.",
    "",
    "Made a video going through all five and the structural fix for each: [URL]",
    "",
    "Curious if others recognize any of these. Number 4 — the Reward Drain — seems to be universal.",
]
add_text_block(doc, reddit_draft_1, size=8, indent=True)

doc.add_paragraph()
add_block(doc, "BORRADOR r/povertyfinance:", size=9, bold=True, color=DARK)
reddit_draft_2 = [
    "",
    "Title: 5 things that drain money before payday — regardless of income level",
    "",
    "One thing I kept noticing: the timing doesn't change with income.",
    "€2,000 earners and €6,000 earners hit the same empty account by payday.",
    "",
    "Mapped out 5 patterns that explain why. None of them are about discipline.",
    "They're behavioral — and they have structural fixes, not willpower fixes.",
    "",
    "The one that surprised me most: the Pre-Spend. Your brain allocates your salary",
    "before it arrives. By Friday, it's just processing a transaction that closed on Wednesday.",
    "",
    "Full breakdown here: [URL]",
]
add_text_block(doc, reddit_draft_2, size=8, indent=True)

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "JUEVES 20:15", GREEN, 12)
add_label_value(doc, "EST (USA)",     "14:15 (prime time USA East Coast)", GREY, 9)
add_label_value(doc, "UTC",           "18:15", GREY, 9)
add_label_value(doc, "SECUENCIA",     "V13 ya publicado. V14 continúa la trilogía. V15 en cola tras V14.", GREY, 9)
add_block(doc, "■ Cadencia canal: Lunes y Jueves 20:15 España. V13 publicó en LUNES — dato comparado con V8 "
               "(jueves) mostró arranque mucho más débil (31 vs 1,105 impresiones a 2.5h). V14 publica en "
               "JUEVES para corregir esta variable.", size=8, color=RED)

divider(doc)

# ── 13. NOTAS DE OUTLIER ──
add_section(doc, "13. NOTAS DE OUTLIER — por qué este título y este hook")
notes = [
    "→ TÍTULO: 'broke before payday' — tema sector-wide (S22), no sub-nicho behavioral finance. "
    "Validado tras analizar outliers 'Real Estate Vs Stocks' (1.5M) y 'Leasing Vs Buying A Car' (794K) — "
    "ambos van a preguntas universales, no a jerga de nicho.",
    "→ FORMATO: Lista con Ranking (5→1) — validado en outliers julio 2026 ('5 Habits REWIRING Your Brain "
    "to Stay Broke' 96×). No requiere datos científicos duros — observaciones conductuales fuertes bastan.",
    "→ HOOK BEAT 1 (S1 — Pregunta Sin Resolver): 'Why does your money always disappear before payday?' — "
    "Efecto Zeigarnik. El viewer ya se hace esa pregunta; el video no la responde hasta entrado el video.",
    "→ S17 THUMBNAIL CONTINUITY: Alex + teléfono + €0.00 en Beat 1 — el viewer reconoce la escena del "
    "thumbnail en <5 segundos.",
    "→ ESTRUCTURA 5 DRENAJES: Card Gap (dolor de pago) → Reward Drain (merecimiento) → Invisible Drain "
    "(fricción de decisión) → Social Spending (audiencia fantasma) → Pre-Spend (asignación mental previa, "
    "el reveal final).",
    "→ VILLAIN INOCULATION: 'I already know this' es el Invisible Drain disfrazado de autoconocimiento — "
    "sella el engagement en tiempo real justo cuando el viewer podría desconectar por familiaridad.",
    "→ IDENTITY CLOSE: 'You're not bad with money' — reencuadre no moralista, evita el recap de las 5 "
    "trampas (ya recibidas), cierre en 7 beats.",
    "→ TRILOGÍA: V13 (5 rewires) → V14 (5 drains) → V15 (the one fix) — end screens encadenados "
    "obligatorios para maximizar sesión y dar señal de watch-time acumulado al algoritmo.",
    "→ CTR TARGET: >6% en primeras 48h. Retention at 30s: >45%. Retention at midpoint: >50%.",
]
for note in notes:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note)
    r.font.size = Pt(9)
    r.font.color.rgb = DARK

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run(
    "NEUROCENTS · V14 FINAL · PRE-PUBLISH CHECKLIST · 5 Things That Drain Your Money Before Payday "
    "(No Matter What You Earn) · 20:15 España"
)
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V14_final_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
