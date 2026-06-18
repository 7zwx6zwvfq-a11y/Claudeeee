#!/usr/bin/env python3
"""Script PDF for Video 12 (revised) — The One Decision That Defeats All Three Brain Traps."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from build_v12_revised_script import SECTIONS, TITLE, SUBTITLE, LABEL

styles = getSampleStyleSheet()
H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=16, leading=20, alignment=TA_CENTER)
SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=10, leading=13,
                      alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                      fontName='Helvetica-Bold')
META = ParagraphStyle('META', parent=styles['Normal'], fontSize=9,  leading=12,
                      alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
SEC  = ParagraphStyle('SEC',  parent=styles['Normal'], fontSize=10, leading=13,
                      textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                      spaceBefore=14, spaceAfter=4)
LINE = ParagraphStyle('LINE', parent=styles['Normal'], fontSize=11, leading=17, spaceAfter=1)


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


all_lines = [line for _, lines in SECTIONS for line in lines]
word_count = sum(len(l.split()) for l in all_lines)
total_beats = len(all_lines)

pdf_path = "/home/user/Claudeeee/V12_revised_SCRIPT.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=18*mm, bottomMargin=18*mm)

flow = [
    Paragraph(esc(SUBTITLE), SUB),
    Spacer(1, 4),
    Paragraph(esc(TITLE), H1),
    Spacer(1, 4),
    Paragraph(f"{LABEL} · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min", META),
    Spacer(1, 14),
]

beat_num = 1
for section_title, lines in SECTIONS:
    if section_title:
        flow.append(Paragraph(f"— {esc(section_title)} —", SEC))
    for line in lines:
        flow.append(Paragraph(
            f'<font color="#888888"><b>[{beat_num}]</b></font>  {esc(line)}', LINE))
        beat_num += 1
    flow.append(Spacer(1, 8))

flow.append(Spacer(1, 10))
flow.append(Paragraph(f"END · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min", META))

doc.build(flow)
print(f"Saved: {pdf_path} | {total_beats} beats | {word_count} words")
