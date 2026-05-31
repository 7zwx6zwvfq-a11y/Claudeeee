#!/usr/bin/env python3
"""Pre-publish checklist document for V9 — Anchoring Bias."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

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
r = t.add_run("NEUROCENTS — VIDEO 9 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Anchoring Bias · Salary Negotiation · Lunes 2 Junio 2026")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. FILE NAME ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "salary-anchoring-bias-job-interview-negotiation-neurocents.mp4",
                GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — 86/100 VidIQ")
add_label_value(doc, "TÍTULO", "The Salary Anchor That Compounds Into Poverty", DARK, 12)
add_block(doc, "vs título anterior: 'The First Number They Show You in a Job Interview Is Not an Offer' = 80/100  →  +6 puntos con el nuevo",
          size=8, color=GREY)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "They didn't start at $36,000. They engineered it.",
    "",
    "Jake left that interview thinking he won $3,000.",
    "The salary band was $40,000 to $55,000. Marcus knew the market rate. He got $48,000.",
    "Same company. Same role. Same week. That gap compounds to over $300,000 in lifetime",
    "earnings — for a single conversation Jake didn't know he was allowed to have.",
    "",
    "This is anchoring bias. The salary negotiation trap built into every job interview",
    "— and how to escape it.",
    "",
    "In this video:",
    "→ Why the first number is not an offer",
    "→ How a $9,000 gap becomes $300,000 over a career",
    "→ How HR calibrates the anchor deliberately",
    "→ How to set your own number before they speak",
    "",
    "───────────────────────────────",
    "📌 Watch this next → [PEGA AQUÍ URL DE V1]",
    "───────────────────────────────",
    "",
    "0:00 The trap",
    "0:25 Jake's first interview",
    "1:40 What anchoring bias does to your brain",
    "3:00 Marcus — same role, $9,000 more",
    "4:15 What $9,000 becomes in 30 years",
    "5:30 How HR sets the anchor deliberately",
    "6:45 Why negotiating harder is the wrong answer",
    "7:30 How to escape the anchor",
    "9:00 Jake at 52",
    "",
    "#salarynegotiation #anchoringbias #behavioralfinance",
]

for line in desc_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)
    if line.startswith("They didn't") or line.startswith("This is anchoring"):
        r.bold = True

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — testeados VidIQ (copia todo el bloque)")
tags = ("anchoring bias, salary negotiation, how to negotiate salary, salary negotiation tips, "
        "financial psychology, behavioral finance, anchoring bias in decision making, cognitive bias, "
        "job interview, interview tips, how to negotiate, decision making, behavioral economics, "
        "career advice, daniel kahneman, anchoring effect, loss aversion, neurocents")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE VIDIQ:", size=8, bold=True, color=GREY)
kw_rows = [
    ("anchoring bias in decision making", "3.4K/mes", "6.8 comp.", "69 ← gema oculta"),
    ("financial psychology",              "145K/mes", "26 comp.",  "75"),
    ("behavioral finance",                "103K/mes", "27 comp.",  "73"),
    ("job interview",                     "123K/mes", "53 comp.",  "64"),
    ("decision making",                   "72K/mes",  "47 comp.",  "64"),
    ("how to negotiate salary",           "26K/mes",  "46 comp.",  "61"),
    ("salary negotiation tips",           "13K/mes",  "40 comp.",  "61"),
    ("daniel kahneman",                   "66K/mes",  "49 comp.",  "63"),
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
add_label_value(doc, "ESTADO", "✅ Hecha — brain villain mirando a cámara, personaje en shock, $40K visible")
add_block(doc, "Score thumbnail: pendiente de subir URL a VidIQ (necesita estar publicada)", size=8, color=GREY)

divider(doc)

# ── 6. CONFIGURACIÓN YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes = [
    "Título:         The Salary Anchor That Compounds Into Poverty",
    "Descripción:    Pegada completa con capítulos y URL de V1",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — brain villain mirando cámara",
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
add_checkbox(doc, "Vídeo: seleccionar V1 (Hyperbolic Discounting) manualmente")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Después de publicar V9: entrar a V1 y actualizar end screen apuntando a V9 específico",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~3:00 → card apuntando a V1")
add_checkbox(doc, "Minuto ~6:30 → card apuntando a V1")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Crear playlist: 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Añadir V9 primero, V1 segundo")
add_checkbox(doc, "Pegar URL de playlist en descripción de ambos vídeos")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "The first number they showed you was not random.\n"
    "It was researched. Drop 🧠 if you've ever left an interview\n"
    "thinking you won — and didn't know the salary band."
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
    ("r/financialindependence", "+30 min — si no shadowban"),
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

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "BALI", "20:00 – 22:00", GREEN, 12)
add_label_value(doc, "EST",  "12:00 – 14:00 (prime time USA lunes)", GREY, 9)

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V9 · PRE-PUBLISH CHECKLIST · Título 86/100 VidIQ · Tags testeados")
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V9_Prepublish_Checklist.docx"
doc.save(path)
print(f"Saved: {path}")
