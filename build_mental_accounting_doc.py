#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'Why Free Money Is the Most Expensive Money You Own' (Video 5 — Mental Accounting / Thaler)."""

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

("Think about the last time you received money you didn't expect.",
 "Medium shot, warm beige background. The main character stands facing slightly left, eyes closed in thought. Inside the transparent skull, the pink brain leans back in a relaxed thinking pose. A soft thought bubble begins to form above the character's head, empty for now.",
 "Medium shot, centered", "Warm beige, soft ceiling spotlight", "Intimate and introspective — the hook is addressed directly to the viewer",
 "Character thinking; brain in relaxed pose; empty thought bubble forming",
 "Static. The thought bubble slowly inflates above the character's head. 2s."),

("A bonus. A gift. A gambling win. An inheritance. A refund of any kind.",
 "Wide shot, white background. Four small floating icons appear in a horizontal row inside the thought bubble: a bonus envelope with a green plus sign, a gift box with ribbon, a poker chip, a will document. Each icon glows softly. Bold label above: 'UNEXPECTED MONEY.'",
 "Wide shot", "Flat, white", "Recognition — the viewer maps their own experience",
 "Four windfall icons floating in thought bubble row",
 "Static. Icons appear one by one from left to right; each pulses once on arrival. 3s."),

("Now think about how long it took you to spend it.",
 "Medium shot. The main character looks at a flat wall calendar. The calendar shows days being crossed off rapidly — fast, almost frantic. A green money icon appears on day 1 and is gone by day 3. Expression: slightly sheepish self-recognition.",
 "Medium shot", "Flat, warm", "Gentle self-incrimination — the viewer recognizes themselves",
 "Character watching calendar; money gone in days; sheepish expression",
 "Animated. Calendar pages flip quickly; money icon disappears by day 3. 3s."),

("Now think about how long it would take you to save that same amount from your monthly salary.",
 "Medium shot. Same calendar — but now a tiny coin is added each month, slowly. The accumulation bar beside it grows painfully slowly. Bold label: 'SAME AMOUNT.' Character watches with mild exasperation.",
 "Medium shot", "Flat, warm", "The contrast lands — the gap is felt before it is named",
 "Character watching slow monthly coin accumulation; exasperated expression",
 "Animated. One coin added per month; accumulation bar inches upward slowly. 3s."),

("The gap between those two numbers is not a personality flaw.",
 "Wide shot, white background. Two bars side by side: left bar labeled 'WINDFALL SPENT' — short, fast, red. Right bar labeled 'SALARY SAVED' — tall, slow, blue. A bold bracket spans the gap between them: 'NOT A FLAW.' The main character stands to the side, arms open.",
 "Wide shot", "Flat, white", "Relief and curiosity — the reframe begins",
 "Two contrasting bars; NOT A FLAW bracket; character arms open",
 "Static. Bracket appears; label drops in. Character opens arms. 2s."),

("It is one of the most studied phenomena in behavioral economics.",
 "Wide shot. A flat library interior — shelves of research papers and journals. A single spotlight illuminates a stack of papers at the center. Bold label on the spine: 'BEHAVIORAL ECONOMICS.' The brain character peeks from behind the stack, intrigued.",
 "Wide shot, library interior", "Warm spotlight on paper stack", "Authority established — this is science, not opinion",
 "Library shelves; spotlit paper stack; brain peeking from behind",
 "Static. Brain peeks further around the stack. 2s."),

("It has been replicated in dozens of countries, across every income level, in people who manage other people's money for a living.",
 "Wide diagram. A flat world map with glowing dots scattered across every continent. Below the map: three horizontal bars labeled 'ALL COUNTRIES,' 'ALL INCOME LEVELS,' 'ALL PROFESSIONS' — each fully filled green. Bold label: 'UNIVERSAL.'",
 "Wide diagram shot", "Flat, white, green highlights", "Scale — this is not a niche finding",
 "World map with global dots; three full green bars; UNIVERSAL label",
 "Static. Dots light up across the map one by one; bars fill. 3s."),

("And it is being used against you right now.",
 "Medium shot of the main character. The brain villain character appears over the character's shoulder — holding a small targeting reticle aimed directly at the character's wallet pocket. Smug expression. The character is unaware. Background fades to dark.",
 "Medium shot", "Flat, dark, targeting reticle glow", "Threat introduced — the pivot from curiosity to urgency",
 "Brain villain with targeting reticle on character's wallet; character unaware",
 "Static. Reticle locks onto the wallet with a soft click. 2s."),

# ── THE IMPOSSIBILITY ──────────────────────────────────────────────────────────

("Here is what makes this strange.",
 "Medium shot, direct address. The main character turns fully to face the camera. Expression: focused and composed. The brain inside the skull has resumed its upright, alert position. White background.",
 "Medium shot, direct address", "Flat, white", "Pivot — the analytical frame opens",
 "Character facing camera directly; brain alert and upright",
 "Static. Direct eye contact held steady. 2s."),

("Money is money.",
 "Close-up, white background. Two identical flat coin icons side by side. Between them: a bold equals sign. Nothing else. Clean, simple, almost mathematical.",
 "Close-up, centered", "Flat, white", "The axiom stated plainly — before it is destroyed",
 "Two identical coins with equals sign between them",
 "Static. Equals sign pulses once. 2s."),

("A hundred euros from your salary and a hundred euros from a bonus are identical objects.",
 "Wide shot. Two identical euro banknotes side by side. Left note labeled 'SALARY.' Right note labeled 'BONUS.' Both notes are identical in every detail — same color, same size, same value. A bold centered bracket: 'IDENTICAL.'",
 "Wide shot", "Flat, white", "The logical premise — stated before the paradox lands",
 "Two identical banknotes; SALARY / BONUS labels; IDENTICAL bracket",
 "Static. Bracket appears; both notes glow softly in sync. 2s."),

("They buy the same things. They have the same value. There is no rational reason to treat them differently.",
 "Wide diagram. Three rows of identical icons stacked: top row — same shopping cart (both notes buy the same things); middle row — same value meter (both at 100); bottom row — a balanced scale. Bold label: 'NO RATIONAL DIFFERENCE.'",
 "Wide stacked diagram", "Flat, white", "Logic complete — the paradox is ready",
 "Three rows of identical icons proving logical equivalence; label",
 "Static. Rows appear one by one from top to bottom. 3s."),

("And yet every human being on Earth does.",
 "Wide shot. A globe at center. Around it: a ring of small character figures of every kind — different clothes, different sizes, different contexts. Each has the same split thought bubble: SALARY (careful) vs BONUS (fast). Bold label: 'EVERY HUMAN BEING.'",
 "Wide shot, globe center", "Flat, white", "Universal — no exceptions",
 "Globe with ring of diverse characters; all showing same split thought bubble",
 "Static. Character ring appears; thought bubbles populate. 3s."),

("Not sometimes. Consistently. Predictably. In ways that can be measured, mapped, and — by the right industry — exploited.",
 "Wide shot, white background. Three bold stacked words: 'CONSISTENTLY.' / 'PREDICTABLY.' / 'EXPLOITABLY.' Each word drops in as its own statement. To the right: a small industry figure with a clipboard, already taking notes.",
 "Wide shot", "Flat, white", "Escalation — the threat is being quantified",
 "Three stacked words dropping in; industry figure with clipboard",
 "Static. Each word drops in with a half-second gap; industry figure ticks clipboard. 3s."),

("This is the story of how that happens. And who built their business model on top of it.",
 "Wide shot, dark background. A simple building silhouette with a bold label: 'BUILT ON YOUR BRAIN.' The main character stands small in front of it, looking up. The brain villain watches from a window at the top.",
 "Wide shot", "Dark, atmospheric", "The stakes established — a whole industry is waiting",
 "Building labeled BUILT ON YOUR BRAIN; character small below; brain at window",
 "Static. Building silhouette holds; brain figure appears at window. 3s."),

