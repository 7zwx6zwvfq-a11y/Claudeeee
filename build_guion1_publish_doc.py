#!/usr/bin/env python3
"""Pre-publish checklist — Guion 1 · Why Smart People Make Terrible Money Decisions."""

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
r = t.add_run("NEUROCENTS — GUION 1 · PRE-PUBLISH CHECKLIST"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RED
s = doc.add_paragraph(); s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Why Smart People Make Terrible Money Decisions · Creator Brief v4 · 138 beats")
r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()

add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "why-smart-people-make-terrible-money-decisions-neurocents.mp4", GREEN, 10)
divider(doc)

add_section(doc, "2. TÍTULO")
add_label_value(doc, "TÍTULO PRINCIPAL", "Why Smart People Make Terrible Money Decisions", DARK, 12)
add_block(doc, "Keyword pilar: 'loss aversion psychology' (17,243/mes · comp. 10.3 — mejor ratio volumen/"
               "competencia del canal hasta la fecha). Patrón de estatus/inteligencia (993x, S21) tal cual "
               "propuso VidIQ originalmente.", size=8, color=GREY)
add_block(doc, "NOTA: este título repite casi literalmente las 3 primeras palabras de V15 ('Why Smart People "
               "Can't Save Money'). Se había cambiado por eso, pero decisión del creador: mantenerlo igual — "
               "V15 está archivado y no se va a publicar, así que la colisión de wording no aplica en la práctica.",
               size=8, color=RED)
divider(doc)

add_section(doc, "3. DESCRIPCIÓN — copia exactamente")
add_text_block(doc, [
    "Alex made €140,000 a year. Master's degree. Read investment books on the train.",
    "The market dropped 9% in six weeks — and he sold everything in one afternoon.",
    "That year, the market gained 18%. He never bought back in.",
    "",
    "He didn't lose €34,000 by selling. He lost it by staying out.",
    "",
    "Three brain traps did this to him — and none of them look like what you'd expect.",
    "One feels like caution. One feels like loyalty. The worst one feels like discipline.",
    "",
    "This video breaks down all three with the real research behind them: Daniel Kahneman's",
    "Nobel Prize-winning work on loss aversion, the famous Cornell 'coffee mug' experiment on",
    "the endowment effect, and the 1985 study that named the disposition effect.",
    "",
    "───────────────────────────────",
    "📌 Watch next → the exact moment your brain decides to spend — three hours before you do it",
    "[PEGA AQUÍ URL cuando esté publicado — Guion 2, dopamine spending]",
    "───────────────────────────────",
    "",
    "0:00 The €34,000 mistake",
    "1:10 Trap 1 — The 2.5x Sting (Loss Aversion)",
    "2:55 If your brain is doing this right now — subscribe",
    "3:10 Trap 2 — The Ownership Markup (Endowment Effect)",
    "4:55 Trap 3 — The Backwards Sort (Disposition Effect)",
    "6:35 Honest counter — when selling IS the right call",
    "7:25 The real total (add up all three traps)",
    "8:35 Which one is running in you right now?",
    "",
    "(Timestamps aproximados — ajustar al montaje real)",
    "",
    "#lossaversion #behavioralfinance #financialpsychology #psychologyofmoney #neurocents",
], size=9)
divider(doc)

add_section(doc, "4. TAGS — copia todo el bloque")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("loss aversion psychology, endowment effect, disposition effect, behavioral finance, "
              "financial psychology, psychology of money, why smart people lose money, "
              "kahneman loss aversion, investing mistakes psychology, cognitive biases investing, "
              "endowment effect experiment, neurocents")
