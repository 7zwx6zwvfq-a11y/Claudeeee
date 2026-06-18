#!/usr/bin/env python3
"""Pre-publish checklist for V12 FINAL — Why Willpower Fails Every Payday."""

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
r = t.add_run("NEUROCENTS — VIDEO 12 FINAL · PRE-PUBLISH CHECKLIST")
r.bold = True
r.font.size = Pt(13)
r.font.color.rgb = RED

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Why Willpower Fails Every Payday · Baumeister Ego Depletion · Thaler & Benartzi · Save More Tomorrow")
r.font.size = Pt(9)
r.font.color.rgb = GREY

doc.add_paragraph()

# ── 1. FILENAME ──
add_section(doc, "1. NOMBRE DEL ARCHIVO — renombra el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO",
                "why-willpower-fails-every-payday-automatic-savings-neurocents.mp4",
                GREEN, 10)

divider(doc)

# ── 2. TÍTULO ──
add_section(doc, "2. TÍTULO — testear en VidIQ antes de publicar")
add_label_value(doc, "TÍTULO PRINCIPAL (outlier-validated)",
                "Why Willpower Fails Every Payday — And the One Decision That Stops It",
                DARK, 12)
add_block(doc,
          "Justificación: 132.7× outlier pattern. 'Why [X] Fails Every [Trigger]' — identidad + mecanismo + solución en 12 palabras.",
          size=8, color=GREEN)
add_block(doc, "Alternativa A: 'The One Decision That Defeats All Three Brain Traps' — mecanismo-first, menor CTR",
          size=8, color=GREY)
add_block(doc, "Alternativa B: 'Why Your Brain Spends Every Payday (And the One Move That Stops It)' — testear score",
          size=8, color=GREY)
add_block(doc, "⚠ El título principal tiene outlier pattern validado ('Why Willpower Fails'). Mantener si VidIQ ≥80.",
          size=8, color=RED)

divider(doc)

# ── 3. DESCRIPCIÓN ──
add_section(doc, "3. DESCRIPCIÓN — copia exactamente")

desc_lines = [
    "Alex watched the last video. He took notes. He sent it to his brother.",
    "On Friday, the salary notification arrived — and four hundred euros were gone again.",
    "",
    "Knowing the name of a trap is not the same as escaping it.",
    "The real fix requires removing the decision from Alex's hands entirely — not making it easier to get right.",
    "",
    "Roy Baumeister found that willpower depletes with every decision you make — not just financial ones.",
    "By payday, you have the least of it exactly when you need the most.",
    "In 1998, his radish experiment showed the mechanism clearly: same puzzle, different reserve.",
    "",
    "Richard Thaler and Shlomo Benartzi tested the solution at the University of Chicago in 2004.",
    "Workers who made one structural decision went from saving 3.5% to 13.6% in five years.",
    "No budgets. No willpower. No spreadsheets.",
    "",
    "In this video:",
    "→ Why understanding a bias doesn't stop it from running",
    "→ Roy Baumeister's ego depletion — the radish experiment",
    "→ Why the standing order fires one minute before the Reward Trap",
    "→ Save More Tomorrow (Thaler & Benartzi, 2004) — 3.5% to 13.6% in five years",
    "→ The Brain Villain's last trick — Present Bias wearing the costume of caution",
    "",
    "───────────────────────────────",
    "📌 Watch next → [PEGA AQUÍ URL DE V13 — TAX REFUND]",
    "📌 Previous: 3 Traps That Rewire Your Brain to Stay Broke → [PEGA AQUÍ URL DE V11]",
    "───────────────────────────────",
    "",
    "0:00  You've started a budget at least three times",
    "0:30  Why knowing isn't enough — Alex still spent it",
    "1:45  Roy Baumeister — ego depletion + radish experiment",
    "3:30  The standing order — how it beats all three traps",
    "5:00  The CTA",
    "5:15  Thaler & Benartzi — Save More Tomorrow",
    "6:30  The Brain Villain's last trick (Present Bias in disguise)",
    "7:30  Identity close + next video",
    "",
    "#behavioralfinance #automaticsavings #savingmoney #egodepletion #neurocents",
]

for line in desc_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(line)
    r.font.size = Pt(9)
    if line.startswith("Alex watched") or line.startswith("Knowing the name"):
        r.bold = True

divider(doc)

