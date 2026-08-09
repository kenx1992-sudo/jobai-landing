import math
import os

INK = "#100F1C"
CAT = "#E3A76F"
CAT_DARK = "#C6884E"
PINK = "#F0A9A3"
CARD = "#1F1E36"
CARD_LINE = "#2C2A4A"
BRAND = "#4F46E5"
GREEN = "#10B981"

def bezier_q(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)

def circle_chain(p0, p1, p2, r0, r1, n, fill):
    out = []
    for i in range(n + 1):
        t = i / n
        x, y = bezier_q(p0, p1, p2, t)
        r = r0 + (r1 - r0) * t
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}"/>')
    return "\n  ".join(out)

def poly(pts, fill):
    s = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polygon points="{s}" fill="{fill}"/>'

def build():
    parts = []
    parts.append(f'<rect x="300" y="90" width="148" height="160" rx="14" fill="{CARD}"/>')
    parts.append(f'<rect x="316" y="110" width="44" height="14" rx="7" fill="{GREEN}"/>')
    parts.append(f'<rect x="316" y="140" width="116" height="10" rx="5" fill="{CARD_LINE}"/>')
    parts.append(f'<rect x="316" y="158" width="84" height="10" rx="5" fill="{CARD_LINE}"/>')
    parts.append(f'<rect x="316" y="208" width="116" height="24" rx="8" fill="{BRAND}"/>')

    parts.append(f'<circle cx="322" cy="100" r="16" fill="{GREEN}"/>')
    parts.append(f'<polyline points="313,100 319,107 332,92" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')

    parts.append(circle_chain((205, 195), (255, 175), (298, 168), 15, 12, 16, CAT))

    parts.append(f'<ellipse cx="155" cy="228" rx="67" ry="60" fill="{CAT}"/>')
    parts.append(f'<ellipse cx="155" cy="245" rx="27" ry="35" fill="#F2C495"/>')

    parts.append(f'<ellipse cx="118" cy="273" rx="18" ry="15" fill="{CAT}"/>')
    parts.append(f'<ellipse cx="194" cy="273" rx="18" ry="15" fill="{CAT}"/>')

    parts.append(f'<ellipse cx="301" cy="168" rx="15" ry="14" fill="{CAT}"/>')

    parts.append(f'<circle cx="150" cy="118" r="56" fill="{CAT}"/>')

    parts.append(poly([(96, 92), (114, 24), (150, 88)], CAT))
    parts.append(poly([(150, 88), (186, 24), (204, 92)], CAT))
    parts.append(poly([(106, 84), (117, 44), (139, 82)], PINK))
    parts.append(poly([(161, 82), (183, 44), (194, 84)], PINK))

    parts.append(f'<ellipse cx="97.5" cy="167.5" rx="7.5" ry="12.5" fill="{CAT_DARK}"/>')
    parts.append(f'<ellipse cx="203.5" cy="167.5" rx="7.5" ry="12.5" fill="{CAT_DARK}"/>')

    parts.append(f'<ellipse cx="133" cy="121" rx="7" ry="7" fill="{INK}"/>')
    parts.append(f'<ellipse cx="167" cy="121" rx="7" ry="7" fill="{INK}"/>')
    parts.append(poly([(144, 132), (156, 132), (150, 141)], PINK))
    parts.append(f'<path d="M138,142 Q150,154 162,142" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')

    for y0, y1 in ((132, 128), (140, 141), (148, 155)):
        parts.append(f'<line x1="92" y1="{y0}" x2="48" y2="{y1}" stroke="{CAT_DARK}" stroke-width="2" stroke-linecap="round"/>')
        parts.append(f'<line x1="208" y1="{y0}" x2="252" y2="{y1}" stroke="{CAT_DARK}" stroke-width="2" stroke-linecap="round"/>')

    return "\n  ".join(parts)

if __name__ == "__main__":
    inner = build()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 340" fill="none">
  {inner}
</svg>
'''
    outdir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{outdir}/cat-mascot.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("svg written")
