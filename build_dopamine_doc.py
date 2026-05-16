#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'Por que comprar se siente mejor que tener' (The Dopamine Trap)."""

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
("You didn't choose to buy it.",
 "Medium shot, white background. The main character stands facing camera, face neutral and unaware. Inside the transparent skull the pink villain brain points one small arm downward, issuing a silent command the character below doesn't notice.",
 "Medium shot, centered", "Flat, white", "Unsettling calm — controlled without knowing it",
 "Brain points downward smugly; character face blank",
 "Static shot. The brain slowly lowers its pointing arm and smirks. Character blinks once, oblivious. 2s subtle loop."),

("Your brain did. About 200 milliseconds before you even knew you wanted it.",
 "Close-up on the transparent skull only. The pink villain brain glows with a yellow electric halo, one arm raised in triumph. A small floating digital readout beside it reads '0.2s' in bold black.",
 "Close-up on skull/brain", "Flat, yellow glow from brain", "Revelation — the brain is faster than you",
 "Brain arm raised, electric glow pulsing, '0.2s' readout",
 "Static. Yellow halo pulses outward twice; the '0.2s' readout flickers in. Brain grins. 2s."),

("That's not a metaphor. That's a neuroscience study.",
 "Medium shot, white background. Character stands at a simple podium presenting a flat white document labeled 'NEUROSCIENCE STUDY' in bold black. The brain inside the skull waves smugly at camera.",
 "Medium shot", "Flat, white", "Dry, matter-of-fact with irony",
 "Character presents document; brain waves",
 "Static. Character lifts the document slightly; brain gives a small two-finger wave. 2s."),

("And it's the most expensive thing nobody ever taught you.",
 "Wide shot of a simple flat classroom. Chalkboard lists MATH, HISTORY, SCIENCE, ENGLISH and one conspicuously empty slot with a faint un-filled dollar-sign-and-brain outline. Small cartoon students at desks, a teacher at front. Warm beige tones.",
 "Wide establishing shot", "Flat, warm beige ambient", "Ironic absence — what's missing is loud",
 "Static scene; empty chalkboard slot visually emphasized",
 "Slow push-in toward the empty chalkboard slot; faint outline flickers. 3s."),

("Here's what actually happens when you tap \"buy now.\"",
 "Close-up of a beige cartoon hand hovering one frame above a flat smartphone showing a large green 'BUY NOW' button. A faint dotted arrow rises from the phone toward an off-frame skull. Dark background for contrast.",
 "Close-up on hand and phone", "Flat, green button glow", "Anticipation — the moment before the trigger",
 "Finger hovering, about to tap",
 "Static. The finger lowers a few pixels toward the button and holds; green button pulses once. 2s."),

("A region deep inside your brain called the nucleus accumbens fires a shot of dopamine",
 "Close-up flat cross-section of a pink cartoon brain on white. A central region labeled 'NUCLEUS ACCUMBENS' with a small arrow glows bright gold and emits tiny cartoon lightning bolts.",
 "Close-up diagram", "Flat, gold glow on one region", "Scientific, slightly ominous",
 "Lightning bolts radiating from the glowing region",
 "Static diagram. The labeled region pulses gold; three tiny lightning bolts flick outward in sequence. 3s."),

("— the same chemical released by cocaine, gambling, and sex.",
 "Wide three-section split panel on white. Left: small white powder pile with a bold red X. Center: a slot machine showing three 7s with coins falling. Right: two floating cartoon hearts. All three connect downward by one arrow to a single bold label 'SAME CHEMICAL.'",
 "Wide split panel", "Flat, white", "Shocking equivalence",
 "Coins falling from slot machine; hearts drifting",
 "Static panels. Slot coins fall in a short loop; hearts bob; the 'SAME CHEMICAL' label flashes once. 3s."),

("Not after the package arrives. Not when you open it. The moment you decide to buy.",
 "Horizontal three-step timeline on white. Step 1 'DECIDE' — hand tapping BUY NOW with a large gold star-burst. Step 2 'RECEIVE' — gray delivery box, no burst. Step 3 'OPEN' — character opening box, gray, no burst.",
 "Wide timeline panel", "Flat, gold burst on step 1 only", "Counterintuitive revelation",
 "Static timeline; emphasis on step 1 burst",
 "Static. The gold burst on 'DECIDE' expands and contracts once while steps 2 and 3 stay flat gray. 3s."),

("The anticipation is the high. The product is just the excuse.",
 "Wide split panel. Left 'ANTICIPATION': character tapping phone, brain blazing gold, eyes wide, arms up. Right 'THE PRODUCT': same character holding an open box, expression flat, brain gray and dim.",
 "Wide split panel", "Flat — gold left, gray-dim right", "Melancholic irony",
 "Excitement vs. deflation contrast",
 "Static split. Left brain glows brighter; right brain dims further; character's right-side shoulders slump. 3s."),

("And the second it arrives, the dopamine is already gone.",
 "Medium shot, simple hallway interior. Character at an open door holding a cardboard box, expression flat. Brain inside skull gray and half-lidded. A faded yellow wisp floats up and away from the skull like dissipating smoke.",
 "Medium shot in doorway", "Flat, faded yellow wisp rising", "Emptiness after the high",
 "Yellow dopamine wisp floating away; flat expression",
 "Static. The yellow wisp drifts upward and fully dissolves; character's eyes lower slightly. 3s."),

("Which is exactly why you're already looking at the next thing.",
 "Medium shot, white background. Character holds the just-opened box loosely in one arm while the other hand already holds a phone; eyes locked on the screen; brain re-illuminated with fresh yellow glow. Box tilts, forgotten.",
 "Medium shot", "Flat, fresh yellow glow returning", "Compulsive loop restarting",
 "Eyes on phone, box neglected, brain glowing again",
 "Static. The box tilts a few degrees lower while the brain's yellow glow brightens. 2s loop."),

("Let's go back to 1954. Montreal.",
 "Wide establishing shot of a simplified 1950s cityscape: flat rectangular buildings, vintage car silhouettes, muted gray-blue palette. Lower-left text card reads 'MONTREAL — 1954' in bold black. No characters.",
 "Wide establishing shot, slight low angle", "Flat, cool gray-blue, overcast", "Historical, clinical scene-set",
 "Static establishing shot",
 "Very slow push-in on the cityscape; the 'MONTREAL — 1954' card fades in. 3s."),

("Two neuroscientists named James Olds and Peter Milner are running an experiment on rats.",
 "Medium-wide flat laboratory interior: counters, beakers, clipboards. Two small cartoon scientists in white coats and blue-tint glasses look down at a glass enclosure on a table containing a small cartoon rat. Warm lab light.",
 "Medium-wide lab interior", "Flat, warm laboratory yellow-white", "Clinical, slightly ominous",
 "Scientists observing the rat, clipboards in hand",
 "Static. One scientist makes a small note on the clipboard; the rat shifts inside the enclosure. 3s."),

("They implant tiny electrodes directly into the reward centers of rat brains.",
 "Close-up flat medical-diagram cross-section of a rat skull with a simplified brain inside. Two tiny electrode wires enter the center with small glowing gold tips. A label reads 'REWARD CENTER' with an arrow. White background.",
 "Close-up diagram", "Flat, gold glow at electrode tips", "Precise, invasive science",
 "Electrode tips glowing at the insertion point",
 "Static diagram. The two gold electrode tips pulse once in sync. 2s."),

("Then they give each rat a lever. Press the lever, get a dopamine hit. Direct. Instant.",
 "Medium shot, light gray background. A cartoon rat inside a simple glass box rests one paw on a small lever. Above its head a gold burst labeled 'DOPAMINE' in bold. Rat intensely focused.",
 "Medium shot inside enclosure", "Flat, gold burst above rat", "Deceptively clean cause-and-effect",
 "Paw presses lever; dopamine burst appears",
 "Static. The rat presses the lever; the gold 'DOPAMINE' burst pops and fades, then repeats. 2s loop."),

