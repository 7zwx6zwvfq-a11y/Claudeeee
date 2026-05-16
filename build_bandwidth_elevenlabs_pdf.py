#!/usr/bin/env python3
"""ElevenLabs narration script PDF for Video 3."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from build_bandwidth_doc import BEATS

styles = getSampleStyleSheet()

H1 = ParagraphStyle('H1', parent=styles['Title'], fontSize=16, leading=20, alignment=TA_CENTER)
SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=10, leading=13,
                     alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                     fontName='Helvetica-Bold')
META = ParagraphStyle('META', parent=styles['Normal'], fontSize=9, leading=12,
                      alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
LINE = ParagraphStyle('LINE', parent=styles['Normal'], fontSize=11, leading=17,
                      spaceAfter=1, leftIndent=0)

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

all_lines = [b[0] for b in BEATS]
word_count = sum(len(l.split()) for l in all_lines)

pdf_path = "/home/user/Claudeeee/Bandwidth_Tax_ELEVENLABS.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=18*mm, bottomMargin=18*mm)

flow = [
    Paragraph("CRAYON CAPITAL — CLONE SESSION · VIDEO 3", SUB),
    Spacer(1, 4),
    Paragraph("Why Poor People Make Bad Decisions (It's Not What You Think)", H1),
    Spacer(1, 4),
    Paragraph(f"ELEVEN LABS — NARRATION SCRIPT · {len(all_lines)} lines · ~{word_count} words", META),
    Spacer(1, 14),
]

for line in all_lines:
    flow.append(Paragraph(esc(line), LINE))

flow.append(Spacer(1, 10))
flow.append(Paragraph(f"END OF SCRIPT · {word_count} words", META))

doc.build(flow)
print(f"Saved: {pdf_path} | {len(all_lines)} lines | {word_count} words")
