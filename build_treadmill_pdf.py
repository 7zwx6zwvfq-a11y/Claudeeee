#!/usr/bin/env python3
"""PDF production document for Video 8 — Hedonic Treadmill / Lifestyle Inflation."""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from build_treadmill_doc import BEATS

styles = getSampleStyleSheet()
H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=14, leading=18, alignment=TA_CENTER)
SUB  = ParagraphStyle('SUB',  parent=styles['Normal'], fontSize=9,  leading=12,
                      alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                      fontName='Helvetica-Bold')
META = ParagraphStyle('META', parent=styles['Normal'], fontSize=8,  leading=11,
                      alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
CELL = ParagraphStyle('CELL', parent=styles['Normal'], fontSize=7,  leading=9,  spaceAfter=0)
BOLD = ParagraphStyle('BOLD', parent=styles['Normal'], fontSize=7,  leading=9,
                      fontName='Helvetica-Bold')

SECTION_STARTS = {
    1:   "HOOK",
    10:  "THE RAISE",
    22:  "THE MECHANISM",
    35:  "THE TREADMILL",
    44:  "THE DIDEROT EFFECT",
    56:  "THE INDUSTRY",
    69:  "THE POPULAR MISREADING",
    78:  "THE REAL CONCLUSION",
    89:  "EL MOVIMIENTO",
    95:  "THE ENDING",
}

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

all_lines = [b[0] for b in BEATS]
word_count = sum(len(l.split()) for l in all_lines)
total_beats = len(BEATS)

pdf_path = "/home/user/Claudeeee/Treadmill_Production.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=landscape(A4),
                        leftMargin=10*mm, rightMargin=10*mm,
                        topMargin=12*mm, bottomMargin=12*mm)

flow = [
    Paragraph("CRAYON CAPITAL — CLONE SESSION · VIDEO 8", SUB),
    Spacer(1, 4),
    Paragraph("Getting Rich Is Making You Poorer", H1),
    Spacer(1, 4),
    Paragraph(f"STATE 5 — PRODUCTION DOCUMENT · {total_beats} beats · ~{word_count} words · "
              f"~{round(word_count/140)} min", META),
    Spacer(1, 10),
]

HDR = ["#", "SEGMENT (NARRATION)", "IMAGE PROMPT", "CAMERA",
       "LIGHTING", "MOOD / TONE", "CHARACTER ACTION", "VIDEO MOTION"]
COL_W = [10*mm, 44*mm, 65*mm, 28*mm, 26*mm, 28*mm, 28*mm, 34*mm]

tbl_data = [HDR]
row_styles = []
row_idx = 1

for beat_num, beat in enumerate(BEATS, 1):
    seg, scene, cam, light, mood, action, video = beat

    if beat_num in SECTION_STARTS:
        sec_label = f"── {SECTION_STARTS[beat_num]} ──"
        tbl_data.append([Paragraph(f'<b>{esc(sec_label)}</b>', CELL),
                         '', '', '', '', '', '', ''])
        row_styles.append(('SPAN',       (0, row_idx), (7, row_idx)))
        row_styles.append(('BACKGROUND', (0, row_idx), (7, row_idx), colors.HexColor('#B02A2A')))
        row_styles.append(('TEXTCOLOR',  (0, row_idx), (7, row_idx), colors.white))
        row_styles.append(('ALIGN',      (0, row_idx), (7, row_idx), 'CENTER'))
        row_idx += 1

    tbl_data.append([
        Paragraph(f'<b>{beat_num}</b>', BOLD),
        Paragraph(f'<b>{esc(seg)}</b>', BOLD),
        Paragraph(esc(scene),  CELL),
        Paragraph(esc(cam),    CELL),
        Paragraph(esc(light),  CELL),
        Paragraph(esc(mood),   CELL),
        Paragraph(esc(action), CELL),
        Paragraph(esc(video),  CELL),
    ])
    bg = colors.HexColor('#F9F9F9') if beat_num % 2 == 0 else colors.white
    row_styles.append(('BACKGROUND', (0, row_idx), (7, row_idx), bg))
    row_idx += 1

base_style = TableStyle([
    ('BACKGROUND',    (0, 0), (7, 0), colors.HexColor('#2C3E50')),
    ('TEXTCOLOR',     (0, 0), (7, 0), colors.white),
    ('FONTNAME',      (0, 0), (7, 0), 'Helvetica-Bold'),
    ('FONTSIZE',      (0, 0), (7, 0), 7),
    ('ALIGN',         (0, 0), (7, 0), 'CENTER'),
    ('GRID',          (0, 0), (-1, -1), 0.3, colors.HexColor('#CCCCCC')),
    ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING',    (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ('LEFTPADDING',   (0, 0), (-1, -1), 2),
    ('RIGHTPADDING',  (0, 0), (-1, -1), 2),
])
for s in row_styles:
    base_style.add(*s)

table = Table(tbl_data, colWidths=COL_W, repeatRows=1)
table.setStyle(base_style)
flow.append(table)
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    f"END OF PRODUCTION DOCUMENT · {total_beats} beats · ~{word_count} words · "
    f"~{round(word_count/140)} min narration", META))

doc.build(flow)
print(f"Saved: {pdf_path} | {total_beats} beats | {word_count} words")