# ── 4. TAGS ──
add_section(doc, "4. TAGS — copia todo el bloque en YouTube Studio")
tags = (
    "automatic savings, ego depletion, save more tomorrow, willpower and money, "
    "behavioral finance, richard thaler, baumeister ego depletion, present bias, "
    "savings psychology, how to save money automatically, brain bias money, "
    "shlomo benartzi, standing order savings, psychology of saving, "
    "behavioral economics, neuroscience money, decision fatigue, neurocents, "
    "why willpower fails, radish experiment"
)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(tags)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TOP KEYWORDS POR SCORE VIDIQ (confirmar en VidIQ antes de publicar):", size=8, bold=True, color=GREY)
kw_rows = [
    ("behavioral finance",               "103K/mes", "27 comp.", "73 ← confirmado"),
    ("automatic savings",                "~67K/mes", "~31 comp.", "← testear"),
    ("how to save money automatically",  "~44K/mes", "~29 comp.", "← alto volumen"),
    ("ego depletion",                    "~12K/mes", "~18 comp.", "← gema oculta"),
    ("save more tomorrow",               "~8K/mes",  "~14 comp.", "← nicho fuerte"),
    ("baumeister ego depletion",         "~5K/mes",  "~10 comp.", "← long-tail preciso"),
    ("savings psychology",               "~22K/mes", "~25 comp.", "← testear"),
    ("willpower and money",              "~19K/mes", "~22 comp.", "← testear"),
    ("present bias",                     "~15K/mes", "~20 comp.", "← bajo comp."),
    ("why willpower fails",              "testear",  "—",         "← título exact match"),
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
add_label_value(doc, "CONCEPTO",
                "Alex con expresión de cansancio / revelación. Fondo blanco estilo Andy/MoneyTom.")
add_label_value(doc, "TEXTO THUMBNAIL",
                "WILLPOWER FAILS  (máx 5 palabras)")
add_label_value(doc, "OBJETO",
                "Villain pequeño vs. standing order (flecha verde) — contraste de tamaño")
add_block(doc, "Alternativa A: Alex exhausted (viernes) LEFT | Alex calm (martes) RIGHT — split panel antes/después.",
          size=8, color=GREY)
add_block(doc, "Alternativa B: Villain durmiendo / vencido, Alex de pie con brazo cruzado. Alex dominante.",
          size=8, color=GREY)
add_block(doc, "⚠ V11 usó villain activo + 3 trampas. V12: Alex dominante, villain en segundo plano o derrotado.",
          size=8, color=RED)
add_block(doc, "⚠ BLUE t-shirt en Alex — NO red. Verificar en Google Flow antes de generar.",
          size=8, color=RED)

divider(doc)

# ── 6. YOUTUBE STUDIO ──
add_section(doc, "6. YOUTUBE STUDIO — configuración antes de publicar")
checkboxes = [
    "Título:         Why Willpower Fails Every Payday — And the One Decision That Stops It",
    "Descripción:    Pegada completa con capítulos y URLs de V11 y V13",
    "Tags:           Todos pegados (ver sección 4)",
    "Categoría:      Education",
    "Miniatura:      Subida — fondo blanco, Alex dominante, texto WILLPOWER FAILS",
    "Capítulos:      Activados (timestamps en descripción)",
    "Subtítulos:     Auto-generados por YouTube (dejar activado)",
    "Visibilidad:    Público — programado 20:00-22:00 hora Bali (12:00-14:00 EST)",
    "Marca de agua:  Neurocents_Watermark.png subida en Studio",
]
for cb in checkboxes:
    add_checkbox(doc, cb)

divider(doc)

# ── 7. END SCREEN ──
add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: seleccionar V13 (Tax Refund — €800 disappears 3× faster) — NO 'mejor opción'")
add_checkbox(doc, "Botón suscripción")
add_block(doc,
          "Script end screen: 'Watch this next — Alex gets a tax refund. Eight hundred euros he wasn't expecting. "
          "His brain treats it completely differently. The money disappears three times faster. "
          "The reason is the one nobody expects.'",
          size=8, color=DARK)
add_block(doc, "⚠ Después de publicar V12: entrar a V11 y actualizar end screen apuntando a V12 específico",
          size=8, color=RED)

divider(doc)

# ── 8. CARDS ──
add_section(doc, "8. CARDS (tarjetas dentro del vídeo)")
add_checkbox(doc, "Minuto ~1:45 (BAUMEISTER) → card apuntando a V11 (3 Traps — contexto de trampas)")
add_checkbox(doc, "Minuto ~5:30 (THE SCIENCE) → card apuntando a V5 (Mental Accounting — Thaler conexión)")

divider(doc)

# ── 9. PLAYLIST ──
add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V12 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden sugerido: V11 → V12 → V13 (secuencia 3 Traps → One Decision → Tax Refund)")
add_checkbox(doc, "Pegar URL de playlist en descripción de V12")

divider(doc)

# ── 10. PRIMER COMENTARIO ──
add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Alex didn't need more willpower. He needed fewer decisions.\n"
    "One bank transfer, set up on a calm Tuesday — before the salary arrives.\n"
    "Drop 🧠 if you felt the discomfort when the standing order was explained. "
    "That was the Brain Villain identifying itself."
)
r.font.size = Pt(10)
r.font.color.rgb = DARK

