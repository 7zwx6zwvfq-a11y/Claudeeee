from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

beats = [
    (1, "Medium shot", "Warm amber desk light", "Relief — a familiar Friday ritual", "Alex reading salary notification; brain perks up", "Hard cut in. No logo, no fade. Phone notification glows. 2s."),
    (2, "Close-up, screen", "Flat, phone glow", "Routine confirmed — baseline established", "3,200 on screen; brain arms crossed contentedly", "Static. Number holds; label fades in below. 2s."),
    (3, "Close-up, screen", "Flat, dim evening light", "Familiar confusion — not alarm, just pattern", "1,980 on screen; Alex confused, not panicked", "Cut. New timestamp. Balance lower. 2s."),
    (4, "Wide shot", "Flat, white", "Elimination — the mystery deepens", "House and bill icons with red X marks; NOT THESE label", "Static. Icons appear; X marks draw through each. 2s."),
    (5, "Medium shot", "Warm ambient interior", "Smugness — the villain satisfied", "Brain Villain satisfied; Alex's thought bubble of small rewards", "Static. Brain Villain's expression holds; thought bubble icons glow. 2s."),
    (6, "Medium shot, slight camera address", "Flat, white", "Pivot — something important is about to land", "Alex turning toward camera; brain leaning forward", "Static. Background fades to white; Alex turns. 2s."),
    (7, "Wide shot", "Flat, white", "Reframe — the premise flipped immediately", "NOT A MATH PROBLEM in bold; math equation crossed out", "Static. Text drops in; X draws through equation. 2s."),
    (8, "Medium shot", "Flat, warm neutral", "Competence established — the problem is elsewhere", "Alex at whiteboard with correct math; brain thumbs-up", "Static. Whiteboard content present; brain holds thumbs-up. 2s."),
    (9, "Wide split panel", "Dual tone: blue left, amber right", "The distinction made visual", "Numbers left vs feelings right; brain character on feelings side", "Static. Split appears; brain migrates to feelings side. 3s."),
    (10, "Wide shot", "Flat, white", "Revelation building — three, not random", "Brain Villain raising three fingers, each glowing in sequence", "Static. Fingers raise one by one; each glows briefly. 3s."),
    (11, "Wide shot, sepia", "Soft sepia tones", "Origin — the programs predate awareness", "Young Alex silhouette; three program icons forming above", "Static. Sepia scene holds; program icons appear. 2s."),
    (12, "Wide timeline shot", "Flat, white", "Scale — evolutionary, not personal", "Evolution timeline; three trap icons persisting through history", "Static. Timeline populates left to right; traps appear early. 3s."),
    (13, "Close-up, phone + brain", "Flat, phone glow", "Automaticity — no choice involved", "Salary notification fires; three brain traps light up simultaneously", "Static. All three icons illuminate at the moment of notification. 2s."),
    (14, "Wide shot, void background", "Dark gray, muted", "The outcome — quiet, inevitable", "Alex holding empty wallet; Brain Villain casual beside him", "Static. Empty wallet prominent; Brain Villain relaxed. 2s."),
    (15, "Medium shot, direct address", "Flat, white", "Declaration — the structure announced", "Alex to camera; Brain Villain holding labeled fingers behind", "Static. Numbered fingers present. 2s."),
    (16, "Wide shot", "Flat, white, dimmed Trap 3", "Curiosity gap — Trap 3 sealed", "Three trap icons; Trap 3 locked with padlock and question marks", "Static. Trap 3 lock is prominent; question marks hover. 2s."),
    (17, "Wide shot", "Flat, white", "Open loop sealed — viewer must see Trap 3", "Bold statement; looping spend arrow; Brain Villain nodding", "Static. Statement drops in; loop arrow animates once. 3s."),
    (18, "Title card", "Red background, white text", "Marker — section declared", "Title card: TRAP 1 — THE REWARD TRAP", "Cut in hard. Title holds 1.5s. Cut to scene."),
    (19, "Medium shot", "Warm amber desk light", "The viewer knows what Alex doesn't", "Alex at Friday desk; corner label he doesn't see", "Static. Label appears in corner; Alex looks elsewhere. 2s."),
    (20, "Close-up", "Warm interior light", "Unawareness as the condition for the trap", "Alex's unaware face; Brain Villain nodding behind", "Static. Brain Villain nod is slow and deliberate. 2s."),
    (21, "Wide shot, exterior", "Late afternoon warm light", "The legitimate case for reward — built honestly", "Alex leaving office Friday; tired posture; week-ending body language", "Static. Warm light on Alex; body language clear. 2s."),
    (22, "Medium shot", "Warm interior, end-of-day light", "Legitimacy — the exhaustion is real", "Alex with back pain; completed week calendar; earned exhaustion", "Static. Calendar tasks prominent; Alex's posture communicates cost. 2s."),
    (23, "Close-up, phone", "Phone glow, warm green", "The trigger — clean and immediate", "Phone salary notification glowing green", "Static. Notification text prominent. 2s."),
    (24, "Close-up, skull interior", "Warm interior, brain glow", "The computation begins — before Alex knows it", "Brain snapping to attention inside skull; focused calculation", "Static. Brain posture shifts from passive to active. 2s."),
    (25, "Wide shot", "Flat, white, red X", "The absent question — it never fires", "SAVE question crossed out with red X", "Static. X draws through the question. 2s."),
    (26, "Wide shot", "Flat, white, warm amber highlight", "The active question — the one that runs", "DESERVE question glowing amber; no X", "Static. Amber glow pulses once. 2s."),
    (27, "Medium shot", "Flat, white", "Reframe — blame redirected to mechanism", "Alex and Brain Villain; neuroscience icon between them; label", "Static. Icon and label appear. 2s."),
    (28, "Wide shot, lab", "Cool lab light", "Authority arrives — specific and real", "Schultz figure in lab; brain scan lightboard; name label", "Static. Name label fades in prominently. 2s."),
    (29, "Close-up, centered", "Gold warm glow", "Credibility anchored — the finding is real", "Nobel medal icon glowing; prize label", "Static. Medal glows; label appears. 2s."),
    (30, "Wide diagram shot", "Flat, white, green spike", "The mechanism — counterintuitive and visual", "Timeline; dopamine spike at expectation; flat line at arrival", "Static. Spike appears at expectation point; flat at arrival. 3s."),
    (31, "Medium shot", "Flat, neutral", "The sequence reversed — feeling preceded the event", "Alex with salary notification; flat post-dopamine expression", "Static. Alex's expression: already past the peak. 2s."),
    (32, "Close-up, thought bubble", "Warm thought-bubble glow", "The spend happened mentally first", "Alex's thought bubble with glowing imagined purchases", "Static. Thought bubble items glow warmly. 2s."),
    (33, "Wide diagram shot", "Flat, white, orange brain highlight", "Timing is the mechanism", "Brain reward center glowing; BEFORE SPENDING arrow; unchanged balance", "Static. Brain region glows; arrow and unchanged balance both visible. 3s."),
    (34, "Close-up, receipt", "Warm restaurant light", "The specific cost — not dramatic, just real", "Restaurant receipt; 85.00 line; REWARD label", "Static. Receipt crisp; label present. 2s."),
    (35, "Wide shot", "Flat, white", "Accumulation — three becomes a pattern", "Three justified purchase items in a row; all labeled REWARD", "Static. Items appear in sequence. 2s."),
    (36, "Wide shot", "Flat, white", "The trap's logic — internally consistent", "Three items with justification labels; Brain Villain ticking notepad", "Static. Labels appear under each item; Brain Villain nods. 3s."),
    (37, "Medium shot", "Flat, warm neutral", "Competence of the trap — it is working as designed", "Brain Villain at desk reviewing notepad; professional satisfaction", "Static. Brain Villain reviews; expression: satisfied and precise. 2s."),
    (38, "Wide diagram shot", "Flat, white", "The reclassification — optional became necessary", "Two columns; rewards in NECESSARY column; OPTIONAL column empty", "Static. Reward icons in necessary column; contrast clear. 3s."),
    (39, "Wide shot", "Flat, white", "The internal logic — balanced and self-defeating", "Balance scale: effort vs rewards; perfectly balanced", "Static. Scale sits in balance. 2s."),
    (40, "Medium shot", "Flat, warm neutral", "Escalation announced — the trap deepens", "Brain Villain turning page; smirk signaling escalation", "Static. Page turn deliberate; smirk held. 2s."),
    (41, "Wide shot, academic", "Warm academic light", "Authority — long-term observation, not theory", "Frank figure before 30-year graph; name and institution label", "Static. Label prominent; graph behind him. 2s."),
    (42, "Wide diagram shot", "Flat, white", "The mechanism named — visual and clear", "Line graph rising after each reward; HEDONIC ADAPTATION label", "Static. Graph builds left to right; baseline rises after each event. 3s."),
    (43, "Close-up, graph", "Flat, white", "The mechanism in detail — one reset, one rise", "Baseline rising after reward; NEW BASELINE label", "Static. Baseline arrow moves up; label appears. 2s."),
    (44, "Medium shot", "Warm restaurant light", "Normalization — the treat has become ordinary", "Alex at restaurant; 85-euro bill; expression of normalcy, not pleasure", "Static. Bill on table; Alex's flat expression. 2s."),
    (45, "Medium shot", "Warm desk light", "Threshold risen — what satisfied now falls short", "Alex with salary; brain unimpressed by 85-euro benchmark", "Static. Brain expression: underwhelmed. 2s."),
    (46, "Wide shot", "Flat, white", "The ratchet visible — floor has risen", "Dinner icon at bottom labeled FLOOR; new reward levels above", "Static. Stack structure clear; FLOOR label prominent. 2s."),
    (47, "Wide diagram shot", "Flat, white", "The compounding cost — the trap's real damage", "Monthly bar chart growing steadily; compounding cost label", "Static. Bars grow month by month; label appears. 3s."),
    (48, "Close-up, skull interior", "Dim interior, tiny glow", "Partial awareness — not enough", "Tiny awareness icon dimly glowing in brain corner", "Static. Awareness icon dim but present. 2s."),
    (49, "Medium shot", "Flat, warm neutral", "False confidence — the setup for Trap 2", "Alex confident; Trap 2 icon in background; mistaken satisfaction", "Static. Alex's confident expression contrasts with unbeaten Trap 2 icon. 2s."),
    (50, "Medium shot, direct address", "Flat, white", "Direct — no pressure, just invitation", "Alex to camera; Brain Villain frozen behind him", "Static. Brain Villain freeze is deliberate. 2s."),
    (51, "Medium shot, cut back", "Flat, white", "Brevity — the CTA earns nothing it doesn't need", "Brain Villain rolling eyes; Alex turning back; hard cut to Trap 2", "Brain Villain eye roll; hard cut. 3s total from CTA start."),
    (52, "Title card", "Red background, white text", "Marker — section declared", "Title card: TRAP 2 — THE SAFE MONEY ILLUSION", "Cut in hard. Title holds 1.5s. Cut to scene."),
    (53, "Medium shot", "Warm interior light, gold label", "Pride before the reveal", "Alex at laptop; RESPONSIBLE label floating above", "Static. Label appears; Alex's expression: satisfied. 2s."),
    (54, "Close-up, screen", "Flat, screen glow, green border", "The safety net — looks responsible", "Savings account screen showing 2,000 with green border and padlock", "Static. Screen crisp; padlock prominent. 2s."),
    (55, "Medium shot", "Flat, warm neutral", "Emotional attachment to the label", "Alex tapping padlock; Brain Villain watching with quiet interest", "Static. Padlock tap deliberate. 2s."),
    (56, "Close-up, screen", "Flat, screen glow, red border", "Contrast — the other account revealed", "Credit card balance showing -1,800 with red border", "Static. Red border present but less prominent than savings. 2s."),
    (57, "Close-up", "Flat, red emphasis", "The mechanism of the trap — specific and real", "23% APR label bold on credit card; Brain Villain approving", "Static. 23% label is large and prominent. 2s."),
    (58, "Wide diagram shot", "Flat, white, red counter", "The cost named — unavoidable arithmetic", "Interest calculation shown; 414 euros per year label in red", "Static. Calculation appears; counter holds. 3s."),
    (59, "Wide diagram shot", "Flat, white, pale green vs red", "The asymmetry — visual and mathematical", "Savings return calculation: 32/year in pale green; contrast with 414 in red", "Static. Both lines visible; contrast clear. 3s."),
    (60, "Wide shot", "Flat, white, red box", "The damage named — annual, compounding", "NET LOSS 382/YEAR in bold red box; Brain Villain circling it", "Static. Red box prominent; Brain Villain's circle deliberate. 2s."),
    (61, "Medium shot", "Flat, warm neutral", "Reframe begins — not stupidity", "Alex reading finance book; competent expression", "Static. Book and expression establish competence. 2s."),
    (62, "Wide shot", "Flat, white", "The wall is the mechanism — same money, divided", "Two equal piles separated by Brain Villain's wall; different labels", "Static. Brain Villain draws wall between identical piles. 3s."),
    (63, "Wide shot", "Flat, white", "Named — the bias gets its title", "MENTAL ACCOUNTING bold label; simple definition below", "Static. Label and definition appear. 2s."),
    (64, "Wide shot, academic", "Warm academic light", "Authority — the highest credential in economics", "Thaler figure; Nobel and institution labels", "Static. Labels prominent and accurate. 2s."),
    (65, "Wide shot", "Flat, white, red X on equals", "The finding stated — clean and confrontational", "MONEY = MONEY equation with X through equals; finding declared", "Static. X draws through equation. 2s."),
    (66, "Wide diagram shot", "Flat, white", "The structure of mental accounting made visible", "Money sorted into labeled category boxes; each treated differently", "Static. Category boxes appear; money sorted into each. 3s."),
    (67, "Close-up", "Warm green glow", "The label creates the feeling — safety", "Green EMERGENCY box; 2,000 inside; warm glow and padlock", "Static. Green glow warm and protective. 2s."),
    (68, "Close-up", "Cool red light", "Same amount, opposite feeling — the trap", "Red DEBT PAYMENT box; 2,000 inside; cold light, no padlock", "Static. Cold light contrasts with previous warmth. 2s."),
    (69, "Wide shot", "Flat, white", "The contradiction stated — brain vs math", "Green and red boxes side by side with equals sign between them", "Static. Equals sign prominent between boxes. 2s."),
    (70, "Wide shot, space metaphor", "Dark space background, two planet tones", "The felt distance — enormous despite math", "Green and red planets; equals sign floating between; vast separation", "Static. Planets separated; equals sign still visible between them. 3s."),
    (71, "Medium shot", "Flat, warm neutral", "The villain's preference — because it's disguised", "Brain Villain approving of EMERGENCY box; genuine appreciation", "Static. Appreciation expression genuine, not ironic. 2s."),
    (72, "Medium shot", "Flat, warm neutral", "The trap's camouflage — genuine virtue hiding the cost", "Alex with proud padlock expression; genuine discipline on display", "Static. Expression real; trap still running. 2s."),
    (73, "Wide shot", "Flat, white", "Cost and pride in the same frame — the juxtaposition is the point", "Alex's proud expression; NET LOSS box visible beneath; Brain Villain watching", "Static. Both elements in frame simultaneously. 3s."),
    (74, "Medium shot", "Flat, warm, gold accents", "The disguise — virtue as camouflage", "Trap with velvet rope and RESPONSIBLE BEHAVIOR gold plaque", "Static. Disguise complete; trap unrecognizable. 2s."),
    (75, "Close-up", "Warm gold glow", "Virtue halo — the final layer of disguise", "Brain Villain placing golden halo over savings trap", "Static. Halo glows; Brain Villain's placement deliberate. 2s."),
    (76, "Medium shot", "Flat, warm neutral", "Name drop — seed planted for next video", "Tax refund notification; Brain Villain lighting up; same trap posture", "Static. Brain Villain's recognition is immediate. 2s."),
    (77, "Wide shot", "Flat, white", "The specific cost of the next trap — curiosity gap", "Salary spend rate vs tax refund spend rate; stark difference", "Static. Bars compare clearly. 2s."),
    (78, "Wide triptych", "Flat, white", "Pattern stated — the trap is structural, not situational", "Triptych showing same Mental Accounting mechanism across contexts", "Static. Middle column identical in both rows. 2s."),
    (79, "Medium shot", "Flat, shifting tone", "Anticipation — even the villain respects Trap Three", "Brain Villain turning toward Trap 3; subtle shift in expression", "Static. Expression shift is deliberate. 2s."),
    (80, "Wide shot", "Flat, white", "Architecture revealed — Trap 3 is the foundation", "Trap 1 and 2 icons sitting on Trap 3 foundation layer", "Static. Foundation relationship clear; Trap 3 carries the others. 3s."),
    (81, "Title card", "Deep red background, white text", "Weight — the biggest trap gets more space", "Title card: TRAP 3 — THE FUTURE IS FAKE", "Cut in hard. Title holds 2s. Cut to scene."),
    (82, "Wide shot", "Flat, white", "Distinction — this trap operates differently", "Trap 1 and 2 with dollar signs; Trap 3 without — different category", "Static. Contrast in trap icon types. 2s."),
    (83, "Close-up, diagram", "Flat, white", "Category shift — psychology not spending", "Perception diagram; PERCEPTION PROBLEM label", "Static. Diagram clean and clear. 2s."),
    (84, "Wide shot, fork in road", "Flat, warm neutral", "The choice — simple and immediate", "Road fork; Alex looking at LEFT path: 100 TODAY", "Static. Left path option prominent. 2s."),
    (85, "Wide shot, fork", "Flat, warm neutral", "The irrational preference — about to be shown", "Right path: 110 IN 1 WEEK; Alex already leaning left despite math", "Static. Both paths visible; Alex's lean is deliberate. 2s."),
    (86, "Wide shot", "Flat, warm neutral", "Universal — not an individual weakness", "Alex walking left; ALMOST EVERYONE label; empty right path", "Static. Empty right path emphasizes universality. 2s."),
    (87, "Wide shot, new fork", "Flat, slightly cooler — distance implied", "Same math, different felt reality", "New fork; LEFT path: 100 IN 52 WEEKS; Alex looking neutrally", "Static. Same fork structure; different time labels. 2s."),
    (88, "Wide shot", "Flat, cool neutral", "The patience is available — when distant", "Right path: 110 IN 53 WEEKS; Alex considering", "Static. Both paths visible; Alex's posture: considering. 2s."),
    (89, "Wide shot", "Flat, warm neutral", "The irrationality exposed — identical math, inverted choice", "Alex walking right; SAME TRADE / DIFFERENT PSYCHOLOGY labels", "Static. Both labels prominent; contrast stated plainly. 3s."),
    (90, "Wide split diagram", "Flat, white", "The gap between math and psychology — made visual", "Math equivalence left; felt weight asymmetry right", "Static. Split diagram holds; contrast clear. 3s."),
    (91, "Wide shot, academic", "Warm academic light", "Authority — Harvard behavioral economics", "Laibson figure; Harvard label; behavioral diagram behind", "Static. Name and institution label prominent. 2s."),
    (92, "Wide shot", "Flat, academic warm light", "Rigor — decades of verification", "Research timeline behind Laibson; decades of data points", "Static. Timeline populated left to right. 2s."),
    (93, "Wide diagram shot", "Flat, white", "The curve — non-linear, not rational", "Hyperbolic discount curve; steep near peak; flat long-term; label", "Static. Curve draws left to right; steepness contrast clear. 3s."),
    (94, "Wide shot", "Flat, white with fade effect at distance", "Felt reality as a function of distance", "Three objects at increasing distance; reality fading with distance", "Static. Fade gradient clear; label present. 3s."),
    (95, "Wide shot, split panels", "Flat, white", "The precise definition — importance vs reality", "Split: NOT LESS IMPORTANT / LESS REAL; Brain Villain in right panel", "Static. Brain Villain's point deliberate. 2s."),
    (96, "Wide shot", "Slightly cooler tones for Future Alex", "Future Alex introduced — specific and real", "Future Alex character with retirement document; slight age indicators", "Static. Future Alex distinct but recognizable as Alex. 2s."),
    (97, "Wide shot", "Flat, cooler tones", "The specificity of Future Alex's burden", "Future Alex surrounded by future bills; holding them", "Static. Bills numerous and specific. 2s."),
    (98, "Wide shot", "Flat, white, consequence chain", "The chain — connecting present choices to future reality", "Consequence chain: present choices to Future Alex; chain visible", "Static. Chain connects across frame. 3s."),
    (99, "Medium shot", "Flat, white, gap between characters", "The estrangement — the key emotion of the trap", "Present and Future Alex facing each other across gap; stranger dynamic", "Static. Gap between them prominent; expressions contrast. 3s."),
    (100, "Wide shot", "Flat, white", "The behavioral consequence — not cruelty, just psychology", "Bold statement; Present Alex turning away from Future Alex", "Static. Turn deliberate; statement holds. 2s."),
    (101, "Medium shot", "Flat, warm present tones", "The trap's internal logic — not stupidity", "Present Alex confident; internally consistent present-moment decisions", "Static. Expression: completely reasonable. 2s."),
    (102, "Medium shot", "Flat, warm neutral", "Connection — Trap 3 enabling Trap 1", "Dinner receipt with Trap 1 icon arrow; connection visible", "Static. Arrow connection clear. 2s."),
    (103, "Medium shot", "Flat, warm neutral", "Connection — Trap 3 enabling Trap 2", "Savings/debt boxes with Trap 2 icon arrow; same connection", "Static. Arrow connection clear. 2s."),
    (104, "Medium shot", "Flat, neutral tones", "The recurring delay — never arrives", "Calendar with empty savings columns; Alex flipping forward month by month", "Static. Pattern of empty columns clear. 2s."),
    (105, "Wide shot", "Slightly faded distance tones", "The perpetual delay — almost arriving, never here", "Future Alex waving from permanent distance; never approaching", "Static. Distance maintained; Future Alex's wave held. 3s."),
    (106, "Wide diagram shot", "Flat, tech-referential white", "Architecture stated — Trap 3 is foundational", "OS boot screen: PRESENT BIAS; two app icons loading beneath", "Static. Boot sequence completes; app icons appear. 3s."),
    (107, "Wide shot", "Flat, tech-metaphor white", "The dependency structure — OS and apps", "Present Bias OS; Reward Trap and Mental Accounting apps open on top", "Static. Dependency structure clear; apps sit on OS layer. 3s."),
    (108, "Wide shot", "Flat, academic white", "Evidence arrives — specific and datable", "Journal cover: 2024 issue; label prominent", "Static. Journal cover clean and specific. 2s."),
    (109, "Wide shot", "Flat, white", "Scale — 14,000 is meaningful", "Grid of 14,000 participant icons; scale communicated", "Static. Grid fills frame systematically. 2s."),
    (110, "Wide shot", "Flat, warm neutral", "The intervention — identity continuity", "Present and Future Alex overlapping; same face emerging", "Static. Overlap deliberate; same-person recognition visible. 3s."),
    (111, "Wide diagram shot", "Flat, white, green 23% bar", "The result — measurable and specific", "Comparison bars; future-self group 23% higher; label prominent", "Static. 23% difference prominent. 3s."),
    (112, "Wide shot", "Flat, white", "Simplicity of the finding — one thing changed one outcome", "Three crossed-out interventions; ZERO ADDITIONAL INTERVENTION label", "Static. Crossed-out items clear; label emphatic. 2s."),
    (113, "Wide shot", "Flat, white, red X marks", "What was NOT needed — the reframe", "App and advisor icons; bold red X marks; not the answer", "Static. X marks clear. 2s."),
    (114, "Wide shot", "Flat, warm neutral", "The resolution — same person, same stake", "Present and Future Alex identical side by side; gap closed", "Static. Identical figures; no gap. 3s."),
    (115, "Wide shot", "Flat, white", "The system assembled — three gears locking", "Three separate gear icons locking together; system forming", "Animated. Gears float; connect; begin spinning together. 3s."),
    (116, "Wide shot", "Flat, warm Friday tones", "Gear 1 active — the first mechanism", "REWARD TRAP gear spinning; salary notification visible", "Static. Gear 1 spinning; notification connected. 2s."),
    (117, "Wide shot", "Flat, white", "OS enabling Trap 1 — the dependency shown", "PRESENT BIAS gear enabling REWARD TRAP gear; permission signal", "Static. Gear connection and permission signal visible. 2s."),
    (118, "Wide shot", "Flat, white", "Gear 2 active — maintaining the separation", "MENTAL ACCOUNTING gear spinning; savings and debt boxes separated", "Static. Gear 2 maintains wall between boxes. 2s."),
    (119, "Wide shot", "Flat, white", "The combined effect — total damage hidden by the system", "All three gears; hidden damage counter; wall obscuring total", "Static. Counter running; wall obscuring it. 3s."),
    (120, "Wide shot", "Flat, white", "Interdependence — the system is fragile if broken correctly", "One gear removed; other two slowing; coordination lost", "Static. System degrading without one gear. 3s."),
    (121, "Wide shot", "Flat, white", "Scalability — the trap grows with income", "All three gears; income counter rising; constant percentage consumed", "Static. Income rises; percentage line stays flat. 3s."),
    (122, "Wide shot, academic", "Warm academic light", "Two Nobel-level authorities — the finding is credible", "Kahneman and Deaton figures; Princeton label; 2010 study", "Static. Both names and institution prominent. 2s."),
    (123, "Wide diagram shot", "Flat, white", "The finding — income does not fix the system", "Income vs behavior graph; flat line above threshold", "Static. Threshold visible; flat line above it. 3s."),
    (124, "Close-up, graph", "Flat, white", "The precise implication — income is not the solution", "Flat behavior line labeled UNCHANGED; system still consuming", "Static. UNCHANGED label prominent. 2s."),
    (125, "Wide diagram shot", "Flat, white", "The proportional trap — percentage is constant", "Pie chart growing; behavioral trap slice constant percentage", "Static. Pie grows; trap slice proportion unchanged. 3s."),
    (126, "Wide shot", "Flat, white", "Scale independence — the traps don't care about salary", "Two Alex versions: 50K and 150K; same Brain Villain and gears beside each", "Static. Both versions identical except salary label. 2s."),
    (127, "Wide diagram shot", "Flat, white", "Proportionality confirmed — the system self-adjusts", "Two pie charts; trap slice identical percentage in both", "Static. Both pies; same trap slice angle. 2s."),
    (128, "Wide shot", "Flat, white", "The system reframe — income is input, system is the variable", "Income arrow entering gear system; processed; same output proportion", "Static. System processes income; label appears. 3s."),
    (129, "Medium shot", "Flat, warm neutral", "Identity reframe begins — from failure to awareness", "Alex calm; gears visible behind him; awareness not blame", "Static. Expression: calm self-recognition, not shame. 2s."),
    (130, "Wide shot", "Flat, warm sepia-to-present gradient", "Evolutionary origin — protection, not sabotage", "Evolution timeline; traps appearing early; protection function labeled", "Static. Timeline shows protection origin. 2s."),
    (131, "Wide shot, ancestor context", "Warm earthy tones", "Original function — the trap was adaptive", "Ancestor figure with functional reward signal after hunt", "Static. Reward signal in correct evolutionary context. 2s."),
    (132, "Wide shot, ancestor context", "Warm earthy tones", "Adaptive context — categorization was survival", "Ancestor with safe/poison piles; categorical thinking as survival", "Static. Categorization in survival context. 2s."),
    (133, "Wide shot, ancestor context", "Warm earthy tones", "Present bias was survival logic — not a flaw", "Ancestor handling immediate predator; future threat distant and vague", "Static. Immediate threat prominent; future threat faded. 3s."),
    (134, "Wide shot", "Flat, white", "Reframe complete — the programs work, the context changed", "Three gears with original function labels; NOT BROKEN label", "Static. Function labels replace trap labels. 2s."),
    (135, "Wide split shot", "Earthy left, modern white right", "The mismatch is structural — not personal", "Ancient environment left; modern world right; MISMATCH arrow", "Static. Split environments; mismatch arrow prominent. 3s."),
    (136, "Medium shot", "Flat, warm neutral", "Honest — awareness is not a cure", "Alex seeing gears clearly; gears still spinning; awareness not stopping them", "Static. Gears still active; Alex's seeing them now is new. 2s."),
    (137, "Medium shot", "Flat, warm neutral", "The villain's position — named but not defeated", "Brain Villain with nameplate; shrug; still present but seen", "Static. Shrug is not defiant — more resigned. 2s."),
    (138, "Wide shot", "Flat, warm neutral", "The shift — from unconscious to conscious", "Alex watching Brain Villain instead of being led; dynamic changed", "Static. Posture shift clear; awareness visible. 2s."),
    (139, "Medium shot", "Flat, warm neutral", "The release — the most important reframe", "Alex with weight lifting; clarity expression; not dramatic relief", "Static. Weight visible as it lifts; expression: quiet clarity. 3s."),
    (140, "Wide shot", "Flat, warm white", "First condition — practical and achievable", "First staircase step labeled; more steps above; beginning visible", "Static. First step prominent; steps above present but unlabeled. 2s."),
    (141, "Wide shot", "Flat, white, red X", "What the solution is NOT — important clarity", "Budget icon crossed out; clear X", "Static. X draws through budget icon. 2s."),
    (142, "Wide shot", "Flat, white", "The promise — one intervention, three effects", "Single key icon; three trap lock icons; ONE DECISION THREE LOCKS label", "Static. End screen card appearing in corner. 3s."),
    (143, "Medium shot, direct address", "Flat, white, end screen visible", "Guide — explicit and named", "Alex to camera; end screen card fully visible", "Static. End screen card prominent. 2s."),
    (144, "Wide shot", "Flat, white", "Final gap — why don't most people make this decision?", "Crowd icons; most walking past the key; few stopping", "Static. Crowd behavior visible; gap planted. 2s."),
    (145, "Wide shot", "Flat, warm fade", "Final seed — curiosity gap for next video", "Three traps; one key; Brain Villain reluctant nod; fade beginning", "Music fades. Brain Villain nod is deliberate and final. 3s."),
]