("No effort required. The rats stopped eating.",
 "Medium shot, light gray. The rat sits with its back to a full food bowl (faint gray X over it), facing the worn lever instead.",
 "Medium shot", "Flat, neutral gray", "Disturbing in its simplicity",
 "Rat faces lever; food bowl untouched",
 "Static. The rat's head turns briefly toward the bowl, then snaps back to the lever. 2s."),

("They stopped sleeping. They stopped doing anything except pressing the lever.",
 "Wide interior of the glass enclosure. The worn lever is center frame; the rat presses it with both paws, eyes wide and compulsive. Untouched food, water bottle, and an empty nest sit in the corners.",
 "Wide interior shot", "Flat, slightly cold gray", "Obsession — everything else abandoned",
 "Rat gripping lever; all else untouched",
 "Static. The rat's paws pump the lever in a tight repetitive loop. 2s loop."),

("Over and over. Thousands of times per hour. Until some of them died.",
 "Extreme close-up on the worn, slightly tilted lever. A counter above reads '4,847×' in bold. A small rat paw is visible at the bottom still pressing.",
 "Extreme close-up on lever and counter", "Flat, white", "Compulsive horror as a number",
 "Paw pressing; counter ticking",
 "Static. The counter number rapidly increments; the paw keeps pressing. 3s."),

("The scientists stood there watching, slowly realizing they hadn't just discovered something about rats.",
 "Medium shot of the two scientists, clipboards now lowered to their sides, mouths slightly open, expressions shifted from clinical to alarmed. The rat enclosure is behind them.",
 "Medium shot on scientists", "Flat, same warm lab light, shifted mood", "Dawning realization",
 "Clipboards lowered; scientists frozen",
 "Static. One scientist's clipboard slips a little lower; both stare without moving. 3s."),

("They had found the override switch for any brain complex enough to want things.",
 "Close-up of the pink villain brain on white. A single large ON/OFF switch in the upright ON position glows gold at its center. Bold label below: 'OVERRIDE.' Brain smirks knowingly.",
 "Close-up, centered", "Flat, gold glow on switch", "Ominous — this applies to you",
 "Switch ON; brain smirking",
 "Static. The switch's gold glow intensifies; the brain's smirk widens slightly. 2s."),

("Including yours.",
 "Close-up of the main character's neutral face on gray. Inside the transparent skull the same ON/OFF 'OVERRIDE' switch sits in the ON position, glowing faint gold. A small red arrow labeled 'YOU' points at the character.",
 "Close-up on character", "Flat, gray, faint gold in skull", "Direct accusation — it's you",
 "Switch glowing inside the viewer-character's skull",
 "Static. The 'YOU' arrow nudges in; the skull switch glows once. 2s."),

("The lever changed shape. But the experiment never ended.",
 "Wide horizontal timeline on white. Left: a 1950s wood-and-metal lever. Center: a 2000s flip phone. Right: a modern smartphone with a glowing green 'BUY NOW' button. One dotted arrow runs left to right. Label: 'SAME EXPERIMENT.'",
 "Wide timeline panel", "Flat, white, slight glow on smartphone", "Continuity of manipulation across time",
 "Static progression left to right",
 "Static. The dotted arrow draws itself left to right; the smartphone button pulses at the end. 3s."),

("Fast forward. You wake up and check your phone before your feet hit the floor.",
 "Wide flat bedroom: bed, pillow, warm orange light from a window. The character lies in bed, eyes just opened, already holding a phone up to their face, feet still under the covers. Brain inside skull already glowing gold.",
 "Wide bedroom shot", "Warm amber morning light from window", "Automatic behavior before consciousness arrives",
 "Eyes open, phone already raised, brain glowing",
 "Static. The character's eyes open from shut to half; the phone screen flicks on; brain glows. 3s."),

("You open an app. The feed refreshes. New content loads. Your nucleus accumbens fires.",
 "Close-up of a phone screen showing a flat feed of content cards, a spinning loader, then new cards. A gold beam shoots upward from the screen toward a partially visible skull at the top of frame. Dark background.",
 "Close-up on phone, partial skull above", "Flat, gold beam from screen upward", "Automated, effortless trigger",
 "Feed refreshing; gold beam firing upward",
 "Static. The loader spins, new cards snap in, and the gold beam flashes upward on each refresh. 3s loop."),

("You scroll to trigger it again. You weren't looking for anything specific. You were pressing the lever.",
 "Medium shot, gray background. Character seated, thumb scrolling a blurred fast-moving feed. The brain inside the skull flashes gold two or three times. Face blank and automatic.",
 "Medium shot", "Flat, gold pulses with each scroll", "Mindless loop — the 2025 lever",
 "Thumb scrolling; brain pulsing per scroll",
 "Static frame, thumb scrubs up repeatedly; brain flashes gold with each motion. 2s loop."),

("Then you see it. A product. A deal. A countdown timer.",
 "Close-up of a phone screen: a flat product ad with bold red 'LIMITED TIME', a countdown timer, a generic product center-screen, and a large green 'BUY NOW' button. A warm glow pulls focus. Dark background.",
 "Close-up on phone screen", "Flat, warm glow from screen", "The trap appears disguised as opportunity",
 "Countdown running; button prominent",
 "Static. The countdown digits tick down; the green button gives a slow attention pulse. 3s."),

("Something you didn't know you needed forty seconds ago.",
 "Wide split panel on white. Left '0:40 AGO': character sitting calmly, no phone, empty thought bubble. Right 'NOW': same character leaning toward the phone, hand over the buy button, thought bubble filled with the product.",
 "Wide split panel", "Flat, white", "Speed of manufactured desire",
 "Empty thought bubble vs. product-filled bubble",
 "Static split. The right thought bubble fills in with the product image while the left stays empty. 3s."),

("Your brain doesn't consult your savings account. It doesn't ask whether you can afford it.",
 "Wide shot on white. Three flat documents — a savings statement, a credit card statement, a budget sheet — lie face-down or X-marked, ignored. The villain brain stands to the side, back turned to all three, arms crossed.",
 "Wide shot of documents and brain", "Flat, white", "Willful ignorance by design",
 "Brain turned away; documents ignored",
 "Static. The brain flicks one dismissive arm without turning around; a document slides slightly. 2s."),

("It feels the anticipation of acquisition",
 "Medium shot, warm gold tones. The character's transparent skull fills with a rising wave of golden liquid; the villain brain rides the crest with arms raised. Character's eyes wide, mouth open with excitement.",
 "Medium shot, centered", "Flat, warm golden glow from within skull", "The flood — overwhelming in the moment",
 "Dopamine wave rising; brain surfing it",
 "Static. The golden liquid rises higher in the skull; the brain rides the crest upward. 2s."),

("and floods your system with the chemical that was built to make you act before you think.",
 "Medium shot. The golden flood now overflows the skull and runs down the character's whole body as glowing gold lines. The small bespectacled 'prefrontal cortex' figure is swept off its feet by the flood inside the skull.",
 "Medium shot", "Flat, gold flood lines down body", "Reason overwhelmed by chemistry",
 "Flood overflowing; rational figure swept away",
 "Static. Gold lines stream down the body; the tiny prefrontal figure tumbles in the flood. 3s."),

("And you tap buy now.",
 "Extreme close-up of a cartoon finger making contact with a glowing green 'BUY NOW' button on a phone. A small gold burst at the contact point. Dark background.",
 "Extreme close-up", "Flat, green glow + gold tap burst", "Point of no return — simple and final",
 "Finger contacts button; burst at tap point",
 "Static. The finger presses down; the gold burst pops at the contact point and fades. 1.5s."),

