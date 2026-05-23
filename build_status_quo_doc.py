#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'The Billion-Dollar Bet Your Bank Is Making Against You Right Now' (Video 6 — Status Quo Bias)."""

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

("Think about the last time you changed your pension fund.",
 f"{STYLE} Medium shot, warm beige background. The main character stands facing slightly left, eyes closed in thought. Inside the transparent skull, the pink brain leans back in a relaxed pose. A small pension document icon floats in a thought bubble above the character's head, slightly dusty and cobwebbed. Bold diegetic label: 'LAST CHANGED?'",
 "Medium shot, centered", "Warm beige, soft ceiling spotlight", "Intimate and direct — hook addressed to the viewer",
 "Character thinking; pension icon dusty in thought bubble; brain relaxed",
 "Static. Thought bubble floats gently. Dust particles drift. 2s."),

("Or moved your savings to a higher-interest account.",
 f"{STYLE} Medium shot, same warm background. The thought bubble now shows a savings account icon — a small jar with coins — with a low flat line beside it and a tall bar barely visible in the background. The gap between them is visible but the character has not noticed. Brain peers sideways.",
 "Medium shot", "Warm beige, soft", "Self-recognition — viewer maps their own situation",
 "Savings jar icon with low interest bar; taller bar faintly visible; brain looking sideways",
 "Static. Low bar visible; tall bar faint in background. 2s."),

("Or switched banks. Or renegotiated your insurance. Or cancelled a subscription you forgot you had.",
 f"{STYLE} Wide shot, white background. Four icons in a row inside the thought bubble: a bank building, an insurance shield, a subscription card, a direct debit slip. Each icon has a cobweb or dust mark. A small clock beside each shows time elapsed. Bold label: 'ALL UNCHANGED.'",
 "Wide shot", "Flat, white", "Recognition builds — the list lands",
 "Four unchanged financial icons; each with cobweb; elapsed time clocks beside them",
 "Static. Icons appear one by one; each gets a small cobweb. 3s."),

("Now think about how long you have been meaning to.",
 f"{STYLE} Medium shot. The main character looks at a flat wall calendar. Months are marked off with a gentle X — January, February, March — continuing forward. A small sticky note on the calendar reads 'DO THIS SOON' — it has turned yellow with age. Expression: sheepish self-recognition.",
 "Medium shot", "Flat, warm", "Gentle self-incrimination — the gap between intent and action",
 "Character watching months pass on calendar; old sticky note visible; sheepish expression",
 "Animated. Calendar months X off slowly; sticky note yellows. 3s."),

("That gap — between intending and doing — is not a character flaw.",
 f"{STYLE} Wide diagram, white background. Two parallel lines: top line labeled 'INTENDED TO' with a start dot near the left. Bottom line labeled 'ACTUALLY DID' — empty, with a question mark at the end. The gap between them is shaded light gray. Bold label: 'NOT A CHARACTER FLAW.'",
 "Wide diagram shot", "Flat, white", "Reframe — relief and curiosity simultaneously",
 "Intention vs action gap diagram; gray shading between lines; reassuring label",
 "Static. Gap shading appears; label fades in. 2s."),

("It is the most reliable source of profit in the financial industry.",
 f"{STYLE} Wide shot. A large bank building in the background — clean, imposing, dark navy facade. In the foreground, a small coin-shaped meter labeled 'PROFIT SOURCE' with an arrow pointing to 'YOUR INACTION.' The brain villain peers from a window of the bank building, smug expression, arms folded.",
 "Wide shot", "Flat, white, bank building solid navy", "The villain introduced — tone shifts slightly",
 "Bank building; profit meter pointing to inaction; brain villain watching from window",
 "Static. Brain villain visible in window; meter arrow steady. 3s."),

("It has a name. It has been studied for decades. It has been deliberately engineered into every financial product you own.",
 f"{STYLE} Wide shot. Three floating cards appear in sequence beside the bank building: '1. IT HAS A NAME', '2. STUDIED FOR DECADES', '3. ENGINEERED INTO YOUR PRODUCTS.' Each card is stamped with a small bank logo. The brain villain in the window nods slowly.",
 "Wide shot", "Flat, white", "The stakes raised — deliberate and studied",
 "Three cards floating; bank stamp on each; brain villain nodding",
 "Animated. Cards appear one by one; each gets a bank stamp. 3s."),

("And right now, while you are watching this, it is running.",
 f"{STYLE} Close-up on the bank building window. The brain villain is now at a small terminal displaying a live counter: '€ RUNNING.' The counter ticks upward in real time. A small clock in the corner shows the current moment. Expression: the brain is not surprised. It expected you to keep watching.",
 "Close-up on bank window", "Dark navy building, spotlight on counter", "Urgency — the mechanism is active now",
 "Brain villain at live counter; euros ticking; clock showing now",
 "Animated. Counter ticks upward steadily. Clock ticks. 3s."),

# ── THE IMPOSSIBILITY ──────────────────────────────────────────────────────────

("Here is what makes this strange.",
 f"{STYLE} Medium shot. The main character turns to face camera, slightly puzzled expression. The brain inside the skull mirrors the expression — brow furrowed, curiosity activated. Clean white background. The mood is about to shift from recognition to revelation.",
 "Medium shot, direct address", "Flat, white", "The pivot — invitation to think harder",
 "Character and brain both puzzled; facing camera; mood shift incoming",
 "Static. Both character and brain hold curious expression. 2s."),

("You did not choose most of your financial settings.",
 f"{STYLE} Wide shot, white background. The main character stands beside a large control panel — dials, switches, sliders — representing financial settings: PENSION, SAVINGS RATE, INSURANCE, FUND ALLOCATION. The character's hands are at their sides. They are not touching any of it. Bold label: 'YOU DID NOT SET THIS.'",
 "Wide shot", "Flat, white, control panel highlighted", "The reveal — the settings exist but were not chosen by you",
 "Character beside financial control panel; hands at sides; did not set it",
 "Static. Control panel visible in full; character not touching it. 3s."),

("Your pension allocation. Your savings interest rate. Your overdraft limit. Your insurance renewal price. Your investment fund.",
 f"{STYLE} Close-up on the control panel. Five dials are highlighted one by one with a red ring: PENSION ALLOCATION, SAVINGS RATE, OVERDRAFT LIMIT, INSURANCE RENEWAL, INVESTMENT FUND. Each dial already has a position set — the needle is fixed. No one asked.",
 "Close-up on control panel", "Flat, white, red rings on each dial", "The specificity lands — viewer recognizes their own life",
 "Five dials highlighted in sequence; each already set; no user input",
 "Animated. Red ring appears around each dial in sequence. 3s."),

("Someone else chose them. Before you arrived. Without asking.",
 f"{STYLE} Wide shot. The bank building in the background. A shadowy figure in a suit stands at the control panel from the previous scene — turning the dials, setting the positions — before the main character has even entered the frame. The character walks in from the left and finds the panel already configured. Expression: mild shock.",
 "Wide shot", "Flat, white, suited figure slightly shadowed", "The betrayal framed clearly — someone chose for you",
 "Suited figure setting dials before character arrives; character walks in to find it done",
 "Animated. Suited figure turns dials; character enters frame; panel already set. 3s."),

("And they chose them for a reason.",
 f"{STYLE} Medium shot on the suited figure. They turn slightly toward camera — face not fully visible, just the outline of a satisfied expression. In their hand: a small profit chart showing an upward line. The reason is clear without being stated.",
 "Medium shot on suited figure", "Flat, white, slight shadow on figure", "The motive implied — discomfort grows",
 "Suited figure with profit chart; reason visible; face not fully shown",
 "Static. Figure holds profit chart. Upward line visible. 2s."),

("Not your reason.",
 f"{STYLE} Wide split. Left: suited figure with profit chart (upward). Right: main character with a different chart — their retirement projection (flat or declining under current defaults). Bold label across the center: 'NOT YOUR REASON.' The contrast is the point.",
 "Wide split diagram", "Flat, white", "The conflict stated — two different interests",
 "Suited figure profit vs character retirement gap; NOT YOUR REASON label",
 "Static. Split holds; label appears between the two. 2s."),

("This is the story of the default. The most powerful financial instrument ever built. And the bet that it will work on you forever.",
 f"{STYLE} Wide shot, white background. A single word appears in large bold diegetic text at center screen: 'THE DEFAULT.' Beneath it, two smaller labels appear in sequence: 'MOST POWERFUL FINANCIAL INSTRUMENT EVER BUILT' and 'THE BET: IT WILL WORK ON YOU FOREVER.' The main character stands to the side, looking at the text. The brain villain's smug face appears briefly in the corner.",
 "Wide shot, text-forward", "Flat, white, text prominent", "The thesis stated — this is what the video is about",
 "THE DEFAULT text dominant; character observing; brain villain in corner",
 "Animated. Title text appears; two labels fade in below in sequence. 3s."),

# ── THE CHECKBOX ──────────────────────────────────────────────────────────────

("In 2003, two researchers published a paper that should have changed how every government on Earth designs policy.",
 f"{STYLE} Wide shot, white background. A large open academic paper floats in the center of the frame — bold title visible. Beside it: a globe with small government building icons on every continent. A bold label: '2003.' The paper has a red IMPORTANT stamp. The researchers are represented by two small cartoon figures with glasses and clipboards.",
 "Wide shot", "Flat, white, paper highlighted", "Historical anchor — something important was discovered",
 "Academic paper floating; globe with government icons; 2003 label; two researchers",
 "Static. Paper floats; IMPORTANT stamp visible. 3s."),

("Eric Johnson and Daniel Goldstein were studying organ donation rates across Europe.",
 f"{STYLE} Wide shot. A map of Europe, clean and flat. Two small cartoon researcher figures — Johnson and Goldstein — stand beside it with clipboards. Small heart icons (organ donation symbols) are scattered across the map at varying densities. The researchers are mid-investigation, pointing at different countries.",
 "Wide shot, map-forward", "Flat, white", "The investigation begins — academic curiosity",
 "Johnson and Goldstein at European map; donation heart icons varying by country",
 "Static. Researchers point at map. Heart icons visible. 2s."),

("The numbers they found made no sense.",
 f"{STYLE} Medium shot on the two researchers. They are staring at a clipboard with numbers — their expressions: confused, leaning in, checking the math again. The numbers on the clipboard are partially visible: large gaps between rows. Bold label above: 'MADE NO SENSE.'",
 "Medium shot on researchers", "Flat, white", "The mystery established — the anomaly is real",
 "Researchers puzzled at clipboard numbers; checking math; confusion visible",
 "Static. Both researchers lean in toward clipboard. 2s."),

