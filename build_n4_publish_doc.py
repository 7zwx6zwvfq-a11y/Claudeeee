#!/usr/bin/env python3
"""Pre-publish checklist document for N4 — The Dopamine Trap."""

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
r = t.add_run("NEUROCENTS — VIDEO N4 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("The Dopamine Trap · Impulse Spending · Lunes 16 Junio 2026")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. FILE NAME ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "dopamine-trap-impulse-buying-spending-neurocents.mp4",
                GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — 84/100 VidIQ")
add_label_value(doc, "TÍTULO", "Your Brain Decides to Buy 200 Milliseconds Before You Do", DARK, 12)
add_block(doc, "Descartados:  'The Hidden Reason You Can't Stop Spending (It's Not Willpower)' = 79/100  |  'Why Buying Feels Better Than Having — And What It's Costing You' = 73/100",
          size=8, color=GREY)
add_block(doc, "Histórico canal:  N3 (V6) = 92/100  ·  N2 (V9) = 86/100  ·  N4 = 84/100",
          size=8, color=GREY)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "Every time you tap \"buy now,\" your brain releases dopamine — and impulse buying is the proof.",
    "Not when the package arrives. Not when you open it.",
    "The moment you decide.",
    "",
    "That's why the cart feels better than the closet.",
    "That's why you keep buying things you already own.",
    "That's why it never feels like a choice.",
    "",
    "In 1954, two neuroscientists in Montreal wired electrodes into rat brains.",
    "The rats stopped eating. Stopped sleeping.",
    "They pressed the lever thousands of times per hour until some of them died.",
    "The lever just changed shape.",
    "",
    "Your smartphone is the lever. The buy button is the lever.",
    "Your brain is running the same experiment — on you.",
    "",
    "In this video:",
    "→ Why your brain fires dopamine 200ms before you consciously decide to buy",
    "→ The Olds & Milner 1954 experiment that found the override switch for any brain",
    "→ Why the package always disappoints — and the brain planned that",
    "→ What stop impulse buying advice gets wrong (it targets the wrong thing)",
    "→ The one question that kills the dopamine trap before it fires",
    "",
    "───────────────────────────────",
    "📌 Watch this next → [PEGA AQUÍ URL DE V6]",
    "───────────────────────────────",
    "",
    "0:00 The trap",
    "0:40 What happens when you tap buy now",
    "1:25 The nucleus accumbens",
    "2:50 Montreal, 1954 — the lever experiment",
    "4:15 The lever never changed",
    "5:30 You were pressing the lever all along",
    "7:00 What impulse spending costs over a lifetime",
    "8:20 Prefrontal cortex vs dopamine flood",
    "9:45 How to override the trap",
    "",
    "#dopaminetrap #impulsebuying #personalfinance",
]

for line in desc_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)
    if line.startswith("Every time you tap") or line.startswith("Your smartphone is the lever"):
        r.bold = True

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — testeados VidIQ (copia todo el bloque)")
tags = ("stop impulse buying, impulse spending psychology, dopamine trap, dopamine and money, "
        "behavioral finance, financial psychology, psychology of money, cognitive bias, "
        "behavioral economics, dopamine detox, how to stop spending money, "
        "impulse buying psychology, personal finance, money mindset, how to save money, "
        "decision making, neuroscience of money, dopamine explained, spending habits, neurocents")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE VIDIQ:", size=8, bold=True, color=GREY)
kw_rows = [
    ("stop impulse buying",          "5.3K/mes",  "22.3 comp.", "64 ← baja comp."),
    ("impulse spending psychology",  "5K/mes",    "20.0 comp.", "65 ← gema oculta"),
    ("dopamine trap",                "20.6K/mes", "44.6 comp.", "61"),
    ("dopamine and money",           "3.7K/mes",  "22.0 comp.", "63 ← baja comp."),
    ("dopamine detox",               "574K/mes",  "49.9 comp.", "72 ← enorme volumen (tag)"),
    ("behavioral finance",           "95.5K/mes", "27.8 comp.", "73 ← volumen + baja comp."),
    ("financial psychology",         "133K/mes",  "24.5 comp.", "76 ← mejor ratio canal"),
    ("how to stop spending money",   "14.3K/mes", "48.0 comp.", "58"),
]
for kw, vol, comp, score in kw_rows:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<42}")
    r1.font.size = Pt(8)
    r2 = p.add_run(f"{vol:<14}{comp:<16}{score}")
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

divider(doc)

# ── 5. MINIATURA ──
add_section(doc, "5. MINIATURA")
add_label_value(doc, "ESTADO", "⚠ Pendiente de crear — ver instrucciones abajo")
add_label_value(doc, "FONDO", "Amarillo neón o naranja brillante — NUNCA oscuro")
add_label_value(doc, "NÚMERO CENTRAL", "$__ / mes  (coste impulso calculado en el vídeo)")
add_label_value(doc, "TEXTO TWIST", "YOU CLICKED  /  BRAIN WON  /  200ms ago.")
add_label_value(doc, "PERSONAJE", "Personaje en shock mirando el teléfono · Brain villain riendo en el cráneo")
add_block(doc, "Estructura viral: fondo brillante + número que duele + twist phrase + brain villain mirando A CÁMARA (rompe 4ª pared)",
          size=8, color=GREY)
add_block(doc, "Score thumbnail: subir URL a VidIQ después de publicar", size=8, color=GREY)

divider(doc)

