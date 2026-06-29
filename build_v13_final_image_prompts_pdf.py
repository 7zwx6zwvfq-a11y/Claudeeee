#!/usr/bin/env python3
"""
V13 FINAL — Image Prompts PDF (104 beats)
5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)
Full STYLE preamble prepended to each prompt — ready to copy-paste into Google Flow / Imagen 4.
Splits into 4 parts of ~26 beats each.
Visual-first rule applied: no text labels repeating narration.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

TITLE    = "5 Ways Your Brain Physically Rewires Itself to Stay Broke (Without Telling You)"
SUBTITLE = "NEUROCENTS · VIDEO 13"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines, clean solid color fills, "
    "no gradients. ALEX: large beige oval head, transparent glass upper skull revealing "
    "pink cartoon Brain Villain, small black dot eyes, thin neutral mouth, black spiky hair, "
    "BLUE t-shirt (NOT RED — verify every time), gray pants. Brain Villain: pink cartoon brain "
    "character, heavy-lidded eyes, slight smirk, small teeth. Palette: beige skin #F5E6C8 · "
    "pink brain #E8A598 · blue shirt · gray pants · green: savings/gains · "
    "red: loss/danger · white: diagram scenes. 16:9, 1280x720."
)

# Format: (beat_num, section, narration, image_prompt)
BEATS = [

    # ── HOOK ──────────────────────────────────────────────────────────────────────────────────
    (1, "HOOK",
     "Alex earns more than he did three years ago. He has less to show for it.",
     "Split panel: LEFT — Alex three years ago, smaller apartment, content expression, hands in pockets, "
     "small savings bar in corner (green, modest). RIGHT — Alex now, larger apartment behind him, face "
     "tight with confusion, larger empty wallet icon visible. Income arrow points UP between panels, "
     "savings bar SMALLER on the right. White background."),

    (2, "HOOK",
     "Not bad investments.",
     "Alex close-up, eyes directed DOWN AND LEFT (defeat direction). No props, no text labels. "
     "Clean white background. Brow slightly lowered."),

    (3, "HOOK",
     "Not unexpected expenses.",
     "Alex close-up, eyes directed UP AND RIGHT (searching direction). Slight headshake implied by "
     "posture. Clean white background. No props."),

    (4, "HOOK",
     "Five programs he was never told about.",
     "Alex's transparent skull shown prominently. Inside: five distinct glowing circuits arranged "
     "around the Brain Villain — each circuit a different color node connected by thin electric lines. "
     "Villain stands at center, arms crossed, expression smug. Alex expression: neutral outside, "
     "unaware. White background."),

    (5, "HOOK",
     "Programs that physically alter the architecture of his brain.",
     "Close-up cross-section of stylized cartoon brain. Five separate red circuit paths etched into "
     "the surface like carved grooves — thick, structural, permanent-looking. No text labels on circuits. "
     "White background. Anatomical diagram style, flat cartoon."),

    (6, "HOOK",
     "The third one gets worse the more educated he becomes.",
     "Alex standing beside a rising graduation-cap icon and open book stack. The third glowing circuit "
     "inside his skull grows BRIGHTER and thicker as the book stack gets taller. Alex's expression: "
     "confident smile — unaware. Irony visual. No text labels."),

    (7, "HOOK",
     "We are going to show you all five.",
     "Alex facing viewer directly, calm and confident. His transparent skull shows all five circuits "
     "lit, Brain Villain visible at center. Alex's posture: open, welcoming — like beginning a "
     "guided tour. White background."),

    (8, "HOOK",
     "The order matters. Trap One fires first.",
     "A horizontal sequence of five numbered circles (1–5) connected by arrows — like a chain "
     "reaction diagram. Circle 1 is red and pulsing. Circles 2–5 are grey/dormant. Alex stands "
     "beside the chain, pointing at circle 1. White background."),

    (9, "HOOK",
     "Your brain started running it this week.",
     "Alex's Brain Villain inside skull at a small control panel — one lever pulled DOWN (active). "
     "Digital clock in corner shows CURRENT DAY icon (mid-week). Villain expression: satisfied smirk. "
     "Alex exterior expression: unaware. Close-up on skull."),

    (10, "HOOK",
     "Wednesday afternoon. He has not been paid.",
     "Alex at desk, mid-week. Calendar on wall — Wednesday circled in neutral blue. Salary notification "
     "icon in corner greyed out (not arrived yet). Alex posture: relaxed, slightly idle. Neutral mood."),

    (11, "HOOK",
     "He already knows what he will buy — the jacket, the dinner, the upgrade.",
     "Thought bubble above Alex's head containing three icons: leather jacket silhouette, fork-and-plate "
     "icon, smartphone with upgrade arrow. Thought bubble is vivid and colorful. Alex's expression: "
     "light anticipatory smile. No text labels on the icons."),

    (12, "HOOK",
     "His brain made those decisions forty-eight hours before his salary existed.",
     "Timeline arrow: LEFT — 'Wednesday' marker (Alex with thought bubble). RIGHT — 'Friday' marker "
     "(salary envelope icon). A dotted decision line starts at Wednesday, BEFORE the salary arrives. "
     "Red dot marks when brain committed. White background, diagram style."),

    # ── TRAP 1: ANTICIPATION BURN ──────────────────────────────────────────────────────────────
    (13, "TRAP 1: ANTICIPATION BURN",
     "Wolfram Schultz. Cambridge University. Nobel Prize in Medicine.",
     "Clean institutional label card: 'WOLFRAM SCHULTZ / CAMBRIDGE' in bold black block letters. "
     "Small brain icon beside name. White background. No photo — text IS the prop here."),

    (14, "TRAP 1: ANTICIPATION BURN",
     "Dopamine does not fire when you receive a reward. It fires when you predict one.",
     "Two-panel diagram. LEFT: monkey reaching for reward, dopamine bar LOW. RIGHT: same monkey "
     "seeing a SIGNAL that reward is coming — dopamine bar HIGH, red/orange spike. Arrow between "
     "panels labeled with small clock icon (timing). No text labels on bars."),

    (15, "TRAP 1: ANTICIPATION BURN",
     "Wednesday peak. Friday declining signal.",
     "Dopamine curve graph: rises sharply at 'WED' marker on x-axis, begins declining through "
     "'THU', lower at 'FRI'. Green highlight at peak, fading to neutral. No text on y-axis. "
     "Small Alex figure stands under the Wednesday peak, looking satisfied."),

    (16, "TRAP 1: ANTICIPATION BURN",
     "By Friday, the spending is just a receipt. The decision was made on Wednesday.",
     "Alex on Friday, tapping phone to complete a purchase. Expression: slightly flat, automatic. "
     "Shadow of his Wednesday self (vivid, excited) looms behind him. Receipt icon appears in hand. "
     "No text. Visual: past self made this choice."),

    (17, "TRAP 1: ANTICIPATION BURN",
     "His brain spent the money before the salary existed.",
     "Bank balance bar. LEFT: empty (pre-salary). RIGHT: salary arrives, but three purchase arrows "
     "immediately drain it — jacket, dinner, upgrade icons flowing out automatically. The drain "
     "arrows were ALREADY DRAWN in dotted lines before the salary bar filled. Automatic. White background."),

    (18, "TRAP 1: ANTICIPATION BURN",
     "This is not a character flaw. This is a mechanism.",
     "Alex looking directly at viewer. Expression: calm, knowing. No props. Clean white background. "
     "Inside his skull: the Brain Villain running the anticipation circuit — mechanical, not malicious. "
     "Villain expression: neutral, operational."),

    (19, "TRAP 1: ANTICIPATION BURN",
     "It runs in every brain.",
     "Three different silhouette figures (different heights, professions implied by clothing icons) — "
     "all three with transparent skulls showing the same Trap 1 circuit pattern glowing identically. "
     "White background. Universal mechanism visual."),

    # ── TRAP 2: BALANCE BLINDSPOT ──────────────────────────────────────────────────────────────
    (20, "TRAP 2: BALANCE BLINDSPOT",
     "Trap One feeds directly into Trap Two.",
     "The horizontal chain diagram from Beat 8 — now circles 1 and 2 are both red and lit. "
     "Arrow between 1 and 2 is thick and glowing. Alex beside the chain, expression shifting "
     "from mild concern to something quieter."),

    (21, "TRAP 2: BALANCE BLINDSPOT",
     "Saturday morning. Alex does not check his balance.",
     "Alex in bed, phone face-down on nightstand. Calendar shows SATURDAY. Balance notification "
     "icon on phone screen (face-down, invisible to Alex). Alex expression: eyes closed or looking "
     "away. The phone screen glows faintly, unseen."),

    (22, "TRAP 2: BALANCE BLINDSPOT",
     "He will check next week.",
     "Same scene. Alex now at kitchen table, coffee in hand. Phone still face-down nearby. "
     "A small thought bubble: calendar with next week indicated by faint arrow. Expression: "
     "vague, non-committal. Brain Villain in skull: satisfied, reclining."),

    (23, "TRAP 2: BALANCE BLINDSPOT",
     "Thirty-day balance check pattern — six checks after paycheck, zero after purchases.",
     "Bar chart calendar — 30 day strip. First 6 days: tall green bars (checks). Days 7–30: "
     "flat zero bars. Small purchase icons appear on days 7–10 where the bars drop to zero. "
     "Pattern is stark and visual. White background. No axis text labels."),

    (24, "TRAP 2: BALANCE BLINDSPOT",
     "Galai and Sade. Hebrew University. Two thousand and six.",
     "Clean institutional label card: 'GALAI & SADE / HEBREW UNIVERSITY / 2006' in bold black. "
     "Small ostrich silhouette icon beneath the names — minimal, iconic. White background."),

    (25, "TRAP 2: BALANCE BLINDSPOT",
     "They called it the ostrich effect.",
     "Alex with head turned away from a glowing phone screen showing a falling red bar chart. "
     "Alex's eyes deliberately averted. Brain Villain inside skull: covering villain's own eyes "
     "with tiny hands, expression theatrical but deliberate. Ostrich-pose implied without "
     "literal ostrich. White background."),

    (26, "TRAP 2: BALANCE BLINDSPOT",
     "Painful information — the brain stops seeking it.",
     "Diagram: LEFT — red painful data icon (downward arrow, red). RIGHT — brain circuit with "
     "a literal OFF switch flicking to OFF position. Arrow between them shows causation. "
     "No text labels on the mechanism. Small Alex silhouette in background, turned away."),

    # ── TRAP 2 CONTINUED + CTA + TRAP 3 START ─────────────────────────────────────────────────
    (27, "TRAP 2: BALANCE BLINDSPOT",
     "Not a choice. A conditioned reflex that reduces cortisol.",
     "Two-stage diagram: Stage 1 — red data icon triggers pain signal (jagged line). "
     "Stage 2 — avoidance behavior flattens the pain signal (smooth line). Automatic arrow "
     "between stages. Alex silhouette at far right, cortisol level bar dropping from red to neutral. "
     "No text on the bars."),

    (28, "TRAP 2: BALANCE BLINDSPOT",
     "Every bad number that was seen became a pain point recorded.",
     "Timeline strip with small red exclamation icons at irregular intervals — each one a "
     "financial pain moment. Alex at far right of the timeline, posture slightly hunched, "
     "accumulated weight of the timeline pressing on him. Visual: learned aversion."),

    (29, "TRAP 2: BALANCE BLINDSPOT",
     "The avoidance became automatic.",
     "The same phone screen from Beat 21 now appears TWICE — Week 1 (Alex briefly looks, "
     "turns away) and Week 4 (Alex does not even glance, phone completely ignored). "
     "Arrow between panels shows time. Automaticity is the story."),

    (30, "TRAP 2: BALANCE BLINDSPOT",
     "Money leaves. Alex does not see it.",
     "Alex standing in room. Multiple small money icons (coins, notes) flow out through a "
     "door behind him — steady stream. Alex faces the opposite direction, completely unaware. "
     "The drain is silent, invisible to him. White background."),

    (31, "TRAP 2: BALANCE BLINDSPOT",
     "Trap One runs undisturbed. And Trap Three gives it a vocabulary.",
     "The chain diagram: circles 1, 2, 3 now connected and lit in sequence. Circle 3 has "
     "a small book icon above it — vocabulary/expertise. Alex beside chain, expression: "
     "unaware but confident. Building tension."),

    (32, "CTA",
     "If your brain is doing this to you right now — subscribe.",
     "Alex turned toward viewer, direct expression, slightly urgent. Inside skull: Brain Villain "
     "holds up a small STOP sign (the Villain trying to prevent the subscribe). Below Alex: "
     "clean red subscribe button icon, minimal style. White background."),

    (33, "CTA",
     "We break down a new bias every week. It's free. And it might save you more than you think.",
     "Subscribe button large and centered, Alex standing beside it with arm around it (friendly). "
     "Brain Villain inside skull: arms crossed, pouting — disapproves of this CTA. "
     "Alex expression: warmly direct. White background."),

    # ── TRAP 3: EXPERTISE TRAP ─────────────────────────────────────────────────────────────────
    (34, "TRAP 3: EXPERTISE TRAP",
     "Alex has been reading behavioral finance.",
     "Alex at desk, thick book open, title spine shows small brain icon (no specific title text). "
     "Multiple sticky notes around desk with concept words visible — but not repeated from narration. "
     "Use abstract squiggles or icons on sticky notes, not words. Alex expression: engaged, studious."),

    (35, "TRAP 3: EXPERTISE TRAP",
     "Vocabulary is floating around his head — he has a language for what is happening.",
     "Alex with thought cloud surrounding his head containing floating abstract concept shapes — "
     "geometric icons suggesting mental models (triangle, gear, node-web, loop arrow). "
     "These are icons, NOT text labels. Alex expression: satisfied, equipped."),

    (36, "TRAP 3: EXPERTISE TRAP",
     "Alex feels confident. Arms crossed. He has got this.",
     "Alex in confident pose: arms crossed firmly, chin slightly raised, half-smile. "
     "Inside skull: Brain Villain mimics the pose but with an even more exaggerated smirk. "
     "White background. Both postures identical — one unaware the other is doing it too."),

    (37, "TRAP 3: EXPERTISE TRAP",
     "Terrance Odean. University of California Berkeley.",
     "Clean institutional label card: 'TERRANCE ODEAN / UC BERKELEY' in bold black. "
     "Small downward chart line icon — minimal. White background."),

    (38, "TRAP 3: EXPERTISE TRAP",
     "He studied investors who traded more frequently. They earned lower returns.",
     "Two investor figures side by side. LEFT: low-activity investor (few trade arrows), "
     "green returns bar: tall. RIGHT: high-activity investor (many trade arrows flying around), "
     "returns bar: lower, red tint. Activity does not equal performance. No text labels on bars."),

    (39, "TRAP 3: EXPERTISE TRAP",
     "The confidence had outpaced the competence.",
     "Split vertical bar chart: CONFIDENCE bar (left, rising steeply, blue) vs COMPETENCE bar "
     "(right, rising slowly, green). Confidence bar is clearly taller. Gap between them is "
     "highlighted with a red bracket. Alex tiny figure stands on top of the confidence bar, "
     "looking down at the gap. No text labels."),

    (40, "TRAP 3: EXPERTISE TRAP",
     "Kahneman. Eighty percent of people believe they are above-average drivers.",
     "Large bold numeral '80%' centered. Below: row of ten simple car icons — eight highlighted "
     "blue (believe above-average), two grey (accurate). Alex among the eight highlighted, "
     "expression confident. No 'Daniel Kahneman' text — just '80%' as the prop."),

    (41, "TRAP 3: EXPERTISE TRAP",
     "Fifty percent are mathematically wrong.",
     "Same row of ten car icons. Now five highlighted cars have a subtle red tint overlay — "
     "these are the ones who were wrong. Alex is in the red-tinted group. Expression: unchanged. "
     "Still confident. That is the point."),

    (42, "TRAP 3: EXPERTISE TRAP",
     "More vocabulary leads to more certainty — not more accuracy.",
     "Two parallel arrows rising from left to right. TOP arrow: rising with book icons along it "
     "(vocabulary accumulating). BOTTOM arrow: rises much more slowly with target-hit icons "
     "(accuracy). The gap between the two arrows WIDENS as they move right. No text labels."),

    (43, "TRAP 3: EXPERTISE TRAP",
     "Alex has the vocabulary. His chart is still flat.",
     "Split image: LEFT — Alex with floating concept-shape cloud around head (from Beat 35). "
     "RIGHT — a flat grey savings/portfolio line chart, no growth. The vocabulary and the "
     "outcome are visually disconnected. Alex looks between them with mild confusion."),

    (44, "TRAP 3: EXPERTISE TRAP",
     "Certainty and accuracy are not the same variable.",
     "Two simple meters side by side: LEFT meter labeled with a lock icon (certainty — needle "
     "at maximum). RIGHT meter labeled with a target icon (accuracy — needle at medium). "
     "Same visual format, different readings. Gap is the story. No text labels on needles."),

    (45, "TRAP 3: EXPERTISE TRAP",
     "Alex in the mirror — confident posture — empty wallet shadow on the wall.",
     "Alex standing in front of mirror. His reflection shows the confident arms-crossed pose. "
     "But his SHADOW on the wall behind him shows a deflated silhouette, wallet icon empty. "
     "The shadow tells a different story than the reflection. High contrast."),

    (46, "TRAP 3: EXPERTISE TRAP",
     "The certainty-accuracy gap is Trap Three.",
     "Clean diagram: two labeled boxes — one with lock icon (certainty), one with target icon "
     "(accuracy) — connected by a dotted line showing the gap. Red bracket highlights the space "
     "between them. Alex's tiny figure stands in the gap, looking up at both boxes. White background."),

    # ── TRAP 4: NIGHT DRAIN ────────────────────────────────────────────────────────────────────
    (47, "TRAP 4: NIGHT DRAIN",
     "Trap Three flows directly into Trap Four.",
     "The chain diagram: circles 1, 2, 3, 4 now all lit in sequence. Circle 4 glows with "
     "a moon/night icon above it. Connection arrows between all four are solid red. "
     "Alex beside the chain, expression showing dawning awareness."),

    (48, "TRAP 4: NIGHT DRAIN",
     "Ten forty-seven PM. Tuesday. Alex is tired at his desk.",
     "Alex slumped slightly at desk, posture lower than earlier beats. Clock on wall or corner: "
     "10:47 PM. Single lamp light pools warm on the desk. Eyes slightly heavy. "
     "Brain Villain inside skull: alert, upright — inverse of Alex's tired posture."),

    (49, "TRAP 4: NIGHT DRAIN",
     "He adds something to his cart. He is not fully sure. He buys it anyway.",
     "Phone screen close-up: shopping cart icon with item silhouette. Alex's finger hovers over "
     "BUY button — small pause visual (thought bubble with question mark). Next: finger taps. "
     "Confirmation icon appears. The moment of unclear purchase."),

    (50, "TRAP 4: NIGHT DRAIN",
     "Shai Danziger. Ben-Gurion University of the Negev.",
     "Clean institutional label card: 'SHAI DANZIGER / BEN-GURION UNIVERSITY' in bold black. "
     "Small gavel icon — judicial context. White background."),

    (51, "TRAP 4: NIGHT DRAIN",
     "Eight judges. Ten months. Every parole hearing they conducted.",
     "Eight silhouette judge figures in a row, small and formal. Timeline beneath them spanning "
     "ten months. Stack of case files beside each figure — emphasizing volume. "
     "White background. No text labels."),

    (52, "TRAP 4: NIGHT DRAIN",
     "Morning: sixty-five percent of parole requests granted.",
     "Bar chart — MORNING section: tall green bar reaching 65% level. Gavel icon at base. "
     "Judge silhouette alert and upright. Sun icon in corner. No percentage text on bar — "
     "the height tells the story."),

    (53, "TRAP 4: NIGHT DRAIN",
     "Afternoon: eleven percent. Same evidence. Same judges.",
     "Same bar chart — AFTERNOON section added: dramatically short red bar, 11% level. "
     "Same gavel icon at base. Judge silhouette slumped slightly. Sun lower in corner. "
     "The contrast between morning and afternoon bars is stark. Same evidence — different outcome."),

    (54, "TRAP 4: NIGHT DRAIN",
     "Alex at nine AM — alert, wallet closed. Alex at ten PM — glazed, wallet open.",
     "Side-by-side comparison. LEFT — Alex 9 AM: upright posture, eyes clear, wallet in pocket "
     "closed, phone face-down. RIGHT — Alex 10 PM: posture lower, eyes slightly glazed, "
     "wallet open on desk, phone in hand with cart icon glowing. Same person, different capacity."),

    (55, "TRAP 4: NIGHT DRAIN",
     "Decision depletion. A declining curve from morning to night.",
     "Line chart: x-axis shows time (morning to night with sun/moon icons). Y-axis: decision "
     "quality implied by curve height. Curve starts HIGH at morning, steadily declines, "
     "reaches LOW at night. No numbers on axes. Alex tiny figure stands under the declining "
     "curve at evening position."),

    (56, "TRAP 4: NIGHT DRAIN",
     "Ten PM plus shopping cart equals depleted battery.",
     "Simple equation visual: clock showing 10 PM icon + shopping cart icon = depleted battery "
     "icon (red, nearly empty). Alex beside the equation, expression connecting the dots. "
     "White background. Icons tell the whole story."),

    (57, "TRAP 4: NIGHT DRAIN",
     "Alex clicks purchase. Brain Villain was waiting for exactly this moment.",
     "Alex's hand clicking phone screen. Inside skull: Brain Villain at the controls, "
     "expression shifts to ALERT and excited the moment the click happens. Villain had been "
     "waiting — posture goes from reclining to upright. The trap fires."),

    (58, "TRAP 4: NIGHT DRAIN",
     "The Villain does not attack. It simply reclines and waits.",
     "Brain Villain inside Alex's skull: reclining in a tiny armchair, heavy-lidded eyes half "
     "closed, arms behind head. Expression: patient, unhurried. This is waiting, not hunting. "
     "The patience is the point. White background. Alex exterior: unaware."),

    (59, "TRAP 4: NIGHT DRAIN",
     "Battery at zero. Tuesday night.",
     "Full scene: Alex slumped at desk, phone glowing in hand, purchase confirmation on screen. "
     "Bottom corner: battery icon at 0% with red empty indicator. Calendar: TUESDAY NIGHT. "
     "Lamp still on. The whole scene conveys depletion without drama."),

    # ── TRAP 5: UPGRADE LOCK / HEDONIC TREADMILL ──────────────────────────────────────────────
    (60, "TRAP 5: UPGRADE LOCK",
     "All four gears are now meshing together.",
     "Four interlocking gears, each with a subtle circuit node or icon representing each trap "
     "(anticipation wave, eye-averted, book/brain gap, moon/battery). All four spinning in "
     "coordination. Alex outside the gear system, watching it run. Mechanical and inevitable."),

    (61, "TRAP 5: UPGRADE LOCK",
     "Alex can see the machine from outside.",
     "Alex standing back, looking at the four-gear system from a distance. Expression: recognition. "
     "He is seeing it for the first time from outside. Small spotlight illuminates the machine. "
     "White background. This is the moment of awareness."),

    (62, "TRAP 5: UPGRADE LOCK",
     "Six months ago — Alex pointing at his apartment, satisfied.",
     "Alex in front of a modest apartment building icon, pointing at it with pride. Expression: "
     "content, pleased. Thought bubble: simple green heart or checkmark. This was enough. "
     "Warm, simple scene."),

    (63, "TRAP 5: UPGRADE LOCK",
     "Satisfaction meter full — then declining over eleven days.",
     "Calendar strip: 11 days shown left to right. Day 1: satisfaction meter (vertical bar) "
     "fully green. Day 6: medium green. Day 11: bar down to 20%, nearly empty. Same apartment "
     "icon at bottom, unchanged. The apartment did not change — only the meter did."),

    (64, "TRAP 5: UPGRADE LOCK",
     "Day eleven. Satisfaction at twenty percent. Same apartment.",
     "Alex now looking at the same apartment from Beat 62 — but posture is different: "
     "slightly deflated, eyes scanning for something better. Apartment unchanged. "
     "Satisfaction bar in corner: 20%. The shift is internal, not external."),

    (65, "TRAP 5: UPGRADE LOCK",
     "Kent Berridge. University of Michigan. Thirty years separating two words.",
     "Clean institutional label card: 'KENT BERRIDGE / UNIVERSITY OF MICHIGAN' in bold black. "
     "Below: two simple word-cards side by side — 'WANTING' and 'LIKING' with a gap/arrow "
     "between them showing they are NOT the same. White background."),

    (66, "TRAP 5: UPGRADE LOCK",
     "Wanting and liking are not the same circuit.",
     "Brain cross-section diagram showing two distinct circuit paths. LEFT circuit: yellow/orange "
     "glow — WANTING path (dopamine arrows). RIGHT circuit: soft green glow — LIKING path. "
     "Clear visual separation. Different colors, different shapes. No text labels on the circuits."),

    (67, "TRAP 5: UPGRADE LOCK",
     "Wanting is the dopamine system — it grows with every upgrade.",
     "WANTING circuit from Beat 66, now isolated. Dopamine arrow icons growing larger with each "
     "frame — the signal amplifies. Each upgrade icon (phone, apartment, car silhouette) adds "
     "another larger dopamine arrow. The system feeds itself."),

    (68, "TRAP 5: UPGRADE LOCK",
     "Liking stays flat.",
     "LIKING circuit: a flat green line, static. Upgrade icons pass by (phone, apartment, car) "
     "but the flat line does not rise. Contrast with the growing WANTING arrows. Two circuits "
     "side by side — one growing, one flat. The mismatch is everything."),

    (69, "TRAP 5: UPGRADE LOCK",
     "Every upgrade raises the wanting. The liking stays the same.",
     "Alex on a simple rising staircase: each step is an upgrade (small phone → big phone → "
     "basic apartment → nicer apartment). At each step, small WANTING arrows grow larger. "
     "Small LIKING meter beside him stays at same level across all steps. No text labels."),

    (70, "TRAP 5: UPGRADE LOCK",
     "Alex wants more. But the liking circuit gets smaller.",
     "Alex at current step on the staircase. WANTING: large arrows. LIKING: meter now slightly "
     "SMALLER than before. The liking shrinks as wanting grows — Brian downregulation visualized. "
     "Alex expression: restless, not satisfied despite having more."),

    (71, "TRAP 5: UPGRADE LOCK",
     "Staircase of apartments — basic, good, better, best. Alex at each step with the same expression.",
     "Four-panel staircase: basic studio → one-bedroom → two-bedroom → penthouse. Alex stands "
     "at each level with IDENTICAL neutral expression. The apartments get better, he feels the "
     "same. Visual: hedonic adaptation. No text labels on apartments."),

    (72, "TRAP 5: UPGRADE LOCK",
     "The brain downregulates — fewer receptors after repetition.",
     "Microscopic-style diagram: LEFT — many receptor icons densely packed (before upgrade). "
     "RIGHT — fewer receptor icons, more spaced out (after repetition). Clean, iconic. "
     "No text labels. The visual says: the system reduces its own sensitivity."),

    (73, "TRAP 5: UPGRADE LOCK",
     "The floor keeps rising. There is no ceiling visible.",
     "Alex's staircase from Beat 69: the floor level (bottom of frame) rises with each step, "
     "compressing the space below. Above Alex: no ceiling visible, just open space suggesting "
     "infinite more steps. The trap has no top. White background."),

    (74, "TRAP 5: UPGRADE LOCK",
     "Alex is satisfied for a moment — then looking upward.",
     "Alex at current step: brief moment of satisfaction (expression: small content smile). "
     "Next instant: eyes shift upward toward next step, expression becomes restless. "
     "Two micro-expressions in sequence on same figure."),

    (75, "TRAP 5: UPGRADE LOCK",
     "Biological compound interest — the circuit grows but remains trapped in the loop.",
     "Circular loop arrow (perpetual motion diagram) with a growing bar chart inside the loop "
     "— the circuit gets stronger but goes nowhere. Green color for the growth, trapped inside "
     "a red circular boundary. Alex tiny figure running inside the loop."),

    # ── SYSTEM CLOSE ──────────────────────────────────────────────────────────────────────────
    (76, "SYSTEM CLOSE",
     "All five are running simultaneously.",
     "Five interlocking gears, each now active (circuit icons, colored nodes). All five spinning "
     "in coordinated motion. Larger than the four-gear diagram from Beat 60. The full machine "
     "revealed. White background. No text labels on gears."),

    (77, "SYSTEM CLOSE",
     "Alex sees the machine from outside.",
     "Alex standing at a distance from the five-gear system. Expression: recognition and "
     "clarity — this is the moment he sees it. Small spotlight from above. The machine is "
     "separate from him, observable. This beat is about awareness, not despair."),

    (78, "SYSTEM CLOSE",
     "Five programs. Five gears. All running.",
     "The five gears labeled with small icons only (no text): 1-anticipation wave, 2-averted eye, "
     "3-book/gap, 4-moon battery, 5-staircase loop. Each icon is distinct and instantly readable. "
     "White background. Clean diagram."),

    (79, "SYSTEM CLOSE",
     "Trap One feeds into Trap Two.",
     "Flow diagram: large circle with anticipation-wave icon → arrow → large circle with "
     "averted-eye icon. Arrow is thick, red, directional. Alex tiny figure in background, "
     "unaware. The causation chain is being built step by step."),

    # ── SYSTEM CHAIN + VILLAIN SETUP ──────────────────────────────────────────────────────────
    (80, "SYSTEM CLOSE",
     "Trap Two feeds into Trap Three. Alex cannot see the balance — so he invests more confidence.",
     "Flow diagram continues: averted-eye circle → arrow → book/gap circle. Alex in background: "
     "eyes averted from balance data, but posture is confident, arms crossed. The blindness "
     "fuels the overconfidence. Visual causation."),

    (81, "SYSTEM CLOSE",
     "Trap Three leads to Trap Four. The expertise feeds the evening confidence.",
     "Flow: book/gap circle → arrow → moon/battery circle. Alex with vocabulary-concept cloud "
     "from earlier now shown at his desk at 10 PM — the confidence persists into tired hours. "
     "The expertise trick makes him trust his depleted judgment."),

    (82, "SYSTEM CLOSE",
     "Trap Four connects to Trap Five. The depleted brain reaches for the next upgrade.",
     "Flow: moon/battery circle → arrow → staircase-loop circle. Alex at 10 PM, depleted, "
     "clicking purchase for the next upgrade. The depleted state makes the upgrade feel necessary. "
     "Full chain connection visual."),

    (83, "SYSTEM CLOSE",
     "The system runs at forty thousand and at a hundred and forty thousand. Same percentage draining.",
     "Two income columns side by side: '€40K' and '€140K' (text IS the prop here — specific numbers). "
     "Both columns show identical percentage drain: same proportion of money flowing out through "
     "five small arrows (one per trap). Income changes, drain rate does not. White background."),

    (84, "SYSTEM CLOSE",
     "The math adjusts. The programs do not.",
     "Two equations side by side — visually identical structure, different numbers. Both equal "
     "the same drain percentage. The equivalence is the point. Alex stands between them, "
     "expression: understanding. Clean white background, diagram style."),

    # ── BRAIN VILLAIN'S LAST TRICK ─────────────────────────────────────────────────────────────
    (85, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain has one response to all five.",
     "Brain Villain inside skull, holding up one finger — making a point. Expression: deliberate, "
     "strategic. Smug but not aggressive. Alex exterior: neutral. The Villain is about to deploy "
     "its final move. Close-up on skull."),

    (86, "BRAIN VILLAIN'S LAST TRICK",
     "You are feeling it right now.",
     "Alex looking at a screen (self-referential — he is the viewer). Inside his skull: Brain Villain "
     "also looking at the same screen direction, smirk widening. Both watching simultaneously. "
     "The Villain is aware the viewer is being addressed. Fourth wall moment."),

    (87, "BRAIN VILLAIN'S LAST TRICK",
     "Not anxiety. Something quieter.",
     "Alex close-up: expression subtly smug, slightly closed-off. NOT anxious or stressed — "
     "something like quiet self-assurance. This is the Expertise Trap deploying in real time. "
     "The expression is the story. White background."),

    (88, "BRAIN VILLAIN'S LAST TRICK",
     "Something that sounds like wisdom: I already know this.",
     "Thought bubble above Alex: 'I already know this.' — text in speech bubble IS the prop here. "
     "Brain Villain inside skull: smiling, approving the thought, nodding. The Villain loves this "
     "particular defense mechanism. No other text."),

    (89, "BRAIN VILLAIN'S LAST TRICK",
     "That thought is not wisdom.",
     "Same thought bubble — 'I already know this.' — now with a thick red X drawn through it. "
     "Brain Villain's smile fading slightly. Alex expression beginning to shift — cracks in "
     "the certainty. The reframe begins."),

    (90, "BRAIN VILLAIN'S LAST TRICK",
     "It is the Expertise Trap wearing the costume of wisdom.",
     "Brain Villain wearing a tiny graduation cap, holding a small scroll — dressed as wisdom. "
     "But behind the Villain: the Trap 3 (book/gap) circuit is highlighted and glowing. "
     "The costume does not hide the mechanism. Alex looks at the Villain with recognition."),

    (91, "BRAIN VILLAIN'S LAST TRICK",
     "Identifying the five programs does not turn them off.",
     "All five gear circuits in Alex's skull — still glowing, still running, after identification. "
     "Alex's expression: calm acceptance (not distress). The gears are not stopped by being named. "
     "This is honest and important. White background."),

    (92, "BRAIN VILLAIN'S LAST TRICK",
     "Your ancestors in an environment where anticipation meant survival.",
     "Simplified flat cartoon — ancient landscape: campfire, distant predator silhouette in trees. "
     "Ancestor figure (simplified Alex design, primitive clothing) with anticipation circuit "
     "glowing bright — spotting a threat early. The circuit was adaptive. Warm amber light."),

    (93, "BRAIN VILLAIN'S LAST TRICK",
     "Naming the predator did not make it stop moving.",
     "Same ancestor scene: thought bubble above ancestor — predator silhouette (the name). "
     "But predator still advancing from trees. Naming ≠ stopping. Visual parallel to "
     "knowing the bias but still experiencing it. Simple and clear."),

    (94, "BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain was built for that world. Not this one.",
     "Split panel: LEFT — Brain Villain in prehistoric setting, campfire glow, looking content "
     "and well-suited. RIGHT — same Brain Villain in modern city background, modern apartment "
     "icons, looking slightly out of place but still operational. The mismatch is visual."),

    # ── IDENTITY CLOSE ─────────────────────────────────────────────────────────────────────────
    (95, "IDENTITY CLOSE",
     "Next video: one decision. Set up on a calm Tuesday. No motivation required.",
     "Preview frame: calendar showing TUESDAY (circled, calm blue). A single clean transfer arrow "
     "icon. Alex pointing forward toward next video. Small '1 DECISION' text on the calendar "
     "(text IS the prop). Expression: forward-looking, calm."),

    (96, "IDENTITY CLOSE",
     "Alex in clean white space — neutral clear expression. No villain visible.",
     "Alex centered, clean white background, calm neutral expression — not triumphant, not worried. "
     "His skull is visible but circuits are quiet (dim, not dark). Brain Villain is present but "
     "subdued. This is clarity, not victory."),

    (97, "IDENTITY CLOSE",
     "The programs are not broken. They are perfectly designed for an environment where early signals meant survival.",
     "Campfire icon scene — ancestor with anticipation circuit, alert and alive. The circuit "
     "SAVED him then. Warm, humanizing light. The narrative: these programs were correct once. "
     "No judgment. Evolutionary context without drama."),

    (98, "IDENTITY CLOSE",
     "One structural decision bypasses all five.",
     "Clean bank diagram: one automatic transfer arrow — BANK ACCOUNT → SAVINGS. Single clean "
     "movement. The five gear circuits visible in a small inset corner, but the arrow bypasses "
     "all of them. Structural solution, not willpower. White background."),

    (99, "IDENTITY CLOSE",
     "One transfer. Set up once. Calendar arrow showing the same automatic monthly transfer firing.",
     "'1 TRANSFER. SET UP ONCE.' — text IS the prop (only two lines, factual). Calendar strip "
     "below showing Tuesday → automatic arrow → next month → automatic arrow → next month. "
     "The automation repeats without decision. Alex not present — the system runs without him."),

    (100, "IDENTITY CLOSE",
     "The Brain Villain is not defeated. It is bypassed.",
     "Brain Villain inside Alex's skull: reclining, asleep — not gone, not defeated. Gentle "
     "ZZZ sleep icon above the Villain. The transfer arrow circles outside the skull, bypassing "
     "the Villain entirely. The Villain sleeps while the system works. This is the hack."),

    (101, "IDENTITY CLOSE",
     "Alex calm. Arms crossed. Five circuits present but contained.",
     "Alex in confident pose — arms crossed, expression calm and knowing. Inside skull: all five "
     "circuits still glowing, but surrounded by a clean structural boundary (the automatic "
     "transfer system acts as a container). Circuits present, not stopped. Alex at peace with it."),

    (102, "IDENTITY CLOSE",
     "If your brain is doing this to you right now — subscribe.",
     "Alex large in frame, direct eye contact with viewer. Brain Villain tiny beside him — "
     "small, not defeated, just contextualized. Below: subscribe button icon clean and simple. "
     "Alex expression: warm and direct. White background."),

    (103, "IDENTITY CLOSE",
     "We break down a new bias every week. It is free. And it might save you more than you think.",
     "Neurocents channel end frame. Clean white background. Alex and Brain Villain side by side — "
     "Alex calm, Villain contained. Channel name visual (no specific logo needed — just 'NEUROCENTS' "
     "text as the prop, clean bold). Simple, memorable close."),

    (104, "IDENTITY CLOSE",
     "Next video: the one decision that bypasses all five programs.",
     "Preview card: forward arrow, TUESDAY calendar marker, single transfer icon. Alex pointing "
     "toward next video — expression: forward momentum. Curiosity gap: what is the one decision? "
     "Viewer must come back. Clean white background. Text: '1 DECISION / NEXT' as prop."),
]

# ── PDF GENERATION ─────────────────────────────────────────────────────────────────────────────

TOTAL = len(BEATS)
CHUNK = 26

parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

# Build section start map
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

pdf_path = "/home/user/Claudeeee/V13_final_IMAGE_PROMPTS.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=16*mm, rightMargin=16*mm,
                        topMargin=15*mm, bottomMargin=15*mm)

flow = [
    Paragraph("NEUROCENTS · VIDEO 13", H2),
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
    flow.append(Paragraph(f"IMAGE PROMPTS — PART {pidx}/4  (Beats {a}–{b})", PART))

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
