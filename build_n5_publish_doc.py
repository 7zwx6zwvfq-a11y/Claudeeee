#!/usr/bin/env python3
"""Pre-publish checklist document for N5 — The Sunk Cost Fallacy."""

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
r = t.add_run("NEUROCENTS — VIDEO N5 · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("The Sunk Cost Fallacy · Behavioral Investing · Lunes 23 Junio 2026")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. FILE NAME ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "sunk-cost-fallacy-investing-brain-bias-neurocents.mp4",
                GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — pendiente score VidIQ")
add_label_value(doc, "TÍTULO", "Your Brain Won't Let You Quit — And It's Costing You Everything", DARK, 12)
add_block(doc, "Alternativas evaluadas:  'The $40,000 Mistake Your Brain Keeps Making'  |  'Why Your Brain Can't Stop Losing Money'",
          size=8, color=GREY)
add_block(doc, "Histórico canal:  N3 (V6) = 92/100  ·  N4 = ~90-94/100  →  mantener línea title psychology: curiosity gap + loss",
          size=8, color=GREY)
add_block(doc, "Thumbnail text: 'YOUR BRAIN WON'T LET YOU QUIT' — coincide con título, refuerza el loop",
          size=8, color=GREY)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "Alex had seven chances to stop.",
    "He passed every single one.",
    "Not because the investment was good. Because of the money he had already spent.",
    "",
    "That's the sunk cost fallacy — and it didn't just cost Alex $40,000.",
    "It cost him four years of compounding he'll never get back.",
    "",
    "In 1985, psychologists Arkes and Blumer ran an experiment.",
    "They told people they'd paid for a ski trip. Then sent a blizzard.",
    "90% said they'd go anyway — dragging through misery to justify money that was already gone.",
    "The money was gone either way.",
    "",
    "Your brain doesn't know that.",
    "Your brain treats past spending as a debt you owe your future self.",
    "And it will keep paying that debt until you name what's happening.",
    "",
    "In this video:",
    "→ Alex's $40,000 mistake — and the seven moments he could have stopped",
    "→ The Arkes & Blumer 1985 ski trip experiment",
    "→ The Concorde Fallacy: when governments lose £1.3 billion because stopping means admitting it",
    "→ The disposition effect: investors hold losing stocks 40% longer than winners",
    "→ Zero-based thinking — the one question that kills sunk cost logic before it fires",
    "",
    "───────────────────────────────",
    "📌 Watch this next → [PEGA AQUÍ URL DE N4 — DOPAMINE TRAP]",
    "───────────────────────────────",
    "",
    "0:00 Alex is about to lose $40,000",
    "0:45 Seven chances to stop — all passed",
    "1:30 Why stopping felt like losing",
    "2:30 What the sunk cost fallacy actually is",
    "3:45 Arkes & Blumer — the ski trip experiment (1985)",
    "5:00 The Concorde: £1.3 billion and they kept going",
    "6:15 The disposition effect — your portfolio is doing this right now",
    "7:30 Zero-based thinking — the one question",
    "8:30 The real cost isn't what you lost",
    "",
    "#sunkcostfallacy #behavioralfinance #investingpsychology",
]

for line in desc_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)
    if line.startswith("Alex had seven") or line.startswith("Your brain doesn't know"):
        r.bold = True

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — copia todo el bloque")
tags = ("sunk cost fallacy, sunk cost, behavioral finance, loss aversion, cognitive bias investing, "
        "investment psychology, financial psychology, psychology of money, behavioral economics, "
        "Concorde fallacy, disposition effect, how to stop losing money investing, "
        "investment mistakes, zero based thinking, money mindset, decision making, "
        "investing for beginners, stock market psychology, why investors lose money, neurocents")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "KEYWORDS ESTIMADOS POR POTENCIAL:", size=8, bold=True, color=GREY)
kw_rows = [
    ("sunk cost fallacy",              "alto volumen",   "comp. media",   "← keyword principal"),
    ("sunk cost",                      "muy alto",       "comp. alta",    "← tag de volumen"),
    ("behavioral finance",             "95.5K/mes",      "27.8 comp.",    "73 ← probado N4"),
    ("loss aversion",                  "alto",           "comp. media",   "← enlaza con tema"),
    ("investment psychology",          "medio",          "baja comp.",    "← nicho exacto"),
    ("financial psychology",           "133K/mes",       "24.5 comp.",    "76 ← mejor ratio"),
    ("how to stop losing money",       "alto",           "comp. media",   "← search intent"),
    ("Concorde fallacy",               "nicho",          "muy baja",      "← long tail específico"),
    ("disposition effect",             "nicho",          "muy baja",      "← académico, long tail"),
    ("zero based thinking",            "medio",          "baja comp.",    "← accionable, FOMO"),
]
for kw, vol, comp, score in kw_rows:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<42}")
    r1.font.size = Pt(8)
    r2 = p.add_run(f"{vol:<16}{comp:<18}{score}")
    r2.font.size = Pt(8)
    r2.font.color.rgb = GREY

divider(doc)

