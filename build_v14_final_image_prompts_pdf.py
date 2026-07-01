#!/usr/bin/env python3
"""
VIDEO 14 — IMAGE PROMPTS · BRIEF v3.1
95 beats · BLUE t-shirt · S17 thumbnail continuity · Visual-first rule
Beat 1 format: S17 OPENING THUMBNAIL CONTINUITY
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

TITLE    = "5 Things That Drain Your Money Before Payday (No Matter What You Earn)"
SUBTITLE = "NEUROCENTS · VIDEO 14"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines on every element, "
    "clean solid color fills, no gradients. "
    "Recurring main character ALEX: large beige oval head with transparent glass upper skull "
    "revealing a pink cartoon Brain Villain inside, small black dot eyes, thin neutral mouth, "
    "black spiky hair, BLUE t-shirt (NOT RED — verify every time), gray pants. "
    "Brain Villain: pink cartoon brain character, heavy-lidded eyes, slight smirk, small teeth — "
    "ALWAYS inside Alex's skull, never floating outside. "
    "Palette: beige skin #F5E6C8 · pink brain #E8A598 · blue t-shirt · gray pants · "
    "green: savings/gains · red: loss/danger · white: diagram scenes · "
    "dark charcoal #1A1A1A: hook/drama scenes. "
    "16:9, 1280x720."
)

# Format: (beat_num, section, narration, image_prompt)
BEATS = [

    # ═══════════════════════════════════════════════════════
    # HOOK — 8 beats — S1 Pregunta Sin Resolver + S17 Continuity
    # ═══════════════════════════════════════════════════════

    (1, "HOOK — PRIMEROS 5 SEGUNDOS",
     "Why does your money always disappear before payday?",
     "BEAT 1 — OPENING [S17 THUMBNAIL CONTINUITY · S1 PREGUNTA SIN RESOLVER]: "
     "Alex standing at a kitchen counter staring at his phone. Bank balance on screen: €0.00 in bold red. "
     "Expression: wide eyes, slight jaw drop — recognition, not panic. The viewer has been here. "
     "Brain Villain ACTIVE inside skull: arms crossed, smirking, lit up — the programs are already running. "
     "Calendar on wall shows two days to payday. Bold number €0.00 dominates the phone screen. "
     "Camera: MEDIUM CLOSE-UP, slight low angle — phone dominant in frame. "
     "Motion: FAST ZOOM IN toward phone screen and balance number. "
     "NOTE: Viewer who just saw thumbnail must recognize this scene in under 5 seconds. "
     "This IS the moment — no setup, no introduction. The question IS the opening."),

    (2, "HOOK",
     "Not sometimes. Every month.",
     "Alex at a desk. Three identical calendar pages side by side showing three different months — "
     "each with a bold red X through the last two days before payday. No text labels. "
     "The red X pattern repeats across all three months — structural, not accidental. "
     "Alex gestures toward calendars with open palm: 'look at this.' "
     "Camera: wide shot — all three calendars visible. Motion: PAN RIGHT across the three months."),

    (3, "HOOK",
     "It doesn't matter if you earn €2,000 or €6,000.",
     "Split frame left/right: LEFT — simple apartment, Alex in casual clothes, phone shows €2,000 salary "
     "notification. RIGHT — nicer apartment, Alex in work shirt, phone shows €6,000 notification. "
     "Both Alex figures have identical expression: Brain Villain glowing with the same smirk in both skulls. "
     "Income level is irrelevant — the Brain Villain is identical in both. "
     "Camera: split panel. Motion: PAN LEFT then PAN RIGHT — scanning both panels."),

    (4, "HOOK",
     "Four weeks. Same empty account.",
     "Alex viewed from above — sitting on floor leaning against wall. "
     "Four empty wallet icons arranged in a circle around him — one per week. All empty. "
     "No text. The empty wallets communicate the cycle. Arms on knees, head tilted — tired but not surprised. "
     "Camera: bird's eye view — Alex small in center, wallets surrounding. Motion: SLOW ZOOM OUT — reveal full circle."),

    (5, "HOOK",
     "Five things are doing this to you.",
     "Dark charcoal background (#1A1A1A). Five numbered slots arranged vertically (5 → 1), "
     "each showing a '?' icon — pulsing faintly. Brain Villain in corner, finger counting down: 5, 4, 3... "
     "The countdown is starting. Alex stands beside the list, expression building toward revelation. "
     "Camera: center composition — list fills frame. Motion: SLOW ZOOM IN into the numbered list."),

    (6, "HOOK",
     "And number one runs before you even get paid.",
     "Close-up on slot #1 — still showing '?'. A calendar behind it: WEDNESDAY highlighted in red. "
     "Payday arrow points to FRIDAY. The '?' pulses at WEDNESDAY — the drain starts before the money arrives. "
     "Brain Villain leans toward slot #1 with a knowing smirk. "
     "Camera: extreme close-up — slot #1 dominant. Motion: FAST ZOOM IN on the Wednesday marker."),

    (7, "HOOK",
     "Not when you spend it. Before.",
     "Timeline graphic on white background: FRIDAY payday arrow on the right. "
     "Brain Villain activity spike on the LEFT at WEDNESDAY — earlier than the money. "
     "No text labels — the visual timeline tells it. Brain Villain sits ON the Wednesday spike, arms crossed. "
     "Camera: wide center — timeline fills frame. Motion: DIAGONAL PAN + ZOOM IN from left spike toward payday."),

    (8, "HOOK",
     "Here's the list.",
     "The five numbered slots from beat 5, now fully illuminated. Still '?' in each — but the list is real. "
     "Brain Villain stands beside it like a game show host. Alex turns to look at the list: the journey begins. "
     "Camera: medium shot — Alex and the list side by side. Motion: SLOW ZOOM IN into the top of the list."),

    # ═══════════════════════════════════════════════════════
    # SETUP — 4 beats
    # ═══════════════════════════════════════════════════════

    (9, "SETUP",
     "These aren't budgeting mistakes.",
     "Torn budget spreadsheet on a desk. Alex's hand observes it, confused — not crumpling it. "
     "Brain Villain floats above the spreadsheet, shaking its head: 'not this.' "
     "Camera: medium — desk level angle. Motion: STATIC."),

    (10, "SETUP",
     "They're not discipline failures.",
     "Alex at 5:30 AM, gym bag over shoulder, coffee in hand — clearly disciplined. "
     "Brain Villain rides on his shoulder, still running its programs. Clock shows 5:30 AM. "
     "Discipline exists — it's not the issue. Camera: medium — full body, slight low angle (capable). "
     "Motion: PAN RIGHT following Alex's walk."),

    (11, "SETUP",
     "They're patterns. And they run automatically.",
     "Inside Alex's glass skull — Brain Villain at a control panel with five switches, all flipped ON. "
     "Labels on switches are blank — the viewer doesn't know what they are yet. "
     "The switches run without Alex's input or awareness. "
     "Camera: close-up — skull interior, control panel fills frame. Motion: SLOW ZOOM IN into panel."),

    (12, "SETUP",
     "Number five is the one everyone knows. And still can't stop.",
     "Slot #5 on the list illuminates — still '?'. A crowd of small figures all point at it simultaneously. "
     "Everyone knows this one. Alex in the crowd, arms crossed, nodding — 'yeah, I know this one.' "
     "Camera: medium — list with crowd below. Motion: FAST ZOOM IN onto slot #5."),

    # ═══════════════════════════════════════════════════════
    # ITEM 5 — THE CARD GAP — 8 beats
    # ═══════════════════════════════════════════════════════

    (13, "ITEM 5 — THE CARD GAP",
     "Number five. The Card Gap.",
     "Slot #5 reveals its label: CARD GAP. Alex holds a contactless card in one hand, cash in the other. "
     "Brain Villain sits between them on a scale — cash side heavy (brain registers loss), card side light (nothing). "
     "Camera: medium — two hands + scale centered. Motion: FAST ZOOM IN on the scale between the hands."),

    (14, "ITEM 5 — THE CARD GAP",
     "When you pay with cash, your brain registers loss.",
     "Alex at a register handing over four €10 bills. Expression: mild grimace — the money feels like it's leaving. "
     "Brain Villain in skull shows a pain indicator spike — the signal fires. "
     "Camera: medium — register transaction angle. Motion: SLOW ZOOM IN toward the bills leaving Alex's hand."),

    (15, "ITEM 5 — THE CARD GAP",
     "You feel the €40 leave.",
     "Close-up on Alex's face: genuine slight wince. The €40 amount visible on register display. "
     "Expression and number together communicate the felt loss — no text labels needed beyond the price. "
     "Camera: extreme close-up — Alex's eyes and register display. Motion: STATIC — let the expression land."),

    (16, "ITEM 5 — THE CARD GAP",
     "When you pay with card — tap, done — the pain disappears.",
     "Same register, same €40 — but Alex taps card. Expression: completely neutral, almost cheerful. "
     "Brain Villain in skull: pain indicator is FLAT — zero signal. Identical scene to beat 14, different internal state. "
     "Camera: same angle as beat 14 — the contrast is in the brain, not the scene. Motion: FAST ZOOM IN on the tap."),

    (17, "ITEM 5 — THE CARD GAP",
     "Same purchase. Different brain response.",
     "Split frame: LEFT — cash transaction (pain spike in Brain Villain). RIGHT — card tap (flat line in Villain). "
     "Same €40. Same store. Only the internal state differs. "
     "Camera: split panel — identical scenes, different brain readouts. Motion: PAN LEFT then PAN RIGHT."),

    (18, "ITEM 5 — THE CARD GAP",
     "Card users spend 20 to 47% more than cash users.",
     "Large bold stat: +20% to +47% dominates the frame. Alex stands beside it. "
     "Brain Villain points at the 47% with a smug expression — this one's mine. "
     "Camera: wide — stat dominates, Alex secondary. Motion: FAST ZOOM IN onto the percentage range."),

    (19, "ITEM 5 — THE CARD GAP",
     "Not because they want to. Because the payment doesn't feel like payment.",
     "Alex mid-swipe on a shopping app, expression completely blank — no guilt, no awareness. "
     "Brain Villain inside skull sits in a tiny hammock — fully relaxed. Nothing to override. "
     "Camera: medium — phone and Alex's face. Motion: SLOW ZOOM IN toward the phone screen."),

    (20, "ITEM 5 — THE CARD GAP",
     "Your brain is still waiting for the money to actually leave.",
     "Alex's skull interior: Brain Villain looks around confused, waiting for a signal that never comes. "
     "Outside the skull, bank balance on phone shows a lower number — the money already left. "
     "Internal lag vs external reality. Camera: medium — skull interior + phone juxtaposed. Motion: SLOW ZOOM OUT."),

    # ═══════════════════════════════════════════════════════
    # ITEM 4 — THE REWARD DRAIN — 8 beats
    # ═══════════════════════════════════════════════════════

    (21, "ITEM 4 — THE REWARD DRAIN",
     "Number four. The Reward Drain.",
     "Slot #4 reveals: REWARD DRAIN. Alex at desk, exhausted, suit jacket over chair. "
     "Brain Villain in skull has a small calculator: it's running numbers. "
     "Small 'I DESERVE THIS' thought bubble floats up from the skull. "
     "Camera: medium — desk scene. Motion: FAST ZOOM IN onto the thought bubble."),

    (22, "ITEM 4 — THE REWARD DRAIN",
     "It's Thursday. You've had a brutal week.",
     "Thursday circled on a desk calendar. Stack of papers, empty coffee cups, multiple browser tabs visible. "
     "Classic brutal-week visual cues — no text labels. The chaos speaks. "
     "Camera: wide — full desk chaos visible. Motion: SLOW ZOOM OUT to reveal full desk."),

    (23, "ITEM 4 — THE REWARD DRAIN",
     "Alex has too. Deadlines. A difficult meeting. Late nights.",
     "Three-panel strip: (1) Alex at desk with deadline clock. (2) Alex in tense meeting, manager pointing. "
     "(3) Alex at desk at night, city lights behind. The week compressed into three images. "
     "Camera: triptych — three small panels. Motion: PAN RIGHT across all three."),

    (24, "ITEM 4 — THE REWARD DRAIN",
     "And his brain does something automatic.",
     "Inside Alex's skull — Brain Villain at the calculator, fingers moving fast. "
     "The calculation runs without Alex's awareness. Outside the skull: Alex's eyes are closed, resting. "
     "Camera: close-up — skull interior, calculator fills frame. Motion: SLOW ZOOM IN into the calculator."),

    (25, "ITEM 4 — THE REWARD DRAIN",
     "It calculates what he's owed.",
     "Calculator screen shows a balance: EFFORT → €?? OWED. "
     "Brain Villain writes on a small ledger: hours worked, difficulty, sacrifices. The debt column grows. "
     "Camera: medium close-up — calculator + ledger. Motion: FAST ZOOM IN onto the OWED amount."),

    (26, "ITEM 4 — THE REWARD DRAIN",
     "Not the salary. Something extra.",
     "Two columns: SALARY (normal check icon — expected) vs EXTRA (pulsing warm glow — the additional claim). "
     "Brain Villain points specifically at EXTRA — this is what the calculation is for. "
     "Camera: split composition — the two columns. Motion: SLOW ZOOM IN toward the EXTRA column."),

    (27, "ITEM 4 — THE REWARD DRAIN",
     "'I worked hard. I deserve this.'",
     "Speech bubble — but it floats INSIDE the skull, not from Alex's mouth. "
     "The Brain Villain's voice, not a conscious decision. Text: I WORKED HARD. I DESERVE THIS. Bold. "
     "Brain Villain nods at the bubble with approval — 'exactly right.' "
     "Camera: close-up — skull interior + speech bubble. Motion: STATIC — let the words land."),

    (28, "ITEM 4 — THE REWARD DRAIN",
     "That sentence has cost more money than any impulse purchase.",
     "Receipt tape unrolling from Alex's pocket — stretching floor to ceiling. "
     "Each item on the receipt begins with 'I deserved...' The total is very large. "
     "Camera: wide — floor to ceiling receipt dominates. Motion: PAN UP rising along the receipt."),

    # ═══════════════════════════════════════════════════════
    # ITEM 3 — THE INVISIBLE DRAIN — 7 beats
    # ═══════════════════════════════════════════════════════

    (29, "ITEM 3 — THE INVISIBLE DRAIN",
     "Number three. The Invisible Drain.",
     "Slot #3 reveals: INVISIBLE DRAIN. Alex's phone — the subscription apps grid. "
     "Several icons have dust particle effects — not opened in months. "
     "Brain Villain barely visible, almost transparent — the 'invisible' quality is the point. "
     "Camera: close-up — phone screen with subscription grid. Motion: SLOW ZOOM IN into the dusty icons."),

    (30, "ITEM 3 — THE INVISIBLE DRAIN",
     "Right now, you have at least three subscriptions you've forgotten about.",
     "Grid of subscription logos (generic icons — no real brands). Three have a 'last opened: 4 months ago' "
     "timestamp badge. They run silently. The viewer counts along. "
     "Camera: wide — full grid visible. Motion: SLOW ZOOM OUT — reveal full subscription grid."),

    (31, "ITEM 3 — THE INVISIBLE DRAIN",
     "Apps you haven't opened in four months.",
     "Calendar page showing: last opened 4 months ago. The app icon beside it — collecting digital dust. "
     "Monthly charge still processing quietly in background. "
     "Camera: medium — calendar + app icon. Motion: STATIC."),

    (32, "ITEM 3 — THE INVISIBLE DRAIN",
     "Services that auto-renewed in January.",
     "January calendar page. Auto-renewal notification pops up — small, easy to dismiss. "
     "Alex's thumb swipes it away without reading. Money leaves quietly. "
     "Camera: close-up — January calendar + dismissal notification. Motion: FAST ZOOM IN on the dismissed notification."),

    (33, "ITEM 3 — THE INVISIBLE DRAIN",
     "Why haven't you cancelled them?",
     "Alex staring at the subscription list. Hand reaches for the cancel button — but stops. "
     "Brain Villain inside skull holds up a 'WAIT' sign. The pause is the trap. "
     "Camera: medium — Alex + phone, hand frozen mid-air. Motion: STATIC — the freeze is the mechanism."),

    (34, "ITEM 3 — THE INVISIBLE DRAIN",
     "Because cancelling requires a decision. And decisions cost energy.",
     "Alex's energy meter (like a phone battery) at LOW. Two arrows: SUBSCRIBE (easy) → meter barely drops. "
     "CANCEL (hard) → meter drops more. The asymmetry is visual — same action, different cost. "
     "Camera: wide — energy meter + decision arrows diagram. Motion: SLOW ZOOM IN into the meter."),

    (35, "ITEM 3 — THE INVISIBLE DRAIN",
     "Your brain doesn't cancel things. It lets them run.",
     "Inside Alex's skull — Brain Villain sits in a tiny recliner, watching the subscriptions run like a screensaver. "
     "Passive. Comfortable. The Villain is NOT acting — that's the program. Inaction is the default. "
     "Camera: close-up — skull interior, Villain in recliner. Motion: SLOW ZOOM IN into the recliner."),

    # ═══════════════════════════════════════════════════════
    # CTA — beats 36-37 = 38% ✅
    # ═══════════════════════════════════════════════════════

    (36, "CTA",
     "If your brain is doing this to you right now — subscribe.",
     "Alex looks directly at camera — fourth wall break. Expression: knowing, complicit. "
     "Brain Villain peeks from behind his skull with a slightly defensive look — it doesn't want this. "
     "Subscribe button graphic appears — simple, no hard sell. "
     "Camera: direct address — slight zoom toward camera. Motion: SLOW ZOOM IN toward Alex's direct gaze."),

    (37, "CTA",
     "We break down a new pattern every week. It's free. And it might save you more than you think.",
     "Small visual: weekly calendar with a Neurocents-style logo appearing each week — consistent, trustworthy. "
     "Alex nods once, returns to the list — CTA done, moving on. "
     "Camera: medium — calendar + logo. Motion: STATIC."),

    # ═══════════════════════════════════════════════════════
    # ITEM 2 — SOCIAL SPENDING — 9 beats
    # ═══════════════════════════════════════════════════════

    (38, "ITEM 2 — SOCIAL SPENDING",
     "Number two. Social Spending.",
     "Slot #2 reveals: SOCIAL SPENDING. Alex in a mirror — looking at himself in a new jacket. "
     "Behind him, a crowd of translucent ghost figures (the imaginary audience) — they're watching. Except they're not real. "
     "Camera: medium — mirror scene, ghost audience visible in reflection. Motion: SLOW ZOOM IN into the mirror."),

    (39, "ITEM 2 — SOCIAL SPENDING",
     "You bought something this month for an audience that wasn't watching.",
     "Ghost audience from beat 38 — now from their perspective: all looking elsewhere, phones out, distracted. "
     "Not watching at all. Alex is buying for no one. "
     "Camera: wide — ghost audience, all looking away. Motion: SLOW ZOOM OUT — reveal full indifferent audience."),

    (40, "ITEM 2 — SOCIAL SPENDING",
     "The car that looks good in the parking lot.",
     "Alex's car in an empty parking lot at night. No one around. Ghost audience figures at the edges — "
     "translucent, barely there. The performance without an audience. "
     "Camera: wide — car in empty lot. Motion: PAN LEFT across the empty lot."),

    (41, "ITEM 2 — SOCIAL SPENDING",
     "The jacket for the meeting.",
     "Alex in a boardroom in a sharp jacket. Meeting participants are ghost figures — translucent. "
     "Alex adjusts jacket cuff mid-meeting — the jacket mattered more than the meeting. "
     "Camera: medium — boardroom, Alex prominent, others ghosted. Motion: SLOW ZOOM IN on the jacket adjustment."),

    (42, "ITEM 2 — SOCIAL SPENDING",
     "The upgrade nobody asked for but someone might notice.",
     "Alex's desk: new monitor setup, latest accessories. Post-it note on monitor: 'Nobody asked for this.' "
     "Ghost audience in background — not noticing. The note is Alex's own realization. "
     "Camera: medium — desk setup. Motion: FAST ZOOM IN onto the post-it note."),

    (43, "ITEM 2 — SOCIAL SPENDING",
     "Who is that person you're buying for?",
     "Alex faces camera directly, expression genuinely questioning. "
     "Around him, ghost audience figures slowly dissolve — fading out. "
     "The question lands in the empty space they leave. "
     "Camera: direct address — medium close-up. Motion: STATIC — let the question breathe."),

    (44, "ITEM 2 — SOCIAL SPENDING",
     "They don't exist. They're a projection.",
     "The ghost audience is now completely transparent — barely visible. "
     "Alex's Brain Villain projects them like a film projector from inside the skull — the audience is his own output. "
     "Camera: medium — the projector-skull visual. Motion: SLOW ZOOM IN into the skull projector."),

    (45, "ITEM 2 — SOCIAL SPENDING",
     "The most expensive audience in your life has never spent a single dollar.",
     "Financial ledger: LEFT column — GHOST AUDIENCE COSTS (long list, €€€€). "
     "RIGHT column — GHOST AUDIENCE CONTRIBUTIONS: empty. Asymmetry is total. "
     "Camera: wide — ledger fills frame. Motion: SLOW ZOOM IN into the empty contributions column."),

    (46, "ITEM 2 — SOCIAL SPENDING",
     "They live entirely in your head. And they have expensive taste.",
     "Alex's skull cross-section: inside, the ghost audience sits in tiny theater seats — "
     "watching a tiny Alex perform for them. Inside his own head. The recursion is the trap. "
     "Camera: close-up — skull interior theater. Motion: FAST ZOOM IN into the tiny internal theater."),

    # ═══════════════════════════════════════════════════════
    # ITEM 1 — THE PRE-SPEND — 12 beats
    # ═══════════════════════════════════════════════════════

    (47, "ITEM 1 — THE PRE-SPEND",
     "Number one. The one nobody names.",
     "Slot #1 glows brightest — still '?'. The other four slots visible but dimmed. "
     "Brain Villain stands beside slot #1 with arms crossed — guarding it. "
     "Camera: wide — all five slots, #1 dominant with spotlight. Motion: FAST ZOOM IN onto slot #1."),

    (48, "ITEM 1 — THE PRE-SPEND",
     "The Pre-Spend.",
     "Slot #1 reveals: THE PRE-SPEND in bold. Brain Villain steps aside reluctantly — it's been named. "
     "The program has a name now. That's the beginning of the power shift. "
     "Camera: close-up — the reveal. Motion: FAST ZOOM IN onto the text THE PRE-SPEND."),

    (49, "ITEM 1 — THE PRE-SPEND",
     "It's Wednesday. Payday is Friday.",
     "Alex at a desk. Wednesday date circled on calendar. Payday circled on Friday — two days away. "
     "Current balance on phone: declining but not zero. The setup is established. "
     "Camera: medium — desk with calendar and phone. Motion: SLOW ZOOM IN toward the calendar."),

    (50, "ITEM 1 — THE PRE-SPEND",
     "Alex hasn't received anything yet.",
     "Bank notification on Alex's phone: NEXT DEPOSIT: FRIDAY. Current balance visible. "
     "Timestamp: WEDNESDAY, 2:00 PM. The money is NOT there yet. "
     "Camera: close-up — phone notification. Motion: STATIC."),

    (51, "ITEM 1 — THE PRE-SPEND",
     "But his brain has already spent it.",
     "Inside Alex's skull: Brain Villain at an accounting desk — rapidly processing allocation arrows. "
     "The salary hasn't arrived but the Villain is already distributing it. "
     "Camera: close-up — skull interior, frantic allocation activity. Motion: FAST ZOOM IN on the Villain's work."),

    (52, "ITEM 1 — THE PRE-SPEND",
     "Not metaphorically. Neurologically.",
     "Split label: LEFT — METAPHOR (crossed out in red). RIGHT — NEUROLOGY (highlighted green). "
     "Brain scan silhouette showing activity in decision-making region — it's literal, not poetic. "
     "Camera: split panel — clean white diagram. Motion: SLOW ZOOM IN toward the NEUROLOGY label."),

    (53, "ITEM 1 — THE PRE-SPEND",
     "The moment you know money is coming — your brain allocates it.",
     "Timeline on white background: WEDNESDAY (knowledge of incoming money) → immediate allocation arrows fire. "
     "FRIDAY payday comes AFTER the allocation is complete. The brain processes future money as if arrived. "
     "Camera: wide — timeline graphic. Motion: PAN RIGHT from Wednesday to Friday."),

    (54, "ITEM 1 — THE PRE-SPEND",
     "The rent. The pending bill. The thing you've been delaying.",
     "Three allocation boxes filling in Alex's mental budget: RENT ✓, BILL ✓, DELAYED THING ✓. "
     "Brain Villain checks each efficiently — these are the legitimate ones. The money isn't there yet. "
     "Camera: medium — the three allocation boxes inside the skull. Motion: SLOW ZOOM IN into the boxes."),

    (55, "ITEM 1 — THE PRE-SPEND",
     "And then — quietly — a few things that feel deserved.",
     "After RENT, BILL, DELAYED THING — a fourth box appears, smaller, slightly dimmer: 'DESERVED EXTRA'. "
     "Brain Villain adds it quietly, almost sheepishly. The creep is subtle. "
     "Camera: close-up — the fourth box appearing. Motion: FAST ZOOM IN onto the DESERVED EXTRA box."),

    (56, "ITEM 1 — THE PRE-SPEND",
     "By the time Friday arrives, the money is already gone in your mind.",
     "Friday arrives on calendar — payday notification appears. But Alex's mental budget is already at zero. "
     "The money arrives into an already-empty mental account. The anticlimax. "
     "Camera: medium — calendar Friday + empty mental budget. Motion: STATIC — the anticlimax lands."),

    (57, "ITEM 1 — THE PRE-SPEND",
     "Friday is just the confirmation.",
     "Split: LEFT — WEDNESDAY (mental spend complete, all arrows allocated). "
     "RIGHT — FRIDAY (money arrives, immediately absorbed). Arrow from right to left — mental preceded physical. "
     "Camera: wide — split timeline. Motion: PAN LEFT from Friday back to Wednesday (reverse is the point)."),

    (58, "ITEM 1 — THE PRE-SPEND",
     "You don't spend your salary. You process a transaction your brain closed on Wednesday.",
     "Alex at bank app — Friday. Transaction processes. Brain Villain holds up a RECEIPT dated WEDNESDAY. "
     "The deal was done two days ago. Friday is administrative. "
     "Camera: close-up — Wednesday receipt in Brain Villain's hand. Motion: FAST ZOOM IN on the WEDNESDAY date."),

    # ═══════════════════════════════════════════════════════
    # MECHANISM CONCLUSION — 5 beats
    # ═══════════════════════════════════════════════════════

    (59, "MECHANISM CONCLUSION",
     "Five patterns. Running automatically.",
     "All five slots now fully labeled and lit: CARD GAP · REWARD DRAIN · INVISIBLE DRAIN · "
     "SOCIAL SPENDING · PRE-SPEND. Five program indicators — all ON. Alex in front of the complete list. "
     "Camera: wide — all five lit. Motion: SLOW ZOOM OUT — pull back to reveal all five simultaneously."),

    (60, "MECHANISM CONCLUSION",
     "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
     "Each slot highlighted in sequence as names land — rapid highlight sequence. "
     "Alex's finger points to each in sequence — naming them out loud. "
     "Camera: wide — same list view. Motion: FAST ZOOM IN 0.5s per slot — five rapid hits."),

    (61, "MECHANISM CONCLUSION",
     "None of them feel like mistakes when they happen.",
     "Three micro-scenes in one frame: Alex mid-Card Gap tap / mid-Reward purchase / mid-subscription-ignore. "
     "Expression in each: completely normal, reasonable, justified. No guilt visible anywhere. "
     "Camera: triptych — three micro-scenes. Motion: PAN RIGHT across the three."),

    (62, "MECHANISM CONCLUSION",
     "The Card Gap feels convenient.",
     "CARD GAP slot. Adjective appears beside it: CONVENIENT. Alex taps card — expression is pleased. "
     "The feeling is real. Camera: close-up — CARD GAP + CONVENIENT. Motion: SLOW ZOOM IN."),

    (63, "MECHANISM CONCLUSION",
     "The Reward Drain feels earned. The Social Spend feels reasonable. The Pre-Spend feels like planning.",
     "Three slots in rapid sequence: REWARD DRAIN + EARNED · SOCIAL SPENDING + REASONABLE · PRE-SPEND + PLANNING. "
     "Each pairing makes ironic sense — the trap IS the logic. "
     "Camera: rapid three-panel reveal. Motion: FAST ZOOM IN 1s per panel."),

    # ═══════════════════════════════════════════════════════
    # THE STRUCTURAL FIX — 10 beats
    # ═══════════════════════════════════════════════════════

    (64, "THE STRUCTURAL FIX",
     "The fix isn't 'spend less.'",
     "The words SPEND LESS crossed out with a bold red X. Not because it's wrong — because it's not a system. "
     "Alex beside it, nodding: 'already tried that.' Camera: wide — the crossed-out advice. Motion: FAST ZOOM IN on the X."),

    (65, "THE STRUCTURAL FIX",
     "That's not a system. That's a wish.",
     "Split: SYSTEM (interlocking gears — a mechanism) vs WISH (a single star — a hope). "
     "SPEND LESS label sits in the WISH column. SYSTEM column is empty — ready to be filled. "
     "Camera: split panel. Motion: PAN LEFT then PAN RIGHT — both columns."),

    (66, "THE STRUCTURAL FIX",
     "For the Card Gap: switch one category to cash. Groceries. Restaurants. One category.",
     "Alex at grocery store with physical cash. Expression: slightly deliberate — the friction is intentional now. "
     "Brain Villain feels the signal it was missing: the pain spike fires correctly. "
     "Camera: medium — grocery checkout. Motion: SLOW ZOOM IN toward cash leaving Alex's hand."),

    (67, "THE STRUCTURAL FIX",
     "You don't need to feel the money leaving everywhere. Just somewhere.",
     "EVERYWHERE (credit card icons overwhelming the frame — chaotic) vs SOMEWHERE (one cash transaction — precise). "
     "Targeted friction beats total friction. Camera: split panel. Motion: SLOW ZOOM IN toward SOMEWHERE."),

    (68, "THE STRUCTURAL FIX",
     "For the Reward Drain: budget it. €80 a month. 'This is my earned money.'",
     "Alex's monthly budget on screen. New dedicated category: EARNED EXTRA — €80. "
     "The Villain has a container now. Camera: medium — budget screen. Motion: FAST ZOOM IN onto the €80 line."),

    (69, "THE STRUCTURAL FIX",
     "When it's gone, it's gone. The Villain needs a container, not a lecture.",
     "The €80 budget depleted — slot shows EMPTY. Brain Villain shrugs, satisfied. "
     "Container was enough — no lecture needed, no willpower required. "
     "Camera: close-up — empty budget slot. Motion: STATIC."),

    (70, "THE STRUCTURAL FIX",
     "For the Invisible Drain: one audit. Once a year. Not monthly — once.",
     "Calendar with ONE date circled per year: SUBSCRIPTION AUDIT. All other months empty. "
     "The simplicity is the solution. Camera: wide — full year calendar. Motion: SLOW ZOOM IN toward the single date."),

    (71, "THE STRUCTURAL FIX",
     "For Social Spending: one question before every non-essential purchase.",
     "Alex mid-purchase, hand reaching for product. Thought bubble appears: WHO AM I BUYING THIS FOR? "
     "The question pauses the automatic reach. Camera: medium — purchase pause moment. Motion: STATIC — the pause is it."),

    (72, "THE STRUCTURAL FIX",
     "'Who am I buying this for?' If the answer isn't you — pause.",
     "Alex's thought bubble splits: ME (solid, clear figure) vs GHOST AUDIENCE (transparent, dissolving). "
     "The answer determines the purchase. Camera: close-up — the two-option thought bubble. Motion: FAST ZOOM IN on the split."),

    (73, "THE STRUCTURAL FIX",
     "For the Pre-Spend: the salary hits the account. You don't touch it for 24 hours.",
     "Friday: salary notification appears. Alex's phone flips face-down deliberately. "
     "Timer starts: 24 HOURS. The gap between arrival and allocation. The pause is the system. "
     "Camera: medium — phone face-down with timer. Motion: SLOW ZOOM IN toward phone going face-down."),

    # ═══════════════════════════════════════════════════════
    # BRAIN VILLAIN'S LAST TRICK — 11 beats (template obligatorio)
    # ═══════════════════════════════════════════════════════

    (74, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain has one response to this list.",
     "Brain Villain in the skull, arms crossed, examining the five solutions. One finger raised — it has a counter. "
     "Camera: close-up — Brain Villain, one finger raised. Motion: SLOW ZOOM IN into the Villain's expression."),

    (75, "BRAIN VILLAIN'S LAST TRICK",
     "You're feeling it right now.",
     "Alex looks directly at camera — fourth wall break. Expression: knowing, directed at the viewer. "
     "Brain Villain mirrors the viewer's position — 'you, watching this.' "
     "Camera: direct address — medium close-up. Motion: STATIC."),

    (76, "BRAIN VILLAIN'S LAST TRICK",
     "Not resistance. Something quieter.",
     "Brain Villain sitting quietly, looking reasonable, wearing a WISDOM costume — graduation cap, small scroll. "
     "The resistance is dressed as common sense. Nothing alarming. Just quiet. "
     "Camera: close-up — Villain in the wisdom costume. Motion: SLOW ZOOM IN into the costume."),

    (77, "BRAIN VILLAIN'S LAST TRICK",
     "Something that sounds like common sense: 'I already know this.'",
     "Speech bubble: 'I ALREADY KNOW THIS.' — text IS the prop. The bubble looks calm, reasonable, like insight. "
     "Brain Villain nods sagely at the bubble — pleased with this particular defense. "
     "Camera: close-up — the speech bubble. Motion: FAST ZOOM IN onto the bubble text."),

    (78, "BRAIN VILLAIN'S LAST TRICK",
     "That thought is not wisdom. Not self-awareness.",
     "The 'I ALREADY KNOW THIS' bubble gets a bold red border — reclassified. "
     "It moves from the WISDOM column to: INVISIBLE DRAIN, WEARING INSIGHT COSTUME. "
     "Camera: wide — reclassification happening. Motion: FAST ZOOM IN on the reclassification arrow."),

    (79, "BRAIN VILLAIN'S LAST TRICK",
     "It is the Invisible Drain wearing the costume of insight.",
     "The INVISIBLE DRAIN slot from the list — but wearing the WISDOM costume. Same pattern, different disguise. "
     "Brain Villain points at the costumed slot with satisfaction: 'exactly.' "
     "Camera: close-up — Invisible Drain slot in the wisdom costume. Motion: STATIC — the metaphor lands."),

    (80, "BRAIN VILLAIN'S LAST TRICK",
     "The programs are not broken.",
     "Brain Villain's control panel — all five switches still ON. Banner across the panel: NOT BROKEN. "
     "The programs are doing exactly what they were designed to do. "
     "Camera: wide — control panel with banner. Motion: SLOW ZOOM IN into the panel."),

    (81, "BRAIN VILLAIN'S LAST TRICK",
     "They were built for a world where money was physical — coins you could feel, resources you could see leaving.",
     "Historical scene: Alex's ancestor (same character design, different era context) "
     "holding physical coins, trading at a market. The money transfer is visible, tactile, real. Warm earth tones. "
     "Camera: wide — historical scene. Motion: PAN RIGHT across the market."),

    (82, "BRAIN VILLAIN'S LAST TRICK",
     "In that world, the Pre-Spend was planning. The Reward Drain was recovery. The Card Gap didn't exist.",
     "Three-part panel: PRE-SPEND = PLANNING AHEAD (checkmark). REWARD DRAIN = RECOVERY (checkmark). "
     "CARD GAP = ? (empty slot — didn't exist). Warm historical light throughout. "
     "Camera: triptych — three historical reframings. Motion: PAN RIGHT across the three."),

    (83, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain was built for that world. Not this one.",
     "Split: THAT WORLD (coins, campfire — Brain Villain fits perfectly, looks content). "
     "THIS WORLD (direct deposits, one-click — Brain Villain confused, misaligned). Same program. Different world. "
     "Camera: split panel. Motion: PAN LEFT then PAN RIGHT."),

    (84, "BRAIN VILLAIN'S LAST TRICK",
     "These five systems were designed for the world you actually live in.",
     "Five solutions — CASH CATEGORY, EARNED CONTAINER, ANNUAL AUDIT, THE QUESTION, 24-HOUR GAP — "
     "displayed against modern world background. They fit this world. The programs don't. "
     "Camera: wide — five modern solutions in their context. Motion: SLOW ZOOM OUT — reveal all five."),

    # ═══════════════════════════════════════════════════════
    # IDENTITY CLOSE — 7 beats (max 9)
    # ═══════════════════════════════════════════════════════

    (85, "IDENTITY CLOSE",
     "Your money doesn't disappear.",
     "Alex looking at his empty bank account — but expression different now. Not defeated. Analytical. "
     "Same situation. New frame. Camera: medium — Alex + phone, new expression. Motion: SLOW ZOOM IN toward expression."),

    (86, "IDENTITY CLOSE",
     "It follows five very predictable routes.",
     "The five labeled slots shown as ROUTES: arrows from Alex's account to each destination. "
     "Predictable. Mappable. Not mysterious anymore. Alex studies the map like a navigation app. "
     "Camera: wide — five routes as a map. Motion: PAN RIGHT — tracing the routes."),

    (87, "IDENTITY CLOSE",
     "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
     "The five names in clean typography — simple, permanent, named. No slots, no icons. "
     "Just the names. Alex reads the list once — the names are now his. "
     "Camera: wide — clean typography, white background. Motion: STATIC — let the names settle."),

    (88, "IDENTITY CLOSE",
     "Name them. And they lose power.",
     "Each name gets a dimmer switch — as Alex names it, the switch turns down. "
     "Programs don't disappear but their automatic intensity reduces. Agency through naming. "
     "Camera: close-up — the five dimmer switches. Motion: FAST ZOOM IN 1s per dimmer — five rapid hits."),

    (89, "IDENTITY CLOSE",
     "You're not bad with money.",
     "Alex looks at camera — direct, warm. Not a pep talk. A correction. "
     "Brain Villain nods in agreement — for once, on the same team. "
     "Camera: direct address — medium close-up, warm. Motion: STATIC."),

    (90, "IDENTITY CLOSE",
     "You're running programs that were never designed for a world with direct deposits and one-click payments.",
     "Alex and Brain Villain side by side — not adversaries. Partners navigating a mismatch. "
     "Modern phone in Alex's hand. Brain Villain examines it with curiosity — learning. "
     "Camera: medium — Alex and Brain Villain as partners. Motion: SLOW ZOOM OUT — show both."),

    (91, "IDENTITY CLOSE",
     "Now you know which five. That's the first thing the Villain didn't want you to have.",
     "The five named routes on Alex's map — now in his hands. He holds the map. "
     "Brain Villain looks at the map, then at Alex — slightly caught. Knowledge is the advantage. "
     "Camera: medium — Alex holds the map, Brain Villain watching. Motion: SLOW ZOOM IN toward the map."),

    # ═══════════════════════════════════════════════════════
    # NEXT VIDEO TEASE — 4 beats
    # ═══════════════════════════════════════════════════════

    (92, "NEXT VIDEO TEASE",
     "Next week — the one decision that stops all five.",
     "A single action slot: ONE DECISION. Arrows from it connect to all five drain slots — cutting all five routes. "
     "The efficiency is the hook. Brain Villain stares at the slot — slightly alarmed. "
     "Camera: wide — single decision + five connections. Motion: SLOW ZOOM OUT — reveal all connections."),

    (93, "NEXT VIDEO TEASE",
     "Not five solutions. One.",
     "The word ONE large on screen. The five solutions fade out — replaced by a single elegant mechanism. "
     "Simplicity as the reveal. Alex holds up one finger — genuine. "
     "Camera: close-up — ONE dominant. Motion: FAST ZOOM IN onto ONE."),

    (94, "NEXT VIDEO TEASE",
     "Made once. Before the patterns activate.",
     "Timeline: DECISION made early (Monday / start of month). Five pattern triggers later — "
     "but the DECISION is already upstream of all of them. Made before the game starts. "
     "Camera: wide — timeline with early decision upstream. Motion: PAN LEFT — moving back to the early decision."),

    (95, "NEXT VIDEO TEASE",
     "See you Thursday.",
     "Alex in default pose — relaxed, confident. Brain Villain visible in skull, calm. "
     "The adversarial energy is gone — they're navigating together now. Thursday calendar visible in background. "
     "Camera: medium — Alex in closing pose. Motion: SLOW ZOOM OUT — final pull back, Alex + Brain Villain."),

]

# ── PDF GENERATION ──────────────────────────────────────────────────────────────

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

pdf_path = "/home/user/Claudeeee/V14_final_IMAGE_PROMPTS.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)

flow = [
    Paragraph("NEUROCENTS · VIDEO 14", H2),
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
