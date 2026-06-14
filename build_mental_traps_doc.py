#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'3 Traps That Rewire Your Brain to Stay Broke' (Video 11 — Reward Trap / Mental Accounting / Present Bias)."""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

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

("Alex checked his bank account on Friday.",
 "Medium shot, warm desk interior. Alex sits at his desk, Friday evening. He holds his phone — screen shows bold green text: 'SALARY RECEIVED — 3,200.' His expression relaxes. The pink brain inside his skull perks up, smug.",
 "Medium shot", "Warm amber desk light", "Relief — a familiar Friday ritual",
 "Alex reading salary notification; brain perks up",
 "Hard cut in. No logo, no fade. Phone notification glows. 2s."),

("Three thousand two hundred arrived — same as last month.",
 "Close-up of the phone screen. The number 3,200 is large, centered, green. A small bold label below: 'SAME AS LAST MONTH.' The brain inside Alex's skull crosses its arms contentedly.",
 "Close-up, screen", "Flat, phone glow", "Routine confirmed — baseline established",
 "3,200 on screen; brain arms crossed contentedly",
 "Static. Number holds; label fades in below. 2s."),

("By Sunday, twelve hundred of it was already gone.",
 "Close-up of same phone. Now Sunday 9pm. The balance reads 1,980. Bold text appears: 'SUNDAY 9PM.' Alex's expression shifts — not panicked, just confused. He's seen this before.",
 "Close-up, screen", "Flat, dim evening light", "Familiar confusion — not alarm, just pattern",
 "1,980 on screen; Alex confused, not panicked",
 "Cut. New timestamp. Balance lower. 2s."),

("Not on rent. Not on bills.",
 "Wide shot, white background. Two icons — a house (RENT) and a utility symbol (BILLS) — each crossed out with a bold red X. Label: 'NOT THESE.' Clean and declarative.",
 "Wide shot", "Flat, white", "Elimination — the mystery deepens",
 "House and bill icons with red X marks; NOT THESE label",
 "Static. Icons appear; X marks draw through each. 2s."),

("On things his brain convinced him he deserved.",
 "Medium shot. The Brain Villain stands in the lower-right corner of frame, arms crossed, satisfied expression. A thought bubble above Alex's head shows small icons: dinner plate, shopping bag, subscription logo. All mundane. All justified.",
 "Medium shot", "Warm ambient interior", "Smugness — the villain satisfied",
 "Brain Villain satisfied; Alex's thought bubble of small rewards",
 "Static. Brain Villain's expression holds; thought bubble icons glow. 2s."),

("Here's what nobody tells you about money problems:",
 "Medium shot. Alex turns partially toward camera. Expression shifts — from confused to direct. The brain inside his skull leans forward. Background fades to flat white.",
 "Medium shot, slight camera address", "Flat, white", "Pivot — something important is about to land",
 "Alex turning toward camera; brain leaning forward",
 "Static. Background fades to white; Alex turns. 2s."),

("They're not math problems.",
 "Wide shot, white background. Bold text dominates the frame: 'NOT A MATH PROBLEM.' A small math equation (3200 - 1200 = 2000) sits below it, with a red X crossing it out. Not dismissed — just insufficient.",
 "Wide shot", "Flat, white", "Reframe — the premise flipped immediately",
 "NOT A MATH PROBLEM in bold; math equation crossed out",
 "Static. Text drops in; X draws through equation. 2s."),

("Alex isn't bad at math. He knows the difference.",
 "Medium shot of Alex at a whiteboard with simple arithmetic — correct, confident. Beside him, his brain gives a thumbs-up. The math is fine. That's not the issue.",
 "Medium shot", "Flat, warm neutral", "Competence established — the problem is elsewhere",
 "Alex at whiteboard with correct math; brain thumbs-up",
 "Static. Whiteboard content present; brain holds thumbs-up. 2s."),

("But his brain doesn't think in numbers. It thinks in feelings.",
 "Wide split panel. Left: numbers and equations — cold blue tones, logical. Right: emotion icons (satisfaction, relief, desire) — warm amber tones, glowing. The brain character stands in the center, clearly on the right side.",
 "Wide split panel", "Dual tone: blue left, amber right", "The distinction made visual",
 "Numbers left vs feelings right; brain character on feelings side",
 "Static. Split appears; brain migrates to feelings side. 3s."),

("And every payday, it runs three very specific programs.",
 "Wide shot, white background. The Brain Villain stands center frame, holding up three fingers — deliberate, slow. Each finger glows as it rises: one, two, three. Expression: this is planned.",
 "Wide shot", "Flat, white", "Revelation building — three, not random",
 "Brain Villain raising three fingers, each glowing in sequence",
 "Static. Fingers raise one by one; each glows briefly. 3s."),

("Programs that were written before Alex had his first job.",
 "Wide shot, soft sepia tones. A young Alex silhouette stands in a childhood scene — simple house, small figure, early life suggestion. The three program icons float above him, already forming.",
 "Wide shot, sepia", "Soft sepia tones", "Origin — the programs predate awareness",
 "Young Alex silhouette; three program icons forming above",
 "Static. Sepia scene holds; program icons appear. 2s."),

("Three traps — designed by millions of years of evolution —",
 "Wide shot, timeline on white. A long horizontal evolutionary timeline: primitive figure on left, modern Alex on right. Three trap icons sit along the timeline, appearing early and persisting to the present.",
 "Wide timeline shot", "Flat, white", "Scale — evolutionary, not personal",
 "Evolution timeline; three trap icons persisting through history",
 "Static. Timeline populates left to right; traps appear early. 3s."),

("that activate the moment your paycheck hits.",
 "Close-up of Alex's phone — salary notification. Three small trap icons light up simultaneously on the brain inside Alex's skull. Instant. Automatic. No delay.",
 "Close-up, phone + brain", "Flat, phone glow", "Automaticity — no choice involved",
 "Salary notification fires; three brain traps light up simultaneously",
 "Static. All three icons illuminate at the moment of notification. 2s."),

("And by the time you realize they're running, the money is already gone.",
 "Wide shot, dark gray void. Alex holds an empty wallet open toward the camera. Brain Villain stands to the side, hands in pockets, casual. The traps already ran. Nothing to do now.",
 "Wide shot, void background", "Dark gray, muted", "The outcome — quiet, inevitable",
 "Alex holding empty wallet; Brain Villain casual beside him",
 "Static. Empty wallet prominent; Brain Villain relaxed. 2s."),

("We're going to show you all three.",
 "Medium shot. Alex turns fully to camera. The Brain Villain behind him holds up three fingers again — but this time each finger is labeled: '1', '2', '3'. Expression: we're doing this deliberately.",
 "Medium shot, direct address", "Flat, white", "Declaration — the structure announced",
 "Alex to camera; Brain Villain holding labeled fingers behind",
 "Static. Numbered fingers present. 2s."),

("The third one is the one nobody suspects —",
 "Wide shot. Three trap-door icons in a row. The first two are visible, detailed. The third is locked — a padlock icon, face obscured. Label: 'TRAP 3: ???'",
 "Wide shot", "Flat, white, dimmed Trap 3", "Curiosity gap — Trap 3 sealed",
 "Three trap icons; Trap 3 locked with padlock and question marks",
 "Static. Trap 3 lock is prominent; question marks hover. 2s."),

("because it's not what you spend. It's why you'll never stop.",
 "Wide shot, white background. Bold statement appears: 'NOT WHAT YOU SPEND. WHY YOU NEVER STOP.' A looping arrow icon — spending loop, no exit — sits beneath. The Brain Villain nods slowly.",
 "Wide shot", "Flat, white", "Open loop sealed — viewer must see Trap 3",
 "Bold statement; looping spend arrow; Brain Villain nodding",
 "Static. Statement drops in; loop arrow animates once. 3s."),

# ── TRAP 1 — THE REWARD TRAP ───────────────────────────────────────────────────

("Trap One.",
 "Full-frame title card. Bold red background. White text: 'TRAP 1 — THE REWARD TRAP.' Clean, weighted. Holds.",
 "Title card", "Red background, white text", "Marker — section declared",
 "Title card: TRAP 1 — THE REWARD TRAP",
 "Cut in hard. Title holds 1.5s. Cut to scene."),

