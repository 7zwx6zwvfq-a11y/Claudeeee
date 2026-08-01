#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Documento maestro: cada frase (beat) + video asignado, en verde si esta
completado (clip descargado en la libreria), o marcado como pendiente si no."""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

from build_beats import expanded, SHOTS, DOWNLOAD_URLS

styles = getSampleStyleSheet()
cell_style = ParagraphStyle("cell", parent=styles["Normal"], fontSize=8, leading=10, wordWrap="CJK")
header_style = ParagraphStyle("header", parent=styles["Normal"], fontSize=9, leading=11,
                               textColor=colors.white, fontName="Helvetica-Bold")
title_style = ParagraphStyle("title", parent=styles["Heading1"], fontSize=16, spaceAfter=4)
subtitle_style = ParagraphStyle("subtitle", parent=styles["Normal"], fontSize=10, spaceAfter=8,
                                  textColor=colors.HexColor("#444444"))
section_style = ParagraphStyle("section", parent=styles["Normal"], fontSize=8.5, leading=10.5,
                                 fontName="Helvetica-Bold")

RED = colors.HexColor("#C62828")
GREEN_BG = colors.HexColor("#C8E6C9")
GREEN_TXT = colors.HexColor("#1B5E20")
PENDING_BG = colors.HexColor("#FFE0B2")
PENDING_TXT = colors.HexColor("#E65100")

data = [[
    Paragraph("Beat", header_style),
    Paragraph("Frase del guion", header_style),
    Paragraph("Video asignado", header_style),
    Paragraph("Estado", header_style),
]]

row_colors = []  # parallel list, one per data row (excluding header)
completed = 0
pending = 0

for section, beat, text, shot_key, motion in expanded:
    entry = SHOTS.get(shot_key)
    has_clip = entry is not None and entry[1] in DOWNLOAD_URLS
    if has_clip:
        title, sid = entry
        video_cell = Paragraph(f"{title} (ID {sid})", cell_style)
        status_cell = Paragraph("<font color='#1B5E20'><b>COMPLETADO</b></font>", cell_style)
        row_colors.append(GREEN_BG)
        completed += 1
    else:
        video_cell = Paragraph("—", cell_style)
        status_cell = Paragraph("<font color='#E65100'><b>SIN ASIGNAR</b></font>", cell_style)
        row_colors.append(PENDING_BG)
        pending += 1
    data.append([
        Paragraph(str(beat), cell_style),
        Paragraph(text, cell_style),
        video_cell,
        status_cell,
    ])

col_widths = [14 * mm, 110 * mm, 100 * mm, 33 * mm]

doc = SimpleDocTemplate(
    "/tmp/claude-0/-home-user-Claudeeee/fed35260-2711-5769-ad05-7e136fd68906/scratchpad/Aceite_Oliva_Frase_a_Video.pdf",
    pagesize=landscape(A4), leftMargin=10 * mm, rightMargin=10 * mm, topMargin=12 * mm, bottomMargin=12 * mm)

table = Table(data, colWidths=col_widths, repeatRows=1)
style_cmds = [
    ("BACKGROUND", (0, 0), (-1, 0), RED),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]
for i, bg in enumerate(row_colors, start=1):
    style_cmds.append(("BACKGROUND", (0, i), (-1, i), bg))
table.setStyle(TableStyle(style_cmds))

elements = [
    Paragraph("Aceite de Oliva — Frase por frase con video asignado", title_style),
    Paragraph(
        f"{len(expanded)} beats totales &nbsp;|&nbsp; "
        f"<font color='#1B5E20'><b>{completed} completados (verde)</b></font> &nbsp;|&nbsp; "
        f"<font color='#E65100'><b>{pending} sin asignar (naranja)</b></font>",
        subtitle_style),
    Spacer(1, 3 * mm),
    table,
]
doc.build(elements)
print(f"Guardado. Completados: {completed} / Pendientes: {pending}")
