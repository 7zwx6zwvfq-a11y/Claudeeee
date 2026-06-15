#!/usr/bin/env python3
"""Production document for Video 12: The One Decision That Defeats All Three Brain Traps."""

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
         "Palette: beige skin, pink brain (#E8A598), red t-shirt, gray pants, green for savings/gains, "
         "red for debt/loss/danger, white for diagram/infographic scenes, "
         "warm beige interiors with soft oval ceiling spotlight, "
         "dark charcoal (#1A1A1A) for hook/void scenes. "
         "Bold black diegetic text labels integrated into the scene. 16:9, 1280x720.")

# (segment, scene, camera, lighting, mood, action, video)
BEATS = [

# ── HOOK ──────────────────────────────────────────────────────────────────────

("Every saving system fails at the same moment: when the salary arrives.",
 "Wide shot, white background. A row of four systems — a spreadsheet labeled BUDGET, a medal labeled DISCIPLINE, a gear labeled HABIT, an app icon labeled TRACKER — all crossed out with bold red X marks. Below each: a timestamp label 'FAILS AT PAYDAY.' Clean and declarative.",
 "Wide shot", "Flat, white", "Confrontational — every alternative destroyed upfront",
 "Four failed systems with X marks; FAILS AT PAYDAY label beneath each",
 "Static. X marks draw through each system in sequence. 2s."),

("Budgets need willpower. Discipline needs energy. Both run out by payday.",
 "Wide diagram. Two side-by-side fuel gauges: WILLPOWER and ENERGY. Both start full on Monday and drain steadily across a work week timeline. By FRIDAY (PAYDAY) both needles are in the red. Bold label: 'EMPTY WHEN YOU NEED THEM MOST.'",
 "Wide diagram shot", "Flat, white, red needles at payday", "The math made visual — both resources depleted at the worst moment",
 "Willpower and energy gauges draining across work week",
 "Animated. Both gauges drain left to right; both hit red at PAYDAY marker. 3s."),

("There is one decision that doesn't compete with any of it.",
 "Wide shot, white background. The same four failed systems from beat 1, faded to gray. But a single new element emerges in the center: a clean bank transfer icon (standing order symbol), no X, warm green border. It stands alone. Label: 'DOESN'T COMPETE.'",
 "Wide shot", "Flat, white, warm green on standing order", "One thing survives the elimination — the counter-system",
 "Four systems faded; one standing order icon emerges clean",
 "Static. Standing order icon fades in bright; failed systems dim. 2s."),

("Because it fires before the salary does.",
 "Close-up timeline diagram. Two events on a horizontal line: STANDING ORDER (left, green, timestamp 9:13) then SALARY ARRIVES (right, blue, timestamp 9:14). Green arrow pointing left: 'FIRES FIRST.' The order of events is the mechanism.",
 "Close-up diagram", "Flat, white, green left of blue", "The timing advantage — sequence is the solution",
 "Standing order left of salary on timeline; green arrow FIRES FIRST",
 "Static. Timeline draws left to right; green fires before blue. 2s."),

("Last Friday, Alex's salary arrived at 9:14 in the morning.",
 "Medium shot, warm desk interior. ALEX at his desk, phone in hand. A salary notification glows green on screen: 'SALARY RECEIVED — 3,200.' Timestamp: 9:14. Alex's expression: familiar Friday relief. Brain villain inside skull stirs awake.",
 "Medium shot, warm interior", "Warm amber desk light, phone glow", "Familiar ritual — the Friday trigger",
 "Alex reading salary notification; brain villain stirring inside skull",
 "Static. Notification glow warm; brain villain opening eyes. 2s."),

("By 9:15, four hundred euros were already gone.",
 "Close-up of phone screen. The balance has changed: a standing order has already fired. Where 3,200 was, now 2,800 shows. A small transfer notification below: 'STANDING ORDER — 400.' Timestamp: 9:15. Clean. Automatic. Done.",
 "Close-up, phone screen", "Flat, phone glow", "The counter-system already ran — before Alex even processed the salary",
 "Balance updated to 2,800; transfer notification visible",
 "Static. New balance holds; transfer notification crisp. 2s."),

("Not on rent. Not on an impulse. Not even on something his brain had been planning.",
 "Wide shot, white background. Three icons crossed out with bold X marks: a house icon (RENT), a shopping bag (IMPULSE), a thought bubble (BRAIN PLAN). None of these. A label beneath all three: 'NOT ANY OF THESE.' The elimination is deliberate.",
 "Wide shot", "Flat, white, red X marks", "Subverting expectations — this isn't the usual story",
 "Rent, impulse, plan icons all X'd out",
 "Static. X marks draw through each. 2s."),

("Four hundred euros moved before his brain registered the number.",
 "Close-up inside Alex's transparent skull. The brain villain is mid-stretch — waking up, eyes half-open. The transfer has already happened. A small 'TRANSFER COMPLETE' notification fades on screen outside the skull. The villain missed the window.",
 "Close-up, skull interior", "Warm interior brain glow", "The system ran before the villain could object",
 "Brain villain waking up too late; transfer already complete",
 "Static. Villain mid-stretch; notification fading. 2s."),

("His brain had no vote. The decision had already been made.",
 "Wide shot, white background. A meeting room scene. A small voting table — Brain Villain raises its hand. But a large CLOSED sign hangs on the table: 'VOTE CLOSED — 9 DAYS AGO.' The villain's hand is raised uselessly. The decision predates the meeting.",
 "Wide shot", "Flat, white", "The mechanism in one image — decision made before the trigger",
 "Brain Villain raising hand at already-closed vote; CLOSED stamp prominent",
 "Static. VOTE CLOSED stamp bold; villain hand frozen raised. 3s."),

("One standing order. Set up nine days earlier.",
 "Close-up of a calendar. Sunday circled — 9 days before payday. A standing order icon pinned to that Sunday. A dotted line connecting it to the following Friday (PAYDAY). The action and its effect, separated by time and calmness.",
 "Close-up, calendar", "Flat, warm calendar light", "The distance between decision and execution is the secret",
 "Sunday circled; standing order pinned; dotted line to payday",
 "Static. Dotted line connects Sunday to Friday. 2s."),

("Before the Reward Trap. Before Mental Accounting. Before Present Bias.",
 "Wide shot. Three trap icons in a row — Reward Trap (red), Mental Accounting (orange), Present Bias (yellow) — familiar from V11. Below them: a horizontal timeline. The standing order icon fires at the far left — before all three traps. Each trap has a later timestamp. Label: 'STANDING ORDER FIRES FIRST.'",
 "Wide shot, timeline", "Flat, white, trap icons in V11 colors", "The architecture of priority — the counter-system precedes the system",
 "Standing order fires first on timeline; three traps arrive later",
 "Static. Timeline fills left to right; standing order leftmost. 3s."),

("In the last video, we showed you the three programs. This is the counter-program.",
 "Wide split panel. LEFT: three trap gear icons, labeled 'THE PROGRAMS.' RIGHT: one single standing order icon, labeled 'THE COUNTER-PROGRAM.' The counter is singular, clean, confident against the three.",
 "Wide split panel", "Flat, white", "The setup and its answer — three programs vs one counter",
 "Three program gears left; one counter-program icon right",
 "Static. Both panels present; contrast clear. 2s."),

("This is it.",
 "Medium shot. ALEX looks directly at camera. Expression: composed, direct. Brain villain visible inside skull — unusually still, not smug. For once it has no immediate plan. Label in lower corner: 'ONE DECISION.'",
 "Medium shot, direct address", "Flat, white", "Declaration — the promise fulfilled in two words",
 "Alex to camera; brain villain uncharacteristically still",
 "Static. Eye contact direct. Label appears. 2s."),

# ── WHY KNOWING ISN'T ENOUGH ───────────────────────────────────────────────────

("Here's the part Alex got wrong.",
 "Medium shot. ALEX at his desk. A notebook is open beside him — pages filled with notes. His expression shifts from satisfaction to a memory of what happened next. Brain villain in the background, watching.",
 "Medium shot, warm interior", "Warm desk light", "Setup for the reversal — Alex thought he understood",
 "Alex with filled notebook; expression shifting to memory",
 "Static. Expression shift subtle but visible. 2s."),

("He watched the last video. He took notes. He sent it to his brother.",
 "Close-up of Alex's phone. Three sequential actions visible: a video playing (behavioral finance thumbnail), a notebook open with handwriting, a sent message thread. Three small checkmarks. He completed all the right steps.",
 "Close-up, phone", "Flat, phone glow", "Competence established — he did everything right, except the one thing",
 "Three phone actions: video watched, notes taken, message sent",
 "Static. Three checkmarks appear in sequence. 2s."),

("He understood exactly why his brain spent the money.",
 "Medium shot. ALEX at a whiteboard. The Reward Trap diagram drawn correctly — arrows, labels, mechanism. He drew it from memory. Brain villain inside skull crosses its arms, mildly impressed against its will.",
 "Medium shot, whiteboard", "Clean academic white", "Understanding is real — that's what makes the next beat hit harder",
 "Alex pointing at correct Reward Trap diagram; brain villain arms crossed",
 "Static. Whiteboard diagram complete. 2s."),

("He felt something shift — the specific feeling of finally getting it.",
 "Close-up of Alex's face. A quiet, precise expression: not triumph — recognition. The specific relief of a pattern clicking into place. Brain villain inside skull looks slightly alarmed for the first time.",
 "Close-up", "Soft warm light", "The false peak — this feeling will be contradicted",
 "Alex's recognition expression; brain villain slightly alarmed",
 "Static. Expression holds; brain villain's alarm subtle. 2s."),

("And on Friday, the salary notification arrived.",
 "Close-up of Alex's phone. The familiar green notification: 'SALARY RECEIVED — 3,200.' Same timestamp. Same green glow. The trigger that the whiteboard diagram was about.",
 "Close-up, phone", "Phone glow, warm green", "The trigger lands — same as always",
 "Salary notification identical to hook scene",
 "Static. Notification glows. 2s."),

("His brain asked: what do I deserve?",
 "Close-up inside Alex's transparent skull. The brain villain — wide awake, eyes sharp — holds up its familiar sign: 'WHAT DO I DESERVE?' The sign glows warm amber. The diagram on the whiteboard is still visible in the background, irrelevant.",
 "Close-up, skull interior", "Warm amber brain glow", "The trap runs anyway — awareness changes nothing",
 "Brain villain holding WHAT DO I DESERVE sign; whiteboard visible behind",
 "Static. Sign glows amber; whiteboard in background ignored. 2s."),

("The same question. The same Friday. The same amount gone.",
 "Wide split panel. LEFT: Last Friday (before watching the video). RIGHT: This Friday (after watching the video). Both panels are identical — same notification, same villain question, same diminished balance. Bold label centered between panels: 'SAME PROGRAM.'",
 "Wide split panel", "Flat, dual warm tones", "The gut punch — knowledge made no difference",
 "Two identical Fridays side by side; SAME PROGRAM label between",
 "Static. Both panels mirror each other exactly. 3s."),

("Knowing the name of a trap does not move the walls.",
 "Wide shot. ALEX stands in a room. The walls are labeled: 'REWARD TRAP' and 'PRESENT BIAS.' He can read the labels clearly. He can even point at them. The walls are still there. The door has not appeared.",
 "Wide shot, room interior", "Flat, slightly confined", "Awareness as a wall — you see it, you're still inside it",
 "Alex in labeled-wall room; walls unchanged by his awareness",
 "Static. Alex looking at labels; no exit visible. 2s."),

("Every finance book gives Alex the diagnosis. None of them give him the surgery.",
 "Wide shot. ALEX surrounded by a stack of finance books. In one hand: a printed DIAGNOSIS page (symptoms listed, cause identified). In the other hand: empty. The surgery side is missing. Bold label: 'DIAGNOSIS ≠ SURGERY.'",
 "Wide shot", "Flat, warm neutral", "The missing half — diagnosis without intervention is incomplete",
 "Alex holding diagnosis; empty hand where surgery should be",
 "Static. Empty hand prominent; label bold. 2s."),

("Because the surgery requires removing the decision — not improving it.",
 "Wide shot, white background. Two options side by side. LEFT: 'IMPROVE THE DECISION' — showing a willpower flexing icon, red X through it. RIGHT: 'REMOVE THE DECISION' — showing a clean standing order icon, green checkmark. The structural insight stated visually.",
 "Wide shot", "Flat, white, red left, green right", "The reframe — the solution is architectural, not behavioral",
 "IMPROVE (X'd out) vs REMOVE (checked); structural contrast clear",
 "Static. X and checkmark appear simultaneously. 3s."),

# ── WHY WILLPOWER FAILS ────────────────────────────────────────────────────────

("Roy Baumeister — social psychologist at Florida State University —",
 "Wide shot, academic setting. A cartoon Baumeister figure — methodical, measured, researcher energy — stands before a Florida State University backdrop. Bold label: 'ROY BAUMEISTER · FLORIDA STATE UNIVERSITY.' A decade of research behind him.",
 "Wide shot, academic", "Cool academic light", "Authority arrives — specific, credentialed, a decade of work",
 "Baumeister figure before university backdrop; name label prominent",
 "Static. Name label fades in. 2s."),

("spent a decade measuring something he calls ego depletion.",
 "Wide shot. A research timeline spanning ten years behind Baumeister — data points accumulating year by year. A central graph shows a depleting line. Bold label: 'EGO DEPLETION — 10 YEARS OF EVIDENCE.' The time investment makes the finding credible.",
 "Wide shot, research setting", "Cool academic light", "Rigor — a decade, not a hunch",
 "Ten-year timeline; ego depletion graph building across it",
 "Static. Timeline populates left to right. 2s."),

("Willpower is not a character trait. It is a finite resource.",
 "Wide diagram, white background. Two panels. LEFT: WILLPOWER AS CHARACTER TRAIT — a muscle icon, fixed, permanent, labeled 'YOU EITHER HAVE IT OR YOU DON'T,' bold red X. RIGHT: WILLPOWER AS RESOURCE — a fuel gauge, finite, depleting, green check. The reclassification is the insight.",
 "Wide diagram shot", "Flat, white", "The reclassification — moral judgment vs mechanism",
 "Character trait panel X'd; resource panel checked",
 "Static. X and check appear. 3s."),

("It depletes with every decision made — not just financial ones.",
 "Wide shot. A fuel gauge labeled WILLPOWER RESERVE. Around it: small decision icons orbiting — lunch menu icon, email reply icon, meeting conflict icon, commute choice icon. Each icon drains the gauge slightly as it orbits. The reserve drops with each non-financial decision.",
 "Wide shot", "Flat, white, gauge central", "Scope revelation — the financial decision competes with everything",
 "Willpower gauge surrounded by life decisions; each draining it",
 "Animated. Icons orbit; gauge drains with each. 3s."),

("Deciding what to eat for lunch draws from the same reserve as deciding not to spend the salary.",
 "Wide diagram. A single pool — WILLPOWER RESERVE. Two pipes draw from it simultaneously: one labeled LUNCH CHOICE (small pipe), one labeled SALARY DECISION (large pipe). Same pool. Both pipes open on payday. Bold label: 'SAME RESERVE.'",
 "Wide diagram shot", "Flat, white", "The shared pool — trivial and critical draw from the same source",
 "One reserve pool with two draining pipes; SAME RESERVE label",
 "Static. Both pipes visible; pool level dropping. 2s."),

("By payday, Alex's reserve is nearly empty.",
 "Close-up of the gauge. A FRIDAY / PAYDAY label on the right. The needle is deep in the red — barely visible above zero. A small critical warning icon. The worst moment to need willpower.",
 "Close-up, gauge", "Red warning light", "The timing problem stated — depleted exactly when needed",
 "Gauge needle deep in red at PAYDAY marker",
 "Static. Needle holds in red. 2s."),

("His back hurts. His focus is gone. He's been patient all week.",
 "Medium shot. ALEX at his desk, Friday end-of-day posture: one hand on lower back, eyes slightly unfocused. A wall calendar shows five weekdays all checked. Every task completed. He paid for the week with his reserve.",
 "Medium shot", "Warm interior, end-of-day light", "Legitimacy — his exhaustion is real and earned",
 "Alex with back pain and unfocused eyes; completed week calendar",
 "Static. Calendar tasks prominent; posture communicates the cost. 2s."),

("The moment he needs discipline most is the exact moment he has the least.",
 "Wide diagram. A timeline from Monday to Friday. Two lines crossing: DISCIPLINE NEEDED (flat horizontal — constant) and DISCIPLINE AVAILABLE (declining steeply). They diverge increasingly toward Friday. At PAYDAY: the gap is largest. Bold label: 'THE WORST MOMENT.'",
 "Wide diagram shot", "Flat, white", "The cruel math — maximum need, minimum resource",
 "Two lines diverging across work week; gap widest at PAYDAY",
 "Static. Gap at payday prominent. 3s."),

("A budget is a willpower machine.",
 "Wide shot. A budget spreadsheet icon reimagined as a machine — gears, input valves, fuel intake pipe labeled WILLPOWER. The machine needs continuous fuel to run. Bold label: 'BUDGET = WILLPOWER MACHINE.' The analogy does the work.",
 "Wide shot", "Flat, white, industrial", "The reframe — a budget is not a tool, it's a fuel consumer",
 "Budget reimagined as machine with willpower fuel intake",
 "Static. Machine label appears. 2s."),

("It asks Alex to make the right decision, at the right moment, every payday, for thirty years.",
 "Wide shot. A long calendar: 30 years of paydays. Each payday marked with a small 'DECISION REQUIRED' icon. 360 paydays. 360 decisions. The scale becomes the problem. Bold label: '360 DECISIONS IN 30 YEARS.'",
 "Wide shot, long calendar", "Flat, white", "The scale — the problem compounded over time",
 "30-year calendar with 360 decision icons; scale visible",
 "Static. Calendar fills; count appears. 3s."),

("The Brain Villain is patient. Willpower has a ceiling.",
 "Medium shot. Brain Villain in a comfortable waiting room chair — unhurried, arms folded, a small clock on the wall. Beside the clock: a glass ceiling labeled WILLPOWER CEILING. The villain knows the math. It can wait.",
 "Medium shot, waiting room", "Flat, warm neutral", "The asymmetry — infinite patience vs finite resource",
 "Brain Villain comfortable in waiting room; willpower ceiling visible",
 "Static. Villain relaxed; ceiling label prominent. 2s."),

("Over thirty years, the math does not favor Alex.",
 "Wide shot. Two lines on a 30-year graph: BRAIN VILLAIN PATIENCE (flat, permanent, never depleting) and ALEX WILLPOWER (erratic, periodically recovering, never consistent). Over thirty years, the villain's line is unbroken. Alex's fluctuates and never reliably rises. Label: 'LONG-TERM MATH.'",
 "Wide diagram shot", "Flat, white", "The verdict — three decades of math against willpower",
 "Two lines: flat villain patience vs erratic willpower; 30-year span",
 "Static. Both lines across full 30-year span. 3s."),

# ── THE DECISION ───────────────────────────────────────────────────────────────

("There is only one way to beat a system that runs automatically.",
 "Wide shot, white background. The three trap gears spinning — the automatic system. A bold question forms below: 'HOW DO YOU BEAT AN AUTOMATIC SYSTEM?' The answer is about to change the frame.",
 "Wide shot", "Flat, white", "The single path — the setup for the reframe",
 "Three trap gears spinning; question forming below them",
 "Animated. Gears spin; question text fades in. 2s."),

("Build a counter-system that also runs automatically.",
 "Wide shot. A new gear emerges — single, clean, green, labeled COUNTER-SYSTEM. It doesn't fight the three trap gears. It slots in BEFORE them on the timeline. It runs first. Label: 'AUTOMATIC vs AUTOMATIC.'",
 "Wide shot", "Flat, white, green counter-gear", "The symmetry — match the system's nature",
 "Counter-system gear slots before trap gears on timeline",
 "Static. Counter-gear arrives and positions before traps. 3s."),

("Alex set up a standing order.",
 "Medium shot. ALEX at his laptop on a Sunday morning. Relaxed posture — coffee nearby, no Friday exhaustion. A bank transfer interface on screen. He fills in: 400 euros, recurring, payday minus one day. He clicks confirm. Brain villain: absent. This decision is made without opposition.",
 "Medium shot, Sunday morning", "Soft warm Sunday light", "The optimal moment — calm, rested, villain not present",
 "Alex at laptop Sunday; bank transfer being set up; villain absent",
 "Static. Screen setup visible; Alex's relaxed expression. 2s."),

("Four hundred euros. Every payday. Before he sees the balance.",
 "Wide shot, white background. Three bold facts stacked: '€400.' 'EVERY PAYDAY.' 'BEFORE HE SEES THE BALANCE.' Clean, declarative. No explanation needed. The three parameters of the counter-system.",
 "Wide shot", "Flat, white, bold text", "The system stated — three parameters, nothing more",
 "Three bold parameters stacked; clean and complete",
 "Static. Parameters appear one at a time, top to bottom. 2s."),

("Before the Reward Trap can ask what he earned.",
 "Medium shot. The Reward Trap gear (labeled, red) beginning to spin as the salary notification arrives. But a standing order checkmark appears one beat before — already done. The trap gear starts spinning into absence. Nothing to capture.",
 "Medium shot", "Flat, red trap vs green checkmark", "Sequence as defense — the trap arrives after the decision ran",
 "Reward Trap gear spinning into empty space; standing order already complete",
 "Static. Checkmark before gear; gear finds nothing. 2s."),

("Before Mental Accounting creates a label for it.",
 "Medium shot. Mental Accounting's label machine (gears creating category boxes) about to run. The standing order already moved the 400 euros. The label machine idles — no money to categorize. A small 'NOTHING TO LABEL' indicator.",
 "Medium shot", "Flat, orange tone for mental accounting", "The label never gets created — the money isn't there",
 "Mental Accounting label machine idling; nothing to process",
 "Static. Machine idle; nothing to label indicator. 2s."),

("Before Present Bias tells him Future Alex will handle it.",
 "Medium shot. Present Bias mechanism — Future Alex silhouette in the distance, receiving the usual deferral signal. But the 400 euros are gone. The deferral message has nothing to defer. Future Alex holds up empty hands: nothing arrived.",
 "Medium shot", "Flat, yellow tone for present bias", "The deferral never lands — the decision predated it",
 "Future Alex receiving empty deferral; nothing to hand over",
 "Static. Empty hands on Future Alex; signal arrives empty. 2s."),

("The Reward Trap fires the moment the salary notification arrives. The standing order fires one minute earlier.",
 "Wide timeline diagram. SALARY ARRIVES: 9:14 (blue). REWARD TRAP FIRES: 9:14 (red). STANDING ORDER FIRES: 9:13 (green, one position left). The green line precedes everything. A bold green arrow: 'ONE MINUTE EARLIER.' The architecture of the advantage.",
 "Wide timeline shot", "Flat, white, green left of red", "The one-minute advantage — the timing is the mechanism",
 "Timeline: green standing order fires before red reward trap",
 "Static. Green leftmost on timeline; one minute label. 3s."),

("Mental Accounting creates emotional categories — labels that make spending feel logical. The standing order creates one category the Brain Villain is never shown.",
 "Wide shot. Mental Accounting's visible category boxes: SALARY, REWARDS, EMERGENCY FUND, SPENDING MONEY — all visible to the Brain Villain (shown looking at them). Then one additional box, separated, dimly bordered, no label, no arrow from villain: 'CATEGORY THE VILLAIN NEVER SEES.'",
 "Wide shot", "Flat, white, hidden box subtly distinct", "The hidden category — outside the villain's visibility",
 "Brain Villain reviewing category boxes; one hidden box outside its view",
 "Static. Hidden box distinct; villain's attention on visible boxes only. 3s."),

("Present Bias says Future Alex will be disciplined. Past Alex already was — nine days ago, when he was calm, rested, and the villain was quiet.",
 "Wide shot. Three Alex versions: FUTURE ALEX (distance, confident wave, promises discipline). PRESENT ALEX (Friday, depleted, open wallet). PAST ALEX (Sunday morning, laptop, bank transfer confirmed, calm expression, villain-free). Bold arrow from Past Alex to PAYDAY: 'ALREADY DONE.' The future arrives handled.",
 "Wide shot, three Alexes", "Gradient: sepia Sunday to warm present to faded future", "The time reversal — the past handled what the future was supposed to",
 "Three Alexes: past calm, present depleted, future promising; past wins",
 "Static. ALREADY DONE arrow bold from Sunday. 3s."),

("Alex didn't learn to say no to the Brain Villain. He cancelled the meeting.",
 "Wide shot. A meeting room. Brain Villain sits at the table — notepad open, arguments prepared, ready to negotiate. Alex is not there. On the door: a bold 'MEETING CANCELLED — 9 DAYS AGO' notice. The villain sits alone in an empty room.",
 "Wide shot, meeting room", "Flat, warm neutral", "The jaw-drop reframe — the fight never happened",
 "Brain Villain alone at meeting table; MEETING CANCELLED on door",
 "Static. Villain alone; cancelled notice prominent. 3s."),

("The Brain Villain cannot fight a decision it was never invited to attend.",
 "Close-up at the meeting table. Brain Villain's notepad of arguments is open but useless. A cancelled invitation sits on the table beside it. The villain cannot object to what it was never part of. Expression: rare confusion.",
 "Close-up, meeting table", "Flat, warm neutral", "The logical consequence — no invitation, no fight",
 "Brain Villain with cancelled invitation and useless argument notepad",
 "Static. Villain's confusion expression rare and deliberate. 2s."),

("The money is simply not there to be calculated.",
 "Medium shot. ALEX's account balance on screen. The 400 euros are visibly absent — a completed transfer line, not a loss. Brain Villain leans in to do its calculation. There is nothing to calculate. Expression: can't compute.",
 "Medium shot", "Flat, neutral", "The clean resolution — no money, no battle",
 "Brain Villain leaning to calculate; nothing to find",
 "Static. Balance shows prior transfer; villain baffled. 2s."),

# ── CTA ────────────────────────────────────────────────────────────────────────

("If your brain is running these programs right now — subscribe.",
 "Medium shot. ALEX turns to camera. Direct, calm. Brain villain freezes behind him — caught mid-operation, hand stuck in forward position.",
 "Medium shot, direct address", "Flat, white", "Direct — no pressure, no theater",
 "Alex to camera; brain villain frozen behind",
 "Static. Villain freeze deliberate. 2s."),

("Every week: one bias. How it works. Who exploits it. And what you can actually do about it.",
 "Medium shot continues. Brain Villain rolls its eyes. Alex turns back. Hard cut — momentum resumes.",
 "Medium shot, cut back", "Flat, white", "Brevity — the CTA earns nothing it doesn't need",
 "Villain eye roll; Alex returning to video; hard cut",
 "Brain Villain eye roll; hard cut. 3s."),

# ── THE SCIENCE ─────────────────────────────────────────────────────────────────

("Richard Thaler and Shlomo Benartzi — University of Chicago and UCLA, 2004 —",
 "Wide shot, academic setting. Two cartoon figures side by side: THALER (warm, professorial, University of Chicago) and BENARTZI (analytical, focused, UCLA). Institution banners behind each. Bold label: 'THALER + BENARTZI · 2004.' Two Nobel-adjacent researchers.",
 "Wide shot, academic", "Warm academic light", "Credibility — two institutions, one year, one idea",
 "Thaler and Benartzi figures; institution labels prominent",
 "Static. Both figures and labels appear. 2s."),

("designed a program called Save More Tomorrow.",
 "Wide shot. A clean program icon on white: 'SAVE MORE TOMORROW.' The name is deliberately paradoxical. Not save now. Tomorrow. A small calendar icon beside it — the delay is the mechanism. Label: 'THE PROGRAM THAT CHANGED BEHAVIORAL ECONOMICS.'",
 "Wide shot", "Flat, white", "The paradox named — save more, but not now",
 "Save More Tomorrow program icon; paradox in the name",
 "Static. Program icon clean and prominent. 2s."),

("They didn't ask workers to save more now.",
 "Wide shot. A conventional savings prompt: a form asking 'SAVE MORE NOW — YES/NO?' Workers shown crossing it out, walking past, shaking heads. The typical ask. The Brain Villain nodding in satisfaction — this approach fails as expected.",
 "Wide shot", "Flat, white, red X on prompt", "What they didn't do — destroy the alternative first",
 "Conventional save-now prompt being rejected; Brain Villain satisfied",
 "Static. Workers rejecting prompt; villain nod. 2s."),

("They asked one question: when your next raise comes, can we automatically redirect a fixed percentage?",
 "Wide shot. A clean single question on a form: 'WHEN YOUR NEXT RAISE COMES — AUTO-REDIRECT A FIXED %?' Workers looking at it. The question removes immediate sacrifice. Brain Villain in corner: not alarmed. The villain doesn't see a threat because there's nothing happening right now.",
 "Wide shot", "Flat, white", "The elegant question — deferral + automation removes resistance",
 "Single clean question on form; workers considering; villain unconcerned",
 "Static. Question holds clean; villain not triggered. 2s."),

("Workers said yes — once.",
 "Close-up of a form. One checkbox: checked. One signature. A bold label: 'YES — ONCE.' Below: 'NO FURTHER DECISIONS REQUIRED.' The finality of one decision activating a decades-long system.",
 "Close-up, form", "Flat, white", "The singularity — one yes triggers everything that follows",
 "Single checkbox checked; YES — ONCE label prominent",
 "Static. Checkbox and label hold. 2s."),

("The system executed automatically, every raise cycle, with no further decisions required.",
 "Wide diagram. A raise cycle timeline: YEAR 1 → YEAR 2 → YEAR 3 → YEAR 4 → YEAR 5. Each year a raise arrives; automatically a percentage redirects. No input from worker. Small auto-execute icon at each step. Label: 'AUTOMATIC EXECUTION — EVERY CYCLE.'",
 "Wide diagram shot", "Flat, white", "The compounding automation — once set, never revisited",
 "Five-year raise cycle; auto-execute at each step; no manual input",
 "Static. Cycle fills left to right; auto icons appear at each raise. 3s."),

("Workers who started at a savings rate of three and a half percent",
 "Wide shot. A bar chart, starting position. One bar at 3.5% — small, honest, labeled 'STARTING RATE: 3.5%.' This is where most people stay forever. The baseline.",
 "Wide shot, bar chart", "Flat, white", "The starting point — modest, real, where most people are",
 "Single bar at 3.5%; STARTING RATE label",
 "Static. Bar holds at 3.5%. 2s."),

("reached thirteen point six percent within five years.",
 "Wide shot, same chart. The bar rises dramatically — from 3.5% to 13.6%. A time marker: '5 YEARS.' The growth is nearly four times. A bold label: '13.6% — FIVE YEARS. ZERO ADDITIONAL DECISIONS.' The result is undeniable.",
 "Wide shot, bar chart", "Flat, white, green bar", "The result — specific, measured, remarkable",
 "Bar rising from 3.5% to 13.6%; FIVE YEARS label; dramatic growth",
 "Animated. Bar rises from 3.5 to 13.6; label appears. 3s."),

("No budgets. No discipline. No willpower.",
 "Wide shot, white background. Three icons, each crossed out with bold X: BUDGET (spreadsheet), DISCIPLINE (flexing icon), WILLPOWER (effort icon). None of these were required. Bold label: 'NONE OF THESE.' The achievement without the tools.",
 "Wide shot", "Flat, white, red X marks", "The absence of the usual suspects — the point is what's missing",
 "Three usual tools all X'd out; NONE OF THESE label",
 "Static. X marks draw through each. 2s."),

("One structural decision replaced sixty monthly battles with the Brain Villain.",
 "Wide shot. LEFT: 60 small battle icons — 60 monthly confrontations, each requiring willpower. RIGHT: ONE standing order icon — clean, single, already set. A bold equals sign between them. Label: '1 DECISION = 60 BATTLES WON.' The math of architecture.",
 "Wide shot, comparison", "Flat, white", "The arithmetic of structure — one decision replaces sixty",
 "60 battle icons vs 1 standing order; equals sign between",
 "Static. Battle icons appear in bulk; one standing order beside them. 3s."),

("The only variable was structure.",
 "Wide shot, white background. A single bold statement dominates: 'THE ONLY VARIABLE: STRUCTURE.' Brain Villain stares at it. Cannot argue. No character flaw identified. No willpower deficit named. Just architecture.",
 "Wide shot", "Flat, white", "The clean verdict — no moral judgment, just engineering",
 "Bold statement: THE ONLY VARIABLE: STRUCTURE; villain staring",
 "Static. Statement holds; villain expression: out of arguments. 3s."),

# ── THE BRAIN VILLAIN'S LAST TRICK ─────────────────────────────────────────────

("The Brain Villain has one response to automation.",
 "Medium shot. Brain Villain — usually smug — now with a different expression: calculating. It's looking at the standing order setup on Alex's laptop. Its usual playbook isn't working. Something new is forming.",
 "Medium shot", "Flat, warm neutral, shifting", "The villain adapting — this is its only remaining move",
 "Brain Villain calculating response to automation; unusual expression",
 "Static. Villain expression shifts from smug to calculating. 2s."),

("It generates a feeling Alex can't immediately name: this doesn't feel safe.",
 "Close-up inside Alex's skull. The brain villain holds a sign that pulses with an unnamed feeling — deliberately vague, no label. A soft mist surrounds the skull interior. Alex's expression: uneasy, unable to identify the source. The feeling has no name yet.",
 "Close-up, skull interior", "Dim, uneasy interior light", "The unnamed feeling — the villain's most sophisticated tool",
 "Brain Villain holding unnamed feeling sign; mist inside skull",
 "Static. Feeling sign pulses; no label visible. 2s."),

("Alex looks at the standing order and thinks: what if I need that money?",
 "Medium shot. ALEX at laptop, standing order confirmed. A thought bubble forms above him: 'WHAT IF I NEED THAT MONEY?' The thought bubble is in Present Bias warm amber tones. Brain villain in corner — nodding slowly, satisfied.",
 "Medium shot", "Flat, warm; thought bubble amber", "The objection surfaces — the villain's costume change",
 "Alex with thought bubble; villain nodding at the objection",
 "Static. Thought bubble amber and warm; villain satisfied. 2s."),

("This is Present Bias wearing a different costume.",
 "Wide shot. The familiar Present Bias icon — the same mechanism from V11 — but now wearing a disguise: a mask labeled 'SAFETY CONCERN.' Underneath: identical mechanism. A hand lifts the mask to reveal: same gear, same Brain Villain operation. Bold label: 'SAME TRAP — DIFFERENT MASK.'",
 "Wide shot", "Flat, white", "The recognition — the villain rebranded, not redesigned",
 "Present Bias mechanism under a SAFETY CONCERN mask; mask lifted to reveal same gear",
 "Static. Mask-lift reveals identical mechanism. 3s."),

("It's not about the money. It's about the option.",
 "Wide shot. Two columns. LEFT: 'THE MONEY — €400' (amount visible, not the issue). RIGHT: 'THE OPTION — ABILITY TO SPEND IT' (abstract, the actual issue). Arrow pointing to RIGHT column. Label: 'THIS IS WHAT THE VILLAIN PROTECTS.'",
 "Wide shot", "Flat, white", "The insight — the villain's actual motivation is optionality, not spending",
 "Money column and option column; arrow to option",
 "Static. Arrow to option column; label appears. 2s."),

("The Brain Villain doesn't need to spend it. It just needs to know it could.",
 "Medium shot. Brain Villain sitting beside an open bank account — hand nearby but not touching. Not withdrawing. Just... watching. Monitoring the option. Expression: the presence of optionality is enough. Label: 'OPTION PRESERVED = VILLAIN SATISFIED.'",
 "Medium shot", "Flat, warm neutral", "The villain's actual satisfaction condition — not spending, just access",
 "Brain Villain near account; hand close but not touching; satisfied",
 "Static. Villain's proximity to account; contentment expression. 2s."),

("The standing order removes the option.",
 "Close-up. The standing order fires. The 400 euros move. The option is gone. Brain Villain reaches for it — nothing there. Not a conflict. Not a fight. Just absence. Clean removal.",
 "Close-up", "Flat, neutral", "The structural solution — not resistance, absence",
 "Brain Villain reaching; money gone; nothing to reach",
 "Static. Villain's reach finds absence. 2s."),

("That's exactly why it works.",
 "Wide shot. The standing order system running without confrontation. No battle icon. No willpower meter. The villain's hand reaches — finds nothing. A clean green checkmark. Label: 'NOT A FIGHT. AN ABSENCE.'",
 "Wide shot", "Flat, white, clean", "The mechanism stated — absence, not resistance",
 "Standing order running; no fight; NOT A FIGHT AN ABSENCE label",
 "Static. Label appears; villain finds nothing. 2s."),

("And exactly why the Brain Villain fights it.",
 "Medium shot. Brain Villain — smaller now, less imposing — looking at the standing order on Alex's laptop. The villain's expression: genuine discomfort. It understands the threat. It cannot negotiate with an absence.",
 "Medium shot", "Flat, warm neutral", "The villain's rare vulnerability — it has no move against absence",
 "Brain Villain smaller, uncomfortable, looking at standing order",
 "Static. Villain expression: discomfort. Rare. 2s."),

# ── IDENTITY CLOSE + GUIDE ─────────────────────────────────────────────────────

("Alex doesn't need more discipline.",
 "Medium shot. ALEX. Calm. The three trap gears visible in background — still spinning — but he is not fighting them. He stands beside his laptop, standing order running. No effort visible. No flexing. No strain.",
 "Medium shot", "Flat, warm neutral", "Identity reframe begins — from failure to architecture",
 "Alex calm; gears spinning behind him but not engaging him",
 "Static. Alex's posture: ease, not effort. 2s."),

("He needs fewer decisions — not better ones.",
 "Wide diagram. Two paths. LEFT: 'BETTER DECISIONS' — infinite repetition icons, willpower consumption, human fallibility, labeled 'EXHAUSTING.' RIGHT: 'FEWER DECISIONS' — one decision point, then automatic, labeled 'STRUCTURAL.' Arrow points right. Label: 'THE ACTUAL SOLUTION.'",
 "Wide diagram shot", "Flat, white", "The precise reframe — quality vs quantity of decisions",
 "Better vs Fewer decisions paths; fewer path labeled structural",
 "Static. Both paths; arrow to fewer decisions. 3s."),

("Every budgeting system asks him to win the same battle every month.",
 "Wide shot. A calendar — 12 months visible. Each month has a small battle icon: Brain Villain vs Alex. Month after month, the same confrontation. Label: '12 BATTLES PER YEAR. 360 IN 30 YEARS.' The repetition is the problem.",
 "Wide shot", "Flat, white", "The repetition made visible — the burden of monthly willpower",
 "Calendar with 12 battle icons; 360 in 30 years label",
 "Static. Battle icons fill calendar. 2s."),

("The standing order asks him to win it once.",
 "Wide shot. Same calendar — but now 11 months are empty. Just one battle icon: Sunday setup day. A bold 'ONCE.' floating over the empty months. The contrast is the point. 11 months of nothing.",
 "Wide shot", "Flat, white", "The contrast — one vs 360 battles",
 "Calendar with only one battle icon; ONCE label; empty months",
 "Static. Eleven empty months; one setup; ONCE label. 3s."),

("The Reward Trap fires on Friday. But the money is already gone.",
 "Medium shot. The Reward Trap gear fires — triggered by salary notification. It reaches for the 400 euros. Gone. A label where the money was: 'ALREADY MOVED.' The trap ran perfectly. Found nothing. The system worked against itself.",
 "Medium shot", "Flat, warm neutral", "The trap defeated not by resistance but by prior action",
 "Reward Trap gear reaching; ALREADY MOVED where money was",
 "Static. Trap finds nothing; ALREADY MOVED label. 2s."),

("Mental Accounting creates false categories. But there's now one it can never reach.",
 "Wide shot. Mental Accounting's category boxes visible: SALARY, REWARDS, EMERGENCY FUND, SPENDING MONEY. Brain Villain assigning labels. Then the hidden box — separated by a gap, slightly out of frame. No path from the label machine to it. Label: 'UNREACHABLE.'",
 "Wide shot", "Flat, white", "The unreachable category — outside the system's jurisdiction",
 "Mental Accounting labeling visible boxes; hidden unreachable box apart",
 "Static. Unreachable box dim but distinct. 2s."),

("Present Bias says Future Alex will be responsible. And this time — he already was.",
 "Wide shot. Present Bias mechanism sending deferral to Future Alex. But Past Alex (Sunday morning, laptop, standing order confirmed, calm) holds up a checkmark. The deferral lands and finds it already handled. Future Alex receives empty responsibility: nothing to do.",
 "Wide shot", "Flat, warm gradient", "The pattern broken — Past Alex handled what Present Bias deferred",
 "Past Alex checkmark; Future Alex receiving empty deferral",
 "Static. Past Alex checkmark; Future Alex empty hands. 3s."),

("The programs are not broken.",
 "Wide shot. The three trap gears — but now their labels change from trap names to their original functions: MOTIVATION SYSTEM, CATEGORIZATION SYSTEM, IMMEDIATE THREAT RESPONSE. Clean, neutral, functional. Bold label: 'NOT BROKEN — CONTEXTUALLY MISAPPLIED.'",
 "Wide shot", "Flat, white", "The reframe — programs as tools, not villains",
 "Three gears relabeled with original evolutionary functions",
 "Static. New labels replace trap labels. 2s."),

("They are perfectly designed for an environment where saving made no survival sense.",
 "Wide shot. Split panel. LEFT: ancient environment — sparse, immediate threats, no storage infrastructure. A figure surviving day to day. Saving food = impossible. RIGHT: modern Alex — salary, bank account, compound interest. The programs: same. The environment: completely different.",
 "Wide split shot", "Warm earthy tones left, clean modern white right", "The mismatch — programs calibrated for a world that no longer exists",
 "Ancient survival environment left; modern Alex right; same programs",
 "Static. Split environments clear; programs identical in both. 3s."),

("You didn't store food in a world where tomorrow was never guaranteed.",
 "Wide shot, ancestor context. A figure in an ancient landscape. No food storage. No planning beyond today. The instinct to spend immediately makes perfect survival sense in this context. Warm earthy tones.",
 "Wide shot, ancestor context", "Warm earthy tones", "The evolutionary logic — present bias was correct in its original world",
 "Ancestor figure; no storage; immediate consumption as survival logic",
 "Static. Ancestor context warm and clear. 2s."),

("The standing order is the first system Alex has ever used that was built for his world — not theirs.",
 "Wide split panel. LEFT: ancient environment (no storage, Present Bias correct). RIGHT: modern Alex with standing order running — built for compound interest, salary cycles, future self continuity. Same brain. Different architecture. Label: 'BUILT FOR THIS WORLD.'",
 "Wide split panel", "Earthy left, modern clean right", "The resolution — a system that matches the actual environment",
 "Ancient world left; modern standing order right; BUILT FOR THIS WORLD label",
 "Static. Split clear; label prominent. 3s."),

("Next video: Alex gets a tax refund. Eight hundred euros he didn't expect.",
 "Medium shot. ALEX's phone shows a new notification — different color from salary, different energy: 'TAX REFUND RECEIVED — 800.' Alex's expression: different. Not the usual salary anticipation. Something else. Brain villain lights up with a different pattern.",
 "Medium shot", "Flat, warm; notification different from salary", "Teaser — the same trap in unexpected clothing",
 "New tax refund notification; Alex's expression different; villain different pattern",
 "Static. Notification distinct from salary; different emotional register. 2s."),

("His brain treats it completely differently from every euro he ever earned.",
 "Close-up inside Alex's skull. The brain villain's response to the tax refund is visibly faster, larger, more urgent than the salary response. A different trigger. A different speed. The 800 euros feel like found money — not earned money.",
 "Close-up, skull interior", "Warm interior, faster brain villain pattern", "The distinction — found money vs earned money triggers differently",
 "Brain villain faster and more urgent for refund than salary",
 "Static. Villain response pattern visibly different. 2s."),

("Same trap. Different label. The refund disappears three times faster.",
 "Wide bar chart comparison. LEFT: SALARY — spend rate moderate, spread over days. RIGHT: TAX REFUND (same amount) — spend rate three times faster, spent in hours. Bold label: 'SAME MENTAL ACCOUNTING. DIFFERENT SPEED.' The mechanism accelerated.",
 "Wide chart comparison", "Flat, white", "The quantified difference — the trap runs faster on found money",
 "Salary spend rate vs refund spend rate; 3x faster for refund",
 "Static. Both bars visible; 3x faster contrast dramatic. 3s."),

("And the reason is the one nobody expects.",
 "Wide shot, white background. Three familiar trap icons visible. But a fourth element emerges — partially revealed, a question mark over it. A new label forming but not complete. Brain Villain gives a slow, reluctant nod. Even it respects this one. End screen appears in corner.",
 "Wide shot", "Flat, white, curiosity gap", "The open loop — sealed shut to drive the next video",
 "Three familiar traps; fourth partially revealed; villain reluctant nod; end screen",
 "Static. Question mark holds; end screen appears. Music fades. 3s."),

]  # end BEATS

