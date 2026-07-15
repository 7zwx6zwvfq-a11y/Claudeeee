#!/usr/bin/env python3
"""Pre-publish checklist — V3 · Why Being Poor Makes You Dumber (Bandwidth Tax)."""

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
r = t.add_run("NEUROCENTS — VIDEO 3 · PRE-PUBLISH CHECKLIST"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RED
s = doc.add_paragraph(); s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Why Being Poor Makes You Dumber · Bandwidth Tax (Mullainathan & Shafir) · próximo en cola tras V8")
r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()

add_block(doc, "⚠ Este video fue producido bajo el nombre de sesión \"Crayon Capital — Clone Session · Video 3\" "
                "(branding antiguo del canal, ahora Neurocents). No existía checklist previo para V2 ni V3 — "
                "este documento cubre V3 (el que tiene guión, narración y 146 image prompts ya completos).",
          size=8, color=RED)
divider(doc)

add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "why-being-poor-makes-you-dumber-bandwidth-tax-neurocents.mp4", GREEN, 10)
divider(doc)

add_section(doc, "2. TÍTULO — status-threat + contrapunto (patrón 993x)")
add_label_value(doc, "TÍTULO PRINCIPAL", "Why Being Poor Makes You Dumber (Not a Metaphor)", DARK, 12)
add_block(doc, "Mejora sobre el título ya fijado en CLAUDE.md (\"Why Being Poor Makes You Dumber\"): añade el "
               "paréntesis contrapunto validado en outliers de neurociencia (máximo multiplicador, S21) y lo ancla "
               "en la línea exacta del guión — beat 38: 'Not metaphorically. Literally.' — lo que refuerza la "
               "continuidad thumbnail→título→Beat 1 (S17).", size=8, color=GREY)
add_block(doc, "Patrón de fondo: amenaza de estatus/inteligencia (\"makes you dumber\") — mismo mecanismo que el "
               "outlier 993x \"Smart People Make Bad Money Decisions\". Negative framing, sin suavizar.", size=8, color=GREY)
add_label_value(doc, "ALTERNATIVA (si A/B en título)", "Why Poverty Costs You 13 IQ Points (It's Not Laziness)", GREY, 9)
divider(doc)

add_section(doc, "3. DESCRIPCIÓN — copia exactamente")
add_text_block(doc, [
    "Two people take the same IQ test. Same table, same questions. One scores like someone",
    "sharp. The other scores like someone who hasn't slept in 24 hours.",
    "",
    "They're the same person. The only thing that changed was a thought experiment about money.",
    "",
    "This is the Bandwidth Tax — the real reason \"just make better decisions\" is the wrong advice",
    "for anyone under financial pressure. Princeton researchers found a 13-point IQ gap from a",
    "single thought experiment about a car repair bill. Sugarcane farmers in Tamil Nadu, India",
    "lost 10 IQ points before harvest and gained them back after — same brain, same genes,",
    "different bank account.",
    "",
    "It's not intelligence. It's bandwidth — and there's a $90 billion industry built specifically",
    "around the moment yours runs out.",
    "",
    "───────────────────────────────",
    "📌 Watch next → [PEGA AQUÍ URL DE V5 — Mental Accounting]",
    "───────────────────────────────",
    "",
    "0:00 The Princeton test — 13 IQ points from one question",
    "0:50 Sendhil Mullainathan & Eldar Shafir — the experiment",
    "2:00 The Bandwidth Tax — what scarcity actually consumes",
    "3:25 Tunneling — why a 400% loan looks rational",
    "4:45 The Minnesota starvation study — same mechanism, different domain",
    "5:30 The $90B industry built around your depleted bandwidth",
    "6:40 The correct question (not \"why don't they decide better\")",
    "7:50 Slack — the one factor that stops the spiral",
    "8:50 Your brain was never broken",
    "",
    "(Timestamps aproximados — ajustar al montaje real)",
    "",
    "#financialpsychology #behavioralfinance #psychologyofmoney #cognitivebias #neurocents",
], size=9)
divider(doc)

add_section(doc, "4. TAGS — copia todo el bloque")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("why poor people make bad decisions, scarcity mindset, bandwidth tax, psychology of poverty, "
              "financial psychology, behavioral finance, psychology of money, cognitive load, "
              "poverty and the brain, why you can't save money, cognitive biases money, "
              "mullainathan shafir scarcity, payday loans explained, iq and poverty, neurocents")
r.font.size = Pt(9); r.font.color.rgb = DARK
doc.add_paragraph()
add_block(doc, "TOP KEYWORDS (volumen confirmado — tabla S13 de CLAUDE.md, ya validada):", size=8, bold=True, color=GREY)
for kw, vol in [("psychology of money", "731,164/mes · comp. 57.5"),
                ("financial psychology", "120,680/mes · comp. 27 · score 74.7 — primario"),
                ("behavioral finance", "98,056/mes · comp. 24.2 · score 75.0 — primario"),
                ("why you can't save money", "11,876/mes · comp. 48.5"),
                ("cognitive biases money", "4,908/mes · comp. 33.7")]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<28}"); r1.font.size = Pt(8)
    r2 = p.add_run(vol); r2.font.size = Pt(8); r2.font.color.rgb = GREY
