#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los PDFs de produccion del video de Cafe (V3):
1) Cafe_ELEVENLABS.pdf   - narracion limpia, linea a linea, para pegar en ElevenLabs
2) Cafe_SCRIPT.pdf       - guion legible con cabeceras de seccion, para revision
3) Cafe_Beats.pdf        - tabla de beats con timecodes, sugerencia visual y CapCut Motion
4) Cafe_Shots_unicos.pdf - tabla de shots unicos reales verificados
"""
import re
import csv
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from cafe_full_script import SECTIONS

base = "/tmp/claude-0/-home-user-Claudeeee/fed35260-2711-5769-ad05-7e136fd68906/scratchpad/"

RED = colors.HexColor("#C62828")
GRAY = colors.HexColor("#666666")

styles = getSampleStyleSheet()
kicker_style = ParagraphStyle("kicker", parent=styles["Normal"], fontSize=9, leading=11,
                                textColor=RED, fontName="Helvetica-Bold",
                                alignment=TA_CENTER, spaceAfter=6)
title_style = ParagraphStyle("title", parent=styles["Heading1"], fontSize=17, leading=21,
                               alignment=TA_CENTER, spaceAfter=4, fontName="Helvetica-Bold")
subtitle_style = ParagraphStyle("subtitle", parent=styles["Normal"], fontSize=9.5, leading=12,
                                  textColor=GRAY, alignment=TA_CENTER, spaceAfter=16)
body_style = ParagraphStyle("body", parent=styles["Normal"], fontSize=10.5, leading=15,
                              alignment=TA_LEFT, spaceAfter=6, fontName="Helvetica")
section_style = ParagraphStyle("section", parent=styles["Heading2"], fontSize=12.5, leading=16,
                                 textColor=RED, fontName="Helvetica-Bold",
                                 spaceBefore=14, spaceAfter=6)
end_style = ParagraphStyle("end", parent=styles["Normal"], fontSize=8.5, leading=11,
                             textColor=GRAY, alignment=TA_CENTER, spaceBefore=14)

KICKER = "CAFE — SESION DE PRODUCCION · VIDEO 3"
TITLE = "10 Marcas de Cafe Que Deberias Dejar de Comprar (Y 5 Que Si Cumplen)"


def split_sentences(text):
    text = text.replace("\n\n", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ"¿¡])', text)
    return [p.strip() for p in parts if p.strip()]


# ---------------- 1) ELEVENLABS PDF (narracion limpia) ----------------
lines = []
for section, text in SECTIONS:
    lines.extend(split_sentences(text))

total_words = sum(len(line.split()) for line in lines)
total_lines = len(lines)

doc = SimpleDocTemplate(base + "Cafe_ELEVENLABS.pdf", pagesize=A4,
                         leftMargin=22 * mm, rightMargin=22 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
elements = [
    Paragraph(KICKER, kicker_style),
    Paragraph(TITLE, title_style),
    Paragraph(f"ELEVEN LABS — GUION DE NARRACION · {total_lines} lineas · ~{total_words} palabras",
              subtitle_style),
]
for line in lines:
    elements.append(Paragraph(line, body_style))
elements.append(Paragraph(f"FIN DEL GUION · {total_words} palabras", end_style))
doc.build(elements)
print(f"Guardado Cafe_ELEVENLABS.pdf ({total_lines} lineas, {total_words} palabras)")


# ---------------- 2) SCRIPT PDF (con cabeceras de seccion, para revision) ----------------
doc2 = SimpleDocTemplate(base + "Cafe_SCRIPT.pdf", pagesize=A4,
                          leftMargin=22 * mm, rightMargin=22 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
elements2 = [
    Paragraph(KICKER, kicker_style),
    Paragraph(TITLE, title_style),
    Paragraph(f"GUION COMPLETO CON SECCIONES · ~{total_words} palabras · ~{total_words/174:.1f} min a 174 ppm",
              subtitle_style),
]
for section, text in SECTIONS:
    elements2.append(Paragraph(section, section_style))
    for para in text.split("\n\n"):
        elements2.append(Paragraph(para.strip(), body_style))
elements2.append(Paragraph(f"FIN DEL GUION · {total_words} palabras", end_style))
doc2.build(elements2)
print(f"Guardado Cafe_SCRIPT.pdf")


# ---------------- 3) BEATS PDF (desde el CSV generado por build_beats_cafe.py) ----------------
cell_style = ParagraphStyle("cell", parent=styles["Normal"], fontSize=7.5, leading=9.5, wordWrap="CJK")
header_style = ParagraphStyle("header", parent=styles["Normal"], fontSize=8.5, leading=10.5,
                               textColor=colors.white, fontName="Helvetica-Bold")
pdf_title_style = ParagraphStyle("pdftitle", parent=styles["Heading1"], fontSize=15, spaceAfter=8)

with open(base + "Cafe_Beats.csv", encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))
header, body = rows[0], rows[1:]

data = [[Paragraph(h, header_style) for h in header]]
for row in body:
    data.append([Paragraph(str(c) if c is not None else "", cell_style) for c in row])

col_widths_mm = [24, 8, 50, 48, 14, 11, 13, 13, 20, 20]
col_widths = [w * mm for w in col_widths_mm]

doc3 = SimpleDocTemplate(base + "Cafe_Beats.pdf", pagesize=landscape(A4),
                          leftMargin=8 * mm, rightMargin=8 * mm, topMargin=12 * mm, bottomMargin=12 * mm)
table = Table(data, colWidths=col_widths, repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), RED),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
elements3 = [
    Paragraph(f"{TITLE} — Beats ({len(body)}) con duracion y timecode (objetivo ~24:00)", pdf_title_style),
    Spacer(1, 3 * mm),
    Paragraph("Shots verificados en el catalogo real de Freepik (IDs reales via stock_search). "
              "Para descargar el archivo final usar stock_download(id, tipo) en el momento de montar "
              "en CapCut -- las URLs firmadas caducan en horas, por eso no se guardan aqui.",
              ParagraphStyle("note", parent=styles["Normal"], fontSize=8, textColor=RED, spaceAfter=4)),
    Spacer(1, 2 * mm),
    table,
]
doc3.build(elements3)
print(f"Guardado Cafe_Beats.pdf ({len(body)} filas)")


# ---------------- 4) SHOTS UNICOS PDF ----------------
with open(base + "Cafe_Shots_unicos.csv", encoding="utf-8-sig") as f:
    rows4 = list(csv.reader(f))
header4, body4 = rows4[0], rows4[1:]
data4 = [[Paragraph(h, header_style) for h in header4]]
for row in body4:
    data4.append([Paragraph(str(c) if c is not None else "", cell_style) for c in row])

col_widths4_mm = [40, 130, 25, 25]
col_widths4 = [w * mm for w in col_widths4_mm]
doc4 = SimpleDocTemplate(base + "Cafe_Shots_unicos.pdf", pagesize=landscape(A4),
                          leftMargin=10 * mm, rightMargin=10 * mm, topMargin=12 * mm, bottomMargin=12 * mm)
table4 = Table(data4, colWidths=col_widths4, repeatRows=1)
table4.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), RED),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
elements4 = [
    Paragraph(f"{TITLE} — Shots unicos ({len(body4)})", pdf_title_style),
    Spacer(1, 3 * mm),
    table4,
]
doc4.build(elements4)
print(f"Guardado Cafe_Shots_unicos.pdf ({len(body4)} filas)")

print("Listo. 4 PDFs generados.")
