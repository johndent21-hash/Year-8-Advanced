import numpy as np
from PIL import Image
OUT='/tmp/claude-0/-home-user/99a9b54c-ab52-54de-aa67-47207f57a4fd/scratchpad/build/img/'

def mandel(cx, cy, width, W, H, maxit):
    h = width*H/W
    x = np.linspace(cx-width/2, cx+width/2, W)
    y = np.linspace(cy+h/2, cy-h/2, H)
    C = x[None,:] + 1j*y[:,None]
    Z = np.zeros_like(C); N = np.zeros(C.shape); alive = np.ones(C.shape, bool)
    for i in range(maxit):
        Z[alive] = Z[alive]**2 + C[alive]
        esc = alive & (np.abs(Z) > 256)
        N[esc] = i + 1 - np.log2(np.log(np.abs(Z[esc])))
        alive &= ~esc
        if not alive.any(): break
    N[alive] = -1
    return N

def palette(stops):
    pos=[s[0] for s in stops]; cols=np.array([s[1] for s in stops],float)
    def f(t):
        t=np.clip(t,0,1)
        return np.stack([np.interp(t,pos,cols[:,k]) for k in range(3)],-1)
    return f

def hexc(h): h=h.lstrip('#'); return [int(h[i:i+2],16) for i in (0,2,4)]

def render(name, cx, cy, width, W, H, maxit, stops, inside='#0b0a24', cyc=40.0, ss=2, gamma=1.0):
    N = mandel(cx, cy, width, W*ss, H*ss, maxit)
    pal = palette([(p, hexc(c)) for p,c in stops])
    t = np.where(N>=0, (np.log1p(np.maximum(N,0))**gamma), 0)
    t = (t % (cyc/10)) / (cyc/10)
    t = 0.5-0.5*np.cos(t*2*np.pi)   # smooth cyclic
    img = pal(t)
    img[N<0] = hexc(inside)
    im = Image.fromarray(img.astype(np.uint8))
    if ss>1: im = im.resize((W,H), Image.LANCZOS)
    im.save(OUT+name+'.jpg', quality=70, optimize=True, progressive=True)
    return im

# palettes
P = {
 'cover': [(0,'#0b0a24'),(0.35,'#2a2f8f'),(0.6,'#1fa3b5'),(0.8,'#f2c14e'),(1,'#fff6e0')],
 'L1': [(0,'#0d1b4c'),(0.5,'#3b6fe0'),(0.8,'#a8d8ff'),(1,'#ffffff')],
 'L2': [(0,'#062a2f'),(0.5,'#0f9b8e'),(0.85,'#b8f2e6'),(1,'#ffffff')],
 'L3': [(0,'#2a0b3d'),(0.5,'#8e3fd1'),(0.85,'#e6c8ff'),(1,'#ffffff')],
 'L4': [(0,'#3b0a0a'),(0.5,'#d1453b'),(0.85,'#ffd0b8'),(1,'#fff7f0')],
 'L5': [(0,'#0a2a12'),(0.5,'#2f9e44'),(0.85,'#c8f7c5'),(1,'#ffffff')],
 'L6': [(0,'#3a1d00'),(0.5,'#e67700'),(0.85,'#ffe3b3'),(1,'#fffaf0')],
 'L7': [(0,'#3a0624'),(0.5,'#d6336c'),(0.85,'#ffc9de'),(1,'#fff5f9')],
 'T':  [(0,'#101828'),(0.5,'#475467'),(0.85,'#d0d5dd'),(1,'#ffffff')],
}
import sys
which = sys.argv[1:] or ['all']
jobs = {
 'cover': lambda: render('cover', -0.7453, 0.1127, 0.0105, 850, 1200, 900, P['cover'], cyc=28),
 'L1': lambda: render('L1', -0.62, 0.0, 3.0, 1200, 150, 300, P['L1'], cyc=30),
 'L2': lambda: render('L2', -0.7485, 0.0985, 0.06, 1200, 150, 500, P['L2'], cyc=30),
 'L3': lambda: render('L3', 0.2925, 0.0145, 0.03, 1200, 150, 600, P['L3'], cyc=30),
 'L4': lambda: render('L4', -0.74364, 0.13182, 0.004, 1200, 150, 900, P['L4'], cyc=30),
 'L5': lambda: render('L5', -1.7686, 0.0, 0.06, 1200, 150, 600, P['L5'], cyc=30),
 'L6': lambda: render('L6', -0.0886, 0.6544, 0.03, 1200, 150, 700, P['L6'], cyc=30),
 'L7': lambda: render('L7', -0.1011, 0.9563, 0.012, 1200, 150, 800, P['L7'], cyc=30),
 'T':  lambda: render('T', -0.16, 1.035, 0.06, 1200, 150, 600, P['T'], cyc=30),
}
for k,f in jobs.items():
    if 'all' in which or k in which: f(); print('done',k)
