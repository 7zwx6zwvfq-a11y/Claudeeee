#!/usr/bin/env python3
"""Word script document for Video 10: Your Brain Won't Let You Quit — And It's Costing You Everything."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE    = "Your Brain Won't Let You Quit — And It's Costing You Everything"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 10"
LABEL    = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "Alex is about to lose forty thousand dollars.",
        "He has had seven chances to stop.",
        "Every single time he had a chance to stop, his brain gave him a reason to continue.",
        "The stock is down sixty percent. It is still falling.",
        "He knows it is bad.",
        "But quitting feels like losing.",
        "And that feeling — not the market — is what's destroying him.",
        "This is the sunk cost fallacy. And by the end of this video, you will never fall for it again.",
    ]),
    ("THE SCENARIO", [
        "Alex is thirty-one years old. He has been saving for four years. He has forty thousand dollars.",
        "A tech stock he has been watching for months catches his eye. Growth story. Strong narrative. Five analysts recommending it.",
        "He buys five hundred shares at eighty dollars each. Forty thousand dollars. All of it.",
        "Two weeks later, the stock is at sixty dollars.",
        "His brain says: 'It will recover. This is temporary. Everyone holds through dips.'",
        "The stock falls to forty dollars. He has lost twenty thousand dollars.",
        "His brain says: 'You can't sell now. You would lock in the loss. Wait a little longer.'",
        "The stock falls to twenty dollars. He has lost thirty thousand dollars.",
        "His brain says: 'You've come this far. Selling now means you went through all of this for nothing.'",
        "The company files for bankruptcy. The stock goes to zero.",
        "Forty thousand dollars. Four years of savings. Gone.",
        "Every single step, the thing that stopped him from leaving was not the market. It was the money he had already spent.",
    ]),
    ("THE MECHANISM", [
        "Here is why.",
        "The sunk cost fallacy is the tendency to continue an investment because of what you have already put in — not because of what it will return.",
        "Your brain uses past investment as a reason to justify present action.",
        "This is backwards. The money you already spent is gone whether you continue or not.",
        "The only question that matters is: will continuing make things better from here?",
        "Alex never asked that question. His brain kept asking a different one: how much have I already lost?",
    ]),
    ("THE SCIENCE", [
        "In 1985, psychologists Hal Arkes and Catherine Blumer ran an experiment that changed how we understand this.",
        "They gave people a hypothetical: you've paid for a ski trip. Then a blizzard hits the resort. Do you go anyway?",
        "Ninety percent said yes. Even though going would add misery and no enjoyment. The money was already gone.",
        "This is your brain treating past spending as a debt you owe your future self.",
        "Kahneman and Tversky showed that losses feel twice as powerful as equivalent gains.",
        "So when Alex looks at a thirty-thousand-dollar paper loss, his brain registers the pain of a sixty-thousand-dollar loss.",
        "Loss aversion plus sunk cost thinking equals a trap so powerful it has a name: the Concorde Fallacy.",
        "Britain and France built an airplane they knew would never be commercially viable. They kept going because stopping meant admitting the past billions were wasted.",
        "The plane cost more to fly than it earned in revenue — for every single flight. For twenty-seven years.",
        "Alex is not running a government. But his brain is running the same program.",
    ]),
    ("THE REAL COST", [
        "Here is what this costs — not in one story, but in the aggregate.",
        "Researchers studying investor behavior found that investors hold losing stocks forty percent longer than winning stocks.",
        "This is called the disposition effect. It is the sunk cost fallacy in your investment portfolio — measured, documented, consistent.",
        "The average investor underperforms the market by two to three percent annually because of behavioral biases — and the sunk cost fallacy is one of the biggest contributors.",
        "On a forty-thousand-dollar portfolio, two percent a year over thirty years is not two percent. It is the difference between $216,000 and $324,000.",
        "That is not money you lost in a crash. That is money you quietly left on the table every year by holding the wrong positions too long.",
        "The market does not punish you for the crash. It punishes you for what you do the day after.",
    ]),
    ("THE MANY FACES", [
        "The sunk cost fallacy is not only investing. It is everywhere.",
        "Alex has been at his job for seven years. The role stopped challenging him after year three. He has stayed because of the four years he already gave.",
        "The cost of staying is not just the salary. It is every year of compounding skill and opportunity he is not building.",
        "He stays because of three years that are already gone.",
        "The same brain runs the same program in relationships.",
        "Two extra years in a relationship that is wrong. Not because it might get better. Because of the five years already given.",
        "Or the restaurant where the food was terrible, but you ate all of it because you paid twenty dollars for the meal.",
        "The scale changes. The mechanism does not.",
    ]),
    ("THE ESCAPE", [
        "There is one question that kills the sunk cost fallacy.",
        "Ask it every time. About the stock, the job, the relationship, the meal.",
        "The question is: if I had not already invested anything — not a dollar, not a day, not a meal — would I start this today?",
        "This is zero-based thinking. You erase the past. You ask only: does the future justify continuing?",
        "Would Alex buy five hundred shares of this stock today, knowing what he knows now? No.",
        "Then the answer to 'should I hold?' is also no. Because hold is just buy without the paperwork.",
        "The exit is not failure. The exit is the correction.",
        "Every dollar and every day you spend on a sunk cost is a dollar and a day you are not investing in something that could actually work.",
    ]),
    ("EL MOVIMIENTO", [
        "Here is what you do with this.",
        "The next time you are about to make a financial decision about something you have already invested in — pause. Ask the zero-based question. Write it down.",
        "Before investing in anything — set a loss limit in advance. 'If this falls twenty percent, I sell.' Write it down before you buy. Your future emotional brain cannot override a rule you set when you were calm.",
        "In your career, run a zero-based review every two years. Would you take this job today if you were offered it fresh? If the answer is no — that is not comfortable information. It is useful information.",
        "The sunk cost fallacy is not fixed by willpower. It is fixed by process. Rules made before the emotion. Questions asked before the defense.",
        "If this is how your brain handles quitting — wait until you see what it does when you believe you deserve something you haven't earned yet.",
    ]),
    ("THE ENDING", [
        "Alex is thirty-five years old now.",
        "He did not make his money back. That forty thousand dollars is gone.",
        "But he has something he did not have before. He knows exactly why he held.",
        "Knowing why you made a mistake is not consolation. It is protection.",
        "The cost is not the forty thousand dollars he lost.",
        "The cost is every dollar he did not make while waiting to get it back.",
        "Your brain will always give you a reason to stay. Name it. Write it down. Then ask the one question that matters.",
        "Would you start this today?",
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
        f"TOTAL: {total_beats} beats · ~{word_count} words · ~{round(word_count/140)} min")
    fr.font.size = Pt(9)
    fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    path = "/home/user/Claudeeee/Sunk_Cost_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
