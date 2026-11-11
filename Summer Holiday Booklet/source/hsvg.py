"""Diagrams for the holiday booklet (drawn to scale unless captioned)."""
import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))
from svg import _svg, _txt, right_tri, poly, STROKE

FILL = 'rgba(10,140,160,0.10)'


def _line(x1, y1, x2, y2, w=0.35, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{STROKE}" stroke-width="{w}"{d}/>'


def _arc(cx, cy, r, a1, a2):
    """arc from angle a1 to a2 (degrees, anticlockwise, maths convention; y down in svg)"""
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2))
    large = 1 if (a2 - a1) % 360 > 180 else 0
    return f'<path d="M{x1:.2f} {y1:.2f} A{r} {r} 0 {large} 0 {x2:.2f} {y2:.2f}" fill="none" stroke="{STROKE}" stroke-width="0.3"/>'


def straight_angle(known, label_known, label_unknown):
    """straight line with a ray at `known` degrees from the right-hand arm"""
    w, h = 40, 18
    cx, cy = 20, 15
    body = _line(2, cy, 38, cy)
    ex, ey = cx + 16 * math.cos(math.radians(known)), cy - 16 * math.sin(math.radians(known))
    body += _line(cx, cy, ex, ey)
    body += _arc(cx, cy, 4, 0, known) + _arc(cx, cy, 5.5, known, 180)
    mid1, mid2 = known / 2, (known + 180) / 2
    body += _txt(cx + 8.5 * math.cos(math.radians(mid1)), cy - 8.5 * math.sin(math.radians(mid1)) + 1, label_known, size=2.8)
    body += _txt(cx + 9.5 * math.cos(math.radians(mid2)), cy - 9.5 * math.sin(math.radians(mid2)) + 1, label_unknown, size=2.8, italic=True)
    return _svg(w, h, body)


def crossing(angle, l1, l2):
    """two lines crossing at `angle` degrees; label vertically opposite angles"""
    w, h = 44, 22
    cx, cy = 26, 11
    L = 15
    a = math.radians(angle / 2)
    pts = [(cx + L * math.cos(a), cy - L * math.sin(a)), (cx - L * math.cos(a), cy + L * math.sin(a)),
           (cx + L * math.cos(a), cy + L * math.sin(a)), (cx - L * math.cos(a), cy - L * math.sin(a))]
    body = _line(*pts[0], *pts[1]) + _line(*pts[2], *pts[3])
    body += _arc(cx, cy, 3.5, -angle / 2, angle / 2) + _arc(cx, cy, 3.5, 180 - angle / 2, 180 + angle / 2)
    body += _txt(cx + 9, cy + 1, l1, size=2.7) + _txt(cx - 11.5, cy + 1, l2, size=2.6, italic=True, anchor='end')
    return _svg(w, h, body)


def parallel(angle, l_known, l_unknown):
    """two horizontal parallel lines cut by a transversal; known angle above-right at top line,
    unknown is co-interior (below-right at top? -> above-right at bottom line)"""
    w, h = 40, 24
    y1, y2 = 7, 18
    body = _line(2, y1, 38, y1) + _line(2, y2, 38, y2)
    # arrows marking parallel
    for y in (y1, y2):
        body += f'<path d="M26 {y-1} l1.4 1 l-1.4 1" fill="none" stroke="{STROKE}" stroke-width="0.3"/>'
    t = math.radians(angle)
    # transversal through points on both lines
    xa = 14; xb = xa - (y2 - y1) / math.tan(t)
    ext = 4
    dx, dy = math.cos(t), -math.sin(t)
    body += _line(xb - dx * ext, y2 - dy * ext, xa + dx * ext, y1 + dy * ext)
    # angle at top intersection, below the line, to the right of transversal: from -(180-angle) to 0
    body += _arc(xa, y1, 3, -(180 - angle), 0)
    body += _txt(xa + 6, y1 + 4, l_known, size=2.6)
    # co-interior at bottom intersection: above the line, right of transversal: from 0 to angle
    body += _arc(xb, y2, 3, 0, angle)
    body += _txt(xb + 6.5, y2 - 2, l_unknown, size=2.6, italic=True)
    return _svg(w, h, body)


def l_shape(W, H, nw, nh, labels):
    """W x H rectangle with nw x nh notch removed from top-right"""
    pts = [(0, 0), (W, 0), (W, H - nh), (W - nw, H - nh), (W - nw, H), (0, H)]
    s = min(22 / W, 11 / H)
    lab = [(W / 2, -3.4 / s, labels[0], 'middle'), (W + 1.0 / s, (H - nh) / 2 - 1.0 / s, labels[1], 'start'),
           (W - nw / 2, H - nh + 0.9 / s, labels[2], 'middle'), (-1.0 / s, H / 2 - 1.0 / s, labels[3], 'end')]
    return poly(pts, lab, s, round(W * s + 22, 1), round(H * s + 12, 1))


def house(W, H, R, labels):
    pts = [(0, 0), (W, 0), (W, H), (W / 2, H + R), (0, H)]
    s = min(22 / W, 14 / (H + R))
    pad = 5
    hh = round((H + R) * s + 12, 1)
    X, Y1, Y2 = pad + W / 2 * s, hh - pad - H * s, hh - pad - (H + R) * s
    extra = _line(X, Y1, X, Y2, 0.3, '1 0.7') + _line(pad, Y1, pad + W * s, Y1, 0.25, '1 0.7')
    lab = [(W / 2, -3.4 / s, labels[0], 'middle'), (W + 1.0 / s, H / 2 - 1.0 / s, labels[1], 'start'),
           (W / 2 + 0.6 / s, H + R * 0.12, labels[2], 'start')]
    return poly(pts, lab, s, round(W * s + 22, 1), hh, extra)


def rect_diag(W, H, lw, lh, ld):
    s = min(20 / W, 9 / H)
    pad = 6
    w, h = W * s + 2 * pad + 4, H * s + 2 * pad
    body = (f'<rect x="{pad}" y="{pad}" width="{W*s:.2f}" height="{H*s:.2f}" fill="{FILL}" stroke="{STROKE}" stroke-width="0.35"/>'
            + _line(pad, pad + H * s, pad + W * s, pad, 0.35, '1 0.7')
            + _txt(pad + W * s / 2, pad + H * s + 4, lw) + _txt(pad - 1.2, pad + H * s / 2 + 1, lh, anchor='end')
            + _txt(pad + W * s / 2 + 2.5, pad + H * s / 2 + 3.6, ld, italic=True))
    return _svg(round(w, 1), round(h, 1), body)


def tri_angles(a, b, la, lb, lc):
    """triangle with base angles a and b (degrees) drawn to scale"""
    base = 30
    A, B = math.radians(a), math.radians(b)
    # apex: intersection
    xc = base * math.tan(B) / (math.tan(A) + math.tan(B))
    yc = xc * math.tan(A)
    s = min(1, 16 / yc)
    pad = 4
    W, Hh = base * s, yc * s
    w, h = W + 2 * pad, Hh + 2 * pad + 2
    P = [(pad, pad + Hh), (pad + W, pad + Hh), (pad + xc * s, pad)]
    pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in P)
    body = f'<polygon points="{pts}" fill="{FILL}" stroke="{STROKE}" stroke-width="0.35"/>'
    body += _txt(P[0][0] + 5.5, P[0][1] - 1.2, la, size=2.6) + _txt(P[1][0] - 5.5, P[1][1] - 1.2, lb, size=2.6)
    body += _txt(P[2][0], P[2][1] + 5, lc, size=2.6, italic=True)
    return _svg(round(w, 1), round(h, 1), body)
