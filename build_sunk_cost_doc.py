#!/usr/bin/env python3
"""Production document for Video 10: Your Brain Won't Let You Quit — And It's Costing You Everything."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

STYLE = ("2D flat cartoon illustration, thick solid black outlines on every element, "
         "clean solid color fills, no gradients except soft warm ambient light. "
         "Recurring main character ALEX: large beige oval head with transparent glass upper "
         "skull revealing a pink cartoon brain inside, small black dot eyes, thin neutral mouth, "
         "black spiky hair, red t-shirt, gray pants. "
         "Brain villain: pink cartoon brain character, smug heavy-lidded eyes, slight smirk, small teeth. "
         "Palette: beige skin, pink brain (#E8A598), red t-shirt, gray pants, green dollar bills, "
         "red for X-marks and losses, white for diagram/infographic scenes, "
         "warm beige interiors with soft oval ceiling spotlight, "
         "dark charcoal (#1A1A1A) for hook/void scenes. "
         "Bold black diegetic text labels integrated into the scene. 16:9, 1280x720.")

BEATS = [
    # ── HOOK ──
    (
        "Alex is about to lose forty thousand dollars.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Single dramatic overhead spotlight on ALEX (red t-shirt, black spiky hair, transparent skull with pink brain). He stands frozen, staring into the void. A faint $40,000 price tag hangs in the darkness. Brain villain in shadows behind him, watching with heavy-lidded smug eyes.",
        "Medium shot, low angle, villain barely visible in shadow",
        "Single overhead spotlight, everything else in darkness",
        "Dread, inevitability, dramatic tension",
        "Alex frozen, staring forward, brain visibly agitated inside skull",
        "Slow push into Alex's face from darkness",
    ),
    (
        "He has had seven chances to stop.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Seven small glowing EXIT signs arranged in an arc behind ALEX. Each sign is crossed out in red — he passed every one. Brain villain stands beside the crossed-out signs, arms folded, satisfied.",
        "Wide shot, seven exit signs visible in darkness behind Alex",
        "Exit signs glow faint red, Alex in center spotlight",
        "Missed opportunities, entrapment",
        "Alex looking forward, oblivious to exits behind him",
        "Camera slowly pulls back to reveal all seven crossed-out exits",
    ),
    (
        "Every single time he had a chance to stop, his brain gave him a reason to continue.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). ALEX's transparent skull fills most of the frame. Inside: the brain villain sitting comfortably in an armchair, holding a list of excuses — 'WAIT FOR RECOVERY,' 'YOU CAN'T QUIT NOW,' 'YOU'VE COME TOO FAR.' Smugly ticking them off.",
        "Close-up on Alex's skull — brain villain visible inside",
        "Skull lit from within by the brain's faint glow, outer darkness total",
        "Sinister comfort, the enemy is internal",
        "Brain villain inside skull ticking off excuses with a quill pen",
        "Excuse list scrolls upward inside skull",
    ),
    (
        "The stock is down sixty percent. It is still falling.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Jagged red descending stock chart fills the frame like a wound. The line cuts brutally downward with no recovery. Bold label: '-60%.' ALEX reflected tiny in the chart's red light, watching helplessly.",
        "Wide — stock chart dominates, Alex tiny below it",
        "Chart glows red, Alex silhouetted below in darkness",
        "Brutal financial hemorrhage",
        "Alex staring up at chart, unable to look away",
        "Red line continues to fall during scene",
    ),
    (
        "He knows it is bad.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Close-up on ALEX's face. His black dot eyes are wide. His transparent skull reveals the brain villain inside — not panicking — smiling slightly, nodding calmly. Two completely opposite reactions. Label: 'HE KNOWS.'",
        "Extreme close-up — Alex's face and skull interior split the frame",
        "Alex's face in cold light, brain villain in warm inner glow",
        "Cognitive dissonance — he knows but cannot act",
        "Alex's face tense, brain villain serene and unconcerned",
        "Slow zoom on the contrast between face and brain",
    ),
    (
        "But quitting feels like losing.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Two doors side by side: left door labeled 'SELL NOW — ACCEPT LOSS' with a red X, right door labeled 'HOLD — MAYBE RECOVER' with a faint green question mark. ALEX's hand is frozen inches from the red X door. Brain villain blocks it gently with one hand.",
        "Wide — two doors, Alex between them, hand reaching for loss door",
        "Red X door in harsh cold light, green door in warm false hope",
        "Paralysis, fear of finality",
        "Alex's hand frozen, unable to open the sell door",
        "Alex's hand trembles millimeters from the door handle",
    ),
    (
        "And that feeling — not the market — is what's destroying him.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Split frame: left half shows the STOCK CHART still falling (real world). Right half shows ALEX's brain interior — brain villain sitting calmly with a 'DO NOT SELL' sign, completely disconnected from the chart. Label: 'THE REAL PROBLEM' with arrow pointing to brain villain.",
        "Split frame — market reality vs brain reality",
        "Left side cold red, right side warm false comfort",
        "The disconnect between reality and brain response",
        "Brain villain holds DO NOT SELL sign, market crashes behind him",
        "Both halves animate simultaneously — market falls, brain stays still",
    ),
    (
        "This is the sunk cost fallacy. And by the end of this video, you will never fall for it again.",
        f"{STYLE} DARK CHARCOAL background (#1A1A1A). Large white bold text materializes: 'THE SUNK COST FALLACY.' Below it, smaller text: 'THE TRAP INSIDE YOUR OWN SKULL.' ALEX stands below the text looking up. Brain villain visible in his skull, arms crossed, awaiting the challenge.",
        "Wide — title text fills upper frame, Alex below it",
        "Text appears in sharp white against darkness",
        "Declaration of war against the mechanism",
        "Alex looks up at the title, brain villain inside skull stiffens",
        "Title text appears line by line with impact",
    ),
    # ── THE SCENARIO ──
    (
        "Alex is thirty-one years old. He has been saving for four years. He has forty thousand dollars.",
        f"{STYLE} ALEX (red t-shirt, black spiky hair, transparent skull) sits at a kitchen table under a warm oval ceiling spotlight. A piggy bank labeled '$40,000' sits beside him. Four calendar years on the wall: crossed out in sequence. Warm beige interior.",
        "Medium wide, warm kitchen setting",
        "Warm oval ceiling spotlight, domestic comfort",
        "Hard-earned savings, earned patience",
        "Alex looking at piggy bank with quiet pride, brain calm inside skull",
        "Camera pans across four crossed-out calendar years",
    ),
    (
        "A tech stock he has been watching for months catches his eye. Growth story. Strong narrative. Five analysts recommending it.",
        f"{STYLE} ALEX at laptop, leaning in with interest. Screen shows a stock ticker with upward green arrows, analyst ratings: five green 'BUY' labels. Brain inside skull lights up with excitement — green glow. Warm desk lamp light.",
        "Medium — Alex at laptop, screen prominent",
        "Warm desk lamp, excitement building in skull",
        "Excitement, FOMO, the narrative seduction",
        "Alex leaning forward, brain visibly energized inside skull",
        "Green BUY ratings pop in one by one on screen",
    ),
    (
        "He buys five hundred shares at eighty dollars each. Forty thousand dollars. All of it.",
        f"{STYLE} ALEX clicking CONFIRM on a brokerage screen. Large confirmation: '500 SHARES × $80 = $40,000.' His piggy bank tilts over, emptied. Green checkmark on screen. Alex's brain: satisfied, expectant. Label: 'ALL IN.'",
        "Medium — confirmation screen and empty piggy bank",
        "Bright confirmation light — feels good",
        "Commitment, the point of no return",
        "Alex clicks confirm, piggy bank empties dramatically",
        "Confirmation screen flashes, piggy bank tips to empty",
    ),
    (
        "Two weeks later, the stock is at sixty dollars.",
        f"{STYLE} ALEX looking at his phone. Stock app: '500 SHARES — CURRENT VALUE: $30,000.' Red minus sign. His face: slight frown. Brain inside skull: alert but reasoning. Label: '-$10,000.' Warm home setting.",
        "Medium — Alex with phone, loss visible",
        "Warm home light but slight cool shift on phone screen",
        "First doubt, first discomfort",
        "Alex frowning at phone, brain calculating inside skull",
        "Phone number ticks down to $30,000",
    ),
    (
        "His brain says: 'It will recover. This is temporary. Everyone holds through dips.'",
        f"{STYLE} ALEX's transparent skull — three speech bubbles from brain villain inside: 'IT WILL RECOVER,' 'TEMPORARY DIP,' 'EVERYONE HOLDS.' Brain villain nodding reassuringly to Alex. Warm inner glow.",
        "Close-up — skull with brain villain speaking",
        "Warm comforting inner skull glow",
        "False reassurance, rationalization factory",
        "Brain villain gesturing calmly, producing reassurance",
        "Speech bubbles appear one by one inside skull",
    ),
    (
        "The stock falls to forty dollars. He has lost twenty thousand dollars.",
        f"{STYLE} ALEX at desk, head slightly bowed. Phone shows: '$20,000 — DOWN 50%.' A large '-$20,000' floats in red above him. Half of his original piggy bank's contents have visually evaporated. His brain inside skull: conflicted, heavier.",
        "Medium wide — Alex at desk, loss label prominent",
        "Cooler light, slight shadow on Alex",
        "Deepening dread, the loss becomes real",
        "Alex staring at phone with heavier expression",
        "-$20,000 label fades in with weight",
    ),
    (
        "His brain says: 'You can't sell now. You would lock in the loss. Wait a little longer.'",
        f"{STYLE} ALEX's skull — brain villain stands beside a lock icon labeled 'LOCKED LOSS.' He points at it with alarm. Speech bubble: 'SELL NOW = MAKING IT REAL.' The loss shown as a ghost — not real until the sell button is pressed. Brain villain holding back Alex's hand.",
        "Close-up — skull interior, lock icon prominent",
        "Warm inner glow, lock glows red",
        "The sunk cost logic in pure form",
        "Brain villain gesturing at locked loss icon, blocking Alex's hand",
        "Lock icon pulses with a click sound implication",
    ),
    (
        "The stock falls to twenty dollars. He has lost thirty thousand dollars.",
        f"{STYLE} ALEX's face in increasing distress. Phone: '$10,000 — DOWN 75%.' Above him: '-$30,000' in large red. Three quarters of his piggy bank contents now shown evaporated. His brain inside skull visibly strained but still reasoning.",
        "Medium — Alex with phone, three quarters of savings gone",
        "Cold light — warm gone from the scene",
        "Hemorrhage, the spiral tightening",
        "Alex gripping phone with white knuckles, brain grinding inside skull",
        "-$30,000 label slams in with weight",
    ),
    (
        "His brain says: 'You've come this far. Selling now means you went through all of this for nothing.'",
        f"{STYLE} ALEX's skull — brain villain points dramatically at a timeline of pain: four years of saving, the buy, the dip, the deeper dip. 'YOU'VE COME THIS FAR — CAN'T STOP NOW.' The word 'NOTHING' in red at the end of the pain timeline if he sells.",
        "Close-up — skull with pain timeline inside",
        "The pain timeline glows warmly — sunk cost logic made visible",
        "Sunk cost logic at its most seductive",
        "Brain villain gesturing at the pain invested, making it feel precious",
        "Pain timeline glows as brain villain traces it",
    ),
    (
        "The company files for bankruptcy. The stock goes to zero.",
        f"{STYLE} ALEX standing in the dark as a notification hits his phone: 'COMPANY BANKRUPT — SHARES WORTHLESS — $0.' The last glow on his phone fades to black. Label: '$0.' Four years of savings: gone. His face: hollow.",
        "Wide — Alex in darkness, phone showing $0",
        "Phone light extinguishes, leaving Alex in near total dark",
        "The final consequence — the void",
        "Alex's expression: hollow, the brain inside skull finally silent",
        "Phone light dies to black on $0 notification",
    ),
    (
        "Forty thousand dollars. Four years of savings. Gone.",
        f"{STYLE} Dark scene — the three numbers in descending red: '$40,000,' '4 YEARS,' 'GONE.' ALEX stands below them, small against the scale of the loss. Brain villain in background, no longer smug — just watching. The consequence is total.",
        "Wide — three loss labels above tiny Alex",
        "Cold dark, labels glowing in red",
        "The full weight of the loss",
        "Alex looking up at the numbers, brain villain watching silently",
        "Three labels drop in one by one with increasing weight",
    ),
    (
        "Every single step, the thing that stopped him from leaving was not the market. It was the money he had already spent.",
        f"{STYLE} Rewind montage — four moments replayed fast: the dip, the deeper dip, the extreme dip, zero. Each moment: brain villain holding up the 'SUNK COST' sign. The sign never changes. The losses get worse each time. Label: 'NOT THE MARKET — THE MONEY ALREADY SPENT.'",
        "Wide — four-panel quick montage",
        "Cold light, red losses consistent across all panels",
        "The mechanism at work through every stage",
        "Brain villain holding SUNK COST sign identically in all four panels",
        "Four panels flash in rapid sequence",
    ),
    # ── THE MECHANISM ──
    (
        "Here is why.",
        f"{STYLE} Clean white background. ALEX stands beside a large blank whiteboard, arms open. His skull transparent, brain villain inside skull preparing to explain. Label: 'THE MECHANISM.' Clinical diagram mode activated.",
        "Medium wide — Alex and whiteboard, white background",
        "Clean clinical white, explanation mode",
        "Transition to mechanism explanation",
        "Alex gesturing at blank whiteboard, brain villain preparing inside skull",
        "Whiteboard wipes clean into frame",
    ),
    (
        "The sunk cost fallacy is the tendency to continue an investment because of what you have already put in — not because of what it will return.",
        f"{STYLE} ALEX beside whiteboard with definition written in bold black text: 'SUNK COST FALLACY: Continuing because of PAST investment, not FUTURE return.' Arrow pointing backward (PAST) glows orange. Arrow pointing forward (FUTURE) is dim. Clean white background.",
        "Wide — definition on whiteboard, Alex pointing",
        "Clean white, definition prominent",
        "Conceptual clarity — naming the mechanism",
        "Alex pointing at definition, brain villain inside skull nodding",
        "Definition writes itself on whiteboard word by word",
    ),
    (
        "Your brain uses past investment as a reason to justify present action.",
        f"{STYLE} Brain diagram on whiteboard: INPUT (past investment arrow, orange) → BRAIN PROCESSING → OUTPUT (continue action, green). But the correct input should be: FUTURE RETURN (dim, barely connected). Label: 'BRAIN USES WRONG INPUT.'",
        "Wide — brain diagram on whiteboard",
        "Clinical white, wrong-input connection glows orange",
        "The logical inversion exposed",
        "Alex tracing the wrong input arrow with concern",
        "Wrong input arrow traces in orange, correct future arrow dims",
    ),
    (
        "This is backwards. The money you already spent is gone whether you continue or not.",
        f"{STYLE} Two scenarios side by side on whiteboard. SCENARIO A: Continue → Past money still gone + future loss. SCENARIO B: Stop now → Past money still gone + no future loss. The past loss is IDENTICAL in both. Bold red label: 'GONE EITHER WAY.'",
        "Wide — two scenarios on whiteboard",
        "Clinical white, red GONE EITHER WAY prominent",
        "The core logical truth",
        "Alex pointing between both scenarios, showing identical past loss",
        "GONE EITHER WAY label appears between both scenarios",
    ),
    (
        "The only question that matters is: will continuing make things better from here?",
        f"{STYLE} Whiteboard wiped clean. Single bold question: 'WILL THIS MAKE THINGS BETTER FROM HERE?' Arrow points forward only — no backward arrow. The past is erased from the diagram. Alex pointing at the single forward question.",
        "Wide — single question on whiteboard, past erased",
        "Clean white, forward arrow glows green",
        "The correct framing — the only question that matters",
        "Alex pointing confidently at forward question, brain villain inside skull uncomfortable",
        "Past erased from whiteboard, single question appears clean",
    ),
    (
        "Alex never asked that question. His brain kept asking a different one: how much have I already lost?",
        f"{STYLE} ALEX's skull — brain villain inside holding two signs. Right sign (what brain asks): 'HOW MUCH HAVE I ALREADY LOST?' glowing orange. Left sign (what it should ask): 'WILL THIS GET BETTER?' dim and ignored. Brain villain only looking at the orange sign.",
        "Close-up — skull with two signs, brain villain ignoring the right one",
        "Orange glow on wrong question, green dim on right question",
        "The fatal substitution",
        "Brain villain fixated on the orange sign, back to the green one",
        "Orange sign pulses, green sign fades in the background",
    ),
    # ── THE SCIENCE ──
    (
        "In 1985, psychologists Hal Arkes and Catherine Blumer ran an experiment that changed how we understand this.",
        f"{STYLE} Clean white background. Academic scene: two researchers at a chalkboard labeled 'ARKES & BLUMER — 1985.' Two stick-figure test subjects. A ski resort drawing in background. Bold label: 'THE EXPERIMENT THAT PROVED IT.'",
        "Wide — academic scene, white background",
        "Clean academic white, authoritative",
        "Scientific credibility, evidence arrives",
        "Alex watching from side as researchers appear",
        "Researchers and chalkboard fade in cleanly",
    ),
    (
        "They gave people a hypothetical: you've paid for a ski trip. Then a blizzard hits the resort. Do you go anyway?",
        f"{STYLE} Ski resort scene: BLIZZARD conditions. A figure standing at a car with ski gear, looking at impassable snowy roads. In a thought bubble: 'I ALREADY PAID $200.' A ticket stub visible. Arkes and Blumer watching with clipboards.",
        "Wide — blizzard scene, figure with ticket stub",
        "Cold blizzard light, thought bubble warm orange",
        "The hypothetical made vivid",
        "Figure standing at car in blizzard, clutching ticket",
        "Blizzard weather animates in over resort",
    ),
    (
        "Ninety percent said yes. Even though going would add misery and no enjoyment. The money was already gone.",
        f"{STYLE} Bar chart: 90% bar labeled 'GO ANYWAY' in red/orange. 10% bar labeled 'STAY HOME, SAVE THE DAY' in green. Bold text: '90% CHOSE MISERY TO AVOID WASTING THE PAST.' Arkes and Blumer looking at the result. ALEX shaking his head.",
        "Wide — bar chart prominent",
        "Clinical white, 90% bar striking",
        "The scale of the effect — nearly universal",
        "Alex and researchers both looking at the overwhelming 90% bar",
        "90% bar rises dramatically, 10% bar tiny beside it",
    ),
    (
        "This is your brain treating past spending as a debt you owe your future self.",
        f"{STYLE} Diagram: PAST ALEX (spent money, orange) connected by a debt chain to FUTURE ALEX (must honor it, red). The chain labeled 'SUNK COST DEBT.' Brain villain holds the chain. The logical correct version: chain is cut, no debt.",
        "Wide — debt chain diagram",
        "Orange for past, red for trapped future",
        "The psychological debt mechanism",
        "Brain villain holding chain, future Alex straining against it",
        "Debt chain glows and tightens",
    ),
    (
        "Kahneman and Tversky showed that losses feel twice as powerful as equivalent gains.",
        f"{STYLE} Balance scale: LEFT — '+$100 GAIN' (one weight). RIGHT — '-$100 LOSS' (two weights, twice as heavy). Scale tips hard to the loss side. Brain villain standing on the loss side, making it heavier. Label: 'LOSS AVERSION — LOSSES HURT 2X MORE.'",
        "Wide — uneven scale diagram",
        "Neutral white, loss side heavier and darker",
        "The asymmetry of pain",
        "Brain villain on loss side making scale tip further",
        "Scale tips dramatically toward loss side",
    ),
    (
        "So when Alex looks at a thirty-thousand-dollar paper loss, his brain registers the pain of a sixty-thousand-dollar loss.",
        f"{STYLE} ALEX looking at phone showing '-$30,000.' But in his transparent skull, the brain processes it as '-$60,000' — twice the size, twice the red. A 2× AMPLIFIER icon visible inside skull. Brain villain operating the amplifier dial.",
        "Close-up — Alex with phone, skull processing visible",
        "Phone shows real number, skull shows amplified horror",
        "The amplification that creates paralysis",
        "Brain villain turning up the pain amplifier inside skull",
        "Skull interior number animates from -$30k to -$60k felt",
    ),
    (
        "Loss aversion plus sunk cost thinking equals a trap so powerful it has a name: the Concorde Fallacy.",
        f"{STYLE} Concorde jet on a runway with a large price tag: '£1.3 BILLION SPENT.' Engineers pointing at it — project is clearly over budget and failing. But executives continuing anyway because of what's been spent. Label: 'THE CONCORDE FALLACY — TOO MUCH SPENT TO STOP.'",
        "Wide — Concorde jet scene",
        "Impressive but doomed light",
        "Historical scale — this trap destroys even governments",
        "Alex watching from ground level as Concorde scene plays out",
        "Price tag grows on the Concorde as scene develops",
    ),
    (
        "Britain and France built an airplane they knew would never be commercially viable. They kept going because stopping meant admitting the past billions were wasted.",
        f"{STYLE} Diagram: CONCORDE PROJECT timeline with mounting costs. Three 'STOP NOW' decision points, each crossed out. Red line of losses growing. Brain villain in government suit at each decision point, overruling the stop signal. Label: 'PRIDE DISGUISED AS LOGIC.'",
        "Wide — decision timeline diagram",
        "Cold institutional gray/white, mounting losses in red",
        "Institutional sunk cost at maximum scale",
        "Brain villain in suit overruling stop signals at each point",
        "Decision points crossed out in sequence, losses mount",
    ),
    (
        "The plane cost more to fly than it earned in revenue — for every single flight. For twenty-seven years.",
        f"{STYLE} Single flight equation: 'COST PER FLIGHT: $1M. REVENUE PER FLIGHT: $0.6M. LOSS PER FLIGHT: $400,000.' Then: '27 YEARS × MULTIPLE FLIGHTS = STAGGERING LOSSES.' ALEX's jaw drops. Scale bar showing 27 years.",
        "Wide — flight loss equation, large numbers",
        "Cold clinical white — numbers brutal",
        "The mathematics of sunk cost at institutional scale",
        "Alex staring at the per-flight loss calculation with disbelief",
        "27-year bar extends slowly across frame",
    ),
    (
        "Alex is not running a government. But his brain is running the same program.",
        f"{STYLE} Side-by-side comparison: CONCORDE project executive (suit, prestige) vs ALEX (red t-shirt, kitchen table). Both with the same brain villain inside their transparent skulls, running the same 'SUNK COST.exe' program. Label: 'SAME PROGRAM. DIFFERENT SCALE.'",
        "Wide — parallel comparison",
        "Same lighting for both — the universality",
        "The humbling universality — kings and commoners alike",
        "Alex and executive both with identical brain villain running same program",
        "Brain villain programs run in sync in both skulls",
    ),
    # ── THE REAL COST ──
    (
        "Here is what this costs — not in one story, but in the aggregate.",
        f"{STYLE} ALEX stepping aside as a large data visualization appears. Multiple investor silhouettes in a crowd — all with transparent skulls, all with brain villains. Label: 'THE AGGREGATE COST.' Clinical data mode. White background.",
        "Wide — crowd of investors, data mode",
        "Clean white, aggregate scale",
        "Scale shift — from one person to the pattern",
        "Alex gesturing at crowd behind him",
        "Crowd of investor silhouettes materializes",
    ),
    (
        "Researchers studying investor behavior found that investors hold losing stocks forty percent longer than winning stocks.",
        f"{STYLE} Two columns of stocks: LEFT column — WINNERS (green) — held for a shorter bar time. RIGHT column — LOSERS (red) — held for 40% longer bar. The disproportion visible at a glance. Label: 'HOLD LOSERS 40% LONGER.' Brain villain behind the loser column, nodding.",
        "Wide — two-column holding time comparison",
        "Green winners left, red losers right — 40% longer right bar",
        "The statistical reality of the fallacy",
        "Brain villain standing behind loser column, encouraging the longer hold",
        "40% longer bar extends beyond winner bar with a click",
    ),
    (
        "This is called the disposition effect. It is the sunk cost fallacy in your investment portfolio — measured, documented, consistent.",
        f"{STYLE} Bold label: 'THE DISPOSITION EFFECT.' Below: definition — 'Investors sell winners too early. Hold losers too long.' Two arrows: winner cut short (scissors icon), loser held long (clamp icon). Academic source label at bottom.",
        "Wide — disposition effect definition diagram",
        "Clinical white, definition prominent",
        "Naming the documented market-wide behavior",
        "Alex pointing at definition, recognition visible",
        "Definition builds on screen piece by piece",
    ),
    (
        "The average investor underperforms the market by two to three percent annually because of behavioral biases — and the sunk cost fallacy is one of the biggest contributors.",
        f"{STYLE} Two investment lines on graph: MARKET RETURN (green, steady upward). AVERAGE INVESTOR (red, same slope but 2-3% below). Over thirty years, the gap becomes enormous. Label: '-2 TO -3% PER YEAR.' ALEX watching the lines diverge.",
        "Wide — diverging line graph, 30-year span",
        "Green above, red below — gap widens",
        "The annual cost made visible over time",
        "Alex watching the lines diverge with growing concern",
        "Lines diverge continuously across the 30-year chart",
    ),
    (
        "On a forty-thousand-dollar portfolio, two percent a year over thirty years is not two percent. It is the difference between $216,000 and $324,000.",
        f"{STYLE} Two growth charts side by side. LEFT: '$40,000 WITHOUT behavior drag → $216,000 at 7%.' RIGHT: '$40,000 WITH behavior drag at 5% → $324,000.' Wait — the CORRECT version: '$40k at 7% = $324k, $40k at 5% = $216k.' Gap between them: '$108,000.' Label: 'BEHAVIORAL DRAG COSTS $108,000.'",
        "Wide — two growth charts, gap prominent",
        "Green on right (full potential), red drag on left",
        "The dollar cost of the behavioral penalty",
        "Alex looking between the two futures, stunned",
        "Gap between charts expands to full $108,000 difference",
    ),
    (
        "That is not money you lost in a crash. That is money you quietly left on the table every year by holding the wrong positions too long.",
        f"{STYLE} ALEX at a dinner table. Money is on the table — he stands up and quietly walks away without picking it up. Year after year (fast montage). The stack grows each year he walks away. Label: 'LEFT ON THE TABLE — EVERY YEAR.'",
        "Wide — table with money, Alex walking away repeatedly",
        "Warm but slightly melancholy domestic light",
        "The quiet, slow, unspectacular cost",
        "Alex repeatedly standing up and walking past the growing money stack",
        "Money stack grows each time Alex walks past",
    ),
    (
        "The market does not punish you for the crash. It punishes you for what you do the day after.",
        f"{STYLE} Two ALEX figures at the same crash moment. LEFT ALEX: sells loser, reallocates, continues up. RIGHT ALEX: holds, waits, watches crash deepen. Two diverging paths from the same crash point. Label: 'THE DAY AFTER IS WHAT COUNTS.'",
        "Wide — two diverging paths from same crash point",
        "Neutral start, diverge to green left and red right",
        "The decision moment after the crash",
        "Two Alexes diverge at the crash moment — one acts, one freezes",
        "Paths diverge from single crash point",
    ),
    # ── THE MANY FACES ──
    (
        "The sunk cost fallacy is not only investing. It is everywhere.",
        f"{STYLE} ALEX in center of white frame. Around him: six icons floating — stock chart, job building, relationship hearts, restaurant plate, video game controller, half-built house. Each icon labeled. Brain villain standing in center beside Alex, arms wide.",
        "Wide — Alex surrounded by six life domain icons",
        "Clean white, icons orbiting Alex",
        "The universality of the trap",
        "Brain villain gesturing proudly at the range of traps surrounding Alex",
        "Icons orbit in from off-frame to surround Alex",
    ),
    (
        "Alex has been at his job for seven years. The role stopped challenging him after year three. He has stayed because of the four years he already gave.",
        f"{STYLE} ALEX at office desk (label 'YEAR 7'). Slumped posture. Clock on wall. Timeline behind him: years 1-3 marked GROWING (green), years 4-7 marked STAGNANT (orange). The four stagnant years glow as sunk cost. Brain villain patting the orange years fondly.",
        "Medium wide — office scene, timeline visible",
        "Warm beige office with oval spotlight, stagnant years in orange",
        "The career trap — four years of sunk cost",
        "Alex slumped at desk, brain villain patting the sunk years",
        "Stagnant years glow as brain villain pats them",
    ),
    (
        "The cost of staying is not just the salary. It is every year of compounding skill and opportunity he is not building.",
        f"{STYLE} Two growth trees side by side. LEFT: ALEX STAYS — tree grows slowly, stunted after year 3. RIGHT: ALEX LEAVES — tree grows taller, branches wider, fruit visible. Year 7 comparison: dramatic difference in tree height. Label: 'OPPORTUNITY COST OF SUNK COST.'",
        "Wide — two growth trees, year 7 comparison",
        "Left tree dim and stunted, right tree full and green",
        "The invisible opportunity cost",
        "Alex looking between his stunted tree and the counterfactual flourishing one",
        "Right tree grows steadily while left tree stagnates",
    ),
    (
        "He stays because of three years that are already gone.",
        f"{STYLE} ALEX at desk again. Three ghost years (years 1-3) float behind him, translucent — they are gone, unreachable. He is reaching backward toward them. Brain villain holds a sign: 'THOSE YEARS ALREADY SPENT — REASON TO STAY.' Logic inverted.",
        "Medium — Alex reaching backward toward ghost years",
        "Ghost years translucent and unreachable, Alex straining backward",
        "The fundamental inversion — past as reason for future",
        "Alex reaching backward at ghost years, brain villain nodding",
        "Ghost years pulse translucently as Alex reaches",
    ),
    (
        "The same brain runs the same program in relationships.",
        f"{STYLE} ALEX and a generic partner figure. Timeline above them: YEAR 1-2 (hearts, good), YEAR 3-5 (neutral faces, flat), YEAR 6-7 (slight frown, mismatch). Alex's brain villain inside skull: 'WE'VE BEEN TOGETHER 7 YEARS.' Label: 'SAME PROGRAM.'",
        "Wide — relationship timeline above two figures",
        "Warm early years, cooling in later years",
        "Pattern interrupt — relationships next",
        "Alex looking at relationship timeline, brain villain inside skull gesturing at year count",
        "Relationship timeline appears above figures in stages",
    ),
    (
        "Two extra years in a relationship that is wrong. Not because it might get better. Because of the five years already given.",
        f"{STYLE} ALEX with thought bubble: '5 YEARS ALREADY GIVEN → 2 MORE YEARS WASTED.' Brain villain inside skull holds up '5 YEARS' sign as justification. The correct question (will this get better?) shown as a ghost bubble, ignored.",
        "Close-up — Alex with thought bubble and ghost question",
        "Orange sunk cost thought bubble, dim green correct question",
        "The relationship trap — five years as justification",
        "Brain villain holding years sign, blocking the correct question bubble",
        "Correct question bubble fades as sunk cost bubble glows",
    ),
    (
        "Or the restaurant where the food was terrible, but you ate all of it because you paid twenty dollars for the meal.",
        f"{STYLE} ALEX at restaurant table. Plate of clearly terrible food in front of him — he is eating it grimly. Label: '$20 ALREADY PAID.' Brain villain sitting across from him: 'FINISH IT — YOU PAID FOR IT.' The meal only getting worse with each bite.",
        "Medium — restaurant scene with grim eating",
        "Warm restaurant light, absurd but real scene",
        "Pattern interrupt — the trivial example that makes it undeniable",
        "Alex eating grimly, brain villain across table encouraging",
        "Alex eating reluctantly, grimace growing",
    ),
    (
        "The scale changes. The mechanism does not.",
        f"{STYLE} Three panels: STOCK ($40,000 loss), JOB (4 years stagnant), RESTAURANT ($20 meal). Brain villain identical in all three — same pose, same sign: 'YOU ALREADY INVESTED — CAN'T STOP NOW.' Label: 'SAME MECHANISM. DIFFERENT SCALE.'",
        "Wide — three-panel comparison",
        "Consistent lighting across all three panels",
        "The universality locked in",
        "Brain villain identically positioned in all three panels",
        "Three panels appear simultaneously",
    ),
    # ── THE ESCAPE ──
    (
        "There is one question that kills the sunk cost fallacy.",
        f"{STYLE} ALEX standing tall in white space, arms slightly open. Above him: a single large glowing question mark. Brain villain inside skull shrinks slightly — something he fears is coming. Label: 'ONE QUESTION CHANGES EVERYTHING.'",
        "Wide — Alex with glowing question mark above",
        "Clean white, glowing question mark",
        "Hope, agency — the solution arrives",
        "Alex standing tall, brain villain inside skull visibly uneasy",
        "Question mark glows and pulses above Alex",
    ),
    (
        "Ask it every time. About the stock, the job, the relationship, the meal.",
        f"{STYLE} The same question mark from previous beat, now spreading outward with arrows toward all the life domains from earlier — stock, job, relationship, restaurant. The one question reaches all of them. Clean white background.",
        "Wide — question mark radiating to all domains",
        "Clean white, radiating arrows",
        "Universal application — one tool for all domains",
        "Alex gesturing as question mark's reach expands to all domains",
        "Arrows radiate from question mark to each domain",
    ),
    (
        "The question is: if I had not already invested anything — not a dollar, not a day, not a meal — would I start this today?",
        f"{STYLE} Bold black text appears on white background: 'IF I HAD NOT ALREADY INVESTED ANYTHING — WOULD I START THIS TODAY?' Text builds word by word. ALEX reading it, brain villain inside skull staring at it with visible discomfort. This question is his kryptonite.",
        "Wide — text-forward scene, question dominates",
        "Clean white, text appears sharp and clear",
        "The kryptonite of the sunk cost fallacy",
        "Alex reading question, brain villain shrinking inside skull",
        "Question text builds word by word",
    ),
    (
        "This is zero-based thinking. You erase the past. You ask only: does the future justify continuing?",
        f"{STYLE} Diagram: before and after. BEFORE: complex tangle of past investments, losses, time spent. AFTER: slate wiped clean, single forward arrow. Label: 'ZERO-BASED THINKING.' ALEX holding the eraser that wiped the past clean.",
        "Wide — before/after diagram, clean slate",
        "Before side cluttered and orange, after side white and clear",
        "The mental reset — elegant and liberating",
        "Alex holding eraser, past wiped clean behind him",
        "Past clutter erases to clean slate",
    ),
    (
        "Would Alex buy five hundred shares of this stock today, knowing what he knows now? No.",
        f"{STYLE} ALEX at brokerage screen, same stock. Past investment wiped clean — he sees it fresh. His brain inside skull: calm, analytical. He sees: company bankrupt, stock at $20, no recovery path. His hand: does NOT press buy. Label: 'ZERO-BASED: WOULD YOU BUY TODAY? NO.'",
        "Medium — Alex at screen, fresh evaluation",
        "Clean neutral light — the fresh-eyes view",
        "The liberation of zero-based clarity",
        "Alex looking at stock with fresh eyes, hand not pressing buy",
        "Alex's hand stays still — no buy",
    ),
    (
        "Then the answer to 'should I hold?' is also no. Because hold is just buy without the paperwork.",
        f"{STYLE} Diagram: 'HOLD' label with equals sign pointing to 'BUY WITHOUT THE PAPERWORK.' Two arrows: one labeled HOLD, one labeled BUY. They both point to the same commitment action. Brain villain deflates as the equation is exposed. Label: 'HOLD = BUY. SAME COMMITMENT.'",
        "Wide — hold equals buy diagram",
        "Clean white, equation prominent",
        "The logical kryptonite — hold is buy",
        "Brain villain staring at the equation, shrinking",
        "Equation appears, brain villain visibly deflates",
    ),
    (
        "The exit is not failure. The exit is the correction.",
        f"{STYLE} ALEX standing at the EXIT door from earlier in the video — the one his brain blocked. He opens it calmly. Green light on the other side. Brain villain in background — small now, unable to stop him. Label: 'THE EXIT IS THE CORRECTION.'",
        "Medium — Alex at exit door, brain villain small behind",
        "Green light beyond door — liberation",
        "The reframe of exit as wisdom, not defeat",
        "Alex opening exit door calmly, brain villain too small to stop him",
        "Door opens to green light, brain villain recedes",
    ),
    (
        "Every dollar and every day you spend on a sunk cost is a dollar and a day you are not investing in something that could actually work.",
        f"{STYLE} Two piles side by side. LEFT: resources (money coins, clock time icons) being poured into a sinking ship labeled 'SUNK COST.' RIGHT: same resources being planted like seeds, growing into a tree. Label: 'SAME RESOURCES — DIFFERENT FUTURES.'",
        "Wide — two piles diagram, sinking ship vs growing tree",
        "Red sinking side left, green growing side right",
        "The opportunity cost of continuing",
        "Alex redirecting resources from left pile to right pile",
        "Resources flow from sinking ship to growing tree",
    ),
    # ── EL MOVIMIENTO ──
    (
        "Here is what you do with this.",
        f"{STYLE} ALEX standing upright, red t-shirt, black spiky hair, transparent skull with calm brain. Five action icons below him. Clean white background. Label: 'EL MOVIMIENTO.' Brain inside skull engaged and ready — no villain this time, just Alex.",
        "Wide — Alex centered, action icons below, white background",
        "Bright purposeful white",
        "Agency — Alex fully in control",
        "Alex with sleeves metaphorically rolled up, brain actively engaged not villainous",
        "Action icons slide in below Alex",
    ),
    (
        "The next time you are about to make a financial decision about something you have already invested in — pause. Ask the zero-based question. Write it down.",
        f"{STYLE} ALEX at desk. Paper in front of him. He writes: 'WOULD I START THIS TODAY WITH FRESH MONEY?' He pauses. His brain inside skull: calm, evaluating. No villain present. Just clear thinking.",
        "Medium wide — Alex at desk writing the question",
        "Warm desk lamp, focused and deliberate",
        "The practical pause — the first action step",
        "Alex writing question carefully, brain evaluating clearly inside skull",
        "Question text appears on paper as he writes",
    ),
    (
        "Before investing in anything — set a loss limit in advance. 'If this falls twenty percent, I sell.' Write it down before you buy. Your future emotional brain cannot override a rule you set when you were calm.",
        f"{STYLE} ALEX at brokerage screen BEFORE buying. He writes a physical note: 'SELL RULE: -20% = EXIT. NO EXCEPTIONS.' He attaches it to the screen. Brain villain tries to reach it — Alex puts it behind glass. Label: 'PRE-COMMIT THE EXIT.'",
        "Wide — Alex pre-committing the exit rule at brokerage",
        "Calm deliberate light — this is preparation mode",
        "Pre-commitment — the brain hack that works",
        "Alex attaching sell rule to screen, brain villain blocked behind glass",
        "Sell rule note attached to screen, glass barrier appears",
    ),
    (
        "In your career, run a zero-based review every two years. Would you take this job today if you were offered it fresh? If the answer is no — that is not comfortable information. It is useful information.",
        f"{STYLE} ALEX at calendar with 'YEAR 2 REVIEW' marked. He holds up a checklist: 'WOULD I TAKE THIS JOB TODAY? YES / NO.' His brain inside skull: honest, evaluating without sunk cost defense. If NO is circled — that is information, not failure.",
        "Wide — Alex with career review calendar and checklist",
        "Focused purposeful light",
        "The career audit habit",
        "Alex running career review, brain evaluating honestly",
        "Calendar review moment — checklist fills out",
    ),
    (
        "The sunk cost fallacy is not fixed by willpower. It is fixed by process. Rules made before the emotion. Questions asked before the defense.",
        f"{STYLE} Two columns on whiteboard: 'WILLPOWER (FAILS)' — sad flexing icon, crossed out. 'PROCESS (WORKS)' — checklist icon, rules icon, question icon, all checked green. ALEX pointing at process column. Brain villain in small corner cannot fight a process.",
        "Wide — two-column whiteboard comparison",
        "Clean white, failed willpower column dim, process column bright",
        "Process beats emotion — the key insight",
        "Alex pointing confidently at process column, brain villain relegated to corner",
        "Process column items check off in sequence",
    ),
    (
        "If this is how your brain handles quitting — wait until you see what it does when you believe you deserve something you haven't earned yet.",
        f"{STYLE} ALEX looking directly at camera with a slight knowing smile. Behind him: a glimpse of the NEXT VIDEO's visual world — a tease of entitlement framing, perhaps a crown or pedestal. Brain villain peeking around the corner, already preparing. Label: 'NEXT: WHAT YOUR BRAIN DOES WITH ENTITLEMENT.'",
        "Medium — Alex direct address to camera, next topic teased behind",
        "Alex in spotlight, next video world lit behind",
        "CTA — curiosity gap opened for next video",
        "Alex speaking directly to camera, slight smile, brain villain peeking ahead",
        "Next video world briefly illuminates behind Alex",
    ),
    # ── THE ENDING ──
    (
        "Alex is thirty-five years old now.",
        f"{STYLE} ALEX at kitchen table (same as the start — warm oval spotlight, warm beige interior). Label: 'FOUR YEARS LATER.' He looks different — not broken, not rich. Just older. A new investment account open on his laptop. Starting again.",
        "Medium wide — same kitchen, four years later",
        "Warm oval spotlight, domestic — same as the start",
        "Return, continuity, the long game",
        "Alex at same kitchen table, new laptop, rebuilding",
        "Slow pull back from same angle as opening scene",
    ),
    (
        "He did not make his money back. That forty thousand dollars is gone.",
        f"{STYLE} ALEX looking at a simple ledger. The '$40,000' line: crossed out in red. No recovery column. No magic return. Just gone. He nods slowly. Brain inside skull: calm now, not in denial.",
        "Close-up — ledger with $40,000 crossed out",
        "Neutral warm light — no drama, just fact",
        "Acceptance without defeat",
        "Alex nodding at ledger, brain calm and accepting inside skull",
        "Camera holds on crossed-out $40,000",
    ),
    (
        "But he has something he did not have before. He knows exactly why he held.",
        f"{STYLE} ALEX holding a small card that reads: 'SUNK COST FALLACY — THE BRAIN KEEPS THROWING GOOD MONEY AFTER BAD.' He reads it calmly. The brain villain inside his skull: still there, but visible now — known, named, watchable.",
        "Medium — Alex holding the card",
        "Warm light — knowledge as power",
        "The value of understanding — not wealth but awareness",
        "Alex reading card, brain villain visible and named inside skull",
        "Camera slowly focuses on the card text",
    ),
    (
        "Knowing why you made a mistake is not consolation. It is protection.",
        f"{STYLE} ALEX holds up the card like a shield. Brain villain inside skull: contained, unable to act unseen now. Shield label: 'UNDERSTANDING = PROTECTION.' Not a trophy for the past loss — a tool for the future.",
        "Medium — Alex with card as shield, brain villain contained",
        "Warm purposeful light",
        "Knowledge as armor — the emotional close",
        "Alex holding understanding card like a shield, brain villain visible but contained",
        "Shield glow around the card pulses once",
    ),
    (
        "The cost is not the forty thousand dollars he lost.",
        f"{STYLE} ALEX standing quietly. The '$40,000' label fades. It was not the real cost. His expression: the real calculation beginning. The brain inside skull: realizing something deeper.",
        "Medium — Alex with fading $40,000 label",
        "Warm light, label fades slowly",
        "Reframe — the real cost is not what we thought",
        "Alex watching $40,000 label fade, something more important coming",
        "$40,000 label slowly fades to nothing",
    ),
    (
        "The cost is every dollar he did not make while waiting to get it back.",
        f"{STYLE} The opportunity cost revealed: a growth chart showing what $40,000 invested in a diversified index fund would have grown to over the same period — while Alex held the dead stock. The gap: larger than the original $40,000 loss. Label: 'THE REAL COST: OPPORTUNITY LOST.'",
        "Wide — opportunity cost chart, the real gap revealed",
        "Green growth chart, Alex's holding period shown as flat red line",
        "The true cost — bigger than the loss itself",
        "Alex looking at the opportunity cost chart, understanding complete",
        "Opportunity cost chart fills in, green line growing as red line stagnates",
    ),
    (
        "Your brain will always give you a reason to stay. Name it. Write it down. Then ask the one question that matters.",
        f"{STYLE} ALEX facing camera directly. Behind him: the brain villain, now small, named, labeled 'SUNK COST FALLACY.' Alex points at the brain villain — labeled, visible, known. Then holds up the zero-based question on a card. Direct address. He is talking to you.",
        "Medium — Alex direct address, brain villain small and named behind him",
        "Alex in warm spotlight, brain villain in shadow but labeled",
        "Empowerment, direct address — the final message",
        "Alex pointing at labeled brain villain, then holding up question card to camera",
        "Slow zoom in as Alex holds card up to camera",
    ),
    (
        "Would you start this today?",
        f"{STYLE} Final frame: clean white. Single bold black question: 'WOULD YOU START THIS TODAY?' ALEX's face below it — small, honest, looking at viewer. No brain villain. No label. Just the question. It stays on screen.",
        "Wide — question above Alex, minimal and final",
        "Clean white, bold black text — no distractions",
        "The final question — lingers with the viewer",
        "Alex looking at viewer honestly, brain calm inside skull",
        "Question holds on screen, slow fade to white",
    ),
]

SECTION_STARTS = {
    1:   "HOOK",
    9:   "THE SCENARIO",
    21:  "THE MECHANISM",
    27:  "THE SCIENCE",
    37:  "THE REAL COST",
    44:  "THE MANY FACES",
    52:  "THE ESCAPE",
    60:  "EL MOVIMIENTO",
    66:  "THE ENDING",
}


def _shade_cell(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = title_p.add_run("CRAYON CAPITAL — CLONE SESSION · VIDEO 10")
    r.bold = True
    r.font.size = Pt(14)

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = sub_p.add_run("STATE 5 — PRODUCTION DOCUMENT")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    t_p = doc.add_paragraph()
    t_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t_p.add_run("Your Brain Won't Let You Quit — And It's Costing You Everything")
    r.bold = True
    r.italic = True
    r.font.size = Pt(14)

    doc.add_paragraph()

    HDR = ["#", "NARRATION", "IMAGE PROMPT", "CAMERA", "LIGHTING", "MOOD", "CHARACTER ACTION", "VIDEO MOTION"]
    tbl = doc.add_table(rows=1, cols=8)
    tbl.style = 'Table Grid'
    hdr_cells = tbl.rows[0].cells
    col_widths = [0.8, 4.5, 6.5, 3.0, 2.8, 2.8, 3.0, 3.2]
    for i, (cell, txt, w) in enumerate(zip(hdr_cells, HDR, col_widths)):
        cell.width = Cm(w)
        p = cell.paragraphs[0]
        run = p.add_run(txt)
        run.bold = True
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        _shade_cell(cell, '2C3E50')

    for beat_num, beat in enumerate(BEATS, 1):
        if beat_num in SECTION_STARTS:
            sec_row = tbl.add_row()
            sec_cells = sec_row.cells
            for i in range(1, 8):
                sec_cells[0].merge(sec_cells[i])
            p = sec_cells[0].paragraphs[0]
            run = p.add_run(f"── {SECTION_STARTS[beat_num]} ──")
            run.bold = True
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            _shade_cell(sec_cells[0], 'B02A2A')

        seg, scene, cam, light, mood, action, video = beat
        row = tbl.add_row()
        cells = row.cells
        data = [str(beat_num), seg, scene, cam, light, mood, action, video]
        for i, (cell, txt) in enumerate(zip(cells, data)):
            p = cell.paragraphs[0]
            run = p.add_run(txt)
            run.font.size = Pt(7)
            if i in (0, 1):
                run.bold = True
            if beat_num % 2 == 0:
                _shade_cell(cell, 'F9F9F9')

    all_lines = [b[0] for b in BEATS]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = len(BEATS)

    doc.add_paragraph()
    foot = doc.add_paragraph()
    foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = foot.add_run(f"END · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Sunk_Cost_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