("Alex calls it the Reward Trap —",
 "Medium shot. Alex at his Friday desk, tired but anticipating. The label 'REWARD TRAP' appears in small text in the corner — but Alex doesn't look at it. He doesn't know it has a name.",
 "Medium shot", "Warm amber desk light", "The viewer knows what Alex doesn't",
 "Alex at Friday desk; corner label he doesn't see",
 "Static. Label appears in corner; Alex looks elsewhere. 2s."),

("though he doesn't call it anything, because he doesn't know it's a trap.",
 "Close-up of Alex's face. Genuine unawareness — not stupid, just unaware. The Brain Villain behind him gives a small, slow nod. He counts on this.",
 "Close-up", "Warm interior light", "Unawareness as the condition for the trap",
 "Alex's unaware face; Brain Villain nodding behind",
 "Static. Brain Villain nod is slow and deliberate. 2s."),

("He worked hard this week. He knows it. His body knows it.",
 "Wide shot. Alex walking out of an office building, Friday afternoon. Shoulders slightly forward. Jacket loosened. The week is over. The posture communicates it before any words do.",
 "Wide shot, exterior", "Late afternoon warm light", "The legitimate case for reward — built honestly",
 "Alex leaving office Friday; tired posture; week-ending body language",
 "Static. Warm light on Alex; body language clear. 2s."),

("By Friday afternoon, his back hurts, his focus is gone, and he's been patient.",
 "Medium shot. Alex at his desk: one hand on lower back, other rubbing eyes. A calendar on the wall shows the week filled with tasks — all checked. He earned the right to feel this way.",
 "Medium shot", "Warm interior, end-of-day light", "Legitimacy — the exhaustion is real",
 "Alex with back pain; completed week calendar; earned exhaustion",
 "Static. Calendar tasks prominent; Alex's posture communicates cost. 2s."),

("So when his phone shows the salary notification,",
 "Close-up of phone screen. Bold green notification: 'SALARY RECEIVED — 3,200.' The glow is warm. Everything shifts.",
 "Close-up, phone", "Phone glow, warm green", "The trigger — clean and immediate",
 "Phone salary notification glowing green",
 "Static. Notification text prominent. 2s."),

("his brain immediately asks one question.",
 "Close-up of Alex's transparent skull. The brain inside snaps to attention — eyes wide, leaning forward, smug expression replaced by focused calculation. One question is forming.",
 "Close-up, skull interior", "Warm interior, brain glow", "The computation begins — before Alex knows it",
 "Brain snapping to attention inside skull; focused calculation",
 "Static. Brain posture shifts from passive to active. 2s."),

("Not: how much do I need to save?",
 "Wide shot, white background. A question appears: 'HOW MUCH DO I NEED TO SAVE?' Then a bold red X strikes through it. This question does not run.",
 "Wide shot", "Flat, white, red X", "The absent question — it never fires",
 "SAVE question crossed out with red X",
 "Static. X draws through the question. 2s."),

("But: what do I deserve?",
 "Wide shot, white background. A second question appears below: 'WHAT DO I DESERVE?' This one glows warm amber. No X. This is the question the brain runs.",
 "Wide shot", "Flat, white, warm amber highlight", "The active question — the one that runs",
 "DESERVE question glowing amber; no X",
 "Static. Amber glow pulses once. 2s."),

("This isn't laziness. This is neuroscience.",
 "Medium shot. Alex and Brain Villain side by side. A neuroscience icon — a stylized brain scan — floats between them. Label: 'THIS IS NEUROSCIENCE.' Not a character flaw. A mechanism.",
 "Medium shot", "Flat, white", "Reframe — blame redirected to mechanism",
 "Alex and Brain Villain; neuroscience icon between them; label",
 "Static. Icon and label appear. 2s."),

("Wolfram Schultz — neuroscientist at Cambridge University —",
 "Wide shot, research lab setting. A cartoon Schultz figure — white coat, focused expression, European academic energy — stands beside a brain scan lightboard. Bold label: 'WOLFRAM SCHULTZ · CAMBRIDGE.'",
 "Wide shot, lab", "Cool lab light", "Authority arrives — specific and real",
 "Schultz figure in lab; brain scan lightboard; name label",
 "Static. Name label fades in prominently. 2s."),

("won the Nobel Prize partly for discovering this:",
 "Close-up. A flat Nobel medal icon glows gold. Beside it: 'NOBEL PRIZE IN PHYSIOLOGY OR MEDICINE.' Small but weighty. The science has been verified at the highest level.",
 "Close-up, centered", "Gold warm glow", "Credibility anchored — the finding is real",
 "Nobel medal icon glowing; prize label",
 "Static. Medal glows; label appears. 2s."),

("the brain releases dopamine not when the reward arrives, but when the reward is expected.",
 "Wide diagram on white. A horizontal timeline: EXPECTATION on the left, REWARD ARRIVES on the right. A bold green dopamine spike appears at EXPECTATION — before the reward. Label: 'DOPAMINE FIRES HERE.' At REWARD ARRIVES, the line is flat.",
 "Wide diagram shot", "Flat, white, green spike", "The mechanism — counterintuitive and visual",
 "Timeline; dopamine spike at expectation; flat line at arrival",
 "Static. Spike appears at expectation point; flat at arrival. 3s."),

("Alex doesn't feel good because he got paid.",
 "Medium shot. Alex holds his phone showing the salary notification. Expression: oddly flat. The feeling already came. This is just the confirmation.",
 "Medium shot", "Flat, neutral", "The sequence reversed — feeling preceded the event",
 "Alex with salary notification; flat post-dopamine expression",
 "Static. Alex's expression: already past the peak. 2s."),

("He feels good because his brain already spent the money in his imagination.",
 "Close-up of Alex's thought bubble. Inside: a dinner table, a jacket, an upgraded subscription icon — all glowing. The money is already spent in the mind. The dopamine ran on the imagination, not the action.",
 "Close-up, thought bubble", "Warm thought-bubble glow", "The spend happened mentally first",
 "Alex's thought bubble with glowing imagined purchases",
 "Static. Thought bubble items glow warmly. 2s."),

("The reward center activated before a single euro left his account.",
 "Wide diagram. Alex's brain with reward center highlighted in warm orange. An arrow: BEFORE SPENDING. The account balance is unchanged. The brain is already satisfied.",
 "Wide diagram shot", "Flat, white, orange brain highlight", "Timing is the mechanism",
 "Brain reward center glowing; BEFORE SPENDING arrow; unchanged balance",
 "Static. Brain region glows; arrow and unchanged balance both visible. 3s."),

("The result? The eighty-five euro dinner.",
 "Close-up of a restaurant receipt. Bold line: '85.00.' A small label: 'REWARD.' Not extravagant. Completely justified in the moment.",
 "Close-up, receipt", "Warm restaurant light", "The specific cost — not dramatic, just real",
 "Restaurant receipt; 85.00 line; REWARD label",
 "Static. Receipt crisp; label present. 2s."),

("The one-forty jacket. The streaming subscription upgraded just for this month.",
 "Wide shot, white background. Three items in a row: receipt (85), shopping bag tag (140), streaming logo with 'UPGRADED' label. All mundane. All justified. All adding up.",
 "Wide shot", "Flat, white", "Accumulation — three becomes a pattern",
 "Three justified purchase items in a row; all labeled REWARD",
 "Static. Items appear in sequence. 2s."),

("Not luxuries — rewards. Small. Justified. Automatic.",
 "Wide shot. The three items from before, now with labels below each: 'SMALL.' 'JUSTIFIED.' 'AUTOMATIC.' The Brain Villain ticks them off on a notepad. Everything checks out.",
 "Wide shot", "Flat, white", "The trap's logic — internally consistent",
 "Three items with justification labels; Brain Villain ticking notepad",
 "Static. Labels appear under each item; Brain Villain nods. 3s."),

("The Brain Villain calculated perfectly:",
 "Medium shot. Brain Villain at a small desk, reviewing his notepad. Expression: professional satisfaction. Not evil — just accurate. He ran the numbers and they worked.",
 "Medium shot", "Flat, warm neutral", "Competence of the trap — it is working as designed",
 "Brain Villain at desk reviewing notepad; professional satisfaction",
 "Static. Brain Villain reviews; expression: satisfied and precise. 2s."),

