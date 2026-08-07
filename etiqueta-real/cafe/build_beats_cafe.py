#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build beats (timecoded, ~9-11 word chunks) for the Cafe video (V3).
Libreria de SHOTS con IDs REALES verificados en el catalogo de Freepik
(via stock_search) - no son sugerencias descriptivas genericas.
Para descargar: usar stock_download(id, type) en el momento de editar
(las URLs firmadas caducan en horas, asi que no se guardan aqui)."""
import re
import csv

from cafe_full_script import SECTIONS

TARGET_SECONDS = 24 * 60  # objetivo de duracion de render: ~24 min (4096 palabras a 174ppm ~23.5min)

MOTIONS = [
    "ZOOM IN SLOW · 4s", "PAN RIGHT · 4s", "ZOOM OUT SLOW · 4s",
    "STATIC", "PAN LEFT · 4s", "DIAGONAL PAN + ZOOM IN · 4s",
    "ZOOM IN FAST · 2s", "PAN UP · 4s",
]

# ---------- SHOT LIBRARY (Freepik IDs reales, verificados via stock_search) ----------
# formato: clave -> (titulo, id, tipo)
SHOTS = {
    # -- reutilizados de la libreria real de V1/V2, conceptos genericos --
    "generic_shelf":       ("Fixed clip of full grocery store shelves, filled with brightly coloured products", 6181813, "video"),
    "network_anim":        ("Central avatar appearing and expanding, sending connecting lines and nodes, showing company network", 7618572, "video"),
    "magnifier_doc":       ("Close-Up of a Magnifying Glass on an Aged Document Highlighting Detailed Text and Graphs", 8534240, "video"),
    "cert_stamp":          ("Stamp with CERTIFIED text of flat style isolated on white background", 3982793, "video"),
    "handshake_boardroom": ("Business people handshake in boardroom, corporate partnership deal", 2466239, "video"),
    "vintage_factory":     ("Archival footage, women working in factories, 1915", 98280, "video"),
    "aisle_dolly":         ("A smooth out-of-focus camera movement travels down a brightly lit retail grocery store aisle", 7917819, "video"),
    "spain_flag1":         ("Waving Flag of Spain", 8567147, "video"),
    "reading_label_store": ("Customer in the supermarket during pandemic time, reading the label on the pack of coffee", 1455528, "video"),
    "elegant_table":       ("Minimalist table setting with white plate, fork, and knife arranged neatly", 5070095, "video"),
    "world_map_network":   ("Blue world map with growing white network of connected icons on black background", 1948107, "video"),
    "bar_chart_growth":    ("Animated Bar Chart Showing Progressive Growth of Colorful Data Columns", 9083856, "video"),
    "checklist_anim":      ("Animated Checklist on Clipboard with Stopwatch for Task Completion", 7352827, "video"),
    "share_button_glow":   ("Animated Share Button Glowing on Black Background", 7196718, "video"),
    "finger_share_phone":  ("Finger on Share Button on Mobile Phone", 4838647, "video"),
    "youtube_share_anim":  ("Premium Youtube Share Animation 1", 7055249, "video"),
    "kitchen_scale":       ("Close up of kitchen digital weighing scale displaying zero with metallic container placed on top", 5302538, "video"),
    "warning_icon":        ("Alert sign attention mark caution icon triangle exclamation mark danger warning emergency hazard", 5695539, "video"),
    "cans_aligned_low":    ("A video still of canned goods lined up on a reflective surface, captured from a low angle", 7103683, "video"),
    # -- nuevos, verificados esta sesion para Cafe --
    "instant_coffee_pour_mug": ("Over the shoulder shot of instant coffee being poured into mug", 5851832, "video"),
    "instant_coffee_jar":      ("Instant Coffee in a Jar", 3742829, "video"),
    "coffee_powder_add_cup":   ("Adding Coffee Powder to Cup", 3739958, "video"),
    "coffee_granules_pour_jar":("Pouring coffee granuals into a jar", 1075121, "video"),
    "coffee_beans_roasting":   ("Close up macro shot of roasting coffee beans in a hot oven, thick smoke", 1009750, "video"),
    "coffee_beans_drum_roaster":("Close-up roasted coffee beans moving and mixing in drum roaster in slow motion", 395194, "video"),
    "coffee_beans_falling_pile":("Close camera movement through falling fresh coffee beans into a pile on wooden surface", 1176322, "video"),
    "coffee_beans_conveyor":   ("Roasted Coffee Beans In Package On Conveyor Belt In Factory. Coffee Production", 4993249, "video"),
    "woman_browsing_shelves":  ("A Young Woman Browsing Grocery Shelves in an Aisle Filled with Various Food Products", 6247619, "video"),
    "espresso_pour_crema":     ("Espresso shots being poured into glass with steam", 680663, "video"),
    "coffee_cup_steam":        ("Close-up of a cup of coffee with steam rising from it", 3477731, "video"),
    "sugar_cube_splash":       ("Sugar cube falling in coffee cup and splashing", 3070550, "video"),
    "barista_espresso":        ("Barista skillfully prepares a rich espresso shot using fresh coffee beans in a cozy cafe", 6853142, "video"),
    "coffee_shop_specialty":   ("Young man in cafe studying menu, artisanal coffee signage, shelves of beans", 7874407, "video"),
    "moka_pot_beans":          ("Freshly ground coffee beans in a moka pot, ready for brewing, close-up shot", 5678612, "video"),
    "coffee_capsule_machine":  ("Closeup making coffee from a capsule in an automated Nespresso machine", 764598, "video"),
    "colombia_flag":           ("Colombia flag waving in a clear sky day", 969584, "video"),
    "mexico_flag":             ("Mexico national flag waving on flagpole", 3087468, "video"),
    "coffee_farmer_picking":   ("A Colombian farmer picking coffee beans in coffee plantation farm, Sierra Nevada Colombia", 5693405, "video"),
    "hand_stirring_coffee":    ("Hand stirring coffee with a spoon", 3682294, "video"),
}

# Rotacion de shots por seccion (ciclo por frase, misma logica que V1/V2)
SECTION_SHOTS = {
    "HOOK": ["instant_coffee_pour_mug", "coffee_cup_steam", "network_anim", "magnifier_doc",
             "coffee_powder_add_cup", "sugar_cube_splash", "reading_label_store"],
    "EL MECANISMO - TORREFACTO": ["coffee_beans_roasting", "sugar_cube_splash", "vintage_factory",
                                    "coffee_beans_drum_roaster", "magnifier_doc", "kitchen_scale",
                                    "coffee_beans_falling_pile"],
    "MARCA 7 - BONKA": ["instant_coffee_jar", "generic_shelf", "network_anim", "aisle_dolly",
                          "cert_stamp", "reading_label_store"],
    "MARCA 6 - MARCILLA": ["vintage_factory", "instant_coffee_jar", "handshake_boardroom",
                             "world_map_network", "bar_chart_growth", "spain_flag1"],
    "CTA SUTIL (~35%)": ["share_button_glow", "finger_share_phone", "youtube_share_anim"],
    "MARCA 5 - SAIMAZA": ["instant_coffee_jar", "spain_flag1", "handshake_boardroom",
                            "world_map_network", "aisle_dolly"],
    "MARCA 4 - HACENDADO": ["coffee_beans_conveyor", "generic_shelf", "world_map_network",
                              "cert_stamp", "aisle_dolly", "coffee_beans_roasting"],
    "MARCA 3 - MARCA BLANCA": ["generic_shelf", "aisle_dolly", "sugar_cube_splash",
                                 "coffee_beans_drum_roaster", "magnifier_doc", "woman_browsing_shelves"],
    "MARCA 2 - NESCAFE": ["instant_coffee_pour_mug", "coffee_granules_pour_jar", "vintage_factory",
                            "cert_stamp", "world_map_network", "warning_icon"],
    "MARCA 1 - L'OR": ["coffee_capsule_machine", "espresso_pour_crema", "handshake_boardroom",
                         "bar_chart_growth", "coffee_cup_steam"],
    "MEJORES OPCIONES": ["coffee_farmer_picking", "colombia_flag", "mexico_flag", "coffee_shop_specialty",
                           "barista_espresso", "moka_pot_beans", "cert_stamp"],
    "CIERRE": ["checklist_anim", "reading_label_store", "hand_stirring_coffee",
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
with open(base + "Cafe_Beats.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Sección", "Beat #", "Texto del guión", "Shot (descripción real)", "Freepik ID",
                "Duración (s)", "Inicio", "Fin", "CapCut Motion", "Ref. shot"])
    for section, beat, text, shot_key, motion, dur, start, end in timed:
        title, sid, stype = SHOTS[shot_key]
        w.writerow([section, beat, text, title, sid, dur, fmt_tc(start), fmt_tc(end), motion, shot_key])

print("Guardado Cafe_Beats.csv")

# ---------------- Hoja de shots unicos (para descargar con stock_download) ----------------
with open(base + "Cafe_Shots_unicos.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Ref.", "Titulo del clip", "Freepik ID", "Tipo"])
    for key, (title, sid, stype) in SHOTS.items():
        w.writerow([key, title, sid, stype])
print(f"Guardado Cafe_Shots_unicos.csv ({len(SHOTS)} shots)")
