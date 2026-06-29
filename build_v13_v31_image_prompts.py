#!/usr/bin/env python3
"""
VIDEO 13 — IMAGE PROMPTS · BRIEF v3.1
93 beats · BLUE t-shirt · S17 thumbnail continuity · Visual-first rule
Beat 1 format: S17 OPENING THUMBNAIL CONTINUITY
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

STYLE_PREAMBLE = (
    "2D flat cartoon illustration, thick solid black outlines on every element, "
    "clean solid color fills, no gradients except soft warm ambient light. "
    "Recurring main character ALEX: large beige oval head with transparent glass upper skull "
    "revealing a pink cartoon Brain Villain inside, small black dot eyes, thin neutral mouth, "
    "black spiky hair, BLUE t-shirt (NOT RED — verify every time), gray pants. "
    "Brain Villain: pink cartoon brain character, heavy-lidded eyes, slight smirk, small teeth — "
    "ALWAYS inside Alex's skull, never floating outside. "
    "Palette: beige skin #F5E6C8 · pink brain #E8A598 · blue t-shirt · gray pants · "
    "green: savings/gains · red: loss/danger/circuits · white: diagram scenes · "
    "dark charcoal #1A1A1A: hook/drama scenes. "
    "16:9, 1280×720."
)

BEATS = [

    # ═══════════════════════════════════════════════════════
    # HOOK — 10 beats — S2 Dato Sin Contexto + S17 Continuity
    # ═══════════════════════════════════════════════════════

    (1, "Five.",
     "BEAT 1 — OPENING [S17 THUMBNAIL CONTINUITY · S2 NUMBER DROP]: "
     "DARK CHARCOAL background (#1A1A1A). Large bold white numeral '5' dominates center frame. "
     "ALEX stands below it, head tilted back, eyes wide open in shock — the number has just appeared "
     "inside his transparent skull as five distinct red neural circuit paths firing simultaneously, "
     "each glowing electric red, numbered 1 through 5 along their paths. "
     "Brain Villain: ACTIVE — arms raised triumphantly inside skull, all five circuits igniting at once, "
     "broad smug grin, heavy-lidded eyes now wide and satisfied. "
     "Alex expression: genuine shock — both hands raised instinctively to sides of head. "
     "Camera: LOW ANGLE looking up at Alex, the '5' and skull circuits filling the upper frame. "
     "Motion: FAST ZOOM OUT from the '5' inside the skull to reveal Alex's full shocked expression. "
     "NOTE: Viewer who just saw thumbnail ('5 WAYS / YOUR BRAIN / REWIRES ITSELF') must recognize "
     "this scene in under 5 seconds. The 5 red circuits match the thumbnail exactly. "
     "NO static pose. NO introduction. The number IS the opening."),

    (2, "That is how many programs your brain is running right now that are keeping you exactly where you are.",
     "DARK CHARCOAL background. Camera pulls back further from Beat 1. "
     "Alex now visible from mid-torso up, expression shifting from shock to grim recognition. "
     "The '5' remains visible above him but slightly smaller — context arriving. "
     "Brain Villain inside skull: arms crossed, satisfied, five circuits still glowing behind it. "
     "Camera: MEDIUM SHOT, slightly tilted. Motion: SLOW PULL BACK. "
     "No text labels — the five glowing circuits carry the '5 programs' message visually."),

    (3, "Not bad decisions. Not poor discipline.",
     "DARK CHARCOAL background. Alex close-up. He shakes his head slowly. "
     "Two thought bubbles appear and dissolve: a crossed-out X over 'bad decisions' icon, "
     "a crossed-out X over 'weak willpower' icon. Brain Villain inside skull shakes its head "
     "in sync — no, not those. "
     "Camera: MEDIUM CLOSE-UP, straight on. Motion: SLIGHT PUSH IN as X's appear."),

    (4, "Actual neural circuits — built through repetition — firing without your knowledge.",
     "DARK CHARCOAL background. Alex's transparent skull fills most of frame. "
     "Inside: the five red circuit paths now shown as literal wired pathways, each one "
     "labeled with a number 1-5 (small, subtle). Brain Villain sitting at a control panel "
     "with five switches, all flipped ON — smug, in control. "
     "Camera: EXTREME CLOSE-UP on skull interior. Motion: SLOW ZOOM INTO skull."),

    (5, "The third one gets worse the more you learn about money.",
     "DARK CHARCOAL background. Alex's skull — circuit path 3 pulses brighter than the others. "
     "A stack of books appears beside Alex, labeled 'FINANCIAL EDUCATION'. "
     "As the book stack grows taller, circuit 3 glows more intensely — inverse relationship. "
     "Brain Villain points at circuit 3 with a knowing smirk. "
     "Camera: MEDIUM SHOT, Alex left, book stack right. Motion: BOOK STACK GROWS frame by frame."),

    (6, "The fifth one is the only financial bias that compounds biologically — not just financially.",
     "DARK CHARCOAL background. Circuit 5 pulses. A DNA helix appears inside the skull beside "
     "the Brain Villain — biological, not just financial. A small coin/dollar icon beside it, smaller. "
     "The biological symbol is larger — biology > money. "
     "Camera: LOW ANGLE, dramatic. Motion: DNA HELIX ROTATES slowly."),

    (7, "One of them fired this morning. Before you opened this video.",
     "DARK CHARCOAL background. Alex's skull — one of the circuits (circuit 1) flashes urgently. "
     "A clock shows 8:47 AM in the corner. Brain Villain inside skull checks a tiny watch — "
     "'already ran it.' Alex expression: unsettled realization. "
     "Camera: TIGHT on skull with clock visible. Motion: CLOCK TICK animation."),

    (8, "We are going to show you all five — in the exact order they fire.",
     "DARK CHARCOAL background fades to white. Five numbered slots appear on screen: "
     "1 · 2 · 3 · 4 · 5 — clean, bold, left to right. Alex stands to the side pointing at slot 1. "
     "Brain Villain inside skull: alert, watching. "
     "Camera: WIDE SHOT, Alex left, five slots right. Motion: SLOTS APPEAR ONE BY ONE."),

    (9, "Your Brain Villain is already running Program One.",
     "DARK CHARCOAL. Brain Villain CLOSE-UP inside Alex's skull — center frame. "
     "It activates a holographic label: 'PROGRAM 1 — RUNNING'. Status light: green/active. "
     "Alex's expression from outside skull: resigned, beginning to understand. "
     "Camera: EXTREME CLOSE-UP on Brain Villain. Motion: LABEL ACTIVATES with a click."),

    (10, "This is what it looks like.",
     "TRANSITION BEAT. Dark background begins to lighten toward warm beige interior. "
     "Alex turns his head — he is entering the scene of Trap 1. The skull interior "
     "shows circuit 1 glowing alone, others dimmed. "
     "Camera: DUTCH ANGLE, suggestive of narrative shift. Motion: SLOW PAN toward new scene."),

    # ═══════════════════════════════════════════════════════
    # TRAP 1 — THE ANTICIPATION BURN — 12 beats
    # ═══════════════════════════════════════════════════════

    (11, "Wednesday. Alex has not been paid.",
     "Warm beige interior. Alex at desk. A wall calendar — Wednesday circled. "
     "His paycheck icon is greyed out, labeled 'FRIDAY'. Alex's expression: neutral waiting. "
     "Brain Villain inside skull: awake, leaning forward with interest. "
     "Camera: MEDIUM WIDE SHOT. Motion: CALENDAR DAY highlight pulses."),

    (12, "He already knows exactly what he will buy when Friday comes.",
     "Same warm interior. Alex's thought bubble: a specific item (headphones/sneakers icon) "
     "with a price tag. The thought bubble is detailed, specific, fully formed. "
     "He hasn't been paid. The item is already decided. "
     "Camera: MEDIUM CLOSE-UP on Alex's face + thought bubble. Motion: THOUGHT BUBBLE MATERIALIZES."),

    (13, "He has been thinking about it since Monday.",
     "Three-panel timeline: MONDAY · TUESDAY · WEDNESDAY — each showing Alex with the same "
     "thought bubble. The bubble grows slightly larger each day. "
     "Brain Villain inside skull: dopamine meter rising each panel. "
     "Camera: WIDE SHOT showing all three panels. Motion: TIMELINE BUILDS left to right."),

    (14, "This is not excitement. This is a dopamine schedule.",
     "Clinical white background. A graph: X-axis = days Mon-Fri, Y-axis = DOPAMINE. "
     "The peak is on WEDNESDAY — not Friday. Friday shows a declining slope. "
     "Alex points at the Wednesday peak, confused. Brain Villain marks the chart. "
     "Camera: MEDIUM SHOT, Alex + chart. Motion: GRAPH LINE DRAWS itself left to right."),

    (15, "Wolfram Schultz — Cambridge — won part of the Nobel Prize for discovering this mechanism.",
     "Academic white scene. A researcher figure at a Cambridge University building. "
     "Label: 'WOLFRAM SCHULTZ · CAMBRIDGE · NOBEL PRIZE'. A simplified neuron diagram shows "
     "dopamine firing pattern. No cartoon brain villain — academic, clean. "
     "Camera: MEDIUM SHOT. Motion: LABEL FADES IN."),

    (16, "Dopamine does not fire when the reward arrives.",
     "Split screen. LEFT: reward arrives (payday check) — dopamine flatline. "
     "RIGHT: dopamine spike → empty (anticipation only). "
     "Bold red label on left: 'NOT HERE'. Bold green label on right: 'HERE'. "
     "Camera: WIDE SPLIT SHOT. Motion: BOTH SIDES REVEAL simultaneously."),

    (17, "It fires when the brain predicts the reward is coming.",
     "Alex's skull close-up. Brain Villain inside fires a dopamine spark toward a "
     "prediction arrow pointing to Friday. The arrow is a forecast, not a memory. "
     "Label inside skull: 'PREDICTION = FIRE'. "
     "Camera: CLOSE-UP skull interior. Motion: SPARK travels along prediction arrow."),

    (18, "By Wednesday the dopamine peak has already passed.",
     "The dopamine graph from Beat 14 reappears. A 'YOU ARE HERE' marker sits on the "
     "downslope — past the Wednesday peak. Alex looks at the graph: the best feeling "
     "already came and went. Expression: mild deflation. "
     "Camera: MEDIUM SHOT. Motion: MARKER slides down the slope."),

    (19, "By Friday — payday — the dopamine signal is declining. The brain has moved to the next prediction.",
     "Friday. Alex receives paycheck. His dopamine graph is already at a lower level. "
     "But inside his skull: Brain Villain has opened a NEW thought bubble — next item. "
     "The cycle restarts before the current one ends. "
     "Camera: WIDE SHOT showing paycheck + skull with new bubble. Motion: NEW BUBBLE OPENS."),

    (20, "Alex spends on Friday not because he wants to. Because the wanting already happened without him.",
     "Alex at checkout (phone payment). Expression: going through the motions. "
     "Ghost image of Alex from Wednesday: same item, full excitement dopamine spike — that "
     "was the real moment. Friday Alex is just executing a decision already made. "
     "Camera: MEDIUM SHOT. Motion: GHOST IMAGE fades in beside Friday Alex."),

    (21, "His Friday spending is not a decision. It is a receipt for a transaction his brain closed on Tuesday.",
     "A receipt prints. At the top: 'TRANSACTION DATE: TUESDAY'. At the bottom: "
     "'EXECUTION DATE: FRIDAY'. Alex holds the receipt. Brain Villain stamps it: 'CLOSED'. "
     "Camera: CLOSE-UP on receipt. Motion: RECEIPT PRINTS from top to bottom."),

    (22, "Trap One fires first. Trap Two makes the damage invisible.",
     "Circuit 1 (ANTICIPATION BURN) glows solid in Alex's skull. Circuit 2 begins to pulse. "
     "A wall appears between Alex and his bank balance — not there yet, coming. "
     "Brain Villain switches on circuit 2. "
     "Camera: MEDIUM SHOT. Motion: CIRCUIT 2 ACTIVATES with a soft click."),

    # ═══════════════════════════════════════════════════════
    # TRAP 2 — THE BALANCE BLINDSPOT — 11 beats
    # ═══════════════════════════════════════════════════════

    (23, "Saturday morning. Alex does not check his balance.",
     "Warm beige kitchen. Morning light. Alex has phone in hand, bank app visible. "
     "He closes the app deliberately. Calendar: SATURDAY. Expression: deliberate avoidance. "
     "Brain Villain inside skull: hands over Alex's eyes from behind — gently, protectively. "
     "Camera: MEDIUM SHOT. Motion: APP CLOSES with a swipe away."),

    (24, "He tells himself he will check next week — when things are calmer.",
     "Alex's thought bubble: a future calendar — 'NEXT WEEK' in soft, calming blue. "
     "Beside it: a storm cloud labeled 'NOW' (financial anxiety). He's choosing the blue calendar. "
     "Brain Villain inside skull: nodding agreeably — 'yes, next week is better.' "
     "Camera: CLOSE-UP on thought bubbles. Motion: NEXT WEEK bubble glows warmly."),

    (25, "Over thirty days: six balance checks. All six came after a paycheck. Zero came after a large purchase.",
     "Calendar grid — 30 days. Six days marked green (paycheck days): balance checked. "
     "Three days marked red (big purchases): no check. Zero red days have a checkmark. "
     "Alex's finger traces the pattern. "
     "Camera: WIDE SHOT of calendar grid. Motion: CHECKMARKS APPEAR on green days only."),

    (26, "Dan Galai and Orly Sade — Hebrew University, 2006 — called this the ostrich effect.",
     "Academic white scene. An ostrich icon burying its head in sand. Label: "
     "'THE OSTRICH EFFECT · GALAI & SADE · HEBREW UNIVERSITY · 2006'. "
     "Clean diagram, no cartoon characters. "
     "Camera: MEDIUM SHOT. Motion: LABEL FADES IN below ostrich icon."),

    (27, "When financial information is likely to be painful, the brain stops seeking it.",
     "Alex's skull interior. A bank statement floats toward Brain Villain. "
     "Brain Villain puts up a hand: STOP. The statement bounces back. "
     "No text label on the statement — just a red minus sign visible. "
     "Camera: CLOSE-UP skull interior. Motion: STATEMENT BOUNCES BACK."),

    (28, "Not a choice. A conditioned reflex — built specifically to reduce cortisol.",
     "A cortisol graph: spikes when Alex looks at a bad number, drops when he doesn't. "
     "The avoidance is the brain's solution to the cortisol spike. "
     "Brain Villain holds a 'CORTISOL -' sign triumphantly. "
     "Camera: MEDIUM SHOT Alex + graph. Motion: GRAPH LINES animate."),

    (29, "Every time Alex looked at a bad number, his brain recorded pain.",
     "A simple memory trace inside Alex's skull. A red number → a pain signal → a recording. "
     "Three instances stacked: the same sequence each time. Brain Villain runs the recording. "
     "Camera: CLOSE-UP skull interior, memory trace visible. Motion: RECORDING plays."),

    (30, "After enough repetitions, avoidance became automatic.",
     "Alex's hand now moving away from phone WITHOUT looking — reflex, not decision. "
     "A dotted line shows the automatic pathway: see phone → move away. No thought bubble. "
     "Brain Villain inside skull: arms folded, job done, no effort needed. "
     "Camera: WIDE SHOT showing automatic motion. Motion: DOTTED PATH animates."),

    (31, "The Brain Villain does not need to hide the numbers. Alex does it for him.",
     "Side by side: LEFT — Brain Villain with 'hide numbers' toolkit, untouched. "
     "RIGHT — Alex with his own hand covering his eyes. "
     "Label: 'UNNECESSARY' crossed out over Brain Villain's toolkit. "
     "Camera: SPLIT SHOT. Motion: TOOLKIT GREYED OUT."),

    (32, "Trap One generated the spend. Trap Two buried the evidence.",
     "Alex's skull — circuits 1 and 2 both glowing. Circuit 1 labeled 'SPEND'. "
     "Circuit 2 labeled 'BURY'. Circuit 3 begins to pulse. "
     "Brain Villain toggling between circuits with satisfaction. "
     "Camera: SKULL INTERIOR wide shot. Motion: CIRCUIT 3 BEGINS TO GLOW."),

    (33, "Trap Three provides the explanation.",
     "Alex at desk, phone in hand, looking confident. A book labeled 'BEHAVIORAL FINANCE' "
     "sits open beside him. He feels equipped. Brain Villain inside skull: "
     "circuit 3 now fully active — THE EXPERTISE TRAP is on. "
     "Camera: MEDIUM SHOT. Motion: CIRCUIT 3 FULLY LIGHTS UP."),

    # ═══════════════════════════════════════════════════════
    # CTA — beats 34-35
    # ═══════════════════════════════════════════════════════

    (34, "If your brain is doing this to you right now — subscribe.",
     "Alex turns to face camera directly. Expression: calm, knowing, peer-to-peer. "
     "Brain Villain visible in skull: small, named, labeled '5 PROGRAMS'. "
     "A subscription bell icon appears beside Alex, simple, not oversized. "
     "Camera: MEDIUM SHOT, Alex center, direct eye contact with viewer. "
     "Motion: BELL ICON pulses once."),

    (35, "We break down a new bias every week. It's free. And it might save you more than you think.",
     "Same direct shot. Alex's expression: confident understatement. "
     "Small text below: 'NEW BIAS · EVERY WEEK'. Clean white background. "
     "Brain Villain inside skull: holds up a sign '+ MORE COMING'. "
     "Camera: SAME MEDIUM SHOT. Motion: TEXT FADES IN below Alex."),

    # ═══════════════════════════════════════════════════════
    # TRAP 3 — THE EXPERTISE TRAP — 12 beats
    # ═══════════════════════════════════════════════════════

    (36, "Alex has been studying behavioral finance for eight months.",
     "Warm interior. Alex at desk surrounded by books, notebooks, highlighted articles. "
     "A wall calendar shows 8 months marked. Expression: engaged, studious, invested. "
     "Brain Villain inside skull: watching with interest — circuit 3 active. "
     "Camera: WIDE SHOT of full study scene. Motion: BOOKS STACK builds."),

    (37, "He knows the vocabulary. Anchoring. Loss aversion. Mental accounting. He can name his biases in real time.",
     "Alex's thought cloud: floating labels — 'ANCHORING' · 'LOSS AVERSION' · 'MENTAL ACCOUNTING'. "
     "All correctly labeled. He has the words. "
     "Brain Villain inside skull: nodding — yes, he knows the words. "
     "Camera: MEDIUM SHOT, thought cloud prominent. Motion: LABELS FLOAT IN one by one."),

    (38, "He feels more in control than ever.",
     "Alex's posture: upright, arms crossed, slight satisfied smile. A confidence meter "
     "beside him reads HIGH. Brain Villain inside skull: arms crossed too — mirroring. "
     "Camera: MEDIUM SHOT. Motion: CONFIDENCE METER rises."),

    (39, "His financial decisions have not improved.",
     "Alex's bank graph: flat line, unchanged. The vocabulary labels float above the flat line. "
     "Words: many. Results: same. "
     "Bold red label over the graph: 'UNCHANGED'. Alex expression: slight confusion. "
     "Camera: WIDE SHOT. Motion: FLAT LINE stays flat while labels stack above."),

    (40, "Terrance Odean — UC Berkeley — studied 35,000 investor accounts for seven years.",
     "Academic white scene. A researcher figure. Label: 'TERRANCE ODEAN · UC BERKELEY · 7 YEARS'. "
     "35,000 small investor icons arranged in a grid. Clean data visualization. "
     "Camera: WIDE SHOT of grid. Motion: ICONS FILL IN progressively."),

    (41, "The investors who traded most frequently earned the lowest returns.",
     "Two columns: LEFT — HIGH FREQUENCY traders (many arrows, many trades) → red return bar at bottom. "
     "RIGHT — LOW FREQUENCY traders (few arrows) → green return bar at top. "
     "The relationship is inverse. "
     "Camera: SPLIT COLUMNS SHOT. Motion: BARS ANIMATE from base."),

    (42, "Not because trading is wrong. Because confidence had outpaced competence.",
     "A scale: CONFIDENCE side heavy (over-weighted, tilted down). "
     "COMPETENCE side lighter (lagging). The gap between them: shaded red. "
     "Brain Villain stands on the CONFIDENCE side making it heavier. "
     "Camera: MEDIUM SHOT on scale. Motion: SCALE TIPS as confidence grows."),

    (43, "Daniel Kahneman documented the same pattern: eighty percent of investors believe they are above average.",
     "A pie chart: 80% slice labeled 'BELIEVE ABOVE AVERAGE' (blue). "
     "20% slice (grey). "
     "Label: 'DANIEL KAHNEMAN'. Alex in the 80% slice, unaware. "
     "Camera: WIDE SHOT with pie chart prominent. Motion: PIE SLICES FILL."),

    (44, "Fifty percent are, by definition, wrong.",
     "Same pie chart. 50% of the 80% slice turns red: 'MATHEMATICALLY WRONG'. "
     "Alex might be in the red zone. He does not know which. "
     "Camera: CLOSE-UP on pie chart. Motion: RED ZONE REVEALS."),

    (45, "The Expertise Trap does not require ignorance. It requires the illusion of knowledge.",
     "Alex's skull interior. Two versions: LEFT — ignorance (dark, empty). "
     "RIGHT — illusion of knowledge (bright, filled with labels). "
     "Brain Villain stands in the RIGHT version, perfectly comfortable. "
     "Circuit 3 glows brightest. "
     "Camera: SKULL INTERIOR SPLIT. Motion: RIGHT SIDE LIGHTS UP."),

    (46, "The more vocabulary Alex acquires, the more certain he feels. The more certain he feels, the less he questions.",
     "A circular arrow diagram: VOCABULARY → CERTAINTY → LESS QUESTIONING → MORE VOCABULARY. "
     "The loop closes. Brain Villain rides the circle. No escape arrow shown. "
     "Camera: WIDE DIAGRAM SHOT. Motion: ARROWS TRACE the loop."),

    (47, "Trap Three rewires in one direction only: more vocabulary, more certainty — not more accuracy.",
     "A single arrow pointing right: VOCABULARY → CERTAINTY. "
     "A second arrow (accuracy) pointing same direction but disconnected — floating, not connected. "
     "Label: 'ACCURACY: NOT INCLUDED'. Brain Villain holds up the disconnected accuracy arrow "
     "with a shrug. "
     "Camera: CLEAN DIAGRAM SHOT. Motion: ACCURACY ARROW FLOATS DETACHED."),

    # ═══════════════════════════════════════════════════════
    # TRAP 4 — THE NIGHT DRAIN — 11 beats
    # ═══════════════════════════════════════════════════════

    (48, "It is 10:47 PM. Alex is tired.",
     "Dark warm interior. 10:47 PM clock prominent. Alex on couch, slouched, phone in hand. "
     "Eyes half-closed. A 'COGNITIVE RESERVE' battery in corner: 12% remaining. "
     "Brain Villain inside skull: awake and alert — inverse of Alex. "
     "Camera: WIDE SHOT of couch scene. Motion: BATTERY ICON visible, low level."),

    (49, "He has made decisions since 7 AM — small ones, large ones, a hundred in between.",
     "A timeline from 7 AM to 10:47 PM. Dozens of decision icons stacked along it "
     "(food, emails, work choices, small purchases). Each depletes the battery slightly. "
     "By 10:47: battery near empty. "
     "Camera: HORIZONTAL TIMELINE SHOT. Motion: DECISION ICONS populate left to right."),

    (50, "He opens his phone. He adds something to his cart.",
     "Alex's phone screen: shopping app. An item in cart. His thumb hovering over BUY. "
     "Brain Villain inside skull: leaning toward the phone, encouraging. "
     "Camera: OVER-SHOULDER SHOT of phone screen. Motion: CART ITEM appears."),

    (51, "He tells himself he will decide in the morning.",
     "Alex's thought bubble: 'DECIDE IN THE MORNING' in calm blue text. "
     "But his thumb is still on the screen. The intention and the action are diverging. "
     "Camera: MEDIUM CLOSE-UP, thought bubble + hand visible. Motion: THUMB STAYS."),

    (52, "He buys it before he puts the phone down.",
     "PURCHASE CONFIRMATION on screen: 'ORDER PLACED.' Alex's thumb moved. "
     "Brain Villain inside skull: one finger raised — 'that's all it took.' "
     "Alex expression: momentary surprise at himself. "
     "Camera: CLOSE-UP on phone screen confirmation. Motion: ORDER PLACED notification."),

    (53, "Shai Danziger — Ben-Gurion University — studied eight judges over ten months.",
     "Academic white scene. A courtroom with eight judge silhouettes. Label: "
     "'SHAI DANZIGER · BEN-GURION UNIVERSITY · 10 MONTHS'. A calendar of hearings. "
     "Camera: WIDE COURTROOM SHOT. Motion: LABEL FADES IN."),

    (54, "Morning parole decisions: granted sixty-five percent of the time.",
     "Morning courtroom. Green gavel. Large '65%' on screen. Judges alert, engaged. "
     "A row of parole applicants — majority approved (green checkmarks). "
     "Camera: WIDE SHOT. Motion: '65%' ANIMATES IN."),

    (55, "Late afternoon: eleven percent.",
     "Same courtroom, different light — late afternoon golden. Red gavel. Large '11%'. "
     "Most applicants now rejected (red X marks). Judges slumped slightly. "
     "Camera: SAME WIDE SHOT as B54 for direct comparison. Motion: '11%' ANIMATES IN."),

    (56, "Same judges. Same cases. Same evidence. Different cognitive reserve.",
     "Split panel: MORNING (left) vs AFTERNOON (right). Identical case files in both. "
     "Only difference: a COGNITIVE RESERVE battery — full on left, near empty on right. "
     "Labels: 'SAME JUDGES · SAME CASES · SAME EVIDENCE.' "
     "Camera: SPLIT PANEL SHOT. Motion: BATTERY drops in right panel."),

    (57, "The Brain Villain does not need to be clever at 11 PM. It only needs to wait.",
     "Alex's skull at 11 PM. Brain Villain seated comfortably in an armchair. "
     "Not scheming — just waiting. Legs crossed, smug smile, heavy-lidded eyes. "
     "A clock on the skull wall shows 11:00 PM. "
     "Camera: SKULL INTERIOR WIDE SHOT. Motion: BRAIN VILLAIN taps fingers on armrest."),

    (58, "Impulse purchases peak between nine and midnight — not because people want more at night, but because the override mechanism has run out of fuel.",
     "A 24-hour purchase graph. Spike between 9 PM - midnight. "
     "Below the spike: a 'WILLPOWER TANK' shown empty for that time window. "
     "Alex's figure small at the base of the spike — one of many. "
     "Camera: WIDE DATA VISUALIZATION. Motion: SPIKE DRAWS, TANK EMPTIES."),

    # ═══════════════════════════════════════════════════════
    # TRAP 5 — THE UPGRADE LOCK — 11 beats
    # ═══════════════════════════════════════════════════════

    (59, "Six months ago, Alex upgraded his apartment.",
     "Alex in a new, better apartment. Bright, modern. Expression: genuine satisfaction. "
     "Calendar on wall: SIX MONTHS AGO. A 'SATISFACTION' meter reads HIGH. "
     "Brain Villain inside skull: circuit 5 activating quietly in background. "
     "Camera: WIDE SHOT of new apartment. Motion: SATISFACTION METER at peak."),

    (60, "The first eleven days were different. Genuinely better.",
     "11-day mini-calendar. Each day has a happy expression icon. "
     "A satisfaction curve: stays high for 11 days. "
     "Alex in the apartment: genuinely content. "
     "Camera: MEDIUM SHOT. Motion: CALENDAR FILLS for 11 days, all positive."),

    (61, "Then it became normal.",
     "Day 12. The same apartment. Alex's expression: neutral. Not unhappy. Not happy. "
     "The satisfaction curve drops from HIGH to BASELINE. The apartment didn't change. "
     "Brain Villain inside skull: circuit 5 now fully active. "
     "Camera: SAME ANGLE as B60 for contrast. Motion: CURVE DROPS to baseline."),

    (62, "He is not unhappy. He is not satisfied either. He is calibrated.",
     "Alex's expression: flat neutral. A calibration dial beside him — pointing exactly to BASELINE. "
     "Not left (unhappy). Not right (satisfied). Dead center: 'CALIBRATED'. "
     "Brain Villain: arms crossed, satisfied with this outcome. "
     "Camera: MEDIUM CLOSE-UP. Motion: DIAL SETTLES at center."),

    (63, "Kent Berridge — University of Michigan — spent thirty years separating two distinct systems.",
     "Academic white scene. A researcher figure. Label: 'KENT BERRIDGE · UNIVERSITY OF MICHIGAN · 30 YEARS'. "
     "Two brain diagrams shown: WANTING system (left) and LIKING system (right), distinct and separate. "
     "Camera: WIDE ACADEMIC SHOT. Motion: TWO SYSTEMS REVEAL."),

    (64, "Wanting. And liking.",
     "Clean white frame. Two large bold words: 'WANTING' (left, dopamine-orange) and 'LIKING' (right, calm-green). "
     "A dividing line between them. They are different systems. "
     "Camera: CLEAN SPLIT SHOT. Motion: WORDS APPEAR with impact."),

    (65, "Wanting is driven by dopamine. It scales with anticipation and exposure.",
     "WANTING system visual: dopamine molecule icon. An arrow pointing UP as exposure increases. "
     "Alex looking at an upgraded item in a store window — wanting intensifies with each look. "
     "Camera: MEDIUM SHOT. Motion: WANTING ARROW grows with each exposure."),

    (66, "Liking is driven by opioid circuits. It decreases with repetition.",
     "LIKING system visual: opioid receptor icon. An arrow pointing DOWN as repetition increases. "
     "Alex in his apartment on day 11, day 30, day 90 — liking decreases each panel. "
     "Camera: THREE-PANEL SHOT. Motion: LIKING ARROW drops at each stage."),

    (67, "Every upgrade strengthens wanting. Every upgrade habituates liking.",
     "Side-by-side bars: WANTING (grows after each upgrade, arrow up). "
     "LIKING (shrinks after each upgrade, arrow down). "
     "Three upgrades shown: the gap widens each time. "
     "Camera: BAR CHART SHOT. Motion: BARS ANIMATE with each upgrade."),

    (68, "The floor does not go back. The ceiling keeps moving.",
     "A vertical scale. Alex's 'acceptable baseline' floor rises with each upgrade — "
     "the old normal is now below acceptable. The ceiling above keeps moving up. "
     "Alex stands between them: the gap stays the same width but both limits shift up. "
     "Camera: VERTICAL SCALE SHOT. Motion: FLOOR and CEILING both move up together."),

    (69, "Trap Five is the only one that compounds biologically — not just financially. Alex does not need to buy more. His brain has already decided he cannot want less.",
     "Alex's skull — circuit 5 pulsing strongest of all five. "
     "A biological compounding graph (steeper than financial): DNA helix growing upward. "
     "Brain Villain at circuit 5: satisfied — this one runs itself. "
     "Camera: SKULL INTERIOR FOCUS on circuit 5. Motion: BIOLOGICAL CURVE steepens."),

    # ═══════════════════════════════════════════════════════
    # SYSTEM CLOSE — 5 beats
    # ═══════════════════════════════════════════════════════

    (70, "Five programs. Running simultaneously. Without permission.",
     "All five circuits in Alex's skull lit simultaneously — electric red, glowing. "
     "Alex in center frame, transparent skull dominant. Brain Villain at control panel: "
     "five switches all active. "
     "Camera: MEDIUM WIDE, skull prominent. Motion: ALL FIVE CIRCUITS pulse in sync."),

    (71, "Program One generates the impulse before the decision exists.",
     "Circuit 1 highlights. A small impulse arrow fires before a decision bubble forms. "
     "Sequence: IMPULSE → (decision bubble appears after, too late). "
     "Camera: SKULL INTERIOR on circuit 1. Motion: IMPULSE FIRES before bubble."),

    (72, "Program Two hides the evidence so it stays invisible.",
     "Circuit 2 highlights. A bank statement approaches — a wall goes up, deflects it. "
     "Alex on other side of wall: cannot see. "
     "Camera: MEDIUM SHOT, wall prominent. Motion: WALL RISES blocking statement."),

    (73, "Program Three provides the vocabulary to feel in control while losing the same way.",
     "Circuit 3 highlights. Alex surrounded by vocabulary labels — but a flat performance "
     "graph shows no improvement. Vocabulary floats above the flat line, disconnected. "
     "Camera: MEDIUM WIDE. Motion: VOCABULARY LABELS float, GRAPH stays flat."),

    (74, "Program Four lowers the override at the exact moment it is needed most. Program Five raises the floor so return is no longer possible.",
     "Circuits 4 and 5 highlight together. LEFT: override battery at 0% when impulse fires. "
     "RIGHT: floor level rises above 'previous normal' — return impossible. "
     "Brain Villain manages both simultaneously. "
     "Camera: SPLIT SKULL INTERIOR. Motion: BATTERY drops and FLOOR rises simultaneously."),

    # ═══════════════════════════════════════════════════════
    # BRAIN VILLAIN'S LAST TRICK — 11 beats
    # ═══════════════════════════════════════════════════════

    (75, "The Brain Villain has one response to this list.",
     "Brain Villain EXTREME CLOSE-UP inside skull. Calm. Unsurprised. "
     "It has heard this kind of naming before. One finger raised — 'I have a response.' "
     "Camera: EXTREME CLOSE-UP on Brain Villain. Motion: SLOW PUSH IN on villain's face."),

    (76, "You are feeling it right now.",
     "Alex turns to face camera directly — second person. Direct address. "
     "He points outward (at viewer). Brain Villain inside skull: nodding at the viewer. "
     "Camera: DIRECT ADDRESS, medium shot. Motion: POINT toward viewer."),

    (77, "Not denial. Something quieter.",
     "Alex's expression: not defensive. Something subtler — a slight confident tilt of head. "
     "No speech bubble, no label. The quietness is the thing. "
     "Camera: CLOSE-UP on Alex's face. Motion: EXPRESSION SHIFT, subtle."),

    (78, "Something that sounds like self-awareness: 'I already knew about most of these.'",
     "Alex's thought bubble: 'I already knew about most of these.' The thought sounds wise. "
     "Brain Villain inside skull: holds this thought bubble up with both hands — proudly. "
     "Camera: MEDIUM SHOT, thought bubble prominent. Motion: BUBBLE APPEARS, villain presents it."),

    (79, "That thought is not insight. Not wisdom. Not progress.",
     "Three icons crossed out in sequence: INSIGHT (crossed out) · WISDOM (crossed out) · "
     "PROGRESS (crossed out). The thought bubble from B78 sits below all three crossed-out icons. "
     "Camera: CLEAN WHITE DIAGRAM. Motion: X MARKS appear on each icon."),

    (80, "It is the Expertise Trap wearing the costume of insight.",
     "Circuit 3 (EXPERTISE TRAP) glows inside skull. But now it wears a costume: "
     "a 'SELF-AWARENESS' mask placed over circuit 3. Same circuit, different disguise. "
     "Brain Villain holds up the mask with satisfaction. "
     "Camera: SKULL INTERIOR. Motion: MASK REVEALS over circuit 3."),

    (81, "The programs are not broken.",
     "All five circuits glowing steadily. No malfunction. No errors. Running perfectly. "
     "Brain Villain stands with arms out — everything working as designed. "
     "Camera: FULL SKULL INTERIOR showing all 5. Motion: ALL CIRCUITS PULSE STEADY."),

    (82, "They are perfectly designed for an environment where pattern recognition and immediate reward were survival.",
     "Scene transition: prehistoric landscape. A silhouetted ancestor figure — same brain shape "
     "visible in skull (the same circuits, same villain). "
     "Environment: savanna, berries, predators. The programs make perfect sense here. "
     "Camera: WIDE LANDSCAPE SHOT. Motion: LANDSCAPE FADES IN around ancestor."),

    (83, "Knowing the name of a predator kept your ancestors alive.",
     "Ancestor figure pointing at a predator, naming it. Small speech bubble: a predator symbol. "
     "The EXPERTISE program (circuit 3) fires — naming things = survival. "
     "Camera: MEDIUM SHOT of ancestor. Motion: CIRCUIT 3 pulses in ancestor's skull."),

    (84, "It does not stop the dopamine from firing on Wednesday.",
     "Return to modern scene. Alex on Wednesday. SAME circuit — now firing for a shopping item. "
     "Same mechanism, wrong environment. Brain Villain: same posture in both eras. "
     "Camera: SIDE-BY-SIDE: ancestor (circuit firing for survival) vs Alex (circuit firing for shopping). "
     "Motion: SAME CIRCUIT PULSE in both scenes."),

    (85, "The Brain Villain was built for that world. Not this one.",
     "Alex's skull. Brain Villain in center. Behind it: the modern world (phone, apps, stores). "
     "The Brain Villain looks slightly out of place — built for something else. "
     "Not malicious. Just outdated. "
     "Camera: SKULL INTERIOR, modern world visible through the transparent glass. "
     "Motion: MODERN WORLD FADES IN behind Brain Villain."),

    # ═══════════════════════════════════════════════════════
    # IDENTITY CLOSE — 8 beats
    # ═══════════════════════════════════════════════════════

    (86, "None of this is a character flaw.",
     "Alex standing straight. Calm. Warm beige light. "
     "A 'CHARACTER FLAW' label appears and immediately dissolves — explicitly erased. "
     "Brain Villain visible in skull but small — named, contained, not threatening. "
     "Camera: MEDIUM SHOT, warm light. Motion: LABEL DISSOLVES."),

    (87, "Anticipation Burn kept ancestors motivated through scarcity. Balance Blindspot reduced cortisol when debt meant death.",
     "Two ancestral scenes, small panels: LEFT — ancestor motivated by anticipation (hunting). "
     "RIGHT — ancestor avoiding painful information (reducing cortisol = survival). "
     "Both circuits shown: 1 and 2 firing in ancestor skulls. "
     "Camera: DUAL PANEL SHOT. Motion: PANELS APPEAR side by side."),

    (88, "Night Drain preserved cognitive resources. Expertise Trap protected identity in a world where certainty built coalitions.",
     "Two more ancestral panels: LEFT — ancestor conserving energy at night (Night Drain = rest). "
     "RIGHT — ancestor's certainty building tribe loyalty (Expertise Trap = status). "
     "Circuits 4 and 3 shown. "
     "Camera: DUAL PANEL SHOT. Motion: PANELS APPEAR."),

    (89, "Upgrade Lock ensured the tribe kept climbing when climbing was survival.",
     "Ancestral tribe climbing: better shelter, better tools, better position. "
     "Circuit 5 firing — the drive to upgrade = tribal advancement. It worked then. "
     "Camera: WIDE ANCESTRAL LANDSCAPE. Motion: TRIBE CLIMBS."),

    (90, "The programs are not broken. They are perfectly designed for an environment that no longer exists.",
     "Side by side: ANCESTRAL WORLD (left, circuits firing = survival). "
     "MODERN WORLD (right, same circuits firing = financial drain). "
     "Same circuits. Different outcomes. Same programs — different world. "
     "Camera: WIDE SPLIT. Motion: BOTH WORLDS shown simultaneously."),

    (91, "The Brain Villain was built for that world. Not this one.",
     "Brain Villain standing in center, modern world around it. "
     "Not evil — just from a different era. A slight sad dignity to it. "
     "Alex stands beside it — understanding, not hostile. "
     "Camera: MEDIUM SHOT, warm tone. Motion: SLIGHT ZOOM OUT reveals full scene."),

    (92, "The next video maps the one structural decision that shuts down three of these five simultaneously.",
     "A preview tease: five circuit paths shown. Three of them show a switch being turned OFF "
     "by a single decision — illustrated simply. '3 OF 5 — ONE DECISION'. "
     "Alex looking at it with interest. "
     "Camera: MEDIUM SHOT. Motion: THREE CIRCUITS DIM as preview."),

    (93, "If your brain is doing this to you right now — subscribe. We break down a new bias every week. It's free. And it might save you more than you think.",
     "FINAL FRAME: Clean white background. Alex facing camera, calm confidence. "
     "Brain Villain in skull — small, visible, named. Five circuits dim and quiet. "
     "Alex's expression: the peer who figured it out first. "
     "Subscription bell icon, small and clean. "
     "Camera: MEDIUM SHOT, direct address. Motion: SLOW ZOOM IN to Alex's face as final beat."),

]


def build_image_prompts_txt():
    """Generate V13_v31_IMAGE_PROMPTS.txt — one prompt per beat, style preamble prepended."""
    lines = []
    lines.append("VIDEO 13 — BRIEF v3.1")
    lines.append("93 IMAGE PROMPTS — copy and paste each BEAT into Google Flow / Imagen 4")
    lines.append("BLUE t-shirt · S17 Thumbnail Continuity · Visual-first rule")
    lines.append("=" * 80)
    lines.append("")

    for beat_num, narration, prompt in BEATS:
        lines.append(f"{'━'*3} BEAT {beat_num} {'━'*3}")
        lines.append(f'"{narration}"')
        lines.append("")
        lines.append(STYLE_PREAMBLE + " " + prompt)
        lines.append("")

    path = "/home/user/Claudeeee/V13_v31_IMAGE_PROMPTS.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"TXT: {path} | {len(BEATS)} beats")
    return path


def build_image_prompts_pdf():
    """Generate V13_v31_IMAGE_PROMPTS.pdf — 4-part PDF with style preamble per beat."""
    styles = getSampleStyleSheet()

    HDR  = ParagraphStyle('HDR',  parent=styles['Normal'], fontSize=10, leading=13,
                          alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                          fontName='Helvetica-Bold')
    H1   = ParagraphStyle('H1',   parent=styles['Title'],  fontSize=13, leading=17, alignment=TA_CENTER)
    META = ParagraphStyle('META', parent=styles['Normal'], fontSize=8,  leading=11,
                          alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    BN   = ParagraphStyle('BN',   parent=styles['Normal'], fontSize=11, leading=15,
                          fontName='Helvetica-Bold', textColor=colors.HexColor('#333333'),
                          spaceBefore=12, spaceAfter=2)
    NAR  = ParagraphStyle('NAR',  parent=styles['Normal'], fontSize=10, leading=14,
                          textColor=colors.HexColor('#555555'), spaceAfter=4)
    PRE  = ParagraphStyle('PRE',  parent=styles['Normal'], fontSize=8,  leading=12,
                          textColor=colors.HexColor('#B02A2A'), spaceAfter=2)
    PRO  = ParagraphStyle('PRO',  parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=6)

    def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

    # Split into 4 parts
    part_size = len(BEATS) // 4
    parts = [
        BEATS[:part_size],
        BEATS[part_size:part_size*2],
        BEATS[part_size*2:part_size*3],
        BEATS[part_size*3:],
    ]
    part_labels = [
        f"HOOK + TRAP 1 — Beats 1–{part_size}",
        f"TRAP 2 + CTA + TRAP 3 — Beats {part_size+1}–{part_size*2}",
        f"TRAP 4 + TRAP 5 + SYSTEM CLOSE — Beats {part_size*2+1}–{part_size*3}",
        f"BRAIN VILLAIN + IDENTITY CLOSE — Beats {part_size*3+1}–93",
    ]

    pdf_path = "/home/user/Claudeeee/V13_v31_IMAGE_PROMPTS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    flow = [
        Paragraph("NEUROCENTS · VIDEO 13 — BRIEF v3.1", HDR),
        Spacer(1, 4),
        Paragraph(esc("5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)"), H1),
        Spacer(1, 4),
        Paragraph("IMAGE PROMPTS · 93 beats · BLUE t-shirt · S17 Continuity · Visual-first rule", META),
        Spacer(1, 16),
    ]

    for part_idx, (part_beats, part_label) in enumerate(zip(parts, part_labels)):
        flow.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#B02A2A')))
        flow.append(Spacer(1, 4))
        flow.append(Paragraph(f"PART {part_idx+1} — {esc(part_label)}", HDR))
        flow.append(Spacer(1, 8))

        for beat_num, narration, prompt in part_beats:
            flow.append(Paragraph(f"━━━ BEAT {beat_num} ━━━", BN))
            flow.append(Paragraph(f'"{esc(narration)}"', NAR))
            flow.append(Paragraph("STYLE:", PRE))
            flow.append(Paragraph(esc(STYLE_PREAMBLE), PRO))
            flow.append(Paragraph("SCENE:", PRE))
            flow.append(Paragraph(esc(prompt), PRO))
            flow.append(Spacer(1, 4))

        flow.append(Spacer(1, 12))

    flow.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#888888')))
    flow.append(Spacer(1, 8))
    flow.append(Paragraph(f"END · 93 beats · BLUE t-shirt · Brief v3.1", META))

    doc.build(flow)
    print(f"PDF: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    build_image_prompts_txt()
    build_image_prompts_pdf()
    print(f"\n✅ V13 IMAGE PROMPTS BRIEF v3.1 — 2 archivos generados")
    print(f"   93 beats · BLUE t-shirt ✅")
    print(f"   Beat 1: S17 Thumbnail Continuity — '5' on screen + 5 circuits ✅")
    print(f"   Visual-first rule: no text repeating narration ✅")
    print(f"   Hook S2 Dato Sin Contexto ✅")
