#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build beats (timecoded, ~9-11 word chunks) for the Atun video.
No hay librería de stock real todavía (pendiente de búsqueda en Freepik),
así que cada beat lleva una SUGERENCIA VISUAL descriptiva en vez de un ID de clip real."""
import re
import csv

from atun_full_script import SECTIONS

TARGET_SECONDS = 26 * 60  # objetivo de duración de render: 26:00 (dentro del rango 25-27 pedido)

MOTIONS = [
    "ZOOM IN SLOW · 4s", "PAN RIGHT · 4s", "ZOOM OUT SLOW · 4s",
    "STATIC", "PAN LEFT · 4s", "DIAGONAL PAN + ZOOM IN · 4s",
    "ZOOM IN FAST · 2s", "PAN UP · 4s",
]

# Sugerencias visuales rotativas por sección (conceptos, no clips reales todavía)
SECTION_VISUALS = {
    "HOOK": [
        "Estanterías de supermercado genérico llenas de latas de atún",
        "Mano comparando dos latas de atún de marcas distintas",
        "Mapa animado con banderas de España, México, Chile, Ecuador y Costa Rica conectándose",
        "Primer plano de la parte trasera de una lata, texto legal en letra pequeña",
        "Animación de red corporativa: un nodo central expandiéndose hacia varios logos genéricos",
        "Carro de la compra avanzando por el pasillo de conservas",
        "Reloj o calendario pasando páginas rápido (paso del tiempo / rutina de compra)",
        "Persona leyendo el envase de una lata con cara de duda",
    ],
    "MARCA 7 - HACENDADO": [
        "Exterior genérico de supermercado tipo gran superficie",
        "Lineal de marca blanca con latas de atún idénticas en diseño",
        "Primer plano de una lata de atún estilo marca blanca (sin logo real)",
        "Interior de fábrica conservera, cinta transportadora con latas",
        "Animación de red corporativa: logo del súper conectado a un fabricante oculto detrás",
        "Documento / informe corporativo genérico en pantalla (memoria de sostenibilidad)",
        "Sello circular tipo certificación de pesca sostenible",
        "Mapa de Galicia con un pin marcando una fábrica",
    ],
    "MARCA 6 - ROBINSON CRUSOE": [
        "Costa rocosa e isla vista aérea (estilo Pacífico sur)",
        "Lata de atún genérica con diseño de bandera chilena de fondo",
        "Mapa animado con línea conectando Chile y España",
        "Barco pesquero navegando en mar abierto",
        "Planta de envasado de conservas, trabajadores con cofia",
        "Bandera de Chile ondeando",
        "Bandera de España ondeando",
        "Animación de red corporativa uniendo dos marcas bajo un mismo logo paraguas",
    ],
    "MARCA 5 - ISABEL": [
        "Mapa animado con España, Ecuador, Perú, Colombia y México iluminándose uno a uno",
        "Lineal de supermercado con latas de atún en primer plano, foco desenfocado en el fondo",
        "Animación de accionariado: dos empresas pequeñas conectadas a una multinacional más grande",
        "Primer plano de etiqueta trasera de lata con texto de especie y zona de pesca",
        "Lupa sobre un párrafo de texto legal en un envase",
        "Icono o gráfico de advertencia junto a un símbolo de balanza / mercurio",
        "Dos latas de atún casi idénticas, una junto a otra, distinguibles solo por una palabra",
        "Familia numerosa repartida en una videollamada (metáfora de países distintos, misma marca)",
    ],
    "CTA SUTIL (~35%)": [
        "Icono de campana de notificación animándose suavemente",
        "Mano tocando la pantalla de un móvil sobre un botón de suscripción genérico",
        "Interfaz genérica de vídeo online con botón de suscribirse resaltado",
    ],
    "MARCA 4 - CARREFOUR": [
        "Exterior genérico de híper con carritos en fila",
        "Lineal de marca blanca en tonos azules y blancos",
        "Dos botellas/latas comparadas: una con aceite de oliva, otra con aceite de girasol",
        "Documento con tabla de resultados de un análisis de calidad (genérico, sin logos)",
        "Báscula de cocina pesando el contenido de una lata escurrida",
        "Primer plano de sal derramándose sobre una superficie",
        "Tabla comparativa animada: peso neto vs peso escurrido",
        "Persona leyendo la etiqueta trasera de una lata en el pasillo",
    ],
    "MARCA 3 - ORTIZ": [
        "Fábrica conservera de aspecto artesanal, ladrillo visto, maquinaria antigua",
        "Lata de atún de diseño vintage/premium sobre fondo de madera",
        "Documento de análisis de consumo con sello de 'resultado' genérico",
        "Primer plano de sal en un salero de cocina",
        "Mesa puesta con mantel elegante, lata de atún gourmet como centro de mesa",
        "Tienda delicatessen / gourmet con productos premium en estantería de madera",
    ],
    "MARCA 2 - NOSTROMO": [
        "Lata de atún con estética italiana (colores cálidos, tipografía clásica)",
        "Mapa animado con línea conectando España e Italia",
        "Animación de red corporativa: dos marcas con logos distintos convergiendo en una sola empresa",
        "Lineal de supermercado con dos marcas de diseño opuesto (una grande, otra 'artesanal') juntas",
        "Interior de fábrica conservera genérica, líneas de producción paralelas",
    ],
    "MARCA 1 - CALVO": [
        "Metraje de archivo en blanco y negro, fábrica de conservas años 40-50",
        "Máquina industrial de enlatado en movimiento, estilo retro",
        "Flota de barcos pesqueros en un puerto gallego",
        "Mapa mundial animado con puntos iluminándose en más de setenta países",
        "Bandera de Brasil ondeando",
        "Gráfico de barras ascendente representando crecimiento regional",
        "Familia genérica reunida en torno a una mesa de despacho (protocolo familiar / empresa familiar)",
        "Documento corporativo con el logo de dos empresas conectadas por una línea de accionariado",
        "Primer plano de una lata de atún icónica sobre fondo neutro",
    ],
    "MEJOR OPCION 3 - FRINSA": [
        "Barco pesquero propio saliendo a faenar al amanecer",
        "Planta procesadora de pescado con trabajadores en primer plano",
        "Mapa de Galicia con costa marcada",
        "Cinta transportadora con lomos de atún antes de enlatar",
    ],
    "MEJOR OPCION 2 - PALACIO DE ORIENTE": [
        "Fachada de fábrica histórica en Vigo, ladrillo antiguo",
        "Fotografía de archivo en sepia de una conservera de principios del siglo XX",
        "Trabajador artesanal seleccionando pescado a mano",
        "Lata de atún de diseño clásico/artesanal sobre mesa de madera",
    ],
    "MEJOR OPCION 1 - CONSORCIO": [
        "Mesa de selección manual de lomos de atún, trabajador revisando pieza a pieza",
        "Primer plano de manos colocando pescado dentro de una lata a mano",
        "Sello de trazabilidad / lote impreso en el fondo de una lata",
        "Lata de atún premium en un estante reducido, poco stock",
    ],
    "CIERRE": [
        "Checklist gráfico animado con 5 puntos marcándose uno a uno",
        "Mano señalando la etiqueta trasera de una lata de atún",
        "Comparativa final: las siete latas de la lista alineadas en una balda",
        "Icono de compartir / enviar mensaje en un móvil",
        "Persona mostrando el móvil a otra persona en la cocina (compartiendo el vídeo)",
    ],
}


def split_sentences(text):
    text = text.replace("\n\n", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ"¿¡])', text)
    return [p.strip() for p in parts if p.strip()]


def split_words(text, target=10):
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunk = words[i:i + target]
        if len(chunk) < 4 and chunks:
            chunks[-1] = chunks[-1] + " " + " ".join(chunk)
        else:
            chunks.append(" ".join(chunk))
        i += target
    return chunks


def fmt_tc(seconds):
    m = int(seconds // 60)
    s = seconds - m * 60
    return f"{m:02d}:{s:05.2f}"


expanded = []
gcount = 0
motion_i = 0

for section, full_text in SECTIONS:
    visual_cycle = SECTION_VISUALS[section]
    sentences = split_sentences(full_text)
    for s_idx, sentence in enumerate(sentences):
        visual = visual_cycle[s_idx % len(visual_cycle)]
        for sub in split_words(sentence, target=10):
            gcount += 1
            motion = MOTIONS[motion_i % len(MOTIONS)]
            motion_i += 1
            expanded.append((section, gcount, sub, visual, motion))

TOTAL_WORDS = sum(len(t.split()) for _, t in SECTIONS)
SEC_PER_WORD = TARGET_SECONDS / TOTAL_WORDS

timed = []
t = 0.0
for section, beat, text, visual, motion in expanded:
    words = len(text.split())
    dur = round(words * SEC_PER_WORD, 1)
    start = t
    end = t + dur
    t = end
    timed.append((section, beat, text, visual, motion, dur, start, end))

print(f"Total beats: {gcount}")
print(f"Total palabras: {TOTAL_WORDS}")
print(f"Duracion objetivo: {TARGET_SECONDS}s ({TARGET_SECONDS/60:.1f} min) -> {SEC_PER_WORD:.4f} s/palabra")
print(f"Duracion timeline calculada: {fmt_tc(t)}")

base = "/tmp/claude-0/-home-user-Claudeeee/fed35260-2711-5769-ad05-7e136fd68906/scratchpad/"
with open(base + "Atun_Beats.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Sección", "Beat #", "Texto del guión", "Sugerencia visual (pendiente de clip real)",
                "Duración (s)", "Inicio", "Fin", "CapCut Motion"])
    for section, beat, text, visual, motion, dur, start, end in timed:
        w.writerow([section, beat, text, visual, dur, fmt_tc(start), fmt_tc(end), motion])

print("Guardado Atun_Beats.csv")
