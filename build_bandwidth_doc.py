#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'The Bandwidth Tax' (Video 3 — financial scarcity and cognitive load)."""

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

("Here is a question that will change how you see poverty.",
 "Medium shot, white background. The main character faces camera directly, one eyebrow slightly raised. Inside the transparent skull the pink brain leans forward, intrigued. A single bold question mark floats beside the character's head.",
 "Medium shot, centered, direct address", "Flat, white", "Quiet provocation — the hook lands before the question is stated",
 "Character facing camera; brain leaning forward; question mark floating",
 "Static. The question mark pulses once gently; the brain leans a hair further forward. 2s."),

("Two people walk into a lab at Princeton University.",
 "Wide establishing shot of a clean flat university corridor leading to a lab door marked 'PRINCETON UNIVERSITY — RESEARCH LAB.' Two small cartoon figures — one in casual clothes, one in a jacket — walk toward the door side by side. Cool institutional gray-white tones.",
 "Wide establishing shot, slight low angle", "Flat, cool institutional white", "Neutral, clinical — the setup arrives",
 "Two figures walking toward the lab door",
 "Static. The two figures take a few small steps closer to the door; the lab sign is crisp and legible. 3s."),

("Same table. Same test. Same questions.",
 "Close-up of a flat white table surface with two identical test booklets side by side, two identical pencils, two identical chairs. A bold centered label reads 'SAME TABLE · SAME TEST · SAME QUESTIONS.' Perfectly symmetrical.",
 "Close-up, overhead view", "Flat, white", "Controlled equality — the experiment is rigorous",
 "Static symmetrical arrangement; label prominent",
 "Static. The label fades in word by word. 2s."),

("One scores like a person of above-average intelligence.",
 "Medium shot of a flat answer sheet. The left half of the sheet shows a near-perfect row of filled circles with a bold green score: '113 IQ equivalent' at the top. The character's hand holds it, relaxed. White background.",
 "Medium shot, centered", "Flat, white, soft green score highlight", "Confident result — baseline established",
 "Near-perfect answer sheet with green score label",
 "Static. The green score label pulses softly once. 2s."),

("The other scores like someone who hasn't slept in 24 hours.",
 "Medium shot of an identical answer sheet, but now riddled with uncertain marks and erasures. A bold red score reads '100 IQ equivalent' at the top. A small inset icon of a tired eye underscores the comparison. White background.",
 "Medium shot, centered", "Flat, white, soft red score highlight", "Deflation — the gap is made visible",
 "Incomplete answer sheet with red score label; tired-eye icon",
 "Static. The red score label appears with a slight drop-in; the tired-eye icon blinks slowly. 2s."),

("They are the same person.",
 "Stark medium shot on white. Two identical character outlines stand side by side, perfectly mirrored. A bold black equals sign connects them. Below it: 'SAME PERSON.' Simple, clean, shocking.",
 "Medium shot, centered", "Flat, white", "Revelation — simple and disorienting",
 "Two identical figures with equals sign",
 "Static. The 'SAME PERSON.' label slides in from below; the equals sign holds steady. 2s."),

("The only thing the researchers changed was a thought experiment about money.",
 "Wide shot, white background. A simple split panel: left side shows the character's head with a calm empty thought bubble; right side shows the same head with a thought bubble filled with a bold dollar sign and a worried expression. Label: 'THE ONLY CHANGE.'",
 "Wide split panel", "Flat, white", "One variable — pinned precisely",
 "Empty thought bubble vs. money-filled thought bubble",
 "Static. The dollar-sign thought bubble fills in on the right; left stays empty. 2s."),

("For half the group: imagine a minor car repair. Three hundred dollars.",
 "Medium shot. The character stands thinking; thought bubble shows a cartoon car with a small wrench and a price tag reading '$300' in calm green text. Expression neutral, relaxed. White background.",
 "Medium shot", "Flat, white", "Low stakes — the control condition",
 "Calm thought bubble with car and $300 tag",
 "Static. The $300 tag swings gently in the thought bubble. 2s."),

("For the other half: a major car repair. Three thousand dollars.",
 "Medium shot. Same character pose but thought bubble now shows a cracked-up car and a price tag reading '$3,000' in bold red. Expression visibly tenser; the brain inside the skull already begins to glow with a reddish worry color. White background.",
 "Medium shot", "Flat, white, faint red glow in skull", "Rising stakes — the experimental stress applied",
 "Stressed thought bubble with $3,000 red tag; worried brain",
 "Static. The $3,000 red tag swings urgently; the brain's red glow intensifies a notch. 2s."),

("The cognitive gap between the two groups was thirteen IQ points.",
 "Wide diagram on white. Two horizontal brain-power bars side by side: top bar full and green labeled 'MINOR REPAIR GROUP,' bottom bar visibly shorter and orange labeled 'MAJOR REPAIR GROUP.' The gap between them is bracketed with bold '13 IQ POINTS.'",
 "Wide diagram shot", "Flat, white", "Quantified — the number is the punch",
 "Two bars with bracketed 13-point gap",
 "Static. The bracket locks onto the gap; '13 IQ POINTS' drops in boldly. 3s."),

("Thirteen. From a thought experiment. About money.",
 "Close-up on white. Three short bold lines stacked: '13.' / 'FROM A THOUGHT EXPERIMENT.' / 'ABOUT MONEY.' Each line lands as its own statement. Minimalist.",
 "Close-up, centered", "Flat, white", "Blunt emphasis — let the number breathe",
 "Three stacked text lines, each with weight",
 "Static. Each line fades in sequentially with a brief pause between. 3s."),

("So the question everyone is asking — why do poor people make bad decisions — is the wrong question.",
 "Wide shot, white background. A large bold question 'WHY DO POOR PEOPLE MAKE BAD DECISIONS?' with a massive red X crossing through it. Below, in smaller black text: 'WRONG QUESTION.' The character stands to the side, arms crossed, composed.",
 "Wide shot", "Flat, white", "The frame shattered — calm, certain",
 "Red X over the wrong question; character observing",
 "Static. The red X draws across the question; character nods once. 3s."),

# ── THE EXPERIMENT ─────────────────────────────────────────────────────────────

("The man behind this research was not supposed to be at Princeton.",
 "Medium shot of a simple office corridor at Princeton. A cartoon figure (Mullainathan stand-in — dark hair, casual attire, slightly unassuming posture) walks a hallway past a 'PRINCETON' crest on the wall. A small label 'NOT SUPPOSED TO BE HERE' floats quietly beside him. Warm institutional tones.",
 "Medium shot, slight tracking feel", "Flat, warm institutional", "Underdog origin — quiet, not triumphant",
 "Figure walking past the Princeton crest; floating label",
 "Static. The figure takes a step; the floating label settles into place beside him. 2s."),

("His name is Sendhil Mullainathan. His mother cleaned houses in rural India before coming to America.",
 "Split panel. Left: a simple flat village exterior — a small house, green fields, muted warm earth tones. A small cartoon woman figure sweeps a step. Right: a young boy figure with a schoolbag stands in an American neighborhood. Bold label arc: 'SENDHIL MULLAINATHAN.'",
 "Wide split panel", "Flat — warm earth left, cooler suburban right", "Origin story — quiet dignity",
 "Village scene left; American neighborhood right; name label",
 "Static. The name label fades in across both panels. 3s."),

("He grew up watching people he loved make decisions that, from the outside, looked irrational.",
 "Medium shot, warm kitchen interior. A young boy (small character version) sits at a table watching two adult figures discuss something with concerned expressions; a bill envelope on the table. Warm amber light, slightly anxious.",
 "Medium shot interior", "Flat, warm amber", "Formative observation — love and confusion",
 "Boy watching adults discuss bills",
 "Static. One adult gestures to the bill; the boy's eyes track the motion. 3s."),

("He became an economist. He wanted to understand why.",
 "Medium shot in a simple flat university study. The grown character version stands before a chalkboard covered with equations and a bold question mark in the center. Expression focused and determined. Warm neutral tones.",
 "Medium shot", "Flat, warm neutral", "Purpose established — a question pursued for life",
 "Character at chalkboard; equations and question mark",
 "Static. The chalk question mark pulses softly at the center of the board. 2s."),

("He partnered with a behavioral scientist named Eldar Shafir.",
 "Medium-wide shot of two cartoon scientist figures side by side at a shared desk, each with notebooks. A bold centered label between them: 'MULLAINATHAN + SHAFIR.' Warm institutional light.",
 "Medium-wide shot", "Flat, warm institutional", "Partnership formed — two minds join",
 "Two figures at shared desk; partnership label",
 "Static. The '+' in the label brightens briefly; both figures lean slightly toward the shared work. 2s."),

("What if, they asked, the decisions weren't the problem?",
 "Close-up on white. A bold question: 'WHAT IF THE DECISIONS WEREN'T THE PROBLEM?' Beneath it, a small cartoon thought-bubble version of the two scientists looks upward in inquiry. Clean and sparse.",
 "Close-up, centered", "Flat, white", "The pivot question — everything reframes here",
 "Bold question with tiny scientist figures thinking",
 "Static. The question text appears letter by letter, then both tiny figures look up. 3s."),

("What if scarcity itself was doing something to the brain before any decision was even made?",
 "Wide diagram on white. A brain diagram on the right; on the left, a nearly-empty wallet and unpaid bill icons. A bold arrow labeled 'BEFORE DECISIONS' points from the wallet toward the brain. Below: 'SCARCITY → BRAIN → THEN DECISIONS.'",
 "Wide diagram shot", "Flat, white", "Causal chain inverted — scarcity acts first",
 "Arrow from wallet to brain; causal chain label",
 "Static. The arrow draws from wallet to brain; the causal-chain label fades in below. 3s."),

("They went to Tamil Nadu, India.",
 "Wide establishing shot of a flat rural Indian landscape: green sugarcane fields, a small village at the horizon, warm golden light. A location card reads 'TAMIL NADU, INDIA' in bold black. No characters yet.",
 "Wide establishing shot", "Flat, warm golden", "Scene set — another world, same truth",
 "Establishing landscape; location card",
 "Static. The location card fades in over the landscape; a gentle warm haze. 3s."),

