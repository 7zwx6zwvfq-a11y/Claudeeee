#!/usr/bin/env python3
"""
VIDEO 17 — IMAGE PROMPTS · COMPARATIVA (Leo vs Marc)
74 beats · Personajes NUEVOS (sin Alex, sin Brain Villain) · split-screens y gráficas de dos curvas
Regla Reducir Personaje aplicada: muchos beats son objetos/diagramas — Leo/Marc solo cuando la
emoción o el contraste lo piden.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v17_final_script import SECTIONS, TITLE

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

SUBTITLE = "NEUROCENTS · VIDEO 17"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines on every element, clean solid color "
    "fills, no gradients. THIS VIDEO HAS NO ALEX AND NO BRAIN VILLAIN — two NEW recurring characters: "
    "LEO: young man, flat cartoon style, rounded head, brown swept hair, GREEN t-shirt in early years "
    "(upgrading to a navy blazer in later years as his lifestyle inflates), expressive, slightly "
    "flashy energy. "
    "MARC: young man, same build, short black hair, plain GRAY t-shirt that NEVER changes across all "
    "years, calm neutral energy. "
    "Both age subtly across the video (slight posture/face maturity at years 10/15/20 — no beards "
    "unless specified). LEFT half of split-screens = LEO (warm tones), RIGHT half = MARC (cool "
    "neutral tones) — keep sides consistent in every split. "
    "Recurring motif: THE CURVE — a two-line wealth graph (Leo flat gray line, Marc green compounding "
    "curve) that grows through the video. Recurring motif: THE NAPKIN — a paper napkin with "
    "handwritten rule. Palette: green savings/growth · red loss · warm gold for Leo's lifestyle · "
    "white/clean backgrounds. 16:9, 1280x720."
)

# Flatten script sections → (num, section, narration)
_flat = []
_n = 1
for _sec, _lines in SECTIONS:
    for _l in _lines:
        _flat.append((_n, _sec, _l))
        _n += 1

PROMPTS = [
    # COLD OPEN (1-5)
    "S17 OPENING [THUMBNAIL CONTINUITY]: split-screen — Leo (left, green shirt) and Marc (right, gray "
    "shirt) each at a desk, both phones lighting up with the identical raise email at the same instant. "
    "Same office layout mirrored. The viewer recognizes the thumbnail's two-figure split in <5 seconds.",
    "Four small mirrored icon pairs between them: building, payslip, city skyline, apartment key — "
    "identical on both sides. Diagram-clean, no text.",
    "Flash-forward: Marc at 45 (subtle gray at temples, same gray shirt) standing relaxed in a doorway "
    "of a boss's office, jacket over shoulder — leaving light. Warm morning sun behind him.",
    "Leo at 45 (navy blazer, tired eyes) at a desk at night, the same sentence visible as a faded "
    "thought bubble with a padlock on it. Office glow, everyone else gone.",
    "THE NAPKIN: a paper napkin sliding onto a table, pen resting on it, marks not yet readable. "
    "Single spotlight. The promise-object of the video.",
    # THE FAIR FIGHT (6-10)
    "A boxing-ring style split card: Leo and Marc facing forward like a fight poster — but everything "
    "on the stat card between them is IDENTICAL (same bars, same icons). The joke: a fair fight nobody stages.",
    "Two identical apartment doors side by side, 25 on both doorplates, same €28,000 payslip taped to each.",
    "Three crossed-out icons floating: inheritance envelope, lottery ticket, rocket coin. Clean white, "
    "red X on each — the usual excuses eliminated.",
    "Two identical brain outlines side by side, running the same gear animation inside — same impulses "
    "ticking. No character bodies, just the twin brains.",
    "A single fork in a road seen from above, both silhouettes still walking the shared segment before "
    "the split. Long shadow of a fork ahead. Tension frame.",
    # YEAR ONE (11-14)
    "Calendar page day 28: two identical wallets, both open, both empty — moths optional but same moth.",
    "Split: both check phones with the same slumped posture; identical takeaway bags on both counters. "
    "Mirror comedy — every detail duplicated.",
    "A party scene where Leo and Marc stand side by side wearing the SAME expression — a friend "
    "silhouette between them literally cannot point at the right one.",
    "Both phones buzz with the raise notification (+€200/month). Between the two phones, the road-fork "
    "icon from beat 10 flickers on. The experiment begins.",
    # THE SPLIT (15-20)
    "Leo's side only: an upgrade montage — apartment key upgrading, restaurant plate upgrading, jacket "
    "upgrading. Warm gold light. Leo smiling, reasonable, NOT a caricature.",
    "Leo at a nicer dinner table raising a glass — earned-it energy. Warm, likable. No judgment framing.",
    "Marc's side: exactly the same kitchen as year one. Nothing changed. The visual joke is the total "
    "absence of change — same mug, same chair.",
    "Marc's phone: an automatic transfer notification sliding money into an account icon behind frosted "
    "glass — visible but blurred. He isn't even looking; he's washing the same mug.",
    "THE NAPKIN in close-up, now readable as handwriting-style icons: a crossed-out raise arrow → "
    "invisible; a life-upgrade icon → only every 5 years. The rule, written once.",
    "The two-line CURVE graph appears for the first time: both lines still overlapping at the origin, "
    "a 20-year x-axis stretching ahead. Clean white diagram.",
    # YEAR FIVE (21-26)
    "Split: both desks now have a small '×2 promotions' badge; both payslips read €36,000. Identical again.",
    "Leo's side glowing: nicer flat interior, car keys, weekend photos pinned. He looks like the winner "
    "— staged like a lifestyle ad.",
    "Marc's side: the year-one room, one better mattress with a small price tag as the only upgrade. "
    "Deadpan humor frame.",
    "Leo's savings jar: a few coins, receipt-leftovers stuffed around it. Number card beside it: €4,000.",
    "Marc's frosted-glass account now visible: €34,000 — and a tiny green sprout growing out of the "
    "number, first compound interest sprout.",
    "Wide: a small crowd applauds Leo's car; Marc stands unnoticed at the edge, hands in pockets, "
    "completely fine. Nobody claps for the invisible.",
    # CTA (27-28)
    "Split-screen freeze of both paths with a subscribe button centered between them — the viewer "
    "literally standing between Leo and Marc.",
    "A calculator running on a Thursday calendar chip — numbers scrolling. Minimal, fast.",
    # YEAR TEN (29-32)
    "Both payslips: €45,000. Both men at 35 — subtle maturity. Identical career badges. The constant "
    "re-established before the reveal.",
    "Leo's highlight reel: better address plaque, better car, vacation photos — framed like social "
    "media posts with hearts floating.",
    "Marc's CURVE graph: his green line crossing €126,000, visibly curving upward now while Leo's "
    "gray line crawls flat. First dramatic divergence frame.",
    "A dotted vertical line on the graph labeled by an eye icon — something crosses here. Zoomed "
    "tension frame, no reveal yet.",
    # THE INVISIBLE LINE (33-36)
    "Diagram: Marc's green curve's yearly growth arrow now TALLER than the original +€200 raise arrow "
    "beside it. The money out-earns the raise.",
    "Two payslip icons hovering over Marc: one from his employer, one printed by the curve itself — "
    "his money's salary. LAPIDARIA frame, minimal.",
    "The second payslip personified slightly: it never sleeps — shown working at a tiny desk under "
    "moonlight while Marc sleeps. Gentle humor, warm night palette.",
    "Leo alone pulling a single rope attached to his entire lifestyle-wagon (car, flat, dinners "
    "stacked). Sweat drop. One worker, growing load.",
    # YEAR FIFTEEN (37-41)
    "Both payslips: €55,000. Age 40 — a bit more tired in both faces, same symmetry.",
    "Leo's monthly flow diagram: €55k pipe in → lifestyle machine consumes almost all → thin trickle "
    "into a jar labeled €20,000 total. Honest, not cruel.",
    "Marc's curve: €318,000 — the green line now steep, leaving the frame's top-right corner. "
    "'Stopped being polite' rendered visually: the curve breaks the chart border.",
    "The same office parking lot: both cars parked side by side (Leo's nicer), same building shadow "
    "over both. Repetition-pattern frame.",
    "A countdown flip-calendar showing 5 YEARS beside Marc's silhouette walking toward a horizon door. "
    "Quiet, cinematic.",
    # YEAR TWENTY (42-47)
    "Both at 45. Both payslips: €62,000. Final symmetry frame before the verdict.",
    "Marc's account: €640,000 — the number rendered as a solid structure he can stand on, like a "
    "platform. The curve holds his weight now.",
    "Diagram: money's salary arrow (from the platform) covering a 'living costs' bar completely. "
    "The definition of free, drawn.",
    "Marc at a Monday sunrise crossroads: two signs — office / mountains — both green. He holds "
    "the choice like car keys. Light, unburdened.",
    "Leo's €62,000 payslip with every cent pre-cut into labeled slices flying away as it lands — "
    "rent slice, car slice, lifestyle slice. Nothing settles.",
    "Final CURVE graph full-frame: identical career milestones marked on both lines — same jobs, "
    "same promotions — one flat, one mountain. Twenty years, one rule apart.",
    # THE NAPKIN (48-52)
    "THE NAPKIN full-frame, now completely readable as clean iconography: rule 1 live-on-first-salary "
    "icon, rule 2 raise→vault arrow, rule 3 five-year upgrade dial.",
    "Icon sequence: salary №1 framed on a wall like a fixed reference; every subsequent raise arrow "
    "auto-curving into a vault the moment it lands. Automatic, no hands.",
    "A lifestyle upgrade dial with 5-YEAR clicks — a hand turning it deliberately one notch, versus "
    "a ghost-hand drifting it constantly. On purpose vs by drift.",
    "Three crossed-out icons: stock-picking chart, hustle-clock, 4AM alarm. White frame, red X each. "
    "The rule needs none of them.",
    "The napkin folded into a paper crane lifting off — the math flies alone. Minimal poetic frame.",
    # WHY YOUR BRAIN PICKS LEO (53-58)
    "A brain icon leaning visibly toward Leo's glowing path on the fork diagram — pulled by a magnet "
    "labeled with a sparkle icon. Honest diagram, no shame framing.",
    "A raise notification bursting like a champagne bottle in hand — celebration physics. The feeling "
    "rendered literally.",
    "Marc's vault on a stage with zero audience — empty chairs, no camera flashes. The invisibility "
    "of the right choice, staged theatrically.",
    "Split ledger of pleasures: Leo's side full of small warm moments (dinners, trips, toasts) — "
    "Marc's side a single quiet number. Both REAL. The honest trade.",
    "A price tag hanging on the concept: two decades rendered as 20 gray calendar-years, each stamped "
    "with a plain 'average-looking' face icon. The real cost of freedom.",
    "A mirror splitting the frame: on one side the viewer-silhouette sees Leo's reflection smiling; "
    "the math sheet lies face-down below the mirror. Mirrors beat math — LAPIDARIA frame.",
    # TO BE FAIR TO LEO (59-62)
    "Leo raising a glass at a genuinely lovely dinner — warm, humanized, zero mockery. The fairness "
    "pivot needs him likable.",
    "A photo wall of Leo's twenties and thirties: real trips, real friends, real wine. Full color, "
    "genuinely good life. These were real.",
    "The single crack: Leo's path drawn as a beautiful moving walkway — that has no OFF button. "
    "A small 'stop' button crossed out at the handrail.",
    "A casino chip labeled with Leo's face icon sliding onto a table he never looked at — the bet "
    "placed without knowing. Quiet, ominous, elegant.",
    # WHICH BET (63-66)
    "The trophy question dissolved: a 'who was right?' trophy fading to gray, replaced by a mirror.",
    "The fork-in-the-road diagram rotated to face the VIEWER first-person — your two paths ahead, "
    "both lit. Empty walking shoes at the start.",
    "A conveyor belt under the viewer's shoes already moving slowly toward Leo's side — you're on a "
    "path even standing still. No hands on any controls.",
    "A giant incoming-mail icon glowing on the horizon of the fork: the next raise, rendered as the "
    "literal fork trigger. Countdown energy.",
    # CLOSE (67-71)
    "A calm desk at night, no chaos: just a single drawer slightly open with a folded napkin inside. "
    "Nothing else to do tonight.",
    "The drawer close-up: napkin resting ready next to a pen. Label-free. The pre-made decision as "
    "a physical object.",
    "The raise email notification arriving on a phone — and the drawer already sliding open by itself "
    "beside it. Decision meets moment.",
    "Marc and Leo as equal silhouettes on the horizon — no winner posing. Between them, only the "
    "napkin on the ground glowing slightly. It was never about the men.",
    "THE NAPKIN handed forward out of frame toward the viewer's hands — POV. Warm final light.",
    # TEASE (72-74)
    "Seven mystery card silhouettes fanned like a poker hand, face down, one glowing at position 4. "
    "Dark teaser palette.",
    "A supermarket aisle with a frozen silhouette mid-gesture at a shelf — a '4' chip glowing beside "
    "the hand. You did this this week.",
    "A THURSDAY calendar chip on white. Clean out.",
]

assert len(PROMPTS) == len(_flat) == 74, f"PROMPTS {len(PROMPTS)} vs beats {len(_flat)}"

BEATS = [(n, s, l, p) for (n, s, l), p in zip(_flat, PROMPTS)]

TOTAL = len(BEATS)
CHUNK = 19
parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

SECTION_STARTS = {}
_last = None
for b in BEATS:
    if b[1] != _last:
        SECTION_STARTS[b[0]] = b[1]
        _last = b[1]


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_pdf():
    styles = getSampleStyleSheet()
    H1  = ParagraphStyle('H1', parent=styles['Title'], fontSize=17, leading=22, alignment=TA_CENTER)
    H2  = ParagraphStyle('H2', parent=styles['Normal'], fontSize=12, leading=15, alignment=TA_CENTER, fontName='Helvetica-Bold')
    SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#444444'))
    META= ParagraphStyle('META', parent=styles['Normal'], fontSize=8, leading=11, alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    SBOX= ParagraphStyle('SBOX', parent=styles['Normal'], fontSize=8, leading=11, textColor=colors.HexColor('#555555'), spaceBefore=4, spaceAfter=8)
    PART= ParagraphStyle('PART', parent=styles['Heading2'], fontSize=12, leading=15, textColor=colors.HexColor('#B02A2A'), spaceBefore=14, spaceAfter=6)
    SECH= ParagraphStyle('SECH', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=2)
    BH  = ParagraphStyle('BH', parent=styles['Normal'], fontSize=10, leading=14, spaceBefore=6, spaceAfter=2)
    IMG = ParagraphStyle('IMG', parent=styles['Normal'], fontSize=8.5, leading=12, spaceAfter=2)
    DONE= ParagraphStyle('DONE', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#1E7A33'), fontName='Helvetica-Bold', spaceBefore=6)

    pdf_path = "/home/user/Claudeeee/V17_final_IMAGE_PROMPTS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=15*mm, bottomMargin=15*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 17", H2), Spacer(1, 4),
        Paragraph("IMAGE PROMPTS — VISUAL REFERENCE", H1), Spacer(1, 3),
        Paragraph(esc(TITLE), SUB), Spacer(1, 4),
        Paragraph(f"{TOTAL} beats · {len(parts)} parts · LEO vs MARC (personajes nuevos, sin Alex/Villain) · split-screens + curva", META),
        Spacer(1, 8),
        Paragraph(f"<b>STYLE PREAMBLE</b> — prepend to every prompt in Google Flow:<br/>{esc(STYLE)}", SBOX),
    ]
    for pidx, (a, b) in enumerate(parts, 1):
        flow.append(Paragraph(f"IMAGE PROMPTS — PART {pidx}/{len(parts)}  (Beats {a}–{b})", PART))
        for num, sec, narration, prompt in BEATS[a - 1:b]:
            if num in SECTION_STARTS:
                flow.append(Paragraph(f'<font color="#B02A2A"><b>── {esc(SECTION_STARTS[num])} ──</b></font>', SECH))
            block = [
                Paragraph(f'<font color="#B02A2A"><b>BEAT {num}</b></font>  <b><i>"{esc(narration)}"</i></b>', BH),
                Paragraph(f'<b>Image Prompt:</b> {esc(STYLE + " " + prompt)}', IMG),
            ]
            flow.append(KeepTogether(block))
        flow.append(Paragraph(f"PART {pidx} DONE — Beats {a}–{b} ✓", DONE))
        flow.append(Spacer(1, 6))
    doc.build(flow)
    print(f"Saved: {pdf_path} | {TOTAL} beats | {len(parts)} parts")


if __name__ == "__main__":
    build_pdf()
