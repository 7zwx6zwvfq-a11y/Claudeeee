#!/usr/bin/env python3
"""Narration script for Video 12 (revised): The One Decision That Defeats All Three Brain Traps."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE    = "The One Decision That Defeats All Three Brain Traps"
SUBTITLE = "NEUROCENTS · VIDEO 12"
LABEL    = "SCRIPT (NARRATION)"

SECTIONS = [
    ("HOOK", [
        "There is one decision that defeats all three brain traps.",
        "Not a budget.",
        "Not discipline.",
        "Not a savings app.",
        "One bank transfer. Set up once. It fires before you can stop it.",
        "Workers who used this went from saving three and a half percent to thirteen point six percent — in five years.",
        "No extra income. No willpower. No spreadsheets.",
        "Just one structural decision made on a calm Tuesday — not a panicked Friday.",
        "Your brain is already calculating why this won't work for you.",
        "That calculation is the last trap. This video was built to dismantle it.",
    ]),
    ("WHY KNOWING ISN'T ENOUGH", [
        "Alex watched the last video.",
        "He understood every trap. He took notes. He sent it to his brother.",
        "He felt the specific shift — the sensation of finally seeing the system clearly.",
        "And on Friday, the salary notification arrived.",
        "His brain asked the same question it always asks: what do I deserve?",
        "Same question. Same Friday. Same four hundred euros gone.",
        "Knowing the name of a trap does not move the walls.",
        "Every personal finance book gives Alex the diagnosis.",
        "None of them give him the surgery.",
        "The surgery requires removing the decision from Alex's hands entirely —",
        "not making it easier to get right.",
    ]),
    ("WHY WILLPOWER FAILS", [
        "Roy Baumeister — social psychologist at Florida State University —",
        "spent a decade measuring something he calls ego depletion.",
        "Willpower is not a character trait. It is a finite daily resource.",
        "It depletes with every decision you make — not just financial ones.",
        "Choosing what to eat for lunch draws from the same reserve as choosing not to spend the salary.",
        "By payday, after a full week of decisions, Alex's reserve is nearly empty.",
        "His back hurts. His focus is gone. He's been patient all week.",
        "The moment he needs the most discipline is the exact moment he has the least.",
        "A budget is a willpower machine.",
        "It asks Alex to make the right call at the right moment, every payday, for thirty years.",
        "The Brain Villain doesn't get tired.",
        "Alex does.",
        "Over thirty years, the math does not favor Alex.",
        "But here's what Baumeister also found — the part that changes how you actually set up the system.",
    ]),
    ("THE DECISION", [
        "There is only one way to beat a system that runs automatically.",
        "Build a counter-system that also runs automatically.",
        "Alex set up a standing order.",
        "Four hundred euros. Every payday. One minute before the salary notification arrives.",
        "Before the Reward Trap fires its first question: what do I deserve?",
        "Before Mental Accounting creates a label: this is mine, this is safe, this is earned.",
        "Before Present Bias whispers: Future Alex will take care of it.",
        "The Reward Trap fires the moment the salary hits. The standing order fires one minute earlier.",
        "Mental Accounting assigns emotional labels to every euro Alex sees.",
        "The standing order moves four hundred euros into a category the Brain Villain is never shown.",
        "Present Bias insists that Future Alex will be more responsible than Present Alex.",
        "Past Alex already was — nine days before payday, when he was rested, calm, and the villain was quiet.",
        "Alex didn't learn to say no to the Brain Villain.",
        "He cancelled the meeting.",
        "The Brain Villain cannot argue with a decision it was never invited to attend.",
        "The money is simply not there.",
        "Not hidden. Not locked. Not off-limits.",
        "Gone before the calculation begins.",
    ]),
    ("CTA", [
        "If your brain is running these programs right now — subscribe.",
        "Every week: one bias. How it works. Who exploits it. And what you can actually do about it.",
    ]),
    ("THE SCIENCE", [
        "Richard Thaler and Shlomo Benartzi — University of Chicago and UCLA, 2004 —",
        "designed a program called Save More Tomorrow.",
        "They didn't ask workers to save more now.",
        "They asked one question, one time: when your next raise arrives, can we automatically redirect a fixed percentage?",
        "Workers said yes — once.",
        "The system then executed automatically, every raise cycle, with no further decision required.",
        "Workers who started at a savings rate of three and a half percent",
        "reached thirteen point six percent within five years.",
        "No budgets. No discipline. No willpower.",
        "One structural decision replaced sixty separate monthly battles with the Brain Villain.",
        "The only variable that changed across those five years was structure.",
        "Not income. Not financial knowledge. Not character.",
        "Structure.",
    ]),
    ("THE BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to automation.",
        "It generates a feeling Alex can't immediately name.",
        "Something like: this doesn't feel safe.",
        "Alex looks at the standing order and thinks: what if I need that money?",
        "This is Present Bias wearing a different costume.",
        "The Villain doesn't need to spend the money.",
        "It just needs to know that it could.",
        "The standing order removes the option.",
        "That's exactly why it works.",
        "And exactly why the Brain Villain will fight it — starting the moment this video ends.",
    ]),
    ("IDENTITY CLOSE + GUIDE", [
        "Alex doesn't need more discipline.",
        "He needs fewer decisions — not better ones.",
        "Every budgeting system ever created asks Alex to win the same battle every month.",
        "The standing order asks him to win it once.",
        "The Reward Trap fires on Friday. But the money is already somewhere else.",
        "Mental Accounting creates its emotional categories. But there's now one it will never see.",
        "Present Bias tells him Future Alex will be responsible.",
        "And this time — he already was.",
        "The programs are not broken.",
        "They are perfectly designed for an environment where saving made no survival sense.",
        "You didn't store food in a world where tomorrow was never guaranteed.",
        "The Brain Villain was built for that world. Not this one.",
        "The standing order is the first system Alex has ever run",
        "that was designed for the world he actually lives in.",
        "Next video: Alex gets a tax refund.",
        "Eight hundred euros he wasn't expecting.",
        "His brain treats it completely differently from every euro he ever earned.",
        "Same trap. Different label.",
        "The money disappears three times faster.",
        "The reason is the one nobody expects.",
    ]),
]


def build_docx():
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(11)

    # Header
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
    fr = footer.add_run(
        f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count / 140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/V12_revised_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words | ~{round(word_count/140)} min")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
