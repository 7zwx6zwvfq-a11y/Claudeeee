#!/usr/bin/env python3
"""
VIDEO 13 — PRODUCTION DOCUMENT · BRIEF v3.1
NEUROCENTS · 93 beats · ~1,100 words · ~8 min
Table format: # | SEGMENT | IMAGE PROMPT | CAMERA | LIGHTING | MOOD/TONE | CHARACTER ACTION | VIDEO MOTION
Matches V10 production document format exactly.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v13_v31_image_prompts import BEATS, STYLE_PREAMBLE

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                 Paragraph, Spacer, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

TITLE   = "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)"
SUBTITLE = "NEUROCENTS · VIDEO 13 — BRIEF v3.1"
META    = "STATE 5 — PRODUCTION DOCUMENT · 93 beats · ~1,100 words · ~8 min"

# Beat number → section header (marks where a new section starts)
SECTION_STARTS = {
    1:  "HOOK",
    11: "TRAP 1 — THE ANTICIPATION BURN",
    23: "TRAP 2 — THE BALANCE BLINDSPOT",
    34: "CTA",
    36: "TRAP 3 — THE EXPERTISE TRAP",
    48: "TRAP 4 — THE NIGHT DRAIN",
    59: "TRAP 5 — THE UPGRADE LOCK",
    70: "SYSTEM CLOSE",
    75: "BRAIN VILLAIN'S LAST TRICK",
    86: "IDENTITY CLOSE",
}

# Production values: (camera, lighting, mood, char_action, video_motion) — one per beat, 93 total
PROD = [
    # ── HOOK beats 1-10 ──
    ("LOW ANGLE, fast zoom out from skull",
     "Dark charcoal #1A1A1A, single overhead on '5'",
     "Shock, revelation — S17 thumbnail match in <5 sec",
     "Alex tilted back, both hands raised to sides of head in shock",
     "FAST ZOOM OUT from '5' inside skull to reveal full Alex"),
    ("MEDIUM SHOT, slight tilt",
     "Dark charcoal, '5' remains visible above Alex",
     "Grim recognition — context arrives",
     "Alex shifts from shock to understanding, expression tightening",
     "SLOW PULL BACK — '5' stays but shrinks as context expands"),
    ("MEDIUM CLOSE-UP, straight on",
     "Dark charcoal",
     "Elimination of excuses — clearing the frame",
     "Alex shakes head slowly, two X thought bubbles appear and dissolve",
     "SLIGHT PUSH IN as X marks appear one by one"),
    ("EXTREME CLOSE-UP on skull interior",
     "Dark charcoal, red circuit glow inside skull",
     "Sinister revelation — the mechanism exposed",
     "Brain Villain at control panel, all 5 switches flipped ON, smug",
     "SLOW ZOOM INTO skull cavity — control panel fills frame"),
    ("MEDIUM SHOT, Alex left, book stack right",
     "Dark charcoal, circuit 3 pulses brighter than others",
     "Counterintuitive — education makes it worse",
     "Brain Villain points at circuit 3 with knowing smirk",
     "BOOK STACK GROWS frame by frame, circuit 3 intensifies in parallel"),
    ("LOW ANGLE, dramatic",
     "Dark charcoal, DNA helix electric glow inside skull",
     "Biological urgency — not just financial",
     "Brain Villain beside DNA helix, biological symbol larger than coin icon",
     "DNA HELIX ROTATES slowly — biology > money visual"),
    ("TIGHT on skull with clock in corner",
     "Dark charcoal, circuit 1 flashing urgently",
     "Unsettled — it already ran this morning",
     "Alex unsettled expression, Brain Villain checks tiny watch — 'already ran it'",
     "CLOCK TICK animation — 8:47 AM timestamp pulses"),
    ("WIDE SHOT, Alex left, five numbered slots right",
     "Dark charcoal fading to white on right side",
     "Promise, structure — the order matters",
     "Alex pointing at slot 1, Brain Villain alert and watching inside skull",
     "SLOTS APPEAR ONE BY ONE left to right — 1 · 2 · 3 · 4 · 5"),
    ("EXTREME CLOSE-UP on Brain Villain inside skull",
     "Dark charcoal, green status light active",
     "Menace, inevitability — already executing",
     "Brain Villain activates hologram: 'PROGRAM 1 — RUNNING'",
     "LABEL ACTIVATES with click — green status light goes live"),
    ("DUTCH ANGLE, narrative shift suggested",
     "Dark charcoal transitioning to warm beige interior",
     "Bridge — entering Trap 1's world",
     "Alex turns head toward new scene, circuit 1 glows alone, others dim",
     "SLOW PAN toward Trap 1 scene — camera transitions"),
    # ── TRAP 1 beats 11-22 ──
    ("MEDIUM WIDE SHOT",
     "Warm beige interior, oval ceiling spotlight",
     "Waiting, anticipation building beneath the surface",
     "Alex at desk, neutral expression, Brain Villain leaning forward with interest",
     "CALENDAR highlight pulses on Wednesday — FRIDAY greyed out"),
    ("MEDIUM CLOSE-UP on face + thought bubble",
     "Warm beige, soft oval spotlight",
     "Pre-committed desire — the decision was already made",
     "Alex with detailed specific thought bubble — item fully formed before payday",
     "THOUGHT BUBBLE MATERIALIZES complete — item and price tag visible"),
    ("WIDE SHOT, three-panel Monday/Tuesday/Wednesday timeline",
     "Warm beige across all three panels",
     "Pattern revealed — the schedule, not the moment",
     "Brain Villain's dopamine meter rises with each panel",
     "TIMELINE BUILDS left to right — bubble grows each day"),
    ("MEDIUM SHOT, Alex + dopamine graph",
     "Clinical white, graph prominent",
     "Scientific clarity — desire peaks before money arrives",
     "Alex points at Wednesday peak, confused — peak is wrong day",
     "GRAPH LINE DRAWS itself: peaks Wednesday, declines Friday"),
    ("MEDIUM SHOT, academic scene",
     "Clean academic white",
     "Nobel authority — this is not opinion",
     "Alex watching Cambridge researcher, attentive",
     "WOLFRAM SCHULTZ · CAMBRIDGE · NOBEL PRIZE label FADES IN"),
    ("EXTREME CLOSE-UP on single neuron diagram",
     "Dark background, electric blue/gold neuron glow",
     "Biological truth — microscopic mechanism",
     "Brain Villain demonstrates at neuron level — points to prediction synapse",
     "DOPAMINE PULSE fires at PREDICTION marker — NOT at reward"),
    ("TIGHT on skull interior, dopamine curve",
     "Warm amber skull glow",
     "Biological inevitability — the peak was already past",
     "Brain Villain marks Wednesday peak on internal dopamine graph",
     "CURVE PEAKS Wednesday, DROPS Friday — annotated in real time"),
    ("MEDIUM SHOT, Alex at checkout/ATM on Friday",
     "Neutral warm",
     "Mechanical receipt — not decision",
     "Alex's hand moves to card automatically, expression blank",
     "RECEIPT PRINTS as beat ends — transaction already closed"),
    ("CLOSE-UP on Alex's hands making purchase",
     "Warm domestic",
     "Automaticity — body acts before mind registers",
     "Hands reach before facial expression changes — fractional delay",
     "SLOW MOTION on hand reaching — brain catches up after"),
    ("WIDE SHOT, Alex acting vs dopamine timeline side by side",
     "Split: warm left (Alex) / white right (graph)",
     "The gap between feeling and decision made visible",
     "Brain Villain timestamps each dopamine event on timeline in sync",
     "TIMELINE ANNOTATES simultaneously with Alex's actions"),
    ("MEDIUM CLOSE-UP, Alex with RECEIPT label",
     "Warm beige",
     "Recognition — the trap named and visible",
     "Alex reads RECEIPT label floating over his purchase — grim understanding",
     "RECEIPT LABEL BURNS IN over purchase action"),
    ("LOW ANGLE, transition beat",
     "Warm shifting to cooler — Trap 2 color bleeding in",
     "Bridge — damage done, now to be hidden",
     "Brain Villain waves toward the evidence that is about to be buried",
     "CAMERA TILTS toward Trap 2 scene — colors shift"),
    # ── TRAP 2 beats 23-33 ──
    ("MEDIUM WIDE SHOT, Saturday morning domestic scene",
     "Warm morning, phone screen dim and ignored",
     "Avoidance — active, not passive",
     "Alex deliberately not reaching for phone — small specific gesture",
     "PHONE SCREEN DIMS unnoticed beside him"),
    ("CLOSE-UP on calendar",
     "Warm domestic",
     "Rationalization — the excuse that always makes sense",
     "Alex flips calendar to next week, Brain Villain nods approvingly",
     "CALENDAR PAGES to 'calmer week' that perpetually recedes"),
    ("WIDE SHOT, 30-day check timeline",
     "Green for post-paycheck checks, red-absent for post-purchase",
     "Pattern exposed — the data indicts the behavior",
     "Brain Villain marks absent post-purchase checks with satisfaction",
     "CHECK MARKS appear green / POST-PURCHASE slots remain empty"),
    ("MEDIUM SHOT, academic scene",
     "Clean academic white",
     "Scientific credibility — it has a name",
     "Alex watching researchers present clipboard data at Hebrew University",
     "'THE OSTRICH EFFECT · GALAI & SADE · HEBREW UNIVERSITY · 2006' label appears"),
    ("CLOSE-UP, ostrich icon morphing to Alex silhouette",
     "Clinical white",
     "Irony — named after avoidance, embodied by Alex",
     "Alex unconsciously mirrors phone-face-down as ostrich buries head",
     "OSTRICH ICON MORPHS into Alex silhouette — seamless"),
    ("MEDIUM SHOT, Alex with cortisol meter",
     "Warm, cortisol diagram in clinical white",
     "Biological protection misapplied — cortisol reduction at cost",
     "Brain Villain adjusts cortisol dial as Alex avoids the balance",
     "CORTISOL DIAL TURNS DOWN as avoidance triggers — relief visible"),
    ("CLOSE-UP on Alex's face over time montage",
     "Progressive dulling of warm light",
     "Conditioning — pain response hardwired through repetition",
     "Alex's expression clouds progressively with each bad number encounter",
     "FAST MONTAGE — bad number moments, expression darkens each time"),
    ("MEDIUM SHOT, reflex arc diagram",
     "Split: warm stimulus / shadow avoidance",
     "The reflex established — automatic, pre-conscious",
     "Brain Villain pulls reflex trigger, Alex avoids before thinking",
     "REFLEX ARC animation: STIMULUS → AVOIDANCE bypass"),
    ("LOW ANGLE on Brain Villain, satisfied",
     "Warm skull glow — comfortable",
     "Effortless control — the villain's best move",
     "Brain Villain crosses arms — job done without effort or detection",
     "Brain Villain sits back, victory without visible work"),
    ("WIDE SHOT, Trap 1 + Trap 2 side by side",
     "Red impulse left + shadow cover right",
     "System revealed — two traps working in sequence",
     "Brain Villain orchestrates both simultaneously from single position",
     "TWO TRAPS shown connected — impulse feeds into cover-up"),
    ("DUTCH ANGLE, transition to Trap 3",
     "Shift toward desk lamp / bookshelf lighting",
     "Bridge — the vocabulary trap incoming",
     "Brain Villain gestures toward books and vocabulary",
     "TRANSITION PAN to Trap 3 scene — books appear"),
    # ── CTA beats 34-35 ──
    ("MEDIUM SHOT, Alex direct address",
     "Warm single spotlight on Alex",
     "Genuine, direct — value already delivered",
     "Alex breaks to direct viewer address — no Brain Villain blocking",
     "SUBTLE ZOOM IN to Alex's face — natural, unhurried"),
    ("MEDIUM SHOT, hold",
     "Same warm spotlight, steady",
     "Value offer, calm invitation",
     "Brain Villain visible but quiet — Alex in full control here",
     "STATIC HOLD — slow subtle pulse on subscribe prompt"),
    # ── TRAP 3 beats 36-47 ──
    ("MEDIUM WIDE, Alex at desk with books",
     "Warm desk lamp, bookshelf background prominent",
     "Intellectual confidence — comfortable, familiar",
     "Alex surrounded by behavioral finance books, comfortable posture",
     "SLOW PAN across book spines — titles legible"),
    ("CLOSE-UP on Alex's face + floating bias labels",
     "Warm confident light",
     "The illusion of mastery — vocabulary feels like control",
     "Alex ticks off bias names on fingers, each one floats as a label",
     "BIAS LABELS appear one by one as Alex names them"),
    ("MEDIUM SHOT, Alex leaning back",
     "Warm, assured",
     "Peak confidence — the trap fully set",
     "Alex arms crossed, leaning back — certainty posture",
     "CONFIDENCE METER fills to top on screen beside him"),
    ("WIDE, split: Alex's trades / red results",
     "Split: warm left (Alex confident) / cold red right (results)",
     "The gap — certainty and accuracy diverging",
     "Alex trades with conviction, result line drops below benchmark",
     "TRADE AFTER TRADE lands below market line — gap widens"),
    ("WIDE, academic scene — UC Berkeley",
     "Clean white, authoritative",
     "Scale of evidence — 35,000 accounts, seven years",
     "Alex observing researcher present findings at UC Berkeley",
     "35,000 ACCOUNTS label materializes — weight of the data"),
    ("BAR CHART, trading frequency vs returns",
     "Clinical white, bars prominent",
     "The inversion — most active = worst returns",
     "Alex points at frequent-trader bar — at the bottom",
     "BARS APPEAR ordered by frequency — most active at bottom of returns"),
    ("WIDE, CONFIDENCE vs COMPETENCE bars",
     "Orange confidence bar / green competence bar",
     "The gap named — confidence outpaced competence",
     "Brain Villain widens confidence bar past competence level",
     "CONFIDENCE BAR grows faster than COMPETENCE BAR — gap opens"),
    ("WIDE, 80% chart",
     "Clinical white, 80% bar prominent",
     "Scale of self-deception — nearly universal pattern",
     "Alex in the 80% bar, looking at the 50% truth",
     "80% BAR rises, then 50% CORRECTION appears — the math doesn't allow it"),
    ("MEDIUM SHOT, Alex with vocabulary list",
     "Warm bookish light",
     "Vocabulary-certainty loop — the feedback that traps",
     "Brain Villain adds new vocab word, Alex nods reassured each time",
     "VOCAB LIST grows — ACCURACY meter stays flat beside it"),
    ("MEDIUM SHOT, vocabulary → certainty arrow diagram",
     "Warm, arrows prominent",
     "The false pathway — vocabulary bypasses accuracy",
     "Alex traces vocab → certainty arrow, accuracy branch is dim and ignored",
     "ARROW from vocab to certainty bypasses accuracy — dead branch shown"),
    ("CLOSE-UP, one-way gate closing",
     "Clinical white, red gate",
     "The lock — one direction only, no return",
     "Brain Villain closes one-way gate — entry only, no exit back to doubt",
     "ONE-WAY GATE closes behind vocabulary growth — irreversible"),
    ("TRANSITION WIDE, clock advancing to night",
     "Day → night time lapse",
     "Bridge — exhaustion is the next trap",
     "Clock advances to 10:47 PM, desk lamp switches on",
     "TIME LAPSE from day to night — transition to Trap 4"),
    # ── TRAP 4 beats 48-58 ──
    ("CLOSE-UP on Alex's tired face",
     "Phone screen glow in darkness — single light source",
     "Exhaustion, vulnerability — peak danger moment",
     "Alex's eyes heavy, phone bright against dark — the contrast is the trap",
     "SUBTLE PULSE on phone glow — rhythm like heartbeat"),
    ("WIDE, decision tally board",
     "Cool overhead, tally marks covering entire board",
     "Depletion mapped — the invisible drain counted",
     "Brain Villain counts tally marks — a hundred decisions charted",
     "TALLY MARKS appear rapidly covering the day board"),
    ("MEDIUM SHOT, Alex in bed with phone",
     "Phone screen only light in dark room",
     "Vulnerable, depleted — override mechanism at zero",
     "Alex's thumb drifts toward cart icon — movement before decision",
     "SCROLL MOTION, cart icon pulses as thumb approaches"),
    ("CLOSE-UP on thought bubble",
     "Dim tired warm light",
     "Deferred to 'morning Alex' — who also had no choice",
     "Alex pictures 'MORNING ALEX' deciding — optimistic, full-reserve figure",
     "MORNING FIGURE appears in bubble — full and capable — then FADES"),
    ("MEDIUM SHOT, phone screen flash at purchase",
     "Phone flash then instant darkness",
     "Impulse without resistance — no friction",
     "Alex clicks buy, eyes already closing — body acting without mind",
     "BUY BUTTON flashes, then screen dims to sleep mode"),
    ("WIDE, judges courtroom scene",
     "Institutional neutral light",
     "Scientific authority — ten months, eight judges",
     "Alex watching judge scene establish — observer perspective",
     "DANZIGER · BEN-GURION UNIVERSITY label appears with scene"),
    ("BAR CHART, morning vs afternoon parole rates",
     "Morning green / afternoon red — stark contrast",
     "65% vs 11% — the data is the argument",
     "Alex stares at the bars — morning high, afternoon near zero",
     "MORNING BAR (65%) high, AFTERNOON BAR (11%) near floor — dramatic"),
    ("MEDIUM SHOT, three judges side by side",
     "Identical lighting for all three — universality",
     "Not character — biology. Same people, different reserves",
     "Three identical judge figures, RESERVE METER differs per panel",
     "RESERVE METER shown under each judge — same person, different level"),
    ("MEDIUM SHOT, Alex's reserve meter depleting",
     "Cool — reserve meter empties through day panels",
     "Same mechanism — Alex is the judge in his own court",
     "Alex's RESERVE METER empties as day timeline advances, Brain Villain waits",
     "RESERVE METER EMPTIES left to right — Brain Villain watches"),
    ("MEDIUM SHOT, Brain Villain waiting patiently",
     "Warm skull glow — patience visualized",
     "Patient predation — timing is the only tool needed",
     "Brain Villain checks watch, sits back, waits for reserve to exhaust",
     "Brain Villain WAITS — calm animation as meter drains to zero"),
    ("WIDE, purchase spike graph 9PM–midnight",
     "Progressive night darkening, spike bars glowing",
     "Biological timing — the peak window documented",
     "Purchase notification icons appear in the dark hours cluster",
     "PURCHASE SPIKES appear between 9PM–midnight on timeline graph"),
    # ── TRAP 5 beats 59-69 ──
    ("MEDIUM WIDE, Alex in upgraded apartment",
     "Warm aspirational — new environment, everything fresh",
     "Genuine satisfaction — temporary, unbeknownst to Alex",
     "Alex looks around with real pleasure, Brain Villain calm inside skull",
     "SLOW PAN of upgraded space — everything catches light"),
    ("CALENDAR showing Day 1 through Day 11",
     "Bright warm Day 1 → neutral grey Day 11",
     "Hedonic fade — the ticking clock on every upgrade",
     "Alex's expression dims panel by panel across eleven days",
     "CALENDAR COUNTS: Day 1 'DIFFERENT' → Day 11 'NORMAL'"),
    ("CLOSE-UP on Alex's face, expression neutral",
     "Neutral flat light — neither warm nor cold",
     "Calibration — not misery, not joy. Baseline reset",
     "Alex expression: unreadable — recalibrated, not broken",
     "EXPRESSION HOLD — ambiguous, still. Viewer reads it themselves"),
    ("WIDE, two circuits separated on diagram",
     "WANTING: electric blue / LIKING: warm orange",
     "Scientific separation — two systems, two trajectories",
     "Brain Villain points to WANTING and LIKING circuits separately",
     "WANTING and LIKING CIRCUITS SEPARATE on diagram — labeled"),
    ("MEDIUM SHOT, Kent Berridge lab scene",
     "Clean white academic",
     "Thirty years of research — the deepest trap has the deepest science",
     "Alex observing Berridge's lab work — attentive",
     "KENT BERRIDGE · UNIVERSITY OF MICHIGAN · 30 YEARS label appears"),
    ("CLOSE-UP, dopamine WANTING circuit",
     "Electric blue — energy, escalation",
     "Wanting scales with exposure — it grows with each upgrade",
     "Brain Villain feeds wanting circuit — meter climbs with each exposure",
     "WANTING METER CLIMBS — each exposure raises baseline"),
    ("CLOSE-UP, opioid LIKING circuit",
     "Warm orange fading to grey — diminishing returns",
     "Liking habituates — same thing, smaller response each time",
     "Brain Villain taps liking circuit — response visibly smaller each time",
     "LIKING METER DIMS with each repetition — same input, less output"),
    ("WIDE, upgrade ladder",
     "Each rung: wanting arrow rises, liking arrow stays flat",
     "The trap in full — upgrades strengthen wanting, habituate liking",
     "Brain Villain climbs upgrade ladder with Alex — WANTING rises each rung",
     "UPGRADE LADDER extends upward — WANTING rises, LIKING stays flat"),
    ("CLOSE-UP on rising floor — no downward arrow",
     "Red floor line — no return",
     "The lock — the floor only moves up",
     "Brain Villain stamps 'NO RETURN' on the rising floor level",
     "FLOOR RISES with each upgrade — no downward arrow possible"),
    ("WIDE comparison, before and after upgrade",
     "Before: warm content / After: calibrated neutral",
     "Biological change — not circumstantial, not reversible",
     "Pre-upgrade Alex content with less / Post-upgrade Alex needs more to reach same",
     "SIDE BY SIDE — before happy at baseline, after baseline permanently shifted"),
    ("WIDE, all 5 program circuits active simultaneously",
     "Five red circuits glowing — the full system",
     "The complete picture — five locks, one system, all running",
     "Brain Villain at center, all five programs active — arms wide",
     "ALL 5 CIRCUITS LIT simultaneously — system fully active animation"),
    # ── SYSTEM CLOSE beats 70-74 ──
    ("WIDE, five program labels appear together",
     "Clinical white — synthesis mode",
     "Synthesis — naming the complete system",
     "Alex sees all five program labels simultaneously — the full map",
     "5 PROGRAM LABELS appear together on screen"),
    ("CLOSE-UP, Program 1 pulse",
     "Warm anticipation glow — dopamine color",
     "The beginning of the cascade",
     "Brain Villain activates Program 1 first — the original impulse",
     "PROGRAM 1 PULSES — initiates the chain"),
    ("MEDIUM SHOT, Program 2 covering",
     "Shadow descends over financial data",
     "The cover — invisible by design",
     "Brain Villain draws shade over numbers and records",
     "SHADE DROPS over evidence — gone"),
    ("WIDE, Program 3 vocabulary card",
     "Warm library light",
     "False safety — vocabulary as anesthetic",
     "Brain Villain hands Alex vocabulary card — Alex accepts, reassured",
     "VOCABULARY CARD dissolves into false certainty bubble"),
    ("WIDE, all 5 cascading — domino effect",
     "Red circuits cascading one to next",
     "The complete trap — five programs, one result",
     "Brain Villain pulls all 5 switches simultaneously — domino fires",
     "DOMINO EFFECT — each trap triggers next, P4 lowers resistance, P5 raises floor"),
    # ── BRAIN VILLAIN'S LAST TRICK beats 75-85 ──
    ("CLOSE-UP on Brain Villain turning to face camera",
     "Warm skull glow — intimate",
     "Direct menace — the villain's final move is the quietest",
     "Brain Villain turns and looks directly at viewer — fourth wall",
     "VILLAIN LOOKS at camera — fourth wall break"),
    ("MEDIUM SHOT, Alex's chest rising",
     "Warm, close",
     "Direct implication — this is happening to the viewer now",
     "Alex's chest rises with the feeling named in narration",
     "SUBTLE PULSE — recognition arriving in real time"),
    ("MEDIUM SHOT, Alex looking calm",
     "Quiet, understated",
     "The real danger — quieter than denial",
     "Alex not panicking — looks deceptively calm and in control",
     "STILLNESS — the quiet IS the threat"),
    ("CLOSE-UP on thought bubble appearing",
     "Comfortable warm light",
     "Self-deception dressed as self-awareness",
     "'I ALREADY KNEW ABOUT MOST OF THESE' thought materializes",
     "THOUGHT BUBBLE appears — comfortable, familiar, dangerous"),
    ("MEDIUM SHOT, Alex examines thought critically",
     "Clinical — examining from outside",
     "Deconstruction — something is wrong with the thought",
     "Alex looks at his own thought critically — cracks forming",
     "THOUGHT BUBBLE EXAMINED — surface cracks appear"),
    ("CLOSE-UP, Expertise Trap label on thought bubble",
     "Red label emerging",
     "Irony — the trap wearing the costume of insight",
     "Brain Villain holds up EXPERTISE TRAP sign wearing costume of self-knowledge",
     "COSTUME REVEAL — label materializes on thought bubble"),
    ("WIDE, evolutionary background emerging behind villain",
     "Warm primeval behind / modern in foreground",
     "Evolutionary context — origin story of the trap",
     "Ancestral world appears behind Brain Villain — pattern recognition saved lives",
     "ANCESTRAL SCENE fades in behind modern scene"),
    ("MEDIUM SHOT, ancestor survives by pattern recognition",
     "Primeval warm, urgent",
     "The original purpose — it worked then",
     "Ancestor figure survives precisely because of pattern recognition",
     "PATTERN RECOGNITION SAVES ancestor — the payoff is visible"),
    ("CLOSE-UP on dopamine circuit — same as Trap 1 / Beat 16",
     "Red and gold — same circuit signature as Beat 16",
     "Unchanged across 50,000 years — same brain, different world",
     "Brain Villain shows dopamine firing Wednesday — same circuit as Trap 1",
     "DOPAMINE PULSE fires — visually identical to Beat 16"),
    ("WIDE SPLIT — ancestral world left / modern world right",
     "Warm evolutionary (left) / cold modern fluorescent (right)",
     "The mismatch — designed for a world that no longer exists",
     "Brain Villain in ancestral scene: perfect fit. In modern scene: lost",
     "SPLIT SCREEN — villain thrives in left, confused in right"),
    ("CLOSE-UP, Brain Villain small in modern context",
     "Modern cold light — villain looks out of place",
     "Wrong environment — not evil, just misplaced",
     "Brain Villain looks around confused in modern financial world",
     "VILLAIN SHRINKS in modern context — loses coherence"),
    # ── IDENTITY CLOSE beats 86-93 ──
    ("MEDIUM SHOT, Alex exhales",
     "Warm — tension releasing",
     "Relief, reframe — not a flaw, never was",
     "Alex exhales visibly — not shame, not defeat, recognition",
     "TENSION RELEASE — shoulders drop, posture opens"),
    ("WIDE, ancestor montage",
     "Warm evolutionary — scarcity and survival",
     "Anticipation Burn kept ancestors alive — historical reframe",
     "Ancestor Alex motivated through scarcity by Anticipation Burn — survives",
     "ANCESTOR SCENE — Anticipation Burn → survival"),
    ("WIDE SPLIT, same brain / two worlds",
     "Split: evolutionary warm (left) / modern cool (right)",
     "The mismatch — design vs context",
     "Same character — same brain — different world beneath his feet",
     "WORLD SHIFTS beneath same character — brain unchanged"),
    ("WIDE, tribal climbing as survival",
     "Warm tribal, communal",
     "Upgrade Lock had evolutionary logic — tribe survival",
     "Tribe climbs together — upgrading meant survival once",
     "TRIBE ADVANCES — upgrade = life in that world"),
    ("MEDIUM SHOT, 'DESIGNED FOR' replaces 'BROKEN'",
     "Clinical recognition",
     "Logical reframe — not broken, built for wrong context",
     "Alex sees 'DESIGNED FOR' stamp replace 'BROKEN' label",
     "'DESIGNED FOR' REPLACES 'BROKEN' — visual swap"),
    ("MEDIUM SHOT, Brain Villain in modern world",
     "Modern cool — villain looks lost, not malevolent",
     "The mismatch acknowledged — villain is not evil, just misplaced",
     "Brain Villain looks at modern world, confused — not threatening here",
     "VILLAIN IN WRONG CONTEXT — not evil, misplaced"),
    ("MEDIUM SHOT, Alex looking toward next video",
     "Warm forward promise",
     "Next video tease — structural solution exists",
     "Alex looks toward what comes next, Brain Villain quiet behind him",
     "TEASER GLIMPSE of structural decision — one decision shuts three"),
    ("MEDIUM SHOT, Alex direct address",
     "Warm single spotlight, clean",
     "Invitation — genuine, direct, earned",
     "Alex speaks directly to viewer — not selling, sharing what works",
     "SLOW ZOOM to Alex's face — then SLOW FADE"),
]

assert len(PROD) == 93, f"PROD has {len(PROD)} entries, expected 93"
assert len(BEATS) == 93, f"BEATS has {len(BEATS)} entries, expected 93"


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

    # Table cell styles
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

    pdf_path = "/home/user/Claudeeee/V13_v31_PRODUCTION.pdf"
    page = landscape(A4)
    doc = SimpleDocTemplate(pdf_path, pagesize=page,
                            leftMargin=10*mm, rightMargin=10*mm,
                            topMargin=12*mm, bottomMargin=12*mm)

    # Column widths (landscape A4 = 297mm usable ≈ 277mm after margins)
    # #(8) | NARR(40) | IMG(75) | CAM(30) | LIGHT(30) | MOOD(28) | CHAR(33) | MOTION(33)
    col_w = [8*mm, 40*mm, 75*mm, 30*mm, 30*mm, 28*mm, 33*mm, 33*mm]
    total = sum(col_w)  # 277mm

    HDR_COLORS = {
        "HOOK": colors.HexColor('#1A1A2E'),
        "TRAP 1 — THE ANTICIPATION BURN": colors.HexColor('#8B1A1A'),
        "TRAP 2 — THE BALANCE BLINDSPOT": colors.HexColor('#7A3B00'),
        "CTA": colors.HexColor('#1A5C1A'),
        "TRAP 3 — THE EXPERTISE TRAP": colors.HexColor('#2B2B8B'),
        "TRAP 4 — THE NIGHT DRAIN": colors.HexColor('#4A0E4E'),
        "TRAP 5 — THE UPGRADE LOCK": colors.HexColor('#8B5A00'),
        "SYSTEM CLOSE": colors.HexColor('#1A3A5C'),
        "BRAIN VILLAIN'S LAST TRICK": colors.HexColor('#5C0000'),
        "IDENTITY CLOSE": colors.HexColor('#1A4A1A'),
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
    row_styles = []  # list of (row_index, style_commands)

    current_row = 1  # 0 = header

    for i, ((beat_num, narration, prompt_text), prod) in enumerate(zip(BEATS, PROD)):
        # Section header row
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

        # Alternating row shading
        if i % 2 == 0:
            row_styles.append((current_row, 'ROWBG', colors.HexColor('#F7F7F7')))
        current_row += 1

    # Build table style
    ts = TableStyle([
        # Header
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
        Paragraph(f'END OF PRODUCTION DOCUMENT · 93 beats · ~1,100 words · ~8 min narration', META_STYLE),
    ]

    doc.build(flow)
    print(f"PDF: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    path = build_pdf()
    print(f"\n✅ V13 PRODUCTION DOCUMENT — BRIEF v3.1")
    print(f"   93 beats · 7 production columns per beat")
    print(f"   10 section headers · Table format matches V10")
    print(f"   {path}")
