"""Mini-DSL: one source string per question -> LaTeX for display + SymPy for checking."""
import re
import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication_application, convert_xor)

T = standard_transformations + (implicit_multiplication_application, convert_xor)
LOC = {'pi': sp.pi, 'sqrt': sp.sqrt, 'cbrt': sp.cbrt}
ERRORS = []


# ---------- source -> sympy ----------
def _match_paren(s, i):
    """s[i] == '(' ; return index of matching ')'."""
    d = 0
    for j in range(i, len(s)):
        if s[j] == '(':
            d += 1
        elif s[j] == ')':
            d -= 1
            if d == 0:
                return j
    raise ValueError('unbalanced: ' + s)


def _frac_to_py(s):
    # [a|b] -> ((a)/(b)), innermost first
    pat = r'\[([^\[\]|]*)\|([^\[\]|]*)\]'
    while re.search(pat, s):
        s = re.sub(pat, r'((\1)/(\2))', s)
    return s


def to_sympy(src, evaluate=True):
    s = src.replace('−', '-').replace('×', '*')
    s = _frac_to_py(s)
    if '÷' in s:
        parts = s.split('÷')
        acc = '(' + parts[0] + ')'
        for p in parts[1:]:
            acc = '(' + acc + ')/(' + p + ')'
        s = acc
    return parse_expr(s, transformations=T, local_dict=LOC, evaluate=evaluate)


# ---------- source -> LaTeX ----------
def _tex_funcs(s):
    for name, pre, post in (('sqrt', r'\sqrt{', '}'), ('cbrt', r'\sqrt[3]{', '}')):
        while name + '(' in s:
            i = s.index(name + '(')
            j = _match_paren(s, i + len(name))
            inner = s[i + len(name) + 1:j]
            s = s[:i] + pre + inner + post + s[j + 1:]
    return s


def tex(src):
    s = src.replace('−', '-')
    pat = r'\[([^\[\]|]*)\|([^\[\]|]*)\]'
    while re.search(pat, s):
        s = re.sub(pat, r'\\dfrac{\1}{\2}', s)
    s = _tex_funcs(s)
    s = re.sub(r'\^\(([^()]*)\)', r'^{\1}', s)
    s = re.sub(r'\^(-?\d+)', r'^{\1}', s)
    s = s.replace('*', r' \times ').replace('÷', r' \div ')
    s = s.replace('pi', r'\pi ')
    s = s.replace('±', r'\pm ')
    return s


# ---------- items ----------
class Item:
    def __init__(self, q, a, tag=None, star=False, kind='S', h=0, check=None, math=True, note=None):
        self.q, self.a, self.tag, self.star, self.kind = q, a, tag, star, kind
        self.h, self.check, self.math, self.note = h, check, math, note
        self.n = None


def m(s, verb=None):
    out = '$' + tex(s) + '$'
    return (f'<span class="verb">{verb}</span> ' + out) if verb else out


def _fail(msg):
    ERRORS.append(msg)


def S(q, a, tag=None, star=False, verb=None):
    """simplify / evaluate: q and a must be equal"""
    try:
        if sp.simplify(to_sympy(q) - to_sympy(a)) != 0:
            _fail(f'S mismatch: {q} -> {a} (got {sp.simplify(to_sympy(q))})')
    except Exception as e:
        _fail(f'S parse error {q} / {a}: {e}')
    return Item(m(q, verb), m(a), tag, star, 'S')


def _has_bracket(e):
    return any(isinstance(arg, sp.Add) for arg in sp.preorder_traversal(e) if arg is not e) or \
        any(isinstance(x, sp.Pow) and isinstance(x.base, sp.Add) for x in sp.preorder_traversal(e))


def E(q, a, tag=None, star=False, verb=None):
    """expand: a equals q and a is expanded"""
    try:
        qa, aa = to_sympy(q), to_sympy(a)
        if sp.expand(qa - aa) != 0:
            _fail(f'E mismatch: {q} -> {a} (want {sp.expand(qa)})')
        if sp.expand(aa) != aa:
            _fail(f'E not expanded: {a}')
    except Exception as e:
        _fail(f'E parse error {q}: {e}')
    return Item(m(q, verb), m(a), tag, star, 'E')