("This is not weakness. This is not a character flaw.",
 "Wide split panel on white. Left: a small wilted sad figure labeled 'WEAKNESS?' with a bold red X over the label. Right: the same character standing upright, neutral, labeled 'NOT THE CAUSE' in clean black.",
 "Wide split panel", "Flat, white", "Reframing — removing self-blame",
 "Static contrast panels",
 "Static. The red X strikes through 'WEAKNESS?'; the right figure straightens posture slightly. 2s."),

("This is the most sophisticated consumer psychology operation in human history working exactly as designed.",
 "Wide flat control room: walls of screens showing graphs, heat maps, behavior data. Small villain-brain figures in lab coats work the panels. A central screen shows the character's silhouette tagged with behavioral-trigger arrows. Cool blue-gray.",
 "Wide establishing shot", "Flat, blue-gray ambient, screens glow", "Scale of the operation — vast, deliberate",
 "Brain operators at panels; data on screens",
 "Static. Graphs on the screens animate subtly; one brain operator turns a dial. 3s."),

("On you. Every single day.",
 "Close-up of the main character's neutral face; behind them a vast flat grid of hundreds of identical character silhouettes receding into the distance. A small red arrow above the front character reads 'YOU.'",
 "Close-up character, wide grid behind", "Flat, gray", "Scale of targeting — singled out in a crowd",
 "'YOU' arrow points; identical grid behind",
 "Static. The 'YOU' arrow bounces once; the grid behind shifts a hair to feel endless. 2s."),

("Meet two people. Same income. Same city. Same year.",
 "Wide perfectly symmetrical split panel on white. Left: a female cartoon character (Dana) in the channel's style. Right: a male character (Marcus), mirrored, identical apartment backgrounds. Centered labels: 'SAME INCOME / SAME CITY / SAME YEAR.'",
 "Wide symmetrical split panel", "Flat, white", "Setup — equality before divergence",
 "Static symmetrical positioning",
 "Static. The three centered labels fade in one by one. 3s."),

("The first one, call her Dana, grew up watching her parents check price tags.",
 "Medium shot, warm muted grocery aisle. Young Dana (smaller version of the female character) watches two adult parent figures thoughtfully examine a price tag on a product.",
 "Medium shot", "Flat, warm muted store tones", "Formative observation — learning by watching",
 "Parents examine price tag; child observes",
 "Static. The parent turns the product to read the tag; young Dana's eyes track it. 3s."),

("Budget was a word she heard at the dinner table.",
 "Medium shot of a simple flat dining table, family of three seated, food on table. A speech bubble from a parent reads 'BUDGET' in bold black. Young Dana listens. Warm amber dining room.",
 "Medium shot of table scene", "Flat, warm amber", "Normalization of money awareness",
 "Speech bubble visible; family seated",
 "Static. The 'BUDGET' speech bubble pops in; young Dana's head turns toward the parent. 2s."),

("She learned early that money required decisions, and decisions required a pause.",
 "Medium shot, white background. Teen Dana holds a product in one hand, a wallet in the other; a large pause symbol (two vertical bars) floats between them. Thoughtful, not anxious. Her brain inside the skull looks calm, not villainous.",
 "Medium shot", "Flat, white", "Practiced pause — healthy friction as habit",
 "Pause symbol floating between product and wallet",
 "Static. The pause symbol gently pulses; Dana's eyes move from product to wallet. 2s."),

("She's never carried a credit card balance she couldn't pay in full at month's end.",
 "Close-up of a flat credit card statement, balance column reading '$0.00' in bold green with a small cartoon checkmark. Dana's hand visible at frame edge holding it. White background.",
 "Close-up on statement", "Flat, white, green text glow", "Clean, satisfying outcome",
 "Static close-up; checkmark visible",
 "Static. The green checkmark draws itself next to the '$0.00'. 2s."),

("Not because she has extraordinary self-control.",
 "Medium shot, gray background. Dana stands relaxed; her brain inside the skull is calm and benign (normal eyes, no smirk). No phones, timers, or buttons anywhere around her.",
 "Medium shot", "Flat, gray", "Absence of the system — peace by default",
 "Calm brain; no external triggers present",
 "Static. Dana's calm brain blinks slowly; the empty space around her stays bare. 2s."),

("Because nobody ever spent a billion dollars optimizing her dopamine system against her.",
 "Split panel. Left: Dana with a calm brain and empty surroundings. Right: the blue-gray control room full of brain-operators — but every screen is blank/off, no target. Bold label bridging them: 'NO TARGET.'",
 "Wide split panel", "Flat — gray left, dim blue-gray right", "She was simply never aimed at",
 "Idle control room; blank screens",
 "Static. The right-side control screens stay dark; one brain operator shrugs. 3s."),

("The second one, call him Marcus, grew up in the era of one-click checkout,",
 "Medium shot of young Marcus surrounded by floating cartoon icons: a '1-CLICK' button, three notification bells with red dots, a small predictive algorithm chart. Slightly overwhelmed, eyes wide. Brain shows an early villain glow.",
 "Medium shot, icons surrounding subject", "Flat, faint red glow on notification icons", "Born into the system",
 "Icons orbiting Marcus; algorithm arrow ahead of him",
 "Static. The icons slowly orbit Marcus; the algorithm arrow inches ahead of him. 3s loop."),

("push notifications, and algorithms that learned his preferences faster than he did.",
 "Close-up of Marcus's profile beside a flat predictive chart that draws his next action before he makes it. A villain-brain analyst points at the chart with a small pointer. Cool blue-gray.",
 "Close-up on chart and profile", "Flat, blue-gray, screen glow", "Predicted before he chooses",
 "Chart predicting ahead of the user",
 "Static. The prediction line extends one step ahead; the brain analyst taps it. 3s."),

("Every platform he uses has a team of engineers",
 "Wide warm-beige office with ceiling spotlight. A long wooden table ringed by small villain-brain characters in lab coats holding clipboards and tools, all focused on one workstation.",
 "Wide interior shot", "Warm beige ambient, soft ceiling spotlight", "Systematic, deliberate",
 "Brain engineers gathered around a workstation",
 "Static. Two brain engineers lean toward the screen; one taps a pen on the clipboard. 3s."),

("whose entire job is to reduce the friction between his impulse and his purchase.",
 "Close-up of a whiteboard: a path from 'IMPULSE' to 'PURCHASE' with a wall labeled 'FRICTION' being knocked down by a villain brain with a hammer; a dial beside it turns to 'FRICTION: 0.'",
 "Close-up on whiteboard", "Flat, warm beige interior", "Friction engineered toward zero",
 "Brain knocking down the friction wall; dial to zero",
 "Static. The brain swings the hammer; the 'FRICTION' wall cracks; the dial rotates to 0. 3s."),

("They A/B tested the color of the buy button.",
 "Close-up of a board split into 'A' and 'B': panel A a green BUY NOW button, panel B an orange one, each with small performance bar charts. A lab-coat villain brain circles the winner in red marker. White background.",
 "Medium shot on board", "Flat, white", "Precision of manipulation",
 "Brain circling the winning button",
 "Static. The brain draws a red circle around panel A; its bar chart ticks up. 2s."),

("They studied exactly how long the confirmation animation should last to maximize the feeling of satisfaction.",
 "Medium shot, warm beige interior with ceiling spotlight. A lab-coat villain brain holds a stopwatch, staring at a phone showing a checkout confirmation (spinner to green checkmark). A clipboard reads 'OPTIMAL DURATION: 1.4 SECONDS.'",
 "Medium shot", "Warm beige, ceiling spotlight", "Engineered pleasure to the millisecond",
 "Brain timing the animation with a stopwatch",
 "Static. The confirmation spinner resolves to a checkmark; the stopwatch hand sweeps and the brain nods. 3s."),

