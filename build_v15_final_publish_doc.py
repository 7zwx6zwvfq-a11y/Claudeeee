#!/usr/bin/env python3
"""Pre-publish checklist — V15 · Why Smart People Can't Save Money (Do This Once Instead)."""

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
r = t.add_run("NEUROCENTS — VIDEO 15 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("The One Decision · Manual vs Automatic · Brief v3.1 · Jueves 20:15 CEST · Paga el tease de V14")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. NOMBRE ARCHIVO ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO",
    "why-smart-people-cant-save-money-financial-psychology-neurocents.mp4",
    GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO")
add_label_value(doc,
    "TÍTULO",
    "Why Smart People Can't Save Money (Do This Once Instead)",
    DARK, 12)
add_block(doc,
    "Patrón 993× — amenaza de estatus 'Smart People' + keyword 'can't save money' + paréntesis contrapunto",
    size=8, color=GREY)
add_block(doc,
    "Keyword principal: why can't I save money (11.8K/mes · comp 48.5 · score 57.1) + financial psychology (120K · 74.7) ✅",
    size=8, color=GREY)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "You're smart. You've read the books. You could explain compound interest at a dinner party.",
    "And your savings account has €140 in it.",
    "",
    "It's not discipline. It's that you keep trying.",
    "Trying is manual. And manual always loses to automatic.",
    "",
    "In this video:",
    "→ Why every budget dies with a quiet fade — around day 12 (the 150-decision problem)",
    "→ The math nobody shows you: thirty correct nos. One tired yes. The yes wins.",
    "→ The one decision that answers all five money drains — made once, in ten minutes",
    "→ Madrian & Shea (Harvard, 2001): 37% → 86% savings rate. Nobody became more disciplined.",
    "→ The Brain Villain's last defense: 'What if I need that money?'",
    "",
    "───────────────────────────────",
    "📌 The 5 drains this decision stops → [PEGA AQUÍ URL DE V14]",
    "───────────────────────────────",
    "",
    "0:00 Smart. Still broke.",
    "0:45 Why every method fails the same way",
    "2:00 Machines vs to-do lists",
    "3:20 The one decision",
    "4:40 What it does to all five drains",
    "5:20 The Harvard study (37% → 86%)",
    "6:20 'What if I need that money?'",
    "7:00 You were never bad at saving",
    "",
    "#financialpsychology #behavioralfinance #savemoney",
]

add_text_block(doc, desc_lines, size=9, indent=True)

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — copia todo el bloque")
tags = (
    "financial psychology, behavioral finance, why can't I save money, how to save money, "
    "automatic savings, pay yourself first, save money automatically, money psychology, "
    "default effect, automatic enrollment, behavioral economics, standing order savings, "
    "smart people money, decision fatigue, savings account, personal finance psychology, "
    "brain and money, neurocents"
)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE:", size=8, bold=True, color=GREY)
kw_rows = [
    ("financial psychology",        "120K/mes", "27 comp.",   "74.7  ← principal"),
    ("behavioral finance",          "98K/mes",  "24.2 comp.", "75.0  ← principal"),
    ("why can't I save money",      "11.8K/mes","48.5 comp.", "57.1  ← título"),
    ("how to save money",           "320K/mes", "70 comp.",   "55"),
    ("automatic savings",           "12K/mes",  "38 comp.",   "60"),
    ("pay yourself first",          "18K/mes",  "35 comp.",   "62"),
    ("money psychology",            "9K/mes",   "30 comp.",   "63"),
    ("behavioral economics",        "45K/mes",  "42 comp.",   "62"),
]
for kw, vol, comp, score in kw_rows:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<40}")
    r1.font.size = Pt(8)
    r2 = p.add_run(f"{vol:<14}{comp:<18}{score}")
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

divider(doc)

# ── 5. MINIATURA ──
add_section(doc, "5. MINIATURA")
add_label_value(doc, "CONCEPTO", "Alex con libros de finanzas leídos + móvil con SAVINGS €140 — smart & broke en un frame")
add_label_value(doc, "TEXTO", "SMART. / STILL / BROKE. — stacked, STILL BROKE en rojo (#C62828)")
add_label_value(doc, "LAYOUT", "Texto izquierda stacked (45%) — Alex derecha (55%) — layout V14 aprobado (S23)")
add_label_value(doc, "EXPRESIÓN", "Boca ABIERTA + ojos grandes (S23: legible a 200px, neutral = rechazar)")
add_block(doc, "Gap check: thumbnail no dice la solución ni 'one decision' → el viewer tiene que clickar para saber el porqué y el fix ✅",
          size=8, color=GREY)