# ── THE DINNER PARTY ───────────────────────────────────────────────────────────

("It started not in a laboratory, but at a dinner party.",
 "Wide establishing shot, warm interior. A cosy flat cartoon dinner party scene — a round table set for dinner in the background, guests milling about. Warm amber ceiling light. A small label in the corner: 'ROCHESTER, 1975.' Intimate and social.",
 "Wide establishing shot", "Warm amber, soft interior light", "Unexpected origin — the science begins in an ordinary room",
 "Dinner party scene; round table in background; guests; 1975 label",
 "Static. Warm scene glows softly. 2s."),

("1975. Richard Thaler, a young economist at the University of Rochester, was hosting colleagues for dinner.",
 "Medium shot. A cartoon Thaler figure — young, slightly disheveled, warm expression, tie loosened — stands at the entrance of his living room welcoming three colleague figures. A bold label: 'RICHARD THALER · UNIVERSITY OF ROCHESTER.' Warm domestic light.",
 "Medium shot, entrance", "Flat, warm amber", "The protagonist arrives — young and unheroic",
 "Young Thaler welcoming colleagues; name label; warm domestic scene",
 "Static. Name label fades in. Thaler gestures welcomingly. 2s."),

("He had put a bowl of cashews on the coffee table as a pre-dinner snack.",
 "Close-up of a flat coffee table. A simple round bowl sits at the center, filled with cartoon cashews — cream-colored, slightly curved. Warm light catches the bowl. Nothing else on the table. Clean and ordinary.",
 "Close-up, centered overhead", "Flat, warm spotlight on bowl", "Ordinary setup — before the extraordinary observation",
 "Cashew bowl on coffee table; clean close-up",
 "Static. Bowl sits quietly at center. 2s."),

("His guests were eating them. Too enthusiastically.",
 "Medium-wide shot. Three colleague figures crowd around the coffee table, each reaching into the bowl with animated enthusiasm. Hands overlapping. The bowl is visibly depleting. Their expressions: pure snacking joy, completely unrestrained.",
 "Medium-wide shot", "Flat, warm", "The problem emerging — visible and slightly absurd",
 "Three guests raiding cashew bowl enthusiastically; depleting rapidly",
 "Animated. Hands reach in repeatedly; bowl level drops visibly. 3s."),

("Thaler worried they would ruin their appetite before the meal.",
 "Medium shot of Thaler standing to the side, looking at the guests, then glancing at the dining table set with a proper meal in the background. A small thought bubble: a dinner plate with a question mark above it. Expression: mild concern.",
 "Medium shot", "Flat, warm", "Practical worry — before the intellectual revelation",
 "Thaler glancing from guests to dinner table; worried thought bubble",
 "Static. Thaler's gaze moves from guests to dining table. 2s."),

("So he took the bowl away.",
 "Medium shot. Thaler lifts the cashew bowl cleanly off the coffee table with both hands. The guests watch. Simple action, ordinary moment. The table is now empty.",
 "Medium shot", "Flat, warm", "The action — simple and unremarkable",
 "Thaler lifting cashew bowl off table; guests watching",
 "Static. Thaler holds bowl; table now empty. 2s."),

("And the room relaxed.",
 "Wide shot of the room. The three guests — who were leaning forward eagerly a moment ago — have all visibly relaxed. Shoulders dropped. Postures open. One lets out a small exhale. Expressions: quiet relief. Warm light.",
 "Wide shot", "Flat, warm", "The paradox revealed — relief at losing something free",
 "Three guests visibly relaxing; shoulders dropping; quiet exhales",
 "Static. All three settle into relaxed postures simultaneously. 3s."),

("Here is what stopped him cold.",
 "Close-up of Thaler's face. His expression has shifted — the casual host expression replaced by something still and focused. A small visible freeze in the frame. The room behind him continues warmly but he is in a different mental space.",
 "Close-up", "Flat, warm", "The intellectual arrest — the moment of insight beginning",
 "Thaler's face freezing into focused stillness; room warm behind",
 "Static. Expression holds in frozen focus. 2s."),

("Every person in that room was a trained economist. And every single one of them had just expressed relief at having a free good removed from their presence.",
 "Wide shot. The three guests are now shown with floating credential labels: PhD ECONOMICS, UNIVERSITY PROFESSOR, ECONOMIC ADVISOR. Below each: a small relief icon (exhale emoji style). Bold connecting label: 'FREE GOOD REMOVED → RELIEF.'",
 "Wide shot", "Flat, warm", "The paradox named — rational people doing irrational things",
 "Guests with economist credentials floating; relief icons below each",
 "Static. Credential labels and relief icons appear simultaneously. 3s."),

("Rational agents don't do that.",
 "Wide shot, white background. Bold centered text: 'RATIONAL AGENTS DON'T DO THAT.' A large textbook icon with 'ECONOMICS 101' on the cover sits beside it, open to a relevant page. Clean and authoritative.",
 "Wide shot", "Flat, white", "The axiom violated — stated plainly",
 "Bold statement; economics textbook open beside it",
 "Static. Text appears with weight; textbook open. 2s."),

("If you wanted to stop eating cashews, you stopped. The bowl being there was irrelevant.",
 "Wide split panel. Left: a character reaching for the cashew bowl, then simply pulling their hand back — easy, clean. Right: the bowl sitting untouched, irrelevant. Bold label: 'SHOULD BE IRRELEVANT.'",
 "Wide split panel", "Flat, white", "The logical case — what should have happened",
 "Character easily stopping vs bowl sitting irrelevant; label",
 "Static. Both panels hold; label appears between them. 2s."),

("Except it wasn't. And everyone in the room knew it.",
 "Wide shot. The earlier relaxed guests are shown again — but now each has a small thought bubble containing a tiny cashew with a red minus sign. They knew. They all knew. Warm light returns.",
 "Wide shot", "Flat, warm", "The shared truth — wordless but universal",
 "Guests with thought bubbles showing cashew awareness; warm light",
 "Static. Thought bubbles appear simultaneously above each guest. 2s."),

("He wrote that moment in his notes.",
 "Close-up of an open notebook. Thaler's hand writes in bold cartoon script: 'BOWL REMOVED — RELIEF — WHY?' The pen underlines 'WHY?' twice. The rest of the page is blank — the question dominates.",
 "Close-up, overhead", "Flat, warm spotlight on notebook", "The question crystallizes — the research begins",
 "Thaler writing WHY? in notebook; underlined twice; page otherwise blank",
 "Static. Pen finishes writing; WHY? holds center stage. 2s."),

("He had just watched a room full of rational economists behave irrationally — and feel grateful about it.",
 "Wide shot, warm interior. The guests are shown again, relaxed, smiling, grateful — completely unaware of the paradox they just demonstrated. Thaler stands apart, notebook in hand, watching with a new kind of attention.",
 "Wide shot", "Flat, warm", "The observation complete — the paradox documented",
 "Grateful guests unaware; Thaler watching with notebook; new attention",
 "Static. Scene warm and ordinary; Thaler's focus is the only tension. 3s."),

("He spent the next decade trying to understand why.",
 "Wide shot. A simple desk scene with a wall calendar behind Thaler. Years flip: 1975 → 1976 → 1977 → ... → 1985. Papers accumulate. Books multiply. Thaler's expression across the years: determined, absorbed, occasionally frustrated.",
 "Wide shot, decade montage", "Flat, warm office light", "Time and obsession — the decade of pursuit",
 "Calendar years flipping; papers accumulating; Thaler's determined expression",
 "Animated. Calendar years flip steadily; paper piles grow. 3s."),

# ── THE THEORY ─────────────────────────────────────────────────────────────────

