import numpy as np, sys
from PIL import Image
OUT = 'img/'

def hexc(h): h = h.lstrip('#'); return [int(h[i:i+2], 16) for i in (0, 2, 4)]

def pal(stops):
    pos = [p for p, _ in stops]; cols = np.array([hexc(c) for _, c in stops], float)
    return lambda t: np.stack([np.interp(t, pos, cols[:, k]) for k in range(3)], -1)

def julia(name, c, cx, cy, width, W, H, maxit, stops, inside, cyc=1.0, ss=2, rot=0.0):
    w, h = W*ss, H*ss
    hh = width*H/W
    x = np.linspace(-width/2, width/2, w); y = np.linspace(hh/2, -hh/2, h)
    Z = x[None, :] + 1j*y[:, None]
    Z = Z*np.exp(1j*rot) + (cx + 1j*cy)
    N = np.zeros(Z.shape); alive = np.ones(Z.shape, bool)
    for i in range(maxit):
        Z[alive] = Z[alive]**2 + c
        esc = alive & (np.abs(Z) > 64)
        N[esc] = i + 1 - np.log2(np.log(np.abs(Z[esc])))
        alive &= ~esc
        if not alive.any(): break
    t = np.where(N > 0, np.log1p(N), 0)
    t = (t / cyc) % 1.0
    t = 0.5 - 0.5*np.cos(2*np.pi*t)
    img = pal(stops)(t)
    img[~(N > 0)] = hexc(inside)
    im = Image.fromarray(img.astype(np.uint8))
    if ss > 1: im = im.resize((W, H), Image.LANCZOS)
    im.save(OUT + name + '.jpg', quality=70, optimize=True, progressive=True)

P = {
 'cover': ([(0, '#1b0f3b'), (0.3, '#7b2d6b'), (0.55, '#f2545b'), (0.78, '#ffb347'), (1, '#fff3d6')], '#0f2a44'),
 'W1': ([(0, '#023e58'), (0.45, '#0aa5b5'), (0.8, '#9ff0e5'), (1, '#fffaf0')], '#f4d9a6'),   # ocean / sand
 'W2': ([(0, '#4a1458'), (0.45, '#e2557b'), (0.8, '#ffc18a'), (1, '#fff6e8')], '#2b0b33'),   # sunset
 'W3': ([(0, '#0c3b2e'), (0.45, '#3fa34d'), (0.8, '#d9f99d'), (1, '#fbfff0')], '#103a31'),   # eucalyptus
 'W4': ([(0, '#5c1d00'), (0.45, '#f08c00'), (0.8, '#ffe066'), (1, '#fffbea')], '#3a1300'),   # mango
 'W5': ([(0, '#0b2a6f'), (0.45, '#3d8bfd'), (0.8, '#bde0fe'), (1, '#ffffff')], '#071b46'),   # sky
 'W6': ([(0, '#5a0f2e'), (0.45, '#ff6f61'), (0.8, '#ffd3c2'), (1, '#fff7f3')], '#3b0820'),   # coral
}
jobs = {
 'cover': lambda: julia('cover', -0.7269+0.1889j, 0, 0, 2.15, 850, 1200, 400, *P['cover'], cyc=0.9, rot=np.pi/2),
 'W1': lambda: julia('W1', -0.8+0.156j, 0.0, 0.0, 3.2, 1200, 190, 300, *P['W1'], cyc=0.9),
 'W2': lambda: julia('W2', -0.4+0.6j, 0.0, 0.0, 3.0, 1200, 190, 300, *P['W2'], cyc=0.9),
 'W3': lambda: julia('W3', 0.285+0.01j, 0.0, 0.0, 2.6, 1200, 190, 400, *P['W3'], cyc=0.9),
 'W4': lambda: julia('W4', -0.70176-0.3842j, 0.0, 0.0, 3.0, 1200, 190, 400, *P['W4'], cyc=0.9),
 'W5': lambda: julia('W5', -0.835-0.2321j, 0.0, 0.0, 3.0, 1200, 190, 400, *P['W5'], cyc=0.9),
 'W6': lambda: julia('W6', 0.355+0.355j, 0.0, 0.0, 2.6, 1200, 190, 400, *P['W6'], cyc=0.9),
}
for k, f in jobs.items():
    if len(sys.argv) == 1 or k in sys.argv[1:]: f(); print('done', k)
