#!/usr/bin/env python3
"""Pre-publish checklist — V16 · Every Money Bias & Its Effect Explained in 8 Minutes."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

RED   = RGBColor(0xB0, 0x2A, 0x2A)
DARK  = RGBColor(0x2C, 0x3E, 0x50)
GREY  = RGBColor(0x77, 0x77, 0x77)
GREEN = RGBColor(0x1A, 0x7A, 0x3C)

def add_section(doc, title):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(14); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(f"── {title} ──"); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = RED

def add_label_value(doc, label, value, value_color=None, value_size=10):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(2)
    lr = p.add_run(f"{label}:  "); lr.bold = True; lr.font.size = Pt(9); lr.font.color.rgb = GREY
    vr = p.add_run(value); vr.font.size = Pt(value_size)
    if value_color: vr.font.color.rgb = value_color

def add_block(doc, text, size=9, color=None, bold=False, indent=False):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    if indent: p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(text); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color

def add_checkbox(doc, text, size=10):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(f"☐  {text}"); r.font.size = Pt(size)

def divider(doc):
    p = doc.add_paragraph("─" * 90); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    for r in p.runs: r.font.size = Pt(7); r.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)

def add_text_block(doc, lines, size=9, indent=True):
    for line in lines:
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
        if indent: p.paragraph_format.left_indent = Cm(0.5)
        r = p.add_run(line); r.font.size = Pt(size)

doc = Document()
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)

t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("NEUROCENTS — VIDEO 16 · PRE-PUBLISH CHECKLIST"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RED
s = doc.add_paragraph(); s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Every Money Bias & Its Effect Explained in 8 Minutes · CATÁLOGO (patrón 4.9M) · 20:15 España / 14:15 EST")
r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()

# 1
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "every-money-bias-explained-8-minutes-behavioral-finance-neurocents.mp4", GREEN, 10)
divider(doc)

# 2
add_section(doc, "2. TÍTULO — espejo del outlier 4.9M")
add_label_value(doc, "TÍTULO PRINCIPAL", "Every Money Bias & Its Effect Explained in 8 Minutes", DARK, 12)
add_block(doc, "Patrón: 'Every X & Its Effect Explained in N Minutes' — formato catálogo validado con 4.9M views.", size=8, color=GREY)
add_block(doc, "Ajustar '8 Minutes' a la duración real del montaje final (±1 min OK; si sale 9:00+, poner 9).", size=8, color=RED)
add_block(doc, "Keyword: behavioral finance (98K · 75.0) + cognitive biases money (4.9K · 59.6) integrados en descripción/tags.", size=8, color=GREY)
divider(doc)

# 3
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")
desc = [
    "Your brain came pre-installed with 10 programs that decide what you buy,",
    "what you keep, and what you can't let go of. Nobody showed you the catalog. This is the catalog.",
    "",
    "Each bias explained like a substance — with its onset, its peak, and its comedown:",
    "→ Anchoring — you never buy the thing, you buy the distance from the first number",
    "→ Loss Aversion — your brain protects the feeling of not losing, not the money",
    "→ Mental Accounting — money doesn't come with labels; your brain prints them",
    "→ Present Bias — it borrows money from someone you haven't met yet: you",
    "→ Herd Instinct — there are no lions at the mall",
    "→ Lifestyle Inflation — a raise makes your old life unaffordable",
    "→ Sunk Cost — buying tickets to watch it sink",
    "→ The Optimism Loop — a great life partner, a terrible accountant",
    "→ Default Bias — the most expensive decisions are the ones you never made",
    "→ Scarcity Mindset — a full-time job your brain works for free",
    "",
    "───────────────────────────────",
    "📌 Watch next → [PEGA AQUÍ URL DE V15 — hasta que exista V17, luego cambiar a V17]",
    "───────────────────────────────",
    "",
    "0:00 Anchoring",
    "0:50 Loss Aversion",
    "1:40 Mental Accounting",
    "2:25 Present Bias",
    "3:10 Herd Instinct",
    "3:55 Lifestyle Inflation",
    "4:40 Sunk Cost",
    "5:25 The Optimism Loop",
    "6:05 Default Bias",
    "6:45 Scarcity Mindset",
    "7:40 The Catalog",
    "",
    "(Timestamps aproximados — ajustar al vídeo real. Los capítulos son CRÍTICOS en este formato:",
    "el vídeo-referencia vive de que la gente salte a 'su' sesgo y vuelva.)",
    "",
    "#behavioralfinance #cognitivebiases #psychologyofmoney #financialpsychology #neurocents",
]
add_text_block(doc, desc, size=9, indent=True)
divider(doc)

# 4
add_section(doc, "4. TAGS — copia todo el bloque en YouTube Studio")
tags = ("behavioral finance, cognitive biases money, psychology of money, financial psychology, "
        "every bias explained, anchoring bias, loss aversion, mental accounting, present bias, "
        "herd mentality money, lifestyle inflation, sunk cost fallacy, optimism bias, default bias, "
        "scarcity mindset, money psychology, brain and money, behavioral economics, "
        "cognitive bias examples, neurocents")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags); r.font.size = Pt(9); r.font.color.rgb = DARK
doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE:", size=8, bold=True, color=GREY)
for kw, vol, comp, score in [
    ("behavioral finance",      "98K/mes",  "24.2 comp.", "75.0  ← primario"),
    ("financial psychology",    "120K/mes", "27 comp.",   "74.7  ← primario"),
    ("psychology of money",     "731K/mes", "57.5 comp.", "69.5  ← alto volumen"),
    ("cognitive biases money",  "4.9K/mes", "33.7 comp.", "59.6  ← exact-match tema"),
    ("sunk cost fallacy",       "~40K/mes", "~35 comp.",  "búsqueda evergreen"),
    ("loss aversion",           "~30K/mes", "~30 comp.",  "búsqueda evergreen"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<32}"); r1.font.size = Pt(8)
    r2 = p.add_run(f"{vol:<12}{comp:<14}{score}"); r2.font.size = Pt(8); r2.font.color.rgb = GREY
divider(doc)

# 5
add_section(doc, "5. MINIATURA — GRID de 10 círculos (Opción A, espejo del 4.9M)")
add_label_value(doc, "CONCEPTO", "Grid 2×5 de círculos de colores con icono-OBJETO negro por sesgo + labels — SIN personaje")
add_label_value(doc, "HEADER", "MONEY BIASES (negro) + EXPLAINED (rojo #C62828) — Impact ultra-bold")
add_label_value(doc, "FONDO", "BLANCO puro. Flat, sin sombras, sin gradientes.")
add_block(doc, "■ Iconos = OBJETOS reconocibles por silueta (etiqueta tachada, moneda rota, sobres, reloj de arena, "
               "ovejas, globo €, barco hundiéndose, sol/calendario, bucle, túnel) — NUNCA conceptos abstractos.", size=8, color=RED)
add_block(doc, "■ Plan B si a 200px se vuelve ruido: Opción C — 5 círculos GRANDES + 'WHICH ONE OWNS YOU?' "
               "(ver V16_Thumbnail_Prompts.txt). Opción B (Villain dealer) = variante para swap a las 48h si CTR <5%.", size=8, color=GREY)
add_block(doc, "■ Test obligatorio a 200px antes de subir: header legible + los 10 círculos distinguibles como formato.", size=8, color=RED)
divider(doc)

# 6
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
for cb in [
    "Título:         Every Money Bias & Its Effect Explained in 8 Minutes (ajustar minutos al montaje)",
    "Descripción:    Pegada completa — 10 sesgos + CAPÍTULOS (críticos en formato catálogo)",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Grid 10 círculos, header MONEY BIASES EXPLAINED, fondo blanco",
    "Capítulos:      Activados — un capítulo por sesgo, nombres exactos de los sesgos",
    "Subtítulos:     Auto-generados (dejar activado)",
    "Visibilidad:    Público — programado HOY 20:15 CEST (= 14:15 EST)",
    "Marca de agua:  Neurocents_Watermark.png",
]:
    add_checkbox(doc, cb)
add_block(doc, "⚠ EDICIÓN: este vídeo NO tiene hook — empieza 'Anchoring. Anchoring is...' en el segundo 0. "
               "No añadir intro, ni logo animado, ni 'welcome back'. El primer frame es el badge teal.", size=8, color=RED)
divider(doc)

# 7
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: V15 (Why Smart People Can't Save Money) — hasta que V17 exista, luego actualizar a V17")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Cuando publiques V17: volver aquí y apuntar el end screen a V17 (el tease 'two people, same salary' es V17).", size=8, color=RED)
divider(doc)

# 8
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~4:40 (Sunk Cost) → card a V10 (Sunk Cost deep-dive) — el catálogo alimenta al catálogo antiguo")
add_checkbox(doc, "Minuto ~6:45 (Scarcity) → card a V3 (Bandwidth Tax) — tema hermano")
divider(doc)

# 9
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V16 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Considerar playlist nueva 'The Bias Catalog' con V16 como cabecera + los deep-dives antiguos (V5, V6, V10...)")
add_checkbox(doc, "Pegar URL de playlist en descripción")
divider(doc)

# 10
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Ten programs. One brain.\n\n"
    "Which one owns you? Name yours below — I'll tell you which deep-dive to watch next.\n\n"
    "(Mine is the Optimism Loop. 'Next month' has been coming for nine years.)"
)
r.font.size = Pt(10); r.font.color.rgb = DARK
divider(doc)

# 11
add_section(doc, "11. REDDIT — publicar 1h después de que el vídeo esté live")
for sub, note in [
    ("r/BehavioralEconomics", "Primero — es literalmente su tema; el ángulo onset/peak/comedown es novedoso"),
    ("r/personalfinance",     "+30 min — ángulo 'the catalog nobody shows you'"),
    ("r/psychology",          "+30 min — sesgos como sustancias (frame nuevo)"),
    ("r/cogsci",              "+30 min — the 10-program pre-install"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<28}"); r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(note); r2.font.size = Pt(8); r2.font.color.rgb = GREY
doc.add_paragraph()
add_block(doc, "BORRADOR r/BehavioralEconomics:", size=9, bold=True, color=DARK)
add_text_block(doc, [
    "",
    "Title: I described the 10 most-studied money biases the way we describe substances — onset, peak, comedown. The parallels are uncomfortable.",
    "",
    "Anchoring's onset is instant (the crossed-out price does all the thinking). Lifestyle inflation",
    "behaves like tolerance — the dose rises, the effect doesn't. Sunk cost has withdrawal ('but I've",
    "already put so much in'). And scarcity mindset is the heavy one: active financial scarcity can",
    "consume more cognitive capacity than a sleepless night (Mani et al., 2013).",
    "",
    "Framing biases as substances made them click for people who tune out at 'cognitive bias':",
    "everyone understands onset, peak, comedown and tolerance.",
    "",
    "Made a video cataloguing all ten this way: [URL]",
    "",
    "Which of the ten do you think has the strongest 'withdrawal' effect?",
], size=8, indent=True)
divider(doc)

# 12
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "HOY 20:15", GREEN, 12)
add_label_value(doc, "EST (USA)", "14:15 — prime time East Coast", GREY, 9)
add_label_value(doc, "UTC", "18:15", GREY, 9)
add_label_value(doc, "SECUENCIA", "V16 catálogo → V17 comparativa (tease final) → V18 señales", GREY, 9)
divider(doc)

# 13
add_section(doc, "13. NOTAS — por qué este formato y este título")
for note in [
    "→ FORMATO: Catálogo (Formato 9) — espejo del outlier más grande analizado (4.9M). El valor es la densidad: "
    "10 items completos, micro-plantilla idéntica, frase lapidaria por sesgo.",
    "→ CERO HOOK: el título es el contrato (S24-P15). El viewer que clickó ya sabe qué viene. Valor en el segundo 1.",
    "→ EL GIRO ÚNICO: sesgos tratados como sustancias (onset/peak/comedown/tolerancia). Nadie lo hace en el nicho dinero.",
    "→ ESCALADA: Anchoring (lo que consume todo el mundo a diario) → Scarcity Mindset (el 'heavy one', tono serio). "
    "Patrón cafeína→opioides del original.",
    "→ EVERGREEN: vídeo-referencia — la gente lo guarda, lo comparte y lo re-busca. Los capítulos por sesgo son clave.",
    "→ SIN ALEX en guión (regla Reducir Alex) — Brain Villain aislado como host/curador en las imágenes.",
    "→ INDEPENDENCIA: cero referencias a otros vídeos. Los sesgos con vídeos antiguos individuales reciben card, no mención.",
    "→ CTR TARGET: >6% primeras 48h. Retención 30s: >50% (sin hook, el que entra ya viene comprometido). "
    "Si CTR <5% a las 48h → swap a thumbnail Opción C.",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note); r.font.size = Pt(9); r.font.color.rgb = DARK
divider(doc)

doc.add_paragraph()
foot = doc.add_paragraph(); foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V16 · PRE-PUBLISH CHECKLIST · Every Money Bias & Its Effect Explained · 20:15 España")
fr.font.size = Pt(8); fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V16_final_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
