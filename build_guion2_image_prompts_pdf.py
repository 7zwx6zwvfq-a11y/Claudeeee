#!/usr/bin/env python3
"""IMAGE_PROMPTS PDF — Guion 2 · Your Brain Treats Spending Like a Drug.

Built from the 133 already-generated Magnific creations (identifiers pulled
from GUION2_timeline.json, prompts pulled from each creation's metadata).
"""

import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

TITLE = "Your Brain Treats Spending Like a Drug (And It Knows Exactly When to Strike)"
SUBTITLE = "NEUROCENTS · GUION 2 — IMAGE PROMPTS (Magnific, doodle style)"

TIMELINE_PATH = "/home/user/Claudeeee/GUION2_timeline.json"
PROMPTS_PATH = "/tmp/claude-0/-home-user-Claudeeee/32f7a540-a0e2-5744-acea-4f95e4f52f35/scratchpad/guion2_prompts_all.json"
PDF_PATH = "/home/user/Claudeeee/GUION2_IMAGE_PROMPTS.pdf"

STYLE_PREAMBLE = (
    "2D flat doodle illustration, thick uneven black marker/pen outlines, "
    "hand-drawn crude simple style, minimal flat colors only, plain solid "
    "white background (black scenes only for the opening night beats), no "
    "gradients, no shading, no photorealism, 16:9, extremely high contrast, "
    "legible at small size. Character Alex: round circle head, two small "
    "black dot eyes, thin flat mouth, small blue rectangle t-shirt patch, "
    "tiny transparent oval patch on top of his head showing a tiny pink "
    "blob “brain villain” with a smirk inside."
)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_pdf():
    with open(TIMELINE_PATH) as f:
        timeline = json.load(f)
    with open(PROMPTS_PATH) as f:
        prompts = json.load(f)

    styles = getSampleStyleSheet()
    H1 = ParagraphStyle("H1", parent=styles["Title"], fontSize=14, leading=18, alignment=TA_CENTER)
    SUB = ParagraphStyle("SUB", parent=styles["Normal"], fontSize=10, leading=13,
                         alignment=TA_CENTER, textColor=colors.HexColor("#B02A2A"),
                         fontName="Helvetica-Bold")
    META = ParagraphStyle("META", parent=styles["Normal"], fontSize=9, leading=12,
                          alignment=TA_CENTER, textColor=colors.HexColor("#777777"))
    PREAMBLE = ParagraphStyle("PREAMBLE", parent=styles["Normal"], fontSize=8.5, leading=11,
                              textColor=colors.HexColor("#555555"), spaceAfter=4)
    BEAT_HEAD = ParagraphStyle("BEAT_HEAD", parent=styles["Normal"], fontSize=10.5, leading=13,
                               fontName="Helvetica-Bold", textColor=colors.HexColor("#1a1a1a"),
                               spaceBefore=10, spaceAfter=2)
    NARR = ParagraphStyle("NARR", parent=styles["Normal"], fontSize=9.5, leading=13,
                          fontName="Helvetica-Oblique", textColor=colors.HexColor("#333333"),
                          spaceAfter=3)
    PROMPT = ParagraphStyle("PROMPT", parent=styles["Normal"], fontSize=9, leading=12,
                            textColor=colors.HexColor("#111111"), spaceAfter=2)
    FNAME = ParagraphStyle("FNAME", parent=styles["Normal"], fontSize=8, leading=10,
                           textColor=colors.HexColor("#999999"), spaceAfter=6)

    doc = SimpleDocTemplate(PDF_PATH, pagesize=A4,
                            leftMargin=18 * mm, rightMargin=18 * mm,
                            topMargin=16 * mm, bottomMargin=16 * mm)

    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"133 BEATS · full generated prompts, one per beat, in filename order", META),
        Spacer(1, 10),
        Paragraph("STYLE PREAMBLE (implicit across all prompts below):", BEAT_HEAD),
        Paragraph(esc(STYLE_PREAMBLE), PREAMBLE),
        Spacer(1, 6),
    ]

    parts = [timeline[0:34], timeline[34:67], timeline[67:100], timeline[100:133]]
    for part_num, part in enumerate(parts, 1):
        if part_num > 1:
            flow.append(PageBreak())
        flow.append(Paragraph(f"PART {part_num} of 4 — Beats {part[0]['beat']}–{part[-1]['beat']}", BEAT_HEAD))
        flow.append(Spacer(1, 4))
        for item in part:
            beat = item["beat"]
            ident = item["identifier"]
            prompt_text = prompts.get(ident, "[prompt not found]")
            flow.append(Paragraph(f"BEAT {beat} — {item['timestamp']}", BEAT_HEAD))
            flow.append(Paragraph(esc(item["text"]), NARR))
            flow.append(Paragraph(esc(prompt_text), PROMPT))
            flow.append(Paragraph(f"file: {item['filename']}", FNAME))

    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END OF IMAGE PROMPTS · 133 beats", META))
    doc.build(flow)
    print(f"IMAGE_PROMPTS: {PDF_PATH} | {len(timeline)} beats")


if __name__ == "__main__":
    build_pdf()
