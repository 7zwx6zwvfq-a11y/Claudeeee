#!/usr/bin/env python3
"""Word + PDF script document for Video 3: Why Poor People Make Bad Decisions."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "Why Poor People Make Bad Decisions (It's Not What You Think)"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 3"
LABEL = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "Here is a question that will change how you see poverty.",
        "Two people walk into a lab at Princeton University.",
        "Same table. Same test. Same questions.",
        "One scores like a person of above-average intelligence.",
        "The other scores like someone who hasn't slept in 24 hours.",
        "They are the same person.",
        "The only thing the researchers changed was a thought experiment about money.",
        "For half the group: imagine a minor car repair. Three hundred dollars.",
        "For the other half: a major car repair. Three thousand dollars.",
        "The cognitive gap between the two groups was thirteen IQ points.",
        "Thirteen. From a thought experiment. About money.",
        "So the question everyone is asking — why do poor people make bad decisions — is the wrong question.",
    ]),
    ("THE EXPERIMENT", [
        "The man behind this research was not supposed to be at Princeton.",
        "His name is Sendhil Mullainathan. His mother cleaned houses in rural India before coming to America.",
        "He grew up watching people he loved make decisions that, from the outside, looked irrational.",
        "He became an economist. He wanted to understand why.",
        "He partnered with a behavioral scientist named Eldar Shafir.",
        "What if, they asked, the decisions weren't the problem?",
        "What if scarcity itself was doing something to the brain before any decision was even made?",
        "They went to Tamil Nadu, India.",
        "The sugarcane harvest creates a predictable economic cycle.",
        "Before harvest: the farmers are poor. Bills unpaid. Food short.",
        "After harvest: the same farmers are flush. Debt cleared. Pantry full.",
        "Mullainathan and Shafir tested the same farmers twice. Before harvest. After.",
        "The difference in cognitive performance: ten IQ points.",
        "Same person. Same brain. Same genes. Same village.",
        "Different bank account.",
        "And the brain changed.",
    ]),
    ("THE MECHANISM", [
        "Here is what they found happening inside.",
        "Your brain has a fixed amount of what researchers call bandwidth.",
        "Not the word used loosely — bandwidth in the precise sense.",
        "The total cognitive capacity available for processing, deciding, and planning.",
        "Think of it as RAM. Available in a finite quantity at any given moment.",
        "When you have enough — bills paid, no crisis — the brain runs efficiently.",
        "It thinks ahead. It weighs options. It plans.",
        "When scarcity enters, something different happens.",
        "The scarcity captures the bandwidth.",
        "Not metaphorically. Literally.",
        "The worry, the calculation, the constant mental arithmetic of not having enough",
        "consumes the processing power your brain needs to make good decisions.",
        "Mullainathan and Shafir called this the bandwidth tax.",
        "Being poor is not just having less money.",
        "It is running the same hardware as everyone else",
        "with far more of it consumed by background processes that never turn off.",
        "Every day, a person in financial scarcity performs a kind of cognitive triage.",
        "Which bill gets paid. Which doesn't. Which problem can wait.",
        "None of these calculations are free.",
        "Each one costs bandwidth.",
        "And bandwidth spent on survival is bandwidth not available for planning.",
    ]),
    ("THE TUNNEL", [
        "What happens when the tax gets severe enough has a name.",
        "Mullainathan and Shafir called it tunneling.",
        "The mind enters a tunnel.",
        "Inside the tunnel, the immediate crisis is in sharp focus.",
        "Urgent. Visible. Demanding.",
        "Everything outside the tunnel — the long-term consequences, the better options, the trap being walked into — disappears.",
        "From inside the tunnel, a payday loan looks rational.",
        "You need four hundred dollars to avoid eviction.",
        "The lender will give you four hundred today.",
        "You pay back four hundred and sixty in two weeks.",
        "That is four hundred percent annualized interest.",
        "From outside the tunnel, this is a catastrophic decision.",
        "From inside the tunnel, it is the only visible option.",
        "The tunnel shows the eviction. The tunnel shows the lender.",
        "The tunnel does not show the debt spiral three months from now.",
        "The same person who would never take a four-hundred-percent loan under normal conditions",
        "takes it without hesitation under sufficient scarcity.",
        "Not because they became less intelligent.",
        "Because the tunnel ate their bandwidth.",
    ]),
    ("THE MINNESOTA EXPERIMENT", [
        "This is not unique to money.",
        "In 1944, thirty-six men at the University of Minnesota volunteered to be deliberately starved for science.",
        "They were conscientious objectors. Educated, thoughtful men with rich intellectual lives.",
        "Within weeks of caloric restriction, something happened to their minds.",
        "They could not stop thinking about food.",
        "Scientists who had arrived with interests in literature, music, politics — all of it collapsed inward.",
        "One man wrote in his journal that he had tried to think about his political beliefs — a topic he cared deeply about — and simply could not.",
        "His mind kept returning to food.",
        "The scarcity had not changed his intelligence.",
        "It had redirected every available cognitive resource toward the one thing his brain identified as the immediate threat.",
        "This is what financial scarcity does.",
        "Not to weak people. Not to irresponsible people.",
        "To all people.",
    ]),
    ("THE INDUSTRY", [
        "Here is where this becomes something other than a science lesson.",
        "The payday lending industry in the United States generates approximately ninety billion dollars per year.",
        "This is not an industry that discovered a market.",
        "It is an industry built — deliberately, specifically, precisely — around the cognitive state of a bandwidth-depleted mind.",
        "The interest rates are disclosed. The terms are available. The math is transparent.",
        "But the paperwork is long. The terms are complex.",
        "The application happens at the moment of maximum stress, maximum urgency, minimum cognitive capacity.",
        "Because that is exactly when you walk through the door.",
        "Researchers found that payday loan customers underestimate the cost of their loans by a factor of three to four times.",
        "Not a rounding error. Not a misunderstanding.",
        "A systematic, predictable failure of bandwidth-depleted cognition.",
        "This is not coincidence.",
        "The complexity is not a side effect. The complexity is the product.",
        "The industry does not create the tunnel.",
        "It builds its storefronts at the entrance.",
    ]),
    ("THE REFRAME", [
        "The question everyone asks about poverty is: why don't they just make better decisions?",
        "Here is the correct question.",
        "Imagine you haven't slept in three days.",
        "You have a child with a fever.",
        "You owe rent you don't have. Your car needs a repair you cannot afford. Without the car you cannot get to work.",
        "Now sit down and optimize your retirement contribution.",
        "Now compare mortgage interest rates.",
        "Now read the fine print on the financial product being offered to you.",
        "This is not a hypothetical exercise. This is Tuesday for tens of millions of people.",
        "The cognitive research is precise.",
        "The bandwidth available to a person managing multiple simultaneous crises",
        "is not materially different from the bandwidth of someone awake for twenty-four hours",
        "or someone who has consumed alcohol to the legal driving limit.",
        "We don't look at an impaired driver and say the outcome reflects their character.",
        "We say: the condition impaired the judgment.",
        "Financial scarcity is the condition.",
        "The decisions are the symptom.",
    ]),
    ("THE SLACK", [
        "Mullainathan and Shafir identified the single factor that separates people who escape the tunnel from those who don't.",
        "They called it slack.",
        "Slack is not wealth. Slack is unused capacity.",
        "A person with a ten-thousand-dollar emergency fund has slack.",
        "A car repair does not become a crisis. A missed shift does not spiral into a payday loan into debt into cognitive overload.",
        "The spiral never starts because the slack absorbed the shock.",
        "A person with no slack — accounts at zero, no credit, no buffer — has no room for error.",
        "Any disruption triggers the tunnel.",
        "And the tunnel produces exactly the behaviors that look, from the outside, like bad character.",
        "Here is the finding that should be taught in every economics class in the world.",
        "When poor households received small cash transfers, their cognitive test scores improved immediately.",
        "Not after they spent the money. Before.",
        "Simply knowing the buffer existed freed bandwidth.",
        "The money didn't change their intelligence.",
        "The slack changed their cognitive availability.",
    ]),
    ("THE ENDING", [
        "The story we tell about poverty is a story about character.",
        "About choices. About values. About discipline.",
        "It is a story that flatters the people telling it",
        "and blames the people it describes.",
        "The research tells a different story.",
        "Being poor is not a moral condition. It is a cognitive one.",
        "The brain making bad decisions inside the tunnel is not a broken brain.",
        "It is a human brain doing exactly what evolution designed it to do —",
        "tunnel on the immediate threat, at the cost of everything else.",
        "The same mechanism that kept your ancestors alive by focusing on the predator directly in front of them",
        "is the mechanism that traps millions of people in financial crisis today.",
        "Your brain was never broken. It was just never built for this.",
        "But you can see the tunnel.",
        "You can understand the bandwidth tax before it finds you.",
        "And you can build slack — before you need it, before the tunnel opens —",
        "so that when the crisis comes, the spiral never starts.",
        "Not because you are smarter than someone inside the tunnel.",
        "Because you were outside it when you learned what it was.",
    ]),
]


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    # Title block
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
    r.font.size = Pt(16)

    doc.add_paragraph()

    beat_num = 1
    for section_title, lines in SECTIONS:
        if section_title:
            sh = doc.add_paragraph()
            sr = sh.add_run(f"— {section_title} —")
            sr.bold = True
            sr.font.size = Pt(11)
            sr.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)
            sh.paragraph_format.space_before = Pt(14)
            sh.paragraph_format.space_after = Pt(4)

        for line in lines:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            num_run = p.add_run(f"[{beat_num}]  ")
            num_run.bold = True
            num_run.font.size = Pt(9)
            num_run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
            p.add_run(line).font.size = Pt(11)
            beat_num += 1

        doc.add_paragraph()

    # Word count
    all_lines = [line for _, lines in SECTIONS for line in lines]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = beat_num - 1

    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Bandwidth_Tax_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
