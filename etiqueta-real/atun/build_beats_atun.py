#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build beats (timecoded, ~9-11 word chunks) for the Atun video.
Librería de SHOTS con IDs REALES verificados en el catálogo de Freepik
(vía stock_search) — ya no son sugerencias descriptivas genéricas.
Para descargar: usar stock_download(id, type) en el momento de editar
(las URLs firmadas caducan en horas, así que no se guardan aquí)."""
import re
import csv

from atun_full_script import SECTIONS

TARGET_SECONDS = 26 * 60  # objetivo de duración de render: 26:00

MOTIONS = [
    "ZOOM IN SLOW · 4s", "PAN RIGHT · 4s", "ZOOM OUT SLOW · 4s",
    "STATIC", "PAN LEFT · 4s", "DIAGONAL PAN + ZOOM IN · 4s",
    "ZOOM IN FAST · 2s", "PAN UP · 4s",
]

# ---------- SHOT LIBRARY (Freepik IDs reales, verificados via stock_search) ----------
# formato: clave -> (titulo, id, tipo)
SHOTS = {
    # -- reutilizados de la libreria real de V1 (Aceite), conceptos genericos --
    "generic_shelf":      ("Fixed clip of full grocery store shelves, filled with brightly coloured products", 6181813, "video"),
    "network_anim":       ("Central avatar appearing and expanding, sending connecting lines and nodes, showing company network", 7618572, "video"),
    "magnifier_doc":      ("Close-Up of a Magnifying Glass on an Aged Document Highlighting Detailed Text and Graphs", 8534240, "video"),
    "cert_stamp":         ("Stamp with CERTIFIED text of flat style isolated on white background", 3982793, "video"),
    "handshake_boardroom": ("Business people handshake in boardroom, corporate partnership deal", 2466239, "video"),
    "vintage_factory":    ("Archival footage, women working in factories, 1915", 98280, "video"),
    "aisle_dolly":        ("A smooth out-of-focus camera movement travels down a brightly lit retail grocery store aisle", 7917819, "video"),
    "spain_flag1":        ("Waving Flag of Spain", 8567147, "video"),
    "two_bottles_compare": ("Two bottles of olive oil and extra virgin olive", 2310359, "video"),
    "modern_oil_factory": ("Interior of modern natural oil factory", 6067479, "video"),
    # -- nuevos, verificados esta sesion para Atun --
    "hand_cart_cans":     ("Hand of elegant shopper reaches into metal grocery cart to lift two tins of canned food by precise fingertips", 5954197, "video"),
    "hand_holding_tuna":  ("Women holding a canned tuna", 2476908, "video"),
    "network_converge":   ("Animation of network of connections and data processing over dark background", 4721014, "video"),
    "cans_aligned_low":   ("A video still of canned goods lined up on a reflective surface, captured from a low angle", 7103683, "video"),
    "opening_tuna_dramatic": ("A close-up sequence shows hands opening a pull-tab can of tuna chunks in mineral water", 6168409, "video"),
    "reading_glass_files": ("Animation of reading glass and text over files", 2082900, "video"),
    "cans_colorful_shelf": ("A Colorful Array of Canned Goods on Grocery Store Shelves", 6843740, "video"),
    "opening_tuna_can":   ("Opening a can of tuna", 5044250, "video"),
    "canned_tuna_plain":  ("Canned Tuna", 3420831, "video"),
    "cannery_conveyor":   ("Closeup of cans moving on a conveyor belt in a food production line", 3455151, "video"),
    "rocky_island_aerial": ("Stunning aerial view of rocky island surrounded by ocean waves", 6758697, "video"),
    "canned_tuna_wood":   ("Canned tuna on wooden table", 2427530, "video"),
    "world_map_lines":    ("Lines showing countries connecting on world map", 3071564, "video"),
    "fishing_boat_galicia": ("Fishing Boat Cruising In The Blue Sea In To Muxia In Spain", 2979449, "video"),
    "factory_workers_pink": ("Factory Workers in Pink Uniforms Packaging Products on an Automated Assembly Line", 8083967, "video"),
    "chile_flag":         ("Chile national flag waving on flagpole", 3091163, "video"),
    "warning_icon":       ("Alert sign attention mark caution icon triangle exclamation mark danger warning emergency hazard", 5695539, "video"),
    "two_cans_compare":   ("Two Cans of Food on a Blue Wooden Tabletop", 3680436, "video"),
    "share_button_glow":  ("Animated Share Button Glowing on Black Background", 7196718, "video"),
    "finger_share_phone": ("Finger on Share Button on Mobile Phone", 4838647, "video"),
    "youtube_share_anim": ("Premium Youtube Share Animation 1", 7055249, "video"),
    "sunflower_oil":      ("Sunflower oil bottle. Cooking oil in glass bottle. Cooking ingredients", 1474089, "video"),
    "kitchen_scale":      ("Close up of kitchen digital weighing scale displaying zero with metallic container placed on top", 5302538, "video"),
    "salt_pouring":       ("Closeup of a Hand Pouring Salt From a Shaker", 3479267, "video"),
    "reading_label_store": ("Person Reading Product Label in Grocery Store", 4972749, "video"),
    "elegant_table":      ("Minimalist table setting with white plate, fork, and knife arranged neatly", 5070095, "video"),
    "deli_shopping":      ("Woman Shopping at an Italian Delicatessen", 4874053, "video"),
    "canning_machine":    ("Industrial canning machine tops and seals cans, four aluminum beverage cans move down production line, HD", 722777, "video"),
    "world_map_network":  ("Blue world map with growing white network of connected icons on black background", 1948107, "video"),
    "brazil_flag":        ("Brazil Flag Waving Cloth Textured", 8588916, "video"),
    "bar_chart_growth":   ("Animated Bar Chart Showing Progressive Growth of Colorful Data Columns", 9083856, "video"),
    "fish_fillet_worker": ("Worker slices fish fillet lengthwise with fish tail resting on cutting board", 8939865, "video"),
    "hands_sorting_fish": ("Hands Sorting Fresh Fish and Adding Ice at a Market", 7803085, "video"),
    "checklist_anim":     ("Animated Checklist on Clipboard with Stopwatch for Task Completion", 7352827, "video"),
    "hand_spoon_tuna":    ("Hands open a can of tuna with a spoon", 3420163, "video"),
}

# Rotacion de shots por seccion (ciclo por frase, misma logica que V1)
SECTION_SHOTS = {
    "HOOK": ["hand_cart_cans", "hand_holding_tuna", "network_converge", "cans_aligned_low",
             "opening_tuna_dramatic", "reading_glass_files", "cans_colorful_shelf",
             "magnifier_doc", "opening_tuna_can"],
    "MARCA 7 - HACENDADO": ["aisle_dolly", "generic_shelf", "canned_tuna_plain", "cannery_conveyor",
                             "network_anim", "reading_glass_files", "cert_stamp", "world_map_lines"],
    "MARCA 6 - ROBINSON CRUSOE": ["rocky_island_aerial", "canned_tuna_wood", "world_map_lines",
                                    "fishing_boat_galicia", "factory_workers_pink", "chile_flag",
                                    "spain_flag1", "network_converge"],
    "MARCA 5 - ISABEL": ["world_map_network", "cans_colorful_shelf", "network_converge",
                          "magnifier_doc", "reading_glass_files", "warning_icon",
                          "two_cans_compare", "cans_colorful_shelf"],
    "CTA SUTIL (~35%)": ["share_button_glow", "finger_share_phone", "youtube_share_anim"],
    "MARCA 4 - CARREFOUR": ["aisle_dolly", "generic_shelf", "sunflower_oil", "reading_glass_files",
                              "kitchen_scale", "salt_pouring", "kitchen_scale", "reading_label_store"],
    "MARCA 3 - ORTIZ": ["modern_oil_factory", "canned_tuna_wood", "reading_glass_files",
                          "salt_pouring", "elegant_table", "deli_shopping"],
    "MARCA 2 - NOSTROMO": ["canned_tuna_wood", "world_map_lines", "network_converge",
                             "cans_colorful_shelf", "cannery_conveyor"],
    "MARCA 1 - CALVO": ["vintage_factory", "canning_machine", "fishing_boat_galicia",
                          "world_map_network", "brazil_flag", "bar_chart_growth",
                          "handshake_boardroom", "network_converge", "canned_tuna_plain"],
    "MEJOR OPCION 3 - FRINSA": ["fishing_boat_galicia", "hands_sorting_fish", "world_map_lines",
                                  "fish_fillet_worker"],
    "MEJOR OPCION 2 - PALACIO DE ORIENTE": ["vintage_factory", "vintage_factory",
                                              "hands_sorting_fish", "canned_tuna_wood"],
    "MEJOR OPCION 1 - CONSORCIO": ["hands_sorting_fish", "hand_spoon_tuna", "cert_stamp",
                                     "cans_colorful_shelf"],
    "CIERRE": ["checklist_anim", "reading_label_store", "cans_aligned_low",
                "finger_share_phone", "youtube_share_anim"],
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
    shot_cycle = SECTION_SHOTS[section]
    sentences = split_sentences(full_text)
    for s_idx, sentence in enumerate(sentences):
        shot_key = shot_cycle[s_idx % len(shot_cycle)]
        for sub in split_words(sentence, target=10):
            gcount += 1
            motion = MOTIONS[motion_i % len(MOTIONS)]
            motion_i += 1
            expanded.append((section, gcount, sub, shot_key, motion))

TOTAL_WORDS = sum(len(t.split()) for _, t in SECTIONS)
SEC_PER_WORD = TARGET_SECONDS / TOTAL_WORDS

timed = []
t = 0.0
for section, beat, text, shot_key, motion in expanded:
    words = len(text.split())
    dur = round(words * SEC_PER_WORD, 1)
    start = t
    end = t + dur
    t = end
    timed.append((section, beat, text, shot_key, motion, dur, start, end))

print(f"Total beats: {gcount}")
print(f"Total palabras: {TOTAL_WORDS}")
print(f"Duracion objetivo: {TARGET_SECONDS}s ({TARGET_SECONDS/60:.1f} min) -> {SEC_PER_WORD:.4f} s/palabra")
print(f"Duracion timeline calculada: {fmt_tc(t)}")
print(f"Shots unicos reales usados: {len(SHOTS)}")

base = "/tmp/claude-0/-home-user-Claudeeee/fed35260-2711-5769-ad05-7e136fd68906/scratchpad/"
with open(base + "Atun_Beats.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Sección", "Beat #", "Texto del guión", "Shot (descripción real)", "Freepik ID",
                "Duración (s)", "Inicio", "Fin", "CapCut Motion", "Ref. shot"])
    for section, beat, text, shot_key, motion, dur, start, end in timed:
        title, sid, stype = SHOTS[shot_key]
        w.writerow([section, beat, text, title, sid, dur, fmt_tc(start), fmt_tc(end), motion, shot_key])

print("Guardado Atun_Beats.csv")

# ---------------- Hoja de shots unicos (para descargar con stock_download) ----------------
with open(base + "Atun_Shots_unicos.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Ref.", "Titulo del clip", "Freepik ID", "Tipo"])
    for key, (title, sid, stype) in SHOTS.items():
        w.writerow([key, title, sid, stype])
print(f"Guardado Atun_Shots_unicos.csv ({len(SHOTS)} shots)")
