#!/usr/bin/env python3
"""Pre-publish checklist — V18 · 7 Signs Your Brain Is Wired to Stay Broke (Count Yours)."""

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

def add_block(doc, text, size=9, color=None, bold=False):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(text); r.font.size = Pt(size); r.bold = bold
    if color: r.font.color.rgb = color

def add_checkbox(doc, text, size=10):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(f"☐  {text}"); r.font.size = Pt(size)

def divider(doc):
    p = doc.add_paragraph("─" * 90); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    for r in p.runs: r.font.size = Pt(7); r.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)

def add_text_block(doc, lines, size=9):
    for line in lines:
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.left_indent = Cm(0.5)
        r = p.add_run(line); r.font.size = Pt(size)

doc = Document()
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)

t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("NEUROCENTS — VIDEO 18 · PRE-PUBLISH CHECKLIST"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RED
s = doc.add_paragraph(); s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("7 Signs Your Brain Is Wired to Stay Broke (Count Yours) · SEÑALES · Jueves 20:15 CEST")
r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()

add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "7-signs-brain-wired-stay-broke-count-yours-neurocents.mp4", GREEN, 10)
divider(doc)

add_section(doc, "2. TÍTULO — número + verbo físico + autoevaluación")
add_label_value(doc, "TÍTULO PRINCIPAL", "7 Signs Your Brain Is Wired to Stay Broke (Count Yours)", DARK, 12)
add_block(doc, "Patrón: número + 'Wired' (verbo físico validado en outliers) + 'Broke' + paréntesis de acción '(Count Yours)'.", size=8, color=GREY)
add_block(doc, "El '(Count Yours)' convierte el título en un test — motor de clics y de comentarios ('I got 5/7').", size=8, color=GREY)
divider(doc)

add_section(doc, "3. DESCRIPCIÓN — copia exactamente")
add_text_block(doc, [
    "Do you open your banking app with one eye half-closed?",
    "That's not a quirk. That's evidence.",
    "",
    "Your brain runs a quiet money program it installed years ago — and it left seven fingerprints.",
    "Most people carry at least three and have never noticed a single one. Count yours:",
    "",
    "7. The One-Eye Check — you're not checking your balance, you're bracing for it",
    "6. The Sale Math — you didn't save €30, you spent €70",
    "5. The Round-Down Memory — your spending always shrinks in the retelling",
    "4. The Checkout Sacrifice — you didn't cut the cost, you bought the feeling of cutting it",
    "3. The Countdown Clock — your money clock only counts down to Friday",
    "2. The 'When' Plan — 'when' is a waiting room, not a plan",
    "1. The Ceiling — the picture of being wealthy feels like someone else's photo",
    "",
    "Drop your count in the comments: ?/7",
    "",
    "───────────────────────────────",
    "📌 Watch next → [PEGA AQUÍ URL DE V17 — Two People, Same Salary]",
    "───────────────────────────────",
    "",
    "0:00 The One-Eye Check (the gesture)",
    "0:35 The rules — count yours",
    "1:00 Sign 7 — The One-Eye Check",
    "1:45 Sign 6 — The Sale Math",
    "2:30 Sign 5 — The Round-Down Memory",
    "3:20 Sign 4 — The Checkout Sacrifice",
    "4:10 If you're at three or four — hold on",
    "4:35 Sign 3 — The Countdown Clock",
    "5:20 Sign 2 — The 'When' Plan",
    "6:05 Sign 1 — The Ceiling",
    "7:00 The Count — what your number means",
    "7:40 The Delete Attempt",
    "8:00 The Catch",
    "",
    "(Timestamps aproximados — ajustar al montaje real)",
    "",
    "#financialpsychology #behavioralfinance #moneyhabits #psychologyofmoney #neurocents",
], size=9)
divider(doc)

