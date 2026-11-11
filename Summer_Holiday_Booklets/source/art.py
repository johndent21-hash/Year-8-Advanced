"""Cover + six week banners per booklet, all cut from the same Julia set
J(c), c = -0.7269 + 0.1889i. Usage: python3 art.py b1 [--draft]"""
import sys, os, random
import numpy as np
from PIL import Image
from julia import julia_mu, colourise_eq, hex2rgb

C = complex(-0.7269, 0.1889)
MAXIT = 650

PAL = {
    # name, cover gradient (far -> near set), title/sub/kicker colours, stripe, week colours
    'b1': dict(name='Watermelon',
               cover=[(0, '#fffaf4'), (0.22, '#ffe2e2'), (0.40, '#ff9aa6'), (0.55, '#f2546b'), (0.68, '#c9284a'), (0.82, '#4fae36'), (0.95, '#c4ea86'), (1, '#ffffff')],
               view=((0.0, 0.02), 1.95, 82), mix=0.45,
               title='#e23350', sub='#4c9a2a', kick='#2b8a3e', kick_d='#2b8a3e', cream='#fffaf4', peach='#fff0ee', firstup='#ff9aa6',
               stripe=['#e23350', '#ff9aa6', '#8fcf3c', '#2b8a3e'],
               weeks=['#e23350', '#4c9a2a', '#d6336c', '#2b8a3e', '#f0643c', '#5c940d']),
    'b2': dict(name='Lagoon',
               cover=[(0, '#f9fdfb'), (0.22, '#dcf6f1'), (0.40, '#7fdcd2'), (0.55, '#22b3ad'), (0.68, '#0b7f86'), (0.82, '#e9a93a'), (0.95, '#fbe3a6'), (1, '#ffffff')],
               view=((-0.05, 0.47), 0.95, 0),
               title='#0b9a9a', sub='#d9822b', kick='#0b8a8a', kick_d='#087f7f', cream='#f9fdfb', peach='#eaf8f5', firstup='#f6c768',
               stripe=['#0b9a9a', '#7fdcd2', '#f2c14e', '#d9822b'],
               weeks=['#0b9a9a', '#c27c0e', '#1a83c6', '#087f5b', '#e8590c', '#0c8599']),
    'b3': dict(name='Mango',
               cover=[(0, '#fffaf0'), (0.22, '#ffedc4'), (0.40, '#ffd04d'), (0.55, '#ffa62b'), (0.68, '#f0661c'), (0.82, '#c2255c'), (0.95, '#f7b3cb'), (1, '#ffffff')],
               view=((0.86, 0.2), 0.42, 25),
               title='#e8590c', sub='#c2255c', kick='#d9480f', kick_d='#c2410c', cream='#fffaf0', peach='#fff1dc', firstup='#ffc04d',
               stripe=['#e8590c', '#ffc93c', '#f783ac', '#c2255c'],
               weeks=['#e8590c', '#d6336c', '#b8860b', '#e03131', '#d9480f', '#a61e4d']),
    'b4': dict(name='Ocean',
               cover=[(0, '#f6fbff'), (0.22, '#d8ecff'), (0.40, '#7cc4f4'), (0.55, '#2f86d8'), (0.68, '#1c4fa8'), (0.82, '#f2b01e'), (0.95, '#ffe7a3'), (1, '#ffffff')],
               view=((0.52, -0.12), 0.34, -30),
               title='#1f5fc4', sub='#e09a00', kick='#1971c2', kick_d='#1864ab', cream='#f6fbff', peach='#eaf3fd', firstup='#ffcf4d',
               stripe=['#1f5fc4', '#7cc4f4', '#f2b01e', '#ff6f61'],
               weeks=['#1f5fc4', '#c27c0e', '#1098ad', '#3b5bdb', '#0b7285', '#e8590c']),
    'b5': dict(name='Sunset',
               cover=[(0, '#fff8f2'), (0.22, '#ffe2cc'), (0.40, '#ffac5c'), (0.55, '#f4724b'), (0.68, '#e0457b'), (0.82, '#7a3db8'), (0.95, '#d9c2f5'), (1, '#ffffff')],
               view=((-0.30, -0.27), 0.40, 35),
               title='#7a3db8', sub='#ee6a2c', kick='#6f42c1', kick_d='#6741d9', cream='#fff8f2', peach='#f6efff', firstup='#ffac5c',
               stripe=['#7a3db8', '#e0457b', '#f4724b', '#ffb703'],
               weeks=['#7a3db8', '#e8590c', '#d6336c', '#5f3dc4', '#c2255c', '#9c36b5']),
    'b6': dict(name='Tropical Palm',
               cover=[(0, '#fbfdf2'), (0.22, '#eef8c8'), (0.40, '#c2e45a'), (0.55, '#4fbf6b'), (0.68, '#0f8a5f'), (0.82, '#f2643c'), (0.95, '#ffc9b5'), (1, '#ffffff')],
               view=((0.36, -0.02), 0.09, 0),
               title='#0f8a5f', sub='#f2643c', kick='#0b7a55', kick_d='#087048', cream='#fbfdf2', peach='#eef8e8', firstup='#ffb199',
               stripe=['#0f8a5f', '#c2e45a', '#f2643c', '#ffc9b5'],
               weeks=['#0f8a5f', '#e8590c', '#2b8a3e', '#d9480f', '#0b7285', '#5c940d']),
}