doc = SimpleDocTemplate(
    "/home/user/Claudeeee/V11_beats_prompts.pdf",
    pagesize=A4,
    leftMargin=1.5*cm,
    rightMargin=1.5*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'Title',
    parent=styles['Normal'],
    fontSize=14,
    fontName='Helvetica-Bold',
    spaceAfter=4,
    textColor=colors.HexColor('#1a1a1a')
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=9,
    fontName='Helvetica',
    spaceAfter=16,
    textColor=colors.HexColor('#555555')
)

beat_title_style = ParagraphStyle(
    'BeatTitle',
    parent=styles['Normal'],
    fontSize=9,
    fontName='Helvetica-Bold',
    spaceBefore=8,
    spaceAfter=2,
    textColor=colors.HexColor('#cc0000')
)

field_style = ParagraphStyle(
    'Field',
    parent=styles['Normal'],
    fontSize=8.5,
    fontName='Helvetica',
    spaceAfter=1,
    leftIndent=8,
    textColor=colors.HexColor('#1a1a1a'),
    leading=12
)

section_style = ParagraphStyle(
    'Section',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Helvetica-Bold',
    spaceBefore=14,
    spaceAfter=4,
    textColor=colors.HexColor('#ffffff'),
    backColor=colors.HexColor('#333333'),
    leftIndent=0,
    borderPad=4
)