("They built a machine calibrated to his specific psychology, and they run it twenty-four hours a day.",
 "Wide diagram shot, gray background. Marcus small at center, ringed by phone, laptop, smartwatch, and tablet — each with a tiny villain-brain icon on screen, all pointing arrows inward at him. A clock above reads '24:00.'",
 "Wide overhead-perspective diagram", "Flat, gray, faint device screen glow", "Total encirclement — no escape",
 "Devices all aimed inward at Marcus",
 "Static. The inward arrows pulse in sequence around the ring; the clock hand sweeps. 3s loop."),

("Marcus is not less intelligent than Dana.",
 "Wide symmetrical split panel on white. Left: Marcus standing, normal expression, normal brain. Right: Dana, same stance, same brain size. A bold black equals sign '=' between them.",
 "Wide symmetrical split panel", "Flat, white", "Fairness — not an intelligence gap",
 "Static equals sign between identical figures",
 "Static. The '=' sign draws itself in between the two; both blink simultaneously. 2s."),

("Marcus is just the primary target of something Dana never had to fight at scale.",
 "Same split panel. Over Marcus: a large red target crosshair and multiple inward arrows; bold red label 'TARGET.' Dana's side: empty, open, untargeted.",
 "Wide split panel", "Flat, white, red crosshair on Marcus", "Asymmetry revealed",
 "Crosshair over Marcus; Dana's side bare",
 "Static. The red crosshair locks onto Marcus with a small snap; Dana's side stays empty. 2s."),

("And here's what those engineers know that most people don't. Friction is the enemy of impulse.",
 "Wide diagram on white. Top: arrow labeled 'IMPULSE' slams into a wall labeled 'FRICTION' and stops dead. Bottom: arrow labeled 'IMPULSE' with no wall shoots straight into a shopping-cart icon. Bold black and red text.",
 "Wide diagram frame", "Flat, white", "Mechanical clarity — the exploit logic",
 "Static contrasting two paths",
 "Static. The top arrow hits the wall and stops; the bottom arrow zips into the cart. 3s."),

("Every second between want and buy is a second your prefrontal cortex",
 "Close-up of the character's head, warm beige interior. Transparent skull shows two regions: the larger villain brain, and a smaller bespectacled 'PREFRONTAL CORTEX' figure just starting to open its eyes. A small clock ticks between them.",
 "Close-up on skull interior", "Warm beige interior", "The rational brain stirring awake",
 "Prefrontal figure waking; clock ticking",
 "Static. The little prefrontal figure rubs its eyes and starts to stand; the clock ticks. 3s."),

("— the rational decision-making region of your brain —",
 "Close-up inside the skull. The small bespectacled 'PREFRONTAL CORTEX' figure now stands fully, holding a tiny clipboard and pen, alert. The villain brain looms larger beside it, watching sideways.",
 "Close-up on skull interior", "Flat, neutral", "The voice of reason, briefly present",
 "Prefrontal figure alert with clipboard",
 "Static. The prefrontal figure raises its clipboard; the villain brain narrows its eyes at it. 2s."),

("has time to wake up and ask the only question that matters: do I actually need this?",
 "Close-up inside the skull. The prefrontal figure holds up a small sign reading 'DO I ACTUALLY NEED THIS?' The villain brain looks annoyed, arms crossed.",
 "Close-up on skull interior", "Flat, neutral", "The decisive question",
 "Prefrontal figure raising the question sign",
 "Static. The sign lifts into view; the villain brain rolls its eyes. 2s."),

("So the entire system is engineered to eliminate those seconds.",
 "Close-up inside the skull. The villain brain slams a big 'SKIP' button; the prefrontal figure is shoved back down asleep; a small clock lies smashed on the skull floor.",
 "Close-up on skull interior", "Flat, white", "The override — reason eliminated by design",
 "Brain pressing SKIP; prefrontal figure knocked out",
 "Static. The brain's hand slams 'SKIP'; the prefrontal figure topples; clock pieces scatter. 2s."),

("One-click purchase. Saved payment information. Buy now, pay later. Same-day delivery.",
 "2x2 grid on white. (1) finger on a '1-CLICK' button, (2) a card stamped 'SAVED ✓', (3) a green 'BUY NOW PAY LATER' badge, (4) a delivery box stamped 'TODAY'. Each panel has a small green corner checkmark.",
 "2x2 grid panel", "Flat, white, green accents", "The arsenal listed clinically",
 "Static grid of four friction-removal tools",
 "Static. The four green checkmarks pop in one after another, clockwise. 3s."),

("No waiting. No pause between the dopamine spike and the damage to your account.",
 "Wide timeline on white: a gold dopamine burst on the left, an almost-nonexistent dotted gap, then a bank statement showing a negative balance on the right. A red bracket around the tiny gap labeled 'THIS IS THE GAP THEY REMOVED.'",
 "Wide timeline panel", "Flat, white, red bracket emphasis", "The missing gap — its absence is the harm",
 "Static timeline; tiny gap emphasized",
 "Static. The red bracket squeezes the gap until it nearly vanishes. 2s."),

("It works.",
 "Minimal close-up on white: a single green 'IT WORKS.' stamp slamming down over a faint outline of the character. Stark and simple.",
 "Close-up, centered", "Flat, white", "Cold, blunt confirmation",
 "Stamp slamming down",
 "Static. The 'IT WORKS.' stamp drops in with a tiny shake on impact. 1.5s."),

("The average American household carries over $21,000 in non-mortgage consumer debt.",
 "Medium-wide shot. A cartoon family of three stands before a simple house under a dark cloud with bold white '$21,000' inside it. Tired, slightly defeated expressions. Warm muted neighborhood.",
 "Medium-wide shot", "Flat, warm muted, dark cloud overhead", "The weight of the average, humanized",
 "Cloud hovering; family looking up",
 "Static. The dark cloud drifts lower over the family; one figure's shoulders drop. 3s."),

("Not because Americans are uniquely irresponsible.",
 "Medium shot of the same family on white. A large red X strikes through a bold label 'UNIQUELY IRRESPONSIBLE.' Their expressions are tired, not ashamed.",
 "Medium shot", "Flat, white", "Exoneration — misplaced blame removed",
 "Red X crossing out the blame label",
 "Static. The red X swipes across 'UNIQUELY IRRESPONSIBLE'; the family relaxes slightly. 2s."),

("Because Americans were the first generation to live inside a fully optimized dopamine extraction system",
 "Wide shot. A large flat machine — pipes, gauges, conveyor — encloses a small cartoon neighborhood; figures walk through it unaware. Label on the machine: 'DOPAMINE EXTRACTION SYSTEM.' Gold drops flow out into a corporate building. Gray industrial outside, warm inside.",
 "Wide establishing shot", "Flat, industrial gray outside / warm inside", "Invisible infrastructure lived inside",
 "Machine running; figures walking through unaware",
 "Static. The conveyor moves; gold drops flow along the pipe into the corporate building. 3s loop."),

("running in their pocket, on their wrist, and on every screen they look at",
 "Medium full-body shot, gray background. Character standing; phone in pocket glowing through fabric, smartwatch glowing on wrist, laptop screen glowing in front — each connected by a dotted line to the brain in the skull, which pulses gold.",
 "Medium full-body shot", "Flat, individual device glows to skull", "Total coverage of the day",
 "Three devices glowing, lines to the brain",
 "Static. Each device glow travels up its dotted line and the brain pulses gold in turn. 3s loop."),

("for an average of seven hours a day.",
 "Close-up of a flat clock face with the segment '7 HOURS' shaded gold and bold. Beside it, a small character silhouette staring into a glowing phone. White background.",
 "Close-up on clock", "Flat, white, gold 7-hour wedge", "The scale of daily exposure",
 "Clock wedge highlighted; silhouette transfixed",
 "Static. The gold 7-hour wedge fills in around the clock face. 2s."),