add_block(doc, "⚠ SIN CONFIRMAR: \"scarcity mindset\" y \"bandwidth tax\" — no encontré volumen de búsqueda real "
               "para estos términos (ni en la tabla del canal ni en research de hoy). Úsalos como tags secundarios/"
               "long-tail, no como keyword principal — mismo error que \"brain traps\" (S13: 0 búsquedas). "
               "Verificar en YouTube Studio o VidIQ antes de publicar.", size=8, color=RED)
divider(doc)

add_section(doc, "5. MINIATURA — número grande + Alex en shock")
add_label_value(doc, "LAYOUT", "1 — Texto izquierda grande (stacked) · Alex derecha (55%)")
add_label_value(doc, "TEXTO", "LOSE 13 IQ POINTS — \"13\" en rojo gigante (#C62828), resto en negro Impact")
add_label_value(doc, "ALEX", "Sosteniendo dos facturas de reparación de coche — \"$300\" vs \"$3,000\" — boca ABIERTA "
                              "en shock genuino, ojos muy abiertos, Brain Villain con smirk dentro del skull")
add_label_value(doc, "FONDO", "BLANCO puro")
add_block(doc, "■ El número 13 en miniatura + en pantalla antes del segundo 20 del video satisface la regla S17 "
               "(el guión ya cumple esto en beat 10-11, ~30-40s).", size=8, color=GREY)
add_block(doc, "PROMPT GOOGLE FLOW: 2D flat cartoon illustration, thick solid black outlines, clean solid color "
               "fills, no gradients, white background, 16:9 1280×720. LEFT 45%: stacked bold Impact text "
               "'LOSE' / '13 IQ' / 'POINTS' with '13' in giant red #C62828 numerals, rest in black. RIGHT 55%: "
               "ALEX (beige oval head #F5E6C8, transparent glass skull with pink Brain Villain #E8A598 smirking "
               "inside, black spiky hair, BLUE t-shirt NOT red, gray pants NOT jeans) holding two price tags in "
               "his hands — one reading '$300' calm green, one reading '$3,000' bold red — mouth OPEN in genuine "
               "shock, eyes wide, eyebrows raised, thick black outline around the transparent skull. Expression "
               "must read clearly at 200px width.", size=8, color=GREY)
divider(doc)

add_section(doc, "6. YOUTUBE STUDIO")
for cb in [
    "Título:         Why Being Poor Makes You Dumber (Not a Metaphor)",
    "Descripción:    Pegada completa — resumen + timestamps + URL V5",
    "Tags:           Pegados (sección 4)",
    "Categoría:      Education",
    "Miniatura:      13 IQ POINTS + Alex shock, fondo blanco",
    "Capítulos:      Activados — uno por sección del guión",
    "Subtítulos:     Auto-generados",
    "Visibilidad:    Público — próximo JUEVES o LUNES 20:15 CEST (= 14:15 EST) según hueco real en cola",
    "Marca de agua:  Neurocents_Watermark.png",
]:
    add_checkbox(doc, cb)
divider(doc)

add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: V5 (Mental Accounting — \"Why Losing Money Makes You Want to Lose More\") — siguiente en cola")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Cola documentada en CLAUDE.md: V8 → V3 → V5 → V4. Verificar que sigue vigente — hay notas de "
               "sesiones más recientes (V16/V17/V18) que sugieren que la cola real pudo haberse movido. Confirmar "
               "antes de fijar el end screen.", size=8, color=RED)
divider(doc)

add_section(doc, "8. CARDS")
add_checkbox(doc, "Minuto ~2:00 (13 IQ points) → card a V1 (Your Brain Is Keeping You Broke — tesis general del canal)")
add_checkbox(doc, "Minuto ~5:30 ($90B industry) → card a V6 (Status Quo Bias — otro mecanismo que \"alguien más gana\")")
divider(doc)

add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V3 a la playlist principal del canal (\"How Your Brain Costs You Money\" o equivalente)")
divider(doc)

add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "13 IQ points. That's what scarcity costs — not stupidity, bandwidth.\n\n"
    "Which part hit hardest: the farmers before/after harvest, the payday loan math, or the "
    "reframe at the end? 👇"
)
r.font.size = Pt(10); r.font.color.rgb = DARK
divider(doc)

