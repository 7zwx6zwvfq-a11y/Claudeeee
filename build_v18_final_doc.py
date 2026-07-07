#!/usr/bin/env python3
"""
VIDEO 18 — PRODUCTION DOCUMENT · SEÑALES (7 Signs)
Tabla landscape idéntica a V13/V15/V16/V17. 94 beats.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v18_final_image_prompts_pdf import BEATS, STYLE as STYLE_PREAMBLE

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER

TITLE    = "7 Signs Your Brain Is Wired to Stay Broke (Count Yours)"
SUBTITLE = "NEUROCENTS · VIDEO 18 — SEÑALES"
META     = "PRODUCTION DOCUMENT · 94 beats · ~1,078 words · ~8 min"

SECTION_STARTS = {}
_last = None
for _b in BEATS:
    if _b[1] != _last:
        SECTION_STARTS[_b[0]] = _b[1]
        _last = _b[1]

PROD = [
    # HOOK (1-9)
    ("EXTREME CLOSE eye + phone", "Screen glow, dim room", "S17 match — the flinch everyone does", "Half-closed eye braces; counter faint in corner", "ZOOM IN FAST · 1.5s → the eye"),
    ("MACRO frozen spinner", "Cold UI light", "The held-breath half-second", "Spinner frozen mid-spin", "STATIC · 2s"),
    ("MACRO fingerprint → code", "Forensic white", "Evidence, not quirk", "Print morphs into code lines", "ZOOM IN SLOW · 3s into the print"),
    ("BASEMENT server tower", "Dark, single bulb", "Installed without consent", "Unchecked 'I agree' floats", "ZOOM IN SLOW · 3s to the box"),
    ("SEVEN prints on wall", "Gallery white", "Seven fingerprints", "Prints glow one by one", "PAN RIGHT · 3s across prints"),
    ("COUNTER hero frame", "Clean spotlight", "The game board", "Seven empty boxes, waiting", "ZOOM IN SLOW · 3s to the card"),
    ("CROWD with glowing backs", "Street neutral", "Most carry three unnoticed", "Prints glow on walking backs", "PAN LEFT · 3s with the crowd"),
    ("POV hand + pen", "Warm desk", "You're playing", "Viewer's hand lifts the pen", "ZOOM IN FAST · 1s → pen grab"),
    ("BOX #1 pulse", "Warning shimmer", "Open loop — number one looms", "Top box pulses; six in shadow", "SHAKE · SHORT on pulse"),
    # SETUP (10-13)
    ("3-STEP diagram", "Flat white", "How to play", "Sign → mirror → tick", "PAN RIGHT · 2s across steps"),
    ("MAGNIFIER + crossed gavel", "Clinical", "Information, not crime", "Gavel crossed out in red", "STATIC · 2s"),
    ("QUIRK icons + price shadow", "Soft neutral", "Small things, expensive shadows", "One quirk casts a price tag", "ZOOM IN FAST · 1.5s → the shadow"),
    ("POV pen over counter", "Start-line light", "Start counting", "Pen hovers over box 1", "ZOOM IN SLOW · 2s"),
    # SIGN 7 (14-20)
    ("SIGN CARD 7 slide-in", "Card spotlight", "Sign named", "Eye-half-closed icon card", "ZOOM IN FAST · 1s → card"),
    ("3-FRAME gesture strip", "Sequence neutral", "The gesture everyone knows", "Phone → app → flinch", "PAN RIGHT · 3s across strip"),
    ("NUMBER-fist vs braced arm", "Impact dramatic", "LAPIDARIA — bracing, not checking", "Forearm guards a face", "SHAKE · SHORT on impact"),
    ("SPLIT calm eye / guarded eye", "Split light", "Control vs impact-prep", "Two ways to read a number", "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("FLASHBACK vignette", "Red balance glow", "Where the flinch was born", "Scar mark burns onto brain icon", "ZOOM IN SLOW · 3s to the scar"),
    ("ALEX braced comically", "Domestic warm", "Humor beat — first Alex", "Villain in tiny helmet inside skull", "ZOOM OUT SLOW · 3s reveal the pose"),
    ("COUNTER check #1", "Clean click light", "That's one", "Red check lands", "ZOOM IN FAST · 1s → the check"),
    # SIGN 6 (21-27)
    ("SIGN CARD 6", "Card spotlight", "Sign named", "Percent-tag icon card", "ZOOM IN FAST · 1s → card"),
    ("TAG into piggy bank", "Absurd bright", "Discount filed as income", "-50% tag deposited like a coin", "ZOOM IN SLOW · 3s to the slot"),
    ("FLIPPED receipt", "Split glow/black", "LAPIDARIA — spent seventy", "'Saved 30' flips to 'spent 70'", "SHAKE · SHORT on the flip"),
    ("BRAIN banks a feeling", "Bank neutral", "The feeling gets deposited", "Coins walk out the back door", "PAN RIGHT · 3s coins exiting"),
    ("SALE magnet uphill", "Red accent", "Sale speeds spending", "Magnet drags the cart", "DIAGONAL PAN + ZOOM IN · 3s uphill"),
    ("TROPHY case of tags", "Dusty case light", "Nobody got rich here", "Discount tags as trophies, dusty", "PAN RIGHT · 3s along the case"),
    ("COUNTER check #2", "Click light", "That's two", "Red check lands", "ZOOM IN FAST · 1s"),
    # SIGN 5 (28-34)
    ("SIGN CARD 5", "Card spotlight", "Sign named", "Round-down arrow icon card", "ZOOM IN FAST · 1s → card"),
    ("SPEECH bubble over table", "Morning-after soft", "The guess", "'20...25?' floats over the remains", "ZOOM IN SLOW · 2s to bubble"),
    ("RECEIPT under lamp", "Hard lamp light", "€38 — the correction", "Receipt unfolds sharply", "ZOOM IN FAST · 1s → the 38"),
    ("MEMORY-CLERK desk", "Office of the mind", "CFO confidence — humor", "Clerk stamps DOWN arrows", "PAN RIGHT · 3s along the desk"),
    ("ONE-WAY street sign", "Diagram flat", "Always down, never up", "Numbers flow downhill only", "STATIC · 2s"),
    ("AIRBRUSHED album", "Nostalgia warm", "LAPIDARIA — protecting the story", "Brush hovers over photos", "ZOOM IN SLOW · 3s to the brush"),
    ("COUNTER check #3", "Click light", "That's three", "Red check lands", "ZOOM IN FAST · 1s"),
    # CTA (35-36)
    ("COUNTER + subscribe", "Clean balanced", "Three ticks — the ask", "Button beside the card", "ZOOM IN FAST · 1s → button"),
    ("PATTERN into spotlight", "Dark → light pull", "The weekly ritual", "Hand drags shape into light", "ZOOM IN SLOW · 2s into the light"),
    # SIGN 4 (37-44)
    ("SIGN CARD 4", "Card spotlight", "The supermarket one", "Cart icon card", "ZOOM IN FAST · 1s → card"),
    ("CHECKOUT belt POV", "Fluorescent", "The total feels high", "Display glows slightly too bright", "ZOOM IN SLOW · 3s to display"),
    ("HAND lifts item", "Slow-motion staging", "The sacrifice begins", "Small item rises from cart", "ZOOM IN SLOW · 2s on the lift"),
    ("CHOCOLATE altar return", "Tiny altar glow", "Ritual complete — humor", "€2 bar placed back with ceremony", "STATIC · 3s — deadpan hold"),
    ("CART waves goodbye", "Cheerful fluorescent", "€60 rolls on", "Cart rolls to register happily", "PAN RIGHT · 3s with the cart"),
    ("RECEIPT feeling line", "Receipt white", "LAPIDARIA — feeling of cutting: €0", "The absurd line prints", "ZOOM IN FAST · 1.5s → the line"),
    ("PERMISSION SLIP diagram", "Clean white", "Permission, not savings", "Chocolate stamp seals the slip", "ZOOM IN SLOW · 2s to the stamp"),
    ("COUNTER check #4", "Click, slight emphasis", "That's four — it lands harder", "Red check hits", "ZOOM IN FAST · 1.5s with punch"),
    # MID REFRAME (45-48)
    ("COUNTER in trembling hand", "Soft honest", "Hold on — reframe begins", "Second hand steadies the first", "STATIC · 3s"),
    ("GLASSES lift alone", "Minimal white", "Seeing is the rare skill", "Glasses rise off the table", "ZOOM IN SLOW · 2s"),
    ("SPLIT blindfolds vs looker", "Crowd flat vs spotlight", "ALEX the one watching — identity", "Alex stopped, observing the wall", "PAN RIGHT · 3s to Alex"),
    ("COUNTER as folded map", "Cartography warm", "Sentence → map", "Checks become route markers", "ZOOM OUT SLOW · 3s reveal the map"),
    # SIGN 3 (49-55)
    ("SIGN CARD 3", "Card spotlight", "Sign named", "Countdown-clock icon card", "ZOOM IN FAST · 1s → card"),
    ("HUD payday overlay", "Crisp HUD glow", "Instant recall", "'9 days' floats over blurred kitchen", "ZOOM IN SLOW · 2s to HUD"),
    ("HUD static noise", "Glitch gray", "No signal for the year", "Fog where the total should be", "SHAKE · SHORT static burst"),
    ("TWO rulers", "Workshop flat", "Day-units vs dusty year-units", "Dust puffs off the year ruler", "PAN RIGHT · 3s ruler to ruler"),
    ("NAPKIN vs stone tablet", "Split textures", "LAPIDARIA — short vs long math", "Two equations carved side by side", "STATIC · 3s"),
    ("TWO telescopes", "Horizon dusk", "Where attention points", "Queue only at the floor-scope", "PAN LEFT · 3s between scopes"),
    ("COUNTER check #5", "Click light", "That's five", "Red check lands", "ZOOM IN FAST · 1s"),
    # SIGN 2 (56-62)
    ("SIGN CARD 2", "Card spotlight", "Sign named", "Waiting-chair icon card", "ZOOM IN FAST · 1s → card"),
    ("THREE ticketed bubbles", "Queue neutral", "The 'when' queue", "Bubbles stamped in soft gray", "PAN RIGHT · 3s along queue"),
    ("PLAN with shackled word", "Document white", "A word you don't control", "Chain leads offscreen", "ZOOM IN SLOW · 2s to the blank"),
    ("WAITING ROOM of plans", "Fluorescent stale", "LAPIDARIA — plans grow beards", "Old magazines, bearded plan", "PAN LEFT · 3s across the room"),
    ("€0 door tag", "Flat honest", "Waiting is free — that's the trap", "Brain icon pays happily", "ZOOM IN FAST · 1s → the tag"),
    ("TINY now-door vs WHEN gate", "Light vs mural", "Smaller now beats grand when", "The ajar door glows; gate is paint", "ZOOM IN SLOW · 3s to the small door"),
    ("COUNTER check #6", "Click light", "That's six", "Red check lands", "ZOOM IN FAST · 1s"),
    # SIGN 1 (63-71)
    ("SIGN CARD 1, slower", "Dimmer staging", "Tone shift — the deep one", "Low-ceiling icon card", "ZOOM IN SLOW · 2s — heavier"),
    ("EMPTY chair spotlight", "Single soft spot", "The live exercise", "Chair faces the viewer", "STATIC · 3s"),
    ("WEALTH collage settles", "Calm morning", "Not the car — the peace", "Flash dissolves to quiet table", "ZOOM IN SLOW · 3s to the table"),
    ("FRAME glitch ripple", "Subtle distortion", "Did something push back?", "The picture resists", "SHAKE · SHORT ripple"),
    ("CHILDLIKE whisper bubble", "Edge shadow", "The voice from below", "Bubble tail rises from the past", "ZOOM IN SLOW · 2s to the tail"),
    ("CHILDHOOD kitchen", "Warm-dim memory", "THE frame — where it was learned", "Child-height view of counted coins", "ZOOM IN SLOW · 5s — the longest hold"),
    ("DOORFRAME € ruler", "Household soft", "The inherited ceiling", "Marks stop at a low line", "PAN UP · 3s up the doorframe"),
    ("FRAMED photo reflection", "Gallery quiet", "LAPIDARIA — someone else's photo", "Reflection shows another silhouette", "ZOOM IN SLOW · 3s into the glass"),
    ("COUNTER check #7 full", "Heavy click", "The card is full", "Card tilts slightly, heavier", "ZOOM IN FAST · 1.5s then STATIC hold"),
    # THE COUNT (72-77)
    ("FULL counter as diagnosis", "Clinical warm", "What's your number?", "POV hand holds the card", "ZOOM IN SLOW · 3s to the card"),
    ("ZONE 0-2 shelf", "Tidy neutral", "Habits — everyone has them", "Ordinary jars, unthreatening", "PAN RIGHT · 2s along shelf"),
    ("ZONE 3-5 string board", "Conspiracy warm", "A program that thinks it protects", "Red string + tiny shield center", "ZOOM OUT SLOW · 3s reveal the web"),
    ("ZONE 6-7 cockpit", "Autopilot glow", "Meeting the pilot", "Child's drawing on the controls; seat turns", "ZOOM IN SLOW · 4s to the turning seat"),
    ("COMMENT box mock", "UI clean", "Comment-engine — drop your number", "'?/7' field glows among fingerprints", "ZOOM IN FAST · 1s → the field"),
    ("BRAIN reaches DELETE", "Corner tension", "Bridge — caught mid-reach", "Hand frozen over the key", "SHAKE · SHORT freeze"),
    # DELETE ATTEMPT (78-82)
    ("THOUGHT half-formed", "Dark soft", "Something is forming", "Bubble materializes slowly", "ZOOM IN SLOW · 2s"),
    ("'INTERESTING' stamp", "Bureaucratic flat", "Calm. Friendly. Final.", "The seal presses down", "SHAKE · SHORT on the press"),
    ("ARCHIVE to furnace", "Industrial dim", "LAPIDARIA — where threats are forgotten", "Boxes wheeled toward moon-furnace", "PAN RIGHT · 3s with the trolley"),
    ("SECURITY monitor alert", "Red monitor glow", "The programs defend themselves", "Counter flagged as threat", "ZOOM IN FAST · 1.5s → the alert"),
    ("STAMP over this video", "Fourth-wall glow", "Scheduled for tonight", "Stamp hovers over the thumbnail mock", "ZOOM IN SLOW · 2s — hold the threat"),
    # CLOSE (83-90)
    ("ASH except the counter", "Ember dim", "What survives", "Card stays solid in the ash", "ZOOM IN SLOW · 3s to the card"),
    ("TOMORROW triptych", "Everyday light", "You'll catch yourself mid-sign", "Ghost checks hover at each scene", "PAN RIGHT · 4s across the three"),
    ("THE CATCH freeze", "High-speed photo", "The half-second that matters", "Hand catches the falling card", "STATIC · 3s — frozen catch"),
    ("BINDER/SCROLL crossed, hand glows", "Minimal", "Not budgets. The catch.", "Two X's and one glow", "ZOOM IN FAST · 1s → the hand"),
    ("SOFT warning triangle", "Gentle amber", "Don't punish the catch", "Whip icon crossed out", "STATIC · 2s"),
    ("FEEDING bowl swap", "Fable warm", "LAPIDARIA — shame feeds them", "Shame bowl out, curiosity lens in", "PAN LEFT · 3s the swap"),
    ("INVENTORY fan + open eye", "Clean display", "What you own now", "Seven cards + counter + eye", "ZOOM OUT SLOW · 3s reveal all"),
    ("SUNRISE flag counter", "Warm dawn", "The whole beginning", "Card planted like a flag", "ZOOM OUT SLOW · 4s wide dawn"),
    # TEASE (91-94)
    ("PHONE mid-send", "Warm friendly", "Send it to the #4 friend", "Counter flies as message", "ZOOM IN SLOW · 2s to send"),
    ("MONEY archaeology strip", "Museum light", "The year money stopped hurting", "Coins → paper → card → tap fade", "PAN RIGHT · 4s along the strip"),
    ("COIN relic vs glowing number", "Split warm/cold", "Bookends of the story", "Hand flinches at the number behind", "ZOOM IN SLOW · 3s to the coin"),
    ("THURSDAY chip", "Clean white", "Out", "Nothing else", "STATIC · 2s"),
]

assert len(PROD) == len(BEATS) == 94, f"PROD {len(PROD)} / BEATS {len(BEATS)}"


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

    pdf_path = "/home/user/Claudeeee/V18_final_PRODUCTION.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(A4), leftMargin=10*mm, rightMargin=10*mm, topMargin=12*mm, bottomMargin=12*mm)
    col_w = [8*mm, 40*mm, 75*mm, 30*mm, 30*mm, 28*mm, 33*mm, 33*mm]

    palette = [colors.HexColor(c) for c in
               ['#1A1A2E', '#2B2B8B', '#7A3B00', '#8B1A1A', '#7A5C00', '#1A5C1A', '#1A3A5C',
                '#6E2E6E', '#8B5A00', '#4A0E4E', '#5C0000', '#333333', '#1A5C3A', '#1A4A1A', '#4A0E4E']]
    HDR_COLORS = {}
    for idx, sec in enumerate(dict.fromkeys(b[1] for b in BEATS)):
        HDR_COLORS[sec] = palette[idx % len(palette)]

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
        Paragraph('END OF PRODUCTION DOCUMENT · 94 beats · counter motif · Alex minimal', META_STYLE),
    ]
    doc.build(flow)
    print(f"PDF: {pdf_path}")


if __name__ == "__main__":
    build_pdf()
