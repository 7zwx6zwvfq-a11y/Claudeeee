#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el PDF de narracion limpia para copiar y pegar en ElevenLabs,
en el mismo estilo que Audio_Eleven_Labs.pdf (Crayon Capital)."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from full_script import SECTIONS

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
end_style = ParagraphStyle("end", parent=styles["Normal"], fontSize=8.5, leading=11,
                             textColor=GRAY, alignment=TA_CENTER, spaceBefore=14)


def split_sentences(text):
    text = text.replace("\n\n", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ"¿¡])', text)
    return [p.strip() for p in parts if p.strip()]


lines = []
for section, text in SECTIONS:
    lines.extend(split_sentences(text))

total_words = sum(len(line.split()) for line in lines)
total_lines = len(lines)

KICKER = "ETIQUETA REAL — SESIÓN DE PRODUCCIÓN · VIDEO 1"
TITLE = "7 Marcas de Aceite de Oliva Que Deberías Dejar de Comprar (Y 3 Que Sí Cumplen)"

doc = SimpleDocTemplate(
    "/tmp/claude-0/-home-user-Claudeeee/fed35260-2711-5769-ad05-7e136fd68906/scratchpad/Aceite_Oliva_ELEVENLABS.pdf",
    pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm, topMargin=20 * mm, bottomMargin=20 * mm)

elements = [
    Paragraph(KICKER, kicker_style),
    Paragraph(TITLE, title_style),
    Paragraph(f"ELEVEN LABS — GUION DE NARRACIÓN · {total_lines} líneas · ~{total_words} palabras",
              subtitle_style),
]

for line in lines:
    elements.append(Paragraph(line, body_style))

elements.append(Paragraph(f"FIN DEL GUION · {total_words} palabras", end_style))

doc.build(elements)
print(f"Guardado. {total_lines} lineas, {total_words} palabras.")