("Mainstream economics had one central assumption: people make decisions based on their total wealth.",
 "Wide shot. A large flat economics textbook open at the center of the frame. A highlighted passage reads: 'AGENTS OPTIMIZE BASED ON TOTAL WEALTH.' Bold label below: 'THE CENTRAL ASSUMPTION.' Clean academic white.",
 "Wide shot", "Flat, white", "The establishment's position — before it is dismantled",
 "Open textbook with highlighted central assumption; label below",
 "Static. Highlighted text glows steadily. 2s."),

("Not where the money came from. Not what category it was in. Total wealth.",
 "Wide diagram. Three labeled categories crossed out with red X marks: 'WHERE IT CAME FROM ✗' / 'WHAT CATEGORY ✗' / 'CONTEXT ✗.' Below them, one surviving label circled in blue: 'TOTAL WEALTH ✓.'",
 "Wide diagram", "Flat, white, red X marks", "The model made explicit — and fragile",
 "Three X'd categories; one surviving TOTAL WEALTH circled",
 "Static. X marks appear one by one; TOTAL WEALTH circle last. 3s."),

("Thaler kept finding violations.",
 "Medium shot of Thaler at his desk, a clipboard in hand. Each item on the clipboard has a red X replacing what should be a checkmark. His expression: the particular focus of someone who keeps finding the same impossible thing.",
 "Medium shot", "Flat, warm office", "Accumulation of evidence — the violations multiply",
 "Thaler with clipboard full of red X violations; focused expression",
 "Static. Clipboard covered in red X marks; Thaler taps one with his pen. 2s."),

("People would walk twenty minutes to save five euros on a fifteen-euro item — but would not cross the street to save five euros on a five-hundred-euro purchase.",
 "Wide split panel. Left: a character cheerfully walking a long road to a small shop to save €5 on a €15 item — a big effort for a small saving. Right: the same character standing beside a €500 store, refusing to cross the street to save €5 — small effort, same saving. Bold bracket: 'IDENTICAL SAVING. OPPOSITE BEHAVIOR.'",
 "Wide split panel", "Flat, white", "The violation made visual — immediately absurd",
 "Long walk for €5 on €15 left; refusing to cross street for €5 on €500 right",
 "Static. Both panels hold; bracket appears; absurdity is immediate. 3s."),

("The saving was identical. The effort was identical. The behavior was completely different.",
 "Wide stacked diagram. Three rows: 'SAVING: €5 = €5 ✓' / 'EFFORT: DIFFERENT ✗' — wait, no. 'SAVING: IDENTICAL ✓' / 'EFFORT: IDENTICAL ✓' / 'BEHAVIOR: COMPLETELY DIFFERENT ✗.' The bottom row breaks the pattern with a bold red X.",
 "Wide stacked diagram", "Flat, white, red bottom row", "The logic of the paradox — laid out precisely",
 "Three-row comparison; top two match; bottom row breaks with red X",
 "Static. Rows appear top to bottom; red X on bottom row lands hard. 3s."),

("He noticed that people held expensive bottles of wine in their cellars for decades — wine they would never sell for what it was worth and would never pay what it now costs to replace.",
 "Wide shot of a flat wine cellar interior. Dusty bottles line the shelves, each with a price tag. One prominent bottle has two floating labels: 'WOULD NOT SELL FOR: €200' and 'WOULD NOT PAY: €200.' The same number on both tags. Thaler stands in the doorway, observing.",
 "Wide shot, cellar interior", "Flat, dim warm cellar light", "Another violation — the irrationality is specific and vivid",
 "Wine cellar; bottle with identical would-not-sell / would-not-pay tags; Thaler observing",
 "Static. Both price tags visible and equal; Thaler notes quietly. 3s."),

("They held both positions simultaneously. Rational agents cannot do that.",
 "Wide shot, white background. A simple Venn diagram. Left circle: 'WOULD NOT SELL AT MARKET PRICE.' Right circle: 'WOULD NOT BUY AT MARKET PRICE.' The overlap section is highlighted red and labeled: 'IMPOSSIBLE — BUT REAL.'",
 "Wide diagram shot", "Flat, white, red overlap", "The formal impossibility — the research is building",
 "Venn diagram with impossible overlap highlighted; IMPOSSIBLE BUT REAL label",
 "Static. Overlap section highlights; label appears. 2s."),

("He was seeing the same thing everywhere. People were not tracking total wealth. They were tracking accounts.",
 "Wide shot. Thaler surrounded by floating examples — the cashews, the calculator, the wine, the grocery store — each connected by a line to a central insight bubble: 'MENTAL ACCOUNTS.' Bold and central.",
 "Wide shot", "Flat, warm", "The pattern recognized — the theory crystallizes",
 "Thaler surrounded by examples; all connecting to MENTAL ACCOUNTS bubble",
 "Static. Connection lines appear; MENTAL ACCOUNTS bubble glows. 3s."),

("He called it mental accounting.",
 "Medium shot. Thaler at a chalkboard. He writes in bold: 'MENTAL ACCOUNTING.' The letters are large, deliberate, underlined. His expression: the satisfaction of naming something real.",
 "Medium shot", "Flat, warm neutral", "The naming — the concept becomes real",
 "Thaler writing MENTAL ACCOUNTING at chalkboard; underlined; satisfied expression",
 "Static. Term is bold and prominent at chalkboard center. 2s."),

("The economics profession told him he was wasting everyone's time.",
 "Wide shot. A conference room of economics professor figures — suits, glasses, arms crossed. One prominent figure at the head of the table points dismissively toward a door. A small Thaler figure stands with his cashew-bowl insight, looking quietly determined.",
 "Wide shot, conference room", "Flat, institutional cold light", "The dismissal — the underdog moment",
 "Conference room of dismissive economists; pointing figure; determined Thaler",
 "Static. Dismissal gesture is prominent; Thaler's expression holds steady. 3s."),

# ── THE EXPERIMENTS ────────────────────────────────────────────────────────────

("In 1985, Thaler ran the experiment that ended the argument.",
 "Wide shot. A clean research lab table. A simple setup: two scenario cards face-down on the table. A clock on the wall shows 1985. Thaler stands beside the table with quiet confidence. Label: 'THE EXPERIMENT · 1985.'",
 "Wide shot, lab table", "Flat, cool lab light", "Anticipation — the decisive test",
 "Lab table with two scenario cards; 1985 clock; confident Thaler",
 "Static. Date label appears; Thaler's stance is composed. 2s."),

("You have bought a twenty-euro ticket to see a concert. On the way, you lose the ticket.",
 "Wide split scene. Left half: the character holds a concert ticket — bold €20 visible. Right half: the same character walking, the ticket slipping from a pocket and falling to the ground. Expression shifts from happy to dismayed.",
 "Wide split scene", "Flat, warm", "The setup — specific and relatable",
 "Character with ticket left; ticket falling from pocket right",
 "Static. Ticket falls in right panel; dismayed expression. 2s."),

("Do you buy another?",
 "Medium shot of the character standing at a box office window. The ticket seller holds up a new ticket. The character hesitates — thought bubble shows an internal calculation. A bold question mark floats above. The moment is suspended.",
 "Medium shot", "Flat, warm", "The question — the viewer asks themselves before the answer comes",
 "Character hesitating at box office; thought bubble calculating; question mark",
 "Static. Question mark pulses once. 2s."),

("Most people say no.",
 "Wide shot, white background. Bold text: 'MOST PEOPLE: NO.' A large red X dominates the right side. The character figure turns away from the box office, empty-handed. Clean, definitive.",
 "Wide shot", "Flat, white, red X", "The answer — decisive and surprising to some",
 "Bold NO text; red X; character turning away from box office",
 "Static. Red X drops in; character turns. 2s."),

