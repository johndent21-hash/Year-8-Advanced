"""Turns lesson data into pages.

A lesson module defines LESSON (a dict). Shared parts (notes, Example 1,
Example 2) are identical in both booklets; 'std' and 'ext' hold the
You do questions for each booklet."""
from layout import *


class Q:
    def __init__(self, q='', fig='', ans='', ln=None, tag='', span=1, h=None, figtop=False):
        self.q, self.fig, self.ans, self.ln, self.tag = q, fig, ans, ln, tag
        self.span, self.h, self.figtop = span, h, figtop


class R:
    def __init__(self, text, cols, qs, h=None, ln=None, info=None, side=None):
        self.text, self.cols, self.qs, self.h, self.ln, self.info = text, cols, qs, h, ln, info
        self.side = side  # width in mm: show the info box beside the cards instead of above


LN_W = [('Working', ''), ('', ''), ('Answer', '')]
LN_A = [('Answer', '')]
LN_A2 = [('', ''), ('Answer', '')]

KINDS = {'std': ('easy', 'medium', 'hard'), 'ext': ('medium', 'hard', 'further')}
LEVELS = {'std': ('EASY', 'MEDIUM', 'HARD'), 'ext': ('MEDIUM', 'HARD', 'GOING FURTHER')}


def _cards(qs, cols, start, h=None, ln=None):
    out = []
    n = start
    for qq in qs:
        out.append(qcard(n, qq.fig, qq.q, qq.ln if qq.ln is not None else ln, qq.tag,
                         qq.h or h, qq.span, qq.figtop))
        n += 1
    return f'<div class="cards c{cols}">{"".join(out)}</div>', n


def _rounds(rounds, first_round_no, start):
    html, n, ans = '', start, []
    for i, r in enumerate(rounds):
        if i:
            html += '<div class="sep"></div>'
        last = n + len(r.qs) - 1
        rng = f'Question {n}' if last == n else f'Questions {n}–{last}'
        inner = round_hdr(first_round_no + i, f'{rng}: {r.text}')
        c, n2 = _cards(r.qs, r.cols, n, r.h, r.ln)
        if r.info and r.side:
            html += (f'<div class="rw">{inner}<div class="rside" style="grid-template-columns:{r.side}mm minmax(0,1fr)">'
                     f'<div class="infobox side">{r.info}</div>{c}</div></div>')
        else:
            if r.info:
                inner += f'<div class="infobox">{r.info}</div><div style="height:2.2mm"></div>'
            html += f'<div class="rw">{inner}{c}</div>'
        for k, qq in enumerate(r.qs):
            ans.append((n + k, qq.ans))
        n = n2
    return html, n, ans


def lesson_pages(L, book, mode, footer, pno):
    """book: 'std' or 'ext'; mode: 'student', 'teacher', 'selfstudy'.
    Returns (list of page html, answers dict)."""
    D = L[book]
    k1, k2, k3 = KINDS[book]
    v1, v2, v3 = LEVELS[book]
    sub = L['sub']
    pages = []
    worked1 = L['ex1'].get('worked') if mode == 'selfstudy' else None
    worked2 = L['ex2'].get('worked') if mode == 'selfstudy' else None
    nmode = {'student': 'student', 'teacher': 'teacher', 'selfstudy': 'selfstudy'}[mode]

    # ---- page 1
    e1 = L['ex1']
    we1 = wedo('Example 1', e1['instr'], e1['parts'], e1.get('box', 17), e1.get('cols', 4), worked1, data=e1.get('data'))
    r_html, n, a1 = _rounds(D['p1'], 1, 1)
    cnt1 = n - 1
    yd1 = youdo(D.get('t1', 'on your own: work down the box, one round at a time. Show your working.'),
                f'{cnt1} QUESTIONS', remember(D['rem1']) + r_html, k1, grow=True)
    p1 = (banner(L['num'], L['title'], sub, v1, L.get('alt', False)) + li_box(L['li'], L['sc'])
          + notes_box(L['notes'], L.get('notes_h', 38), nmode) + we1 + yd1)
    pages.append(page(p1, footer, pno, 'fill'))

    # ---- page 2
    r_html2, n2, a2 = _rounds(D['p2'], len(D['p1']) + 1, n)
    yd2 = youdo('on your own: keep going, one round at a time. Show your working.', f'{n2 - n} QUESTIONS',
                remember(D['rem2']) + r_html2, k2, grow=True)
    pages.append(page(banner(L['num'], L['title'], sub, v2, L.get('alt', False)) + yd2, footer, pno + 1, 'fill'))

    # ---- page 3
    e2 = L['ex2']
    we2 = wedo('Example 2', e2['instr'], e2['parts'], e2.get('box', 17), e2.get('cols', 4), worked2, data=e2.get('data'))
    c3, n3 = _cards(D['p3'], D.get('p3cols', 3), 1, D.get('p3h', 36), LN_A2)
    a3 = [(i + 1, qq.ans) for i, qq in enumerate(D['p3'])]
    yd3 = youdo('on your own: work in order. A tag shows an earlier lesson or year. Show your working.',
                f'{len(D["p3"])} QUESTIONS', remember(D['rem3']) + '<div class="rw" style="margin-top:2.4mm">' + c3 + '</div>', k3, grow=True)
    cw, _ = _cards(D['word'], D.get('wordcols', 3), 1, D.get('wordh', 34), LN_A2)
    aw = [(i + 1, qq.ans) for i, qq in enumerate(D['word'])]
    ydw = youdo('draw a diagram or a table if it helps, then solve. Show your working.',
                f'{len(D["word"])} PROBLEMS', '<div style="height:.6mm"></div>' + cw, k3, 'WORDED PROBLEMS')
    pages.append(page(banner(L['num'], L['title'], sub, v3, L.get('alt', False)) + we2 + yd3 + ydw, footer, pno + 2, 'fill'))
    answers = dict(rounds=a1 + a2, p3=a3, word=aw)
    return pages, answers


def answer_block(L, answers, book):
    lv = LEVELS[book]
    h = f'<div class="blk"><h3>Lesson {L["num"]} · {L["title"]}</h3>'
    h += f'<h4>PAGES 1–2 · {lv[0].title()} and {lv[1].title()} rounds</h4>'
    h += ''.join(f'<p><b>{n}</b>{a}</p>' for n, a in answers['rounds'])
    h += f'<h4>PAGE 3 · {lv[2].title()}</h4>'
    h += ''.join(f'<p><b>{n}</b>{a}</p>' for n, a in answers['p3'])
    h += '<h4>WORDED PROBLEMS</h4>'
    h += ''.join(f'<p><b>W{n}</b>{a}</p>' for n, a in answers['word'])
    return h + '</div>'


def example_answer_block(L):
    """Answers to the We do examples (teacher copy only)."""
    out = ''
    for key, lab in (('ex1', 'Example 1'), ('ex2', 'Example 2')):
        sol = L[key].get('ans')
        if sol:
            out += f'<h4>{lab.upper()} (WE DO)</h4>' + ''.join(f'<p><b>{"abcd"[i]}</b>{s}</p>' for i, s in enumerate(sol))
    return out
