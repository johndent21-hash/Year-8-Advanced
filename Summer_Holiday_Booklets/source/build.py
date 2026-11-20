"""python3 build.py b1 [--draft]  -> out/<file>.pdf"""
import sys, os, importlib, subprocess, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render
from art import PAL, shade
import pikepdf

JNOTE = {
    'b1': 'this one is the whole set, turned on its side.',
    'b2': 'this one looks straight down on its top spiral.',
    'b3': 'this one zooms in on a cluster of small spirals.',
    'b4': 'this one dives into the heart of one of its two big spirals.',
    'b5': 'this one looks along the valley between two spirals.',
    'b6': 'this one is a deep zoom, about 35 times closer than the full set.',
}


def prep(key):
    bk = importlib.import_module(key).BK
    p = PAL[key]
    bk['pal'] = dict(cream=p['cream'], cream_a=p['cream'] + 'cc', title=p['title'], sub=p['sub'], kick=p['kick'],
                     kick_d=p['kick_d'], peach=p['peach'], firstup=p['firstup'], stripe=p['stripe'])
    bk['week_cols'] = p['weeks']
    bk['chip_cols'] = p['weeks']
    bk['gcols'] = [render.NAME_COLS[g[0]] for g in bk['groups']]
    assert len(set(bk['gcols'])) == 8, bk['gcols']
    assert len(bk['hints']) == 8 and all(h[0].split(' &')[0].split(',')[0] in g[0] or g[0] in h[0] for h, g in zip(bk['hints'], bk['groups'])), [(h[0], g[0]) for h, g in zip(bk['hints'], bk['groups'])]
    bk['tints'] = [shade(c, 0.94) for c in bk['gcols']]
    bk['julia_note'] = JNOTE[key]
    return bk


def ensure_dots(here):
    """Dot-grid tiles used as the working-space background (one shared PNG keeps the PDF small)."""
    from PIL import Image, ImageDraw
    os.makedirs(os.path.join(here, 'art'), exist_ok=True)
    for name, col in [('dots.png', (180, 188, 199)), ('dots_gold.png', (220, 199, 126))]:
        p = os.path.join(here, 'art', name)
        if os.path.exists(p):
            continue
        S = 4
        im = Image.new('RGBA', (13 * S, 12 * S), (255, 255, 255, 0))
        r, cx, cy = 0.95 * S, 2.5 * S, 4 * S
        ImageDraw.Draw(im).ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (255,))
        im.save(p, optimize=True)


def build(key, draft=False):
    bk = prep(key)
    here = os.path.dirname(os.path.abspath(__file__))
    ensure_dots(here)
    art = os.path.join(here, 'art', key)
    html = render.build_html(bk, 'file://' + art)
    os.makedirs(os.path.join(here, 'out'), exist_ok=True)
    hp = os.path.join(here, 'out', key + '.html')
    open(hp, 'w').write(html)
    raw = os.path.join(here, 'out', key + '_raw.pdf')
    subprocess.run(['node', os.path.join(here, 'print.js'), hp, raw], check=True)
    final = os.path.join(here, 'out', bk['file'] + '.pdf')
    with pikepdf.open(raw) as pdf:
        with pdf.open_metadata() as meta:
            meta['dc:title'] = 'Summer Maths: ' + bk['ready']
            meta['dc:creator'] = ['Kingscliff High School Mathematics']
        pdf.docinfo['/Title'] = 'Summer Maths: ' + bk['ready']
        pdf.docinfo['/Author'] = 'Kingscliff High School Mathematics'
        pdf.save(final, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    print(final, os.path.getsize(final) // 1024, 'KB')
    return final


if __name__ == '__main__':
    build(sys.argv[1], draft='--draft' in sys.argv)
