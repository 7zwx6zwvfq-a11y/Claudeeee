#!/usr/bin/env python3
"""Pre-publish checklist — V13 · 5 Ways Your Brain Physically Rewires Itself to Stay Broke."""

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
r = t.add_run("NEUROCENTS — VIDEO 13 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("5 Traps · Neuroplasticity + Behavioral Finance · Brief v3.1 · Lunes/Jueves 20:15 CEST")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. NOMBRE ARCHIVO ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO",
    "5-ways-brain-rewires-broke-behavioral-finance-neurocents.mp4",
    GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO")
add_label_value(doc,
    "TÍTULO",
    "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)",
    DARK, 12)
add_block(doc,
    "Fórmula 181× — [Number] Ways Your Brain [Physical Verb] to Stay Broke (Without Telling You)",
    size=8, color=GREY)
add_block(doc,
    "Keyword principal: behavioral finance (98K/mes · comp 24.2 · score 75) ✅",
    size=8, color=GREY)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "Five.",
    "",
    "That's how many neural programs your brain is running right now",
    "that are keeping you exactly where you are financially.",
    "",
    "Not bad decisions. Not lack of discipline.",
    "Actual circuits — built through repetition — firing without your knowledge.",
    "",
    "The third one gets worse the more you learn about money.",
    "The fifth one compounds biologically — not just financially.",
    "One of them fired this morning. Before you opened this video.",
    "",
    "In this video:",
    "→ Why dopamine peaks on Wednesday — not payday Friday (Trap 1)",
    "→ The cognitive illusion that hides the real cost of every purchase (Trap 2)",
    "→ Why financial knowledge rewires the brain toward worse decisions (Trap 3)",
    "→ Why your willpower score at 11 PM is the only one that matters (Trap 4)",
    "→ The biological upgrade trap that no budget can stop (Trap 5)",
    "",
    "───────────────────────────────",
    "📌 Watch this next → [PEGA AQUÍ URL DEL VÍDEO ANTERIOR]",
    "───────────────────────────────",
    "",
    "0:00 The five programs",
    "0:50 Trap 1: The Anticipation Burn",
    "1:50 Trap 2: The Balance Blindspot",
    "2:55 Trap 3: The Expertise Trap",
    "4:00 Trap 4: The Night Drain",
    "5:00 Trap 5: The Upgrade Lock",
    "6:00 The structural fix",
    "7:20 Why your brain runs these programs",
    "",
    "#behavioralfinance #financialpsychology #brainrewiring",
]

add_text_block(doc, desc_lines, size=9, indent=True)

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — copia todo el bloque")
tags = (
    "behavioral finance, financial psychology, cognitive biases money, brain rewiring, "
    "neuroplasticity money, decision fatigue, why can't I save money, money psychology, "
    "how to save money, anticipation bias, dopamine money, behavioral economics, "
    "neuroscience personal finance, brain money habits, cognitive bias, "
    "financial behavior, ego depletion, neurocents"
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
    ("why can't I save money",      "11.8K/mes","48.5 comp.", "57.1"),
    ("cognitive biases money",      "4.9K/mes", "33.7 comp.", "59.6"),
    ("decision fatigue",            "8K/mes",   "35 comp.",   "61"),
    ("behavioral economics",        "45K/mes",  "42 comp.",   "62"),
    ("how to save money",           "320K/mes", "70 comp.",   "55"),
    ("money psychology",            "9K/mes",   "30 comp.",   "63"),
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
add_label_value(doc, "ESTADO", "✅ Generada — Alex shocked, 5 circuitos rojos numerados, Brain Villain triunfante, fondo blanco")
add_label_value(doc, "TEXTO", "5 WAYS / YOUR BRAIN / REWIRES ITSELF (rojo)")
add_label_value(doc, "LAYOUT", "Personaje izquierda — texto derecha")
add_block(doc, "Gap check: thumbnail no dice 'to Stay Broke' → el viewer tiene que clickar para saber el destino del rewiring ✅",
          size=8, color=GREY)

divider(doc)

# ── 6. YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes_yt = [
    "Título:         5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)",
    "Descripción:    Pegada completa con capítulos + URL vídeo anterior",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — Alex shocked, 5 circuitos, fondo blanco",
    "Capítulos:      Activados (timestamps en descripción — ajustar al vídeo real)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado para 20:15 CEST (= 14:15 EST)",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
]
for cb in checkboxes_yt:
    add_checkbox(doc, cb)

