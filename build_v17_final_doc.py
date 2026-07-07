#!/usr/bin/env python3
"""
VIDEO 17 — PRODUCTION DOCUMENT · COMPARATIVA (Leo vs Marc)
Tabla landscape idéntica a V13/V15/V16. 74 beats.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v17_final_image_prompts_pdf import BEATS, STYLE as STYLE_PREAMBLE

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER

TITLE    = "Two People, Same Salary: Why Only One Stops Working at 45"
SUBTITLE = "NEUROCENTS · VIDEO 17 — COMPARATIVA"
META     = "PRODUCTION DOCUMENT · 74 beats · ~933 words · ~7 min"

SECTION_STARTS = {}
_last = None
for _b in BEATS:
    if _b[1] != _last:
        SECTION_STARTS[_b[0]] = _b[1]
        _last = _b[1]

PROD = [
    # COLD OPEN (1-5)
    ("SPLIT symmetrical, both desks", "Office neutral, phones glowing", "S17 match — two lives, one email", "Both phones light at same instant", "ZOOM IN FAST · 1.5s → both screens"),
    ("DIAGRAM mirrored icon pairs", "Flat white", "Everything identical — fairness", "Icons mirror perfectly", "PAN RIGHT · 3s across pairs"),
    ("MEDIUM Marc at boss's door", "Warm morning sun", "Flash-forward — the free one", "Jacket over shoulder, relaxed exit", "ZOOM IN SLOW · 3s to doorway light"),
    ("MEDIUM Leo at night desk", "Office glow, empty floor", "The sentence he can't say", "Padlocked thought bubble fades", "ZOOM OUT SLOW · 3s — alone wide"),
    ("MACRO napkin + pen", "Single spotlight", "The promise object", "Napkin slides in, marks unreadable", "ZOOM IN SLOW · 3s to napkin"),
    # FAIR FIGHT (6-10)
    ("FIGHT-POSTER split card", "Poster dramatic, comic tone", "A fair fight nobody stages", "Identical stat bars between them", "ZOOM IN FAST · 1s → the equal bars"),
    ("TWO identical doors", "Flat daylight", "Same start, doorplate 25", "Payslips taped to both doors", "STATIC · 2s"),
    ("THREE crossed-out icons", "White void", "Excuses eliminated", "Red X lands on each icon", "ZOOM IN FAST · 1s per X"),
    ("TWIN brain outlines", "Clinical white", "Same software, same impulses", "Same gears tick in both", "STATIC · 2s"),
    ("AERIAL road fork ahead", "Long shadows", "The split hasn't happened yet", "Two silhouettes on shared path", "DIAGONAL PAN + ZOOM IN · 4s toward fork"),
    # YEAR ONE (11-14)
    ("CALENDAR day 28 + wallets", "Deadpan flat", "Both broke, identically", "Two empty wallets, same moth", "STATIC · 2s"),
    ("SPLIT slumped phone-check", "Late-night phone glow", "Mirror comedy", "Same posture, same takeaway bags", "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("PARTY scene, friend confused", "Warm party", "Indistinguishable", "Friend can't point at the right one", "ZOOM IN SLOW · 3s to twin faces"),
    ("BOTH phones + fork icon", "Notification glow", "The experiment begins", "+€200 lands; fork flickers on", "SHAKE · SHORT on notification"),
    # THE SPLIT (15-20)
    ("LEO montage of upgrades", "Warm gold", "Raises are for upgrading", "Key/plate/jacket morph upward", "PAN UP · 3s along upgrades"),
    ("LEO dinner toast", "Restaurant warm", "Earned-it energy — likable", "Glass raised, genuine smile", "ZOOM IN SLOW · 3s to the toast"),
    ("MARC unchanged kitchen", "Flat domestic", "The joke is zero change", "Same mug, same chair as year one", "STATIC · 3s — let sameness land"),
    ("MARC phone auto-transfer", "Soft screen glow", "The rule works unseen", "Transfer slides behind frosted glass", "ZOOM IN FAST · 1.5s → notification"),
    ("NAPKIN close-up readable", "Spotlight warm", "The rule, written once", "Icon-handwriting revealed", "ZOOM IN SLOW · 4s across the napkin"),
    ("CURVE graph debut", "Clean white diagram", "Two lines, still together", "20-year axis stretches ahead", "ZOOM OUT SLOW · 3s reveal full axis"),
    # YEAR FIVE (21-26)
    ("SPLIT desks + promo badges", "Office neutral", "Still identical on paper", "×2 badges, €36k payslips", "STATIC · 2s"),
    ("LEO lifestyle-ad frame", "Golden ad lighting", "He looks like the winner", "Flat, car keys, pinned weekends", "PAN RIGHT · 3s across the ad"),
    ("MARC mattress-only upgrade", "Deadpan flat", "One tagged upgrade in 5 years", "Price tag on the mattress corner", "ZOOM IN FAST · 1s → the tag"),
    ("LEO savings jar", "Dim honest light", "Leftovers, mostly", "Few coins; €4,000 card beside", "ZOOM IN SLOW · 2s to jar"),
    ("MARC €34,000 + sprout", "Fresh green accent", "First compound sprout", "Sprout grows from the number", "ZOOM IN SLOW · 3s to sprout"),
    ("WIDE applause vs invisible", "Crowd warm vs edge neutral", "Nobody claps for Marc — the point", "Marc fine at the edge, hands in pockets", "ZOOM OUT SLOW · 4s to include both"),
    # CTA (27-28)
    ("SPLIT freeze + button center", "Balanced light", "The viewer stands between them", "Subscribe button centered", "ZOOM IN FAST · 1s → button"),
    ("CALCULATOR on Thursday chip", "Minimal", "Weekly numbers ritual", "Digits scroll", "STATIC · 2s"),
    # YEAR TEN (29-32)
    ("SPLIT symmetry re-set", "Office neutral", "The constant before the reveal", "€45k payslips, subtle aging", "STATIC · 2s"),
    ("LEO social-media reel", "Feed glow", "Hearts floating — still 'ahead'", "Address plaque, car, vacations", "PAN RIGHT · 3s across posts"),
    ("CURVE first divergence", "White + green surge", "€126,000 — the curve bends", "Green line lifts off gray line", "DIAGONAL PAN + ZOOM IN · 4s along curve"),
    ("DOTTED line + eye icon", "Tension spotlight", "Something crosses here", "Zoom on unrevealed marker", "ZOOM IN SLOW · 3s to the marker"),
    # INVISIBLE LINE (33-36)
    ("ARROW comparison diagram", "Clean white", "Money out-earns the raise", "Growth arrow taller than raise arrow", "ZOOM IN FAST · 1.5s → taller arrow"),
    ("TWO payslips over Marc", "Minimal", "LAPIDARIA — two salaries", "Second payslip printed by the curve", "STATIC · 3s"),
    ("PAYSLIP working at night", "Moonlight warm humor", "The worker that never sleeps", "Tiny desk, Marc asleep behind", "ZOOM IN SLOW · 3s to tiny desk"),
    ("LEO pulling lifestyle wagon", "Strain warm", "One worker, growing load", "Rope taut, sweat drop", "PAN LEFT · 3s along the wagon"),
    # YEAR FIFTEEN (37-41)
    ("SPLIT payslips €55k", "Office neutral, older light", "Age 40 — symmetry holds", "Both faces subtly tired", "STATIC · 2s"),
    ("LEO flow diagram", "Honest clinical", "Lifestyle machine eats 54/55", "Thin trickle to €20k jar", "PAN RIGHT · 3s through the pipe"),
    ("CURVE breaks the frame", "Green dominant", "€318,000 — impolite curve", "Line exits top-right border", "DIAGONAL PAN + ZOOM IN · 4s chasing it"),
    ("PARKING LOT twin cars", "Same building shadow", "Same lot, same jobs", "Leo's car nicer, same shadow", "STATIC · 3s"),
    ("5-YEAR flip countdown", "Quiet cinematic", "Five years from never needing it", "Marc walks toward horizon door", "ZOOM IN SLOW · 4s to the door"),
    # YEAR TWENTY (42-47)
    ("FINAL symmetry frame", "Neutral", "45 years old, €62k both", "Last identical stat card", "STATIC · 2s"),
    ("€640,000 platform", "Solid green light", "The number holds his weight", "Marc stands on the number", "ZOOM OUT SLOW · 3s reveal platform"),
    ("FREEDOM definition diagram", "Clean white", "Money's salary covers life", "Arrow covers living-costs bar", "ZOOM IN FAST · 1.5s → full coverage"),
    ("MONDAY crossroads", "Sunrise", "Every Monday is a choice", "Office/mountains signs both green", "PAN RIGHT · 3s across both signs"),
    ("LEO payslip pre-sliced", "Cold fluorescent", "Nothing settles", "Slices fly off as it lands", "SHAKE · SHORT as slices scatter"),
    ("FULL final curve", "Gallery white", "Twenty years, one rule apart", "Same milestones, flat vs mountain", "ZOOM OUT SLOW · 5s full graph"),
    # NAPKIN (48-52)
    ("NAPKIN full-frame readable", "Warm document light", "The rule, in three icons", "Three-rule iconography clear", "ZOOM IN SLOW · 4s across rules"),
    ("SALARY №1 framed + auto-arrows", "Clean white", "Bank every raise, automatically", "Raise arrows curve into vault alone", "PAN RIGHT · 3s following arrows"),
    ("5-YEAR upgrade dial", "Workshop light", "On purpose vs by drift", "Hand clicks one notch; ghost-hand drifts", "ZOOM IN FAST · 1.5s → the click"),
    ("THREE crossed-out heroics", "White void", "No hustle heroics needed", "Red X on chart/clock/alarm", "ZOOM IN FAST · 1s per X"),
    ("NAPKIN paper crane lifts off", "Poetic soft", "The math flies alone", "Crane rises gently", "ZOOM OUT SLOW · 4s as it lifts"),
    # WHY BRAIN PICKS LEO (53-58)
    ("BRAIN leaning to Leo's path", "Diagram honest", "The pull, without shame", "Magnet drags brain toward glow", "ZOOM IN SLOW · 3s to the magnet"),
    ("RAISE as champagne burst", "Celebration warm", "New money reads as permission", "Notification pops the cork", "SHAKE · SHORT on the pop"),
    ("VAULT on empty stage", "Theater dim", "No applause for the right choice", "Empty chairs face the vault", "ZOOM OUT SLOW · 4s reveal empty seats"),
    ("SPLIT ledger of pleasures", "Warm vs quiet", "Both sides are REAL", "Small joys vs one silent number", "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("20 gray calendar-years", "Muted gallery", "The price: looking average", "Average-face stamp on each year", "PAN RIGHT · 4s along the years"),
    ("MIRROR vs face-down math", "Mirror light", "LAPIDARIA — mirrors beat math", "Reflection smiles as Leo", "ZOOM IN SLOW · 3s into mirror"),
    # FAIR TO LEO (59-62)
    ("LEO lovely dinner, humanized", "Genuine warm", "He didn't lose", "Real toast, zero mockery", "ZOOM IN SLOW · 3s warm close"),
    ("PHOTO WALL of real years", "Full color", "Those decades were real", "Trips, friends, wine — honest", "PAN RIGHT · 4s across photos"),
    ("WALKWAY with no OFF button", "Subtle unease", "The one crack in the plan", "Crossed-out stop button at rail", "ZOOM IN FAST · 1.5s → dead button"),
    ("CASINO chip slides", "Elegant dim", "The bet he never saw", "Chip with Leo icon onto the felt", "ZOOM IN SLOW · 3s following chip"),
    # WHICH BET (63-66)
    ("TROPHY dissolves to mirror", "Gray fade", "Wrong question retired", "'Who was right' fades out", "STATIC · 2s"),
    ("FIRST-PERSON fork", "Both paths lit", "Your two roads, right now", "Empty shoes at the start line", "DIAGONAL PAN + ZOOM IN · 4s down the fork"),
    ("CONVEYOR under the shoes", "Subtle motion light", "Standing still is choosing", "Belt drifts toward Leo's side", "PAN LEFT · 3s with the drift"),
    ("INCOMING MAIL on horizon", "Countdown glow", "The next raise is the fork", "Giant email icon approaches", "ZOOM IN SLOW · 4s toward it"),
    # CLOSE (67-71)
    ("CALM desk, drawer ajar", "Night quiet", "Nothing to redo tonight", "One drawer, one napkin inside", "ZOOM IN SLOW · 3s to drawer"),
    ("DRAWER close-up", "Soft focus", "A decision, stored", "Napkin + pen, ready", "STATIC · 2s"),
    ("EMAIL arrives + drawer opens", "Notification glow", "Decision meets moment", "Drawer slides open by itself", "ZOOM IN FAST · 1.5s → the meeting"),
    ("EQUAL silhouettes horizon", "Dusk balanced", "It was never about the men", "Napkin glows between them", "ZOOM OUT SLOW · 4s wide"),
    ("NAPKIN handed to viewer POV", "Warm final", "The napkin is yours", "Hand extends napkin to camera", "ZOOM IN SLOW · 3s to the handoff"),
    # TEASE (72-74)
    ("SEVEN cards face down", "Dark teaser", "New loop opens", "Card 4 glows in the fan", "PAN RIGHT · 3s across the fan"),
    ("SUPERMARKET freeze-frame", "Fluorescent", "You did this this week", "'4' chip beside the frozen hand", "ZOOM IN FAST · 1.5s → the chip"),
    ("THURSDAY chip on white", "Clean", "Out", "Nothing else", "STATIC · 2s"),
]

assert len(PROD) == len(BEATS) == 74, f"PROD {len(PROD)} / BEATS {len(BEATS)}"


def build_pdf():
    styles = getSampleStyleSheet()
    TITLE_STYLE = ParagraphStyle('TitleS', parent=styles['Normal'], fontSize=14, leading=18, fontName='Helvetica-Bold', alignment=TA_CENTER)
    SUB_STYLE   = ParagraphStyle('SubS', parent=styles['Normal'], fontSize=10, leading=13, fontName='Helvetica-Bold', alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'))
    META_STYLE  = ParagraphStyle('MetaS', parent=styles['Normal'], fontSize=8, leading=11, alignment=TA_CENTER, textColor=colors.HexColor('#666666'))
    BEAT_NUM   = ParagraphStyle('BN', parent=styles['Normal'], fontSize=8, leading=10, fontName='Helvetica-Bold', alignment=TA_CENTER)
    NARR_BOLD  = ParagraphStyle('NB', parent=styles['Normal'], fontSize=7.5, leading=10, fontName='Helvetica-Bold')
    BODY_CELL  = ParagraphStyle('BC', parent=styles['Normal'], fontSize=7, leading=9.5)
    IMG_CELL   = ParagraphStyle('IC', parent=styles['Normal'], fontSize=6.5, leading=8.5)
    SEC_STYLE  = ParagraphStyle('SS', parent=styles['Normal'], fontSize=9, leading=12, fontName='Helvetica-Bold', textColor=colors.white, alignment=TA_CENTER)

    def esc(t):
        return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))

    pdf_path = "/home/user/Claudeeee/V17_final_PRODUCTION.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(A4), leftMargin=10*mm, rightMargin=10*mm, topMargin=12*mm, bottomMargin=12*mm)
    col_w = [8*mm, 40*mm, 75*mm, 30*mm, 30*mm, 28*mm, 33*mm, 33*mm]

    HDR_COLORS = {
        "COLD OPEN": colors.HexColor('#1A1A2E'),
        "THE FAIR FIGHT": colors.HexColor('#2B2B8B'),
        "YEAR ONE": colors.HexColor('#7A3B00'),
        "THE SPLIT": colors.HexColor('#8B1A1A'),
        "YEAR FIVE": colors.HexColor('#7A5C00'),
        "CTA": colors.HexColor('#1A5C1A'),
        "YEAR TEN": colors.HexColor('#1A3A5C'),
        "THE INVISIBLE LINE": colors.HexColor('#1A5C3A'),
        "YEAR FIFTEEN": colors.HexColor('#4A0E4E'),
        "YEAR TWENTY": colors.HexColor('#5C0000'),
        "THE NAPKIN": colors.HexColor('#8B5A00'),
        "WHY YOUR BRAIN PICKS LEO": colors.HexColor('#6E2E6E'),
        "TO BE FAIR TO LEO": colors.HexColor('#3E7CA6'),
        "WHICH BET ARE YOU PLACING": colors.HexColor('#333333'),
        "CLOSE — THE DRAWER": colors.HexColor('#1A4A1A'),
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
            table_data.append([Paragraph(f'<b>■■ {esc(sec_name)} ■■</b>', SEC_STYLE)] + [''] * 7)
            row_styles.append((current_row, 'SPAN', HDR_COLORS.get(sec_name, colors.HexColor('#333333'))))
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
        Paragraph('END OF PRODUCTION DOCUMENT · 74 beats · Leo vs Marc · no Alex/Villain', META_STYLE),
    ]
    doc.build(flow)
    print(f"PDF: {pdf_path}")


if __name__ == "__main__":
    build_pdf()
