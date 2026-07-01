#!/usr/bin/env python3
"""V14 Prepublish Checklist — 5 Things That Drain Your Money Before Payday."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

RED   = RGBColor(0xB0, 0x2A, 0x2A)
DARK  = RGBColor(0x2C, 0x3E, 0x50)
GREY  = RGBColor(0x77, 0x77, 0x77)
GREEN = RGBColor(0x1A, 0x7A, 0x3C)

def add_section(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(f"── {title} ──")
    r.bold = True; r.font.size = Pt(10); r.font.color.rgb = RED

def add_field(doc, label, value, label_color=GREY, value_color=DARK):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{label}: ")
    r1.bold = True; r1.font.size = Pt(9); r1.font.color.rgb = label_color
    r2 = p.add_run(value)
    r2.font.size = Pt(10); r2.font.color.rgb = value_color

def add_check(doc, text, checked=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(1)
    prefix = "☑" if checked else "☐"
    r = p.add_run(f"{prefix}  {text}")
    r.font.size = Pt(10); r.font.color.rgb = DARK

def add_multiline(doc, label, lines, label_color=GREY):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.5)
    r1 = p.add_run(f"{label}:")
    r1.bold = True; r1.font.size = Pt(9); r1.font.color.rgb = label_color
    for line in lines:
        p2 = doc.add_paragraph()
        p2.paragraph_format.space_before = Pt(1)
        p2.paragraph_format.space_after = Pt(1)
        p2.paragraph_format.left_indent = Cm(1)
        r = p2.add_run(line)
        r.font.size = Pt(10); r.font.color.rgb = DARK

def build_checklist():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(10)

    # Title
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("NEUROCENTS — VIDEO 14 — PREPUBLISH CHECKLIST")
    r.bold = True; r.font.size = Pt(14); r.font.color.rgb = RED

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run("5 Things That Drain Your Money Before Payday (No Matter What You Earn)")
    r.font.size = Pt(11); r.font.color.rgb = DARK

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run("Publish: Thursday 20:15 Spain (CEST) = 14:15 EST · 95 beats · Lista con Ranking · Hook S1")
    r.font.size = Pt(9); r.font.color.rgb = GREY

    doc.add_paragraph()

    # ── TITLE & METADATA ──
    add_section(doc, "TITLE & METADATA")
    add_field(doc, "TITLE (primary)", "5 Things That Drain Your Money Before Payday (No Matter What You Earn)")
    add_field(doc, "TITLE (alt A)", "5 Reasons You're Broke Before Payday (No Matter What You Earn)")
    add_field(doc, "TITLE (alt B)", "Why You're Broke Before Payday — 5 Things Your Brain Does")
    add_field(doc, "Hook Strategy", "S1 — Pregunta Sin Resolver (Zeigarnik Effect)")
    add_field(doc, "Format", "Lista con Ranking (5 → 1), sector-wide topic, no scientific data")
    add_field(doc, "Beat Count", "95 beats (~8–10 min)")
    add_field(doc, "Keyword target", "behavioral finance / psychology of money / financial psychology")

    # ── YOUTUBE DESCRIPTION ──
    add_section(doc, "YOUTUBE DESCRIPTION")
    description_lines = [
        "Why does your money always disappear before payday? Not sometimes. Every month.",
        "",
        "It doesn't matter if you earn €2,000 or €6,000. Four weeks. Same empty account.",
        "",
        "5 things are draining your money before payday — and none of them feel like mistakes when they happen.",
        "",
        "In this video:",
        "5. The Card Gap — why card payments silence the part of your brain that registers loss",
        "4. The Reward Drain — the sentence that has cost more than any impulse purchase",
        "3. The Invisible Drain — why your brain doesn't cancel things, it lets them run",
        "2. Social Spending — the most expensive audience in your life has never spent a single dollar",
        "1. The Pre-Spend — the one nobody names. It runs before the money arrives.",
        "",
        "These aren't budgeting mistakes. They're not discipline failures.",
        "They're patterns. And they run automatically.",
        "",
        "We break down a new financial pattern every week. Subscribe — it's free.",
        "",
        "#behavioralfinance #psychologyofmoney #financialpsychology #personalfinance #moneypsychology",
    ]
    add_multiline(doc, "DESCRIPTION", description_lines)

    # ── TAGS ──
    add_section(doc, "TAGS (YouTube Studio — paste as comma-separated)")
    tags = [
        "behavioral finance, psychology of money, financial psychology, why am I broke before payday,",
        "money psychology, brain and money, cognitive biases money, why money disappears,",
        "neuroscience money, personal finance psychology, broke before payday, card gap,",
        "reward drain, invisible drain, social spending, pre-spend, money patterns,",
        "why you can't save money, financial behavior, money habits, brain villain,",
        "subscription drain, impulsive spending psychology, payday money gone",
    ]
    for tag_line in tags:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(tag_line)
        r.font.size = Pt(9); r.font.color.rgb = DARK

    # ── THUMBNAIL ──
    add_section(doc, "THUMBNAIL SPEC")
    add_field(doc, "Background", "WHITE — Andy/MoneyTom style. Not dark.")
    add_field(doc, "Character", "Alex — BLUE t-shirt, wide eyes (recognition not panic), Brain Villain lit inside skull")
    add_field(doc, "Key visual", "Phone showing €0.00 balance. Two-day countdown to payday on calendar.")
    add_field(doc, "Text overlay", "BROKE BEFORE PAYDAY — max 3 words, bold Impact, left or center")
    add_field(doc, "Layout", "Alex right, text left — or Alex center with text above and below")
    add_field(doc, "CRITICAL", "Thumbnail → Title → Beat 1 continuity: Alex with €0.00 = recognition in <5 seconds")

    add_multiline(doc, "Thumbnail Generation Prompt (Google Flow)",
        [
            "2D flat cartoon illustration, thick solid black outlines, clean solid color fills, no gradients.",
            "Alex: large beige oval head (#F5E6C8), transparent glass upper skull revealing pink cartoon Brain Villain (#E8A598),",
            "small black dot eyes, expression: wide eyes and slight jaw drop (recognition + dread — NOT panic),",
            "black spiky hair, BLUE t-shirt (NOT RED — verify), gray pants.",
            "Brain Villain: pink cartoon brain, heavy-lidded eyes, smirking — lit up and satisfied.",
            "Alex holds phone showing €0.00 in bold. Calendar in background: two days marked to payday.",
            "White background. Text overlay: BROKE BEFORE PAYDAY in bold black Impact, left side.",
            "16:9 thumbnail composition. Clean, high contrast.",
        ]
    )

    # ── REDDIT STRATEGY ──
    add_section(doc, "REDDIT DISTRIBUTION")
    add_field(doc, "Primary subreddits", "r/personalfinance · r/financialindependence · r/povertyfinance")
    add_field(doc, "Secondary", "r/psychology · r/cogsci · r/mildlyinteresting")
    add_field(doc, "Post timing", "Same day as publish, after 2–3h (first wave should be visible)")

    add_multiline(doc, "Reddit Post (r/personalfinance)",
        [
            "Title: The reason you're broke before payday isn't what you think",
            "",
            "Body:",
            "I spent a while mapping why money disappears before payday — not sometimes, but every single month —",
            "even when income goes up.",
            "",
            "Turned out it wasn't budgeting failures. It was 5 specific patterns that run automatically.",
            "The worst one activates before the money even arrives.",
            "",
            "The five: Card Gap, Reward Drain, Invisible Drain, Social Spending, and the Pre-Spend.",
            "None of them feel like mistakes when they happen. That's what makes them effective.",
            "",
            "Made a video going through all five and the structural fix for each:",
            "[LINK]",
            "",
            "Curious if others recognize any of these. Number 4 — the Reward Drain — seems to be universal.",
        ]
    )

    add_multiline(doc, "Reddit Post (r/povertyfinance)",
        [
            "Title: 5 things that drain money before payday — regardless of income level",
            "",
            "Body:",
            "One thing I kept noticing: the timing doesn't change with income.",
            "€2,000 earners and €6,000 earners hit the same empty account by payday.",
            "",
            "Mapped out 5 patterns that explain why. None of them are about discipline.",
            "They're behavioral — and they have structural fixes.",
            "",
            "The one that surprised me most: the Pre-Spend. Your brain allocates your salary",
            "before it arrives. By Friday, it's just processing a transaction that closed on Wednesday.",
            "",
            "Full breakdown here: [LINK]",
        ]
    )

    # ── YOUTUBE STUDIO CONFIG ──
    add_section(doc, "YOUTUBE STUDIO CONFIGURATION")
    add_field(doc, "Publish Time", "Thursday 20:15 Spain CEST / 14:15 EST")
    add_field(doc, "Playlist", "Add to: Behavioral Finance / Brain & Money series")
    add_field(doc, "End Screen", "Add subscribe button + previous video card (last 20 seconds)")
    add_field(doc, "Cards", "Place at ~35% (CTA beat) and ~80% (Brain Villain section)")
    add_field(doc, "Category", "Education")
    add_field(doc, "Language", "English (US)")
    add_field(doc, "Subtitles", "Add auto-generated, review for accuracy after upload")
    add_field(doc, "First Comment", "Pin within 15 minutes: question to drive comments (see below)")

    # ── PINNED COMMENT ──
    add_section(doc, "PINNED COMMENT + REPLIES")

    add_multiline(doc, "Pinned Comment (post immediately)",
        [
            "Which of the 5 hit you hardest?",
            "",
            "For me it's always been number 4 — the Reward Drain.",
            "The math the brain does on a brutal Thursday is frighteningly fast.",
            "Drop yours below 👇",
        ]
    )

    comments = [
        ("Comment 1 suggestion",
         "The Pre-Spend is the one I can't unsee now. I check my balance on Wednesday and it's fine. "
         "By Friday when the money hits, somehow it's already gone. That receipt dated Wednesday is real."),
        ("Comment 2 suggestion",
         "The ghost audience bit was uncomfortable because I have 3 items in my closet that were "
         "bought for people who weren't even in the room. And still wouldn't have noticed."),
        ("Comment 3 suggestion",
         "The Card Gap number (20-47% more spending) is the one I'd have argued with before this. "
         "Now I can't use a card for groceries without thinking about it."),
        ("Comment 4 suggestion",
         "The annual subscription audit is the most underrated tip here. Once. Per year. "
         "That's the version I can actually do."),
        ("Comment 5 suggestion",
         "'Not five solutions. One.' — I need that video to exist immediately."),
    ]

    replies = [
        ("Reply to Comment 1",
         "The Wednesday receipt is the most disorienting part. The money arrives and your brain is like "
         "'already processed that.' Literally just confirmation at that point."),
        ("Reply to Comment 2",
         "The ghost audience living in your head and having expensive taste — that's the part that "
         "doesn't go away. The question 'who am I buying this for' starts following every purchase."),
        ("Reply to Comment 3",
         "The 47% is the high end but even the low end (20%) over a year compounds into something "
         "you can feel. One cash category is genuinely enough to change the signal."),
        ("Reply to Comment 4",
         "Once per year. That's it. The reason most people don't do it is the feeling that it should "
         "be more frequent — and that friction kills it before it starts."),
        ("Reply to Comment 5",
         "Thursday. See you there."),
    ]

    for label, text in comments:
        add_field(doc, label, text, label_color=GREEN)

    doc.add_paragraph()
    for label, text in replies:
        add_field(doc, label, text, label_color=GREY)

    # ── PRE-PUBLISH CHECKLIST ──
    add_section(doc, "PRE-PUBLISH CHECKLIST")
    checks = [
        "Script (95 beats) narrated and audio rendered in ElevenLabs",
        "All 95 images generated in Google Flow — BLUE t-shirt verified in all",
        "CapCut: Zoom In Slow (Acercamiento) on all clips, Zoom In Fast on key numbers",
        "Music: royalty-free atmospheric ambient piano — consistent volume under narration",
        "Thumbnail: Alex + €0.00 + Brain Villain lit — WHITE background — text left/center",
        "Thumbnail tested: thumbnail → title → beat 1 continuity <5 seconds",
        "YouTube title confirmed: 5 Things That Drain Your Money Before Payday (No Matter What You Earn)",
        "Description pasted — check all 5 items listed correctly",
        "Tags pasted (comma-separated in YouTube Studio)",
        "Publish scheduled: Thursday 20:15 Spain / 14:15 EST",
        "End screen set (subscribe + previous video card)",
        "Cards placed at ~35% and ~80%",
        "Reddit posts drafted and ready to paste day-of",
        "Pinned comment ready — post within 15 minutes of going live",
        "V13 analytics checked before publishing — note current state",
    ]
    for check in checks:
        add_check(doc, check)

    # ── NEXT VIDEO NOTE ──
    add_section(doc, "NEXT VIDEO — V15 PLANNING NOTE")
    add_field(doc, "Tease in V14", "Next week — the one decision that stops all five.")
    add_field(doc, "Hook commitment", "ONE DECISION. Made once. Before the patterns activate.")
    add_field(doc, "Hook Strategy (do NOT repeat S1)", "Use S3 (In Medias Res) or S4 (Contraintuitiva) — check rotation table")
    add_field(doc, "Format options", "Mechanism deep-dive OR comparativa (one decision vs five individual fixes)")
    add_field(doc, "Keyword target", "behavioral finance / save more tomorrow / automatizar finanzas")
    add_field(doc, "Note", "The 'one decision' tease creates committed viewers — V15 must deliver that promise immediately.")

    path = "/home/user/Claudeeee/V14_final_Prepublish_Checklist.docx"
    doc.save(path)
    print(f"✅ Prepublish_Checklist.docx saved: {path}")
    return path

build_checklist()
