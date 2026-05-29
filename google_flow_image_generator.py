#!/usr/bin/env python3
"""
Google Flow Image Generator — auto-generates all production images via Gemini Imagen.

Reads BEATS from every build_*_doc.py, extracts the image prompt (index [1]),
and calls the Imagen API to produce a 16:9 PNG for each beat.

Output layout:
    images/
    ├── V01_Dopamine_Trap/
    │   ├── beat_001.png
    │   ├── beat_002.png
    │   └── …
    ├── V02_Bandwidth_Tax/
    │   └── …
    └── …

Usage:
    export GEMINI_API_KEY="your-key-here"

    python google_flow_image_generator.py              # dry-run (list prompts)
    python google_flow_image_generator.py --generate   # generate all videos
    python google_flow_image_generator.py --generate --video anchor
    python google_flow_image_generator.py --generate --video anchor --beat 3
    python google_flow_image_generator.py --generate --force  # re-generate existing
"""

import argparse
import importlib.util
import os
import sys
import time

# ── Video registry ────────────────────────────────────────────────────────────
# (module_file, output_folder_label)
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

# Imagen model — same engine that powers Google Flow
IMAGEN_MODEL = "imagen-3.0-generate-002"
ASPECT_RATIO = "16:9"

# Rate-limit guard: max requests per minute (free tier = 10, paid = 50+)
REQUESTS_PER_MINUTE = 10
SLEEP_BETWEEN = 60 / REQUESTS_PER_MINUTE  # seconds


# ── Helpers ───────────────────────────────────────────────────────────────────

def _load_beats(module_path: str) -> list[tuple]:
    """Import a build_*_doc.py and return its BEATS list."""
    spec = importlib.util.spec_from_file_location("_prod_doc", module_path)
    mod  = importlib.util.module_from_spec(spec)
    # Suppress the docx side-effects (they only run under __main__)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:
        print(f"  WARNING: could not load {module_path}: {exc}")
        return []
    return getattr(mod, "BEATS", [])


def _prompt(beat: tuple) -> str:
    """Index [1] of each BEAT tuple is the full image prompt."""
    return beat[1]


def _narration_slug(beat: tuple, max_len: int = 40) -> str:
    text = beat[0].replace("/", "-").replace("\\", "-")
    slug = "".join(c if c.isalnum() or c in " -_" else "" for c in text)
    return slug[:max_len].strip().replace(" ", "_").lower()


def collect(video_filter: str | None = None) -> list[dict]:
    """Return a flat list of {video, label, beat_num, path, prompt} dicts."""
    entries = []
    for module_file, label in VIDEOS:
        short = label.lower().replace("v0", "").replace("_", "").lstrip("0123456789").lstrip("_")
        module_name = module_file.lower()
        if video_filter and video_filter.lower() not in label.lower() and video_filter.lower() not in module_name:
            continue

        full_path = os.path.join(BASE_DIR, module_file)
        if not os.path.exists(full_path):
            print(f"  MISSING: {module_file}")
            continue

        beats = _load_beats(full_path)
        folder = os.path.join(OUTPUT_DIR, label)

        for i, beat in enumerate(beats, start=1):
            fname = f"beat_{i:03d}.png"
            entries.append({
                "label":    label,
                "beat_num": i,
                "folder":   folder,
                "path":     os.path.join(folder, fname),
                "prompt":   _prompt(beat),
                "narration": beat[0][:80],
            })

    return entries


# ── Generation ────────────────────────────────────────────────────────────────

def _build_client():
    """Build a Gemini client from GEMINI_API_KEY env var."""
    try:
        from google import genai
    except ImportError:
        print(
            "Missing google-genai library.\n"
            "Install with:  pip install google-genai"
        )
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(
            "GEMINI_API_KEY environment variable not set.\n"
            "Get a key at: https://aistudio.google.com/app/apikey\n"
            "Then run:  export GEMINI_API_KEY='your-key'"
        )
        sys.exit(1)

    from google import genai
    return genai.Client(api_key=api_key)


def generate_image(client, prompt: str, output_path: str) -> bool:
    """Call Imagen API and write PNG to output_path. Returns True on success."""
    from google.genai import types

    try:
        response = client.models.generate_images(
            model=IMAGEN_MODEL,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=ASPECT_RATIO,
                safety_filter_level="BLOCK_ONLY_HIGH",
            ),
        )
    except Exception as exc:
        print(f"    ERROR: {exc}")
        return False

    images = response.generated_images
    if not images:
        print("    WARN: no image returned (prompt may have been filtered)")
        return False

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as fh:
        fh.write(images[0].image.image_bytes)
    return True


# ── CLI modes ─────────────────────────────────────────────────────────────────

def dry_run(entries: list[dict], beat_filter: int | None) -> None:
    print(f"\nDRY RUN — {len(entries)} image prompts found\n")
    current_label = None
    for e in entries:
        if beat_filter and e["beat_num"] != beat_filter:
            continue
        if e["label"] != current_label:
            current_label = e["label"]
            print(f"\n  {current_label}/")
        print(f"    beat_{e['beat_num']:03d}.png")
        print(f"      {e['narration'][:70]}")
    print(f"\nRun with --generate to start producing images.")


def run_generation(entries: list[dict], beat_filter: int | None, force: bool) -> None:
    client = _build_client()

    to_do = [e for e in entries if beat_filter is None or e["beat_num"] == beat_filter]
    total  = len(to_do)
    done   = 0
    skipped = 0
    errors  = 0

    print(f"\nGenerating {total} images using {IMAGEN_MODEL} …\n")

    for idx, e in enumerate(to_do, start=1):
        out = e["path"]

        if os.path.exists(out) and not force:
            print(f"[{idx}/{total}] SKIP  {e['label']}/beat_{e['beat_num']:03d}.png")
            skipped += 1
            continue

        print(f"[{idx}/{total}] {e['label']}/beat_{e['beat_num']:03d}.png")
        print(f"  {e['narration'][:70]}")

        os.makedirs(e["folder"], exist_ok=True)
        ok = generate_image(client, e["prompt"], out)

        if ok:
            print(f"  → saved")
            done += 1
        else:
            errors += 1

        # Respect rate limit (skip sleep on last item)
        if idx < total:
            time.sleep(SLEEP_BETWEEN)

    print(f"\n{'─'*50}")
    print(f"Generated: {done}  |  Skipped: {skipped}  |  Errors: {errors}")
    if done:
        print(f"Images saved in: {OUTPUT_DIR}/")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate production images via Google Imagen.")
    parser.add_argument("--generate", action="store_true", help="Call the API (default: dry-run)")
    parser.add_argument("--video",  default=None, help="Filter by video name, e.g. 'anchor'")
    parser.add_argument("--beat",   type=int, default=None, help="Generate only this beat number")
    parser.add_argument("--force",  action="store_true", help="Re-generate already-saved images")
    args = parser.parse_args()

    entries = collect(video_filter=args.video)

    if not entries:
        print("No matching beats found. Check --video spelling.")
        sys.exit(0)

    if args.generate:
        run_generation(entries, beat_filter=args.beat, force=args.force)
    else:
        dry_run(entries, beat_filter=args.beat)


if __name__ == "__main__":
    main()