add_section(doc, "11. REDDIT — multi-subreddit (ranking #1 breakout del canal, CLAUDE.md S.\"Objetivos\")")
for sub, note in [
    ("r/personalfinance", "Primero — el ángulo \"por qué el consejo de fuerza de voluntad falla bajo presión financiera\""),
    ("r/sociology",       "+30 min — el experimento Tamil Nadu / harvest cycle como estudio de campo"),
    ("r/psychology",      "+30 min — bandwidth tax + tunneling como mecanismo cognitivo, no de carácter"),
    ("r/science",         "+45 min — foco en el paper de Mullainathan & Shafir (Science, 2013) y la réplica Minnesota"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<20}"); r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(note); r2.font.size = Pt(8); r2.font.color.rgb = GREY
doc.add_paragraph()
add_block(doc, "BORRADOR r/personalfinance (150-200 palabras, sin spam, aporta valor primero):", size=9, bold=True, color=DARK)
add_text_block(doc, [
    "",
    "Title: There's a 13-point IQ gap between two groups asked the exact same question —",
    "the only difference was how expensive a hypothetical car repair was",
    "",
    "Princeton researchers (Mullainathan & Shafir) ran a simple experiment: split people into",
    "two groups, ask one to imagine a $300 repair and the other a $3,000 repair, then give",
    "everyone the same cognitive test. The group primed with the bigger number scored 13 IQ",
    "points lower. Same people, same intelligence — just a different number in their head.",
    "",
    "They found the same effect in the field: sugarcane farmers in India tested 10 IQ points",
    "lower before harvest (broke) than after harvest (flush) — same brain, same genes,",
    "different bank account.",
    "",
    "The takeaway that changed how I think about \"just budget better\" advice: financial",
    "scarcity taxes the exact cognitive bandwidth you'd need to make good decisions. It's not",
    "a character problem, it's a resource problem — and there's a whole industry (payday",
    "lending) built around catching people at the exact moment that tax is highest.",
    "",
    "Made a video walking through the research if anyone wants the full mechanism + the one",
    "factor (\"slack\") that reliably protects against it: [URL]",
], size=8)
divider(doc)

add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "Próximo LUNES o JUEVES 20:15 (confirmar hueco exacto en cola tras V8)", GREEN, 12)
add_label_value(doc, "EST", "14:15 · UTC 18:15", GREY, 9)
add_label_value(doc, "SECUENCIA DOCUMENTADA", "V8 → V3 → V5 → V4 (CLAUDE.md) — verificar si sigue vigente", GREY, 9)
divider(doc)

add_section(doc, "13. NOTAS — por qué esta estructura, y qué no pude confirmar")
for note in [
    "→ V3 está clasificado #1 en potencial de breakout por el propio canal (CLAUDE.md, Objetivos): "
    "\"stat de 13 IQ points, controversial, multi-subreddit\". El título y la miniatura están diseñados para "
    "explotar exactamente ese activo — el número, no el nombre del sesgo, es el gancho.",
    "→ Patrón de título: amenaza de estatus/inteligencia (\"makes you dumber\") — mismo mecanismo que el outlier "
    "993x \"Smart People Make Bad Money Decisions\" (S21). Paréntesis contrapunto (\"Not a Metaphor\") citando "
    "textualmente el beat 38 del guión — refuerza continuidad thumbnail→Beat 1 sin inventar nada nuevo.",
    "→ NO TENGO ACCESO A VIDIQ EN VIVO en esta sesión. Los volúmenes de \"psychology of money / financial "
    "psychology / behavioral finance / why you can't save money / cognitive biases money\" vienen de la tabla ya "
    "validada del canal (S13 de CLAUDE.md). Hice búsquedas web hoy para \"scarcity mindset\" y \"bandwidth tax\" y "
    "no encontré cifras de volumen fiables para ninguno de los dos — tratarlos como long-tail, no como pilar SEO.",
    "→ COMPETENCIA DETECTADA: existe un vídeo reciente de otro canal, \"The Brain on Poverty: How Scarcity Taxes "
    "Our Mental Bandwidth\" (oct. 2025), cubriendo el mismo territorio. Señal de que el tema tiene tracción de "
    "búsqueda activa — pero también que hay que diferenciarse con el dispositivo narrativo Alex/Brain Villain y "
    "los números exactos (13, 10, $90B, 400%) que un canal explicativo genérico no va a replicar.",
    "→ Este guión es anterior a la Regla de Independencia (S20, vigente desde V16) y al ratio 30/30/30/10 "
    "Alex/Villain (S9) — no se ha tocado el guión ni los 146 image prompts ya generados, solo la capa de "
    "publicación (título, miniatura, descripción, tags, Reddit).",
    "→ CTA y estructura del guión (146 beats, ~10 min) no se tocan aquí — esta checklist cubre exclusivamente "
    "los elementos de descubribilidad y distribución.",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note); r.font.size = Pt(9); r.font.color.rgb = DARK
divider(doc)

doc.add_paragraph()
foot = doc.add_paragraph(); foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V3 · PRE-PUBLISH CHECKLIST · Why Being Poor Makes You Dumber · próximo hueco Lunes/Jueves 20:15 España")
fr.font.size = Pt(8); fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V3_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
