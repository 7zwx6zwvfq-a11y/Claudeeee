#!/usr/bin/env python3
"""ElevenLabs narration-only PDF — Guion 2 · Your Brain Treats Spending Like a Drug."""

import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

TITLE = "Your Brain Treats Spending Like a Drug (And It Knows Exactly When to Strike)"
SUBTITLE = "NEUROCENTS · GUION 2 (Creator Brief v4)"

SCRIPT_PATH = "/home/user/Claudeeee/GUION2_Dopamine_Anticipation_SCRIPT.txt"
PDF_PATH = "/home/user/Claudeeee/GUION2_ELEVENLABS.pdf"


def extract_lines():
    lines = []
    with open(SCRIPT_PATH) as f:
        for raw in f:
            m = re.match(r"^\[\d+\]\s*(.*)$", raw.strip())
            if m:
                lines.append(m.group(1))
    return lines


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_elevenlabs_pdf():
    lines = extract_lines()
    wc = sum(len(l.split()) for l in lines)

    styles = getSampleStyleSheet()
    H1 = ParagraphStyle("H1", parent=styles["Title"], fontSize=14, leading=18, alignment=TA_CENTER)
    SUB = ParagraphStyle("SUB", parent=styles["Normal"], fontSize=10, leading=13,
                         alignment=TA_CENTER, textColor=colors.HexColor("#B02A2A"),
                         fontName="Helvetica-Bold")
    META = ParagraphStyle("META", parent=styles["Normal"], fontSize=9, leading=12,
                          alignment=TA_CENTER, textColor=colors.HexColor("#777777"))
    LINE = ParagraphStyle("LINE", parent=styles["Normal"], fontSize=12, leading=20, spaceAfter=3)

    doc = SimpleDocTemplate(PDF_PATH, pagesize=A4,
                            leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=18 * mm)
    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph(f"ELEVENLABS — NARRATION ONLY · {len(lines)} lines · ~{wc} words · ~{round(wc / 140)} min", META),
        Spacer(1, 16),
    ]
    for line in lines:
        flow.append(Paragraph(esc(line), LINE))
    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END OF SCRIPT · {len(lines)} lines · ~{wc} words", META))
    doc.build(flow)
    print(f"ELEVENLABS: {PDF_PATH} | {len(lines)} lines | ~{wc} words")


if __name__ == "__main__":
    build_elevenlabs_pdf()
