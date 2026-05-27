#!/usr/bin/env python3
"""Production document for Video 8: Getting Rich Is Making You Poorer."""

from docx import Document
from docx.shared import Pt, RGBColor
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

BEATS = [
    # ── HOOK ──
    (
        "You did everything right.",
        f"{STYLE} Character stands tall in an office, chest out, holding a payslip with a large green number circled. Soft warm ceiling spotlight on him. Confident posture.",
        "Medium shot, slightly low angle — heroic framing",
        "Warm amber office, soft oval ceiling spotlight",
        "Pride, earned confidence",
        "Standing straight, slight smile, payslip in one hand",
        "Slow push in toward character",
    ),
    (
        "You worked hard. You got the raise. Maybe you got the promotion.",
        f"{STYLE} Boss (older character, suit, glasses) extends hand with an envelope toward character. Both smiling. Office background with framed certificates on wall.",
        "Medium wide, two-shot at handshake",
        "Warm office light, spotlight on envelope",
        "Achievement, institutional warmth",
        "Character receiving envelope with both hands",
        "Gentle drift right as envelope changes hands",
    ),
    (
        "For about two weeks — maybe three — it felt like something had finally changed.",
        f"{STYLE} Character floats slightly above ground, small golden stars orbiting his head. Payslip visible in hand glowing softly green. Pure warm interior background.",
        "Medium shot, centered",
        "Bright celebratory warm light",
        "Brief euphoria, weightlessness",
        "Arms slightly raised, eyes closed in satisfaction",
        "Stars sparkle in, character bounces gently once",
    ),
    (
        "That specific relief. The sense that the number on your payslip matched the life you were supposed to have.",
        f"{STYLE} Close-up on payslip held in both hands. Large green number circled. Diegetic label beside it: 'FINALLY.' Character's thumbs visible gripping edges.",
        "Close-up on payslip, hands framing",
        "Warm backlight on paper, slight glow on number",
        "Relief, arrival, deserved rest",
        "Hands grip payslip gently, slight tremor of emotion",
        "Very slow zoom into circled number",
    ),
    (
        "And then it faded.",
        f"{STYLE} Same character now at home desk. Same payslip visible but no longer glowing. Face has returned to flat neutral. Small calendar on wall shows '3 WEEKS LATER.'",
        "Medium shot, slightly above — deflation angle",
        "Cooler, dimmer — same room feels different",
        "Quiet deflation, unexplained flatness",
        "Sitting, staring forward, shoulders slightly dropped",
        "Color temperature cools slightly across frame",
    ),
    (
        "Not the money. The money was still there.",
        f"{STYLE} Over-shoulder view of phone showing bank app with healthy green balance number. Character holds phone, face expressionless. Money is present but empty.",
        "Over-shoulder, phone in focus",
        "Cool blue phone glow, dim room behind",
        "Hollow, confusing disconnect",
        "Scrolling slowly, no reaction to the number",
        "Slow zoom out from phone screen to reveal flat expression",
    ),
    (
        "But the feeling was gone. And you were back — stretched, anxious, never quite enough.",
        f"{STYLE} Character at cluttered desk surrounded by floating bill envelopes labeled 'RENT,' 'CAR PAYMENT,' 'SUBSCRIPTIONS.' Slightly hunched. Dark gray tone creeping in from edges.",
        "Wide shot showing full environment of pressure",
        "Darker, gray tones bleeding in from edges",
        "Familiar dread, deja vu of old anxiety",
        "Head in hands, papers scattered",
        "Slow pan across scattered bills left to right",
    ),
    (
        "This is not a personal failure.",
        f"{STYLE} Large bold diegetic text label appears: 'NOT YOUR FAULT.' Character looks up at it, head tilting with curiosity. Plain white background — clean informational beat.",
        "Medium, character looking up at text",
        "Neutral bright white — informational",
        "Shift from shame to curiosity",
        "Head tilts up, slight question mark expression",
        "Text pops in with bounce, character reacts",
    ),
    (
        "It is a mechanism. And the people who profit from it are hoping you never find its name.",
        f"{STYLE} Brain villain (pink brain, navy t-shirt, smug heavy-lidded eyes) slides in from right edge behind character, holding a small gear labeled 'THE MECHANISM.' He looks directly at viewer. Character unaware.",
        "Medium wide — character foreground, villain emerging behind",
        "Villain has subtle red backlight; character in warm light",
        "Conspiracy revealed, ominous introduction",
        "Brain villain steps into frame, taps gear knowingly",
        "Villain slides in from right with eerie smoothness",
    ),
    # ── THE RAISE ──
    (
        "His name doesn't matter. He is every version of you that has ever gotten what you worked for.",
        f"{STYLE} New character introduced: generic everyman — beige head, black hair, dark blue t-shirt, gray pants. Standing in void with label 'AGE 24' above him. Simple, clean.",
        "Medium shot, centered",
        "Neutral warm light, soft spotlight",
        "Universal, relatable introduction",
        "Standing neutrally, arms at sides",
        "Character fades in from white",
    ),
    (
        "Twenty-four years old. First real job. The salary felt enormous.",
        f"{STYLE} Character at entry-level office desk. Small plant, basic computer. Payslip on desk with modest number but character looking at it with wide eyes — enormous to him.",
        "Medium wide — character at desk",
        "Warm office light, ceiling spotlight",
        "Wonder at first real income",
        "Leaning forward over payslip, eyes wide",
        "Slow zoom in on his face",
    ),
    (
        "He upgraded his apartment. It made sense — he could afford it now.",
        f"{STYLE} Two apartments side by side. Left: tiny studio, box labeled 'BEFORE.' Right: slightly larger flat, label 'UPGRADE #1.' Arrow pointing right. Character moves from left to right.",
        "Wide comparison shot",
        "Neutral informational light",
        "Logical, justified choice",
        "Character walks from left apartment to right",
        "Arrow animates left to right",
    ),
    (
        "He upgraded his car. It made sense — he was making more.",
        f"{STYLE} Two cars side by side: old small beaten-up car labeled 'BEFORE,' newer shinier car labeled 'UPGRADE #2.' Character standing between them nodding.",
        "Wide comparison, street setting",
        "Bright daylight, clean",
        "Rational upgrade, self-reward",
        "Nodding at new car, old car behind",
        "New car gleams with a brief shine effect",
    ),
    (
        "At twenty-eight, he got a promotion. Forty percent more than when he started.",
        f"{STYLE} Same character now slightly older (label 'AGE 28'). Boss hands him new payslip. A large '+40%' floats above in green. Confetti pops briefly.",
        "Medium two-shot, office",
        "Celebratory warm light",
        "Achievement, momentum",
        "Character holds payslip, small proud smile",
        "'+40%' pops in with bounce, confetti burst",
    ),
    (
        "He moved to a better neighbourhood. Better restaurants. Better clothes.",
        f"{STYLE} Triptych panel: left — nicer apartment exterior. Center — upscale restaurant with character dining. Right — character in smarter clothes. Labels: 'NEW FLAT,' 'FINE DINING,' 'NEW WARDROBE.'",
        "Wide triptych, three panels",
        "Warm lifestyle lighting across all three",
        "Upward mobility, natural progression",
        "Character present in each panel",
        "Panels slide in left to right",
    ),
    (
        "At thirty-two, he was earning three times what he earned at twenty-four.",
        f"{STYLE} Bar chart: two bars. Left 'AGE 24' short bar. Right 'AGE 32' tall bar — three times height — bright green. Label 'x3' between them with arrow.",
        "Wide infographic, white background",
        "Clean informational light",
        "Impressive growth, visual impact",
        "Character stands next to tall bar, looking up at it",
        "Tall bar grows upward from short bar",
    ),
    (
        "He was also, quietly, more anxious about money than he had ever been in his life.",
        f"{STYLE} Same character — 'AGE 32' label. Despite the tall income bar visible in background, character sits hunched at desk, hands clasped. Small sweat drop. Anxiety cloud above head.",
        "Medium shot, character in focus, chart blurred behind",
        "Dimmer foreground despite bright chart behind",
        "Quiet contradiction — success and dread coexist",
        "Hunched posture, clasped hands, unfocused gaze",
        "Anxiety cloud pulses gently above",
    ),
    (
        "His lifestyle had grown to match every raise, every time, without a single conscious decision.",
        f"{STYLE} Staircase graphic: each step labeled with a raise year ('AGE 24,' '26,' '28,' '32'). On each step stands the character's lifestyle icon (apartment, car, clothes). Character climbs but the floor keeps rising too.",
        "Wide staircase diagram",
        "Neutral diagram lighting",
        "Automatic, unconscious escalation",
        "Character climbing but never gaining height",
        "Steps rise automatically as character climbs",
    ),
    (
        "He was further from savings than he had been at twenty-four.",
        f"{STYLE} Two piggy banks side by side: 'AGE 24' piggy bank has a coin inside. 'AGE 32' piggy bank is cracked and empty despite big income bar beside it. Red X over savings.",
        "Wide comparison, white background",
        "Stark lighting, red X glows slightly",
        "Paradox, shock",
        "Character looks at empty piggy bank, baffled",
        "Crack appears on AGE 32 piggy bank",
    ),
    (
        "He could not explain it. The numbers said he should be fine.",
        f"{STYLE} Character holding a spreadsheet that shows green income numbers. But his face shows confusion, eyebrows raised. A calculator beside him shows question marks instead of answers.",
        "Medium, character with spreadsheet",
        "Warm light but uneasy",
        "Cognitive dissonance",
        "Holding spreadsheet up, head tilting",
        "Calculator question marks flash softly",
    ),
    (
        "The numbers were not the problem.",
        f"{STYLE} Close-up of spreadsheet: all numbers look correct in green. But a brain villain hand reaches in and taps the paper knowingly. Small label appears: 'WRONG QUESTION.'",
        "Close-up, villain hand entering from right",
        "Slightly ominous — villain light from right",
        "Reframe, the real issue is elsewhere",
        "Villain finger taps spreadsheet twice",
        "Label 'WRONG QUESTION' fades in on paper",
    ),
    # ── THE MECHANISM ──
    (
        "Here is what was happening inside his brain.",
        f"{STYLE} Cross-section diagram of character's head. Transparent skull shows pink brain inside, now displayed as an anatomy diagram with arrow pointing inward. Clean white background.",
        "Medium close-up, head cross-section",
        "Clinical white with warm pink brain highlight",
        "Transition to explanation mode",
        "Character head tilted, brain diagram glowing",
        "Diagram lines draw in from center",
    ),
    (
        "The human brain does not measure wealth in absolute terms.",
        f"{STYLE} Brain villain on white background holding a ruler. He tries to measure a stack of coins with the ruler — but shakes his head. Label: 'NOT ABSOLUTE.' Red X over ruler.",
        "Medium, white background, villain with ruler",
        "Clean informational white",
        "Counterintuitive insight",
        "Villain shakes head, tosses ruler aside",
        "Ruler bounces off, red X appears",
    ),
    (
        "It measures wealth relative to a reference point.",
        f"{STYLE} Horizontal scale/balance. Left side: character's current income. Right side: label 'REFERENCE POINT' with an arrow. The balance tips based on the reference point, not absolute amount.",
        "Wide balance diagram, white background",
        "Clean, neutral informational",
        "Relative measurement concept",
        "Balance tips left and right as reference point moves",
        "Scale tips with smooth motion",
    ),
    (
        "That reference point is not fixed. It moves.",
        f"{STYLE} Same balance diagram. The 'REFERENCE POINT' anchor on the right starts sliding to the right along a rail. The scale tips further. Label: 'MOVING TARGET.'",
        "Wide, same balance from prev beat",
        "Same clean light",
        "The trap revealed",
        "Brain villain pushes reference point further right",
        "Reference point slides right with a mechanical sound effect implied",
    ),
    (
        "Every time your circumstances improve, your brain recalibrates what normal feels like.",
        f"{STYLE} Dial/gauge labeled 'NORMAL METER.' Arrow points to a position. As a small upgrade icon appears (new apartment), the dial arrow automatically shifts right to higher position. Recalibration animation.",
        "Close-up on dial, neutral background",
        "Neutral white, dial highlighted",
        "Automatic recalibration — no choice involved",
        "Brain villain's hand turns dial up automatically",
        "Dial arrow moves right as upgrade appears",
    ),
    (
        "The new apartment becomes the baseline. The new salary becomes the floor.",
        f"{STYLE} Two-panel split: left — 'NEW APARTMENT' icon with label 'NOW = NORMAL.' Right — payslip with new salary, label 'NOW = MINIMUM.' Old versions crossed out with red X.",
        "Wide split panel, white background",
        "Clean informational",
        "The baseline shift crystallized",
        "Character stands between panels, nodding resignedly",
        "Red X stamps appear on old versions",
    ),
    (
        "This is called hedonic adaptation.",
        f"{STYLE} Large clean bold diegetic label: 'HEDONIC ADAPTATION.' Below it, a simple icon: treadmill with character running, staying in place. Plain white background.",
        "Wide, centered on label",
        "Clean white, label prominent",
        "Conceptual anchor — naming the mechanism",
        "Character points at label from below",
        "Label appears with a clean type-on effect",
    ),
    (
        "It is not a flaw in your psychology. It is a feature.",
        f"{STYLE} Checkmark icon next to the brain diagram. Label reads: 'DESIGN FEATURE — NOT BUG.' Green checkmark. Brain villain looks offended at the framing.",
        "Medium, centered, white background",
        "Green accent on checkmark",
        "Reframe — evolutionary origin",
        "Brain villain crosses arms, mildly offended",
        "Checkmark draws in with a bounce",
    ),
    (
        "For most of human history, this mechanism kept us alive.",
        f"{STYLE} Prehistoric setting: caveman version of character with spear, cave background. After catching food, he looks satisfied briefly, then immediately scans horizon for threats. Alert posture.",
        "Wide, cave environment",
        "Warm firelight from left",
        "Evolutionary survival context",
        "Brief satisfaction, then immediate vigilance",
        "Camera pans from food kill to scanning horizon",
    ),
    (
        "When conditions improved, the brain stopped celebrating and started preparing for the next threat.",
        f"{STYLE} Same caveman character: small celebration icon (thumbs up) immediately crossed out, replaced by eyes-scanning icon. Arrow: 'CELEBRATION → SCAN.' Brain visible in transparent skull shifting gears.",
        "Medium, caveman character",
        "Warm cave light",
        "Rapid transition from relief to vigilance",
        "Brief thumbs up then immediately scanning mode",
        "Quick cut-style transition between poses",
    ),
    (
        "The problem is that it was never designed for a world where conditions can keep improving indefinitely.",
        f"{STYLE} Modern cityscape with ascending escalator going endlessly upward. Caveman brain character at the bottom looking up confused — this landscape has no ceiling. Label: 'INFINITE UPGRADES.'",
        "Wide, city skyline, escalator prominent",
        "Modern bright city light",
        "Design mismatch — ancient tool, modern trap",
        "Caveman brain looks up at endless escalator, baffled",
        "Escalator extends beyond top of frame",
    ),
    (
        "In that world, the adaptation never stops.",
        f"{STYLE} Infinity symbol made of the recalibration dial arrows, cycling endlessly. Brain villain sits in the center of the infinity loop, relaxed, feet up. Label: '∞ RESET.'",
        "Wide, centered on infinity loop",
        "Cool blue-gray — endless, mechanical",
        "The loop with no exit",
        "Brain villain lounges in center, unbothered",
        "Infinity loop spins slowly, continuously",
    ),
    (
        "And neither does the feeling that you need just a little more.",
        f"{STYLE} Horizon line. A 'FINISH LINE' banner on it. Character running toward it. As he gets close, brain villain in background pulls the finish line further away on a rope. Label: 'JUST A LITTLE MORE →'",
        "Wide, horizon perspective",
        "Warm but slightly hopeless light",
        "The perpetual chase",
        "Character runs, finish line retreats",
        "Finish line pulled away as character approaches",
    ),
    # ── THE TREADMILL ──
    (
        "There is a name for what he was running on.",
        f"{STYLE} Treadmill machine appears center frame, clean white background. Diegetic label tag hanging from it, still blank. Character stands beside it looking at it.",
        "Medium wide, treadmill centered",
        "Clean neutral white",
        "Anticipation — naming moment",
        "Character examines treadmill curiously",
        "Treadmill fades in from white",
    ),
    (
        "The hedonic treadmill.",
        f"{STYLE} Same treadmill, now with bold label 'THE HEDONIC TREADMILL' stamped across the side. Brain villain stands beside it proudly, one hand on it like a salesman. Clean white background.",
        "Medium wide, villain and treadmill",
        "Spotlight on treadmill and label",
        "Dramatic reveal, villain ownership",
        "Brain villain pats treadmill with pride",
        "Label stamps on with impact",
    ),
    (
        "You run. The belt moves. You stay in exactly the same place.",
        f"{STYLE} Character running on treadmill, legs moving fast. Through a window behind the treadmill: the scenery is static, not moving. Character sweating slightly. No progress.",
        "Medium — character on treadmill",
        "Warm effort lighting, slight sweat sheen",
        "Futility, effort without progress",
        "Running at full effort, zero forward movement",
        "Legs animate, background stays frozen",
    ),
    (
        "Every raise, every upgrade — the belt adjusts to match your speed.",
        f"{STYLE} Treadmill belt with speed dial. As character gets a small 'RAISE +' badge, brain villain turns up the belt speed dial. Character must run faster just to stay in place.",
        "Medium — treadmill speed dial prominent",
        "Slightly adversarial lighting — villain controls",
        "The rigged machine",
        "Brain villain turning speed dial higher with each raise",
        "Speed dial rotates, belt accelerates",
    ),
    (
        "Lottery winners report, within eighteen months of the win, the same levels of financial anxiety they reported before.",
        f"{STYLE} Timeline: LEFT — lottery ticket with large 'YOU WIN!' Champagne, euphoria. CENTER — '18 MONTHS LATER' label. RIGHT — same character at desk, same anxious posture as before. Parallel composition.",
        "Wide timeline, three beats left to right",
        "Left: bright celebratory. Right: same dim anxiety",
        "The reset in action — brutal comparison",
        "Character euphoric left, identical anxiety right",
        "Timeline arrows connect left to right",
    ),
    (
        "Not worse. Not better. The same.",
        f"{STYLE} Two identical anxiety meters side by side: 'BEFORE WIN' and '18 MONTHS AFTER WIN.' Both needles point to same position. Bold label: 'IDENTICAL.' Red underline.",
        "Wide comparison, white background",
        "Clinical neutral light",
        "Shock — the sameness is the point",
        "Character looks between two meters, deflated",
        "Needles align simultaneously",
    ),
    (
        "The money changed the circumstances. The brain changed the baseline.",
        f"{STYLE} Two-column diagram. Left: 'MONEY → CIRCUMSTANCES' with upward arrow (house, car, lifestyle). Right: 'BRAIN → BASELINE' with upward arrow matching exactly. Both arrows identical height.",
        "Wide two-column diagram",
        "Neutral white, informational",
        "The counter-mechanism explained",
        "Brain villain points at right column knowingly",
        "Right column arrow rises to match left in sync",
    ),
    (
        "The treadmill does not care how fast you run.",
        f"{STYLE} Character sprinting on treadmill, sweat flying, legs blurred with speed. Brain villain watching from armchair beside treadmill, legs crossed, utterly unbothered.",
        "Medium wide — both characters",
        "Effort light on character, comfortable light on villain",
        "Indifference of the mechanism",
        "Brain villain sips drink while character exhausts himself",
        "Character blur-runs, villain doesn't move",
    ),
    (
        "It only cares that you keep running.",
        f"{STYLE} Close-up on treadmill power button — glowing green. ON/OFF switch — only 'ON' is illuminated. The 'OFF' button is missing entirely, just a blank space. Brain villain in bg smirking.",
        "Close-up on power panel",
        "Green glow on ON button",
        "The trap with no off switch",
        "Brain villain shrugs in background",
        "Camera slowly pushes in on missing OFF button",
    ),
    # ── THE DIDEROT EFFECT ──
    (
        "In the eighteenth century, the French philosopher Denis Diderot received a gift: a beautiful scarlet robe.",
        f"{STYLE} 18th century French study setting. Diderot character (period clothing — but drawn in same cartoon style) holds up a vivid red/scarlet robe. Eyes wide with delight. Warm candlelight.",
        "Medium, Diderot holding robe up",
        "Warm candlelight, robe glows red",
        "Delight, gift received",
        "Holding robe up admiringly, slight smile",
        "Robe shimmers softly in candlelight",
    ),
    (
        "He loved it.",
        f"{STYLE} Diderot character wearing the scarlet robe, arms wide, spinning slowly in center of his study. Stars of satisfaction orbiting. Warm study interior.",
        "Medium, full character in robe",
        "Warm golden glow surrounding him",
        "Pure satisfaction",
        "Spinning arms-wide, beaming",
        "Stars orbit in a slow circle",
    ),
    (
        "He put it on and immediately noticed that everything else in his study looked shabby by comparison.",
        f"{STYLE} Same study interior. Diderot in scarlet robe looks around. Everything else (chair, desk, curtains, art) now has a gray tint and small 'OLD/SHABBY' labels appearing on each item.",
        "Wide — full study visible",
        "Robe stays vivid red, everything else grays out",
        "Contrast triggered, gap appears",
        "Eyes moving around room, face shifting from joy to dissatisfaction",
        "Gray desaturation spreads from edges inward",
    ),
    (
        "So he replaced his chair. Then his desk. Then the curtains. Then the art on the walls.",
        f"{STYLE} Quick replacement sequence: four panels showing each item being swapped out — old chair → new chair, old desk → new desk, etc. Green checkmarks on new items, red X on old.",
        "Triptych/quad panels",
        "Each new item slightly brighter",
        "The cascade begins",
        "Diderot pointing and directing replacements",
        "Items swap out in rapid sequence left to right",
    ),
    (
        "By the end, he had renovated the entire room — and gone into debt doing it.",
        f"{STYLE} Beautiful renovated study. Diderot sits in it looking pleased — but beside him is a massive DEBT scroll/bill unrolling to the floor. Small worried sweat drop.",
        "Medium wide — beautiful room + debt scroll",
        "Beautiful warm room light vs red debt scroll",
        "Achievement and consequence together",
        "Seated in beautiful room, but holding huge bill",
        "Debt scroll unrolls dramatically downward",
    ),
    (
        "He wrote about it himself. He called it a spiral he could not explain.",
        f"{STYLE} Diderot at desk writing with a quill. A spiral illustration appears on his parchment. He looks up at it, shakes his head slightly. Candlelight.",
        "Medium, writing scene",
        "Warm candlelight",
        "Honest self-observation",
        "Writing intently, pausing to look at spiral",
        "Quill traces spiral on parchment",
    ),
    (
        "The name came later: the Diderot Effect.",
        f"{STYLE} Parchment becomes modern whiteboard. The spiral icon redrawn cleanly. Bold label: 'THE DIDEROT EFFECT.' Arrow showing: one new thing → cascade of replacements.",
        "Wide — whiteboard presentation style",
        "Clean white, label highlighted in red",
        "Naming moment — knowledge solidified",
        "Character points at label from side",
        "Label appears with sharp impact",
    ),
    (
        "One upgrade makes everything adjacent to it feel inadequate.",
        f"{STYLE} New shiny car parked in front of an old garage. The car gleams; the garage visibly looks dingy and old by comparison. Arrow between them: 'MAKES THIS → LOOK LIKE THIS.'",
        "Wide, car and garage side by side",
        "Car in bright spotlight, garage in shadow",
        "Contrast is automatic, involuntary",
        "Character stands between them, seeing both",
        "Garage darkens slightly as car gleams",
    ),
    (
        "The new car makes the old garage unbearable. The new apartment makes the old furniture look wrong.",
        f"{STYLE} Split screen: left — new car next to old garage (labeled 'UNBEARABLE'). Right — new apartment with old worn furniture (labeled 'LOOKS WRONG'). Both have dissatisfied character.",
        "Wide split, two scenes",
        "New items bright, old items gray",
        "The cascade is everywhere",
        "Character in both scenes grimacing at old items",
        "Old items pulse gray to emphasize inadequacy",
    ),
    (
        "The raise that was supposed to create breathing room instead creates a new set of gaps to fill.",
        f"{STYLE} Character holds a raise payslip, looks relieved — 'BREATHING ROOM' label appears. But immediately, gap icons (small chasms) appear around him labeled 'NEW GAP 1,' 'NEW GAP 2,' etc.",
        "Medium wide — character and gaps",
        "Brief warm relief light, then shadows appear",
        "The trap of the raise",
        "Relief → immediately surrounded by gaps",
        "Gap labels pop in around character quickly",
    ),
    (
        "Your consumption does not grow in line with your income.",
        f"{STYLE} Two line graphs: blue line 'INCOME' rising steadily. Red line 'CONSUMPTION' rising faster, already above income line. Both labeled clearly.",
        "Wide line graph, white background",
        "Blue and red lines contrast clearly",
        "The divergence",
        "Brain villain traces the red line with satisfaction",
        "Red line draws ahead of blue, widening gap",
    ),
    (
        "It grows in cascades.",
        f"{STYLE} Waterfall/cascade diagram: one upgrade at top cascades down into 5–6 smaller upgrade icons below it. Each one triggers more. Label: 'THE DIDEROT CASCADE.' Brain villain at top pushing first domino.",
        "Wide cascade diagram",
        "Neutral white, cascade highlighted",
        "The multiplier effect",
        "Brain villain flicks first upgrade into cascade",
        "Cascade falls downward in sequence",
    ),
    # ── THE INDUSTRY ──
    (
        "None of this is accidental.",
        f"{STYLE} Factory exterior: large industrial building labeled 'THE RESET FACTORY.' Smoke from chimneys shaped like currency symbols. Brain villain stands at entrance in factory manager hard hat.",
        "Wide, factory exterior",
        "Industrial gray, villain in spotlight at entrance",
        "Conspiracy reveal — systemic not personal",
        "Brain villain adjusts hard hat, nods at factory",
        "Camera slowly pulls back to reveal full factory scale",
    ),
    (
        "The consumer economy is calibrated to the reset.",
        f"{STYLE} Inside the factory: conveyor belt producing 'RESET' boxes. Workers (generic characters) packaging them efficiently. Brain villain oversees from elevated platform.",
        "Wide interior, conveyor belt visible",
        "Industrial lighting, brain villain elevated",
        "Systemic production of the mechanism",
        "Brain villain surveys factory floor with satisfaction",
        "Conveyor belt moves steadily left to right",
    ),
    (
        "It does not sell you things you need. It sells you the next version of your baseline.",
        f"{STYLE} Store shelf. Left side: items labeled 'WHAT YOU NEED' — plain, functional, unsold. Right side: items labeled 'YOUR NEW BASELINE' — shiny, aspirational, flying off shelves.",
        "Wide store shelf, two sections",
        "Left section dimly lit, right section bright spotlight",
        "The real product being sold",
        "Character reaches for right section automatically",
        "Right section items glow as hand reaches for them",
    ),
    (
        "Planned obsolescence ensures that what you own today feels inadequate within two years.",
        f"{STYLE} Phone on table. Calendar pages flip: TODAY — phone looks fine. 6 MONTHS — slight gray tinge. 2 YEARS — phone looks ancient, red 'OUTDATED' stamp appears. New model glows behind it.",
        "Wide, phone and calendar side by side",
        "Phone ages and dims as time passes",
        "Engineered inadequacy — time-stamped",
        "Character watching phone age, looking increasingly dissatisfied",
        "Calendar pages flip, phone grays out progressively",
    ),
    (
        "The subscription economy charges you monthly so each payment feels too small to cancel — while the total cost stays invisible.",
        f"{STYLE} Character's phone showing many subscription logos (generic icons). Each shows a small monthly amount (€9, €12, €8). Below them, a total adds up to a large annual sum — but character only sees the small numbers.",
        "Medium close-up, phone subscription list",
        "Phone glow, each payment feels small",
        "Death by a thousand small cuts",
        "Character glances at small numbers, shrugs each time",
        "Annual total appears at bottom, large and red",
    ),
    (
        "Consumer credit exists to close the gap between what you earn and what the reset tells you that you should have.",
        f"{STYLE} Gap diagram: income line lower, reset/lifestyle line higher. Between them: a bridge made of credit cards spanning the gap. Label: 'CONSUMER CREDIT — THE BRIDGE.'",
        "Wide gap diagram with credit card bridge",
        "Green income, red lifestyle, credit bridge in between",
        "Credit as the mechanism's enabler",
        "Brain villain builds the bridge from below, satisfied",
        "Bridge assembles itself from credit cards",
    ),
    (
        "The average household carries credit card debt not because of emergencies.",
        f"{STYLE} Average house exterior, label 'AVERAGE HOUSEHOLD.' Credit card emerging from mailbox with a debt amount on it. No emergency icon — just the regular lifestyle.",
        "Medium wide, house and mailbox",
        "Ordinary suburban lighting",
        "Normalised debt",
        "Character collects credit bill from mailbox, unsurprised",
        "Bill slides out of mailbox slowly",
    ),
    (
        "Because the lifestyle expanded before the income did.",
        f"{STYLE} Timeline bar: LIFESTYLE bar shoots up early. INCOME bar follows behind, never quite catching up. Gap between them labeled 'DEBT.' Brain villain drew the lifestyle bar first.",
        "Wide timeline bar chart",
        "Lifestyle bar red, income bar green",
        "The sequence that creates the trap",
        "Brain villain points at the gap proudly",
        "Lifestyle bar shoots up ahead of income",
    ),
    (
        "Your bank does not want you to be financially free.",
        f"{STYLE} Large cartoon bank building with smiling face on its facade. Inside: stacks of money. Outside: character looking at bank, small chained wallet around his wrist. Bank facade smile is slightly sinister.",
        "Wide, bank facade + character",
        "Bank bright and welcoming; chain on wallet visible",
        "The bank's incentive revealed",
        "Character looks at bank, then at chained wallet",
        "Chain on wallet clinks subtly",
    ),
    (
        "Financial freedom means you stop borrowing.",
        f"{STYLE} Character cutting a credit card in half with scissors. Chain around wallet falls off. Label: 'FINANCIAL FREEDOM.' Bank building in background — lights going out one by one as character cuts card.",
        "Medium — character cutting card",
        "Bright on character, bank dims behind",
        "The bank's fear",
        "Scissors cut through card decisively",
        "Bank lights flicker out as card is cut",
    ),
    (
        "The product they are selling is the gap between your income and your reset.",
        f"{STYLE} Product box on store shelf: label reads 'THE GAP™' — brain villain's logo on it. Gap diagram printed on the box. Price tag shows 'INTEREST RATE %.'",
        "Medium — product box in foreground",
        "Retail spotlight on product box",
        "The actual product named and boxed",
        "Brain villain holds up the box like a salesman",
        "Camera zooms in on 'THE GAP™' label",
    ),
    (
        "The wider the gap, the more interest you pay.",
        f"{STYLE} Gap diagram again — but now the gap is shown as a jar filling with red liquid labeled 'INTEREST.' The wider the gap arrow, the more the jar fills. Brain villain pours more in.",
        "Wide diagram, jar prominent",
        "Red interest liquid fills ominously",
        "The cost of the mechanism made visible",
        "Brain villain pours interest into widening gap",
        "Jar fills as gap widens",
    ),
    (
        "The treadmill is not a metaphor. It is a business model.",
        f"{STYLE} Treadmill with 'BUSINESS MODEL' label replacing 'THE HEDONIC TREADMILL.' Brain villain stands next to it holding a pie chart showing his profits. Character still running on it.",
        "Medium wide — treadmill and villain",
        "Business-like cold lighting",
        "The coldest truth of the video",
        "Villain holds up profit chart while character runs",
        "Label on treadmill swaps from metaphor to business model",
    ),
    # ── THE POPULAR MISREADING ──
    (
        "Everyone who understands this arrives at the same conclusion.",
        f"{STYLE} Multiple generic characters in a row, each with a thought bubble. All thought bubbles show identical lightbulb icon. Label above: 'EVERYONE THINKS THE SAME THING.'",
        "Wide — row of characters",
        "Neutral white, identical thought bubbles",
        "Universal misreading setup",
        "All characters nod simultaneously",
        "Thought bubbles pop in one by one, all identical",
    ),
    (
        "The solution is discipline. Willpower. Spend less.",
        f"{STYLE} Same characters from prev beat — now each holds a 'WILLPOWER' dumbbell and a 'DISCIPLINE' planner. Looking determined. Label: 'JUST TRY HARDER.'",
        "Wide — same characters with new items",
        "Motivational bright light",
        "The intuitive but wrong answer",
        "Characters flex willpower dumbbells",
        "Dumbbells appear in hands with a 'clang'",
    ),
    (
        "That is not what happens.",
        f"{STYLE} Large red X stamped over the willpower dumbbell and discipline planner. Characters deflate. Brain villain in corner shaking head slowly — not gloating, just knowing.",
        "Wide — X stamp over previous scene",
        "Red X dominates frame",
        "Deflation of the obvious answer",
        "Characters droop, dumbbells fall",
        "Red X slams down with impact",
    ),
    (
        "Willpower is a finite resource. It depletes.",
        f"{STYLE} Willpower meter (like a phone battery). Starts full green. Throughout the day (morning → afternoon → evening timeline), it drains: 60%, 40%, 10%, then red and empty.",
        "Wide — battery meter and day timeline",
        "Battery drains from green to red",
        "The depletion is measurable, inevitable",
        "Character gets progressively more tired as battery drains",
        "Battery depletes in stages",
    ),
    (
        "A strategy that requires you to constantly resist your own baseline fails the moment your attention is elsewhere.",
        f"{STYLE} Character trying to hold back a wall of baseline lifestyle items (car, apartment, phone, clothes) with both hands — straining. One moment distracted (looking left) and the wall breaks through.",
        "Wide — character vs wall of upgrades",
        "Strain lighting — effort visible",
        "The inevitable failure of resistance",
        "Character strains to hold back wall, then looks away briefly",
        "Wall bursts through when character looks away",
    ),
    (
        "The people who escape the treadmill do not do it by spending less through force.",
        f"{STYLE} Two characters: LEFT — straining against lifestyle wall (struggling, failing). RIGHT — standing calm beside a treadmill that is not running. Right character looks peaceful, not straining.",
        "Wide comparison — two characters",
        "Left: strain lighting. Right: peaceful warm light",
        "The contrast between the two approaches",
        "Left character strains; right character stands at ease",
        "Right character's treadmill is visibly switched off",
    ),
    (
        "They do it by changing what their brain registers as the reference point.",
        f"{STYLE} Brain villain's recalibration dial from earlier — but now a different character (calm one from prev beat) is turning it manually, deliberately setting it LOWER. Label: 'CHOOSE YOUR BASELINE.'",
        "Medium close-up — dial being turned",
        "Calm purposeful light",
        "Agency — the dial can be set intentionally",
        "Calm character turns dial to lower position deliberately",
        "Dial turns with a satisfying click implied",
    ),
    (
        "Not by earning more.",
        f"{STYLE} Income arrow pointing upward — but a red X through it labeled 'NOT THE ANSWER.' Character looks at upward arrow, shakes head.",
        "Medium — arrow with X",
        "Neutral white, X prominent",
        "Counterintuitive — earning more is not the fix",
        "Character shakes head at income arrow",
        "X slides over income arrow",
    ),
    (
        "By deciding — in advance, automatically — what the baseline will not include.",
        f"{STYLE} Contract-style document: 'MY BASELINE AGREEMENT.' Character signing it. Key line visible: 'THE FOLLOWING ARE NOT INCLUDED IN MY NORMAL.' List below: luxury items, latest phone, etc. Peaceful expression.",
        "Medium — character signing document",
        "Warm purposeful light",
        "Agency and automation — the actual solution",
        "Character signs with a deliberate pen stroke",
        "Signature completes with a satisfying flourish",
    ),
    # ── THE REAL CONCLUSION ──
    (
        "In 1974, the economist Richard Easterlin published a finding that became one of the most discussed in his field.",
        f"{STYLE} Book cover: 'EASTERLIN 1974' with a simple graph on the cover showing the paradox. Historical academic setting but clean cartoon style. Character holds the book open.",
        "Medium — character with book",
        "Neutral academic light",
        "Credibility anchor",
        "Character opens book, looks at graph inside",
        "Book opens with a page-turn effect",
    ),
    (
        "Across countries, across income levels, across decades — beyond a certain threshold, more money does not produce more wellbeing.",
        f"{STYLE} World map with income-vs-happiness data overlaid: rising income bars (green) across multiple countries, but happiness lines (yellow) flatline above a threshold. Bold label: 'BEYOND THIS POINT →'",
        "Wide world map infographic",
        "Clean informational, world map prominent",
        "Global scale of the finding",
        "Character traces the flatline with one finger",
        "Flatline draws across map after income bars rise",
    ),
    (
        "Countries that had grown significantly richer over thirty years showed no significant increase in reported happiness.",
        f"{STYLE} Two-line chart: 'GDP PER CAPITA' line climbs steeply over 30 years (green). 'REPORTED HAPPINESS' line stays flat (yellow). Both clearly labeled. Time axis: '1960 → 1990.'",
        "Wide line chart, white background",
        "Green climbs, yellow stays flat",
        "The paradox in data",
        "Brain villain looks at flat yellow line, satisfied",
        "Green line climbs while yellow holds flat",
    ),
    (
        "He called it the Easterlin Paradox.",
        f"{STYLE} Bold diegetic label: 'THE EASTERLIN PARADOX.' Below it: the two-line chart (one up, one flat). Clean white background. Character points at label.",
        "Wide, label centered",
        "Clean white, label in red",
        "Naming moment",
        "Character points at paradox label",
        "Label appears with a sharp stamp effect",
    ),
    (
        "The paradox is only a paradox if you believe money accumulates into wellbeing.",
        f"{STYLE} Money pile on left side of scale. Wellbeing/happiness icon (sun) on right side. Money pile grows — but happiness side doesn't move. Arrow showing: 'MONEY ≠ WELLBEING.'",
        "Wide balance scale",
        "Neutral white, scale prominent",
        "The false assumption exposed",
        "Character adds money to scale, checks happiness side — nothing moves",
        "Happiness side stays still despite money piling on",
    ),
    (
        "It does not. It accumulates into baseline.",
        f"{STYLE} Same scale. Money now pouring into a 'BASELINE' bucket instead of the happiness side. Bucket labeled 'BASELINE' fills up. The happiness icon gets nothing.",
        "Wide — scale with baseline bucket",
        "Neutral, slight red on baseline bucket",
        "The actual accumulation target revealed",
        "Brain villain redirects money from happiness to baseline bucket",
        "Money stream reroutes with a satisfying redirect",
    ),
    (
        "Enough is not a number.",
        f"{STYLE} Giant digital number display — cycling through amounts ($10k, $50k, $200k, $1M). Question mark at the end. Character watches numbers cycle, looking unsatisfied at each.",
        "Wide — large number display",
        "Numbers glow but feel cold",
        "Numbers cannot define enough",
        "Character shakes head at each number",
        "Numbers cycle rapidly, then land on '?'",
    ),
    (
        "Enough is a decision.",
        f"{STYLE} Number display replaced by a single word: 'ENOUGH.' Below it, a contract being signed by the character. Calm warm lighting. No more cycling — stillness.",
        "Medium — character signing",
        "Warm calm light — stillness",
        "Agency — the actual answer",
        "Character signs with calm deliberation",
        "'ENOUGH' appears in large clean letters",
    ),
    (
        "The people who feel rich are not the ones with the most money.",
        f"{STYLE} Two characters side by side: LEFT — wealthy character (mansion, cars, label '$$$$$') but looking stressed, anxious. RIGHT — modest character (small house, label '$$') but smiling, relaxed.",
        "Wide comparison",
        "Left: cold wealth light. Right: warm content light",
        "The inversion of the assumption",
        "Left character counts money anxiously; right stands peacefully",
        "Contrast between the two is the entire frame",
    ),
    (
        "They are the ones who stopped moving the finish line.",
        f"{STYLE} Finish line planted firmly in the ground. Calm character from prev beat has hammered it in — flag in ground. Brain villain tries to pull it further but it won't move. Character stands past the finish line.",
        "Wide — finish line and both characters",
        "Warm triumphant light on calm character",
        "The decision made, the escape achieved",
        "Calm character plants flag, finish line holds",
        "Brain villain tugs finish line — it doesn't move",
    ),
    (
        "And they did it before the next raise arrived.",
        f"{STYLE} Calendar showing 'NEXT RAISE: JUNE.' Character already has automatic transfer set up on laptop — '10% AUTO-TRANSFER' active. Done before the raise lands. Calm, prepared expression.",
        "Medium — character at laptop, calendar visible",
        "Warm proactive light",
        "The timing that makes it work",
        "Character already set up transfer, closing laptop satisfied",
        "Calendar date and transfer confirmation in frame together",
    ),
    # ── EL MOVIMIENTO ──
    (
        "Here is what you do with this.",
        f"{STYLE} Character stands center, rolled-up sleeves, determined expression. Clean white background. Label above: 'EL MOVIMIENTO.' Five action icons arranged in a row below him.",
        "Medium, centered, white background",
        "Bright purposeful light",
        "Transition to agency — empowerment",
        "Character rolls up sleeves, ready",
        "Five action icons slide in below",
    ),
    (
        "Automate ten percent of every payslip before it hits your account. Your baseline never sees it.",
        f"{STYLE} Payslip arriving. Automated arrow splits it: 90% → current account (labeled 'BASELINE SEES THIS'), 10% → savings vault (labeled 'BASELINE NEVER SEES THIS'). Clean diagram.",
        "Wide split-flow diagram",
        "Green savings flow prominent",
        "Simple automated action",
        "Character watches automation work without doing anything",
        "Arrow splits payslip automatically",
    ),
    (
        "Next raise: freeze your lifestyle for one year. Bank the entire difference.",
        f"{STYLE} Raise arrives ('+15%' badge). Character's lifestyle items (apartment, car) shown with a 'FROZEN' ice block over them — unchanged. Difference arrow points straight to savings vault.",
        "Wide — raise badge, frozen lifestyle, savings",
        "Cool ice-blue on frozen items",
        "The raise intercepted before the treadmill speeds up",
        "Character holds raise badge, points to savings, not upgrades",
        "Ice block appears over lifestyle with a freeze effect",
    ),
    (
        "Check your bank statement right now. Cancel one subscription you forgot you had.",
        f"{STYLE} Bank statement on screen. Multiple subscription lines. One highlighted in yellow: a service the character clearly doesn't remember. Cancel button in red. Character's surprised expression.",
        "Medium close-up — statement on screen",
        "Statement glow, one line highlighted",
        "Immediate actionable step",
        "Character squints at forgotten subscription, clicks cancel",
        "Cancel button pressed, subscription line disappears",
    ),
    (
        "Build three months of expenses in a separate account you cannot see daily. That buffer kills more anxiety than any raise.",
        f"{STYLE} New bank account card labeled 'EMERGENCY BUFFER — DO NOT CHECK DAILY.' Three months of expenses visible as a filled meter. Character's anxiety cloud above head — shrinking as buffer fills.",
        "Medium — buffer account and anxiety meter",
        "Warm steady light — security",
        "The buffer as anxiety reducer",
        "Character watches anxiety cloud shrink as buffer fills",
        "Anxiety cloud deflates as buffer meter fills",
    ),
    (
        "Raise your pension contribution by one percent this year. Over thirty years, that single percent compounds into more than most bonuses.",
        f"{STYLE} Pension contribution dial: moving from current % to +1% higher. Below it: compound growth chart showing the 1% snowballing over 30 years into a large final amount. Label: '30 YEARS LATER.'",
        "Wide — dial and compound chart",
        "Green compound growth glows",
        "Long-term power of small action",
        "Character turns dial one click, watches chart explode upward",
        "Compound curve shoots upward dramatically",
    ),
    # ── THE ENDING ──
    (
        "You cannot stop the reset.",
        f"{STYLE} Treadmill still running, belt moving. Character standing beside it — not on it, but it's still running. No off switch. Calm acceptance rather than defeat.",
        "Medium — character beside treadmill",
        "Neutral realistic light",
        "Acceptance, not defeat",
        "Character looks at running treadmill, nods",
        "Treadmill runs but character is beside it, not on it",
    ),
    (
        "Your brain will always recalibrate.",
        f"{STYLE} Brain villain inside the transparent skull — still adjusting the baseline dial. Can't be removed. Character looks at his own head with the brain doing its thing. Calm acceptance.",
        "Medium close — character's head, brain visible",
        "Warm neutral light",
        "The mechanism is permanent but manageable",
        "Character observes brain recalibrating, not fighting it",
        "Baseline dial moves slightly, character unbothered",
    ),
    (
        "But you can stop funding the next version of the baseline with money that should be building your future.",
        f"{STYLE} Money flow diagram: before — all money going to 'NEXT BASELINE' upgrade icons. After — money split: some to baseline, larger portion going to 'YOUR FUTURE' vault. Character controls the valve.",
        "Wide flow diagram — before and after",
        "Future vault glows warm gold",
        "The controllable choice",
        "Character turns valve — more money flows to future",
        "Valve turns, flow shifts toward future vault",
    ),
    (
        "The treadmill runs whether you fight it or not.",
        f"{STYLE} Treadmill running in background. Character in foreground facing viewer, arms crossed, calm. Not fighting the treadmill. Not on it. Just aware of it. Slight knowing expression.",
        "Medium — character foreground, treadmill background",
        "Character in warm light, treadmill in background",
        "Calm awareness replaces resistance",
        "Arms crossed, calm expression, not engaging with treadmill",
        "Slow zoom out reveals character's full composure",
    ),
    (
        "The question is whether you are putting something aside before you step back on.",
        f"{STYLE} Character standing at treadmill. In one hand: savings contribution slip going into vault. Then stepping onto treadmill. The vault is filled before the run begins.",
        "Medium wide — vault, character, treadmill sequence",
        "Vault glows warm before treadmill starts",
        "The order of operations is everything",
        "Character deposits into vault first, then steps on treadmill",
        "Vault fills, then character steps on — sequence visible",
    ),
    (
        "Every video on this channel is one way your financial gut has been engineered against you.",
        f"{STYLE} Video thumbnails arranged in a grid (generic rectangular placeholders). Each thumbnail glows briefly. Character stands in front watching them. Label: 'YOUR FINANCIAL GUT — ENGINEERED.'",
        "Wide — thumbnail grid and character",
        "Each thumbnail pulses with brief glow",
        "Channel series call-back",
        "Character gestures at the grid",
        "Thumbnails light up one by one",
    ),
    (
        "This is how they turned your raise into their revenue.",
        f"{STYLE} Final frame: brain villain facing viewer directly, holding a stack of money with a smug smile. Behind him, the treadmill running with a generic character on it. Direct eye contact with viewer.",
        "Medium — villain direct address to camera",
        "Villain in dramatic spotlight, character on treadmill behind",
        "Final reveal, fourth wall break, memorable close",
        "Brain villain holds money up, smirks directly at viewer",
        "Slow zoom in on villain's smug face",
    ),
]

