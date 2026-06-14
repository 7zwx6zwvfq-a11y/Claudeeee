#!/usr/bin/env python3
"""Image prompts PDF for Video 11 — 3 Traps That Rewire Your Brain to Stay Broke.
One full image prompt per beat (STYLE + scene), formatted for copy-paste into Google Flow."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                KeepTogether)

from build_mental_traps_doc import BEATS, STYLE

SECTION_STARTS = {
    1:   "HOOK",
    18:  "TRAP 1 — THE REWARD TRAP",
    50:  "CTA",
    52:  "TRAP 2 — THE SAFE MONEY ILLUSION",
    81:  "TRAP 3 — THE FUTURE IS FAKE",
    115: "SYSTEM CLOSE",
    129: "IDENTITY CLOSE + GUIDE",
}

TOTAL = len(BEATS)
CHUNK = 36
parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

styles = getSampleStyleSheet()
H1    = ParagraphStyle('H1',    parent=styles['Title'],    fontSize=19, leading=23,
                       alignment=TA_CENTER)
H2    = ParagraphStyle('H2',    parent=styles['Normal'],   fontSize=13, leading=16,
                       alignment=TA_CENTER, fontName='Helvetica-Bold')
SUB   = ParagraphStyle('SUB',   parent=styles['Normal'],   fontSize=11, leading=14,
                       alignment=TA_CENTER, textColor=colors.HexColor('#444444'))
INTRO = ParagraphStyle('INTRO', parent=styles['Normal'],   fontSize=9,  leading=12,
                       alignment=TA_CENTER, textColor=colors.HexColor('#555555'))
PART  = ParagraphStyle('PART',  parent=styles['Heading2'], fontSize=13, leading=16,
                       textColor=colors.HexColor('#B02A2A'), spaceBefore=14, spaceAfter=6)
BEATH = ParagraphStyle('BEATH', parent=styles['Normal'],   fontSize=10.5, leading=14,
                       spaceBefore=8, spaceAfter=2)
IMG   = ParagraphStyle('IMG',   parent=styles['Normal'],   fontSize=9,  leading=13,
                       spaceAfter=2)
DONE  = ParagraphStyle('DONE',  parent=styles['Normal'],   fontSize=10, leading=13,
                       textColor=colors.HexColor('#1E7A33'), fontName='Helvetica-Bold',
                       spaceBefore=6)


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


pdf_path = "/home/user/Claudeeee/Mental_Traps_IMAGE_PROMPTS.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=16*mm,
                        rightMargin=16*mm, topMargin=15*mm, bottomMargin=15*mm)

flow = [
    Paragraph("CRAYON CAPITAL — CLONE SESSION · VIDEO 11", H1),
    Spacer(1, 4),
    Paragraph("STATE 1 — IMAGE PROMPTS", H2),
    Spacer(1, 3),
    Paragraph("3 Traps That Rewire Your Brain to Stay Broke", SUB),
    Spacer(1, 5),
    Paragraph(
        f"Full image prompt (style + scene) for each of the {TOTAL} beats. "
        f"In {len(parts)} parts of {CHUNK} beats max.",
        INTRO),
]

for pidx, (a, b) in enumerate(parts, 1):
    flow.append(Paragraph(
        f"IMAGE PROMPTS — PARTE {pidx} (Beats {a}–{b})", PART))

    for n in range(a, b + 1):
        seg, scene, cam, light, mood, action, video = BEATS[n - 1]
        section_label = SECTION_STARTS.get(n)
        if section_label:
            flow.append(Spacer(1, 4))
            flow.append(Paragraph(
                f'<font color="#B02A2A"><b>── {esc(section_label)} ──</b></font>',
                BEATH))

        full_prompt = f"{STYLE} {scene}"
        block = [
            Paragraph(
                f'<font color="#B02A2A"><b>BEAT {n}</b></font> &nbsp; '
                f'<b><i>"{esc(seg)}"</i></b>', BEATH),
            Paragraph(f'<b>Image Prompt:</b> {esc(full_prompt)}', IMG),
        ]
        flow.append(KeepTogether(block))

    flow.append(Paragraph(
        f"PARTE {pidx} COMPLETA — Beats {a}–{b} ✓", DONE))

doc.build(flow)
print(f"Saved: {pdf_path} | {TOTAL} beats | {len(parts)} parts")
