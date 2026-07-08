#!/usr/bin/env python3
"""
Google Flow Automation — genera imágenes automáticamente usando tu sesión de Google Flow.

Abre Playwright con tu perfil de Chrome/Chromium existente (ya logueado en Google),
navega a tu proyecto de Google Flow, mete cada prompt, espera la generación
y descarga todas las imágenes.

REQUISITOS (instalar una sola vez en tu máquina):
    pip install playwright
    playwright install chromium

USO:
    # Genera las 101 imágenes del Video 8 (Treadmill)
    python google_flow_automation.py

    # Solo un beat específico (para probar)
    python google_flow_automation.py --beat 1

    # Otro video
    python google_flow_automation.py --video anchor

    # Con tu propio directorio de perfil de Chrome
    python google_flow_automation.py --profile "/Users/tuusuario/Library/Application Support/Google/Chrome"
"""

import argparse
import importlib.util
import os
import sys
import time

# ── URL de tu proyecto Google Flow ────────────────────────────────────────────
FLOW_PROJECT_URL = "https://labs.google/fx/es/tools/flow/project/eaaa0d5b-2b72-4639-9d94-86a00e70fc2f"

# ── Videos disponibles ────────────────────────────────────────────────────────
VIDEOS = [
    ("build_dopamine_doc.py",          "V01_Dopamine_Trap"),
    ("build_bandwidth_doc.py",         "V02_Bandwidth_Tax"),
    ("build_iowa_doc.py",              "V03_Iowa_Gambling"),
    ("build_mental_accounting_doc.py", "V04_Mental_Accounting"),
    ("build_peak_doc.py",              "V05_Peak"),
    ("build_status_quo_doc.py",        "V06_Status_Quo"),
    ("build_treadmill_doc.py",         "V08_Getting_Rich_Is_Making_You_Poorer"),
    ("build_anchor_doc.py",            "V09_Anchor"),
]

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "images")

# Tiempo máximo esperando que aparezca la imagen generada (segundos)
GENERATION_TIMEOUT = 120


# ── Carga de prompts ──────────────────────────────────────────────────────────

def _load_beats(module_path: str) -> list[tuple]:
    spec = importlib.util.spec_from_file_location("_prod_doc", module_path)
    mod  = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:
        print(f"  WARNING: {module_path}: {exc}")
        return []
    return getattr(mod, "BEATS", [])


def collect(video_filter: str | None = None, beat_filter: int | None = None) -> list[dict]:
    entries = []
    for module_file, label in VIDEOS:
        module_name = module_file.lower()
        if video_filter and video_filter.lower() not in label.lower() and video_filter.lower() not in module_name:
            continue

        full_path = os.path.join(BASE_DIR, module_file)
        if not os.path.exists(full_path):
            continue

        beats  = _load_beats(full_path)
        folder = os.path.join(OUTPUT_DIR, label)

        for i, beat in enumerate(beats, start=1):
            if beat_filter and i != beat_filter:
                continue
            entries.append({
                "label":     label,
                "beat_num":  i,
                "folder":    folder,
                "path":      os.path.join(folder, f"beat_{i:03d}.png"),
                "prompt":    beat[1],
                "narration": beat[0][:80],
            })
    return entries


# ── Automatización Playwright ─────────────────────────────────────────────────

