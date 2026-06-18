#!/usr/bin/env python3
"""
V12 REVISED — The One Decision That Defeats All Three Brain Traps
NEW: Viral hook (30s, no storytelling) + visual-first beats (no redundant text labels)
89 beats · ~960 words · ~7.5 min
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph,
    Spacer, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# ─── STYLE GUIDE NOTE ────────────────────────────────────────────────────────
# IMAGE PROMPTS below contain ONLY scene-specific info.
# Prepend this block to every prompt when pasting into Google Flow:
#
# "2D flat cartoon illustration, thick solid black outlines, clean solid color
#  fills, no gradients. ALEX: large beige oval head, transparent glass upper
#  skull revealing pink cartoon brain villain, small black dot eyes, thin
#  neutral mouth, black spiky hair, blue t-shirt, gray pants. Brain villain:
#  pink cartoon brain, heavy-lidded eyes, smirk, small teeth. Palette: beige
#  skin (#F5E6C8), pink brain (#E8A598), blue shirt, gray pants, green for
#  savings, red for loss/danger, white for diagrams. 16:9, 1280x720."
# ─────────────────────────────────────────────────────────────────────────────

BEATS = [

# ══════════════════════════════════════════════════════════════════════════════
# HOOK — 30 seconds — NO storytelling — Promise + Hype + Open loop
# ══════════════════════════════════════════════════════════════════════════════

(1,"HOOK",
 "There is one decision that defeats all three brain traps.",
 "Alex facing camera, arms relaxed. Behind him: three trap gears visible but frozen, dormant. Villain behind Alex — unusually small, arms crossed defensively. No text labels anywhere.",
 "Medium shot, direct","Flat white",
 "Direct declaration — something is already different",
 "Alex steady gaze at camera; villain defensively small behind him",
 "Static. Hold 3s."),

(2,"HOOK",
 "Not a budget.",
 "White background. Budget spreadsheet icon centered. Bold red X strikes through it instantly.",
 "Close-up","Flat white",
 "Rapid elimination — destroy the alternative",
 "—",
 "X draws through icon. Fast. 1s."),

(3,"HOOK",
 "Not discipline.",
 "White background. Flexing arm / medal icon. Bold red X strikes through it.",
 "Close-up","Flat white",
 "Elimination",
 "—",
 "X draws through. Fast. 1s."),

(4,"HOOK",
 "Not a savings app.",
 "White background. Smartphone with app interface. Bold red X strikes through it.",
 "Close-up","Flat white",
 "Elimination",
 "—",
 "X draws through. Fast. 1s."),

(5,"HOOK",
 "One bank transfer. Set up once. Takes three minutes.",
 "Close-up of a clean laptop screen. A bank transfer form: single amount field, single date field, RECURRING toggle switched on. The form is almost embarrassingly simple. Cursor hovering over CONFIRM. No labels.",
 "Close-up, laptop screen","Soft laptop glow",
 "Simplicity — the solution is smaller than expected",
 "Cursor hovering over confirm; form nearly complete",
 "Form holds clean. 2s."),

(6,"HOOK",
 "And it fires before your brain gets a vote.",
 "Horizontal timeline. Two dots: LEFT green dot with timestamp 9:13. RIGHT blue dot with timestamp 9:14. A small green arrow points to the green dot — it fires first. No text labels beyond the timestamps.",
 "Wide timeline shot","Flat white, green left of blue",
 "The timing advantage stated visually — sequence is the mechanism",
 "—",
 "Green dot appears first; blue follows. 2s."),

(7,"HOOK",
 "Researchers tested this on four thousand workers. Starting savings rate: three and a half percent. Five years later: thirteen point six. Zero additional decisions.",
 "Bar chart. One bar: starts at 3.5% (small). Animates to 13.6% (nearly 4x taller). Two numeric labels only: '3.5%' at base, '13.6%' at peak. Small time marker: '5 YRS.' Nothing else on screen.",
 "Wide bar chart","Flat white, green bar rising",
 "The result — specific, undeniable, no commentary needed",
 "—",
 "Bar rises from 3.5 to 13.6. 3s."),

(8,"HOOK",
 "The Reward Trap. Mental Accounting. Present Bias. One decision — all three. Gone.",
 "Three trap gears spinning (red, orange, yellow — familiar from V11). A single green gear enters from the LEFT, slots in BEFORE them on a timeline. The three traps continue spinning — but into empty space. Nothing to catch.",
 "Wide shot","Flat white, green gear dominant",
 "The mechanism — one counter defeats three by arriving first",
 "—",
 "Green gear slots in; trap gears spin uselessly into empty space. 2s."),

(9,"HOOK",
 "In this video: exactly how it works — and the one move your brain will make to talk you out of it.",
 "Alex at camera. Confident. Behind him: the path is clear. Villain visible inside skull — eyes suddenly snapping open, alert. Something shifts. It has a plan.",
 "Medium shot, direct","Flat white",
 "Promise + open loop — the antagonist reactivates",
 "Alex confident; villain's eyes animate open behind him",
 "Villain eyes snap open. 2s."),

(10,"HOOK",
 "It knows this video exists.",
 "Close-up inside skull. Villain — smirk returning, notepad appearing, pen in hand. Writing something we can't see. Eyes sharp. For the first time: it looks ready.",
 "Close-up, skull interior","Warm interior brain glow",
 "The antagonist reloaded — open loop sealed",
 "Villain writing in notepad; scheming expression",
 "Notepad appears; pen moving. Cut. 2s."),

# ══════════════════════════════════════════════════════════════════════════════
# THE DEMONSTRATION — Alex's salary story
# ══════════════════════════════════════════════════════════════════════════════

(11,"THE DEMONSTRATION",
 "Last Friday, Alex's salary arrived at 9:14 in the morning.",
 "Medium shot, warm desk interior. Alex at desk, phone in hand. A green salary notification glows on screen — timestamp 9:14 visible. Alex's expression: familiar Friday feeling. Villain inside skull beginning to stir.",
 "Medium shot, warm interior","Warm amber desk light, phone glow",
 "Familiar trigger — the Friday ritual begins",
 "Alex reads notification; villain eyes opening inside skull",
 "Notification warm glow; villain waking. 2s."),

(12,"THE DEMONSTRATION",
 "By 9:15, four hundred euros were already gone.",
 "Close-up of phone screen. Balance changed: 3,200 is now 2,800. A completed transfer line below: STANDING ORDER — €400. Timestamp: 9:15. Clean. Already done.",
 "Close-up, phone screen","Flat, phone glow",
 "The counter-system already ran — before Alex processed the salary",
 "Balance updated; transfer line visible",
 "New balance holds; transfer line crisp. 2s."),

(13,"THE DEMONSTRATION",
 "Not on rent. Not on an impulse. Not on anything his brain had been planning.",
 "Wide shot, white background. Three icons: house (rent), shopping bag (impulse), thought bubble (plan). Each gets a red X through it — clean elimination. No text labels.",
 "Wide shot","Flat white, red X marks",
 "Subverted expectations — not the usual story",
 "—",
 "X marks draw through each in sequence. 2s."),

(14,"THE DEMONSTRATION",
 "Four hundred euros moved before his brain registered the number.",
 "Close-up inside Alex's transparent skull. Villain mid-stretch — waking up, eyes half-open. Outside the skull: a small TRANSFER COMPLETE notification already fading. The villain missed the window entirely.",
 "Close-up, skull interior","Warm interior brain glow",
 "The system ran before the villain could object",
 "Villain waking too late; notification fading outside",
 "Villain mid-stretch; notification already dim. 2s."),

(15,"THE DEMONSTRATION",
 "His brain had no vote.",
 "Wide shot, white background. A meeting room. Villain at the table, hand raised to vote. On the table: a large VOTE CLOSED stamp, ink still fresh. The decision predated this meeting entirely.",
 "Wide shot, meeting room","Flat white",
 "The mechanism — decision made before the trigger arrived",
 "Villain hand raised uselessly; VOTE CLOSED stamp prominent",
 "Stamp bold; villain hand frozen raised. 3s."),

(16,"THE DEMONSTRATION",
 "One standing order. Set up nine days earlier.",
 "Close-up of a calendar. A Sunday circled in green — nine days before payday. A standing order icon pinned to that Sunday. A dotted line connecting it forward to the following Friday.",
 "Close-up, calendar","Flat, warm calendar light",
 "The distance between decision and execution is the secret",
 "Sunday circled; icon pinned; dotted line to Friday",
 "Dotted line draws Sunday to Friday. 2s."),

(17,"THE DEMONSTRATION",
 "Before the Reward Trap. Before Mental Accounting. Before Present Bias.",
 "Wide timeline. Standing order icon fires at far left — before all three trap icons (red, orange, yellow). Each trap has a later timestamp. The sequence is the defence.",
 "Wide timeline shot","Flat white, trap icons in V11 colors",
 "Architecture of priority — counter-system fires first",
 "Standing order leftmost; three traps arrive later",
 "Timeline fills left to right; standing order fires first. 3s."),

(18,"THE DEMONSTRATION",
 "In the last video, we showed you the three programs. This is the counter-program.",
 "Wide split panel. LEFT: three trap gears (from V11, familiar). RIGHT: one single clean green standing order icon. The counter is singular, confident.",
 "Wide split panel","Flat white",
 "The setup and its answer — three programs vs one counter",
 "Three gears left; one counter-program icon right",
 "Both panels present; contrast clear. 2s."),

(19,"THE DEMONSTRATION",
 "This is it.",
 "Medium shot. Alex looks directly at camera. Composed. Villain inside skull — unusually still. No active scheme.",
 "Medium shot, direct address","Flat white",
 "Declaration — the promise fulfilled in two words",
 "Alex direct gaze; villain uncharacteristically still",
 "Eye contact holds. 2s."),

# ══════════════════════════════════════════════════════════════════════════════
# WHY KNOWING ISN'T ENOUGH
# ══════════════════════════════════════════════════════════════════════════════

(20,"WHY KNOWING ISN'T ENOUGH",
 "Here's the part Alex got wrong.",
 "Medium shot. Alex at his desk. A notebook open beside him — pages filled with notes. His expression shifts from satisfaction to a memory of what came next. Villain in background, watching quietly.",
 "Medium shot, warm interior","Warm desk light",
 "Setup for the reversal — Alex thought he understood",
 "Alex with filled notebook; expression shifting",
 "Expression shift subtle but visible. 2s."),

(21,"WHY KNOWING ISN'T ENOUGH",
 "He watched the last video. He took notes. He sent it to his brother.",
 "Close-up of Alex's phone. Three sequential actions: a behavioral finance video playing, a notebook open with handwriting, a sent message thread. Three checkmarks appear.",
 "Close-up, phone","Flat phone glow",
 "Competence established — he did everything right except one thing",
 "Three phone actions visible; checkmarks accumulate",
 "Three checkmarks appear in sequence. 2s."),

(22,"WHY KNOWING ISN'T ENOUGH",
 "He understood exactly why his brain spent the money.",
 "Medium shot. Alex at a whiteboard. The Reward Trap mechanism drawn correctly from memory. Villain inside skull crosses its arms — mildly impressed against its will.",
 "Medium shot, whiteboard","Clean academic white",
 "Understanding is real — that makes the next beat hit harder",
 "Alex pointing at correct diagram; villain arms crossed in reluctant respect",
 "Whiteboard complete. 2s."),

(23,"WHY KNOWING ISN'T ENOUGH",
 "He felt something shift — the specific feeling of finally getting it.",
 "Close-up of Alex's face. A quiet, precise expression: recognition. Not triumph. The relief of a pattern clicking into place. Villain inside skull looks slightly alarmed — for the first time.",
 "Close-up","Soft warm light",
 "The false peak — this feeling will be contradicted",
 "Alex's recognition expression; villain slightly alarmed",
 "Expression holds; villain's alarm subtle. 2s."),

(24,"WHY KNOWING ISN'T ENOUGH",
 "And on Friday, the salary notification arrived.",
 "Close-up of Alex's phone. Familiar green notification. Same timestamp. Same green glow. The trigger the whiteboard diagram was about.",
 "Close-up, phone","Phone glow, warm green",
 "The trigger lands — identical to before",
 "Salary notification identical to earlier scene",
 "Notification glows. 2s."),

(25,"WHY KNOWING ISN'T ENOUGH",
 "His brain asked: what do I deserve?",
 "Close-up inside Alex's transparent skull. Villain — wide awake, eyes sharp — holds up its sign: 'WHAT DO I DESERVE?' Warm amber. The whiteboard diagram still visible in background, ignored.",
 "Close-up, skull interior","Warm amber brain glow",
 "The trap runs anyway — awareness changes nothing",
 "Villain holding sign; whiteboard irrelevant in background",
 "Sign glows amber; whiteboard untouched. 2s."),

(26,"WHY KNOWING ISN'T ENOUGH",
 "The same question. The same Friday. The same amount gone.",
 "Wide split panel. LEFT: last Friday (before the video). RIGHT: this Friday (after the video). Both panels identical — same notification, same villain, same balance change. No labels. The silence says it.",
 "Wide split panel","Flat, dual warm tones",
 "The gut punch — knowledge made no difference",
 "Two identical Fridays mirrored side by side",
 "Both panels mirror exactly. 3s."),

(27,"WHY KNOWING ISN'T ENOUGH",
 "Knowing the name of a trap does not move the walls.",
 "Wide shot, room interior. Alex stands in a room. The walls are physically labeled with bias names. He can read them. He can point at them. The walls are still there. No exit.",
 "Wide shot, room interior","Flat, slightly confined",
 "Awareness as a wall — you see it, you're still inside",
 "Alex looking at labeled walls; no exit visible",
 "Alex and walls static. No movement. 2s."),

(28,"WHY KNOWING ISN'T ENOUGH",
 "Every finance book gives Alex the diagnosis. None of them give him the surgery.",
 "Wide shot. Alex surrounded by stacked finance books. One hand: a DIAGNOSIS page — symptoms listed, cause circled. Other hand: empty. The empty hand is the point.",
 "Wide shot","Flat, warm neutral",
 "The missing half — diagnosis without intervention",
 "Alex holding diagnosis; empty hand prominent",
 "Empty hand stays empty. 2s."),

(29,"WHY KNOWING ISN'T ENOUGH",
 "Because the surgery requires removing the decision — not improving it.",
 "Wide shot, white background. Two paths side by side. LEFT: willpower icon, human figure straining, effort arrows — red X through it. RIGHT: one standing order icon, single click, then automatic — green arrow forward.",
 "Wide shot","Flat white, red left, green right",
 "The reframe — architectural, not behavioral",
 "Two paths: effort X'd out vs automation chosen",
 "X and arrow appear simultaneously. 3s."),

# ══════════════════════════════════════════════════════════════════════════════
# WHY WILLPOWER FAILS
# ══════════════════════════════════════════════════════════════════════════════

(30,"WHY WILLPOWER FAILS",
 "Roy Baumeister — social psychologist at Florida State University —",
 "Wide shot, academic setting. Cartoon Baumeister figure — methodical, measured — before a Florida State University backdrop. Name label: 'ROY BAUMEISTER · FLORIDA STATE UNIVERSITY.'",
 "Wide shot, academic","Cool academic light",
 "Authority — specific, credentialed, a decade of work",
 "Baumeister figure before university backdrop; name label",
 "Name label fades in. 2s."),

(31,"WHY WILLPOWER FAILS",
 "spent a decade measuring something he calls ego depletion.",
 "Wide shot. A research timeline behind Baumeister — ten years of accumulating data points. A central depleting line graph. Label: 'EGO DEPLETION.'",
 "Wide shot, research setting","Cool academic light",
 "Rigor — a decade, not a hunch",
 "Ten-year timeline building; ego depletion graph depleting",
 "Timeline populates left to right. 2s."),

(32,"WHY WILLPOWER FAILS",
 "Willpower is not a character trait. It is a finite resource.",
 "Wide diagram, white background. Two panels. LEFT: fixed muscle icon — X through it. RIGHT: fuel gauge, needle descending — green check beside it. The reclassification in one image.",
 "Wide diagram shot","Flat white",
 "The reclassification — moral judgment vs mechanism",
 "Character trait X'd; resource panel checked",
 "X and check appear. 3s."),

(33,"WHY WILLPOWER FAILS",
 "It depletes with every decision made — not just financial ones.",
 "Wide shot. A fuel gauge at center. Around it: small decision icons orbiting — a lunch menu, an email, a meeting conflict, a commute. Each icon drains the gauge slightly as it orbits.",
 "Wide shot","Flat white, gauge central",
 "Scope revelation — everything draws from the same reserve",
 "Gauge surrounded by life decisions; each draining it",
 "Icons orbit; gauge drains with each pass. 3s."),

(34,"WHY WILLPOWER FAILS",
 "Deciding what to eat for lunch draws from the same reserve as deciding not to spend the salary.",
 "Wide diagram. A single pool at center labeled WILLPOWER RESERVE. Two pipes drawing from it simultaneously: one small (LUNCH CHOICE), one large (SALARY DECISION). Same pool. Both draining.",
 "Wide diagram shot","Flat white",
 "The shared pool — trivial and critical draw from the same source",
 "One reserve pool with two draining pipes",
 "Pool level dropping with both pipes open. 2s."),

(35,"WHY WILLPOWER FAILS",
 "By payday, Alex's reserve is nearly empty.",
 "Close-up of the gauge. Needle deep in red. A PAYDAY marker on the dial. Warning light on. The worst moment to need it.",
 "Close-up, gauge","Red warning light",
 "The timing problem — depleted exactly when needed",
 "Gauge needle deep in red at PAYDAY marker",
 "Needle holds in red. 2s."),

(36,"WHY WILLPOWER FAILS",
 "His back hurts. His focus is gone. He's been patient all week.",
 "Medium shot. Alex at his desk, Friday end-of-day: one hand on lower back, eyes slightly unfocused. A wall calendar behind him — five weekdays all checked. Every task completed.",
 "Medium shot","Warm interior, end-of-day light",
 "Legitimate exhaustion — the week cost something real",
 "Alex with back pain, unfocused; completed week calendar",
 "Calendar checks prominent; posture communicates the cost. 2s."),

(37,"WHY WILLPOWER FAILS",
 "The moment he needs discipline most is the exact moment he has the least.",
 "Wide diagram. Timeline from Monday to Friday. Two lines diverging: one flat (DISCIPLINE NEEDED, constant), one declining steeply (DISCIPLINE AVAILABLE). At PAYDAY: the gap between them is widest.",
 "Wide diagram shot","Flat white",
 "The cruel math — maximum need, minimum resource",
 "Two diverging lines; gap widest at PAYDAY",
 "Lines diverge to widest point at payday. 3s."),

(38,"WHY WILLPOWER FAILS",
 "A budget is a willpower machine.",
 "Wide shot. A budget spreadsheet icon reimagined as an industrial machine — gears, intake valve, a fuel pipe labeled WILLPOWER feeding it. The machine needs continuous fuel to run.",
 "Wide shot","Flat white, industrial",
 "The reframe — a budget is not a tool, it's a fuel consumer",
 "Budget reimagined as machine; willpower fuel intake visible",
 "Machine label appears. 2s."),

(39,"WHY WILLPOWER FAILS",
 "It asks Alex to make the right decision, at the right moment, every payday, for thirty years.",
 "Wide shot. A long calendar — 30 years of Fridays visible. Each payday has a small decision icon. In the corner, a counter climbs: 120... 240... 360. The scale becomes the problem.",
 "Wide shot, long calendar","Flat white",
 "The scale — the burden compounded over decades",
 "30-year calendar filling with decision icons; counter climbing to 360",
 "Calendar fills; counter climbs. 3s."),

(40,"WHY WILLPOWER FAILS",
 "The Brain Villain is patient. Willpower has a ceiling.",
 "Medium shot, waiting room. Villain in a comfortable chair — unhurried, arms folded. A clock on the wall. Above: a physical glass ceiling. Villain knows the math. It can wait.",
 "Medium shot, waiting room","Flat, warm neutral",
 "The asymmetry — infinite patience vs finite resource",
 "Villain comfortable; clock on wall; glass ceiling above",
 "Villain relaxed; ceiling visible. 2s."),

(41,"WHY WILLPOWER FAILS",
 "Over thirty years, the math does not favor Alex.",
 "Wide diagram. Two lines across a 30-year span. TOP line: flat and unbroken (villain's patience — permanent). BOTTOM line: erratic, periodically recovering but never consistent (Alex's willpower). After 30 years, villain's line is unbroken.",
 "Wide diagram shot","Flat white",
 "The verdict — three decades of math",
 "Flat villain line vs erratic willpower line across 30 years",
 "Both lines held across full span. 3s."),

# ══════════════════════════════════════════════════════════════════════════════
# THE DECISION
# ══════════════════════════════════════════════════════════════════════════════

(42,"THE DECISION",
 "There is only one way to beat a system that runs automatically.",
 "Wide shot, white background. Three trap gears spinning — the automatic system. Below them: a large question mark forming, growing.",
 "Wide shot","Flat white",
 "The single path — setup for the reframe",
 "Three trap gears spinning; question mark forming below",
 "Gears spin; question mark fades in. 2s."),

(43,"THE DECISION",
 "Build a counter-system that also runs automatically.",
 "Wide shot. A new green gear enters from the left — single, clean. It does not fight the three trap gears. It slots in BEFORE them on the timeline. It runs first.",
 "Wide shot","Flat white, green counter-gear",
 "The symmetry — match the system's nature",
 "Counter-system gear slots before trap gears on timeline",
 "Green gear positions before traps. 3s."),

(44,"THE DECISION",
 "Alex set up a standing order.",
 "Medium shot. Alex at his laptop on a Sunday morning. Relaxed — coffee nearby, no Friday exhaustion. Bank transfer form on screen. Villain: absent from skull entirely. This decision happens in silence.",
 "Medium shot, Sunday morning","Soft warm Sunday light",
 "The optimal moment — calm, rested, villain not present",
 "Alex at laptop Sunday; villain noticeably absent from skull",
 "Alex relaxed; empty skull visible. 2s."),

(45,"THE DECISION",
 "Four hundred euros. Every payday. Before he sees the balance.",
 "Close-up of laptop screen. Bank transfer form: €400 in amount field. RECURRING selected. Date: payday minus one day. Cursor on CONFIRM. Three clean fields. Nothing else.",
 "Close-up, laptop screen","Soft laptop glow",
 "The three parameters — simple, structural, complete",
 "Three form fields filled; cursor on confirm",
 "Form holds clean. 2s."),

(46,"THE DECISION",
 "Before the Reward Trap can ask what he earned.",
 "Medium shot. The Reward Trap gear (red) beginning to spin as salary notification arrives. A green checkmark appears one beat before it — transfer already complete. The trap gear spins into empty space.",
 "Medium shot","Flat, red trap vs green checkmark",
 "Sequence as defence — trap arrives after decision ran",
 "Reward Trap gear spinning into empty space; transfer already marked",
 "Checkmark before gear; gear finds nothing. 2s."),

(47,"THE DECISION",
 "Before Mental Accounting creates a label for it.",
 "Medium shot. Mental Accounting's labeling mechanism about to run. The standing order already moved the money. The labeler idles — nothing to process.",
 "Medium shot","Flat, orange tone for mental accounting",
 "The label never gets created — money isn't there",
 "Label mechanism idling; nothing to categorize",
 "Machine idle. 2s."),

(48,"THE DECISION",
 "Before Present Bias tells him Future Alex will handle it.",
 "Medium shot. Future Alex silhouette in the distance — the usual recipient of deferrals. The deferral signal arrives with nothing attached. Future Alex holds up empty hands.",
 "Medium shot","Flat, yellow tone for present bias",
 "The deferral never lands — decision predated it",
 "Future Alex receiving empty deferral; empty hands",
 "Signal arrives empty. 2s."),

(49,"THE DECISION",
 "The Reward Trap fires the moment the salary notification arrives. The standing order fires one minute earlier.",
 "Wide timeline. Three points on the line: STANDING ORDER at 9:13 (green, leftmost). SALARY ARRIVES at 9:14 (blue). REWARD TRAP FIRES at 9:14 (red, same position as salary). Green arrow under 9:13: it was here first.",
 "Wide timeline shot","Flat white, green left of red",
 "The one-minute advantage — timing is the mechanism",
 "Timeline: green standing order fires before red reward trap",
 "Timeline draws; green fires first. 3s."),

(50,"THE DECISION",
 "Mental Accounting creates emotional categories — labels that make spending feel logical. The standing order creates one category the Brain Villain is never shown.",
 "Wide shot. Mental Accounting's visible category boxes — SALARY, REWARDS, SPENDING MONEY — all in villain's line of sight. Then one additional box, separated, slightly off-frame: no path connecting villain to it. Unreachable by design.",
 "Wide shot","Flat white, hidden box subtly distinct",
 "The hidden category — outside villain's visibility",
 "Villain reviewing visible boxes; one box outside its view",
 "Hidden box distinct; villain attention on visible boxes only. 3s."),

(51,"THE DECISION",
 "Present Bias says Future Alex will be disciplined. Past Alex already was — nine days ago, when he was calm, rested, and the villain was quiet.",
 "Wide shot. Three Alex versions in one frame. FUTURE ALEX: distant, confident wave. PRESENT ALEX: Friday, depleted, open wallet. PAST ALEX: Sunday morning, laptop, transfer confirmed, calm, villain absent. A bold arrow from Past Alex forward to payday.",
 "Wide shot, three Alexes","Gradient: sepia Sunday, warm present, faded future",
 "Time reversal — the past handled what the future promised",
 "Three Alexes; past has checkmark; arrow to payday",
 "Arrow from Sunday bold. 3s."),

(52,"THE DECISION",
 "Alex didn't learn to say no to the Brain Villain. He cancelled the meeting.",
 "Wide shot, meeting room. Villain at the table — notepad open, arguments prepared, ready to negotiate. Alex is not there. On the door: a MEETING CANCELLED notice. The villain sits alone in an empty room.",
 "Wide shot, meeting room","Flat, warm neutral",
 "The jaw-drop reframe — the fight never happened",
 "Villain alone at meeting table; CANCELLED notice on door",
 "Villain alone; door notice prominent. 3s."),

(53,"THE DECISION",
 "The Brain Villain cannot fight a decision it was never invited to attend.",
 "Close-up at the meeting table. Villain's notepad of arguments open — useless. A cancelled invitation on the table beside it. Villain expression: rare confusion.",
 "Close-up, meeting table","Flat, warm neutral",
 "The logical consequence — no invitation, no fight",
 "Villain with cancelled invitation and useless notepad",
 "Villain confusion expression. Rare. 2s."),

(54,"THE DECISION",
 "The money is simply not there to be calculated.",
 "Medium shot. Alex's account balance on screen. The €400 absent — a completed transfer line, not a loss. Villain leans in to calculate. Finds nothing. Expression: can't compute.",
 "Medium shot","Flat, neutral",
 "Clean resolution — no money, no battle",
 "Villain leaning to calculate; nothing there; baffled",
 "Balance shows prior transfer; villain baffled. 2s."),

# ══════════════════════════════════════════════════════════════════════════════
# CTA
# ══════════════════════════════════════════════════════════════════════════════

(55,"CTA",
 "If your brain is running these programs right now — subscribe.",
 "Medium shot. Alex turns to camera. Direct, calm. Villain freezes behind him — caught mid-operation, hand stuck forward.",
 "Medium shot, direct address","Flat white",
 "Direct — no pressure, no theater",
 "Alex to camera; villain frozen mid-operation",
 "Villain freeze deliberate. 2s."),

(56,"CTA",
 "Every week: one bias. How it works. Who exploits it. And what you can actually do about it.",
 "Medium shot continues. Villain rolls its eyes. Alex turns back. Hard cut.",
 "Medium shot, cut back","Flat white",
 "Brevity — the CTA earns nothing it doesn't need",
 "Villain eye roll; Alex returning to video; hard cut",
 "Eye roll; hard cut. 3s."),

# ══════════════════════════════════════════════════════════════════════════════
# THE SCIENCE — Thaler & Benartzi
# ══════════════════════════════════════════════════════════════════════════════

(57,"THE SCIENCE",
 "Richard Thaler and Shlomo Benartzi — University of Chicago and UCLA, 2004 —",
 "Wide shot, academic setting. Two cartoon figures side by side: THALER (professorial, University of Chicago banner) and BENARTZI (analytical, UCLA banner). Label: 'THALER + BENARTZI · 2004.'",
 "Wide shot, academic","Warm academic light",
 "Credibility — two institutions, one year, one idea",
 "Thaler and Benartzi figures; institution labels prominent",
 "Both figures and labels appear. 2s."),

(58,"THE SCIENCE",
 "designed a program called Save More Tomorrow.",
 "Wide shot. A clean program icon: SAVE MORE TOMORROW. The name deliberately paradoxical. A small calendar icon beside it — the delay is the mechanism.",
 "Wide shot","Flat white",
 "The paradox named — save more, but not now",
 "Save More Tomorrow program icon; calendar beside it",
 "Icon appears. 2s."),

(59,"THE SCIENCE",
 "They didn't ask workers to save more now.",
 "Wide shot. A conventional save-now prompt — a YES/NO checkbox form. Workers crossing it out, walking past, shaking heads. Villain nodding in satisfaction — this approach fails as expected.",
 "Wide shot","Flat white, red X on conventional prompt",
 "Destroy the alternative first",
 "Workers rejecting save-now prompt; villain satisfied",
 "Workers rejecting; villain nods. 2s."),

(60,"THE SCIENCE",
 "They asked one question: when your next raise comes, can we automatically redirect a fixed percentage?",
 "Wide shot. A single clean question on a simple form. Workers looking at it, considering. Villain in the corner — not alarmed. It doesn't see a threat because nothing is happening right now.",
 "Wide shot","Flat white",
 "The elegant question — deferral plus automation removes resistance",
 "Single question on form; workers considering; villain unconcerned",
 "Question holds clean; villain not triggered. 2s."),

(61,"THE SCIENCE",
 "Workers said yes — once.",
 "Close-up of a form. One checkbox: checked. One signature. The form is closed and slid into a drawer. Done. Nothing more required.",
 "Close-up, form","Flat white",
 "The singularity — one yes triggers everything that follows",
 "Checkbox checked; form filed into drawer",
 "Drawer closes. 2s."),

(62,"THE SCIENCE",
 "The system executed automatically, every raise cycle, with no further decisions required.",
 "Wide diagram. A raise cycle timeline: YEAR 1 → YEAR 2 → YEAR 3 → YEAR 4 → YEAR 5. Each year: a raise arrives, a percentage auto-redirects. A small auto-execute symbol at each step. No human figure involved.",
 "Wide diagram shot","Flat white",
 "Compounding automation — set once, never revisited",
 "Five-year raise cycle; auto-execute symbols at each step",
 "Cycle fills left to right; auto symbols appear at each raise. 3s."),

(63,"THE SCIENCE",
 "Workers who started at a savings rate of three and a half percent",
 "Wide shot, bar chart. One bar: 3.5% — small, with '3.5%' label. This is where most people stay.",
 "Wide shot, bar chart","Flat white",
 "The starting point — modest and real",
 "Single bar at 3.5%",
 "Bar holds. 2s."),

(64,"THE SCIENCE",
 "reached thirteen point six percent within five years.",
 "Same chart. The bar rises dramatically to 13.6% — nearly four times taller. A small time marker: '5 YRS.' The '13.6%' label at the top of the bar. Nothing else.",
 "Wide shot, bar chart","Flat white, green bar",
 "The result — specific and remarkable",
 "Bar rising from 3.5 to 13.6; dramatic visual growth",
 "Bar rises to 13.6; label appears at peak. 3s."),

(65,"THE SCIENCE",
 "No budgets. No discipline. No willpower.",
 "Wide shot, white background. Three icons, each X'd out: budget spreadsheet, flexing arm, effort figure. Clean. The absence is the message.",
 "Wide shot","Flat white, red X marks",
 "The absence of the usual suspects — what's missing is the point",
 "Three usual tools X'd out",
 "X marks draw through each. 2s."),

(66,"THE SCIENCE",
 "One structural decision replaced sixty monthly battles with the Brain Villain.",
 "Wide comparison. LEFT: 60 small battle icons — dense, clustered, exhausting. RIGHT: ONE standing order icon — clean, single, already set. A bold equals sign between them.",
 "Wide shot, comparison","Flat white",
 "The arithmetic of structure",
 "60 battle icons vs 1 standing order; equals sign between",
 "Battle icons appear in bulk; standing order beside. 3s."),

(67,"THE SCIENCE",
 "The only variable was structure.",
 "Wide shot, white background. Villain staring at the standing order icon. Its usual weapons scattered on the floor unused: a temptation flag, an urgency alarm, a persuasion notepad. All useless. Villain expression: out of arguments.",
 "Wide shot","Flat white",
 "The clean verdict — no moral judgment, just engineering",
 "Villain surrounded by useless weapons on floor; staring at standing order",
 "Weapons scattered; villain expression: baffled. 3s."),

# ══════════════════════════════════════════════════════════════════════════════
# BRAIN VILLAIN'S LAST TRICK
# ══════════════════════════════════════════════════════════════════════════════

(68,"BRAIN VILLAIN'S LAST TRICK",
 "The Brain Villain has one response to automation.",
 "Medium shot. Villain — usually smug — now with a different expression: calculating. Looking at the standing order setup. Its usual playbook isn't working. Something new is forming.",
 "Medium shot","Flat, warm neutral, shifting",
 "The villain adapting — its only remaining move",
 "Villain calculating; expression shifts from smug to scheming",
 "Expression shift. 2s."),

(69,"BRAIN VILLAIN'S LAST TRICK",
 "It generates a feeling Alex can't immediately name: this doesn't feel safe.",
 "Close-up inside Alex's skull. Villain holds a sign — but the sign is deliberately BLANK, no text. A soft mist inside the skull. Alex's expression: uneasy, unable to identify the source.",
 "Close-up, skull interior","Dim, uneasy interior light",
 "The unnamed feeling — villain's most sophisticated tool",
 "Villain holding blank sign; mist inside skull; Alex uneasy",
 "Blank sign pulses; mist drifts. 2s."),

(70,"BRAIN VILLAIN'S LAST TRICK",
 "Alex looks at the standing order and thinks: what if I need that money?",
 "Medium shot. Alex at laptop, standing order confirmed. A thought bubble forms above him — warm amber tone (Present Bias color from V11). Villain in corner: nodding slowly, satisfied.",
 "Medium shot","Flat, warm; thought bubble amber",
 "The objection surfaces — villain's costume change",
 "Alex with amber thought bubble; villain nodding in corner",
 "Thought bubble appears amber; villain satisfied nod. 2s."),

(71,"BRAIN VILLAIN'S LAST TRICK",
 "This is Present Bias wearing a different costume.",
 "Wide shot. The familiar Present Bias mechanism from V11 — but now wearing a mask. The mask label: SAFETY CONCERN. A hand lifts the mask to reveal: same gear underneath, same mechanism, identical.",
 "Wide shot","Flat white",
 "The recognition — villain rebranded, not redesigned",
 "Present Bias under SAFETY CONCERN mask; mask lifted to reveal same gear",
 "Mask-lift reveals identical mechanism. 3s."),

(72,"BRAIN VILLAIN'S LAST TRICK",
 "It's not about the money. It's about the option.",
 "Wide shot. Two columns. LEFT: a stack of money (the euros themselves). RIGHT: an open door with a handle — the option to open it. An arrow points exclusively to the RIGHT column.",
 "Wide shot","Flat white",
 "The insight — villain protects optionality, not spending",
 "Money column vs option door; arrow to door",
 "Arrow to option column; door highlighted. 2s."),

(73,"BRAIN VILLAIN'S LAST TRICK",
 "The Brain Villain doesn't need to spend it. It just needs to know it could.",
 "Medium shot. Villain sitting beside an open bank account display — hand nearby but not touching. Not withdrawing. Just monitoring. Expression: the presence of optionality is enough.",
 "Medium shot","Flat, warm neutral",
 "Villain's actual satisfaction — not spending, just access",
 "Villain near account; hand close but not touching; satisfied",
 "Villain proximity; hand still. 2s."),

(74,"BRAIN VILLAIN'S LAST TRICK",
 "The standing order removes the option.",
 "Close-up. Standing order fires. The €400 moves. Villain reaches for the space where the money was. Empty. Not a fight. Just absence.",
 "Close-up","Flat, neutral",
 "Structural solution — absence, not resistance",
 "Villain reaching; empty space where money was",
 "Villain's reach finds nothing. 2s."),

(75,"BRAIN VILLAIN'S LAST TRICK",
 "That's exactly why it works. And exactly why the Brain Villain fights it.",
 "Medium shot. Villain — smaller now, less imposing — staring at the standing order on Alex's laptop. Expression: genuine discomfort. First time it has no move.",
 "Medium shot","Flat, warm neutral",
 "The villain's rare vulnerability — no move against absence",
 "Villain smaller, uncomfortable; looking at standing order",
 "Villain discomfort expression. First time. 2s."),

# ══════════════════════════════════════════════════════════════════════════════
# IDENTITY CLOSE + GUIDE
# ══════════════════════════════════════════════════════════════════════════════

(76,"IDENTITY CLOSE",
 "Alex doesn't need more discipline.",
 "Medium shot. Alex. Calm. Three trap gears visible in background — still spinning — but he is not fighting them. He stands beside his laptop, standing order running. No effort. No strain.",
 "Medium shot","Flat, warm neutral",
 "Identity reframe — from failure to architecture",
 "Alex calm; gears spinning in background but not engaging him",
 "Alex's posture: ease, not effort. 2s."),

(77,"IDENTITY CLOSE",
 "He needs fewer decisions — not better ones.",
 "Wide diagram. Two paths. LEFT: endless repetition of decision icons, human figure straining — red X. RIGHT: one decision point, then automatic, then nothing — green arrow forward.",
 "Wide diagram shot","Flat white",
 "The precise reframe — quantity of decisions, not quality",
 "Two paths: endless decisions X'd vs one structural choice chosen",
 "Arrow to fewer decisions. 3s."),

(78,"IDENTITY CLOSE",
 "Every budgeting system asks him to win the same battle every month.",
 "Wide shot. A year calendar — 12 months. Each month has a small confrontation icon: villain vs Alex, same fight, month after month. A count builds in the corner: 12. Then 120. Then 360.",
 "Wide shot","Flat white",
 "The repetition made visible — the burden of monthly willpower",
 "Calendar with 12 confrontation icons per year; count building",
 "Battle icons fill calendar; counter climbs. 2s."),

(79,"IDENTITY CLOSE",
 "The standing order asks him to win it once.",
 "Same calendar — but now 11 months are empty white. Only one month has a setup icon: a green checkmark. Eleven months of silence.",
 "Wide shot","Flat white",
 "The contrast — one setup vs 360 battles",
 "Calendar with only one setup icon; eleven empty months",
 "Eleven empty months; one checkmark. 3s."),

(80,"IDENTITY CLOSE",
 "The Reward Trap fires on Friday. But the money is already gone.",
 "Medium shot. The Reward Trap gear fires — triggered by salary notification. It reaches for the €400. The space is empty. A completed transfer line where the money was.",
 "Medium shot","Flat, warm neutral",
 "Trap defeated by prior action, not resistance",
 "Reward Trap reaching; completed transfer line where money was",
 "Trap finds nothing; transfer line visible. 2s."),

(81,"IDENTITY CLOSE",
 "Mental Accounting creates false categories. But there's now one it can never reach.",
 "Wide shot. Mental Accounting's category boxes — SALARY, REWARDS, SPENDING MONEY — all visible to villain. Then one box, separated, slightly out of frame. No path from the labeling machine to it.",
 "Wide shot","Flat white, hidden box distinct",
 "The unreachable category — outside the system's jurisdiction",
 "Villain labeling visible boxes; unreachable box apart",
 "Unreachable box dim but distinct. 2s."),

(82,"IDENTITY CLOSE",
 "Present Bias says Future Alex will be responsible. And this time — he already was.",
 "Wide shot. Present Bias deferral signal heading to Future Alex. But Past Alex (Sunday, calm, transfer confirmed) holds up a checkmark. Future Alex receives empty responsibility — nothing to do.",
 "Wide shot","Flat, warm gradient",
 "The pattern broken — past handled what present deferred",
 "Past Alex checkmark; Future Alex receiving empty signal",
 "Past Alex checkmark bold; Future Alex empty hands. 3s."),

(83,"IDENTITY CLOSE",
 "The programs are not broken.",
 "Wide shot. Three trap gears — but their labels change from trap names to their original evolutionary functions: MOTIVATION SYSTEM, CATEGORIZATION SYSTEM, IMMEDIATE THREAT RESPONSE. Clean and neutral.",
 "Wide shot","Flat white",
 "The reframe — programs as tools, not villains",
 "Three gears relabeled with original evolutionary functions",
 "New labels replace trap labels. 2s."),

(84,"IDENTITY CLOSE",
 "They are perfectly designed for an environment where saving made no survival sense.",
 "Wide split shot. LEFT: sparse ancient landscape — immediate threats, no storage infrastructure. A figure surviving day to day. RIGHT: modern Alex — salary, bank account, compound interest. Same programs. Completely different world.",
 "Wide split shot","Warm earthy tones left, clean modern white right",
 "The mismatch — programs built for a world that no longer exists",
 "Ancient survival left; modern Alex right; same programs, different world",
 "Split environments clear. 3s."),

(85,"IDENTITY CLOSE",
 "The standing order is the first system Alex has ever used that was built for his world — not theirs.",
 "Wide split panel. LEFT: ancient environment (spending immediately was survival). RIGHT: modern Alex with standing order running — built for compound interest, salary cycles, future self. Same brain. Different architecture.",
 "Wide split panel","Earthy left, modern clean right",
 "Resolution — a system that matches the actual environment",
 "Ancient world left; modern standing order right",
 "Split clear; contrast prominent. 3s."),

# ══════════════════════════════════════════════════════════════════════════════
# GUIDE — next video teaser
# ══════════════════════════════════════════════════════════════════════════════

(86,"GUIDE",
 "Next video: Alex gets a tax refund. Eight hundred euros he didn't expect.",
 "Medium shot. Alex's phone shows a NEW notification — different color from the salary notification, different energy: TAX REFUND RECEIVED — 800. Alex's expression: something is different. Villain activates with a different, faster pattern.",
 "Medium shot","Flat, warm; notification different color from salary",
 "Teaser — same trap in unexpected clothing",
 "New notification distinct; villain different activation pattern",
 "Notification distinct; villain different response. 2s."),

(87,"GUIDE",
 "His brain treats it completely differently from every euro he ever earned.",
 "Close-up inside skull. Villain's response to the tax refund: visibly faster, larger, more urgent than the salary response. Different trigger. Different speed.",
 "Close-up, skull interior","Warm interior, faster villain pattern",
 "Found money triggers differently than earned money",
 "Villain faster and more urgent for refund than for salary",
 "Villain response pattern visibly accelerated. 2s."),

(88,"GUIDE",
 "Same trap. Different label. The refund disappears three times faster.",
 "Wide bar chart comparison. LEFT: SALARY spend rate — moderate, spread over days. RIGHT: TAX REFUND (same amount) — spend rate three times faster, consumed in hours. The bars tell the story without words.",
 "Wide chart comparison","Flat white",
 "The quantified difference — same trap, different speed",
 "Salary spend bar vs refund spend bar; refund 3x taller and faster",
 "Both bars visible; contrast dramatic. 3s."),

(89,"GUIDE",
 "And the reason is the one nobody expects.",
 "Wide shot, white background. Three familiar trap icons visible. A fourth element emerges — partially revealed, a question mark covering it. A new label forming but incomplete. Villain gives a slow, reluctant nod. End screen appears in corner.",
 "Wide shot","Flat white, curiosity gap",
 "The open loop — drive the next video",
 "Three familiar traps; fourth partially revealed; villain reluctant nod; end screen",
 "Question mark holds; end screen appears; music fades. 3s."),

]

# ─────────────────────────────────────────────────────────────────────────────
# PDF GENERATION
# ─────────────────────────────────────────────────────────────────────────────

SECTION_COLORS = {
    "HOOK":                    colors.HexColor("#1A1A2E"),
    "THE DEMONSTRATION":       colors.HexColor("#16213E"),
    "WHY KNOWING ISN'T ENOUGH":colors.HexColor("#0F3460"),
    "WHY WILLPOWER FAILS":     colors.HexColor("#533483"),
    "THE DECISION":            colors.HexColor("#1B5E20"),
    "CTA":                     colors.HexColor("#E65100"),
    "THE SCIENCE":             colors.HexColor("#1565C0"),
    "BRAIN VILLAIN'S LAST TRICK": colors.HexColor("#B71C1C"),
    "IDENTITY CLOSE":          colors.HexColor("#2E7D32"),
    "GUIDE":                   colors.HexColor("#4A148C"),
}

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=15*mm, leftMargin=15*mm,
        topMargin=20*mm, bottomMargin=20*mm
    )

    styles = {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold",
                                fontSize=16, textColor=colors.HexColor("#1A1A1A"),
                                alignment=TA_CENTER, spaceAfter=4),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica",
                                   fontSize=10, textColor=colors.HexColor("#555555"),
                                   alignment=TA_CENTER, spaceAfter=2),
        "note": ParagraphStyle("note", fontName="Helvetica-Oblique",
                               fontSize=7.5, textColor=colors.HexColor("#888888"),
                               alignment=TA_CENTER, spaceAfter=12),
        "section": ParagraphStyle("section", fontName="Helvetica-Bold",
                                  fontSize=8.5, textColor=colors.white,
                                  alignment=TA_CENTER),
        "beat_num": ParagraphStyle("beat_num", fontName="Helvetica-Bold",
                                   fontSize=14, textColor=colors.HexColor("#1A1A1A"),
                                   alignment=TA_CENTER),
        "label": ParagraphStyle("label", fontName="Helvetica-Bold",
                                fontSize=7, textColor=colors.HexColor("#777777"),
                                spaceAfter=1),
        "body": ParagraphStyle("body", fontName="Helvetica",
                               fontSize=8.5, textColor=colors.HexColor("#1A1A1A"),
                               leading=12, spaceAfter=0),
        "narration": ParagraphStyle("narration", fontName="Helvetica-BoldOblique",
                                    fontSize=9, textColor=colors.HexColor("#1A1A1A"),
                                    leading=13, spaceAfter=0),
    }

    story = []

    # Title
    story.append(Paragraph("NEUROCENTS · VIDEO 12", styles["title"]))
    story.append(Paragraph("The One Decision That Defeats All Three Brain Traps", styles["subtitle"]))
    story.append(Paragraph(
        "REVISED · 89 beats · ~960 words · ~7.5 min · "
        "New viral hook (30s) + visual-first image prompts",
        styles["note"]
    ))
    story.append(Paragraph(
        "STYLE NOTE — Prepend to every image prompt: "
        "'2D flat cartoon, thick black outlines, clean solid fills, no gradients. "
        "ALEX: beige oval head, glass skull with pink brain villain, black spiky hair, blue t-shirt, gray pants. "
        "Brain villain: pink cartoon brain, heavy-lidded eyes, smirk. "
        "Palette: #F5E6C8 skin, #E8A598 brain, blue shirt, gray pants. 16:9 1280x720.'",
        styles["note"]
    ))
    story.append(HRFlowable(width="100%", thickness=1,
                            color=colors.HexColor("#CCCCCC"), spaceAfter=8))

    current_section = None

    for beat in BEATS:
        (num, section, narration, image_prompt,
         camera, lighting, mood, char_action, video_motion) = beat

        # Section header
        if section != current_section:
            current_section = section
            sec_color = SECTION_COLORS.get(section, colors.HexColor("#333333"))
            sec_table = Table(
                [[Paragraph(f"■■  {section}  ■■", styles["section"])]],
                colWidths=[180*mm]
            )
            sec_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), sec_color),
                ("TOPPADDING",    (0,0), (-1,-1), 5),
                ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ]))
            story.append(Spacer(1, 6))
            story.append(sec_table)
            story.append(Spacer(1, 4))

        # Beat card
        card_data = [
            # Row 0: beat number + narration
            [
                Paragraph(str(num), styles["beat_num"]),
                Paragraph(narration, styles["narration"])
            ],
            # Row 1: image prompt (spans both columns)
            [
                Paragraph("IMAGE PROMPT", styles["label"]),
                Paragraph(image_prompt, styles["body"])
            ],
            # Row 2: camera / lighting / mood
            [
                Paragraph("CAMERA · LIGHTING · MOOD", styles["label"]),
                Paragraph(
                    f"<b>{camera}</b>  |  {lighting}  |  <i>{mood}</i>",
                    styles["body"]
                )
            ],
            # Row 3: character action + video motion
            [
                Paragraph("CHARACTER ACTION", styles["label"]),
                Paragraph(char_action, styles["body"])
            ],
            [
                Paragraph("VIDEO MOTION", styles["label"]),
                Paragraph(video_motion, styles["body"])
            ],
        ]

        card = Table(card_data, colWidths=[28*mm, 152*mm])
        card.setStyle(TableStyle([
            # Outer border
            ("BOX",         (0,0), (-1,-1), 0.5, colors.HexColor("#DDDDDD")),
            ("LINEBELOW",   (0,0), (-1, 0), 0.5, colors.HexColor("#EEEEEE")),
            ("LINEBELOW",   (0,1), (-1, 1), 0.3, colors.HexColor("#F0F0F0")),
            ("LINEBELOW",   (0,2), (-1, 2), 0.3, colors.HexColor("#F0F0F0")),
            ("LINEBELOW",   (0,3), (-1, 3), 0.3, colors.HexColor("#F0F0F0")),
            # Row 0 background (beat number + narration)
            ("BACKGROUND",  (0,0), (-1, 0), colors.HexColor("#F7F7F7")),
            # Padding
            ("TOPPADDING",    (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING",   (0,0), (-1,-1), 6),
            ("RIGHTPADDING",  (0,0), (-1,-1), 6),
            ("VALIGN",        (0,0), (-1,-1), "TOP"),
            ("VALIGN",        (0,0), (0, 0), "MIDDLE"),
        ]))

        story.append(KeepTogether([card, Spacer(1, 5)]))

    doc.build(story)
    print(f"✅  PDF generated: {filename}")
    print(f"    {len(BEATS)} beats across {len(set(b[1] for b in BEATS))} sections")


if __name__ == "__main__":
    build_pdf("/home/user/Claudeeee/V12_revised_production.pdf")