("The sugarcane harvest creates a predictable economic cycle.",
 "Wide diagram shot showing a circular cycle: tall green sugarcane stalks on one arc, harvested bundles and coins on another arc, a bare field on the third. Bold arrows connect them in a loop. Label: 'PREDICTABLE CYCLE.'",
 "Wide circular diagram", "Flat, warm green and gold tones", "Structure — a natural experiment visible",
 "Cycle diagram with sugarcane, harvest, bare field",
 "Static. The bold arrows draw around the cycle in sequence. 3s."),

("Before harvest: the farmers are poor. Bills unpaid. Food short.",
 "Wide shot of a simple flat farmhouse interior. A farmer character sits at a bare table; an unpaid bills stack is marked with red X's; a nearly empty pantry shelf is visible. Muted, slightly dim tones.",
 "Wide interior shot", "Flat, muted dim", "Scarcity made concrete — quiet hardship",
 "Farmer at bare table; red X bills; empty pantry",
 "Static. A bill on the stack flutters slightly; the pantry stays bare. 3s."),

("After harvest: the same farmers are flush. Debt cleared. Pantry full.",
 "Wide shot of the same farmhouse interior, now warm and full. The same farmer character sits at a well-stocked table; green checkmarks replace the red X's on the bill stack; pantry is full. Warm amber light.",
 "Wide interior shot", "Flat, warm amber", "Abundance — same house, transformed",
 "Farmer at full table; green checkmark bills; full pantry",
 "Static. A green checkmark gleams on the bill stack; the full pantry glows softly. 2s."),

("Mullainathan and Shafir tested the same farmers twice. Before harvest. After.",
 "Wide horizontal timeline on white. Left node 'BEFORE HARVEST': a muted farmer figure with a small test paper. Right node 'AFTER HARVEST': the same farmer figure, warmer colors, same test paper. A dotted line between them labeled 'SAME FARMERS · TESTED TWICE.'",
 "Wide timeline diagram", "Flat, white", "Scientific method — the natural experiment",
 "Timeline with before/after nodes and same-farmer label",
 "Static. The connecting dotted line draws from left to right. 3s."),

("The difference in cognitive performance: ten IQ points.",
 "Wide diagram on white. Two horizontal cognitive-performance bars: top bar full and warm-green 'AFTER HARVEST,' bottom bar visibly shorter and muted-orange 'BEFORE HARVEST.' A bracket labels the gap: '10 IQ POINTS.'",
 "Wide diagram shot", "Flat, white", "The number arrives — clean and jarring",
 "Two bars with bracketed 10-point gap",
 "Static. The bracket snaps onto the gap; '10 IQ POINTS' appears boldly. 2s."),

("Same person. Same brain. Same genes. Same village.",
 "Close-up on white. Four stacked bold lines: 'SAME PERSON.' / 'SAME BRAIN.' / 'SAME GENES.' / 'SAME VILLAGE.' Each line appears in sequence, building weight. Minimalist.",
 "Close-up, centered", "Flat, white", "Controlled variables restated — rhythm builds tension",
 "Four stacked text lines appearing in sequence",
 "Static. Each line fades in with a beat of pause between. 3s."),

("Different bank account.",
 "Close-up on white. One final bold line: 'DIFFERENT BANK ACCOUNT.' Below it, a flat bank statement icon — one side showing a near-zero balance, the other a positive number. Sparse and conclusive.",
 "Close-up, centered", "Flat, white", "The single variable — lands with weight",
 "Single text line; two bank balance icons below",
 "Static. The 'DIFFERENT BANK ACCOUNT.' line drops in; the two balance icons appear below it. 2s."),

("And the brain changed.",
 "Close-up of the character's transparent skull. Two versions of the brain shown side by side inside: left — dim, slow, subdued; right — brighter, more active, clearer. A bold arrow between them labeled 'BANK ACCOUNT CHANGED → BRAIN CHANGED.'",
 "Close-up on skull, split interior view", "Flat, white — dim left, bright right", "The conclusion — simple and profound",
 "Dim brain vs. active brain inside the skull; labeled arrow",
 "Static. The arrow between the two brain states pulses once; the right brain brightens. 2s."),

# ── THE MECHANISM ──────────────────────────────────────────────────────────────

("Here is what they found happening inside.",
 "Medium shot, warm beige interior with ceiling spotlight. The character faces camera calmly, one hand raised slightly as if beginning an explanation. Inside the transparent skull the brain sits alert and ready. A subtle label 'INSIDE.' glows softly.",
 "Medium shot, direct address", "Warm beige, ceiling spotlight", "Turning inward — the mechanism begins",
 "Character prepared to explain; brain alert; 'INSIDE.' label",
 "Static. The 'INSIDE.' label glows on; the brain straightens its posture. 2s."),

("Your brain has a fixed amount of what researchers call bandwidth.",
 "Close-up diagram of the pink cartoon brain on white. Above it, a flat horizontal 'BANDWIDTH' bar — fully filled, labeled with a small fixed bracket at both ends. Bold label: 'FIXED AMOUNT.' Clean and clinical.",
 "Close-up diagram", "Flat, white", "The key concept introduced — precise",
 "Brain with fixed bandwidth bar above it",
 "Static. The fixed-amount bracket locks onto both ends of the bar with a small click effect. 2s."),

("Not the word used loosely — bandwidth in the precise sense.",
 "Medium shot, white background. The character holds up a small 'PRECISE DEFINITION' card. Beside it, a loose casual use of the word 'bandwidth' is crossed out in red. Clean, educational.",
 "Medium shot", "Flat, white", "Precision established — this is a technical term",
 "Character holding definition card; loose usage crossed out",
 "Static. The red cross-out marks the casual usage; the definition card is held steady. 2s."),

("The total cognitive capacity available for processing, deciding, and planning.",
 "Wide diagram on white. A single horizontal bar labeled 'COGNITIVE BANDWIDTH' spans the frame. Three sections are marked beneath it: 'PROCESSING,' 'DECIDING,' 'PLANNING' — each with a small icon. Clean infographic style.",
 "Wide diagram shot", "Flat, white", "Definition made visual — the full resource",
 "Bandwidth bar with three labeled sections",
 "Static. The three section labels appear in sequence below the bar. 3s."),

("Think of it as RAM. Available in a finite quantity at any given moment.",
 "Medium shot on white. The transparent skull of the character contains a visible flat chip labeled 'RAM' with a small capacity meter beside it. The villain brain points at the chip with one arm, nodding knowingly.",
 "Medium shot", "Flat, white", "Analogy — familiar concept makes it click",
 "RAM chip in skull; brain pointing at it",
 "Static. The RAM meter blinks once; the brain nods and points. 2s."),

("When you have enough — bills paid, no crisis — the brain runs efficiently.",
 "Wide shot, warm beige interior. The character stands calmly at a desk; a green 'BILLS PAID' checkmark on a paper; a rising productivity chart beside. The brain inside the skull is composed and clear. Warm, ordered.",
 "Wide interior shot", "Flat, warm beige", "Baseline health — order and efficiency",
 "Bills paid; productivity chart up; calm brain",
 "Static. The green checkmark gleams; the productivity chart ticks up one notch. 2s."),

("It thinks ahead. It weighs options. It plans.",
 "Wide diagram on white. Three flat panels in sequence: (1) brain with an arrow pointing forward labeled 'AHEAD,' (2) brain holding two options on a scale labeled 'OPTIONS,' (3) brain drawing a roadmap labeled 'PLANS.' All bright and clear.",
 "Wide three-panel diagram", "Flat, white", "Capability showcased — this is what full bandwidth does",
 "Three-panel sequence of brain functions",
 "Static. Each panel lights in turn from left to right. 3s."),

("When scarcity enters, something different happens.",
 "Medium shot, warm beige interior. The character sits at a desk; a red 'BILLS OVERDUE' envelope slides into the scene from the right. The brain inside the skull turns its head toward it, expression shifting from composed to alert.",
 "Medium shot", "Flat, warm beige, red envelope entering", "Intrusion — the scarcity arrives",
 "Red overdue envelope entering; brain's attention captured",
 "Static. The red envelope slides in and comes to rest; the brain's head swivels toward it. 2s."),

("The scarcity captures the bandwidth.",
 "Close-up diagram of the bandwidth bar. A dark red 'SCARCITY' block appears on the left end of the bar and rapidly fills a large portion of it, pushing the remaining usable capacity to a small green sliver on the right. Bold label: 'CAPTURED.'",
 "Close-up diagram", "Flat, white, red filling the bar", "The mechanism — vivid and alarming",
 "Scarcity block filling most of the bandwidth bar",
 "Static. The dark red block expands across the bar from left to right, shrinking the green sliver. 3s."),

("Not metaphorically. Literally.",
 "Close-up on white. Two bold stacked words: 'NOT METAPHORICALLY.' / 'LITERALLY.' Below, a tiny brain-scan style flat diagram with the scarcity region shown as a large lit-up zone. Stark and direct.",
 "Close-up, centered", "Flat, white", "Precision underscored — not a figure of speech",
 "Two-line statement; brain-scan diagram below",
 "Static. Each line drops in separately; the brain-scan diagram appears below. 2s."),

("The worry, the calculation, the constant mental arithmetic of not having enough",
 "Wide interior shot, warm beige with ceiling spotlight. The character sits at a kitchen table covered in bills, a calculator, and a near-empty wallet. Inside the skull, the brain is surrounded by floating arithmetic symbols, bill icons, and worry lines. Overwhelmed.",
 "Wide interior shot", "Warm beige, slightly anxious", "The daily cognitive labor — made visible",
 "Character at bill-covered table; brain surrounded by arithmetic",
 "Static. The arithmetic symbols drift around the brain; the character's brow furrows slightly. 3s."),