("Austria: 99.98 percent of the population registered donors.",
 f"{STYLE} Close-up on the European map. Austria highlighted in bright green. A bold label appears: 'AUSTRIA: 99.98%.' A green filled bar beside the country icon reaches nearly to the top. Expression on the map: abundance.",
 "Close-up on map — Austria", "Flat, white, Austria green", "The first data point — near-total participation",
 "Austria highlighted green; 99.98% label; near-full bar",
 "Animated. Green fill appears; bar rises to near-top. 2s."),

("Germany: 12 percent.",
 f"{STYLE} Same close-up on the map. Germany highlighted beside Austria — but in pale gray. Bold label: 'GERMANY: 12%.' A tiny bar barely visible beside it. The contrast with the Austria bar is immediate and stark.",
 "Close-up on map — Germany", "Flat, white, Germany pale gray", "The contrast lands — jarring gap",
 "Germany gray beside green Austria; 12% label; tiny bar vs full bar",
 "Animated. Germany bar appears small; contrast with Austria is stark. 2s."),

("France: 99.91 percent.",
 f"{STYLE} Map expands to show France. Highlighted in bright green. Bold label: 'FRANCE: 99.91%.' Full bar beside France, matching Austria. Two green countries, one gray — the pattern begins to suggest something.",
 "Map — France highlighted", "Flat, white, France green", "Pattern forming — two greens, one gray",
 "France green with 99.91% label; full bar matching Austria",
 "Animated. France bar rises to near-top. 2s."),

("Denmark: 4.25 percent.",
 f"{STYLE} Map shows Denmark. Highlighted in pale gray, even lighter than Germany. Bold label: 'DENMARK: 4.25%.' The bar is barely a sliver. The four bars now visible side by side: Austria full, Germany tiny, France full, Denmark near-zero. The pattern is unmistakable.",
 "Map — Denmark highlighted", "Flat, white, Denmark pale gray", "The pattern completes — the mystery is sharp",
 "Denmark near-zero bar; four countries side by side; full vs empty pattern clear",
 "Animated. Denmark bar appears as sliver. All four bars visible. 3s."),

("Same continent. Similar cultures. Similar legal systems. A gap of 95 percentage points.",
 f"{STYLE} Wide diagram. The four country bars side by side in a clean comparison chart. A large double-headed arrow spans from the lowest bar (Denmark 4.25%) to the highest (Austria 99.98%). Bold label across the arrow: '95 PERCENTAGE POINTS.' Below the chart: three check marks — SAME CONTINENT, SIMILAR CULTURES, SIMILAR LEGAL SYSTEMS. The gap is the mystery.",
 "Wide comparison chart", "Flat, white", "The anomaly quantified — 95 points demands explanation",
 "Four country bars; 95-point gap arrow; three same-factors listed below",
 "Static. Arrow and gap label appear after bars. 3s."),

("Johnson and Goldstein looked for the variable. They checked religion. Wealth. Education. Political systems. Healthcare attitudes.",
 f"{STYLE} Wide shot. The two researchers stand at a large whiteboard covered in checked-off categories: RELIGION ✗, WEALTH ✗, EDUCATION ✗, POLITICAL SYSTEMS ✗, HEALTHCARE ATTITUDES ✗. Each has a red cross through it. They are running out of explanations. Expression: frustrated, methodical.",
 "Wide shot at whiteboard", "Flat, white, red crosses visible", "The systematic elimination — the answer is not obvious",
 "Researchers crossing off categories; whiteboard of explanations eliminated",
 "Animated. Crosses appear one by one on each category. 3s."),

("Nothing explained it.",
 f"{STYLE} Medium shot. Both researchers stare at the whiteboard — all categories crossed off. The whiteboard is full of red Xs. They look at each other. Expression: stumped. A single question mark floats above both of them.",
 "Medium shot", "Flat, white", "The mystery at its peak — no answer yet",
 "Both researchers stumped; whiteboard covered in red Xs; shared question mark above",
 "Static. Question mark floats. Silence before the reveal. 2s."),

("Then they looked at the government form.",
 f"{STYLE} Wide shot. One researcher holds up a simple government form — flat, clean, two versions side by side. The form is unremarkable except for one small checkbox at the bottom. A spotlight focuses on the form. Bold label: 'THE FORM.' Expression: the moment of realization beginning.",
 "Wide shot, form highlighted", "Spotlight on form, warm", "The pivot — the answer was simple all along",
 "Researcher holding government form; spotlight on it; checkbox visible at bottom",
 "Static. Spotlight narrows to the form. 2s."),

("In Austria, the form said: you are a donor unless you actively opt out.",
 f"{STYLE} Close-up on the left version of the form. Bold text visible: 'YOU ARE A DONOR UNLESS YOU OPT OUT.' A checkbox at the bottom is empty — no action required to be enrolled. A green checkmark appears automatically beside the enrollment line. Label: 'OPT-OUT.'",
 "Close-up on opt-out form", "Flat, white, green checkmark", "The mechanism revealed — opt-out default",
 "Opt-out form; automatic enrollment shown; green checkmark appears without action",
 "Animated. Green checkmark appears automatically with no hand touching it. 2s."),

("In Germany, the form said: check this box if you want to be a donor.",
 f"{STYLE} Close-up on the right version of the form. Bold text visible: 'CHECK THIS BOX TO BECOME A DONOR.' The checkbox at the bottom is empty — waiting for action. No automatic checkmark. The box sits there, unfilled. Label: 'OPT-IN.' The emptiness of the box is the entire point.",
 "Close-up on opt-in form", "Flat, white, empty checkbox", "The contrast — opt-in requires action that rarely happens",
 "Opt-in form; empty checkbox waiting; no automatic enrollment",
 "Static. Empty checkbox holds. No action. 2s."),

("That was it.",
 f"{STYLE} Wide shot. The two researchers stand beside the two forms, now placed side by side on a table. They look at each other. The realization has landed. The only difference between 99.98% and 12% is visible on the table in front of them. Expression: awe at the simplicity.",
 "Wide shot", "Flat, white", "The simplicity of the answer — awe and discomfort",
 "Researchers beside both forms; the only difference visible; expressions of awe",
 "Static. Both researchers look from forms to each other. 2s."),

("Same people. Same values. Same decision available to everyone.",
 f"{STYLE} Wide diagram. Three check marks in a row: SAME PEOPLE ✓, SAME VALUES ✓, SAME DECISION AVAILABLE ✓. Below them, a bold question mark: then why the 95-point gap? The viewer is being held at the edge of the answer.",
 "Wide diagram", "Flat, white", "Building the logic — what was the same, so what was different?",
 "Three same-factors checkmarks; question mark below; answer one beat away",
 "Static. Checkmarks appear; question mark holds. 2s."),

("Different default.",
 f"{STYLE} Wide shot, white background. Two large boxes side by side. Left box: green, labeled 'OPT-OUT DEFAULT — 99.98%.' Right box: gray, labeled 'OPT-IN DEFAULT — 4.25–12%.' Between them, a single bold word: 'DEFAULT.' The difference is the entire gap. Nothing else.",
 "Wide split", "Flat, white, green vs gray", "The answer delivered — clean and undeniable",
 "Green opt-out box vs gray opt-in box; DEFAULT label between them; the gap explained",
 "Static. Both boxes visible; DEFAULT label prominent. 3s."),

("In the opt-out countries, 99 percent of people never changed the default.",
 f"{STYLE} Wide shot. A crowd of cartoon figures — many, representing 99 out of 100. 99 stand still, unchanged. One figure in the corner has moved — the 1 percent who opted out. Bold label: '99% NEVER CHANGED IT.' The stillness of the crowd is the visual.",
 "Wide crowd shot", "Flat, white", "The scale of inertia — almost no one moves",
 "99 figures still; 1 figure moved; crowd stillness visible; label above",
 "Static. 99 still figures; 1 moved figure in corner. 3s."),

("In the opt-in countries, 85 percent of people never changed the default.",
 f"{STYLE} Same crowd framing but now the default is different — the 85 figures who never checked the box are gray (not enrolled). 15 figures in green have actively signed up. Bold label: '85% NEVER CHANGED IT EITHER.' In both systems, the same behavior: most people follow the default. The system, not the people, determined the outcome.",
 "Wide crowd shot", "Flat, white, gray majority vs green minority", "The parallel inertia — same behavior, different default, different outcome",
 "85 gray figures; 15 green figures; label shows same inertia different default",
 "Static. Crowd holds; label fades in. 2s."),

("Everyone followed the path of least resistance.",
 f"{STYLE} Wide diagram. Two paths side by side — each with a 'path of least resistance' arrow pointing forward along the default track. In both cases, the arrow goes straight ahead without deviation. A dotted side-path (the opt-out or opt-in action) branches off but is barely visible. Bold label: 'PATH OF LEAST RESISTANCE.'",
 "Wide diagram", "Flat, white, arrows on both paths", "The mechanism named — it is not the person, it is the path",
 "Two default paths with forward arrows; side-paths barely visible; least resistance label",
 "Static. Arrows point forward on both paths. Side-paths faint. 2s."),

("The default was not a suggestion. For almost everyone, in every country, the default was the decision.",
 f"{STYLE} Wide shot. The government form from earlier, now large and central. The checkbox or lack of checkbox has been circled in bold red. Above it: 'NOT A SUGGESTION.' Below it: 'THE DECISION.' The main character stands beside it, reading the form for the first time — the brain inside the skull has gone quiet, processing.",
 "Wide shot, form central", "Flat, white, form highlighted", "The conclusion of the story — the default IS the decision",
 "Form centered; NOT A SUGGESTION / THE DECISION labels; character reading for first time",
 "Static. Form holds; labels appear above and below in sequence. 3s."),

# ── THE THEORY ────────────────────────────────────────────────────────────────

("In 1988, two economists at Harvard — William Samuelson and Richard Zeckhauser — ran a series of experiments.",
 f"{STYLE} Wide shot. A Harvard building in clean flat style in the background. Two cartoon researcher figures — Samuelson and Zeckhauser — stand at a table with financial documents. Bold label: '1988 · HARVARD.' The scene has an academic, deliberate quality.",
 "Wide shot", "Flat, white, Harvard building in background", "Historical anchor — academic origin of status quo bias",
 "Samuelson and Zeckhauser at Harvard table with financial documents; 1988 label",
 "Static. Researchers at table. 2s."),

