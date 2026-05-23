#!/usr/bin/env python3
"""Word script document for Video 6: The Billion-Dollar Bet Your Bank Is Making Against You Right Now."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "The Billion-Dollar Bet Your Bank Is Making Against You Right Now"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 6"
LABEL = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "Think about the last time you changed your pension fund.",
        "Or moved your savings to a higher-interest account.",
        "Or switched banks. Or renegotiated your insurance. Or cancelled a subscription you forgot you had.",
        "Now think about how long you have been meaning to.",
        "That gap — between intending and doing — is not a character flaw.",
        "It is the most reliable source of profit in the financial industry.",
        "It has a name. It has been studied for decades. It has been deliberately engineered into every financial product you own.",
        "And right now, while you are watching this, it is running.",
    ]),
    ("THE IMPOSSIBILITY", [
        "Here is what makes this strange.",
        "You did not choose most of your financial settings.",
        "Your pension allocation. Your savings interest rate. Your overdraft limit. Your insurance renewal price. Your investment fund.",
        "Someone else chose them. Before you arrived. Without asking.",
        "And they chose them for a reason.",
        "Not your reason.",
        "This is the story of the default. The most powerful financial instrument ever built. And the bet that it will work on you forever.",
    ]),
    ("THE CHECKBOX", [
        "In 2003, two researchers published a paper that should have changed how every government on Earth designs policy.",
        "Eric Johnson and Daniel Goldstein were studying organ donation rates across Europe.",
        "The numbers they found made no sense.",
        "Austria: 99.98 percent of the population registered donors.",
        "Germany: 12 percent.",
        "France: 99.91 percent.",
        "Denmark: 4.25 percent.",
        "Same continent. Similar cultures. Similar legal systems. A gap of 95 percentage points.",
        "Johnson and Goldstein looked for the variable. They checked religion. Wealth. Education. Political systems. Healthcare attitudes.",
        "Nothing explained it.",
        "Then they looked at the government form.",
        "In Austria, the form said: you are a donor unless you actively opt out.",
        "In Germany, the form said: check this box if you want to be a donor.",
        "That was it.",
        "Same people. Same values. Same decision available to everyone.",
        "Different default.",
        "In the opt-out countries, 99 percent of people never changed the default.",
        "In the opt-in countries, 85 percent of people never changed the default.",
        "Everyone followed the path of least resistance.",
        "The default was not a suggestion. For almost everyone, in every country, the default was the decision.",
    ]),
    ("THE THEORY", [
        "In 1988, two economists at Harvard — William Samuelson and Richard Zeckhauser — ran a series of experiments.",
        "They gave participants financial choices. Investment portfolios. Insurance plans. Medical treatments.",
        "In every scenario, one option was labeled as the status quo — the current state, already in place.",
        "In every scenario, the status quo option was chosen significantly more often than the alternatives.",
        "Even when the alternatives were objectively, measurably better.",
        "Even when participants acknowledged, out loud, that the alternative was better — they still chose the status quo.",
        "They called it status quo bias.",
        "The bias was not small. It was not occasional. It was consistent across every demographic, every income level, every level of financial education.",
        "Including people who managed money professionally.",
        "The default wins. Not sometimes. Almost always.",
    ]),
    ("THE EXPERIMENTS", [
        "The most consequential experiment about defaults was not run in a psychology lab.",
        "It was run inside a corporation.",
        "2001. Two economists — Brigitte Madrian and Dennis Shea — studied a large American company that changed how it enrolled employees in its retirement plan.",
        "Before the change: employees had to actively sign up. Opt in. Take an action.",
        "Enrollment: 49 percent.",
        "The company changed one thing. Employees were now automatically enrolled. They could opt out at any time. Nothing else changed.",
        "Same salary. Same employer match. Same tax benefits. Same plan.",
        "Enrollment: 86 percent.",
        "A 37 percentage point jump. From one change. To one form. To which option required action.",
        "But here is the part that stopped the researchers.",
        "The employees who were auto-enrolled did not change their contribution rate or fund selection once enrolled.",
        "They stayed in whatever the default was. The percentage the company chose. The fund the company selected.",
        "The default did not just decide whether they enrolled.",
        "The default decided how they invested.",
        "For years.",
    ]),
    ("THE MECHANISM", [
        "Here is what is happening inside.",
        "Every decision has a cost.",
        "Not a financial cost. A cognitive cost.",
        "To change anything — your bank, your fund, your insurance — you have to compare options, evaluate risk, accept the possibility of choosing wrong, and take an action.",
        "That process is expensive. Not in money. In mental energy.",
        "The default costs nothing. It is already done. It requires no comparison, no evaluation, no risk of regret.",
        "Your brain runs a constant, automatic calculation: is the effort of changing worth the uncertain benefit of what I might get?",
        "Most of the time, the answer is no. Not because the benefit is not real. Because the calculation itself is hard.",
        "Psychologists call this the omission bias. Inaction feels safer than action — even when the outcomes are identical.",
        "And there is something underneath that.",
        "Changing something you already have means risking what you have for something you do not have yet.",
        "Your brain treats that asymmetrically. Always.",
        "This is not a rational calculation. It is architecture.",
        "And every financial institution in the world has had decades to study it.",
    ]),
    ("THE POPULAR MISREADING", [
        "Everyone who hears about status quo bias arrives at the same conclusion.",
        "Some people are just passive. Some people do not take their finances seriously. Some people need to try harder.",
        "That is not what the research shows.",
        "Madrian and Shea found the same patterns in companies full of highly educated, high-income professionals.",
        "Johnson and Goldstein found no relationship between donation rates and financial literacy or civic engagement.",
        "Samuelson and Zeckhauser ran their experiments on economists.",
        "The status quo bias showed up in all of them.",
        "This is not a character flaw. It is architecture.",
        "Your brain was not designed to actively re-evaluate every standing arrangement in your life on a recurring basis.",
        "It was designed to conserve energy by treating existing states as safe and change as risky.",
        "That was a good design. For most of human history, the existing state usually was safe.",
        "The financial industry discovered what happens when you build products around that design.",
    ]),
    ("THE INDUSTRY", [
        "In the 1990s, the retail banking industry discovered something.",
        "Customers who never switched accounts were worth significantly more than customers who actively managed their finances.",
        "Not because they had more money. Because they asked for less.",
        "Today, the average savings account at a major bank pays 0.1 percent interest.",
        "The central bank base rate: 5.25 percent.",
        "The bank is borrowing your money at 0.1 percent and deploying it at 5 percent.",
        "The difference is not a fee. It is not a charge. It is not disclosed anywhere in large print.",
        "It is just the default. And the bank knows, with statistical certainty, that most customers will never change it.",
        "The bet is not that you are unaware. The bet is that awareness alone is not enough to make you act.",
        "They are right. Studies show that even customers who know they are on a poor-rate account do not switch.",
        "The pension fund industry runs the same calculation.",
        "The average actively managed pension fund charges 1.5 percent per year in fees.",
        "A global index fund tracking the same market charges 0.07 percent.",
        "Over a 30-year working life, that difference in fees compounds into tens of thousands of euros less at retirement.",
        "The default fund is almost never the cheapest fund.",
        "It is the fund the provider chose to place there. And 86 percent of enrolled employees never change it.",
        "The insurance industry discovered auto-renewal.",
        "Every year, your premium increases slightly. The letter arrives. The language is dense. The deadline is short.",
        "The path of least resistance is to do nothing. The policy renews. The higher premium clears.",
        "Across the industry, auto-renewal customers pay an average of 30 percent more than customers who actively switch.",
        "The product being sold is not insurance. The product being sold is your inertia.",
    ]),
    ("THE REAL CONCLUSION", [
        "Richard Thaler — the same economist from the last video — had spent years watching institutions exploit defaults against the people they were supposed to serve.",
        "In 2008, he and legal scholar Cass Sunstein published a book called Nudge.",
        "The central argument: if defaults are inevitable — and they are — they should be designed for the person, not for the institution.",
        "They called it libertarian paternalism. You remain free to choose anything. But the default is set in your favor.",
        "The United Kingdom used it. In 2012, the government mandated automatic pension enrollment for all employed workers.",
        "Participation went from 55 percent to 85 percent in two years.",
        "No campaigns. No education programs. No incentives beyond the enrollment itself.",
        "One change: which option required action.",
        "Thaler won the Nobel Prize in Economic Sciences in 2017.",
        "The insight that earned it: the most powerful financial intervention is not advice. It is not education. It is not willpower.",
        "It is the setting.",
        "And the setting can work for you. Or against you.",
        "For most people, right now, it is working against them.",
    ]),
    ("EL MOVIMIENTO", [
        "Here is what you do with this.",
        "Open your pension account today — not this week, today — and find the default fund. Look at the annual management charge. If it is above 0.3 percent, you are paying for the default, not for performance. Switch to the lowest-cost index fund available in your plan.",
        "Find your savings account interest rate. If it is more than one percent below the central bank base rate, you are gifting money to the bank every month. A high-yield savings account at a challenger bank takes twenty minutes to open. That twenty minutes, compounded over five years, is worth more than most people expect.",
        "Check every insurance policy you hold for auto-renewal clauses. Set a calendar reminder thirty days before each renewal date. The reminder is the system. You do not need willpower. You need the reminder in the calendar.",
        "Now use the default against itself. Set up an automatic investment transfer on the same day your salary arrives — before you see the money, before the spending begins. You are not fighting the system. You are becoming the default.",
        "And find one subscription you have not actively chosen to keep in the last six months. Cancel it today. Not because the amount is large. Because the act of auditing your defaults — once — trains the behavior that the financial industry has spent decades trying to prevent.",
    ]),
    ("THE ENDING", [
        "You cannot stop institutions from setting defaults.",
        "Every financial product you will ever own arrives with settings someone else chose.",
        "The pension. The savings account. The insurance. The investment fund. The bank itself.",
        "All of it came with a default. And the default was not chosen for you.",
        "But you can read the settings.",
        "Once a year. Thirty minutes. One question per account.",
        "Is this the setting I would choose if I were choosing deliberately?",
        "The bank made a billion-dollar bet that you would never ask that question.",
        "The bet is still running.",
        "Every video on this channel is one way your financial gut has been hacked.",
        "This is how they turned your inaction into their income.",
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

    path = "/home/user/Claudeeee/Status_Quo_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