("The lever is everywhere now. And it never stops.",
 "Wide shot of a flat city street where ordinary objects all subtly become the 1950s lever: lamp posts, door handles, phone, ATM. Small character walking through, surrounded. Cool gray with gold lever accents.",
 "Wide street shot", "Flat, cool gray, gold lever accents", "Inescapable saturation",
 "Levers embedded everywhere; character walking through",
 "Static. The lever-shaped objects each give a tiny pulse as the character passes. 3s."),

("But here's the part they never put on the packaging. And this is the part that changes everything.",
 "Close-up of a flat product box, label reading 'DOPAMINE = PLEASURE ✓' in bold marketing type, with a large red X being drawn across it. A villain brain peeks from behind the box with a knowing smirk.",
 "Close-up on package", "Flat, white", "The lie about to be exposed",
 "Red X over the false label; brain peeking",
 "Static. The red X strokes across the label; the brain peeks further out and smirks. 2s."),

("Dopamine is not the pleasure chemical.",
 "Stark close-up on white. Bold black text 'PLEASURE CHEMICAL' with a heavy red strike-through. A small dim-gray brain sits beside it, unimpressed.",
 "Close-up, centered", "Flat, white", "Flat myth-busting statement",
 "Strike-through over the false phrase",
 "Static. The red strike-through draws across 'PLEASURE CHEMICAL'. 1.5s."),

("For decades, that's what science called it. The reward molecule. The feel-good neurotransmitter.",
 "Medium shot of a vintage flat textbook page or chalkboard listing 'DOPAMINE: reward molecule / feel-good neurotransmitter' in old-style type. A small scientist figure points at it confidently. Muted sepia tones.",
 "Medium shot on textbook/board", "Flat, muted sepia", "Established but outdated belief",
 "Scientist pointing at the old definition",
 "Static. The scientist taps the chalkboard line; a little chalk dust puffs. 2s."),

("But the research that came after tells a completely different story.",
 "Medium shot. The same chalkboard with the old definition now half-erased; a new bolder line being written: 'DOPAMINE = WANTING.' A different scientist with a fresh marker stands beside it. Cooler, brighter tones.",
 "Medium shot", "Flat, cooler bright tones", "Paradigm shift",
 "Old definition erased; new one written",
 "Static. The eraser wipes the old line; the new 'WANTING' line writes itself in. 3s."),

("Dopamine is not what you feel when you enjoy something.",
 "Medium shot, gray background. Character calmly eating, expression of genuine contentment — but the brain inside the skull is dim gray. Small label: 'ENJOYMENT — NO DOPAMINE.'",
 "Medium shot", "Flat, gray, dim brain", "Counterintuitive — pleasure without dopamine",
 "Calm eating; brain dim",
 "Static. The character chews slowly and contentedly while the brain stays dim gray. 2s."),

("Dopamine is what you feel when you anticipate something.",
 "Medium shot. Same character holding food near the mouth, eyes wide with anticipation — brain inside the skull blazing gold. Label: 'ANTICIPATION — DOPAMINE.'",
 "Medium shot", "Flat, blazing gold brain", "The true trigger revealed",
 "Food held near mouth; brain blazing",
 "Static. The food hovers near the mouth; the brain's gold glow flares brighter. 2s."),

("It's the hunger, not the meal. The wanting, not the having.",
 "Wide two-icon panel on white. Left: a growling empty stomach icon labeled 'HUNGER ← DOPAMINE' with gold glow. Right: a full plate labeled 'THE MEAL → NO DOPAMINE', no glow. Below: 'THE WANTING, NOT THE HAVING.'",
 "Wide icon panel", "Flat, white, gold glow on hunger side only", "Reductive clarity",
 "Static contrast icons",
 "Static. The gold glow pulses on the hunger icon while the meal icon stays flat. 2s."),

("Which means the system was never designed to satisfy you.",
 "Medium interior shot, warm beige, ceiling spotlight. A villain brain sits at a corporate desk, feet up, smug. Desk nameplate: 'KEEP THEM WANTING.' Framed wall chart shows a desire line that rises forever, never plateauing.",
 "Medium interior shot", "Warm beige, ceiling spotlight on desk", "Corporate deliberateness",
 "Brain relaxed at desk; ever-rising chart",
 "Static. The brain leans back further; the wall chart's line creeps upward. 3s."),

("It was designed to keep you wanting.",
 "Close-up of the wall chart from the previous scene: a desire curve climbing endlessly off the top of the frame, no peak, labeled 'DESIRE' with a small looping arrow. White-beige background.",
 "Close-up on chart", "Flat, warm neutral", "Endless by design",
 "Desire curve climbing without end",
 "Static. The desire curve extends upward and the looping arrow rotates once. 2s."),

("A satisfied customer stops spending. A wanting customer never does.",
 "Wide split panel. Left 'SATISFIED — STOPS': calm character, arms crossed, empty cart, red downward purchase chart. Right 'WANTING — NEVER STOPS': restless character surrounded by packages, green rising chart.",
 "Wide split panel", "Flat — red-tinted left, green-tinted right", "Business logic made visible",
 "Two contrasting charts and figures",
 "Static. The left chart ticks down; the right chart climbs and packages stack higher. 3s."),

("Satisfaction is a business risk. Desire is a business model.",
 "Close-up on white. Two bold framed signs side by side: 'SATISFACTION = RISK' (red) and 'DESIRE = BUSINESS MODEL' (green). A villain brain in a tiny tie stands between them, gesturing to the green one.",
 "Close-up on signs", "Flat, white", "The thesis stated bluntly",
 "Brain endorsing the 'DESIRE' sign",
 "Static. The brain points its arm toward the green 'DESIRE' sign and nods. 2s."),

("This is why the package arrives and the feeling is already fading.",
 "Medium shot, warm neutral background. Character holds a just-arrived box; the brain's gold glow visibly dissipates as yellow wisps float up and away. Flat, slightly blank expression.",
 "Medium shot", "Flat, warm neutral, fading gold wisps", "Post-purchase anti-climax",
 "Dopamine wisps rising; expression deflating",
 "Static. The gold wisps drift up and dissolve; the character's eyes lower. 3s."),

("This is why you've bought things you can barely remember.",
 "Wide warm interior with ceiling spotlight. A closet/storage room of unopened boxes and tagged items. Character stands before it scratching head, thought bubble with a question mark.",
 "Wide interior shot", "Warm interior, ceiling spotlight", "Accumulation without memory",
 "Character scanning shelves blankly",
 "Static. The character's head tilts as the eyes scan the shelves; the '?' bubble bobs. 3s."),

("This is why the closet is full and the account is empty",
 "Wide split panel. Left 'CLOSET': overflowing chaotic closet of items. Right 'ACCOUNT': a flat bank screen showing '$0.00' / near-empty bar. Bold connecting arrow: 'SAME BRAIN. DIFFERENT DIRECTION.'",
 "Wide split panel", "Flat, white", "The paradox made concrete",
 "Static contrast; connecting arrow",
 "Static. The connecting arrow draws from the full closet to the empty account. 2s."),

("and you still find yourself scrolling at midnight feeling like something is missing.",
 "Medium shot in a dark bedroom, only the phone glow lighting the character's face from below. Eyes tired and hollow, still scrolling. A small empty-shaped hole glows faintly in the chest area. Dark blue night tones.",
 "Medium shot", "Dark, cold phone glow from below", "Hollow late-night emptiness",
 "Endless scrolling; faint void in chest",
 "Static. The phone glow flickers with each scroll; the faint chest void pulses dimly. 3s loop."),

("You were never going to find it. You were looking in exactly the place they built for you to look.",
 "Wide bird's-eye shot: the character small inside a vast flat maze shaped like a shopping bag; a glowing 'SHOPPING' sign marks the only entrance. The character wanders the dead-end interior, lost.",
 "Wide bird's-eye shot", "Flat, cool gray, glowing entrance sign", "The search was rigged from the start",
 "Character lost inside a purpose-built maze",
 "Static. The character walks a few steps into a dead end and stops; the 'SHOPPING' sign pulses. 3s."),

