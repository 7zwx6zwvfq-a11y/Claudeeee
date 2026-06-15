#!/usr/bin/env python3
"""Pre-publish checklist document for V7 — Availability Heuristic / FOMO Investing."""

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

doc = Document()
st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(10)

# ── HEADER ──
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("NEUROCENTS — VIDEO 7 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Availability Heuristic · FOMO Investing · Lunes 16 Junio 2026")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. FILE NAME ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO",
                "someone-needs-you-to-buy-at-the-top-fomo-availability-heuristic-neurocents.mp4",
                GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — testear en VidIQ antes de publicar")
add_label_value(doc, "TÍTULO", "Someone Needs You to Buy at the Top. Here's Who.", DARK, 12)
add_block(doc, "Alternativa A: 'The Person Who Needed You to Buy at the Top (It Wasn't the Market)' — testear score",
          size=8, color=GREY)
add_block(doc, "Alternativa B: 'Why Everyone Always Buys at the Top — And Who Designed It' — testear score",
          size=8, color=GREY)
add_block(doc, "⚠ Elegir el que saque mayor score VidIQ. El título original tiene gancho fuerte — mantenerlo si es ≥85.",
          size=8, color=RED)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "In October 1929, Joseph Kennedy had his shoes shined.",
    "The shoeshine boy started giving him stock tips.",
    "",
    "Kennedy walked back to his office and sold everything.",
    "Three weeks later, the market collapsed.",
    "Kennedy's fortune was intact. Everyone else lost everything.",
    "",
    "He wasn't smarter than the market. He understood something simpler:",
    "by the time the shoeshine boy knows which stocks to buy,",
    "the people who knew first have been waiting for you.",
    "",
    "This is the availability heuristic — the reason your brain reads media noise",
    "as certainty. And the reason the week everyone's talking about something",
    "is the worst week to buy it.",
    "",
    "In this video:",
    "→ The information hierarchy — who knows first, and in what order",
    "→ The availability heuristic — why ubiquitous information feels like certainty",
    "→ 400 years of the same pattern: tulips, South Sea, dot-com, Dogecoin",
    "→ Why professional fund managers fall for it exactly like you do",
    "→ How financial media's business model is structurally against your portfolio",
    "→ Robert Shiller's Nobel Prize research — and the one rule that changes everything",
    "",
    "───────────────────────────────",
    "📌 Watch this next → [PEGA AQUÍ URL DE V10]",
    "───────────────────────────────",
    "",
    "0:00 The pull",
    "0:30 The shoeshine boy — Kennedy, 1929",
    "1:45 What Kennedy understood",
    "2:45 The mechanism — availability heuristic",
    "4:00 400 years: tulips → South Sea → dot-com → Dogecoin",
    "5:30 The popular misreading",
    "6:30 The industry — financial media's real incentive",
    "7:45 Robert Shiller — narrative economics (Nobel 2013)",
    "9:00 What you can do",
    "10:15 You were not late. You were targeted.",
    "",
    "#FOMO #behavioralfinance #investingpsychology",
]

for line in desc_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)
    if line.startswith("In October 1929") or line.startswith("This is the availability"):
        r.bold = True

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — testeados VidIQ (copia todo el bloque)")
tags = ("availability heuristic, FOMO investing, financial FOMO, behavioral finance, "
        "investment psychology, cognitive bias, herd mentality investing, financial bubble, "
        "stock market psychology, how to avoid FOMO, narrative economics, robert shiller, "
        "crypto bubble, dot com bubble, greater fool theory, behavioral economics, "
        "financial psychology, decision making, neurocents")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE VIDIQ (estimados — confirmar en VidIQ antes de publicar):", size=8, bold=True, color=GREY)
kw_rows = [
    ("FOMO investing",                   "~89K/mes",  "~42 comp.",  "← testear"),
    ("availability heuristic",           "~18K/mes",  "~22 comp.",  "← gema oculta"),
    ("stock market psychology",          "~54K/mes",  "~45 comp.",  "← volumen alto"),
    ("behavioral finance",               "103K/mes",  "27 comp.",   "73 ← confirmado"),
    ("how to avoid FOMO",                "~31K/mes",  "~38 comp.",  "← testear"),
    ("financial bubble",                 "~22K/mes",  "~35 comp.",  "← testear"),
    ("herd mentality investing",         "~12K/mes",  "~28 comp.",  "← baja comp."),
    ("narrative economics",              "~3K/mes",   "~15 comp.",  "← nicho fuerte"),
]
for kw, vol, comp, score in kw_rows:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<40}")
    r1.font.size = Pt(8)
    r2 = p.add_run(f"{vol:<14}{comp:<16}{score}")
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

