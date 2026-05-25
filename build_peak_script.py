#!/usr/bin/env python3
"""Word script document for Video 7: Someone Needs You to Buy at the Top. Here's Who."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "Someone Needs You to Buy at the Top. Here's Who."
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 7"
LABEL = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "At some point in the last five years, you heard about something that felt like the financial opportunity of a lifetime.",
        "Maybe it was a stock. A cryptocurrency. A sector. A company everyone was suddenly talking about.",
        "You felt it. The pull.",
        "Something between excitement and urgency. A voice that said: if you don't move now, you will miss it.",
        "Some of you moved. Some of you watched it rise and wished you had.",
        "Either way, you felt it.",
        "That feeling has a name. It has a mechanism. And it has a beneficiary.",
        "The beneficiary was never you.",
    ]),
    ("THE SHOESHINE BOY", [
        "October 1929. Boston.",
        "Joseph Kennedy — businessman, investor, one of the wealthiest men in America — is having his shoes shined.",
        "The shoeshine boy, while working, begins giving him stock tips.",
        "Which stocks to buy. Which sectors are moving. Which names everyone is talking about.",
        "Kennedy listened.",
        "He said nothing.",
        "He walked back to his office and sold everything he owned in the stock market.",
        "Every position. Every holding. Complete liquidation.",
        "Three weeks later, the market collapsed.",
        "Black Thursday. Black Monday. The beginning of the Great Depression.",
        "While thousands of investors — many of them far more sophisticated than a shoeshine boy's clients — lost everything, Kennedy's fortune was intact.",
        "He was asked, later, what made him sell.",
        "His answer was simple.",
        "When the shoeshine boy knows which stocks to buy, it is too late to be in the market.",
        "Kennedy had no name for what he understood.",
        "The name came decades later.",
    ]),
    ("WHAT KENNEDY UNDERSTOOD", [
        "Here is what Kennedy saw that morning.",
        "Information about an investment travels in a specific order.",
        "First: the people closest to the asset. The founders, the early backers, the insiders.",
        "Then: institutional investors. The funds, the banks, the professional money.",
        "Then: financial media. The stories appear. The coverage builds.",
        "Then: mainstream culture. The dinner table. The taxi driver. The shoeshine boy.",
        "By the time information reaches the last group — the group furthest from the source — the first group has been holding for months.",
        "The first group needs to sell.",
        "To sell, they need buyers.",
        "The buyers are the people who just found out.",
        "Kennedy was not smarter than the market.",
        "He understood something simpler: by the time you hear about it at the shoeshine stand, the people who knew first have been waiting for you.",
    ]),
    ("THE MECHANISM", [
        "Here is what is happening inside your brain.",
        "Your brain does not calculate probability mathematically.",
        "It estimates probability by how easily it can recall examples.",
        "When something is in every conversation, every feed, every headline — your brain registers: this is everywhere. This must be important. This must be working.",
        "Psychologists call this the availability heuristic.",
        "The more easily you can recall something, the more probable your brain judges it to be.",
        "And nothing makes information more available than mass media coverage.",
        "Here is the problem.",
        "Media coverage of an investment peaks at the same moment as its price.",
        "The week you hear about it the most is the week it costs the most.",
        "Your brain reads the signal and says: opportunity.",
        "The signal actually says: exit.",
        "The early money is leaving.",
        "And they needed your attention — your brain's availability calculation — to make the exit possible.",
    ]),
    ("THE SAME PATTERN, 400 YEARS", [
        "Kennedy saw it in 1929. But the pattern is older than Kennedy.",
        "1637. The Dutch Republic. Tulip bulbs were trading at ten times the annual wage of a skilled craftsman.",
        "People mortgaged their homes for flowers.",
        "When the tulip had become the topic of conversation at every tavern in Amsterdam — when everyone knew the names of the most valuable varieties — the collapse came within weeks.",
        "1720. The South Sea Company. A British trading firm with vague promises of profit from South American trade.",
        "Members of parliament bought in. Then their families. Then the servants.",
        "When the servants were buying, the company directors were selling.",
        "2000. Dot-com. Companies with no product, no revenue, and no customers were valued at billions.",
        "When your parents started asking if they should buy internet stocks, the Nasdaq was six weeks from its all-time high.",
        "2021. A cryptocurrency featuring a dog — created as a joke — reached a market capitalisation of eighty billion dollars.",
        "It got there the week it became a meme. The week everyone had heard of it.",
        "The assets change. The technology changes. The narrative changes.",
        "The mechanism does not.",
        "Kennedy understood it with a shoeshine brush. You now have the name for it.",
    ]),
    ("THE POPULAR MISREADING", [
        "Everyone who hears this arrives at the same conclusion.",
        "The solution is to be smarter. To see through the hype. To have better judgment than the average investor.",
        "That is not what the research shows.",
        "In study after study, professional fund managers — people whose entire career is identifying good investments before others do — show the same pattern of entering late-stage narratives.",
        "Not because they are unsophisticated.",
        "Because the availability heuristic does not discriminate between amateur and expert.",
        "When information is everywhere, the brain of a portfolio manager and the brain of a first-time investor run the same calculation.",
        "The feeling of certainty that comes from ubiquitous information is neurologically indistinguishable from the feeling of certainty that comes from good analysis.",
        "Your brain cannot tell the difference between knowing something and having heard it everywhere.",
        "Kennedy was not smarter. He was further from the noise.",
    ]),
    ("THE INDUSTRY", [
        "Financial media does not make money from your returns.",
        "It makes money from your attention.",
        "Attention is maximised by urgency. By excitement. By the feeling that something important is happening right now.",
        "The content that generates the most engagement is the content about things that are moving.",
        "Things that are moving are things already in motion.",
        "Things already in motion are things you are already late to.",
        "A financial influencer with a million followers has incentives that are structurally misaligned with yours.",
        "Their income comes from engagement — views, clicks, shares.",
        "An asset that is rising generates engagement.",
        "An asset that is rising and that their audience is not yet in generates more.",
        "The content that performs best for the creator is precisely the content that gets you in at the point that maximises someone else's exit.",
        "This is not always intentional. It is structural.",
        "The financial attention economy is perfectly calibrated to deliver you to the market at the worst possible moment.",
    ]),
    ("THE REAL CONCLUSION", [
        "In 1996, economist Robert Shiller published research that reframed how we understand financial manias.",
        "Markets, he argued, do not move on fundamentals alone. They move on narratives.",
        "Stories spread like viruses — from insider to institution to media to dinner table — and they inflate prices as they travel.",
        "The further the narrative spreads, the higher the price.",
        "The further the narrative spreads, the closer you are to the end.",
        "He called it narrative economics.",
        "Shiller won the Nobel Prize in Economic Sciences in 2013.",
        "His insight: the shoeshine boy was not a quirk of 1929. He is a structural feature of every financial mania.",
        "The moment the narrative becomes universal is the moment its function changes.",
        "It stops being a story about opportunity.",
        "It becomes a mechanism of exit.",
        "You were not late.",
        "You were targeted.",
    ]),
    ("EL MOVIMIENTO", [
        "Here is what you do with this.",
        "Before you buy anything you first heard about in the last thirty days — from news, from social media, from any conversation — ask one question: when did the early money go in? Search the price chart for the twelve months before the coverage you are seeing now. If prices were already up significantly before the story reached you, you are standing at the shoeshine stand.",
        "Set a rule: minimum seventy-two hours between first hearing about an investment and making any decision. That window is where your prefrontal cortex catches up to the availability signal your brain has already processed as certainty.",
        "Use coverage volume as a contrarian signal. The investment nobody in your network is discussing is not the one with no future. It is the one where the narrative has not yet finished travelling. You are closer to the beginning, not the end.",
        "Automate your core investment in a low-cost index fund so that every week you spend not chasing narratives, your money is already compounding in something no story can inflate or destroy.",
        "And find one financial media source you consume regularly and stop consuming it for thirty days. Not because it is lying. Because its incentive structure is not aligned with your portfolio. Every week without that input is a week your availability heuristic runs on less manufactured urgency.",
    ]),
    ("THE ENDING", [
        "You cannot stop the narratives from forming.",
        "Every generation will have its shoeshine boy moment.",
        "The story changes. The mechanism does not.",
        "But you can learn to read where in the cycle the story is.",
        "When it reaches you — when everyone you know is talking about it, when it feels urgent and obvious and inevitable — that is information.",
        "Not the information the coverage is trying to give you.",
        "The information about where you are standing in the cycle.",
        "Someone needed you to buy at the top.",
        "Now you know who.",
        "Every video on this channel is one way your financial gut has been hacked.",
        "This is how they turned your attention into their exit.",
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

    path = "/home/user/Claudeeee/Peak_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