("The neuroscientist Kent Berridge ran experiments in the 1990s that quietly broke the model everyone was using.",
 "Medium-wide flat 1990s laboratory: boxy computer, clipboards. A calm scientist figure (glasses, white coat) studies a rat enclosure on a table. A wall calendar reads '1990s.' Warm lab light.",
 "Medium-wide lab interior", "Flat, warm lab light", "Quiet, paradigm-breaking science",
 "Scientist studying the enclosure",
 "Static. The scientist leans in and makes a note; the rat shifts in the enclosure. 3s."),

("He found a way to block dopamine in rats completely without touching their capacity for pleasure.",
 "Close-up flat diagram of a rat brain: the dopamine pathway shown as a gold line with a bold black 'BLOCKED' barrier across it, while a separate small 'PLEASURE' region still glows soft warm. White background.",
 "Close-up diagram", "Flat, white, gold line blocked / soft pleasure glow", "Two systems cleanly separated",
 "Dopamine path blocked; pleasure region intact",
 "Static. The 'BLOCKED' barrier snaps onto the gold path; the pleasure region keeps a soft glow. 2s."),

("The dopamine-free rats still showed enjoyment responses when food touched their mouths.",
 "Medium shot, light background. A cartoon rat with a small content smile as a food morsel touches its mouth; a tiny soft warm glow at the cheeks. No gold dopamine burst anywhere.",
 "Medium shot", "Flat, soft warm cheek glow, no gold", "Pleasure intact without wanting",
 "Rat showing contentment, no dopamine burst",
 "Static. The rat's cheeks glow softly and it gives a small satisfied wiggle. 2s."),

("They could still feel good. They just stopped wanting.",
 "Split panel. Left: the content rat with a soft warm glow, label 'STILL LIKES.' Right: the same rat lying still beside an untouched lever, label 'STOPPED WANTING.' Neutral background.",
 "Wide split panel", "Flat, soft glow left / flat right", "Liking without wanting",
 "Content rat vs. motionless rat",
 "Static. Left rat keeps its soft glow; right rat lies still as the lever sits ignored. 2s."),

("They stopped seeking. They lay still and waited.",
 "Medium shot, muted neutral background. The rat lies flat and calm in the center of the enclosure, eyes half-closed, the lever and food both within reach but untouched. Stillness emphasized.",
 "Medium shot", "Flat, muted neutral", "Inert calm — drive switched off",
 "Rat motionless; resources ignored",
 "Static. The rat's chest rises and falls slowly; nothing else moves. 2s."),

("Then he reversed it. He amplified the dopamine signal without increasing pleasure.",
 "Close-up diagram of the rat brain: the gold dopamine path now thick, oversized, and blazing bright; the separate 'PLEASURE' region unchanged, still only a soft small glow. White background.",
 "Close-up diagram", "Flat, white, oversized blazing gold path", "Wanting amplified, liking unchanged",
 "Dopamine path super-charged; pleasure flat",
 "Static. The gold path swells and brightens while the pleasure region stays the same soft size. 2s."),

("Those rats wanted desperately. They worked harder, pressed levers longer, pursued rewards more aggressively.",
 "Medium shot. A frantic wide-eyed rat hammering a lever with both paws, motion lines around it, an obsessive expression. Gold bursts firing rapidly above. Light gray background.",
 "Medium shot", "Flat, rapid gold bursts", "Desperate, frantic compulsion",
 "Rat hammering the lever furiously",
 "Static. The rat's paws pump the lever fast; gold bursts flash rapidly above. 2s loop."),

("But when they got what they were chasing, the satisfaction was flat.",
 "Medium shot. The same rat finally holds the reward (a food pellet) but its expression is blank and unmoved; no warm glow, no smile. A small flat-line graph floats beside it labeled 'SATISFACTION.'",
 "Medium shot", "Flat, neutral, no glow", "Empty payoff",
 "Rat with reward but blank expression",
 "Static. The rat holds the pellet; the 'SATISFACTION' graph stays a dead flat line. 2s."),

("They wanted more without ever feeling more.",
 "Split panel. Left 'WANTING': frantic rat at the lever with huge gold bursts. Right 'FEELING': same rat with the reward, flat expression, flat-line graph. Bold gap between them labeled 'NO BRIDGE.'",
 "Wide split panel", "Flat — gold left, flat right", "The broken link between want and reward",
 "Frantic wanting vs. empty feeling",
 "Static. Left side bursts gold rapidly; right side stays a flat line; the 'NO BRIDGE' gap holds. 3s."),

("Wanting and liking. Two completely separate systems in the brain.",
 "Close-up diagram of the brain split into two clearly separated, differently colored zones: gold 'WANTING' on one side, soft warm 'LIKING' on the other, a clean black divider between them. White background.",
 "Close-up diagram", "Flat, white, gold vs. soft warm zones", "Clean conceptual separation",
 "Two labeled brain systems side by side",
 "Static. Each zone lights in turn — gold 'WANTING', then soft 'LIKING' — across the divider. 3s."),

("And the one being monetized — every app, every algorithm, every push notification — is wanting.",
 "Medium shot. The gold 'WANTING' brain zone wired to floating icons — app, algorithm chart, notification bell — all plugged into it by cables. The soft 'LIKING' zone sits unplugged and ignored. Cool blue-gray.",
 "Medium shot", "Flat, blue-gray, gold wired zone", "Only wanting is harvested",
 "Wanting zone cabled to platforms; liking ignored",
 "Static. The cables pulse gold from the icons into the 'WANTING' zone; 'LIKING' stays dark. 3s loop."),

("Not your happiness. Your hunger.",
 "Stark close-up on white. Two words stacked: 'HAPPINESS' struck through in red, 'HUNGER' below it in bold gold. A small villain brain sits beside 'HUNGER', tapping it.",
 "Close-up, centered", "Flat, white, red strike / gold word", "Blunt final distinction",
 "Strike-through on 'HAPPINESS'; brain taps 'HUNGER'",
 "Static. The red strike crosses 'HAPPINESS'; the brain taps 'HUNGER' and it glows gold. 2s."),

("So what do you actually do with this?",
 "Medium shot, neutral gray background. The character faces camera directly, calm and serious, no villain glow — a genuine pause. A simple bold question mark floats beside their head.",
 "Medium shot, direct address", "Flat, neutral gray", "Pivot — the turn toward the solution",
 "Character meeting the viewer's eyes; '?' floating",
 "Static. The character holds a steady gaze; the question mark gently pulses once. 2s."),

("You cannot think your way out of a dopamine loop.",
 "Medium shot. The small bespectacled 'prefrontal' figure inside the skull pushes uselessly against a giant spinning gold loop that dwarfs it; the villain brain rides the loop, amused.",
 "Medium shot on skull interior", "Flat, gold spinning loop", "Reason alone is overpowered",
 "Tiny rational figure shoving a giant loop in vain",
 "Static. The gold loop spins; the small figure strains against it and slides back. 2s loop."),

("You cannot reason past a system that was built by teams of neuroscientists and behavioral economists",
 "Wide blue-gray war-room shot: rows of villain-brain experts in lab coats at terminals, a giant central screen modeling the character. One small lone 'prefrontal' figure stands before it all, tiny by comparison.",
 "Wide establishing shot", "Flat, blue-gray, screen glow", "Asymmetry of forces",
 "Vast expert team vs. one tiny rational figure",
 "Static. The terminal screens flicker with data; the lone figure looks up at the giant display. 3s."),