r.font.size = Pt(9); r.font.color.rgb = DARK
doc.add_paragraph()
add_block(doc, "TOP KEYWORDS:", size=8, bold=True, color=GREY)
for kw, vol in [("loss aversion psychology", "17,243/mes · comp. 10.3 — primario, mejor ratio del canal"),
                ("financial psychology", "120,680/mes · comp. 27 — validado S13"),
                ("psychology of money", "731,164/mes · comp. 57.5 — validado S13"),
                ("behavioral finance", "74,718/mes (2ª pasada VidIQ) ó 98,056/mes (S13) — cifra sin resolver, no usar como pilar")]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<28}"); r1.font.size = Pt(8)
    r2 = p.add_run(vol); r2.font.size = Pt(8); r2.font.color.rgb = GREY
divider(doc)

add_section(doc, "5. MINIATURA — Concepto B: SELL vs MARKET (elegido)")
add_label_value(doc, "ARCHIVO FINAL", "GUION1_Thumbnail_ConceptoB_SELLvsMARKET.png (1280×720)", GREEN, 10)
add_block(doc, "Split panel: izquierda 'SELL' — Alex pulsando botón rojo, pánico, brain villain visible, "
               "flecha roja cayendo. Derecha 'MARKET' — flecha verde +18%, silueta de Alex tachada en rojo "
               "(se lo perdió). Texto: 'HE PICKED SAFE.' / 'IT COST HIM €34,000'.", size=8, color=GREY)
add_block(doc, "Elegido sobre el Concepto A (ecuación) por ser más rico narrativamente — muestra el coste "
               "de oportunidad explícito, no solo la pérdida. Se descartó el Concepto C (tier list) por "
               "prometer un formato de ranking que el guion no entrega (desajuste S17).", size=8, color=GREY)
divider(doc)

add_section(doc, "6. YOUTUBE STUDIO")
for cb in [
    "Título:         Why Smart People Make Terrible Money Decisions",
    "Descripción:    Pegada completa — resumen + timestamps + tease Guion 2",
    "Tags:           Pegados (sección 4)",
    "Categoría:      Education",
    "Miniatura:      GUION1_Thumbnail_ConceptoB_SELLvsMARKET.png",
    "Capítulos:      Activados — uno por sección (Hook / Trap 1 / CTA / Trap 2 / Trap 3 / Honest Counter / System Close / Cierre)",
    "Subtítulos:     Auto-generados",
    "Visibilidad:    Público — próximo LUNES o JUEVES 20:15 CEST (= 14:15 EST) según hueco real en la cola",
    "Marca de agua:  Neurocents_Watermark.png",
]:
    add_checkbox(doc, cb)
divider(doc)

add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: Guion 2 (dopamine spending) — pegar URL cuando esté publicado")
add_checkbox(doc, "Mientras Guion 2 no exista: enlazar a V1 (Your Brain Is Keeping You Broke — intro del canal) o al vídeo más reciente publicado")
add_checkbox(doc, "Botón suscripción")
divider(doc)

add_section(doc, "8. CARDS")
add_checkbox(doc, "Minuto ~1:10 (2.5x Sting revelado) → card a V1 (tesis general del canal)")
add_checkbox(doc, "Minuto ~7:25 (el total sumado) → card al vídeo más reciente publicado del canal")
divider(doc)

add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir a la playlist principal del canal")
add_checkbox(doc, "Crear/usar playlist 'Creator Brief v4' si se quiere agrupar esta nueva tanda de guiones")
divider(doc)

add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Which one is running in you right now — the fear, the loyalty, or the discipline that isn't? 👇\n\n"
    "Mine's the Backwards Sort (#3) — I sell winners way too early. What's yours?"
)
r.font.size = Pt(10); r.font.color.rgb = DARK
divider(doc)

