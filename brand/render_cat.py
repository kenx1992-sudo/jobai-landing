import math
import os
from PIL import Image, ImageDraw

S = 3
W, H = 460, 340
G = (W * S, H * S)

INK = "#100F1C"
CAT = "#E3A76F"
CAT_DARK = "#C6884E"
PINK = "#F0A9A3"
CARD = "#1F1E36"
CARD_LINE = "#2C2A4A"
BRAND = "#4F46E5"
GREEN = "#10B981"
MUTED = "#6B688A"

def sc(v):
    return v * S

def sc_pt(p):
    return (p[0] * S, p[1] * S)

def new_canvas():
    return Image.new("RGBA", G, (0, 0, 0, 0))

def bezier_q(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)

def tapered_chain(d, p0, p1, p2, r0, r1, n, fill):
    for i in range(n + 1):
        t = i / n
        x, y = bezier_q(p0, p1, p2, t)
        r = r0 + (r1 - r0) * t
        d.ellipse([sc(x - r), sc(y - r), sc(x + r), sc(y + r)], fill=fill)

def draw_cat_scene():
    img = new_canvas()
    d = ImageDraw.Draw(img)

    # card (job listing being saved) on the right
    card_box = [300, 90, 448, 250]
    d.rounded_rectangle([sc(v) for v in card_box], radius=sc(14), fill=CARD)
    d.rounded_rectangle([sc(316), sc(110), sc(360), sc(124)], radius=sc(7), fill=GREEN)
    d.rounded_rectangle([sc(316), sc(140), sc(432), sc(150)], radius=sc(5), fill=CARD_LINE)
    d.rounded_rectangle([sc(316), sc(158), sc(400), sc(168)], radius=sc(5), fill=CARD_LINE)
    d.rounded_rectangle([sc(316), sc(208), sc(432), sc(232)], radius=sc(8), fill=BRAND)

    # saved badge popping off the card corner
    badge_c = (322, 100)
    d.ellipse([sc(badge_c[0] - 16), sc(badge_c[1] - 16), sc(badge_c[0] + 16), sc(badge_c[1] + 16)], fill=GREEN)
    check = [(313, 100), (319, 107), (332, 92)]
    d.line([sc_pt(p) for p in check], fill="#FFFFFF", width=int(sc(4)), joint="curve")
    for p in (check[0], check[-1]):
        r = sc(2)
        d.ellipse([sc_pt(p)[0]-r, sc_pt(p)[1]-r, sc_pt(p)[0]+r, sc_pt(p)[1]+r], fill="#FFFFFF")

    # arm reaching to the card (tapered chain, behind paw)
    tapered_chain(d, (205, 195), (255, 175), (298, 168), 15, 12, 16, CAT)

    # body
    d.ellipse([sc(88), sc(168), sc(222), sc(288)], fill=CAT)
    # belly patch
    d.ellipse([sc(128), sc(210), sc(182), sc(280)], fill="#F2C495")

    # back paws (sitting)
    d.ellipse([sc(100), sc(258), sc(136), sc(288)], fill=CAT)
    d.ellipse([sc(176), sc(258), sc(212), sc(288)], fill=CAT)

    # working paw resting on the card
    d.ellipse([sc(286), sc(154), sc(316), sc(182)], fill=CAT)

    # head
    head_c, head_r = (150, 118), 56
    d.ellipse([sc(head_c[0]-head_r), sc(head_c[1]-head_r), sc(head_c[0]+head_r), sc(head_c[1]+head_r)], fill=CAT)

    # ears
    d.polygon([sc_pt(p) for p in [(96, 92), (114, 24), (150, 88)]], fill=CAT)
    d.polygon([sc_pt(p) for p in [(150, 88), (186, 24), (204, 92)]], fill=CAT)
    d.polygon([sc_pt(p) for p in [(106, 84), (117, 44), (139, 82)]], fill=PINK)
    d.polygon([sc_pt(p) for p in [(161, 82), (183, 44), (194, 84)]], fill=PINK)

    # tabby markings on head/body
    d.ellipse([sc(90), sc(155), sc(105), sc(180)], fill=CAT_DARK)
    d.ellipse([sc(196), sc(155), sc(211), sc(180)], fill=CAT_DARK)

    # face
    d.ellipse([sc(126), sc(114), sc(140), sc(128)], fill=INK)
    d.ellipse([sc(160), sc(114), sc(174), sc(128)], fill=INK)
    d.polygon([sc_pt(p) for p in [(144, 132), (156, 132), (150, 141)]], fill=PINK)
    smile = [(138, 142)]
    n = 16
    for i in range(1, n + 1):
        t = i / n
        x, y = bezier_q((138, 142), (150, 154), (162, 142), t)
        smile.append((x, y))
    d.line([sc_pt(p) for p in smile], fill=INK, width=int(sc(3)), joint="curve")

    # whiskers
    for y0, y1 in ((132, 128), (140, 141), (148, 155)):
        d.line([sc(92), sc(y0), sc(48), sc(y1)], fill=CAT_DARK, width=int(sc(2)))
    for y0, y1 in ((132, 128), (140, 141), (148, 155)):
        d.line([sc(208), sc(y0), sc(252), sc(y1)], fill=CAT_DARK, width=int(sc(2)))

    return img

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    img = draw_cat_scene()
    bg = Image.new("RGBA", G, INK)
    bg.alpha_composite(img)
    bg.resize((W, H), Image.LANCZOS).save(f"{outdir}/cat_preview.png")
    print("done")
