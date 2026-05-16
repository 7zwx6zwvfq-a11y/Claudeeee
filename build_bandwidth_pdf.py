#!/usr/bin/env python3
"""Render the same beat data to PDF via reportlab."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether)

from build_bandwidth_doc import BEATS, STYLE  # reuse the single source of truth

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Title'], fontSize=20, leading=24,
                    alignment=TA_CENTER)
SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=12, leading=15,
                     alignment=TA_CENTER, textColor=colors.HexColor('#444444'))
META = ParagraphStyle('META', parent=styles['Normal'], fontSize=8.5,
                      leading=11, alignment=TA_CENTER,
                      textColor=colors.HexColor('#666666'))
SEC = ParagraphStyle('SEC', parent=styles['Heading2'], fontSize=12,
                     leading=15, textColor=colors.HexColor('#111111'),
                     spaceBefore=10, spaceAfter=4)
BEAT = ParagraphStyle('BEAT', parent=styles['Normal'], fontSize=12,
                      leading=15, textColor=colors.HexColor('#B02A2A'),
                      spaceBefore=12, spaceAfter=2)
SEG = ParagraphStyle('SEG', parent=styles['Normal'], fontSize=10,
                     leading=13, fontName='Helvetica-BoldOblique',
                     spaceAfter=4)
CELL = ParagraphStyle('CELL', parent=styles['Normal'], fontSize=8.5,
                      leading=11)
LBL = ParagraphStyle('LBL', parent=styles['Normal'], fontSize=8,
                     leading=11, fontName='Helvetica-Bold')
BODY = ParagraphStyle('BODY', parent=styles['Normal'], fontSize=9.5,
                      leading=13)

pdf_path = "/home/user/Claudeeee/Bandwidth_Tax_Production.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=15*mm, rightMargin=15*mm,
                        topMargin=15*mm, bottomMargin=15*mm)
flow = []
flow.append(Paragraph("CRAYON CAPITAL — CLONE SESSION · VIDEO 3", H1))
flow.append(Spacer(1, 4))
flow.append(Paragraph('"The Bandwidth Tax" &nbsp;·&nbsp; '
                      'Financial Scarcity &amp; Cognitive Load', SUB))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Neuroeconomics · English · "
                      "%d beats (3–5s each)" % len(BEATS), META))
flow.append(Spacer(1, 12))
flow.append(Paragraph("VISUAL STYLE PROFILE (locked — embedded in every prompt "
                      "for standalone use)", SEC))
flow.append(Paragraph(STYLE, BODY))
flow.append(Spacer(1, 8))
flow.append(Paragraph("STATES 8 &amp; 9 — IMAGE PROMPTS + VIDEO PROMPTS", SEC))
flow.append(Paragraph("Every script segment covered. Each image prompt is fully "
                      "standalone. Each beat = max 3–5 seconds of narration.", BODY))

avail = doc.width


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


for i, (seg, scene, cam, light, mood, action, video) in enumerate(BEATS, 1):
    block = [Paragraph("BEAT %d" % i, BEAT),
             Paragraph('"%s"' % esc(seg), SEG)]
    rows = [
        [Paragraph("IMAGE PROMPT", LBL),
         Paragraph(esc(STYLE + " " + scene), CELL)],
        [Paragraph("Camera", LBL), Paragraph(esc(cam), CELL)],
        [Paragraph("Lighting", LBL), Paragraph(esc(light), CELL)],
        [Paragraph("Mood", LBL), Paragraph(esc(mood), CELL)],
        [Paragraph("Action", LBL), Paragraph(esc(action), CELL)],
        [Paragraph("VIDEO PROMPT", LBL), Paragraph(esc(video), CELL)],
    ]
    t = Table(rows, colWidths=[26*mm, avail - 26*mm])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#FDECEC')),
        ('BACKGROUND', (0, 5), (0, 5), colors.HexColor('#EAF3FB')),
        ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#FFF6F6')),
        ('BACKGROUND', (1, 5), (1, 5), colors.HexColor('#F4F9FD')),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    block.append(t)
    flow.append(KeepTogether(block))

doc.build(flow)
print("Saved PDF:", pdf_path, "with", len(BEATS), "beats")
