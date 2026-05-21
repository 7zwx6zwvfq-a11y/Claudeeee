#!/usr/bin/env python3
"""PDF script document for Video 5: Why Free Money Is the Most Expensive Money You Own."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from build_mental_accounting_script import SECTIONS, TITLE, SUBTITLE, LABEL

styles = getSampleStyleSheet()
H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=18, leading=22, alignment=TA_CENTER)
H2   = ParagraphStyle('H2',   parent=styles['Normal'], fontSize=11, leading=14,
                      alignment=TA_CENTER, fontName='Helvetica-Bold',
                      textColor=colors.HexColor('#B02A2A'))
SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=10, leading=13,
                      alignment=TA_CENTER, textColor=colors.HexColor('#555555'))
SEC  = ParagraphStyle('SEC',  parent=styles['Normal'], fontSize=10, leading=13,
                      fontName='Helvetica-Bold', textColor=colors.HexColor('#B02A2A'),
                      spaceBefore=14, spaceAfter=4)
BEAT = ParagraphStyle('BEAT', parent=styles['Normal'], fontSize=10.5, leading=14, spaceAfter=2)
FOOT = ParagraphStyle('FOOT', parent=styles['Normal'], fontSize=8.5, leading=11,
                      alignment=TA_CENTER, textColor=colors.HexColor('#888888'))

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

pdf_path = "/home/user/Claudeeee/Mental_Accounting_SCRIPT.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=18*mm, rightMargin=18*mm,
                        topMargin=15*mm, bottomMargin=15*mm)
flow = [
    Paragraph(esc(SUBTITLE), H2),
    Spacer(1, 3),
    Paragraph(esc(LABEL), SUB),
    Spacer(1, 5),
    Paragraph(esc(TITLE), H1),
    Spacer(1, 12),
]

beat_num = 1
all_words = 0
for section_title, lines in SECTIONS:
    if section_title:
        flow.append(Paragraph(f"— {esc(section_title)} —", SEC))
    for line in lines:
        flow.append(Paragraph(
            f'<font color="#999999"><b>[{beat_num}]</b></font>  {esc(line)}', BEAT))
        beat_num += 1
        all_words += len(line.split())
    flow.append(Spacer(1, 6))

total_beats = beat_num - 1
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    f"TOTAL: {total_beats} beats · ~{all_words} words · ~{round(all_words/140)} min", FOOT))

doc.build(flow)
print(f"Saved: {pdf_path} | {total_beats} beats | {all_words} words")
