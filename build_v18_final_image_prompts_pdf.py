#!/usr/bin/env python3
"""
VIDEO 18 — IMAGE PROMPTS · SEÑALES (banco: 7 Signs)
94 beats · Alex REDUCIDO AL MÁXIMO (regla Sección 9) — la mayoría de beats son objetos, manos,
pantallas y el checklist-contador. Alex solo en momentos de identidad. Brain Villain aislado puntual.
Motivo recurrente: EL CONTADOR — checklist vertical de 7 casillas que se va marcando en rojo.
"""

import sys
sys.path.insert(0, '/home/user/Claudeeee')
from build_v18_signs_bank_script import SECTIONS, TITLE

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

SUBTITLE = "NEUROCENTS · VIDEO 18"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines on every element, clean solid color "
    "fills, no gradients. ALEX appears ONLY where the prompt names him — most beats have NO "
    "character: objects, hands, phone screens and diagrams carry the frame. "
    "ALEX (when present): large beige oval head (#F5E6C8), transparent glass upper skull revealing "
    "pink cartoon Brain Villain (#E8A598), small black dot eyes, thin neutral mouth, black spiky "
    "hair, BLUE t-shirt (NOT RED), gray pants (NOT jeans). "
    "BRAIN VILLAIN may appear ISOLATED (no body/skull) where named: pink cartoon brain, heavy-lidded "
    "eyes, slight smirk, small teeth. "
    "RECURRING MOTIF — THE COUNTER: a vertical checklist card with 7 empty checkboxes that gains a "
    "bold RED check after each sign; always same design, bottom-right corner unless framed as hero. "
    "Palette: beige #F5E6C8 · pink #E8A598 · red checks/danger · green savings · white backgrounds. "
    "16:9, 1280x720."
)

_flat = []
_n = 1
for _sec, _lines in SECTIONS:
    for _l in _lines:
        _flat.append((_n, _sec, _l))
        _n += 1

