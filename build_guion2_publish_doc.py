#!/usr/bin/env python3
"""Pre-publish checklist — Guion 2 · Your Brain Treats Spending Like a Drug."""

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
r = t.add_run("NEUROCENTS — GUION 2 · PRE-PUBLISH CHECKLIST"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RED
s = doc.add_paragraph(); s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run("Your Brain Treats Spending Like a Drug (And It Knows Exactly When to Strike) · Creator Brief v4 · 133 beats")
r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()

add_section(doc, "1. NOMBRE DEL ARCHIVO — renombrar el MP4 ANTES de subir")
add_label_value(doc, "ARCHIVO", "your-brain-treats-spending-like-a-drug-neurocents.mp4", GREEN, 10)
divider(doc)

add_section(doc, "2. TÍTULO")
add_label_value(doc, "TÍTULO PRINCIPAL", "Your Brain Treats Spending Like a Drug (And It Knows Exactly When to Strike)", DARK, 12)
add_block(doc, "Keyword pilar: 'dopamine spending' (5,190/mes · comp. 15.6 — S25). Fórmula paréntesis "
               "contrapunto (S21, patrón de máximo multiplicador en outliers de neurociencia).", size=8, color=GREY)
add_block(doc, "Diferenciación vs V2 ('Why Buying Feels Better Than Having'): V2 cubre la dopamina de la "
               "COMPRA/tenencia en sí. Este guion cubre la dopamina de la ANTICIPACIÓN — el hit ocurre al ver "
               "la notificación, antes de que exista ninguna compra. Cero solape de mecanismo o cita.", size=8, color=GREY)
divider(doc)

add_section(doc, "3. DESCRIPCIÓN — copia exactamente")
add_text_block(doc, [
    "It's 11:47pm. Alex sees a notification: 24-hour sale, 30% off.",
    "He doesn't buy anything for three more hours. At 2:50am, he finally taps confirm.",
    "",
    "Ask him when he decided, and he'll say 2:50am. He's wrong.",
    "",
    "His brain already got its reward the instant the screen lit up — three hours before",
    "any money changed hands. The purchase itself was almost irrelevant.",
    "",
    "Three traps run on this exact mechanism, and none of them feel like what you'd expect.",
    "One feels like excitement. One feels like relief. The one nobody suspects feels like",
    "just moving on.",
    "",
    "This video breaks down all three with the real research behind them: Wolfram Schultz's",
    "Cambridge experiments on reward prediction error (the discovery that dopamine fires at",
    "the SIGNAL, not the reward), and Van Boven & Gilovich's Cornell study on why material",
    "purchases fade in 48 hours while experiences don't.",
    "",
    "───────────────────────────────",
    "📌 Watch next → why your brain treats your future self like a complete stranger",
    "[PEGA AQUÍ URL cuando esté publicado — Guion 3, present bias / future self]",
    "───────────────────────────────",
    "",
    "0:00 The 11:47pm notification",
    "0:50 What nobody tells you about impulse spending",
    "1:35 Trap 1 — The Maybe Hit (Schultz's monkeys)",
    "3:04 If your brain is doing this right now — subscribe",
    "3:17 Trap 2 — The 48-Hour Fade (Van Boven & Gilovich)",
    "5:24 Trap 3 — The Empty Refill",
    "7:14 Honest counter — when it's a real need, not the Villain",
    "8:22 The system: €2,870, one loop, three traps",
    "10:37 Which part is running in you tonight?",
    "",
    "(Timestamps aproximados — ajustar al montaje real)",
    "",
    "#dopaminespending #impulsespending #behavioralfinance #financialpsychology #neurocents",
], size=9)
divider(doc)

add_section(doc, "4. TAGS — copia todo el bloque")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run("dopamine spending, impulse spending psychology, reward prediction error, wolfram schultz dopamine, "
              "why do i impulse buy, dopamine and money, behavioral finance, financial psychology, "
              "impulse buying science, buyer's remorse psychology, neurocents")
r.font.size = Pt(9); r.font.color.rgb = DARK
doc.add_paragraph()
add_block(doc, "TOP KEYWORDS:", size=8, bold=True, color=GREY)
for kw, vol in [("dopamine spending", "5,190/mes · comp. 15.6 — primario, S25"),
                ("impulse spending psychology", "5,039/mes · comp. 5.3 — mejor ratio competencia/volumen de la tanda"),
                ("financial psychology", "120,680/mes · comp. 27 — validado S13"),
                ("behavioral finance", "74,718/mes (2ª pasada VidIQ) ó 98,056/mes (S13) — cifra sin resolver, no usar como pilar")]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{kw:<28}"); r1.font.size = Pt(8)
    r2 = p.add_run(vol); r2.font.size = Pt(8); r2.font.color.rgb = GREY
divider(doc)

add_section(doc, "5. MINIATURA — concepto rewind-arrow (elegido)")
add_block(doc, "Generada vía Magnific en esta sesión (2 conceptos comparados) — elegido el que muestra la "
               "flecha roja de rewind desde el dedo/CONFIRM ORDER hacia la notificación original, con el "
               "Brain Villain ya iluminado en rosa dentro del cráneo transparente, brazos cruzados, sonrisa "
               "satisfecha, como si ya hubiera cobrado. Estilo doodle: fondo negro puro en la escena nocturna, "
               "trazo grueso irregular, sin texto salvo el número/hora si aplica.", size=8, color=GREY)
add_block(doc, "PENDIENTE: el archivo final aún no se ha descargado a este repo — las dos opciones generadas "
               "están disponibles solo como enlaces webUrl de Magnific (bloqueo de red del contenedor impide "
               "la descarga directa aquí). Descargar manualmente desde Magnific y guardarlo como "
               "GUION2_Thumbnail_Final.png antes de publicar.", size=8, color=RED)
divider(doc)

add_section(doc, "6. YOUTUBE STUDIO")
for cb in [
    "Título:         Your Brain Treats Spending Like a Drug (And It Knows Exactly When to Strike)",
    "Descripción:    Pegada completa — resumen + timestamps + tease Guion 3",
    "Tags:           Pegados (sección 4)",
    "Categoría:      Education",
    "Miniatura:      GUION2_Thumbnail_Final.png (descargar de Magnific antes de subir — ver sección 5)",
    "Capítulos:      Activados — uno por sección (Hook / Trap 1 / CTA / Trap 2 / Trap 3 / Honest Counter / System Close / Cierre)",
    "Subtítulos:     GUION2.srt ya generado — subir en vez de depender del auto-generado",
    "Visibilidad:    Público — próximo LUNES o JUEVES 20:15 CEST (= 14:15 EST) según hueco real en la cola",
    "Marca de agua:  Neurocents_Watermark.png",
]:
    add_checkbox(doc, cb)
divider(doc)

add_section(doc, "7. END SCREEN — últimos 20 segundos")
add_checkbox(doc, "Vídeo: Guion 3 (present bias / future self as stranger) — pegar URL cuando esté publicado")
add_checkbox(doc, "Mientras Guion 3 no exista: enlazar a Guion 1 (Why Smart People Make Terrible Money Decisions) o al vídeo más reciente publicado")
add_checkbox(doc, "Botón suscripción")
divider(doc)

add_section(doc, "8. CARDS")
add_checkbox(doc, "Minuto ~1:35 (Maybe Hit revelado) → card a V2 (Why Buying Feels Better Than Having — dopamina relacionada, ángulo distinto)")
add_checkbox(doc, "Minuto ~8:22 (el total de €2,870) → card al vídeo más reciente publicado del canal")
divider(doc)

add_section(doc, "9. PLAYLIST")
add_checkbox(doc, "Añadir a la playlist principal del canal")
add_checkbox(doc, "Añadir a la playlist 'Creator Brief v4' (junto a Guion 1)")
divider(doc)

add_section(doc, "10. PRIMER COMENTARIO — fijar nada más publicar")
p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.5)
r = p.add_run(
    "Which part is running in you tonight — the maybe, the fade, or the quiet refill? 👇\n\n"
    "Mine's the Empty Refill (#3) — I never feel like I'm chasing anything, I just keep 'finding good deals.' What's yours?"
)
r.font.size = Pt(10); r.font.color.rgb = DARK
divider(doc)

