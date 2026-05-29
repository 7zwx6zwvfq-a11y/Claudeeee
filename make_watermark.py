#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

SIZE = 150
img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 220))
draw = ImageDraw.Draw(img)

# Red heart
heart = "♥"
try:
    font_heart = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
    font_sub   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
except:
    font_heart = ImageFont.load_default()
    font_sub   = ImageFont.load_default()

# Draw heart
hx, hy = 30, 30
draw.text((hx, hy), heart, font=font_heart, fill=(220, 40, 40, 255))

# Draw SUBSCRIBE
draw.text((18, 75), "SUB", font=font_sub, fill=(255, 255, 255, 255))
draw.text((8, 105), "SCRIBE", font=font_sub, fill=(255, 255, 255, 255))

path = "/home/user/Claudeeee/Neurocents_Watermark.png"
img.save(path)
print(f"Saved: {path}")