("They gave participants financial choices. Investment portfolios. Insurance plans. Medical treatments.",
 f"{STYLE} Wide shot. Three floating cards on the table: a bar chart (INVESTMENT PORTFOLIO), a shield icon (INSURANCE PLAN), a medical cross (MEDICAL TREATMENT). Cartoon participant figures sit across from the researchers, looking at the cards. Expression: evaluating.",
 "Wide shot", "Flat, white", "The experiment set up — financial choices on the table",
 "Three choice cards on table; participants evaluating; researchers watching",
 "Static. Three cards visible; participants lean in slightly. 2s."),

("In every scenario, one option was labeled as the status quo — the current state, already in place.",
 f"{STYLE} Close-up on the investment portfolio card. One option has a small badge on it: 'STATUS QUO — ALREADY IN PLACE.' The other options have no badge. The badge is subtle but present. A faint glow around the status quo option.",
 "Close-up on choice card", "Flat, white, status quo option faintly glowing", "The experimental manipulation — one option pre-labeled",
 "Status quo option with badge; others without; subtle differentiation",
 "Static. Status quo badge visible; faint glow around that option. 2s."),

("In every scenario, the status quo option was chosen significantly more often than the alternatives.",
 f"{STYLE} Wide chart. A bar chart showing choice frequency across the experiment: the STATUS QUO bar is significantly taller than all alternatives. The gap is wide and consistent. Bold label: 'CHOSEN SIGNIFICANTLY MORE.'",
 "Wide chart shot", "Flat, white, status quo bar taller", "The finding — the bias is consistent and large",
 "Bar chart with status quo dominating; alternatives shorter; label above",
 "Animated. Status quo bar rises first and tallest. 3s."),

("Even when the alternatives were objectively, measurably better.",
 f"{STYLE} Wide diagram. Two options side by side: STATUS QUO with a flat performance line and a BETTER OPTION with a clear upward line. A green star beside the better option: 'OBJECTIVELY BETTER.' An arrow points to STATUS QUO with label: 'STILL CHOSEN MORE.' The irrationality is quantified.",
 "Wide comparison diagram", "Flat, white, better option starred green", "The irrationality named — better options lost to defaults",
 "Status quo vs better option; better option starred; status quo still chosen",
 "Static. Green star on better option; arrow to status quo still chosen. 3s."),

("Even when participants acknowledged, out loud, that the alternative was better — they still chose the status quo.",
 f"{STYLE} Medium shot on a participant figure. A speech bubble above them: 'THE OTHER OPTION IS BETTER.' Their hand points to the status quo card anyway. Expression: slightly confused by their own behavior. The brain villain watches from the corner with a knowing nod.",
 "Medium shot on participant", "Flat, white", "The paradox — knowing and still not acting",
 "Participant acknowledging better option verbally; hand pointing to status quo anyway",
 "Static. Speech bubble and pointing hand visible simultaneously. 3s."),

("They called it status quo bias.",
 f"{STYLE} Wide shot. The researchers stand at a whiteboard. Samuelson writes in bold: 'STATUS QUO BIAS.' The words appear large and clear. The main character reads it from the side. The brain inside the skull perks up — recognition. Bold diegetic label on whiteboard.",
 "Wide shot at whiteboard", "Flat, white, label prominent", "The naming — the phenomenon has a name",
 "STATUS QUO BIAS written on whiteboard; character reading; brain recognizing",
 "Animated. Text written stroke by stroke on whiteboard. 2s."),

("The bias was not small. It was not occasional. It was consistent across every demographic, every income level, every level of financial education.",
 f"{STYLE} Wide diagram. Three horizontal rows, each representing a demographic group: HIGH INCOME, LOW INCOME, FINANCIAL PROFESSIONALS. In every row, the same result: status quo bar dominant. Bold label across all three: 'CONSISTENT.' No exceptions. No demographic immune.",
 "Wide multi-row diagram", "Flat, white", "The universality — no one is exempt",
 "Three demographic rows all showing same bias; CONSISTENT label across all",
 "Static. Three rows visible; label spans all. 3s."),

("Including people who managed money professionally.",
 f"{STYLE} Close-up on the FINANCIAL PROFESSIONALS row. The cartoon figures in this row wear suits, carry briefcases, have small chart icons on their name badges. The status quo bar for this group is identical to all others. Bold label: 'INCLUDING PROFESSIONALS.' The brain villain behind the suit figures nods.",
 "Close-up on professionals row", "Flat, white", "The punch — even experts fall for it",
 "Professional figures with suits and briefcases; same bias as everyone; brain villain nodding",
 "Static. Professional row highlighted; bias bar identical to others. 2s."),

("The default wins. Not sometimes. Almost always.",
 f"{STYLE} Wide shot. A large scoreboard — clean and flat — showing: DEFAULT: 95 — ALTERNATIVE: 5. The numbers are stark. Bold diegetic label: 'ALMOST ALWAYS.' The main character reads the scoreboard. The brain villain sits atop it, legs dangling, satisfied.",
 "Wide shot, scoreboard", "Flat, white, scoreboard prominent", "The summary — default dominance quantified",
 "Scoreboard DEFAULT 95 vs ALTERNATIVE 5; brain villain on top; character reading",
 "Static. Scoreboard holds. Brain villain satisfied. 3s."),

# ── THE EXPERIMENTS ───────────────────────────────────────────────────────────

("The most consequential experiment about defaults was not run in a psychology lab.",
 f"{STYLE} Wide shot. A psychology lab in the background — clean, clinical, white walls, test equipment. A large red X appears over it. Bold label: 'NOT HERE.' The camera is about to pan elsewhere.",
 "Wide shot", "Flat, white, red X on lab", "Subversion of expectation — not in a lab",
 "Psychology lab with red X over it; NOT HERE label; about to go elsewhere",
 "Static. Red X on lab. Label appears. 2s."),

("It was run inside a corporation.",
 f"{STYLE} Wide shot. An office building — clean flat-style, corporate, several floors visible. Employee cartoon figures visible through the windows at desks. Bold label: 'INSIDE A CORPORATION.' The shift from academic to real-world is visual.",
 "Wide shot, office building", "Flat, warm office tones", "The real-world setting — stakes are higher",
 "Corporate office building; employees visible through windows; real-world setting",
 "Static. Office building holds. 2s."),

("2001. Two economists — Brigitte Madrian and Dennis Shea — studied a large American company that changed how it enrolled employees in its retirement plan.",
 f"{STYLE} Wide shot. Two researcher figures — Madrian and Shea — stand outside the office building with clipboards. Bold label: '2001.' A small icon of a retirement fund document is visible on Madrian's clipboard. They are observing, not intervening.",
 "Wide shot", "Flat, warm", "The researchers introduced — observational study",
 "Madrian and Shea outside office; clipboards; retirement fund icon; 2001 label",
 "Static. Researchers observe from outside. 2s."),

("Before the change: employees had to actively sign up. Opt in. Take an action.",
 f"{STYLE} Wide shot inside the office. An employee figure stands at a desk with a pension enrollment form. The form has an empty checkbox at the top: 'SIGN HERE TO ENROLL.' The employee looks at it, looks away, puts it in a drawer. Action required — action not taken.",
 "Wide shot inside office", "Flat, warm", "The before state — action required means action not taken",
 "Employee with opt-in form; empty checkbox; form placed in drawer without signing",
 "Animated. Employee slides form into drawer without signing. 3s."),

("Enrollment: 49 percent.",
 f"{STYLE} Wide diagram. A large circle divided: 49% filled in green (ENROLLED), 51% gray (NOT ENROLLED). Bold label: '49% ENROLLED — OPT-IN.' Below: 'More than half never enrolled.' The gray majority is the problem.",
 "Wide diagram, pie chart", "Flat, white, green vs gray", "The before number — barely half enrolled",
 "Pie chart 49% green 51% gray; opt-in label; majority not enrolled",
 "Animated. Pie fills to 49% green; rest stays gray. 2s."),

("The company changed one thing. Employees were now automatically enrolled. They could opt out at any time. Nothing else changed.",
 f"{STYLE} Wide shot of same office. The enrollment form has changed: it now reads 'YOU ARE ENROLLED. CHECK HERE TO OPT OUT.' The checkbox at the bottom is empty — action to opt out is available but not required. Bold label: 'ONE THING CHANGED.' Everything else in the office is identical.",
 "Wide shot inside office", "Flat, warm", "The single change — minimal but powerful",
 "New opt-out form; opt-out checkbox at bottom; office otherwise identical",
 "Static. New form visible; ONE THING CHANGED label. 2s."),

("Same salary. Same employer match. Same tax benefits. Same plan.",
 f"{STYLE} Wide diagram. Four paired comparison icons side by side — SALARY (equal), EMPLOYER MATCH (equal), TAX BENEFITS (equal), PLAN (equal). Each pair has an equals sign between them. Bold label: 'EVERYTHING ELSE: IDENTICAL.' Nothing substantive changed except the default.",
 "Wide comparison diagram", "Flat, white", "The control established — nothing else changed",
 "Four equal pairs; IDENTICAL label; default was the only variable",
 "Static. Four equal pairs visible; label confirms. 2s."),

("Enrollment: 86 percent.",
 f"{STYLE} Wide diagram. The same large circle — now 86% filled in green (ENROLLED), 14% gray (OPT-OUT). Bold label: '86% ENROLLED — AUTO-ENROLL.' The green majority is stark. Beside the old pie chart for comparison: 49% vs 86% side by side.",
 "Wide diagram, two pie charts", "Flat, white, green dominant", "The after number — the jump is enormous",
 "86% green pie chart; compared to 49% original; auto-enroll label",
 "Animated. New pie fills to 86%; old chart visible for comparison. 3s."),

("A 37 percentage point jump. From one change. To one form. To which option required action.",
 f"{STYLE} Wide diagram. The two pie charts side by side with a bold upward arrow between them: '+37 PERCENTAGE POINTS.' Below the arrow: three labels stacked — '1 CHANGE. 1 FORM. WHICH OPTION REQUIRED ACTION.' The simplicity of the mechanism is the point.",
 "Wide diagram", "Flat, white, arrow prominent", "The mechanism stated cleanly — one change, massive result",
 "Two pies with 37-point jump arrow; three simple labels below",
 "Static. Arrow and labels visible. 3s."),

("But here is the part that stopped the researchers.",
 f"{STYLE} Medium shot. Madrian and Shea stare at a second clipboard — different data. Their expressions: not triumphant. Something else is on the page. Expression: concerned, leaning in. Bold label above: 'BUT WAIT.'",
 "Medium shot on researchers", "Flat, white", "The second finding — something more troubling",
 "Researchers examining second data set; concerned expressions; BUT WAIT label",
 "Static. Researchers lean in. 2s."),