# ── 5. MINIATURA ──
add_section(doc, "5. MINIATURA — MrBeast 3-element rule")
add_label_value(doc, "ESTADO", "⚠ Pendiente confirmar versión final — usar opción B generada")
add_label_value(doc, "FONDO", "Naranja brillante (#FF5500) — sólido, sin texturas")
add_label_value(doc, "TEXTO", "YOUR BRAIN WON'T LET YOU QUIT — Impact negro, outline blanco, arriba")
add_label_value(doc, "CARA", "Alex — shocked, Home Alone pose, ojos A CÁMARA, dominante izquierda")
add_label_value(doc, "OBJETO", "Brain villain en suit sosteniendo cash $40,000 — derecha, más pequeño que Alex")
add_block(doc, "Regla: máximo 3 elementos — texto + cara + villain con cash. Sin barra roja. Sin fondo oscuro. Sin segundo texto.",
          size=8, color=GREY)
add_block(doc, "Iteración pendiente: Alex mirando directamente a cámara (ojos al viewer). Añadir al prompt: 'CRITICAL: eyes directly into camera lens, pupils centered, eye contact with viewer'",
          size=8, color=RED)

divider(doc)

# ── 6. YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes = [
    "Título:         Your Brain Won't Let You Quit — And It's Costing You Everything",
    "Descripción:    Pegada completa con capítulos y URL de N4 (Dopamine Trap)",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — naranja, Alex shocked a cámara, brain villain con $40,000",
    "Capítulos:      Activados (timestamps en descripción)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado 20:15 hora España (lunes 23 junio)",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
    "Etiqueta IA:    Activada (narración generada con IA)",
]
for cb in checkboxes:
    add_checkbox(doc, cb)

divider(doc)

# ── 7. END SCREEN ──
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: seleccionar N4 (Dopamine Trap) manualmente — NO 'mejor opción'")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Después de publicar N5: entrar a N4 y actualizar end screen apuntando a N5 específico",
          size=8, color=RED)
add_block(doc, "⚠ Entrar a V6 y V9 y actualizar cards/end screen si son relevantes",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~3:45 → card apuntando a N4 (Dopamine Trap — mismo tema: tu cerebro toma decisiones por ti)")
add_checkbox(doc, "Minuto ~7:30 → card apuntando a V6 (Status Quo Bias — mismo tema: el cerebro evita cambiar)")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir N5 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden: N5 primero, N4 segundo, V6 tercero, V9 cuarto")
add_checkbox(doc, "Pegar URL de playlist en descripción de N5")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Alex had $40,000. His brain gave him seven reasons not to stop.\n"
    "Every single one made perfect sense in the moment.\n"
    "Drop 🧠 if you've ever held on to something longer than you should have."
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. AMIGOS — comentarios de apoyo ──
add_section(doc, "11. COMENTARIOS AMIGOS — pedir el día del lanzamiento")
friend_comments = [
    ("Amigo 1", "The ski trip experiment hit me hard. I would have been in the 90%. I know I would have."),
    ("Amigo 2", "I've been holding a stock for two years telling myself 'it'll recover.' Just asked the zero-based question. Selling tomorrow."),
    ("Amigo 3", "The Concorde section is insane. Countries do the same thing we do with $20 restaurant meals. The scale changes, the mechanism doesn't."),
    ("Amigo 4", "Hold is just buy without the paperwork. That one sentence broke something in my brain. Never thought about it that way."),
    ("Amigo 5", "The part about the real cost not being the $40,000 — but every dollar you didn't make while waiting to get it back. That's the one that actually hurts."),
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
    "The scariest part: the brain isn't broken. It's doing exactly what it evolved to do. "
    "Sunk cost logic protected our ancestors — abandoning effort meant starvation. "
    "The problem is the environment changed. The brain didn't. "
    "The zero-based question at 7:30 is the only override I've found that actually works."
)
r.font.size = Pt(9)
r.font.color.rgb = DARK

divider(doc)

# ── 12. REDDIT ──
add_section(doc, "12. REDDIT — ⚠ ESTRATEGIA SUSPENDIDA")
add_block(doc, "Posts anteriores eliminados automáticamente por karma bajo de cuenta nueva.",
          size=9, color=RED, bold=True)
add_block(doc, "Alternativas mientras se construye karma:",
          size=8, color=GREY)
add_block(doc, "  → Comentar en posts existentes de r/personalfinance sobre pérdidas de inversión",
          size=8, color=GREY, indent=True)
add_block(doc, "  → Responder en r/BehavioralEconomics con insight del vídeo (sin enlace)",
          size=8, color=GREY, indent=True)
add_block(doc, "  → Título preparado si se puede usar: 'The sunk cost fallacy cost me 4 years of compounding — not just the original loss'",
          size=8, color=GREY, indent=True)

divider(doc)

# ── 13. HORA ──
add_section(doc, "13. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA",  "20:15 CEST", GREEN, 12)
add_label_value(doc, "UTC",     "18:15 UTC", GREY, 9)
add_label_value(doc, "EST",     "14:15 EST (prime time USA lunes tarde)", GREY, 9)
add_label_value(doc, "FECHA",   "Lunes 23 Junio 2026 — 1 semana después de N4 (16 junio)", GREY, 9)
add_label_value(doc, "NOTA",    "Subir directamente programado — NUNCA pasar por oculto antes", GREY, 9)

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · N5 · PRE-PUBLISH CHECKLIST · V10 Sunk Cost Fallacy · 73 beats · ~9 min")
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/N5_Prepublish_Checklist.docx"
doc.save(path)
print(f"Saved: {path}")