("Same situation. You are on your way to buy a twenty-euro ticket at the door. On the way, you lose a twenty-euro note from your wallet.",
 "Wide split scene. Left half: character walking toward a concert venue, wallet visible. Right half: a €20 note slips from the wallet and falls to the ground. The loss is identical — but the source is different.",
 "Wide split scene", "Flat, warm", "The parallel — the viewer begins to see it",
 "Character walking toward venue left; €20 note falling from wallet right",
 "Static. Note falls; character notices with dismay. 2s."),

("Do you still go?",
 "Medium shot of the same character, now standing at the venue door. Ticket still available. The character pauses — thought bubble shows a brief calculation. Same question mark floats above. The moment mirrors the earlier one exactly.",
 "Medium shot", "Flat, warm", "The mirror question — the comparison is primed",
 "Character at venue door; thought bubble; question mark floating",
 "Static. Question mark pulses — echoing the earlier beat. 2s."),

("Most people say yes.",
 "Wide shot, white background. Bold text: 'MOST PEOPLE: YES.' A large green checkmark. The character figure buys the ticket, enters the venue. Clean, definitive — and jarring against the previous answer.",
 "Wide shot", "Flat, white, green check", "The contradiction — stated plainly",
 "Bold YES text; green check; character buying ticket and entering",
 "Static. Green check appears; contrast with the red X is immediate. 2s."),

("In both cases you have lost twenty euros. In both cases attending costs another twenty. The math is identical.",
 "Wide diagram. Two parallel equation lines: 'SCENARIO A: Lost €20 + Pay €20 = €40 spent' / 'SCENARIO B: Lost €20 + Pay €20 = €40 spent.' Both lines identical. Bold label: 'MATHEMATICALLY IDENTICAL.' The equations glow in sync.",
 "Wide diagram shot", "Flat, white", "The math — undeniable and exposed",
 "Two identical equations; MATHEMATICALLY IDENTICAL label",
 "Static. Both equations glow in sync; label appears. 3s."),

("But in the first case, the concert budget — the mental account — has already been spent.",
 "Wide shot. A flat mental ledger appears — a simple account book. The CONCERT ACCOUNT page shows: 'BALANCE: €20. STATUS: SPENT.' A red closed-folder icon appears beside it. The account is closed.",
 "Wide shot", "Flat, white, red closed folder", "The mental account made visible — the mechanism begins",
 "Mental ledger; CONCERT ACCOUNT spent and closed; red folder",
 "Static. Red closed-folder icon appears; account balance zeroed. 2s."),

("Paying again feels like paying forty euros for a twenty-euro experience.",
 "Close-up of a concert ticket with a price tag. The tag reads €20 — but a second hand is adding a second €20 sticker on top, making it €40. The character stares at it, pained. Expression: this is wrong.",
 "Close-up", "Flat, white, double price tag", "The felt cost — visceral and specific",
 "Concert ticket with €20 becoming €40 via double sticker; pained expression",
 "Static. Second price sticker appears; character's pain expression holds. 2s."),

("In the second case, the twenty euros came from the general cash account. The concert account is untouched.",
 "Wide shot. Two mental ledgers side by side. Left: GENERAL CASH ACCOUNT — shows a €20 debit, still open, plenty of balance remaining. Right: CONCERT ACCOUNT — untouched, full, green. The concert account is intact.",
 "Wide shot, dual ledgers", "Flat, white, green CONCERT account", "The account separation — made visible",
 "Two ledgers; CASH debited left; CONCERT untouched green right",
 "Static. Both ledgers visible; contrast is clear. 3s."),

("Same money. Same outcome. Completely different decision.",
 "Wide shot, white background. Three bold stacked lines: 'SAME MONEY.' / 'SAME OUTCOME.' / 'COMPLETELY DIFFERENT DECISION.' The first two lines are calm and blue. The third line is bold red — the rupture.",
 "Wide shot", "Flat, white, red third line", "The core paradox distilled — three lines, complete",
 "Three stacked lines; first two blue calm; third red dissonant",
 "Static. Lines appear one at a time; third lands with color contrast. 3s."),

("Thaler ran the same logic through bonuses, gambling wins, inheritances, gifts. Every single time, the same result.",
 "Wide diagram. Four new scenarios in small panels — a bonus envelope, a casino win, an inheritance document, a gift box — each with the same outcome arrow: 'SPENT FASTER.' A bold unifying label: 'EVERY TIME. SAME RESULT.'",
 "Wide diagram, four panels", "Flat, white", "Universality established — the pattern holds across contexts",
 "Four windfall types; each with SPENT FASTER arrow; unified label",
 "Static. Four panels appear; outcome arrows point right simultaneously. 3s."),

("The brain does not process money as money.",
 "Close-up of the brain character inside the skull, shaking its head firmly. Beside it: a bold equation with a red X: 'MONEY ≠ MONEY (to the brain).' Expression: the smug satisfaction of knowing something the character doesn't.",
 "Close-up", "Flat, white", "The mechanism stated — from inside the skull",
 "Brain character shaking head; MONEY ≠ MONEY label with red X",
 "Static. Brain shakes head; equation holds. 2s."),

("It processes money as money-from-here or money-from-there.",
 "Wide diagram. A central BRAIN icon. Two arrows lead outward: left arrow labeled 'MONEY-FROM-HERE (EARNED)' in muted blue; right arrow labeled 'MONEY-FROM-THERE (WINDFALL)' in warm gold. The two streams are distinct and separate.",
 "Wide diagram shot", "Flat, white, dual stream colors", "The filing system exposed — two streams, not one",
 "Brain with two separate money streams; EARNED blue / WINDFALL gold",
 "Static. Both arrows appear; streams hold separate colors. 3s."),

("And the behavior follows the account, not the amount.",
 "Wide diagram. Two scenarios at bottom: ACCOUNT A → CAREFUL BEHAVIOR. ACCOUNT B → FAST BEHAVIOR. The amount in both is identical (€500 each), shown explicitly. The account label is the only variable. Bold label: 'ACCOUNT DETERMINES BEHAVIOR.'",
 "Wide diagram shot", "Flat, white", "The rule stated — the key insight crystallized",
 "Two accounts; identical amounts; different behavior outcomes; rule label",
 "Static. Rule label drops in boldly. 3s."),

# ── THE MECHANISM ──────────────────────────────────────────────────────────────

("Here is what is happening inside.",
 "Medium shot. The main character turns to camera with an explanatory gesture — one hand open toward the viewer. The brain inside the skull sits forward, ready to demonstrate. White background.",
 "Medium shot, direct address", "Flat, white", "The mechanism section opens — the explanation is about to go deeper",
 "Character with open explanatory gesture; brain leaning forward ready",
 "Static. Character's gesture holds invitingly. 2s."),

("When you earn money through labor — through time, through effort, through sacrifice — it carries a cost signal.",
 "Wide shot. The character working — at a desk, clearly tired but focused. Each euro earned has a small red signal icon attached: a tiny exclamation mark. The earned money is tagged. Warm work lighting.",
 "Wide shot, work setting", "Flat, warm work light", "Earned money has weight — felt and marked",
 "Character working; each earned euro with red cost signal icon attached",
 "Static. Earned euros appear with red signal tags. 2s."),

("Your nervous system registered what it took to produce it. Every euro spent from that account costs something real and felt.",
 "Close-up split panel. Left: the nervous system diagram — a simple signal line from effort to brain to money tag. Right: the character spending from the earned account, a small wince visible. Label: 'REAL AND FELT.'",
 "Close-up split panel", "Flat, white", "The physical reality of earned spending",
 "Nervous system signal left; character wincing at earned spend right; label",
 "Static. Signal line pulses; wince expression on spending. 2s."),