("The employees who were auto-enrolled did not change their contribution rate or fund selection once enrolled.",
 f"{STYLE} Wide shot. Auto-enrolled employee figures at their desks. Above each: a small pension dashboard showing: CONTRIBUTION RATE — DEFAULT, FUND SELECTION — DEFAULT. The dials are on the same settings they arrived with. No one has touched them. The control panel from earlier, with the settings already fixed.",
 "Wide shot inside office", "Flat, warm", "The second inertia — enrolled but still on defaults",
 "Auto-enrolled employees; pension dashboards showing default settings; nothing changed",
 "Static. Default settings visible on every dashboard. 3s."),

("They stayed in whatever the default was. The percentage the company chose. The fund the company selected.",
 f"{STYLE} Close-up on one employee's pension dashboard. Two dials highlighted: CONTRIBUTION % (set by company) and FUND SELECTION (set by company). Both dials have a small stamp on them: 'COMPANY CHOICE.' The employee's hand is visible — not touching the dials.",
 "Close-up on pension dashboard", "Flat, warm, company stamp highlighted", "The company's defaults remained — not the employee's choice",
 "Pension dashboard with company choice stamps; employee hand not touching dials",
 "Static. Company Choice stamps visible. Employee hand beside, not on dials. 2s."),

("The default did not just decide whether they enrolled.",
 f"{STYLE} Wide diagram. A flow chart: DEFAULT → ENROLLED (yes/no). The first arrow is labeled and clear. Then a second arrow from DEFAULT → FUND SELECTION. Then a third: DEFAULT → CONTRIBUTION RATE. The default is not one decision — it is all decisions.",
 "Wide flow diagram", "Flat, white", "The scope expands — default controls more than enrollment",
 "Flow chart showing default controlling enrollment, fund, and contribution rate",
 "Animated. Second and third arrows appear after first. 3s."),

("The default decided how they invested.",
 f"{STYLE} Wide shot. A large bold label dominates: 'THE DEFAULT DECIDED HOW THEY INVESTED.' The main character reads it. The brain villain in the background has a small profit chart — the default fund choice benefited the provider, not the employee.",
 "Wide shot, label dominant", "Flat, white", "The finding stated — the default is investment strategy",
 "Bold label; character reading; brain villain with provider profit chart",
 "Static. Label holds. Brain villain visible. 3s."),

("For years.",
 f"{STYLE} Wide shot. A wall calendar — years passing: 2001, 2002, 2003, 2004, 2005. The pension dashboard in the corner: same default settings, year after year. No hands touching it. Bold label: 'FOR YEARS.' The static is the story.",
 "Wide shot", "Flat, warm, years passing on calendar", "The duration — the inertia is long-term",
 "Calendar years passing; pension dashboard unchanged throughout; FOR YEARS label",
 "Animated. Calendar years flip; dashboard stays identical. 3s."),

# ── THE MECHANISM ─────────────────────────────────────────────────────────────

("Here is what is happening inside.",
 f"{STYLE} Medium shot. The main character faces camera. The brain inside the transparent skull shifts to an attentive, focused expression — ready to explain. Clean white background. This is the mechanism section — analytical and precise.",
 "Medium shot, direct address", "Flat, white", "The pivot to mechanism — analytical clarity",
 "Character and brain both attentive; facing camera; explanation incoming",
 "Static. Brain shifts to focused expression. 2s."),

("Every decision has a cost.",
 f"{STYLE} Wide diagram. A single decision icon at center — a scales of justice, simple and flat. Beside it, a small cost meter: not money, but mental energy. The meter is labeled: 'COGNITIVE COST.' Even a simple decision has a non-zero reading on the meter.",
 "Wide diagram", "Flat, white", "The concept introduced — decisions cost energy",
 "Decision scales with cognitive cost meter; non-zero reading visible",
 "Static. Meter shows non-zero cost. 2s."),

("Not a financial cost. A cognitive cost.",
 f"{STYLE} Wide split diagram. Left: a euro coin with a red X — NOT THIS. Right: a brain outline with an energy lightning bolt — THIS. Bold label: 'COGNITIVE COST.' The distinction is clean.",
 "Wide split diagram", "Flat, white", "The clarification — mental energy, not money",
 "Euro coin with red X vs brain with energy bolt; COGNITIVE COST label",
 "Static. Both sides visible; label prominent. 2s."),

("To change anything — your bank, your fund, your insurance — you have to compare options, evaluate risk, accept the possibility of choosing wrong, and take an action.",
 f"{STYLE} Wide diagram. A flow chart of the decision process: COMPARE OPTIONS → EVALUATE RISK → ACCEPT POSSIBILITY OF ERROR → TAKE ACTION. Each step has a small energy-cost meter that increments. By the final step, the total cognitive cost meter is high. Bold label: 'THE COST OF CHANGING.'",
 "Wide flow diagram", "Flat, white, cost meter incrementing", "The full cost of change — every step costs energy",
 "Four-step change process; cost meter rising with each step; total cost visible",
 "Animated. Steps appear in sequence; meter rises at each. 3s."),

("That process is expensive. Not in money. In mental energy.",
 f"{STYLE} Wide shot. The total cognitive cost meter from the previous diagram — now shown prominently, needle high. Below it: '€0' in gray (no financial cost) vs a red energy bar at high (mental cost). Bold label: 'EXPENSIVE IN MENTAL ENERGY.'",
 "Wide shot", "Flat, white, energy bar prominent", "The cost quantified — mental energy, not euros",
 "High energy bar; zero financial cost; expensive in mental energy label",
 "Static. Energy bar high; financial cost zero. 2s."),

("The default costs nothing. It is already done. It requires no comparison, no evaluation, no risk of regret.",
 f"{STYLE} Wide diagram. The same four-step flow chart — but for the DEFAULT option, all four steps are replaced with a single flat line: 'ALREADY DONE.' The cost meter reads zero. Bold label: 'DEFAULT: ZERO COST.' The contrast with the previous diagram is the point.",
 "Wide diagram", "Flat, white, cost meter at zero", "The default's advantage — zero cognitive cost",
 "Default path replaces four steps with ALREADY DONE; cost meter at zero",
 "Animated. Four steps collapse into one flat line; meter drops to zero. 3s."),

("Your brain runs a constant, automatic calculation: is the effort of changing worth the uncertain benefit of what I might get?",
 f"{STYLE} Medium shot on the brain inside the skull. The brain is shown at a tiny internal calculator — two inputs on screen: EFFORT OF CHANGING (high bar) vs UNCERTAIN BENEFIT (low bar with a question mark). The calculator spits out: 'ANSWER: NO.' Automatically. Without conscious input.",
 "Close-up on brain at calculator", "Flat, warm interior", "The automatic calculation — the brain does this without asking",
 "Brain at internal calculator; effort vs uncertain benefit; calculator outputs NO",
 "Animated. Calculator inputs load; output appears: NO. 2s."),

("Most of the time, the answer is no. Not because the benefit is not real. Because the calculation itself is hard.",
 f"{STYLE} Wide diagram. Two side-by-side calculations. Left: BENEFIT IS REAL (green checkmark). Right: CALCULATION IS HARD (red complexity icon). Arrow pointing to brain output: 'ANSWER: NO.' The real benefit does not overcome the calculation difficulty. Bold label: 'THE CALCULATION IS THE PROBLEM.'",
 "Wide diagram", "Flat, white", "The nuance — benefit exists but calculation blocks it",
 "Benefit real vs calculation hard; NO output despite real benefit; label",
 "Static. Both sides visible; NO output prominent. 3s."),

("Psychologists call this the omission bias. Inaction feels safer than action — even when the outcomes are identical.",
 f"{STYLE} Wide shot. The researchers at a whiteboard. Bold text written: 'OMISSION BIAS.' Below it: two identical outcome boxes side by side — INACTION and ACTION — both pointing to the same result. But a brain figure weighs them asymmetrically: INACTION feels lighter, ACTION feels heavier. The outcomes are the same; the feeling is not.",
 "Wide shot at whiteboard", "Flat, white", "The name given — omission bias explained",
 "OMISSION BIAS on whiteboard; identical outcomes; brain weighing them asymmetrically",
 "Animated. Text appears; asymmetric weighting shown by brain. 2s."),

("And there is something underneath that.",
 f"{STYLE} Medium shot. The character leans forward slightly, as if looking beneath the surface. The brain inside the skull peers down. Below the omission bias diagram, a deeper layer appears — a floor panel opens, revealing something below. Bold label: 'UNDERNEATH.'",
 "Medium shot", "Flat, white, deeper layer hint", "The layer beneath — something more fundamental",
 "Character and brain peering down; floor panel revealing deeper layer",
 "Animated. Floor panel opens; deeper layer glows below. 2s."),

("Changing something you already have means risking what you have for something you do not have yet.",
 f"{STYLE} Wide diagram. Left side: what you HAVE — a stable platform with your current financial setup (pension, savings, insurance). Right side: what you MIGHT GET — a dotted outline platform, uncertain. An arrow from left to right passes through a RISK ZONE in the middle — shaded gray, labeled 'RISK.' The solid platform vs the dotted one.",
 "Wide diagram", "Flat, white, risk zone shaded", "The asymmetry of change — certainty vs uncertainty",
 "Solid current platform vs dotted future platform; risk zone between them",
 "Static. Solid vs dotted platforms visible; risk zone shaded. 3s."),

("Your brain treats that asymmetrically. Always.",
 f"{STYLE} Medium shot on the brain inside the skull. The brain holds a scales — one side has the current setup (heavy, solid, concrete) and the other has the potential gain (lighter, dotted, uncertain). The scales tip toward the current setup — not because it is heavier in reality, but because the brain weights it that way. Bold label: 'ASYMMETRIC. ALWAYS.'",
 "Medium shot on brain with scales", "Flat, warm", "The asymmetry stated — a permanent feature",
 "Brain holding asymmetric scales; current setup heavier by brain's weighting; label",
 "Animated. Scales tip toward current setup; label appears. 2s."),

("This is not a rational calculation. It is architecture.",
 f"{STYLE} Wide shot. The character and the brain side by side. The brain points to a blueprint of itself — structural, architectural, designed. Label on the blueprint: 'ARCHITECTURE.' Not a mistake. Not a flaw. A design feature. Bold label: 'NOT RATIONAL. ARCHITECTURAL.'",
 "Wide shot", "Flat, white, blueprint visible", "The reframe — built in, not chosen",
 "Brain pointing to own architectural blueprint; design feature not mistake; label",
 "Static. Blueprint visible; label prominent. 2s."),

