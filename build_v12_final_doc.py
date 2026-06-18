#!/usr/bin/env python3
"""
V12 FINAL — Production Document (102 beats)
Why Willpower Fails Every Payday — And the One Decision That Stops It
Full image prompts + camera + lighting + mood + character action + video motion
CHANGES vs. previous version:
  - CTA moved to beat 40 (~39%), after "Alex does." emotional low
  - Identity Close trimmed from 14 to 9 beats
  - 15 visual-first violations fixed (text labels replaced with icon/visual-only)
  - Beats 2-3: differentiated eye direction (down-left vs up-right)
  - Beats 24-26: broke 3-diagram sequence with Alex-centered beat 25
  - Beats 46-48: varied camera (close-up / top-down / profile)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

TITLE    = "Why Willpower Fails Every Payday — And the One Decision That Stops It"
SUBTITLE = "NEUROCENTS · VIDEO 12 — FINAL"

STYLE = (
    "2D flat cartoon illustration, thick solid black outlines, clean solid color fills, "
    "no gradients. ALEX: large beige oval head, transparent glass upper skull revealing "
    "pink cartoon brain villain, small black dot eyes, thin neutral mouth, black spiky hair, "
    "blue t-shirt, gray pants. Brain villain: pink cartoon brain character, heavy-lidded eyes, "
    "slight smirk, small teeth. Palette: beige skin (#F5E6C8), pink brain (#E8A598), blue shirt, "
    "gray pants, green for savings/gains, red for loss/danger, white for diagram scenes. 16:9, 1280x720."
)

# Format: (num, section, narration, image_prompt, camera, lighting, mood, char_action, video_motion)
BEATS = [
    # ── HOOK ──────────────────────────────────────────────────────────────────
    (1, "HOOK",
     "You've started a budget at least three times. It never survived payday.",
     "Alex at desk: three budget calendars pinned to wall, each crossed out in thick red marker. Pages torn. Empty mug.",
     "Medium shot", "Warm side light, late afternoon", "Recognition / Weary familiarity",
     "Alex stares at crossed-out calendars, slight resigned nod",
     "Slow push in toward the calendar wall"),

    (2, "HOOK",
     "Not because you're bad with money.",
     "Alex close-up, eyes directed DOWN AND LEFT — defeat/guilt direction. Clean white background. No props or text.",
     "Extreme close-up", "Flat neutral", "Defeat / Inward guilt",
     "Alex eyes drift down-left, brow slightly lowered — shame direction",
     "Static"),

    (3, "HOOK",
     "Not because you lack discipline.",
     "Alex close-up, eyes directed UP AND RIGHT — searching, self-questioning. Clean white background. No props or text.",
     "Extreme close-up", "Flat neutral", "Self-questioning / Searching",
     "Alex eyes drift up-right, brow slightly raised — wondering direction",
     "Static"),

    (4, "HOOK",
     "Because you've been fighting an automated system with a manual weapon.",
     "Split frame: LEFT massive red industrial gear system (automated, enormous). RIGHT Alex holding tiny notepad labeled 'BUDGET'. Extreme scale contrast.",
     "Wide establishing shot", "High contrast — dramatic", "Stark / Revealing",
     "Alex on right holds notepad up toward gear machine",
     "Slow zoom out to reveal full scale contrast"),

    (5, "HOOK",
     "One bank transfer. Set up once. It fires before you can stop it.",
     "Single clean green arrow: BANK ACCOUNT → SAVINGS. Automated clock icon beside it. White background.",
     "Medium shot, diagram style", "Clean white", "Efficient / Inevitable",
     "No character — clean motion graphic",
     "Arrow animates left to right with clock ticking"),

    (6, "HOOK",
     "Workers who used this went from three and a half percent savings to thirteen point six — in five years.",
     "Bar chart: LEFT small green bar '3.5%'. RIGHT dramatically taller green bar '13.6% — 5 YEARS'. White background.",
     "Wide shot, diagram", "Clean bright", "Impressive / Data clarity",
     "No character — clean data graphic",
     "RIGHT bar grows upward from baseline"),

    (7, "HOOK",
     "No extra income. No willpower. No spreadsheets.",
     "Three items with bold red X: income arrow (flat), flexing arm icon, spreadsheet grid.",
     "Wide shot, diagram", "Clean white", "Liberating",
     "No character",
     "Each X appears in sequence left to right"),

    (8, "HOOK",
     "Just one structural decision made on a calm Tuesday — not a panicked Friday.",
     "Calendar split: LEFT Tuesday (calm blue dot, clear sky). RIGHT Friday (red background, alarm icon, SALARY notification exploding).",
     "Wide shot, split panel", "LEFT: calm cool / RIGHT: chaotic warm red", "Contrast — peace vs. panic",
     "No character",
     "LEFT panel steady, RIGHT panel vibrates slightly"),

    (9, "HOOK",
     "Your brain is already calculating why this won't work for you.",
     "Alex's transparent skull: villain inside at small calculator, furiously typing objections. Villain expression: smirk + concentration.",
     "Medium close-up", "Internal glow from villain", "Conspiratorial",
     "Alex expression neutral outside, villain working intensely inside",
     "Slow push in on skull to reveal villain working"),

    (10, "HOOK",
     "That calculation is the last trap. This video was built to dismantle it.",
     "The villain's calculator cracks and shatters. Alex looks directly at camera, expression: calm and knowing.",
     "Medium close-up", "Neutral, stable", "Confident / Direct",
     "Alex direct eye contact with camera. Calculator debris settles.",
     "Static — holds eye contact"),

    # ── WHY KNOWING ISN'T ENOUGH ───────────────────────────────────────────────
    (11, "WHY KNOWING ISN'T ENOUGH",
     "Alex watched the last video.",
     "Alex on couch with laptop, V11 thumbnail visible on screen ('3 Brain Traps').",
     "Medium shot", "Living room warm evening light", "Engaged",
     "Alex leaning toward screen, attentive",
     "Slow push in on laptop screen"),

    (12, "WHY KNOWING ISN'T ENOUGH",
     "He understood every trap. He took notes. He sent it to his brother.",
     "Alex's notepad: three circled words — REWARD / MENTAL / PRESENT. Phone screen: 'Sent to: Daniel ✓'.",
     "Close-up alternating notepad / phone", "Warm interior", "Satisfied (false confidence)",
     "Alex writing then tapping phone to send",
     "Cut between notepad and phone"),

    (13, "WHY KNOWING ISN'T ENOUGH",
     "He felt the specific shift — the sensation of finally seeing the system clearly.",
     "Alex with genuine 'aha' expression. Through transparent skull: lightbulb (not villain-shaped) glowing.",
     "Medium close-up", "Warm glow from insight", "Illumination",
     "Alex expression opens — eyes widen with recognition",
     "Subtle light pulse from skull interior"),

    (14, "WHY KNOWING ISN'T ENOUGH",
     "And on Friday, the salary notification arrived.",
     "Phone screen close-up: 'SALARY DEPOSITED — €2,400'. Friday date visible above phone.",
     "Extreme close-up on phone", "Screen glow only", "Anticipation",
     "No character — just phone notification",
     "Notification animation — screen lights up"),

    (15, "WHY KNOWING ISN'T ENOUGH",
     "His brain asked the same question it always asks: what do I deserve?",
     "Villain in Alex's skull holding microphone, performing. Speech bubble: 'What do I deserve?'",
     "Medium shot, focus on skull interior", "Spotlight on villain", "Theatrical / Predatory",
     "Villain taps microphone, leans in, smirk",
     "Villain steps forward into spotlight"),

    (16, "WHY KNOWING ISN'T ENOUGH",
     "Same question. Same Friday. Same four hundred euros gone.",
     "Three stacked horizontal panels: Panel 1 'FRIDAY'. Panel 2 villain with microphone. Panel 3 '€400 GONE'. Like identical photocopies.",
     "Wide shot, stacked panels", "Flat / Clinical", "Mechanical repetition",
     "No character movement — static triplication",
     "Panels appear top to bottom in quick sequence"),

    (17, "WHY KNOWING ISN'T ENOUGH",
     "Knowing the name of a trap does not move the walls.",
     "Alex inside a small box/cage. On the wall: 'TRAP' label clearly visible. Alex reads it. Walls unchanged.",
     "Medium shot", "Confined, dim", "Trapped / Frustrated",
     "Alex looks at label on wall, then looks at camera — walls unchanged",
     "Static — no movement in walls"),

    (18, "WHY KNOWING ISN'T ENOUGH",
     "Every personal finance book gives Alex the diagnosis.",
     "Stack of personal finance books. Each cover: 'DIAGNOSIS' rubber stamp impression.",
     "Wide shot", "Library warm tones", "Ironic",
     "No character",
     "Books stack upward one by one"),

    (19, "WHY KNOWING ISN'T ENOUGH",
     "None of them give him the surgery.",
     "Same book stack — beside it: empty surgical table with unused tools. Surgery never happened.",
     "Wide shot", "Clinical contrast", "Absence / Gap",
     "No character",
     "Camera slowly moves from books to empty surgical table"),

    (20, "WHY KNOWING ISN'T ENOUGH",
     "The surgery requires removing the decision from Alex's hands entirely —",
     "Alex's open hands. A decision coin being mechanically LIFTED out of them by a robotic arm.",
     "Close-up on hands", "Neutral clean", "Releasing control",
     "Alex hands open, passive — not grabbing the coin as it lifts away",
     "Coin lifts slowly, mechanically upward"),

    (21, "WHY KNOWING ISN'T ENOUGH",
     "not making it easier to get right.",
     "The coin hovering above empty hands. Hands still open. Coin gone from reach.",
     "Close-up on hands", "Same clean neutral", "Finality",
     "Alex hands lower slightly — nothing to hold",
     "Coin continues upward, out of frame"),

    # ── WHY WILLPOWER FAILS ────────────────────────────────────────────────────
    (22, "WHY WILLPOWER FAILS",
     "Roy Baumeister — social psychologist at Florida State University —",
     "Academic nameplate: 'ROY BAUMEISTER' bold. 'Florida State University' below. Clean white background.",
     "Close-up, flat graphic", "Clean white", "Authoritative",
     "No character — clean typographic card",
     "Text appears word by word"),

    (23, "WHY WILLPOWER FAILS",
     "spent a decade measuring something he calls ego depletion.",
     "10-year timeline bar filled left to right. At the right end a fuel gauge depleting from full to empty. No text label for the concept — visual only.",
     "Wide shot, diagram", "Clinical white", "Scientific",
     "No character",
     "Timeline bar fills, then fuel gauge needle drops at the end"),

    (24, "WHY WILLPOWER FAILS",
     "Willpower is not a character trait. It is a finite daily resource.",
     "Two columns: LEFT muscle/trophy icon (symbol of personal quality) with red X through it. RIGHT fuel gauge going FULL to EMPTY. No text labels — visual contrast only.",
     "Wide shot, split diagram", "Clean contrast", "Revelatory",
     "No character",
     "Left X strikes through muscle icon; right gauge needle drops from full to empty"),

    (25, "WHY WILLPOWER FAILS",
     "It depletes with every decision you make — not just financial ones.",
     "Alex at desk: visible battery/reserve indicator icon on his chest showing 80% full. Multiple decision arrows pulling from it simultaneously — fork icon (lunch), envelope icon (email), shirt-hanger icon (outfit), coin icon (savings). Alex reacts with concerned expression as indicator drops.",
     "Medium shot", "Warm neutral", "Personal / Accumulative drain",
     "Alex looks down at depleting chest indicator, concerned expression as arrows pull from it",
     "Indicator drops as each decision arrow activates around Alex"),

    (26, "WHY WILLPOWER FAILS",
     "Every decision draws from the same reserve. Lunch. Email. What to wear. Whether to save.",
     "Large central tank draining through four icon-labeled taps simultaneously: fork icon (lunch), envelope icon (email), shirt/hanger icon (outfit), coin icon (savings). Tank level drops visibly. No text words on the taps — icons only.",
     "Wide shot", "Clean neutral", "Systemic drain",
     "No character",
     "All four icon-taps open simultaneously, tank level drops"),

    (27, "WHY WILLPOWER FAILS",
     "In 1998, Baumeister ran an experiment. Two groups. One room.",
     "Simple room bird's-eye diagram. Two tables with groups of stick figures. '1998' label in corner.",
     "Top-down diagram", "Clean academic", "Historical setup",
     "No character — diagram",
     "Room layout appears, groups populate their seats"),

    (28, "WHY WILLPOWER FAILS",
     "One plate had fresh chocolate chip cookies. The other: radishes.",
     "Two plates side by side on white: LEFT warm golden cookies with steam wisps. RIGHT plain pale radishes. No text labels.",
     "Close-up, centered", "Warm LEFT, cool neutral RIGHT", "Appetite contrast",
     "No character",
     "LEFT plate revealed first, RIGHT slides in"),

    (29, "WHY WILLPOWER FAILS",
     "Half the group could only eat the radishes — and resist the cookies.",
     "Radish group at table. Cookies visible behind rope barrier. Figures have strained expressions.",
     "Medium shot", "Same room tones", "Restraint / Strain",
     "Figures sitting rigidly, eyes darting toward cookies",
     "Camera pans from figures to cookies and back"),

    (30, "WHY WILLPOWER FAILS",
     "Then both groups received the same unsolvable puzzle.",
     "Both tables now have identical red puzzle boxes. Pieces scattered off the table, figures hunched in frustrated postures. Visual confusion without text labels.",
     "Wide shot", "Neutral clinical", "Setup for reveal",
     "Both groups lean toward puzzles, figures visibly tense",
     "Puzzle boxes appear simultaneously on both tables, pieces scattered"),

    (31, "WHY WILLPOWER FAILS",
     "Radish eaters gave up in eight minutes. Cookie eaters lasted nineteen.",
     "Two stopwatches: LEFT shows 8:00 in red — figure head-down on table beneath it (visual gave up). RIGHT shows 19:00 in green — figure still hunched working beneath it (visual still going). Numbers stay, no text labels.",
     "Wide shot, diagram", "LEFT: red / RIGHT: green", "Data clarity / Impact",
     "No character",
     "Left stopwatch runs to 8:00, figure slumps. Right continues to 19:00, figure still working."),

    (32, "WHY WILLPOWER FAILS",
     "Same puzzle. Same intelligence. Different reserve.",
     "Equation rows: PUZZLE (equal both sides). INTELLIGENCE (equal both sides). RESERVE (bars differ — full vs. empty, NOT EQUAL).",
     "Wide shot, equation diagram", "Clean white", "Precise contrast",
     "No character",
     "Rows appear top to bottom, not-equal sign on RESERVE emphasized"),

    (33, "WHY WILLPOWER FAILS",
     "By payday, Alex has been eating radishes for five days.",
     "Alex surrounded by five radish icons (Mon-Fri calendar layout). Expression: tired, depleted.",
     "Medium shot", "Dim, end of day", "Depleted",
     "Alex slightly slumped, radish icons orbit him like a weight",
     "Radish icons appear one by one around Alex"),

    (34, "WHY WILLPOWER FAILS",
     "His back hurts. His focus is gone. He's been patient all week.",
     "Alex visibly tired: hunched posture, dark circles. Five faded calendar pages behind him.",
     "Medium shot", "Late day warm dim", "Exhaustion",
     "Alex rolls neck, eyes heavy",
     "Slow push in on Alex's tired face"),

    (35, "WHY WILLPOWER FAILS",
     "The moment he needs the most discipline is the exact moment he has the least.",
     "Line graph: X-axis Mon–Fri. Y-axis Willpower %. Line slopes to near-zero by Friday. 'PAYDAY' marker at lowest point.",
     "Wide shot, graph", "Clean white, red accent at lowest point", "Ironic revelation",
     "No character",
     "Line draws left to right, hits bottom at PAYDAY marker"),

    (36, "WHY WILLPOWER FAILS",
     "A budget is a willpower machine.",
     "Budget spreadsheet shown with mechanical gears visible behind it. Fuel gauge depleting visually as gears turn. No text label on the mechanism — visual only.",
     "Medium shot", "Mechanical industrial tones", "Reframing",
     "No character",
     "Gears begin turning, fuel gauge drops as they turn"),

    (37, "WHY WILLPOWER FAILS",
     "It asks Alex to make the right call at the right moment, every payday, for thirty years.",
     "Long horizontal timeline: 30 years of payday markers. Each marker has a tiny sword-and-shield icon (representing the required 'right call'). No text flags.",
     "Wide shot, timeline", "Clean horizontal", "Daunting scale",
     "No character",
     "Timeline extends right — camera pans to follow it, sword-shield icons populate each payday"),

    (38, "WHY WILLPOWER FAILS",
     "The Brain Villain doesn't get tired.",
     "Villain in armchair, fresh coffee, newspaper. Alert, comfortable. Beside him: exhausted Alex slumped.",
     "Wide shot, contrast", "Bright for villain, dim for Alex", "Unfair advantage",
     "Villain reads newspaper calmly. Alex slumps further.",
     "Slow reveal from villain (bright) to Alex (dim)"),

    (39, "WHY WILLPOWER FAILS",
     "Alex does.",
     "Alex completely slumped at desk. Eyes half-closed. Coffee cold.",
     "Close-up", "Dim, blue fatigue light", "Exhaustion — punctuation beat",
     "Alex barely holds head up",
     "Static — maximum stillness"),

    # ── CTA ────────────────────────────────────────────────────────────────────
    (40, "CTA",
     "If your brain is running these programs right now — subscribe.",
     "Alex pointing directly at camera with calm confidence. Green subscribe button glows beside him.",
     "Medium shot, direct to camera", "Bright, welcoming", "Direct / Warm",
     "Alex points at camera, slight knowing smile",
     "Subscribe button pulses once"),

    (41, "CTA",
     "Every week: one bias. How it works. Who exploits it. And what you can actually do about it.",
     "Weekly calendar grid with small repeating icons (alternating brain icon and coin icon) each week, one week highlighted in green. No text labels.",
     "Wide shot, calendar graphic", "Clean", "Promise / Regularity",
     "No character",
     "Calendar grid fills with alternating icons, one week pulses green"),

    # ── continuation (no section header) ──────────────────────────────────────
    (42, "",
     "Over thirty years, the math does not favor Alex.",
     "Bar race chart over 30-year timeline: VILLAIN stamina bar stays high/flat. ALEX bar declines each year.",
     "Wide shot, bar chart", "Clean, red villain / blue Alex", "Sobering calculation",
     "No character",
     "Both bars animate year by year — villain flat, Alex declining"),

    (43, "",
     "But here's what Baumeister also found — the part that changes how you actually set up the system.",
     "Baumeister nameplate again. Large question mark appearing to the right of it, off-frame arrow pointing beyond. Visual curiosity gap without text.",
     "Close-up, flat graphic", "Clean white, slight warm tint", "Pivot — anticipation",
     "No character",
     "Question mark appears beside nameplate with subtle emphasis, then holds"),

    # ── THE DECISION ───────────────────────────────────────────────────────────
    (44, "THE DECISION",
     "There is only one way to beat a system that runs automatically.",
     "The large red gear system from beat 4. Single spotlight illuminating it. No Alex yet.",
     "Wide shot", "Single spotlight, dramatic", "Confrontation",
     "No character — spotlight on gear system",
     "Spotlight sweeps to settle on gear system"),

    (45, "THE DECISION",
     "Build a counter-system that also runs automatically.",
     "A second green gear system appears beside the red one. They interlock. Green matches red in size and momentum.",
     "Wide shot", "Dramatic — red and green contrast", "Resolution / Power",
     "No character",
     "Green gears emerge and interlock with red system"),

    (46, "THE DECISION",
     "Alex set up a standing order.",
     "Alex at computer, single mouse click. Clean green 'STANDING ORDER' arrow appears on screen.",
     "Medium shot", "Computer screen glow", "Decisive simplicity",
     "Alex clicks once — deliberately. One finger, one click.",
     "Mouse click registers; standing order graphic appears"),

    (47, "THE DECISION",
     "Four hundred euros. Every payday. One minute before the salary notification arrives.",
     "Timeline: 'PAYDAY - 1 MIN' → green standing order arrow fires. 'PAYDAY' → blue salary notification arrives. Green clearly precedes blue.",
     "Wide shot, timeline", "Clean, precise", "Mechanical advantage",
     "No character",
     "Timeline plays left to right — green fires first, then blue"),

    (48, "THE DECISION",
     "Before the Reward Trap fires its first question: what do I deserve?",
     "EXTREME CLOSE-UP on villain's face — mouth slowly opening for the question — but FREEZE MID-MOTION. Money space already empty. Expression: starting question but stopped cold.",
     "Extreme close-up", "Interior spotlight dims suddenly", "Too late — frozen",
     "Villain's mouth opens halfway, freezes in place",
     "Villain begins question motion — hard freeze mid-motion"),

    (49, "THE DECISION",
     "Before Mental Accounting creates a label: this is mine, this is safe, this is earned.",
     "BIRD'S-EYE VIEW (top-down): label-maker printing completely blank white labels into empty space. No coin visible. No text on the labels — blankness IS the visual.",
     "Top-down overhead", "Office-style clean, overhead angle", "Futility of mechanism",
     "No character — top-down view of printer ejecting blank labels",
     "Printer cycles from above, blank labels curl out into empty space"),

    (50, "THE DECISION",
     "Before Present Bias whispers: Future Alex will take care of it.",
     "PROFILE SHOT of villain leaning toward empty air, whispering. The target has vanished. Speech bubble forms — contains only an empty silhouette outline. Nothing to whisper to.",
     "Side profile", "Whisper scene — intimate dark, profile angle", "Empty promise revealed",
     "Villain leans toward nothing, speech bubble shows void silhouette",
     "Villain whisper animation profile — speech bubble forms with empty outline"),

    (51, "THE DECISION",
     "The Reward Trap fires the moment the salary hits. The standing order fires one minute earlier.",
     "Race graphic: two countdown timers. STANDING ORDER fires at T-1:00 (green). REWARD TRAP fires at T+0:00 (red). Clear winner.",
     "Wide shot, race graphic", "High contrast — green vs. red", "Speed advantage",
     "No character",
     "Both timers count down; green fires at -1:00, red at 0:00"),

    (52, "THE DECISION",
     "Mental Accounting assigns emotional labels to every euro Alex sees.",
     "Villain with label printer, stamping arriving euros: 'EARNED' / 'SAFE' / 'MINE' in sequence.",
     "Medium shot", "Warm office tones", "Mechanical enthusiasm",
     "Villain stamps labels rapidly, enjoying the process",
     "Label stamps hit coins in rapid sequence"),

    (53, "THE DECISION",
     "The standing order moves four hundred euros into a category the Brain Villain is never shown.",
     "Villain's filing cabinet: many visible labeled folders. One folder is INVISIBLE — villain's hand passes right through where it should be.",
     "Medium shot", "Slightly mysterious", "Invisible category",
     "Villain searches cabinet, hand passes through invisible folder",
     "Villain's hand sweeps through invisible folder's location"),

    (54, "THE DECISION",
     "Present Bias insists that Future Alex will be more responsible than Present Alex.",
     "Two identical Alexes side by side. Present Bias villain points at Future Alex: 'He'll handle it' speech bubble.",
     "Wide shot", "Split left/right same lighting", "False promise",
     "Villain points confidently at Future Alex. Both Alexes look identical.",
     "Static — emphasis on villain's confident pointing"),

    (55, "THE DECISION",
     "Past Alex already was — nine days before payday, when he was rested, calm, and the villain was quiet.",
     "Calendar: 9 days before payday. Alex at desk: well-rested, upright, clear eyes. Through skull: villain small, sleepy, quiet.",
     "Medium shot", "Clear daytime light — calm", "Peace / Competence",
     "Alex alert and calm. Villain barely visible — eyes half-closed, dormant.",
     "Slow reveal — camera pans from villain (small/quiet) to Alex (capable)"),

    (56, "THE DECISION",
     "Alex didn't learn to say no to the Brain Villain.",
     "Alex NOT in confrontation with villain. No boxing ring. No argument. Alex neutral, alone, standing.",
     "Medium shot", "Neutral clean", "Non-confrontation",
     "Alex arms at sides — not fighting, not engaging. Villain absent.",
     "Static — conspicuously no conflict"),

    (57, "THE DECISION",
     "He cancelled the meeting.",
     "Calendar entry: 'MEETING: Alex vs. Brain Villain — PAYDAY 9AM'. Large red CANCELLED stamp over it.",
     "Close-up on calendar", "Clean office", "Resolution — clean break",
     "No character — calendar close-up",
     "CANCELLED stamp slams onto calendar entry"),

    (58, "THE DECISION",
     "The Brain Villain cannot argue with a decision it was never invited to attend.",
     "Villain outside a closed meeting room door. Sign: 'STANDING ORDER MEETING — PRIVATE'. Villain reads sign, tries handle.",
     "Medium shot", "Office corridor — fluorescent", "Exclusion",
     "Villain reads door sign, tries handle — door stays locked",
     "Villain tries door handle — door stays closed"),

    (59, "THE DECISION",
     "The money is simply not there.",
     "Alex's mental wallet: he opens it, the €400 space is clearly empty. Simple, clean.",
     "Close-up on wallet", "Clean neutral", "Simple fact",
     "Alex holds open wallet, looks at empty space without distress",
     "Wallet opens — empty space revealed"),

    (60, "THE DECISION",
     "Not hidden. Not locked. Not off-limits.",
     "Three icons in a row, each with bold red X: box with lock (HIDDEN), padlock (LOCKED), warning sign (OFF-LIMITS).",
     "Wide shot, icon row", "Clean white", "Clarification",
     "No character",
     "Each X strikes through in rapid left-to-right sequence"),

    (61, "THE DECISION",
     "Gone before the calculation begins.",
     "Villain's abacus/calculator: completely empty. No numbers, no inputs. Villain stares at it.",
     "Medium shot", "Clean white", "Checkmate",
     "Villain looks at empty calculator, expression shifts from expectation to confusion",
     "Villain's abacus beads absent — empty frame"),

    # ── THE SCIENCE ────────────────────────────────────────────────────────────
    (62, "THE SCIENCE",
     "Richard Thaler and Shlomo Benartzi — University of Chicago and UCLA, 2004 —",
     "Two academic nameplates: 'RICHARD THALER / U. of Chicago' and 'SHLOMO BENARTZI / UCLA'. '2004' centered below both.",
     "Wide shot, flat graphic", "Clean academic white", "Authoritative",
     "No character",
     "Left nameplate appears, then right, then year"),

    (63, "THE SCIENCE",
     "designed a program called Save More Tomorrow.",
     "Program title card: 'SAVE MORE TOMORROW' — large bold typography. Simple green arrow below.",
     "Close-up, typographic", "Clean white", "Introducing the solution",
     "No character",
     "Title fades in with emphasis"),

    (64, "THE SCIENCE",
     "They didn't ask workers to save more now.",
     "Workers at desks. Thaler/Benartzi figures NOT approaching them. 'NOW' crossed out in large red X.",
     "Wide shot", "Office tones", "Contrast — the approach",
     "Worker figures continue work; researchers stand back",
     "Red X strikes through 'NOW' label"),

    (65, "THE SCIENCE",
     "They asked one question, one time: when your next raise arrives, can we automatically redirect a fixed percentage?",
     "Single large question mark dominating frame. Below it: one finger raised (index finger pointing up). No text labels.",
     "Close-up, graphic", "Clean white, slight warm", "Simplicity",
     "No character",
     "Question mark appears, then single finger rises below it"),

    (66, "THE SCIENCE",
     "Workers said yes — once.",
     "Single large green checkmark. 'ONCE.' below it. Maximum minimalism.",
     "Close-up, graphic", "Clean bright white", "Decisive simplicity",
     "No character",
     "Checkmark draws itself — single motion"),

    (67, "THE SCIENCE",
     "The system then executed automatically, every raise cycle, with no further decision required.",
     "Automated green gear system running completely unattended — no hands, no figure at controls. Calendar pages flipping in background automatically. Hands-free visual tells the story.",
     "Wide shot", "Green mechanical", "Automated inevitability",
     "No character — gears run themselves, calendar flips alone",
     "Gears turn, calendar pages flip automatically — no human intervention visible"),

    (68, "THE SCIENCE",
     "Workers who started at a savings rate of three and a half percent",
     "Bar chart at starting position: small green bar labeled '3.5%'. Rest of chart empty — anticipation of growth.",
     "Wide shot, chart", "Clean white", "Starting point",
     "No character",
     "Small bar appears at 3.5% — holds"),

    (69, "THE SCIENCE",
     "reached thirteen point six percent within five years.",
     "Same chart: bar dramatically grows to '13.6% — 5 YEARS'. Height difference striking.",
     "Wide shot, chart", "Green — growth tones", "Impact",
     "No character",
     "Bar grows upward to 13.6% — slow dramatic rise"),

    (70, "THE SCIENCE",
     "No budgets. No discipline. No willpower.",
     "Three items with bold red X: budget spreadsheet, flexing bicep icon, depleted fuel gauge.",
     "Wide shot, icon row", "Clean white", "Liberation",
     "No character",
     "Each X appears left to right"),

    (71, "THE SCIENCE",
     "One structural decision replaced sixty separate monthly battles with the Brain Villain.",
     "ONE large green gear (labeled '1 DECISION') beside 60 tiny red conflict icons scattered chaotically.",
     "Wide shot", "Green vs. red contrast", "Scale revelation",
     "No character",
     "60 red icons appear chaotically, then ONE green gear dominates"),

    (72, "THE SCIENCE",
     "The only variable that changed across those five years was structure.",
     "Five-year timeline, four tracked lines: INCOME (flat), KNOWLEDGE (flat), CHARACTER (flat). STRUCTURE (ascending green). Same graph as prior beats with all lines visible.",
     "Wide shot, multi-line graph", "Clean white, green highlight", "Isolation of variable",
     "No character",
     "All lines draw simultaneously — only STRUCTURE rises"),

    (73, "THE SCIENCE",
     "Not income. Not financial knowledge. Not character.",
     "Same graph from beat 72: the three flat lines each get a bold red X mark through them while the green STRUCTURE line continues ascending. Visual elimination without text labels.",
     "Wide shot, multi-line graph", "Clean white, red X marks", "Precision elimination",
     "No character",
     "Red X marks strike through each flat line in sequence — STRUCTURE line continues"),

    (74, "THE SCIENCE",
     "Structure.",
     "Single word: 'STRUCTURE.' — large, bold, centered. Pure white background. Nothing else.",
     "Extreme close-up, typographic", "Pure white background", "Maximum weight — silence",
     "No character",
     "Word appears and holds — static, nothing else moves"),

    # ── THE BRAIN VILLAIN'S LAST TRICK ────────────────────────────────────────
    (75, "THE BRAIN VILLAIN'S LAST TRICK",
     "The Brain Villain has one response to automation.",
     "Villain alone in frame. One finger raised, thinking. Smirk. Clean white background.",
     "Medium shot", "Clean neutral", "Calculating",
     "Villain raises single finger, slight satisfied smirk",
     "Villain appears mid-thought"),

    (76, "THE BRAIN VILLAIN'S LAST TRICK",
     "You're feeling it right now.",
     "Alex looking at camera — no villain visible. Direct, calm, gentle. Eyebrow slightly raised.",
     "Medium close-up, direct to camera", "Warm neutral", "Direct / Knowing",
     "Alex makes direct eye contact with camera, slight knowing expression",
     "Static — holds eye contact with viewer"),

    (77, "THE BRAIN VILLAIN'S LAST TRICK",
     "Not anxiety. Something quieter.",
     "Emotional spectrum: 'ANXIETY' in large red on left with X. Right side: smaller, unnamed feeling — vague shape, no label.",
     "Wide shot, diagram", "LEFT: red, RIGHT: quiet grey", "Subtle distinction",
     "No character",
     "ANXIETY appears and is X'd; quiet feeling shape appears vaguely"),

    (78, "THE BRAIN VILLAIN'S LAST TRICK",
     "Something that sounds like responsibility: what if I need that money?",
     "Villain in formal business suit, expression of mock-concern. Speech bubble: 'What if I need that money?'",
     "Medium shot", "Professional office lighting", "Disguise — responsible costume",
     "Villain in suit adjusts tie, puts on concerned expression",
     "Villain smooths suit jacket, composes 'responsible' expression"),

    (79, "THE BRAIN VILLAIN'S LAST TRICK",
     "That thought is not intuition. Not wisdom. Not financial prudence.",
     "Three villain costumes in a row, each with red X through it: judge's robe (intuition symbol), owl shape (wisdom symbol), banker briefcase (prudence symbol). Visual elimination without text labels.",
     "Wide shot, graphic", "Clean white", "Precision elimination",
     "No character",
     "Each costume X'd out in sequence — rapid visual elimination"),

    (80, "THE BRAIN VILLAIN'S LAST TRICK",
     "It is Present Bias wearing the costume of caution.",
     "Villain in bright yellow CAUTION safety vest and hard hat. Villain pulls vest open slightly: 'PRESENT BIAS' label visible underneath.",
     "Medium shot", "Yellow safety tones", "Unmasked disguise",
     "Villain looks down at vest, pulls it open revealing PRESENT BIAS",
     "Vest pulls open — PRESENT BIAS label revealed"),

    (81, "THE BRAIN VILLAIN'S LAST TRICK",
     "The Villain doesn't need to spend the money.",
     "Villain shaking head 'no' at a shopping/spending icon. Hands up: not that.",
     "Medium shot", "Neutral clean", "Clarification",
     "Villain waves off spending icon — that's not the goal",
     "Villain dismissively waves at spending icon"),

    (82, "THE BRAIN VILLAIN'S LAST TRICK",
     "It just needs to know it could.",
     "Villain holding a large key — not using it, not walking anywhere, just holding it. Expression: content, satisfied.",
     "Close-up", "Neutral, slightly warm", "Option as power",
     "Villain holds key, looks at it with satisfaction — no intent to use it",
     "Static — villain looks at key contentedly"),

    (83, "THE BRAIN VILLAIN'S LAST TRICK",
     "That option — the ability to reach the money — is exactly what the standing order removes.",
     "The key in villain's hand DISSOLVES. Villain's hand: empty. Expression shifts from content to unsettled.",
     "Close-up", "Slight chill, cooler tones", "Loss of option",
     "Villain stares at empty hand, expression shifts",
     "Key dissolves from villain's hand — hand closes on nothing"),

    (84, "THE BRAIN VILLAIN'S LAST TRICK",
     "And your brain just demonstrated why.",
     "Alex looking at camera — calm, knowing. Direct eye contact. Expression: 'you felt that, didn't you?'",
     "Medium close-up, direct to camera", "Warm neutral", "Direct / Complicit",
     "Alex direct eye contact — subtle knowing nod toward camera",
     "Static — holds with knowing expression"),

    (85, "THE BRAIN VILLAIN'S LAST TRICK",
     "The discomfort you felt in the last thirty seconds —",
     "Small ripple/wave emanating from Alex's chest area. Subtle, internal. Almost imperceptible.",
     "Medium shot", "Neutral, intimate", "Interior sensation",
     "Alex's hand moves briefly to chest — acknowledging something felt",
     "Ripple effect from chest, small and quiet"),

    (86, "THE BRAIN VILLAIN'S LAST TRICK",
     "that was the trap identifying itself.",
     "The ripple from beat 85 briefly forms the silhouette shape of the villain — then dissipates.",
     "Medium shot", "Same as 85", "Revelation",
     "Alex watches the ripple transform — mild recognition on face",
     "Ripple transforms into villain shape, then dissolves"),

    (87, "THE BRAIN VILLAIN'S LAST TRICK",
     "The standing order doesn't just move money. It removes the Brain Villain's last lever.",
     "Villain's lever mechanism (large physical lever labeled 'LAST LEVER'): lever breaks off at base, falls. Villain stares at empty hands.",
     "Wide shot", "Slightly dramatic", "Mechanical defeat",
     "Villain watches lever break, slowly opens empty hands",
     "Lever breaks and falls — villain watches"),

    # ── IDENTITY CLOSE + GUIDE ────────────────────────────────────────────────
    (88, "IDENTITY CLOSE + GUIDE",
     "Alex doesn't need more discipline.",
     "Alex standing calm. No gauge, no metrics. Just Alex, neutral, at peace.",
     "Medium shot", "Clean neutral, warm", "Simplicity / Relief",
     "Alex stands comfortably, no strain",
     "Static — peaceful, unburdened"),

    (89, "IDENTITY CLOSE + GUIDE",
     "He needs fewer decisions — not better ones.",
     "Decision stack: tall pile of papers. The pile SHRINKS dramatically — not refined, just fewer.",
     "Wide shot", "Clean", "Reduction",
     "No character",
     "Decision pile shrinks — papers disappear from top"),

    (90, "IDENTITY CLOSE + GUIDE",
     "Every budgeting system ever created asks Alex to win the same battle every month.",
     "Long calendar: 12 months per year, multiple years. Each payday: tiny red battle icon. Repeated endlessly.",
     "Wide shot, calendar timeline", "Tiring, repetitive visual", "Systemic demand",
     "No character",
     "Calendar extends with identical battle icons repeating"),

    (91, "IDENTITY CLOSE + GUIDE",
     "The standing order asks him to win it once.",
     "Single battle icon. Single green victory checkmark over it. Then: gear system running — no more battles.",
     "Wide shot", "Green, resolved", "One-time victory",
     "No character",
     "Single battle → single victory → automated gears take over"),

    (92, "IDENTITY CLOSE + GUIDE",
     "The programs are not broken.",
     "Three brain programs running as gears — perfectly smooth, no errors. Just mismatched to environment.",
     "Wide shot", "Neutral, analytical", "Reframe — not broken",
     "No character — gears running smoothly",
     "Gears turn steadily — perfectly functional"),

    (93, "IDENTITY CLOSE + GUIDE",
     "They are perfectly designed for an environment where saving made no survival sense.",
     "Ancestral wilderness background. Same three gear programs overlaid — they FIT the ancient environment.",
     "Wide shot, contrast scene", "Warm ancient tones", "Historical fit",
     "No character — gear programs overlaid on ancient setting",
     "Scene transitions to ancestral background — gears still running"),

    (94, "IDENTITY CLOSE + GUIDE",
     "You didn't store food in a world where tomorrow was never guaranteed.",
     "Ancestral Alex (same character, simple clothes) holding berries — nowhere safe to store them. Hostile wilderness.",
     "Medium shot", "Ancient warm", "Evolutionary logic",
     "Ancestral Alex holds food, looks at wilderness — storing impossible",
     "Ancestral Alex looks around for storage — finds none"),

    (95, "IDENTITY CLOSE + GUIDE",
     "The Brain Villain was built for that world. Not this one.",
     "Split panel: LEFT villain thriving in ancient wilderness (confident, in element). RIGHT villain in modern apartment, confused, mismatched.",
     "Wide split panel", "LEFT: ancient warm / RIGHT: modern cool", "Displacement",
     "LEFT: villain flourishing / RIGHT: villain lost",
     "Split reveals simultaneously — villain in each context"),

    (96, "IDENTITY CLOSE + GUIDE",
     "The standing order is the first system designed for the world he actually lives in.",
     "Modern world backdrop: bank app on phone, apartment window, calendar with paydays. Green standing order gear running behind Alex — supporting him, integrated perfectly into his modern environment.",
     "Wide shot", "Modern clean — warm green glow", "Resolution / Fit",
     "Alex stands in modern setting — green gear system behind him, supporting him",
     "Modern environment elements settle around Alex, green gear activates behind him"),

    # ── NEXT VIDEO TEASE ──────────────────────────────────────────────────────
    (97, "NEXT VIDEO TEASE",
     "Next video: Alex gets a tax refund.",
     "Envelope arriving at Alex's door. Label: 'TAX REFUND'. Alex expression: surprised delight.",
     "Medium shot", "Bright daylight — unexpected good news", "Surprise",
     "Alex opens mailbox, finds tax refund envelope — eyes widen",
     "Envelope slides out, Alex reacts"),

    (98, "NEXT VIDEO TEASE",
     "Eight hundred euros he wasn't expecting.",
     "'€800' appearing from envelope in large numbers. 'UNEXPECTED' implied visually by his expression.",
     "Close-up", "Bright, generous light", "Pleasant surprise",
     "No character — €800 dominates frame",
     "€800 amount appears from envelope"),

    (99, "NEXT VIDEO TEASE",
     "His brain treats it completely differently from every euro he ever earned.",
     "Split brain diagram: LEFT 'EARNED EUROS' — one processing track. RIGHT 'UNEXPECTED EUROS' — completely different track, different color.",
     "Wide split diagram", "Clean with distinct tracks", "Different processing",
     "No character — brain diagram",
     "Two tracks shown simultaneously — different pathways"),

    (100, "NEXT VIDEO TEASE",
     "Same trap. Different label.",
     "Two identical villain trap mechanisms — exact same design. LEFT labeled 'SALARY'. RIGHT labeled 'REFUND'.",
     "Wide shot", "Clean contrast", "Pattern recognition",
     "No character",
     "Two traps appear side by side — identical mechanism, different labels"),

    (101, "NEXT VIDEO TEASE",
     "The money disappears three times faster.",
     "Speedometer graphic: normal depletion rate vs. €800 refund depletion rate — refund depletes 3× faster.",
     "Wide shot, speedometer", "Dynamic red for fast depletion", "Warning",
     "No character",
     "Speedometer needle swings 3× faster for refund track"),

    (102, "NEXT VIDEO TEASE",
     "The reason is the one nobody expects.",
     "Villain holding large '?' sign. Direct eye contact with camera. Hard cut.",
     "Medium shot, direct to camera", "Dramatic — slight spotlight", "Curiosity gap",
     "Villain holds '?' sign, slight smile — knows the answer",
     "Static — villain holds question mark. Hard cut."),
]

assert len(BEATS) == 102, f"Expected 102 beats, got {len(BEATS)}"


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_production_pdf():
    styles = getSampleStyleSheet()

    H1    = ParagraphStyle('H1',    parent=styles['Title'],   fontSize=16, leading=20, alignment=TA_CENTER)
    SUB   = ParagraphStyle('SUB',   parent=styles['Normal'],  fontSize=10, leading=13,
                           alignment=TA_CENTER, textColor=colors.HexColor('#B02A2A'),
                           fontName='Helvetica-Bold')
    REC   = ParagraphStyle('REC',   parent=styles['Normal'],  fontSize=8,  leading=11,
                           alignment=TA_CENTER, textColor=colors.HexColor('#1A7A3C'))
    META  = ParagraphStyle('META',  parent=styles['Normal'],  fontSize=8,  leading=11,
                           alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
    STYLE_BOX = ParagraphStyle('STYLE_BOX', parent=styles['Normal'], fontSize=7.5, leading=10.5,
                               textColor=colors.HexColor('#555555'), spaceBefore=4, spaceAfter=8)
    SEC   = ParagraphStyle('SEC',   parent=styles['Normal'],  fontSize=10, leading=13,
                           textColor=colors.HexColor('#B02A2A'), fontName='Helvetica-Bold',
                           spaceBefore=14, spaceAfter=4)
    NARR  = ParagraphStyle('NARR',  parent=styles['Normal'],  fontSize=10.5, leading=15,
                           spaceBefore=5, spaceAfter=2)
    IMG   = ParagraphStyle('IMG',   parent=styles['Normal'],  fontSize=8.5, leading=12,
                           textColor=colors.HexColor('#334455'), spaceAfter=2)
    PROD  = ParagraphStyle('PROD',  parent=styles['Normal'],  fontSize=8, leading=11,
                           textColor=colors.HexColor('#666666'), spaceAfter=6)

    pdf_path = "/home/user/Claudeeee/V12_final_PRODUCTION.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=16*mm, rightMargin=16*mm,
                            topMargin=15*mm, bottomMargin=15*mm)

    flow = [
        Paragraph(esc(SUBTITLE), SUB),
        Spacer(1, 4),
        Paragraph(esc(TITLE), H1),
        Spacer(1, 4),
        Paragraph('TÍTULO ALTERNATIVO ORIGINAL: "The One Decision That Defeats All Three Brain Traps"', REC),
        Spacer(1, 4),
        Paragraph(f"PRODUCTION DOCUMENT · {len(BEATS)} beats · Visual-first image prompts", META),
        Spacer(1, 8),
        Paragraph(f"<b>STYLE PREAMBLE</b> — prepend to every Google Flow prompt:<br/>{esc(STYLE)}", STYLE_BOX),
    ]

    last_sec = None
    for beat in BEATS:
        num, sec, narration, img, cam, light, mood, char_action, motion = beat

        if sec != last_sec:
            if sec:  # only show header if section name is non-empty
                flow.append(Paragraph(f"— {esc(sec)} —", SEC))
            last_sec = sec

        full_prompt = f"{STYLE} {img}"
        block = [
            Paragraph(
                f'<font color="#B02A2A"><b>[{num}]</b></font>  '
                f'<b>{esc(narration)}</b>', NARR),
            Paragraph(
                f'<b>Image:</b> {esc(img)}', IMG),
            Paragraph(
                f'Cam: {esc(cam)}  ·  Light: {esc(light)}  ·  Mood: {esc(mood)}<br/>'
                f'Character: {esc(char_action)}<br/>'
                f'Motion: {esc(motion)}', PROD),
        ]
        flow.append(KeepTogether(block))

    flow.append(Spacer(1, 10))
    flow.append(Paragraph(f"END · {len(BEATS)} beats · V12 FINAL PRODUCTION", META))

    doc.build(flow)
    print(f"PRODUCTION PDF: {pdf_path} | {len(BEATS)} beats")


if __name__ == "__main__":
    build_production_pdf()
    print("\n✅ V12 FINAL — Production document generated")
    print(f"   {len(BEATS)} beats · Full image prompts + camera + lighting + mood + character + motion")
