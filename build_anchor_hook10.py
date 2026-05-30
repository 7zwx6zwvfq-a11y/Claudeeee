#!/usr/bin/env python3
"""V9 — First 8 Beats Rewritten for 10/10 Hook (0-30 seconds)."""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

BEATS_HOOK = [
    {
        "beat": 1,
        "time": "0-2s",
        "narration": "You just lost $200,000. And you thought you won.",
        "image": (
            "Dark charcoal background (#1A1A1A). Single dramatic overhead spotlight center frame. "
            "JAKE stands frozen holding an offer letter — '$42,000' circled in green, expression of pride. "
            "Above him in the dark: a massive '$200,000' in faded red slowly materializing like a ghost. "
            "Brain villain inside skull stares directly at camera with a slow wide smug grin. "
            "Label bottom: 'YOU THOUGHT YOU WON.' 16:9, 1280x720."
        ),
        "camera": "Medium, slight low angle. Brain locked on viewer.",
        "lighting": "Dark background, single spotlight on Jake. Red glow on the $200,000 figure above.",
        "mood": "Menacing revelation. Viewer feels something is wrong before understanding why.",
        "action": "The $200,000 figure materializes slowly. Brain villain turns gaze from Jake to camera.",
        "video": "3s. $200,000 fades in above Jake while he smiles unaware. Brain makes eye contact with viewer. Slow zoom toward brain's expression.",
    },
    {
        "beat": 2,
        "time": "2-4s",
        "narration": "The number they gave you first was not an offer. It was a trap.",
        "image": (
            "Dark background. Close-up on HR document sliding across a desk — bold number '$38,000' "
            "underlit with cold red glow. A cartoon hand (brain villain's) pushes it across. "
            "Label burned into the paper: 'THE TRAP.' No faces visible. Just the number and the hand. "
            "16:9, 1280x720."
        ),
        "camera": "Extreme close-up, top-down on document and hand.",
        "lighting": "Cold red underlighting on the document. Dark surrounding.",
        "mood": "Sinister reveal. The mechanism exposed before it is explained.",
        "action": "Paper slides slowly into frame. Label 'THE TRAP' appears letter by letter.",
        "video": "2s. Slow slide of document into frame. Label burns in last.",
    },
    {
        "beat": 3,
        "time": "4-7s",
        "narration": "You pushed back. You got $42,000. You felt like you won.",
        "image": (
            "Split screen. LEFT — '$38,000' crossed out in red. RIGHT — '$42,000' circled in green. "
            "JAKE's brain celebrates on the right side, doing a small fist pump. "
            "Background still dark — the celebration feels hollow. Label: '+$4,000 YOU WON.' 16:9, 1280x720."
        ),
        "camera": "Wide split panel, centered.",
        "lighting": "Green glow right side, red glow left side. Dark overall.",
        "mood": "False victory. The celebration is real. The win is not.",
        "action": "Green circle pulses. Brain fist pumps. Dark background never lets the mood fully lift.",
        "video": "3s. Green circle pulses twice. Brain celebrates against dark background.",
    },
    {
        "beat": 4,
        "time": "7-9s",
        "narration": "The salary band for that role was $48,000 to $62,000.",
        "image": (
            "Dark background. HR internal document slams into frame — stamped 'CONFIDENTIAL' at top. "
            "Bold text: 'SALARY BAND: $48,000 — $62,000' in green. "
            "Jake's $42,000 marked with red arrow pointing DOWN — below even the floor of the band. "
            "Jake blurred in background still celebrating, unaware. 16:9, 1280x720."
        ),
        "camera": "Document foreground full frame. Jake blurred behind.",
        "lighting": "Cold institutional light on document. Jake in warm celebration light behind.",
        "mood": "Devastating. The gap is visceral. The contrast between Jake's joy and the truth is brutal.",
        "action": "Document slams in from top. Red arrow drops to Jake's number. Jake keeps celebrating, oblivious.",
        "video": "2s. Document impact drop from top. Arrow drops with weight.",
    },
    {
        "beat": 5,
        "time": "9-12s",
        "narration": "You never knew. Because the first number they showed you made sure of it.",
        "image": (
            "Close-up on JAKE's face — the moment he sees the document. "
            "Brain inside skull visibly short-circuits: eyes wide, jaw loose, hand pressed to glass skull. "
            "The '$38,000' from the original offer glows behind him like a ghost — "
            "anchor chain extending from that number down to Jake's ankle, pulling him below the salary band. "
            "Label: 'THE ANCHOR.' 16:9, 1280x720."
        ),
        "camera": "Close-up, Jake's reaction. Anchor chain visible in background.",
        "lighting": "Cold blue on the chain. Warm spotlight on Jake's face.",
        "mood": "The mechanism clicks into place. Understanding arrives.",
        "action": "Chain appears connecting '$38,000' to Jake's ankle. Brain reacts. Number glows.",
        "video": "3s. Chain materializes from the number to Jake's ankle. Brain reaction plays out.",
    },
    {
        "beat": 6,
        "time": "12-15s",
        "narration": "The $4,000 you won was measured against a number they chose. Not yours.",
        "image": (
            "Dark background. Giant balance scale center frame. "
            "LEFT: '$4,000 YOU WON' — tiny green coin glowing with Jake's celebration energy. "
            "RIGHT: heavy black anchor bolt labeled 'THEIR NUMBER' — crushing the scale down. "
            "Brain villain stands beside scale, one hand resting on the anchor, completely relaxed. "
            "The imbalance is extreme and visual. 16:9, 1280x720."
        ),
        "camera": "Wide, scale centered, slight low angle.",
        "lighting": "Green glow left. Red-dark glow right on the anchor.",
        "mood": "The win reframed as a loss. Visceral imbalance.",
        "action": "Scale slams down on anchor side. Brain villain taps anchor with one finger — effortless.",
        "video": "3s. Scale tips with impact. Brain's tap is casual and devastating.",
    },
    {
        "beat": 7,
        "time": "15-17s",
        "narration": "The real band was $48,000 to $62,000. You never got close.",
        "image": (
            "Dark background. Same scale — now shows full salary band '$48,000 — $62,000' glowing green. "
            "Jake's $42,000 marked with red X below even the floor of the band. "
            "Bold red gap arrow shows the distance between Jake's result and what the role was worth. "
            "Label: 'THE REAL GAP.' Brain villain shakes head slowly. 16:9, 1280x720."
        ),
        "camera": "Wide, scale with gap measurement prominent.",
        "lighting": "Green band glow above. Red gap arrow below.",
        "mood": "The full extent of the damage visible for the first time.",
        "action": "Green band drops in from above. Red gap arrow measures down to $42k. Brain shakes head.",
        "video": "2s. Band drops. Gap arrow measures down. Brain shakes head almost sympathetically.",
    },
    {
        "beat": 8,
        "time": "17-20s",
        "narration": "That anchor follows you. Every raise, every promotion, every job after.",
        "image": (
            "Dark background. JAKE walking forward — anchor chain attached to ankle dragging behind him, "
            "connected to the original '$38,000' number. Ahead: three doors labeled 'RAISE,' 'PROMOTION,' "
            "'NEXT JOB.' Each door slightly lower than it should be — warped downward by the chain's weight. "
            "Label above: 'COMPOUNDING.' 16:9, 1280x720."
        ),
        "camera": "Wide side view. Jake walking right, chain dragging left.",
        "lighting": "Warm light ahead on the doors. Cold dark behind where the chain comes from.",
        "mood": "The mechanism fully revealed. Stakes fully established.",
        "action": "Jake walks forward. Chain drags. Doors visibly pulled lower by the anchor's gravity.",
        "video": "3s. Jake walks. Chain pulls. Doors warp downward under the anchor's weight.",
    },
]

