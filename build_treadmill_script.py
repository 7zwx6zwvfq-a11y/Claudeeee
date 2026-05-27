#!/usr/bin/env python3
"""Word script document for Video 8: Getting Rich Is Making You Poorer."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE    = "Getting Rich Is Making You Poorer"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 8"
LABEL    = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "You did everything right.",
        "You worked hard. You got the raise. Maybe you got the promotion.",
        "For about two weeks — maybe three — it felt like something had finally changed.",
        "That specific relief. The sense that the number on your payslip matched the life you were supposed to have.",
        "And then it faded.",
        "Not the money. The money was still there.",
        "But the feeling was gone. And you were back — stretched, anxious, never quite enough.",
        "This is not a personal failure.",
        "It is a mechanism. And the people who profit from it are hoping you never find its name.",
    ]),
    ("THE RAISE", [
        "His name doesn't matter. He is every version of you that has ever gotten what you worked for.",
        "Twenty-four years old. First real job. The salary felt enormous.",
        "He upgraded his apartment. It made sense — he could afford it now.",
        "He upgraded his car. It made sense — he was making more.",
        "At twenty-eight, he got a promotion. Forty percent more than when he started.",
        "He moved to a better neighbourhood. Better restaurants. Better clothes.",
        "At thirty-two, he was earning three times what he earned at twenty-four.",
        "He was also, quietly, more anxious about money than he had ever been in his life.",
        "His lifestyle had grown to match every raise, every time, without a single conscious decision.",
        "He was further from savings than he had been at twenty-four.",
        "He could not explain it. The numbers said he should be fine.",
        "The numbers were not the problem.",
    ]),
    ("THE MECHANISM", [
        "Here is what was happening inside his brain.",
        "The human brain does not measure wealth in absolute terms.",
        "It measures wealth relative to a reference point.",
        "That reference point is not fixed. It moves.",
        "Every time your circumstances improve, your brain recalibrates what normal feels like.",
        "The new apartment becomes the baseline. The new salary becomes the floor.",
        "This is called hedonic adaptation.",
        "It is not a flaw in your psychology. It is a feature.",
        "For most of human history, this mechanism kept us alive.",
        "When conditions improved, the brain stopped celebrating and started preparing for the next threat.",
        "The problem is that it was never designed for a world where conditions can keep improving indefinitely.",
        "In that world, the adaptation never stops.",
        "And neither does the feeling that you need just a little more.",
    ]),
    ("THE TREADMILL", [
        "There is a name for what he was running on.",
        "The hedonic treadmill.",
        "You run. The belt moves. You stay in exactly the same place.",
        "Every raise, every upgrade — the belt adjusts to match your speed.",
        "Lottery winners report, within eighteen months of the win, the same levels of financial anxiety they reported before.",
        "Not worse. Not better. The same.",
        "The money changed the circumstances. The brain changed the baseline.",
        "The treadmill does not care how fast you run.",
        "It only cares that you keep running.",
    ]),
    ("THE DIDEROT EFFECT", [
        "In the eighteenth century, the French philosopher Denis Diderot received a gift: a beautiful scarlet robe.",
        "He loved it.",
        "He put it on and immediately noticed that everything else in his study looked shabby by comparison.",
        "So he replaced his chair. Then his desk. Then the curtains. Then the art on the walls.",
        "By the end, he had renovated the entire room — and gone into debt doing it.",
        "He wrote about it himself. He called it a spiral he could not explain.",
        "The name came later: the Diderot Effect.",
        "One upgrade makes everything adjacent to it feel inadequate.",
        "The new car makes the old garage unbearable. The new apartment makes the old furniture look wrong.",
        "The raise that was supposed to create breathing room instead creates a new set of gaps to fill.",
        "Your consumption does not grow in line with your income.",
        "It grows in cascades.",
    ]),
    ("THE INDUSTRY", [
        "None of this is accidental.",
        "The consumer economy is calibrated to the reset.",
        "It does not sell you things you need. It sells you the next version of your baseline.",
        "Planned obsolescence ensures that what you own today feels inadequate within two years.",
        "The subscription economy charges you monthly so each payment feels too small to cancel — while the total cost stays invisible.",
        "Consumer credit exists to close the gap between what you earn and what the reset tells you that you should have.",
        "The average household carries credit card debt not because of emergencies.",
        "Because the lifestyle expanded before the income did.",
        "Your bank does not want you to be financially free.",
        "Financial freedom means you stop borrowing.",
        "The product they are selling is the gap between your income and your reset.",
        "The wider the gap, the more interest you pay.",
        "The treadmill is not a metaphor. It is a business model.",
    ]),
    ("THE POPULAR MISREADING", [
        "Everyone who understands this arrives at the same conclusion.",
        "The solution is discipline. Willpower. Spend less.",
        "That is not what happens.",
        "Willpower is a finite resource. It depletes.",
        "A strategy that requires you to constantly resist your own baseline fails the moment your attention is elsewhere.",
        "The people who escape the treadmill do not do it by spending less through force.",
        "They do it by changing what their brain registers as the reference point.",
        "Not by earning more.",
        "By deciding — in advance, automatically — what the baseline will not include.",
    ]),
    ("THE REAL CONCLUSION", [
        "In 1974, the economist Richard Easterlin published a finding that became one of the most discussed in his field.",
        "Across countries, across income levels, across decades — beyond a certain threshold, more money does not produce more wellbeing.",
        "Countries that had grown significantly richer over thirty years showed no significant increase in reported happiness.",
        "He called it the Easterlin Paradox.",
        "The paradox is only a paradox if you believe money accumulates into wellbeing.",
        "It does not. It accumulates into baseline.",
        "Enough is not a number.",
        "Enough is a decision.",
        "The people who feel rich are not the ones with the most money.",
        "They are the ones who stopped moving the finish line.",
        "And they did it before the next raise arrived.",
    ]),
    ("EL MOVIMIENTO", [
        "Here is what you do with this.",
        "Automate ten percent of every payslip before it hits your account. Your baseline never sees it.",
        "Next raise: freeze your lifestyle for one year. Bank the entire difference.",
        "Check your bank statement right now. Cancel one subscription you forgot you had.",
        "Build three months of expenses in a separate account you cannot see daily. That buffer kills more anxiety than any raise.",
        "Raise your pension contribution by one percent this year. Over thirty years, that single percent compounds into more than most bonuses.",
    ]),
    ("THE ENDING", [
        "You cannot stop the reset.",
        "Your brain will always recalibrate.",
        "But you can stop funding the next version of the baseline with money that should be building your future.",
        "The treadmill runs whether you fight it or not.",
        "The question is whether you are putting something aside before you step back on.",
        "Every video on this channel is one way your financial gut has been engineered against you.",
        "This is how they turned your raise into their revenue.",
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

    path = "/home/user/Claudeeee/Treadmill_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