add_section(doc, "4. TAGS — copia todo el bloque")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("signs you're bad with money, money habits, financial psychology, behavioral finance, "
              "psychology of money, scarcity mindset, money mindset, why am I always broke, "
              "bad money habits, money personality test, brain and money, count yours, "
              "checkout psychology, sale psychology, neurocents")
r.font.size = Pt(9); r.font.color.rgb = DARK
doc.add_paragraph()
add_block(doc, "TOP KEYWORDS:", size=8, bold=True, color=GREY)
for kw, vol in [("money habits", "~25K/mes — exact match"),
                ("why am I always broke", "~10K/mes — intención de búsqueda directa"),
                ("financial psychology", "120K/mes · 74.7 — primario"),
                ("behavioral finance", "98K/mes · 75.0 — primario")]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<28}"); r1.font.size = Pt(8)
    r2 = p.add_run(vol); r2.font.size = Pt(8); r2.font.color.rgb = GREY
divider(doc)

add_section(doc, "5. MINIATURA — CHECKLIST + Alex contando")
add_label_value(doc, "CONCEPTO", "Checklist gigante de 7 casillas (3 marcadas en ROJO) izquierda + Alex derecha contando con "
                                  "los dedos (3 dedos), boca ABIERTA en shock, Brain Villain smirking en el skull")
add_label_value(doc, "TEXTO", "HOW MANY? — stacked o una línea, Impact negro, '?' en rojo (#C62828)")
add_label_value(doc, "FONDO", "BLANCO puro")
add_block(doc, "■ S23 obligatorio: boca abierta legible a 200px · camiseta AZUL · pantalones GRISES (no jeans) · "
               "contorno grueso del skull.", size=8, color=RED)
add_block(doc, "PROMPT GOOGLE FLOW: Flat 2D cartoon, thick black outlines, solid fills, no gradients, white background, "
               "16:9 1280×720. LEFT 45%: giant vertical checklist card with 7 checkboxes — boxes 2, 4 and 6 ticked with "
               "bold RED checks, the rest empty. RIGHT 55%: ALEX (beige oval head #F5E6C8, transparent glass skull with "
               "pink Brain Villain #E8A598 smirking inside, black spiky hair, BLUE t-shirt NOT red, gray pants NOT jeans) "
               "counting on raised fingers — three fingers up — mouth OPEN in genuine shock, eyes wide, eyebrows raised. "
               "TEXT top: 'HOW MANY?' ultra-bold Impact black with the '?' in red #C62828. Expression and checks must "
               "read clearly at 200px width.", size=8, color=GREY)
divider(doc)

add_section(doc, "6. YOUTUBE STUDIO")
for cb in [
    "Título:         7 Signs Your Brain Is Wired to Stay Broke (Count Yours)",
    "Descripción:    Pegada completa — las 7 señales listadas + capítulos + URL V17",
    "Tags:           Pegados (sección 4)",
    "Categoría:      Education",
    "Miniatura:      Checklist 3/7 en rojo + Alex contando, fondo blanco",
    "Capítulos:      Activados — un capítulo por señal",
    "Subtítulos:     Auto-generados",
    "Visibilidad:    Público — JUEVES 20:15 CEST (= 14:15 EST)",
    "Marca de agua:  Neurocents_Watermark.png",
]:
    add_checkbox(doc, cb)
divider(doc)

add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: V17 (Two People, Same Salary) — el catálogo interno se retroalimenta")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Al publicar V18: entrar a V17 y actualizar su end screen para apuntar a V18 (cierra el tease de las señales).", size=8, color=RED)
divider(doc)

add_section(doc, "8. CARDS")
add_checkbox(doc, "Minuto ~2:30 (Sale Math) → card a V16 (el catálogo — sesgo hermano: anchoring)")
add_checkbox(doc, "Minuto ~6:05 (The Ceiling) → card a V3 (Bandwidth Tax — el mecanismo de fondo)")
divider(doc)

add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V18 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Trilogía nueva ordenada: V16 → V17 → V18")
divider(doc)