SECTION_STARTS = {
    1:   "HOOK",
    14:  "WHY KNOWING ISN'T ENOUGH",
    24:  "WHY WILLPOWER FAILS",
    36:  "THE DECISION",
    49:  "CTA",
    51:  "THE SCIENCE",
    62:  "THE BRAIN VILLAIN'S LAST TRICK",
    71:  "IDENTITY CLOSE + GUIDE",
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
    r = title_p.add_run("CRAYON CAPITAL — CLONE SESSION · VIDEO 12")
    r.bold = True
    r.font.size = Pt(14)

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = sub_p.add_run("STATE 1 — PRODUCTION DOCUMENT")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    t_p = doc.add_paragraph()
    t_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t_p.add_run("The One Decision That Defeats All Three Brain Traps")
    r.bold = True
    r.italic = True
    r.font.size = Pt(14)

    doc.add_paragraph()

    HDR = ["#", "NARRATION", "IMAGE PROMPT", "CAMERA", "LIGHTING", "MOOD", "CHARACTER ACTION", "VIDEO MOTION"]
    tbl = doc.add_table(rows=1, cols=8)
    tbl.style = 'Table Grid'
    hdr_cells = tbl.rows[0].cells
    col_widths = [0.8, 4.5, 6.5, 3.0, 2.8, 2.8, 3.0, 3.2]
    for cell, txt, w in zip(hdr_cells, HDR, col_widths):
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
        data = [str(beat_num), seg, f"{STYLE} {scene}", cam, light, mood, action, video]
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

    path = "/home/user/Claudeeee/One_Decision_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
