#!/usr/bin/env python3
"""Word narration script document for Video 11: 3 Traps That Rewire Your Brain to Stay Broke."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "3 Traps That Rewire Your Brain to Stay Broke"
SUBTITLE = "NEUROCENTS — VIDEO 11"
LABEL = "SCRIPT (NARRATION)"

SECTIONS = [
    ("HOOK", [
        "Alex checked his bank account on Friday.",
        "Three thousand two hundred arrived — same as last month.",
        "By Sunday, twelve hundred of it was already gone.",
        "Not on rent. Not on bills.",
        "On things his brain convinced him he deserved.",
        "Here's what nobody tells you about money problems:",
        "They're not math problems.",
        "Alex isn't bad at math. He knows the difference.",
        "But his brain doesn't think in numbers. It thinks in feelings.",
        "And every payday, it runs three very specific programs.",
        "Programs that were written before Alex had his first job.",
        "Three traps — designed by millions of years of evolution —",
        "that activate the moment your paycheck hits.",
        "And by the time you realize they're running, the money is already gone.",
        "We're going to show you all three.",
        "The third one is the one nobody suspects —",
        "because it's not what you spend. It's why you'll never stop.",
    ]),
    ("TRAP 1 — THE REWARD TRAP", [
        "Trap One.",
        "Alex calls it the Reward Trap —",
        "though he doesn't call it anything, because he doesn't know it's a trap.",
        "He worked hard this week. He knows it. His body knows it.",
        "By Friday afternoon, his back hurts, his focus is gone, and he's been patient.",
        "So when his phone shows the salary notification,",
        "his brain immediately asks one question.",
        "Not: how much do I need to save?",
        "But: what do I deserve?",
        "This isn't laziness. This is neuroscience.",
        "Wolfram Schultz — neuroscientist at Cambridge University —",
        "won the Nobel Prize partly for discovering this:",
        "the brain releases dopamine not when the reward arrives, but when the reward is expected.",
        "Alex doesn't feel good because he got paid.",
        "He feels good because his brain already spent the money in his imagination.",
        "The reward center activated before a single euro left his account.",
        "The result? The eighty-five euro dinner.",
        "The one-forty jacket. The streaming subscription upgraded just for this month.",
        "Not luxuries — rewards. Small. Justified. Automatic.",
        "The Brain Villain calculated perfectly:",
        "rewards feel necessary, not optional.",
        "Alex didn't overspend. His brain spent exactly what it felt it earned.",
        "And here's where Trap One gets expensive.",
        "Professor Robert Frank — Cornell University, thirty years of research —",
        "documented what happens after every reward: hedonic adaptation.",
        "Every reward resets the baseline.",
        "The eighty-five euro dinner becomes the new normal.",
        "Next payday, eighty-five euros doesn't feel like a reward anymore.",
        "It feels like the floor.",
        "Trap One doesn't cost you once. It raises the price every single month.",
        "Trap One is the one Alex knows about, somewhere in the back of his mind.",
        "Trap Two is the one he thinks he's beating.",
    ]),
    ("CTA", [
        "If your brain is doing this to you right now — subscribe.",
        "We break down a new bias every week. It's free. And it might save you more than you think.",
    ]),
    ("TRAP 2 — THE SAFE MONEY ILLUSION", [
        "Trap Two.",
        "Alex does something most people call responsible.",
        "He keeps two thousand euros in a savings account.",
        "Emergency fund. He's proud of it. He calls it untouchable.",
        "Meanwhile, he carries eighteen hundred euros in credit card debt.",
        "Annual interest rate: twenty-three percent.",
        "Alex is paying four hundred and fourteen euros a year in interest —",
        "to protect money that earns thirty-two euros a year in savings.",
        "Net loss: three hundred and eighty-two euros. Every year.",
        "Not because Alex is bad at finance.",
        "Because his brain refuses to see these as the same money.",
        "This is Mental Accounting.",
        "Richard Thaler — Nobel Prize in Economics, 2017, University of Chicago —",
        "proved that humans don't treat money as money.",
        "We treat it as labeled categories.",
        "Two thousand euros in an account called emergency",
        "feels completely different from two thousand euros that could pay off debt.",
        "They are mathematically identical.",
        "Psychologically, they live on different planets.",
        "The Brain Villain loves this trap because it feels responsible.",
        "Alex is being careful with his emergency fund. He's being disciplined.",
        "He's paying three hundred and eighty-two euros a year for that discipline.",
        "The trap doesn't feel like a trap.",
        "It feels like a virtue.",
        "In the next video, we show why Alex's brain does the exact same trick with tax refunds —",
        "and why that money disappears faster than any other money he earns.",
        "Same trap. Different label. Same result.",
        "But before that — Trap Three.",
        "The one that makes Trap One and Trap Two inevitable.",
    ]),
    ("TRAP 3 — THE FUTURE IS FAKE", [
        "Trap Three.",
        "This one is harder to see because it's not a spending habit.",
        "It's a perception problem.",
        "Ask Alex: would you rather have a hundred euros today,",
        "or a hundred and ten in one week?",
        "He takes the hundred. Almost everyone does.",
        "Now ask him: would you rather have a hundred euros in fifty-two weeks,",
        "or a hundred and ten in fifty-three weeks?",
        "Same trade. One year later. He'll happily wait the extra week.",
        "The math is identical. The psychology is completely different.",
        "David Laibson — behavioral economist at Harvard University —",
        "spent decades quantifying this pattern.",
        "He calls it hyperbolic discounting.",
        "The further something is in the future, the less real it feels.",
        "Not less important. Less real.",
        "Future Alex — the one who needs the retirement account,",
        "the one who has to pay Future Alex's bills,",
        "the one living the consequences of Present Alex's choices —",
        "doesn't feel like Alex. He feels like a stranger.",
        "And we don't sacrifice for strangers.",
        "So Present Alex makes decisions that make perfect sense right now.",
        "Eighty-five euro dinner? He deserves it. That's Trap One.",
        "Keep the savings, carry the debt? That's responsible. That's Trap Two.",
        "Start saving next month? Future Alex will be disciplined.",
        "Future Alex is always about to be disciplined.",
        "Present Bias is the operating system.",
        "Trap One and Trap Two are the applications running on top of it.",
        "A 2024 study in the Journal of Behavioral Decision Making",
        "tracked fourteen thousand participants.",
        "People who could mentally picture their future self as the same person",
        "made twenty-three percent better financial decisions",
        "without any other intervention.",
        "Not a budgeting app. Not a financial advisor.",
        "Just the ability to see Future Alex as Alex.",
    ]),
    ("SYSTEM CLOSE", [
        "Here's what makes these three traps expensive: they don't work separately.",
        "The Reward Trap fires on Friday.",
        "Present Bias tells Alex that Future Alex will compensate.",
        "Mental Accounting keeps the debt and savings in separate boxes —",
        "so the damage never looks total.",
        "Remove any one gear, and the other two lose power.",
        "Let all three run together, and they form a system that scales with income.",
        "Researchers at Princeton — Daniel Kahneman and Angus Deaton, 2010 —",
        "found that above a certain income level, additional earnings have almost no effect",
        "on day-to-day financial behavior.",
        "Because behavioral traps consume the same percentage of income regardless of salary.",
        "Alex could earn fifty thousand or a hundred and fifty thousand.",
        "The system adjusts. The percentage stays roughly the same.",
        "This isn't about how much he earns. It's about what the system does with it.",
    ]),
    ("IDENTITY CLOSE + GUIDE", [
        "Alex isn't bad with money.",
        "He's someone whose brain was trained to protect him.",
        "The Reward Trap kept his ancestors motivated to hunt.",
        "Mental Accounting helped them separate food from poison.",
        "Present Bias kept them alive by prioritizing real, immediate threats over hypothetical future ones.",
        "The programs are not broken.",
        "They are perfectly designed for an environment that no longer exists.",
        "Knowing the three traps doesn't make them disappear.",
        "The Brain Villain doesn't retire when you name him.",
        "But it changes something fundamental:",
        "you stop blaming yourself for a system you didn't design.",
        "And that's the first condition for changing it.",
        "The next step isn't a budget.",
        "It's one decision that interrupts all three traps at the same time.",
        "Watch the next video — it shows exactly what that decision is,",
        "and why most people never make it.",
        "One decision. Three traps. The math might surprise you.",
    ]),
]


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

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

    all_lines = [line for _, lines in SECTIONS for line in lines]
    word_count = sum(len(l.split()) for l in all_lines)
    total_beats = beat_num - 1

    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer.add_run(f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Mental_Traps_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