("rewards feel necessary, not optional.",
 "Wide diagram. Two columns: 'NECESSARY' (solid, weighted, green border) vs 'OPTIONAL' (dashed, lighter, gray border). The reward icons all sit in the NECESSARY column. The label is the Brain Villain's verdict.",
 "Wide diagram shot", "Flat, white", "The reclassification — optional became necessary",
 "Two columns; rewards in NECESSARY column; OPTIONAL column empty",
 "Static. Reward icons in necessary column; contrast clear. 3s."),

("Alex didn't overspend. His brain spent exactly what it felt it earned.",
 "Wide shot. A balance scale. Left side: effort/hours worked that week. Right side: the reward purchases. They balance. The brain's accounting is internally consistent — and wrong for building wealth.",
 "Wide shot", "Flat, white", "The internal logic — balanced and self-defeating",
 "Balance scale: effort vs rewards; perfectly balanced",
 "Static. Scale sits in balance. 2s."),

("And here's where Trap One gets expensive.",
 "Medium shot. Brain Villain looks up from notepad. Smirks. Turns a page. The expensive part is just beginning.",
 "Medium shot", "Flat, warm neutral", "Escalation announced — the trap deepens",
 "Brain Villain turning page; smirk signaling escalation",
 "Static. Page turn deliberate; smirk held. 2s."),

("Professor Robert Frank — Cornell University, thirty years of research —",
 "Wide shot, academic setting. A cartoon Frank figure — professorial, measured — stands before a graph spanning thirty years. Bold label: 'ROBERT FRANK · CORNELL · 30 YEARS.'",
 "Wide shot, academic", "Warm academic light", "Authority — long-term observation, not theory",
 "Frank figure before 30-year graph; name and institution label",
 "Static. Label prominent; graph behind him. 2s."),

("documented what happens after every reward: hedonic adaptation.",
 "Wide diagram. A simple line graph. After each reward event (marked with a small star), the baseline rises slightly. Never comes back down. Label appears: 'HEDONIC ADAPTATION.' The line only goes up.",
 "Wide diagram shot", "Flat, white", "The mechanism named — visual and clear",
 "Line graph rising after each reward; HEDONIC ADAPTATION label",
 "Static. Graph builds left to right; baseline rises after each event. 3s."),

("Every reward resets the baseline.",
 "Close-up of the graph. A dashed horizontal line marks the 'BASELINE.' After a reward star, an arrow moves the baseline up. The new baseline is higher. Bold label: 'NEW BASELINE.'",
 "Close-up, graph", "Flat, white", "The mechanism in detail — one reset, one rise",
 "Baseline rising after reward; NEW BASELINE label",
 "Static. Baseline arrow moves up; label appears. 2s."),

("The eighty-five euro dinner becomes the new normal.",
 "Medium shot. Alex at a restaurant. The 85-euro bill arrives. He barely looks at it. His expression: not pleasure, not regret — just normal. The dinner that was once a treat is now the floor.",
 "Medium shot", "Warm restaurant light", "Normalization — the treat has become ordinary",
 "Alex at restaurant; 85-euro bill; expression of normalcy, not pleasure",
 "Static. Bill on table; Alex's flat expression. 2s."),

("Next payday, eighty-five euros doesn't feel like a reward anymore.",
 "Medium shot. Alex back at desk. Salary notification arrives. He does not think about the 85-euro dinner. The brain inside his skull barely registers it. Below the reward threshold now.",
 "Medium shot", "Warm desk light", "Threshold risen — what satisfied now falls short",
 "Alex with salary; brain unimpressed by 85-euro benchmark",
 "Static. Brain expression: underwhelmed. 2s."),

("It feels like the floor.",
 "Wide shot, white background. The 85-euro dinner icon now sits at the bottom of a stack — labeled 'FLOOR.' Above it, new reward levels are forming. The floor is higher than it was last month.",
 "Wide shot", "Flat, white", "The ratchet visible — floor has risen",
 "Dinner icon at bottom labeled FLOOR; new reward levels above",
 "Static. Stack structure clear; FLOOR label prominent. 2s."),

("Trap One doesn't cost you once. It raises the price every single month.",
 "Wide diagram. A bar chart — monthly spending on rewards, growing steadily month over month. Not dramatic. Steady. Relentless. Label: 'COST: MONTHLY AND COMPOUNDING.'",
 "Wide diagram shot", "Flat, white", "The compounding cost — the trap's real damage",
 "Monthly bar chart growing steadily; compounding cost label",
 "Static. Bars grow month by month; label appears. 3s."),

("Trap One is the one Alex knows about, somewhere in the back of his mind.",
 "Close-up of Alex's skull. The brain is there — and in a small, dim corner of it, a tiny awareness icon glows faintly. Alex knows, distantly. Not enough to act.",
 "Close-up, skull interior", "Dim interior, tiny glow", "Partial awareness — not enough",
 "Tiny awareness icon dimly glowing in brain corner",
 "Static. Awareness icon dim but present. 2s."),

("Trap Two is the one he thinks he's beating.",
 "Medium shot. Alex looks confident. A small Trap 2 icon is visible in the background — but Alex glances at it with satisfaction. He believes he's handling it. He's wrong.",
 "Medium shot", "Flat, warm neutral", "False confidence — the setup for Trap 2",
 "Alex confident; Trap 2 icon in background; mistaken satisfaction",
 "Static. Alex's confident expression contrasts with unbeaten Trap 2 icon. 2s."),

# ── CTA ────────────────────────────────────────────────────────────────────────

("If your brain is doing this to you right now — subscribe.",
 "Medium shot. Alex turns directly to camera. Calm, measured. Brain Villain freezes mid-action behind him — caught off guard by the direct address.",
 "Medium shot, direct address", "Flat, white", "Direct — no pressure, just invitation",
 "Alex to camera; Brain Villain frozen behind him",
 "Static. Brain Villain freeze is deliberate. 2s."),

("We break down a new bias every week. It's free. And it might save you more than you think.",
 "Medium shot continues. Alex finishes. Brain Villain rolls his eyes. Alex turns back to the story. Hard cut — momentum resumes immediately. Total CTA: 5 seconds.",
 "Medium shot, cut back", "Flat, white", "Brevity — the CTA earns nothing it doesn't need",
 "Brain Villain rolling eyes; Alex turning back; hard cut to Trap 2",
 "Brain Villain eye roll; hard cut. 3s total from CTA start."),

# ── TRAP 2 — THE SAFE MONEY ILLUSION ──────────────────────────────────────────

("Trap Two.",
 "Full-frame title card. Bold red background. White text: 'TRAP 2 — THE SAFE MONEY ILLUSION.' Holds.",
 "Title card", "Red background, white text", "Marker — section declared",
 "Title card: TRAP 2 — THE SAFE MONEY ILLUSION",
 "Cut in hard. Title holds 1.5s. Cut to scene."),

("Alex does something most people call responsible.",
 "Medium shot. Alex at his laptop, expression of quiet pride. The word 'RESPONSIBLE' floats gently above him in warm gold. He has a system. He's proud of it.",
 "Medium shot", "Warm interior light, gold label", "Pride before the reveal",
 "Alex at laptop; RESPONSIBLE label floating above",
 "Static. Label appears; Alex's expression: satisfied. 2s."),

("He keeps two thousand euros in a savings account.",
 "Close-up of laptop screen. A savings account interface shows: 'BALANCE: 2,000.00.' Green border. A padlock icon beside it. Label: 'EMERGENCY FUND.'",
 "Close-up, screen", "Flat, screen glow, green border", "The safety net — looks responsible",
 "Savings account screen showing 2,000 with green border and padlock",
 "Static. Screen crisp; padlock prominent. 2s."),

("Emergency fund. He's proud of it. He calls it untouchable.",
 "Medium shot. Alex taps the padlock icon with one finger. Expression: this is protected. The Brain Villain stands behind him, watching with interest — not alarm. Not yet.",
 "Medium shot", "Flat, warm neutral", "Emotional attachment to the label",
 "Alex tapping padlock; Brain Villain watching with quiet interest",
 "Static. Padlock tap deliberate. 2s."),

