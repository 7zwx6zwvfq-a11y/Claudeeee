#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

# High resolution then downscale for crisp result
SCALE = 4
SIZE = 150 * SCALE  # 600px, then downscale to 150

img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 210))
draw = ImageDraw.Draw(img)

try:
    font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80 * SCALE // 4)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36 * SCALE // 4)
except:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Red heart centered top
heart = "♥"
bbox = draw.textbbox((0, 0), heart, font=font_big)
w = bbox[2] - bbox[0]
draw.text(((SIZE - w) // 2, SIZE // 8), heart, font=font_big, fill=(220, 40, 40, 255))

# SUBSCRIBE centered bottom
word = "SUBSCRIBE"
bbox2 = draw.textbbox((0, 0), word, font=font_small)
w2 = bbox2[2] - bbox2[0]
draw.text(((SIZE - w2) // 2, SIZE * 58 // 100), word, font=font_small, fill=(255, 255, 255, 255))

# Downscale to 150x150 with antialiasing
out = img.resize((150, 150), Image.LANCZOS)
path = "/home/user/Claudeeee/Neurocents_Watermark.png"
out.save(path)
print(f"Saved: {path}")
