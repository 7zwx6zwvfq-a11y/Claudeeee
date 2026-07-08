#!/usr/bin/env python3
"""
VIDEO 16 — IMAGE PROMPTS · FORMATO CATÁLOGO
81 beats · SIN ALEX · Brain Villain SOLO en 7 beats (25, 32, 46, 54, 61, 67, 76) con posición/tamaño variados — el resto sin personajes
Cada sesgo tiene un BADGE circular de color con icono-objeto negro (eco del thumbnail grid).
Beat 1 = badge de Anchoring llenando pantalla → S17 continuity con el thumbnail grid.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

TITLE    = "Every Money Bias & Its Effect Explained in 8 Minutes"
SUBTITLE = "NEUROCENTS · VIDEO 16"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines on every element, clean solid color "
    "fills, no gradients. THIS VIDEO HAS NO ALEX — do not draw the recurring main character. "
    "THE BRAIN VILLAIN appears ISOLATED (no human body, no skull) ONLY in the handful of beats "
    "where the prompt explicitly names him — pink cartoon brain (#E8A598), heavy-lidded eyes, "
    "slight smirk, small teeth, tiny arms. When he appears, VARY his position and size "
    "(center / left / right / background, large / small) — never the same corner twice. "
    "MOST BEATS HAVE NO CHARACTERS AT ALL: badges, objects and diagrams carry the frame alone. "
    "Generic humans when a scene needs people: simple flat silhouette-style figures with minimal "
    "features, varied builds — never Alex. "
    "BIAS BADGES: each bias has a colored circle badge with a black flat object-icon inside "
    "(echoing the thumbnail grid): Anchoring teal #2C93A8 crossed-out price tag · Loss Aversion "
    "red #C0392B cracked coin · Mental Accounting purple #7B5FA6 three envelopes · Present Bias "
    "orange #E8892C melting hourglass · Herd pink #D9527A three sheep · Lifestyle Inflation gold "
    "#E8C13C rising balloon with € · Sunk Cost brown #8B5A2B sinking ship · Optimism sky #58A6D6 "
    "sun over calendar · Default gray #8A8A8A recycling loop · Scarcity dark navy #4A4A6A closing "
    "tunnel. Palette: pink brain #E8A598 · green savings · red loss · white/clean backgrounds. "
    "16:9, 1280x720."
)

# (beat_num, section, narration, image_prompt)
BEATS = [

    # ═══ BIAS 1 — ANCHORING (teal badge) ═══
    (1, "BIAS 1 — ANCHORING",
     "Anchoring. Anchoring is your brain's habit of trusting the first number it sees.",
     "S17 OPENING [THUMBNAIL CONTINUITY]: The teal ANCHORING badge (crossed-out price tag icon) fills "
     "the frame, exactly as seen in the thumbnail grid — alone, huge, with one slow confident pulse. "
     "Clean white background. NO characters: the badge IS the opening."),
    (2, "BIAS 1 — ANCHORING",
     "It's everywhere. Price tags, salaries, menus. The most consumed bias on Earth.",
     "Rapid montage grid: a price tag, a salary offer letter, a restaurant menu — each with a glowing "
     "first number highlighted. Small teal badges hover over each like certification stamps."),
    (3, "BIAS 1 — ANCHORING",
     "You see a jacket: two hundred euros, crossed out. Now ninety.",
     "Close-up of a jacket on a rack. Price tag dominant: €200 crossed out in red, €90 below in bold. "
     "The tag is the protagonist — shot like a jewel. No people."),
    (4, "BIAS 1 — ANCHORING",
     "The onset is instant. Ninety stops being a price — it becomes a bargain.",
     "The €90 on the tag morphs visually: sprouting a golden 'bargain' glow, tiny sparkles. "
     "ONSET meter appearing at frame edge (small syringe-style gauge filling, teal). No characters."),
    (5, "BIAS 1 — ANCHORING",
     "Your brain never asked if the jacket was worth ninety. It only compared it to two hundred.",
     "Diagram: brain icon with two input arrows — a big €200 arrow feeding it, and a tiny unused "
     "question mark arrow ('worth it?') lying disconnected on the floor. White diagram background."),
    (6, "BIAS 1 — ANCHORING",
     "At the peak, the crossed-out number does all your thinking. The real question — 'do I even want this?' — never loads.",
     "PEAK: a loading bar labeled with a question-mark icon frozen at 10%, glitching. Above it, the "
     "crossed-out €200 pulses at full brightness. The comparison runs; the question never renders."),
    (7, "BIAS 1 — ANCHORING",
     "The comedown arrives at home: a ninety-euro jacket you never planned to buy.",
     "COMEDOWN: the jacket hanging in a dark closet, tag still on, faint teal glow fading. "
     "A silhouette figure looks at it from the doorway, deflated posture. Moody dim light."),
    (8, "BIAS 1 — ANCHORING",
     "Repeated daily, anchoring quietly decides what 'normal' costs — rent, phones, haircuts, everything.",
     "Wide shot: a city street where every price sign (rent ad, phone shop, barber) has a small "
     "teal anchor icon stamped on it. The bias owns the landscape. No main characters."),
    (9, "BIAS 1 — ANCHORING",
     "You never buy the thing. You buy the distance from the first number.",
     "LAPIDARIA FRAME: minimal composition — two numbers on white (€200 faded, €90 bold) with a "
     "measuring-tape arc drawn between them — the arc alone bridges the two numbers. "
     "Maximum white space. No characters."),

    # ═══ BIAS 2 — LOSS AVERSION (red badge) ═══
    (10, "BIAS 2 — LOSS AVERSION",
     "Loss Aversion. The oldest bias in the building.",
     "The red LOSS AVERSION badge (cracked coin icon) fills frame on a stone-texture backdrop, "
     "resting on a small carved pedestal like a museum relic — this one is ancient. No characters."),
    (11, "BIAS 2 — LOSS AVERSION",
     "Losing a hundred euros hurts about twice as much as winning a hundred feels good. That asymmetry runs your life.",
     "Balance scale diagram: left pan holds one €100 note pointing down HARD (heavy, red glow); right "
     "pan holds an identical €100 note floating light (soft green glow). Same note, double weight."),
    (12, "BIAS 2 — LOSS AVERSION",
     "The onset: you check a price, an account, an investment — and your chest tightens before your thoughts arrive.",
     "ONSET: a silhouette figure looking at a phone; inside their chest area, a fist-clench icon "
     "squeezes. A tiny red gauge fills at frame edge. The thought bubble above is still empty — "
     "the body reacted first."),
    (13, "BIAS 2 — LOSS AVERSION",
     "At the peak, you'll do irrational things to avoid a small loss — hold a bad investment, keep a broken subscription, stay in the wrong plan.",
     "PEAK triptych: hands gripping a falling stock chart · hands hugging a broken subscription box "
     "(cracked, sparking) · hands clinging to a contract on fire. Three grips, zero logic. No faces needed."),
    (14, "BIAS 2 — LOSS AVERSION",
     "Not to win. Just to not lose.",
     "Minimal frame: a trophy icon crossed out in gray; beside it, a shield icon glowing red, "
     "standing alone. White background, huge negative space. No characters."),
    (15, "BIAS 2 — LOSS AVERSION",
     "The comedown is invisible: all the better options you never took because they smelled like risk.",
     "COMEDOWN: a corridor of faded, translucent doors labeled with icons (growth chart, new job "
     "briefcase, plane) — all untouched, cobwebbed. The only opened door behind leads back to a "
     "gray room. Ghost-light palette."),
    (16, "BIAS 2 — LOSS AVERSION",
     "Long-term damage: a life optimized against losing is a life that never compounds.",
     "Two life-lines on a graph: a flat safe gray line hugging the floor, and a dotted green "
     "compounding curve rising away from it — marked as 'never taken' by a faded ghost texture."),
    (17, "BIAS 2 — LOSS AVERSION",
     "Your brain doesn't protect your money. It protects the feeling of not losing it.",
     "LAPIDARIA FRAME: a glass jar labeled with a heart icon — inside the jar is NOT money, just a "
     "soft glowing cushion. Actual coins lie ignored outside the jar. White bg. No characters."),

    # ═══ BIAS 3 — MENTAL ACCOUNTING (purple badge) ═══
    (18, "BIAS 3 — MENTAL ACCOUNTING",
     "Mental Accounting. Your brain runs separate wallets for the same money.",
     "The purple MENTAL ACCOUNTING badge (three envelopes icon) fills frame; below it, three real "
     "envelopes lie fanned on a table like a dealt hand — nobody holding them. Clean white background."),
    (19, "BIAS 3 — MENTAL ACCOUNTING",
     "Salary money is serious. Refund money is free. Birthday money is fun.",
     "Three envelopes personified: a gray envelope with a tie (serious) · a bouncing green envelope "
     "with party streamers (free!) · a pink envelope with a birthday hat. Identical € bills peek "
     "from all three."),
    (20, "BIAS 3 — MENTAL ACCOUNTING",
     "The onset: a hundred euros arrives outside your salary — and it lands in the 'doesn't count' wallet.",
     "ONSET: a €100 note parachuting down, drifting on drawn wind-lines away from a sturdy safe "
     "and into a flimsy paper bag labeled with a shrug icon. Purple gauge at frame edge. No characters."),
    (21, "BIAS 3 — MENTAL ACCOUNTING",
     "At the peak, you'll spend a tax refund in a weekend while agonizing over a forty-euro grocery bill.",
     "PEAK split: left — confetti and shopping bags devouring a refund letter in fast-forward blur; "
     "right — a silhouette sweating over a €40 supermarket receipt with a magnifying glass. Same wallet, "
     "two universes."),
    (22, "BIAS 3 — MENTAL ACCOUNTING",
     "Same currency. Same account. Different rules.",
     "Minimal: two identical €50 notes side by side on white; one behind velvet museum ropes, one "
     "inside a hamster wheel spinning. No text."),
    (23, "BIAS 3 — MENTAL ACCOUNTING",
     "The comedown: at the end of the year, the 'free money' is gone and you can't name a single thing it built.",
     "COMEDOWN: December calendar page; beside it an open, empty paper bag (the 'doesn't count' wallet) "
     "turned inside out, a single moth flying out. Cold winter light."),
    (24, "BIAS 3 — MENTAL ACCOUNTING",
     "Money doesn't come with labels. Your brain prints them.",
     "LAPIDARIA FRAME: a tiny label-printer machine with a mechanical arm sticking labels "
     "(party icon, shrug icon, tie icon) onto identical passing € notes on a conveyor belt — "
     "running entirely by itself. No characters."),

    # ═══ BIAS 4 — PRESENT BIAS (orange badge) ═══
    (25, "BIAS 4 — PRESENT BIAS",
     "Present Bias. The dealer that always finds you.",
     "The orange PRESENT BIAS badge (melting hourglass icon) fills frame. Brain Villain — CENTER "
     "frame, LARGE, his biggest appearance of the video — in a subtle trench coat, opens one side "
     "revealing tiny 'NOW' pills glowing orange. Dark alley vignette, still cartoon-friendly."),
    (26, "BIAS 4 — PRESENT BIAS",
     "To your brain, you-today is a real person. You-in-ten-years is a stranger in a stock photo.",
     "Split: left — a vivid, full-color silhouette labeled by a bright TODAY sun icon; right — a "
     "grainy, gray, out-of-focus cardboard cutout inside a cheap picture frame. The contrast is the joke."),
    (27, "BIAS 4 — PRESENT BIAS",
     "The onset: 'I'll start saving next month.' It feels responsible. It's actually the high.",
     "ONSET: a calendar where the 'next month' page glows warm and golden like a sunrise — while an "
     "orange gauge quietly fills at frame edge. A relaxed silhouette leans back, feet up, bathed in "
     "that warm postponement light."),
    (28, "BIAS 4 — PRESENT BIAS",
     "At the peak, today's wants outvote tomorrow's needs every single time — dinner beats retirement, now beats later.",
     "PEAK: a voting scene — five energetic bright 'today' figures stuffing a ballot box, while one "
     "gray elderly figure waits at an empty second box. The count board shows tally marks 5 vs 0."),
    (29, "BIAS 4 — PRESENT BIAS",
     "The comedown never comes today. That's the design. The bill is always addressed to the stranger.",
     "COMEDOWN: an envelope sliding forward through a paper calendar tunnel, addressed with the "
     "gray stranger's blurry portrait stamp. It travels away from the vivid TODAY figure who waves happily."),
    (30, "BIAS 4 — PRESENT BIAS",
     "Until one morning you're the stranger, opening the mail.",
     "The gray cardboard-cutout figure now stands in color — older silhouette at a mailbox at dawn, "
     "holding the accumulated envelope stack. The vivid young figure is now the faded photo on the wall."),
    (31, "BIAS 4 — PRESENT BIAS",
     "Present bias doesn't steal your money. It borrows it from someone you haven't met yet — you.",
     "LAPIDARIA FRAME: an anonymous hand passing a signed IOU note INTO a mirror — the reflection "
     "reaching back to receive it is the same hand, older and grayer. Minimal, white background, mirror center."),

    # ═══ CTA ═══
    (32, "CTA",
     "Four down, six to go. If your brain has already shown up twice in this catalog — subscribe.",
     "The four completed badges (teal, red, purple, orange) lined up like collected stamps; six empty "
     "slots waiting. A clean subscribe button below. Brain Villain — SMALL, tucked in the bottom-right "
     "corner — checks items off a clipboard."),
    (33, "CTA",
     "We name one of these programs every week. Free, painless, and mildly uncomfortable in the good way.",
     "Weekly calendar strip with a small brain icon on each Thursday. Minimal, fast, no hard sell. "
     "No characters."),

    # ═══ BIAS 5 — HERD INSTINCT (pink badge) ═══
    (34, "BIAS 5 — HERD INSTINCT",
     "Herd Instinct. Social proof. The party drug.",
     "The pink HERD INSTINCT badge (three sheep icon) fills frame with confetti falling around it — "
     "the badge alone at the party. No characters."),
    (35, "BIAS 5 — HERD INSTINCT",
     "Your brain outsources decisions to the crowd — if everyone's buying, it must be safe.",
     "A brain icon with its 'decision' cable physically unplugged from itself and plugged into a "
     "crowd of silhouettes walking one direction. Diagram style, white background."),
    (36, "BIAS 5 — HERD INSTINCT",
     "The onset feels like belonging: everyone has the phone, the trip, the coin, the sneakers.",
     "ONSET: a warm circle of silhouettes all holding the same glowing phone/sneaker/coin icons; an "
     "empty welcoming gap in the circle invites the viewer in. Pink gauge fills at frame edge."),
    (37, "BIAS 5 — HERD INSTINCT",
     "At the peak, 'everyone's doing it' overrides every number you know. FOMO isn't fear of missing the thing — it's fear of standing outside the group.",
     "PEAK: through a warm window, a party of silhouettes glows inside; outside in cold blue, a single "
     "figure looks in. Between them, a falling price chart lies on the ground — ignored, stepped over "
     "by the figure walking toward the door."),
    (38, "BIAS 5 — HERD INSTINCT",
     "The comedown hits when the crowd moves on and you're still holding the receipt.",
     "COMEDOWN: confetti settling on an empty street at dawn; one silhouette holds a long receipt "
     "curling to the floor. The crowd is tiny dots leaving on the horizon toward a new glow."),
    (39, "BIAS 5 — HERD INSTINCT",
     "The crowd got the memories. You got the credit card statement.",
     "Split: left — polaroid photos of the group scattering in the wind; right — a single credit card "
     "statement pinned under a coffee mug, red total circled. No faces."),
    (40, "BIAS 5 — HERD INSTINCT",
     "Herds are great protection against lions. There are no lions at the mall.",
     "LAPIDARIA FRAME + humor: a herd of cartoon sheep packed inside a shopping mall atrium, alert, "
     "scanning for predators. A janitor silhouette mops, unbothered. One 'SALE' sign glows where a "
     "lion would be. White mall light."),

    # ═══ BIAS 6 — LIFESTYLE INFLATION (gold badge) ═══
    (41, "BIAS 6 — LIFESTYLE INFLATION",
     "Lifestyle Inflation. The tolerance effect.",
     "The gold LIFESTYLE INFLATION badge (rising balloon with € icon) fills frame; a clinical "
     "tolerance-scale ruler leans against it like lab equipment. No characters."),
    (42, "BIAS 6 — LIFESTYLE INFLATION",
     "Every raise feels enormous for exactly one month.",
     "A firework labeled with a € burst exploding brilliantly over a calendar month — and by the "
     "calendar's last row, only a thin smoke trail remains. One month, full arc."),
    (43, "BIAS 6 — LIFESTYLE INFLATION",
     "The onset: more money arrives, and 'needs' quietly upgrade themselves to match. Better coffee. Better car. Better everything.",
     "ONSET: an escalator of objects upgrading themselves as they ride up: paper coffee cup → artisan "
     "cup, small car → SUV, phone → newer phone. Gold gauge filling at frame edge. Nobody is pressing "
     "any buttons — the escalator runs alone."),
    (44, "BIAS 6 — LIFESTYLE INFLATION",
     "At the peak, you're earning double what you did five years ago — and saving exactly the same: nothing.",
     "PEAK: two paychecks side by side (one twice as tall) pouring into the same funnel — and from "
     "the funnel's bottom drips the identical single coin into an identical near-empty jar. Diagram style."),
    (45, "BIAS 6 — LIFESTYLE INFLATION",
     "That's tolerance. The dose went up. The effect didn't.",
     "A syringe-style gauge marked with € symbols: dose level rising high; beside it a flat "
     "'satisfaction' meter unmoved at the same low bar. Clinical white diagram, cartoon-clean."),
    (46, "BIAS 6 — LIFESTYLE INFLATION",
     "The comedown is the trap itself: there is no comedown. It just becomes your baseline. Forever.",
     "COMEDOWN subverted: the gauge's needle welded permanently at the high mark with a tiny padlock. "
     "The floor of the frame literally rises to meet it. Brain Villain — mid-size, EXITING the frame "
     "on the RIGHT edge — pockets the key mid-stroll."),
    (47, "BIAS 6 — LIFESTYLE INFLATION",
     "A raise doesn't make you richer. It makes your old life unaffordable.",
     "LAPIDARIA FRAME: a silhouette looks back at a small cozy glowing house now behind a velvet rope "
     "with a price tag higher than the mansion ahead. Minimal, dusk palette."),

    # ═══ BIAS 7 — SUNK COST (brown badge) ═══
    (48, "BIAS 7 — SUNK COST",
     "Sunk Cost. The loyalty program of bad decisions.",
     "The brown SUNK COST badge (sinking ship icon) fills frame. Beside it: a loyalty card full of "
     "little anchor stamps with the stamper frozen mid-air above it — 'buy 9 mistakes, the 10th is "
     "free.' Visual joke, no text needed beyond stamps. No characters."),
    (49, "BIAS 7 — SUNK COST",
     "You keep paying for the gym you don't attend, the course you don't finish, the project that died last year.",
     "Triptych of dusty objects: a gym card in cobwebs, an online course at 12% progress bar frozen, "
     "a project folder with a tiny gravestone. Each still has a glowing auto-payment cable attached."),
    (50, "BIAS 7 — SUNK COST",
     "The onset is a sentence: 'But I've already put so much into it.'",
     "ONSET: a silhouette knee-deep in a hole, still digging; the pile of already-removed dirt towers "
     "behind them, casting the shadow that keeps them in the hole. Brown gauge at frame edge."),
    (51, "BIAS 7 — SUNK COST",
     "At the peak, the past runs your future — you throw good money after bad, because quitting would make the loss real.",
     "PEAK: fresh green coins marching single-file off a pier into dark water where older sunken coins "
     "glimmer below. A hand keeps waving them forward like traffic control."),
    (52, "BIAS 7 — SUNK COST",
     "Here's what your brain hides from you: the money is already gone. It left when you spent it.",
     "Diagram: a wallet with a clean cut cable labeled by a past-calendar icon — the money's ghost "
     "already walked out the door long ago, waving. The wallet still holds the cut cable hopefully."),
    (53, "BIAS 7 — SUNK COST",
     "The comedown lasts years: every month you stay is another payment on a decision you already know was wrong.",
     "COMEDOWN: a long staircase downward where each step is a monthly receipt; a silhouette descends "
     "slowly, dropping a coin on each step. The staircase visibly leads nowhere — it fades into fog."),
    (54, "BIAS 7 — SUNK COST",
     "You're not protecting your investment. You're buying tickets to watch it sink.",
     "LAPIDARIA FRAME: a tiny theater: rows of seats facing a window where a ship sinks in slow "
     "motion. A silhouette buys another ticket at the booth — run by Brain Villain, SMALL, tucked in "
     "the BACKGROUND-LEFT. Deadpan staging."),

    # ═══ BIAS 8 — THE OPTIMISM LOOP (sky badge) ═══
    (55, "BIAS 8 — THE OPTIMISM LOOP",
     "The Optimism Loop. Planning fallacy, if you want the lab name.",
     "The sky-blue OPTIMISM LOOP badge (sun over calendar icon) fills frame; a tiny lab flask and a "
     "clipboard rest beside it — the 'lab name' gag. No characters."),
    (56, "BIAS 8 — THE OPTIMISM LOOP",
     "Next month, you'll spend less. Next month has been coming for nine years.",
     "A horizon road lined with identical 'NEXT MONTH' signposts stretching to the vanishing point — "
     "nine mile-markers visible. The sun never quite rises past the horizon."),
    (57, "BIAS 8 — THE OPTIMISM LOOP",
     "The onset: every budget you make stars a fictional character — a disciplined, unhurried you with no birthdays, no emergencies, no Fridays.",
     "ONSET: a movie poster mock-up: a glowing, caped, serene silhouette titled by a halo icon — "
     "surrounded by crossed-out icons: birthday cake, broken pipe, Friday cocktail. Sky gauge fills."),
    (58, "BIAS 8 — THE OPTIMISM LOOP",
     "At the peak, you plan for the best month you've ever had — every month.",
     "PEAK: twelve identical calendar pages pinned on a wall, each with the same single gold star "
     "template stapled on top. A stapler hand keeps going. Repetition is the image."),
    (59, "BIAS 8 — THE OPTIMISM LOOP",
     "The comedown arrives on day twenty-something, with a calendar full of exceptions that were 'one-time things.' All twelve months have one-time things.",
     "COMEDOWN: one calendar month covered in colorful collision stickers (cake, wrench, plane, gift, "
     "pizza) burying the neat budget grid beneath. Zoom-out hint: the other eleven months identical."),
    (60, "BIAS 8 — THE OPTIMISM LOOP",
     "Optimism is a great life partner and a terrible accountant.",
     "LAPIDARIA FRAME: split desk — left, a sunny figure watering a plant (great partner); right, the "
     "same sunny figure buried in receipts wearing a crooked accountant visor, numbers floating wrong. "
     "White background."),

    # ═══ BIAS 9 — DEFAULT BIAS (gray badge) ═══
    (61, "BIAS 9 — DEFAULT BIAS",
     "Default Bias. The silent subscription.",
     "The gray DEFAULT BIAS badge (recycling loop icon) fills frame — but dimmed, half-asleep. "
     "Brain Villain — CENTER frame in a soft spotlight, his one theatrical moment — tiptoes past "
     "it with a finger to his lips: shhh."),
    (62, "BIAS 9 — DEFAULT BIAS",
     "Whatever is already happening keeps happening — not because it's good, but because changing it requires a decision.",
     "A train running in a perfect circle on a gray loop of track; a lever for switching tracks stands "
     "nearby, cobwebbed, untouched. Nobody is driving the train."),
    (63, "BIAS 9 — DEFAULT BIAS",
     "The onset is nothing. That's its trick. The same bank since you were eighteen. The same tariff. The same insurance, renewing itself in the dark.",
     "ONSET: a dark room at night; three contracts on a desk quietly re-signing themselves with "
     "self-moving pens, glowing faint gray. The gauge at frame edge fills with static — 'nothing' "
     "as a substance."),
    (64, "BIAS 9 — DEFAULT BIAS",
     "At the peak, entire industries price your inertia into their business model — the loyalty penalty has a name because it's that reliable.",
     "PEAK: a corporate boardroom of suited silhouettes toasting over a chart labeled with a sleeping "
     "customer icon; the revenue bar built literally out of tiny sleeping figures stacked like bricks."),
    (65, "BIAS 9 — DEFAULT BIAS",
     "The comedown is spread so thin you never feel it: thirty euros here, sixty there, every month, for decades.",
     "COMEDOWN: a bathtub with a barely visible pinhole leak; single drops fall in slow rhythm into "
     "a bucket below that is, revealed by a step back, already ocean-sized. Decades in one image."),
    (66, "BIAS 9 — DEFAULT BIAS",
     "The most expensive decisions of your life are the ones you never made.",
     "LAPIDARIA FRAME: an auction room where the gavel slams down BY ITSELF on lots labeled with "
     "clock icons — sold to an EMPTY chair with a name card. No auctioneer, no characters. "
     "White, stark, minimal."),

    # ═══ BIAS 10 — SCARCITY MINDSET (dark navy badge) ═══
    (67, "BIAS 10 — SCARCITY MINDSET",
     "Scarcity Mindset. The heavy one.",
     "The dark navy SCARCITY badge (closing tunnel icon) fills frame — heavier, matte, absorbing "
     "light. Brain Villain — CENTER-LOW in frame, subdued — sets it down with visible effort, no "
     "jokes this time. Tone shift: quieter staging, more shadow."),
    (68, "BIAS 10 — SCARCITY MINDSET",
     "When money has been tight long enough, scarcity stops being a situation and becomes an operating system.",
     "A computer boot screen made of everyday life: a kitchen scene rendered inside a loading bar, "
     "booting an OS whose logo is the closing tunnel icon. The system starts before the person wakes."),
    (69, "BIAS 10 — SCARCITY MINDSET",
     "The onset: money worries start taxing your attention — rent math running in the background of every conversation.",
     "ONSET: two silhouettes talking at a café; above one, a faint transparent calculator overlay "
     "runs rent arithmetic nonstop behind their eyes. Navy gauge fills at frame edge — slowly, heavily."),
    (70, "BIAS 10 — SCARCITY MINDSET",
     "Researchers measured it: active financial scarcity can consume more cognitive capacity than a full night without sleep.",
     "Clean comparison diagram: two brain icons — one with a moon/no-sleep icon dimming 20% of it; "
     "one with a € worry icon dimming MORE of it. The scarcity brain is darker. Clinical white."),
    (71, "BIAS 10 — SCARCITY MINDSET",
     "At the peak, the tunnel closes in. Today's fire is all there is. Long-term thinking isn't a choice you're refusing — it's a luxury the tunnel doesn't stock.",
     "PEAK: first-person view inside a narrowing tunnel; the only lit thing ahead is a small fire "
     "labeled by a TODAY sun icon. On the tunnel walls, shelf outlines sit empty where 'future' items "
     "would be — bare hooks, no stock."),
    (72, "BIAS 10 — SCARCITY MINDSET",
     "And the cruelest part: the tunnel makes the exact decisions that keep you in the tunnel.",
     "Diagram: the tunnel drawn as a circle — decisions exiting the tunnel mouth curve around and "
     "become the bricks of the tunnel itself. A self-building loop. Navy on white, minimal."),
    (73, "BIAS 10 — SCARCITY MINDSET",
     "The comedown isn't even yours. It's inherited — scarcity teaches children what money feels like before they ever earn any.",
     "COMEDOWN: a kitchen table at night; two adult silhouettes over bills in low voices — and in the "
     "doorway, small and unnoticed, a child silhouette absorbing the scene. The navy gauge quietly "
     "begins refilling next to the child. Heaviest frame of the video."),
    (74, "BIAS 10 — SCARCITY MINDSET",
     "Poverty isn't just a number in an account. It's a full-time job your brain works for free.",
     "LAPIDARIA FRAME: a timecard machine; a brain icon punches in at a clock showing all 24 hours "
     "highlighted. The payslip printing out reads zero (icon: empty circle). Stark, dignified, no jokes."),

    # ═══ CLOSE ═══
    (75, "CLOSE — THE CATALOG",
     "Ten programs. One brain. Yours came pre-installed with all of them.",
     "All ten badges arranged in the thumbnail grid formation around a single central brain icon, "
     "cables connecting each badge to it like a motherboard. Full-circle echo of the thumbnail."),
    (76, "CLOSE — THE CATALOG",
     "You can't uninstall a bias. Nobody can.",
     "A cursor dragging one badge toward a trash bin — the badge snaps back on an elastic cable. "
     "Brain Villain — SMALL at the right edge — shrugs sympathetically: it's not personal, it's architecture."),
    (77, "CLOSE — THE CATALOG",
     "But a named program never runs quietly again — from now on, when one fires, some part of you will be watching.",
     "The ten badges now each have a small OPEN EYE icon etched into their corner. One badge lights "
     "up trying to run — and a spotlight snaps onto it instantly. The grid is under surveillance now."),
    (78, "CLOSE — THE CATALOG",
     "That part is new. It didn't exist eight minutes ago.",
     "Minimal: a single small eye icon on white, freshly drawn — construction lines still visible "
     "around it like wet ink. Quiet frame, maximum negative space."),
    (79, "CLOSE — THE CATALOG",
     "Send this catalog to the friend who's deep in sunk cost right now. They'll know exactly which one they're on.",
     "A phone mid-send: the ten-badge grid flying as a message bubble toward a contact avatar. "
     "The SUNK COST badge subtly glows on the recipient's side. Warm, friendly framing."),

    # ═══ TEASE ═══
    (80, "NEXT VIDEO TEASE",
     "Next week: two people. Same salary. Same city. At forty-five, one of them stops needing to work.",
     "Teaser split: two identical silhouettes at 25 walking away from a shared starting line — "
     "years-marks pass — at the 45 mark, one silhouette sits free on a hill, the other still walks "
     "the office treadmill. Dawn palette."),
    (81, "NEXT VIDEO TEASE",
     "The difference fits on a napkin. See you Thursday.",
     "A folded paper napkin on a table, one corner lifted, faint pen marks visible but unreadable. "
     "A tiny THURSDAY calendar chip beside it. Clean close."),
]

# ── PDF GENERATION ─────────────────────────────────────────────────────────────

TOTAL = len(BEATS)
CHUNK = 21

parts = []
i = 0
while i < TOTAL:
    parts.append((i + 1, min(i + CHUNK, TOTAL)))
    i += CHUNK

SECTION_STARTS = {}
last_sec = None
for b in BEATS:
    if b[1] != last_sec:
        SECTION_STARTS[b[0]] = b[1]
        last_sec = b[1]


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_pdf():
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

    pdf_path = "/home/user/Claudeeee/V16_final_IMAGE_PROMPTS.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=16*mm, rightMargin=16*mm,
                            topMargin=15*mm, bottomMargin=15*mm)

    flow = [
        Paragraph("NEUROCENTS · VIDEO 16", H2),
        Spacer(1, 4),
        Paragraph("IMAGE PROMPTS — VISUAL REFERENCE", H1),
        Spacer(1, 3),
        Paragraph(esc(TITLE), SUB),
        Spacer(1, 4),
        Paragraph(f"{TOTAL} beats · {len(parts)} parts · SIN ALEX · Villain solo en 7 beats (posición/tamaño variados) · resto: solo objetos/badges",
                  META),
        Spacer(1, 8),
        Paragraph(f"<b>STYLE PREAMBLE</b> — prepend to every prompt in Google Flow:<br/>{esc(STYLE)}",
                  STYLE_BOX),
    ]

    for pidx, (a, b) in enumerate(parts, 1):
        flow.append(Paragraph(f"IMAGE PROMPTS — PART {pidx}/{len(parts)}  (Beats {a}–{b})", PART))
        for beat in BEATS[a - 1:b]:
            num, sec, narration, image_prompt = beat
            if num in SECTION_STARTS:
                flow.append(Paragraph(
                    f'<font color="#B02A2A"><b>── {esc(SECTION_STARTS[num])} ──</b></font>', SEC_H))
            full_prompt = f"{STYLE} {image_prompt}"
            block = [
                Paragraph(f'<font color="#B02A2A"><b>BEAT {num}</b></font>  '
                          f'<b><i>"{esc(narration)}"</i></b>', BEATH),
                Paragraph(f'<b>Image Prompt:</b> {esc(full_prompt)}', IMG),
            ]
            flow.append(KeepTogether(block))
        flow.append(Paragraph(f"PART {pidx} DONE — Beats {a}–{b} ✓", DONE))
        flow.append(Spacer(1, 6))

    doc.build(flow)
    print(f"Saved: {pdf_path} | {TOTAL} beats | {len(parts)} parts")


if __name__ == "__main__":
    build_pdf()