def shade(hexc, f):
    """f<0 darker (towards black), f>0 lighter (towards white)."""
    c = hex2rgb(hexc)
    c = c * (1 + f) if f < 0 else c + (255 - c) * f
    return '#%02x%02x%02x' % tuple(int(round(v)) for v in np.clip(c, 0, 255))


def banner_stops(col, accent):
    return [(0, shade(col, -0.55)), (0.30, shade(col, -0.25)), (0.52, col), (0.70, shade(col, 0.45)),
            (0.84, shade(accent, 0.55)), (0.95, shade(col, 0.85)), (1, '#ffffff')]


def candidate_views(seed, n):
    """Random strips of the set, scored so each shows plenty of structure."""
    rng = random.Random(seed)
    coarse, _ = julia_mu(C, (0, 0), 3.2, 320, 200, maxiter=200, ss=1)
    ys, xs = np.where(coarse > 60)
    pts = [((x / 320 - 0.5) * 3.2, -(y / 200 - 0.5) * 2.0) for y, x in zip(ys, xs)]
    out = []
    tries = 0
    while len(out) < n and tries < 400:
        tries += 1
        cx, cy = rng.choice(pts)
        w = rng.uniform(0.35, 1.0)
        rot = rng.uniform(-70, 70)
        mu, _ = julia_mu(C, (cx, cy), w, 240, 38, rot=rot, maxiter=250, ss=1)
        frac = (mu > 40).mean()
        if 0.3 < frac < 0.8 and all(abs(cx - a) + abs(cy - b) > 0.25 and abs(cx + a) + abs(cy + b) > 0.25 for (a, b), _, _ in out):
            out.append(((cx, cy), w, rot))
    return out


def make(key, draft=False):
    p = PAL[key]
    d = os.path.join('art', key)
    os.makedirs(d, exist_ok=True)
    ss = 1 if draft else 2
    q = 70
    cen, w, rot = p['view']
    W, H = (425, 600) if draft else (850, 1200)
    mu, s = julia_mu(C, cen, w, W, H, rot=rot, maxiter=MAXIT, ss=ss)
    colourise_eq(mu, s, p['cover'], MAXIT, mix=p.get('mix', 0.65)).save(os.path.join(d, 'cover.jpg'), quality=q, optimize=True, progressive=True)
    seed = {'b1': 11, 'b2': 23, 'b3': 37, 'b4': 41, 'b5': 53, 'b6': 67}[key]
    views = candidate_views(seed, 6)
    BW, BH = (600, 95) if draft else (1200, 190)
    accents = p['stripe']
    for i, (cen, w, rot) in enumerate(views):
        mu, s = julia_mu(C, cen, w, BW, BH, rot=rot, maxiter=MAXIT, ss=ss)
        col = p['weeks'][i]
        acc = accents[(i + 1) % len(accents)]
        colourise_eq(mu, s, banner_stops(col, acc), MAXIT).save(os.path.join(d, f'w{i + 1}.jpg'), quality=q, optimize=True, progressive=True)
    with open(os.path.join(d, 'views.txt'), 'w') as f:
        f.write(repr(views))


if __name__ == '__main__':
    make(sys.argv[1], draft='--draft' in sys.argv)