("consumes the processing power your brain needs to make good decisions.",
 "Close-up diagram of the bandwidth bar again. The 'SCARCITY CALCULATIONS' block now fills almost all of the bar. A tiny labeled section labeled 'GOOD DECISIONS' is a sliver at the far right, nearly gone. A red arrow points to it: 'ALMOST NONE LEFT.'",
 "Close-up diagram", "Flat, white, red emphasis", "Depletion measured — barely anything remains",
 "Bandwidth bar nearly consumed; tiny decisions sliver",
 "Static. The 'ALMOST NONE LEFT' arrow nudges toward the sliver. 2s."),

("Mullainathan and Shafir called this the bandwidth tax.",
 "Medium shot, warm beige interior with ceiling spotlight. The character faces camera calmly. A bold floating label behind them reads 'THE BANDWIDTH TAX' as if naming a concept on a whiteboard. The brain inside the skull nods with recognition.",
 "Medium shot", "Warm beige, ceiling spotlight", "The concept named — a landmark moment",
 "Character facing camera; 'THE BANDWIDTH TAX' label behind them",
 "Static. The label materializes fully; the brain nods. 2s."),

("Being poor is not just having less money.",
 "Wide shot, white background. The character stands beside a simple near-empty wallet. A bold 'NOT JUST' sticker overlaps a label that reads 'LESS MONEY.' Calm, deliberate reframing.",
 "Wide shot", "Flat, white", "The reframe begins — bigger than money",
 "Character beside wallet; 'NOT JUST' label",
 "Static. The 'NOT JUST' sticker appears over the 'LESS MONEY' label. 2s."),

("It is running the same hardware as everyone else",
 "Wide split panel on white. Left: a character in comfortable surroundings; Right: the character in sparse surroundings. Both have identical brain hardware shown inside their skulls, labeled 'SAME HARDWARE.' Bold equals sign between them.",
 "Wide split panel", "Flat, white", "Equality of hardware — the injustice of the tax",
 "Two characters with identical brain hardware labels",
 "Static. The 'SAME HARDWARE' labels fade in on both sides simultaneously. 3s."),

("with far more of it consumed by background processes that never turn off.",
 "Close-up diagram of the bandwidth bar. A large dark portion labeled 'BACKGROUND PROCESSES — NEVER OFF' fills most of the bar with a repeating pattern suggesting constant activity. A small clear section labeled 'AVAILABLE' is barely visible. The pattern subtly pulses.",
 "Close-up diagram", "Flat, white, pulsing dark section", "The invisible always-on cost — haunting",
 "Bandwidth bar dominated by background processes",
 "Static. The 'NEVER OFF' section pulses slowly; the tiny 'AVAILABLE' sliver barely holds. 3s."),

("Every day, a person in financial scarcity performs a kind of cognitive triage.",
 "Wide interior shot, warm beige. The character sits at a table with several bill envelopes and a mental sorting gesture — one hand pushing some aside, one holding another closer. Expression concentrated. Inside the skull the brain is prioritizing with tiny flags.",
 "Wide interior shot", "Warm beige, ceiling spotlight", "Daily cognitive labor — triage as survival",
 "Character sorting bills; brain flagging priorities",
 "Static. The character moves one bill to a 'WAIT' pile; the brain places a priority flag. 3s."),

("Which bill gets paid. Which doesn't. Which problem can wait.",
 "Wide diagram on white. Three flat bill envelopes side by side: first labeled 'PAID ✓' (green), second labeled 'SKIP ✗' (red), third labeled 'WAIT' (gray). A bold header: 'DAILY TRIAGE.' Clean clinical grid.",
 "Wide diagram shot", "Flat, white", "The calculus laid bare — cold but real",
 "Three bill envelopes with outcome labels",
 "Static. Each label appears on its envelope in sequence: green, red, gray. 2s."),

("None of these calculations are free.",
 "Close-up on white. A large bold 'NONE OF THESE ARE FREE.' label. Below it, each calculation from the previous beat shown as a small coin being taken from the bandwidth bar. Clinical precision.",
 "Close-up, centered", "Flat, white", "Cost underscored — no such thing as free cognitive work",
 "Bold label; coins draining from bandwidth bar",
 "Static. The coins drain one by one from the bandwidth bar below the label. 2s."),

("Each one costs bandwidth.",
 "Close-up diagram of the bandwidth bar. A small coin icon above each calculation type — and each coin is deducted, shrinking the bar visibly. A running total depletes. Bold label: 'EACH ONE COSTS BANDWIDTH.'",
 "Close-up diagram", "Flat, white", "The meter running — every decision has a price",
 "Coins deducting from bandwidth bar",
 "Static. Coins deduct in sequence; the bar shortens with each deduction. 3s."),

("And bandwidth spent on survival is bandwidth not available for planning.",
 "Wide split panel on white. Left 'SURVIVAL': bandwidth bar nearly full with red 'SURVIVAL' blocks, almost no free space. Right 'PLANNING': a wide empty green portion of the bar labeled 'NEEDS THIS SPACE — UNAVAILABLE.' A red X bridges the two.",
 "Wide split panel", "Flat, white, red vs. green tones", "The trade-off — planning evicted by survival",
 "Survival consuming bandwidth; planning section blocked",
 "Static. The red X appears between the two panels; the green planning section grays out. 3s."),

# ── THE TUNNEL ─────────────────────────────────────────────────────────────────

("What happens when the tax gets severe enough has a name.",
 "Medium shot, warm beige interior. The character faces camera, expression serious. A bold floating label materializes: 'IT HAS A NAME.' The brain inside the skull looks toward the label with a mix of recognition and gravity.",
 "Medium shot, direct address", "Warm beige, ceiling spotlight", "The name is coming — anticipation builds",
 "Character facing camera; label materializing; brain attentive",
 "Static. The label materializes fully; the brain's expression turns serious. 2s."),

("Mullainathan and Shafir called it tunneling.",
 "Medium shot on white. A bold centered text: 'TUNNELING.' Below it, a simple flat dark oval tunnel mouth, perfectly centered, with a small bright point of light at its far end. Clinical and visual simultaneously.",
 "Medium shot, centered", "Flat, white — dark tunnel mouth, distant bright point", "The concept named and visualized",
 "Bold 'TUNNELING.' label above a dark flat oval tunnel mouth",
 "Static. The tunnel mouth holds; the distant bright point at the end glows steadily. 2s."),

("The mind enters a tunnel.",
 "Wide shot, dark gray-black background. The character stands at the entrance of a large dark oval tunnel. Inside, a single bright focal point shines at the far end. The character takes a step inward. The walls are flat, thick, and black-outlined.",
 "Wide shot, character entering tunnel", "Flat, dark — bright focal point at tunnel end", "Entry — the threshold crossed",
 "Character stepping into the dark oval tunnel; bright end visible",
 "Static. The character takes one step into the tunnel; the bright focal point stays fixed at the far end. 3s."),

("Inside the tunnel, the immediate crisis is in sharp focus.",
 "POV shot from inside the dark tunnel. At the bright focal end: a glowing, sharp, detailed crisis image — a bold red 'EVICTION NOTICE' and a car with a broken part. Everything crisp at the center. Tunnel walls dark and flat.",
 "POV inside the tunnel, narrow bright center", "Dark tunnel walls — vivid bright center", "Tunnel vision — hyper-focus on crisis",
 "Bright crisis images sharply lit at tunnel's end",
 "Static. The crisis images at the bright end pulse with clarity; the dark walls hold still. 2s."),

("Urgent. Visible. Demanding.",
 "Close-up on the tunnel's bright focal point. Three bold pulsing words radiate from the crisis images: 'URGENT.' / 'VISIBLE.' / 'DEMANDING.' Each word appears in thick black capitals. Dark surrounding tunnel.",
 "Close-up on tunnel focal point", "Flat, dark tunnel — vivid center", "The pull — the tunnel commands attention",
 "Three bold words radiating from the bright crisis center",
 "Static. Each word pulses in sequence outward from the center: URGENT, VISIBLE, DEMANDING. 3s."),

("Everything outside the tunnel — the long-term consequences, the better options, the trap being walked into — disappears.",
 "Wide shot inside the dark tunnel. Beyond the tunnel walls, faint ghost outlines of 'LONG-TERM CONSEQUENCES,' 'BETTER OPTIONS,' and 'THE TRAP' exist — but they are washed out, invisible to the character standing in the tunnel, looking only forward.",
 "Wide inside-tunnel shot", "Flat, dark — ghost outlines outside walls invisible", "Peripheral blindness — the cost of tunneling",
 "Character in tunnel; ghost outlines outside the walls",
 "Static. The ghost outlines fade further into darkness; the character looks only at the bright center. 3s."),

("From inside the tunnel, a payday loan looks rational.",
 "Medium shot inside the tunnel. The character stands in the narrow tunnel space; at the bright focal end: a simple flat sign reading 'PAYDAY LOAN — $400 TODAY.' It glows with reasonable clarity. From this angle, it looks like a door, not a trap.",
 "Medium shot inside tunnel", "Flat, dark tunnel — bright sign at end", "The rationality of the tunnel — seductive",
 "Character viewing the payday loan sign as a reasonable option",
 "Static. The 'PAYDAY LOAN' sign glows steadily; the character's head tilts toward it as if considering. 2s."),

("You need four hundred dollars to avoid eviction.",
 "Close-up of a flat eviction notice pinned to a door. Bold red text: 'EVICTION NOTICE — 48 HOURS.' A small $400 figure circled in red at the bottom. Dark, urgent framing.",
 "Close-up on eviction notice", "Flat, dark urgent", "The immediate crisis made concrete",
 "Eviction notice with $400 circled in red",
 "Static. The $400 circled figure pulses with a red glow. 2s."),

("The lender will give you four hundred today. You pay back four hundred and sixty in two weeks.",
 "Wide diagram on white. A simple flat transaction timeline: left — '$400 TODAY' in green (given); right — '$460 IN 2 WEEKS' in red (owed). A dotted arrow connects them. Label: 'THE DEAL.'",
 "Wide diagram shot", "Flat, white", "The transaction laid bare — looks simple from inside",
 "Timeline: $400 given, $460 owed in 2 weeks",
 "Static. The dotted arrow draws from the $400 to the $460; the gap in cost is visible. 3s."),

