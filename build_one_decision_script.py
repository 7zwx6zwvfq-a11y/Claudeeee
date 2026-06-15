#!/usr/bin/env python3
"""Narration script for Video 12: The One Decision That Defeats All Three Brain Traps."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE    = "The One Decision That Defeats All Three Brain Traps"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 12"
LABEL    = "STATE 1 — SCRIPT (NARRATION)"

SECTIONS = [
    ("HOOK", [
        "Every saving system fails at the same moment: when the salary arrives.",
        "Budgets need willpower. Discipline needs energy. Both run out by payday.",
        "There is one decision that doesn't compete with any of it.",
        "Because it fires before the salary does.",
        "Last Friday, Alex's salary arrived at 9:14 in the morning.",
        "By 9:15, four hundred euros were already gone.",
        "Not on rent. Not on an impulse. Not even on something his brain had been planning.",
        "Four hundred euros moved before his brain registered the number.",
        "His brain had no vote. The decision had already been made.",
        "One standing order. Set up nine days earlier.",
        "Before the Reward Trap. Before Mental Accounting. Before Present Bias.",
        "In the last video, we showed you the three programs. This is the counter-program.",
        "This is it.",
    ]),
    ("WHY KNOWING ISN'T ENOUGH", [
        "Here's the part Alex got wrong.",
        "He watched the last video. He took notes. He sent it to his brother.",
        "He understood exactly why his brain spent the money.",
        "He felt something shift — the specific feeling of finally getting it.",
        "And on Friday, the salary notification arrived.",
        "His brain asked: what do I deserve?",
        "The same question. The same Friday. The same amount gone.",
        "Knowing the name of a trap does not move the walls.",
        "Every finance book gives Alex the diagnosis. None of them give him the surgery.",
        "Because the surgery requires removing the decision — not improving it.",
    ]),
    ("WHY WILLPOWER FAILS", [
        "Roy Baumeister — social psychologist at Florida State University —",
        "spent a decade measuring something he calls ego depletion.",
        "Willpower is not a character trait. It is a finite resource.",
        "It depletes with every decision made — not just financial ones.",
        "Deciding what to eat for lunch draws from the same reserve as deciding not to spend the salary.",
        "By payday, Alex's reserve is nearly empty.",
        "His back hurts. His focus is gone. He's been patient all week.",
        "The moment he needs discipline most is the exact moment he has the least.",
        "A budget is a willpower machine.",
        "It asks Alex to make the right decision, at the right moment, every payday, for thirty years.",
        "The Brain Villain is patient. Willpower has a ceiling.",
        "Over thirty years, the math does not favor Alex.",
    ]),
    ("THE DECISION", [
        "There is only one way to beat a system that runs automatically.",
        "Build a counter-system that also runs automatically.",
        "Alex set up a standing order.",
        "Four hundred euros. Every payday. Before he sees the balance.",
        "Before the Reward Trap can ask what he earned.",
        "Before Mental Accounting creates a label for it.",
        "Before Present Bias tells him Future Alex will handle it.",
        "The Reward Trap fires the moment the salary notification arrives. The standing order fires one minute earlier.",
        "Mental Accounting creates emotional categories — labels that make spending feel logical. The standing order creates one category the Brain Villain is never shown.",
        "Present Bias says Future Alex will be disciplined. Past Alex already was — nine days ago, when he was calm, rested, and the villain was quiet.",
        "Alex didn't learn to say no to the Brain Villain. He cancelled the meeting.",
        "The Brain Villain cannot fight a decision it was never invited to attend.",
        "The money is simply not there to be calculated.",
    ]),
    ("CTA", [
        "If your brain is running these programs right now — subscribe.",
        "Every week: one bias. How it works. Who exploits it. And what you can actually do about it.",
    ]),
    ("THE SCIENCE", [
        "Richard Thaler and Shlomo Benartzi — University of Chicago and UCLA, 2004 —",
        "designed a program called Save More Tomorrow.",
        "They didn't ask workers to save more now.",
        "They asked one question: when your next raise comes, can we automatically redirect a fixed percentage?",
        "Workers said yes — once.",
        "The system executed automatically, every raise cycle, with no further decisions required.",
        "Workers who started at a savings rate of three and a half percent",
        "reached thirteen point six percent within five years.",
        "No budgets. No discipline. No willpower.",
        "One structural decision replaced sixty monthly battles with the Brain Villain.",
        "The only variable was structure.",
    ]),
    ("THE BRAIN VILLAIN'S LAST TRICK", [
        "The Brain Villain has one response to automation.",
        "It generates a feeling Alex can't immediately name: this doesn't feel safe.",
        "Alex looks at the standing order and thinks: what if I need that money?",
        "This is Present Bias wearing a different costume.",
        "It's not about the money. It's about the option.",
        "The Brain Villain doesn't need to spend it. It just needs to know it could.",
        "The standing order removes the option.",
        "That's exactly why it works.",
        "And exactly why the Brain Villain fights it.",
    ]),
    ("IDENTITY CLOSE + GUIDE", [
        "Alex doesn't need more discipline.",
        "He needs fewer decisions — not better ones.",
        "Every budgeting system asks him to win the same battle every month.",
        "The standing order asks him to win it once.",
        "The Reward Trap fires on Friday. But the money is already gone.",
        "Mental Accounting creates false categories. But there's now one it can never reach.",
        "Present Bias says Future Alex will be responsible. And this time — he already was.",
        "The programs are not broken.",
        "They are perfectly designed for an environment where saving made no survival sense.",
        "You didn't store food in a world where tomorrow was never guaranteed.",
        "The standing order is the first system Alex has ever used that was built for his world — not theirs.",
        "Next video: Alex gets a tax refund. Eight hundred euros he didn't expect.",
        "His brain treats it completely differently from every euro he ever earned.",
        "Same trap. Different label. The refund disappears three times faster.",
        "And the reason is the one nobody expects.",
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
    fr = footer.add_run(
        f"END · {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/One_Decision_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