# ── 6. YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes = [
    "Título:         Your Brain Decides to Buy 200 Milliseconds Before You Do",
    "Descripción:    Pegada completa con capítulos y URL de V6",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — fondo amarillo/naranja, número central, brain villain",
    "Capítulos:      Activados (añadidos en descripción con timestamps)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado para 20:00-22:00 hora Bali",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
    "Etiqueta IA:    Activada (ElevenLabs narración)",
]
for cb in checkboxes:
    add_checkbox(doc, cb)

divider(doc)

# ── 7. END SCREEN ──
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: seleccionar V6 (Status Quo Bias) manualmente — NO 'mejor opción'")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Después de publicar N4: entrar a V6 y actualizar end screen apuntando a N4 específico",
          size=8, color=RED)
add_block(doc, "⚠ Entrar a V9 y actualizar cards/end screen si es relevante",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~4:15 → card apuntando a V6 (status quo bias — mismo tema decisiones automáticas)")
add_checkbox(doc, "Minuto ~7:00 → card apuntando a V9 (anchoring bias — mismo tema dinero)")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir N4 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden: N4 primero, V6 segundo, V9 tercero, V1 cuarto")
add_checkbox(doc, "Pegar URL de playlist en descripción de N4")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Your brain fires dopamine before you consciously decide to buy. 200ms before.\n"
    "Not at delivery. Not at unboxing. At the click.\n"
    "Drop 🧠 if you've ever opened a package and felt... nothing."
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. AMIGOS — comentarios de apoyo ──
add_section(doc, "11. COMENTARIOS AMIGOS — pedir el día del lanzamiento")
friend_comments = [
    ("Amigo 1", "This explains so much. I always feel empty after packages arrive. Never connected it to dopamine before."),
    ("Amigo 2", "The rat lever analogy is terrifying. And I literally checked my phone before watching this video."),
    ("Amigo 3", "200 milliseconds. That's all the 'choice' I had? I've been overestimating my willpower my entire life."),
    ("Amigo 4", "The Olds & Milner experiment is wild. The fact that the lever just changed shape and now it's my phone... that hit."),
    ("Amigo 5", "I paused this at 7:00 to check how much I spent on impulse buys last month. Do NOT recommend."),
]
for name, text in friend_comments:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{name}:  ")
    r1.bold = True
    r1.font.size = Pt(8)
    r1.font.color.rgb = GREY
    r2 = p.add_run(text)
    r2.font.size = Pt(9)
    r2.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "PINNED (tu respuesta al primer comentario):", size=8, bold=True, color=GREY)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "The scariest part isn't that it happens. It's that knowing doesn't stop it — "
    "the dopamine fires before the prefrontal cortex even gets the memo. "
    "The only move that actually works is what I cover at 9:45."
)
r.font.size = Pt(9)
r.font.color.rgb = DARK

divider(doc)

# ── 12. REDDIT ──
add_section(doc, "12. REDDIT — publicar después de que el vídeo lleve 1h live")
reddit_posts = [
    ("r/personalfinance",       "Esperar 30 min entre posts"),
    ("r/BehavioralEconomics",   "+30 min"),
    ("r/psychology",            "+30 min"),
    ("r/mildlyinfuriating",     "+30 min — ángulo 'el botón buy now está diseñado así'"),
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
add_block(doc, "TÍTULO REDDIT (mismo para todos):", size=8, bold=True, color=GREY)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("TIL your brain releases dopamine at the moment of deciding to buy — not when the package arrives. The anticipation is the drug.")
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "CUERPO DEL POST (texto puro, sin enlace):", size=8, bold=True, color=GREY)
reddit_body = [
    "Came across this in the context of the Olds & Milner 1954 rat experiment.",
    "",
    "They wired electrodes directly into the reward centers of rat brains and gave each rat a lever.",
    "Press the lever = instant dopamine hit. The rats stopped eating, stopped sleeping.",
    "Some pressed it thousands of times per hour until they died.",
    "",
    "The part that got me: your nucleus accumbens fires dopamine at the DECISION to buy,",
    "not at receiving the product. That's why the cart always feels better than the closet.",
    "That's why packages disappoint.",
    "",
    "The lever just changed shape. Now it's a buy button.",
    "",
    "Has anyone managed to actually break this? Curious what's worked practically.",
]
for line in reddit_body:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)

doc.add_paragraph()
add_block(doc, "PRIMER COMENTARIO (con el enlace):", size=8, bold=True, color=GREY)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("I actually went deeper on this in a video if anyone wants the full mechanism + the override: [PEGA AQUÍ URL DEL VÍDEO]")
r.font.size = Pt(9)
r.font.color.rgb = GREY

divider(doc)

# ── 13. HORA ──
add_section(doc, "13. HORA DE PUBLICACIÓN")
add_label_value(doc, "BALI", "20:00 – 22:00", GREEN, 12)
add_label_value(doc, "EST",  "12:00 – 14:00 (prime time USA lunes)", GREY, 9)
add_label_value(doc, "FECHA", "Lunes 16 Junio 2026 — 1 semana después de N3 (V6)", GREY, 9)
add_label_value(doc, "NOTA", "Subir directamente programado — NUNCA pasar por oculto antes", GREY, 9)

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · N4 · PRE-PUBLISH CHECKLIST · Título 84/100 VidIQ · Tags testeados")
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/N4_Prepublish_Checklist.docx"
doc.save(path)
print(f"Saved: {path}")
