#!/usr/bin/env python3
"""Image prompts PDF for Video 12 (revised) — The One Decision That Defeats All Three Brain Traps.
Full image prompt (STYLE + scene) per beat — ready to copy-paste into Google Flow / Imagen 4."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, KeepTogether)

from build_v12_revised import BEATS

# ── Style preamble — prepend to every image prompt ───────────────────────────
STYLE = (
    "2D flat cartoon illustration, thick solid black outlines, clean solid color fills, "
    "no gradients. ALEX: large beige oval head, transparent glass upper skull revealing "
    "pink cartoon brain villain inside, small black dot eyes, thin neutral mouth, black "
    "spiky hair, blue t-shirt, gray pants. Brain villain: pink cartoon brain character, "
    "heavy-lidded eyes, slight smirk, small teeth. Palette: beige skin (#F5E6C8), pink "
    "brain (#E8A598), blue shirt, gray pants, green for savings/gains, red for "
    "loss/danger, white for diagram scenes. 16:9, 1280x720."
)

# ── Build section start map from BEATS ────────────────────────────────────────
SECTION_STARTS = {}
last_sec = None
for beat in BEATS:
    num, sec = beat[0], beat[1]
    if sec != last_sec:
        SECTION_STARTS[num] = sec
        last_sec = sec

TOTAL = len(BEATS)
CHUNK = 30

parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

styles = getSampleStyleSheet()
H1    = ParagraphStyle('H1',    parent=styles['Title'],    fontSize=17, leading=22, alignment=TA_CENTER)
H2    = ParagraphStyle('H2',    parent=styles['Normal'],   fontSize=12, leading=15,
                       alignment=TA_CENTER, fontName='Helvetica-Bold')
SUB   = ParagraphStyle('SUB',   parent=styles['Normal'],   fontSize=10, leading=13,
                       alignment=TA_CENTER, textColor=colors.HexColor('#444444'))
META  = ParagraphStyle('META',  parent=styles['Normal'],   fontSize=8,  leading=11,
                       alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
STYLE_BOX = ParagraphStyle('STYLE_BOX', parent=styles['Normal'], fontSize=8, leading=11,
                            textColor=colors.HexColor('#555555'), spaceBefore=4, spaceAfter=8)
PART  = ParagraphStyle('PART',  parent=styles['Heading2'], fontSize=12, leading=15,
                       textColor=colors.HexColor('#B02A2A'), spaceBefore=14, spaceAfter=6)
SEC_H = ParagraphStyle('SEC_H', parent=styles['Normal'],   fontSize=9,  leading=12,
                       textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                       spaceBefore=8, spaceAfter=2)
BEATH = ParagraphStyle('BEATH', parent=styles['Normal'],   fontSize=10, leading=14,
                       spaceBefore=6, spaceAfter=2)
IMG   = ParagraphStyle('IMG',   parent=styles['Normal'],   fontSize=8.5, leading=12, spaceAfter=2)
DONE  = ParagraphStyle('DONE',  parent=styles['Normal'],   fontSize=9, leading=12,
                       textColor=colors.HexColor('#1E7A33'), fontName='Helvetica-Bold',
                       spaceBefore=6)


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


pdf_path = "/home/user/Claudeeee/V12_revised_IMAGE_PROMPTS.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)

flow = [
    Paragraph("NEUROCENTS · VIDEO 12", H2),
    Spacer(1, 4),
    Paragraph("IMAGE PROMPTS — VISUAL REFERENCE", H1),
    Spacer(1, 3),
    Paragraph("The One Decision That Defeats All Three Brain Traps", SUB),
    Spacer(1, 4),
    Paragraph(f"{TOTAL} beats · {len(parts)} parts of max {CHUNK} beats · Visual-first (no redundant text labels)", META),
    Spacer(1, 8),
    Paragraph(
        f"<b>STYLE PREAMBLE</b> — prepend to every prompt in Google Flow:<br/>{esc(STYLE)}",
        STYLE_BOX),
]

for pidx, (a, b) in enumerate(parts, 1):
    flow.append(Paragraph(f"IMAGE PROMPTS — PART {pidx}  (Beats {a}–{b})", PART))

    for beat in BEATS[a - 1:b]:
        num, sec, narration, image_prompt = beat[0], beat[1], beat[2], beat[3]

        if num in SECTION_STARTS:
            flow.append(Paragraph(
                f'<font color="#B02A2A"><b>── {esc(SECTION_STARTS[num])} ──</b></font>',
                SEC_H))

        full_prompt = f"{STYLE} {image_prompt}"
        block = [
            Paragraph(
                f'<font color="#B02A2A"><b>BEAT {num}</b></font>  '
                f'<b><i>"{esc(narration)}"</i></b>', BEATH),
            Paragraph(f'<b>Image Prompt:</b> {esc(full_prompt)}', IMG),
        ]
        flow.append(KeepTogether(block))

    flow.append(Paragraph(f"PART {pidx} DONE — Beats {a}–{b} ✓", DONE))
    flow.append(Spacer(1, 6))

doc.build(flow)
print(f"Saved: {pdf_path} | {TOTAL} beats | {len(parts)} parts")