story = []

story.append(Paragraph("NEUROCENTS — VIDEO 11", title_style))
story.append(Paragraph("3 Traps That Rewire Your Brain to Stay Broke — 145 beats · Video prompts", subtitle_style))

sections = {
    1: "HOOK (beats 1–17)",
    18: "TRAP 1 — THE REWARD TRAP (beats 18–49)",
    50: "CTA (beats 50–51)",
    52: "TRAP 2 — THE SAFE MONEY ILLUSION (beats 52–80)",
    81: "TRAP 3 — THE FUTURE IS FAKE (beats 81–114)",
    115: "SYSTEM CLOSE (beats 115–128)",
    129: "IDENTITY CLOSE + GUIDE (beats 129–145)",
}

for beat_num, camera, lighting, mood, character, motion in beats:
    if beat_num in sections:
        story.append(Paragraph(f"  {sections[beat_num]}  ", section_style))

    story.append(Paragraph(f"BEAT {beat_num}", beat_title_style))
    story.append(Paragraph(f"<b>Camera:</b> {camera}", field_style))
    story.append(Paragraph(f"<b>Lighting:</b> {lighting}", field_style))
    story.append(Paragraph(f"<b>Mood:</b> {mood}", field_style))
    story.append(Paragraph(f"<b>Character Action:</b> {character}", field_style))
    story.append(Paragraph(f"<b>Video Motion:</b> {motion}", field_style))

doc.build(story)
print("PDF generated: V11_beats_prompts.pdf")
