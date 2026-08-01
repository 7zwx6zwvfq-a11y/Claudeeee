#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert the 4 CSV sheets into standalone PDFs (no Excel needed)."""
import csv
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

styles = getSampleStyleSheet()
cell_style = ParagraphStyle("cell", parent=styles["Normal"], fontSize=7.5, leading=9.5, wordWrap="CJK")
header_style = ParagraphStyle("header", parent=styles["Normal"], fontSize=8.5, leading=10.5,
                               textColor=colors.white, fontName="Helvetica-Bold")
title_style = ParagraphStyle("title", parent=styles["Heading1"], fontSize=16, spaceAfter=10)

RED = colors.HexColor("#C62828")


def load_csv(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.reader(f))


def make_pdf(csv_path, pdf_path, title, col_widths_mm):
    rows = load_csv(csv_path)
    header, body = rows[0], rows[1:]

    data = [[Paragraph(h, header_style) for h in header]]
    for row in body:
        data.append([Paragraph(str(c) if c is not None else "", cell_style) for c in row])

    col_widths = [w * mm for w in col_widths_mm]

    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(A4),
                             leftMargin=10 * mm, rightMargin=10 * mm,
                             topMargin=12 * mm, bottomMargin=12 * mm)

    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), RED),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))

    elements = [Paragraph(title, title_style), Spacer(1, 4 * mm), table]
    doc.build(elements)
    print(f"Saved {pdf_path} ({len(body)} filas)")


base = "/tmp/claude-0/-home-user-Claudeeee/fed35260-2711-5769-ad05-7e136fd68906/scratchpad/"

make_pdf(base + "Aceite_Oliva_1_Beats.csv", base + "Aceite_Oliva_1_Beats.pdf",
          "Aceite de Oliva — Beats (444) con duracion y timecode (audio real 22:30)",
          col_widths_mm=[22, 8, 55, 45, 10, 14, 14, 14, 20, 15])

make_pdf(base + "Aceite_Oliva_2_Shots_unicos.csv", base + "Aceite_Oliva_2_Shots_unicos.pdf",
          "Aceite de Oliva — Shots unicos (101)",
          col_widths_mm=[26, 90, 15, 22, 124])

make_pdf(base + "Aceite_Oliva_3_Clip_a_Beats.csv", base + "Aceite_Oliva_3_Clip_a_Beats.pdf",
          "Aceite de Oliva — Clip -> Beats",
          col_widths_mm=[26, 85, 15, 18, 133])

make_pdf(base + "Aceite_Oliva_4_Pendiente_por_buscar.csv", base + "Aceite_Oliva_4_Pendiente_por_buscar.pdf",
          "Aceite de Oliva — Pendiente por buscar",
          col_widths_mm=[85, 192])

print("Listo.")