def F(q, a, tag=None, star=False, verb=None, full=False):
    """factorise: expand(a)==q; HCF fully removed (or full sympy factor if full=True)"""
    try:
        qa, aa = to_sympy(q), to_sympy(a)
        if sp.expand(qa - aa) != 0:
            _fail(f'F mismatch: {q} -> {a}')
        if full:
            if sp.factor(qa) != sp.factor(aa) or sp.expand(sp.factor(qa) - aa) != 0:
                _fail(f'F not full: {q} -> {a} (sympy {sp.factor(qa)})')
        else:
            # every bracket's content must be primitive (no common factor left inside)
            for x in sp.preorder_traversal(to_sympy(a, evaluate=False)):
                if isinstance(x, sp.Add):
                    x = sp.sympify(str(x))
                    c, prim = x.as_content_primitive()
                    if c != 1 or sp.factor_terms(prim) != prim:
                        _fail(f'F not fully factorised: {a}')
            # outside factor must equal HCF of terms (up to sign)
            ft = sp.factor_terms(qa)
            if sp.simplify(ft / aa) not in (1, -1) and sp.simplify(ft/aa) != 1:
                _fail(f'F differs from HCF form: {a} vs {ft}')
    except Exception as e:
        _fail(f'F parse error {q}: {e}')
    return Item(m(q, verb), m(a), tag, star, 'F')


def Q(eq, sols, tag=None, star=False, var=None, approx=None, verb=None):
    """equation 'lhs=rhs'; sols list of source strings"""
    try:
        lhs, rhs = eq.split('=')
        ex = to_sympy(lhs) - to_sympy(rhs)
        v = sp.Symbol(var) if var else sorted(ex.free_symbols, key=str)[0]
        got = set(sp.nsimplify(sp.simplify(x)) for x in sp.solve(ex, v))
        want = set(sp.simplify(to_sympy(s)) for s in sols)
        if got != want:
            _fail(f'Q mismatch {eq}: got {got} want {want}')
        vname = str(v)
    except Exception as e:
        _fail(f'Q error {eq}: {e}')
        vname = 'x'
    if len(sols) == 2 and sp.simplify(to_sympy(sols[0]) + to_sympy(sols[1])) == 0:
        pos = sols[0] if not sols[0].startswith('-') else sols[1]
        ans = f'${vname} = \\pm {tex(pos)}$'
    else:
        ans = '$' + ', '.join(f'{vname} = {tex(s)}' for s in sols) + '$'
    if approx:
        ans = ans[:-1] + r' \approx ' + approx + '$'
    return Item(m(eq, verb), ans, tag, star, 'Q')


def N(q, a, check, tag=None, star=False, h=0):
    """free-form question (html with $..$); check is a bool or callable returning bool"""
    ok = check() if callable(check) else check
    if not ok:
        _fail(f'N check failed: {q[:60]} -> {a}')
    return Item(q, a, tag, star, 'N', h=h, math=False)


def L(q, a, h=18, check=True, tag=None, star=False):
    """long / worded question with working box h mm"""
    ok = check() if callable(check) else check
    if not ok:
        _fail(f'L check failed: {q[:60]}')
    return Item(q, a, tag, star, 'L', h=h, math=False)


def close(x, y, tol=1e-9):
    return abs(float(x) - float(y)) < tol


def r(x, dp):
    """round half up to dp places (matches NSW convention)"""
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(float(x))).quantize(q, rounding=ROUND_HALF_UP))


def V(q, vals, a, tag=None, star=False, verb=None):
    """substitution: evaluate q at vals (dict name->value) equals a"""
    try:
        e = to_sympy(q).subs({sp.Symbol(k): sp.nsimplify(v) for k, v in vals.items()})
        if sp.simplify(e - to_sympy(a)) != 0:
            _fail(f'V mismatch {q} at {vals}: got {e} want {a}')
    except Exception as ex:
        _fail(f'V error {q}: {ex}')
    return Item(m(q, verb), m(a), tag, star, 'V')
