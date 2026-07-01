#!/usr/bin/env python3
"""V14 Image Prompts PDF — 4 parts with STYLE preamble."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER

STYLE_PREAMBLE = (
    "STYLE: 2D flat cartoon illustration, thick solid black outlines, clean solid color fills, "
    "no gradients. ALEX: large beige oval head (#F5E6C8), transparent glass upper skull revealing "
    "pink cartoon Brain Villain (#E8A598), small black dot eyes, thin neutral mouth, black spiky hair, "
    "BLUE t-shirt (NOT RED — verify every time), gray pants. Brain Villain: pink cartoon brain character, "
    "heavy-lidded eyes, slight smirk, small teeth. Palette: beige skin #F5E6C8 · pink brain #E8A598 · "
    "blue shirt · gray pants · green: savings/gains · red: loss/danger · white: diagram scenes. 16:9, 1280×720."
)

BEATS_DATA = [
    # (BEAT_NUM, SECTION, NARRATION, IMAGE_PROMPT)
    (1, "HOOK — PRIMEROS 5 SEGUNDOS",
     "Why does your money always disappear before payday?",
     "BEAT 1 — OPENING [THUMBNAIL CONTINUITY]: Alex standing at a kitchen counter staring at his phone. "
     "Bank balance on screen: €0.00. Expression: wide eyes, slight jaw drop — recognition, not panic. "
     "Brain Villain lights up inside skull, smirking, arms crossed. Calendar on wall shows two days left "
     "to payday. Bold number €0.00 visible on phone screen. NOTE: Viewer who just saw the thumbnail must "
     "recognize this scene in under 5 seconds. Static image + CapCut ZOOM IN FAST delivers opening impact."),
    (2, "HOOK",
     "Not sometimes. Every month.",
     "Alex at a desk. Three identical calendar pages side by side showing three different months — each with "
     "a red X through the last two days before payday. No text labels — the red X pattern communicates "
     "the repetition without narration."),
    (3, "HOOK",
     "It doesn't matter if you earn €2,000 or €6,000.",
     "Split frame left/right: left side — simple apartment, Alex in casual clothes, phone shows €2,000 salary "
     "notification. Right side — nicer apartment, Alex in work shirt, phone shows €6,000 salary notification. "
     "Both Alex figures have identical expression: Brain Villain glowing with the same smirk. The income "
     "level is irrelevant — the Brain Villain is identical in both."),
    (4, "HOOK",
     "Four weeks. Same empty account.",
     "Alex viewed from above — sitting on floor leaning against wall. Four empty wallet icons arranged in a "
     "circle around him — one per week. All empty. No text. The empty wallets communicate the cycle."),
    (5, "HOOK",
     "Five things are doing this to you.",
     "Dark background. Five numbered slots arranged vertically (5 → 1), each empty with a '?' icon. Slots "
     "pulse faintly. Brain Villain in corner, finger counting down: 5, 4, 3..."),
    (6, "HOOK",
     "And number one runs before you even get paid.",
     "Close-up on slot #1 — still showing '?'. A calendar behind it shows WEDNESDAY. Payday arrow points to "
     "FRIDAY. The '?' pulses at WEDNESDAY — the drain starts before money arrives."),
    (7, "HOOK",
     "Not when you spend it. Before.",
     "Timeline graphic: payday arrow on the right (FRIDAY). Brain Villain activity spike on the LEFT "
     "(WEDNESDAY). The spike is earlier than the money. Clean white background — diagram style."),
    (8, "HOOK",
     "Here's the list.",
     "The five numbered slots fully illuminated. Still '?' in each — but the list is real. "
     "Brain Villain stands beside it like a game show host. Alex looks at the list: the journey begins."),
    (9, "SETUP",
     "These aren't budgeting mistakes.",
     "Torn budget spreadsheet on a desk. Alex's hand observes it, confused. Brain Villain floats above, "
     "shaking its head: 'not this'. The spreadsheet is not the problem."),
    (10, "SETUP",
     "They're not discipline failures.",
     "Alex at 5:30 AM, gym bag over shoulder, coffee in hand — clearly disciplined. Brain Villain rides on "
     "his shoulder, still running. Caption on gym clock: 5:30 AM. Discipline exists — it's not the issue."),
    (11, "SETUP",
     "They're patterns. And they run automatically.",
     "Inside Alex's glass skull — Brain Villain at a control panel with five switches, all flipped ON. "
     "Labels on switches are blank. The switches run without Alex's input."),
    (12, "SETUP",
     "Number five is the one everyone knows. And still can't stop.",
     "Slot #5 on the list illuminates — still '?'. A crowd of small figures all point at it simultaneously. "
     "Everyone knows this one. Alex in the crowd, arms crossed, nodding."),
    (13, "ITEM 5 — THE CARD GAP",
     "Number five. The Card Gap.",
     "Slot #5 reveals label: CARD GAP. Alex holds a contactless card in one hand, cash in the other. "
     "Brain Villain sits between them on a scale — cash side heavy, card side light."),
    (14, "ITEM 5",
     "When you pay with cash, your brain registers loss.",
     "Alex at a register handing over four €10 bills. Expression: mild grimace — the money feels like it's "
     "leaving. Brain Villain in skull shows a pain indicator spike."),
    (15, "ITEM 5",
     "You feel the €40 leave.",
     "Close-up on Alex's face: slight wince. The €40 amount visible on register display. "
     "Expression and number together communicate the felt loss."),
    (16, "ITEM 5",
     "When you pay with card — tap, done — the pain disappears.",
     "Same register, same €40, Alex taps card. Expression: completely neutral, almost cheerful. "
     "Brain Villain in skull: the pain indicator is FLAT — zero signal. Identical scene to beat 14, "
     "different internal state."),
    (17, "ITEM 5",
     "Same purchase. Different brain response.",
     "Split frame: left — cash transaction (pain spike in Brain Villain). Right — card tap (flat line "
     "in Brain Villain). Same €40. Same store. Different internal state only."),
    (18, "ITEM 5",
     "Card users spend 20 to 47% more than cash users.",
     "Large stat on screen: +20% to +47% in bold. Alex stands beside it. Brain Villain points at the "
     "higher number with a smug expression."),
    (19, "ITEM 5",
     "Not because they want to. Because the payment doesn't feel like payment.",
     "Alex mid-swipe on a shopping app, expression blank — no guilt, no awareness. Brain Villain "
     "inside skull sits in a hammock — fully relaxed."),
    (20, "ITEM 5",
     "Your brain is still waiting for the money to actually leave.",
     "Alex's skull interior: Brain Villain looks around confused, waiting for a signal that never comes. "
     "Outside the skull, bank balance on phone shows lower number. Internal lag vs external reality."),
    (21, "ITEM 4 — THE REWARD DRAIN",
     "Number four. The Reward Drain.",
     "Slot #4 reveals: REWARD DRAIN. Alex at desk, exhausted, suit jacket over chair. Brain Villain in "
     "skull has a calculator. Small 'I DESERVE THIS' thought bubble floats up."),
    (22, "ITEM 4",
     "It's Thursday. You've had a brutal week.",
     "Thursday circled on a desk calendar. Stack of papers, empty coffee cups, multiple browser tabs "
     "visible. Classic brutal-week visual cues. No text labels needed."),
    (23, "ITEM 4",
     "Alex has too. Deadlines. A difficult meeting. Late nights.",
     "Three-panel strip: (1) Alex at desk with deadline clock. (2) Alex in tense meeting, manager "
     "pointing. (3) Alex at desk at night, city lights behind. The week compressed."),
    (24, "ITEM 4",
     "And his brain does something automatic.",
     "Inside Alex's skull — Brain Villain at the calculator, fingers moving fast. The calculation runs "
     "without Alex's awareness. Outside the skull: Alex's eyes are closed."),
    (25, "ITEM 4",
     "It calculates what he's owed.",
     "Calculator screen shows: EFFORT → €?? OWED. Brain Villain writes on a small ledger: hours worked, "
     "difficulty, sacrifices. The debt column grows."),
]

BEATS_DATA_PART2 = [
    (26, "ITEM 4",
     "Not the salary. Something extra.",
     "Two columns side by side: SALARY (normal check icon) vs EXTRA (pulsing glow, special icon). "
     "Brain Villain points specifically at EXTRA."),
    (27, "ITEM 4",
     "'I worked hard. I deserve this.'",
     "Speech bubble from Alex's direction — but it floats inside the skull, not from Alex's mouth. "
     "It's the Brain Villain's voice. The words: I WORKED HARD. I DESERVE THIS. Bold inside the bubble."),
    (28, "ITEM 4",
     "That sentence has cost more money than any impulse purchase.",
     "Receipt tape unrolling from Alex's pocket — stretching floor to ceiling. Each item on the receipt "
     "starts with 'I deserved...' The total at the bottom is very large."),
    (29, "ITEM 3 — THE INVISIBLE DRAIN",
     "Number three. The Invisible Drain.",
     "Slot #3 reveals: INVISIBLE DRAIN. Alex's phone — the subscription apps grid. Several have dust "
     "particle effects on their icons — not opened in months. Brain Villain barely visible, almost "
     "transparent — the 'invisible' quality."),
    (30, "ITEM 3",
     "Right now, you have at least three subscriptions you've forgotten about.",
     "Grid of subscription logos (generic icons, no real brands) — three have 'last opened: 4 months ago' "
     "timestamps. Running silently."),
    (31, "ITEM 3",
     "Apps you haven't opened in four months.",
     "Calendar showing: last opened date 4 months ago. The app icon beside it — collecting digital dust. "
     "Monthly charge still processing in the background."),
    (32, "ITEM 3",
     "Services that auto-renewed in January.",
     "January calendar page. Auto-renewal notification popping up — small, easy to dismiss. Alex's thumb "
     "swipes it away without reading. Money leaves quietly."),
    (33, "ITEM 3",
     "Why haven't you cancelled them?",
     "Alex staring at the subscription list. His hand reaches for the cancel button — but stops. "
     "Brain Villain inside skull holds up a 'WAIT' sign. The pause is the trap."),
    (34, "ITEM 3",
     "Because cancelling requires a decision. And decisions cost energy.",
     "Alex's energy meter (like a phone battery) at LOW. Two arrows: SUBSCRIBE (easy) → meter barely "
     "drops. CANCEL (hard) → meter drops more. The asymmetry is the mechanism."),
    (35, "ITEM 3",
     "Your brain doesn't cancel things. It lets them run.",
     "Inside Alex's skull — Brain Villain sits in a recliner, watching the subscriptions run like a "
     "screensaver. Passive. Comfortable. Inaction is the program."),
    (36, "CTA",
     "If your brain is doing this to you right now — subscribe.",
     "Alex looks directly at camera — fourth wall break. Expression: knowing, complicit. Brain Villain "
     "peeks from behind his skull with a slightly defensive look. Subscribe button graphic appears."),
    (37, "CTA",
     "We break down a new pattern every week. It's free. And it might save you more than you think.",
     "Small visual: weekly calendar with a Neurocents logo appearing each week. Simple, non-flashy. "
     "Alex nods, returns to the list."),
    (38, "ITEM 2 — SOCIAL SPENDING",
     "Number two. Social Spending.",
     "Slot #2 reveals: SOCIAL SPENDING. Alex in a mirror — looking at himself in a new jacket. Behind him, "
     "a crowd of translucent ghost figures (the imaginary audience). They're watching. Except they're not real."),
    (39, "ITEM 2",
     "You bought something this month for an audience that wasn't watching.",
     "Ghost audience from beat 38 — shown from their perspective: they're all looking elsewhere, phones out, "
     "distracted. Not watching at all. Alex is buying for no one."),
    (40, "ITEM 2",
     "The car that looks good in the parking lot.",
     "Alex's car in an empty parking lot at night. No one around. Ghost audience members stand at the "
     "edges — translucent, barely there. The performance without an audience."),
    (41, "ITEM 2",
     "The jacket for the meeting.",
     "Alex in a boardroom in a sharp jacket. Other meeting participants are ghost figures — translucent. "
     "Alex notices his own jacket cuff adjustment — the jacket mattered more than the meeting."),
    (42, "ITEM 2",
     "The upgrade nobody asked for but someone might notice.",
     "Alex's desk: new monitor setup, latest accessories. Post-it note on monitor: 'Nobody asked for this.' "
     "Ghost audience in background — not noticing."),
    (43, "ITEM 2",
     "Who is that person you're buying for?",
     "Alex faces camera directly, expression genuinely questioning. Around him, ghost audience figures "
     "slowly dissolve. The question lands in the empty space they leave."),
    (44, "ITEM 2",
     "They don't exist. They're a projection.",
     "The ghost audience is now completely transparent. Alex's Brain Villain projects them like a film "
     "projector from inside the skull. The audience is his own output."),
    (45, "ITEM 2",
     "The most expensive audience in your life has never spent a single dollar.",
     "Financial ledger: left column — GHOST AUDIENCE COSTS (long list, €€€). Right column — GHOST AUDIENCE "
     "CONTRIBUTIONS: empty. The asymmetry is total."),
    (46, "ITEM 2",
     "They live entirely in your head. And they have expensive taste.",
     "Alex's skull cross-section: inside, the ghost audience sits in tiny theater seats — watching a tiny "
     "Alex perform for them. Inside his own head. The recursion is the trap."),
    (47, "ITEM 1 — THE PRE-SPEND",
     "Number one. The one nobody names.",
     "Slot #1 glows brightest — still '?'. Other four slots visible but dimmed. Brain Villain stands "
     "beside slot #1 with arms crossed — guarding it."),
    (48, "ITEM 1",
     "The Pre-Spend.",
     "Slot #1 reveals: THE PRE-SPEND. Brain Villain steps aside reluctantly. The name appears in bold."),
    (49, "ITEM 1",
     "It's Wednesday. Payday is Friday.",
     "Alex at a desk. Wednesday date visible on calendar. Payday circled on Friday — two days away. "
     "Alex's phone shows current balance: not zero, but declining."),
    (50, "ITEM 1",
     "Alex hasn't received anything yet.",
     "Bank notification on Alex's phone: NEXT DEPOSIT: FRIDAY. Current balance visible. "
     "Timestamp: WEDNESDAY, 2:00 PM."),
]

BEATS_DATA_PART3 = [
    (51, "ITEM 1",
     "But his brain has already spent it.",
     "Inside Alex's skull: Brain Villain at an accounting desk — rapidly typing on calculator, moving "
     "money allocation arrows. The salary hasn't arrived but the Villain is already processing it."),
    (52, "ITEM 1",
     "Not metaphorically. Neurologically.",
     "Split label: left — METAPHOR (crossed out). Right — NEUROLOGY (highlighted). Brain scan silhouette "
     "showing activity in decision-making region."),
    (53, "ITEM 1",
     "The moment you know money is coming — your brain allocates it.",
     "Timeline: WEDNESDAY knowledge → immediate allocation arrows fire in brain. FRIDAY payday comes "
     "AFTER the allocation is complete. The brain processes future money as if already arrived."),
    (54, "ITEM 1",
     "The rent. The pending bill. The thing you've been delaying.",
     "Three allocation boxes filling up in Alex's mental budget: RENT ✓, BILL ✓, DELAYED THING ✓. "
     "Each checked off by Brain Villain — but the money isn't there yet."),
    (55, "ITEM 1",
     "And then — quietly — a few things that feel deserved.",
     "The allocation boxes continue: after RENT, BILL, DELAYED THING — a fourth box appears, smaller, "
     "slightly dimmer: 'DESERVED EXTRA'. Brain Villain adds it quietly, almost sheepishly."),
    (56, "ITEM 1",
     "By the time Friday arrives, the money is already gone in your mind.",
     "Friday arrives on calendar — payday notification appears. But Alex's mental budget is already at "
     "zero. The money arrives into an already-empty mental account."),
    (57, "ITEM 1",
     "Friday is just the confirmation.",
     "Split: left — WEDNESDAY (mental spend complete, arrows all allocated). Right — FRIDAY (money "
     "arrives, immediately absorbed). Arrow from right to left shows mental spend preceded physical arrival."),
    (58, "ITEM 1",
     "You don't spend your salary. You process a transaction your brain closed on Wednesday.",
     "Alex at ATM or bank app — Friday. The transaction processes. Brain Villain holds up a 'RECEIPT' "
     "dated WEDNESDAY. The deal was done two days ago."),
    (59, "MECHANISM CONCLUSION",
     "Five patterns. Running automatically.",
     "All five slots now fully labeled and lit: CARD GAP · REWARD DRAIN · INVISIBLE DRAIN · "
     "SOCIAL SPENDING · PRE-SPEND. Five program indicators — all ON."),
    (60, "MECHANISM CONCLUSION",
     "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
     "Each slot highlighted in sequence as the names are spoken. The names land one by one. "
     "Alex's finger points to each in sequence."),
    (61, "MECHANISM CONCLUSION",
     "None of them feel like mistakes when they happen.",
     "Alex mid-Card Gap tap, mid-Reward purchase, mid-subscription-ignore — three micro-scenes in one "
     "frame. Expression in each: completely normal, reasonable, justified."),
    (62, "MECHANISM CONCLUSION",
     "The Card Gap feels convenient.",
     "Single slot: CARD GAP. Adjective appears: CONVENIENT. Alex taps card — expression is pleased."),
    (63, "MECHANISM CONCLUSION",
     "The Reward Drain feels earned. The Social Spend feels reasonable. The Pre-Spend feels like planning.",
     "Three slots in rapid sequence: REWARD DRAIN + EARNED · SOCIAL SPENDING + REASONABLE · "
     "PRE-SPEND + PLANNING. Each pairing makes ironic sense."),
    (64, "THE STRUCTURAL FIX",
     "The fix isn't 'spend less.'",
     "The words SPEND LESS crossed out with a bold red X. Alex beside it, nodding. "
     "He already knew this wasn't the answer."),
    (65, "THE STRUCTURAL FIX",
     "That's not a system. That's a wish.",
     "Split: SYSTEM (gears interlocking) vs WISH (a single star). SPEND LESS goes in the WISH column. "
     "Nothing in the SYSTEM column yet."),
    (66, "THE STRUCTURAL FIX",
     "For the Card Gap: switch one category to cash. Groceries. Restaurants. One category.",
     "Alex at grocery store with physical cash. Expression: slightly more deliberate — the friction is "
     "intentional now. Brain Villain feels the signal it was missing."),
    (67, "THE STRUCTURAL FIX",
     "You don't need to feel the money leaving everywhere. Just somewhere.",
     "EVERYWHERE (credit card icons filling the frame — overwhelming) vs SOMEWHERE (one cash transaction "
     "— specific, intentional). The targeted friction beats total friction."),
    (68, "THE STRUCTURAL FIX",
     "For the Reward Drain: budget it. €80 a month. 'This is my earned money.'",
     "Alex's monthly budget on screen. New category: EARNED EXTRA — €80. The category has its own "
     "dedicated slot. The Villain has a container now."),
    (69, "THE STRUCTURAL FIX",
     "When it's gone, it's gone. The Villain needs a container, not a lecture.",
     "The €80 budget depleted — the slot shows EMPTY. Brain Villain shrugs, satisfied. "
     "The container was enough."),
    (70, "THE STRUCTURAL FIX",
     "For the Invisible Drain: one audit. Once a year. Not monthly — once.",
     "Calendar with ONE annual date circled: SUBSCRIPTION AUDIT. All other months empty. The simplicity "
     "is the solution."),
    (71, "THE STRUCTURAL FIX",
     "For Social Spending: one question before every non-essential purchase.",
     "Alex mid-purchase — hand reaching for a product. Thought bubble appears: WHO AM I BUYING THIS FOR? "
     "The question pauses the action."),
    (72, "THE STRUCTURAL FIX",
     "'Who am I buying this for?' If the answer isn't you — pause.",
     "Alex's thought bubble shows: ME (clear, solid figure) vs GHOST AUDIENCE (transparent, dissolving). "
     "The answer determines the purchase."),
    (73, "THE STRUCTURAL FIX",
     "For the Pre-Spend: the salary hits the account. You don't touch it for 24 hours.",
     "Friday: salary notification appears. Alex's phone flips face-down. Timer starts: 24 HOURS. "
     "The deliberate pause between arrival and allocation."),
    (74, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain has one response to this list.",
     "Brain Villain in the skull, arms crossed, looking at the five solutions. One finger raised — "
     "it has a counter."),
    (75, "BRAIN VILLAIN'S LAST TRICK",
     "You're feeling it right now.",
     "Alex looks directly at camera — fourth wall break. Expression: knowing. Brain Villain mirrors "
     "the viewer's position."),
]

BEATS_DATA_PART4 = [
    (76, "BRAIN VILLAIN'S LAST TRICK",
     "Not resistance. Something quieter.",
     "Brain Villain sitting quietly, looking reasonable, wearing a WISDOM costume. The resistance "
     "is dressed as common sense."),
    (77, "BRAIN VILLAIN'S LAST TRICK",
     "Something that sounds like common sense: 'I already know this.'",
     "Speech bubble: 'I ALREADY KNOW THIS.' The bubble looks calm, reasonable, like genuine insight. "
     "Brain Villain nods sagely at it — very pleased with itself."),
    (78, "BRAIN VILLAIN'S LAST TRICK",
     "That thought is not wisdom. Not self-awareness.",
     "The 'I ALREADY KNOW THIS' bubble gets a red border — reclassified. It moves from the WISDOM "
     "column to INVISIBLE DRAIN, WEARING INSIGHT COSTUME."),
    (79, "BRAIN VILLAIN'S LAST TRICK",
     "It is the Invisible Drain wearing the costume of insight.",
     "Visual: the INVISIBLE DRAIN slot from the list — but wearing the WISDOM costume. Same pattern, "
     "different disguise. Brain Villain points at it with satisfaction."),
    (80, "BRAIN VILLAIN'S LAST TRICK",
     "The programs are not broken.",
     "Brain Villain's control panel — all five switches still ON. Banner across the panel: NOT BROKEN. "
     "The programs are doing exactly what they were designed to do."),
    (81, "BRAIN VILLAIN'S LAST TRICK",
     "They were built for a world where money was physical — coins you could feel, resources you could see leaving.",
     "Historical scene: Alex's ancestor holding physical coins, trading at a market. The money transfer "
     "is visible, tactile, real. Warm earth tones."),
    (82, "BRAIN VILLAIN'S LAST TRICK",
     "In that world, the Pre-Spend was planning. The Reward Drain was recovery. The Card Gap didn't exist.",
     "Three-part panel: PRE-SPEND = PLANNING AHEAD. REWARD DRAIN = RECOVERY. CARD GAP = ? (empty — "
     "didn't exist in that world). Warm historical light throughout."),
    (83, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain was built for that world. Not this one.",
     "Split: THAT WORLD (physical coins, Brain Villain fits perfectly) vs THIS WORLD (direct deposits, "
     "one-click payments — Brain Villain misaligned). Same program. Different world. Mismatch."),
    (84, "BRAIN VILLAIN'S LAST TRICK",
     "These five systems were designed for the world you actually live in.",
     "The five solutions — CASH CATEGORY, EARNED CONTAINER, ANNUAL AUDIT, THE QUESTION, 24-HOUR GAP — "
     "displayed against the modern world background. They fit. The programs don't. The systems do."),
    (85, "IDENTITY CLOSE",
     "Your money doesn't disappear.",
     "Alex looking at his empty bank account — but expression is different now. Not defeated. Analytical. "
     "The situation is the same. The frame has changed."),
    (86, "IDENTITY CLOSE",
     "It follows five very predictable routes.",
     "The five labeled slots shown as ROUTES: arrows leading from Alex's account to each destination. "
     "Predictable. Mappable. Not mysterious."),
    (87, "IDENTITY CLOSE",
     "Card Gap. Reward Drain. Invisible Drain. Social Spending. Pre-Spend.",
     "The five names in clean typography — simple, direct. No slots, no icons. Just the names, "
     "permanent and named. Alex reads the list once."),
    (88, "IDENTITY CLOSE",
     "Name them. And they lose power.",
     "Each name gets a dimmer switch — as Alex 'names' it, the switch turns down. The programs don't "
     "disappear but their automatic intensity reduces."),
    (89, "IDENTITY CLOSE",
     "You're not bad with money.",
     "Alex looks at camera — direct, warm. Not a pep talk. A correction. Brain Villain nods in "
     "agreement — for once on the same team."),
    (90, "IDENTITY CLOSE",
     "You're running programs that were never designed for a world with direct deposits and one-click payments.",
     "Alex and Brain Villain side by side — not adversaries. Partners navigating a mismatch. Modern phone "
     "in Alex's hand. Brain Villain examining it with curiosity — learning."),
    (91, "IDENTITY CLOSE",
     "Now you know which five. That's the first thing the Villain didn't want you to have.",
     "The five named routes on Alex's map — now in his hands. He holds the map. Brain Villain looks "
     "at the map, then at Alex — slightly caught. The knowledge is the advantage."),
    (92, "NEXT VIDEO TEASE",
     "Next week — the one decision that stops all five.",
     "A single action slot labeled: ONE DECISION. Arrows from it connect to all five drain slots — "
     "cutting all five routes simultaneously."),
    (93, "NEXT VIDEO TEASE",
     "Not five solutions. One.",
     "The word ONE large on screen. The five solutions from earlier fade out — replaced by a single "
     "elegant mechanism."),
    (94, "NEXT VIDEO TEASE",
     "Made once. Before the patterns activate.",
     "Timeline: DECISION made early (Monday or start of month). Five pattern triggers later in the "
     "timeline — but the DECISION is already upstream."),
    (95, "NEXT VIDEO TEASE",
     "See you Thursday.",
     "Alex in his default pose — relaxed, confident. Brain Villain visible in skull, also calm. "
     "Thursday calendar date visible in background. The adversarial energy is gone."),
]

def build_image_prompts_pdf():
    path = "/home/user/Claudeeee/V14_final_IMAGE_PROMPTS.pdf"
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm
    )

    title_style = ParagraphStyle('title', fontSize=13, leading=18,
                                  spaceBefore=0, spaceAfter=6,
                                  textColor=colors.HexColor('#B02A2A'),
                                  fontName='Helvetica-Bold', alignment=TA_CENTER)
    subtitle_style = ParagraphStyle('subtitle', fontSize=9, leading=13,
                                     spaceAfter=8, fontName='Helvetica',
                                     alignment=TA_CENTER,
                                     textColor=colors.HexColor('#2C3E50'))
    preamble_style = ParagraphStyle('preamble', fontSize=8, leading=13,
                                     spaceBefore=6, spaceAfter=10,
                                     fontName='Helvetica-Oblique',
                                     textColor=colors.HexColor('#555555'),
                                     borderPad=6,
                                     backColor=colors.HexColor('#F9F4F4'),
                                     borderColor=colors.HexColor('#B02A2A'),
                                     borderWidth=0.5)
    section_style = ParagraphStyle('section', fontSize=9, leading=13,
                                    spaceBefore=10, spaceAfter=3,
                                    textColor=colors.HexColor('#B02A2A'),
                                    fontName='Helvetica-Bold')
    beat_num_style = ParagraphStyle('beatnum', fontSize=8, leading=12,
                                     fontName='Helvetica-Bold',
                                     textColor=colors.HexColor('#777777'))
    narration_style = ParagraphStyle('narration', fontSize=9, leading=13,
                                      spaceAfter=3, fontName='Helvetica-Oblique',
                                      textColor=colors.HexColor('#2C3E50'))
    prompt_style = ParagraphStyle('prompt', fontSize=10, leading=15,
                                   spaceAfter=10, fontName='Helvetica',
                                   leftIndent=10)

    def build_part(story, part_num, beats, is_first=False):
        if is_first:
            story.append(Paragraph("NEUROCENTS — VIDEO 14", title_style))
            story.append(Paragraph("5 Things That Drain Your Money Before Payday (No Matter What You Earn)", subtitle_style))
        story.append(Paragraph(f"IMAGE PROMPTS — PART {part_num} OF 4", title_style))
        story.append(Paragraph(STYLE_PREAMBLE, preamble_style))
        story.append(Spacer(1, 0.3*cm))

        current_section = ""
        for beat_num, section, narration, image_prompt in beats:
            if section != current_section:
                current_section = section
                story.append(Paragraph(f"── {section} ──", section_style))
            story.append(Paragraph(f"BEAT {beat_num:02d}", beat_num_style))
            story.append(Paragraph('"' + narration + '"', narration_style))
            story.append(Paragraph(image_prompt, prompt_style))

    story = []
    build_part(story, 1, BEATS_DATA, is_first=True)
    story.append(PageBreak())
    build_part(story, 2, BEATS_DATA_PART2)
    story.append(PageBreak())
    build_part(story, 3, BEATS_DATA_PART3)
    story.append(PageBreak())
    build_part(story, 4, BEATS_DATA_PART4)

    doc.build(story)
    print(f"✅ IMAGE_PROMPTS.pdf saved: {path}")
    return path

build_image_prompts_pdf()
