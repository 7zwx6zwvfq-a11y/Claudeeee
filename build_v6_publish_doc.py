#!/usr/bin/env python3
"""Pre-publish checklist document for V6 — Status Quo Bias."""

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
r = t.add_run("NEUROCENTS — VIDEO 6 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Status Quo Bias · Bank Defaults · Lunes 9 Junio 2026")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. FILE NAME ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "status-quo-bias-bank-fees-pension-default-neurocents.mp4",
                GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — 92/100 VidIQ")
add_label_value(doc, "TÍTULO", "The Billion-Dollar Bet Your Bank Wins Every Single Day", DARK, 12)
add_block(doc, "vs título anterior: 'The Billion-Dollar Bet Your Bank Is Making Against You Right Now' = 83/100  →  +9 puntos con el nuevo",
          size=8, color=GREY)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "Jake's pension has been on the default setting since he was 22.",
    "He knew he should check it. He meant to. He never did.",
    "",
    "At 55, he compared his fund to Marcus — same salary, same contributions, same company.",
    "Marcus switched to a low-cost index fund fifteen years ago.",
    "Fee difference: 1.5% vs 0.3%. Same money. Same time. Same market.",
    "Different default.",
    "",
    "The gap: $40,000. Gone. Not stolen. Just... never moved.",
    "",
    "This is status quo bias. The most profitable cognitive bias in the financial industry",
    "— and the one your bank spent billions engineering into your account.",
    "",
    "In this video:",
    "→ Why 99.98% of Austrians are organ donors (and 12% of Germans)",
    "→ The one-checkbox experiment that changed retirement policy forever",
    "→ How your pension default was chosen — and who chose it",
    "→ Why knowing about it is not enough to escape it",
    "→ The three moves that override the default",
    "",
    "───────────────────────────────",
    "📌 Watch this next → [PEGA AQUÍ URL DE V9]",
    "───────────────────────────────",
    "",
    "0:00 The trap",
    "0:45 The decisions you never made",
    "1:25 The organ donation experiment",
    "3:20 Status quo bias — what it is",
    "4:15 The pension default study",
    "5:40 Why your brain stays put",
    "7:00 The popular misreading",
    "8:10 How your bank engineered this",
    "10:10 The real cost",
    "11:20 How to escape the default",
    "11:55 The bank's billion-dollar bet",
    "",
    "#statusquobias #behavioralfinance #personalfinance",
]

for line in desc_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)
    if line.startswith("Jake's pension") or line.startswith("This is status quo"):
        r.bold = True

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — testeados VidIQ (copia todo el bloque)")
tags = ("status quo bias, status quo bias explained, cognitive bias, behavioral finance, "
        "behavioural economics, financial psychology, how to save money, personal finance, "
        "mind hacks, pension fees, bank fees, default effect, endowment effect, "
        "decision making, daniel kahneman, cognitive biases, behavioral economics, "
        "anchoring bias, loss aversion, psychology of money, neurocents")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE VIDIQ:", size=8, bold=True, color=GREY)
kw_rows = [
    ("how to save money",          "254K/mes", "48.5 comp.", "69 ← volumen alto"),
    ("mind hacks",                 "25K/mes",  "31.9 comp.", "67 ← gema oculta"),
    ("status quo bias explained",  "5K/mes",   "17.3 comp.", "66 ← baja comp."),
    ("best bank for savings",      "9.9K/mes", "29.8 comp.", "64"),
    ("status quo bias",            "4.2K/mes", "23.6 comp.", "63"),
    ("behavioural economics",      "13.6K/mes","41.2 comp.", "61"),
    ("cognitive biases",           "66.7K/mes","55 comp.",   "61"),
    ("high yield savings account", "53K/mes",  "50.4 comp.", "62"),
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
add_label_value(doc, "ESTADO", "✅ Hecha — fondo amarillo, $40,000, brain villain en ventanilla, Jake en shock")
add_label_value(doc, "TEXTO", "YOUR BANK WON  /  $40,000  /  you never checked.")
add_block(doc, "Score thumbnail: pendiente de subir URL a VidIQ (necesita estar publicada)", size=8, color=GREY)

divider(doc)

# ── 6. CONFIGURACIÓN YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes = [
    "Título:         The Billion-Dollar Bet Your Bank Wins Every Single Day",
    "Descripción:    Pegada completa con capítulos y URL de V9",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — fondo amarillo, $40,000 centro",
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
add_checkbox(doc, "Vídeo: seleccionar V9 (Salary Anchor) manualmente — NO 'mejor opción'")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Después de publicar V6: entrar a V9 y actualizar end screen apuntando a V6 específico",
          size=8, color=RED)
add_block(doc, "⚠ Entrar a V1 y actualizar end screen / cards apuntando a V6 si es relevante",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~4:15 → card apuntando a V9 (salary negotiation — mismo tema dinero)")
add_checkbox(doc, "Minuto ~8:10 → card apuntando a V1 (hyperbolic discounting — mismo tema banco)")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V6 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden: V6 primero, V9 segundo, V1 tercero")
add_checkbox(doc, "Pegar URL de playlist en descripción de V6")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Your pension is probably on the same default it was set to on your first day.\n"
    "Not because you chose it. Because no one made you change it.\n"
    "Drop 🧠 if you've never actually looked at your fund allocation."
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. REDDIT ──
add_section(doc, "11. REDDIT — publicar después de que el vídeo lleve 1h live")
reddit_posts = [
    ("r/personalfinance",       "Esperar 30 min entre posts"),
    ("r/BehavioralEconomics",   "+30 min"),
    ("r/careerguidance",        "+30 min"),
    ("r/cogsci",                "+30 min — si no shadowban"),
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
r = p.add_run("I made a video about the fee difference that cost someone $40,000 — and they never noticed")
r.font.size = Pt(9)
r.font.color.rgb = DARK

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "BALI", "20:00 – 22:00", GREEN, 12)
add_label_value(doc, "EST",  "12:00 – 14:00 (prime time USA lunes)", GREY, 9)
add_label_value(doc, "NOTA", "Lunes 9 Junio 2026 — consistencia con V1 y V9", GREY, 9)

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V6 · PRE-PUBLISH CHECKLIST · Título 92/100 VidIQ · Tags testeados")
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V6_Prepublish_Checklist.docx"
doc.save(path)
print(f"Saved: {path}")