("When money arrives without labor — a bonus, a gift, a gambling win — it does not carry that signal.",
 "Wide shot. Three money arrivals from above — a bonus envelope, a gift box, a casino chip — falling gently into the character's hands. Each is clean, untagged, no red signal icon. They arrive without cost.",
 "Wide shot", "Flat, warm gold arrival light", "Windfall money is weightless — no signal attached",
 "Three windfalls arriving from above; no red signal tags; clean arrival",
 "Static. Three items descend gently; character receives them without wincing. 3s."),

("The brain files it differently. Money in that account moves faster, easier, with almost no friction.",
 "Wide shot. The brain character takes the windfall money and files it in a gold-colored folder labeled 'WINDFALL.' The folder opens easily, money flows in smoothly. Contrasted with the blue 'EARNED' folder which requires more deliberate handling.",
 "Wide shot", "Flat, white, gold vs blue folders", "The filing made visible — two different systems",
 "Brain filing windfall in gold folder smoothly; contrast with careful earned folder",
 "Static. Gold folder opens easily; money flows in. 2s."),

("Thaler called this the pain of paying.",
 "Medium shot. Thaler at his chalkboard again. He writes in bold: 'PAIN OF PAYING.' Below it, a simple diagram: a payment arrow with a lightning bolt crossing it — the jolt of spending. His expression: this is the key.",
 "Medium shot", "Flat, warm neutral", "The naming of the core mechanism",
 "Thaler writing PAIN OF PAYING at chalkboard; lightning bolt diagram",
 "Static. Term is bold; lightning bolt diagram appears below. 2s."),

("Cash hurts. You feel it leave your hand.",
 "Close-up. The character's hand extends with a cash note. As it leaves the hand, a small red pain pulse radiates from the palm. The expression: a slight wince. Physical and immediate.",
 "Close-up", "Flat, white, red pain pulse", "The physical experience — everyone recognizes it",
 "Hand releasing cash; red pain pulse from palm; wince expression",
 "Static. Pain pulse radiates from palm; expression winces slightly. 2s."),

("Cards reduce the pain — the money goes later, abstractly, somewhere in the future.",
 "Wide shot. Same purchase — but now the character taps a card. The pain pulse is smaller, fainter, almost invisible. A ghostly calendar floats in the background — the money will leave later, abstractly. Expression: easy, unconcerned.",
 "Wide shot", "Flat, warm, faint future calendar", "Reduced friction — the mechanism of cards",
 "Card tap; faint pain pulse; ghostly future calendar; relaxed expression",
 "Static. Card tap; pain pulse barely visible; calendar ghost fades in. 2s."),

("Casino chips reduce it further — they no longer look like money at all.",
 "Wide shot. The character at a casino table, surrounded by chips. Reaching for a stack of chips — no pain pulse at all. Zero. The chips look like colorful discs, nothing like money. The character's expression: completely uninhibited.",
 "Wide shot, casino table", "Flat, warm casino light", "Chips eliminate the signal — money becomes play",
 "Character at casino with chips; zero pain pulse; uninhibited expression",
 "Static. Character reaches for chips; no pain response visible. 2s."),

("Contactless payment nearly eliminates it entirely.",
 "Close-up of a phone tapping a payment terminal. A single number: €0.00 pain signal (shown as a nearly flat line on a small monitor beside the terminal). The transaction is invisible, instant, painless. Expression: not even registered.",
 "Close-up", "Flat, white, near-zero signal", "The final step — frictionless money",
 "Phone tap; near-zero pain signal on monitor; transaction barely registered",
 "Static. Tap happens; signal line nearly flat. 2s."),

("Each step away from physical, earned, hard-counted money lowers the pain signal.",
 "Wide descending diagram. Four payment methods left to right: CASH → CARD → CHIPS → CONTACTLESS. Below each: a descending pain signal bar — tall red for cash, progressively shorter and cooler-toned toward contactless. A bold downward arrow: 'PAIN DECREASES.'",
 "Wide diagram shot", "Flat, white, descending colors", "The spectrum made visible — the design of frictionlessness",
 "Four payment methods with descending pain bars; downward arrow",
 "Static. Bars appear left to right in descending height. 3s."),

("Lower pain means higher spending.",
 "Wide diagram. Two inverse bars: PAIN SIGNAL (going down) on the left, SPENDING AMOUNT (going up) on the right. They move in perfect opposition. Bold label: 'INVERSE RELATIONSHIP.'",
 "Wide diagram shot", "Flat, white, inverse bars", "The equation — simple and alarming",
 "Two inverse bars; pain down / spending up; INVERSE RELATIONSHIP label",
 "Static. Both bars shown in opposition; label appears. 2s."),

("The account determines the behavior. Always.",
 "Wide shot, white. Bold centered statement: 'THE ACCOUNT DETERMINES THE BEHAVIOR.' Below it, in even bolder font: 'ALWAYS.' The brain character stands beside the statement, arms crossed, smugly certain.",
 "Wide shot", "Flat, white", "The rule — stated with finality",
 "Bold statement; ALWAYS beneath; brain character arms crossed smugly",
 "Static. ALWAYS appears after main statement; brain holds pose. 2s."),

# ── THE POPULAR MISREADING ─────────────────────────────────────────────────────

("Everyone who hears this arrives at the same conclusion.",
 "Wide shot. A row of five diverse character figures, all with identical thought bubbles above their heads — the same conclusion forming simultaneously. The sameness is the point. White background.",
 "Wide shot", "Flat, white", "The universal misread — everyone makes the same mistake",
 "Row of five characters with identical conclusion thought bubbles forming",
 "Static. All five thought bubbles appear simultaneously. 2s."),

("So some people are just impulsive. Some people lack discipline. Some people cannot manage money.",
 "Wide shot, white background. Three small character stereotypes in a row with floating labels: 'IMPULSIVE,' 'UNDISCIPLINED,' 'CAN'T MANAGE MONEY.' Each looks slightly ashamed. The labels are condescending and reductive.",
 "Wide shot", "Flat, white", "The wrong conclusion stated — before it is destroyed",
 "Three stereotyped characters with reductive shame labels",
 "Static. Labels float above each character. 2s."),

("That is not what the research shows.",
 "Wide shot, white background. A massive red X draws itself across the three stereotyped characters and their labels. Bold text replaces them: 'THAT IS NOT WHAT THE RESEARCH SHOWS.' Clean, decisive.",
 "Wide shot", "Flat, white, red X", "The reframe — delivered with authority",
 "Red X across stereotypes; replacement statement bold and clear",
 "Static. Red X draws across; replacement text appears. 2s."),

("Thaler ran these experiments on economists. On financial advisors. On people who managed other people's money professionally.",
 "Wide shot. Three professional figures in a row — economist with textbooks, financial advisor with charts, fund manager with portfolio. All with impressive credentials floating above. All three have mental accounting icons active in their heads.",
 "Wide shot", "Flat, warm professional tones", "The experts are not immune — the paradox is universal",
 "Three credentialed professionals; mental accounting icons active in each",
 "Static. Credentials and mental account icons visible simultaneously. 3s."),

("The mental accounts showed up in all of them.",
 "Wide diagram. The same mental accounting dual-folder system (EARNED blue / WINDFALL gold) appears inside each of the three professional figures' heads — identical in all three. Bold label: 'ALL OF THEM.'",
 "Wide diagram shot", "Flat, white", "Universality confirmed — expertise offers no protection",
 "Mental accounting folders visible in all three professional heads; ALL OF THEM label",
 "Static. Folders appear in all three heads simultaneously; label appears. 3s."),

("This is not a character flaw. It is architecture.",
 "Wide shot, white background. Two bold statements side by side: 'CHARACTER FLAW ✗' crossed out in red / 'ARCHITECTURE ✓' in solid blue. Below, a simple building blueprint — the structure is engineered, not chosen.",
 "Wide shot", "Flat, white", "The reframe complete — structural not moral",
 "CHARACTER FLAW crossed out; ARCHITECTURE confirmed; blueprint below",
 "Static. Cross-out appears first; ARCHITECTURE label second; blueprint fades in. 3s."),