("That is four hundred percent annualized interest.",
 "Close-up on white. Large bold red text: '400% ANNUALIZED INTEREST.' Below it, a small flat calculator icon and a tiny shocked cartoon character. Stark and clinical.",
 "Close-up, centered", "Flat, white, bold red text", "The real cost revealed — clinical and damning",
 "400% figure in bold red; shocked character icon",
 "Static. The '400%' figure stamps in with impact; the shocked character appears below. 2s."),

("From outside the tunnel, this is a catastrophic decision.",
 "Wide shot from outside the tunnel entrance. The dark tunnel mouth is visible; beyond it the character is a small silhouette walking toward the bright 'PAYDAY LOAN' sign. From outside, a large red 'CATASTROPHIC' label hangs over the tunnel entrance.",
 "Wide shot from outside tunnel", "Flat, exterior view — dark tunnel mouth prominent", "The external view — the danger is obvious from out here",
 "Tunnel exterior view; 'CATASTROPHIC' label over entrance",
 "Static. The 'CATASTROPHIC' label hovers over the tunnel mouth; the silhouette inside keeps walking. 3s."),

("From inside the tunnel, it is the only visible option.",
 "POV from inside the tunnel again. Everything dark except the bright 'PAYDAY LOAN' sign at the end. A bold label appears beside it: 'ONLY VISIBLE OPTION.' No other exits, no side paths, just the one bright point.",
 "POV inside tunnel", "Flat, dark — single bright option", "The cognitive trap completed",
 "Single bright option in dark tunnel; 'ONLY VISIBLE OPTION' label",
 "Static. The 'ONLY VISIBLE OPTION' label materializes beside the sign. 2s."),

("The tunnel shows the eviction. The tunnel shows the lender.",
 "Wide inside-tunnel shot. At the bright focal center: two clear images side by side — the eviction notice and the lender's sign. Both crisp and visible. Dark tunnel walls around them. Label: 'THE TUNNEL SHOWS:'",
 "Wide inside-tunnel shot", "Flat, dark — two bright focal images", "What the tunnel illuminates — its selective logic",
 "Two bright images at tunnel center; tunnel-shows label",
 "Static. The 'THE TUNNEL SHOWS:' label appears; both images remain vividly lit. 2s."),

("The tunnel does not show the debt spiral three months from now.",
 "Wide inside-tunnel shot. At the dark periphery beyond the tunnel walls: a ghost outline of a spiraling debt chart labeled 'THREE MONTHS FROM NOW — NOT VISIBLE.' Washed out, invisible to the character inside.",
 "Wide inside-tunnel shot", "Flat, dark — ghost debt spiral in periphery", "What the tunnel hides — the long term erased",
 "Ghost debt spiral outside tunnel walls; 'NOT VISIBLE' label",
 "Static. The ghost debt spiral fades even further; the 'NOT VISIBLE' label stays dim. 3s."),

("The same person who would never take a four-hundred-percent loan under normal conditions",
 "Wide split panel. Left 'NORMAL CONDITIONS': the character at a well-lit desk calmly reviewing a loan document with '400%' in bold red — expression clearly rejecting it, hand waving it away. Warm, clear lighting.",
 "Wide split panel — left panel only active", "Flat, warm clear light", "The same person — baseline behavior established",
 "Character calmly rejecting the 400% loan",
 "Static. The character's hand waves the loan document away; expression firm. 2s."),

("takes it without hesitation under sufficient scarcity.",
 "Wide split panel continued. Right 'INSIDE THE TUNNEL': same character in the dark tunnel, hand reaching forward to accept the same '400%' loan document at the bright focal end. Face focused, no hesitation. Same person — different cognitive state.",
 "Wide split panel — both panels", "Flat — warm left, dark tunnel right", "The transformation — the same person, different state",
 "Character accepting loan inside the tunnel",
 "Static. The right character's hand reaches forward and accepts the document; the tunnel darkness frames them. 3s."),

("Not because they became less intelligent.",
 "Medium shot on white. A bold red X over the label 'BECAME LESS INTELLIGENT.' The character stands calmly beside it, expression steady. Clean and direct.",
 "Medium shot", "Flat, white", "Exoneration — intelligence is not the variable",
 "Red X over intelligence-loss label; character steady",
 "Static. The red X draws across the label; the character holds steady. 2s."),

("Because the tunnel ate their bandwidth.",
 "Close-up inside the tunnel. The bandwidth bar is shown inside the character's skull — the 'TUNNEL' block has consumed almost all of it, leaving only a hair of available capacity. The bar looks visually devoured. Bold label: 'THE TUNNEL ATE THEIR BANDWIDTH.'",
 "Close-up inside tunnel, skull view", "Flat, dark — bandwidth bar nearly gone", "The mechanism complete — cause explained",
 "Bandwidth bar consumed by tunnel block; label",
 "Static. The tunnel block finishes consuming the last of the bar. 2s."),

# ── THE MINNESOTA EXPERIMENT ───────────────────────────────────────────────────

("This is not unique to money.",
 "Medium shot, white background. The character faces camera, one arm extended toward a wide space as if introducing a new context. The brain inside the skull shifts its gaze outward. Bold label: 'NOT UNIQUE TO MONEY.'",
 "Medium shot, direct address", "Flat, white", "Widening the lens — the principle is universal",
 "Character gesturing outward; 'NOT UNIQUE' label",
 "Static. The label appears beside the extended arm. 2s."),

("In 1944, thirty-six men at the University of Minnesota volunteered to be deliberately starved for science.",
 "Wide establishing shot of a flat 1940s institutional building exterior. Thirty-six small identical cartoon figures line up at the entrance. A bold location-date card: 'UNIVERSITY OF MINNESOTA — 1944.' Muted olive and gray tones.",
 "Wide establishing shot", "Flat, muted 1940s olive-gray", "Historical — another scarcity experiment, different domain",
 "Thirty-six figures entering the building; date card",
 "Static. The date card fades in; the line of figures shifts forward slightly. 3s."),

("They were conscientious objectors. Educated, thoughtful men with rich intellectual lives.",
 "Medium-wide shot of a flat common room. Four of the thirty-six figures sit with books, a chessboard, and a newspaper. Warm, slightly institutional amber. A label: 'EDUCATED · THOUGHTFUL · RICH INTELLECTUAL LIVES.'",
 "Medium-wide shot", "Flat, warm institutional amber", "Humanity established — these are not empty figures",
 "Figures reading, playing chess; descriptive label",
 "Static. Each activity continues subtly; the label holds prominently. 3s."),

("Within weeks of caloric restriction, something happened to their minds.",
 "Medium shot, same room but now dimmer and barer. The same figures sit differently — books down, chess pieces untouched, posture changed. A clock on the wall shows weeks passed. Expression quieter. A subtle label: 'WEEKS LATER.'",
 "Medium shot", "Flat, slightly dimmer amber", "Transition — the change is coming",
 "Figures sitting quietly; clock marking weeks; 'WEEKS LATER' label",
 "Static. The clock hand ticks forward; one figure's book slides from their hands. 3s."),

("They could not stop thinking about food.",
 "Wide shot of the interior. Every character's thought bubble is now filled with a single image: cartoon food. Bread, soup, vegetables — all thought bubbles pointing upward, identical obsession. Bold label: 'COULD NOT STOP THINKING ABOUT FOOD.'",
 "Wide shot", "Flat, neutral institutional", "Total cognitive capture — the scarcity mechanism in a new domain",
 "All characters' thought bubbles filled with food",
 "Static. The thought bubbles fill in with food icons simultaneously; the label appears. 3s."),

("Scientists who had arrived with interests in literature, music, politics — all of it collapsed inward.",
 "Wide diagram on white. A fan of interest labels radiating outward from a character icon: 'LITERATURE,' 'MUSIC,' 'POLITICS,' 'PHILOSOPHY.' Each label collapses back inward toward a single central label: 'FOOD.' Arrows reverse.",
 "Wide diagram shot", "Flat, white", "Collapse visualized — the mind narrowed involuntarily",
 "Interest labels collapsing inward toward 'FOOD'",
 "Static. Each interest label collapses inward with its arrow reversing direction toward 'FOOD.' 3s."),

("One man wrote in his journal that he had tried to think about his political beliefs — a topic he cared deeply about — and simply could not.",
 "Close-up of a flat open journal page. Handwritten-style text (bold, black): 'Tried to think about politics. Simply could not.' A half-finished entry trails off. A small food doodle fills the margin instead of the writing. Warm paper tones.",
 "Close-up on journal page", "Flat, warm paper tones", "Personal and specific — the evidence is human",
 "Journal entry trailing off; food doodle in the margin",
 "Static. The pen trail fades off mid-sentence; the food doodle sits quietly in the margin. 2s."),

("His mind kept returning to food.",
 "Medium shot, neutral background. The character sits with a book open, genuinely trying to read. But inside the transparent skull, the brain keeps turning its head to stare at a floating food image — book ignored. Loops quietly.",
 "Medium shot", "Flat, neutral", "Involuntary return — the override is automatic",
 "Character reading; brain inside skull turning toward food image",
 "Static. The brain's head rotates away from the book and back toward the food image; the character keeps trying to read. 2s loop."),

("The scarcity had not changed his intelligence.",
 "Medium shot on white. The character stands beside a stable IQ bar — unchanged from a baseline. A bold label: 'INTELLIGENCE UNCHANGED.' The brain inside the skull has the same smug but stable expression.",
 "Medium shot", "Flat, white", "The constant restated — not diminished, just redirected",
 "Stable IQ bar; 'INTELLIGENCE UNCHANGED' label",
 "Static. The IQ bar stays flat; the label holds. 2s."),

