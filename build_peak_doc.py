#!/usr/bin/env python3
"""Generate the full beat-by-beat production document for
'Someone Needs You to Buy at the Top. Here's Who.' (Video 7 — Availability Heuristic / Narrative Economics)."""

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

BEATS = [

# ── HOOK ──────────────────────────────────────────────────────────────────────

("At some point in the last five years, you heard about something that felt like the financial opportunity of a lifetime.",
 f"{STYLE} Medium shot, warm beige background. The main character sits on a sofa, phone in hand, scrolling. On the phone screen: a glowing news headline about a rising asset — partially visible. The brain inside the skull leans forward, eyes lighting up with recognition. Expression: the beginning of excitement.",
 "Medium shot", "Warm beige, soft ceiling spotlight", "Intimate recognition — the viewer's own experience starting",
 "Character on sofa with phone; news headline visible; brain leaning forward with interest",
 "Static. Phone screen glow illuminates character's face slightly. 2s."),

("Maybe it was a stock. A cryptocurrency. A sector. A company everyone was suddenly talking about.",
 f"{STYLE} Wide shot, white background. Four floating icons in a row inside a thought bubble: a stock ticker, a cryptocurrency coin, a sector chart, a company logo (generic). Each icon glows with a subtle golden light. Expression on character: recognition — one of these was theirs.",
 "Wide shot", "Flat, white", "Universal recognition — viewer maps their own experience",
 "Four investment type icons floating; each glowing; character recognizing",
 "Static. Icons appear one by one; each pulses once. 3s."),

("You felt it. The pull.",
 f"{STYLE} Close-up on the character's chest. A visual pull — a magnetic arrow pointing forward, toward the phone screen. The brain inside the skull has leaned so far forward it is nearly pressed against the inside of the glass. Bold diegetic label near the arrow: 'THE PULL.'",
 "Close-up on character", "Warm, slightly intensified", "The feeling named — visceral and personal",
 "Magnetic pull arrow toward phone; brain pressed against glass; THE PULL label",
 "Animated. Arrow pulses gently forward. Brain leans further. 2s."),

("Something between excitement and urgency. A voice that said: if you don't move now, you will miss it.",
 f"{STYLE} Medium shot. Above the character, two intertwined signals: a green excitement spark and a red urgency flash — both active simultaneously. A small speech bubble from the brain: 'MOVE NOW OR MISS IT.' Expression on character: caught between the two signals.",
 "Medium shot", "Warm, dual-signal lighting", "The FOMO mechanism introduced — excitement + urgency combined",
 "Green excitement and red urgency signals; brain speech bubble MOVE NOW; character caught between",
 "Animated. Two signals pulse alternately; speech bubble appears. 3s."),

("Some of you moved. Some of you watched it rise and wished you had.",
 f"{STYLE} Wide split. Left: a character figure that moved — small green position in a rising chart, expression satisfied. Right: a character figure that watched — same chart rising, no position held, expression of regret. Bold label between them: 'BOTH FELT THE SAME PULL.'",
 "Wide split", "Flat, white", "Universal reach — both groups in the same trap",
 "Mover with position vs watcher with regret; same chart rising; both felt pull",
 "Static. Both figures visible; chart identical for both. 2s."),

("Either way, you felt it.",
 f"{STYLE} Medium shot, direct address. The character faces camera. The brain inside the skull also faces camera — a rare moment of alignment. Expression: honest acknowledgment. Bold label: 'YOU FELT IT.' No judgment. Just recognition.",
 "Medium shot, direct address", "Flat, white", "The acknowledgment — honest, not accusatory",
 "Character and brain both facing camera; YOU FELT IT label; honest expression",
 "Static. Both hold direct address. 2s."),

("That feeling has a name. It has a mechanism. And it has a beneficiary.",
 f"{STYLE} Wide shot. Three floating cards appear beside the character: 'A NAME,' 'A MECHANISM,' 'A BENEFICIARY.' Each card face down — about to be revealed. Expression on character: leaning forward. The brain villain in the corner watches with a knowing expression.",
 "Wide shot", "Flat, white", "The thesis — three things will be revealed",
 "Three face-down cards; character leaning forward; brain villain watching",
 "Animated. Cards appear one by one face down; brain villain visible. 3s."),

("The beneficiary was never you.",
 f"{STYLE} Wide shot. The BENEFICIARY card flips over — it shows a silhouetted suited figure, not the main character. The character reads it. Expression: the hook lands. Bold red label on the card: 'NOT YOU.' The brain villain in the corner nods slowly.",
 "Wide shot", "Flat, white, red label on card", "The hook lands — betrayal established",
 "Beneficiary card flips to show suited figure not character; NOT YOU label; brain villain nods",
 "Animated. Card flips; red label appears; brain villain nods once. 3s."),

# ── THE SHOESHINE BOY ─────────────────────────────────────────────────────────

("October 1929. Boston.",
 f"{STYLE} Wide shot. A 1929 Boston street scene — flat cartoon style, warm sepia-adjacent tones. Period-appropriate storefronts, suited pedestrians, cobblestone street. A bold diegetic label on a storefront sign: 'OCTOBER 1929 · BOSTON.' The scene establishes a different era without photorealism.",
 "Wide shot, period street scene", "Warm sepia-adjacent tones, flat", "Historical anchor — the story begins",
 "1929 Boston street; period storefronts; suited pedestrians; date label on sign",
 "Static. Period scene holds. Date label visible. 2s."),

("Joseph Kennedy — businessman, investor, one of the wealthiest men in America — is having his shoes shined.",
 f"{STYLE} Medium shot. A well-dressed cartoon figure sits in a shoeshine chair — large, confident posture, three-piece suit, small round glasses. A bold label floats beside him: 'JOSEPH KENNEDY.' Beside it: small icons — dollar signs, briefcase, a small 'WEALTHIEST IN AMERICA' badge. A second, younger figure kneels at his feet with a shoeshine kit.",
 "Medium shot", "Warm, period tones", "Kennedy introduced — wealth and status established",
 "Kennedy in shoeshine chair with wealth indicators; shoeshine boy kneeling; labels",
 "Static. Kennedy's posture communicates wealth and authority. 2s."),

("The shoeshine boy, while working, begins giving him stock tips.",
 f"{STYLE} Medium shot. The shoeshine boy looks up while polishing, a bright excited expression on his face. A speech bubble appears above him with small stock ticker symbols and an upward arrow: specific names barely readable. Kennedy's expression shifts — he is listening carefully, but his internal reaction is not yet visible.",
 "Medium shot", "Warm, period tones", "The tip moment — the inciting incident",
 "Shoeshine boy giving tips with speech bubble; Kennedy listening carefully; tickers in bubble",
 "Static. Speech bubble with tickers visible; Kennedy expression attentive. 3s."),

("Which stocks to buy. Which sectors are moving. Which names everyone is talking about.",
 f"{STYLE} Close-up on the speech bubble. Three items now clearly labeled: WHICH TO BUY (stock list), WHICH SECTORS (moving arrows), WHICH NAMES (bold type: 'EVERYONE IS TALKING ABOUT'). The last phrase is highlighted. The shoeshine boy is enthusiastic — he knows things.",
 "Close-up on speech bubble", "Warm", "The content of the tip — the key phrase is 'everyone is talking about'",
 "Speech bubble with three tip categories; EVERYONE IS TALKING ABOUT highlighted",
 "Static. Speech bubble content visible; last phrase highlighted. 2s."),

("Kennedy listened.",
 f"{STYLE} Close-up on Kennedy's face. His expression is carefully neutral. Behind his eyes — visible through a small thought window — the brain is calculating, not excited. While the shoeshine boy speaks, Kennedy's brain is running a very different analysis than the boy expects.",
 "Close-up on Kennedy", "Warm", "The calculation begins — Kennedy processes differently",
 "Kennedy's neutral expression; thought window showing calculating brain; different analysis",
 "Static. Kennedy's neutral face holds. Calculating brain visible. 2s."),

("He said nothing.",
 f"{STYLE} Medium shot. Kennedy's speech bubble is empty — deliberately blank. The shoeshine boy is still talking. Kennedy offers no reaction. Bold label beside the empty speech bubble: 'NOTHING.' The silence is loaded.",
 "Medium shot", "Warm", "The silence — loaded with meaning",
 "Kennedy with empty speech bubble; shoeshine boy still talking; NOTHING label",
 "Static. Empty speech bubble holds. Contrast with boy's full bubble. 2s."),

("He walked back to his office and sold everything he owned in the stock market.",
 f"{STYLE} Wide shot. Kennedy walks away from the shoeshine stand toward a large office building. As he walks, a series of SELL orders flies out of his briefcase — small papers, each labeled SOLD. By the time he reaches the office door, the papers trail behind him like a paper stream. Bold label: 'SOLD EVERYTHING.'",
 "Wide shot", "Flat, warm", "The decision — immediate and complete",
 "Kennedy walking to office; SOLD order papers trailing behind him; SOLD EVERYTHING label",
 "Animated. Papers fly out of briefcase as he walks; trail behind. 3s."),

("Every position. Every holding. Complete liquidation.",
 f"{STYLE} Wide diagram. A portfolio dashboard — all positions visible, one by one going to zero and turning gray. COMPLETE LIQUIDATION label appears across the portfolio when the last position closes. The dashboard is empty. Kennedy stands beside it, calm.",
 "Wide diagram", "Flat, white", "The scale — total exit, nothing held",
 "Portfolio positions closing to zero one by one; COMPLETE LIQUIDATION label; Kennedy calm",
 "Animated. Positions close in sequence; each turns gray; final label appears. 3s."),

("Three weeks later, the market collapsed.",
 f"{STYLE} Wide shot. A large stock chart — warm, period style. The line rises to a peak, then in three calendar weeks it drops sharply. A bold label at the drop: 'THREE WEEKS LATER.' The chart crash is dramatic and visual. Small figures of investors falling with it.",
 "Wide shot, chart", "Flat, warm to dark", "The collapse — the stakes of Kennedy's decision",
 "Stock chart rising then crashing; THREE WEEKS LATER label; investor figures falling",
 "Animated. Chart line rises then drops sharply. Investor figures fall. 3s."),

("Black Thursday. Black Monday. The beginning of the Great Depression.",
 f"{STYLE} Wide shot. Three bold labels in sequence: BLACK THURSDAY, BLACK MONDAY, THE GREAT DEPRESSION BEGINS. Each appears against a darkening background. Newspaper front pages floating — headlines of the crash. Period storefronts now have CLOSED signs. The warm sepia tones have shifted to gray.",
 "Wide shot", "Gradually darkening, gray tones", "The historical weight — the crash was civilizational",
 "Three bold date labels; newspaper headlines; CLOSED storefronts; world going gray",
 "Animated. Labels appear in sequence; background darkens progressively. 3s."),

("While thousands of investors — many of them far more sophisticated than a shoeshine boy's clients — lost everything, Kennedy's fortune was intact.",
 f"{STYLE} Wide split. Left: a crowd of suited investor figures — portfolios empty, expressions devastated, buildings behind them closing. Right: Kennedy stands alone, fortune intact, same calm expression. A bold comparison label: 'SOPHISTICATED INVESTORS: LOST EVERYTHING. KENNEDY: INTACT.' The irony is the visual.",
 "Wide split", "Left gray, right warm", "The contrast — sophistication did not protect them",
 "Sophisticated investors ruined vs Kennedy intact; comparison label; irony visible",
 "Static. Split holds. Contrast clear. 3s."),

("He was asked, later, what made him sell.",
 f"{STYLE} Medium shot. Kennedy sits across a table from a journalist figure — notepad, press badge. The journalist's speech bubble: 'WHAT MADE YOU SELL?' Kennedy's expression: almost amused. The answer is simpler than anyone expected.",
 "Medium shot", "Warm", "The question — the journalist stands in for the viewer",
 "Kennedy across table from journalist; question in speech bubble; Kennedy slightly amused",
 "Static. Scene holds; journalist leaning forward. 2s."),

("His answer was simple.",
 f"{STYLE} Close-up on Kennedy. His expression settles — not smug, just clear. A single speech bubble begins to form above him, not yet complete. The simplicity is the point. The viewer leans forward.",
 "Close-up on Kennedy", "Warm, soft spotlight", "The reveal incoming — simple answer to the biggest question",
 "Kennedy's clear expression; speech bubble forming; simplicity building",
 "Static. Speech bubble forming slowly. 2s."),

("When the shoeshine boy knows which stocks to buy, it is too late to be in the market.",
 f"{STYLE} Wide shot. Kennedy's speech bubble now full and prominent: 'WHEN THE SHOESHINE BOY KNOWS WHICH STOCKS TO BUY, IT IS TOO LATE TO BE IN THE MARKET.' The shoeshine boy stands beside Kennedy — now a symbol, not just a character. Bold diegetic text. The viewer reads it twice.",
 "Wide shot", "Warm, speech bubble prominent", "The Kennedy rule — the central insight of the video",
 "Kennedy's full speech bubble with the rule; shoeshine boy as symbol beside him",
 "Static. Full speech bubble holds. Viewer reads it. 4s."),

("Kennedy had no name for what he understood.",
 f"{STYLE} Medium shot on Kennedy. Above his head: a thought bubble — but instead of a label or formula, it contains a blank page. He understood the pattern without having the vocabulary for it. Expression: clarity without theory. Bold label: 'NO NAME FOR IT YET.'",
 "Medium shot", "Warm", "The historical gap — insight before science",
 "Kennedy with blank thought bubble; understood without the name; NO NAME YET label",
 "Static. Blank thought bubble holds. 2s."),

("The name came decades later.",
 f"{STYLE} Wide shot. A timeline appears: 1929 (Kennedy's shoeshine moment) on the left, connected by a long dotted line to the right side — a university setting, researchers, a textbook cover barely visible. Bold label at the right end: 'DECADES LATER.' The insight waited for the science to catch up.",
 "Wide shot, timeline", "Flat, white", "The bridge — from 1929 to the science",
 "Timeline from 1929 to decades later; Kennedy on left; research on right",
 "Static. Timeline holds; dotted line connects both points. 2s."),

# ── WHAT KENNEDY UNDERSTOOD ───────────────────────────────────────────────────

("Here is what Kennedy saw that morning.",
 f"{STYLE} Medium shot. The character faces camera — in the present, not 1929. The brain inside the skull shifts to an analytical, focused expression. Clean white background. The shoeshine scene is now in a small thought bubble beside the character — the story being decoded.",
 "Medium shot, direct address", "Flat, white", "The analysis begins — Kennedy's insight decoded",
 "Character facing camera; shoeshine scene in small thought bubble; brain analytical",
 "Static. Character holds direct address; thought bubble visible. 2s."),

("Information about an investment travels in a specific order.",
 f"{STYLE} Wide diagram. A horizontal flow: a single investment icon at the left, with a series of arrows pointing right through different groups. The groups are not yet labeled — just the directional flow established. Bold label: 'TRAVELS IN ORDER.'",
 "Wide diagram", "Flat, white", "The framework introduced — information has direction",
 "Horizontal flow diagram; investment icon; groups not yet labeled; order established",
 "Static. Flow direction clear. Groups empty for now. 2s."),

("First: the people closest to the asset. The founders, the early backers, the insiders.",
 f"{STYLE} Close-up on first group in the flow. Small figures: a founder with a lightbulb, an early backer with a small check, an insider with a key. Bold label: 'STAGE 1: INSIDERS.' Price chart beside them shows price near the bottom. They are in early.",
 "Close-up on stage 1", "Flat, white, stage 1 highlighted", "The first group — they know first, buy early",
 "Founder, backer, insider figures; STAGE 1 label; low price chart beside them",
 "Static. Stage 1 highlighted; low price visible. 2s."),

("Then: institutional investors. The funds, the banks, the professional money.",
 f"{STYLE} Close-up on second group. Larger figures: fund building, bank logo, professional investor with briefcase. Bold label: 'STAGE 2: INSTITUTIONS.' Price chart beside them shows price rising — already up from stage 1.",
 "Close-up on stage 2", "Flat, white, stage 2 highlighted", "The second group — institutions arrive, price rises",
 "Fund, bank, professional figures; STAGE 2 label; rising price chart",
 "Static. Stage 2 highlighted; price visibly higher than stage 1. 2s."),

("Then: financial media. The stories appear. The coverage builds.",
 f"{STYLE} Close-up on third group. News camera, newspaper front page, broadcast microphone icons. Bold label: 'STAGE 3: MEDIA.' Price chart beside them shows price significantly higher — the narrative is now being broadcast. Coverage icons multiplying.",
 "Close-up on stage 3", "Flat, white, stage 3 highlighted", "The third group — media amplifies, price higher still",
 "News camera, newspaper, microphone icons; STAGE 3 label; higher price chart",
 "Static. Stage 3 highlighted; price significantly higher. 2s."),

("Then: mainstream culture. The dinner table. The taxi driver. The shoeshine boy.",
 f"{STYLE} Close-up on fourth group. Three icons: a dinner table with talking figures, a taxi with a driver, the shoeshine boy from 1929. Bold label: 'STAGE 4: EVERYONE.' Price chart beside them shows price at the top — the peak.",
 "Close-up on stage 4", "Flat, white, stage 4 highlighted", "The fourth group — retail arrives at the top",
 "Dinner table, taxi driver, shoeshine boy icons; STAGE 4 label; price at peak",
 "Static. Stage 4 highlighted; price at maximum. 3s."),

("By the time information reaches the last group — the group furthest from the source — the first group has been holding for months.",
 f"{STYLE} Wide diagram showing all four stages. A timeline above the stages shows how long each group has been holding. Stage 1: MONTHS. Stage 2: WEEKS. Stage 3: DAYS. Stage 4: TODAY. The holding time differential is the point. Bold label: 'STAGE 1 HAS BEEN HOLDING FOR MONTHS.'",
 "Wide diagram, all four stages", "Flat, white", "The time differential — stage 1 has been waiting",
 "All four stages with holding time differential above; stage 1 months vs stage 4 today",
 "Static. Timeline above stages shows differential. 3s."),

("The first group needs to sell.",
 f"{STYLE} Close-up on stage 1 figures. They now hold SELL signs — not aggressive, just ready. They have been waiting. Their price chart shows the current peak. Bold label above them: 'NEED TO SELL.' They are not villains — they are rational. They just knew first.",
 "Close-up on stage 1", "Flat, white", "The stage 1 incentive — they need an exit",
 "Stage 1 figures holding sell signs; peak price chart; NEED TO SELL label",
 "Static. Sell signs held; price at peak. 2s."),

("To sell, they need buyers.",
 f"{STYLE} Wide diagram. A simple supply-demand visual: SELLERS (stage 1, left) need BUYERS (right side, empty). An arrow from sellers to an empty space labeled: 'NEED: BUYERS.' The empty space is waiting to be filled.",
 "Wide diagram", "Flat, white", "The market mechanic — sellers need buyers",
 "Stage 1 sellers need buyers; empty buyer space; supply-demand dynamic",
 "Static. Empty buyer space prominent. 2s."),

("The buyers are the people who just found out.",
 f"{STYLE} Wide diagram. The empty buyer space fills in — with the stage 4 figures: dinner table, taxi driver, shoeshine boy. They walk in from the right, money in hand, excited. Bold label: 'THE BUYERS: STAGE 4.' The circle closes.",
 "Wide diagram", "Flat, white", "The circuit completed — stage 4 is the exit liquidity",
 "Stage 4 figures filling buyer space; money in hand; THE BUYERS label",
 "Animated. Stage 4 figures walk in to fill buyer space. 3s."),

("Kennedy was not smarter than the market.",
 f"{STYLE} Medium shot. Kennedy figure beside a brain icon — his brain is the same size as a normal brain. No special intelligence indicated. Bold label: 'NOT SMARTER.' The reframe: his edge was not IQ.",
 "Medium shot", "Flat, white", "The reframe — intelligence was not the advantage",
 "Kennedy with normal-sized brain; NOT SMARTER label; IQ not the variable",
 "Static. Normal brain size. Label clear. 2s."),

("He understood something simpler: by the time you hear about it at the shoeshine stand, the people who knew first have been waiting for you.",
 f"{STYLE} Wide shot. Kennedy stands at the shoeshine stand again — but now the diagram from above is visible behind him: the four stages, the time differential, stage 1 waiting with sell signs. He sees the whole system. Bold label: 'THEY HAVE BEEN WAITING FOR YOU.' The shoeshine boy is stage 4. Kennedy refused to be stage 4.",
 "Wide shot", "Flat, warm", "The complete insight — Kennedy saw the whole system",
 "Kennedy at shoeshine stand with full system diagram behind him; WAITING FOR YOU label",
 "Static. System diagram visible behind Kennedy; his understanding complete. 3s."),

# ── THE MECHANISM ─────────────────────────────────────────────────────────────

("Here is what is happening inside your brain.",
 f"{STYLE} Medium shot. The main character faces camera. The brain inside the skull shifts to a focused, analytical expression — ready to explain. Clean white background. The shoeshine story is behind us; the mechanism is now.",
 "Medium shot, direct address", "Flat, white", "The mechanism section begins — analytical pivot",
 "Character and brain both analytical; facing camera; mechanism incoming",
 "Static. Brain shifts to focused expression. 2s."),

("Your brain does not calculate probability mathematically.",
 f"{STYLE} Wide diagram. A mathematical probability formula (simple Bayesian-style) with a bold red X through it. Beside it: the brain figure with arms crossed — not using this method. Bold label: 'NOT MATHEMATICALLY.'",
 "Wide diagram", "Flat, white, red X on formula", "The false assumption corrected",
 "Math formula with red X; brain not using it; NOT MATHEMATICALLY label",
 "Static. Red X on formula; brain turned away from it. 2s."),

("It estimates probability by how easily it can recall examples.",
 f"{STYLE} Wide diagram. Instead of a formula, the brain holds a simple stack of memory cards — each card is a recalled example. The more cards, the higher the estimated probability. Bold label: 'ESTIMATES BY RECALL.' Simple, visual, clear.",
 "Wide diagram", "Flat, white", "The actual mechanism — recall as probability proxy",
 "Brain holding memory card stack; more cards = higher probability estimate; label",
 "Animated. Cards stack up; probability bar rises with each card. 3s."),

("When something is in every conversation, every feed, every headline — your brain registers: this is everywhere. This must be important. This must be working.",
 f"{STYLE} Wide shot. The main character is surrounded by media inputs: phone screen, laptop, TV, friend talking, newspaper. All showing the same asset. Above the character's head: the memory card stack is overflowing. The brain registers: EVERYWHERE = IMPORTANT = WORKING. Three automatic conclusions in sequence.",
 "Wide shot, surrounded by media", "Flat, white, inputs from all sides", "The availability flood — ubiquity creates false certainty",
 "Character surrounded by media all showing same asset; memory stack overflowing; three auto-conclusions",
 "Animated. Inputs arrive from all sides; memory stack grows; three conclusions pop up. 3s."),

("Psychologists call this the availability heuristic.",
 f"{STYLE} Wide shot. A textbook-style label appears in bold: 'AVAILABILITY HEURISTIC.' Below it: the memory card stack visual from before. The brain inside the skull reads the label with recognition. Bold diegetic text on a clean white board.",
 "Wide shot", "Flat, white", "The name — availability heuristic defined",
 "AVAILABILITY HEURISTIC label; memory stack below; brain recognizing",
 "Animated. Label appears stroke by stroke. 2s."),

("The more easily you can recall something, the more probable your brain judges it to be.",
 f"{STYLE} Wide diagram. Two examples: LEFT — easy to recall (many cards, full stack) → HIGH PROBABILITY estimated. RIGHT — hard to recall (few cards, thin stack) → LOW PROBABILITY estimated. The correlation is direct and visual. Bold label: 'RECALL = PROBABILITY.'",
 "Wide diagram", "Flat, white", "The rule stated visually — recall drives probability",
 "Easy recall vs hard recall; probability estimates inversely matching; RECALL = PROBABILITY",
 "Static. Both sides visible; correlation clear. 3s."),

("And nothing makes information more available than mass media coverage.",
 f"{STYLE} Wide shot. A media coverage meter — a dial going from LOW to HIGH. At HIGH: the memory card stack is enormous, overflowing. Bold label: 'MEDIA COVERAGE = MAXIMUM AVAILABILITY.' The mechanism connecting media to brain is complete.",
 "Wide shot", "Flat, white, coverage meter prominent", "The connection — media is the availability amplifier",
 "Coverage meter at high; overflowing memory stack; MEDIA = MAX AVAILABILITY label",
 "Animated. Meter rises to high; stack grows correspondingly. 2s."),

("Here is the problem.",
 f"{STYLE} Medium shot. The character and brain both pause. The brain's expression shifts slightly — the problem is incoming. Bold label: 'HERE IS THE PROBLEM.' A visual pause before the reveal.",
 "Medium shot", "Flat, white", "The pivot — problem about to be named",
 "Character and brain pausing; problem expression; HERE IS THE PROBLEM label",
 "Static. Both hold paused expression. 2s."),

("Media coverage of an investment peaks at the same moment as its price.",
 f"{STYLE} Wide diagram. Two lines on the same chart: a PRICE line (green) and a MEDIA COVERAGE line (red). They rise together and peak at the exact same point — simultaneously. Bold label: 'PEAK COVERAGE = PEAK PRICE.' The synchrony is the trap.",
 "Wide diagram, dual chart", "Flat, white, two lines", "The core problem — coverage and price peak together",
 "Price and media coverage lines peaking simultaneously; PEAK COVERAGE = PEAK PRICE label",
 "Animated. Both lines rise and peak at the same point. 3s."),

("The week you hear about it the most is the week it costs the most.",
 f"{STYLE} Wide diagram. A weekly calendar. The week with the most news icons (headlines, social posts, friend mentions) has a bold price tag above it: MOST EXPENSIVE. Bold label: 'MOST HEARD = MOST EXPENSIVE.' The viewer's highest information week is their worst buying week.",
 "Wide diagram, calendar", "Flat, white", "The personal version — your peak awareness is peak price",
 "Calendar week with most news icons = highest price tag; MOST HEARD = MOST EXPENSIVE label",
 "Static. Calendar holds; peak week highlighted. 3s."),

("Your brain reads the signal and says: opportunity.",
 f"{STYLE} Medium shot on the brain inside the skull. It reads the coverage flood as a flashing green OPPORTUNITY signal. Brain expression: excited, certain, ready to act. The signal it is reading is real — the certainty it feels is real. The interpretation is wrong.",
 "Medium shot on brain", "Flat, warm, green OPPORTUNITY signal", "The false read — brain interprets coverage as opportunity",
 "Brain reading OPPORTUNITY signal from coverage; excited expression; signal interpretation",
 "Animated. OPPORTUNITY signal flashes; brain responds with certainty. 2s."),

("The signal actually says: exit.",
 f"{STYLE} Same medium shot on brain. The OPPORTUNITY signal flips — or rather, a second layer reveals itself underneath: EXIT. The true signal. The brain has been reading the visible layer (coverage = opportunity) but missing the underlying signal (coverage = exit in progress). Bold label: 'ACTUAL SIGNAL: EXIT.'",
 "Medium shot on brain", "Flat, white, EXIT revealed beneath", "The reveal — the signal's true meaning",
 "OPPORTUNITY signal flips to reveal EXIT underneath; brain's misread exposed; label",
 "Animated. Signal layer flips to reveal EXIT. Brain expression shifts. 3s."),

("The early money is leaving.",
 f"{STYLE} Wide diagram. The four-stage flow from before — but now stage 1 figures are walking out of the frame on the left, money in hand, sell orders complete. Stage 4 figures are walking in on the right, money leaving their hands. The flow of capital is visible and directional.",
 "Wide diagram, flow visible", "Flat, white", "The capital flow — stage 1 out, stage 4 in",
 "Stage 1 walking out with money; stage 4 walking in with money; directional flow",
 "Animated. Stage 1 exits; stage 4 enters; capital changes direction. 3s."),

("And they needed your attention — your brain's availability calculation — to make the exit possible.",
 f"{STYLE} Wide shot. Stage 1 figures hold a large megaphone pointed at the media building. The media building broadcasts to the character's phone. The character's availability heuristic fires. The character moves toward the market. Stage 1 gets their exit. The chain is complete. Bold label: 'YOUR ATTENTION ENABLED THE EXIT.'",
 "Wide shot, full chain visible", "Flat, white", "The full mechanism — attention as exit infrastructure",
 "Stage 1 → media → character's brain → market entry; stage 1 exit complete; chain labeled",
 "Animated. Chain flows left to right; each step activates next. 3s."),

# ── THE SAME PATTERN, 400 YEARS ───────────────────────────────────────────────

("Kennedy saw it in 1929. But the pattern is older than Kennedy.",
 f"{STYLE} Wide shot. A long horizontal timeline. Kennedy's 1929 shoeshine moment is marked with a dot — but the timeline extends far to the left, into the past. Bold label: 'OLDER THAN 1929.' The pattern predates Kennedy by centuries.",
 "Wide shot, timeline", "Flat, white", "The pattern's age — Kennedy was not the first to see it",
 "Timeline extending past 1929; Kennedy dot visible; OLDER THAN 1929 label",
 "Static. Timeline extends left far past Kennedy. 2s."),

("1637. The Dutch Republic. Tulip bulbs were trading at ten times the annual wage of a skilled craftsman.",
 f"{STYLE} Wide shot. A Dutch Republic scene — windmills, canals, flat cartoon style. A single tulip in the center of the frame — ornate, glowing, almost sacred. Beside it: a price tag showing 10x annual wage. Small figures of craftsmen looking up at it in awe. Bold label: '1637 · DUTCH REPUBLIC.'",
 "Wide shot, Dutch scene", "Flat, warm Dutch tones", "Tulip mania — first bubble in the pattern",
 "Dutch scene with revered tulip; 10x wage price tag; craftsmen figures; date label",
 "Static. Tulip prominent; price tag visible. 3s."),

("People mortgaged their homes for flowers.",
 f"{STYLE} Wide shot. A cartoon figure handing over a house deed in exchange for a tulip bulb. Expression: certain, excited. The house icon goes left; the bulb goes right. Bold label: 'MORTGAGED FOR FLOWERS.' The irony is the visual.",
 "Wide shot", "Flat, warm", "The irrationality quantified — houses for flowers",
 "Figure exchanging house deed for tulip bulb; certain expression; label",
 "Static. Exchange visible; expression of certainty. 2s."),

("When the tulip had become the topic of conversation at every tavern in Amsterdam — when everyone knew the names of the most valuable varieties — the collapse came within weeks.",
 f"{STYLE} Wide shot. Multiple tavern scenes — each with figures talking, and above each table a tulip icon in the conversation bubble. The availability is total. Then: a bold collapse graphic — tulip price chart dropping to near zero. Bold label: 'WEEKS AFTER EVERYONE KNEW.' The timing is the point.",
 "Wide shot, multiple taverns", "Flat, warm to dark", "The timing — collapse follows universal awareness",
 "Taverns all discussing tulips; universal awareness; collapse chart weeks later",
 "Animated. Tavern bubbles fill; collapse follows. WEEKS AFTER label. 3s."),

("1720. The South Sea Company. A British trading firm with vague promises of profit from South American trade.",
 f"{STYLE} Wide shot. A British 1720 scene — Parliament building, period streets. A large company sign: 'SOUTH SEA COMPANY — PROFITS FROM SOUTH AMERICAN TRADE.' The promises on the sign are deliberately vague — ornate language, no specifics. Bold label: '1720 · SOUTH SEA COMPANY.'",
 "Wide shot, British period scene", "Flat, warm period tones", "South Sea — second bubble in the pattern",
 "1720 British scene; South Sea Company sign with vague promises; date label",
 "Static. Company sign prominent; vague language visible. 2s."),

("Members of parliament bought in. Then their families. Then the servants.",
 f"{STYLE} Wide shot showing three tiers: top tier — large Parliament figures buying in (stage 1-2). Middle tier — their families buying in (stage 3). Bottom tier — servants buying in (stage 4). A price chart beside each tier shows the price rising as you move down. The cascade is visual.",
 "Wide shot, three tiers", "Flat, warm", "The cascade — the pattern travels down the social hierarchy",
 "Parliament, families, servants in three tiers; price rising as tiers descend",
 "Animated. Tiers appear from top to bottom; price rises with each. 3s."),

("When the servants were buying, the company directors were selling.",
 f"{STYLE} Wide split. Left: servant figures buying in, excited, money leaving their hands. Right: company director figures selling, calm, money arriving in their hands. The split shows simultaneous opposing flows. Bold label across center: 'DIRECTORS SELLING AS SERVANTS BUY.'",
 "Wide split", "Flat, white", "The simultaneous exit — stage 1 exits as stage 4 enters",
 "Servants buying vs directors selling simultaneously; opposing flows visible",
 "Static. Split holds; both flows visible simultaneously. 3s."),

("2000. Dot-com. Companies with no product, no revenue, and no customers were valued at billions.",
 f"{STYLE} Wide shot. A 2000 tech office scene — computers, startup energy, bold valuations. A company sign: '.COM — NO PRODUCT, NO REVENUE, NO CUSTOMERS — VALUED: $2 BILLION.' The absurdity is in the numbers. Suited investor figures throwing money at the sign. Bold label: '2000 · DOT-COM.'",
 "Wide shot, 2000 tech scene", "Flat, bright tech tones", "Dot-com — third bubble in the pattern",
 "2000 tech office; company sign with absurd valuation despite no product; investors throwing money",
 "Static. Valuation sign prominent. Absurdity clear. 3s."),

("When your parents started asking if they should buy internet stocks, the Nasdaq was six weeks from its all-time high.",
 f"{STYLE} Medium shot. Two parent-aged cartoon figures at a dinner table, speech bubble: 'SHOULD WE BUY INTERNET STOCKS?' Beside them: a Nasdaq chart with a bold marker SIX WEEKS BEFORE THE HIGH. Bold label: 'WHEN YOUR PARENTS ASK — YOU ARE SIX WEEKS FROM THE TOP.' The viewer's shoeshine boy moment.",
 "Medium shot", "Flat, warm domestic", "The personal version of dot-com — parents as shoeshine boy",
 "Parent figures asking about internet stocks; Nasdaq chart showing six weeks from high",
 "Static. Parents' question and chart position visible simultaneously. 3s."),

("2021. A cryptocurrency featuring a dog — created as a joke — reached a market capitalisation of eighty billion dollars.",
 f"{STYLE} Wide shot. A cartoon dog coin — Dogecoin-style, exaggerated, clearly absurd — floating in the center of the frame. A price tag: $80 BILLION MARKET CAP. Small figures around it on their phones — memes, tweets, social media posts visible. Bold label: '2021 · CREATED AS A JOKE.'",
 "Wide shot", "Flat, bright social media tones", "Crypto meme — fourth bubble in the pattern",
 "Dog coin with $80B market cap; phone users with memes around it; JOKE label",
 "Static. Dog coin prominent; market cap label. 3s."),

("It got there the week it became a meme. The week everyone had heard of it.",
 f"{STYLE} Wide diagram. A meme spread chart and a price chart side by side — both showing the same peak week. The week the meme went universal is the week the price peaked. Bold label: 'MEME PEAK = PRICE PEAK.' The availability mechanism in modern form.",
 "Wide diagram", "Flat, white", "The modern shoeshine moment — meme virality as the signal",
 "Meme spread and price chart peaking same week; MEME PEAK = PRICE PEAK label",
 "Static. Both charts peak in same column. 3s."),

("The assets change. The technology changes. The narrative changes.",
 f"{STYLE} Wide shot. Four small icons in a row — tulip, South Sea ship, .com logo, dog coin — each different, each from its era. Bold labels: ASSET CHANGES, TECHNOLOGY CHANGES, NARRATIVE CHANGES. Three checkmarks of things that are different. What follows will be the one thing that isn't.",
 "Wide shot", "Flat, white", "The three things that change — building to the one that doesn't",
 "Four era icons; three CHANGES labels; preparing for the constant",
 "Animated. Three change labels appear above different icons. 3s."),

("The mechanism does not.",
 f"{STYLE} Wide shot. Below the four icons — a single horizontal bar connecting all four, labeled: 'THE MECHANISM.' It has not changed. The same availability signal, the same four-stage cycle, the same shoeshine moment. Bold label: 'DOES NOT CHANGE.' The bar is unbroken across all four eras.",
 "Wide shot", "Flat, white, connecting bar prominent", "The constant — the mechanism across all eras",
 "Connecting bar across all four eras; THE MECHANISM label; unbroken constant",
 "Static. Bar connects all four; DOES NOT CHANGE label. 3s."),

("Kennedy understood it with a shoeshine brush. You now have the name for it.",
 f"{STYLE} Wide shot. Left: Kennedy in 1929 with a shoeshine brush — intuitive understanding, no formula. Right: the main character today with the AVAILABILITY HEURISTIC label visible. Both understood the same thing — Kennedy by feel, the viewer by name. Bold label: 'SAME UNDERSTANDING. DIFFERENT ERA.'",
 "Wide shot, split — Kennedy and viewer", "Flat, warm left, white right", "The bridge — 1929 intuition meets modern science",
 "Kennedy with brush vs character with availability heuristic label; same understanding",
 "Static. Both sides of split visible; SAME UNDERSTANDING label. 3s."),

# ── THE POPULAR MISREADING ────────────────────────────────────────────────────

("Everyone who hears this arrives at the same conclusion.",
 f"{STYLE} Wide shot. A crowd of cartoon figures — all with matching thought bubbles beginning to form above their heads. Bold label: 'SAME CONCLUSION.' The crowd is diverse but the thought bubbles are identical in shape.",
 "Wide crowd shot", "Flat, white", "The setup — the wrong conclusion is universal",
 "Crowd with matching thought bubbles forming; SAME CONCLUSION label",
 "Static. Crowd visible; thought bubbles uniformly shaped. 2s."),

("The solution is to be smarter. To see through the hype. To have better judgment than the average investor.",
 f"{STYLE} Wide shot. The thought bubbles reveal: 'BE SMARTER,' 'SEE THROUGH HYPE,' 'BETTER JUDGMENT.' A brain icon above the crowd with a graduation cap — intelligence as the proposed solution. Bold label: 'THE POPULAR MISREADING.'",
 "Wide shot", "Flat, white", "The wrong conclusion named — intelligence as false solution",
 "Thought bubbles showing BE SMARTER / SEE THROUGH HYPE / BETTER JUDGMENT; popular misreading label",
 "Animated. Three conclusion labels appear in bubbles. 3s."),

("That is not what the research shows.",
 f"{STYLE} Wide shot. A bold red X appears over the thought bubbles. Research papers float in. Bold label: 'NOT WHAT THE RESEARCH SHOWS.' The correction is incoming.",
 "Wide shot", "Flat, white, red X", "The correction — research overrides popular belief",
 "Red X over intelligence solution bubbles; research papers floating in",
 "Animated. Red X appears; research papers arrive. 2s."),

("In study after study, professional fund managers — people whose entire career is identifying good investments before others do — show the same pattern of entering late-stage narratives.",
 f"{STYLE} Wide shot. A professional fund manager figure — suit, briefcase, Bloomberg terminal, portfolio charts. Above them: the same stage 4 entry pattern from before. Same late-stage entry. Same availability heuristic firing. Bold label: 'FUND MANAGERS — SAME PATTERN.'",
 "Wide shot", "Flat, white", "The professional evidence — experts fall for it too",
 "Fund manager figure with late-stage entry pattern above; professional fails same way",
 "Static. Fund manager and entry pattern visible; SAME PATTERN label. 3s."),

("Not because they are unsophisticated.",
 f"{STYLE} Medium shot on fund manager figure. Intelligence indicators around them: advanced degree badge, years of experience counter, portfolio size. Not lacking sophistication. Bold label: 'NOT UNSOPHISTICATED.' Something else explains it.",
 "Medium shot", "Flat, white", "The counter — intelligence is not the variable",
 "Fund manager with sophistication indicators; NOT UNSOPHISTICATED label",
 "Static. Sophistication indicators visible. 2s."),

("Because the availability heuristic does not discriminate between amateur and expert.",
 f"{STYLE} Wide diagram. Two brains side by side: AMATEUR (small figure) and EXPERT (suited figure). Both brains run identical availability heuristic calculations — same mechanism, same output. Bold label across both: 'SAME MECHANISM. NO DISCRIMINATION.'",
 "Wide diagram", "Flat, white", "The universality — the heuristic runs on all brains equally",
 "Amateur and expert brains running identical availability calculations; no discrimination label",
 "Static. Both brains showing identical mechanism. 3s."),

("When information is everywhere, the brain of a portfolio manager and the brain of a first-time investor run the same calculation.",
 f"{STYLE} Wide shot. A portfolio manager and a first-time investor side by side — both surrounded by the same media flood. Above both heads: identical availability stacks, identical OPPORTUNITY signals. Bold label: 'IDENTICAL CALCULATION.'",
 "Wide shot", "Flat, white, media flood from all sides", "The equality of the heuristic — same flood, same output",
 "Portfolio manager and first-time investor; identical availability stacks; identical signals",
 "Static. Both figures with identical brain outputs. 3s."),

("The feeling of certainty that comes from ubiquitous information is neurologically indistinguishable from the feeling of certainty that comes from good analysis.",
 f"{STYLE} Wide split diagram. Left: CERTAINTY FROM COVERAGE — brain flooded with media, certainty meter high. Right: CERTAINTY FROM ANALYSIS — brain working through data, certainty meter equally high. Both meters identical. Bold label: 'NEUROLOGICALLY INDISTINGUISHABLE.'",
 "Wide split diagram", "Flat, white", "The neurological truth — certainty feels identical from both sources",
 "Coverage certainty vs analysis certainty; identical meters; indistinguishable label",
 "Static. Both certainty meters at same level. 3s."),

("Your brain cannot tell the difference between knowing something and having heard it everywhere.",
 f"{STYLE} Medium shot on the brain inside the skull. Two input signals arrive: KNOWING (a small analysis document) and HEARD EVERYWHERE (a massive media flood). The brain's output for both: identical green CERTAINTY signal. Bold label: 'CANNOT TELL THE DIFFERENCE.'",
 "Medium shot on brain", "Flat, warm", "The brain's limitation — knowing vs ubiquity feel the same",
 "Brain receiving knowing and heard-everywhere inputs; identical certainty output; cannot tell difference",
 "Animated. Both inputs arrive; same output produced. 3s."),

("Kennedy was not smarter. He was further from the noise.",
 f"{STYLE} Wide shot. Kennedy stands at a distance from the media flood — not because he is more intelligent, but because he is physically further from it. The noise reaches him, but attenuated. Small noise icons fading before they reach him. Bold label: 'FURTHER FROM THE NOISE.' Distance, not intelligence, was the advantage.",
 "Wide shot", "Flat, white, noise fading with distance", "The real advantage — distance from noise, not intelligence",
 "Kennedy at distance from media noise; noise fading before reaching him; FURTHER label",
 "Static. Noise icons fading with distance from Kennedy. 3s."),

# ── THE INDUSTRY ──────────────────────────────────────────────────────────────

("Financial media does not make money from your returns.",
 f"{STYLE} Wide shot. A financial media building — sleek, modern. Inside: screens showing markets, anchors, tickers. A profit meter on the side: pointing away from YOUR RETURNS (flat line) toward ATTENTION (rising line). Bold label: 'NOT FROM YOUR RETURNS.'",
 "Wide shot, media building", "Flat, white", "The incentive misalignment stated",
 "Financial media building; profit meter pointing to attention not returns; label",
 "Static. Profit meter direction prominent. 2s."),

("It makes money from your attention.",
 f"{STYLE} Same wide shot. The attention meter now highlighted — rising, prominent. Small eye icons flowing from viewer figures into the media building. A dollar sign at the attention meter's peak. Bold label: 'FROM YOUR ATTENTION.'",
 "Wide shot", "Flat, white, attention meter highlighted", "The actual profit mechanism — attention economy",
 "Attention meter rising; eye icons flowing to media building; dollar sign at peak",
 "Animated. Attention meter rises; eyes flow in. 2s."),

("Attention is maximised by urgency. By excitement. By the feeling that something important is happening right now.",
 f"{STYLE} Wide diagram. Three attention maximizers floating: URGENCY (red clock icon), EXCITEMENT (green spark), SOMETHING IMPORTANT RIGHT NOW (bold exclamation). Each feeds into the attention meter. Bold label: 'ATTENTION MAXIMIZERS.'",
 "Wide diagram", "Flat, white", "The tools — urgency and excitement drive attention",
 "Three attention maximizers feeding attention meter; MAXIMIZERS label",
 "Static. Three tools feeding meter. 3s."),

("The content that generates the most engagement is the content about things that are moving.",
 f"{STYLE} Wide shot. A content engagement chart — two types of content: MOVING ASSETS (high engagement bar) vs STABLE ASSETS (low engagement bar). The gap is significant. Bold label: 'MOVING = ENGAGEMENT.'",
 "Wide chart shot", "Flat, white", "The content selection bias — movement drives engagement",
 "Engagement chart; moving assets bar much higher than stable; MOVING = ENGAGEMENT label",
 "Animated. Both bars appear; moving bar clearly dominant. 2s."),

("Things that are moving are things already in motion.",
 f"{STYLE} Wide diagram. A price chart with a coverage arrow tracking below it. By the time the coverage arrow is high, the price chart has already been moving for months. Bold label: 'ALREADY IN MOTION.' Coverage lags price. When you see coverage, the motion started without you.",
 "Wide diagram", "Flat, white", "The lag — coverage tracks movement that already happened",
 "Price chart with coverage arrow lagging below; ALREADY IN MOTION label",
 "Static. Coverage lag clearly visible below price. 2s."),

("Things already in motion are things you are already late to.",
 f"{STYLE} Wide shot. The main character running toward a moving train. The train is the asset in motion. The character is running to catch it — but the train is already at speed. A small label on the last car: 'ALREADY LATE.' The character may catch it — but will be in the last car.",
 "Wide shot", "Flat, white", "The lateness — coverage means you're chasing motion",
 "Character running toward already-moving train; ALREADY LATE label on last car",
 "Animated. Train moves; character runs but is behind. 2s."),

("A financial influencer with a million followers has incentives that are structurally misaligned with yours.",
 f"{STYLE} Wide shot. A financial influencer figure — phone, ring light, follower counter showing 1M. Beside them: two arrows — THEIR INCENTIVE (engagement, views, money) pointing one direction, YOUR INCENTIVE (portfolio returns) pointing the opposite direction. Bold label: 'STRUCTURALLY MISALIGNED.'",
 "Wide shot", "Flat, white", "The influencer's misalignment — their success is not your success",
 "Influencer with 1M followers; two opposing incentive arrows; MISALIGNED label",
 "Static. Opposing arrows prominent. 3s."),

("Their income comes from engagement — views, clicks, shares.",
 f"{STYLE} Close-up on influencer's income sources. Three streams flowing in: VIEWS, CLICKS, SHARES. Each stream has a dollar sign at the end. The streams flow from the audience — their engagement is the product. Bold label: 'ENGAGEMENT = THEIR INCOME.'",
 "Close-up", "Flat, white", "The monetization model — engagement is their product",
 "Three engagement streams flowing to influencer income; ENGAGEMENT = INCOME label",
 "Animated. Three streams flow in; income counter rises. 2s."),

("An asset that is rising generates engagement.",
 f"{STYLE} Wide shot. A rising asset price chart beside an engagement meter. As the price rises, engagement rises identically. Bold label: 'RISING ASSET = ENGAGEMENT.' Simple correlation. Viewers click when things are going up.",
 "Wide shot", "Flat, white", "The engagement driver — rising prices drive clicks",
 "Rising asset chart beside rising engagement meter; RISING = ENGAGEMENT label",
 "Animated. Both lines rise together. 2s."),

("An asset that is rising and that their audience is not yet in generates more.",
 f"{STYLE} Same shot, different label. The engagement meter now higher — because the rising asset is something the audience hasn't bought yet. FOMO for the audience = maximum engagement for the creator. Bold label: 'AUDIENCE NOT YET IN = MAXIMUM ENGAGEMENT.'",
 "Wide shot", "Flat, white, engagement meter higher", "The maximum engagement scenario — FOMO content",
 "Same chart but audience not in = even higher engagement; FOMO content label",
 "Animated. Engagement meter rises further than before. 2s."),

("The content that performs best for the creator is precisely the content that gets you in at the point that maximises someone else's exit.",
 f"{STYLE} Wide diagram. The full chain: CREATOR'S BEST CONTENT → VIEWER BUYS AT PEAK → STAGE 1 EXIT COMPLETED. The chain is visible and complete. Bold label across the center: 'YOUR ENTRY = THEIR EXIT.' The creator's incentive and stage 1's need are aligned. Your interest is not in this equation.",
 "Wide diagram, full chain", "Flat, white", "The complete chain — creator aligns with stage 1 against viewer",
 "Creator content → viewer buys at peak → stage 1 exits; YOUR ENTRY = THEIR EXIT label",
 "Animated. Chain flows left to right; each stage activates next. 3s."),

("This is not always intentional. It is structural.",
 f"{STYLE} Wide shot. The influencer figure — now shown without villain framing, just a regular creator following incentives. Above: the structural diagram showing how incentives automatically produce this outcome without malice. Bold label: 'STRUCTURAL, NOT ALWAYS INTENTIONAL.' The system is the villain.",
 "Wide shot", "Flat, white", "The nuance — structure, not malice",
 "Influencer without villain framing; structural incentive diagram above; system is villain",
 "Static. Structural diagram visible; influencer just following incentives. 2s."),

("The financial attention economy is perfectly calibrated to deliver you to the market at the worst possible moment.",
 f"{STYLE} Wide shot. A large machine — the financial attention economy — with inputs (media, social, influencers) and one output: VIEWER ENTERS MARKET AT PEAK. The calibration is precise. Bold label: 'PERFECTLY CALIBRATED.' The brain villain sits atop the machine, monitoring its output.",
 "Wide shot, machine", "Flat, white, machine prominent", "The system named — attention economy as delivery mechanism",
 "Attention economy machine delivering viewer to peak entry; brain villain monitoring; CALIBRATED label",
 "Static. Machine and output visible; brain villain overseeing. 3s."),

# ── THE REAL CONCLUSION ───────────────────────────────────────────────────────

("In 1996, economist Robert Shiller published research that reframed how we understand financial manias.",
 f"{STYLE} Wide shot. Robert Shiller as a cartoon figure — professorial, thoughtful. A book or research paper floating beside him. Bold label: '1996 · ROBERT SHILLER.' Behind him: the four bubble timeline (tulips, South Sea, dot-com foreshadowed). He is about to name what Kennedy already knew.",
 "Wide shot", "Flat, white", "Shiller introduced — the academic who named the pattern",
 "Shiller figure with research; bubble timeline behind him; 1996 label",
 "Static. Shiller and timeline visible. 2s."),

("Markets, he argued, do not move on fundamentals alone. They move on narratives.",
 f"{STYLE} Wide diagram. Two market drivers: FUNDAMENTALS (small icon, labeled) and NARRATIVES (large flowing story-scroll icon, labeled). The narratives icon is significantly larger. Bold label: 'MARKETS MOVE ON NARRATIVES.' Traditional economics shown smaller beside it.",
 "Wide diagram", "Flat, white, narratives larger", "The core Shiller insight — narratives drive markets",
 "Fundamentals small vs narratives large; MARKETS MOVE ON NARRATIVES label",
 "Static. Narratives clearly larger than fundamentals. 3s."),

("Stories spread like viruses — from insider to institution to media to dinner table — and they inflate prices as they travel.",
 f"{STYLE} Wide diagram. The four-stage information flow — but now visualized as a virus spreading. Each stage represents a new wave of infection. At each wave, the price inflates. The narrative travels and inflates as it goes. Bold label: 'NARRATIVE SPREADS — PRICE INFLATES.'",
 "Wide diagram, viral spread", "Flat, white", "The narrative virus — spread and inflation linked",
 "Four-stage spread visualized as viral waves; price inflating at each wave; label",
 "Animated. Waves spread outward; price inflates at each stage. 3s."),

("The further the narrative spreads, the higher the price.",
 f"{STYLE} Wide diagram. A correlation chart: NARRATIVE REACH (x-axis) vs PRICE (y-axis). The line rises steadily as reach increases. Simple, clean, direct. Bold label: 'SPREAD = PRICE RISE.'",
 "Wide diagram", "Flat, white", "The correlation — reach and price move together",
 "Narrative reach vs price correlation; rising line; SPREAD = PRICE RISE label",
 "Animated. Line rises as reach increases on x-axis. 2s."),

("The further the narrative spreads, the closer you are to the end.",
 f"{STYLE} Same chart — but now a second line appears: DISTANCE TO END (declining as reach increases). The two lines cross. As spread increases, you are simultaneously closer to the price peak AND to the collapse. Bold label: 'CLOSER TO THE END.'",
 "Wide diagram", "Flat, white, second line added", "The inverse — max spread = end of the cycle",
 "Narrative reach chart with distance-to-end line declining; CLOSER TO END label",
 "Animated. Second line added, declining as first rises. 3s."),

("He called it narrative economics.",
 f"{STYLE} Wide shot. Shiller at a whiteboard. Bold text written: 'NARRATIVE ECONOMICS.' Below it: the virus spread diagram. The main character reads it from the side. The brain inside the skull nods — Kennedy's shoeshine intuition finally has its name.",
 "Wide shot at whiteboard", "Flat, white, label prominent", "The name given — narrative economics defined",
 "NARRATIVE ECONOMICS on whiteboard; Shiller writing it; character and brain reading",
 "Animated. Text appears; brain nods in recognition. 2s."),

("Shiller won the Nobel Prize in Economic Sciences in 2013.",
 f"{STYLE} Wide shot. Nobel Prize medal floating — gold, flat cartoon style. Shiller stands beside it, the same quiet expression. Bold label: 'NOBEL PRIZE — ECONOMICS — 2013.' Kennedy saw it in 1929. Shiller named it in 1996. It was validated in 2013.",
 "Wide shot", "Flat, white, Nobel medal prominent", "The Nobel — validation",
 "Shiller beside Nobel medal; 2013 label; understated satisfaction",
 "Static. Medal glows softly. 2s."),

("His insight: the shoeshine boy was not a quirk of 1929. He is a structural feature of every financial mania.",
 f"{STYLE} Wide shot. The shoeshine boy figure — now not in 1929 but in a timeline that spans 1637 to 2021. The same figure present at every bubble. Bold label: 'STRUCTURAL FEATURE — EVERY MANIA.' Kennedy's shoeshine boy is Shiller's structural feature. They were the same thing.",
 "Wide shot, full timeline", "Flat, white", "The structural insight — the shoeshine boy repeats",
 "Shoeshine boy figure across full 400-year timeline; STRUCTURAL FEATURE label",
 "Static. Shoeshine boy visible at every bubble. 3s."),

("The moment the narrative becomes universal is the moment its function changes.",
 f"{STYLE} Wide diagram. A narrative spread curve — rising toward universal coverage. At the moment it becomes universal, a vertical bold line appears: 'FUNCTION CHANGES HERE.' Before the line: OPPORTUNITY SIGNAL. After the line: EXIT MECHANISM. The crossover is the key.",
 "Wide diagram", "Flat, white, crossover line prominent", "The function change — opportunity becomes exit at universality",
 "Narrative spread curve; crossover line at universal coverage; function change labeled",
 "Animated. Curve rises; vertical line appears at universal coverage. 3s."),

("It stops being a story about opportunity.",
 f"{STYLE} Wide shot. The OPPORTUNITY label on the narrative — crossed out with a slow, deliberate red X. Bold label: 'NO LONGER OPPORTUNITY.' The story has not changed. Its function has.",
 "Wide shot", "Flat, white, red X on opportunity", "The function end — opportunity label removed",
 "OPPORTUNITY label crossed out deliberately; NO LONGER label; story unchanged but function different",
 "Animated. Red X crosses out OPPORTUNITY slowly. 2s."),

("It becomes a mechanism of exit.",
 f"{STYLE} Same wide shot. Where OPPORTUNITY was: now EXIT MECHANISM appears. The narrative is the same. The exits are the same. The mechanism has simply revealed itself. Bold label: 'EXIT MECHANISM.' The brain villain in the corner nods — this is what it always was.",
 "Wide shot", "Flat, white", "The function revealed — it was always an exit mechanism",
 "EXIT MECHANISM label replacing opportunity; brain villain nods; always was this",
 "Static. EXIT MECHANISM label prominent. Brain villain visible. 3s."),

("You were not late.",
 f"{STYLE} Medium shot, direct address. The character faces camera. Expression: the relief of reframing. Bold label: 'NOT LATE.' Not a failure of speed or intelligence. Something else was happening.",
 "Medium shot, direct address", "Flat, white", "The reframe — lateness was not the problem",
 "Character facing camera; NOT LATE label; relief expression",
 "Static. Character holds direct address. 2s."),

("You were targeted.",
 f"{STYLE} Wide shot. The character standing in the center of a targeting circle — four concentric rings, with the character at the bulls-eye. Around the targeting circle: the four-stage flow, the media machine, the availability heuristic mechanism. All of it pointing at the character. Bold label: 'TARGETED.' Expression: not defeat — understanding.",
 "Wide shot, targeting circle", "Flat, white", "The closing reframe — targeted, not late",
 "Character at targeting bulls-eye; entire system pointing inward; TARGETED label",
 "Static. Targeting circle holds; system visible around it. 3s."),

# ── EL MOVIMIENTO ──────────────────────────────────────────────────────────────

("Here is what you do with this.",
 f"{STYLE} Medium shot. The character turns to camera — practical, focused, ready. The brain shifts from its usual expression to a clear, action-oriented one. The shoeshine stand is visible in the background — a reminder. Bold label: 'THE MOVE.' Clean white background.",
 "Medium shot, direct address", "Flat, white, single spotlight", "The transition into action",
 "Character turns to camera; brain action-oriented; shoeshine stand in background",
 "Static. Character holds direct address; THE MOVE label. 2s."),

("Before you buy anything you first heard about in the last thirty days — from news, from social media, from any conversation — ask one question: when did the early money go in? Search the price chart for the twelve months before the coverage you are seeing now. If prices were already up significantly before the story reached you, you are standing at the shoeshine stand.",
 f"{STYLE} Wide shot. Character at laptop with a price chart open — twelve months of history visible. A marker on the chart: WHEN EARLY MONEY ENTERED (far left, low price). A second marker: WHEN YOU HEARD ABOUT IT (far right, high price). Bold label: 'CHECK THE CHART BEFORE YOU BUY.' The gap between the two markers is the warning.",
 "Wide shot", "Flat, warm, chart visible", "The first action — price history check",
 "Character at laptop; chart with early money vs heard-about markers; CHECK BEFORE BUY label",
 "Animated. Two markers appear on chart; gap visible between them. 3s."),

("Set a rule: minimum seventy-two hours between first hearing about an investment and making any decision. That window is where your prefrontal cortex catches up to the availability signal your brain has already processed as certainty.",
 f"{STYLE} Wide shot. A timer appears: 72 HOURS. Below it: a brain with two zones — AVAILABILITY SIGNAL (fired immediately, red zone) and PREFRONTAL CORTEX ANALYSIS (active after 72 hours, green zone). The timer is the gap between them. Bold label: '72 HOUR RULE.'",
 "Wide shot", "Flat, white, timer prominent", "The second action — 72-hour rule",
 "72-hour timer; brain showing availability signal vs prefrontal analysis zones; rule label",
 "Animated. Timer counts down; green zone activates at zero. 3s."),

("Use coverage volume as a contrarian signal. The investment nobody in your network is discussing is not the one with no future. It is the one where the narrative has not yet finished travelling. You are closer to the beginning, not the end.",
 f"{STYLE} Wide split diagram. Left: HIGH COVERAGE — stage 4, near the end. Right: LOW COVERAGE — stage 1 or 2, near the beginning. A bold label on the left: 'NEAR THE END.' On the right: 'NEAR THE BEGINNING.' The contrarian read: less coverage = more runway.",
 "Wide split diagram", "Flat, white", "The third action — coverage as contrarian indicator",
 "High coverage = near end vs low coverage = near beginning; contrarian read labeled",
 "Static. Both sides visible; contrarian labels clear. 3s."),

("Automate your core investment in a low-cost index fund so that every week you spend not chasing narratives, your money is already compounding in something no story can inflate or destroy.",
 f"{STYLE} Wide shot. An automatic investment arrow flowing into an index fund icon — labeled LOW COST, DIVERSIFIED, AUTOMATED. In the background: narratives swirling (media flood, influencer content) — but the automated transfer is immune, running regardless. Bold label: 'AUTOMATED — NARRATIVE PROOF.'",
 "Wide shot", "Flat, white, automated arrow prominent", "The fourth action — automated index investment",
 "Automatic transfer to index fund; narrative swirl in background; AUTOMATED NARRATIVE PROOF label",
 "Animated. Transfer arrow runs while narratives swirl around it; immune. 3s."),

("And find one financial media source you consume regularly and stop consuming it for thirty days. Not because it is lying. Because its incentive structure is not aligned with your portfolio. Every week without that input is a week your availability heuristic runs on less manufactured urgency.",
 f"{STYLE} Wide shot. The character's media consumption — one source highlighted with a 30-day pause button. A graph showing: WITHOUT THAT SOURCE → AVAILABILITY HEURISTIC DECREASES → MANUFACTURED URGENCY DECREASES. Not censorship — recalibration. Bold label: '30 DAYS. RECALIBRATE.'",
 "Wide shot", "Flat, warm", "The fifth action — media diet to recalibrate availability",
 "One media source paused; availability heuristic decreasing without it; 30 DAYS label",
 "Animated. Pause button pressed; availability meter gradually drops. 3s."),

# ── THE ENDING ────────────────────────────────────────────────────────────────

("You cannot stop the narratives from forming.",
 f"{STYLE} Wide shot. Stories forming in the background — bubbles, tulips, coins, charts — all narrative types across history. The character stands in front, small but present. The narratives are not going away. Expression: realistic, not defeated.",
 "Wide shot", "Flat, white, narratives forming in background", "The honest limit — narratives are permanent",
 "Narratives forming in background across eras; character in foreground; realistic expression",
 "Static. Background narratives visible. Character composed. 2s."),

("Every generation will have its shoeshine boy moment.",
 f"{STYLE} Wide shot. A timeline of shoeshine boy figures across generations — 1929 shoeshine, 1720 servant, 2000 parent asking about internet stocks, 2021 meme sharer. Each generation's version of the same figure. Bold label: 'EVERY GENERATION.'",
 "Wide shot, timeline of shoeshine figures", "Flat, white", "The permanent feature — the shoeshine moment repeats",
 "Shoeshine boy equivalents across all four bubble eras; EVERY GENERATION label",
 "Static. Timeline of shoeshine figures holds. 3s."),

("The story changes. The mechanism does not.",
 f"{STYLE} Wide shot. The four bubble assets (tulip, South Sea, dot-com, dog coin) above the same single availability heuristic mechanism below. The top changes; the bottom is constant. Bold split label: 'STORY CHANGES — MECHANISM DOES NOT.'",
 "Wide shot, split", "Flat, white", "The constant restated — closing the pattern",
 "Four changing assets above; single mechanism below; split label",
 "Static. Split holds; mechanism constant below. 2s."),

("But you can learn to read where in the cycle the story is.",
 f"{STYLE} Wide shot. The main character stands at the four-stage cycle diagram — but now with a magnifying glass, reading which stage the current narrative is in. The brain inside the skull has its focused, watchful expression. Expression: capable.",
 "Wide shot", "Flat, white, soft diagram glow", "The capability — reading the cycle position",
 "Character with magnifying glass at cycle diagram; reading current stage; capable expression",
 "Static. Character examines cycle with magnifying glass. Brain focused. 2s."),

("When it reaches you — when everyone you know is talking about it, when it feels urgent and obvious and inevitable — that is information.",
 f"{STYLE} Wide shot. The character's phone pinging with messages — all about the same asset. Friends mentioning it. Media covering it. Urgency feeling rising. But above the character's head: a calm label — 'INFORMATION.' Not panic. Not action. Information about cycle position.",
 "Wide shot", "Flat, warm, notification flood", "The reframe of urgency — urgency as cycle data",
 "Notification flood from all sides; character calm; INFORMATION label above not panic",
 "Animated. Notifications arrive; character stays calm; INFORMATION label holds. 3s."),

("Not the information the coverage is trying to give you.",
 f"{STYLE} Wide shot. The coverage's intended message crossed out with a red X: 'BUY NOW — THIS IS THE OPPORTUNITY.' Bold label below: 'NOT THIS INFORMATION.' What the coverage says is not the information the viewer should receive.",
 "Wide shot", "Flat, white, red X on coverage message", "The distinction — two types of information",
 "Coverage message crossed out; NOT THIS INFORMATION label; wrong message rejected",
 "Animated. Red X crosses out coverage message. 2s."),

("The information about where you are standing in the cycle.",
 f"{STYLE} Wide shot. The character stands at the four-stage cycle diagram — their position clearly marked at stage 4. Bold label: 'WHERE YOU ARE STANDING.' The cycle position is the only information that matters. Stage 4 arrival = signal to observe, not act.",
 "Wide shot", "Flat, white, character position on cycle marked", "The real information — cycle position",
 "Character position marked at stage 4 on cycle; WHERE YOU ARE STANDING label",
 "Static. Cycle position clear. Character's marker visible. 3s."),

("Someone needed you to buy at the top.",
 f"{STYLE} Wide shot. The stage 1 figures from earlier — now visible again, sell orders in hand, waiting at the market exit. They needed a buyer. The main character faces them across the market. Expression on the character: recognition, not anger. Now they understand the dynamic.",
 "Wide shot", "Flat, white", "The answer delivered — who needed you",
 "Stage 1 figures with sell orders facing character; recognition not anger; dynamic understood",
 "Static. Stage 1 figures and character facing each other. 3s."),

("Now you know who.",
 f"{STYLE} Medium shot, direct address. The character faces camera — the brain inside the skull with its composed, watchful expression. Expression: informed and capable. The shoeshine stand is faintly visible in the background — now just a memory and a warning. Bold label: 'NOW YOU KNOW.'",
 "Medium shot, direct address", "Flat, white", "The answer complete — the viewer is informed",
 "Character facing camera; brain watchful; shoeshine stand faintly behind; NOW YOU KNOW label",
 "Static. Character holds direct address. Composed. 2s."),

("Every video on this channel is one way your financial gut has been hacked.",
 f"{STYLE} Wide shot, white background. The main character faces camera directly — the brain inside the skull with its focused, watching expression. A row of small icons stretches behind: bandwidth, dopamine, somatic markers, mental accounting, status quo, availability — each labeled. The channel's pattern is complete.",
 "Wide shot, direct address", "Flat, white", "Channel mission — the pattern named",
 "Character facing camera; row of channel topic icons behind; brain watchful and composed",
 "Static. Topic icons glow softly; channel mission clear. 3s."),

("This is how they turned your attention into their exit.",
 f"{STYLE} Wide shot, closing frame. The financial attention economy machine from earlier — but now the character stands outside it, observing it rather than being fed into it. The stage 1 figures, the media building, the influencer — all visible as a system. The character watches with recognition. Expression: understanding and readiness. The system has not changed. The viewer has.",
 "Wide shot, closing frame", "Flat, white, warm machine light", "The closing image — the system visible, the viewer informed",
 "Character outside attention economy machine observing it; system visible as a whole",
 "Static. Character expression is understanding and readiness. Final hold. 3s."),

]  # end BEATS


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    TITLE = "Someone Needs You to Buy at the Top. Here's Who."
    SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 7"
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
        9:   "THE SHOESHINE BOY",
        25:  "WHAT KENNEDY UNDERSTOOD",
        37:  "THE MECHANISM",
        51:  "THE SAME PATTERN, 400 YEARS",
        65:  "THE POPULAR MISREADING",
        75:  "THE INDUSTRY",
        88:  "THE REAL CONCLUSION",
        101: "EL MOVIMIENTO",
        107: "THE ENDING",
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

    path = "/home/user/Claudeeee/Peak_Production.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