("Meanwhile, he carries eighteen hundred euros in credit card debt.",
 "Close-up of a second screen section. A credit card interface: 'BALANCE OWED: -1,800.00.' Red border. No padlock. No label. It just sits there.",
 "Close-up, screen", "Flat, screen glow, red border", "Contrast — the other account revealed",
 "Credit card balance showing -1,800 with red border",
 "Static. Red border present but less prominent than savings. 2s."),

("Annual interest rate: twenty-three percent.",
 "Close-up. A bold label appears over the credit card interface: '23% APR.' The Brain Villain looks at this number with appreciation. He didn't set it. He benefits from it.",
 "Close-up", "Flat, red emphasis", "The mechanism of the trap — specific and real",
 "23% APR label bold on credit card; Brain Villain approving",
 "Static. 23% label is large and prominent. 2s."),

("Alex is paying four hundred and fourteen euros a year in interest —",
 "Wide diagram on white. A simple calculation: '1,800 x 0.23 = 414 / YEAR.' A bold red counter runs: '414 EUROS — INTEREST PAID PER YEAR.' Not dramatic. Just math.",
 "Wide diagram shot", "Flat, white, red counter", "The cost named — unavoidable arithmetic",
 "Interest calculation shown; 414 euros per year label in red",
 "Static. Calculation appears; counter holds. 3s."),

("to protect money that earns thirty-two euros a year in savings.",
 "Wide diagram. Below the interest calculation: a second line — '2,000 x 0.016 = 32 / YEAR' — pale green. The savings return. 32 vs 414. The diagram does the work.",
 "Wide diagram shot", "Flat, white, pale green vs red", "The asymmetry — visual and mathematical",
 "Savings return calculation: 32/year in pale green; contrast with 414 in red",
 "Static. Both lines visible; contrast clear. 3s."),

("Net loss: three hundred and eighty-two euros. Every year.",
 "Wide shot. A bold red box appears: 'NET LOSS: 382 / YEAR.' Below it, smaller: '...EVERY YEAR.' The Brain Villain circles this number on his notepad. He considers it a success.",
 "Wide shot", "Flat, white, red box", "The damage named — annual, compounding",
 "NET LOSS 382/YEAR in bold red box; Brain Villain circling it",
 "Static. Red box prominent; Brain Villain's circle deliberate. 2s."),

("Not because Alex is bad at finance.",
 "Medium shot. Alex reading a finance book — competent, attentive. He's not ignorant. The system isn't a result of ignorance.",
 "Medium shot", "Flat, warm neutral", "Reframe begins — not stupidity",
 "Alex reading finance book; competent expression",
 "Static. Book and expression establish competence. 2s."),

("Because his brain refuses to see these as the same money.",
 "Wide shot. Two money piles, same size. Between them: a wall, drawn by the Brain Villain. One pile labeled 'SAVINGS — UNTOUCHABLE.' Other pile labeled 'DEBT — MANAGEABLE.' Same amount. Completely separated.",
 "Wide shot", "Flat, white", "The wall is the mechanism — same money, divided",
 "Two equal piles separated by Brain Villain's wall; different labels",
 "Static. Brain Villain draws wall between identical piles. 3s."),

("This is Mental Accounting.",
 "Wide shot. Bold label on white: 'MENTAL ACCOUNTING.' Below it: a simple definition — 'Treating identical money differently based on its label.' Clean, academic, final.",
 "Wide shot", "Flat, white", "Named — the bias gets its title",
 "MENTAL ACCOUNTING bold label; simple definition below",
 "Static. Label and definition appear. 2s."),

("Richard Thaler — Nobel Prize in Economics, 2017, University of Chicago —",
 "Wide shot, academic setting. A cartoon Thaler figure — warm expression, professional — stands before a University of Chicago backdrop. Bold label: 'RICHARD THALER · NOBEL 2017 · CHICAGO.'",
 "Wide shot, academic", "Warm academic light", "Authority — the highest credential in economics",
 "Thaler figure; Nobel and institution labels",
 "Static. Labels prominent and accurate. 2s."),

("proved that humans don't treat money as money.",
 "Wide shot, white background. A large 'MONEY = MONEY' equation. A bold X strikes through the equals sign. Humans break this rule reflexively. Thaler proved it.",
 "Wide shot", "Flat, white, red X on equals", "The finding stated — clean and confrontational",
 "MONEY = MONEY equation with X through equals; finding declared",
 "Static. X draws through equation. 2s."),

("We treat it as labeled categories.",
 "Wide diagram. Money icons sorted into labeled boxes: 'SALARY,' 'TAX REFUND,' 'EMERGENCY FUND,' 'FOUND MONEY,' 'BONUS.' Each box treated differently. The money is identical. The labels change everything.",
 "Wide diagram shot", "Flat, white", "The structure of mental accounting made visible",
 "Money sorted into labeled category boxes; each treated differently",
 "Static. Category boxes appear; money sorted into each. 3s."),

("Two thousand euros in an account called emergency",
 "Close-up of a green box labeled 'EMERGENCY.' Two thousand euros inside. A warm glow. A padlock. This money feels safe, protected, righteous.",
 "Close-up", "Warm green glow", "The label creates the feeling — safety",
 "Green EMERGENCY box; 2,000 inside; warm glow and padlock",
 "Static. Green glow warm and protective. 2s."),

("feels completely different from two thousand euros that could pay off debt.",
 "Close-up of a red box labeled 'DEBT PAYMENT.' Two thousand euros inside — same amount. Cold light. No padlock. This money feels uncomfortable, aggressive, wrong.",
 "Close-up", "Cool red light", "Same amount, opposite feeling — the trap",
 "Red DEBT PAYMENT box; 2,000 inside; cold light, no padlock",
 "Static. Cold light contrasts with previous warmth. 2s."),

("They are mathematically identical.",
 "Wide shot. The two boxes — green and red — placed side by side. Between them: a mathematical equals sign in bold black. The math says: same. The brain refuses.",
 "Wide shot", "Flat, white", "The contradiction stated — brain vs math",
 "Green and red boxes side by side with equals sign between them",
 "Static. Equals sign prominent between boxes. 2s."),

("Psychologically, they live on different planets.",
 "Wide shot. The two boxes are now on separate planets — one green planet, one red planet. The equals sign is still there, floating in space between them. The math is unchanged. The experience is not.",
 "Wide shot, space metaphor", "Dark space background, two planet tones", "The felt distance — enormous despite math",
 "Green and red planets; equals sign floating between; vast separation",
 "Static. Planets separated; equals sign still visible between them. 3s."),

("The Brain Villain loves this trap because it feels responsible.",
 "Medium shot. Brain Villain standing before the green EMERGENCY box, arms crossed approvingly. Expression: genuine appreciation. This is the cleanest trap — it is disguised as a virtue.",
 "Medium shot", "Flat, warm neutral", "The villain's preference — because it's disguised",
 "Brain Villain approving of EMERGENCY box; genuine appreciation",
 "Static. Appreciation expression genuine, not ironic. 2s."),

("Alex is being careful with his emergency fund. He's being disciplined.",
 "Medium shot. Alex with the same proud expression as before — padlock tapped, savings protected. All true. And all consistent with losing 382 euros a year.",
 "Medium shot", "Flat, warm neutral", "The trap's camouflage — genuine virtue hiding the cost",
 "Alex with proud padlock expression; genuine discipline on display",
 "Static. Expression real; trap still running. 2s."),

("He's paying three hundred and eighty-two euros a year for that discipline.",
 "Wide shot. The NET LOSS box returns: '382 / YEAR.' Beneath Alex's proud expression. He doesn't see the connection. The Brain Villain does.",
 "Wide shot", "Flat, white", "Cost and pride in the same frame — the juxtaposition is the point",
 "Alex's proud expression; NET LOSS box visible beneath; Brain Villain watching",
 "Static. Both elements in frame simultaneously. 3s."),

("The trap doesn't feel like a trap.",
 "Medium shot. The savings trap is dressed up — velvet rope around it, a small gold plaque: 'RESPONSIBLE BEHAVIOR.' It looks like a good thing. Because it is, in isolation.",
 "Medium shot", "Flat, warm, gold accents", "The disguise — virtue as camouflage",
 "Trap with velvet rope and RESPONSIBLE BEHAVIOR gold plaque",
 "Static. Disguise complete; trap unrecognizable. 2s."),

