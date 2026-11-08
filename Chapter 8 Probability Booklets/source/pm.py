"""Probability maths helpers. Every numerical answer in the booklets is
computed here from the question's own data (sample spaces, counts), so the
answer key cannot drift from the questions."""
from fractions import Fraction as Fr
from decimal import Decimal, ROUND_HALF_UP

DIE = [1, 2, 3, 4, 5, 6]
PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['H', 'D', 'C', 'S']
DECK = [(r, s) for s in SUITS for r in RANKS]
RED = {'H', 'D'}
PICTURE = {'J', 'Q', 'K'}


def P(fav, tot):
    return Fr(fav, tot)


def count(space, pred):
    fav = [x for x in space if pred(x)]
    return fav, Fr(len(fav), len(space))


def die_p(pred, sides=6):
    return count(list(range(1, sides + 1)), pred)


def card_p(pred):
    return count(DECK, pred)


def rank_val(r):
    return {'A': 1, 'J': 11, 'Q': 12, 'K': 13}.get(r, None) or int(r)


def letters_p(word, pred):
    return count(list(word.replace(' ', '')), pred)


def spin_p(sectors, colour):
    """sectors: list of (colour, weight, label)"""
    tot = sum(Fr(w) for _, w, _ in sectors)
    return sum(Fr(w) for c, w, _ in sectors if c == colour) / tot


# ---------------------------------------------------------------- formatting
def fr(x, big=False):
    """HTML stacked fraction in simplest form (whole numbers stay whole)."""
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator)
    s = '−' if x < 0 else ''
    x = abs(x)
    return f'{s}<span class="fr{" big" if big else ""}"><span>{x.numerator}</span><span>{x.denominator}</span></span>'


def frs(a, b):
    """Unsimplified stacked fraction a/b (for working)."""
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'


def dec(x, dp=None):
    x = Fr(x)
    if dp is None:
        # exact terminating decimal
        d = x.denominator
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        assert d == 1, f'{x} does not terminate'
        s = str(Decimal(x.numerator) / Decimal(x.denominator))
        if 'E' in s:
            s = format(Decimal(x.numerator) / Decimal(x.denominator), 'f')
        return s
    q = (Decimal(x.numerator) / Decimal(x.denominator)).quantize(Decimal(1).scaleb(-dp), ROUND_HALF_UP)
    return str(q)


def pct(x, dp=None):
    v = Fr(x) * 100
    if v.denominator == 1:
        return f'{v.numerator}%'
    if dp is None:
        return dec(v) + '%'
    return dec(v, dp) + '%'


def pct_third(x):
    """Percent with a mixed fraction, e.g. 33 1/3%."""
    v = Fr(x) * 100
    w, r = divmod(v.numerator, v.denominator)
    if r == 0:
        return f'{w}%'
    return f'{w}{fr(Fr(r, v.denominator))}%'


def all3(x, dp=None):
    return f'{fr(x)} = {dec(x, dp)} = {pct(x, None if dp is None else max(dp - 2, 0))}'


def setstr(xs):
    return '{' + ', '.join(str(x) for x in xs) + '}'


def mixed_dec(x, dp=1):
    return dec(x, dp)


def htab(label_row, row_label, values, label2='Frequency', size=8.4, cap=None):
    """Two-row horizontal frequency table."""
    h = f'<table class="t" style="font-size:{size}pt"><tr><th>{label_row}</th>' + ''.join(f'<td>{x}</td>' for x in row_label) + '</tr>'
    h += f'<tr><th>{label2}</th>' + ''.join(f'<td>{x}</td>' for x in values) + '</tr></table>'
    return h


def vtab(head, rows, size=8.2):
    h = f'<table class="t" style="font-size:{size}pt"><tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>'
    for r in rows:
        h += '<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>'
    return h + '</table>'