("Your brain was never designed to treat money as a fungible, interchangeable unit of abstract value.",
 "Wide shot. The brain character inside the skull shakes its head at a floating abstract currency symbol — a generic coin with a question mark. Expression: genuinely confused, not dismissive. The brain was never built for this.",
 "Wide shot", "Flat, white", "Evolutionary honesty — the brain's real design",
 "Brain character confused by abstract currency symbol; head shaking",
 "Static. Brain shakes head; abstract symbol floats unanswered. 2s."),

("It was designed to track resources the way a hunter tracks resources — by source, by effort, by context.",
 "Wide shot. A flat forest scene. A hunter figure tracks game — but each resource is labeled: THIS KILL (effort-tagged), FOUND FOOD (no tag), SHARED MEAL (context-tagged). The tracking system is visible and specific.",
 "Wide shot, forest setting", "Flat, natural warm tones", "The evolutionary origin — specific and credible",
 "Hunter tracking labeled resources by source/effort/context in forest",
 "Static. Resource labels appear as hunter approaches each. 3s."),

("A kill you made yourself is worth more than an animal you found already dead. The effort cost something real.",
 "Wide split panel. Left: hunter with a self-made kill — glowing with effort-value tag, held with pride. Right: hunter finding a dead animal — no glow, no tag, treated with less reverence. Same animal. Different value.",
 "Wide split panel", "Flat, natural tones", "The evolutionary logic — effort creates perceived value",
 "Hunter with self-kill (glowing) left vs found animal (no glow) right",
 "Static. Effort-value glow contrast is immediate. 2s."),

("Money is the modern version of the same system.",
 "Wide shot. The forest scene morphs smoothly into a modern city scene. The hunter figure becomes the main character. The resource labels stay identical: EARNED (effort-tagged), BONUS (no tag). The system is the same — only the wrapper changed.",
 "Wide shot, forest-to-city morph", "Flat, transitioning warm tones", "The connection — ancient system, modern context",
 "Forest morphing into city; hunter becoming character; labels unchanged",
 "Static. Morph holds at midpoint; both contexts visible. 3s."),

("And the system has been mapped.",
 "Wide shot, white background. A complete diagram of the mental accounting system — all accounts labeled, all triggers identified, all behaviors charted. Every entry point marked. A corporate figure stands over the map with a satisfied expression. The map is not academic. It is operational.",
 "Wide shot", "Flat, white", "The threat returns — the system is in enemy hands",
 "Complete mental accounting map; corporate figure with satisfied expression over it",
 "Static. Map is fully detailed; corporate figure's satisfaction is clear. 3s."),

# ── THE INDUSTRY ───────────────────────────────────────────────────────────────

("In the 1980s, casinos discovered something.",
 "Wide establishing shot of a flat 1980s casino floor — card tables, slot machines, soft neon light. A group of casino management figures in suits huddle around a table, examining data. Label: '1980s.'",
 "Wide establishing shot", "Flat, 1980s neon warmth", "The industry story begins — specific and grounded",
 "1980s casino floor; management figures examining data; era label",
 "Static. Casino scene glows softly; huddle of figures focused on data. 2s."),

("When chips look and feel too much like real money, players slow down.",
 "Wide shot. A casino table. A player reaches for chips that look very coin-like — heavy, metal-looking, realistic. The player's hand hesitates. A pain signal fires faintly from the palm. A small graph beside the table: BET SIZE drops when chips feel real.",
 "Wide shot", "Flat, casino light, faint pain signal", "The discovery — the friction point identified",
 "Player hesitating at realistic chips; faint pain signal; bet-size graph dropping",
 "Static. Hesitation is visible; graph shows correlation. 3s."),

("So they engineered the texture. The weight. The color.",
 "Close-up of a casino chip design process — a flat blueprint panel. Three separate design iterations shown: texture test, weight calibration dial, color spectrum. Each labeled with a deliberate design choice. This is engineering, not aesthetics.",
 "Close-up, blueprint layout", "Flat, technical light", "The deliberate design — every property chosen",
 "Chip design blueprint; texture, weight, color engineering panels",
 "Static. Three design panels crisp and labeled. 2s."),

("The exact sensory point where a chip feels real enough to hold and fake enough to throw across a table.",
 "Wide shot. A chip in a hand — the perfect chip. A split diagram shows: too real (left, player hesitates) / too fake (left player ignores) / OPTIMAL ZONE (center, player throws freely). The optimal chip sits in the center zone.",
 "Wide shot, sensory diagram", "Flat, white, optimal zone highlighted", "The engineering target — specific and chilling",
 "Three-zone chip diagram; optimal zone highlighted; freely thrown chip at center",
 "Static. Optimal zone highlighted; chip in center glows. 2s."),

("That is not a design aesthetic. That is applied mental accounting.",
 "Wide shot, white background. A casino chip blueprint with a bold stamp across it: 'APPLIED MENTAL ACCOUNTING.' The corporate figure from earlier stands beside it with arms crossed. The stamp is official. This is documented.",
 "Wide shot", "Flat, white, bold stamp", "The naming — the exploitation is identified",
 "Chip blueprint with APPLIED MENTAL ACCOUNTING stamp; corporate figure",
 "Static. Stamp appears with weight; corporate figure holds steady. 2s."),

("The same logic runs every loyalty points program you have ever been enrolled in.",
 "Wide shot. A row of loyalty cards — airline, coffee shop, hotel, supermarket. Each card glows faintly gold: the windfall account is activated. The character holds one with a familiar, slightly proud expression. They feel rewarded.",
 "Wide shot", "Flat, white, gold glow on cards", "Universal application — the viewer's own experience",
 "Row of loyalty cards glowing gold; character holding one with pride",
 "Static. All cards glow simultaneously; character's expression: familiar recognition. 3s."),

("The points feel like a bonus — like money you found rather than money you earned.",
 "Wide split panel. Left: points accumulating — labeled 'FOUND MONEY' with no cost signal, gold and light. Right: the equivalent cash spent to earn those points — labeled 'EARNED MONEY' with a cost signal, blue and weighty. Same value. Different feel.",
 "Wide split panel", "Flat, white, gold left / blue right", "The misclassification — points are not windfalls",
 "Points as found money (gold, light) vs cash cost (blue, heavy); same value",
 "Static. Both panels hold; value equivalence labeled. 3s."),

("So you spend them on upgrades you would never pay cash for. The friction disappears. The margin increases.",
 "Wide shot. Three panels in sequence: character upgrading a flight seat with points (happy, no hesitation) → same upgrade offered in cash (character recoils, declines) → airline margin meter rising. The sequence is tight and complete.",
 "Wide triptych", "Flat, white", "The exploit in action — the behavior and the profit",
 "Points upgrade (happy) → cash upgrade (refuses) → airline margin rising",
 "Static. Three panels in sequence; margin meter rises last. 3s."),

("The same logic runs the bonus industry.",
 "Wide shot. A corporate payroll scene. Two compensation structures side by side: HIGH BASE SALARY (steady, weighted, blue) vs LOW BASE + BIG BONUS (bonus arrives gold, treated as windfall). The total is identical. The mental account is not.",
 "Wide shot", "Flat, white, blue vs gold compensation", "Bonus structure is a mental accounting tool",
 "Two compensation structures; identical total; different mental account treatment",
 "Static. Both structures present; total amounts match; account treatment differs. 2s."),

("The same logic runs the consumer credit industry. Not the interest rate. The friction removal.",
 "Wide shot. A credit industry diagram. The interest rate percentage sits in a corner, deliberately small. Center stage: a large FRICTION REMOVAL system diagram — the real product. Bold label: 'THE PRODUCT IS THE FRICTION REMOVAL.'",
 "Wide shot, industry diagram", "Flat, white", "The reframe — credit's real mechanism named",
 "Credit diagram with friction removal center-stage; interest rate minimized; label",
 "Static. Friction removal diagram dominates; interest rate is peripheral. 3s."),

