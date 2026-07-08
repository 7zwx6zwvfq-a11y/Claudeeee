#!/usr/bin/env python3
"""
VIDEO 16 — PRODUCTION DOCUMENT · CATÁLOGO
Tabla: # | SEGMENT | IMAGE PROMPT | CAMERA | LIGHTING | MOOD/TONE | CHARACTER ACTION | VIDEO MOTION
Formato landscape idéntico a V13/V15. 81 beats.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v16_final_image_prompts_pdf import BEATS, STYLE as STYLE_PREAMBLE

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER

TITLE    = "Every Money Bias & Its Effect Explained in 8 Minutes"
SUBTITLE = "NEUROCENTS · VIDEO 16 — CATALOG FORMAT"
META     = "PRODUCTION DOCUMENT · 81 beats · ~1,210 words · ~9 min"

SECTION_STARTS = {}
_last = None
for _b in BEATS:
    if _b[1] != _last:
        SECTION_STARTS[_b[0]] = _b[1]
        _last = _b[1]

# (camera, lighting, mood, char_action, video_motion) × 81
PROD = [
    # BIAS 1 — ANCHORING (1-9)
    ("FULL FRAME on teal badge", "Clean white, badge saturated", "Catalog opens — S17 grid match", "No characters — badge alone, one confident pulse", "ZOOM IN FAST · 1.5s → badge center"),
    ("GRID montage, 3 cells", "Neutral bright", "Ubiquity — it's everywhere", "Villain tiny, top-right corner — stamps each cell", "PAN RIGHT · 3s across cells"),
    ("MACRO on price tag", "Boutique warm spot", "The bait, shot like a jewel", "Alex examines the tag, hand on chin, eyebrows rising", "ZOOM IN SLOW · 3s into €90"),
    ("CLOSE on tag + gauge edge", "Warm gold glow rising", "ONSET — bargain feeling ignites", "No characters — golden glow + gauge only", "ZOOM IN FAST · 1s → sparkle burst"),
    ("DIAGRAM, brain + arrows", "Flat white clinical", "The comparison shortcut exposed", "Villain center, medium — plays the processor", "STATIC · 2s"),
    ("CLOSE on frozen loading bar", "Cold UI light + hot €200 pulse", "PEAK — real question never loads", "Alex stares at the frozen bar, hypnotized", "SHAKE · SHORT on glitch"),
    ("MEDIUM, dark closet", "Dim, teal glow fading", "COMEDOWN — buyer's silence", "Alex deflates at the doorway", "ZOOM OUT SLOW · 4s from jacket"),
    ("WIDE city street", "Flat daylight", "The bias owns the landscape", "Alex walks through, small in frame, unaware", "PAN LEFT · 4s across street"),
    ("MINIMAL two numbers + arc", "Max white space", "LAPIDARIA — let it land", "No characters — the arc bridges the numbers", "ZOOM IN SLOW · 4s to arc center"),
    # BIAS 2 — LOSS AVERSION (10-17)
    ("FULL FRAME red badge", "Stone-texture backdrop", "The ancient one", "No characters — badge on stone pedestal", "ZOOM IN FAST · 1.5s → badge"),
    ("DIAGRAM balance scale", "Split red/green glows", "The 2x asymmetry", "No characters — same note, double weight visual", "STATIC · 3s — read the scale"),
    ("MEDIUM Alex + phone", "Cool screen light", "ONSET — body before thought", "Alex looks at his phone, chest fist-clench icon squeezes", "ZOOM IN FAST · 1s → chest"),
    ("TRIPTYCH of grips", "Neutral, red accents", "PEAK — three irrational holds", "Alex grips a falling chart, hugs a box, clings to a burning contract", "PAN RIGHT · 4s across grips"),
    ("MINIMAL trophy vs shield", "White void", "Not to win. Not to lose.", "Villain small, center, hugs the glowing shield like a teddy bear", "STATIC · 2s"),
    ("CORRIDOR of faded doors", "Ghost light", "COMEDOWN — unlived options", "Alex walks the corridor, touches nothing", "PAN RIGHT · 4s down corridor"),
    ("GRAPH two life-lines", "Clean white", "The uncompounded life", "No characters — ghost curve rises, gray line crawls", "DIAGONAL PAN + ZOOM IN · 4s along curve"),
    ("CLOSE jar + ignored coins", "Soft warm on jar", "LAPIDARIA — protecting a feeling", "Villain left side, medium, hugs the jar; coins ignored outside", "ZOOM IN SLOW · 3s into jar"),
    # BIAS 3 — MENTAL ACCOUNTING (18-24)
    ("FULL FRAME purple badge", "Clean white", "The three wallets", "No characters — envelopes fanned on table", "ZOOM IN FAST · 1.5s → badge"),
    ("THREE envelopes personified", "Bright flat", "Same bills, three personalities", "No characters — envelopes act as tie / streamers / party hat", "PAN RIGHT · 3s across envelopes"),
    ("WIDE parachute descent", "Sky light", "ONSET — steering the windfall", "Villain top-left, tiny pilot goggles, steers the note down", "DIAGONAL PAN + ZOOM IN · 3s follow drop"),
    ("SPLIT refund vs receipt", "Confetti warm vs desk lamp", "PEAK — two universes, one wallet", "Alex sweats over the €40 receipt with a magnifying glass", "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("MINIMAL two €50 notes", "Museum spot vs wheel blur", "Same currency, different rules", "Villain tiny, bottom-right, naps as museum guard", "STATIC · 2s"),
    ("DECEMBER desk scene", "Cold winter light", "COMEDOWN — nothing built", "Alex shakes the empty bag upside down", "ZOOM IN SLOW · 3s into empty bag"),
    ("CLOSE label printer", "Workshop warm", "LAPIDARIA — the brain prints labels", "Villain right side, medium, gleeful at the label printer", "PAN RIGHT · 3s along conveyor"),
    # BIAS 4 — PRESENT BIAS (25-31)
    ("FULL FRAME orange badge", "Alley vignette, cartoon-safe", "The dealer arrives", "Villain CENTER, LARGE — his big entrance", "ZOOM IN FAST · 1.5s → badge"),
    ("SPLIT vivid vs cutout", "Color vs grayscale", "Today is real, future is stock photo", "Alex vivid today; older Alex faded cardboard cutout", "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("CALENDAR glow scene", "Golden postponement light", "ONSET — the responsible-feeling high", "Alex reclines, feet up, bathed in the glow", "ZOOM IN SLOW · 3s into glowing month"),
    ("VOTING scene", "Bright vs gray corners", "PEAK — 5 today-votes vs 0", "No characters — today-figures stuff the ballot box", "SHAKE · SHORT on ballot stuff"),
    ("ENVELOPE through calendar tunnel", "Warm sender, gray receiver", "COMEDOWN — bill rides to the stranger", "No characters — vivid figure waves the bill goodbye", "DIAGONAL PAN + ZOOM IN · 4s follow envelope"),
    ("DAWN mailbox", "Cold morning blue", "The stranger is you", "Older Alex holds the accumulated envelope stack", "ZOOM IN SLOW · 4s to mailbox"),
    ("MIRROR IOU handoff", "White minimal, mirror center", "LAPIDARIA — borrowing from yourself", "Alex passes the IOU; his older reflection receives it", "ZOOM IN SLOW · 3s into mirror"),
    # CTA (32-33)
    ("STAMP-COLLECTION layout", "Clean bright", "Four badges down, six slots open", "Villain SMALL bottom-right, checks clipboard", "ZOOM IN FAST · 1s → subscribe button"),
    ("CALENDAR strip", "Neutral", "Weekly rhythm, no hard sell", "No characters — calendar strip alone", "STATIC · 3s"),
    # BIAS 5 — HERD (34-40)
    ("FULL FRAME pink badge + confetti", "Party warm", "The party drug", "Villain peeks from behind the badge, tiny party hat", "ZOOM IN FAST · 1.5s → badge"),
    ("DIAGRAM unplugged brain", "Flat white", "Decision outsourced to crowd", "Villain center, medium — replugs the decision cable into the crowd", "STATIC · 2s"),
    ("CIRCLE of glowing owners", "Warm inclusion light", "ONSET — belonging feels safe", "No characters — gap in circle invites viewer in", "ZOOM IN SLOW · 4s toward the gap"),
    ("WINDOW party vs outside", "Warm inside, cold blue out", "PEAK — fear of standing outside", "Alex stands outside looking in, steps over the ignored chart", "DIAGONAL PAN + ZOOM IN · 4s to door"),
    ("DAWN street, confetti settling", "Hangover gray-gold", "COMEDOWN — crowd moved on", "Alex holds the long receipt curling to the floor", "ZOOM OUT SLOW · 4s lonely wide"),
    ("SPLIT polaroids vs statement", "Wind vs desk lamp", "Memories vs the bill", "No characters — photos scatter; total circled red", "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("MALL full of sheep", "White mall light", "LAPIDARIA + humor — no lions here", "No characters — sheep scan for predators; janitor mops", "ZOOM OUT SLOW · 4s reveal absurd herd"),
    # BIAS 6 — LIFESTYLE INFLATION (41-47)
    ("FULL FRAME gold badge", "Pharmacy clean", "The tolerance effect", "No characters — ruler leans on badge", "ZOOM IN FAST · 1.5s → badge"),
    ("FIREWORK over calendar", "Night burst → fade", "One month of enormous", "No characters — smoke trail by month's end", "ZOOM OUT SLOW · 3s as it fades"),
    ("ESCALATOR of upgrades", "Retail bright", "ONSET — needs upgrade themselves", "Alex rides the escalator as objects upgrade around him", "PAN UP · 4s along escalator"),
    ("FUNNEL diagram", "Clinical white", "PEAK — double in, same drip out", "No characters — two paychecks pour, one coin drips", "ZOOM IN FAST · 1s → the single coin"),
    ("GAUGE dose vs effect", "Lab clean", "Tolerance in one image", "Villain right side, small, lab coat — reads the gauge", "STATIC · 3s"),
    ("WELDED needle + rising floor", "Industrial dim", "COMEDOWN denied — new baseline", "Villain mid-size EXITING frame right, pockets key", "ZOOM IN SLOW · 3s to padlock"),
    ("DUSK look-back", "Split dusk palette", "LAPIDARIA — old life unaffordable", "Alex looks back at the roped-off house", "DIAGONAL PAN + ZOOM IN · 4s past the rope"),
    # BIAS 7 — SUNK COST (48-54)
    ("FULL FRAME brown badge", "Clean white", "Loyalty program of bad decisions", "Villain bottom-left, small — stamps the loyalty card", "ZOOM IN FAST · 1.5s → badge"),
    ("TRIPTYCH dusty objects", "Dusty warm", "Still paying, long dead", "No characters — auto-payment cables still glowing", "PAN RIGHT · 4s across relics"),
    ("HOLE + dirt tower", "Overhead hard light", "ONSET — 'already put so much in'", "Alex keeps digging, knee-deep in the hole", "ZOOM OUT SLOW · 4s reveal dirt tower"),
    ("PIER of marching coins", "Dark water, green coins", "PEAK — good money after bad", "No characters — a hand waves coins off the pier", "PAN RIGHT · 3s following the march"),
    ("WALLET + ghost diagram", "Flat white", "The money already left", "No characters — money-ghost waves from the door", "STATIC · 2s"),
    ("RECEIPT staircase down", "Fog below", "COMEDOWN — years of installments", "Alex descends, dropping a coin on each step", "PAN DOWN · 4s descending steps"),
    ("TINY THEATER of the sinking", "Projector dim", "LAPIDARIA — tickets to watch it sink", "Villain SMALL at booth, background-left", "ZOOM IN SLOW · 4s to the window-screen"),
    # BIAS 8 — OPTIMISM LOOP (55-60)
    ("FULL FRAME sky badge", "Lab bright", "The lab name gag", "Villain bottom-left, small, lab goggles — holds flask + clipboard", "ZOOM IN FAST · 1.5s → badge"),
    ("HORIZON road of signposts", "Eternal golden hour", "Nine years of 'next month'", "No characters — sun never clears the horizon", "DIAGONAL PAN + ZOOM IN · 4s down the road"),
    ("MOVIE POSTER mock-up", "Spotlight glam", "ONSET — the fictional star", "Alex as the glowing caped poster hero", "ZOOM IN SLOW · 3s into poster"),
    ("WALL of twelve calendars", "Office flat", "PEAK — best month, every month", "No characters — stapler hand repeats the gold star", "PAN RIGHT · 3s along the wall"),
    ("STICKER-BURIED month", "Colorful chaos", "COMEDOWN — one-time things, always", "No characters — collision stickers bury the grid", "SHAKE · SHORT as stickers land"),
    ("SPLIT partner vs accountant", "Sunny vs desk lamp", "LAPIDARIA — great partner, bad CFO", "Alex waters a plant / Alex buried in receipts, two jobs", "STATIC · 3s"),
    # BIAS 9 — DEFAULT (61-66)
    ("FULL FRAME gray badge, dimmed", "Low light", "The silent subscription", "Villain CENTER spotlight, tiptoeing shhh", "ZOOM IN SLOW · 3s → half-asleep badge"),
    ("CIRCULAR train track", "Flat gray", "Nothing changes by itself", "No characters — cobwebbed lever untouched", "PAN RIGHT · 4s following the loop"),
    ("DARK room of self-signing", "Night, faint gray glow", "ONSET — nothing, as a substance", "Villain barely visible in the shadows behind the desk", "ZOOM IN SLOW · 4s to moving pens"),
    ("BOARDROOM toast", "Corporate cold", "PEAK — inertia priced in", "No characters — revenue bar of sleeping figures", "ZOOM IN FAST · 1.5s → the bar"),
    ("BATHTUB pinhole leak", "Bathroom neutral → reveal", "COMEDOWN — drops become ocean", "Villain tiny, corner, plumber cap — shrugs at the leak", "ZOOM OUT SLOW · 5s the big reveal"),
    ("AUCTION to empty chair", "Stark white", "LAPIDARIA — decisions never made", "No characters — gavel falls alone, sold to empty chair", "STATIC · 3s"),
    # BIAS 10 — SCARCITY (67-74)
    ("FULL FRAME navy badge, matte", "Shadowed, quiet", "Tone shift — the heavy one", "Villain CENTER-LOW, subdued, sets it down", "ZOOM IN SLOW · 3s — slower, heavier"),
    ("BOOT SCREEN kitchen", "Cold OS glow", "Scarcity as operating system", "No characters — life loads inside a loading bar", "ZOOM IN SLOW · 4s into boot logo"),
    ("CAFÉ conversation overlay", "Warm café vs ghost calculator", "ONSET — background rent math", "Alex talks with a friend, calculator overlay runs behind his eyes", "ZOOM IN SLOW · 3s to the overlay"),
    ("TWO-BRAIN comparison", "Clinical white", "Heavier than a sleepless night", "No characters — scarcity brain visibly darker", "STATIC · 3s"),
    ("TUNNEL first-person", "Single fire light", "PEAK — the tunnel stocks no future", "No characters — empty shelf hooks on tunnel walls", "ZOOM IN SLOW · 5s deeper into tunnel"),
    ("CIRCULAR tunnel diagram", "Navy on white", "Self-building loop", "No characters — decisions become tunnel bricks", "PAN RIGHT · 3s around the circle"),
    ("KITCHEN at night + child", "Low lamp, doorway shadow", "COMEDOWN — inherited gauge", "No characters — child silhouette absorbs the scene unnoticed", "ZOOM OUT SLOW · 5s to include doorway"),
    ("TIMECARD machine", "Stark industrial", "LAPIDARIA — full-time job, unpaid", "No characters — brain punches in, payslip prints zero", "ZOOM IN FAST · 1.5s → the zero"),
    # CLOSE (75-79)
    ("MOTHERBOARD grid of ten", "Clean reveal", "Full circle to the thumbnail", "Villain center — holds the badge cables like leashes", "ZOOM OUT SLOW · 5s reveal full grid"),
    ("DRAG-TO-TRASH gag", "UI clean", "Can't uninstall", "Villain small, right edge — shrugs, badge snaps back on elastic", "SHAKE · SHORT on the snap-back"),
    ("GRID under surveillance", "Spotlight snaps", "Named programs get watched", "No characters — eye icons etched on every badge", "ZOOM IN FAST · 1s → spotlight hit"),
    ("SINGLE fresh eye icon", "Max negative space", "Something new exists now", "No characters — wet-ink construction lines visible", "STATIC · 3s — quietest frame"),
    ("PHONE mid-send", "Warm friendly", "Share with the sunk-cost friend", "Alex mid-send, badge grid flies as message bubble", "ZOOM IN SLOW · 3s to the send"),
    # TEASE (80-81)
    ("SPLIT life-paths teaser", "Dawn palette", "Two people, one rule apart", "No characters — one silhouette free on hill, one on treadmill", "PAN RIGHT · 4s across the years"),
    ("NAPKIN on table", "Soft close light", "The napkin promise", "No characters — corner lifted, marks unreadable", "ZOOM IN SLOW · 3s to the napkin"),
]

assert len(PROD) == len(BEATS) == 81, f"PROD {len(PROD)} / BEATS {len(BEATS)}"


def build_pdf():
    styles = getSampleStyleSheet()
    TITLE_STYLE = ParagraphStyle('TitleS', parent=styles['Normal'], fontSize=14, leading=18,
                                  fontName='Helvetica-Bold', alignment=TA_CENTER)
    SUB_STYLE   = ParagraphStyle('SubS', parent=styles['Normal'], fontSize=10, leading=13,
                                  fontName='Helvetica-Bold', alignment=TA_CENTER,
                                  textColor=colors.HexColor('#B02A2A'))
    META_STYLE  = ParagraphStyle('MetaS', parent=styles['Normal'], fontSize=8, leading=11,
                                  alignment=TA_CENTER, textColor=colors.HexColor('#666666'))
    BEAT_NUM   = ParagraphStyle('BN', parent=styles['Normal'], fontSize=8, leading=10,
                                 fontName='Helvetica-Bold', alignment=TA_CENTER)
    NARR_BOLD  = ParagraphStyle('NB', parent=styles['Normal'], fontSize=7.5, leading=10, fontName='Helvetica-Bold')
    BODY_CELL  = ParagraphStyle('BC', parent=styles['Normal'], fontSize=7, leading=9.5)
    IMG_CELL   = ParagraphStyle('IC', parent=styles['Normal'], fontSize=6.5, leading=8.5)
    SEC_STYLE  = ParagraphStyle('SS', parent=styles['Normal'], fontSize=9, leading=12,
                                 fontName='Helvetica-Bold', textColor=colors.white, alignment=TA_CENTER)

    def esc(t):
        return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))

    pdf_path = "/home/user/Claudeeee/V16_final_PRODUCTION.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(A4),
                            leftMargin=10*mm, rightMargin=10*mm,
                            topMargin=12*mm, bottomMargin=12*mm)

    col_w = [8*mm, 40*mm, 75*mm, 30*mm, 30*mm, 28*mm, 33*mm, 33*mm]

    HDR_COLORS = {
        "BIAS 1 — ANCHORING": colors.HexColor('#2C93A8'),
        "BIAS 2 — LOSS AVERSION": colors.HexColor('#C0392B'),
        "BIAS 3 — MENTAL ACCOUNTING": colors.HexColor('#7B5FA6'),
        "BIAS 4 — PRESENT BIAS": colors.HexColor('#E8892C'),
        "CTA": colors.HexColor('#1A5C1A'),
        "BIAS 5 — HERD INSTINCT": colors.HexColor('#D9527A'),
        "BIAS 6 — LIFESTYLE INFLATION": colors.HexColor('#B8960F'),
        "BIAS 7 — SUNK COST": colors.HexColor('#8B5A2B'),
        "BIAS 8 — THE OPTIMISM LOOP": colors.HexColor('#3E7CA6'),
        "BIAS 9 — DEFAULT BIAS": colors.HexColor('#6E6E6E'),
        "BIAS 10 — SCARCITY MINDSET": colors.HexColor('#4A4A6A'),
        "CLOSE — THE CATALOG": colors.HexColor('#1A3A5C'),
        "NEXT VIDEO TEASE": colors.HexColor('#4A0E4E'),
    }

    HEADER_ROW = [Paragraph(h, BEAT_NUM) for h in
                  ['#', '<b>SEGMENT (NARRATION)</b>', '<b>IMAGE PROMPT</b>', '<b>CAMERA</b>',
                   '<b>LIGHTING</b>', '<b>MOOD / TONE</b>', '<b>CHARACTER ACTION</b>', '<b>VIDEO MOTION</b>']]

    table_data = [HEADER_ROW]
    row_styles = []
    current_row = 1

    for i, ((beat_num, section, narration, prompt_text), prod) in enumerate(zip(BEATS, PROD)):
        if beat_num in SECTION_STARTS:
            sec_name = SECTION_STARTS[beat_num]
            sec_color = HDR_COLORS.get(sec_name, colors.HexColor('#333333'))
            table_data.append([Paragraph(f'<b>■■ {esc(sec_name)} ■■</b>', SEC_STYLE)] + [''] * 7)
            row_styles.append((current_row, 'SPAN', sec_color))
            current_row += 1

        cam, light, mood, act, mot = prod
        table_data.append([
            Paragraph(str(beat_num), BEAT_NUM),
            Paragraph(f'<b>{esc(narration)}</b>', NARR_BOLD),
            Paragraph(esc(STYLE_PREAMBLE + " " + prompt_text), IMG_CELL),
            Paragraph(esc(cam), BODY_CELL),
            Paragraph(esc(light), BODY_CELL),
            Paragraph(esc(mood), BODY_CELL),
            Paragraph(esc(act), BODY_CELL),
            Paragraph(esc(mot), BODY_CELL),
        ])
        if i % 2 == 0:
            row_styles.append((current_row, 'ROWBG', colors.HexColor('#F7F7F7')))
        current_row += 1

    ts = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C2C2C')),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0, 0), (-1, 0), 8),
        ('ALIGN',      (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('GRID',       (0, 0), (-1, -1), 0.25, colors.HexColor('#CCCCCC')),
        ('LEFTPADDING',  (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING',   (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 2),
    ])
    for item in row_styles:
        r = item[0]
        if item[1] == 'SPAN':
            ts.add('SPAN', (0, r), (7, r))
            ts.add('BACKGROUND', (0, r), (7, r), item[2])
            ts.add('TEXTCOLOR', (0, r), (7, r), colors.white)
            ts.add('FONTNAME', (0, r), (7, r), 'Helvetica-Bold')
        else:
            ts.add('BACKGROUND', (0, r), (-1, r), item[2])

    table = Table(table_data, colWidths=col_w, repeatRows=1)
    table.setStyle(ts)

    flow = [
        Paragraph(SUBTITLE, SUB_STYLE), Spacer(1, 3),
        Paragraph(TITLE, TITLE_STYLE), Spacer(1, 3),
        Paragraph(META, META_STYLE), Spacer(1, 8),
        table, Spacer(1, 8),
        Paragraph('END OF PRODUCTION DOCUMENT · 81 beats · catalog format · character mix 30% Alex / 30% Villain solo / 30% no characters / 10% flexible', META_STYLE),
    ]
    doc.build(flow)
    print(f"PDF: {pdf_path}")


if __name__ == "__main__":
    build_pdf()