add_block(doc, "S23 prompt addition obligatorio: mouth open in shock · gray pants NOT jeans · BLUE t-shirt · thick outline en skull",
          size=8, color=RED)

divider(doc)

# ── 6. YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes_yt = [
    "Título:         Why Smart People Can't Save Money (Do This Once Instead)",
    "Descripción:    Pegada completa con capítulos + URL de V14 (los 5 drains)",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — SMART. STILL BROKE. + Alex con libros + €140, fondo blanco",
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
add_checkbox(doc, "Vídeo: V14 (5 Things That Drain Your Money) — cierre del loop de la trilogía")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ CRÍTICO después de publicar V15: actualizar end screen de V14 para apuntar a V15 — es el payoff del tease. También V13 → V14.",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~2:10 (beats 24-26, 'remember the five drains') → card a V14 — el momento exacto de la referencia")
add_checkbox(doc, "Minuto ~6:00 → card a V12 (Why Willpower Fails Every Payday) — tema hermano")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V15 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Ordenar trilogía consecutiva en playlist: V13 → V14 → V15")
add_checkbox(doc, "Pegar URL de playlist en descripción de V15")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Manual vs automatic. That's the whole war.\n\n"
    "Which method died the quietest for you — the app, the no-spend month, or the beautiful spreadsheet?\n"
    "Drop it below 👇\n\n"
    "(And if you actually set up the transfer after this video — tell me. "
    "That's the comment I want to read.)"
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. REDDIT ──
add_section(doc, "11. REDDIT — publicar cuando el vídeo lleve 1h live")

reddit_posts = [
    ("r/personalfinance",       "Post principal — Madrian & Shea 37%→86% / defaults beat decisions"),
    ("r/povertyfinance",        "+30 min — ángulo 'no es disciplina, es la asimetría manual vs automático'"),
    ("r/BehavioralEconomics",   "+30 min — auto-enrollment / default effect (hallazgo canónico del campo)"),
    ("r/financialindependence", "+30 min — pay yourself first automatizado / hour-zero transfer"),
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
reddit_draft = [
    "",
    "Title: The Harvard study that convinced me budgets were never the problem — defaults are",
    "",
    "Madrian & Shea (2001) studied a company that changed exactly one thing about",
    "its retirement plan. Before: you had to opt in — a form, a meeting, a decision.",
    "37% of employees were saving.",
    "",
    "After: everyone was enrolled by default, and opting OUT took one form.",
    "86%.",
    "",
    "No raise. No bonus. No financial education seminar. Nobody became more",
    "disciplined that year. The decision just moved from 'every payday, forever' to 'once.'",
    "",
    "This reframed everything for me: every budget I'd tried required ~150 correct",
    "decisions a month. The things draining my money required zero. Machines beat",
    "to-do lists.",
    "",
    "The copy-at-home version is a standing transfer that fires the morning your",
    "salary lands — separate bank, no card attached. Made a video breaking down the",
    "full mechanism if anyone's curious: [URL]",
    "",
    "What's the method that died quietest for you?",
]
add_text_block(doc, reddit_draft, size=8, indent=True)

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "JUEVES 20:15", GREEN, 12)
add_label_value(doc, "EST (USA)",     "14:15 — jueves confirmado como mejor slot del canal (V8: 1,105 imp/2.5h vs V13 lunes: 31)", GREY, 9)
add_label_value(doc, "CADENCIA",      "Jueves para majors — mantener consistencia", GREY, 9)

divider(doc)

# ── 13. S17 CHECK ──
add_section(doc, "13. S17 — THUMBNAIL → TÍTULO → BEAT 1 CONTINUITY CHECK")
s17_rows = [
    ("THUMBNAIL muestra",  "Alex con libros de finanzas + móvil SAVINGS €140 · Villain cómodo · 'SMART. / STILL / BROKE.'"),
    ("TÍTULO promete",     "Why Smart People Can't Save Money (Do This Once Instead)"),
    ("BEAT 1 entrega",     "'You're smart. So why can't you save money?' — Alex + libros + €140 en pantalla · viewer reconoce en <5 seg ✅"),
    ("GAP check",          "Thumbnail no revela el porqué ni el fix → el viewer TIENE que clickar para resolver la disonancia ✅"),
]
for label, value in s17_rows:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.3)
    r1 = p.add_run(f"{label:<22}")
    r1.bold = True
    r1.font.size = Pt(9)
    r1.font.color.rgb = GREY
    r2 = p.add_run(value)
    r2.font.size = Pt(9)

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run(
    "NEUROCENTS · V15 · PRE-PUBLISH CHECKLIST · Brief v3.1 · "
    "Keywords: financial psychology 74.7 · behavioral finance 75 · why can't I save money 57.1"
)
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V15_final_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