("Every contactless payment, every one-click purchase, every subscription that bills silently in the background is an engineered reduction of the pain of paying.",
 "Wide shot. Three panels: contactless terminal (tap — pain zero), one-click button (click — pain zero), subscription icon pulsing quietly (billing silently — pain zero). Each has a pain meter at zero. Bold unifying label: 'ENGINEERED PAINLESSNESS.'",
 "Wide triptych", "Flat, white, zero pain meters", "Three weapons — named and shown",
 "Three payment mechanisms; each with zero pain meter; unified label",
 "Static. All three pain meters read zero simultaneously; label appears. 3s."),

("The account determines the behavior. The behavior determines the profit.",
 "Wide diagram. A three-link chain: ACCOUNT → BEHAVIOR → PROFIT. Each link solid, connected, inevitable. The profit end glows green. Bold label: 'THE CHAIN.'",
 "Wide diagram shot", "Flat, white, green profit end", "The mechanism complete — the chain is closed",
 "Three-link chain: ACCOUNT → BEHAVIOR → PROFIT; profit end glows",
 "Static. Chain links appear left to right; profit end glows last. 2s."),

("Mental accounting appeared in academic literature in 1985. These industries had working versions of it long before anyone published a paper.",
 "Wide timeline. A horizontal line marked: 'CASINOS — 1950s' / 'CREDIT CARDS — 1960s' / 'LOYALTY PROGRAMS — 1970s' / 'ACADEMIC PAPER — 1985.' Each industry marker appears before the academic marker. Bold label: 'THEY KNEW FIRST.'",
 "Wide timeline shot", "Flat, white", "The industrial precedence — the science confirmed what industry already practiced",
 "Timeline with industry markers predating academic publication; THEY KNEW FIRST label",
 "Static. Industry markers appear first; academic marker appears last; label lands. 3s."),

# ── THE REAL CONCLUSION ────────────────────────────────────────────────────────

("Here is what Thaler actually concluded.",
 "Medium shot. Thaler figure returns — now older, more settled, at a clean desk. Expression: calm and precise. He holds a single index card with his conclusion on it, face-down. The character watches from the side. The room is quiet.",
 "Medium shot", "Flat, warm neutral", "The real conclusion arrives — unhurried",
 "Older Thaler at desk; conclusion card face-down; character watching",
 "Static. Thaler's expression is composed and certain. 2s."),

("Not that humans are broken. That humans are predictable.",
 "Wide shot, white background. Two bold statements side by side: 'NOT BROKEN' (with a gentle crossing-out of a broken icon) / 'PREDICTABLE' (with a steady waveform icon). The second statement is the more powerful one. Thaler stands between them.",
 "Wide shot", "Flat, white", "The reframe — more useful than condemnation",
 "NOT BROKEN vs PREDICTABLE contrast; Thaler between them",
 "Static. Both statements appear; PREDICTABLE carries more visual weight. 2s."),

("The accounts are consistent. The triggers are consistent. The behavior that follows is consistent.",
 "Wide stacked diagram. Three rows, each with a steady green consistency waveform: 'ACCOUNTS: CONSISTENT ✓' / 'TRIGGERS: CONSISTENT ✓' / 'BEHAVIOR: CONSISTENT ✓.' All three waveforms in sync. Orderly, measurable, real.",
 "Wide stacked diagram", "Flat, white, green waveforms", "Predictability is the opportunity — not the problem",
 "Three consistent waveform rows; all green and synchronized",
 "Static. All three waveforms appear and hold in steady sync. 3s."),

("Which means if you can see the accounts, you can audit them.",
 "Wide shot. The main character now holds a magnifying glass. They are examining their own mental account filing cabinet — the same EARNED / WINDFALL folders from earlier. The magnifying glass reveals the labels clearly. Expression: focused and capable.",
 "Wide shot", "Flat, white", "The agency — the viewer can do this",
 "Character with magnifying glass examining own mental account folders",
 "Static. Magnifying glass moves slowly across the cabinet; labels visible and clear. 3s."),

("The bonus that feels like a windfall is compensation. Name it that the moment it arrives.",
 "Wide shot. A bonus envelope arrives. Instead of filing into the gold WINDFALL folder automatically, the character intercepts it — relabels it with a blue COMPENSATION sticker — and files it into the EARNED folder deliberately. Expression: calm and intentional.",
 "Wide shot", "Flat, white", "The first audit — simple and actionable",
 "Character intercepting bonus; relabeling from windfall to compensation; filing deliberately",
 "Static. Relabeling action is deliberate; EARNED folder receives the envelope. 2s."),

("The loyalty points that feel like free money are the portion of your spending the company returned to you.",
 "Wide shot. A loyalty points card — but now decoded. A transparent overlay shows: these points = €X of your spending returned. Bold label: 'YOUR MONEY RETURNED.' The gold windfall glow fades; it becomes neutral — neither exciting nor shameful.",
 "Wide shot", "Flat, white, neutral tone", "The second audit — demystifying the points",
 "Loyalty card with YOUR MONEY RETURNED decoded overlay; windfall glow fades",
 "Static. Overlay appears; glow fades to neutral. 2s."),

("The casino chip is fifty euros. Every time you reach for it, translate it back into the number.",
 "Close-up. A casino chip in the character's hand. A small translation overlay appears: '= €50.' Every time the hand reaches for another chip, the overlay refreshes. The brain inside the skull now watches with its alert expression — no longer smug, but watchful.",
 "Close-up", "Flat, warm casino light, translation overlay", "The third audit — naming the chip restores the signal",
 "Chip with €50 translation overlay; brain alert and watchful, not smug",
 "Static. Translation overlay refreshes each time chip is touched. 2s."),

("Thaler won the Nobel Prize in Economic Sciences in 2017.",
 "Wide shot. A flat Nobel Prize medal — gold, clean, elegant — displayed on a white background. Bold label: 'NOBEL PRIZE IN ECONOMIC SCIENCES · 2017.' Thaler stands beside it. His expression: the specific quiet satisfaction of someone who was told they were wasting everyone's time.",
 "Wide shot", "Flat, white, gold medal", "The vindication — earned over decades",
 "Nobel medal; 2017 label; Thaler with quiet satisfaction beside it",
 "Static. Medal glows softly; Thaler's expression holds. 2s."),

("He had spent forty years being told he was wasting everyone's time.",
 "Wide timeline. A horizontal line from 1975 to 2017 — 42 years. Along the line: recurring dismissal icons (crossed-out thought bubbles, closed doors, shaking heads). The Nobel star appears at the end. Bold label: '42 YEARS.'",
 "Wide timeline shot", "Flat, white", "The journey — the decades of dismissal before the prize",
 "42-year timeline with dismissal icons; Nobel star at end; 42 YEARS label",
 "Static. Timeline populates left to right; Nobel star arrives last. 3s."),

("It started with a bowl of cashews at a dinner party in 1975.",
 "Medium shot. The dinner party scene from the beginning — the cashew bowl on the coffee table, the warm amber light, the relaxing guests. The same image, but seen differently now. Small label: '1975.' The bowl is the whole story.",
 "Medium shot", "Warm amber, identical to earlier scene", "The return — the full circle closed",
 "Cashew bowl scene returns; warm and familiar; 1975 label",
 "Static. Scene is identical to the opening dinner party beat; recognition lands. 3s."),