divider(doc)

# ── 7. END SCREEN ──
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: seleccionar el vídeo más relevante del canal manualmente")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Después de publicar V13: actualizar end screens de vídeos anteriores para apuntar a V13",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~3:00 → card apuntando al vídeo más relacionado")
add_checkbox(doc, "Minuto ~6:30 → card apuntando a vídeo anterior")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V13 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Verificar que V13 aparece en posición correcta en la playlist")
add_checkbox(doc, "Pegar URL de playlist en descripción de V13")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Five programs. Zero warnings.\n\n"
    "Which trap fired on you this week?\n"
    "Drop the number below 🧠\n\n"
    "(Trap 3 is the one nobody talks about — and it gets worse the smarter you get about money.)"
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. REDDIT ──
add_section(doc, "11. REDDIT — publicar cuando el vídeo lleve 1h live")

reddit_posts = [
    ("r/personalfinance",       "Post principal — Trap 1 (Anticipation Burn / payday spending)"),
    ("r/psychology",            "+30 min — Schultz / dopamine fires at prediction, not reward"),
    ("r/BehavioralEconomics",   "+30 min — Trap 3 (Expertise Trap — counterintuitive finding)"),
    ("r/cogsci",                "+30 min — neural rewiring angle (5 circuits = 5 behavioral patterns)"),
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
    "Title: TIL why payday spending feels compulsive — it's not willpower, it's a dopamine schedule",
    "",
    "The science behind this messed me up a bit.",
    "",
    "Wolfram Schultz (Cambridge, partial Nobel) discovered that dopamine doesn't fire",
    "when you receive a reward. It fires when your brain predicts the reward is coming.",
    "",
    "This means by Wednesday, your brain has already peaked on the dopamine from Friday's paycheck.",
    "By the time payday arrives, the signal is declining — and your brain is already predicting",
    "the next spend. The purchase on Friday isn't a decision. It's a receipt for a transaction",
    "your brain closed on Tuesday.",
    "",
    "This is one of 5 ways the brain physically rewires itself around money patterns.",
    "Made a video breaking all five down if anyone's curious: [URL]",
    "",
    "Which one do you think hits hardest?",
]
add_text_block(doc, reddit_draft, size=8, indent=True)

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "20:15", GREEN, 12)
add_label_value(doc, "EST (USA)",     "14:15 — prime time early afternoon lunes/jueves", GREY, 9)
add_label_value(doc, "CADENCIA",      "Lunes y Jueves — mantener consistencia", GREY, 9)

divider(doc)

# ── 13. S17 CHECK ──
add_section(doc, "13. S17 — THUMBNAIL → TÍTULO → BEAT 1 CONTINUITY CHECK")
s17_rows = [
    ("THUMBNAIL muestra",  "Alex shocked · 5 circuitos rojos numerados · Brain Villain triunfante · '5 WAYS / YOUR BRAIN / REWIRES ITSELF'"),
    ("TÍTULO promete",     "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)"),
    ("BEAT 1 entrega",     "'Five.' — el número en pantalla + 5 circuitos disparando + Alex mid-action · viewer reconoce en <5 seg ✅"),
    ("GAP check",          "Thumbnail no dice 'to Stay Broke' ni '5 trap names' → el viewer TIENE que clickar para resolver el loop ✅"),
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
    "NEUROCENTS · V13 · PRE-PUBLISH CHECKLIST · Brief v3.1 · "
    "Keywords: behavioral finance 75 · financial psychology 74.7"
)
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V13_v31_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