("And every financial institution in the world has had decades to study it.",
 f"{STYLE} Wide shot. Bank buildings, insurance towers, pension fund logos arranged in a row — all pointing to the architectural blueprint from the previous beat. Research papers floating around each building. A bold label: 'DECADES OF STUDY.' The brain villain watches from a high window, satisfied. They know the blueprint.",
 "Wide shot", "Flat, white, institutions studying blueprint", "The industry's awareness — they know the architecture",
 "Financial institutions all studying character's brain blueprint; decades of research",
 "Static. Institutions and papers visible; brain villain watching. 3s."),

# ── THE POPULAR MISREADING ────────────────────────────────────────────────────

("Everyone who hears about status quo bias arrives at the same conclusion.",
 f"{STYLE} Wide shot. A crowd of cartoon figures — diverse, different expressions — all shown with matching thought bubbles above their heads. The thought bubbles all contain the same words, not yet visible. Bold label: 'SAME CONCLUSION.'",
 "Wide crowd shot", "Flat, white", "The setup — the wrong conclusion is universal",
 "Crowd with matching thought bubbles; same conclusion incoming; label above",
 "Static. Crowd visible; thought bubbles uniformly shaped. 2s."),

("Some people are just passive. Some people do not take their finances seriously. Some people need to try harder.",
 f"{STYLE} Wide shot. The thought bubbles from the crowd now reveal their content — three labels: 'JUST PASSIVE,' 'DON'T TAKE IT SERIOUSLY,' 'NEED TO TRY HARDER.' All pointing to individual figures in the crowd. Expression in the crowd: judgmental. Bold label: 'THE POPULAR MISREADING.'",
 "Wide shot, thought bubbles visible", "Flat, white", "The misreading named — character blame",
 "Three judgment labels in crowd thought bubbles; popular misreading label",
 "Animated. Three labels appear in thought bubbles. 3s."),

("That is not what the research shows.",
 f"{STYLE} Wide shot. A bold red X appears over the three judgment labels. Research papers float in — Madrian & Shea, Johnson & Goldstein, Samuelson & Zeckhauser. Bold label: 'NOT WHAT THE RESEARCH SHOWS.' The misreading is being corrected.",
 "Wide shot", "Flat, white, red X on labels", "The correction — research overrides the popular read",
 "Red X on three judgment labels; research papers floating in; correction label",
 "Animated. Red X appears; research papers float in. 2s."),

("Madrian and Shea found the same patterns in companies full of highly educated, high-income professionals.",
 f"{STYLE} Wide shot. A corporate office full of suited, briefcased, high-income professional figures. The same status quo bias bar chart appears above them — identical to the general population chart. Bold label: 'HIGH-INCOME PROFESSIONALS — SAME BIAS.'",
 "Wide shot", "Flat, white", "The first professional group — bias is the same",
 "High-income professionals in corporate office; same bias chart above them",
 "Static. Professional crowd visible; bias chart identical. 2s."),

("Johnson and Goldstein found no relationship between donation rates and financial literacy or civic engagement.",
 f"{STYLE} Wide diagram. Two correlation charts side by side: FINANCIAL LITERACY vs DONATION RATE — flat line, no relationship. CIVIC ENGAGEMENT vs DONATION RATE — flat line, no relationship. Bold label: 'NO CORRELATION.' The variable that mattered was only the form.",
 "Wide diagram, two correlation charts", "Flat, white", "Correlation destroyed — literacy and engagement don't predict it",
 "Two flat correlation lines; no relationship found; form was the only variable",
 "Static. Both flat lines visible; no correlation label. 2s."),

("Samuelson and Zeckhauser ran their experiments on economists.",
 f"{STYLE} Wide shot. A seminar room. The experiment participants from the theory section — but now revealed as economists. Name badges visible: small chart icons, ECONOMIST labels. The same status quo bias charts above them. Expression on the researchers: they expected this.",
 "Wide shot", "Flat, white", "The economist group — the most ironic finding",
 "Economists as experiment participants; same bias shown; researchers unsurprised",
 "Static. Economist figures visible; bias chart identical to others. 2s."),

("The status quo bias showed up in all of them.",
 f"{STYLE} Wide shot. Three groups lined up: GENERAL PUBLIC, HIGH-INCOME PROFESSIONALS, ECONOMISTS. Above each group: identical bias bar charts. Bold label spanning all three: 'ALL OF THEM.' No group is exempt. No expertise protects.",
 "Wide shot, three groups", "Flat, white", "The universality — no exception found anywhere",
 "Three groups; identical bias charts above all; ALL OF THEM label",
 "Static. Three groups side by side; label spans all. 3s."),

("This is not a character flaw. It is architecture.",
 f"{STYLE} Wide shot. The architectural blueprint of the brain from the mechanism section returns. Bold label: 'NOT A CHARACTER FLAW — ARCHITECTURE.' The blueprint is clean and structural. The main character stands beside it, no longer ashamed. The brain inside the skull nods in agreement.",
 "Wide shot, blueprint", "Flat, white", "The reframe — relief and empowerment",
 "Brain blueprint returns; NOT A CHARACTER FLAW label; character standing tall",
 "Static. Blueprint visible; character posture confident. 2s."),

("Your brain was not designed to actively re-evaluate every standing arrangement in your life on a recurring basis.",
 f"{STYLE} Wide diagram. A list of standing arrangements: PENSION, BANK ACCOUNT, INSURANCE, SUBSCRIPTIONS, INVESTMENT FUND. Beside each: a recurring calendar icon. Below: a brain figure with a hand raised — STOP. Label: 'NOT DESIGNED FOR THIS.' The brain was never meant to audit everything constantly.",
 "Wide diagram", "Flat, white", "The design limit — constant re-evaluation was never the plan",
 "List of standing arrangements with recurring calendars; brain stopping; NOT DESIGNED label",
 "Static. List visible; brain's stop signal clear. 3s."),

("It was designed to conserve energy by treating existing states as safe and change as risky.",
 f"{STYLE} Wide diagram. Two categories: EXISTING STATE — green, labeled SAFE, low energy cost. CHANGE — red, labeled RISKY, high energy cost. The brain's design logic is clear: conserve by defaulting to safe. A small energy conservation meter beside the brain shows efficient use.",
 "Wide diagram", "Flat, white, green vs red categories", "The design logic — energy conservation is the goal",
 "Existing state as safe green; change as risky red; brain conserving energy",
 "Static. Two categories visible; conservation meter shown. 2s."),

("That was a good design. For most of human history, the existing state usually was safe.",
 f"{STYLE} Wide shot. A prehistoric scene — same flat cartoon style. The main character's ancestor stands in a landscape with a cave, fire, familiar surroundings. The EXISTING STATE label: SAFE. The environment around them is stable. The design served them well. The brain inside the skull is small and content.",
 "Wide shot, prehistoric setting", "Flat, warm, prehistoric tones", "The origin context — the design worked in its original environment",
 "Ancestor character in prehistoric setting; existing state safe; brain content",
 "Static. Prehistoric setting holds. Existing state safe label. 2s."),

("The financial industry discovered what happens when you build products around that design.",
 f"{STYLE} Wide shot. Flash forward — the prehistoric scene dissolves into the modern bank building from the opening. The same brain villain at the window, now holding the architectural blueprint of the human brain. The bank was built to fit the brain's default preference. Bold label: 'BUILT AROUND THAT DESIGN.'",
 "Wide shot, bank building", "Flat, white, modern contrast", "The exploitation — the industry found the design and used it",
 "Bank building with brain villain holding human brain blueprint; BUILT AROUND design label",
 "Animated. Prehistoric scene dissolves to modern bank. Brain villain reveals blueprint. 3s."),

# ── THE INDUSTRY ──────────────────────────────────────────────────────────────

("In the 1990s, the retail banking industry discovered something.",
 f"{STYLE} Wide shot. A bank building — large, imposing, dark navy — circa 1990s. Inside a conference room visible through the window: suited figures around a table, looking at a chart. A light bulb appears above the table. Bold label: '1990s · THE DISCOVERY.'",
 "Wide shot, bank building", "Flat, white, navy bank", "Historical anchor — the banking discovery",
 "Bank conference room; suited figures at table; light bulb discovery; 1990s label",
 "Static. Conference room visible. Light bulb above table. 2s."),

("Customers who never switched accounts were worth significantly more than customers who actively managed their finances.",
 f"{STYLE} Wide diagram. Two customer types side by side: NEVER SWITCHED (green value bar, tall) vs ACTIVELY MANAGED (shorter value bar). A bold arrow from NEVER SWITCHED to a profit icon: 'MORE VALUABLE.' The suited figures from the conference room point to the left bar with satisfaction.",
 "Wide diagram", "Flat, white, green bar taller", "The discovery stated — inertia is more profitable",
 "Two customer value bars; never switched taller; profit arrow; suited figures pointing",
 "Animated. Two bars appear; never switched clearly taller. 3s."),

("Not because they had more money. Because they asked for less.",
 f"{STYLE} Wide split diagram. Left: wealth comparison — BOTH EQUAL (equal bars). Right: demands comparison — NEVER SWITCHED: silent (empty speech bubble), ACTIVE MANAGER: speaking (speech bubble with question marks and demands). The profit came from silence, not wealth. Bold label: 'ASKED FOR LESS.'",
 "Wide split diagram", "Flat, white", "The mechanism of profitability — silence is the product",
 "Equal wealth vs unequal demands; never switched silent; asked for less label",
 "Static. Both comparisons visible; silence of never-switched prominent. 2s."),

("Today, the average savings account at a major bank pays 0.1 percent interest.",
 f"{STYLE} Wide shot. A bank counter scene. An employee figure in bank uniform stands behind the counter. On the counter: a savings account statement showing INTEREST RATE: 0.1%. A small icon of a coin barely moving. Bold diegetic label on the statement: '0.1% — YOUR RATE.'",
 "Wide shot, bank counter", "Flat, warm interior", "The current reality — your money earns almost nothing",
 "Bank employee with savings statement showing 0.1% rate; barely moving coin icon",
 "Static. Statement holds; 0.1% label prominent. 2s."),

