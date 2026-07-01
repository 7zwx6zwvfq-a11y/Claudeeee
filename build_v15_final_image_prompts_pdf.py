#!/usr/bin/env python3
"""
VIDEO 15 — IMAGE PROMPTS · BRIEF v3.1
94 beats · BLUE t-shirt · S17 thumbnail continuity · Visual-first rule
Beat 1 format: S17 OPENING THUMBNAIL CONTINUITY
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

TITLE    = "Why Smart People Can't Save Money (Do This Once Instead)"
SUBTITLE = "NEUROCENTS · VIDEO 15"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines on every element, "
    "clean solid color fills, no gradients. "
    "Recurring main character ALEX: large beige oval head with transparent glass upper skull "
    "revealing a pink cartoon Brain Villain inside, small black dot eyes, thin neutral mouth, "
    "black spiky hair, BLUE t-shirt (NOT RED — verify every time), gray pants (NOT jeans). "
    "Brain Villain: pink cartoon brain character, heavy-lidded eyes, slight smirk, small teeth — "
    "ALWAYS inside Alex's skull, never floating outside. "
    "Palette: beige skin #F5E6C8 · pink brain #E8A598 · blue t-shirt · gray pants · "
    "green: savings/gains/automation · red: loss/danger/manual effort · white: diagram scenes. "
    "16:9, 1280x720."
)

# Format: (beat_num, section, narration, image_prompt)
BEATS = [

    # ═══════════════════════════════════════════════════════
    # HOOK — 10 beats — S4 Afirmación Contraintuitiva + S17 Continuity
    # ═══════════════════════════════════════════════════════

    (1, "HOOK — PRIMEROS 5 SEGUNDOS",
     "You're smart. So why can't you save money?",
     "BEAT 1 — OPENING [S17 THUMBNAIL CONTINUITY · S4 CONTRAINTUITIVA]: "
     "Alex at his desk surrounded by evidence of intelligence: a stack of read finance books "
     "(worn spines, bookmarks), a laptop with a budgeting app open, a framed diploma on the wall. "
     "In his hand: phone showing SAVINGS: €140 in bold red. "
     "Expression: wide eyes, eyebrows raised — the dissonance face. Smart. Still broke. "
     "Brain Villain ACTIVE inside skull: reclining comfortably, smirking — completely unthreatened by the books. "
     "Camera: MEDIUM CLOSE-UP, slight low angle — phone and books both visible. "
     "Motion: ZOOM IN FAST toward the €140 on the phone. "
     "NOTE: Viewer who just saw thumbnail ('SMART. STILL BROKE.') must recognize this scene in under 5 seconds. "
     "The books + the €140 ARE the thumbnail promise. No introduction. The contradiction IS the opening."),

    (2, "HOOK",
     "You've read the books. You understand compound interest. You could explain inflation at a dinner party.",
     "Alex at a dinner party, mid-explanation, one hand gesturing confidently. Above his head: a small "
     "thought bubble with a clean rising compound-interest curve. Two guest figures listen, impressed. "
     "Alex expression: fluent, in his element. Brain Villain inside skull: bored, examining its nails — "
     "knowledge changes nothing for it."),

    (3, "HOOK",
     "And your savings account has €140 in it.",
     "Extreme close-up of Alex's phone: banking app, SAVINGS ACCOUNT: €140 in bold red digits. "
     "Reflected faintly in the screen: the stack of finance books from Beat 1. "
     "The contrast is the whole image. No other elements. White background."),

    (4, "HOOK",
     "Here's the uncomfortable part: it's not because you lack discipline.",
     "Alex at 6:00 AM: gym bag on shoulder, completed to-do list in hand — every box checked. "
     "Clock shows 6:00 AM. Evidence of discipline everywhere. "
     "Brain Villain inside skull: shrugging — discipline was never the battlefield. "
     "A faint red X floats over a 'discipline' dumbbell icon: wrong suspect."),

    (5, "HOOK",
     "It's because you keep trying.",
     "THE TWIST IMAGE: Alex straining at a heavy manual crank connected to a savings meter — "
     "sweating, both hands gripping, the meter needle barely moving. "
     "His posture: maximum effort, minimum result. "
     "Brain Villain inside skull: watching with amused patience — it knows the crank resets every night. "
     "The effort itself is the trap. White background, single spotlight on the crank."),

    (6, "HOOK",
     "Trying is manual. And manual always loses to automatic.",
     "Split frame: LEFT — Alex hand-cranking the savings meter, exhausted, needle low. "
     "RIGHT — a compact green machine humming by itself, its meter steadily climbing, no one touching it. "
     "Same meter design both sides. Only the power source differs: human vs automatic."),

    (7, "HOOK",
     "Every drain on your money runs automatically. Your defense runs on willpower.",
     "Wide shot: five mechanical arms (each with a small icon — card, gift, subscription loop, mirror, calendar) "
     "reaching toward a pile of coins. Facing them: Alex alone, holding a small wooden shield. "
     "The asymmetry is visual — five machines vs one tired human. No text labels."),

    (8, "HOOK",
     "That's not a fair fight. It was never a fair fight.",
     "Same scene from Beat 7, pulled back further: Alex tiny in frame, the five mechanical arms "
     "looming larger, moving in coordinated rhythm. His shield looks smaller from this distance. "
     "Flat clinical light — this is just the arithmetic of the situation."),

    (9, "HOOK",
     "One decision ends it. Made once. On a calm morning.",
     "Clean white frame: a single green toggle switch, large, centered. Alex's hand hovering over it, calm. "
     "Soft warm morning light. No machines, no chaos — the visual opposite of Beats 7-8. "
     "Brain Villain inside skull: suddenly alert, leaning forward — this switch worries it."),

    (10, "HOOK",
     "Your brain is already listing reasons this won't work. Good. That's the part we dismantle last.",
     "Close-up on skull interior: Brain Villain rapidly writing a list on a small clipboard — "
     "each entry a crossed-out lightbulb or warning icon (objections forming, no readable text). "
     "Villain expression: focused, defensive, working fast. "
     "Alex exterior: calm half-smile — he knows the list is coming and he's ready."),

    # ═══════════════════════════════════════════════════════
    # WHY THE COMMON SOLUTION FAILS — 10 beats
    # ═══════════════════════════════════════════════════════

    (11, "WHY THE COMMON SOLUTION FAILS",
     "Alex has tried everything. Watch.",
     "Alex pulling open a large desk drawer. Inside: a graveyard of abandoned methods — "
     "a phone with a budgeting app icon, a stack of labeled cash envelopes, a rolled-up spreadsheet printout, "
     "a piggy bank with dust on it. Each item slightly faded. Museum of good intentions."),

    (12, "WHY THE COMMON SOLUTION FAILS",
     "January: a budgeting app. Every expense categorized. Color-coded.",
     "Phone screen close-up: budgeting app with beautiful color-coded categories, pie chart, JANUARY header. "
     "Alex's finger mid-tap, expression: fresh optimism. Calendar page beside phone: JAN 1 circled in green."),

    (13, "WHY THE COMMON SOLUTION FAILS",
     "It lasted nineteen days.",
     "The same January calendar: days 1-19 checked in green. Day 20 onward: blank, untouched. "
     "The app icon in the corner now has faint dust particles. No text labels — the abrupt stop tells it."),

    (14, "WHY THE COMMON SOLUTION FAILS",
     "March: a no-spend month. He made it to day twelve.",
     "MARCH calendar: red X marks crossing out days 1-12, then nothing. Day 13 has a small shopping bag icon — "
     "the quiet surrender. Alex in background, looking away from the calendar."),

    (15, "WHY THE COMMON SOLUTION FAILS",
     "June: the 50/30/20 rule. The spreadsheet was beautiful.",
     "Laptop screen: an immaculate spreadsheet — clean rows, a perfect 50/30/20 pie chart in three colors. "
     "Alex beside it, arms crossed, genuinely proud. This is his best work. JUNE calendar in corner."),

    (16, "WHY THE COMMON SOLUTION FAILS",
     "The spreadsheet is still beautiful. It just doesn't match reality anymore.",
     "Split frame: LEFT — the pristine spreadsheet, glowing, perfect. RIGHT — a real bank statement, "
     "messy, numbers that don't match, red entries. A jagged gap between the two panels. "
     "Alex looks from one to the other, deflated."),

    (17, "WHY THE COMMON SOLUTION FAILS",
     "Every method failed the same way. Not with a crash — with a quiet fade.",
     "Three icons in a row — budgeting app, no-spend calendar, spreadsheet — each progressively "
     "more transparent left to right, dissolving into the white background. No explosion, no drama. "
     "Just fade. Alex watches the dissolve, resigned."),

    (18, "WHY THE COMMON SOLUTION FAILS",
     "Because every method had the same flaw.",
     "The three faded method icons from Beat 17 — now a single red crack runs beneath all three, "
     "connecting them like a fault line under buildings. Same crack, three casualties."),

    (19, "WHY THE COMMON SOLUTION FAILS",
     "They all required Alex to make the right decision. Every day. Forever.",
     "Alex standing at the start of an endless corridor of identical doors, stretching to the horizon — "
     "each door with a small decision icon (coffee cup, cart, card). The corridor never ends. "
     "Perspective vanishing point. Alex's posture: shoulders dropping as he takes it in."),

    (20, "WHY THE COMMON SOLUTION FAILS",
     "About a hundred and fifty money decisions a month. And he had to win all of them.",
     "Large bold counter: '150' dominating the frame. Below it, a small scoreboard: "
     "REQUIRED: 150/150. Alex beside the scoreboard, exhausted just reading it. "
     "Brain Villain inside skull: grinning — it only needs him to lose once."),

    # ═══════════════════════════════════════════════════════
    # THE MECHANISM — 16 beats
    # ═══════════════════════════════════════════════════════

    (21, "THE MECHANISM",
     "Saying no to a purchase saves money exactly once.",
     "Alex at a shop counter, hand raised in a polite 'no' gesture. A single coin drops into a small jar "
     "beside him. One coin. The jar is nearly empty. The effort-to-result ratio is the image."),

    (22, "THE MECHANISM",
     "And you get no points for the nos.",
     "A scoreboard showing ZERO. Beside it: a tall pile of small green 'no' checkmarks Alex has accumulated — "
     "but the scoreboard doesn't count them. Alex points at the pile, then at the zero, confused. "
     "The game doesn't reward defense."),

    (23, "THE MECHANISM",
     "Thirty correct nos. One tired yes. The yes wins.",
     "Domino visual: thirty small green dominoes standing in a neat line — and one large red domino "
     "falling at the end, knocking the entire line flat. Clock in corner: 11 PM. "
     "The one tired yes undoes everything. No text labels."),

    (24, "THE MECHANISM",
     "Now remember the five drains.",
     "The five drain slots from Video 14 reappear — dimly lit, familiar: five vertical slots in a column. "
     "Alex turns toward them with recognition. Brain Villain inside skull: straightens up — "
     "its greatest hits are being discussed."),

    (25, "THE MECHANISM",
     "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
     "The five slots light up in sequence, each with its label: CARD GAP · REWARD DRAIN · INVISIBLE DRAIN · "
     "SOCIAL SPENDING · PRE-SPEND. Rapid highlight sequence, one pulse per name. V14 continuity — "
     "same slot design as the previous video."),

    (26, "THE MECHANISM",
     "If you haven't seen that video, it's the one right before this. One detail matters here:",
     "Small video-card thumbnail floating in corner (generic previous-video card with the five slots visible). "
     "Alex points past it toward one highlighted detail: a small gear icon glowing under the slots. "
     "The gear is the detail that matters."),

    (27, "THE MECHANISM",
     "All five run automatically. Zero effort. Zero decisions. Zero fatigue.",
     "The five slots now shown with spinning gears beneath each one — all turning in unison, "
     "no hands, no operator. Three small counters nearby all reading ZERO (effort, decisions, fatigue icons). "
     "The machine room of the brain."),

    (28, "THE MECHANISM",
     "The Card Gap doesn't get tired. The Pre-Spend doesn't take weekends off.",
     "Night scene: Alex asleep in bed, peaceful. Through the window of the frame, the five gears "
     "still spinning in the dark, faintly glowing. A small SATURDAY calendar tag. "
     "The drains work the night shift and the weekend."),

    (29, "THE MECHANISM",
     "Your drains are machines. Your savings plan is a to-do list.",
     "Split frame: LEFT — five interlocked spinning gears, solid, industrial, green-lit. "
     "RIGHT — a paper to-do list pinned to a corkboard: a single checkbox with a piggy bank icon, unchecked, "
     "the paper slightly curling. Machine vs paper. The mismatch is the message."),

    (30, "THE MECHANISM",
     "Machines beat to-do lists. Every time. In every brain.",
     "The gears from the left panel physically shredding the paper to-do list — strips of paper "
     "falling from the mechanism. Not violent, just mechanical. Inevitable. "
     "Alex watches, hands in pockets — he's seen this happen to every list he's made."),

    (31, "THE MECHANISM",
     "This isn't laziness. This is arithmetic.",
     "Clean white diagram: a simple visual equation — [gear icon] > [paper checklist icon]. "
     "Below it, no judgment imagery: just the two icons on a balance scale, gear side down (heavier). "
     "Clinical, neutral, mathematical."),

    (32, "THE MECHANISM",
     "And this is why being smart doesn't help.",
     "Alex wearing a graduation cap, standing beside the shredded remains of the to-do list. "
     "The cap changes nothing about the shredder. His expression: the slow realization. "
     "Brain Villain inside skull: taps the gear approvingly."),

    (33, "THE MECHANISM",
     "Intelligence improves each decision. It doesn't reduce how many you have to make.",
     "Two meters side by side: DECISION QUALITY dial — needle high, green. DECISION COUNT counter — "
     "still locked at 150, unchanged, red. Alex's hand on the quality dial: it turns. "
     "The count doesn't. The count is the problem."),

    (34, "THE MECHANISM",
     "A smarter driver still gets tired on a ten-hour drive.",
     "Night highway scene: a car on an endless road, headlights on. Inside, driver silhouette with a "
     "graduation cap — and a fuel-gauge-style fatigue meter above the car dropping toward empty. "
     "The cap doesn't refill the gauge. Simple, cinematic, flat cartoon."),

    (35, "THE MECHANISM",
     "So the real question was never: how do I make better money decisions?",
     "A question card floating in frame — a lightbulb-and-coin icon representing 'better decisions' — "
     "with a thick red X stamped across it. Alex swipes it aside with one hand. Wrong question."),

    (36, "THE MECHANISM",
     "It's: how do I need fewer? Ideally — zero.",
     "The counter from Beat 33 — now rolling down: 150 → 80 → 20 → 0. The digits mid-roll, blurring toward zero. "
     "Alex watching the counter with the first genuinely hopeful expression of the video. "
     "Brain Villain inside skull: alarmed for the first time."),

    # ═══════════════════════════════════════════════════════
    # CTA — beats 37-38 = 39% ✅
    # ═══════════════════════════════════════════════════════

    (37, "CTA",
     "If your brain is doing this to you right now — subscribe.",
     "Alex looks directly at camera — fourth wall break. Expression: knowing, complicit. "
     "Brain Villain peeks from behind the skull glass with a slightly defensive look — it doesn't want this. "
     "Clean red subscribe button icon below, minimal style. White background."),

    (38, "CTA",
     "We break down a new pattern every week. It's free. And it might save you more than you think.",
     "Small visual: weekly calendar with a Neurocents-style brain icon appearing on each week — "
     "consistent, trustworthy rhythm. Alex nods once, already turning back toward the counter at zero. "
     "CTA done, momentum preserved."),

    # ═══════════════════════════════════════════════════════
    # MECHANISM CONCLUSION — 3 beats
    # ═══════════════════════════════════════════════════════

    (39, "MECHANISM CONCLUSION",
     "So here's the pivot: stop trying to save money.",
     "THE SCANDALOUS FRAME: Alex releasing the manual crank from Beat 5 — letting go, stepping back, "
     "shaking out his tired hands. Not defeat: relief. The crank sits abandoned. "
     "Brain Villain inside skull: confused — this isn't surrender, and it doesn't know what it is yet."),

    (40, "MECHANISM CONCLUSION",
     "Trying is the strategy that's been failing for years.",
     "The drawer of abandoned methods from Beat 11 — now being calmly closed by Alex's hand. "
     "Final. No nostalgia. The app, the envelopes, the spreadsheet disappear into the dark drawer."),

    (41, "MECHANISM CONCLUSION",
     "Replace trying with something that doesn't need you.",
     "A curtain-reveal tease: behind a half-drawn curtain, the silhouette of a small green machine glowing softly. "
     "Alex's hand on the curtain edge, about to pull. Brain Villain pressing against the skull glass to see. "
     "Curiosity gap at maximum."),

    # ═══════════════════════════════════════════════════════
    # THE DECISION — 17 beats
    # ═══════════════════════════════════════════════════════

    (42, "THE DECISION",
     "The one decision.",
     "Minimal frame: the single green toggle switch from Beat 9, centered, large, alone on pure white. "
     "Nothing else. Two words of narration, one object on screen. Maximum weight."),

    (43, "THE DECISION",
     "The morning your salary arrives, a fixed amount leaves your account. Automatically.",
     "Bank app diagram: salary notification arrives (green arrow IN) — and instantly a second arrow (green) "
     "splits off toward a separate box, automatic, same moment. Morning light palette. "
     "The split happens at the moment of arrival, not later."),

    (44, "THE DECISION",
     "Before you see it. Before anything can be calculated about it.",
     "Alex still asleep in bed, early morning. On the nightstand: his phone lighting up with the transfer "
     "confirmation — the arrow already fired. Brain Villain inside sleeping Alex's skull: also asleep. "
     "The transfer happened while both of them were unconscious. That's the point."),

    (45, "THE DECISION",
     "A standing transfer. Set up once. Ten minutes on a calm Sunday.",
     "Alex on his sofa, Sunday morning, coffee in hand, phone in the other — calmly tapping through "
     "a standing-order setup screen. Relaxed posture, soft light, plant in background. "
     "A small '10 MIN' clock icon in corner. This is the entire cost of the system."),

    (46, "THE DECISION",
     "Not at the end of the month. There is no end of the month — you've seen your balance.",
     "Calendar page where days 25-31 are literally missing — torn away, ragged edge. "
     "A small empty-wallet icon sits where day 28 used to be. Dark humor visual. "
     "Alex shrugs at the calendar: we both know."),

    (47, "THE DECISION",
     "Hour zero. The morning it lands.",
     "Clock face at early morning, first light through a window. A single green transfer arrow fires "
     "across the frame at the exact moment. Precision timing visual — the arrow beats everything else awake."),

    (48, "THE DECISION",
     "Where does it go? A separate account. Different bank. No card attached.",
     "Diagram: a second bank icon on an island, surrounded by a moat. A pair of scissors cutting a card "
     "in half above it — no card exists for this account. The money's new home is deliberately remote. "
     "Clean white diagram style."),

    (49, "THE DECISION",
     "If reaching the money takes three days and two passwords, your 11 PM brain can't touch it.",
     "Night scene: tired 11 PM Alex (glazed eyes, phone glow) looking across the moat at the island bank. "
     "Between him and it: a raised drawbridge, two padlock icons, a '3 DAYS' hourglass. "
     "His shoulders drop — too far. He gives up and goes to bed. The friction wins. Designed friction."),

    (50, "THE DECISION",
     "How much? Smaller than feels impressive. €100. Even €50.",
     "Two modest green amount cards: €100 and €50 — small, solid, unglamorous. "
     "Beside them, a crossed-out oversized €800 card (too heroic, will fail). "
     "Alex points at the small ones. Sustainable beats impressive."),

    (51, "THE DECISION",
     "The amount is not the point. The automation is the point. You can raise it later.",
     "A small gear stamping the transfer arrow onto a calendar — month after month, identical marks "
     "repeating across the months. A small up-arrow beside the amount shows it can grow later. "
     "The repetition is the hero of this image, not the number."),

    (52, "THE DECISION",
     "Now watch what one transfer does to all five drains.",
     "Showdown framing: the five drain slots from V14 lined up on the right — and a single green transfer "
     "arrow entering from the left, calm and steady. Alex watches from the corner. "
     "Brain Villain grips the skull glass. Five vs one — but this time the one is automatic too."),

    (53, "THE DECISION",
     "The Card Gap: you can't tap money that isn't in the account.",
     "A contactless card taps against an account box — but the section where the money used to be "
     "is visibly empty, already moved to the island vault. The tap lands on nothing. "
     "CARD GAP slot dims to grey. One down."),

    (54, "THE DECISION",
     "The Reward Drain calculates what you deserve from the balance it sees. That balance just got smaller.",
     "Brain Villain at its calculator recalculating 'deserved extra' — but the visible balance feeding "
     "the calculation is smaller now. The result on the calculator shrinks accordingly. "
     "Villain shakes the calculator, confused. REWARD DRAIN slot dims. Two down."),

    (55, "THE DECISION",
     "The Invisible Drain keeps running — but it drains the leftovers now, not your future.",
     "The subscription siphon still running (honest visual — it doesn't stop) — but it now draws from "
     "a small 'leftovers' pool, while a protected vault labeled with a lock icon sits untouched behind the moat. "
     "INVISIBLE DRAIN slot half-dims. Contained, not killed. Honesty is the credibility."),

    (56, "THE DECISION",
     "Social Spending: the ghost audience can't order from an account they can't see.",
     "The translucent ghost audience from V14 peering at Alex's bank app — but the vault account "
     "doesn't appear on the screen at all. The ghosts shrug and fade further. "
     "SOCIAL SPENDING slot dims. Four down."),

    (57, "THE DECISION",
     "And the Pre-Spend? It still runs. Your brain still allocates everything in advance.",
     "Brain Villain at its allocation desk, still working, still assigning arrows — "
     "but now it allocates a visibly smaller pool. The machine runs; the territory shrank. "
     "PRE-SPEND slot flickers but stays lit. The last one doesn't die."),

    (58, "THE DECISION",
     "But the first allocation already happened. You made it months ago. On purpose. You didn't stop the Pre-Spend — you got there first.",
     "THE LINE OF THE VIDEO: timeline diagram — Alex's green transfer flag planted at the START of the "
     "timeline, BEFORE the Brain Villain's allocation spike. The Villain arrives at the timeline to find "
     "the flag already there. Its posture: caught, out-planned. Alex's flag was first. "
     "This is the checkmate frame — give it space, minimal elements."),

    # ═══════════════════════════════════════════════════════
    # THE SCIENCE — 12 beats
    # ═══════════════════════════════════════════════════════

    (59, "THE SCIENCE",
     "This is the most replicated finding in savings research. Not a hack. A law.",
     "A column of identical small study icons stacking up like bricks — replication after replication, "
     "same result each time. The stack forms a solid pillar. Clean academic white background."),

    (60, "THE SCIENCE",
     "Madrian and Shea. Harvard. 2001.",
     "Clean institutional label card: 'MADRIAN & SHEA / HARVARD / 2001' in bold black block letters. "
     "Small toggle-switch icon beneath the names — the default switch. White background. "
     "Text IS the prop here."),

    (61, "THE SCIENCE",
     "They studied one company that changed one thing about its retirement plan.",
     "A single office building icon. Beside it: one small switch being flipped — just one. "
     "Everything else about the building identical before and after. Minimal diagram."),

    (62, "THE SCIENCE",
     "Before: joining required a decision. A form. An enrollment meeting.",
     "Obstacle-course diagram: employee silhouette at left — then a form icon, a meeting-room icon, "
     "a signature icon — hurdles between the employee and the savings plan door at right. "
     "The path requires effort. Some silhouettes turn back."),

    (63, "THE SCIENCE",
     "Thirty-seven percent of employees were saving.",
     "Bar chart: a modest grey-blue bar rising to 37% level. A row of ten employee silhouettes below — "
     "about four highlighted, six greyed out. No y-axis text — the bar height and the silhouettes tell it."),

    (64, "THE SCIENCE",
     "After: everyone was enrolled by default. Same plan. Same money. Leaving took one form.",
     "The same diagram reversed: the savings plan door now stands OPEN by default, employees walking "
     "straight through — and one small exit form off to the side for anyone who wants out. "
     "The hurdles moved from entry to exit."),

    (65, "THE SCIENCE",
     "Eighty-six percent.",
     "The bar chart from Beat 63 — now a tall green bar at 86% beside the modest 37% bar. "
     "The gap between them is the entire story. Nearly nine of ten silhouettes highlighted below. "
     "Number as prop, nothing else."),

    (66, "THE SCIENCE",
     "Thirty-seven to eighty-six. No raise. No bonus. No motivational seminar.",
     "Both bars side by side. Above the gap: three crossed-out icons — money bag (raise), gift (bonus), "
     "podium (seminar). None of the usual suspects caused this. The X marks eliminate them one by one."),

    (67, "THE SCIENCE",
     "Nobody became more disciplined that year.",
     "The same row of employee silhouettes shown twice — before and after — completely identical figures, "
     "same postures, same faces. Nothing about the people changed. Arrow between the two rows: '='. "
     "The people are the constant; the default is the variable."),

    (68, "THE SCIENCE",
     "The decision moved from 'every payday, forever' to 'once.'",
     "Diagram: LEFT — an infinite calendar loop icon (payday repeating forever, spiral). "
     "RIGHT — a single dot labeled with a one-time checkmark. A clean arrow from loop to dot. "
     "The compression of infinite decisions into one is the visual."),

    (69, "THE SCIENCE",
     "Defaults beat decisions. In every study since. In every country it's been tested.",
     "Simplified world map, flat cartoon style: small green toggle-switch dots lighting up across "
     "different countries, one after another — same result everywhere. No country labels needed."),

    (70, "THE SCIENCE",
     "You can't join their plan. But the transfer copies the mechanism exactly.",
     "Two mirrored diagrams side by side: LEFT — the company's auto-enrollment switch. "
     "RIGHT — Alex's standing transfer switch, identical design, home-sized. "
     "An equals sign between them. Alex's hand rests on his own switch."),

    # ═══════════════════════════════════════════════════════
    # BRAIN VILLAIN'S LAST TRICK — 11 beats (template obligatorio)
    # ═══════════════════════════════════════════════════════

    (71, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain has one response to this transfer.",
     "Brain Villain inside skull, arms crossed, one finger now raised — it has prepared its counter. "
     "Expression: deliberate, strategic, not panicked. The clipboard from Beat 10 is in its other hand. "
     "Close-up on skull. Alex exterior: waiting."),

    (72, "BRAIN VILLAIN'S LAST TRICK",
     "You're feeling it right now.",
     "Alex looking directly at the viewer — fourth wall break. Inside his skull, the Brain Villain "
     "ALSO looks directly at the viewer. Both aware of the audience simultaneously. "
     "The Villain knows the viewer is feeling the objection too."),

    (73, "BRAIN VILLAIN'S LAST TRICK",
     "Not doubt. Something quieter.",
     "Brain Villain seated calmly in a small armchair inside the skull — reasonable posture, hands folded, "
     "nothing aggressive. The resistance doesn't look like resistance. It looks sensible. "
     "Soft, non-threatening light."),

    (74, "BRAIN VILLAIN'S LAST TRICK",
     "Something that sounds like prudence: 'What if I need that money?'",
     "Speech bubble from the skull: 'WHAT IF I NEED THAT MONEY?' — text IS the prop. "
     "The bubble is drawn soft-edged, calm, reasonable-looking — like genuine wisdom. "
     "Brain Villain gestures at it with an open palm: see? Just being careful."),

    (75, "BRAIN VILLAIN'S LAST TRICK",
     "That thought is not caution. Not planning. Not flexibility.",
     "The same speech bubble — now getting a thick red border stamped around it, reclassification in progress. "
     "Three small crossed-out icons fall away from it: a shield (caution), a map (planning), a spring (flexibility). "
     "The disguises drop one by one."),

    (76, "BRAIN VILLAIN'S LAST TRICK",
     "It is the Pre-Spend defending its territory — wearing the costume of prudence.",
     "Brain Villain wearing a prim 'prudence' costume — small reading glasses, a neat shawl — "
     "but behind it, clearly visible, the PRE-SPEND slot glowing, still lit from Beat 57. "
     "The costume does not hide the mechanism. V14 continuity: the last drain fights back dressed as wisdom."),

    (77, "BRAIN VILLAIN'S LAST TRICK",
     "The programs are not broken.",
     "The Brain Villain's control panel — switches still ON — with a clean banner across it: 'NOT BROKEN'. "
     "Villain stands beside the panel, and for once Alex (exterior) nods in agreement. "
     "No conflict in this frame. A statement of fact."),

    (78, "BRAIN VILLAIN'S LAST TRICK",
     "They were built for a world where every resource had to stay within arm's reach — where an unexpected winter could end you.",
     "Ancestral scene, warm earth tones: ancestor-Alex (same character, primitive clothing) by a campfire, "
     "food supplies stacked close beside him, one hand resting on them. Snow beginning outside the cave mouth. "
     "Keeping resources close WAS the correct program."),

    (79, "BRAIN VILLAIN'S LAST TRICK",
     "In that world, locking food away from yourself was madness.",
     "The same ancestral scene: a locked wooden chest sitting far from the fire, out in the snow — "
     "ancestor-Alex staring at it, bewildered. Distance from resources = danger in that world. "
     "The absurdity is the point: the instinct was right, once."),

    (80, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain was built for that world. Not this one.",
     "Split panel: LEFT — Brain Villain in the prehistoric cave, content, perfectly at home by the fire. "
     "RIGHT — same Brain Villain in a modern apartment with direct-deposit phone and one-click icons, "
     "slightly lost, out of place but still operational. Same character. Wrong era."),

    (81, "BRAIN VILLAIN'S LAST TRICK",
     "The transfer is the first system designed for the world you actually live in — where the threat isn't winter. It's you, on a Tuesday night, with a phone.",
     "Dark modern room, 11 PM: Alex's face lit only by phone glow, thumb hovering over a BUY button. "
     "TUESDAY calendar tag in corner. The modern predator is this exact moment. "
     "In the background, faint: the island vault, safely out of reach. The system holds even now."),

    # ═══════════════════════════════════════════════════════
    # IDENTITY CLOSE — 8 beats (max 9)
    # ═══════════════════════════════════════════════════════

    (82, "IDENTITY CLOSE",
     "You were never bad at saving.",
     "Alex centered, calm, direct eye contact with viewer. A grey label reading nothing specific — "
     "a faded 'bad with money' tag — peels off his chest and drifts away. Clean white background. "
     "Not triumphant. Corrected."),

    (83, "IDENTITY CLOSE",
     "You were playing a manual game against automatic opponents.",
     "Chessboard visual: Alex's side — one hand moving a single piece, deliberate, tired. "
     "The opponent's side — pieces moving by themselves on small gears, five of them, coordinated. "
     "The game was never about skill. It was about the mechanism."),

    (84, "IDENTITY CLOSE",
     "Smart never mattered. Tired always did.",
     "A balance scale: on one side, a graduation cap. On the other, a nearly-empty battery icon. "
     "The battery side sits heavier — it always decided the outcome. Minimal, clinical, no judgment."),

    (85, "IDENTITY CLOSE",
     "One transfer. Set up once. It doesn't need your motivation, your mood, or your Monday.",
     "The green toggle switch, now ON, small and quiet in the corner of a calm domestic scene. "
     "Around it, three faded icons drift away unneeded: a flame (motivation), a face (mood), a MON calendar tag. "
     "The switch needs none of them."),

    (86, "IDENTITY CLOSE",
     "It runs while you sleep. It runs on your worst week. It runs.",
     "Triptych: (1) Alex asleep, transfer arrow firing. (2) Alex having a visibly terrible day — rain, "
     "spilled coffee — transfer arrow firing anyway. (3) Just the arrow, alone, firing. "
     "Three panels, same arrow, zero conditions."),

    (87, "IDENTITY CLOSE",
     "Six months from now you'll open that account and feel something unfamiliar.",
     "Calendar pages flipping — six months passing in one frame. Then: Alex opening the island-vault app. "
     "The balance bar has grown — modest, real, green. His face beginning to register it."),

    (88, "IDENTITY CLOSE",
     "Not pride. Evidence.",
     "Extreme close-up: just the account screen. A plain, solid, grown number. No confetti, no celebration "
     "graphics, no fireworks. A fact that exists. The restraint of this frame IS the emotion."),

    (89, "IDENTITY CLOSE",
     "Evidence that your brain was never the enemy — it just needed one decision it couldn't argue with.",
     "Alex and Brain Villain looking at the balance together — the Villain inside the skull gives a small, "
     "grudging shrug of acceptance. Not defeated. Bypassed, and oddly at peace with it. "
     "Warm resolved light. The adversaries are just roommates now."),

    # ═══════════════════════════════════════════════════════
    # NEXT VIDEO TEASE — 5 beats — V16: 7 Signs (Formato Señales)
    # ═══════════════════════════════════════════════════════

    (90, "NEXT VIDEO TEASE",
     "Next week: seven signs your brain is already wired to stay broke.",
     "Seven mysterious sign-silhouettes in a row — each a small dark card with a '?' — numbered 1 to 7. "
     "None revealed. Brain Villain eyes them nervously: its tells are about to be published."),

    (91, "NEXT VIDEO TEASE",
     "Not habits. Signs. Things you do without noticing you do them.",
     "A magnifying glass hovering over an ordinary daily scene — Alex walking, coffee in hand, unaware. "
     "Under the lens, a faint red pattern glows on his ordinary gesture. Invisible until magnified."),

    (92, "NEXT VIDEO TEASE",
     "Number four happens in the supermarket. You probably did it this week.",
     "Supermarket aisle, flat cartoon: Alex mid-gesture reaching for a shelf — frozen frame — "
     "with sign-card #4 glowing beside the exact gesture, still showing only '?'. "
     "The viewer's own week is implicated."),

    (93, "NEXT VIDEO TEASE",
     "If you recognize three or more, that video is going to be uncomfortable.",
     "A checklist of seven anonymous rows — three checkmarks already glowing warning-red. "
     "Alex looks at the checklist, then at the viewer: you're counting yours already."),

    (94, "NEXT VIDEO TEASE",
     "See you Thursday.",
     "Alex in his default closing pose — relaxed, confident, slight knowing smile. Brain Villain calm "
     "inside the skull. THURSDAY visible on a wall calendar. Warm resolved light. "
     "The tension is released; the loop stays open."),

]

# ── PDF GENERATION ─────────────────────────────────────────────────────────────

TOTAL = len(BEATS)
CHUNK = 24

parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

SECTION_STARTS = {}
last_sec = None
for beat in BEATS:
    num, sec = beat[0], beat[1]
    if sec != last_sec:
        SECTION_STARTS[num] = sec
        last_sec = sec


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_pdf():
    styles = getSampleStyleSheet()
    H1       = ParagraphStyle('H1',       parent=styles['Title'],   fontSize=17, leading=22, alignment=TA_CENTER)
    H2       = ParagraphStyle('H2',       parent=styles['Normal'],  fontSize=12, leading=15,
                              alignment=TA_CENTER, fontName='Helvetica-Bold')
    SUB      = ParagraphStyle('SUB',      parent=styles['Normal'],  fontSize=10, leading=13,
                              alignment=TA_CENTER, textColor=colors.HexColor('#444444'))
    META     = ParagraphStyle('META',     parent=styles['Normal'],  fontSize=8,  leading=11,
                              alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    STYLE_BOX= ParagraphStyle('STYLE_BOX',parent=styles['Normal'],  fontSize=8,  leading=11,
                              textColor=colors.HexColor('#555555'), spaceBefore=4, spaceAfter=8)
    PART     = ParagraphStyle('PART',     parent=styles['Heading2'], fontSize=12, leading=15,
                              textColor=colors.HexColor('#B02A2A'), spaceBefore=14, spaceAfter=6)
    SEC_H    = ParagraphStyle('SEC_H',    parent=styles['Normal'],  fontSize=9,  leading=12,
                              textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                              spaceBefore=8, spaceAfter=2)
    BEATH    = ParagraphStyle('BEATH',    parent=styles['Normal'],  fontSize=10, leading=14,
                              spaceBefore=6, spaceAfter=2)
    IMG      = ParagraphStyle('IMG',      parent=styles['Normal'],  fontSize=8.5, leading=12, spaceAfter=2)
    DONE     = ParagraphStyle('DONE',     parent=styles['Normal'],  fontSize=9,  leading=12,
                              textColor=colors.HexColor('#1E7A33'), fontName='Helvetica-Bold',
                              spaceBefore=6)

    pdf_path = "/home/user/Claudeeee/V15_final_IMAGE_PROMPTS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=16*mm, rightMargin=16*mm,
                            topMargin=15*mm, bottomMargin=15*mm)

    flow = [
        Paragraph("NEUROCENTS · VIDEO 15", H2),
        Spacer(1, 4),
        Paragraph("IMAGE PROMPTS — VISUAL REFERENCE", H1),
        Spacer(1, 3),
        Paragraph(esc(TITLE), SUB),
        Spacer(1, 4),
        Paragraph(
            f"{TOTAL} beats · {len(parts)} parts of ~{CHUNK} beats · Visual-first (no redundant text labels)",
            META),
        Spacer(1, 8),
        Paragraph(
            f"<b>STYLE PREAMBLE</b> — prepend to every prompt in Google Flow:<br/>{esc(STYLE)}",
            STYLE_BOX),
    ]

    for pidx, (a, b) in enumerate(parts, 1):
        flow.append(Paragraph(f"IMAGE PROMPTS — PART {pidx}/{len(parts)}  (Beats {a}–{b})", PART))

        for beat in BEATS[a - 1:b]:
            num, sec, narration, image_prompt = beat[0], beat[1], beat[2], beat[3]

            if num in SECTION_STARTS:
                flow.append(Paragraph(
                    f'<font color="#B02A2A"><b>── {esc(SECTION_STARTS[num])} ──</b></font>',
                    SEC_H))

            full_prompt = f"{STYLE} {image_prompt}"
            block = [
                Paragraph(
                    f'<font color="#B02A2A"><b>BEAT {num}</b></font>  '
                    f'<b><i>"{esc(narration)}"</i></b>', BEATH),
                Paragraph(f'<b>Image Prompt:</b> {esc(full_prompt)}', IMG),
            ]
            flow.append(KeepTogether(block))

        flow.append(Paragraph(f"PART {pidx} DONE — Beats {a}–{b} ✓", DONE))
        flow.append(Spacer(1, 6))

    doc.build(flow)
    print(f"Saved: {pdf_path} | {TOTAL} beats | {len(parts)} parts")


if __name__ == "__main__":
    build_pdf()
