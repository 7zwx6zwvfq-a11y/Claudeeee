#!/usr/bin/env python3
"""Pre-publish checklist — V17 · Two People, Same Salary: Why Only One Stops Working at 45."""

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
r = t.add_run("NEUROCENTS — VIDEO 17 · PRE-PUBLISH CHECKLIST"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RED
s = doc.add_paragraph(); s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Two People, Same Salary: Why Only One Stops Working at 45 · COMPARATIVA · Jueves 20:15 CEST")
r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()

add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "two-people-same-salary-stops-working-45-financial-psychology-neurocents.mp4", GREEN, 10)
divider(doc)

add_section(doc, "2. TÍTULO — patrón comparativa sector-wide")
add_label_value(doc, "TÍTULO PRINCIPAL", "Two People, Same Salary: Why Only One Stops Working at 45", DARK, 12)
add_block(doc, "Patrón: comparativa universal (outlier 'Real Estate vs Stocks' 1.5M) + número concreto (45) + curiosity gap.", size=8, color=GREY)
add_block(doc, "Sector-wide S22: 'same salary' lo entiende el 100% de la audiencia en 1 segundo. Sin jerga de nicho.", size=8, color=GREY)
divider(doc)

add_section(doc, "3. DESCRIPCIÓN — copia exactamente")
add_text_block(doc, [
    "Leo and Marc get the same raise email at the same minute. Same company, same salary,",
    "same city, same rent. Twenty years later, one of them tells his boss he's not coming back.",
    "He's forty-five. The other one can't afford to say that sentence — ever.",
    "",
    "The difference between their lives fits on a napkin:",
    "→ Live on your first real salary",
    "→ Bank every raise automatically, the month it arrives",
    "→ Upgrade your life once every five years — on purpose, never by drift",
    "",
    "In this video: the year-by-year math (34K → 126K → 318K → 640K), why your brain",
    "desperately wants Leo's path, the honest price of freedom (two decades of looking average),",
    "and the one email that decides which of the two you become.",
    "",
    "───────────────────────────────",
    "📌 Watch next → [PEGA AQUÍ URL DE V16 — Every Money Bias Explained]",
    "───────────────────────────────",
    "",
    "0:00 The same email",
    "0:40 The fair fight",
    "1:15 Year one — identical",
    "1:50 The split: one rule",
    "2:30 Year five — Leo looks like the winner",
    "3:20 Year ten — the invisible line",
    "4:10 Year fifteen — the curve stops being polite",
    "4:50 Year twenty — one of them is free",
    "5:30 The napkin, written out",
    "6:00 Why your brain picks Leo",
    "6:45 To be fair to Leo",
    "7:00 Which bet are you placing?",
    "",
    "(Timestamps aproximados — ajustar al montaje real)",
    "",
    "#personalfinance #financialpsychology #behavioralfinance #compoundinterest #neurocents",
], size=9)
divider(doc)

add_section(doc, "4. TAGS — copia todo el bloque")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("same salary different results, lifestyle inflation, bank your raise, compound interest, "
              "financial independence, retire at 45, stop working, personal finance psychology, "
              "behavioral finance, financial psychology, why one gets rich, wealth building, "
              "pay raise what to do, lifestyle creep, money psychology, neurocents")
r.font.size = Pt(9); r.font.color.rgb = DARK
doc.add_paragraph()
add_block(doc, "TOP KEYWORDS:", size=8, bold=True, color=GREY)
for kw, vol in [("financial independence", "~90K/mes — alto volumen"),
                ("lifestyle creep", "~15K/mes — exact match del mecanismo"),
                ("compound interest", "~200K/mes — evergreen"),
                ("financial psychology", "120K/mes · 74.7 — primario del canal")]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<28}"); r1.font.size = Pt(8)
    r2 = p.add_run(vol); r2.font.size = Pt(8); r2.font.color.rgb = GREY
divider(doc)

add_section(doc, "5. MINIATURA — SPLIT Leo vs Marc")
add_label_value(doc, "CONCEPTO", "Split vertical: IZQ Leo 45 años (blazer, coche, copa — pero encadenado a un escritorio con "
                                  "un grillete sutil). DER Marc 45 (camiseta gris de siempre — sentado libre en una colina al amanecer).")
add_label_value(doc, "TEXTO", "SAME SALARY. — una sola línea gigante, Impact negro; el punto final en rojo (#C62828)")
add_label_value(doc, "FONDO", "BLANCO puro ambos lados; línea divisoria negra fina al centro")
add_block(doc, "■ La ironía visual ES el gancho: el 'ganador' aparente está encadenado; el 'promedio' está libre.", size=8, color=RED)
add_block(doc, "■ Test 200px: las dos figuras + SAME SALARY legibles. Expresiones: Leo tenso, Marc en paz.", size=8, color=RED)
add_block(doc, "PROMPT GOOGLE FLOW: Flat 2D cartoon, thick black outlines, solid fills, no gradients, white background, "
               "16:9 1280×720. LEFT: LEO, 45, navy blazer, holding wine glass, nice car silhouette behind — but a subtle "
               "shackle chains his ankle to an office desk; tense forced smile. RIGHT: MARC, 45, plain gray t-shirt, "
               "sitting relaxed on a hilltop at sunrise, arms back, at peace. Thin black vertical divider. "
               "TEXT top center: 'SAME SALARY.' ultra-bold Impact black, final period in red #C62828. "
               "Both expressions must read clearly at 200px.", size=8, color=GREY)
