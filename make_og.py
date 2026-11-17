#!/usr/bin/env python3
"""og.png 1200x630 — Restaurant Fleur (2x supersample).
Letterhead share art: ivory paper, double hairline gold frame, gold fleur-de-lis
(bezier-built), bordeaux eyebrow, Georgia-bold masthead, address line.
Shop identity only — no builder markers."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

PAPER = (251, 247, 239); PAPER2 = (241, 234, 219)
INK = (32, 28, 35); INK2 = (58, 51, 60)
WINE = (122, 46, 63); GOLD = (168, 138, 84); GOLD_D = (143, 116, 67); LINE = (217, 207, 188)

def font(paths, size):
    bases = ["/System/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size * S)
                except Exception: pass
    return ImageFont.load_default()

geob = lambda s: font(["Georgia Bold.ttf", "Georgia.ttf"], s)
geo  = lambda s: font(["Georgia.ttf"], s)

img = Image.new("RGB", (W * S, H * S), PAPER)
d = ImageDraw.Draw(img)
px = lambda x, y: (int(x * S), int(y * S))

def tracked(cx, y, text, fnt, fill, sp):
    widths = [d.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + sp * (len(text) - 1)
    x = cx * S - total / 2
    for ch, w in zip(text, widths):
        d.text((x, y * S), ch, font=fnt, fill=fill)
        x += w + sp

def bez_chain(segs):
    pts = []
    for (x0, y0, c1, c2, (x3, y3)) in segs:
        n = 36
        for i in range(n + 1):
            t = i / n
            mt = 1 - t
            x = mt**3 * x0 + 3 * mt**2 * t * c1[0] + 3 * mt * t**2 * c2[0] + t**3 * x3
            y = mt**3 * y0 + 3 * mt**2 * t * c1[1] + 3 * mt * t**2 * c2[1] + t**3 * y3
            pts.append((x, y))
    return pts

def fleur(cx, cy, size, fill):
    s = size / 24.0
    def T(p): return (cx + (p[0] - 12) * s * S, cy + (p[1] - 12) * s * S)
    def mir(segs):
        out = []
        for (x0, y0, c1, c2, e) in segs:
            out.append((24 - x0, y0, (24 - c1[0], c1[1]), (24 - c2[0], c2[1]), (24 - e[0], e[1])))
        return out[::-1]
    center = [(12, 1.4, (13.4, 4.4), (14.9, 7.1), (14.9, 9.7)),
              (14.9, 9.7, (14.9, 11.4), (13.6, 12.7), (12, 12.7)),
              (12, 12.7, (10.4, 12.7), (9.1, 11.4), (9.1, 9.7)),
              (9.1, 9.7, (9.1, 7.1), (10.6, 4.4), (12, 1.4))]
    lobe = [(9.1, 6.2, (6.4, 6.9), (4.4, 9.0), (4.1, 11.6)),
            (4.1, 11.6, (4.05, 13.5), (5.4, 14.9), (7.2, 14.9)),
            (7.2, 14.9, (8.8, 14.9), (10.0, 14.0), (10.5, 12.5))]
    stem = [(12, 16, (12, 18.3), (10.7, 20.0), (8.7, 21.0)),
            (8.7, 21.0, (11.1, 21.3), (12, 22.1), (12, 22.7)),
            (12, 22.7, (12, 22.1), (12.9, 21.3), (15.3, 21.0)),
            (15.3, 21.0, (13.3, 20.0), (12, 18.3), (12, 16))]
    for segs in (center, lobe, mir(lobe), stem):
        d.polygon([T(p) for p in bez_chain(segs)], fill=fill)
    d.rounded_rectangle([T((4.6, 14.3)), T((19.4, 16.0))], radius=0.85 * s * S, fill=fill)

# double hairline frame
d.rectangle([px(26, 26), px(1174, 604)], outline=GOLD, width=3 * S)
d.rectangle([px(36, 36), px(1164, 594)], outline=GOLD_D, width=1 * S)

fleur(600, 128, 150, GOLD)

tracked(600, 232, "OPENING SOON · DOWNTOWN LITTLE ROCK", geo(21), WINE, 5.2 * S)

mast = geob(76)
bb = d.textbbox((0, 0), "Restaurant Fleur", font=mast)
d.text(((W * S - (bb[2] - bb[0])) / 2 - bb[0], 288 * S), "Restaurant Fleur", font=mast, fill=INK)

sub = "Elevated French-American dining · chef's tasting menus"
bb = d.textbbox((0, 0), sub, font=geo(29))
d.text(((W * S - (bb[2] - bb[0])) / 2 - bb[0], 402 * S), sub, font=geo(29), fill=INK2)

d.line([px(470, 480), px(730, 480)], fill=GOLD, width=1 * S)
d.line([px(470, 484), px(730, 484)], fill=GOLD, width=1 * S)

tracked(600, 520, "101 W CAPITOL AVE · LITTLE ROCK, AR 72201", geo(17), GOLD_D, 3.4 * S)

img = img.resize((W, H), Image.LANCZOS)
img.save(OUT, "PNG")
print("og.png written", os.path.getsize(OUT))