("The central bank base rate: 5.25 percent.",
 f"{STYLE} Same bank counter. Behind the employee, a large government building icon — the central bank — with a bold label: 'BASE RATE: 5.25%.' The gap between 5.25% and 0.1% is now visible. A bold double-headed arrow between the two rates begins to suggest the spread.",
 "Wide shot, bank counter with central bank icon", "Flat, white, central bank prominent", "The rate gap introduced — the spread is huge",
 "Bank 0.1% vs central bank 5.25%; double arrow between rates; gap visible",
 "Animated. Central bank label appears; double arrow between rates. 2s."),

("The bank is borrowing your money at 0.1 percent and deploying it at 5 percent.",
 f"{STYLE} Wide flow diagram. Your money flows from YOUR ACCOUNT (0.1% label) → into the BANK (large building) → out to DEPLOYED USES (loans, mortgages, investments — 5% label). The flow is clean and directional. Bold label: 'YOUR MONEY, THEIR RETURN.'",
 "Wide flow diagram", "Flat, white, flow direction clear", "The mechanism of the spread — your money, their profit",
 "Money flowing from your account through bank to deployments; rate difference labeled",
 "Animated. Flow arrows appear in sequence; rates labeled at each point. 3s."),

("The difference is not a fee. It is not a charge. It is not disclosed anywhere in large print.",
 f"{STYLE} Wide shot. Three items crossed off with a red X: FEE ✗, CHARGE ✗, LARGE PRINT DISCLOSURE ✗. The spread disappears into the background — invisible, unlabeled, deliberately quiet. Bold label: 'IT IS INVISIBLE.'",
 "Wide shot", "Flat, white, red Xs", "The invisibility — no disclosure, no transparency",
 "Three crossed-off labels; spread invisible in background; IT IS INVISIBLE label",
 "Animated. Three red Xs appear; spread fades to invisible. 2s."),

("It is just the default. And the bank knows, with statistical certainty, that most customers will never change it.",
 f"{STYLE} Wide shot. The bank building with the brain villain at the window. The villain holds a statistical chart: 'X% WILL NEVER SWITCH.' Expression: calm certainty. The spread running below — invisible but steady. Bold label: 'STATISTICAL CERTAINTY.'",
 "Wide shot, bank building", "Flat, white, navy bank", "The bank's confidence — statistical certainty of inertia",
 "Brain villain with statistical certainty chart; spread running invisibly below",
 "Static. Brain villain holds chart calmly. Spread visible below. 3s."),

("The bet is not that you are unaware. The bet is that awareness alone is not enough to make you act.",
 f"{STYLE} Wide shot. Two boxes side by side: UNAWARE (gray, crossed out — not the bet) vs AWARE BUT WON'T ACT (green, the actual bet). The brain villain points to the second box. Bold label: 'THE REAL BET.' The sophistication of the bet is the point.",
 "Wide shot", "Flat, white", "The sophistication revealed — awareness is not protection",
 "Unaware crossed out; aware but won't act highlighted; brain villain pointing; real bet label",
 "Static. Brain villain points to second box. Real bet label appears. 3s."),

("They are right. Studies show that even customers who know they are on a poor-rate account do not switch.",
 f"{STYLE} Wide diagram. A two-column table: Column 1: KNOWS ABOUT BETTER RATES — YES. Column 2: SWITCHED — NO. Rows of customer data showing the same pattern. Bold label: 'KNOWLEDGE ≠ ACTION.' The pattern is consistent and documented.",
 "Wide diagram, table", "Flat, white", "The data confirms the bet — knowing is not enough",
 "Table showing knows but doesn't switch; KNOWLEDGE ≠ ACTION label; consistent pattern",
 "Static. Table holds; label prominent. 3s."),

("The pension fund industry runs the same calculation.",
 f"{STYLE} Wide shot. Transition from bank building to pension fund building — similar imposing architecture, different logo. The same brain villain visible in the window, different building. Same posture. Bold label: 'SAME CALCULATION.'",
 "Wide shot, pension fund building", "Flat, white, navy building", "The industry expands — same logic, different sector",
 "Pension fund building with brain villain; same posture as bank; same calculation label",
 "Static. Building holds. Brain villain identical posture. 2s."),

("The average actively managed pension fund charges 1.5 percent per year in fees.",
 f"{STYLE} Close-up on a pension statement. Bold text: 'ANNUAL MANAGEMENT CHARGE: 1.5%.' Below the charge: a small annual fee amount in euros. A small fee meter on the statement. The number looks small — the compounding effect is not yet visible.",
 "Close-up on pension statement", "Flat, warm", "The fee introduced — looks small until compounded",
 "Pension statement with 1.5% AMC; fee meter; small annual amount visible",
 "Static. Statement holds; 1.5% prominent. 2s."),

("A global index fund tracking the same market charges 0.07 percent.",
 f"{STYLE} Same close-up format, different statement. An index fund statement: 'ANNUAL MANAGEMENT CHARGE: 0.07%.' Beside the two statements side by side: 1.5% vs 0.07%. Bold comparison label: '21X MORE EXPENSIVE.' The fee difference is stark in percentage terms.",
 "Close-up, two statements side by side", "Flat, white", "The alternative — dramatically cheaper",
 "Index fund 0.07% vs pension fund 1.5%; 21x more expensive label",
 "Static. Two statements side by side; comparison label above. 2s."),

("Over a 30-year working life, that difference in fees compounds into tens of thousands of euros less at retirement.",
 f"{STYLE} Wide diagram. Two compound growth lines over 30 years: INDEX FUND (green, higher line) and ACTIVE FUND (red, lower line due to fee drag). The gap between the lines at year 30 is large — labeled: 'TENS OF THOUSANDS LESS.' The compounding of fees is shown visually.",
 "Wide diagram, 30-year chart", "Flat, white, green vs red lines", "The compounding cost — the fee gap grows into real money",
 "30-year compound chart; index fund vs active fund; gap labeled tens of thousands",
 "Animated. Both lines grow over 30 years; gap widens visibly; label at year 30. 3s."),

("The default fund is almost never the cheapest fund.",
 f"{STYLE} Wide shot. A pension fund menu — multiple options visible. The DEFAULT label is on a middle option — not the cheapest, not the most expensive. A green arrow points to the cheapest option (0.07%): 'NOT HERE.' The default arrow points elsewhere: 'DEFAULT IS HERE.' The mismatch is visible.",
 "Wide shot, fund menu", "Flat, white", "The placement — default ≠ cheapest",
 "Fund menu; default label on non-cheapest option; cheapest option not the default",
 "Static. Menu holds; default vs cheapest arrows visible. 2s."),

("It is the fund the provider chose to place there. And 86 percent of enrolled employees never change it.",
 f"{STYLE} Wide shot. The suited figure from earlier — the provider — placing the DEFAULT label on a specific fund on the menu. In the background, 86 figures standing still (auto-enrolled, never changed). Only 14 have moved to a different fund. Bold label: '86% NEVER CHANGED IT.'",
 "Wide shot", "Flat, white", "The provider's choice — and the employees who accepted it",
 "Provider placing default label; 86 figures unchanged; 14 changed; label above",
 "Static. Provider placing label; crowd of 86 unchanged behind. 3s."),

("The insurance industry discovered auto-renewal.",
 f"{STYLE} Wide shot. Transition to an insurance building. A calendar on the wall shows AUTO-RENEWAL dates circled in red — each year, the same date. A small stack of renewal letters beside the calendar. Bold label: 'AUTO-RENEWAL.' The mechanism is set and running.",
 "Wide shot, insurance building", "Flat, warm, renewal calendar", "Third industry — auto-renewal as the mechanism",
 "Insurance building; auto-renewal calendar; renewal letters stacked; label",
 "Static. Calendar and letters visible. 3s."),

("Every year, your premium increases slightly. The letter arrives. The language is dense. The deadline is short.",
 f"{STYLE} Close-up. A renewal letter in the main character's hands. The text on the letter is dense, small, difficult to parse. A small highlight on the premium: UP 8% FROM LAST YEAR. A deadline stamp: RESPOND BY [DATE — SOON]. The character's expression: overwhelmed, likely to do nothing.",
 "Close-up on renewal letter", "Flat, warm", "The engineering of inaction — dense, short deadline",
 "Character holding dense renewal letter; 8% increase highlighted; tight deadline visible",
 "Static. Letter in hands; character expression overwhelmed. 2s."),

("The path of least resistance is to do nothing. The policy renews. The higher premium clears.",
 f"{STYLE} Wide shot. The renewal letter placed back on the counter — nothing done. A calendar flips forward: new policy year begins. A bank statement in the corner shows the higher premium clearing automatically. Expression on the character: forgot about it. Bold label: 'PATH OF LEAST RESISTANCE.'",
 "Wide shot", "Flat, warm", "The inertia cycle — do nothing, premium renews higher",
 "Letter untouched; calendar flips; higher premium clears automatically",
 "Animated. Calendar flips; premium clears; character unaware. 3s."),

("Across the industry, auto-renewal customers pay an average of 30 percent more than customers who actively switch.",
 f"{STYLE} Wide diagram. Two customer figures side by side: AUTO-RENEWAL (pays 130) vs ACTIVE SWITCHER (pays 100). Bold label: '+30% PREMIUM.' A bold percentage tag on the auto-renewal figure: 'LOYALTY TAX.' The framing redefines the 30% as a tax on inertia.",
 "Wide diagram", "Flat, white, 30% prominent", "The cost quantified — loyalty tax on inertia",
 "Auto-renewal pays 130 vs active switcher pays 100; +30% label; loyalty tax tag",
 "Static. Both figures visible; 30% gap prominent. 3s."),

("The product being sold is not insurance. The product being sold is your inertia.",
 f"{STYLE} Wide shot. The insurance building with a bold rebranded sign: not 'INSURANCE' but 'INERTIA — FOR SALE.' The brain villain at the window, now holding a small 'INERTIA' product box with a price tag. Expression: the real business model, finally named.",
 "Wide shot, insurance building", "Flat, white", "The reframe — inertia is the actual product",
 "Insurance building rebranded to INERTIA FOR SALE; brain villain with inertia product box",
 "Static. Rebranded sign holds. Brain villain with product box. 3s."),

# ── THE REAL CONCLUSION ───────────────────────────────────────────────────────

("Richard Thaler — the same economist from the last video — had spent years watching institutions exploit defaults against the people they were supposed to serve.",
 f"{STYLE} Wide shot. Richard Thaler as a cartoon figure — recognizable style, professorial. He stands watching the bank, pension, and insurance buildings from a distance, with a troubled expression. Documents in hand. Bold label: 'RICHARD THALER — AGAIN.' His concern is visible.",
 "Wide shot", "Flat, white", "Thaler reintroduced — the connector to previous video",
 "Thaler figure watching financial institutions with troubled expression; documents",
 "Static. Thaler holds documents. Expression concerned. 2s."),