def run_automation(entries: list[dict], force: bool, user_data_dir: str | None) -> None:
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
    except ImportError:
        print(
            "Playwright no está instalado.\n"
            "Instala con:\n"
            "    pip install playwright\n"
            "    playwright install chromium"
        )
        sys.exit(1)

    total   = len(entries)
    done    = 0
    skipped = 0
    errors  = 0

    # Directorio de perfil por defecto según sistema operativo
    if not user_data_dir:
        if sys.platform == "darwin":
            user_data_dir = os.path.expanduser(
                "~/Library/Application Support/Google/Chrome"
            )
        elif sys.platform == "win32":
            user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
        else:
            user_data_dir = os.path.expanduser("~/.config/google-chrome")

    print(f"\nUsando perfil de Chrome: {user_data_dir}")
    print(f"Generando {total} imágenes en Google Flow …\n")

    with sync_playwright() as p:
        # Lanza Chromium con el perfil de Chrome real (ya logueado en Google)
        context = p.chromium.launch_persistent_context(
            user_data_dir,
            channel="chrome",          # usa Chrome instalado
            headless=False,            # visible para que puedas ver el progreso
            args=["--start-maximized"],
            no_viewport=True,
        )
        page = context.new_page()

        print(f"Abriendo Google Flow …")
        page.goto(FLOW_PROJECT_URL, wait_until="networkidle", timeout=30_000)
        time.sleep(3)

        for idx, e in enumerate(entries, start=1):
            out = e["path"]

            if os.path.exists(out) and not force:
                print(f"[{idx}/{total}] SKIP  {e['label']}/beat_{e['beat_num']:03d}.png")
                skipped += 1
                continue

            print(f"[{idx}/{total}] beat_{e['beat_num']:03d} — {e['narration'][:60]}")
            os.makedirs(e["folder"], exist_ok=True)

            try:
                # 1. Localiza el campo de texto de Google Flow
                textarea = page.locator(
                    "textarea, [contenteditable='true'], [placeholder*='crear'], [placeholder*='create'], [aria-label*='prompt']"
                ).first
                textarea.wait_for(state="visible", timeout=15_000)
                textarea.click()
                textarea.fill("")
                textarea.type(e["prompt"], delay=5)

                # 2. Pulsa el botón de generar (→)
                submit = page.locator(
                    "button[aria-label*='generar'], button[aria-label*='Generate'], button[aria-label*='enviar'], button[aria-label*='Send'], button:has(svg)"
                ).last
                submit.click()

                # 3. Espera a que aparezca al menos una imagen generada
                img_selector = "img[src*='blob:'], img[src*='data:'], [data-testid*='image'] img, .generated-image img, figure img"
                page.wait_for_selector(img_selector, timeout=GENERATION_TIMEOUT * 1000)
                time.sleep(2)  # deja que carguen todas las variantes

                # 4. Descarga la primera imagen generada
                images = page.locator(img_selector).all()
                if not images:
                    raise Exception("No se encontraron imágenes generadas")

                # Guarda la primera variante (puedes cambiar el índice para elegir otra)
                first_img = images[0]
                src = first_img.get_attribute("src")

                if src and src.startswith("data:"):
                    # imagen inline base64
                    import base64
                    data = src.split(",", 1)[1]
                    with open(out, "wb") as f:
                        f.write(base64.b64decode(data))
                elif src:
                    # imagen URL — descarga mediante fetch en el contexto de la página
                    img_bytes = page.evaluate(f"""
                        async () => {{
                            const r = await fetch('{src}');
                            const buf = await r.arrayBuffer();
                            return Array.from(new Uint8Array(buf));
                        }}
                    """)
                    with open(out, "wb") as f:
                        f.write(bytes(img_bytes))
                else:
                    # Screenshot del elemento como fallback
                    first_img.screenshot(path=out)

                print(f"  → guardada ({os.path.getsize(out) // 1024} KB)")
                done += 1

            except PWTimeout:
                print(f"  TIMEOUT — la imagen tardó más de {GENERATION_TIMEOUT}s")
                errors += 1
            except Exception as exc:
                print(f"  ERROR: {exc}")
                errors += 1

            # Pequeña pausa entre peticiones para no saturar
            time.sleep(2)

        context.close()

    print(f"\n{'─'*50}")
    print(f"Generadas: {done}  |  Saltadas: {skipped}  |  Errores: {errors}")
    if done:
        print(f"Imágenes en: {OUTPUT_DIR}/")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Automatiza Google Flow para generar imágenes de producción."
    )
    parser.add_argument("--video",   default="treadmill", help="Filtrar por video (default: treadmill = V08)")
    parser.add_argument("--beat",    type=int, default=None, help="Solo este beat (para probar)")
    parser.add_argument("--force",   action="store_true", help="Re-generar imágenes ya guardadas")
    parser.add_argument("--profile", default=None, help="Ruta al perfil de Chrome (si no es el por defecto)")
    parser.add_argument("--all",     action="store_true", help="Todos los videos, no solo treadmill")
    args = parser.parse_args()

    video_filter = None if args.all else args.video
    entries = collect(video_filter=video_filter, beat_filter=args.beat)

    if not entries:
        print("No se encontraron beats. Revisa --video.")
        sys.exit(0)

    print(f"{'─'*50}")
    print(f"Google Flow Automation")
    print(f"Video:  {video_filter or 'TODOS'}")
    print(f"Beats:  {len(entries)}")
    print(f"Salida: {OUTPUT_DIR}/")
    print(f"{'─'*50}")

    run_automation(entries, force=args.force, user_data_dir=args.profile)


if __name__ == "__main__":
    main()