("It had redirected every available cognitive resource toward the one thing his brain identified as the immediate threat.",
 "Wide diagram on white. Multiple cognitive resource arrows (labeled 'PLANNING,' 'REASON,' 'MEMORY,' 'CREATIVITY') all redirected toward one central pulsing icon: 'IMMEDIATE THREAT.' The arrows converge forcefully. Bold red center.",
 "Wide diagram shot", "Flat, white, red pulsing center", "Redirection — the brain's emergency protocol",
 "All cognitive arrows converging on the immediate threat",
 "Static. Each labeled arrow swings from its original direction to point at the red center. 3s."),

("This is what financial scarcity does.",
 "Medium shot, warm beige interior. The character faces camera calmly. The brain inside the skull is surrounded by financial symbols — bills, dollar signs, debt numbers. Bold label: 'FINANCIAL SCARCITY DOES THIS.'",
 "Medium shot, direct address", "Warm beige", "Bridge — Minnesota to money",
 "Character facing camera; brain surrounded by financial symbols",
 "Static. The financial symbols drift around the brain; the label settles. 2s."),

("Not to weak people. Not to irresponsible people.",
 "Wide shot on white. Two figures with red X labels: left 'WEAK PEOPLE ✗', right 'IRRESPONSIBLE PEOPLE ✗.' Both crossed out firmly. The character stands between them, steady and un-labeled.",
 "Wide shot", "Flat, white", "Blame removed — the myth dismantled",
 "Two red-X labels crossed out; unlabeled character between them",
 "Static. The red X marks appear on both labels; the character holds steady. 2s."),

("To all people.",
 "Wide shot. A vast flat grid of diverse character silhouettes — all sizes, all styles — and above the whole grid: 'TO ALL PEOPLE.' Bold, inclusive, sweeping.",
 "Wide shot", "Flat, white", "Universal — no one is exempt",
 "Large grid of diverse silhouettes; 'TO ALL PEOPLE' label",
 "Static. The 'TO ALL PEOPLE' label sweeps in over the grid. 2s."),

# ── THE INDUSTRY ───────────────────────────────────────────────────────────────

("Here is where this becomes something other than a science lesson.",
 "Medium shot, warm beige interior with ceiling spotlight. The character faces camera with a slight shift in posture — a pivot. The brain inside the skull leans forward. A subtle change in the scene's tone. Bold label: 'THIS IS WHERE IT CHANGES.'",
 "Medium shot, direct address", "Warm beige, ceiling spotlight — slight tone shift", "The pivot — from science to industry",
 "Character pivoting; brain leaning forward; label",
 "Static. The label materializes; the brain leans in. 2s."),

("The payday lending industry in the United States generates approximately ninety billion dollars per year.",
 "Wide shot. A flat industrial building complex labeled 'PAYDAY LENDING INDUSTRY' with a large green '$90 BILLION / YEAR' banner across it. Small figures walking in and out. Bold, slightly ominous. Cool gray exterior.",
 "Wide establishing shot", "Flat, cool gray exterior", "Scale of the industry — vast and deliberate",
 "Industry complex with $90 billion banner; figures entering",
 "Static. The banner text holds firm; figures walk in and out at the entrance. 3s."),

("This is not an industry that discovered a market.",
 "Medium shot on white. A bold red X over the phrase 'DISCOVERED A MARKET.' The character stands calmly beside it. Precise and direct.",
 "Medium shot", "Flat, white", "Intent established — this was designed",
 "Red X over 'DISCOVERED A MARKET'; character beside it",
 "Static. The red X draws across the phrase. 2s."),

("It is an industry built — deliberately, specifically, precisely — around the cognitive state of a bandwidth-depleted mind.",
 "Wide diagram on white. A flat architectural blueprint of the payday loan storefront. The foundation slab is labeled 'BANDWIDTH-DEPLETED MIND.' Three pillars above it: 'DELIBERATELY,' 'SPECIFICALLY,' 'PRECISELY.' The storefront sits atop. Blueprint lines throughout.",
 "Wide diagram shot", "Flat, white, blueprint style", "Architecture of exploitation — the design is exposed",
 "Blueprint with 'BANDWIDTH-DEPLETED MIND' as foundation",
 "Static. The three pillar labels appear in sequence; the storefront sits on top. 3s."),

("The interest rates are disclosed. The terms are available. The math is transparent.",
 "Wide three-panel diagram on white. Panel 1: 'RATES DISCLOSED ✓' (green check). Panel 2: 'TERMS AVAILABLE ✓' (green check). Panel 3: 'MATH TRANSPARENT ✓' (green check). All technically compliant.",
 "Wide three-panel diagram", "Flat, white, green checks", "Technical compliance — but this is the setup",
 "Three green-check compliance panels",
 "Static. Each green check appears in sequence on the panels. 2s."),

("But the paperwork is long. The terms are complex.",
 "Wide split panel. Left 'WHAT THEY SAY': simple clean document, green check. Right 'WHAT IS DELIVERED': a towering stack of fine-print documents, daunting and dense. A bold 'BUT' bridges them. Cooler, more ominous tone.",
 "Wide split panel", "Flat — clean green left, dense gray-right", "The gap — compliance hides the trap",
 "Simple claim vs. dense reality; 'BUT' bridge",
 "Static. The stack on the right grows by one layer; the 'BUT' holds boldly between. 3s."),

("The application happens at the moment of maximum stress, maximum urgency, minimum cognitive capacity.",
 "Wide diagram on three axes on white. A flat stress meter maxed out (red), an urgency meter maxed out (red), and a cognitive capacity meter nearly empty (red). All three meters at their worst simultaneously. Label: 'THE MOMENT OF APPLICATION.'",
 "Wide three-meter diagram", "Flat, white, all-red meters", "The window — perfectly chosen by design",
 "Three maxed-out meters; application moment label",
 "Static. Each meter's red indicator blinks; the label appears below. 3s."),

("Because that is exactly when you walk through the door.",
 "Wide shot. The character — stressed, slightly disheveled, carrying overdue bill envelopes — walks through the door of the payday loan storefront. The storefront light is warm and welcoming. The timing is perfect. From the industry's perspective.",
 "Wide shot, storefront entrance", "Flat — warm storefront interior visible through door", "The designed moment — they were waiting for this",
 "Stressed character entering storefront at exactly the right moment",
 "Static. The character steps through the door; the storefront's warm light spills out. 2s."),

("Researchers found that payday loan customers underestimate the cost of their loans by a factor of three to four times.",
 "Wide diagram on white. A flat scale: on one side the customer's estimated loan cost (small stack), on the other the actual cost (three-to-four-times taller stack). The scale tips dramatically. Label: '3–4× UNDERESTIMATE.'",
 "Wide diagram shot", "Flat, white", "The measurement — systematic and predictable",
 "Tilted scale: estimated vs. actual cost; 3-4x label",
 "Static. The scale tips down on the actual-cost side; the label appears. 3s."),

("Not a rounding error. Not a misunderstanding.",
 "Medium shot on white. Two bold red X labels: 'ROUNDING ERROR ✗' and 'MISUNDERSTANDING ✗.' The character stands to the side, composed.",
 "Medium shot", "Flat, white", "Precision — these explanations are refused",
 "Two red-X labels crossed out; character beside them",
 "Static. Both red X's draw across their labels simultaneously. 2s."),

("A systematic, predictable failure of bandwidth-depleted cognition.",
 "Wide diagram on white. A repeating pattern of identical customer icons, each with a nearly-empty bandwidth bar, each making the same underestimate — a systematic row. Bold label: 'SYSTEMATIC · PREDICTABLE · BANDWIDTH-DEPLETED COGNITION.'",
 "Wide diagram shot", "Flat, white", "The pattern — not random, by design",
 "Row of identical customer icons with empty bandwidth bars",
 "Static. The row of icons fills in left to right, each with the same depleted bar. 3s."),

("This is not coincidence.",
 "Close-up on white. Three bold centered words: 'NOT A COINCIDENCE.' A single flat line beneath them for emphasis. Stark.",
 "Close-up, centered", "Flat, white", "Intent asserted — the accusation is building",
 "Bold 'NOT A COINCIDENCE.' text centered",
 "Static. The text appears with a firm stamp effect. 1.5s."),

("The complexity is not a side effect. The complexity is the product.",
 "Wide split panel on white. Left 'SIDE EFFECT ✗' — a red X label. Right 'THE PRODUCT ✓' — a green check, with the complexity itself illustrated as a dense fine-print document proudly displayed as merchandise. Startling inversion.",
 "Wide split panel", "Flat, white", "The thesis of exploitation — the design reversed",
 "Complexity as product; red X on side effect",
 "Static. The green check appears on 'THE PRODUCT' panel; the product complexity is displayed proudly. 3s."),

("The industry does not create the tunnel.",
 "Medium shot on white. A flat tunnel entrance; the industry building beside it — not building the tunnel, but positioned nearby. Bold label: 'DOES NOT CREATE THE TUNNEL.' The tunnel was already there.",
 "Medium shot", "Flat, white", "The distinction — nature vs. exploitation",
 "Industry building beside pre-existing tunnel; label",
 "Static. The 'DOES NOT CREATE' label appears over the industry-building connection. 2s."),

("It builds its storefronts at the entrance.",
 "Wide shot. The dark oval tunnel mouth with a bright interior; right at the tunnel entrance, the payday loan storefront is positioned perfectly — welcoming, lit, precisely placed. A bold label: 'STOREFRONT AT THE ENTRANCE.' Chilling clarity.",
 "Wide shot", "Flat — dark tunnel, lit storefront at mouth", "The business model revealed — location is everything",
 "Payday storefront positioned precisely at tunnel mouth",
 "Static. The storefront sign lights up at the tunnel entrance; the dark tunnel recedes behind it. 3s."),

# ── THE REFRAME ────────────────────────────────────────────────────────────────

("The question everyone asks about poverty is: why don't they just make better decisions?",
 "Wide shot on white. A large bold question in a speech bubble: 'WHY DON'T THEY JUST MAKE BETTER DECISIONS?' Multiple small crowd figures around it — some nodding, some shrugging. A red tinge to the overall scene.",
 "Wide shot", "Flat, white, slight red tinge", "The wrong question — stated plainly before being dismantled",
 "Crowd figures around the wrong question bubble",
 "Static. The question bubble expands slightly; crowd figures nod. 2s."),