("and tested on hundreds of millions of users before it ever reached you. That's not a fair fight.",
 "Wide shot. A massive grid of identical user silhouettes labeled 'TESTED ON: HUNDREDS OF MILLIONS' on one side; a single small character alone on the other, a lopsided scale tipping hard against them. Gray background.",
 "Wide shot", "Flat, gray", "Rigged from the start",
 "Lopsided scale; lone user vs. millions",
 "Static. The scale tips further down on the 'millions' side; the lone figure rises helplessly. 3s."),

("And anyone who tells you it comes down to willpower has never looked at what willpower actually is in the brain",
 "Close-up inside the skull: a small 'WILLPOWER' battery icon held by the prefrontal figure, already partly drained, with a red low-charge indicator. The villain brain eyes it hungrily.",
 "Close-up on skull interior", "Flat, white, red low-battery indicator", "Willpower as a finite resource",
 "Prefrontal figure holding a draining battery",
 "Static. The 'WILLPOWER' battery bar drops a notch; the red indicator blinks. 2s."),

("a limited resource that depletes across a day and fails under stress, which is exactly when the lever gets pressed hardest.",
 "Split panel. Left 'MORNING': full green willpower battery, calm character. Right 'NIGHT, STRESSED': near-empty red battery, frazzled character mashing a glowing lever. Cool tones left, hot red tones right.",
 "Wide split panel", "Flat — calm green left, hot red right", "Depletion meets peak temptation",
 "Full battery vs. drained battery at the lever",
 "Static. The right battery drains to red as the frazzled character pumps the glowing lever. 3s."),

("You build friction instead.",
 "Medium shot on clean white. The character calmly and deliberately places a solid brick wall labeled 'FRICTION' between their own hand and a glowing 'BUY NOW' phone. Composed, intentional expression.",
 "Medium shot", "Flat, white", "The turn — deliberate counter-design",
 "Character building a wall between hand and phone",
 "Static. The character sets the last brick of the 'FRICTION' wall into place and steps back. 2s."),

("The same way the system removes friction to make you spend, you add it back deliberately",
 "Wide split panel. Left 'THEM': villain brain sliding a 'FRICTION' dial down to 0. Right 'YOU': the character turning the same dial back up, calm and deliberate. Mirrored composition.",
 "Wide split panel", "Flat, white", "Reclaiming the dial",
 "Brain lowering friction vs. character raising it",
 "Static. Left dial turns to 0; right dial turns back up; the two motions mirror. 3s."),

("to give your prefrontal cortex the seconds it needs to do its job.",
 "Close-up inside the skull, warm beige. The bespectacled prefrontal figure now stands fully awake with a clipboard, a calm clock ticking steadily beside it; the villain brain waits, restrained behind a small barrier.",
 "Close-up on skull interior", "Warm beige interior", "Reason finally given room",
 "Prefrontal figure working; brain held back",
 "Static. The prefrontal figure checks the clipboard against the ticking clock; the brain waits behind the barrier. 3s."),

("You delete saved payment information. You put 24 hours between wanting something and buying it.",
 "Wide split panel on white. Left: a card icon labeled 'SAVED' being dragged into a trash bin. Right: a calendar with a bold '24h' arc drawn between a 'WANT' marker and a 'BUY' marker.",
 "Wide split panel", "Flat, white", "Concrete tactic #1 and #2",
 "Card deleted; 24-hour gap inserted",
 "Static. The 'SAVED' card drops into the bin; the '24h' arc draws between the two markers. 3s."),

("You use cash for the categories where you consistently overspend,",
 "Medium shot. The character hands over physical green cash to a simple shopfront; a small visible wince on their face. Bold label: 'CASH.' Warm muted retail background.",
 "Medium shot", "Flat, warm muted", "Tactic #3 — make payment tangible",
 "Character handing over cash, slight wince",
 "Static. The cash passes from hand to hand; the character winces slightly as it leaves. 2s."),

("because the physical sensation of handing over money activates what researchers call the pain of paying",
 "Close-up of the character's hand releasing cash; a small red 'ouch' spark at the fingertips and a tiny red label 'PAIN OF PAYING.' Inside the skull, the prefrontal figure perks up, alert.",
 "Close-up on hand and skull", "Flat, white, small red spark", "A useful, real friction",
 "Cash leaving hand; red 'pain' spark; reason alerted",
 "Static. The red spark flicks at the fingertips as the cash leaves; the prefrontal figure looks up. 2s."),

("a real neurological response that card tapping completely bypasses.",
 "Split panel. Left 'CASH': hand releasing cash with a red 'pain' spark, brain alert. Right 'TAP': a card tapping a reader, smooth and painless, brain asleep. Bold contrast.",
 "Wide split panel", "Flat, white", "Why frictionless payment is dangerous",
 "Painful cash vs. painless tap",
 "Static. Left side sparks red; right side taps smoothly with no spark and a sleeping brain. 3s."),

("You remove apps that function as lever systems from your home screen.",
 "Medium shot of a flat phone home screen; several glowing 'lever' app icons being dragged off into a folder labeled 'OFF' or into a trash bin. The character's hand calmly performs the action.",
 "Medium shot on phone", "Flat, neutral", "Tactic #4 — strip the levers",
 "Lever-apps dragged off the home screen",
 "Static. One glowing lever-app icon is dragged off-screen and the home screen calms. 2s."),

("You are not fighting weakness. You are fighting infrastructure.",
 "Wide split panel. Left 'NOT THIS': a small wilted figure labeled 'WEAKNESS' with a red X. Right 'THIS': the same character facing a large industrial machine labeled 'INFRASTRUCTURE', standing firm.",
 "Wide split panel", "Flat, white", "Reframe — the real opponent",
 "Weakness X-ed out vs. character facing the machine",
 "Static. The red X strikes 'WEAKNESS'; the character squares up to the 'INFRASTRUCTURE' machine. 2s."),

("And you fight infrastructure by redesigning the environment, not by trying to overpower it.",
 "Medium shot. The character calmly rearranges large environmental blocks (labeled 'BANK', 'PHONE', 'CART') into a new safer layout — not straining, just designing. Clean white background, blueprint-style guide lines.",
 "Medium shot", "Flat, white, faint blueprint lines", "Design over force",
 "Character rearranging environment blocks",
 "Static. The character slides one labeled block into a new position; blueprint lines snap to it. 3s."),

("One participant in a behavioral savings study saved an additional $14,000 over three years",
 "Medium shot of a calm female character beside a rising green bar chart; a bold floating label '+$14,000' and a small tag 'OVER 3 YEARS.' Warm neutral background.",
 "Medium shot", "Flat, warm neutral, green chart", "A concrete, real-world win",
 "Character beside a rising savings chart",
 "Static. The green bars rise step by step toward the '+$14,000' label. 3s."),

("through a single structural change. She moved her savings to a bank with no mobile app.",
 "Medium shot. The character closes a glowing banking app (X over a phone) and instead stands before a simple solid brick bank building with no screen anywhere. Calm, deliberate.",
 "Medium shot", "Flat, neutral", "One structural change, not willpower",
 "App closed; physical bank chosen",
 "Static. The phone's banking app winks out; the solid brick bank stands plainly behind her. 2s."),

("No instant transfers. If she wanted that money, she had to make a deliberate physical trip and wait.",
 "Wide shot. The character walking a visible path toward a distant brick bank, a small 'WAIT' signpost along the way. Deliberate friction shown as literal distance. Warm muted outdoor tones.",
 "Wide shot", "Flat, warm muted outdoor", "Friction as literal distance",
 "Character walking the long path to the bank",
 "Static. The character takes a few steps along the path; the 'WAIT' signpost passes by. 3s."),

("She never touched it.",
 "Close-up of the brick bank's solid closed door with the savings safely behind it; a faint green glow inside. The character's hand hovers far away, then lowers, choosing not to. Calm resolution.",
 "Close-up on bank door", "Flat, faint green glow within", "Quiet, decisive restraint",
 "Hand hovering, then withdrawing",
 "Static. The distant hand lifts slightly, then lowers and relaxes; the door stays closed. 2s."),