add_section(doc, "11. REDDIT — publicar el día de publicación")
for sub, note in [
    ("r/personalfinance", "Primero — ángulo directo: por qué el 'buyer's remorse' no llega antes de comprar"),
    ("r/AntiConsumption",  "+30 min — encaja de forma natural con el tema del sub (compras impulsivas, 14 objetos olvidados)"),
    ("r/psychology",       "+30 min — el mecanismo de Schultz (reward prediction error) como hallazgo central"),
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{sub:<20}"); r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(note); r2.font.size = Pt(8); r2.font.color.rgb = GREY
doc.add_paragraph()
add_block(doc, "BORRADOR r/personalfinance (150-200 palabras, sin spam, aporta valor primero):", size=9, bold=True, color=DARK)
add_text_block(doc, [
    "",
    "Title: The 'buyer's remorse' timeline is backwards — the dopamine hit happens before you buy, not after",
    "",
    "There's a well-known experiment (Wolfram Schultz, Cambridge) where monkeys got a light cue",
    "followed by juice two seconds later. After a few repetitions, the dopamine neurons stopped",
    "firing for the juice — they fired for the light instead. The brain rewards the SIGNAL that",
    "something good might be coming, not the reward itself.",
    "",
    "That's exactly what a 'flash sale' notification does. The dopamine hit fires the instant you",
    "see it — hours before you actually check out. By the time you pay, your brain has already",
    "moved on. Tracked this for one person: 14 separate 'impulse' purchases in a year, €2,870",
    "total, almost none of it still felt like anything within days.",
    "",
    "The part that surprised me most: the 'I just like finding good deals' feeling isn't wrong,",
    "it's just the same mechanism wearing a different outfit — once a want is satisfied, a system",
    "built to search just goes looking for the next thing to search for.",
    "",
    "Made a video walking through the full mechanism and the actual studies if useful: [URL]",
], size=8)
divider(doc)

add_section(doc, "12. HORA DE PUBLICACIÓN")
add_label_value(doc, "ESPAÑA (CEST)", "Próximo LUNES o JUEVES 20:15 (confirmar hueco en la cola actual — después de Guion 1)", GREEN, 12)
add_label_value(doc, "EST", "14:15 · UTC 18:15", GREY, 9)
divider(doc)

add_section(doc, "13. NOTAS — decisiones tomadas en esta tanda")
for note in [
    "→ Segundo guion de la arquitectura 'Creator Brief v4' (CLAUDE.md S25). Formato: Alex hiperespecífico "
    "(11:47pm, notificación de venta flash) → 3 traps → CTA (~32-34%) → Honest Counter cuantificado → "
    "System Close → Identity Close + pregunta-espejo + tease.",
    "→ Hook reescrito una vez tras autocrítica (7/10 inicial): Beat 1 original era demasiado narrativo/scene-"
    "setting (violaba S19 — 'primeros 5 segundos'), y el giro tardaba ~30s en llegar (fuera del límite de 20s "
    "de S17). Se reescribieron los beats 1-9 con dirección de Camera/CapCut Motion explícita para comprimir "
    "el giro a ~24s y activar el Brain Villain en Beat 2 (no Beat 1), demostrando visualmente la propia tesis "
    "del hook antes de que la narración la explique.",
    "→ Verificación de frescura contra Guion 1: comparación línea a línea encontró 8 coincidencias — 2 frases "
    "de marca obligatorias (aceptadas, S3) y 6 dispositivos propios reciclados (violación real de la regla de "
    "frescura) — las 6 se reescribieron con redacción nueva antes de dar el guion por bueno.",
    "→ Tercer trap (Empty Refill) usa un segundo hallazgo de Schultz sobre extinción de la señal dopaminérgica, "
    "en vez de la propuesta original ('Reward Resetting' ligada al ingreso), que se descartó por solapar con "
    "el mecanismo previsto para Guion 4 (hedonic treadmill / lifestyle creep).",
    "→ Producción de imágenes (133 beats) completada vía Claude Cowork con Magnific, estilo doodle (fondo "
    "negro en escena nocturna de apertura, fondo blanco en el resto). Los 133 PNG ya generados y descargados "
    "por el usuario mediante script PowerShell local (bloqueo de red de este contenedor impide la descarga "
    "directa desde aquí). GUION2_IMAGE_PROMPTS.pdf reconstruido a partir de los metadatos de cada creación "
    "para revisión de producción.",
    "→ SRT (GUION2.srt) y hoja de montaje (GUION2_editing_sheet.csv) generados a partir del timeline exportado "
    "de Cowork — timestamps exactos por beat listos para importar en el editor.",
    "→ Miniatura: 2 conceptos generados vía Magnific en esta sesión, elegido el de la flecha de rewind. "
    "Archivo final pendiente de descarga manual (ver sección 5) — mismo bloqueo de red del CDN de Magnific.",
]:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.3)
    r = p.add_run(note); r.font.size = Pt(9); r.font.color.rgb = DARK
divider(doc)

doc.add_paragraph()
foot = doc.add_paragraph(); foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = foot.add_run("NEUROCENTS · GUION 2 · PRE-PUBLISH CHECKLIST · Your Brain Treats Spending Like a Drug")
fr.font.size = Pt(8); fr.font.color.rgb = GREY

path = "/home/user/Claudeeee/GUION2_Prepublish_Checklist.docx"
doc.save(path)
print(f"✅ Saved: {path}")