("Here is the correct question.",
 "Medium shot, warm beige interior with ceiling spotlight. The character faces camera, composed, deliberate. The brain inside the skull leans forward attentively. A bold label: 'THE CORRECT QUESTION.' The tone pivots.",
 "Medium shot, direct address", "Warm beige, ceiling spotlight", "The pivot — composure signals authority",
 "Character facing camera; 'THE CORRECT QUESTION' label",
 "Static. The label materializes; the brain leans in attentively. 2s."),

("Imagine you haven't slept in three days.",
 "Medium shot of the character in a dim bedroom. Dark circles drawn under the eyes; a clock on the wall showing three days' worth of tally marks. Expression hollow with exhaustion. Dark blue-gray room tones.",
 "Medium shot", "Flat, dim blue-gray", "The thought experiment begins — visceral and immediate",
 "Exhausted character; three-day tally on clock",
 "Static. The character's eyes blink heavily; the tally marks on the clock hold. 3s."),

("You have a child with a fever.",
 "Medium-wide shot of a warm dim bedroom. The character stands beside a small cot where a child figure lies with a bright red cheek and a small fever thermometer. Expression tight with worry. Warm amber light, anxious.",
 "Medium-wide shot", "Flat, warm amber, anxious", "A parent's crisis — the weight multiplies",
 "Parent beside feverish child; worried expression",
 "Static. The child's cheek glows red; the parent's hand moves to check the child's forehead. 2s."),

("You owe rent you don't have. Your car needs a repair you cannot afford. Without the car you cannot get to work.",
 "Wide interior shot. The character sits at a kitchen table surrounded by overlapping crisis icons: a rent overdue notice (red), a broken-car icon (red), a work-building with a dotted line to the car (interrupted). All simultaneous. Overwhelmed.",
 "Wide interior shot", "Flat, warm beige — multiple red crisis icons", "Crisis stacking — the simultaneous weight",
 "Multiple simultaneous crisis icons around the character",
 "Static. Each crisis icon glows in sequence, overlapping; character is surrounded. 3s."),

("Now sit down and optimize your retirement contribution.",
 "Medium shot on white. The same crisis-surrounded character tries to sit at a desk with a clean flat retirement planning form. The form looks absurd beside the crisis icons still visible. Bold label: 'NOW OPTIMIZE YOUR RETIREMENT.' Deliberate irony.",
 "Medium shot", "Flat, white", "Absurdity — the contrast is the point",
 "Crisis character attempting retirement form; ironic label",
 "Static. The retirement form sits untouched; the crisis icons still pulse around the character. 2s."),

("Now compare mortgage interest rates.",
 "Medium shot on white. Same overwhelmed character now trying to hold two mortgage rate sheets. The sheets wilt in their hands. Bold label: 'NOW COMPARE MORTGAGE RATES.' The absurdity deepens.",
 "Medium shot", "Flat, white", "Absurdity compounding — the exercise is brutal",
 "Overwhelmed character holding limp mortgage sheets",
 "Static. The mortgage sheets sag in the character's hands; the label appears firmly above. 2s."),

("Now read the fine print on the financial product being offered to you.",
 "Medium shot on white. The character tries to read a tall stack of dense fine-print documents. Head forward, squinting. The stack towers over them. Bold label: 'NOW READ THE FINE PRINT.' The impossibility is complete.",
 "Medium shot", "Flat, white", "The final blow — the fine print arrives at the worst moment",
 "Character squinting at towering fine-print stack",
 "Static. The fine-print stack wobbles slightly; the character squints harder. 2s."),

("This is not a hypothetical exercise. This is Tuesday for tens of millions of people.",
 "Wide shot. The same crisis-surrounded scene but now replicated across a grid of dozens of identical character setups — a Tuesday repeated at scale. Bold label: 'THIS IS TUESDAY FOR TENS OF MILLIONS.'",
 "Wide shot, replicated grid", "Flat, white", "Scale — the thought experiment is someone's reality",
 "Grid of repeated crisis setups; scale label",
 "Static. The grid fills out; the label sweeps across the top. 3s."),

("The cognitive research is precise.",
 "Medium shot, warm beige interior. The character faces camera, steady. A flat research chart appears beside them — clean, labeled, precise. The brain inside the skull holds up a small 'PRECISE.' placard. Clinical authority.",
 "Medium shot", "Flat, warm beige", "Authority grounded — the science is exact",
 "Character beside precise research chart; brain holding placard",
 "Static. The 'PRECISE.' placard is held up by the brain; the chart is sharp and labeled. 2s."),

("The bandwidth available to a person managing multiple simultaneous crises",
 "Wide interior shot. The character sits at the kitchen table, multiple crisis icons active simultaneously. The bandwidth bar in the skull is nearly consumed — barely a sliver of green remains.",
 "Wide interior shot", "Flat, warm beige — red crisis icons active", "The depletion shown in real context",
 "Character amid simultaneous crises; nearly empty bandwidth bar",
 "Static. The bandwidth bar's sliver pulses; crisis icons hold active around the character. 3s."),

("is not materially different from the bandwidth of someone awake for twenty-four hours",
 "Wide split panel on white. Left 'MULTIPLE CRISES': the bandwidth bar at its depleted state. Right '24 HOURS AWAKE': an identical bandwidth bar at the same depleted state. A bold '≈' equals-approximately sign between them. Label: 'NOT MATERIALLY DIFFERENT.'",
 "Wide split panel", "Flat, white", "Equivalence — the impairment is real and comparable",
 "Two identical depleted bandwidth bars; equivalence sign",
 "Static. The '≈' sign appears between the two identical bars. 2s."),

("or someone who has consumed alcohol to the legal driving limit.",
 "Wide three-panel diagram on white. Panel 1: 'MULTIPLE CRISES' bar (depleted). Panel 2: '24HRS AWAKE' bar (same depletion). Panel 3: '0.08% BAC' bar (same depletion). A bold equals sign connects all three. Bold label: 'SAME IMPAIRMENT.'",
 "Wide three-panel diagram", "Flat, white", "The third equivalence — makes the analogy undeniable",
 "Three identical depleted bars; 'SAME IMPAIRMENT' label",
 "Static. The third bar appears with the same depletion; the 'SAME IMPAIRMENT' label spans all three. 3s."),

("We don't look at an impaired driver and say the outcome reflects their character.",
 "Wide shot. A flat simple car accident scene — a car off the road, a red 'IMPAIRED DRIVER' label. A speech bubble from an observer reads 'THIS REFLECTS HIS CHARACTER' — with a large bold red X over the speech bubble.",
 "Wide shot", "Flat, white", "The analogy applied — we already know better",
 "Accident scene; red X over character-blame speech bubble",
 "Static. The red X stamps over the character-blame bubble. 2s."),

("We say: the condition impaired the judgment.",
 "Medium shot on white. A bold green speech bubble replaces the red-X'd one: 'THE CONDITION IMPAIRED THE JUDGMENT.' Clean and authoritative. The impaired-driver icon beside it is treated as a neutral data point.",
 "Medium shot", "Flat, white", "The correct frame stated — calm and clinical",
 "Green speech bubble with correct framing; neutral icon",
 "Static. The green bubble fills in with the correct statement. 2s."),

("Financial scarcity is the condition.",
 "Close-up on white. Bold centered text: 'FINANCIAL SCARCITY = THE CONDITION.' Below it, a flat icon of an empty wallet, a bill stack, and a near-zero bank balance — all equal-signed to the word 'CONDITION.' Clean and exact.",
 "Close-up, centered", "Flat, white", "The definition locked — scarcity = condition",
 "Bold equation with financial scarcity icons",
 "Static. The equals sign links scarcity icons to 'THE CONDITION' label. 2s."),

("The decisions are the symptom.",
 "Close-up on white. Bold centered text: 'THE DECISIONS = THE SYMPTOM.' Below it, a small symptom flowchart: CONDITION → BANDWIDTH TAX → DECISIONS. Arrow chain. Clean and clinical.",
 "Close-up, centered", "Flat, white", "The causal chain completed — reframe is done",
 "Bold equation with symptom flowchart",
 "Static. The flowchart arrows draw in sequence: condition to tax to decisions. 3s."),

# ── THE SLACK ──────────────────────────────────────────────────────────────────

("Mullainathan and Shafir identified the single factor that separates people who escape the tunnel from those who don't.",
 "Medium shot, warm beige interior with ceiling spotlight. The character faces camera, composed. Behind them, a simple flat diagram: two paths from the tunnel — one emerging, one staying inside. The brain inside the skull raises one arm toward the emerging path. Bold label: 'THE SINGLE FACTOR.'",
 "Medium shot", "Warm beige, ceiling spotlight", "The answer is coming — setup is deliberate",
 "Character beside two-path tunnel diagram; brain pointing",
 "Static. The brain's raised arm holds pointing at the escape path; the label materializes. 3s."),

("They called it slack.",
 "Close-up on white. A single bold word centered: 'SLACK.' Below it, a wide flat horizontal bar with a generous empty section at the right end — unused capacity clearly visible, drawn in calm green. Clean and visually satisfying.",
 "Close-up, centered", "Flat, white", "The concept arrives — visually intuitive",
 "Bold 'SLACK.' label; bar with generous unused green section",
 "Static. The green unused section of the bar glows softly once. 2s."),

("Slack is not wealth. Slack is unused capacity.",
 "Wide split panel on white. Left 'WEALTH ✗' — a tall pile of gold coins with a red X. Right 'UNUSED CAPACITY ✓' — the bandwidth bar with a healthy unused green portion, green check. Bold label: 'SLACK = UNUSED CAPACITY.'",
 "Wide split panel", "Flat — red X left, green check right", "Definition precise — slack ≠ wealth",
 "Wealth red-X'd; unused capacity green-checked",
 "Static. Both panels show their labels simultaneously; the red X and green check both appear. 2s."),