divider(doc)

# ── 11. REDDIT ──
add_section(doc, "11. REDDIT — publicar 1h después de que el vídeo esté live")
reddit_posts = [
    ("r/personalfinance",       "Primero — ahorro automático, muy activo"),
    ("r/BehavioralEconomics",   "+30 min — Thaler & Benartzi + Baumeister"),
    ("r/psychology",            "+30 min — ego depletion / radish experiment"),
    ("r/cogsci",                "+30 min — sistema automático vs willpower"),
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
add_block(doc, "TÍTULO REDDIT (r/psychology / r/BehavioralEconomics):", size=8, bold=True, color=GREY)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Baumeister's 1998 radish experiment found that willpower depletes with every decision — not just financial ones. "
    "By payday (after 5 days of choosing), you have the least of it exactly when you need the most. "
    "The only real fix isn't a better budget. (Made a short video on the mechanism + the structural solution)"
)
r.font.size = Pt(9)
r.font.color.rgb = DARK

doc.add_paragraph()
add_block(doc, "TÍTULO REDDIT (r/personalfinance):", size=8, bold=True, color=GREY)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Thaler & Benartzi found that one structural decision — automatic redirect on raise day — "
    "took workers from 3.5% to 13.6% savings in 5 years. No budgets, no willpower. "
    "The insight isn't the savings rate — it's why the decision needs to happen on a Tuesday, not a Friday. "
    "(Short video on the mechanism)"
)
r.font.size = Pt(9)
r.font.color.rgb = DARK

divider(doc)

# ── 12. HORA ──
add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "BALI", "20:00 – 22:00", GREEN, 12)
add_label_value(doc, "EST",  "12:00 – 14:00 (prime time USA)", GREY, 9)
add_label_value(doc, "SECUENCIA",
                "Publicar V12 máximo 7 días después de V11 — son una unidad narrativa", GREY, 9)
add_block(doc, "⚠ V12 debe publicarse pronto después de V11 para mantener la continuidad narrativa.",
          size=8, color=RED)

divider(doc)

# ── 13. OUTLIER NOTES ──
add_section(doc, "13. NOTAS DE OUTLIER — por qué este título y este hook")
outlier_notes = [
    "TÍTULO: 'Why Willpower Fails Every Payday' — Outlier pattern validado (132.7×): 'Why [X] Fails Every [Trigger]'",
    "HOOK BEAT 1: Identity-first — espectador se reconoce antes de hacer clic (3 presupuestos, ninguno sobrevivió)",
    "BAUMEISTER EXPERIMENT: concreto, narrativo, contrastivo — mismo tipo de datos que generan retención alta",
    "VILLAIN INOCULATION (beats 76-86): segunda persona directa en tiempo real — sella el engagement con el concepto",
    "IDENTITY CLOSE: 'The programs are not broken' — cierre no moralista = mayor retención hasta el final",
]
for note in outlier_notes:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(f"→  {note}")
    r.font.size = Pt(8)
    r.font.color.rgb = DARK

divider(doc)

# ── FOOTER ──
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run(
    "NEUROCENTS · V12 FINAL · PRE-PUBLISH CHECKLIST · "
    "Why Willpower Fails Every Payday · Tags a confirmar en VidIQ"
)
fr.font.size = Pt(8)
fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V12_final_Prepublish_Checklist.docx"
doc.save(path)
print(f"Saved: {path}")