("It feels like a virtue.",
 "Close-up. A small halo appears over the savings box. Golden. Glowing. The Brain Villain places it there carefully, like a prop.",
 "Close-up", "Warm gold glow", "Virtue halo — the final layer of disguise",
 "Brain Villain placing golden halo over savings trap",
 "Static. Halo glows; Brain Villain's placement deliberate. 2s."),

("In the next video, we show why Alex's brain does the exact same trick with tax refunds —",
 "Medium shot. A tax refund notification appears on Alex's phone. Brain Villain immediately lights up — same posture as with the salary notification. Same trap. Different trigger.",
 "Medium shot", "Flat, warm neutral", "Name drop — seed planted for next video",
 "Tax refund notification; Brain Villain lighting up; same trap posture",
 "Static. Brain Villain's recognition is immediate. 2s."),

("and why that money disappears faster than any other money he earns.",
 "Wide shot. A simple bar graph: salary money (slow spend), tax refund money (fast disappear). The tax refund bar drops fast. Same trap, stronger trigger.",
 "Wide shot", "Flat, white", "The specific cost of the next trap — curiosity gap",
 "Salary spend rate vs tax refund spend rate; stark difference",
 "Static. Bars compare clearly. 2s."),

("Same trap. Different label. Same result.",
 "Wide shot, white background. Three panels in a row: EMERGENCY FUND — MENTAL ACCOUNTING — DEBT. TAX REFUND — MENTAL ACCOUNTING — SPENT. Three columns, same middle box, same outcome.",
 "Wide triptych", "Flat, white", "Pattern stated — the trap is structural, not situational",
 "Triptych showing same Mental Accounting mechanism across contexts",
 "Static. Middle column identical in both rows. 2s."),

("But before that — Trap Three.",
 "Medium shot. Brain Villain turns away from the Mental Accounting boxes. His expression shifts — a flicker of something. Trap Three is the one he relies on most.",
 "Medium shot", "Flat, shifting tone", "Anticipation — even the villain respects Trap Three",
 "Brain Villain turning toward Trap 3; subtle shift in expression",
 "Static. Expression shift is deliberate. 2s."),

("The one that makes Trap One and Trap Two inevitable.",
 "Wide shot. Trap 1 and Trap 2 icons visible — but now, beneath them, a larger foundation layer appears: TRAP 3. The gears preview: Trap 3 is the base. The others sit on top of it.",
 "Wide shot", "Flat, white", "Architecture revealed — Trap 3 is the foundation",
 "Trap 1 and 2 icons sitting on Trap 3 foundation layer",
 "Static. Foundation relationship clear; Trap 3 carries the others. 3s."),

# ── TRAP 3 — THE FUTURE IS FAKE ────────────────────────────────────────────────

("Trap Three.",
 "Full-frame title card. Bold deep red background. White text: 'TRAP 3 — THE FUTURE IS FAKE.' Larger than previous title cards. Held longer. More weight.",
 "Title card", "Deep red background, white text", "Weight — the biggest trap gets more space",
 "Title card: TRAP 3 — THE FUTURE IS FAKE",
 "Cut in hard. Title holds 2s. Cut to scene."),

("This one is harder to see because it's not a spending habit.",
 "Wide shot, white background. Trap 1 and Trap 2 icons with visible dollar signs — spending visible. Trap 3 icon: no dollar sign. No spending symbol. Something else.",
 "Wide shot", "Flat, white", "Distinction — this trap operates differently",
 "Trap 1 and 2 with dollar signs; Trap 3 without — different category",
 "Static. Contrast in trap icon types. 2s."),

("It's a perception problem.",
 "Close-up. A simple perception diagram — the same object looking different from two distances. Label: 'PERCEPTION PROBLEM.' Clean, psychological, not financial.",
 "Close-up, diagram", "Flat, white", "Category shift — psychology not spending",
 "Perception diagram; PERCEPTION PROBLEM label",
 "Static. Diagram clean and clear. 2s."),

("Ask Alex: would you rather have a hundred euros today,",
 "Wide shot. An animated fork in a road. Left path labeled: '100 EUROS — TODAY.' Alex stands at the fork, looking left.",
 "Wide shot, fork in road", "Flat, warm neutral", "The choice — simple and immediate",
 "Road fork; Alex looking at LEFT path: 100 TODAY",
 "Static. Left path option prominent. 2s."),

("or a hundred and ten in one week?",
 "Wide shot continues. Right path labeled: '110 EUROS — 1 WEEK.' Both options visible. The math: 10% in one week is exceptional. But Alex is already moving left.",
 "Wide shot, fork", "Flat, warm neutral", "The irrational preference — about to be shown",
 "Right path: 110 IN 1 WEEK; Alex already leaning left despite math",
 "Static. Both paths visible; Alex's lean is deliberate. 2s."),

("He takes the hundred. Almost everyone does.",
 "Wide shot. Alex walks left. Bold label: 'ALMOST EVERYONE.' The road to 110 is empty. The math doesn't matter. The immediacy does.",
 "Wide shot", "Flat, warm neutral", "Universal — not an individual weakness",
 "Alex walking left; ALMOST EVERYONE label; empty right path",
 "Static. Empty right path emphasizes universality. 2s."),

("Now ask him: would you rather have a hundred euros in fifty-two weeks,",
 "Wide shot. New fork. Same style — but now LEFT path: '100 EUROS — 52 WEEKS.' Distant. Hypothetical. Alex looks at it without urgency.",
 "Wide shot, new fork", "Flat, slightly cooler — distance implied", "Same math, different felt reality",
 "New fork; LEFT path: 100 IN 52 WEEKS; Alex looking neutrally",
 "Static. Same fork structure; different time labels. 2s."),

("or a hundred and ten in fifty-three weeks?",
 "Wide shot continues. RIGHT path: '110 EUROS — 53 WEEKS.' One extra week, one year from now. Alex considers.",
 "Wide shot", "Flat, cool neutral", "The patience is available — when distant",
 "Right path: 110 IN 53 WEEKS; Alex considering",
 "Static. Both paths visible; Alex's posture: considering. 2s."),

("Same trade. One year later. He'll happily wait the extra week.",
 "Wide shot. Alex walks right. Bold label: 'SAME TRADE.' Label below: 'DIFFERENT PSYCHOLOGY.' Same math. Opposite choice. The irrationality is structural.",
 "Wide shot", "Flat, warm neutral", "The irrationality exposed — identical math, inverted choice",
 "Alex walking right; SAME TRADE / DIFFERENT PSYCHOLOGY labels",
 "Static. Both labels prominent; contrast stated plainly. 3s."),

("The math is identical. The psychology is completely different.",
 "Wide split diagram. Left: the two trade comparisons side by side — mathematically identical (both = 10% gain, 1 week wait). Right: felt reality bars — first trade feels urgent, second feels neutral. Same math, opposite felt weight.",
 "Wide split diagram", "Flat, white", "The gap between math and psychology — made visual",
 "Math equivalence left; felt weight asymmetry right",
 "Static. Split diagram holds; contrast clear. 3s."),

("David Laibson — behavioral economist at Harvard University —",
 "Wide shot, Harvard setting. A cartoon Laibson figure — precise, academic, Harvard energy — stands before a behavioral economics diagram. Bold label: 'DAVID LAIBSON · HARVARD.'",
 "Wide shot, academic", "Warm academic light", "Authority — Harvard behavioral economics",
 "Laibson figure; Harvard label; behavioral diagram behind",
 "Static. Name and institution label prominent. 2s."),

("spent decades quantifying this pattern.",
 "Wide shot. A research timeline behind Laibson — decades marked, data points accumulating. This wasn't a hunch. It was measured, repeatedly.",
 "Wide shot", "Flat, academic warm light", "Rigor — decades of verification",
 "Research timeline behind Laibson; decades of data points",
 "Static. Timeline populated left to right. 2s."),

("He calls it hyperbolic discounting.",
 "Wide diagram. A curve on white — not a straight line, but a hyperbola. Near-term rewards: massively overvalued (curve peaks steeply). Long-term rewards: barely valued (curve flat). Bold label: 'HYPERBOLIC DISCOUNTING.'",
 "Wide diagram shot", "Flat, white", "The curve — non-linear, not rational",
 "Hyperbolic discount curve; steep near peak; flat long-term; label",
 "Static. Curve draws left to right; steepness contrast clear. 3s."),