add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "What's your count? ?/7 👇\n\n"
    "Be honest — nobody's checking your homework.\n"
    "(Mine is 4/7. Number 4 gets me every single week. The chocolate goes back. The €60 stays.)"
)
r.font.size = Pt(10); r.font.color.rgb = DARK
divider(doc)

add_section(doc, "11. REDDIT — publicar 1h después de live")
for sub, note in [
    ("r/personalfinance", "Primero — las 7 señales como observaciones conductuales"),
    ("r/psychology",      "+30 min — el ángulo 'signs as fingerprints of a program'"),
    ("r/povertyfinance",  "+30 min — The Ceiling / scarcity heredada resuena fuerte aquí"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<24}"); r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(note); r2.font.size = Pt(8); r2.font.color.rgb = GREY
doc.add_paragraph()
add_block(doc, "BORRADOR r/personalfinance:", size=9, bold=True, color=DARK)
add_text_block(doc, [
    "",
    "Title: Started noticing 'money tells' — small behaviors that predict how someone's finances actually look. Collected seven.",
    "",
    "The one that started it: watching people (myself included) open their banking app with one eye",
    "half-closed. You're not checking the balance — you're bracing for it.",
    "",
    "Others: counting 'saved' money from discounts as if it were income. Remembering every expense",
    "rounded down ('it was like 20' — it was 38). Putting the €2 item back at checkout while the €60",
    "cart sails through — buying the feeling of cutting costs instead of cutting them.",
    "",
    "The deepest one: try picturing yourself actually wealthy. If something pushes back — a voice",
    "that says 'that's not for people like us' — that ceiling usually got installed before age 12.",
    "",
    "Made a video with all seven so people can count theirs: [URL]",
    "",
    "Curious what the average count is here. Mine was 4/7.",
], size=8)
divider(doc)

add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "JUEVES 20:15", GREEN, 12)
add_label_value(doc, "EST", "14:15 · UTC 18:15", GREY, 9)
add_label_value(doc, "SECUENCIA", "V16 catálogo → V17 comparativa → V18 señales (cierra la trilogía nueva)", GREY, 9)
divider(doc)

add_section(doc, "13. NOTAS — por qué esta estructura")
for note in [
    "→ FORMATO 3 Señales (primera vez) + mecánica de contador acumulativo (patrón catálogo 4.9M adaptado a autoevaluación).",
    "→ HOOK S6 Villain Reveal (última vez V12): 'el programa ya corre y dejó huellas' + micro-momento del one-eye check.",
    "→ MOTOR DE COMENTARIOS: '?/7' — pedir el número es la pregunta más fácil de contestar de todo YouTube.",
    "→ ESCALADA leve→identidad: del gesto del ojo (universal, gracioso) a The Ceiling (infancia, la cocina). El beat 68 "
    "('that voice has an accent — it sounds like your childhood kitchen') es el más fuerte del guión.",
    "→ INOCULACIÓN NUEVA ('The Delete Attempt'): el cerebro archiva el vídeo como 'interesting' para olvidarlo — "
    "cero solape con las inoculaciones de V14/V15/V16.",
    "→ CIERRE ANTI-VERGÜENZA (patrón outlier procrastinación): 'Shame is what these programs eat. Curiosity is what starves them.'",
    "→ ALEX REDUCIDO: solo 2 apariciones en 94 beats (beat 19 humor, beat 47 identidad). El COUNTER es el protagonista visual.",
    "→ CTR TARGET: >6% · comentarios con número = señal de satisfacción fuerte para el algoritmo.",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note); r.font.size = Pt(9); r.font.color.rgb = DARK
divider(doc)

doc.add_paragraph()
foot = doc.add_paragraph(); foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V18 · PRE-PUBLISH CHECKLIST · 7 Signs (Count Yours) · Jueves 20:15 España")
fr.font.size = Pt(8); fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V18_final_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
