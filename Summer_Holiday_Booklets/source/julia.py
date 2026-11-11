import numpy as np
from PIL import Image

def julia_mu(c, center, width, W, H, rot=0.0, maxiter=400, ss=2):
    """Smooth escape-time values for z->z^2+c over a rotated viewport."""
    w, h = W*ss, H*ss
    height = width * H / W
    xs = (np.arange(w) + 0.5) / w - 0.5
    ys = (np.arange(h) + 0.5) / h - 0.5
    X, Y = np.meshgrid(xs * width, -ys * height)
    ang = np.deg2rad(rot)
    Z = (X*np.cos(ang) - Y*np.sin(ang)) + 1j*(X*np.sin(ang) + Y*np.cos(ang)) + complex(*center)
    mu = np.full(Z.shape, float(maxiter))
    alive = np.ones(Z.shape, bool)
    z = Z.copy()
    for n in range(maxiter):
        z[alive] = z[alive]**2 + c
        esc = alive & (np.abs(z) > 4)
        if esc.any():
            az = np.abs(z[esc])
            mu[esc] = n + 1 - np.log(np.log(az)) / np.log(2)
            alive &= ~esc
        if not alive.any():
            break
    return mu, ss

def hex2rgb(h):
    h = h.lstrip('#'); return np.array([int(h[i:i+2], 16) for i in (0, 2, 4)], float)

def colourise(mu, ss, stops, maxiter, gamma=0.5, interior='#ffffff'):
    """stops: list of (t, hex). t in [0,1] on a gamma-scaled iteration axis."""
    t = np.clip(mu / maxiter, 0, 1) ** gamma
    ts = np.array([s[0] for s in stops]); cols = np.array([hex2rgb(s[1]) for s in stops])
    out = np.zeros(mu.shape + (3,))
    for k in range(3):
        out[..., k] = np.interp(t, ts, cols[:, k])
    out[mu >= maxiter] = hex2rgb(interior)
    img = Image.fromarray(out.clip(0, 255).astype(np.uint8))
    if ss > 1:
        img = img.resize((mu.shape[1]//ss, mu.shape[0]//ss), Image.LANCZOS)
    return img

def colourise_log(mu, ss, stops, maxiter, lo=1.0, interior='#ffffff'):
    m = np.clip(mu, lo, maxiter)
    t = (np.log(m) - np.log(lo)) / (np.log(maxiter) - np.log(lo))
    ts = np.array([s[0] for s in stops]); cols = np.array([hex2rgb(s[1]) for s in stops])
    out = np.zeros(mu.shape + (3,))
    for k in range(3):
        out[..., k] = np.interp(t, ts, cols[:, k])
    out[mu >= maxiter] = hex2rgb(interior)
    img = Image.fromarray(out.clip(0, 255).astype(np.uint8))
    if ss > 1:
        img = img.resize((mu.shape[1]//ss, mu.shape[0]//ss), Image.LANCZOS)
    return img

def colourise_eq(mu, ss, stops, maxiter, interior='#ffffff', mix=0.65, lo=2.0):
    """Blend of histogram-equalised and log-scaled escape values, so every colour
    band gets a fair share of the picture whatever the zoom."""
    esc = mu < maxiter
    t = np.zeros(mu.shape)
    v = mu[esc]
    ranks = np.argsort(np.argsort(v)).astype(float) / max(len(v) - 1, 1)
    m = np.clip(v, lo, maxiter)
    lg = (np.log(m) - np.log(lo)) / (np.log(maxiter) - np.log(lo))
    t[esc] = mix * ranks + (1 - mix) * lg
    ts = np.array([s[0] for s in stops]); cols = np.array([hex2rgb(s[1]) for s in stops])
    out = np.zeros(mu.shape + (3,))
    for k in range(3):
        out[..., k] = np.interp(t, ts, cols[:, k])
    out[~esc] = hex2rgb(interior)
    img = Image.fromarray(out.clip(0, 255).astype(np.uint8))
    if ss > 1:
        img = img.resize((mu.shape[1]//ss, mu.shape[0]//ss), Image.LANCZOS)
    return img