divider(doc)

# ── 5. MINIATURA ──
add_section(doc, "5. MINIATURA")
add_label_value(doc, "CONCEPTO",
                "Fondo rojo/urgente. Alex mirando gráfico subiendo. Brain Villain susurrando al oído.")
add_label_value(doc, "TEXTO",
                "THEY NEEDED A BUYER  /  AT THE TOP  /  (pequeño: you were targeted)")
add_block(doc, "Alternativa: fondo negro, gráfico subiendo en verde que colapsa en rojo, texto 'WHO NEEDED YOU TO BUY?'",
          size=8, color=GREY)
add_block(doc, "Score thumbnail: pendiente de subir URL a VidIQ (necesita estar publicada)", size=8, color=GREY)

divider(doc)

# ── 6. CONFIGURACIÓN YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes = [
    "Título:         Someone Needs You to Buy at the Top. Here's Who.",
    "Descripción:    Pegada completa con capítulos y URL de V10",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — fondo rojo, THEY NEEDED A BUYER",
    "Capítulos:      Activados (añadidos en descripción con timestamps)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado para 20:00-22:00 hora Bali",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
]
for cb in checkboxes:
    add_checkbox(doc, cb)

divider(doc)

# ── 7. END SCREEN ──
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: seleccionar V10 (Sunk Cost — Your Brain Won't Let You Quit) — NO 'mejor opción'")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Después de publicar V7: entrar a V10 y actualizar end screen apuntando a V7 específico",
          size=8, color=RED)
add_block(doc, "⚠ Lógica: V7 (compras en el pico por FOMO) → V10 (no puedes salir por sunk cost) = secuencia natural",
          size=8, color=GREY)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~4:00 → card apuntando a V10 (sunk cost — no saber cuándo salir)")
add_checkbox(doc, "Minuto ~7:45 → card apuntando a V6 (status quo — defaults en inversión)")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V7 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden actualizado: V7 primero, V10 segundo, V6 tercero, V9 cuarto")
add_checkbox(doc, "Pegar URL de playlist en descripción de V7")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "The week everyone in your life was talking about the same stock, coin, or sector —\n"
    "that was not the signal to buy. That was the exit signal for the people who knew first.\n"
    "Drop 🧠 if you've ever felt the pull and wished you'd moved sooner."
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. REDDIT ──
add_section(doc, "11. REDDIT — publicar después de que el vídeo lleve 1h live")
reddit_posts = [
    ("r/personalfinance",       "Esperar 30 min entre posts"),
    ("r/BehavioralEconomics",   "+30 min"),
    ("r/investing",             "+30 min"),
    ("r/CryptoCurrency",        "+30 min — Dogecoin mencionado específicamente"),
]
for sub, timing in reddit_posts:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<32}")
    r1.font.size = Pt(9)
    r1.bold = True
    r2 = p.add_run(timing)
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

doc.add_paragraph()
add_block(doc, "TÍTULO REDDIT (mismo para todos los subs):", size=8, bold=True, color=GREY)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "In 1929, a shoeshine boy gave Joseph Kennedy stock tips. Kennedy sold everything. "
    "Three weeks later, the market collapsed. (Made a video on why this pattern repeats every decade)"
)
r.font.size = Pt(9)
r.font.color.rgb = DARK

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "BALI", "20:00 – 22:00", GREEN, 12)
add_label_value(doc, "EST",  "12:00 – 14:00 (prime time USA lunes)", GREY, 9)
add_label_value(doc, "NOTA", "Lunes 16 Junio 2026 — consistencia cadencia semanal", GREY, 9)

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V7 · PRE-PUBLISH CHECKLIST · Score VidIQ pendiente · Tags a confirmar")
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V7_Prepublish_Checklist.docx"
doc.save(path)
print(f"Saved: {path}")
