#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'Why the Smartest People Make the Worst Financial Decisions' (Video 4 — Damasio / Iowa Gambling Task)."""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

STYLE = ("2D flat cartoon illustration, thick solid black outlines on every element, "
         "clean solid color fills, no gradients except soft warm ambient light. "
         "Recurring main character: large beige oval head with a transparent glass upper "
         "skull revealing a pink cartoon brain inside; small black dot eyes, thin neutral "
         "mouth, black spiky hair, muted blue t-shirt, gray pants. The brain is an expressive "
         "character with a smug villain default expression (heavy-lidded eyes, slight smirk, "
         "small teeth). Palette: beige skin, black hair, muted blue shirt, gray pants, pink "
         "brain (#E8A598), green dollar bills, red for X-marks and danger, white for "
         "diagram/infographic scenes, warm beige interiors with a soft oval ceiling "
         "spotlight, dark gray for void/loss scenes. Bold black diegetic text labels "
         "integrated into the scene. 16:9, 1280x720.")

# (segment, scene, camera, lighting, mood, action, video)
BEATS = [

# ── HOOK ──────────────────────────────────────────────────────────────────────

("Meet Elliot.",
 "Medium shot, white background. A clean-cut cartoon man — neat hair, button shirt, calm expression — stands centered. A small bold label below reads 'ELLIOT.' The main character's pink brain watches from the side, curious.",
 "Medium shot, centered", "Flat, white", "Calm introduction — no alarm yet",
 "Elliot figure standing; brain watching from the side",
 "Static. The name label 'ELLIOT' fades in beneath the figure. 2s."),

("He had everything.",
 "Wide shot, warm beige interior. Elliot stands in a well-furnished living room — bookshelves, a framed diploma, a smiling family photo on the wall. Everything is orderly and prosperous. Soft warm ceiling spotlight.",
 "Wide shot, warm interior", "Warm amber, soft ceiling spotlight", "Success established — baseline before the fall",
 "Elliot in prosperous living room; diploma, family photo",
 "Static. A gentle warm glow sweeps across the room. 3s."),

("A good job. A family. A reputation as one of the sharpest people in the room.",
 "Medium shot of Elliot at an office desk, colleagues leaning in to listen. A thought-bubble above shows a diploma, a house, and a smiling family icon. Expression confident and composed. Warm office light.",
 "Medium shot, office setting", "Flat, warm office light", "Competence established — the fall will be earned",
 "Elliot at desk with admiring colleagues; achievement thought bubble",
 "Static. The thought bubble icons glow briefly one by one. 3s."),

("And then a tumor.",
 "Close-up of a flat medical scan image — a dark silhouette of a brain with a small red mass visible in the front-left area. Bold black text appears beside it: 'TUMOR.' The background is clinical white.",
 "Close-up, centered", "Clinical white, red highlight on tumor", "Sudden interruption — the turn comes fast",
 "Brain scan with red tumor mass; bold label",
 "Static. 'TUMOR.' drops in with a hard cut; the red mass pulses once. 2s."),

("The surgeons removed it successfully.",
 "Medium shot of an operating theater — simple flat scene, two surgeon figures in scrubs leaning over a table. A green checkmark floats above. Clean, clinical tones.",
 "Medium shot, overhead-leaning", "Clinical white, green checkmark highlight", "Relief — the surgery worked",
 "Surgeons in OR; green checkmark floating above",
 "Static. The green checkmark pulses once. 2s."),

("His IQ was intact.",
 "Wide diagram on white. A horizontal IQ bar sits at 'ABOVE AVERAGE' — fully filled, green. A bold label: 'INTELLIGENCE: INTACT.' The brain character stands beside it, arms crossed, satisfied.",
 "Wide diagram shot", "Flat, white", "Reassurance — the mind appears fine",
 "Full green IQ bar; brain character satisfied",
 "Static. The bar fills from left to right; label appears. 2s."),

("His memory was intact.",
 "Wide diagram on white. A second bar labeled 'MEMORY: INTACT' — fully filled, blue. Clean and symmetrical with the IQ bar above.",
 "Wide diagram shot", "Flat, white", "Continued reassurance — accumulating normality",
 "Full blue memory bar beneath IQ bar",
 "Static. The memory bar fills; both bars glow softly. 2s."),

("His language. His perception. His reasoning. All intact.",
 "Wide diagram with four green bars stacked — LANGUAGE, PERCEPTION, REASONING, LOGIC — all full. A bold headline: 'ALL NORMAL.' The brain character gives a thumb-up on the side.",
 "Wide stacked diagram", "Flat, white", "Full normalcy — before the twist lands",
 "Four full green bars; brain character thumb-up",
 "Static. Bars fill one by one in sequence; 'ALL NORMAL.' appears last. 3s."),

("But Elliot could not make a decision.",
 "Medium shot of Elliot at his desk, staring blankly at two pieces of paper side by side — a simple A/B choice. His expression is empty. A clock on the wall ticks. The brain inside his skull sits still, dim, disengaged.",
 "Medium shot", "Flat, warm office, clock ticking", "The rupture — quiet and disorienting",
 "Elliot frozen before two choices; dim brain; ticking clock",
 "Slow zoom in. The clock hand ticks visibly; Elliot does not move. 3s."),

("Not big decisions. Any decision.",
 "Wide shot, split panel on white. Left: Elliot staring at a restaurant menu, frozen. Right: Elliot staring at two nearly identical appointment slots on a calendar, equally frozen. Label centered: 'ANY DECISION.'",
 "Wide split panel", "Flat, white", "Scale collapse — the dysfunction is total",
 "Frozen Elliot at menu / frozen Elliot at calendar; label",
 "Static. Both panels appear; 'ANY DECISION.' fades in between them. 3s."),

("He could spend hours deciding where to eat.",
 "Medium shot of Elliot at a café counter, staring at a simple menu board with only three items. A thought bubble above cycles between the three options in an endless loop — sandwich, salad, soup, sandwich, salad... A clock in the corner shows hours passing.",
 "Medium shot", "Flat, warm café tones", "Absurdity that is also tragedy — the paradox is visible",
 "Elliot cycling options endlessly; clock advancing",
 "Animated. The thought bubble rotates through the three food items repeatedly; the clock hands advance noticeably. 3s."),

("He lost his job. His marriage. His savings.",
 "Wide shot, dark gray void background. Three faded icons fall away from Elliot in sequence: a briefcase (job), a wedding ring (marriage), a stack of coins (savings). Elliot stands in the center, expression flat, unmoved.",
 "Wide shot, void background", "Dark gray, muted", "Loss accumulates — but no emotion shows",
 "Three loss icons falling away from Elliot; flat expression",
 "Static. Icons drop one at a time from Elliot's silhouette. 3s."),

("And the strangest part — he knew all of this was happening.",
 "Medium shot of Elliot at a table with a doctor figure. Elliot describes his situation calmly, pointing to a diagram of his own life's collapse on a piece of paper. Expression: clinical, detached, almost academic. Doctor looks puzzled.",
 "Medium shot", "Flat, warm neutral", "Knowing without feeling — the core of the paradox",
 "Elliot describing his collapse calmly; puzzled doctor",
 "Static. Elliot gestures at the diagram; doctor leans forward. 2s."),

("He could describe, in perfect detail, why each of his decisions had been a mistake.",
 "Close-up of Elliot's face — calm, analytical, no distress. A thought bubble contains a clear diagram of bad-decision logic with arrows, labels, and annotations. Everything is logical and correct. The brain inside his skull looks bright but oddly cold.",
 "Close-up", "Flat, white", "Intelligence without wisdom — the distinction made visible",
 "Elliot's calm face; logical thought diagram; cold bright brain",
 "Static. The thought diagram fills in detail; brain glows a cool blue, not warm pink. 2s."),

("He just could not stop making them.",
 "Wide shot, white background. A timeline of Elliot's bad decisions stretches across the scene — each marked with a small red X. The sequence loops: decision, X, decision, X. Elliot walks the timeline, pointing at each X calmly.",
 "Wide shot, timeline layout", "Flat, white", "The trap — endless, calm, and incomprehensible",
 "Elliot walking timeline of red-X decisions calmly",
 "Static. Red X marks appear one after another along the timeline; Elliot gestures to each. 3s."),

# ── DAMASIO ────────────────────────────────────────────────────────────────────

("In 1991, a neurologist at the University of Iowa noticed something that did not fit any existing model.",
 "Wide establishing shot of the University of Iowa campus — flat cartoon exterior, a sign reading 'UNIVERSITY OF IOWA — DEPT. OF NEUROLOGY.' A single figure in a white coat walks toward the entrance. Warm exterior light.",
 "Wide establishing shot", "Warm exterior light", "A new mind enters — unhurried, precise",
 "Iowa campus exterior; lone neurologist figure approaching",
 "Static. The figure takes a measured step forward; sign legible and prominent. 2s."),

("His name was Antonio Damasio.",
 "Medium shot. A cartoon Damasio figure — white coat, calm confident expression, salt-and-pepper hair — stands in a research lab surrounded by brain scan images on a light board. Bold label: 'ANTONIO DAMASIO.'",
 "Medium shot, lab setting", "Flat, cool lab light", "The protagonist arrives — authority without arrogance",
 "Damasio in lab; brain scans on light board; name label",
 "Static. Name label fades in. The brain scans glow softly. 2s."),

("He had been studying patients like Elliot — people with damage to a specific region of the prefrontal cortex.",
 "Wide diagram on white. A cartoon brain outline highlights a front-left region in orange: 'vmPFC — VENTROMEDIAL PREFRONTAL CORTEX.' Arrows point to a cluster of patient icons. Damasio figure stands beside the diagram.",
 "Wide diagram shot", "Flat, white, orange highlight", "Medical precision — the lesion is pinned",
 "Brain diagram with vmPFC highlighted; patient icons; Damasio",
 "Static. Orange highlight pulses once; arrows appear. 3s."),

("These patients had perfectly normal cognitive function — by every standard test.",
 "Wide stacked diagram, echoing the earlier Elliot bars: IQ, MEMORY, LANGUAGE, REASONING — all green and full. Label: 'STANDARD TESTS: NORMAL.' Damasio stands beside it, expression focused.",
 "Wide stacked diagram", "Flat, white", "The diagnostic puzzle — nothing should be wrong",
 "Full green bars; 'STANDARD TESTS: NORMAL' label; Damasio",
 "Static. Bars present from the start; Damasio taps the label. 2s."),

("And yet, every one of them was unable to function in daily life.",
 "Wide shot, void background. A row of small cartoon figures — all styled like Elliot — stand paralyzed, each facing a simple fork-in-the-road decision symbol. None moves. Red X marks float above each.",
 "Wide shot, void background", "Dark gray void, red X marks", "Universal — this is a pattern, not an exception",
 "Row of paralyzed figures; decision forks; red X marks",
 "Static. Figures present; red X marks drop in above each. 3s."),

("Damasio had a hypothesis.",
 "Medium shot of Damasio at a chalkboard, drawing a simplified diagram with an arrow from 'BODY' to 'BRAIN.' He taps the arrow with conviction. Expression intense and still.",
 "Medium shot", "Flat, warm neutral", "The idea forming — quiet certainty",
 "Damasio at chalkboard; BODY→BRAIN arrow; tapping",
 "Static. Damasio's chalk arrow is already drawn; he taps it once. 2s."),

("Emotion was not the enemy of rational decision-making.",
 "Wide shot, white background. A bold statement is written across the scene: 'EMOTION ≠ ENEMY OF REASON.' A large red X strikes through an older equation that said 'EMOTION → BAD DECISIONS.'",
 "Wide shot", "Flat, white", "The paradigm flipped — clean and declarative",
 "Bold equation; red X through old model",
 "Static. The red X draws through the old equation; new statement fades in below. 3s."),

("Emotion was the engine of it.",
 "Wide shot, white background. A large flat engine diagram — but instead of mechanical parts, the fuel source is labeled 'EMOTION' in bold warm red. Arrows flow from EMOTION → PROCESSING → DECISION. Clean infographic style.",
 "Wide diagram shot", "Flat, white, warm red fuel source", "Reframe completes — the engine metaphor lands",
 "Engine diagram with EMOTION as fuel; arrows to DECISION",
 "Static. Arrows appear in sequence; 'EMOTION' fuel glows. 3s."),

# ── THE IOWA GAMBLING TASK ─────────────────────────────────────────────────────

("To prove it, his team designed one of the most elegant experiments in the history of neuroscience.",
 "Wide shot. A flat lab table holds four decks of cards labeled A, B, C, D. Two chairs face each other. A simple clean setup — nothing elaborate. Soft lab light. Label: 'IOWA GAMBLING TASK · 1994.'",
 "Wide shot, lab table", "Flat, cool lab light", "Anticipation — the experiment is introduced simply",
 "Four card decks on table; IGT label; clean setup",
 "Static. The four decks are crisp and labeled; the IGT date label fades in. 3s."),

("Four decks of cards on a table.",
 "Close-up overhead of the four decks labeled A, B, C, D — each deck a distinct color: A and B in warm red tones, C and D in cool blue tones. No other information shown. The choice is pure.",
 "Close-up, overhead", "Flat, overhead light", "Simplicity — the game is the thing",
 "Four labeled decks overhead; A/B red, C/D blue",
 "Static. Decks crisp and labeled. 2s."),

("Each card you turn over either gives you money or takes it away.",
 "Medium shot of a cartoon hand turning a card. On one side: a green plus sign with a dollar bill. On the other: a red minus sign with a dollar bill leaving. Split reveal.",
 "Medium shot", "Flat, white", "The mechanic explained — gain or loss",
 "Hand turning card; green gain / red loss reveal",
 "Static. The card flips in two stages — gain side first, loss side second. 2s."),

("Decks A and B: high rewards — but even higher penalties.",
 "Wide diagram. Decks A and B sit on the left, each with a tall green reward bar and a taller red penalty bar beside it. The penalty clearly exceeds the reward. Label: 'NET: NEGATIVE.'",
 "Wide diagram shot", "Flat, white, red dominant", "Risk established — the trap is visible in data",
 "A/B decks with reward vs penalty bars; NET: NEGATIVE",
 "Static. Bars appear; 'NET: NEGATIVE' label drops in red. 3s."),

("Decks C and D: smaller rewards — but small, predictable penalties.",
 "Wide diagram. Decks C and D sit on the right, each with a modest green reward bar and a shorter red penalty bar. The reward clearly wins over time. Label: 'NET: POSITIVE.'",
 "Wide diagram shot", "Flat, white, green dominant", "The safe path — visible in contrast to the trap",
 "C/D decks with modest reward vs small penalty bars; NET: POSITIVE",
 "Static. Bars appear; 'NET: POSITIVE' label glows green. 3s."),

("The instructions told participants nothing about the structure of the decks.",
 "Medium shot of a participant figure sitting at the table, receiving a single instruction card. The instruction reads only: 'Try to win as much money as possible.' The deck structure is hidden. Expression neutral.",
 "Medium shot", "Flat, cool lab light", "Uncertainty — the player enters blind",
 "Participant with minimal instruction card; decks face-down",
 "Static. The instruction card is presented; deck tops are blank. 2s."),

("They were simply told: try to win as much money as possible.",
 "Close-up on the instruction card — 'TRY TO WIN AS MUCH MONEY AS POSSIBLE.' Bold black text on white. Clean. No hints.",
 "Close-up, centered", "Flat, white", "The goal stated — nothing else given",
 "Instruction card close-up; single bold directive",
 "Static. The text is crisp and prominent. 2s."),

("Here is what happened with normal participants.",
 "Wide shot. A timeline across the white background showing a normal participant's card-selecting sequence. Early choices scattered across A, B, C, D. Over time the choices cluster toward C and D. A subtle green glow builds on the right side.",
 "Wide shot, timeline layout", "Flat, white", "Learning in action — the pattern emerges",
 "Participant choice timeline; gradual C/D clustering",
 "Static. Choices populate the timeline from left to right; green zone expands on C/D side. 3s."),

("By about the fiftieth card, most people had shifted toward decks C and D.",
 "Wide diagram. The card-50 mark is highlighted with a vertical line. Left of the line: scattered choices. Right of the line: clear clustering on C and D. A bold label: 'SHIFT AT ~50 CARDS.'",
 "Wide diagram shot", "Flat, white, green highlight on C/D", "The learning confirmed — the system worked",
 "50-card shift line; scattered left, clustered right; label",
 "Static. The shift line and label appear; C/D clustering glows. 2s."),

("They could not explain why.",
 "Medium shot of a participant figure sitting with the interviewer figure. Participant shrugs, expression genuinely uncertain. Thought bubble above: empty with a question mark. Label below: 'COULD NOT EXPLAIN.'",
 "Medium shot", "Flat, warm neutral", "Intuition without language — important detail",
 "Participant shrugging; empty thought bubble with question mark",
 "Static. The question mark in the thought bubble floats. 2s."),

("They just felt that C and D were safer.",
 "Medium shot. Participant figure reaches toward deck C confidently. Inside their chest — a simple flat heart icon glows warm. No text needed. Expression calm and certain without knowing why.",
 "Medium shot", "Flat, warm neutral, chest glow", "Felt knowledge — pre-verbal and certain",
 "Participant reaching for C/D; warm chest glow",
 "Static. The chest glow pulses once as the hand extends. 2s."),

# ── SOMATIC MARKERS ────────────────────────────────────────────────────────────

("Damasio's team added one instrument to the experiment.",
 "Wide shot of the lab table. An additional flat device sits beside the participant — a simple skin conductance monitor with two electrode pads attached to the participant's fingers. Clean and minimal. Label: 'SKIN CONDUCTANCE MONITOR.'",
 "Wide shot", "Flat, cool lab light", "Instrument arrives — anticipation of the reveal",
 "Lab table with skin conductance monitor added; electrode labels",
 "Static. The monitor and electrode pads are crisp; label fades in. 2s."),

("A skin conductance sensor — measuring the body's stress response through the palms.",
 "Close-up of flat cartoon hands with electrode pads attached. A simple signal line traces from the pads to a monitor showing a readout. Bold label: 'PALM SWEAT = STRESS SIGNAL.'",
 "Close-up", "Flat, cool lab light", "Scientific precision — the tool is explained",
 "Hands with electrodes; signal line to monitor; label",
 "Static. Signal line pulses gently on the monitor. 2s."),

("What they found was extraordinary.",
 "Medium shot of Damasio and a colleague leaning over data printouts at a table. Both look at the same page. Damasio's expression: the specific stillness of someone who has just seen something they cannot yet fully explain.",
 "Medium shot", "Flat, warm lab light", "The discovery moment — contained excitement",
 "Damasio and colleague over data; expression of quiet discovery",
 "Static. Both figures lean slightly over the data. 2s."),

("Normal participants' palms began to sweat when they reached toward decks A or B —",
 "Wide shot. Participant figure extends hand toward deck A. The skin conductance line on the monitor spikes upward — bold red peak. The hand hesitates mid-reach. The participant's expression shows no conscious alarm.",
 "Wide shot", "Flat, lab light, red spike on monitor", "The body knew — before the mind did",
 "Hand reaching toward A; monitor spike; hesitating hand",
 "Static. The monitor line spikes as the hand nears deck A. 3s."),

("before they had consciously identified A and B as dangerous.",
 "Close-up split panel. Left: the participant's palm with sweat droplets visible on the sensor. Right: a thought bubble — still empty, no conscious realization yet. Bold connecting label: 'BODY KNEW FIRST.'",
 "Close-up split panel", "Flat, white", "The sequence is the key insight",
 "Sweating palm / empty thought bubble; BODY KNEW FIRST label",
 "Static. Label appears between the two panels. 3s."),

("The body was generating a warning signal ten seconds before conscious awareness.",
 "Wide diagram. A horizontal timeline. At left: a bold red dot labeled 'BODY SIGNAL.' Ten seconds to the right: a smaller blue dot labeled 'CONSCIOUS AWARENESS.' The gap between them is wide and bracketed.",
 "Wide diagram shot", "Flat, white", "The temporal gap — made spatial and visible",
 "Timeline with body signal 10s before conscious awareness",
 "Static. The body signal dot appears first; then the awareness dot; bracket locks the gap. 3s."),

("Damasio called these signals somatic markers.",
 "Medium shot of Damasio at a chalkboard. He writes in bold: 'SOMATIC MARKERS.' Below it, a simple diagram: body → signal → decision path. Expression calm and certain.",
 "Medium shot", "Flat, warm neutral", "The naming — the concept crystallizes",
 "Damasio writing SOMATIC MARKERS at chalkboard; signal diagram",
 "Static. The term is bold and prominent; diagram arrows appear. 2s."),

("Soma — body. Marker — a tag, a flag, a signal embedded in a memory.",
 "Wide diagram on white. Two definitions side by side: 'SOMA = BODY' in warm earth tones, 'MARKER = SIGNAL TAG' in cool blue. Arrows merge toward a central icon: a simple flag planted in a memory timeline.",
 "Wide diagram shot", "Flat, white, dual tones", "Etymology as clarity — the concept becomes concrete",
 "Two definitions merging into signal-flag icon on memory timeline",
 "Static. Definitions appear; arrows merge to central icon. 3s."),

("Every significant experience you have ever had left a somatic trace in your nervous system.",
 "Wide shot, beige interior. The main character stands in a corridor of floating memory images — each memory has a small colored marker attached: a red flag for danger, a green flag for safety, a yellow flag for uncertainty.",
 "Wide shot, corridor of memories", "Flat, warm beige corridor", "Scale of the system — lifelong, continuous",
 "Character in corridor of flagged memories; red, green, yellow markers",
 "Static. Memory images and flags glow softly. The corridor recedes into depth. 3s."),

("A bad deal that cost you. A relationship that harmed you. A time you ignored a warning and paid for it.",
 "Wide shot, three panels. Panel 1: character looking at a crumpled contract with a red flag. Panel 2: character at a distance from a shadowy departing figure, red flag. Panel 3: character walking past a warning sign, yellow flag, with red aftermath visible beyond.",
 "Wide triptych", "Flat, muted warning tones", "Personal — the viewer maps their own experiences",
 "Three panels: bad deal, harmful relationship, ignored warning — each with markers",
 "Static. Panels appear in sequence; flags are prominent. 3s."),

("Each one left a marker.",
 "Close-up of a single memory icon with a bold red flag planted firmly beside it. The flag reads 'MARKER.' Clean, final.",
 "Close-up, centered", "Flat, white", "Distillation — the concept at its simplest",
 "Single memory icon with bold MARKER flag",
 "Static. Flag is crisp and prominent. 2s."),

("When a similar situation appears in your future, the marker fires before you think.",
 "Wide shot. The main character stands at a decision point. An identical-looking situation to one of the bad deals appears. Before the character's thought bubble activates — a red flash fires from the chest outward. Fast, silent, automatic.",
 "Wide shot", "Flat, white, red chest flash", "Speed of the system — pre-cognitive and involuntary",
 "Character at decision point; red marker fires from chest before thought bubble",
 "Static. Red flash appears before thought bubble opens. 2s."),

("You feel reluctant. Uneasy. You want to leave.",
 "Medium shot of the main character facing a salesperson figure. The main character's body language: leaning back, arms slightly closed. The pink brain inside the skull is sending small red pulses downward to the chest. The character hasn't thought — the body is already retreating.",
 "Medium shot", "Flat, warm neutral", "Felt experience — the viewer recognizes this",
 "Character leaning back from salesperson; brain sending red chest pulses",
 "Static. Red pulses descend from brain to chest. 2s."),

("That feeling is not noise.",
 "Close-up, white background. Bold text: 'THAT FEELING IS NOT NOISE.' The main character's transparent skull shows the brain pointing directly at the viewer, expression firm.",
 "Close-up, direct address", "Flat, white", "Authority — the key reframe stated plainly",
 "Bold text; brain pointing at viewer",
 "Static. Text and brain hold steady; direct address. 2s."),

("It is a compressed record of every relevant experience your nervous system has ever filed away.",
 "Wide shot. A giant flat filing cabinet occupies the right side of the frame. Dozens of memory-file folders with colored markers extend from the drawers. The main character stands to the left, connected to the cabinet by a simple signal line.",
 "Wide shot", "Flat, white", "The system made visible — vast but organized",
 "Character connected by signal line to massive memory filing cabinet",
 "Static. Signal line pulses once from character to cabinet. 3s."),

# ── ELLIOT REVISITED ───────────────────────────────────────────────────────────

("Now go back to Elliot.",
 "Medium shot. Elliot figure returns — center frame, same clean-cut appearance, same blank expression. But now the viewer knows what's missing. A simple diagram floats behind him: the body-to-brain signal path, with the body-to-brain arrow cut by a dashed red line.",
 "Medium shot", "Flat, white", "Return with new knowledge — the tragedy is now understood",
 "Elliot figure with broken body-brain signal diagram behind him",
 "Static. The broken signal arrow is prominent; red dashes hold steady. 3s."),

("The tumor and surgery had severed the connection between his vmPFC and his body's signaling system.",
 "Wide diagram. A cartoon brain outline. The vmPFC region is highlighted. A signal path runs from the vmPFC downward to a body outline. The path is cut — a bold red X across the connection. Label: 'SIGNAL SEVERED.'",
 "Wide diagram shot", "Flat, white, red highlight on severed path", "The mechanism of Elliot's tragedy — precise and visual",
 "Brain diagram with vmPFC→body path severed; red X; label",
 "Static. The red X appears on the signal path; label drops in. 3s."),

("Elliot could reason perfectly. He simply could not feel the answer.",
 "Close-up split panel. Left: a perfectly organized logical diagram in Elliot's thought bubble — all correct, all rational. Right: the body signal path — flat, dark, no signal. Label bridging: 'REASON WITHOUT FEEL.'",
 "Close-up split panel", "Flat, white", "The exact deficit — articulated finally",
 "Logical thought bubble vs. flat body signal; REASON WITHOUT FEEL label",
 "Static. Both panels present; label appears between them. 3s."),

("When he faced a decision, the somatic markers that should have pre-filtered the options — pointed him toward the safe choice before analysis began — simply did not fire.",
 "Wide shot of Elliot at the decision table. Four options in front of him — all identical in appearance to his brain. No red flags. No green flags. No markers at all. His thought bubble opens to a flat gray screen — equal probability assigned to everything.",
 "Wide shot", "Flat, cool gray", "Equal gray — no guidance, no pre-filter",
 "Elliot at table; four blank options; empty gray thought bubble",
 "Static. All options remain equal; no markers appear; thought bubble stays gray. 3s."),

("Without markers, every option looked equally valid.",
 "Wide shot. All four options expand into equal-height gray bars. No differentiation. Elliot's expression: genuinely vacant, not lazy — there is simply nothing to choose from.",
 "Wide shot", "Flat, gray", "The cognitive desert — emptiness of equal weights",
 "Four identical gray option bars; vacant Elliot",
 "Static. Bars hold equal height; Elliot's expression remains neutral. 2s."),

("So he evaluated everything. For hours. And chose nothing.",
 "Wide shot. A clock on the wall advances rapidly. Elliot sits at the table surrounded by paper calculations — all equally valid analyses of each option. No decision circle is drawn anywhere. The brain inside his skull runs fast but goes nowhere.",
 "Wide shot", "Flat, warm, clock advancing", "Paralysis by infinite analysis — vivid and specific",
 "Elliot surrounded by calculations; clock advancing; brain spinning in place",
 "Static. Clock hands advance; papers multiply; no decision circle. 3s."),

# ── WHAT THE INDUSTRY KNOWS ───────────────────────────────────────────────────

("Now here is where this stops being a neuroscience lesson.",
 "Medium shot of the main character turning directly to face camera, expression shifting from analytical to direct. The brain inside the skull leans forward, smug expression returning. Background fades to flat white.",
 "Medium shot, direct address", "Flat, white", "Pivot — the practical application begins",
 "Character turning to camera; brain leaning forward, smug",
 "Static. Character turns; brain leans forward. 2s."),

("The industries that want your money — have known about somatic markers for decades.",
 "Wide shot, white background. A large bold statement: 'THEY KNOW.' Below it: a simple row of industry icons — a bank building, a phone screen, a retail storefront, a casino chip. Each icon has a small signal-targeting icon beside it.",
 "Wide shot", "Flat, white", "The frame shifts — from science to exploitation",
 "THEY KNOW statement; industry icons with targeting signals",
 "Static. Industry icons appear one by one; targeting signals lock on. 3s."),

("The field is called neuromarketing.",
 "Medium shot. A simple flat research setup — a participant in a chair wearing a simple biometric monitor. A corporate logo floats above. Label: 'NEUROMARKETING — the study of how the brain responds to commercial stimuli.'",
 "Medium shot", "Flat, cool lab light", "Named and real — no conspiracy, just science applied",
 "Neuromarketing research setup with participant and biometric monitor",
 "Static. Label appears; biometric readout pulses. 2s."),

("And its entire purpose is to engineer the somatic signal you feel before you think.",
 "Wide diagram. A consumer figure on the left. On the right: a product/service icon. Between them: a pipeline of engineered stimuli — color, sound, urgency, scarcity, social proof — each designed to fire a specific somatic marker. Label: 'ENGINEERED GUT FEELING.'",
 "Wide diagram shot", "Flat, white", "The mechanism exposed — deliberate and systematic",
 "Consumer ← stimulus pipeline ← product; ENGINEERED GUT FEELING label",
 "Static. Pipeline elements appear one by one; label drops in. 3s."),

("The countdown timer on the checkout page.",
 "Close-up of a flat checkout screen. A bold red countdown timer reads '00:07:43 — OFFER EXPIRES.' Below it, a faint heartbeat line pulses on the screen. The consumer's hand hovers over the 'BUY NOW' button.",
 "Close-up, screen", "Flat, white, red countdown highlight", "Familiar and specific — the viewer has seen this",
 "Checkout screen with countdown; hovering hand; heartbeat line",
 "Static. Countdown digits tick; hand hovers. 2s."),

("The 'Only 3 left in stock' label.",
 "Close-up of a product page. Bold label: 'ONLY 3 LEFT IN STOCK.' A small scarcity bar beneath it shows three remaining units in amber. Consumer figure leans in slightly, body tightening.",
 "Close-up", "Flat, white, amber scarcity", "Manufactured scarcity — somatic urgency engineered",
 "Product page with scarcity label; consumer leaning in",
 "Static. Scarcity label pulses; amber bar visible. 2s."),

("The one-click purchase button.",
 "Close-up of a large flat 'BUY NOW — ONE CLICK' button in bold orange. Frictionless. No confirmation. No pause. The consumer's hand is already moving before the brain thought bubble has opened.",
 "Close-up", "Flat, white, orange button", "Frictionlessness as design — pre-cognitive action engineered",
 "One-click BUY NOW button; hand moving before thought bubble opens",
 "Static. The button glows; hand is already moving. 2s."),

("None of these are accidental.",
 "Wide shot, white background. Three elements from the previous beats — countdown timer, scarcity label, one-click button — arranged in a row. A corporate strategy diagram connects them all to a single label: 'DESIGNED TO BYPASS COGNITION.'",
 "Wide shot", "Flat, white", "Intentionality made explicit — design, not accident",
 "Three elements connected to DESIGNED TO BYPASS COGNITION label",
 "Static. Connection lines appear; label drops in boldly. 3s."),

("They are all designed to fire a somatic signal — urgency, scarcity, social proof —",
 "Wide diagram. Three signal types in separate panels: URGENCY (red countdown), SCARCITY (amber bar), SOCIAL PROOF (crowd icon). Each fires an arrow directly toward a body outline's chest region.",
 "Wide triptych diagram", "Flat, white, warm signal colors", "The three weapons — named and visualized",
 "Three signal panels firing arrows at body chest; labeled triggers",
 "Static. Arrows appear from each trigger toward the body. 3s."),

("before your prefrontal cortex has a chance to evaluate.",
 "Wide shot. A flat brain diagram shows the prefrontal cortex region still dark — not yet activated. The body's chest signal is already firing. A clock shows: BODY SIGNAL at 0.0s, PFC ACTIVATION at 0.3s.",
 "Wide diagram shot", "Flat, white", "The timing is the weapon",
 "Brain diagram with PFC dark; body signal firing; timing clock",
 "Static. Body signal fires first; PFC region remains dark. 3s."),

("You feel the pull.",
 "Medium shot of the main character standing before a large glowing phone screen. The pull is visible — the character leans toward the screen slightly, the brain in the skull has temporarily lost its smug expression, replaced by a mild glazed fixation.",
 "Medium shot", "Flat, screen glow", "Vulnerability — even the smart character is caught",
 "Character leaning toward phone screen; brain glazed, not smug",
 "Static. Screen glow pulls character slightly forward; brain expression soft. 2s."),

("And by the time your brain's evaluation system catches up — you've already clicked.",
 "Wide shot. The character's finger is already on the 'CONFIRM PURCHASE' button. A small thought bubble floats slightly behind the action, still loading. Bold label: 'ALREADY CLICKED.'",
 "Wide shot", "Flat, white", "The sequence played out — recognition after the fact",
 "Character's finger on Confirm button; thought bubble loading behind",
 "Static. The thought bubble appears visibly after the finger is already down. 3s."),

# ── THE SMARTER PROBLEM ────────────────────────────────────────────────────────

("Here is the problem with being smart.",
 "Medium shot, direct address. The main character faces the camera, the brain inside the skull resuming its smug-but-slightly-wary expression. Expression: self-aware, not defensive.",
 "Medium shot, direct address", "Flat, white", "The knife twist — intelligence as vulnerability",
 "Character facing camera; brain self-aware expression",
 "Static. Direct address; brain holds expression. 2s."),

("Smarter people have more sophisticated reasoning systems.",
 "Wide diagram. A reasoning engine schematic — complex, multi-geared, elaborate. Label: 'HIGH-INTELLIGENCE REASONING SYSTEM.' Gears labeled: LOGIC, RATIONALIZATION, JUSTIFICATION, NARRATIVE-BUILDING.",
 "Wide diagram shot", "Flat, white", "The double-edged gift — made visible structurally",
 "Complex reasoning engine diagram; intelligence-labeled gears",
 "Static. Gear labels appear one by one. 3s."),

("Which means they are better at constructing post-hoc justifications for decisions the body already made.",
 "Wide shot. Consumer character has already clicked a purchase. The thought bubble — previously lagging — is now fully active, producing an elaborate logical chain: 'I needed this. The discount was significant. The timing was right. This is rational.' All arrows lead to: 'CONFIRMED.'",
 "Wide shot", "Flat, white", "The trap for the clever — more elaborate rationalizations",
 "Post-hoc justification chain flowing from already-made purchase",
 "Static. Justification chain appears in sequence; all arrows converge on CONFIRMED. 3s."),

("The emotion came first. The reasoning followed.",
 "Wide shot, split timeline. Left half: BODY SIGNAL fires (labeled EMOTION, t=0). Right half: REASONING begins (labeled LOGIC, t=+0.3s). A bold arrow points right: 'THIS IS ALWAYS THE SEQUENCE.'",
 "Wide split timeline", "Flat, white", "The universal sequence — no exceptions",
 "Emotion at t=0 / Logic at t+0.3s timeline; THIS IS ALWAYS THE SEQUENCE",
 "Static. Timeline appears; arrow and label drop in. 3s."),

("The intelligence was used to defend a somatic choice — not to make a rational one.",
 "Wide diagram. A courtroom metaphor — flat cartoon. The SOMATIC MARKER sits in the judge's chair, already decided. The reasoning system is the defense attorney, building a case for the judge's decision. Label: 'INTELLIGENCE AS DEFENSE ATTORNEY.'",
 "Wide diagram, courtroom metaphor", "Flat, white", "The structural role of intelligence — redefined",
 "Somatic marker as judge; reasoning as defense attorney; label",
 "Static. Courtroom scene crisp; label fades in. 3s."),

("This is why brilliant people get into terrible investments.",
 "Wide shot, three small scene panels. Panel 1: Suited professional signing an obviously bad contract, expression confident. Panel 2: Academic type buying into a scheme with elaborate printed justification in hand. Panel 3: Engineer making a leveraged bet with color-coded spreadsheet.",
 "Wide triptych", "Flat, warm professional tones", "The universality — the smart trap is a human trap",
 "Three panels: professional, academic, engineer in bad financial decisions",
 "Static. Panels appear; each figure holds their rationalization artifact. 3s."),

("The somatic marker fires — excitement, prestige, the feeling of being the one who saw it first.",
 "Wide diagram. The same three figures, but now with their somatic signals shown — each fires an arrow from chest to decision. Signal labels: EXCITEMENT, PRESTIGE, EXCLUSIVITY. The decisions are already made.",
 "Wide diagram shot", "Flat, white", "The actual mechanism — the somatic signals named",
 "Three figures with named somatic signals firing to decisions",
 "Static. Signal arrows and labels appear. 3s."),

("And then the intelligence goes to work — justifying.",
 "Wide shot. The elaborate reasoning machines from before activate behind each figure, building justification towers above each decision. Each tower is tall, ornate, logical-looking. And completely post-hoc.",
 "Wide shot", "Flat, white", "The intelligence trap complete — the more clever, the higher the tower",
 "Three justification towers above decisions; reasoning machines active",
 "Static. Towers build upward from the decisions. 3s."),

# ── THE REFRAME ────────────────────────────────────────────────────────────────

("So what do you do with this?",
 "Medium shot of the main character, direct address, hands open — not defensive, genuinely asking with the viewer.",
 "Medium shot, direct address", "Flat, white", "Open question — brings the viewer in",
 "Character with open hands, direct address",
 "Static. Character holds the open-handed pose. 2s."),

("The answer is not to stop trusting your gut.",
 "Wide shot, white background. A large gut-signal icon in warm yellow — with a bold label: 'NOT THE ENEMY.' The main character stands beside it, one hand resting on the icon.",
 "Wide shot", "Flat, white, warm yellow gut signal", "Recalibration not rejection — the nuance",
 "Gut signal icon with NOT THE ENEMY label; character beside it",
 "Static. Label appears; character's hand rests on icon. 2s."),

("Damasio's patients without somatic markers couldn't function.",
 "Medium shot of the row of Elliot-type figures, frozen at decision forks, returning briefly to make the point. A single label: 'NO MARKERS = NO DECISIONS.'",
 "Medium shot", "Flat, dark gray", "The cost of the opposite extreme — no gut is not the answer",
 "Frozen Elliot-type figures; NO MARKERS = NO DECISIONS label",
 "Static. Figures frozen; label appears. 2s."),

("The answer is to audit the markers that are being engineered into you.",
 "Wide shot, white background. The main character stands with a clipboard — performing an audit of the engineered-signal pipeline from earlier. Each engineered trigger has a new overlay: a small magnifying glass icon. Label: 'AUDIT YOUR MARKERS.'",
 "Wide shot", "Flat, white", "The action — specific and practical",
 "Character auditing engineered signal pipeline with magnifying glass",
 "Static. Magnifying glass icons appear on each trigger. 3s."),

("When you feel urgency — ask who built that feeling.",
 "Medium shot. The countdown timer returns. But now the main character's brain has its smug expression back — and is pointing a finger at the timer. Thought bubble: 'WHO BUILT THIS?'",
 "Medium shot", "Flat, white, red timer", "Interrogating the trigger — the core habit",
 "Character's brain pointing at countdown timer; WHO BUILT THIS thought bubble",
 "Static. Brain points; thought bubble appears. 2s."),

("When you feel excitement about a financial opportunity — ask how that excitement was constructed.",
 "Wide shot. The investment scene returns — but now the character pauses before signing. The brain shows a flashlight beam scanning the deal structure, looking for the engineered signals: EXCLUSIVITY, URGENCY, SOCIAL PROOF.",
 "Wide shot", "Flat, white", "Pause before action — the new habit in practice",
 "Character scanning investment deal with flashlight; finding engineered signals",
 "Static. Flashlight scans; signal labels illuminate as found. 3s."),

("When you feel certain — ask when you last updated that certainty.",
 "Medium shot. The main character examines a mental-model card — a gut-certainty card with a date stamp: '2019.' Thought bubble: 'IS THIS STILL ACCURATE?' Expression: curious, not alarmed.",
 "Medium shot", "Flat, white", "Temporal audit — the gut must be maintained",
 "Character examining outdated certainty card; IS THIS STILL ACCURATE thought bubble",
 "Static. Date stamp prominent; thought bubble appears. 2s."),

("The gut is not always right.",
 "Wide shot, white. A gut-signal icon with a calibration dial below it. The dial is not at zero and not at maximum — it's in a calibration zone. Label: 'CALIBRATE — DON'T SILENCE.'",
 "Wide shot", "Flat, white", "Nuance — the takeaway is precise",
 "Gut signal icon with calibration dial; CALIBRATE label",
 "Static. Dial sits in calibration zone; label appears. 2s."),

("But it is the fastest decision system you have.",
 "Wide shot, speed comparison diagram. Three timing bars: CONSCIOUS REASONING (slow, wide bar), SOMATIC MARKER (fast, narrow bar), INSTINCT (fastest). The somatic bar is highlighted: 'FASTEST USEFUL SYSTEM.',",
 "Wide speed diagram", "Flat, white", "The value of the gut — confirmed in context",
 "Speed comparison bars; somatic marker highlighted as fastest useful",
 "Static. Bars appear in sequence; somatic marker bar highlighted. 3s."),

("And it was designed — by evolution and by your life — to protect you.",
 "Wide shot. The main character in a natural setting — a simple flat forest background. A somatic signal fires from the chest at a shadowy threat in the distance. The signal is fast and accurate. Label: 'BUILT TO PROTECT.'",
 "Wide shot, natural setting", "Flat, warm natural light", "Purpose of the system — protective and earned",
 "Character in forest; chest signal firing at threat; BUILT TO PROTECT label",
 "Static. Signal fires; label appears. 2s."),

("The problem is not the gut.",
 "Medium shot, direct address. The main character turns fully to camera. The brain inside the skull is alert, composed, smug-but-serious.",
 "Medium shot, direct address", "Flat, white", "Building to the channel mission",
 "Character facing camera; brain alert and composed",
 "Static. Direct address. 2s."),

# ── CHANNEL MISSION ────────────────────────────────────────────────────────────

("The problem is the hacking of the gut.",
 "Wide shot, white background. A large gut-signal icon — but now it has a hacker figure standing behind it, attaching engineered signal wires to the back. Label: 'THE GUT — HACKED.'",
 "Wide shot", "Flat, white", "The central thesis stated — the channel's reason for existing",
 "Gut signal icon with hacker figure attaching wires; THE GUT HACKED label",
 "Static. Hacker figure and wires appear; label drops in. 3s."),

("And the hack is not new. And it is not stopping.",
 "Wide timeline on white. A long horizontal line marked with decades: 1950s, 1970s, 1990s, 2010s, NOW. At each mark: a small icon of a different industry — advertising, payday lending, social media, algorithmic feeds. All targeting the same gut signal.",
 "Wide timeline shot", "Flat, white", "Historical scope — the viewer understands the scale",
 "Decade timeline with industry icons targeting gut signal across eras",
 "Static. Timeline populates from left to right; industry icons appear at each mark. 3s."),

("Elliot knew which decks were bad.",
 "Medium shot. Elliot returns — seated at the Iowa Gambling Task table. He looks at decks A and B, then at C and D. In his thought bubble, a correct diagram: A/B = NEGATIVE, C/D = POSITIVE. The knowledge is there.",
 "Medium shot", "Flat, warm neutral", "The tragic knowledge — the punchline arrives",
 "Elliot at IGT table; correct knowledge in thought bubble",
 "Static. Thought bubble shows correct deck assessment. 2s."),

("He just couldn't feel it.",
 "Close-up of Elliot's chest region. The body signal path is flat — dark, quiet, no pulse. The knowledge floats above unused. Bold label: 'COULDN'T FEEL IT.'",
 "Close-up", "Flat, dark", "The gap made physical — the tragedy of Elliot",
 "Flat dark chest signal beneath correct knowledge; COULDN'T FEEL IT label",
 "Static. Signal path remains flat; label appears. 2s."),

("You still can.",
 "Medium shot of the main character — direct address. Expression: calm, direct, not inspirational in a cheap way — just true. The brain inside the skull has a quiet, alert expression. The chest signal pulses once — warm, steady, present.",
 "Medium shot, direct address", "Flat, white, warm chest pulse", "The offer — delivered with economy",
 "Character with direct expression; steady warm chest pulse",
 "Static. Chest pulse fires once; character holds eye contact. 2s."),

("Every video on this channel is one way your financial gut has been hacked.",
 "Wide shot, white background. A bold visual: the channel's thematic frame. A row of labeled signal-hack icons stretches across the scene, each representing a future video concept: dopamine, bandwidth, somatic markers, loss aversion, social comparison. Above them all: the main character, clipboard in hand.",
 "Wide shot", "Flat, white", "Channel mission declared — the viewer understands what they are subscribing to",
 "Row of hack icons; character with clipboard above; channel frame established",
 "Static. Icons appear one by one; character stands above the row. 3s."),

("And what you can do about it.",
 "Medium shot. The main character turns from the clipboard to the camera. The brain inside the skull has a composed, focused expression. A simple bold label appears beside the character: 'AND WHAT YOU CAN DO ABOUT IT.'",
 "Medium shot", "Flat, white", "The mission complete — both the problem and the agency",
 "Character turning from clipboard to camera; mission label beside",
 "Static. Character turns; label appears. 2s."),

]  # end BEATS


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    TITLE = "Why the Smartest People Make the Worst Financial Decisions"
    SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 4"
    LABEL = "STATE 5 — PRODUCTION DOCUMENT (FULL BEAT SHEET)"

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run(SUBTITLE)
    r.bold = True
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run(LABEL)
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run(TITLE)
    r.bold = True
    r.italic = True
    r.font.size = Pt(16)

    doc.add_paragraph()

    HEADERS = [
        "HOOK",
        "DAMASIO",
        "THE IOWA GAMBLING TASK",
        "SOMATIC MARKERS",
        "ELLIOT REVISITED",
        "WHAT THE INDUSTRY KNOWS",
        "THE SMARTER PROBLEM",
        "THE REFRAME",
        "CHANNEL MISSION",
    ]
    SECTION_STARTS = {
        1: "HOOK",
        17: "DAMASIO",
        26: "THE IOWA GAMBLING TASK",
        38: "SOMATIC MARKERS",
        52: "ELLIOT REVISITED",
        59: "WHAT THE INDUSTRY KNOWS",
        73: "THE SMARTER PROBLEM",
        82: "THE REFRAME",
        93: "CHANNEL MISSION",
    }

    COL_LABELS = ["#", "SEGMENT (NARRATION)", "IMAGE PROMPT", "CAMERA", "LIGHTING",
                  "MOOD / TONE", "CHARACTER ACTION", "VIDEO MOTION"]
    COL_WIDTHS = [Inches(0.35), Inches(1.7), Inches(2.5), Inches(0.9), Inches(0.8),
                  Inches(1.0), Inches(1.0), Inches(1.25)]

    tbl = doc.add_table(rows=1, cols=8)
    tbl.style = 'Table Grid'
    hdr = tbl.rows[0].cells
    for i, (label, width) in enumerate(zip(COL_LABELS, COL_WIDTHS)):
        hdr[i].width = width
        p = hdr[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(label)
        run.bold = True
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        hdr[i]._tc.get_or_add_tcPr()
        from docx.oxml.ns import qn
        from docx.oxml import OxmlElement
        shading = OxmlElement('w:shd')
        shading.set(qn('w:val'), 'clear')
        shading.set(qn('w:color'), 'auto')
        shading.set(qn('w:fill'), '2C3E50')
        hdr[i]._tc.get_or_add_tcPr().append(shading)

    for beat_num, beat in enumerate(BEATS, 1):
        seg, scene, cam, light, mood, action, video = beat

        if beat_num in SECTION_STARTS:
            sec_row = tbl.add_row()
            sec_cell = sec_row.cells[0]
            sec_cell.merge(sec_row.cells[7])
            p = sec_cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(f"── {SECTION_STARTS[beat_num]} ──")
            run.bold = True
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            sec_cell._tc.get_or_add_tcPr()
            from docx.oxml.ns import qn
            from docx.oxml import OxmlElement
            shading = OxmlElement('w:shd')
            shading.set(qn('w:val'), 'clear')
            shading.set(qn('w:color'), 'auto')
            shading.set(qn('w:fill'), 'B02A2A')
            sec_cell._tc.get_or_add_tcPr().append(shading)

        row = tbl.add_row()
        cells = row.cells
        for i, width in enumerate(COL_WIDTHS):
            cells[i].width = width

        def cell_text(cell, text, bold=False, sz=9, color=None):
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.bold = bold
            run.font.size = Pt(sz)
            if color:
                run.font.color.rgb = color

        cell_text(cells[0], str(beat_num), bold=True, sz=9, color=RGBColor(0x99, 0x99, 0x99))
        cell_text(cells[1], seg, bold=True, sz=9)
        cell_text(cells[2], scene, sz=8)
        cell_text(cells[3], cam, sz=8)
        cell_text(cells[4], light, sz=8)
        cell_text(cells[5], mood, sz=8)
        cell_text(cells[6], action, sz=8)
        cell_text(cells[7], video, sz=8)

    all_lines = [b[0] for b in BEATS]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = len(BEATS)

    doc.add_paragraph()
    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(
        f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min narration")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Iowa_Gambling_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