PROMPTS = [
    # HOOK (1-9)
    "S17 OPENING [THUMBNAIL CONTINUITY]: extreme close-up of a hand holding a phone, banking app "
    "loading — and above it, one HALF-CLOSED EYE in close-up, flinching. The 7-checkbox COUNTER card "
    "appears faintly at the corner, all boxes empty. Alex NOT visible as full figure — just eye + hand.",
    "The loading spinner on the banking app frozen mid-spin; the half-second pause rendered as a "
    "held-breath frame. No characters.",
    "A fingerprint magnified under glass, turning slowly into a tiny paragraph of code. 'Evidence' "
    "as image. Minimal white.",
    "An old computer tower quietly running in a dark basement labeled by a piggy-bank icon — "
    "installation date dust-marked years ago. No consent checkbox was ever ticked: an unchecked "
    "'I agree' box floats beside it.",
    "Five... no — SEVEN faint fingerprints glowing on a white wall, arranged like the counter card.",
    "The COUNTER card hero-framed: seven empty checkboxes, crisp, waiting. Nothing else.",
    "A crowd of generic silhouettes walking; three fingerprints glow on most backs without them "
    "noticing. No Alex.",
    "A hand picks up a pen next to the COUNTER card. The game begins. POV framing — the viewer's hand.",
    "Checkbox #1 at the top pulses once with a warning shimmer; the other six wait in shadow below. "
    "Open-loop frame.",
    # SETUP (10-13)
    "Simple instruction diagram: sign card → mirror icon → pen ticking a box. Three-step how-to, "
    "clean icons, no characters.",
    "A fingerprint inside a magnifying glass with a NOT-guilty gavel crossed out beside it — "
    "information, not crime. White frame.",
    "A row of tiny quirk-sized icons (a wink, a shrug, a coffee cup) with one revealing a price tag "
    "shadow behind it. Small things casting expensive shadows.",
    "The pen hovers over the COUNTER. Start-line energy. POV hand again.",
    # SIGN 7 — ONE-EYE CHECK (14-20)
    "SIGN CARD 7 slides in: a minimal card with an eye-half-closed icon. Same card design for all "
    "seven signs. No characters.",
    "Sequence strip of three micro-frames: phone out → app opening → the flinch (eye squint) — "
    "the gesture everyone knows, drawn as anonymous close-ups.",
    "LAPIDARIA frame: a boxing glove made of numbers mid-punch toward the viewer, and a forearm "
    "braced in front of a face. You're not checking — you're bracing.",
    "Split: one relaxed open eye reading a number calmly / one squinted eye behind a raised guard. "
    "Control vs impact-prep.",
    "A tiny flashback vignette: a past bad-number moment (red balance glow) burning a small scar "
    "mark onto a brain icon. Origin of the flinch.",
    "ALEX appears (first time): braced comically behind his own phone like it might explode, "
    "Brain Villain inside the skull wearing a tiny helmet. Humor beat.",
    "THE COUNTER: checkbox #1 gets its bold red check. Satisfying click frame. Nothing else.",
    # SIGN 6 — SALE MATH (21-27)
    "SIGN CARD 6: percent-tag icon card slides in.",
    "A -50% price tag physically deposited into a piggy bank — the discount treated as income. "
    "Absurdity rendered literally.",
    "LAPIDARIA: split receipt — left shows 'saved €30' glowing happily; right shows the true line: "
    "'spent €70' in heavy black. Same receipt, flipped.",
    "A brain icon at a bank counter depositing a FEELING (a warm glow blob) while actual coins "
    "walk out the door behind it.",
    "The word-shape 'SALE' as a big red magnet pulling a shopping cart uphill — faster, not slower.",
    "A trophy case filled with discount tags instead of trophies; dust on all of them. Nobody got "
    "rich here.",
    "THE COUNTER: checkbox #2 red check. Click.",
    # SIGN 5 — ROUND-DOWN MEMORY (28-34)
    "SIGN CARD 5: a rounded-down arrow icon card.",
    "A speech bubble saying '20... 25?' floating over a table of last night's remains (two glasses, "
    "a bill folded). No faces.",
    "The real receipt unfolds under a lamp: €38 in sharp focus. Short, hard frame.",
    "A tiny accountant-desk inside a head silhouette: the memory-clerk stamping every receipt with "
    "a DOWN arrow, confident as a CFO. Humor.",
    "A one-way street sign where all numbers flow downhill only. Minimal diagram.",
    "LAPIDARIA: a photo album where every money-memory photo has been lightly airbrushed — the "
    "brain protecting its story. A brush still hovers.",
    "THE COUNTER: checkbox #3 red check.",
    # CTA (35-36)
    "The COUNTER with 3 red checks next to a clean subscribe button — 'if you've already ticked "
    "three' visualized. Minimal.",
    "A dark pattern-shape being pulled into a spotlight by a hand. Weekly ritual icon strip below.",
    # SIGN 4 — CHECKOUT SACRIFICE (37-44)
    "SIGN CARD 4: shopping-cart icon card. (The supermarket one.)",
    "A supermarket checkout belt POV: full cart, the total display glowing slightly too bright. "
    "Anonymous hands only.",
    "One hand lifts a small item out of the cart in slow-motion framing.",
    "The €2 chocolate bar placed back on the shelf with ceremonial care — tiny altar lighting. "
    "Ritual complete. Humor via staging.",
    "The rest of the cart — €60 of stuff — rolls on happily toward the register, waving goodbye "
    "to the chocolate.",
    "LAPIDARIA: a receipt printing the line-item 'FEELING OF CUTTING: €0' between real items.",
    "Brain icon holding a signed PERMISSION SLIP for the full cart, stamped by the sacrificed "
    "chocolate. Diagram-clean.",
    "THE COUNTER: checkbox #4 red check — this one lands harder: slight zoom emphasis.",
    # MID REFRAME (45-48)
    "The COUNTER at 3-4 checks held in a hand, trembling slightly — then a steadying second hand. "
    "'Hold on' framing.",
    "A pair of glasses lifting off a table by themselves — the act of SEEING as the rare skill.",
    "Split: a crowd walking past a wall of patterns blindfolded / one figure stopped, looking. "
    "ALEX as the one looking — second appearance, identity moment.",
    "The COUNTER redrawn as a folded MAP with the checks as route markers. Sentence → map reframe.",
    # SIGN 3 — COUNTDOWN CLOCK (49-55)
    "SIGN CARD 3: a countdown-clock icon card.",
    "A mental HUD overlay: '9 days to payday' floating crisp and bright over a blurred kitchen. "
    "Instant-recall rendering.",
    "The same HUD asked for 'last year total spending': static noise, no signal. Split of clarity "
    "vs fog.",
    "A ruler measuring money in tiny day-units versus a second ruler in year-units gathering dust.",
    "LAPIDARIA: two equations carved side by side — short math on a napkin scrap vs long math on "
    "a stone tablet.",
    "A telescope pointed at the floor (10 days ahead) next to one pointed at the horizon (10 years) "
    "— only one has a user queue.",
    "THE COUNTER: checkbox #5 red check.",
    # SIGN 2 — 'WHEN' PLAN (56-62)
    "SIGN CARD 2: a waiting-room-chair icon card.",
    "Three thought bubbles queued like tickets: raise-arrow bubble, calm-waters bubble, new-year "
    "bubble — all stamped WHEN in soft gray.",
    "A plan document whose first word is a blank space shackled to someone else's hand offscreen. "
    "Control lives elsewhere.",
    "LAPIDARIA: a waiting room with plans sitting in chairs, magazines from years ago on the table. "
    "One plan has grown a beard.",
    "A €0 price tag on the waiting-room door — waiting costs nothing today. The brain icon happily "
    "pays it.",
    "Split: a tiny door labeled with a small 'now' icon, ajar with light behind it / the grand 'WHEN' "
    "gate, closed, ornate, painted on a wall.",
    "THE COUNTER: checkbox #6 red check.",
    # SIGN 1 — THE CEILING (63-71)
    "SIGN CARD 1 slides in slower, heavier: a low-ceiling icon card. Tone shift: dimmer staging.",
    "An empty chair facing the viewer with a soft spotlight: the try-it-now exercise frame. "
    "Nothing else on screen.",
    "A wealthy-life collage assembling — then the flashy items (car, beach) dissolve, leaving just "
    "a calm silhouette at a kitchen table with morning light and no dread.",
    "The assembled picture GLITCHES — a subtle push-back ripple across the frame.",
    "A small speech bubble, childlike font-shape, whispering from the frame's edge into the scene. "
    "No text needed: the bubble's tail comes from below, from the past.",
    "A warm-dim childhood kitchen: small table, old radio, a child-height view of adults' hands "
    "counting coins at month's end. THE frame of the video. No faces.",
    "A ruler drawn on a doorframe — but instead of height marks, tiny € marks stop at a low line "
    "labeled by a family-photo icon. Inherited ceiling.",
    "LAPIDARIA: a framed photo of 'wealthy you' hanging on a wall — but the reflection in the "
    "glass shows someone else's silhouette. Someone else's photo.",
    "THE COUNTER: checkbox #7 red check — the card is full. Held beat. Then the counter tilts "
    "slightly, heavier than before.",
    # THE COUNT (72-77)
    "The full COUNTER card center-frame, all seven red checks. A hand holds it like a diagnosis. "
    "POV.",
    "Zone strip 0-2: a shelf with a few ordinary habit-jars, tidy, unthreatening.",
    "Zone strip 3-5: the jars connected by red string into a WALL-BOARD pattern — a program "
    "revealed, conspiracy-board style, but it thinks it's protecting you: a tiny shield icon at center.",
    "Zone strip 6-7: an autopilot cockpit, engaged since childhood — a child's drawing taped to "
    "the controls. First time meeting the pilot: the pilot seat slowly turning.",
    "A comment-box mock-up with a large '?/7' field glowing, surrounded by dozens of tiny matching "
    "fingerprint icons from other commenters. Comment-engine frame.",
    "A brain icon reaching for a big DELETE key in the corner of the frame — caught mid-reach. "
    "Bridge tension.",
    # DELETE ATTEMPT (78-82)
    "A thought forming as a slow bubble over a dark background — half-materialized.",
    "The bubble crystallizes into a polite stamp: a calm, friendly, FINAL seal pressing down. "
    "'Interesting' as a rubber stamp.",
    "LAPIDARIA: an archive room where stamped 'interesting' boxes are wheeled into a furnace "
    "labeled with a moon icon (tonight). Bureaucratic forgetting.",
    "The seven-check COUNTER flagged as a THREAT on a brain-security monitor — red alert boxes "
    "around it. The programs defending themselves.",
    "The stamp hovers over THIS video's own thumbnail mock — scheduled for tonight's furnace. "
    "Fourth-wall pressure frame.",
    # CLOSE (83-90)
    "Everything from the video dissolves to ash EXCEPT the counter card with your number — it "
    "stays solid, glowing faintly. What survives.",
    "Triptych of tomorrow: checkout belt / banking app / SALE sign — each with a tiny red check "
    "ghost hovering, waiting to be noticed mid-act.",
    "THE CATCH rendered: a hand catching a falling pattern-card mid-air — frozen at the exact "
    "half-second. High-speed-photo staging.",
    "Two crossed-out icons (budget binder, resolution scroll) and one glowing icon: the catching "
    "hand. Where change actually lives.",
    "A warning triangle — but soft, rounded: the DON'T PUNISH frame. A whip icon crossed out.",
    "LAPIDARIA: the programs drawn as small creatures at a feeding bowl labeled with a shame-cloud "
    "icon — bowl being taken away; a curiosity-magnifying-glass replaces it. They starve politely.",
    "Seven sign-cards fanned + the counter + a single OPEN EYE above them. Inventory of what the "
    "viewer now owns.",
    "A sunrise over the counter card planted like a flag on a small hill. The whole beginning. "
    "Warm, quiet.",
    # TEASE (91-94)
    "A phone mid-send: the counter card flying as a message to a contact avatar with a shopping-"
    "cart badge — the friend who does #4 weekly. Warm share frame.",
    "Teaser: a timeline of money-objects fading from tactile coins → paper → card → glass tap — "
    "the year money stopped hurting, rendered as an archaeology strip.",
    "A single coin held up to the light like a relic, and a modern hand flinching at a glowing "
    "number in the background. Story bookends.",
    "A THURSDAY calendar chip on white. Out.",
]

assert len(PROMPTS) == len(_flat) == 94, f"PROMPTS {len(PROMPTS)} vs beats {len(_flat)}"

BEATS = [(n, s, l, p) for (n, s, l), p in zip(_flat, PROMPTS)]

TOTAL = len(BEATS)
CHUNK = 24
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

    pdf_path = "/home/user/Claudeeee/V18_final_IMAGE_PROMPTS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=15*mm, bottomMargin=15*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 18", H2), Spacer(1, 4),
        Paragraph("IMAGE PROMPTS — VISUAL REFERENCE", H1), Spacer(1, 3),
        Paragraph(esc(TITLE), SUB), Spacer(1, 4),
        Paragraph(f"{TOTAL} beats · {len(parts)} parts · Alex reducido (solo 2 apariciones) · motivo COUNTER de 7 casillas", META),
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
