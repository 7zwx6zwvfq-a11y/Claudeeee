#!/usr/bin/env python3
"""Word script document for Video 9: The First Number They Show You in a Job Interview Is Not an Offer."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE    = "The First Number They Show You in a Job Interview Is Not an Offer"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 9"
LABEL    = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "You walked out of that interview feeling like you won.",
        "You negotiated. They started at $38,000. You pushed back. They came up to $42,000.",
        "Four thousand dollars more than they offered. You did better than most people.",
        "The salary band for that role was $48,000 to $62,000.",
        "You never knew.",
        "The $4,000 you won was measured against a number they chose.",
        "Not against what the role was worth. Against the anchor they set.",
        "That anchor — and everything that compounded from it — is what this video is about.",
    ]),
    ("THE INTERVIEW", [
        "His name is Jake. He is twenty-four years old and this is his first real interview.",
        "He has prepared. He knows the company. He knows the role. He is ready.",
        "The HR manager smiles and slides a paper across the desk.",
        "The number on it is $36,000.",
        "'We think this reflects your experience level,' she says. 'There is room to grow.'",
        "Jake feels the pull immediately. His current salary is $31,000. This is a sixteen percent raise.",
        "He counters. She says she can go to $39,000. Jake accepts.",
        "He drives home feeling like he won the negotiation.",
        "The salary band for that role was $40,000 to $55,000.",
        "He would not learn this for eleven years.",
    ]),
    ("THE MECHANISM", [
        "Here is what happened in that room.",
        "Before Jake saw the number, he had no anchor.",
        "His brain was open. The market rate, the role value, his own worth — all of it was floating, undefined.",
        "The moment $36,000 appeared on that paper, his brain locked onto it.",
        "Not as a starting point. As a reference.",
        "Every number after that was evaluated in relation to it.",
        "$39,000 felt like a win because it was $3,000 more than $36,000.",
        "Not because $39,000 was a fair price for the work. Because it was higher than the anchor.",
        "This is called anchoring bias.",
        "The first number introduced in any negotiation becomes the gravitational center of everything that follows.",
        "It does not matter if that number is arbitrary, low, or specifically designed to limit you.",
        "Your brain treats it as the starting truth.",
        "And it recalculates everything — including your sense of victory — relative to it.",
    ]),
    ("THE MULTIPLICATION", [
        "Now meet Marcus. Same company, same role, same week.",
        "Before the interview, Marcus spent two hours on salary research. Market rate: $47,000 to $54,000.",
        "When the HR manager slid the paper across the desk showing $36,000, Marcus paused.",
        "'I've seen the market range for this role at $47,000 to $54,000. I was expecting something in that range.'",
        "Silence.",
        "The HR manager left the room. Came back ten minutes later. $46,000.",
        "Marcus countered at $50,000. They settled at $48,000.",
        "Same company. Same role. Same week. Same starting point.",
        "Jake: $39,000. Marcus: $48,000.",
        "A difference of $9,000.",
        "Jake thought the gap was the negotiation. It was not.",
        "The gap was the anchor.",
    ]),
    ("THE COMPOUND GAP", [
        "Here is what $9,000 becomes.",
        "Both receive three percent raises every year. The percentage is identical. The base is not.",
        "Year five: Jake earns $45,200. Marcus earns $55,600.",
        "Year ten: Jake earns $52,400. Marcus earns $64,500.",
        "Year twenty: Jake earns $70,400. Marcus earns $86,600.",
        "The gap does not stay at $9,000. It grows every year because raises are percentages.",
        "A three percent raise on $39,000 is $1,170. A three percent raise on $48,000 is $1,440.",
        "The person who earns more always earns more from every raise.",
        "Add pension contributions — both putting in five percent of salary — and the pension gap at year thirty exceeds $80,000.",
        "Total lifetime earnings difference: over $300,000.",
        "For a single conversation Jake did not know he was allowed to have.",
    ]),
    ("THE INDUSTRY", [
        "HR departments do not guess at salary numbers.",
        "Every role has a band. A floor and a ceiling, set before the interview begins.",
        "The number they show you first is rarely the midpoint of that band.",
        "It is calibrated to anchor low — close enough to what they know you currently earn, high enough that it feels like an upgrade.",
        "The question 'what are you currently earning?' is not curiosity. It is data collection.",
        "It tells them exactly where to place the anchor.",
        "If you earn $31,000, they show you $36,000. You feel the sixteen percent gain. You stop thinking about the ceiling.",
        "If you earned $45,000, they would have shown you $48,000. Same mechanism. Different number.",
        "The band never changes. Only the anchor does.",
        "In several US states and many countries, asking for your current salary in a job interview is now illegal.",
        "Not because it is rude. Because legislators understood what it was being used for.",
        "The industry fought those laws.",
    ]),
    ("THE POPULAR MISREADING", [
        "Everyone who understands this arrives at the same conclusion.",
        "The solution is to negotiate harder.",
        "That is the wrong answer.",
        "Negotiating harder moves you up within the anchor's range.",
        "It does not escape the anchor.",
        "Jake negotiated. He went from $36,000 to $39,000.",
        "He negotiated well. He just negotiated inside a frame he had already accepted.",
        "The anchor is not set during the negotiation. It is set before it.",
    ]),
    ("THE REAL CONCLUSION", [
        "The first number is not the offer.",
        "It is the frame inside which the offer will happen.",
        "Everything you negotiate after that — every counter, every pushback, every silence — is evaluated by your brain relative to a number that was chosen specifically to limit you.",
        "Marcus did not negotiate better than Jake.",
        "Marcus refused the frame.",
        "He walked in with his own number, placed it on the table before their anchor could land, and made their first move irrelevant.",
        "That is the only negotiation that actually changes the outcome.",
        "Not pushing back harder on their number.",
        "Replacing it with yours before they get to speak first.",
    ]),
    ("EL MOVIMIENTO", [
        "Here is what you do with this.",
        "Never give a number first. When asked your expectations, name a number before they do — research the market rate and anchor above the midpoint.",
        "If they ask your current salary, you do not have to answer. In many places they cannot legally ask. Say: 'I prefer to focus on the market rate for this role.'",
        "Before every interview, spend one hour on salary research. Glassdoor, LinkedIn Salary, industry reports. That number — not theirs — is your anchor.",
        "When they show you a number, pause five seconds before responding. That pause is not awkward. It is the moment your brain resets from their anchor to yours.",
        "Renegotiate internally every eighteen months. Salary compression is real — your newest colleague may be earning more than you for identical work.",
    ]),
    ("THE ENDING", [
        "Jake is fifty-two years old.",
        "He has been promoted. He is good at his job. His colleagues respect him.",
        "He earns $70,000.",
        "His colleague who joined the same week, in the same role, earns $86,000.",
        "Jake has never known this.",
        "He did not lose at fifty-two.",
        "He lost at twenty-four, in a room he thought he had won, against a number he thought was the starting point.",
        "The first number they show you is not an offer.",
        "It is a decision about how much of the value you create they intend to keep.",
        "Every video on this channel is one way your financial gut has been engineered against you.",
        "This is how they turned your anchor into their margin.",
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

    path = "/home/user/Claudeeee/Anchor_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