("The insight it produced — that every financial decision you make is shaped not by how much money you have, but by which mental account the money is in — is one of the most replicated findings in the history of economics.",
 "Wide diagram. The central insight laid out cleanly: NOT [amount] → DECISION. But [ACCOUNT] → DECISION. The account box is highlighted. Around the diagram: small citation icons representing dozens of replications. Bold label: 'MOST REPLICATED.'",
 "Wide diagram shot", "Flat, white, account box highlighted", "The finding at its most precise — the key sentence",
 "Central insight diagram; ACCOUNT highlighted not AMOUNT; replication citations",
 "Static. Diagram appears; account box illuminates; citations populate. 3s."),

("And the industries that want your money understood it before the Nobel committee announced his name.",
 "Wide timeline. The industry markers from earlier return — CASINOS, CREDIT CARDS, LOYALTY PROGRAMS — all preceding the NOBEL marker. A corporate figure watches the Nobel ceremony from a distance, arms crossed, unsurprised. They already knew.",
 "Wide timeline shot", "Flat, white", "The final industry statement — unsettling in its timing",
 "Industry markers preceding Nobel; corporate figure unsurprised; already knew",
 "Static. Timeline holds; corporate figure's unsurprise is the point. 3s."),

# ── THE ENDING ─────────────────────────────────────────────────────────────────

("You cannot stop your brain from keeping mental accounts.",
 "Medium shot of the main character. The brain inside the skull is filing automatically — EARNED here, WINDFALL there — the folders moving on their own without the character's input. Automatic. Below conscious control. The character can't see it.",
 "Medium shot", "Flat, white", "The honest limit — but not hopeless",
 "Brain filing automatically below character's awareness; automatic filing visible",
 "Static. Folders move on their own; character is unaware of the filing. 2s."),

("The system runs below the threshold of conscious thought. It was there before you knew the word for it.",
 "Wide diagram. A horizontal consciousness line across the center. Above: the character's deliberate thoughts. Below: the mental accounting system running quietly — folders, signals, triggers — all active and invisible. Label: 'BELOW CONSCIOUS THRESHOLD.'",
 "Wide diagram shot", "Flat, white", "The depth of the system — below reach but not invisible",
 "Consciousness threshold line; mental accounting active below; label",
 "Static. System below line is detailed and active; above line is calm. 3s."),

("But you can learn to read the filing.",
 "Wide shot. The character now has a window into the filing system — a small transparent panel in their own chest through which the EARNED / WINDFALL folders are visible. The character examines it calmly. A magnifying glass in hand.",
 "Wide shot", "Flat, white, soft chest panel glow", "The capability — seeing is the first step",
 "Character with transparent chest panel showing filing system; magnifying glass",
 "Static. Chest panel glows softly; magnifying glass positioned. 2s."),

("When money arrives — any money — ask one question before you do anything with it.",
 "Wide shot. Money arrives from above — any kind, all types. The character catches it. Before filing, before spending, before anything — a single bold pause symbol appears. A question mark floats above. The pause is the practice.",
 "Wide shot", "Flat, white", "The habit introduced — the pause before the filing",
 "Money arriving; character catching; pause symbol appearing; question mark above",
 "Static. Pause symbol appears before any action is taken. 2s."),

("Which account is my brain putting this in?",
 "Close-up. The mental account filing cabinet with its two folders — EARNED (blue) and WINDFALL (gold). One folder begins to open automatically. The question mark floats above: which one? The character's hand hovers, choosing to observe rather than react.",
 "Close-up", "Flat, white, folders visible", "The question — the entire practice in one line",
 "Filing cabinet with two folders; one opening automatically; character observing",
 "Static. Cabinet holds; automatic filing paused by the question. 2s."),

("And is that the account I would choose if I were choosing deliberately?",
 "Close-up. The same filing cabinet — but now a second, deliberate hand appears beside the automatic one. The deliberate hand points to a different folder. The two hands are visible together: automatic vs chosen. The choice belongs to the character.",
 "Close-up", "Flat, white", "The second question — autonomy reclaimed",
 "Automatic hand vs deliberate hand at filing cabinet; two choices visible",
 "Static. Both hands visible; deliberate hand points to considered choice. 3s."),

("The bonus, the win, the gift, the refund — your brain has already filed them somewhere.",
 "Wide shot. Four money types arrive and are instantly auto-filed by the brain — bonus to WINDFALL, win to WINDFALL, gift to WINDFALL, refund to WINDFALL. All four go to the same folder automatically, instantly, before any conscious thought.",
 "Wide shot", "Flat, white", "The automatic system — the default is already running",
 "Four money types auto-filed to WINDFALL instantly; no conscious input",
 "Static. All four file to WINDFALL simultaneously; speed is the point. 2s."),

("The only question is whether you agree with the filing.",
 "Wide shot. The same four money types — but now the character stands at the cabinet, reviewing each filing with a pen. Some stay in WINDFALL. Some get moved to EARNED. The character makes deliberate choices, one by one. Expression: calm and capable.",
 "Wide shot", "Flat, white", "The agency — the audit is possible and practical",
 "Character reviewing and adjusting auto-filings deliberately; pen in hand",
 "Static. Character moves items with deliberate intention; expression is composed. 3s."),

("Every video on this channel is one way your financial gut has been hacked.",
 "Wide shot, white background. The main character faces camera — the brain inside the skull now with its composed, watchful expression (not smug). A row of small icons stretches behind the character: dopamine, bandwidth, somatic markers, mental accounts — each labeled. The channel's mission is visible.",
 "Wide shot, direct address", "Flat, white", "Channel mission — the promise to the viewer",
 "Character facing camera; row of channel topic icons behind; brain watchful",
 "Static. Topic icons glow softly; character holds direct address. 3s."),

("This is how they got to your windfall before you did.",
 "Wide shot, closing frame. The industry figure from earlier is shown reaching into a gold WINDFALL folder — taking the contents — before the character has even received the money. The character walks toward the folder and finds it already half-empty. Expression: recognition, not defeat. Now they know.",
 "Wide shot", "Flat, white", "The closing image — recognition and agency, not despair",
 "Industry figure at windfall folder before character arrives; character sees and recognizes",
 "Static. Character's expression is recognition and understanding — not defeat. Final hold. 3s."),

]  # end BEATS


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    TITLE = "Why Free Money Is the Most Expensive Money You Own"
    SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 5"
    LABEL_DOC = "STATE 5 — PRODUCTION DOCUMENT (FULL BEAT SHEET)"

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run(SUBTITLE)
    r.bold = True
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run(LABEL_DOC)
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    s2 = doc.add_paragraph()
    s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s2.add_run(TITLE)
    r.bold = True
    r.italic = True
    r.font.size = Pt(16)

    doc.add_paragraph()

    SECTION_STARTS = {
        1: "HOOK",
        9: "THE IMPOSSIBILITY",
        16: "THE DINNER PARTY",
        33: "THE THEORY",
        43: "THE EXPERIMENTS",
        60: "THE MECHANISM",
        74: "THE POPULAR MISREADING",
        85: "THE INDUSTRY",
        99: "THE REAL CONCLUSION",
        112: "THE ENDING",
    }

    COL_LABELS = ["#", "SEGMENT (NARRATION)", "IMAGE PROMPT", "CAMERA",
                  "LIGHTING", "MOOD / TONE", "CHARACTER ACTION", "VIDEO MOTION"]
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

        cell_text(cells[0], str(beat_num), bold=True, sz=9,
                  color=RGBColor(0x99, 0x99, 0x99))
        cell_text(cells[1], seg, bold=True, sz=9)
        cell_text(cells[2], scene, sz=8)
        cell_text(cells[3], cam, sz=8)
        cell_text(cells[4], light, sz=8)
        cell_text(cells[5], mood, sz=8)
        cell_text(cells[6], action, sz=8)
        cell_text(cells[7], video, sz=8)

    all_lines = [b[0] for b in BEATS]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = len(BEATS)

    doc.add_paragraph()
    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(
        f"TOTAL: {total_beats} beats · ~{word_count} words · "
        f"~{round(word_count/140)} min narration")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Mental_Accounting_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
