#!/usr/bin/env python3
"""PDF version of the standalone VIDEO PROMPTS document (Video 2)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                KeepTogether)

from build_dopamine_doc import BEATS

TOTAL = len(BEATS)
CHUNK = 36
parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Title'], fontSize=19, leading=23,
                    alignment=TA_CENTER)
H2 = ParagraphStyle('H2', parent=styles['Normal'], fontSize=13, leading=16,
                    alignment=TA_CENTER, fontName='Helvetica-Bold')
SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=11, leading=14,
                     alignment=TA_CENTER, textColor=colors.HexColor('#444444'))
INTRO = ParagraphStyle('INTRO', parent=styles['Normal'], fontSize=9.5,
                       leading=12, alignment=TA_CENTER,
                       textColor=colors.HexColor('#555555'))
PART = ParagraphStyle('PART', parent=styles['Heading2'], fontSize=13,
                      leading=16, textColor=colors.HexColor('#B02A2A'),
                      spaceBefore=14, spaceAfter=6)
BEATH = ParagraphStyle('BEATH', parent=styles['Normal'], fontSize=10.5,
                       leading=14, spaceBefore=8, spaceAfter=2)
VID = ParagraphStyle('VID', parent=styles['Normal'], fontSize=9.5,
                     leading=13, spaceAfter=2)
DONE = ParagraphStyle('DONE', parent=styles['Normal'], fontSize=10,
                      leading=13, textColor=colors.HexColor('#1E7A33'),
                      fontName='Helvetica-Bold', spaceBefore=6)


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


pdf_path = "/home/user/Claudeeee/Dopamine_Trap_VIDEO_PROMPTS.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=16*mm,
                        rightMargin=16*mm, topMargin=15*mm, bottomMargin=15*mm)
flow = [
    Paragraph("CRAYON CAPITAL — CLONE SESSION · VIDEO 2", H1),
    Spacer(1, 4),
    Paragraph("STATE 9 — VIDEO PROMPTS", H2),
    Spacer(1, 3),
    Paragraph('"Por qué comprar se siente mejor que tener" · The Dopamine Trap',
              SUB),
    Spacer(1, 5),
    Paragraph("Un video prompt para cada uno de los %d beats. "
              "Por volumen, en %d partes." % (TOTAL, len(parts)), INTRO),
]

for pidx, (a, b) in enumerate(parts, 1):
    flow.append(Paragraph("VIDEO PROMPTS — PARTE %d (Beats %d–%d)"
                          % (pidx, a, b), PART))
    for n in range(a, b + 1):
        seg, scene, cam, light, mood, action, video = BEATS[n - 1]
        block = [
            Paragraph('<font color="#B02A2A"><b>BEAT %d</b></font> &nbsp; '
                      '<b><i>"%s"</i></b>' % (n, esc(seg)), BEATH),
            Paragraph('<b>Video Prompt:</b> %s' % esc(video), VID),
        ]
        flow.append(KeepTogether(block))
    flow.append(Paragraph("PARTE %d COMPLETA — Beats %d–%d &#10003;"
                          % (pidx, a, b), DONE))

doc.build(flow)
print("Saved PDF:", pdf_path, "|", TOTAL, "beats |", len(parts), "parts")
