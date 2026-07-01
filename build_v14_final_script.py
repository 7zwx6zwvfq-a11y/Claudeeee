#!/usr/bin/env python3
"""V14 Script — 5 Things That Drain Your Money Before Payday (No Matter What You Earn)."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

RED   = RGBColor(0xB0, 0x2A, 0x2A)
DARK  = RGBColor(0x2C, 0x3E, 0x50)
GREY  = RGBColor(0x77, 0x77, 0x77)
GREEN = RGBColor(0x1A, 0x7A, 0x3C)

BEATS = [
    # SECTION, BEAT_NUM, TEXT
    ("HOOK — PRIMEROS 5 SEGUNDOS",  1,  "Why does your money always disappear before payday?"),
    ("HOOK",                         2,  "Not sometimes. Every month."),
    ("HOOK",                         3,  "It doesn't matter if you earn €2,000 or €6,000."),
    ("HOOK",                         4,  "Four weeks. Same empty account."),
    ("HOOK",                         5,  "Five things are doing this to you."),
    ("HOOK",                         6,  "And number one runs before you even get paid."),
    ("HOOK",                         7,  "Not when you spend it. Before."),
    ("HOOK",                         8,  "Here's the list."),

    ("SETUP",                        9,  "These aren't budgeting mistakes."),
    ("SETUP",                       10,  "They're not discipline failures."),
    ("SETUP",                       11,  "They're patterns. And they run automatically."),
    ("SETUP",                       12,  "Number five is the one everyone knows. And still can't stop."),

    ("ITEM 5 — THE CARD GAP",       13,  "Number five. The Card Gap."),
    ("ITEM 5",                      14,  "When you pay with cash, your brain registers loss."),
    ("ITEM 5",                      15,  "You feel the €40 leave."),
    ("ITEM 5",                      16,  "When you pay with card — tap, done — the pain disappears."),
    ("ITEM 5",                      17,  "Same purchase. Different brain response."),
    ("ITEM 5",                      18,  "Card users spend 20 to 47% more than cash users."),
    ("ITEM 5",                      19,  "Not because they want to. Because the payment doesn't feel like payment."),
    ("ITEM 5",                      20,  "Your brain is still waiting for the money to actually leave."),

    ("ITEM 4 — THE REWARD DRAIN",   21,  "Number four. The Reward Drain."),
    ("ITEM 4",                      22,  "It's Thursday. You've had a brutal week."),
    ("ITEM 4",                      23,  "Alex has too. Deadlines. A difficult meeting. Late nights."),
    ("ITEM 4",                      24,  "And his brain does something automatic."),
    ("ITEM 4",                      25,  "It calculates what he's owed."),
    ("ITEM 4",                      26,  "Not the salary. Something extra."),
    ("ITEM 4",                      27,  "'I worked hard. I deserve this.'"),
    ("ITEM 4",                      28,  "That sentence has cost more money than any impulse purchase."),

    ("ITEM 3 — THE INVISIBLE DRAIN",29,  "Number three. The Invisible Drain."),
    ("ITEM 3",                      30,  "Right now, you have at least three subscriptions you've forgotten about."),
    ("ITEM 3",                      31,  "Apps you haven't opened in four months."),
    ("ITEM 3",                      32,  "Services that auto-renewed in January."),
    ("ITEM 3",                      33,  "Why haven't you cancelled them?"),
    ("ITEM 3",                      34,  "Because cancelling requires a decision. And decisions cost energy."),
    ("ITEM 3",                      35,  "Your brain doesn't cancel things. It lets them run."),

    ("CTA",                         36,  "If your brain is doing this to you right now — subscribe."),
    ("CTA",                         37,  "We break down a new pattern every week. It's free. And it might save you more than you think."),

    ("ITEM 2 — SOCIAL SPENDING",    38,  "Number two. Social Spending."),
    ("ITEM 2",                      39,  "You bought something this month for an audience that wasn't watching."),
    ("ITEM 2",                      40,  "The car that looks good in the parking lot."),
    ("ITEM 2",                      41,  "The jacket for the meeting."),
    ("ITEM 2",                      42,  "The upgrade nobody asked for but someone might notice."),
    ("ITEM 2",                      43,  "Who is that person you're buying for?"),
    ("ITEM 2",                      44,  "They don't exist. They're a projection."),
    ("ITEM 2",                      45,  "The most expensive audience in your life has never spent a single dollar."),
    ("ITEM 2",                      46,  "They live entirely in your head. And they have expensive taste."),

    ("ITEM 1 — THE PRE-SPEND",      47,  "Number one. The one nobody names."),
    ("ITEM 1",                      48,  "The Pre-Spend."),
    ("ITEM 1",                      49,  "It's Wednesday. Payday is Friday."),
    ("ITEM 1",                      50,  "Alex hasn't received anything yet."),
    ("ITEM 1",                      51,  "But his brain has already spent it."),
    ("ITEM 1",                      52,  "Not metaphorically. Neurologically."),
    ("ITEM 1",                      53,  "The moment you know money is coming — your brain allocates it."),
    ("ITEM 1",                      54,  "The rent. The pending bill. The thing you've been delaying."),
    ("ITEM 1",                      55,  "And then — quietly — a few things that feel deserved."),
    ("ITEM 1",                      56,  "By the time Friday arrives, the money is already gone in your mind."),
    ("ITEM 1",                      57,  "Friday is just the confirmation."),
    ("ITEM 1",                      58,  "You don't spend your salary. You process a transaction your brain closed on Wednesday."),

    ("MECHANISM CONCLUSION",        59,  "Five patterns. Running automatically."),
    ("MECHANISM CONCLUSION",        60,  "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend."),
    ("MECHANISM CONCLUSION",        61,  "None of them feel like mistakes when they happen."),
    ("MECHANISM CONCLUSION",        62,  "The Card Gap feels convenient."),
    ("MECHANISM CONCLUSION",        63,  "The Reward Drain feels earned. The Social Spend feels reasonable. The Pre-Spend feels like planning."),

    ("THE STRUCTURAL FIX",          64,  "The fix isn't 'spend less.'"),
    ("THE STRUCTURAL FIX",          65,  "That's not a system. That's a wish."),
    ("THE STRUCTURAL FIX",          66,  "For the Card Gap: switch one category to cash. Groceries. Restaurants. One category."),
    ("THE STRUCTURAL FIX",          67,  "You don't need to feel the money leaving everywhere. Just somewhere."),
    ("THE STRUCTURAL FIX",          68,  "For the Reward Drain: budget it. €80 a month. 'This is my earned money.'"),
    ("THE STRUCTURAL FIX",          69,  "When it's gone, it's gone. The Villain needs a container, not a lecture."),
    ("THE STRUCTURAL FIX",          70,  "For the Invisible Drain: one audit. Once a year. Not monthly — once."),
    ("THE STRUCTURAL FIX",          71,  "For Social Spending: one question before every non-essential purchase."),
    ("THE STRUCTURAL FIX",          72,  "'Who am I buying this for?' If the answer isn't you — pause."),
    ("THE STRUCTURAL FIX",          73,  "For the Pre-Spend: the salary hits the account. You don't touch it for 24 hours."),

    ("BRAIN VILLAIN'S LAST TRICK",  74,  "The Brain Villain has one response to this list."),
    ("BRAIN VILLAIN'S LAST TRICK",  75,  "You're feeling it right now."),
    ("BRAIN VILLAIN'S LAST TRICK",  76,  "Not resistance. Something quieter."),
    ("BRAIN VILLAIN'S LAST TRICK",  77,  "Something that sounds like common sense: 'I already know this.'"),
    ("BRAIN VILLAIN'S LAST TRICK",  78,  "That thought is not wisdom. Not self-awareness."),
    ("BRAIN VILLAIN'S LAST TRICK",  79,  "It is the Invisible Drain wearing the costume of insight."),
    ("BRAIN VILLAIN'S LAST TRICK",  80,  "The programs are not broken."),
    ("BRAIN VILLAIN'S LAST TRICK",  81,  "They were built for a world where money was physical — coins you could feel, resources you could see leaving."),
    ("BRAIN VILLAIN'S LAST TRICK",  82,  "In that world, the Pre-Spend was planning. The Reward Drain was recovery. The Card Gap didn't exist."),
    ("BRAIN VILLAIN'S LAST TRICK",  83,  "The Brain Villain was built for that world. Not this one."),
    ("BRAIN VILLAIN'S LAST TRICK",  84,  "These five systems were designed for the world you actually live in."),

    ("IDENTITY CLOSE",              85,  "Your money doesn't disappear."),
    ("IDENTITY CLOSE",              86,  "It follows five very predictable routes."),
    ("IDENTITY CLOSE",              87,  "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend."),
    ("IDENTITY CLOSE",              88,  "Name them. And they lose power."),
    ("IDENTITY CLOSE",              89,  "You're not bad with money."),
    ("IDENTITY CLOSE",              90,  "You're running programs that were never designed for a world with direct deposits and one-click payments."),
    ("IDENTITY CLOSE",              91,  "Now you know which five. That's the first thing the Villain didn't want you to have."),

    ("NEXT VIDEO TEASE",            92,  "Next week — the one decision that stops all five."),
    ("NEXT VIDEO TEASE",            93,  "Not five solutions. One."),
    ("NEXT VIDEO TEASE",            94,  "Made once. Before the patterns activate."),
    ("NEXT VIDEO TEASE",            95,  "See you Thursday."),
]

# ── DOCX SCRIPT ──
def build_script_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(10)

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("NEUROCENTS — VIDEO 14")
    r.bold = True; r.font.size = Pt(14); r.font.color.rgb = RED

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run("5 Things That Drain Your Money Before Payday (No Matter What You Earn)")
    r.font.size = Pt(11); r.font.color.rgb = DARK

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run("95 beats · Hook S1 · Lista con Ranking · Sin datos científicos · CapCut static")
    r.font.size = Pt(9); r.font.color.rgb = GREY

    doc.add_paragraph()

    current_section = ""
    for section, num, text in BEATS:
        if section != current_section:
            current_section = section
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(f"── {section} ──")
            r.bold = True; r.font.size = Pt(10); r.font.color.rgb = RED

        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(0.5)
        r1 = p.add_run(f"[{num:02d}]  ")
        r1.bold = True; r1.font.size = Pt(9); r1.font.color.rgb = GREY
        r2 = p.add_run(text)
        r2.font.size = Pt(11)

    path = "/home/user/Claudeeee/V14_final_SCRIPT.docx"
    doc.save(path)
    print(f"✅ SCRIPT.docx saved: {path}")
    return path

# ── PDF ELEVENLABS ──
def build_elevenlabs_pdf():
    path = "/home/user/Claudeeee/V14_final_ELEVENLABS.pdf"
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    beat_style = ParagraphStyle('beat', fontSize=12, leading=18,
                                spaceAfter=6, fontName='Helvetica')
    section_style = ParagraphStyle('section', fontSize=10, leading=14,
                                   spaceAfter=4, spaceBefore=16,
                                   textColor=colors.HexColor('#B02A2A'),
                                   fontName='Helvetica-Bold')
    story = []
    story.append(Paragraph("NEUROCENTS · V14 · ELEVENLABS SCRIPT", section_style))
    story.append(Paragraph("5 Things That Drain Your Money Before Payday (No Matter What You Earn)", beat_style))
    story.append(Spacer(1, 0.4*cm))

    current_section = ""
    for section, num, text in BEATS:
        if section != current_section:
            current_section = section
            story.append(Spacer(1, 0.3*cm))
            story.append(Paragraph(f"── {section} ──", section_style))
        story.append(Paragraph(text, beat_style))

    doc.build(story)
    print(f"✅ ELEVENLABS.pdf saved: {path}")
    return path

build_script_docx()
build_elevenlabs_pdf()