("The further something is in the future, the less real it feels.",
 "Wide shot. Three identical objects at different distances. Near: crisp, solid, large. Mid: slightly faded. Far: barely visible, almost transparent. Label: 'DISTANCE = REALITY FADE.'",
 "Wide shot", "Flat, white with fade effect at distance", "Felt reality as a function of distance",
 "Three objects at increasing distance; reality fading with distance",
 "Static. Fade gradient clear; label present. 3s."),

("Not less important. Less real.",
 "Wide shot. Two panels. Left: 'LESS IMPORTANT? NO.' Right: 'LESS REAL? YES.' Brain Villain stands in the right panel, pointing. This is the distinction. The problem isn't priority. It's felt reality.",
 "Wide shot, split panels", "Flat, white", "The precise definition — importance vs reality",
 "Split: NOT LESS IMPORTANT / LESS REAL; Brain Villain in right panel",
 "Static. Brain Villain's point deliberate. 2s."),

("Future Alex — the one who needs the retirement account,",
 "Wide shot. A second Alex character appears — slightly grayer, slightly older. This is Future Alex. He holds a retirement account document. Expression: he needs this. He's counting on Present Alex.",
 "Wide shot", "Slightly cooler tones for Future Alex", "Future Alex introduced — specific and real",
 "Future Alex character with retirement document; slight age indicators",
 "Static. Future Alex distinct but recognizable as Alex. 2s."),

("the one who has to pay Future Alex's bills,",
 "Wide shot. Future Alex surrounded by bills — rent, health, basics. He's holding them. They're real. Present Alex doesn't feel the weight of them.",
 "Wide shot", "Flat, cooler tones", "The specificity of Future Alex's burden",
 "Future Alex surrounded by future bills; holding them",
 "Static. Bills numerous and specific. 2s."),

("the one living the consequences of Present Alex's choices —",
 "Wide shot. A chain of consequence: Present Alex's small decisions (dinner, upgrade, delay) → chain of arrows → Future Alex receiving each consequence. The chain is visible. The distance makes it abstract.",
 "Wide shot", "Flat, white, consequence chain", "The chain — connecting present choices to future reality",
 "Consequence chain: present choices → Future Alex; chain visible",
 "Static. Chain connects across frame. 3s."),

("doesn't feel like Alex. He feels like a stranger.",
 "Medium shot. Present Alex and Future Alex face each other across a gap. Present Alex looks at Future Alex: polite, distant, unrecognizing. Future Alex looks back: desperate, familiar.",
 "Medium shot", "Flat, white, gap between characters", "The estrangement — the key emotion of the trap",
 "Present and Future Alex facing each other across gap; stranger dynamic",
 "Static. Gap between them prominent; expressions contrast. 3s."),

("And we don't sacrifice for strangers.",
 "Wide shot, white background. A bold statement: 'WE DON'T SACRIFICE FOR STRANGERS.' Present Alex turns away from Future Alex. Not maliciously. Just... Future Alex isn't real enough to sacrifice for.",
 "Wide shot", "Flat, white", "The behavioral consequence — not cruelty, just psychology",
 "Bold statement; Present Alex turning away from Future Alex",
 "Static. Turn deliberate; statement holds. 2s."),

("So Present Alex makes decisions that make perfect sense right now.",
 "Medium shot. Present Alex — confident, justified, internally consistent. Every choice he makes is rational in the present moment. The trap is not irrationality. It's a different time horizon.",
 "Medium shot", "Flat, warm present tones", "The trap's internal logic — not stupidity",
 "Present Alex confident; internally consistent present-moment decisions",
 "Static. Expression: completely reasonable. 2s."),

("Eighty-five euro dinner? He deserves it. That's Trap One.",
 "Medium shot. The dinner receipt appears. Trap 1 icon connects to it with an arrow. The operating system (Present Bias) enables Trap 1 to run.",
 "Medium shot", "Flat, warm neutral", "Connection — Trap 3 enabling Trap 1",
 "Dinner receipt with Trap 1 icon arrow; connection visible",
 "Static. Arrow connection clear. 2s."),

("Keep the savings, carry the debt? That's responsible. That's Trap Two.",
 "Medium shot. The two account boxes from before. Trap 2 icon connects. Present Bias tells Alex: Future Alex will sort the debt. So the mental accounting stays.",
 "Medium shot", "Flat, warm neutral", "Connection — Trap 3 enabling Trap 2",
 "Savings/debt boxes with Trap 2 icon arrow; same connection",
 "Static. Arrow connection clear. 2s."),

("Start saving next month? Future Alex will be disciplined.",
 "Medium shot. A calendar. The current month's savings column: empty. Alex flips to next month. That month's column: also empty. He flips again. Same.",
 "Medium shot", "Flat, neutral tones", "The recurring delay — never arrives",
 "Calendar with empty savings columns; Alex flipping forward month by month",
 "Static. Pattern of empty columns clear. 2s."),

("Future Alex is always about to be disciplined.",
 "Wide shot. Future Alex waves from the distance — cheerful, optimistic. He's always just about to arrive. But the distance never closes. The discipline never begins.",
 "Wide shot", "Slightly faded distance tones", "The perpetual delay — almost arriving, never here",
 "Future Alex waving from permanent distance; never approaching",
 "Static. Distance maintained; Future Alex's wave held. 3s."),

("Present Bias is the operating system.",
 "Wide diagram. A flat OS boot screen: 'PRESENT BIAS — OPERATING SYSTEM v∞.' Boot complete. Below it: two app icons — REWARD TRAP and MENTAL ACCOUNTING — starting up.",
 "Wide diagram shot", "Flat, tech-referential white", "Architecture stated — Trap 3 is foundational",
 "OS boot screen: PRESENT BIAS; two app icons loading beneath",
 "Static. Boot sequence completes; app icons appear. 3s."),

("Trap One and Trap Two are the applications running on top of it.",
 "Wide shot. The OS diagram: PRESENT BIAS as base. REWARD TRAP and MENTAL ACCOUNTING as app windows open above. The apps depend on the OS. Kill the OS — the apps have no foundation.",
 "Wide shot", "Flat, tech-metaphor white", "The dependency structure — OS and apps",
 "Present Bias OS; Reward Trap and Mental Accounting apps open on top",
 "Static. Dependency structure clear; apps sit on OS layer. 3s."),

("A 2024 study in the Journal of Behavioral Decision Making",
 "Wide shot. A journal cover — flat, academic, credible. 'JOURNAL OF BEHAVIORAL DECISION MAKING · 2024.' Label and year prominent.",
 "Wide shot", "Flat, academic white", "Evidence arrives — specific and datable",
 "Journal cover: 2024 issue; label prominent",
 "Static. Journal cover clean and specific. 2s."),

("tracked fourteen thousand participants.",
 "Wide shot. A grid of small human icons: 14,000 arranged in rows. Scale visible. This is not a small study.",
 "Wide shot", "Flat, white", "Scale — 14,000 is meaningful",
 "Grid of 14,000 participant icons; scale communicated",
 "Static. Grid fills frame systematically. 2s."),

("People who could mentally picture their future self as the same person",
 "Wide shot. Two Alex figures — Present and Future — but now they overlap, merge slightly. They share the same face. Same posture. The gap closes. Future Alex is Alex.",
 "Wide shot", "Flat, warm neutral", "The intervention — identity continuity",
 "Present and Future Alex overlapping; same face emerging",
 "Static. Overlap deliberate; same-person recognition visible. 3s."),

("made twenty-three percent better financial decisions",
 "Wide diagram. A comparison bar: CONTROL GROUP vs FUTURE SELF GROUP. The future-self group bar is 23% taller. Bold label: '+23% BETTER DECISIONS.' One change. No apps, no advisors.",
 "Wide diagram shot", "Flat, white, green 23% bar", "The result — measurable and specific",
 "Comparison bars; future-self group 23% higher; label prominent",
 "Static. 23% difference prominent. 3s."),