add_section(doc, "11. REDDIT — publicar el día de publicación")
for sub, note in [
    ("r/investing",      "Primero — ángulo Kahneman/loss aversion aplicado a decisiones de venta reales"),
    ("r/personalfinance", "+30 min — el endowment effect aplicado a acciones de tu propia empresa"),
    ("r/psychology",      "+30 min — los 3 sesgos como mecanismo, no como carácter"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<20}"); r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(note); r2.font.size = Pt(8); r2.font.color.rgb = GREY
doc.add_paragraph()
add_block(doc, "BORRADOR r/investing (150-200 palabras, sin spam, aporta valor primero):", size=9, bold=True, color=DARK)
add_text_block(doc, [
    "",
    "Title: Ran the real numbers on why panic-selling during a dip usually costs more than the dip itself",
    "",
    "Kahneman's research puts a number on it: losses feel about 2.5x more intense than equivalent",
    "gains. So a 9% drop doesn't get processed as 'maybe temporary' — it gets processed as an",
    "emergency, right now.",
    "",
    "Modeled a specific case: someone sells everything during a 9% dip, the market recovers and",
    "gains 18% that year, and they never buy back in. The €34,000 they 'lost' wasn't from selling —",
    "it was from staying out afterward.",
    "",
    "Two other biases compound this one: the endowment effect (holding your own company's stock",
    "too long because it's yours, not because the data supports it) and the disposition effect —",
    "the well-documented tendency to sell winners early and hold losers long, found across almost",
    "every retail portfolio studied since 1985.",
    "",
    "Made a video walking through all three with the actual studies if anyone wants the full",
    "breakdown: [URL]",
], size=8)
divider(doc)

add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "Próximo LUNES o JUEVES 20:15 (confirmar hueco en la cola actual)", GREEN, 12)
add_label_value(doc, "EST", "14:15 · UTC 18:15", GREY, 9)
divider(doc)

add_section(doc, "13. NOTAS — decisiones tomadas en esta tanda")
for note in [
    "→ Primer guion de la arquitectura 'Creator Brief v4' (CLAUDE.md S25): canal sigue siendo Neurocents "
    "(Alex + Brain Villain + neurociencia real), pero con conceptos accesibles a público general y la "
    "estructura de guion viral derivada de 4 outliers de otros nichos finance.",
    "→ Trap 3 cambiado de Sunk Cost Fallacy (propuesta original de VidIQ) a Disposition Effect para no "
    "duplicar V10, que ya cubre sunk cost/Concorde.",
    "→ Guion revisado dos veces tras críticas propias: v1→v2 añadió honest counter cuantificado, scoreboard "
    "combinado (€51,600 total), etiquetas propias (2.5x Sting / Ownership Markup / Backwards Sort) y la "
    "pregunta-espejo final. v2→v3 corrigió un desajuste hook/pago ('patience' vs 'discipline'), una cifra "
    "de tiempo incorrecta ('18 meses' no cuadraba con la línea temporal real de ~4 años, eliminada), y una "
    "colisión de marca ('2.5x Tax' vs la 'Bandwidth Tax' ya usada en V3).",
    "→ Thumbnail: se generaron y compararon 3 conceptos (ecuación / split panel / tier list). Se descartó "
    "el tier list por prometer un formato de ranking que el contenido no entrega. Elegido: Concepto B "
    "(SELL vs MARKET), por representar con más fidelidad el mecanismo real del vídeo (coste de oportunidad).",
    "→ Sin acceso a VidIQ en vivo en esta sesión — los volúmenes de keyword vienen de la tabla ya validada "
    "del canal (S13/S25). La cifra de 'behavioral finance' tiene dos versiones distintas sin resolver — "
    "no usarla como keyword pilar hasta verificar en YouTube Studio o VidIQ directamente.",
    "→ Producción de imágenes (138 beats + thumbnail) delegada a Claude Cowork vía GUION1_COWORK_HANDOFF.md, "
    "que incluye guion completo, estilo visual bloqueado y regla de consistencia con Magnific.",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note); r.font.size = Pt(9); r.font.color.rgb = DARK
divider(doc)

doc.add_paragraph()
foot = doc.add_paragraph(); foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · GUION 1 · PRE-PUBLISH CHECKLIST · Why Smart People Make Terrible Money Decisions")
fr.font.size = Pt(8); fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/GUION1_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
