#!/usr/bin/env python3
"""V14 Production Doc — 5 Things That Drain Your Money Before Payday."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

STYLE_PREAMBLE = (
    "2D flat cartoon illustration, thick solid black outlines, clean solid color fills, "
    "no gradients. ALEX: large beige oval head (#F5E6C8), transparent glass upper skull "
    "revealing pink cartoon Brain Villain (#E8A598), small black dot eyes, thin neutral "
    "mouth, black spiky hair, BLUE t-shirt (NOT RED — verify every time), gray pants. "
    "Brain Villain: pink cartoon brain character, heavy-lidded eyes, slight smirk, small teeth. "
    "Palette: beige skin #F5E6C8 · pink brain #E8A598 · blue shirt · gray pants · "
    "green: savings/gains · red: loss/danger · white: diagram scenes. 16:9, 1280×720."
)

# Each entry: (SECTION, BEAT_NUM, NARRATION, IMAGE_PROMPT, CAMERA, LIGHTING, MOOD, CHARACTER_ACTION, CAPCUT_MOTION)
BEATS = [
    # ── HOOK ──
    (
        "HOOK — PRIMEROS 5 SEGUNDOS", 1,
        "Why does your money always disappear before payday?",
        "Alex standing at a kitchen counter staring at his phone. Bank balance on screen: €0.00. "
        "Expression: wide eyes, slight jaw drop — recognition, not panic. Brain Villain lights up inside skull, "
        "smirking, arms crossed. Calendar on wall shows two days left to payday. "
        "Bold number €0.00 visible on phone screen. NOTE: Viewer who just saw the thumbnail must "
        "recognize this scene in under 5 seconds.",
        "Medium close-up, slight low angle — phone dominant in frame",
        "Warm kitchen light, soft shadows",
        "Familiar dread — the viewer has been here",
        "Eyes fixed on phone, body still — frozen moment of recognition",
        "ZOOM IN FAST · 1.5s → toward phone screen and balance number",
    ),
    (
        "HOOK", 2,
        "Not sometimes. Every month.",
        "Alex at a desk. Three identical calendar pages side by side showing three different months — "
        "each with a red X through the last two days before payday. No text labels — the red X says it all.",
        "Wide shot — all three calendars visible",
        "Neutral flat light, slightly cold",
        "Pattern recognition — this is structural, not random",
        "Alex gestures toward calendars with open palm — 'look at this'",
        "PAN RIGHT · 3s across the three calendars",
    ),
    (
        "HOOK", 3,
        "It doesn't matter if you earn €2,000 or €6,000.",
        "Split frame: left side — simple apartment, Alex in casual clothes, phone shows €2,000 salary notification. "
        "Right side — nicer apartment, Alex in work shirt, phone shows €6,000 salary notification. "
        "Both Alex figures have identical expression: Brain Villain glowing with the same smirk.",
        "Split panel — left/right composition",
        "Left: slightly cooler light. Right: warmer — but same Brain Villain in both",
        "Universality — the income level is irrelevant",
        "Both Alexes look at their phones simultaneously — mirror pose",
        "PAN LEFT · 3s then PAN RIGHT · 3s — scanning both panels",
    ),
    (
        "HOOK", 4,
        "Four weeks. Same empty account.",
        "Alex viewed from above — sitting on floor leaning against wall. "
        "Four empty wallet icons arranged in a circle around him — one per week. All empty. "
        "No text. The empty wallets speak for themselves.",
        "Bird's eye view — Alex small in center, wallets surrounding",
        "Flat overhead light — clinical, exposing",
        "Inevitability — the cycle is locked",
        "Arms resting on knees, head slightly tilted — tired but not surprised",
        "ZOOM OUT SLOW · 4s — reveal the full circle of empty wallets",
    ),
    (
        "HOOK", 5,
        "Five things are doing this to you.",
        "Dark background. Five numbered slots arranged vertically (5 → 1), each empty with a '?' icon. "
        "Slots pulse faintly — anticipation. Brain Villain in corner, finger counting down: 5, 4, 3...",
        "Center composition — list fills the frame",
        "Dark background with soft glow on slots — spotlight effect",
        "Tension building — the countdown starts",
        "Brain Villain counting with one finger raised, slightly amused",
        "ZOOM IN SLOW · 5s — into the numbered list",
    ),
    (
        "HOOK", 6,
        "And number one runs before you even get paid.",
        "Close-up on slot #1 — still showing '?'. A calendar behind it shows WEDNESDAY. "
        "Payday arrow points to FRIDAY. But the '?' pulses at WEDNESDAY — the drain starts early.",
        "Extreme close-up — slot #1 dominant",
        "Red-tinted light on the Wednesday marker",
        "Intrigue — the violation happens BEFORE the money arrives",
        "Brain Villain leans toward slot #1 with a knowing smirk",
        "ZOOM IN FAST · 1s → on the Wednesday marker",
    ),
    (
        "HOOK", 7,
        "Not when you spend it. Before.",
        "Timeline graphic: payday arrow on the right (FRIDAY). Brain Villain activity spike on the LEFT "
        "(WEDNESDAY). The spike is earlier than the money. No text labels — the visual timeline tells it.",
        "Wide center — timeline fills frame",
        "Clean white background — diagram style",
        "Revelation — the timing is wrong in a new way",
        "Brain Villain sits ON the Wednesday spike, arms crossed, pleased",
        "DIAGONAL PAN + ZOOM IN · 4s — from left (Wednesday spike) toward right (payday)",
    ),
    (
        "HOOK", 8,
        "Here's the list.",
        "The five numbered slots from beat 5, now fully illuminated. Still showing '?' in each — "
        "but the list is real, the countdown is starting. Brain Villain stands beside it like a game show host.",
        "Medium shot — Alex and the list side by side",
        "Bright reveal lighting — show is starting",
        "Anticipation peaks — we're going in",
        "Alex turns to look at list — the journey begins",
        "ZOOM IN SLOW · 3s — into the top of the list",
    ),
    # ── SETUP ──
    (
        "SETUP", 9,
        "These aren't budgeting mistakes.",
        "Torn budget spreadsheet on a desk. Alex's hand is not crumpling it — "
        "he's just observing it, confused. Brain Villain floats above, shaking its head: 'not this'.",
        "Medium — desk level angle",
        "Neutral flat light",
        "Clarification — the problem is deeper than a spreadsheet",
        "Alex looks at spreadsheet with mild confusion, not shame",
        "STATIC · 2s",
    ),
    (
        "SETUP", 10,
        "They're not discipline failures.",
        "Alex at 5:30 AM, gym bag over shoulder, coffee in hand — clearly disciplined. "
        "Brain Villain rides on his shoulder, still running. Caption on gym clock: 5:30 AM. "
        "Discipline is NOT the issue.",
        "Medium — full body shot, slight low angle (makes Alex look capable)",
        "Early morning blue-grey light",
        "Capability — discipline exists, the problem is elsewhere",
        "Alex in confident stride — he has discipline",
        "PAN RIGHT · 3s — following Alex's walk",
    ),
    (
        "SETUP", 11,
        "They're patterns. And they run automatically.",
        "Inside Alex's glass skull — Brain Villain at a control panel with five switches, "
        "all flipped ON. Labels on switches are blank — the viewer doesn't know what they are yet. "
        "The switches are running without Alex's input.",
        "Close-up — skull interior, control panel filling frame",
        "Warm amber glow from inside the skull",
        "Automation — these are programs, not choices",
        "Brain Villain's hand hovers over the panel — it's already running",
        "ZOOM IN SLOW · 4s — into the control panel",
    ),
    (
        "SETUP", 12,
        "Number five is the one everyone knows. And still can't stop.",
        "Slot #5 on the list illuminates — still '?'. But a crowd of small figures (different people) "
        "all point at it simultaneously. Everyone knows this one. And yet.",
        "Medium — the list with crowd below it",
        "Spotlight on slot #5",
        "Familiar irony — knowledge doesn't equal immunity",
        "Alex in the crowd, arms crossed, nodding — 'yeah, I know this one'",
        "ZOOM IN FAST · 1.5s → onto slot #5",
    ),
    # ── ITEM 5 ──
    (
        "ITEM 5 — THE CARD GAP", 13,
        "Number five. The Card Gap.",
        "Slot #5 reveals its label: CARD GAP. Alex holds a contactless card in one hand, "
        "cash in the other. Brain Villain sits between them on a scale — "
        "cash side heavy, card side light. The gap is visual.",
        "Medium — the two hands + scale centered",
        "Split lighting: warm on cash side, cool on card side",
        "Introduction — naming the enemy",
        "Alex looks between the two hands — comparing",
        "ZOOM IN FAST · 1s → onto the scale between the two hands",
    ),
    (
        "ITEM 5", 14,
        "When you pay with cash, your brain registers loss.",
        "Alex at a register handing over four €10 bills. His expression: mild grimace — "
        "the money FEELS like it's leaving. Brain Villain in skull shows a pain indicator spike.",
        "Medium — register transaction angle",
        "Warm shop light",
        "Mild pain — the friction is real",
        "Alex's hand slightly hesitates before releasing the bills",
        "ZOOM IN SLOW · 3s — toward the bills changing hands",
    ),
    (
        "ITEM 5", 15,
        "You feel the €40 leave.",
        "Close-up on Alex's face: slight wince. The €40 amount visible on register display. "
        "No text — the expression and the number together tell it.",
        "Extreme close-up — Alex's eyes and the register display",
        "Warm register glow on face",
        "Physical sensation of money leaving",
        "Eyes move from bills to register — the loss registers in real time",
        "STATIC · 2s — let the expression land",
    ),
    (
        "ITEM 5", 16,
        "When you pay with card — tap, done — the pain disappears.",
        "Same register, same €40, but now Alex taps card. Expression: completely neutral, "
        "almost cheerful. Brain Villain in skull: the pain indicator is FLAT — zero signal.",
        "Same angle as beat 14 — direct visual contrast",
        "Same warm shop light — emphasizes the contrast is in the brain, not the scene",
        "Frictionless — dangerous absence of feeling",
        "Alex's hand taps card with zero hesitation — one fluid gesture",
        "ZOOM IN FAST · 1s → on the tap gesture",
    ),
    (
        "ITEM 5", 17,
        "Same purchase. Different brain response.",
        "Split frame: left — cash transaction (pain spike in Brain Villain). "
        "Right — card tap (flat line in Brain Villain). Same €40. Same store. Different internal state.",
        "Split panel — identical scenes, different brain readouts",
        "Identical lighting both sides — difference is ONLY internal",
        "Stark contrast — same external, different internal",
        "Two Alexes in mirror poses — only the Brain Villain panels differ",
        "PAN LEFT · 2s then PAN RIGHT · 2s",
    ),
    (
        "ITEM 5", 18,
        "Card users spend 20 to 47% more than cash users.",
        "Large stat on screen: +20% to +47% in bold. Alex stands beside it, "
        "Brain Villain points at the higher number with a smug expression. "
        "No academic labels — just the numbers.",
        "Wide — stat dominates, Alex secondary",
        "Clean white background — stat presentation",
        "Data revelation — the gap is enormous",
        "Brain Villain taps the 47% with one finger — 'this one's mine'",
        "ZOOM IN FAST · 1.5s → onto the percentage range",
    ),
    (
        "ITEM 5", 19,
        "Not because they want to. Because the payment doesn't feel like payment.",
        "Alex mid-swipe on a shopping app, expression completely blank — no guilt, no awareness. "
        "Brain Villain inside skull sits in a hammock — fully relaxed. Nothing to override.",
        "Medium — phone and Alex's face",
        "Soft blue screen light",
        "Unconscious spending — the absence of friction",
        "Finger scrolls and taps effortlessly — no internal resistance",
        "ZOOM IN SLOW · 4s — toward the phone screen",
    ),
    (
        "ITEM 5", 20,
        "Your brain is still waiting for the money to actually leave.",
        "Alex's skull interior: Brain Villain looks around confused, waiting for a signal "
        "that never comes. Outside the skull, money has already left the account — "
        "bank balance on phone shows lower number. Internal lag vs external reality.",
        "Medium — skull interior + phone balance juxtaposed",
        "Warm skull interior vs cool phone light",
        "Delay — the internal lag is the trap",
        "Brain Villain checks left and right — 'where's the signal?'",
        "ZOOM OUT SLOW · 4s — pull back to show both skull interior and phone",
    ),
    # ── ITEM 4 ──
    (
        "ITEM 4 — THE REWARD DRAIN", 21,
        "Number four. The Reward Drain.",
        "Slot #4 reveals: REWARD DRAIN. Alex at desk, exhausted, suit jacket over chair. "
        "Brain Villain in skull has a calculator: it's calculating something. "
        "A small 'I DESERVE THIS' thought bubble floats up.",
        "Medium — desk scene, Alex leaning back",
        "Late afternoon warm light — end of hard day",
        "Introduction — the calculation begins",
        "Alex rubs eyes with both hands — genuine fatigue",
        "ZOOM IN FAST · 1.5s → onto the thought bubble",
    ),
    (
        "ITEM 4", 22,
        "It's Thursday. You've had a brutal week.",
        "Thursday circled on a desk calendar. Stack of papers, empty coffee cups, "
        "multiple browser tabs visible. Classic brutal-week visual cues.",
        "Wide — full desk chaos visible",
        "Harsh office fluorescent light — it's been a long day",
        "Exhaustion — earned, real, visible",
        "Alex surveys the desk rubble with a tired but functional expression",
        "ZOOM OUT SLOW · 4s — reveal full desk chaos",
    ),
    (
        "ITEM 4", 23,
        "Alex has too. Deadlines. A difficult meeting. Late nights.",
        "Three-panel strip: (1) Alex at desk with deadline clock. (2) Alex in tense meeting, "
        "manager pointing. (3) Alex at desk at night, city lights behind. "
        "All three in one beat — the week compressed.",
        "Triptych — three small panels stacked or side by side",
        "Each panel slightly darker than the last — escalating fatigue",
        "Compression of a full week into one moment",
        "Alex's expression progresses: focused → stressed → exhausted",
        "PAN RIGHT · 4s across all three panels",
    ),
    (
        "ITEM 4", 24,
        "And his brain does something automatic.",
        "Inside Alex's skull — Brain Villain at the calculator, fingers moving fast. "
        "The calculation is running without Alex's awareness. Outside the skull: Alex's eyes are closed.",
        "Close-up — skull interior, calculator activity",
        "Warm amber skull light",
        "Automatic — the program runs without consent",
        "Brain Villain focused on calculator, completely absorbed",
        "ZOOM IN SLOW · 3s — into the calculator",
    ),
    (
        "ITEM 4", 25,
        "It calculates what he's owed.",
        "Calculator screen shows a balance: EFFORT → €?? OWED. "
        "Brain Villain writes on a small ledger: hours worked, difficulty, sacrifices. "
        "The debt column grows.",
        "Medium close-up — calculator + ledger",
        "Warm amber light",
        "Entitlement math — the brain keeps score",
        "Brain Villain's finger traces down the ledger columns with satisfaction",
        "ZOOM IN FAST · 1s → onto the OWED amount",
    ),
    (
        "ITEM 4", 26,
        "Not the salary. Something extra.",
        "Two columns side by side: SALARY (normal check icon) vs EXTRA (pulsing glow, special icon). "
        "Brain Villain points specifically at EXTRA — this is what it calculated for.",
        "Split composition — the two columns",
        "The EXTRA column has warmer, more inviting light",
        "Distinction — this is beyond compensation, it's reward logic",
        "Brain Villain's finger taps EXTRA with emphasis",
        "ZOOM IN SLOW · 3s — toward the EXTRA column",
    ),
    (
        "ITEM 4", 27,
        "'I worked hard. I deserve this.'",
        "Speech bubble from Alex's direction — but it floats inside the skull, "
        "not from Alex's mouth. It's the Brain Villain's voice, not a conscious decision. "
        "The words: I WORKED HARD. I DESERVE THIS. Bold inside the bubble.",
        "Close-up — skull interior + speech bubble",
        "Warm amber skull light",
        "The justification — self-serving but feels noble",
        "Brain Villain looks at the speech bubble with approval — 'exactly right'",
        "STATIC · 3s — let the words sit",
    ),
    (
        "ITEM 4", 28,
        "That sentence has cost more money than any impulse purchase.",
        "Receipt tape unrolling from Alex's pocket — stretching floor to ceiling. "
        "Each item on the receipt starts with 'I deserved...' — different purchases. "
        "The total at the bottom is very large.",
        "Wide — floor to ceiling receipt",
        "Cool clinical light — like a financial audit",
        "The cumulative cost — it adds up over a lifetime",
        "Alex looks up at the receipt with slow realization",
        "PAN UP · 5s — rising from bottom to top of the receipt",
    ),
    # ── ITEM 3 ──
    (
        "ITEM 3 — THE INVISIBLE DRAIN", 29,
        "Number three. The Invisible Drain.",
        "Slot #3 reveals: INVISIBLE DRAIN. Alex's phone — the subscription apps grid. "
        "Several have dust particle effects on their icons — not opened in months. "
        "Brain Villain is barely visible, almost transparent — the 'invisible' part.",
        "Close-up — phone screen with subscription app grid",
        "Screen glow, dark surroundings — late night feel",
        "Introduction — something hidden is running",
        "Alex stares at the apps with faint recognition — 'oh, those are still there'",
        "ZOOM IN SLOW · 4s — into the dusty app icons",
    ),
    (
        "ITEM 3", 30,
        "Right now, you have at least three subscriptions you've forgotten about.",
        "Grid of subscription logos (generic icons, no real brands) — three of them have "
        "'last opened: 4 months ago' timestamps. The apps are running silently.",
        "Wide — the full grid visible",
        "Dark screen-glow only — the darkness emphasizes invisibility",
        "Invisible drain — running in background like malware",
        "Alex's finger hovers over the icons without touching — not sure which to cancel",
        "ZOOM OUT SLOW · 3s — reveal full grid of subscriptions",
    ),
    (
        "ITEM 3", 31,
        "Apps you haven't opened in four months.",
        "Calendar showing: last opened date 4 months ago. The app icon visible beside it — "
        "collecting digital dust. Monthly charge still processing in the background.",
        "Medium — calendar + app icon composition",
        "Cool blue screen light",
        "Time passing unnoticed — the invisibility of routine",
        "Alex does not look at this — he's looking at a different screen",
        "STATIC · 2s",
    ),
    (
        "ITEM 3", 32,
        "Services that auto-renewed in January.",
        "January calendar page. Auto-renewal notification popping up — small, easy to dismiss. "
        "Alex's thumb swipes it away without reading. Money leaves quietly.",
        "Close-up — January calendar + dismissal notification",
        "Flat cold January light",
        "The casual cost — dismissed without thought",
        "Alex's thumb swipes the notification away in one fluid motion — habitual",
        "ZOOM IN FAST · 1s → on the notification being dismissed",
    ),
    (
        "ITEM 3", 33,
        "Why haven't you cancelled them?",
        "Alex staring at the subscription list. His hand reaches for the cancel button — "
        "but stops. Brain Villain inside skull holds up a 'WAIT' sign. The pause is the trap.",
        "Medium — Alex + phone, hand frozen",
        "Soft screen light",
        "The friction — cancellation requires a decision",
        "Hand hovering over cancel button — mid-air, frozen",
        "STATIC · 3s — the freeze is the point",
    ),
    (
        "ITEM 3", 34,
        "Because cancelling requires a decision. And decisions cost energy.",
        "Alex's energy meter (a visual gauge, like a phone battery) sitting at LOW. "
        "Two arrows: one points to SUBSCRIBE (easy) → energy meter barely drops. "
        "One points to CANCEL (hard) → energy meter drops more. The asymmetry is visual.",
        "Wide — energy meter + decision arrows",
        "Clean white background — diagram clarity",
        "Energy economics — the cost of action vs inaction",
        "Brain Villain points at the asymmetry with a knowing nod",
        "ZOOM IN SLOW · 4s — into the energy meter",
    ),
    (
        "ITEM 3", 35,
        "Your brain doesn't cancel things. It lets them run.",
        "Inside Alex's skull — Brain Villain sits in a recliner, watching the subscriptions run "
        "like a screensaver. Passive. Comfortable. The Villain is NOT acting — that's the problem.",
        "Close-up — skull interior, Villain in recliner",
        "Warm amber skull light",
        "Default mode — inaction as the program",
        "Brain Villain crossed arms, eyes half-closed — comfortably passive",
        "ZOOM IN SLOW · 4s — into the recliner scene",
    ),
    # ── CTA ──
    (
        "CTA", 36,
        "If your brain is doing this to you right now — subscribe.",
        "Alex looks directly at camera — fourth wall break. Expression: knowing, complicit. "
        "Brain Villain peeks from behind his skull with a slightly defensive look. "
        "Subscribe button graphic appears — simple, no hard sell.",
        "Direct address — slight zoom toward camera",
        "Clean warm light — personal, direct",
        "Connection — the viewer is seen",
        "Alex holds gaze at camera for a full beat — genuine, not salesy",
        "ZOOM IN SLOW · 3s — toward Alex's direct gaze",
    ),
    (
        "CTA", 37,
        "We break down a new pattern every week. It's free. And it might save you more than you think.",
        "Small visual: weekly calendar with a Neurocents logo appearing each week. "
        "Simple, non-flashy. The value is in the consistency.",
        "Medium — calendar + logo",
        "Clean neutral light",
        "Understated value — no hype, just regularity",
        "Alex nods once, returns to the list — CTA done, moving on",
        "STATIC · 3s",
    ),
    # ── ITEM 2 ──
    (
        "ITEM 2 — SOCIAL SPENDING", 38,
        "Number two. Social Spending.",
        "Slot #2 reveals: SOCIAL SPENDING. Alex in a mirror — looking at himself in a new jacket. "
        "Behind him, a crowd of translucent ghost figures (the imaginary audience). "
        "They're watching. Except they're not real.",
        "Medium — mirror scene, ghost audience visible in reflection",
        "Vanity lighting — warm, flattering",
        "Introduction — performing for an audience that doesn't exist",
        "Alex adjusts jacket collar, looking at ghost audience more than himself",
        "ZOOM IN SLOW · 4s — into the mirror reflection",
    ),
    (
        "ITEM 2", 39,
        "You bought something this month for an audience that wasn't watching.",
        "Same ghost audience from beat 38 — but now shown from their perspective: "
        "they're all looking elsewhere, phones out, distracted. Not watching at all. "
        "Alex is buying for no one.",
        "Wide — ghost audience, all looking away",
        "Cool light on the audience — detached, absent",
        "The absence — the audience is fictional",
        "Ghost figures face away or look at their own phones — completely indifferent",
        "ZOOM OUT SLOW · 4s — reveal the full indifferent audience",
    ),
    (
        "ITEM 2", 40,
        "The car that looks good in the parking lot.",
        "Alex's car in an empty parking lot at night. No one around. "
        "The car looks good. The lot is empty. Ghost audience members stand at the edges — "
        "but they're translucent, barely there.",
        "Wide — car in empty parking lot",
        "Night lighting, cool and lonely",
        "The performance without an audience",
        "Alex stands beside the car, looking at it — not getting in",
        "PAN LEFT · 4s across the empty lot",
    ),
    (
        "ITEM 2", 41,
        "The jacket for the meeting.",
        "Alex in a boardroom in a sharp jacket. The other meeting participants are ghost figures "
        "— translucent, barely registering. Alex notices his own jacket cuff adjustment. "
        "The jacket mattered more to him than the meeting.",
        "Medium — boardroom, Alex prominent, others ghosted",
        "Cool conference room light",
        "Performance anxiety — the audience exists only in his head",
        "Alex smooths jacket lapel mid-meeting — the gesture reveals the priority",
        "ZOOM IN SLOW · 3s — onto the jacket cuff adjustment",
    ),
    (
        "ITEM 2", 42,
        "The upgrade nobody asked for but someone might notice.",
        "Alex's desk: new monitor setup, latest accessories. "
        "Post-it note on monitor: 'Nobody asked for this.' "
        "The note is Alex's own realization. Ghost audience in background — not noticing.",
        "Medium — desk setup",
        "Home office light — personal space",
        "Self-aware irony — the upgrade served no one",
        "Alex looks at the setup, then at the ghost audience, then back — slight grimace",
        "ZOOM IN FAST · 1.5s → onto the post-it note",
    ),
    (
        "ITEM 2", 43,
        "Who is that person you're buying for?",
        "Alex faces camera directly, expression genuinely questioning. "
        "Around him, ghost audience figures slowly dissolve — they're fading. "
        "The question lands in the empty space they leave.",
        "Direct address — medium close-up",
        "Light focuses on Alex, background dims as audience fades",
        "Confrontation — gentle, not accusatory",
        "Alex holds the question with honest curiosity, not shame",
        "STATIC · 3s — let the question breathe",
    ),
    (
        "ITEM 2", 44,
        "They don't exist. They're a projection.",
        "The ghost audience is now completely transparent — almost invisible. "
        "Alex's Brain Villain projects them like a film projector from inside the skull. "
        "The audience is his own output.",
        "Medium — the projector-skull visual",
        "Warm skull light projecting cold ghost light",
        "Revelation — the audience is internal, not external",
        "Brain Villain operates the projector, slight satisfaction in its expression",
        "ZOOM IN SLOW · 4s — into the projector inside the skull",
    ),
    (
        "ITEM 2", 45,
        "The most expensive audience in your life has never spent a single dollar.",
        "A financial ledger: left column — GHOST AUDIENCE COSTS (long list, €€€). "
        "Right column — GHOST AUDIENCE CONTRIBUTIONS: empty. "
        "The asymmetry is total.",
        "Wide — ledger fills frame",
        "Clean white accounting light",
        "The cost accounting — pure loss",
        "Brain Villain reviews the ledger with academic interest — 'fascinating'",
        "ZOOM IN SLOW · 4s — into the empty contributions column",
    ),
    (
        "ITEM 2", 46,
        "They live entirely in your head. And they have expensive taste.",
        "Alex's skull cross-section: inside, the ghost audience sits in tiny theater seats — "
        "watching a tiny Alex perform for them. Inside his own head. "
        "The recursion is the trap.",
        "Close-up — skull interior theater",
        "Warm amber skull light on the tiny internal theater",
        "The recursion — performing for self-generated audience",
        "Ghost audience in skull watches tiny Alex with approval — feeding the loop",
        "ZOOM IN FAST · 1.5s → into the tiny skull theater",
    ),
    # ── ITEM 1 ──
    (
        "ITEM 1 — THE PRE-SPEND", 47,
        "Number one. The one nobody names.",
        "Slot #1 glows brightest — still '?'. The other four slots visible but dimmed. "
        "Brain Villain stands beside slot #1 with arms crossed — guarding it. "
        "The reveal is coming.",
        "Wide — all five slots, #1 dominant",
        "Spotlight on slot #1",
        "Peak anticipation — the reveal is imminent",
        "Brain Villain stands protectively in front of slot #1 — 'you sure you want to know?'",
        "ZOOM IN FAST · 2s → onto slot #1",
    ),
    (
        "ITEM 1", 48,
        "The Pre-Spend.",
        "Slot #1 reveals: THE PRE-SPEND. The Brain Villain steps aside reluctantly. "
        "The name appears in bold — revealed for the first time.",
        "Close-up — the slot reveal",
        "Bright reveal light — like a game show",
        "Revelation — the name lands",
        "Brain Villain steps back, slightly caught — the program has been named",
        "ZOOM IN FAST · 1s → onto the text THE PRE-SPEND",
    ),
    (
        "ITEM 1", 49,
        "It's Wednesday. Payday is Friday.",
        "Alex at a desk. Wednesday date visible on calendar. "
        "Payday circled on Friday — two days away. "
        "Alex's phone shows current balance: not zero, but declining.",
        "Medium — desk with calendar and phone",
        "Neutral office light",
        "Setup — the timeline is established",
        "Alex glances at calendar, then at phone balance",
        "ZOOM IN SLOW · 3s — toward the calendar",
    ),
    (
        "ITEM 1", 50,
        "Alex hasn't received anything yet.",
        "Bank notification on Alex's phone: NEXT DEPOSIT: FRIDAY. "
        "Current balance visible — the money is NOT there yet. "
        "Timestamp: WEDNESDAY, 2:00 PM.",
        "Close-up — phone notification",
        "Screen glow",
        "Before — the money hasn't arrived",
        "Alex reads the notification, expression neutral",
        "STATIC · 2s",
    ),
    (
        "ITEM 1", 51,
        "But his brain has already spent it.",
        "Inside Alex's skull: Brain Villain at an accounting desk — "
        "rapidly typing on a calculator, moving money allocation arrows. "
        "The salary hasn't arrived but the Villain is already processing it.",
        "Close-up — skull interior, frantic allocation activity",
        "Warm amber skull light, slightly frantic energy",
        "Pre-emption — the spending happens mentally before physically",
        "Brain Villain's fingers move fast over the calculator — deadline mentality",
        "ZOOM IN FAST · 1.5s → onto the Brain Villain's allocation work",
    ),
    (
        "ITEM 1", 52,
        "Not metaphorically. Neurologically.",
        "Split label: left — METAPHOR (crossed out). Right — NEUROLOGY (highlighted). "
        "Brain scan silhouette showing activity in decision-making region — it's literal.",
        "Split panel — clean white background",
        "Clinical bright light — medical precision",
        "Scientific grounding — this is physical, not poetic",
        "Alex observes the split panel — nodding at the neurology side",
        "ZOOM IN SLOW · 3s — toward the NEUROLOGY label",
    ),
    (
        "ITEM 1", 53,
        "The moment you know money is coming — your brain allocates it.",
        "Timeline: WEDNESDAY knowledge → immediate allocation arrows fire in brain. "
        "FRIDAY payday comes AFTER the allocation is complete. "
        "The brain processes the future money as if it already arrived.",
        "Wide — timeline graphic",
        "Clean white diagrammatic light",
        "The mechanism — the sequence is wrong",
        "Brain Villain stands at the Wednesday point — 'already done it'",
        "PAN RIGHT · 4s — moving along the timeline from Wednesday to Friday",
    ),
    (
        "ITEM 1", 54,
        "The rent. The pending bill. The thing you've been delaying.",
        "Three allocation boxes filling up in Alex's mental budget: RENT ✓, BILL ✓, DELAYED THING ✓. "
        "Each gets checked off by Brain Villain — but the money isn't there yet.",
        "Medium — the three allocation boxes",
        "Warm amber skull light",
        "Legitimate allocations first — the logic seems sound",
        "Brain Villain checks each box efficiently — doing real financial work",
        "ZOOM IN SLOW · 4s — into the allocation boxes",
    ),
    (
        "ITEM 1", 55,
        "And then — quietly — a few things that feel deserved.",
        "The allocation boxes continue: after RENT, BILL, DELAYED THING — "
        "a fourth box appears, smaller, slightly dimmer: 'DESERVED EXTRA'. "
        "Brain Villain adds it quietly, almost sheepishly.",
        "Close-up — the fourth box appearing",
        "The fourth box glows slightly differently — warmer, more personal",
        "The creep — the deserved items slip in quietly",
        "Brain Villain adds the fourth box with a subtle gesture — not announcing it",
        "ZOOM IN FAST · 1.5s → onto the DESERVED EXTRA box",
    ),
    (
        "ITEM 1", 56,
        "By the time Friday arrives, the money is already gone in your mind.",
        "Friday arrives on calendar — payday notification appears. "
        "But Alex's mental budget is already at zero — all allocated. "
        "The money arrives into an already-empty mental account.",
        "Medium — calendar Friday + empty mental budget",
        "Cool Friday light — the anticlimax",
        "Pre-consumption — arrival of money is just confirmation",
        "Alex sees payday notification with mild expression — already knew it",
        "STATIC · 3s — the anticlimax lands",
    ),
    (
        "ITEM 1", 57,
        "Friday is just the confirmation.",
        "Split: left — WEDNESDAY (mental spend complete, arrows all allocated). "
        "Right — FRIDAY (money arrives, immediately absorbed). The arrow from right to left "
        "shows the mental spend preceded the physical arrival.",
        "Wide — split timeline",
        "Clean white diagram light",
        "The inversion — mental precedes physical",
        "Brain Villain on the Wednesday side looks smug — 'already handled it'",
        "PAN LEFT · 3s — from Friday back to Wednesday (reverse direction is the point)",
    ),
    (
        "ITEM 1", 58,
        "You don't spend your salary. You process a transaction your brain closed on Wednesday.",
        "Alex at ATM or bank app — Friday. The transaction processes. "
        "But Brain Villain holds up a 'RECEIPT' dated WEDNESDAY. "
        "The deal was done two days ago.",
        "Close-up — the Wednesday receipt in Brain Villain's hand",
        "Cool ATM light",
        "The reframe — the action was earlier than the event",
        "Brain Villain hands the Wednesday receipt to Alex — 'just confirming what I already decided'",
        "ZOOM IN FAST · 1.5s → onto the WEDNESDAY date on the receipt",
    ),
    # ── MECHANISM CONCLUSION ──
    (
        "MECHANISM CONCLUSION", 59,
        "Five patterns. Running automatically.",
        "All five slots now fully labeled and lit: CARD GAP · REWARD DRAIN · INVISIBLE DRAIN · "
        "SOCIAL SPENDING · PRE-SPEND. Five program indicators — all ON.",
        "Wide — the full list, all lit",
        "Clean reveal lighting",
        "Inventory — all five named",
        "Alex stands in front of the complete list — the full picture visible",
        "ZOOM OUT SLOW · 5s — pull back to reveal all five simultaneously",
    ),
    (
        "MECHANISM CONCLUSION", 60,
        "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
        "Each slot highlighted in sequence as the names are spoken — "
        "a rapid highlight sequence. The names land one by one.",
        "Wide — same list view",
        "Each slot pulses briefly as named",
        "Recognition — the viewer names them too",
        "Alex's finger points to each in sequence — naming them out loud",
        "ZOOM IN FAST · 0.5s per slot — five rapid hits",
    ),
    (
        "MECHANISM CONCLUSION", 61,
        "None of them feel like mistakes when they happen.",
        "Alex mid-Card Gap tap, mid-Reward purchase, mid-subscription-ignore — "
        "three micro-scenes in one frame. Expression in each: completely normal, "
        "reasonable, justified. No guilt visible.",
        "Triptych — three micro-scenes",
        "Normal, ambient light in each — nothing dramatic",
        "Normality — these feel correct in the moment",
        "Alex in each mini-scene looks completely at ease — that's the trap",
        "PAN RIGHT · 4s across the three scenes",
    ),
    (
        "MECHANISM CONCLUSION", 62,
        "The Card Gap feels convenient.",
        "Single slot: CARD GAP. Adjective appears: CONVENIENT. "
        "Alex taps card — expression is pleased. The feeling is real.",
        "Close-up — CARD GAP slot + CONVENIENT label",
        "Clean light",
        "The subjective reality — it genuinely feels this way",
        "Alex taps card with mild pleasure — the convenience is real to him",
        "ZOOM IN SLOW · 2s",
    ),
    (
        "MECHANISM CONCLUSION", 63,
        "The Reward Drain feels earned. The Social Spend feels reasonable. The Pre-Spend feels like planning.",
        "Three slots in rapid sequence: REWARD DRAIN + EARNED · SOCIAL SPENDING + REASONABLE · "
        "PRE-SPEND + PLANNING. Each pairing makes ironic sense. The trap is the logic.",
        "Rapid three-panel reveal",
        "Warm light on each — they all feel right",
        "Ironic recognition — the feelings are real, the patterns are traps",
        "Alex nods at each pairing — 'yes, that's exactly how it felt'",
        "ZOOM IN FAST · 1s per panel — three rapid hits",
    ),
    # ── THE STRUCTURAL FIX ──
    (
        "THE STRUCTURAL FIX", 64,
        "The fix isn't 'spend less.'",
        "The words SPEND LESS crossed out with a bold red X. "
        "Not because spending less is bad — but because it's not a system. "
        "Alex beside it, nodding. He already knew this wasn't the answer.",
        "Wide — the crossed-out advice",
        "Clean white background",
        "Dismissal — the obvious answer isn't the right one",
        "Alex gestures toward the X with agreement — 'already tried that'",
        "ZOOM IN FAST · 1.5s → onto the red X",
    ),
    (
        "THE STRUCTURAL FIX", 65,
        "That's not a system. That's a wish.",
        "Split: SYSTEM (gears interlocking — a mechanism) vs WISH (a single star — a hope). "
        "SPEND LESS goes in the WISH column. Nothing in the SYSTEM column yet.",
        "Split panel — SYSTEM vs WISH",
        "Clean diagrammatic light",
        "The distinction — wishes vs systems",
        "Alex moves 'spend less' label from one side to the other — it belongs in WISH",
        "PAN LEFT · 2s then PAN RIGHT · 2s — showing both columns",
    ),
    (
        "THE STRUCTURAL FIX", 66,
        "For the Card Gap: switch one category to cash. Groceries. Restaurants. One category.",
        "Alex at grocery store with physical cash. Expression: slightly more deliberate — "
        "the friction is intentional now. Brain Villain feels the signal it was missing.",
        "Medium — grocery checkout, cash transaction",
        "Warm grocery store light",
        "Friction by design — the solution is structural",
        "Alex counts bills deliberately — feeling each one leave",
        "ZOOM IN SLOW · 3s — toward the cash leaving Alex's hand",
    ),
    (
        "THE STRUCTURAL FIX", 67,
        "You don't need to feel the money leaving everywhere. Just somewhere.",
        "EVERYWHERE (credit card icons filling the frame — overwhelming) vs "
        "SOMEWHERE (one cash transaction — specific, intentional). "
        "The targeted friction beats total friction.",
        "Split panel — everywhere vs somewhere",
        "Cooler light on EVERYWHERE (chaos), warmer on SOMEWHERE (controlled)",
        "Targeted precision — one point of friction is enough",
        "Alex's hand in the SOMEWHERE panel — deliberate, calm",
        "ZOOM IN SLOW · 3s — toward the SOMEWHERE panel",
    ),
    (
        "THE STRUCTURAL FIX", 68,
        "For the Reward Drain: budget it. €80 a month. 'This is my earned money.'",
        "Alex's monthly budget on screen. New category: EARNED EXTRA — €80. "
        "The category has its own dedicated slot. The villain has a container now.",
        "Medium — budget screen",
        "Warm accounting light",
        "Containment — giving the pattern a sanctioned outlet",
        "Alex adds the EARNED EXTRA line with deliberate satisfaction",
        "ZOOM IN FAST · 1.5s → onto the EARNED EXTRA €80 line",
    ),
    (
        "THE STRUCTURAL FIX", 69,
        "When it's gone, it's gone. The Villain needs a container, not a lecture.",
        "The €80 budget depleted — the slot shows EMPTY. Brain Villain shrugs, satisfied. "
        "The container was enough — no lecture needed, no willpower required.",
        "Close-up — the empty budget slot",
        "Neutral light — this is fine, not a failure",
        "Sufficiency — the container works",
        "Brain Villain looks at empty slot and shrugs — 'fair enough'",
        "STATIC · 2s",
    ),
    (
        "THE STRUCTURAL FIX", 70,
        "For the Invisible Drain: one audit. Once a year. Not monthly — once.",
        "Calendar with ONE annual date circled: SUBSCRIPTION AUDIT. "
        "All other months empty — no recurring task. "
        "The simplicity is the solution.",
        "Wide — full year calendar",
        "Clean neutral light",
        "Simplicity — one action, maximum leverage",
        "Alex circles the annual date with deliberate confidence — this is manageable",
        "ZOOM IN SLOW · 3s — toward the single circled date",
    ),
    (
        "THE STRUCTURAL FIX", 71,
        "For Social Spending: one question before every non-essential purchase.",
        "Alex mid-purchase — hand reaching for a product. "
        "Thought bubble appears: WHO AM I BUYING THIS FOR? "
        "The question pauses the action.",
        "Medium — purchase pause moment",
        "Warm store light, slightly desaturated to indicate pause",
        "The pause — the question creates friction",
        "Alex's hand freezes mid-reach — the question stops the automatic motion",
        "STATIC · 3s — the pause is the mechanism",
    ),
    (
        "THE STRUCTURAL FIX", 72,
        "'Who am I buying this for?' If the answer isn't you — pause.",
        "Alex's thought bubble shows: ME (clear, solid figure) vs GHOST AUDIENCE "
        "(transparent, dissolving). The answer determines the purchase.",
        "Close-up — the two-option thought bubble",
        "Thought bubble has warmer light on ME side",
        "Decision clarity — the question cuts through",
        "Alex tilts head considering — actually evaluating, not defaulting",
        "ZOOM IN FAST · 1.5s → onto the ME vs GHOST split",
    ),
    (
        "THE STRUCTURAL FIX", 73,
        "For the Pre-Spend: the salary hits the account. You don't touch it for 24 hours.",
        "Friday: salary notification appears. Alex's phone flips face-down. "
        "Timer starts: 24 HOURS. The deliberate pause — the gap between arrival and allocation.",
        "Medium — phone face-down with timer",
        "Neutral Friday light",
        "The gap — the pause prevents the automatic allocation from winning",
        "Alex places phone face-down with intention — the gesture is the system",
        "ZOOM IN SLOW · 3s — toward the phone going face-down",
    ),
    # ── BRAIN VILLAIN'S LAST TRICK ──
    (
        "BRAIN VILLAIN'S LAST TRICK", 74,
        "The Brain Villain has one response to this list.",
        "Brain Villain in the skull, arms crossed, looking at the five solutions. "
        "It's processing. One finger raised — it has a counter.",
        "Close-up — Brain Villain, one finger raised",
        "Warm amber skull light",
        "Setup — the Villain is not done",
        "Brain Villain tilts head slightly, calculating its response",
        "ZOOM IN SLOW · 3s — into the Brain Villain's expression",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 75,
        "You're feeling it right now.",
        "Direct address — Alex looks at camera again. "
        "But this time the expression is directed at the viewer: 'you're feeling this.' "
        "Brain Villain mirrors the viewer's position.",
        "Direct address — medium close-up",
        "Warm personal light",
        "Second person — the viewer is implicated",
        "Alex holds gaze at camera — knowing, not accusatory",
        "STATIC · 3s",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 76,
        "Not resistance. Something quieter.",
        "Not Brain Villain fighting. Instead: Brain Villain sitting quietly, "
        "looking reasonable, wearing a WISDOM costume. The resistance is dressed as sense.",
        "Close-up — Villain in the wisdom costume",
        "Soft light — nothing alarming, just quiet",
        "The disguise — resistance doesn't look like resistance",
        "Brain Villain adjusts its 'wise' costume, expression calm and reasonable",
        "ZOOM IN SLOW · 3s — into the wisdom costume",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 77,
        "Something that sounds like common sense: 'I already know this.'",
        "Speech bubble from the Villain's direction: 'I ALREADY KNOW THIS.' "
        "The bubble looks calm, reasonable, like genuine insight. That's the trap.",
        "Close-up — the speech bubble",
        "Soft warm light — the comfort of familiarity",
        "The false insight — knowing and changing are not the same",
        "Brain Villain nods sagely at the speech bubble — very pleased with itself",
        "ZOOM IN FAST · 1.5s → onto the speech bubble text",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 78,
        "That thought is not wisdom. Not self-awareness.",
        "The 'I ALREADY KNOW THIS' bubble gets a red border — reclassified. "
        "It moves from the WISDOM column to a new column: INVISIBLE DRAIN, WEARING INSIGHT COSTUME.",
        "Wide — the reclassification happening",
        "Slightly cooler light as the reclassification occurs",
        "Exposure — the false label is corrected",
        "Alex watches the reclassification with recognition — 'oh. oh no.'",
        "ZOOM IN FAST · 1s → onto the reclassification arrow",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 79,
        "It is the Invisible Drain wearing the costume of insight.",
        "Visual metaphor: the INVISIBLE DRAIN slot from the list — "
        "but now wearing the WISDOM costume. The same pattern, different disguise.",
        "Close-up — Invisible Drain slot in the wisdom costume",
        "Slightly deceptive warm light — it looks wise, it isn't",
        "The revelation — pattern recognition transfers",
        "Brain Villain points at the costumed slot with satisfaction — 'exactly'",
        "STATIC · 3s — the metaphor lands",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 80,
        "The programs are not broken.",
        "Brain Villain's control panel — all five switches still ON. "
        "But a banner across the panel: NOT BROKEN. "
        "The programs are doing exactly what they were designed to do.",
        "Wide — the control panel with banner",
        "Warm amber skull light",
        "Reframe beginning — the Villain is not the enemy",
        "Brain Villain looks at the banner and nods — 'correct'",
        "ZOOM IN SLOW · 4s — into the control panel",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 81,
        "They were built for a world where money was physical — coins you could feel, resources you could see leaving.",
        "Historical scene: Alex's ancestor holding physical coins, trading at a market. "
        "The money transfer is visible, tactile, real. The programs evolved for THIS world.",
        "Wide — historical scene, warm earth tones",
        "Warm historical light — past world",
        "Origin — the programs have legitimate history",
        "Historical Alex (same character, different era context) examines coins carefully",
        "PAN RIGHT · 4s — across the historical scene",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 82,
        "In that world, the Pre-Spend was planning. The Reward Drain was recovery. The Card Gap didn't exist.",
        "Split three-part panel: PRE-SPEND = PLANNING AHEAD. REWARD DRAIN = RECOVERY. "
        "CARD GAP = ? (slot empty — it didn't exist in that world).",
        "Triptych — three historical reframings",
        "Warm historical light throughout",
        "Historical accuracy — these were rational behaviors",
        "Brain Villain stands beside each panel nodding — 'these were good programs'",
        "PAN RIGHT · 4s across the three historical framings",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 83,
        "The Brain Villain was built for that world. Not this one.",
        "Split: THAT WORLD (physical coins, historical context — Brain Villain fits perfectly) "
        "vs THIS WORLD (direct deposits, one-click payments — Brain Villain is misaligned). "
        "Same program. Different world. Mismatch.",
        "Split panel — historical world vs modern world",
        "Warm historical light vs cool modern light",
        "The mismatch — the problem is context, not the program",
        "Brain Villain stands in the historical world looking comfortable; in the modern world looking confused",
        "PAN LEFT · 3s then PAN RIGHT · 3s",
    ),
    (
        "BRAIN VILLAIN'S LAST TRICK", 84,
        "These five systems were designed for the world you actually live in.",
        "The five solutions from earlier — CASH CATEGORY, EARNED CONTAINER, ANNUAL AUDIT, "
        "THE QUESTION, 24-HOUR GAP — now displayed against the modern world background. "
        "They fit. The programs don't. The systems do.",
        "Wide — the five solutions, modern world context",
        "Clean modern light",
        "The fit — the solutions were designed for this environment",
        "Alex stands beside the five modern solutions — they belong in his world",
        "ZOOM OUT SLOW · 5s — reveal all five systems in their context",
    ),
    # ── IDENTITY CLOSE ──
    (
        "IDENTITY CLOSE", 85,
        "Your money doesn't disappear.",
        "Alex looking at his empty bank account — but expression is different now. "
        "Not defeated. Analytical. The situation is the same. The frame has changed.",
        "Medium — Alex and phone, new expression",
        "Warmer light than beat 1 — same scene, different feel",
        "The reframe — same facts, new understanding",
        "Alex tilts head slightly — analyzing, not despairing",
        "ZOOM IN SLOW · 3s — toward Alex's new expression",
    ),
    (
        "IDENTITY CLOSE", 86,
        "It follows five very predictable routes.",
        "The five labeled slots again — but now they're shown as ROUTES: arrows leading from "
        "Alex's account to each destination. Predictable. Mappable. Not mysterious.",
        "Wide — the five routes as a map",
        "Clear navigation-style lighting",
        "Predictability — if you know the routes, you can redirect them",
        "Alex studies the map with the expression of someone reading a navigation app",
        "PAN RIGHT · 4s — tracing the routes",
    ),
    (
        "IDENTITY CLOSE", 87,
        "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
        "The five names in clean typography — simple, direct. No slots, no icons. "
        "Just the names, permanent and named.",
        "Wide — typography, clean white background",
        "Clean flat light",
        "Naming power — named things can be managed",
        "Alex reads the list once — the names are now his",
        "STATIC · 3s — let the names settle",
    ),
    (
        "IDENTITY CLOSE", 88,
        "Name them. And they lose power.",
        "Each name gets a dimmer switch — as Alex 'names' it, the switch turns down. "
        "The programs don't disappear but their automatic intensity reduces.",
        "Close-up — the dimmer switches",
        "Slightly warmer, lighter as each switch dims",
        "Agency — naming gives control",
        "Alex's hand at each dimmer, turning it down with intention",
        "ZOOM IN FAST · 1s per dimmer — five rapid hits",
    ),
    (
        "IDENTITY CLOSE", 89,
        "You're not bad with money.",
        "Alex looks at camera — direct, warm. Not a pep talk. A correction. "
        "Brain Villain nods in agreement — for once on the same team.",
        "Direct address — medium close-up, warm",
        "Warm personal light",
        "The identity shift — removing the false label",
        "Alex's expression: quiet confidence. Not a sales pitch. A fact.",
        "STATIC · 3s",
    ),
    (
        "IDENTITY CLOSE", 90,
        "You're running programs that were never designed for a world with direct deposits and one-click payments.",
        "Alex and Brain Villain side by side — not adversaries. Partners navigating a mismatch. "
        "Modern phone in Alex's hand. Brain Villain examining it with curiosity — learning.",
        "Medium — Alex and Brain Villain as partners",
        "Warm collaborative light",
        "Partnership — the Villain is not the enemy",
        "Brain Villain examines the phone with genuine interest — adapting",
        "ZOOM OUT SLOW · 4s — show both Alex and Brain Villain in the same frame",
    ),
    (
        "IDENTITY CLOSE", 91,
        "Now you know which five. That's the first thing the Villain didn't want you to have.",
        "The five named routes on Alex's map — now in his hands. He holds the map. "
        "Brain Villain looks at the map, then at Alex — slightly caught. "
        "The knowledge is the advantage.",
        "Medium — Alex holds the map, Brain Villain watching",
        "Warm empowering light",
        "The payoff — knowledge is the structural change",
        "Alex holds the map with ownership. Brain Villain has no counter.",
        "ZOOM IN SLOW · 4s — toward the map in Alex's hands",
    ),
    # ── NEXT VIDEO TEASE ──
    (
        "NEXT VIDEO TEASE", 92,
        "Next week — the one decision that stops all five.",
        "A single action slot labeled: ONE DECISION. Arrows from it connect to all five drain slots — "
        "cutting all five routes simultaneously. The efficiency is the hook.",
        "Wide — the single decision + five connections",
        "Clean white background — diagram",
        "Curiosity gap — one thing stops five patterns",
        "Brain Villain stares at the ONE DECISION slot — slightly alarmed",
        "ZOOM OUT SLOW · 4s — reveal all the connections from one point",
    ),
    (
        "NEXT VIDEO TEASE", 93,
        "Not five solutions. One.",
        "The word ONE large on screen. The five solutions from earlier fade out — "
        "replaced by a single elegant mechanism. Simplicity as the reveal.",
        "Close-up — ONE dominant",
        "Bright clean light",
        "Simplicity — the more elegant the solution, the more curiosity",
        "Alex holds up one finger — genuine",
        "ZOOM IN FAST · 1.5s → onto ONE",
    ),
    (
        "NEXT VIDEO TEASE", 94,
        "Made once. Before the patterns activate.",
        "Timeline: DECISION made early (Monday or start of month). "
        "Five pattern triggers later in the timeline — but the DECISION is already upstream. "
        "Made before the game started.",
        "Wide — timeline with decision upstream of patterns",
        "Clean diagrammatic light",
        "The upstream advantage — earlier is better",
        "Brain Villain looks at the decision point, then at the patterns — it can't run before the decision",
        "PAN LEFT · 3s — moving backward in the timeline to the early decision point",
    ),
    (
        "NEXT VIDEO TEASE", 95,
        "See you Thursday.",
        "Alex in his default pose — relaxed, confident. Brain Villain visible in skull, "
        "also calm. The adversarial energy is gone — they're figuring it out together. "
        "Thursday calendar date visible in background.",
        "Medium — Alex in closing pose",
        "Warm, resolved light — the tension is released",
        "Resolution — see you next time",
        "Alex's expression: knowing nod, slight smile. Not salesy. Just genuine.",
        "ZOOM OUT SLOW · 4s — final pull back, Alex and Brain Villain visible",
    ),
]

def build_production_pdf():
    path = "/home/user/Claudeeee/V14_final_PRODUCTION.pdf"
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('title', fontSize=14, leading=18,
                                  spaceBefore=0, spaceAfter=6,
                                  textColor=colors.HexColor('#B02A2A'),
                                  fontName='Helvetica-Bold', alignment=TA_CENTER)
    subtitle_style = ParagraphStyle('subtitle', fontSize=10, leading=14,
                                     spaceAfter=10, fontName='Helvetica',
                                     alignment=TA_CENTER,
                                     textColor=colors.HexColor('#2C3E50'))
    section_style = ParagraphStyle('section', fontSize=10, leading=14,
                                    spaceBefore=14, spaceAfter=4,
                                    textColor=colors.HexColor('#B02A2A'),
                                    fontName='Helvetica-Bold')
    beat_num_style = ParagraphStyle('beatnum', fontSize=8, leading=12,
                                     fontName='Helvetica-Bold',
                                     textColor=colors.HexColor('#777777'))
    narration_style = ParagraphStyle('narration', fontSize=10, leading=15,
                                      spaceAfter=4, fontName='Helvetica-Oblique',
                                      textColor=colors.HexColor('#2C3E50'))
    label_style = ParagraphStyle('label', fontSize=7, leading=10,
                                  fontName='Helvetica-Bold',
                                  textColor=colors.HexColor('#777777'))
    value_style = ParagraphStyle('value', fontSize=9, leading=13,
                                  spaceAfter=2, fontName='Helvetica')
    image_label_style = ParagraphStyle('imglab', fontSize=7, leading=10,
                                        fontName='Helvetica-Bold',
                                        textColor=colors.HexColor('#B02A2A'))
    image_value_style = ParagraphStyle('imgval', fontSize=8, leading=12,
                                        spaceAfter=6, fontName='Helvetica')

    story = []
    story.append(Paragraph("NEUROCENTS — VIDEO 14", title_style))
    story.append(Paragraph("5 Things That Drain Your Money Before Payday (No Matter What You Earn)", subtitle_style))
    story.append(Paragraph("PRODUCTION DOCUMENT · 95 beats · Hook S1 · Lista con Ranking · CapCut static", subtitle_style))
    story.append(Spacer(1, 0.3*cm))

    current_section = ""
    for row in BEATS:
        section, num, narration, image_prompt, camera, lighting, mood, char_action, capcut = row

        if section != current_section:
            current_section = section
            story.append(Paragraph(f"── {section} ──", section_style))

        story.append(Paragraph(f"BEAT {num:02d}", beat_num_style))
        story.append(Paragraph('"' + narration + '"', narration_style))

        story.append(Paragraph("IMAGE PROMPT:", image_label_style))
        story.append(Paragraph(image_prompt, image_value_style))

        table_data = [
            [Paragraph("CAMERA", label_style), Paragraph(camera, value_style)],
            [Paragraph("LIGHTING", label_style), Paragraph(lighting, value_style)],
            [Paragraph("MOOD", label_style), Paragraph(mood, value_style)],
            [Paragraph("CHARACTER ACTION", label_style), Paragraph(char_action, value_style)],
            [Paragraph("CAPCUT MOTION", label_style), Paragraph(capcut, value_style)],
        ]
        t = Table(table_data, colWidths=[3.5*cm, 13*cm])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F7F7F7')),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#DDDDDD')),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.25*cm))

    doc.build(story)
    print(f"✅ PRODUCTION.pdf saved: {path}")
    return path

build_production_pdf()