("without any other intervention.",
 "Wide shot, white background. A clean panel: 'NO BUDGETING APP. NO ADVISOR. NO PRODUCT.' Just one change in perception. Label: 'ZERO ADDITIONAL INTERVENTION.'",
 "Wide shot", "Flat, white", "Simplicity of the finding — one thing changed one outcome",
 "Three crossed-out interventions; ZERO ADDITIONAL INTERVENTION label",
 "Static. Crossed-out items clear; label emphatic. 2s."),

("Not a budgeting app. Not a financial advisor.",
 "Wide shot. Two icons: a budgeting app logo and a financial advisor figure. Both crossed out with bold X marks. Not required. Not the intervention.",
 "Wide shot", "Flat, white, red X marks", "What was NOT needed — the reframe",
 "App and advisor icons; bold red X marks; not the answer",
 "Static. X marks clear. 2s."),

("Just the ability to see Future Alex as Alex.",
 "Wide shot. Present Alex and Future Alex stand side by side — same height, same appearance, same expression. They are the same person. The gap is gone. The distance is gone.",
 "Wide shot", "Flat, warm neutral", "The resolution — same person, same stake",
 "Present and Future Alex identical side by side; gap closed",
 "Static. Identical figures; no gap. 3s."),

# ── SYSTEM CLOSE ───────────────────────────────────────────────────────────────

("Here's what makes these three traps expensive: they don't work separately.",
 "Wide shot. Three gear icons — REWARD TRAP, MENTAL ACCOUNTING, PRESENT BIAS — floating unconnected. Then they move toward each other and lock together. The system forms.",
 "Wide shot", "Flat, white", "The system assembled — three gears locking",
 "Three separate gear icons locking together; system forming",
 "Animated. Gears float; connect; begin spinning together. 3s."),

("The Reward Trap fires on Friday.",
 "Wide shot. Gear 1 (REWARD TRAP) spins. Alex's phone notification visible. Trap 1 engages automatically.",
 "Wide shot", "Flat, warm Friday tones", "Gear 1 active — the first mechanism",
 "REWARD TRAP gear spinning; salary notification visible",
 "Static. Gear 1 spinning; notification connected. 2s."),

("Present Bias tells Alex that Future Alex will compensate.",
 "Wide shot. Gear 3 (PRESENT BIAS) connects to Gear 1 — enabling it. The operating system gives Trap 1 permission. Future Alex will handle it. Present Alex spends.",
 "Wide shot", "Flat, white", "OS enabling Trap 1 — the dependency shown",
 "PRESENT BIAS gear enabling REWARD TRAP gear; permission signal",
 "Static. Gear connection and permission signal visible. 2s."),

("Mental Accounting keeps the debt and savings in separate boxes —",
 "Wide shot. Gear 2 (MENTAL ACCOUNTING) spins — keeping the two boxes separated. The wall is maintained. The damage stays invisible.",
 "Wide shot", "Flat, white", "Gear 2 active — maintaining the separation",
 "MENTAL ACCOUNTING gear spinning; savings and debt boxes separated",
 "Static. Gear 2 maintains wall between boxes. 2s."),

("so the damage never looks total.",
 "Wide shot. All three gears spinning. A hidden damage counter runs in the background — but it's behind the wall. The separation keeps the total invisible. Alex cannot see the full picture.",
 "Wide shot", "Flat, white", "The combined effect — total damage hidden by the system",
 "All three gears; hidden damage counter; wall obscuring total",
 "Static. Counter running; wall obscuring it. 3s."),

("Remove any one gear, and the other two lose power.",
 "Wide shot. One gear removed. The other two slow — lose coordination, lose the system's effectiveness. The gears need each other.",
 "Wide shot", "Flat, white", "Interdependence — the system is fragile if broken correctly",
 "One gear removed; other two slowing; coordination lost",
 "Static. System degrading without one gear. 3s."),

("Let all three run together, and they form a system that scales with income.",
 "Wide shot. Gears reconnect. An income counter rises: 30K, 50K, 100K, 150K. The system percentage consumed stays constant. More income, same percentage gone. The system scales.",
 "Wide shot", "Flat, white", "Scalability — the trap grows with income",
 "All three gears; income counter rising; constant percentage consumed",
 "Static. Income rises; percentage line stays flat. 3s."),

("Researchers at Princeton — Daniel Kahneman and Angus Deaton, 2010 —",
 "Wide shot, academic setting. Two cartoon figures — Kahneman and Deaton — in a Princeton research environment. Bold label: 'KAHNEMAN + DEATON · PRINCETON · 2010.'",
 "Wide shot, academic", "Warm academic light", "Two Nobel-level authorities — the finding is credible",
 "Kahneman and Deaton figures; Princeton label; 2010 study",
 "Static. Both names and institution prominent. 2s."),

("found that above a certain income level, additional earnings have almost no effect",
 "Wide diagram. An income vs behavior-change line graph. Below threshold: behavior changes with income. Above threshold: the line flattens. More income, same behavior. The system adapts.",
 "Wide diagram shot", "Flat, white", "The finding — income does not fix the system",
 "Income vs behavior graph; flat line above threshold",
 "Static. Threshold visible; flat line above it. 3s."),

("on day-to-day financial behavior.",
 "Close-up of the flat section of the graph. Label: 'BEHAVIOR UNCHANGED.' The income is higher. The system percentage stays the same. The trap consumes proportionally.",
 "Close-up, graph", "Flat, white", "The precise implication — income is not the solution",
 "Flat behavior line labeled UNCHANGED; system still consuming",
 "Static. UNCHANGED label prominent. 2s."),

("Because behavioral traps consume the same percentage of income regardless of salary.",
 "Wide diagram. A simple pie chart. One slice labeled 'BEHAVIORAL TRAPS.' The slice stays the same size as the total pie grows: 30K, 50K, 100K. Same percentage. Bigger numbers. Same slice.",
 "Wide diagram shot", "Flat, white", "The proportional trap — percentage is constant",
 "Pie chart growing; behavioral trap slice constant percentage",
 "Static. Pie grows; trap slice proportion unchanged. 3s."),

("Alex could earn fifty thousand or a hundred and fifty thousand.",
 "Wide shot. Two versions of Alex: one with '50K/YEAR' label, one with '150K/YEAR' label. Same character. Same Brain Villain beside each. Same trap gears running.",
 "Wide shot", "Flat, white", "Scale independence — the traps don't care about salary",
 "Two Alex versions: 50K and 150K; same Brain Villain and gears beside each",
 "Static. Both versions identical except salary label. 2s."),

("The system adjusts. The percentage stays roughly the same.",
 "Wide diagram. Two rows: 50K pie with trap slice, 150K pie with trap slice. Both trap slices: same angle, same percentage. Bigger pie. Same slice. The system is proportional.",
 "Wide diagram shot", "Flat, white", "Proportionality confirmed — the system self-adjusts",
 "Two pie charts; trap slice identical percentage in both",
 "Static. Both pies; same trap slice angle. 2s."),

("This isn't about how much he earns. It's about what the system does with it.",
 "Wide shot. Income arrow entering the three-gear system from the left. The gears process it. Output: same percentage consumed, regardless of input amount. Label: 'INPUT IRRELEVANT. SYSTEM DECIDES.'",
 "Wide shot", "Flat, white", "The system reframe — income is input, system is the variable",
 "Income arrow entering gear system; processed; same output proportion",
 "Static. System processes income; label appears. 3s."),

# ── IDENTITY CLOSE + GUIDE ─────────────────────────────────────────────────────

("Alex isn't bad with money.",
 "Medium shot. Alex, calm. Direct. The three gears still visible in the background — but he's looking at them now. Not trapped. Aware. Not self-blaming.",
 "Medium shot", "Flat, warm neutral", "Identity reframe begins — from failure to awareness",
 "Alex calm; gears visible behind him; awareness not blame",
 "Static. Expression: calm self-recognition, not shame. 2s."),

("He's someone whose brain was trained to protect him.",
 "Wide shot. A timeline — ancient environment on left, modern Alex on right. The three trap programs appear on the timeline early — they've been running since before modern money existed.",
 "Wide shot", "Flat, warm sepia-to-present gradient", "Evolutionary origin — protection, not sabotage",
 "Evolution timeline; traps appearing early; protection function labeled",
 "Static. Timeline shows protection origin. 2s."),