("A person with a ten-thousand-dollar emergency fund has slack.",
 "Medium shot, warm neutral background. A calm character stands beside a simple flat bank account icon showing '$10,000 EMERGENCY FUND' in green. Expression relaxed. A generous green section sits unused in the bandwidth bar above the skull.",
 "Medium shot", "Flat, warm neutral, green tones", "Slack illustrated — concrete and calming",
 "Calm character beside $10,000 emergency fund; green bandwidth slack",
 "Static. The green slack section glows steadily; the character's expression is easy. 2s."),

("A car repair does not become a crisis. A missed shift does not spiral into a payday loan into debt into cognitive overload.",
 "Wide diagram on white. Two branching paths from a 'CAR REPAIR' or 'MISSED SHIFT' node: Top path (no slack) — spiraling downward arrows through 'PAYDAY LOAN → DEBT → COGNITIVE OVERLOAD.' Bottom path (slack) — a flat horizontal arrow: 'ABSORBED → NO SPIRAL.' Bold contrast.",
 "Wide branching diagram", "Flat, white — red spiral top, green flat bottom", "The spiral vs. the absorption — the difference made visual",
 "Spiral path vs. flat absorbed path from same event",
 "Static. The top spiral path draws downward in red; the bottom flat path stays green and calm. 3s."),

("The spiral never starts because the slack absorbed the shock.",
 "Medium shot, warm neutral. The character stands calmly beside a shock-absorber icon (a simple flat spring) that has compressed and released between a 'CRISIS' label and the character — absorbing it. Bold label: 'SPIRAL NEVER STARTS.'",
 "Medium shot", "Flat, warm neutral", "The mechanism of slack — prevention, not cure",
 "Shock-absorber icon absorbing crisis; 'SPIRAL NEVER STARTS' label",
 "Static. The spring absorber compresses and releases once; the 'SPIRAL NEVER STARTS' label holds. 2s."),

("A person with no slack — accounts at zero, no credit, no buffer — has no room for error.",
 "Wide shot. A character stands on a flat platform with zero clearance on all sides: a '₀' bank account icon, a 'NO CREDIT' label, a 'NO BUFFER' label. The platform has no safety margin. Everything at the edge. Tense.",
 "Wide shot", "Flat, slightly tense gray-white", "Zero margin — the cliff edge",
 "Character on zero-margin platform; no-buffer labels",
 "Static. Each zero-margin label appears around the platform's edges. 3s."),

("Any disruption triggers the tunnel.",
 "Wide shot. The zero-margin character from the previous scene; a single small disruption icon (a minor bill, a minor car issue) appears — and the dark oval tunnel mouth immediately opens behind the character. The drop-in is instant.",
 "Wide shot", "Flat — dark tunnel opens instantly behind character", "No buffer = immediate tunnel — the fragility shown",
 "Minor disruption icon; tunnel mouth opening instantly behind character",
 "Static. The tunnel mouth snaps open behind the character as the disruption icon appears. 2s."),

("And the tunnel produces exactly the behaviors that look, from the outside, like bad character.",
 "Wide shot from outside the tunnel. The dark tunnel mouth is visible; inside, faint silhouettes of the behaviors — a payday loan acceptance, a skipped bill — are visible only dimly. From outside, bold labels float above: 'LOOKS LIKE BAD CHARACTER.' But the observer perspective is outside the tunnel.",
 "Wide shot from outside tunnel", "Flat — dark tunnel interior, clear observer outside", "The external misread — the view from the wrong side",
 "Observer outside tunnel; bad-character labels hovering; behaviors barely visible inside",
 "Static. The 'LOOKS LIKE BAD CHARACTER' labels float above the tunnel from outside; inside the behaviors are dimly lit. 3s."),

("Here is the finding that should be taught in every economics class in the world.",
 "Wide establishing shot of a flat classroom. A teacher figure writes on a chalkboard. Bold chalkboard text: 'THE SLACK FINDING.' Multiple small student figures sit attentive. Warm institutional light. Bold label: 'SHOULD BE TAUGHT EVERYWHERE.'",
 "Wide classroom shot", "Flat, warm institutional", "The finding elevated — it belongs in the curriculum",
 "Classroom scene with 'THE SLACK FINDING' on chalkboard",
 "Static. The chalkboard text fills in; student figures look up attentively. 3s."),

("When poor households received small cash transfers, their cognitive test scores improved immediately.",
 "Wide diagram on white. Timeline: left 'SMALL CASH TRANSFER' icon (green), then an immediate upward arrow labeled 'COGNITIVE TEST SCORES' rising to a higher bar. The improvement is instant. Bold label: 'IMMEDIATELY.'",
 "Wide diagram shot", "Flat, white, green upward arrow", "The finding — the brain responds immediately to slack",
 "Cash transfer to immediate score improvement timeline",
 "Static. The score bar rises immediately after the cash transfer icon appears; 'IMMEDIATELY' label appears. 3s."),

("Not after they spent the money. Before.",
 "Wide split panel on white. Left 'AFTER SPENDING ✗': character spending money, score flat. Right 'BEFORE SPENDING — JUST KNOWING IT EXISTS ✓': character with money in hand, not yet spent, score already risen. Bold 'BEFORE.' label.",
 "Wide split panel", "Flat, white", "Counterintuitive — knowledge of slack is enough",
 "Before-spending score rise vs. after-spending score",
 "Static. The right-panel score rises without the money being spent; the 'BEFORE.' label appears. 3s."),

("Simply knowing the buffer existed freed bandwidth.",
 "Close-up on white. The bandwidth bar inside the transparent skull, with a new generous green section opening up — not from spending, but from the awareness of the buffer. A small green 'BUFFER EXISTS ✓' icon causes the green section to expand. Quiet and precise.",
 "Close-up on skull, bandwidth bar", "Flat, white, green expanding", "The mechanism — cognition, not cash",
 "Green bandwidth slack expanding from buffer-knowledge icon",
 "Static. The green slack section expands as the 'BUFFER EXISTS ✓' icon appears. 2s."),

("The money didn't change their intelligence.",
 "Medium shot on white. A bold red X over 'CHANGED THEIR INTELLIGENCE.' The character stands calmly beside it, composed. IQ bar unchanged on a nearby chart.",
 "Medium shot", "Flat, white", "Intelligence constant — the variable is identified precisely",
 "Red X over 'CHANGED THEIR INTELLIGENCE'; stable IQ bar",
 "Static. The red X draws across the phrase; the IQ bar stays flat. 2s."),

("The slack changed their cognitive availability.",
 "Close-up diagram. Two bandwidth bars side by side: left 'BEFORE SLACK' — mostly consumed, tiny available sliver. Right 'WITH SLACK' — large green available section. A bold '→ SLACK CHANGED THIS' arrow points from left to right. The change is dramatic.",
 "Close-up diagram", "Flat, white — red left, green right", "The mechanism complete — slack = available bandwidth",
 "Before-slack vs. with-slack bandwidth bars; arrow label",
 "Static. The right bar's green section expands dramatically; the arrow label appears. 3s."),

# ── THE ENDING ─────────────────────────────────────────────────────────────────

("The story we tell about poverty is a story about character.",
 "Medium shot, neutral gray background. The character stands beside a simple flat storybook open to a page. The storybook reads 'A STORY ABOUT CHARACTER' with small icons of choices, values, discipline. The character reads it without expression — observing.",
 "Medium shot", "Flat, neutral gray", "The story named — it's about to be questioned",
 "Character observing the storybook; 'A STORY ABOUT CHARACTER' page",
 "Static. The storybook page holds open; the character's eyes scan it without judgment. 2s."),

("About choices. About values. About discipline.",
 "Close-up of the storybook page. Three bold chapter headers: 'CHOICES.' / 'VALUES.' / 'DISCIPLINE.' Each with a small icon. Clean, moralistic, slightly oppressive in its certainty.",
 "Close-up on storybook page", "Flat, neutral", "The story's contents — a moral framework about to be shattered",
 "Three chapter headers on storybook page",
 "Static. Each header appears in sequence with its icon. 2s."),

("It is a story that flatters the people telling it",
 "Medium shot, warm interior with ceiling spotlight. A group of three well-appointed character figures sit comfortably, storybook in hand, expressions pleased and self-satisfied. Warm, comfortable, unexamined.",
 "Medium shot interior", "Flat, warm comfortable", "The tellers — the flattery is their comfort",
 "Comfortable figures reading story with pleased expressions",
 "Static. One figure closes the book slightly with a satisfied nod. 2s."),

("and blames the people it describes.",
 "Split panel continuation. Right panel: the same storybook's moral judgment lands as a bold 'YOUR FAULT' arrow pointing at a struggling character figure, who accepts it with a lowered head. The contrast with the comfortable left-panel figures is sharp.",
 "Wide split panel", "Flat — warm left, cold gray right", "The injustice made visible — who pays and who profits from the story",
 "Comfortable tellers vs. blamed described figure",
 "Static. The 'YOUR FAULT' arrow appears on the right panel; the figure's head lowers. 3s."),

("The research tells a different story.",
 "Medium shot, warm beige interior with ceiling spotlight. The character faces camera, composed. The storybook from before is closed. A new flat research document opens beside them. Bold label: 'A DIFFERENT STORY.'",
 "Medium shot, direct address", "Warm beige, ceiling spotlight", "The turn — the research replaces the narrative",
 "Old storybook closed; research document open; label",
 "Static. The research document opens; the storybook closes. The label appears. 2s."),

("Being poor is not a moral condition. It is a cognitive one.",
 "Wide split panel on white. Left 'MORAL CONDITION ✗' — red X over a scales-of-justice icon. Right 'COGNITIVE CONDITION ✓' — green check beside the bandwidth bar and brain diagram. Bold bridging label: 'NOT MORAL. COGNITIVE.'",
 "Wide split panel", "Flat — red X left, green check right", "The redefinition — clean and final",
 "Moral condition red-X'd; cognitive condition green-checked",
 "Static. Both panel labels appear simultaneously; the green check gleams. 3s."),

