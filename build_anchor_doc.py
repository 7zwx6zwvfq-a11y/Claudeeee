#!/usr/bin/env python3
"""Production document for Video 9: The First Number They Show You in a Job Interview Is Not an Offer."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

STYLE = ("2D flat cartoon illustration, thick solid black outlines on every element, "
         "clean solid color fills, no gradients except soft warm ambient light. "
         "Two recurring characters: JAKE — large beige oval head with transparent glass upper "
         "skull revealing a pink cartoon brain inside, black spiky hair, navy blue t-shirt, "
         "gray pants; MARCUS — large beige oval head with transparent glass upper skull "
         "revealing a pink cartoon brain inside, short blonde/yellow hair, orange t-shirt, "
         "gray pants. Brain villain: pink cartoon brain character, smug heavy-lidded eyes, "
         "slight smirk, small teeth, navy t-shirt. Palette: beige skin, pink brain (#E8A598), "
         "navy blue, orange, green dollar bills, red for X-marks and danger, white for "
         "diagram/infographic scenes, warm beige interiors with soft oval ceiling spotlight, "
         "dark gray for void/loss scenes. Bold black diegetic text labels integrated into "
         "the scene. 16:9, 1280x720.")

BEATS = [
    # ── HOOK ──
    (
        "You walked out of that interview feeling like you won.",
        f"{STYLE} JAKE (navy t-shirt, black spiky hair, transparent skull with pink brain) exits office building, thumbs up, slight smile. Briefcase in hand. Warm exterior light.",
        "Medium shot, slightly low angle",
        "Warm afternoon sun, confident",
        "Victory, earned pride",
        "Thumbs up, walking forward",
        "Slow push forward as Jake exits",
    ),
    (
        "You negotiated. They started at $38,000. You pushed back. They came up to $42,000.",
        f"{STYLE} JAKE holds offer letter. Two numbers visible: $38,000 crossed out in red, $42,000 circled in green. Jake's brain inside skull glowing with satisfaction.",
        "Medium, document prominent",
        "Warm spotlight on paper",
        "Satisfaction, earned win",
        "Holding letter up, brain visibly pleased",
        "Green circle pulses gently on $42,000",
    ),
    (
        "Four thousand dollars more than they offered. You did better than most people.",
        f"{STYLE} JAKE at home, feet up, coffee in hand. Phone shows bank notification. Small label: '+$4,000' floating above him. Relaxed.",
        "Medium wide, home setting",
        "Warm home light, evening",
        "Contentment, relaxation",
        "Feet up, satisfied posture",
        "'+$4,000' label floats up gently",
    ),
    (
        "The salary band for that role was $48,000 to $62,000.",
        f"{STYLE} Internal HR document revealed: 'SALARY BAND: $48,000 — $62,000.' Jake's celebrated $42,000 circled in red at the bottom of the range, far below the midpoint. Jake unaware in background.",
        "Wide — document foreground, Jake blurred behind",
        "Cold reveal light on document",
        "Dramatic reveal, the gap exposed",
        "Jake celebrating in background, unaware",
        "Document slides up from bottom of frame",
    ),
    (
        "You never knew.",
        f"{STYLE} Close-up on JAKE's face. The HR document now visible to him — his brain inside the transparent skull visibly reacting, eyes wide, mouth slightly open. Label: 'YOU NEVER KNEW.'",
        "Close-up, Jake's face",
        "Cooler, realisation light",
        "Shock, dawning understanding",
        "Brain reacting visibly inside skull",
        "Slow zoom in on Jake's expression",
    ),
    (
        "The $4,000 you won was measured against a number they chose.",
        f"{STYLE} Scale/balance: left side '$4,000 YOU WON' (small, green). Right side 'THEIR NUMBER' (large anchor bolt, heavy). The $4,000 win looks tiny relative to the anchor.",
        "Wide, balance scale centered",
        "Neutral white, scale prominent",
        "The real measurement exposed",
        "Brain villain's hand placed the anchor on the right side",
        "Scale tips heavily toward anchor side",
    ),
    (
        "Not against what the role was worth. Against the anchor they set.",
        f"{STYLE} Same scale, but now shows full band $48k-$62k on right side. Jake's $42k result is far below even the floor of the band. Label: 'REAL VALUE' pointing to band. 'YOUR RESULT' pointing to $42k.",
        "Wide, scale with full band visible",
        "Red accent on the gap between Jake's result and the real band",
        "Devastating comparison",
        "Jake looks at scale, brain deflates slightly",
        "Real value band drops in from above",
    ),
    (
        "That anchor — and everything that compounded from it — is what this video is about.",
        f"{STYLE} Large anchor bolt icon center frame, labeled 'THE ANCHOR.' From it, compound arrows spread outward showing: salary, pension, raises, lifetime earnings. Brain villain stands beside it, hand on it proudly.",
        "Wide, anchor with spreading compound arrows",
        "Villain in slight red backlight",
        "Scale of the mechanism revealed",
        "Brain villain pats anchor with satisfaction",
        "Compound arrows radiate outward from anchor",
    ),
    # ── THE INTERVIEW ──
    (
        "His name is Jake. He is twenty-four years old and this is his first real interview.",
        f"{STYLE} JAKE (age 24, label 'AGE 24' above him) stands outside a glass office building in his navy t-shirt, transparent skull visible, black spiky hair. Slightly nervous but ready.",
        "Medium, Jake outside building",
        "Bright professional daylight",
        "Youth, anticipation, readiness",
        "Standing straight, adjusting collar slightly",
        "Camera slowly pulls back to reveal building",
    ),
    (
        "He has prepared. He knows the company. He knows the role. He is ready.",
        f"{STYLE} JAKE at desk the night before — notes spread out, laptop open with company website. Brain inside skull glowing with preparation energy. Highlighters, printed pages.",
        "Medium wide, preparation scene",
        "Warm desk lamp light, evening",
        "Diligent preparation",
        "Highlighting notes, brain actively engaged",
        "Pan across preparation materials",
    ),
    (
        "The HR manager smiles and slides a paper across the desk.",
        f"{STYLE} HR manager (generic character, suit, glasses, warm smile) slides a folded paper across a clean desk toward JAKE. Jake's hands reach for it. Professional office setting.",
        "Medium two-shot, desk between them",
        "Professional office light, ceiling spotlight",
        "Formal warmth, professional ritual",
        "HR manager's hand pushing paper, Jake's hand receiving",
        "Paper slides across desk in slow motion",
    ),
    (
        "The number on it is $36,000.",
        f"{STYLE} Close-up: paper opened, '$36,000' in large bold font. JAKE's hands holding the edges. The number dominates the frame. Nothing else on the paper visible.",
        "Extreme close-up, number fills frame",
        "Spotlight on number",
        "The anchor lands",
        "Hands grip paper edges",
        "Number appears with a subtle impact",
    ),
    (
        "'We think this reflects your experience level,' she says. 'There is room to grow.'",
        f"{STYLE} HR manager speaking, confident smile, hand gesturing reassuringly. JAKE listening, brain inside skull visibly processing. Speech bubble shows her words in neat text.",
        "Medium two-shot",
        "Warm professional light",
        "Reassurance, institutional warmth",
        "HR manager gesturing, Jake nodding",
        "Speech bubble appears and fades",
    ),
    (
        "Jake feels the pull immediately. His current salary is $31,000. This is a sixteen percent raise.",
        f"{STYLE} JAKE's thought bubble: '$31,000 → $36,000 = +16%' with upward green arrow. Brain inside skull lights up green with the gain calculation. His expression: quiet excitement.",
        "Medium, Jake with thought bubble",
        "Warm internal thought lighting",
        "The anchor working — gain feels real",
        "Brain visibly calculating, lighting up green",
        "Thought bubble numbers animate in",
    ),
    (
        "He counters. She says she can go to $39,000. Jake accepts.",
        f"{STYLE} JAKE speaking assertively (counter-offer gesture). HR manager pausing, then sliding new paper: '$39,000.' Jake extending hand for handshake. Brain in skull: satisfied glow.",
        "Medium two-shot, handshake moment",
        "Warm office light",
        "Negotiation won — or so it seems",
        "Handshake, both nodding",
        "Handshake held, brief warm glow",
    ),
    (
        "He drives home feeling like he won the negotiation.",
        f"{STYLE} JAKE driving, one hand on wheel, slight smile. Brain inside transparent skull visibly content, small victory stars orbiting. Cityscape passing outside window.",
        "Medium — driving scene, city behind",
        "Golden hour exterior light",
        "Victory, earned satisfaction",
        "One hand on wheel, relaxed posture",
        "Stars orbit inside transparent skull",
    ),
    (
        "The salary band for that role was $40,000 to $55,000.",
        f"{STYLE} Same HR desk but now empty. A confidential file opens itself to reveal: 'ROLE SALARY BAND: $40,000 — $55,000.' Jake's accepted $39,000 shown below the floor. Label: 'BELOW BAND FLOOR.'",
        "Wide — desk with document",
        "Cold reveal light",
        "Devastating quiet reveal",
        "Document opens itself, no one watching",
        "Band document appears, Jake's number shown below floor",
    ),
    (
        "He would not learn this for eleven years.",
        f"{STYLE} JAKE at desk, older (label 'AGE 35'). Same navy t-shirt, same transparent skull. Working away, unaware. Calendar on wall. Small label bottom of frame: '11 YEARS LATER.'",
        "Medium, Jake at desk",
        "Ordinary office light — nothing remarkable",
        "Quiet tragedy, mundane unawareness",
        "Working normally, no idea",
        "Calendar pages blur past briefly",
    ),
    # ── THE MECHANISM ──
    (
        "Here is what happened in that room.",
        f"{STYLE} Cross-section diagram of JAKE's head — transparent skull with brain inside shown as an anatomy chart. Arrow pointing into the brain: 'THE MECHANISM.' Clean white background.",
        "Medium close-up, head cross-section diagram",
        "Clinical white, brain highlighted",
        "Transition to explanation mode",
        "Jake's head tilted, diagram lines appearing",
        "Diagram lines draw in cleanly",
    ),
    (
        "Before Jake saw the number, he had no anchor.",
        f"{STYLE} JAKE standing in white void. Brain inside skull shown as open, floating, with question marks and floating values orbiting loosely. Nothing fixed. Label: 'NO REFERENCE POINT.'",
        "Wide, white void setting",
        "Pure white, open feeling",
        "Open, undefined — the pre-anchor state",
        "Arms slightly open, brain with floating values",
        "Values orbit loosely, nothing anchored",
    ),
    (
        "His brain was open. The market rate, the role value, his own worth — all of it was floating, undefined.",
        f"{STYLE} Inside JAKE's transparent skull: floating icons — '$52k MARKET,' '$48k ROLE VALUE,' '$45k SELF-WORTH' — all drifting freely, no hierarchy. Brain watching them float.",
        "Close-up, inside skull visualization",
        "Soft open light inside skull",
        "Possibility, undefined space",
        "Brain watching floating values with curiosity",
        "Values drift slowly in different directions",
    ),
    (
        "The moment $36,000 appeared on that paper, his brain locked onto it.",
        f"{STYLE} The '$36,000' number appears in JAKE's skull space. Instantly all other floating values stop. The brain snaps its gaze to $36,000. Magnetic pull lines radiating from the number.",
        "Close-up inside skull",
        "Sudden spotlight on $36,000",
        "The lock-in — decisive moment",
        "Brain snaps attention to $36,000 immediately",
        "All other values freeze as $36,000 appears",
    ),
    (
        "Not as a starting point. As a reference.",
        f"{STYLE} '$36,000' now at the center of JAKE's skull, glowing, with a gravitational field around it. Other numbers now orbit IT. Label: 'REFERENCE — NOT START POINT.'",
        "Close-up, skull interior",
        "Gravitational warm glow on $36,000",
        "The anchor embedded",
        "Brain watching $36,000 as fixed center",
        "$36,000 pulses as gravitational center",
    ),
    (
        "Every number after that was evaluated in relation to it.",
        f"{STYLE} Diagram: $36,000 fixed at center. Arrows from it to other numbers: '+$3k = WIN,' '+$6k = GREAT,' '-$2k = LOSS.' All relative to anchor. Brain villain drew the diagram.",
        "Wide diagram, white background",
        "Neutral informational light",
        "Relativity of all subsequent values",
        "Brain villain points at diagram arrows",
        "Arrows draw from anchor outward",
    ),
    (
        "$39,000 felt like a win because it was $3,000 more than $36,000.",
        f"{STYLE} '$39,000 vs $36,000' on a scale. Left side heavy: '$3,000 MORE' in green. JAKE's brain inside skull glowing green — WIN signal. The anchor is the measurement tool.",
        "Wide, scale comparison",
        "Green glow on WIN side",
        "The false victory crystallized",
        "Jake's brain celebrating the green $3k",
        "Green WIN glow pulses",
    ),
    (
        "Not because $39,000 was a fair price for the work. Because it was higher than the anchor.",
        f"{STYLE} Same scale but now 'MARKET VALUE $52,000' added on right side. Jake's $39,000 suddenly looks tiny. His brain's green WIN glow fades. Label: 'FAIR PRICE' vs 'ANCHOR PRICE.'",
        "Wide, scale with market value added",
        "Green fades, neutral reality sets in",
        "The illusion exposed",
        "Jake's brain glow dims as real value appears",
        "Market value drops in, scale tips the other way",
    ),
    (
        "This is called anchoring bias.",
        f"{STYLE} Bold diegetic label center frame: 'ANCHORING BIAS.' Below it: anchor bolt icon + brain icon connected by arrow. JAKE stands beside it, pointing. Clean white background.",
        "Wide, centered on label",
        "Clean white, red label",
        "Conceptual anchor — naming the mechanism",
        "Jake points at label from below",
        "Label types on with sharp effect",
    ),
    (
        "The first number introduced in any negotiation becomes the gravitational center of everything that follows.",
        f"{STYLE} Solar system diagram: '$36,000' as the sun at center, other values as planets orbiting at different distances. Gravitational field lines visible. Label: 'GRAVITATIONAL CENTER.'",
        "Wide, solar system diagram",
        "Warm gravitational glow on center",
        "Scale and inevitability of the mechanism",
        "Brain villain points at the sun/anchor",
        "Planets orbit in slow animation",
    ),
    (
        "It does not matter if that number is arbitrary, low, or specifically designed to limit you.",
        f"{STYLE} Three anchors side by side: 'ARBITRARY,' 'LOW,' 'DESIGNED TO LIMIT.' All three equally heavy, all three labeled 'SAME EFFECT.' Brain in all three scenarios locked on the anchor.",
        "Wide, three-anchor comparison",
        "Neutral white",
        "The universality of anchoring",
        "Brain reacting identically to all three",
        "Three brains snap to anchors simultaneously",
    ),
    (
        "Your brain treats it as the starting truth.",
        f"{STYLE} JAKE's brain inside skull stamping '$36,000' with a 'TRUTH' stamp. The number now has an official seal on it. Label: 'STARTING TRUTH.' Padlock appears on the number.",
        "Close-up, skull interior",
        "Official stamp lighting",
        "Institutionalization of the anchor",
        "Brain stamps the number with authority",
        "TRUTH stamp slams down on number",
    ),
    (
        "And it recalculates everything — including your sense of victory — relative to it.",
        f"{STYLE} JAKE holding trophy labeled 'I NEGOTIATED +$3k.' Brain villain behind him quietly holds a larger trophy labeled 'I KEPT $13k.' Jake unaware. Both trophies relative to same starting band.",
        "Medium wide — Jake foreground, villain behind",
        "Jake in warm light, villain in shadow",
        "The engineered victory",
        "Jake proud with small trophy, villain amused with large one",
        "Villain trophy slowly revealed as Jake celebrates",
    ),
    # ── THE MULTIPLICATION ──
    (
        "Now meet Marcus. Same company, same role, same week.",
        f"{STYLE} MARCUS introduced: beige oval head, transparent skull with pink brain inside, short blonde/yellow hair, orange t-shirt, gray pants. Standing confidently. Label: 'MARCUS — SAME ROLE, SAME WEEK.'",
        "Medium, Marcus centered",
        "Neutral warm spotlight",
        "Introduction — new character",
        "Standing straight, confident default posture",
        "Marcus fades in from white",
    ),
    (
        "Before the interview, Marcus spent two hours on salary research. Market rate: $47,000 to $54,000.",
        f"{STYLE} MARCUS at laptop: Glassdoor and LinkedIn Salary pages visible on screen. Note on paper: 'MARKET RATE: $47k–$54k.' Brain inside skull actively engaged. Orange t-shirt visible.",
        "Medium wide, Marcus at laptop",
        "Warm desk lamp, research mode",
        "Preparation — but different preparation",
        "Marcus taking notes, brain lit with data",
        "Screen data reflects on Marcus's face",
    ),
    (
        "When the HR manager slid the paper across the desk showing $36,000, Marcus paused.",
        f"{STYLE} Same HR desk scene. Paper shows $36,000. MARCUS (orange t-shirt, blonde hair) looks at it. His brain inside skull does NOT glow green. Neutral pause. No reaction. '...' bubble above him.",
        "Medium two-shot, Marcus and HR",
        "Professional office light",
        "Calm non-reaction — the anchor doesn't land",
        "Marcus pauses, face neutral, brain unimpressed",
        "Pause held — no immediate reaction",
    ),
    (
        "'I've seen the market range for this role at $47,000 to $54,000. I was expecting something in that range.'",
        f"{STYLE} MARCUS speaking, calm and direct. Speech bubble: 'MARKET RANGE: $47k–$54k.' HR manager's expression shifts — slight surprise. MARCUS holds his own research paper visibly.",
        "Medium two-shot",
        "Marcus in confident light",
        "Controlled, data-backed confidence",
        "Marcus speaking clearly, HR listening",
        "Speech bubble with Marcus's counter appears",
    ),
    (
        "Silence.",
        f"{STYLE} Wide shot of the interview room. MARCUS and HR manager sitting across the desk. Complete stillness. '...' above HR manager. Clock on wall visible. Pure quiet tension.",
        "Wide, room visible",
        "Tense neutral light",
        "Power in silence",
        "Both completely still",
        "Clock hand ticks once",
    ),
    (
        "The HR manager left the room. Came back ten minutes later. $46,000.",
        f"{STYLE} Three-panel sequence: HR manager standing to leave → empty room with MARCUS waiting calmly → HR returning with new paper showing $46,000. Marcus's brain: still calm, processing.",
        "Triptych, three moments",
        "Consistent professional light",
        "The system responding to the refusal",
        "Marcus waits calmly, returns to find new offer",
        "Three panels slide in left to right",
    ),
    (
        "Marcus countered at $50,000. They settled at $48,000.",
        f"{STYLE} MARCUS speaking: '$50,000' in speech bubble. HR counter: '$48,000.' MARCUS extending hand for handshake. HR accepting. Brain inside Marcus's skull: calm green glow — satisfied but measured.",
        "Medium two-shot, handshake",
        "Warm professional light",
        "Measured victory — from a position of knowledge",
        "Handshake, Marcus calm, HR accepting",
        "Handshake held, calm green glow in Marcus's skull",
    ),
    (
        "Same company. Same role. Same week. Same starting point.",
        f"{STYLE} Side-by-side comparison: JAKE (navy) on left, MARCUS (orange) on right. Labels: 'SAME COMPANY / SAME ROLE / SAME WEEK.' Identical office backgrounds. Identical starting conditions.",
        "Wide split comparison",
        "Mirror lighting on both sides",
        "The identical starting conditions",
        "Both standing in identical poses",
        "Labels appear one by one between them",
    ),
    (
        "Jake: $39,000. Marcus: $48,000.",
        f"{STYLE} Same split frame. Below JAKE: '$39,000' in gray. Below MARCUS: '$48,000' in bold green. Both visible simultaneously. Simple, stark comparison.",
        "Wide split, salaries prominent",
        "Gray for Jake's number, green for Marcus's",
        "The simple consequence",
        "Both characters looking at their own salary labels",
        "Numbers appear simultaneously with impact",
    ),
    (
        "A difference of $9,000.",
        f"{STYLE} '$9,000' in large red bold text between JAKE and MARCUS. Arrow pointing from Jake's salary to Marcus's salary showing the gap. The anchor bolt visible between them as the cause.",
        "Wide, gap number prominent",
        "Red accent on gap number",
        "The gap crystallized",
        "Both characters looking at $9,000 between them",
        "$9,000 appears with a sharp stamp",
    ),
    (
        "Jake thought the gap was the negotiation. It was not.",
        f"{STYLE} JAKE with thought bubble: 'I NEGOTIATED WELL.' But the anchor bolt from earlier is visible between his $39k and Marcus's $48k. The anchor is highlighted with a red circle.",
        "Medium, Jake with thought bubble",
        "Slight irony in the warm light",
        "The misunderstanding",
        "Jake nodding, unaware of anchor's role",
        "Anchor bolt highlighted as real cause",
    ),
    (
        "The gap was the anchor.",
        f"{STYLE} Full frame: the anchor bolt between the two salary numbers. Red arrow from anchor to the $9,000 gap. Label: 'THE ANCHOR CREATED THE GAP.' Brain villain in corner nodding.",
        "Wide, anchor and gap prominent",
        "Red emphasis on the connection",
        "The mechanism revealed simply",
        "Brain villain nodding knowingly",
        "Arrow draws from anchor to gap",
    ),
    # ── THE COMPOUND GAP ──
    (
        "Here is what $9,000 becomes.",
        f"{STYLE} '$9,000' on left side of frame. Large transformation arrow pointing right. '?' on right side. JAKE and MARCUS in background, both looking at the arrow. Clean white background.",
        "Wide, transformation arrow",
        "Clean white, anticipation",
        "Setup for the number reveal",
        "Both characters looking at the question mark",
        "Arrow pulses slightly",
    ),
    (
        "Both receive three percent raises every year. The percentage is identical. The base is not.",
        f"{STYLE} Two thermometers side by side. JAKE's (navy): starts lower. MARCUS's (orange): starts higher. Same '+3%' label on both. But JAKE's thermometer rises less each year.",
        "Wide, two thermometers",
        "Neutral diagram white",
        "The mechanism of divergence",
        "Thermometers filling at same rate but from different bases",
        "Both thermometers fill simultaneously at same rate",
    ),
    (
        "Year five: Jake earns $45,200. Marcus earns $55,600.",
        f"{STYLE} Split comparison at 'YEAR 5' label. JAKE (navy) with payslip '$45,200.' MARCUS (orange) with payslip '$55,600.' Gap label between them: '$10,400.' Gap has grown from $9k.",
        "Wide split, year 5",
        "Year 5 label prominent",
        "Gap growing",
        "Both holding payslips, Marcus's clearly larger",
        "Gap label grows slightly from initial $9k",
    ),
    (
        "Year ten: Jake earns $52,400. Marcus earns $64,500.",
        f"{STYLE} Same split at 'YEAR 10.' JAKE: '$52,400.' MARCUS: '$64,500.' Gap: '$12,100.' Both characters slightly older. Gap visibly wider than year 5.",
        "Wide split, year 10",
        "Same comparative lighting",
        "Divergence accelerating",
        "Gap between them physically wider in frame",
        "Gap arrow widens from year 5 position",
    ),
    (
        "Year twenty: Jake earns $70,400. Marcus earns $86,600.",
        f"{STYLE} Same split at 'YEAR 20.' JAKE: '$70,400.' MARCUS: '$86,600.' Gap: '$16,200.' Both noticeably older. Gap now prominent — a clear chasm between them.",
        "Wide split, year 20",
        "Older characters, same visual language",
        "The chasm made visible",
        "Both holding payslips, chasm between them obvious",
        "Chasm between characters animated wider",
    ),
    (
        "The gap does not stay at $9,000. It grows every year because raises are percentages.",
        f"{STYLE} Line graph: two diverging lines from same starting date. JAKE's line (navy) below, MARCUS's line (orange) above. Gap between lines widens year by year. Label: 'RAISES ARE PERCENTAGES.'",
        "Wide line graph, white background",
        "Navy and orange lines diverge clearly",
        "The mathematical compounding visualized",
        "Brain villain traces the widening gap with satisfaction",
        "Lines diverge in continuous animation",
    ),
    (
        "A three percent raise on $39,000 is $1,170. A three percent raise on $48,000 is $1,440.",
        f"{STYLE} Two raise calculations side by side. Left (JAKE, navy): '$39,000 × 3% = $1,170.' Right (MARCUS, orange): '$48,000 × 3% = $1,440.' Difference: '$270/year.' Bold labels.",
        "Wide two-column calculation",
        "Clean white, numbers prominent",
        "The per-year mechanism exposed",
        "Both characters receiving their respective raise amounts",
        "Calculation completes with totals bolded",
    ),
    (
        "The person who earns more always earns more from every raise.",
        f"{STYLE} Staircase diagram: MARCUS's staircase (orange) higher at every step. JAKE's staircase (navy) climbing same number of steps but from lower start. Each step labeled '+3%.' Gap constant between stairs.",
        "Wide staircase diagram",
        "Orange above navy, consistent gap",
        "The structural advantage of the higher base",
        "Both characters climbing their respective staircases",
        "Staircases climb in parallel, gap maintained",
    ),
    (
        "Add pension contributions — both putting in five percent of salary — and the pension gap at year thirty exceeds $80,000.",
        f"{STYLE} Two pension pots growing side by side. JAKE's (navy label): shorter. MARCUS's (orange label): taller. Label: '30 YEARS — PENSION GAP: $80,000+.' Same 5% contribution rate on both.",
        "Wide, two pension pots",
        "Warm savings light on both pots",
        "The compounding extends to retirement savings",
        "Both pouring same percentage into different-sized pots",
        "Pots fill at same rate but to different heights",
    ),
    (
        "Total lifetime earnings difference: over $300,000.",
        f"{STYLE} '$300,000+' in massive bold red text center frame. Below it: a small '$9,000' in gray with an arrow to the large number. JAKE and MARCUS flanking it — same shocked expressions.",
        "Wide, number dominates frame",
        "Red accent on $300,000",
        "The full cost of the anchor",
        "Both characters staring at the number",
        "$300,000 appears with maximum impact",
    ),
    (
        "For a single conversation Jake did not know he was allowed to have.",
        f"{STYLE} JAKE in interview room, same scene as before. Speech bubble above him: empty '...' — the conversation he didn't have. MARCUS in parallel frame: speech bubble full of text — the one he did.",
        "Split — two interview rooms",
        "Jake's side dim, Marcus's side bright",
        "The silence that cost $300,000",
        "Jake silent, Marcus speaking",
        "Marcus's speech bubble fills while Jake's stays empty",
    ),
    # ── THE INDUSTRY ──
    (
        "HR departments do not guess at salary numbers.",
        f"{STYLE} HR office interior: filing cabinets, salary documents, spreadsheets. A large board on the wall shows ROLE SALARY BANDS in a structured table. Organized, deliberate, systematic.",
        "Wide, HR office",
        "Professional institutional light",
        "The systematic nature of anchoring",
        "HR manager reviewing band document with purpose",
        "Camera slowly pans across organized HR materials",
    ),
    (
        "Every role has a band. A floor and a ceiling, set before the interview begins.",
        f"{STYLE} Salary band diagram: horizontal bar with FLOOR at left and CEILING at right. Label: 'SET BEFORE ANY INTERVIEW.' Brain villain in HR manager role pointing at the bar confidently.",
        "Wide, band diagram",
        "Neutral institutional light",
        "The pre-existing structure",
        "Brain villain points at band with authority",
        "Band appears before any interview character arrives",
    ),
    (
        "The number they show you first is rarely the midpoint of that band.",
        f"{STYLE} Same band bar. Midpoint marked with dotted line. The number actually shown to candidates: a red dot significantly below midpoint, labeled 'WHAT THEY SHOW YOU.' Gap between dot and midpoint highlighted.",
        "Wide, band with midpoint marked",
        "Red dot below midpoint highlighted",
        "The strategic low-anchoring",
        "Brain villain places red dot deliberately below midpoint",
        "Red dot placed below midpoint with a strategic click",
    ),
    (
        "It is calibrated to anchor low — close enough to what they know you currently earn, high enough that it feels like an upgrade.",
        f"{STYLE} Calibration dial in HR office. Brain villain turns it: left = 'TOO LOW (rejected),' right = 'TOO HIGH (leaves money),' center-left = 'SWEET SPOT — feels like upgrade.' Brain villain sets it to sweet spot.",
        "Wide, calibration dial prominent",
        "Technical precision light",
        "The engineered sweet spot",
        "Brain villain turns dial to sweet spot precisely",
        "Dial turns to sweet spot with a click",
    ),
    (
        "The question 'what are you currently earning?' is not curiosity. It is data collection.",
        f"{STYLE} HR manager asking JAKE: 'WHAT ARE YOU CURRENTLY EARNING?' Arrow from Jake's answer → brain villain's notepad labeled 'DATA.' Label on the question: 'NOT CURIOSITY — DATA COLLECTION.'",
        "Wide, interview room with data flow visible",
        "Slightly cold, analytical",
        "The extraction of anchoring data",
        "HR manager writing down Jake's answer immediately",
        "Data flow arrow animates from Jake to notepad",
    ),
    (
        "It tells them exactly where to place the anchor.",
        f"{STYLE} Formula on whiteboard: 'CANDIDATE EARNS X → SHOW THEM X + 10-15% → ANCHOR SET.' Brain villain writes formula on board. Label: 'THE ANCHOR FORMULA.'",
        "Wide, whiteboard formula",
        "Cold clinical white",
        "The algorithm of anchoring",
        "Brain villain completes formula, underlines it",
        "Formula writes itself line by line",
    ),
    (
        "If you earn $31,000, they show you $36,000. You feel the sixteen percent gain. You stop thinking about the ceiling.",
        f"{STYLE} JAKE entering interview: '$31,000' visible above him (current salary). Paper slid: '$36,000.' Jake's brain: green +16% glow. Above the frame, ceiling of band ($55,000) faded and invisible to Jake.",
        "Wide, Jake with current salary and offer visible",
        "Ceiling deliberately faded/invisible",
        "The ceiling made invisible by the anchor",
        "Jake focused on +16%, blind to ceiling",
        "Ceiling fades from Jake's view as he focuses on offer",
    ),
    (
        "If you earned $45,000, they would have shown you $48,000. Same mechanism. Different number.",
        f"{STYLE} Alternate JAKE with '$45,000' above him. Different paper slid: '$48,000.' Same green glow in brain for +$3k. Label: 'SAME MECHANISM.' Band still $40k-$55k — still above what was offered.",
        "Wide, alternate scenario",
        "Same lighting pattern as prev beat",
        "The universality of the mechanism",
        "Jake's brain reacts identically in both scenarios",
        "Scenario swap with same visual pattern",
    ),
    (
        "The band never changes. Only the anchor does.",
        f"{STYLE} Band bar stays fixed on screen. Two different anchor red dots appear on it — one for each scenario from prev beats — at different positions but both below midpoint. Label: 'BAND FIXED. ANCHOR VARIABLE.'",
        "Wide, band with two anchor positions",
        "Fixed band, variable anchor highlighted",
        "The mechanism's flexibility",
        "Band stays fixed, anchors move",
        "Two anchor dots appear at different positions",
    ),
    (
        "In several US states and many countries, asking for your current salary in a job interview is now illegal.",
        f"{STYLE} Map of USA with states colored green (salary history ban). Additional world map inset showing countries with similar laws. Label: 'SALARY HISTORY BANS — EXPANDING.'",
        "Wide, map with green states",
        "Legal/governmental neutral light",
        "The legal response to anchoring",
        "Map fills with green states one by one",
        "Green states appear progressively",
    ),
    (
        "Not because it is rude. Because legislators understood what it was being used for.",
        f"{STYLE} Legislature/government building. Inside: legislators reading the anchoring mechanism diagram. Label on diagram: 'THIS IS WHY.' Brain villain outside the building, looking in, concerned.",
        "Wide, government building",
        "Authoritative governmental light",
        "The legal recognition of the harm",
        "Legislators pointing at anchoring diagram",
        "Brain villain outside looks concerned for first time",
    ),
    (
        "The industry fought those laws.",
        f"{STYLE} Brain villain in suit at press conference/podium, microphones in front of him. Behind him: company logos. He holds a sign: 'PROTECT SALARY HISTORY QUESTIONS.' Crowd of corporate figures behind him.",
        "Wide, press conference setting",
        "Press conference lighting",
        "Corporate self-interest exposed",
        "Brain villain at podium, gesturing defensively",
        "Microphones close in as villain speaks",
    ),
    # ── THE POPULAR MISREADING ──
    (
        "Everyone who understands this arrives at the same conclusion.",
        f"{STYLE} Row of generic characters — all with thought bubbles showing the same lightbulb icon. Label: 'UNIVERSAL REACTION.' Clean white background.",
        "Wide, row of characters",
        "Neutral white",
        "Universal but wrong intuition",
        "All characters nodding simultaneously",
        "Thought bubbles pop in identically",
    ),
    (
        "The solution is to negotiate harder.",
        f"{STYLE} Same characters now holding 'NEGOTIATE HARDER' dumbbells. Determined expressions. Label: 'THE OBVIOUS ANSWER.' Bold typography.",
        "Wide, characters with dumbbells",
        "Motivational bright light",
        "The intuitive but incomplete answer",
        "Characters flexing negotiation dumbbells",
        "Dumbbells appear with a clang",
    ),
    (
        "That is the wrong answer.",
        f"{STYLE} Large red X stamps over the 'NEGOTIATE HARDER' dumbbells. Characters deflate slightly. Brain villain in corner shaking head — not gloating, just knowing.",
        "Wide, X over prev scene",
        "Red X dominates",
        "Deflation of the obvious answer",
        "Characters droop, villain shakes head knowingly",
        "Red X slams down with impact",
    ),
    (
        "Negotiating harder moves you up within the anchor's range.",
        f"{STYLE} JAKE inside a box labeled 'ANCHOR'S RANGE: $36k–$42k.' He negotiates hard, pushes to the TOP of the box. But he is still inside the box. Can't get out.",
        "Medium, Jake inside box",
        "Boxed-in lighting",
        "The ceiling within the anchor's frame",
        "Jake pushing against the top of the box",
        "Jake reaches top of box but can't exit",
    ),
    (
        "It does not escape the anchor.",
        f"{STYLE} Same box. Jake at the very top — $42,000 (his max negotiated). The band's floor is ABOVE the box — $40,000 label ABOVE Jake's ceiling. He fought hard to reach the band's floor.",
        "Wide, box with band above it",
        "The gap between box ceiling and band floor highlighted",
        "The impossibility of escaping the anchor by negotiating harder",
        "Jake exhausted at top of box, band floor still above",
        "Band floor label appears above the box ceiling",
    ),
    (
        "Jake negotiated. He went from $36,000 to $39,000.",
        f"{STYLE} JAKE's negotiation shown: $36k → $39k with green arrow. Label: 'HE NEGOTIATED WELL.' But the box is still drawn around the range $36k–$39k, clearly inside the full band.",
        "Medium, Jake with negotiation range",
        "Warm acknowledgment light",
        "Credit given — but contextualised",
        "Jake proud of negotiation",
        "Box clearly visible around the entire negotiation",
    ),
    (
        "He negotiated well. He just negotiated inside a frame he had already accepted.",
        f"{STYLE} JAKE holding his '$39,000' result trophy, standing inside a glass frame labeled 'THEIR FRAME.' He can see the full band outside the glass — but accepted the frame before negotiating.",
        "Medium, Jake inside glass frame",
        "Inside frame warm, outside frame shows real range",
        "The trap of accepted frames",
        "Jake proud inside frame, unaware of outside",
        "Camera slowly pulls back to reveal full band outside frame",
    ),
    (
        "The anchor is not set during the negotiation. It is set before it.",
        f"{STYLE} Timeline: 'BEFORE INTERVIEW' — brain villain places anchor. 'INTERVIEW BEGINS' — negotiation starts (anchor already embedded). 'NEGOTIATION' — all happens within anchor's gravity.",
        "Wide timeline diagram",
        "Timeline flows left to right",
        "The timing is the key insight",
        "Brain villain places anchor before the negotiation clock starts",
        "Timeline arrow moves left to right, anchor pre-placed",
    ),
    # ── THE REAL CONCLUSION ──
    (
        "The first number is not the offer.",
        f"{STYLE} Large paper on desk labeled '$36,000.' Red text stamp over it: 'NOT AN OFFER.' Below: 'IT IS A FRAME.' Clean white background. The reframe is total.",
        "Wide, paper with stamp",
        "Red stamp prominent",
        "The central reframe",
        "Stamp slams down on offer paper",
        "NOT AN OFFER stamp appears with impact",
    ),
    (
        "It is the frame inside which the offer will happen.",
        f"{STYLE} The '$36,000' paper morphs into a picture frame. Inside the frame: the entire negotiation space ($36k–$39k range). Outside the frame: the full band ($40k–$55k) invisible to the negotiator.",
        "Wide, frame metaphor",
        "Frame lit, outside dark",
        "The frame as the real mechanism",
        "Brain villain holds up the frame like a painter",
        "Paper transforms into frame",
    ),
    (
        "Everything you negotiate after that — every counter, every pushback, every silence — is evaluated by your brain relative to a number that was chosen specifically to limit you.",
        f"{STYLE} JAKE inside the frame. Every negotiation move shown as small arrows inside the frame — up, down, counter, pushback. All contained. The number '$36,000' anchored at bottom of frame.",
        "Wide, Jake inside frame with arrows",
        "Contained light inside frame",
        "The totality of the trap",
        "Jake making moves — all inside the frame",
        "Arrows animate within the frame boundaries",
    ),
    (
        "Marcus did not negotiate better than Jake.",
        f"{STYLE} MARCUS (orange, blonde) standing outside any frame. No box around him. Clean open space. Label: 'HE DID NOT NEGOTIATE BETTER.' His brain inside skull: calm and open.",
        "Medium, Marcus in open space",
        "Open, uncontained light",
        "The real distinction is not negotiation skill",
        "Marcus standing freely, no frame",
        "Open space emphasised around Marcus",
    ),
    (
        "Marcus refused the frame.",
        f"{STYLE} MARCUS holding up the '$36,000' frame — and setting it aside on the floor. He stands in the open band space. Label: 'HE REFUSED THE FRAME.' Simple, powerful.",
        "Medium, Marcus setting frame aside",
        "Liberating open light",
        "The only move that changes everything",
        "Marcus places frame on floor deliberately",
        "Frame placed down, Marcus steps away from it",
    ),
    (
        "He walked in with his own number, placed it on the table before their anchor could land, and made their first move irrelevant.",
        f"{STYLE} MARCUS entering interview room. Before HR manager can place paper, Marcus places his own research document: '$47k–$54k MARKET RANGE.' HR's '$36,000' paper still in their hands — unplaced.",
        "Wide, interview room",
        "Marcus's document in spotlight, HR's paper in shadow",
        "The pre-emptive anchor",
        "Marcus placing document before HR moves",
        "Marcus's document lands first — HR's stays in hand",
    ),
    (
        "That is the only negotiation that actually changes the outcome.",
        f"{STYLE} Two outcomes side by side: JAKE's path (into frame, negotiates within it, $39k). MARCUS's path (refuses frame, places own anchor, $48k). Label: 'OUTCOME CHANGED HERE' with arrow at the refusal moment.",
        "Wide, two path comparison",
        "Decision point highlighted",
        "The lever that changes everything",
        "Arrow at refusal moment as the critical fork",
        "Fork in path highlighted at anchor refusal",
    ),
    (
        "Not pushing back harder on their number.",
        f"{STYLE} JAKE pushing against the anchor number with all his strength — moving it slightly. Label: 'PUSHING BACK HARDER' with red X. The anchor barely moves despite the effort.",
        "Medium, Jake pushing anchor",
        "Strain lighting, effort visible",
        "The insufficient response",
        "Jake straining against anchor, minimal movement",
        "Red X appears over the struggling effort",
    ),
    (
        "Replacing it with yours before they get to speak first.",
        f"{STYLE} MARCUS placing his own anchor bolt into the ground — labeled with his market research number — before HR even opens their folder. Clean decisive action. Green checkmark above.",
        "Medium, Marcus placing own anchor",
        "Purposeful decisive light",
        "The actual solution",
        "Marcus plants anchor decisively",
        "Green checkmark appears above with a clean pop",
    ),
    # ── EL MOVIMIENTO ──
    (
        "Here is what you do with this.",
        f"{STYLE} JAKE and MARCUS both standing side by side, sleeves rolled up, ready. Five action icons below them. White background. Label: 'EL MOVIMIENTO.' Both brains inside skulls visibly engaged.",
        "Wide, both characters centered",
        "Bright purposeful white",
        "Agency — both characters united in action",
        "Both rolling sleeves, ready posture",
        "Action icons slide in below both characters",
    ),
    (
        "Never give a number first. When asked your expectations, name a number before they do — research the market rate and anchor above the midpoint.",
        f"{STYLE} Interview scene: HR about to speak — JAKE holds up hand. Jake places his own research paper first. Label: 'YOU SPEAK FIRST.' Market rate document visible with number above midpoint circled.",
        "Medium, interview room",
        "Confident proactive light",
        "The first and most important move",
        "Jake holds up hand, places own paper first",
        "Jake's paper lands before HR's",
    ),
    (
        "If they ask your current salary, you do not have to answer. In many places they cannot legally ask. Say: 'I prefer to focus on the market rate for this role.'",
        f"{STYLE} HR asking question with label 'WHAT DO YOU EARN?' JAKE holds up a sign: 'I PREFER TO FOCUS ON MARKET RATE.' Legal shield icon beside Jake. Deflection without confrontation.",
        "Medium, interview room",
        "Neutral balanced light",
        "The legal and tactical deflection",
        "Jake calm, holding deflection sign",
        "Legal shield icon appears beside Jake",
    ),
    (
        "Before every interview, spend one hour on salary research. Glassdoor, LinkedIn Salary, industry reports. That number — not theirs — is your anchor.",
        f"{STYLE} JAKE at laptop: Glassdoor, LinkedIn Salary tabs open. Timer showing '1 HOUR.' Research notes filling up. Label: 'YOUR ANCHOR — NOT THEIRS.' Brain inside skull filling with data.",
        "Wide, research scene",
        "Focused warm desk light",
        "The preparation that changes outcomes",
        "Jake taking notes efficiently, brain filling with data",
        "Research tabs populate quickly",
    ),
    (
        "When they show you a number, pause five seconds before responding. That pause is not awkward. It is the moment your brain resets from their anchor to yours.",
        f"{STYLE} JAKE in interview, paper just received. '5... 4... 3... 2... 1...' countdown visible. Jake's brain inside skull: red (their anchor) fading, green (his anchor) returning. HR watching, slightly uncertain.",
        "Medium, Jake with countdown",
        "Pause lighting — suspended moment",
        "The reset window",
        "Jake pausing deliberately, brain transitioning",
        "Countdown numbers tick down, brain color shifts",
    ),
    (
        "Renegotiate internally every eighteen months. Salary compression is real — your newest colleague may be earning more than you for identical work.",
        f"{STYLE} Calendar showing '18 MONTHS.' JAKE at manager's desk for renegotiation. Beside him: comparison of his salary vs new hire salary for same role. Label: 'SALARY COMPRESSION.' Slight shock.",
        "Wide, calendar and renegotiation scene",
        "Purposeful proactive light",
        "The ongoing maintenance of fair compensation",
        "Jake at manager's desk, calendar and comparison visible",
        "Calendar and salary comparison appear side by side",
    ),
    # ── THE ENDING ──
    (
        "Jake is fifty-two years old.",
        f"{STYLE} JAKE at 52 (label 'AGE 52'). Same transparent skull, same black hair (slightly grayer at temples), same navy t-shirt. Senior office. Awards on shelf. Comfortable.",
        "Medium, Jake at senior desk",
        "Warm established professional light",
        "Accomplishment, seniority",
        "Sitting at desk, relaxed senior posture",
        "Slow zoom out reveals full senior office",
    ),
    (
        "He has been promoted. He is good at his job. His colleagues respect him.",
        f"{STYLE} JAKE's office wall: promotion certificates, 'EMPLOYEE OF THE YEAR' plaques, team photos. Colleagues in background smiling at him. Genuine respect visible.",
        "Wide, office wall and colleagues",
        "Warm appreciation light",
        "Earned success — the tragedy is not failure",
        "Colleagues waving at Jake, he waves back",
        "Camera pans across achievements on wall",
    ),
    (
        "He earns $70,000.",
        f"{STYLE} JAKE's payslip visible: '$70,000.' He looks at it with satisfaction. It is a good salary. He has no reason to think anything is wrong.",
        "Close-up, payslip",
        "Warm satisfaction light",
        "Earned but incomplete satisfaction",
        "Jake nodding at payslip, content",
        "Camera holds on $70,000 number",
    ),
    (
        "His colleague who joined the same week, in the same role, earns $86,000.",
        f"{STYLE} MARCUS (blonde, orange t-shirt, 52 years old) in adjacent office. His payslip visible: '$86,000.' Same company floor. Same job title on door. $16,000 gap label between the two offices.",
        "Wide split — both offices side by side",
        "Same light for both offices — equal seniority",
        "The parallel life made visible",
        "Marcus at his desk, payslip prominent",
        "Gap label appears between the two offices",
    ),
    (
        "Jake has never known this.",
        f"{STYLE} JAKE in his office. No awareness of Marcus's salary. Brain inside transparent skull: calm, content, unaware. Label: 'HE HAS NEVER KNOWN.' The gap floats between the offices, invisible to Jake.",
        "Medium, Jake in office",
        "Normal warm light — no alarm",
        "The quiet, invisible injustice",
        "Jake working normally, gap invisible to him",
        "Gap label visible to viewer but not to Jake",
    ),
    (
        "He did not lose at fifty-two.",
        f"{STYLE} JAKE at 52 looking fine. 'HE DID NOT LOSE AT 52' label appears. Time rewind arrow visible. Jake's expression: unchanged, unaware of what is about to be revealed.",
        "Medium, Jake with label",
        "Neutral transition light",
        "Reframe — the loss happened elsewhere",
        "Jake unaware as label appears",
        "Time rewind arrow materializes",
    ),
    (
        "He lost at twenty-four, in a room he thought he had won, against a number he thought was the starting point.",
        f"{STYLE} Time rewind: Jake at 24 in interview room. Paper sliding across desk. '$36,000.' The whole scene replays. 'HE LOST HERE' label over the paper. Brain villain visible in the corner — he was always there.",
        "Wide, interview room — 28 years earlier",
        "Same room, younger Jake",
        "The origin of the loss",
        "Young Jake reaching for paper, villain watching",
        "Time rewind animation to interview room",
    ),
    (
        "The first number they show you is not an offer.",
        f"{STYLE} Close-up of the paper: '$36,000.' Bold text below it stamped: 'NOT AN OFFER.' The brain villain's hand is the one that wrote the number. His hand visible at the edge of the paper.",
        "Close-up, paper and villain's hand",
        "Reveal lighting — cold clarity",
        "The central truth of the video",
        "Villain's hand visible as author of the anchor",
        "NOT AN OFFER stamp appears with final impact",
    ),
    (
        "It is a decision about how much of the value you create they intend to keep.",
        f"{STYLE} Value flow diagram: JAKE creates $100k of value. Company keeps $61k. Jake receives $39k. Same diagram for MARCUS: creates same value. Company keeps $52k. Marcus receives $48k. Brain villain owns the company.",
        "Wide, value flow diagram",
        "Clear clinical light on value flows",
        "The economic truth behind the mechanism",
        "Brain villain at top of diagram receiving the larger share",
        "Value flows animate from workers to company",
    ),
    (
        "Every video on this channel is one way your financial gut has been engineered against you.",
        f"{STYLE} Video thumbnail grid (generic rectangular placeholders, 9 thumbnails). Each pulses briefly. JAKE and MARCUS both standing in front of the grid. Label: 'YOUR FINANCIAL GUT — ENGINEERED.'",
        "Wide, thumbnail grid and both characters",
        "Each thumbnail pulses with brief glow",
        "Channel series call-back — both characters united",
        "Both characters gesture at the grid",
        "Thumbnails light up one by one",
    ),
    (
        "This is how they turned your anchor into their margin.",
        f"{STYLE} Final frame: brain villain facing viewer directly, holding a large stack of money. Behind him: JAKE (navy) and MARCUS (orange) — Jake with $70k label, Marcus with $86k label. Villain smirks at viewer. Direct eye contact.",
        "Medium — villain direct address to camera",
        "Villain in dramatic spotlight, both characters behind",
        "Final fourth-wall break — memorable close",
        "Brain villain holds money up, smirks directly at viewer",
        "Slow zoom in on villain's smug face",
    ),
]

SECTION_STARTS = {
    1:   "HOOK",
    9:   "THE INTERVIEW",
    19:  "THE MECHANISM",
    32:  "THE MULTIPLICATION",
    44:  "THE COMPOUND GAP",
    55:  "THE INDUSTRY",
    67:  "THE POPULAR MISREADING",
    75:  "THE REAL CONCLUSION",
    84:  "EL MOVIMIENTO",
    90:  "THE ENDING",
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
    r = title_p.add_run("CRAYON CAPITAL — CLONE SESSION · VIDEO 9")
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
    r = t_p.add_run("The First Number They Show You in a Job Interview Is Not an Offer")
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

    path = "/home/user/Claudeeee/Anchor_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