("The Reward Trap kept his ancestors motivated to hunt.",
 "Wide shot. Ancestor figure — simple, cave-context. A reward signal fires from the chest after a successful hunt. The dopamine reward was functional: effort → reward → survival.",
 "Wide shot, ancestor context", "Warm earthy tones", "Original function — the trap was adaptive",
 "Ancestor figure with functional reward signal after hunt",
 "Static. Reward signal in correct evolutionary context. 2s."),

("Mental Accounting helped them separate food from poison.",
 "Wide shot. Ancestor figure with two piles: safe food (green, labeled SAFE) and poison (red, labeled DANGER). Mental accounting was survival — categorization was life or death.",
 "Wide shot, ancestor context", "Warm earthy tones", "Adaptive context — categorization was survival",
 "Ancestor with safe/poison piles; categorical thinking as survival",
 "Static. Categorization in survival context. 2s."),

("Present Bias kept them alive by prioritizing real, immediate threats over hypothetical future ones.",
 "Wide shot. Ancestor figure facing an immediate predator — threat right now. In the background, a vague future threat (drought, winter). Present Bias: handle the predator. Not wrong for the context.",
 "Wide shot, ancestor context", "Warm earthy tones", "Present bias was survival logic — not a flaw",
 "Ancestor handling immediate predator; future threat distant and vague",
 "Static. Immediate threat prominent; future threat faded. 3s."),

("The programs are not broken.",
 "Wide shot, white background. The three trap gears — but now labeled differently: MOTIVATION, CATEGORIZATION, IMMEDIATE RESPONSE. The original functions. Bold label: 'NOT BROKEN — CONTEXTUALLY MISAPPLIED.'",
 "Wide shot", "Flat, white", "Reframe complete — the programs work, the context changed",
 "Three gears with original function labels; NOT BROKEN label",
 "Static. Function labels replace trap labels. 2s."),

("They are perfectly designed for an environment that no longer exists.",
 "Wide shot. Split: LEFT — ancient environment where the programs fit. RIGHT — modern financial world where they misfire. The programs are the same. The environment is different. Arrow: 'MISMATCH.'",
 "Wide split shot", "Earthy left, modern white right", "The mismatch is structural — not personal",
 "Ancient environment left; modern world right; MISMATCH arrow",
 "Static. Split environments; mismatch arrow prominent. 3s."),

("Knowing the three traps doesn't make them disappear.",
 "Medium shot. Alex looks at the three trap gears. He can see them clearly now. They're still spinning. Awareness doesn't stop them — but the relationship to them changes.",
 "Medium shot", "Flat, warm neutral", "Honest — awareness is not a cure",
 "Alex seeing gears clearly; gears still spinning; awareness not stopping them",
 "Static. Gears still active; Alex's seeing them now is new. 2s."),

("The Brain Villain doesn't retire when you name him.",
 "Medium shot. Brain Villain is named — a nameplate appears: 'BRAIN VILLAIN.' He looks at it. Shrugs. Still here. Still doing the job. But something has shifted in the dynamic.",
 "Medium shot", "Flat, warm neutral", "The villain's position — named but not defeated",
 "Brain Villain with nameplate; shrug; still present but seen",
 "Static. Shrug is not defiant — more resigned. 2s."),

("But it changes something fundamental:",
 "Wide shot. Alex and Brain Villain — same frame, but Alex's posture is different now. He's watching the Brain Villain, not being led by him. The dynamic has shifted. The gears are visible to both.",
 "Wide shot", "Flat, warm neutral", "The shift — from unconscious to conscious",
 "Alex watching Brain Villain instead of being led; dynamic changed",
 "Static. Posture shift clear; awareness visible. 2s."),

("you stop blaming yourself for a system you didn't design.",
 "Medium shot. Alex. A weight lifts — not dramatically, but visibly. Expression: not relief exactly. More like clarity. The self-blame was always the wrong frame. The system was running before he arrived.",
 "Medium shot", "Flat, warm neutral", "The release — the most important reframe",
 "Alex with weight lifting; clarity expression; not dramatic relief",
 "Static. Weight visible as it lifts; expression: quiet clarity. 3s."),

("And that's the first condition for changing it.",
 "Wide shot. A single step on a staircase — the first one. Label: 'STEP 1: STOP BLAMING THE WRONG THING.' Above it, more steps — unlabeled, ahead. This is where the change begins.",
 "Wide shot", "Flat, warm white", "First condition — practical and achievable",
 "First staircase step labeled; more steps above; beginning visible",
 "Static. First step prominent; steps above present but unlabeled. 2s."),

("The next step isn't a budget.",
 "Wide shot. A budget spreadsheet icon — crossed out with a bold X. Not wrong. Just not the right first step. The system doesn't break with a spreadsheet.",
 "Wide shot", "Flat, white, red X", "What the solution is NOT — important clarity",
 "Budget icon crossed out; clear X",
 "Static. X draws through budget icon. 2s."),

("It's one decision that interrupts all three traps at the same time.",
 "Wide shot. A single key icon. Below it: three lock icons — one for each trap. The key fits all three. Label: 'ONE DECISION. THREE LOCKS.' End screen card begins to appear in corner.",
 "Wide shot", "Flat, white", "The promise — one intervention, three effects",
 "Single key icon; three trap lock icons; ONE DECISION THREE LOCKS label",
 "Static. End screen card appearing in corner. 3s."),

("Watch the next video — it shows exactly what that decision is,",
 "Medium shot. Alex directly to camera. End screen card now fully visible. Expression: composed, direct. He's done the work. The next step exists.",
 "Medium shot, direct address", "Flat, white, end screen visible", "Guide — explicit and named",
 "Alex to camera; end screen card fully visible",
 "Static. End screen card prominent. 2s."),

("and why most people never make it.",
 "Wide shot. A crowd of small character icons — most walking past the key. A few stopping. The key is available. Most don't stop. The curiosity gap: why?",
 "Wide shot", "Flat, white", "Final gap — why don't most people make this decision?",
 "Crowd icons; most walking past the key; few stopping",
 "Static. Crowd behavior visible; gap planted. 2s."),

("One decision. Three traps. The math might surprise you.",
 "Wide shot. Three trap gear icons. One key. A small calculator icon. Expression from Brain Villain: a small, reluctant nod. Even he respects the next move. Music fades.",
 "Wide shot", "Flat, warm fade", "Final seed — curiosity gap for next video",
 "Three traps; one key; Brain Villain reluctant nod; fade beginning",
 "Music fades. Brain Villain nod is deliberate and final. 3s."),

]  # end BEATS


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    TITLE = "3 Traps That Rewire Your Brain to Stay Broke"
    SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 11"
    LABEL = "STATE 1 — PRODUCTION DOCUMENT"

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run(SUBTITLE)
    r.bold = True
    r.font.size = Pt(14)

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run(LABEL)
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run(TITLE)
    r.bold = True
    r.italic = True
    r.font.size = Pt(14)

    doc.add_paragraph()

    SECTION_STARTS = {
        1:   "HOOK",
        18:  "TRAP 1 — THE REWARD TRAP",
        50:  "CTA",
        52:  "TRAP 2 — THE SAFE MONEY ILLUSION",
        81:  "TRAP 3 — THE FUTURE IS FAKE",
        115: "SYSTEM CLOSE",
        129: "IDENTITY CLOSE + GUIDE",
    }

    COL_LABELS = ["#", "NARRATION", "IMAGE PROMPT", "CAMERA", "LIGHTING",
                  "MOOD", "CHARACTER ACTION", "VIDEO MOTION"]
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

        cell_text(cells[0], str(beat_num), bold=True, sz=7)
        cell_text(cells[1], seg, bold=True, sz=7)
        cell_text(cells[2], f"{STYLE} {scene}", sz=7)
        cell_text(cells[3], cam, sz=7)
        cell_text(cells[4], light, sz=7)
        cell_text(cells[5], mood, sz=7)
        cell_text(cells[6], action, sz=7)
        cell_text(cells[7], video, sz=7)

    all_lines = [b[0] for b in BEATS]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = len(BEATS)

    doc.add_paragraph()
    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(
        f"END · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Mental_Traps_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