def build_doc():
    doc = Document()

    # Title
    title = doc.add_heading("V9 — HOOK REMASTERED · BEATS 1–8 · 10/10", level=1)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in title.runs:
        run.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

    sub = doc.add_paragraph("Anchoring Bias / Salary Negotiation · First 30 seconds · Dark dramatic opening")
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].font.size = Pt(9)
    sub.runs[0].font.color.rgb = RGBColor(0x77, 0x77, 0x77)

    doc.add_paragraph()

    for b in BEATS_HOOK:
        # Beat header
        hdr = doc.add_paragraph()
        hdr.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = hdr.add_run(f"BEAT {b['beat']}  ·  {b['time']}")
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xB0, 0x2A, 0x2A)

        # Narration
        p = doc.add_paragraph()
        p.add_run("NARRATION  ").bold = True
        p.add_run(b["narration"]).font.size = Pt(10)

        # Image
        p2 = doc.add_paragraph()
        p2.add_run("IMAGE  ").bold = True
        p2.add_run(b["image"]).font.size = Pt(8)

        # Camera / Lighting / Mood / Action / Video in a compact block
        for label, key in [("CAMERA", "camera"), ("LIGHTING", "lighting"),
                           ("MOOD", "mood"), ("ACTION", "action"), ("VIDEO", "video")]:
            p3 = doc.add_paragraph()
            p3.add_run(f"{label}  ").bold = True
            p3.add_run(b[key]).font.size = Pt(8)

        doc.add_paragraph("─" * 80)

    path = "/home/user/Claudeeee/Anchor_Hook10_Beats1-8.docx"
    doc.save(path)
    print(f"Saved: {path}")

build_doc()