("In 2008, he and legal scholar Cass Sunstein published a book called Nudge.",
 f"{STYLE} Wide shot. Thaler and a second figure — Sunstein, professorial, glasses, legal documents — stand together. Between them: a large book cover floating. The book is bold and clean: 'NUDGE — THALER & SUNSTEIN.' Bold label: '2008.' Expression: collaborative, purposeful.",
 "Wide shot", "Flat, white, book prominent", "The book introduced — a response to exploitation",
 "Thaler and Sunstein with Nudge book between them; 2008 label; purposeful expressions",
 "Static. Book floats between them. 2s."),

("The central argument: if defaults are inevitable — and they are — they should be designed for the person, not for the institution.",
 f"{STYLE} Wide diagram. Two default directions: FOR THE INSTITUTION (arrow pointing to profit chart) vs FOR THE PERSON (arrow pointing to retirement nest egg). The key word: INEVITABLE — defaults always exist. The question is only which direction they point. Bold label: 'DESIGN THE DEFAULT FOR THE PERSON.'",
 "Wide diagram", "Flat, white", "The central insight — defaults can be flipped",
 "Two default directions; institution vs person; INEVITABLE label; design choice",
 "Static. Both directions visible; FOR THE PERSON arrow highlighted. 3s."),

("They called it libertarian paternalism. You remain free to choose anything. But the default is set in your favor.",
 f"{STYLE} Wide diagram. A choice diagram: all options available — nothing blocked. But the DEFAULT marker is moved to the best option for the person. A small label: 'FREE TO CHOOSE ANYTHING' (all options visible). And: 'DEFAULT IN YOUR FAVOR.' Both conditions visible simultaneously.",
 "Wide diagram", "Flat, white", "The concept named — freedom preserved, default improved",
 "All options available with default on best option; libertarian paternalism concept",
 "Static. Default marker on best option; all options still accessible. 2s."),

("The United Kingdom used it. In 2012, the government mandated automatic pension enrollment for all employed workers.",
 f"{STYLE} Wide shot. A UK government building — flat, clean, recognizable style. A bold policy document floating: 'AUTO-ENROLLMENT — ALL EMPLOYED WORKERS — 2012.' Small worker figures across the country — all automatically enrolled. Bold label: '2012 · UK POLICY.'",
 "Wide shot, UK government building", "Flat, white", "The real-world application — government scale",
 "UK government building; policy document; worker figures auto-enrolled; 2012 label",
 "Static. Policy document prominent. Workers enrolled across country. 2s."),

("Participation went from 55 percent to 85 percent in two years.",
 f"{STYLE} Wide diagram. Two large pie charts side by side: BEFORE (55% enrolled, 45% not) and AFTER TWO YEARS (85% enrolled, 15% not). A bold arrow between them labeled: '+30 PERCENTAGE POINTS.' Below: 'TWO YEARS.' The jump is the same mechanism as the Madrian & Shea study — replicated at national scale.",
 "Wide diagram, two pie charts", "Flat, white, green dominant", "The national result — same mechanism, national scale",
 "55% vs 85% enrollment pies; +30 point arrow; TWO YEARS label",
 "Animated. Before pie then after pie; arrow and label appear. 3s."),

("No campaigns. No education programs. No incentives beyond the enrollment itself.",
 f"{STYLE} Wide shot. Three items crossed off with a red X: CAMPAIGNS ✗, EDUCATION PROGRAMS ✗, INCENTIVES ✗. Bold label: 'NONE OF THESE.' The only change was the default. The three traditional policy tools failed where one default change succeeded.",
 "Wide shot", "Flat, white, red Xs", "The contrast — traditional tools failed, default worked",
 "Three traditional tools crossed off; NONE OF THESE label; default was sufficient",
 "Animated. Three red Xs appear in sequence. 2s."),

("One change: which option required action.",
 f"{STYLE} Wide shot. A single bold label fills the frame: 'ONE CHANGE: WHICH OPTION REQUIRED ACTION.' Below it: the opt-in vs opt-out forms from earlier, tiny in comparison. The simplicity is the lesson. The main character reads it. Expression: the insight landing.",
 "Wide shot, label dominant", "Flat, white", "The simplicity stated — one change, everything else followed",
 "ONE CHANGE label dominant; forms small below; character reading with insight",
 "Static. Label holds. Character expression shows understanding. 3s."),

("Thaler won the Nobel Prize in Economic Sciences in 2017.",
 f"{STYLE} Wide shot. A Nobel Prize medal floating — gold, clean, flat cartoon style. Thaler stands beside it, the same troubled-then-satisfied expression. Bold label: 'NOBEL PRIZE — ECONOMICS — 2017.' The journey from dismissed to decorated is visible.",
 "Wide shot", "Flat, white, Nobel medal prominent", "The Nobel — validation after years of work",
 "Thaler beside Nobel medal; 2017 label; journey from dismissed to decorated",
 "Static. Medal glows softly. Thaler's expression settled. 2s."),

("The insight that earned it: the most powerful financial intervention is not advice. It is not education. It is not willpower.",
 f"{STYLE} Wide diagram. Three interventions crossed off with red Xs: ADVICE ✗, EDUCATION ✗, WILLPOWER ✗. A bold question mark remains. What was it? The viewer is one beat from the answer.",
 "Wide diagram", "Flat, white, red Xs", "The setup for the final answer — three tools eliminated",
 "Three interventions crossed off; question mark remaining; answer one beat away",
 "Animated. Three red Xs appear; question mark holds. 2s."),

("It is the setting.",
 f"{STYLE} Wide shot. A single bold word fills the frame: 'THE SETTING.' The control panel from the opening — but now the dials are being turned in the right direction by the character, not by the suited figure. Bold diegetic label: 'THE SETTING IS THE INTERVENTION.' The viewer has the answer.",
 "Wide shot, control panel", "Flat, white, setting prominent", "The answer — the setting is the most powerful tool",
 "THE SETTING label dominant; character now turning own dials; intervention complete",
 "Animated. Label appears; character turns dials. 3s."),

("And the setting can work for you. Or against you.",
 f"{STYLE} Wide split. Left: control panel dials turned in favor of the character — green indicators, healthy settings. Right: the same panel with dials set by the suited figure — extractive settings, red indicators. Bold label across center: 'FOR YOU. OR AGAINST YOU.' The choice of who sets the default.",
 "Wide split", "Flat, white, green vs red indicators", "The binary — default direction is everything",
 "Green self-set dials vs red institution-set dials; FOR YOU OR AGAINST YOU label",
 "Static. Both panels visible; colors contrast. 2s."),

("For most people, right now, it is working against them.",
 f"{STYLE} Wide shot. The red-indicator panel from the previous split, now shown full screen. The brain villain at the bank window in the background, watching the red indicators run. A live counter ticks upward — the billion-dollar bet, still running. Bold label: 'RIGHT NOW.'",
 "Wide shot", "Flat, white, red indicators running", "The current state — for most people, the default is extractive",
 "Red indicator panel running; brain villain watching; live counter ticking; RIGHT NOW label",
 "Animated. Counter ticks; brain villain watches calmly. 3s."),

# ── EL MOVIMIENTO ──────────────────────────────────────────────────────────────

("Here is what you do with this.",
 f"{STYLE} Medium shot. The main character turns directly to camera — relaxed, practical, ready. The brain inside the skull shifts from its usual smug expression to a focused, action-oriented one. The control panel from the video is visible behind them, dials ready to be turned. Bold label: 'THE MOVE.' Clean white background.",
 "Medium shot, direct address", "Flat, white, single spotlight", "The transition into action — viewer attention sharpens",
 "Character turns to camera; brain shifts to practical expression; control panel behind",
 "Static. Character holds direct address; brain focused. 2s."),

("Open your pension account today — not this week, today — and find the default fund. Look at the annual management charge. If it is above 0.3 percent, you are paying for the default, not for performance. Switch to the lowest-cost index fund available in your plan.",
 f"{STYLE} Wide shot. The character sits at a laptop with a pension account open. The screen shows: DEFAULT FUND — AMC: 1.5%. A bold arrow points to a different option: INDEX FUND — AMC: 0.07%. A hand reaches to the keyboard. Bold label: 'SWITCH TODAY — NOT THIS WEEK.' The action is specific and immediate.",
 "Wide shot", "Flat, warm, laptop screen visible", "The first action — pension audit and switch",
 "Character at laptop with pension account; default fund vs index fund; switch label",
 "Animated. Arrow points from default to index fund; hand moves to keyboard. 3s."),

("Find your savings account interest rate. If it is more than one percent below the central bank base rate, you are gifting money to the bank every month. A high-yield savings account at a challenger bank takes twenty minutes to open. That twenty minutes, compounded over five years, is worth more than most people expect.",
 f"{STYLE} Wide shot. A savings account statement showing 0.1% rate. Beside it: a challenger bank app showing 4.5% rate. A bold arrow: 'SWITCH IN 20 MINUTES.' A compound interest chart below shows the 5-year difference. Label: 'YOUR 20 MINUTES = THEIR LOSS.'",
 "Wide shot", "Flat, white, comparison visible", "The second action — savings rate audit and switch",
 "Low-rate statement vs high-yield app; 20 minute switch label; 5-year compound chart",
 "Static. Comparison holds; 20-minute label prominent. 3s."),

("Check every insurance policy you hold for auto-renewal clauses. Set a calendar reminder thirty days before each renewal date. The reminder is the system. You do not need willpower. You need the reminder in the calendar.",
 f"{STYLE} Wide shot. The character's calendar — insurance renewal dates circled. A 30-day-before reminder added beside each: bright green flag. Bold label: 'THE REMINDER IS THE SYSTEM.' A small graphic: WILLPOWER (crossed out) vs CALENDAR REMINDER (checkmark). The system does the work.",
 "Wide shot, calendar", "Flat, warm, green flags visible", "The third action — calendar reminder as system",
 "Calendar with renewal dates and 30-day reminders; willpower crossed out; system label",
 "Animated. Green flags added to calendar; label appears. 3s."),

("Now use the default against itself. Set up an automatic investment transfer on the same day your salary arrives — before you see the money, before the spending begins. You are not fighting the system. You are becoming the default.",
 f"{STYLE} Wide shot. A salary payment arrow arriving at the character's account. Before it reaches the main balance, an automatic arrow diverts a portion directly to INVESTMENT ACCOUNT. The spending account receives the rest. Bold label: 'BECOME THE DEFAULT.' The character is not fighting — they are using the mechanism.",
 "Wide shot", "Flat, white, diversion arrow green", "The fourth action — becoming the default",
 "Salary arriving; automatic diversion to investment before spending; BECOME THE DEFAULT label",
 "Animated. Salary arrives; automatic diversion happens before balance shows. 3s."),