divider(doc)

add_section(doc, "6. YOUTUBE STUDIO")
for cb in [
    "Título:         Two People, Same Salary: Why Only One Stops Working at 45",
    "Descripción:    Pegada completa con capítulos + URL V16",
    "Tags:           Pegados (sección 4)",
    "Categoría:      Education",
    "Miniatura:      Split Leo/Marc + SAME SALARY., fondo blanco",
    "Capítulos:      Activados — los checkpoints de año son los capítulos",
    "Subtítulos:     Auto-generados",
    "Visibilidad:    Público — JUEVES 20:15 CEST (= 14:15 EST)",
    "Marca de agua:  Neurocents_Watermark.png",
]:
    add_checkbox(doc, cb)
divider(doc)

add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: V16 (Every Money Bias) — hasta que V18 exista, luego actualizar a V18")
add_checkbox(doc, "Botón suscripción")
add_block(doc, "⚠ Al publicar V17: entrar a V16 y actualizar su end screen para apuntar a V17 (cierra el tease del catálogo).", size=8, color=RED)
divider(doc)

add_section(doc, "8. CARDS")
add_checkbox(doc, "Minuto ~3:20 (year ten / invisible line) → card a V15 (la transferencia automática — mecanismo hermano)")
add_checkbox(doc, "Minuto ~6:00 (why your brain picks Leo) → card a V16 (el catálogo de sesgos)")
divider(doc)

add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir V17 a playlist 'How Your Brain Costs You Money — Neurocents'")
add_checkbox(doc, "Orden trilogía nueva: V16 → V17 → V18")
divider(doc)

add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Be honest: which one are you right now — Leo or Marc?\n\n"
    "No judgment either way. Leo's wine was real. Marc's freedom is real.\n"
    "The only wrong answer is not knowing which bet you're placing.\n\n"
    "(And if you got a raise this year: what did it become?)"
)
r.font.size = Pt(10); r.font.color.rgb = DARK
divider(doc)

add_section(doc, "11. REDDIT — publicar 1h después de live")
for sub, note in [
    ("r/financialindependence", "Primero — retire-at-45 es literalmente su tema"),
    ("r/personalfinance",       "+30 min — ángulo 'what to do with a raise'"),
    ("r/Fire",                  "+30 min — the napkin rule"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<28}"); r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(note); r2.font.size = Pt(8); r2.font.color.rgb = GREY
doc.add_paragraph()
add_block(doc, "BORRADOR r/financialindependence:", size=9, bold=True, color=DARK)
add_text_block(doc, [
    "",
    "Title: Ran the 20-year math on two identical careers where the only difference is what happens to each raise. The gap is bigger than I expected.",
    "",
    "Same starting salary (28K), same promotions, same city. Person A upgrades lifestyle with",
    "each raise (normal behavior). Person B lives on the original salary and banks every raise",
    "automatically, upgrading deliberately every 5 years.",
    "",
    "Year 5: 4K vs 34K. Year 10: ~20K vs 126K. Year 20: person B sits at ~640K invested —",
    "enough that the portfolio's return covers his base lifestyle. Same career. One rule.",
    "",
    "The interesting part isn't the math (it's just compounding) — it's why almost nobody does it:",
    "banking a raise gives you nothing to show anyone. No photos, no applause. The cost of the",
    "path is two decades of looking average, and most people can't pay that — not because of",
    "math, because of mirrors.",
    "",
    "Video with the full year-by-year breakdown: [URL]",
], size=8)
divider(doc)

add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "JUEVES 20:15", GREEN, 12)
add_label_value(doc, "EST", "14:15 · UTC 18:15", GREY, 9)
add_label_value(doc, "SECUENCIA", "V16 ya publicado → V17 → V18 (banco listo)", GREY, 9)
divider(doc)

add_section(doc, "13. NOTAS — por qué este título y esta estructura")
for note in [
    "→ FORMATO 2 Comparativa (primera vez) — patrón del outlier 1.5M. La retención está en el esqueleto: "
    "checkpoints temporales = re-pregunta implícita '¿quién gana AHORA?' cada 60-90s.",
    "→ PERSONAJES NUEVOS (Leo/Marc) — Alex y Brain Villain descansan. Frescura estructural máxima tras V16 sin personaje.",
    "→ HOOK S3 In Medias Res (última vez V9): el email llega en el beat 1, el flash-forward al minuto 0:15.",
    "→ FAIRNESS PIVOT: defender a Leo compra la confianza de los dos bandos y enciende el debate en comentarios.",
    "→ LAPIDARIAS: 'two salaries: his — and his money's' / 'two decades of looking average' / 'because of mirrors'.",
    "→ CERO solape con V15: V15 = automatizar el ahorro base. V17 = qué hacer con LAS SUBIDAS. Mecanismos distintos.",
    "→ CTR TARGET: >6% · Retención 30s >50% (el flash-forward del beat 3 es el candado).",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note); r.font.size = Pt(9); r.font.color.rgb = DARK
divider(doc)

doc.add_paragraph()
foot = doc.add_paragraph(); foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · V17 · PRE-PUBLISH CHECKLIST · Two People, Same Salary · Jueves 20:15 España")
fr.font.size = Pt(8); fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/V17_final_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
