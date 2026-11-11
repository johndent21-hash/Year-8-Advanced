"""Independently recompute every answer that has a machine check, and list the
ones that need a human read. Usage: python3 verify.py b1 [b2 ...]"""
import sys, importlib, re
import sympy as sp
from sympy import Rational, sqrt, pi, expand, factor, isprime, simplify, log, sin, cos, tan, nsimplify

SYMS = {n: sp.Symbol(n) for n in 'a b c d h k m n p q r s t u v w x y z A P'.split()}
NS = dict(SYMS, sp=sp, Rational=Rational, sqrt=sqrt, pi=pi, expand=expand, factor=factor, isprime=isprime,
          log=log, sin=sin, cos=cos, tan=tan, rad=sp.rad, S=sp.S, oo=sp.oo, Abs=sp.Abs)


def ev(s):
    if not isinstance(s, str):
        return sp.sympify(s)
    try:
        return sp.sympify(eval(s, dict(NS, __builtins__=__builtins__)))
    except Exception:
        return sp.sympify(s, locals=NS)


def check(c):
    kind = c[0]
    if kind == 'eq':
        a, b = ev(c[1]), ev(c[2])
        diff = a - b
        if diff.has(sp.Float) and not diff.free_symbols:
            return abs(float(diff)) < 1e-9, f'{a} vs {b}'
        return sp.simplify(diff) == 0, f'{a} vs {b}'
    if kind == 'solve':
        _, lhs, rhs, var, sols = c
        v = SYMS[var]
        got = sp.solve(sp.Eq(ev(lhs), ev(rhs)), v)
        want = [ev(s) for s in sols]
        ok = len(got) == len(want) and all(any(sp.simplify(g - w) == 0 for g in got) for w in want)
        return ok, f'solve -> {got}; claimed {want}'
    if kind == 'fac':
        expr, claimed = ev(c[1]), ev(c[2])
        same = sp.expand(expr - claimed) == 0
        return same, f'factor() gives {sp.factor(expr)}; claimed {c[2]}'
    if kind == 'py':
        env = dict(NS, __builtins__=__builtins__)
        if len(c) > 2:
            env.update(c[2])
        res = eval(c[1], env)
        return bool(res), c[1][:70]
    if kind == 'man':
        return None, c[1]
    raise ValueError(kind)


def main(keys):
    sys.path.insert(0, '.')
    total = bad = manual = 0
    for key in keys:
        bk = importlib.import_module(key).BK
        for w, qs in enumerate(bk['weeks']):
            assert len(qs) == 20, (key, w, len(qs))
            items = [(str(i + 1), q) for i, q in enumerate(qs)] + [('B', bk['bonus'][w])]
            for n, q in items:
                total += 1
                if not q.get('c'):
                    print(f'  {key} W{w + 1} Q{n}: NO CHECK  | {q["t"][:60]}')
                    manual += 1
                    continue
                try:
                    ok, info = check(q['c'])
                except Exception as e:
                    ok, info = False, f'ERROR {e!r}'
                if ok is None:
                    manual += 1
                    print(f'  {key} W{w + 1} Q{n}: MANUAL  | {info} | ans: {q["a"]}')
                elif not ok:
                    bad += 1
                    print(f'**{key} W{w + 1} Q{n}: FAIL    | {info} | ans: {q["a"]}')
                if q.get('c') and q['c'][0] == 'fac':
                    print(f'  {key} W{w + 1} Q{n}: FACTOR  | {info}')
    print(f'\n{total} items, {bad} failed, {manual} manual')


if __name__ == '__main__':
    main(sys.argv[1:])
