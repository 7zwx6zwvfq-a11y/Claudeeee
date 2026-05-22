#!/usr/bin/env python3
"""Word script document for Video 5: Why Free Money Is the Most Expensive Money You Own."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "Why Free Money Is the Most Expensive Money You Own"
SUBTITLE = "CRAYON CAPITAL — CLONE SESSION · VIDEO 5"
LABEL = "STATE 5 — SCRIPT (NARRATION)"

SECTIONS = [
    ("", [
        "Think about the last time you received money you didn't expect.",
        "A bonus. A gift. A gambling win. An inheritance. A refund of any kind.",
        "Now think about how long it took you to spend it.",
        "Now think about how long it would take you to save that same amount from your monthly salary.",
        "The gap between those two numbers is not a personality flaw.",
        "It is one of the most studied phenomena in behavioral economics.",
        "It has been replicated in dozens of countries, across every income level, in people who manage other people's money for a living.",
        "And it is being used against you right now.",
    ]),
    ("THE IMPOSSIBILITY", [
        "Here is what makes this strange.",
        "Money is money.",
        "A hundred euros from your salary and a hundred euros from a bonus are identical objects.",
        "They buy the same things. They have the same value. There is no rational reason to treat them differently.",
        "And yet every human being on Earth does.",
        "Not sometimes. Consistently. Predictably. In ways that can be measured, mapped, and — by the right industry — exploited.",
        "This is the story of how that happens. And who built their business model on top of it.",
    ]),
    ("THE DINNER PARTY", [
        "It started not in a laboratory, but at a dinner party.",
        "1975. Richard Thaler, a young economist at the University of Rochester, was hosting colleagues for dinner.",
        "He had put a bowl of cashews on the coffee table as a pre-dinner snack.",
        "His guests were eating them. Too enthusiastically.",
        "Thaler worried they would ruin their appetite before the meal.",
        "So he took the bowl away.",
        "And the room relaxed.",
        "Here is what stopped him cold.",
        "Every person in that room was a trained economist. And every single one of them had just expressed relief at having a free good removed from their presence.",
        "Rational agents don't do that.",
        "If you wanted to stop eating cashews, you stopped. The bowl being there was irrelevant.",
        "Except it wasn't. And everyone in the room knew it.",
        "He wrote that moment in his notes.",
        "He had just watched a room full of rational economists behave irrationally — and feel grateful about it.",
        "He spent the next decade trying to understand why.",
    ]),
    ("THE THEORY", [
        "Mainstream economics had one central assumption: people make decisions based on their total wealth.",
        "Not where the money came from. Not what category it was in. Total wealth.",
        "Thaler kept finding violations.",
        "People would walk twenty minutes to save five euros on a fifteen-euro item — but would not cross the street to save five euros on a five-hundred-euro purchase.",
        "The saving was identical. The effort was identical. The behavior was completely different.",
        "He noticed that people held expensive bottles of wine in their cellars for decades — wine they would never sell for what it was worth and would never pay what it now costs to replace.",
        "They held both positions simultaneously. Rational agents cannot do that.",
        "He was seeing the same thing everywhere. People were not tracking total wealth. They were tracking accounts.",
        "He called it mental accounting.",
        "The economics profession told him he was wasting everyone's time.",
    ]),
    ("THE EXPERIMENTS", [
        "In 1985, Thaler ran the experiment that ended the argument.",
        "You have bought a twenty-euro ticket to see a concert. On the way, you lose the ticket.",
        "Do you buy another?",
        "Most people say no.",
        "Same situation. You are on your way to buy a twenty-euro ticket at the door. On the way, you lose a twenty-euro note from your wallet.",
        "Do you still go?",
        "Most people say yes.",
        "In both cases you have lost twenty euros. In both cases attending costs another twenty. The math is identical.",
        "But in the first case, the concert budget — the mental account — has already been spent.",
        "Paying again feels like paying forty euros for a twenty-euro experience.",
        "In the second case, the twenty euros came from the general cash account. The concert account is untouched.",
        "Same money. Same outcome. Completely different decision.",
        "Thaler ran the same logic through bonuses, gambling wins, inheritances, gifts. Every single time, the same result.",
        "The brain does not process money as money.",
        "It processes money as money-from-here or money-from-there.",
        "And the behavior follows the account, not the amount.",
    ]),
    ("THE MECHANISM", [
        "Here is what is happening inside.",
        "When you earn money through labor — through time, through effort, through sacrifice — it carries a cost signal.",
        "Your nervous system registered what it took to produce it. Every euro spent from that account costs something real and felt.",
        "When money arrives without labor — a bonus, a gift, a gambling win — it does not carry that signal.",
        "The brain files it differently. Money in that account moves faster, easier, with almost no friction.",
        "Thaler called this the pain of paying.",
        "Cash hurts. You feel it leave your hand.",
        "Cards reduce the pain — the money goes later, abstractly, somewhere in the future.",
        "Casino chips reduce it further — they no longer look like money at all.",
        "Contactless payment nearly eliminates it entirely.",
        "Each step away from physical, earned, hard-counted money lowers the pain signal.",
        "Lower pain means higher spending.",
        "The account determines the behavior. Always.",
    ]),
    ("THE POPULAR MISREADING", [
        "Everyone who hears this arrives at the same conclusion.",
        "So some people are just impulsive. Some people lack discipline. Some people cannot manage money.",
        "That is not what the research shows.",
        "Thaler ran these experiments on economists. On financial advisors. On people who managed other people's money professionally.",
        "The mental accounts showed up in all of them.",
        "This is not a character flaw. It is architecture.",
        "Your brain was never designed to treat money as a fungible, interchangeable unit of abstract value.",
        "It was designed to track resources the way a hunter tracks resources — by source, by effort, by context.",
        "A kill you made yourself is worth more than an animal you found already dead. The effort cost something real.",
        "Money is the modern version of the same system.",
        "And the system has been mapped.",
    ]),
    ("THE INDUSTRY", [
        "In the 1980s, casinos discovered something.",
        "When chips look and feel too much like real money, players slow down.",
        "So they engineered the texture. The weight. The color.",
        "The exact sensory point where a chip feels real enough to hold and fake enough to throw across a table.",
        "That is not a design aesthetic. That is applied mental accounting.",
        "The same logic runs every loyalty points program you have ever been enrolled in.",
        "The points feel like a bonus — like money you found rather than money you earned.",
        "So you spend them on upgrades you would never pay cash for. The friction disappears. The margin increases.",
        "The same logic runs the bonus industry.",
        "The same logic runs the consumer credit industry. Not the interest rate. The friction removal.",
        "Every contactless payment, every one-click purchase, every subscription that bills silently in the background is an engineered reduction of the pain of paying.",
        "The account determines the behavior. The behavior determines the profit.",
        "Mental accounting appeared in academic literature in 1985. These industries had working versions of it long before anyone published a paper.",
    ]),
    ("THE REAL CONCLUSION", [
        "Here is what Thaler actually concluded.",
        "Not that humans are broken. That humans are predictable.",
        "The accounts are consistent. The triggers are consistent. The behavior that follows is consistent.",
        "Which means if you can see the accounts, you can audit them.",
        "The bonus that feels like a windfall is compensation. Name it that the moment it arrives.",
        "The loyalty points that feel like free money are the portion of your spending the company returned to you.",
        "The casino chip is fifty euros. Every time you reach for it, translate it back into the number.",
        "Thaler won the Nobel Prize in Economic Sciences in 2017.",
        "He had spent forty years being told he was wasting everyone's time.",
        "It started with a bowl of cashews at a dinner party in 1975.",
        "The insight it produced — that every financial decision you make is shaped not by how much money you have, but by which mental account the money is in — is one of the most replicated findings in the history of economics.",
        "And the industries that want your money understood it before the Nobel committee announced his name.",
    ]),
    ("EL MOVIMIENTO", [
        "Here is what you do with this.",
        "The next time a bonus arrives — before you spend a single euro — set up an automatic transfer to your investment account or emergency fund for that same day.",
        "Not because you need discipline. Because your brain is about to file it as free money. You are faster than the filing.",
        "If your employer offers a pension match and you are not maximizing it — that is not a benefit you are leaving on the table. That is your own compensation that your brain has quietly filed as optional.",
        "Decide now — before the next windfall arrives — what percentage goes to savings or investment. When the money comes, the rule runs. The brain villain never gets to open the folder.",
        "And use the pain of paying deliberately. Automate your savings transfer on the same day you get paid, before the rest moves. When the transfer hurts slightly, the account is real. When it feels like nothing, it does not exist yet.",
    ]),
    ("THE ENDING", [
        "You cannot stop your brain from keeping mental accounts.",
        "The system runs below the threshold of conscious thought. It was there before you knew the word for it.",
        "But you can learn to read the filing.",
        "When money arrives — any money — ask one question before you do anything with it.",
        "Which account is my brain putting this in?",
        "And is that the account I would choose if I were choosing deliberately?",
        "The bonus, the win, the gift, the refund — your brain has already filed them somewhere.",
        "The only question is whether you agree with the filing.",
        "Every video on this channel is one way your financial gut has been hacked.",
        "This is how they got to your windfall before you did.",
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

    path = "/home/user/Claudeeee/Mental_Accounting_SCRIPT.docx"
    doc.save(path)
    print(f"Saved: {path} | {total_beats} beats | {word_count} words")
    return path, total_beats, word_count


if __name__ == "__main__":
    build_docx()
