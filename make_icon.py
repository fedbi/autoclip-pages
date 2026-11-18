"""Genera icon.png (1024x1024) para la app de TikTok: un clip vertical con un 'play' y marcas de corte."""
from PIL import Image, ImageDraw

S = 1024
img = Image.new("RGB", (S, S), (18, 18, 24))
d = ImageDraw.Draw(img)

# fondo con degradé diagonal
for y in range(S):
    t = y / S
    d.line([(0, y), (S, y)], fill=(int(30 + 60 * t), int(20 + 10 * t), int(70 + 90 * t)))

# tarjeta vertical 9:16
w, h = 430, 764
x0, y0 = (S - w) // 2, (S - h) // 2
d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=60, fill=(250, 250, 252))

# triángulo de "play"
cx, cy, r = S // 2 + 20, S // 2, 120
d.polygon([(cx - r * 0.8, cy - r), (cx - r * 0.8, cy + r), (cx + r, cy)], fill=(255, 45, 85))

# marcas de corte (inicio y fin del clip)
for yy in (y0 + 110, y0 + h - 110):
    d.rounded_rectangle([x0 + 70, yy - 10, x0 + w - 70, yy + 10], radius=10, fill=(37, 244, 238))

img.save("icon.png", optimize=True)
print("icon.png", img.size)