("The brain making bad decisions inside the tunnel is not a broken brain.",
 "Close-up inside the dark tunnel. The character's brain — shown inside the tunnel, working frantically in the narrow bright focus — with a bold red X over the label 'BROKEN BRAIN.' The brain is working. It is not broken.",
 "Close-up inside tunnel, skull view", "Flat, dark tunnel — brain clearly working", "Compassion — the brain is not at fault",
 "Brain working in tunnel; 'BROKEN BRAIN' red-X'd",
 "Static. The red X draws across 'BROKEN BRAIN'; the brain continues working in the tunnel. 2s."),

("It is a human brain doing exactly what evolution designed it to do —",
 "Medium shot, split: left — an ancient flat landscape, a prehistoric figure's brain glowing gold and focused on an immediate threat (a predator). Right — the same brain structure, same glow, in a modern financial crisis. Bold label: 'DOING EXACTLY WHAT IT WAS DESIGNED TO DO.'",
 "Wide split panel", "Flat — warm ancient left, modern right", "Evolution — the function is correct, the context is wrong",
 "Ancient brain response vs. modern brain response — identical mechanism",
 "Static. Both brain glows appear simultaneously in their respective contexts; the label spans both. 3s."),

("tunnel on the immediate threat, at the cost of everything else.",
 "Wide inside-tunnel shot. The bright focal point blazes on the immediate threat; everything peripheral is in complete darkness. Cost icons — planning, foresight, long-term thinking — all sit dark outside the tunnel walls. Bold label: 'AT THE COST OF EVERYTHING ELSE.'",
 "Wide inside-tunnel shot", "Flat, dark tunnel — blazing focal center", "The evolutionary trade-off visualized",
 "Bright threat focus; cost icons dark outside tunnel",
 "Static. The peripheral cost icons fade even further into the dark; the focal center blazes. 3s."),

("The same mechanism that kept your ancestors alive by focusing on the predator directly in front of them",
 "Wide shot, ancient flat landscape. A prehistoric character figure stares at a large predator icon directly ahead; the brain inside the skull blazes gold with hyper-focus. Everything to the sides is ignored. Warm earthy tones.",
 "Wide shot, ancient setting", "Flat, warm earthy", "The ancestral function — the design had a purpose",
 "Prehistoric character focused on predator; gold brain",
 "Static. The gold brain blazes; the predator icon holds center frame; peripheral elements fade. 3s."),

("is the mechanism that traps millions of people in financial crisis today.",
 "Wide modern shot. A vast grid of character figures, each inside their own dark oval tunnel, all focused on immediate financial crisis icons at the bright ends. A bold bridging label: 'SAME MECHANISM — TODAY.' The scale is staggering.",
 "Wide modern shot, grid of tunnels", "Flat, dark — multiple bright focal points", "The same brain, the wrong context — millions trapped",
 "Grid of characters in individual tunnels; 'SAME MECHANISM TODAY' label",
 "Static. The grid of tunnels holds; the 'SAME MECHANISM — TODAY' label sweeps across. 3s."),

("Your brain was never broken. It was just never built for this.",
 "Medium close-up of the main character, calm and dignified. The brain inside the skull is gently lit — neutral, unblamed, simply present. A bold label: 'NEVER BROKEN.' Below it: 'NEVER BUILT FOR THIS.' Warm soft tones. Compassionate.",
 "Medium close-up", "Flat, warm soft", "Absolution — calm and generous",
 "Calm character; gently lit brain; 'NEVER BROKEN' label",
 "Static. The character exhales; the brain settles into a calm neutral expression. 2s."),

("But you can see the tunnel.",
 "Medium shot. The character stands outside a dark oval tunnel, looking at it calmly and clearly — not inside it, not panicking. A bold label: 'YOU CAN SEE IT.' The perspective of the observer, not the trapped.",
 "Medium shot", "Flat, neutral — dark tunnel visible but character outside it", "The first gift — perspective",
 "Character observing tunnel from outside; 'YOU CAN SEE IT' label",
 "Static. The character's gaze is calm and steady on the tunnel from outside. 2s."),

("You can understand the bandwidth tax before it finds you.",
 "Medium shot, warm beige interior with ceiling spotlight. The character holds the bandwidth bar concept — a simple flat diagram — at arm's length, studying it before the red scarcity block has arrived. Calm, preventive. Bold label: 'BEFORE IT FINDS YOU.'",
 "Medium shot", "Warm beige, ceiling spotlight", "Preventive understanding — learned in advance",
 "Character studying bandwidth diagram before scarcity arrives",
 "Static. The character examines the diagram; the red scarcity block is absent. 2s."),

("And you can build slack — before you need it, before the tunnel opens —",
 "Wide shot. The character is actively, calmly building: placing labeled green blocks ('EMERGENCY FUND,' 'BUFFER,' 'CUSHION') into a growing structure. The tunnel mouth is visible nearby but closed — not yet opened. Label: 'BUILD IT NOW.'",
 "Wide shot", "Flat, warm neutral — green blocks prominent", "Construction before crisis — the window is now",
 "Character building slack structure; closed tunnel nearby; 'BUILD IT NOW' label",
 "Static. The character places a green block on the structure; the tunnel mouth stays closed. 3s."),

("so that when the crisis comes, the spiral never starts.",
 "Wide diagram on white. A branching diagram: a crisis event on the left splits into two paths — top path (no slack) spiraling red downward; bottom path (with slack) absorbed by a green buffer, flat and stable. Bold label: 'SPIRAL NEVER STARTS.'",
 "Wide branching diagram", "Flat, white — red spiral top, green flat bottom", "The protection — the spiral pre-empted",
 "Two-path crisis diagram; spiral vs. absorbed",
 "Static. The top red spiral draws downward; the bottom green path holds flat. 3s."),

("Not because you are smarter than someone inside the tunnel.",
 "Wide split panel. Left: the character outside the tunnel, composed. Right: a character inside the tunnel, focused on their crisis — also clearly intelligent, also working hard. A bold 'NOT SMARTER' label bridges them. The intelligence is equal.",
 "Wide split panel", "Flat — light left exterior, dark tunnel right", "Not superiority — location is the variable",
 "Outside-tunnel character vs. inside-tunnel character; 'NOT SMARTER' bridge",
 "Static. The 'NOT SMARTER' label appears between the two panels. 2s."),

("Because you were outside it when you learned what it was.",
 "Wide split panel continued. A bold new label replaces 'NOT SMARTER': 'OUTSIDE IT WHEN YOU LEARNED.' The left-panel character now holds the research document — they learned while outside the tunnel. The right-panel character inside the tunnel holds nothing — they couldn't access the knowledge in time.",
 "Wide split panel", "Flat — light left, dark tunnel right", "The only difference — timing of learning",
 "Outside character with knowledge; inside character without",
 "Static. The 'OUTSIDE IT WHEN YOU LEARNED' label replaces the bridge; the outside character's document glows. 3s."),

("That is the only difference.",
 "Final medium shot. The main character faces camera, calm and clear. A single bold centered label: 'THE ONLY DIFFERENCE.' The brain inside the skull rests neutral — not a villain, not smug. Just present. Warm soft light. Conclusive and still.",
 "Medium shot, direct address", "Flat, warm soft light", "The conclusion — quiet, earned, complete",
 "Character facing camera; 'THE ONLY DIFFERENCE' label; calm brain",
 "Static. The character holds a steady, open gaze. The warm light settles. 3s — final frame."),

]


def shade(cell, hexcolor):
    from docx.oxml.ns import nsdecls
    from docx.oxml import parse_xml
    cell._tc.get_or_add_tcPr().append(
        parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), hexcolor)))


def build():
    doc = Document()

    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(10.5)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("CRAYON CAPITAL — CLONE SESSION · VIDEO 3")
    run.bold = True
    run.font.size = Pt(18)

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = sub.add_run('"The Bandwidth Tax"  ·  Financial Scarcity & Cognitive Load')
    r.italic = True
    r.font.size = Pt(12)

    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    meta.add_run("Neuroeconomics · English · {} beats (3–5s each)".format(len(BEATS))).font.size = Pt(9)

    doc.add_paragraph()

    h = doc.add_paragraph()
    h.add_run("VISUAL STYLE PROFILE (locked — embedded in every prompt for standalone use)").bold = True
    p = doc.add_paragraph(STYLE)
    p.paragraph_format.space_after = Pt(6)

    doc.add_paragraph()
    h = doc.add_paragraph()
    h.add_run("STATES 8 & 9 — IMAGE PROMPTS + VIDEO PROMPTS").bold = True
    doc.add_paragraph("Every script segment covered. Each image prompt is fully standalone. "
                      "Each beat = max 3–5 seconds of narration.").runs[0].italic = True

    for i, (seg, scene, cam, light, mood, action, video) in enumerate(BEATS, 1):
        doc.add_paragraph()
        bh = doc.add_paragraph()
        br = bh.add_run("BEAT {}".format(i))
        br.bold = True
        br.font.size = Pt(12)
        br.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

        sp = doc.add_paragraph()
        sr = sp.add_run('"{}"'.format(seg))
        sr.bold = True
        sr.italic = True

        tbl = doc.add_table(rows=0, cols=2)
        tbl.style = 'Table Grid'
        tbl.autofit = True

        def row(label, value, fill=None):
            cells = tbl.add_row().cells
            lr = cells[0].paragraphs[0].add_run(label)
            lr.bold = True
            lr.font.size = Pt(9)
            cells[0].width = Inches(1.15)
            vp = cells[1].paragraphs[0]
            vp.add_run(value).font.size = Pt(9.5)
            if fill:
                shade(cells[0], fill)

        row("IMAGE PROMPT", "{} {}".format(STYLE, scene), "FDECEC")
        row("Camera", cam)
        row("Lighting", light)
        row("Mood", mood)
        row("Action", action)
        row("VIDEO PROMPT", video, "EAF3FB")

    docx_path = "/home/user/Claudeeee/Bandwidth_Tax_Production.docx"
    doc.save(docx_path)
    print("Saved DOCX:", docx_path, "| {} beats".format(len(BEATS)))


if __name__ == "__main__":
    build()
