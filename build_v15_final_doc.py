#!/usr/bin/env python3
"""
VIDEO 15 — PRODUCTION DOCUMENT · BRIEF v3.1
NEUROCENTS · 94 beats · ~1,011 words · ~7.5 min
Table format: # | SEGMENT | IMAGE PROMPT | CAMERA | LIGHTING | MOOD/TONE | CHARACTER ACTION | VIDEO MOTION
Matches V13/V10 production document format exactly.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v15_final_image_prompts_pdf import BEATS, STYLE as STYLE_PREAMBLE

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                 Paragraph, Spacer, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

TITLE    = "Why Smart People Can't Save Money (Do This Once Instead)"
SUBTITLE = "NEUROCENTS · VIDEO 15 — BRIEF v3.1"
META     = "PRODUCTION DOCUMENT · 94 beats · ~1,011 words · ~7.5 min"

# Beat number → section header (derived from BEATS section field)
SECTION_STARTS = {}
_last = None
for _b in BEATS:
    if _b[1] != _last:
        SECTION_STARTS[_b[0]] = _b[1]
        _last = _b[1]

# Production values: (camera, lighting, mood, char_action, video_motion) — one per beat, 94 total
PROD = [
    # ── HOOK beats 1-10 ──
    ("MEDIUM CLOSE-UP, slight low angle — phone + books visible",
     "Warm desk lamp, evidence of study everywhere",
     "Dissonance — smart and broke in one frame. S17 match in <5 sec",
     "Alex holds phone with €140, eyes wide, eyebrows raised — the contradiction lands",
     "ZOOM IN FAST · 1.5s → onto the €140 balance"),
    ("MEDIUM SHOT, dinner party scene",
     "Warm social evening light",
     "Fluency — he knows the theory cold",
     "Alex mid-gesture explaining, guests impressed, Villain bored inside skull",
     "PAN RIGHT · 3s across the dinner table to Alex"),
    ("EXTREME CLOSE-UP on phone screen",
     "Cold screen glow, books faintly reflected",
     "The receipt — theory meets balance",
     "No character motion — the €140 is the actor",
     "STATIC · 2s — let the number sit"),
    ("MEDIUM SHOT, 6 AM discipline scene",
     "Early morning blue-grey",
     "Elimination — discipline was never the problem",
     "Alex with gym bag + checked to-do list, Villain shrugs",
     "PAN RIGHT · 3s following Alex's stride"),
    ("MEDIUM SHOT, single spotlight on crank",
     "White void, hard spotlight — theatrical",
     "THE TWIST — effort itself is the trap",
     "Alex strains at manual crank, sweating, meter barely moves",
     "ZOOM IN SLOW · 4s — into the straining grip"),
    ("SPLIT PANEL, mirror composition",
     "Left: warm effort tones. Right: cool green automation",
     "The asymmetry named — manual vs automatic",
     "Left Alex cranks exhausted; right machine hums alone",
     "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("WIDE SHOT, five arms vs one man",
     "Flat clinical white",
     "Unfair by design — five machines, one human",
     "Five mechanical arms reach for coins; Alex raises small wooden shield",
     "ZOOM OUT SLOW · 4s — reveal all five arms"),
    ("EXTRA WIDE, Alex tiny in frame",
     "Same clinical white, colder",
     "Scale of the mismatch — arithmetic, not drama",
     "Alex tiny, shield smaller from distance, arms in coordinated rhythm",
     "ZOOM OUT SLOW · 4s — keep pulling back"),
    ("CENTER COMPOSITION, single switch",
     "Soft warm morning light — visual reset",
     "Calm promise — the opposite energy of beats 7-8",
     "Alex's hand hovers over large green toggle; Villain leans forward alarmed",
     "ZOOM IN SLOW · 4s — toward the switch"),
    ("EXTREME CLOSE-UP on skull interior",
     "Warm amber skull glow",
     "Open loop — the objections are coming, and we know it",
     "Villain writes objection list fast on clipboard; Alex outside calm half-smile",
     "ZOOM IN FAST · 1.5s → onto the clipboard"),

    # ── WHY THE COMMON SOLUTION FAILS beats 11-20 ──
    ("MEDIUM SHOT, desk drawer opening",
     "Domestic warm, dust motes",
     "Museum of good intentions",
     "Alex opens drawer of abandoned methods, surveys the graveyard",
     "PAN DOWN · 3s into the drawer contents"),
    ("CLOSE-UP on phone, app pristine",
     "Fresh January light, optimistic",
     "New-year optimism — this time it's different",
     "Alex's finger taps color-coded app, expression hopeful",
     "ZOOM IN SLOW · 3s — into the perfect categories"),
    ("MEDIUM SHOT, calendar with abrupt stop",
     "Neutral flat",
     "The quiet fade begins — day 19, no drama",
     "No character — checked days 1-19, blank from 20. Dust on app icon",
     "PAN RIGHT · 3s across the calendar to the blank days"),
    ("MEDIUM SHOT, March calendar",
     "Neutral flat, slightly colder",
     "Second failure, same shape",
     "Alex looks away from calendar; shopping bag icon on day 13",
     "ZOOM IN FAST · 1s → onto day 12-13 transition"),
    ("MEDIUM SHOT, laptop + proud Alex",
     "Warm screen glow",
     "Peak spreadsheet pride — his best work",
     "Alex arms crossed beside immaculate 50/30/20 pie chart",
     "ZOOM IN SLOW · 3s — into the beautiful spreadsheet"),
    ("SPLIT PANEL, spreadsheet vs statement",
     "Left: clean glow. Right: messy red entries",
     "Theory vs reality — the gap is the story",
     "Alex looks left-right between panels, deflating",
     "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("WIDE SHOT, three icons dissolving",
     "White, progressively washed out left to right",
     "The quiet fade made visible — no crash, just entropy",
     "Alex watches app/calendar/spreadsheet icons fade to transparent",
     "PAN RIGHT · 4s following the dissolve"),
    ("MEDIUM SHOT, fault-line diagram",
     "Clinical white",
     "Pattern diagnosis — one flaw, three casualties",
     "Red crack runs beneath all three faded icons, connecting them",
     "ZOOM IN SLOW · 3s — along the crack"),
    ("WIDE SHOT, infinite door corridor",
     "Vanishing-point perspective, flat light",
     "The real enemy revealed: forever",
     "Alex at corridor start, shoulders dropping as he sees no end",
     "DIAGONAL PAN + ZOOM IN · 4s — down the endless corridor"),
    ("CENTER, giant counter '150'",
     "Hard spotlight on the number",
     "The impossible scoreboard — perfection required",
     "Alex exhausted reading REQUIRED: 150/150; Villain grins — needs one miss",
     "ZOOM IN FAST · 1.5s → onto the 150"),

    # ── THE MECHANISM beats 21-36 ──
    ("MEDIUM SHOT, shop counter refusal",
     "Neutral shop light",
     "The tiny reward of no",
     "Alex polite 'no' gesture; single coin drops into near-empty jar",
     "ZOOM IN SLOW · 3s — onto the single coin"),
    ("MEDIUM SHOT, scoreboard at zero",
     "Clinical white",
     "The game doesn't count defense",
     "Alex points from pile of green checkmarks to the zero, confused",
     "STATIC · 2s"),
    ("WIDE SHOT, domino line",
     "White, red accent on final domino, 11 PM clock",
     "The brutal math — one yes beats thirty nos",
     "Thirty green dominoes stand; one red domino falls and flattens the line",
     "PAN RIGHT · 3s following the collapse"),
    ("MEDIUM SHOT, five dim slots return",
     "Dim recall lighting — memory palette",
     "V14 continuity — the drains re-enter",
     "Alex turns with recognition; Villain straightens proudly",
     "ZOOM IN SLOW · 3s — toward the familiar slots"),
    ("WIDE SHOT, five slots lighting in sequence",
     "Sequential pulse highlights",
     "Naming — the viewer names them along",
     "Each slot pulses as named: CARD GAP → PRE-SPEND",
     "ZOOM IN FAST · 0.5s per slot — five rapid hits"),
    ("MEDIUM SHOT, video card + gear detail",
     "Neutral white",
     "Cold-viewer rescue + the detail that matters",
     "Alex points past V14 thumbnail card to glowing gear icon",
     "ZOOM IN FAST · 1s → onto the gear"),
    ("WIDE SHOT, machine room",
     "Industrial green glow under each slot",
     "Automation exposed — nobody is operating these",
     "Five gears spin under five slots; three counters read ZERO",
     "PAN RIGHT · 4s across the machine room"),
    ("WIDE SHOT, night shift scene",
     "Dark night blues, faint gear glow, SATURDAY tag",
     "The drains never sleep",
     "Alex asleep peaceful; gears keep spinning in the dark",
     "ZOOM OUT SLOW · 4s — from sleeping Alex to working gears"),
    ("SPLIT PANEL, gears vs paper list",
     "Left: solid industrial. Right: curling paper on corkboard",
     "THE frame of the video — machine vs to-do list",
     "Five interlocked gears face one unchecked 'save money' checkbox",
     "PAN LEFT · 2s then PAN RIGHT · 2s"),
    ("MEDIUM SHOT, the shredding",
     "Neutral — mechanical, not violent",
     "Inevitability — this happens to every list",
     "Gears shred the paper list; Alex watches, hands in pockets",
     "ZOOM IN SLOW · 3s — into the shredder teeth"),
    ("CENTER, balance scale diagram",
     "Clean clinical white",
     "Elevation — arithmetic, not character",
     "Gear icon outweighs checklist icon on balance scale",
     "STATIC · 2s — let the equation land"),
    ("MEDIUM SHOT, graduation cap by the shreds",
     "Neutral white",
     "Title payoff — smart doesn't move the gears",
     "Alex in grad cap beside shredded list; Villain taps gear approvingly",
     "ZOOM IN FAST · 1.5s → onto the cap + shreds"),
    ("SPLIT METERS, quality vs count",
     "Green dial left, red counter right",
     "The insight — quality turns, quantity doesn't",
     "Alex turns QUALITY dial up; COUNT stays locked at 150",
     "ZOOM IN SLOW · 3s — onto the locked 150"),
    ("WIDE SHOT, night highway",
     "Dark road, headlights, fatigue gauge dropping",
     "Analogy — the cap doesn't refill the tank",
     "Capped driver silhouette drives; fatigue meter drains toward empty",
     "PAN RIGHT · 4s following the car down the road"),
    ("MEDIUM SHOT, question card rejected",
     "Clean white",
     "Wrong question dismissed",
     "Alex swipes aside the crossed-out 'better decisions' card",
     "ZOOM IN FAST · 1s → on the red X stamp"),
    ("CENTER, counter rolling to zero",
     "White with green glow growing as digits fall",
     "Hope enters — the right question has an answer",
     "Counter rolls 150→0; Alex hopeful; Villain alarmed for the first time",
     "ZOOM IN SLOW · 4s — into the rolling digits"),

    # ── CTA beats 37-38 ──
    ("DIRECT ADDRESS, medium close-up",
     "Clean warm, personal",
     "Complicity — the viewer is seen",
     "Alex direct eye contact; Villain peeks defensively; subscribe button below",
     "ZOOM IN SLOW · 3s — toward Alex's gaze"),
    ("MEDIUM SHOT, weekly calendar",
     "Clean neutral",
     "Understated value — rhythm, not hype",
     "Brain icon appears week after week; Alex nods once and turns back",
     "STATIC · 3s"),

    # ── MECHANISM CONCLUSION beats 39-41 ──
    ("MEDIUM SHOT, releasing the crank",
     "Spotlight softening — tension leaving the frame",
     "The scandalous pivot — letting go as strategy",
     "Alex releases crank, shakes out hands — relief, not defeat; Villain confused",
     "ZOOM OUT SLOW · 4s — as the grip releases"),
    ("CLOSE-UP, drawer closing",
     "Domestic warm, final",
     "Closure without nostalgia",
     "Alex's hand calmly closes the drawer of dead methods",
     "PAN DOWN · 2s with the closing drawer"),
    ("MEDIUM SHOT, curtain tease",
     "Green glow leaking from behind curtain",
     "Maximum curiosity gap",
     "Alex's hand on curtain edge; Villain pressed against skull glass to see",
     "ZOOM IN SLOW · 3s — toward the glow"),

    # ── THE DECISION beats 42-58 ──
    ("CENTER, switch alone on white",
     "Pure white, single soft shadow",
     "Reveal — two words, one object",
     "The green toggle switch, large, centered, untouched",
     "ZOOM IN FAST · 1.5s → onto the switch"),
    ("DIAGRAM, split-at-arrival",
     "Morning palette, green arrows",
     "The mechanism in one motion — split at hour zero",
     "Salary arrow arrives; second arrow splits off instantly to separate box",
     "DIAGONAL PAN + ZOOM IN · 4s — following the split arrow"),
    ("WIDE SHOT, bedroom at dawn",
     "Pre-dawn blues, phone glow on nightstand",
     "The transfer needs no witness",
     "Alex asleep, Villain asleep, phone confirms transfer alone",
     "ZOOM IN SLOW · 4s — toward the glowing confirmation"),
    ("MEDIUM SHOT, Sunday sofa setup",
     "Soft weekend light, plant, coffee",
     "The entire cost of the system: ten calm minutes",
     "Alex taps through standing-order setup, relaxed; '10 MIN' clock icon",
     "STATIC · 3s — calm is the message"),
    ("CLOSE-UP, torn calendar",
     "Neutral with dark-humor flatness",
     "Dark joke — the end of the month doesn't exist",
     "Days 25-31 torn away; empty wallet icon at the ragged edge; Alex shrugs",
     "ZOOM IN FAST · 1s → onto the torn edge"),
    ("CENTER, clock at first light",
     "Dawn gradient — first light through window",
     "Precision — hour zero beats everything awake",
     "Green transfer arrow fires across frame at the exact moment",
     "ZOOM IN FAST · 1.5s → with the firing arrow"),
    ("DIAGRAM, island vault",
     "Clean white diagram, moat blue",
     "Deliberate remoteness — the money's new home",
     "Second bank on island; scissors cut the card above it",
     "ZOOM OUT SLOW · 4s — reveal moat and island"),
    ("NIGHT SCENE, 11 PM at the moat",
     "Dark, phone-glow on tired face",
     "Designed friction wins at the weakest hour",
     "Tired Alex sees drawbridge up, two locks, 3-day hourglass — gives up, goes to bed",
     "ZOOM IN SLOW · 4s — toward the raised drawbridge"),
    ("MEDIUM SHOT, modest amount cards",
     "Clean white, green accents",
     "Sustainable beats impressive",
     "Alex points at €100/€50 cards; oversized €800 card crossed out",
     "ZOOM IN FAST · 1s → onto the small green cards"),
    ("DIAGRAM, repeating stamp",
     "Clean white, rhythmic green marks",
     "Repetition is the hero, not the amount",
     "Gear stamps identical transfer marks across months; small up-arrow on amount",
     "PAN RIGHT · 4s across the repeating months"),
    ("WIDE SHOT, showdown framing",
     "Dramatic split: five slots right, one arrow left",
     "The rematch — but this time both sides are automatic",
     "Green transfer arrow approaches the five drain slots; Villain grips skull glass",
     "ZOOM IN SLOW · 4s — arrow advancing on the slots"),
    ("MEDIUM SHOT, card taps nothing",
     "Neutral shop light, empty account section visible",
     "Drain 5 down — nothing to tap against",
     "Card taps empty section; money already on the island; CARD GAP slot dims",
     "ZOOM IN FAST · 1s → on the failed tap"),
    ("CLOSE-UP, recalculating Villain",
     "Warm amber skull glow",
     "Drain 4 down — the math shrinks with the visible balance",
     "Villain shakes calculator; 'deserved' result smaller; REWARD DRAIN dims",
     "ZOOM IN FAST · 1.5s → onto the shrinking result"),
    ("DIAGRAM, siphon on leftovers",
     "Neutral, vault locked behind moat",
     "Drain 3 contained, not killed — honesty beat",
     "Subscription siphon draws from leftovers pool; vault untouched; slot half-dims",
     "ZOOM IN SLOW · 3s — from siphon to locked vault"),
    ("MEDIUM SHOT, ghosts see nothing",
     "Cool ghost translucency over bank app",
     "Drain 2 down — no audience for an invisible account",
     "Ghost audience peers at app, vault absent from screen, ghosts shrug and fade",
     "ZOOM OUT SLOW · 3s — as the ghosts fade"),
    ("CLOSE-UP, Villain still allocating",
     "Warm amber, smaller pool visible",
     "Drain 1 survives — the twist before the checkmate",
     "Villain keeps allocating a visibly smaller pool; PRE-SPEND flickers but stays lit",
     "STATIC · 3s — the machine still runs"),
    ("WIDE DIAGRAM, the flag planted first",
     "Clean white, single green flag, maximum space",
     "CHECKMATE FRAME — you got there first",
     "Alex's transfer flag stands BEFORE Villain's spike on the timeline; Villain arrives late, caught",
     "DIAGONAL PAN + ZOOM IN · 5s — from Villain's late arrival back to the planted flag"),

    # ── THE SCIENCE beats 59-70 ──
    ("WIDE SHOT, replication pillar",
     "Clean academic white",
     "Authority — a law, not a hack",
     "Identical study icons stack into a solid pillar",
     "PAN UP · 4s climbing the pillar"),
    ("CENTER, institutional card",
     "Clean white, bold black type",
     "Name — institution — year",
     "'MADRIAN & SHEA / HARVARD / 2001' card with toggle icon",
     "ZOOM IN FAST · 1s → onto the card"),
    ("DIAGRAM, one building one switch",
     "Minimal white",
     "One variable changed — clean experiment",
     "Office building icon; single switch flips beside it",
     "STATIC · 2s"),
    ("DIAGRAM, obstacle course to enroll",
     "Neutral, hurdles in grey",
     "Before — effort guards the door",
     "Employee silhouettes face form/meeting/signature hurdles; some turn back",
     "PAN RIGHT · 3s along the obstacle path"),
    ("BAR CHART, 37%",
     "Grey-blue modest bar",
     "Number 1 — the before state",
     "Bar rises to 37%; four of ten silhouettes highlighted",
     "ZOOM IN SLOW · 3s — as the bar rises"),
    ("DIAGRAM, open-door default",
     "Warmer, door open, path clear",
     "After — the hurdles moved to the exit",
     "Employees walk straight through open door; one exit form off to the side",
     "PAN RIGHT · 3s through the open door"),
    ("BAR CHART, 86% beside 37%",
     "Tall green bar, stark gap",
     "Number 2 — the entire story in one gap",
     "86% bar towers beside 37%; nine of ten silhouettes highlighted",
     "ZOOM IN FAST · 1.5s → onto the 86%"),
    ("BAR CHART with crossed-out suspects",
     "Same chart, three X'd icons above",
     "Elimination — no raise, no bonus, no seminar",
     "Money bag, gift, podium icons each get red X",
     "ZOOM IN FAST · 1s per X — three rapid hits"),
    ("DIAGRAM, identical rows of people",
     "Flat clinical white",
     "The people were the constant",
     "Same silhouettes before/after, '=' between rows",
     "PAN DOWN · 3s from row to row"),
    ("DIAGRAM, loop compressed to dot",
     "White, spiral to single point",
     "The compression — forever becomes once",
     "Infinite payday loop collapses into a single checkmarked dot",
     "ZOOM IN SLOW · 4s — into the single dot"),
    ("WORLD MAP, switches lighting",
     "Flat map, green dots spreading",
     "Universality — same result everywhere",
     "Toggle dots light up across countries one by one",
     "PAN RIGHT · 4s across the lighting map"),
    ("MIRRORED DIAGRAM, plan vs transfer",
     "Clean white, equals sign center",
     "The bridge — copy the mechanism at home",
     "Company switch and Alex's home switch mirrored; his hand on his own",
     "ZOOM IN SLOW · 3s — onto Alex's switch"),

    # ── BRAIN VILLAIN'S LAST TRICK beats 71-81 ──
    ("CLOSE-UP on skull, finger raised",
     "Warm amber skull glow",
     "The counter is prepared",
     "Villain arms crossed, one finger up, clipboard from Beat 10 in hand",
     "ZOOM IN SLOW · 3s — into the Villain's expression"),
    ("DIRECT ADDRESS, double gaze",
     "Warm personal light",
     "Fourth wall — both of them see you",
     "Alex and Villain look at viewer simultaneously",
     "STATIC · 3s"),
    ("CLOSE-UP, Villain in armchair",
     "Soft, nothing alarming",
     "The resistance looks sensible",
     "Villain seated calmly, hands folded, reasonable posture",
     "ZOOM IN SLOW · 3s — into the calm"),
    ("CLOSE-UP, the prudence bubble",
     "Soft warm — comfort of the excuse",
     "The objection lands — it sounds wise",
     "'WHAT IF I NEED THAT MONEY?' bubble; Villain open-palm gestures at it",
     "ZOOM IN FAST · 1.5s → onto the bubble text"),
    ("MEDIUM SHOT, reclassification",
     "Cooling light as the stamp lands",
     "The disguises drop",
     "Red border stamps the bubble; shield/map/spring icons fall away crossed out",
     "ZOOM IN FAST · 1s → on the red border stamp"),
    ("MEDIUM SHOT, Villain in costume",
     "Deceptive warm — looks wise, isn't",
     "Unmasking — the Pre-Spend in a shawl",
     "Villain in glasses+shawl costume; PRE-SPEND slot glows behind it",
     "STATIC · 3s — the metaphor lands"),
    ("WIDE SHOT, NOT BROKEN banner",
     "Warm amber, neutral truce",
     "Reframe begins — fact, not fight",
     "Control panel with banner; Alex nods in agreement outside",
     "ZOOM IN SLOW · 4s — into the panel"),
    ("WIDE SHOT, ancestral cave",
     "Warm firelight, snow at cave mouth",
     "Origin — the program was correct once",
     "Ancestor-Alex keeps food stacked within arm's reach by the fire",
     "PAN RIGHT · 4s across the cave scene"),
    ("MEDIUM SHOT, absurd locked chest",
     "Cold snow blues vs warm fire",
     "The instinct was right, in that world",
     "Ancestor stares bewildered at locked chest out in the snow",
     "ZOOM IN SLOW · 3s — toward the absurd chest"),
    ("SPLIT PANEL, cave vs apartment",
     "Warm prehistoric left, cool modern right",
     "The mismatch — same program, wrong era",
     "Villain content by fire left; lost among one-click icons right",
     "PAN LEFT · 3s then PAN RIGHT · 3s"),
    ("DARK ROOM, 11 PM phone glow",
     "Phone glow only, TUESDAY tag",
     "The modern predator revealed — it's you, tonight",
     "Alex's thumb hovers over BUY; island vault safe in background",
     "ZOOM IN SLOW · 4s — toward the glowing thumb"),

    # ── IDENTITY CLOSE beats 82-89 ──
    ("CENTER, label peeling off",
     "Clean white, warm",
     "Correction, not pep talk",
     "Faded 'bad with money' tag peels off Alex's chest and drifts away",
     "ZOOM IN SLOW · 3s — as the label detaches"),
    ("WIDE SHOT, rigged chessboard",
     "Neutral, gears glinting on opponent side",
     "It was never about skill",
     "Alex moves one piece by hand; five opponent pieces move themselves",
     "PAN RIGHT · 3s across the board"),
    ("CENTER, cap vs battery scale",
     "Clinical white",
     "The variable that always decided",
     "Graduation cap vs near-empty battery; battery side heavier",
     "STATIC · 2s"),
    ("MEDIUM SHOT, quiet switch ON",
     "Calm domestic warm",
     "The system needs nothing from you",
     "Green toggle ON in corner; flame/face/MON icons drift away unneeded",
     "ZOOM OUT SLOW · 3s — the switch small and steady"),
    ("TRIPTYCH, three unconditional fires",
     "Sleep blues / bad-day grey / pure white",
     "Zero conditions — it just runs",
     "Arrow fires while asleep, on worst day, and alone in empty frame",
     "PAN RIGHT · 4s across the three panels"),
    ("MEDIUM SHOT, six months later",
     "Warm progression light",
     "Time-lapse to the payoff",
     "Calendar pages flip; Alex opens vault app; green bar has grown",
     "ZOOM IN SLOW · 4s — toward the grown balance"),
    ("EXTREME CLOSE-UP, the plain number",
     "Flat, no celebration graphics",
     "Not pride. Evidence. Restraint IS the emotion",
     "Just the account screen with a solid grown number",
     "STATIC · 3s — hold on the fact"),
    ("MEDIUM SHOT, roommates at peace",
     "Warm resolved light",
     "The enemy reframed — bypassed, not defeated",
     "Alex and Villain look at balance together; Villain gives grudging shrug",
     "ZOOM OUT SLOW · 4s — both in frame, at peace"),

    # ── NEXT VIDEO TEASE beats 90-94 ──
    ("WIDE SHOT, seven mystery cards",
     "Dark cards on white, spotlights",
     "New loop opens — the signs",
     "Seven '?' cards in a row; Villain eyes them nervously",
     "PAN RIGHT · 3s across the seven cards"),
    ("CLOSE-UP, magnifying glass",
     "Neutral with red glow under lens",
     "Invisible until magnified",
     "Lens over ordinary gesture reveals faint red pattern; Alex unaware",
     "ZOOM IN SLOW · 3s — through the lens"),
    ("MEDIUM SHOT, supermarket freeze-frame",
     "Supermarket fluorescent",
     "Implication — you did this one this week",
     "Alex frozen mid-reach at shelf; card #4 glows beside the gesture, still '?'",
     "ZOOM IN FAST · 1.5s → onto card #4"),
    ("CLOSE-UP, checklist warning",
     "White, three warning-red checks",
     "The viewer counts their own",
     "Three of seven rows glow red-checked; Alex looks from list to viewer",
     "ZOOM IN FAST · 1s → onto the third checkmark"),
    ("MEDIUM SHOT, closing pose",
     "Warm resolved, THURSDAY on wall",
     "Release with the loop held open",
     "Alex relaxed knowing smile; Villain calm; Thursday visible",
     "ZOOM OUT SLOW · 4s — final pull back"),
]

assert len(PROD) == 94, f"PROD has {len(PROD)} entries, expected 94"
assert len(BEATS) == 94, f"BEATS has {len(BEATS)} entries, expected 94"


def build_pdf():
    styles = getSampleStyleSheet()

    TITLE_STYLE = ParagraphStyle('TitleS', parent=styles['Normal'],
                                  fontSize=14, leading=18,
                                  fontName='Helvetica-Bold', alignment=TA_CENTER)
    SUB_STYLE   = ParagraphStyle('SubS', parent=styles['Normal'],
                                  fontSize=10, leading=13,
                                  fontName='Helvetica-Bold', alignment=TA_CENTER,
                                  textColor=colors.HexColor('#B02A2A'))
    META_STYLE  = ParagraphStyle('MetaS', parent=styles['Normal'],
                                  fontSize=8, leading=11,
                                  alignment=TA_CENTER,
                                  textColor=colors.HexColor('#666666'))

    BEAT_NUM   = ParagraphStyle('BN', parent=styles['Normal'],
                                 fontSize=8, leading=10, fontName='Helvetica-Bold',
                                 alignment=TA_CENTER)
    NARR_BOLD  = ParagraphStyle('NB', parent=styles['Normal'],
                                 fontSize=7.5, leading=10, fontName='Helvetica-Bold')
    BODY_CELL  = ParagraphStyle('BC', parent=styles['Normal'],
                                 fontSize=7, leading=9.5)
    IMG_CELL   = ParagraphStyle('IC', parent=styles['Normal'],
                                 fontSize=6.5, leading=8.5)
    SEC_STYLE  = ParagraphStyle('SS', parent=styles['Normal'],
                                 fontSize=9, leading=12, fontName='Helvetica-Bold',
                                 textColor=colors.white, alignment=TA_CENTER)

    def esc(t):
        return (t.replace('&', '&amp;')
                  .replace('<', '&lt;')
                  .replace('>', '&gt;')
                  .replace('"', '&quot;'))

    def img_prompt(beat_num, scene_specific):
        return STYLE_PREAMBLE + " " + scene_specific

    pdf_path = "/home/user/Claudeeee/V15_final_PRODUCTION.pdf"
    page = landscape(A4)
    doc = SimpleDocTemplate(pdf_path, pagesize=page,
                            leftMargin=10*mm, rightMargin=10*mm,
                            topMargin=12*mm, bottomMargin=12*mm)

    col_w = [8*mm, 40*mm, 75*mm, 30*mm, 30*mm, 28*mm, 33*mm, 33*mm]

    HDR_COLORS = {
        "HOOK — PRIMEROS 5 SEGUNDOS": colors.HexColor('#1A1A2E'),
        "WHY THE COMMON SOLUTION FAILS": colors.HexColor('#8B1A1A'),
        "THE MECHANISM": colors.HexColor('#7A3B00'),
        "CTA": colors.HexColor('#1A5C1A'),
        "MECHANISM CONCLUSION": colors.HexColor('#2B2B8B'),
        "THE DECISION": colors.HexColor('#1A5C3A'),
        "THE SCIENCE": colors.HexColor('#1A3A5C'),
        "BRAIN VILLAIN'S LAST TRICK": colors.HexColor('#5C0000'),
        "IDENTITY CLOSE": colors.HexColor('#1A4A1A'),
        "NEXT VIDEO TEASE": colors.HexColor('#4A0E4E'),
    }

    HEADER_ROW = [
        Paragraph('#', BEAT_NUM),
        Paragraph('<b>SEGMENT (NARRATION)</b>', BEAT_NUM),
        Paragraph('<b>IMAGE PROMPT</b>', BEAT_NUM),
        Paragraph('<b>CAMERA</b>', BEAT_NUM),
        Paragraph('<b>LIGHTING</b>', BEAT_NUM),
        Paragraph('<b>MOOD / TONE</b>', BEAT_NUM),
        Paragraph('<b>CHARACTER ACTION</b>', BEAT_NUM),
        Paragraph('<b>VIDEO MOTION</b>', BEAT_NUM),
    ]

    table_data = [HEADER_ROW]
    row_styles = []

    current_row = 1

    for i, ((beat_num, section, narration, prompt_text), prod) in enumerate(zip(BEATS, PROD)):
        if beat_num in SECTION_STARTS:
            sec_name = SECTION_STARTS[beat_num]
            sec_color = HDR_COLORS.get(sec_name, colors.HexColor('#333333'))
            sec_row = [Paragraph(f'<b>■■ {esc(sec_name)} ■■</b>', SEC_STYLE)] + [''] * 7
            table_data.append(sec_row)
            row_styles.append((current_row, 'SPAN', (0, current_row), (7, current_row), sec_color))
            current_row += 1

        cam, light, mood, char_act, vid_mot = prod
        full_prompt = img_prompt(beat_num, prompt_text)

        row = [
            Paragraph(str(beat_num), BEAT_NUM),
            Paragraph(f'<b>{esc(narration)}</b>', NARR_BOLD),
            Paragraph(esc(full_prompt), IMG_CELL),
            Paragraph(esc(cam), BODY_CELL),
            Paragraph(esc(light), BODY_CELL),
            Paragraph(esc(mood), BODY_CELL),
            Paragraph(esc(char_act), BODY_CELL),
            Paragraph(esc(vid_mot), BODY_CELL),
        ]
        table_data.append(row)

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
        if item[1] == 'SPAN':
            _, _, span_start, span_end, bg_color = item
            r = span_start[1]
            ts.add('SPAN',       (0, r), (7, r))
            ts.add('BACKGROUND', (0, r), (7, r), bg_color)
            ts.add('TEXTCOLOR',  (0, r), (7, r), colors.white)
            ts.add('ALIGN',      (0, r), (7, r), 'CENTER')
            ts.add('FONTNAME',   (0, r), (7, r), 'Helvetica-Bold')
            ts.add('FONTSIZE',   (0, r), (7, r), 9)
        elif item[1] == 'ROWBG':
            r, _, bg = item
            ts.add('BACKGROUND', (0, r), (-1, r), bg)

    table = Table(table_data, colWidths=col_w, repeatRows=1)
    table.setStyle(ts)

    flow = [
        Paragraph(esc(SUBTITLE), SUB_STYLE),
        Spacer(1, 3),
        Paragraph(esc(TITLE), TITLE_STYLE),
        Spacer(1, 3),
        Paragraph(esc(META), META_STYLE),
        Spacer(1, 8),
        table,
        Spacer(1, 8),
        Paragraph('END OF PRODUCTION DOCUMENT · 94 beats · ~1,011 words · ~7.5 min narration', META_STYLE),
    ]

    doc.build(flow)
    print(f"PDF: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    path = build_pdf()
    print(f"\n✅ V15 PRODUCTION DOCUMENT — BRIEF v3.1")
    print(f"   94 beats · 7 production columns per beat")
    print(f"   10 section headers · Table format matches V13/V10")
    print(f"   {path}")
