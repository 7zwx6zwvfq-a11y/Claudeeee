#!/usr/bin/env python3
"""Word script document for Video 4: Why the Smartest People Make the Worst Financial Decisions."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "Why the Smartest People Make the Worst Financial Decisions"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 4"
LABEL = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "Meet Elliot.",
        "He had everything.",
        "A good job. A family. A reputation as one of the sharpest people in the room.",
        "And then a tumor.",
        "The surgeons removed it successfully.",
        "His IQ was intact.",
        "His memory was intact.",
        "His language. His perception. His reasoning. All intact.",
        "But Elliot could not make a decision.",
        "Not big decisions. Any decision.",
        "He could spend hours deciding where to eat.",
        "He lost his job. His marriage. His savings.",
        "And the strangest part — he knew all of this was happening.",
        "He could describe, in perfect detail, why each of his decisions had been a mistake.",
        "He just could not stop making them.",
    ]),
    ("DAMASIO", [
        "In 1991, a neurologist at the University of Iowa noticed something that did not fit any existing model.",
        "His name was Antonio Damasio.",
        "He had been studying patients like Elliot — people with damage to a specific region of the prefrontal cortex.",
        "These patients had perfectly normal cognitive function — by every standard test.",
        "And yet, every one of them was unable to function in daily life.",
        "Damasio had a hypothesis.",
        "Emotion was not the enemy of rational decision-making.",
        "Emotion was the engine of it.",
    ]),
    ("THE IOWA GAMBLING TASK", [
        "To prove it, his team designed one of the most elegant experiments in the history of neuroscience.",
        "Four decks of cards on a table.",
        "Each card you turn over either gives you money or takes it away.",
        "Decks A and B: high rewards — but even higher penalties.",
        "Decks C and D: smaller rewards — but small, predictable penalties.",
        "The instructions told participants nothing about the structure of the decks.",
        "They were simply told: try to win as much money as possible.",
        "Here is what happened with normal participants.",
        "By about the fiftieth card, most people had shifted toward decks C and D.",
        "They could not explain why.",
        "They just felt that C and D were safer.",
    ]),
    ("SOMATIC MARKERS", [
        "Damasio's team added one instrument to the experiment.",
        "A skin conductance sensor — measuring the body's stress response through the palms.",
        "What they found was extraordinary.",
        "Normal participants' palms began to sweat when they reached toward decks A or B —",
        "before they had consciously identified A and B as dangerous.",
        "The body was generating a warning signal ten seconds before conscious awareness.",
        "Damasio called these signals somatic markers.",
        "Soma — body. Marker — a tag, a flag, a signal embedded in a memory.",
        "Every significant experience you have ever had left a somatic trace in your nervous system.",
        "A bad deal that cost you. A relationship that harmed you. A time you ignored a warning and paid for it.",
        "Each one left a marker.",
        "When a similar situation appears in your future, the marker fires before you think.",
        "You feel reluctant. Uneasy. You want to leave.",
        "That feeling is not noise.",
        "It is a compressed record of every relevant experience your nervous system has ever filed away.",
    ]),
    ("ELLIOT REVISITED", [
        "Now go back to Elliot.",
        "The tumor and surgery had severed the connection between his vmPFC and his body's signaling system.",
        "Elliot could reason perfectly. He simply could not feel the answer.",
        "When he faced a decision, the somatic markers that should have pre-filtered the options — pointed him toward the safe choice before analysis began — simply did not fire.",
        "Without markers, every option looked equally valid.",
        "So he evaluated everything. For hours. And chose nothing.",
    ]),
    ("WHAT THE INDUSTRY KNOWS", [
        "Now here is where this stops being a neuroscience lesson.",
        "The industries that want your money — have known about somatic markers for decades.",
        "The field is called neuromarketing.",
        "And its entire purpose is to engineer the somatic signal you feel before you think.",
        "The countdown timer on the checkout page.",
        "The 'Only 3 left in stock' label.",
        "The one-click purchase button.",
        "None of these are accidental.",
        "They are all designed to fire a somatic signal — urgency, scarcity, social proof —",
        "before your prefrontal cortex has a chance to evaluate.",
        "You feel the pull.",
        "And by the time your brain's evaluation system catches up — you've already clicked.",
    ]),
    ("THE SMARTER PROBLEM", [
        "Here is the problem with being smart.",
        "Smarter people have more sophisticated reasoning systems.",
        "Which means they are better at constructing post-hoc justifications for decisions the body already made.",
        "The emotion came first. The reasoning followed.",
        "The intelligence was used to defend a somatic choice — not to make a rational one.",
        "This is why brilliant people get into terrible investments.",
        "The somatic marker fires — excitement, prestige, the feeling of being the one who saw it first.",
        "And then the intelligence goes to work — justifying.",
    ]),
    ("THE REFRAME", [
        "So what do you do with this?",
        "The answer is not to stop trusting your gut.",
        "Damasio's patients without somatic markers couldn't function.",
        "The answer is to audit the markers that are being engineered into you.",
        "When you feel urgency — ask who built that feeling.",
        "When you feel excitement about a financial opportunity — ask how that excitement was constructed.",
        "When you feel certain — ask when you last updated that certainty.",
        "The gut is not always right.",
        "But it is the fastest decision system you have.",
        "And it was designed — by evolution and by your life — to protect you.",
        "The problem is not the gut.",
    ]),
    ("CHANNEL MISSION", [
        "The problem is the hacking of the gut.",
        "And the hack is not new. And it is not stopping.",
        "Elliot knew which decks were bad.",
        "He just couldn't feel it.",
        "You still can.",
        "Every video on this channel is one way your financial gut has been hacked.",
        "And what you can do about it.",
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

    path = "/home/user/Claudeeee/Iowa_Gambling_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