("And find one subscription you have not actively chosen to keep in the last six months. Cancel it today. Not because the amount is large. Because the act of auditing your defaults — once — trains the behavior that the financial industry has spent decades trying to prevent.",
 f"{STYLE} Wide shot. A subscription list on a screen. The character scans the list — one item highlighted: a subscription with a cobweb on it, last actively reviewed six months ago. A cancel button highlighted. Bold label: 'ONE AUDIT TRAINS THE HABIT.' The act is symbolic as much as financial.",
 "Wide shot", "Flat, warm, subscription list", "The fifth action — one audit to train the behavior",
 "Subscription list with cobwebbed item; cancel button; ONE AUDIT TRAINS HABIT label",
 "Animated. Cobwebbed item highlighted; cancel button pressed. 3s."),

# ── THE ENDING ────────────────────────────────────────────────────────────────

("You cannot stop institutions from setting defaults.",
 f"{STYLE} Wide shot. The bank, pension, and insurance buildings — all three visible in a row, imposing. Each has a DEFAULTS: SET sign visible. The character stands in front of them, small but present. The buildings are not going away. Expression: realistic, not defeated.",
 "Wide shot", "Flat, white, three institutions", "The honest limit — defaults will always exist",
 "Three institutions with defaults set; character small but present; realistic expression",
 "Static. Three buildings visible. Character composed. 2s."),

("Every financial product you will ever own arrives with settings someone else chose.",
 f"{STYLE} Wide shot. A delivery truck arrives — labeled FINANCIAL PRODUCTS. Packages being unloaded: PENSION, SAVINGS, INSURANCE, INVESTMENT FUND. Each package has a SETTINGS PRE-CONFIGURED tag on it, sealed by someone else. The character receives the packages.",
 "Wide shot", "Flat, warm", "The universal truth — all products arrive with defaults",
 "Delivery truck with pre-configured financial product packages; character receiving them",
 "Animated. Packages unloaded one by one; each shows pre-configured tag. 3s."),

("The pension. The savings account. The insurance. The investment fund. The bank itself.",
 f"{STYLE} Wide shot. The delivered packages opened — five icons visible: PENSION, SAVINGS, INSURANCE, INVESTMENT FUND, BANK. Each has a dial showing its default setting. All dials set by someone else. The control panel from the video's opening, but now owned by the character.",
 "Wide shot", "Flat, white, five icons", "The full inventory — every product is a default",
 "Five financial product icons opened; each with pre-set dial; character's control panel",
 "Static. Five icons with pre-set dials visible. 2s."),

("All of it came with a default. And the default was not chosen for you.",
 f"{STYLE} Wide diagram. The five icons with a bold label beside each: 'NOT CHOSEN FOR YOU.' The suited figure from earlier — ghost-like now, diminished — is shown in the background having set all five. Expression on the character: understanding, not anger. The system is visible.",
 "Wide diagram", "Flat, white, suited figure in background", "The summary — not chosen for you, but now visible",
 "Five icons with NOT CHOSEN FOR YOU labels; suited figure diminished in background",
 "Static. All five labels visible; suited figure present but small. 3s."),

("But you can read the settings.",
 f"{STYLE} Wide shot. The character now stands at the control panel — the one from the beginning of the video. The dials are the same but the character holds a magnifying glass, reading each one carefully. Expression: calm, capable. The brain inside the skull has its focused, watchful expression.",
 "Wide shot", "Flat, white, soft panel glow", "The capability — reading the settings is the skill",
 "Character with magnifying glass at control panel; reading each dial; capable expression",
 "Static. Magnifying glass examining dials. Brain focused. 2s."),

("Once a year. Thirty minutes. One question per account.",
 f"{STYLE} Wide diagram. A simple annual audit framework: ONCE A YEAR (calendar icon) — THIRTY MINUTES (clock icon) — ONE QUESTION PER ACCOUNT (question mark icon). Three clean icons in a row. Bold label: 'THE AUDIT.' Simple, practical, executable.",
 "Wide diagram", "Flat, white, three icons", "The practice — annual audit is the system",
 "Three audit framework icons; ONCE A YEAR, THIRTY MINUTES, ONE QUESTION; label",
 "Static. Three icons visible; THE AUDIT label. 2s."),

("Is this the setting I would choose if I were choosing deliberately?",
 f"{STYLE} Close-up on the control panel — one dial in focus. Above it: the question in bold text: 'IS THIS THE SETTING I WOULD CHOOSE IF I WERE CHOOSING DELIBERATELY?' The character's hand hovers over the dial — not yet moving, just reading. The question is the practice.",
 "Close-up on dial", "Flat, white, question text prominent", "The question — the entire practice in one sentence",
 "Single dial in focus; deliberate choice question above; character's hand hovering",
 "Static. Question text holds. Hand hovering. 2s."),

("The bank made a billion-dollar bet that you would never ask that question.",
 f"{STYLE} Wide shot. The bank building from the opening — imposing, navy. The brain villain at the window, watching. A large betting slip visible through the glass: 'THE BET: VIEWER NEVER ASKS THE QUESTION — VALUE: $1,000,000,000.' Expression on the brain villain: calm confidence.",
 "Wide shot, bank building", "Flat, white, navy bank", "The bet named — a billion dollars on your inaction",
 "Bank with billion-dollar betting slip visible; brain villain confident; BET label",
 "Static. Betting slip prominent. Brain villain watching. 3s."),

("The bet is still running.",
 f"{STYLE} Same wide shot. The live counter from beat 8 — ticking upward — is now visible again in the bank window. The bet has not ended. It is running now. On every viewer who finishes this video and does not act. Bold label: 'STILL RUNNING.'",
 "Wide shot, bank building", "Flat, white", "The ongoing bet — it continues until you act",
 "Live counter ticking in bank window; bet still running; STILL RUNNING label",
 "Animated. Counter ticks upward. Label appears. 2s."),

("Every video on this channel is one way your financial gut has been hacked.",
 f"{STYLE} Wide shot, white background. The main character faces camera — the brain inside the skull with its composed, watchful expression. A row of small icons stretches behind: bandwidth, dopamine, somatic markers, mental accounting, status quo — each labeled. The channel's pattern is visible. Expression: the mission.",
 "Wide shot, direct address", "Flat, white", "Channel mission — the promise to the viewer",
 "Character facing camera; row of channel topic icons behind; brain watchful",
 "Static. Topic icons glow softly; character holds direct address. 3s."),

("This is how they turned your inaction into their income.",
 f"{STYLE} Wide shot, closing frame. The bank, pension, and insurance buildings — all three visible, lit warmly. A flow of invisible euro coins moving from the character's direction toward each building — the inaction dividend running silently. The character watches it now. Expression: recognition, understanding, and readiness. The buildings are not closed. But they are no longer invisible.",
 "Wide shot, closing frame", "Flat, white, warm building light", "The closing image — the mechanism visible, the viewer informed",
 "Three institutions receiving inaction dividend; character watching and understanding",
 "Static. Character expression is recognition and readiness. Final hold. 3s."),

]  # end BEATS


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    TITLE = "The Billion-Dollar Bet Your Bank Is Making Against You Right Now"
    SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 6"
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
        1:   "HOOK",
        9:   "THE IMPOSSIBILITY",
        16:  "THE CHECKBOX",
        36:  "THE THEORY",
        46:  "THE EXPERIMENTS",
        61:  "THE MECHANISM",
        75:  "THE POPULAR MISREADING",
        87:  "THE INDUSTRY",
        108: "THE REAL CONCLUSION",
        121: "EL MOVIMIENTO",
        127: "THE ENDING",
    }

    COL_LABELS = ["#", "SEGMENT (NARRATION)", "IMAGE PROMPT", "CAMERA",
                  "LIGHTING", "MOOD / TONE", "CHARACTER ACTION", "VIDEO MOTION"]
    COL_WIDTHS = [Inches(0.35), Inches(1.7), Inches(2.5), Inches(0.9), Inches(0.8),
                  Inches(1.0), Inches(1.0), Inches(1.25)]

    tbl = doc.add_table(rows=1, cols=8)
    tbl.style = 'Table Grid'
    hdr = tbl.rows[0].cells
    for i, label in enumerate(COL_LABELS):
        hdr[i].width = COL_WIDTHS[i]
        p = hdr[i].paragraphs[0]
        run = p.add_run(label)
        run.bold = True
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        from docx.oxml.ns import qn
        from docx.oxml import OxmlElement
        tc = hdr[i]._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), '2C3E50')
        tcPr.append(shd)

    def cell_text(cell, text, bold=False, sz=8, color=None):
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        run = p.add_run(text)
        run.bold = bold
        run.font.size = Pt(sz)
        if color:
            run.font.color.rgb = color

    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    def shade_row(row, hex_color):
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), hex_color)
            tcPr.append(shd)

    for beat_num, beat in enumerate(BEATS, 1):
        seg, scene, cam, light, mood, action, video = beat

        if beat_num in SECTION_STARTS:
            sec_row = tbl.add_row()
            sec_row.cells[0].merge(sec_row.cells[7])
            p = sec_row.cells[0].paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(f"── {SECTION_STARTS[beat_num]} ──")
            run.bold = True
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            from docx.enum.text import WD_ALIGN_PARAGRAPH as WAP
            p.alignment = WAP.CENTER
            shade_row(sec_row, 'B02A2A')

        row = tbl.add_row()
        for i, w in enumerate(COL_WIDTHS):
            row.cells[i].width = w

        cell_text(row.cells[0], str(beat_num), bold=True, sz=9)
        cell_text(row.cells[1], seg, bold=True, sz=8)
        cell_text(row.cells[2], scene, sz=7)
        cell_text(row.cells[3], cam, sz=7)
        cell_text(row.cells[4], light, sz=7)
        cell_text(row.cells[5], mood, sz=7)
        cell_text(row.cells[6], action, sz=7)
        cell_text(row.cells[7], video, sz=7)

        bg = 'F9F9F9' if beat_num % 2 == 0 else 'FFFFFF'
        shade_row(row, bg)

    all_lines = [b[0] for b in BEATS]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = len(BEATS)

    doc.add_paragraph()
    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(
        f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min narration")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Status_Quo_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