SECTION_STARTS = {
    1:   "HOOK",
    10:  "THE RAISE",
    22:  "THE MECHANISM",
    35:  "THE TREADMILL",
    44:  "THE DIDEROT EFFECT",
    56:  "THE INDUSTRY",
    69:  "THE POPULAR MISREADING",
    78:  "THE REAL CONCLUSION",
    89:  "EL MOVIMIENTO",
    95:  "THE ENDING",
}


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = title_p.add_run("CRAYON CAPITAL — CLONE SESSION · VIDEO 8")
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
    r = t_p.add_run("Getting Rich Is Making You Poorer")
    r.bold = True
    r.italic = True
    r.font.size = Pt(16)

    doc.add_paragraph()

    HDR = ["#", "NARRATION", "IMAGE PROMPT", "CAMERA", "LIGHTING", "MOOD", "CHARACTER ACTION", "VIDEO MOTION"]
    tbl = doc.add_table(rows=1, cols=8)
    tbl.style = 'Table Grid'
    hdr_cells = tbl.rows[0].cells
    col_widths_cm = [0.8, 4.5, 6.5, 3.0, 2.8, 2.8, 3.0, 3.2]
    from docx.shared import Cm
    for i, (cell, txt, w) in enumerate(zip(hdr_cells, HDR, col_widths_cm)):
        cell.width = Cm(w)
        p = cell.paragraphs[0]
        run = p.add_run(txt)
        run.bold = True
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        from docx.oxml.ns import qn
        from docx.oxml import OxmlElement
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), '2C3E50')
        tcPr.append(shd)

    current_section = None
    for beat_num, beat in enumerate(BEATS, 1):
        if beat_num in SECTION_STARTS:
            current_section = SECTION_STARTS[beat_num]
            sec_row = tbl.add_row()
            sec_cells = sec_row.cells
            for i in range(1, 8):
                sec_cells[0].merge(sec_cells[i])
            p = sec_cells[0].paragraphs[0]
            run = p.add_run(f"── {current_section} ──")
            run.bold = True
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            from docx.oxml.ns import qn
            from docx.oxml import OxmlElement
            tc = sec_cells[0]._tc
            tcPr = tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), 'B02A2A')
            tcPr.append(shd)

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
                from docx.oxml.ns import qn
                from docx.oxml import OxmlElement
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                shd = OxmlElement('w:shd')
                shd.set(qn('w:val'), 'clear')
                shd.set(qn('w:color'), 'auto')
                shd.set(qn('w:fill'), 'F9F9F9')
                tcPr.append(shd)

    all_lines = [b[0] for b in BEATS]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = len(BEATS)

    doc.add_paragraph()
    foot = doc.add_paragraph()
    foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = foot.add_run(f"END · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Treadmill_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