("Not because she had more willpower than the person beside her. Because she built a better cage.",
 "Wide split panel. Left: a frantic figure mashing a lever in a bare cage (the rat-cage motif, human version). Right: the calm character inside a redesigned, open, well-built environment — same cage concept, better design.",
 "Wide split panel", "Flat, white", "Design beats willpower",
 "Bad cage vs. well-designed environment",
 "Static. Left figure keeps mashing the lever; right character stands calm in the better-built space. 3s."),

("The rats in Montreal pressed the lever until they died",
 "Medium shot, cold gray. A worn lever center frame, a small still rat collapsed beside it, the cage walls tight and bare. Somber, restrained.",
 "Medium shot", "Flat, cold gray", "Somber callback to the experiment",
 "Collapsed rat beside the worn lever",
 "Static. A faint dust settles around the still rat; nothing moves. 3s."),

("because the lever was the only thing in the cage and they had no ability to see the cage from the outside.",
 "Wide shot from inside the bare cage looking at the lone lever; the bars are drawn so the viewer is positioned inside, with no outside visible. Claustrophobic, gray.",
 "Wide shot, inside-the-cage POV", "Flat, cold gray", "Trapped without perspective",
 "Lone lever; no outside visible",
 "Static. A very slow push toward the lone lever; the bars stay closed around the frame. 3s."),

("You can.",
 "Medium shot. The main character stands at the cage bars and, unlike the rat, looks up and out — pulling one bar aside to reveal a bright open space beyond. Hopeful pivot. Warm light breaking in from outside.",
 "Medium shot", "Flat, warm light breaking in", "The turn — perspective the rat never had",
 "Character looking out, opening the cage",
 "Static. The character pulls a bar aside; warm light widens across their face. 2s."),

("The dopamine trap is not a personal failure.",
 "Medium shot on white. The character stands upright and calm; a bold label 'PERSONAL FAILURE' beside them is struck through in red. No villain glow — just composure.",
 "Medium shot", "Flat, white", "Absolution restated",
 "Red strike-through on 'PERSONAL FAILURE'",
 "Static. The red strike crosses 'PERSONAL FAILURE'; the character's posture stays steady. 2s."),

("It is a designed system running on hardware that evolution built to help you survive scarcity",
 "Split panel. Left: a primitive savanna scene, an ancient figure grabbing scarce berries, the brain glowing gold (survival). Right: the same brain in a modern shopping aisle, glowing the same gold — mismatch. Bold label: 'SAME HARDWARE.'",
 "Wide split panel", "Flat — warm savanna left, modern aisle right", "Ancient hardware in a modern trap",
 "Survival glow then misfiring in a store",
 "Static. The gold glow appears in the savanna, then reappears identically in the modern aisle. 3s."),

("not to protect you from an industry that turned abundance into addiction.",
 "Wide shot. A towering modern shelf of infinite identical products looming over a small ancient-looking figure whose gold brain misfires; bold label arc: 'ABUNDANCE → ADDICTION.' Cool overwhelming tones.",
 "Wide shot", "Flat, cool overwhelming tones", "Abundance weaponized",
 "Tiny figure dwarfed by infinite product shelf",
 "Static. The shelf seems to extend upward; the small figure's gold brain flickers. 3s."),

("Your brain was never broken. It was just never meant for this.",
 "Medium close-up of the character, calm and a little tired but dignified; the brain inside the skull rendered neutral and unblamed, gently lit — not a villain here, just out of place. Warm soft background.",
 "Medium close-up", "Flat, warm soft", "Compassion — the brain is not the enemy",
 "Calm character; neutral, gently lit brain",
 "Static. The character exhales; the brain inside settles into a calm, neutral expression. 2s."),

("But you are not a rat. You can see the lever. You can study who built it and why.",
 "Medium shot. The character stands outside the cage now, calmly examining the lever in their hand like an object of study, the villain brain shrunk and quiet behind glass. Clear, composed. Neutral light background.",
 "Medium shot", "Flat, neutral", "Empowered perspective",
 "Character studying the lever from the outside",
 "Static. The character turns the lever over, examining it; the contained brain watches quietly. 3s."),

("And you can, slowly and imperfectly, build an environment",
 "Wide shot. The character, mid-build, assembling a calm, well-designed personal space out of labeled blocks ('FRICTION', 'CASH', 'WAIT', 'NO APP'). Some blocks slightly crooked — imperfect but real. Soft daylight.",
 "Wide shot", "Flat, soft daylight", "Honest, imperfect construction",
 "Character building a personal environment",
 "Static. The character sets another labeled block; one sits slightly crooked but holds. 3s."),

("where your brain's oldest instincts and your actual financial future are not working directly against each other.",
 "Split panel resolving into one. Left: ancient gold-glow instinct. Right: a rising green financial-future chart. The two arrows, once opposed, now bend to run parallel in the same direction. Warm hopeful tones.",
 "Wide split resolving to unified", "Flat, warm hopeful", "Reconciliation — alignment at last",
 "Opposed arrows turning to run parallel",
 "Static. The two opposing arrows slowly rotate until they point the same way, side by side. 3s."),

("That decision doesn't come with a notification.",
 "Medium shot, calm neutral background. The character makes a quiet, resolved choice; a phone nearby sits dark and silent with a small crossed-out notification bell. Stillness, no glow.",
 "Medium shot", "Flat, calm neutral", "Quiet, unrewarded choice",
 "Silent phone; crossed-out notification bell",
 "Static. The phone stays dark; the crossed-out bell holds; the character is still. 2s."),

("It doesn't arrive in two days.",
 "Close-up of an empty doorstep — no package, just clean ground and a calm shadow. A faint crossed-out delivery-box icon in the corner. Quiet, restrained.",
 "Close-up on doorstep", "Flat, calm neutral", "No instant payoff",
 "Empty doorstep; no delivery",
 "Static. The empty doorstep holds; the crossed-out box icon stays faint. 2s."),

("It doesn't release dopamine when you make it.",
 "Close-up of the character's transparent skull: the brain stays calm and neutral — no gold burst, no glow — quietly at peace. White background, very clean.",
 "Close-up on skull", "Flat, white, no glow", "The right choice feels like nothing",
 "Calm brain; deliberately no dopamine burst",
 "Static. The brain rests still and neutral; pointedly no gold flash occurs. 2s."),

("That's exactly how you know it matters.",
 "Final medium shot. The character faces camera directly, calm, clear-eyed, quietly resolved; soft warm light, no devices, no villain brain visible — just composure. A clean, conclusive frame.",
 "Medium shot, direct address", "Flat, soft warm light", "Quiet, earned conclusion",
 "Character meeting the viewer's gaze, at peace",
 "Static. The character holds a steady, calm gaze; the warm light settles. 3s — final frame."),
]


def shade(cell, hexcolor):
    from docx.oxml.ns import nsdecls
    from docx.oxml import parse_xml
    cell._tc.get_or_add_tcPr().append(
        parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), hexcolor)))


doc = Document()

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(10.5)

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("CRAYON CAPITAL — CLONE SESSION · VIDEO 2")
run.bold = True
run.font.size = Pt(18)

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run('"Por qué comprar se siente mejor que tener"  ·  The Dopamine Trap')
r.italic = True
r.font.size = Pt(12)

meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
meta.add_run("Neuroeconomía · Inglés · Target 1,700 · Final 1,724 words · {} beats (3–5s each)".format(len(BEATS))).font.size = Pt(9)

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

docx_path = "/home/user/Claudeeee/Dopamine_Trap_Production.docx"
doc.save(docx_path)
print("Saved DOCX:", docx_path, "with", len(BEATS), "beats")
