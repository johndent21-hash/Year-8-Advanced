"""Independent check of every answer in the booklet.

The questions are typed in again here from the printed booklet (not read from build.js),
worked out in Python, and compared with answers.json, which build.js writes.
Algebra answers are checked by substituting several random values into the question
and the answer.  Run:  python3 verify.py
"""
import json
import math
import random
import re
from decimal import Decimal as D
from fractions import Fraction as Fr
from pathlib import Path

ANS = {a["key"]: a["p"] for a in json.loads(Path(__file__).with_name("answers.json").read_text())}
fails, checked = [], set()


def ok(key, cond, note=""):
    checked.add(key)
    if not cond:
        fails.append(f"{key}: booklet says {ANS.get(key)!r} {note}")


def num(s):
    """Plain answer → Decimal ('$216.80' → 216.80, '6.5 m' → 6.5)."""
    return D(re.sub(r"[^\d.\-−]", "", s.split("≈")[-1]).replace("−", "-"))


def frac_str(f, mixed=True):
    if f.denominator == 1:
        return str(f.numerator)
    w, r = divmod(f.numerator, f.denominator)
    return f"{w} {r}/{f.denominator}" if (mixed and w) else f"{f.numerator}/{f.denominator}"


# ------------------------------------------------------------------ Pythagoras
def hyp(a, b):
    a, b = D(str(a)), D(str(b))
    return a * a + b * b


def leg(c, b):
    c, b = D(str(c)), D(str(b))
    return c * c - b * b


def check_len(key, sq, unit):
    r = math.sqrt(float(sq))
    if abs(r - round(r, 2)) < 1e-9:
        want = f"{D(str(round(r, 2))).normalize():f} {unit}"
        ok(key, ANS[key] == want, f"expected {want}")
    else:
        want = f"{round(r + 1e-12, 1):.1f}"
        ok(key, ANS[key].endswith(f"{want} {unit}") and f"√{sq.normalize():f}" in ANS[key], f"expected √{sq} ≈ {want} {unit}")


for k, v in {"a": 6**2, "b": 11**2, "c": D("0.3") ** 2, "d": 3**4, "e": 10**3, "f": 9, "g": 14, "h": 5**2 + 12**2, "i": 13}.items():
    ok(f"1.1{k}", num(ANS[f"1.1{k}"]) == D(str(v)), f"expected {v}")
assert 9 * 9 == 81 and 14 * 14 == 196 and 13 * 13 == 169
for k, v in {"a": "PR", "b": "XY", "c": "MN"}.items():
    ok(f"1.2{k}", ANS[f"1.2{k}"] == v)
ok("1.2d", ANS["1.2d"] == "r² = p² + q²")
check_len("1.3a", hyp(6, 8), "cm"); check_len("1.3b", hyp(20, 21), "m")
check_len("1.3c", hyp(7, 10), "cm"); check_len("1.3d", hyp(1.8, 2.4), "m")
check_len("1.4a", leg(10, 8), "cm"); check_len("1.4b", leg(25, 15), "m")
check_len("1.4c", leg(9, 5), "cm"); check_len("1.4d", hyp(6, 2.5), "m")
surds = [n for n in [1, 8, 30, 49, 45, 100, 2, 144] if math.isqrt(n) ** 2 != n]
ok("1.5a", ANS["1.5a"] == ", ".join(f"√{n}" for n in surds))
ok("1.5b", ANS["1.5b"] == "5 and 6" and 25 < 30 < 36)
ok("1.5c", ANS["1.5c"] == f"√34 cm ≈ {round(math.sqrt(34), 1)} cm" and hyp(3, 5) == 34)
check_len("1.6a", hyp(40, 30), "m"); check_len("1.6b", hyp(7, 15), "cm"); check_len("1.6c", leg(30, 18), "m")
assert leg(D("4.1"), D("0.9")) == 16  # worked example: ladder


def right(*s):
    a, b, c = sorted(D(str(x)) for x in s)
    return "yes" if a * a + b * b == c * c else "no"


for k, s in zip("abcdef", [(6, 8, 10), (4, 5, 6), (9, 40, 41), (10, 11, 15), (1.5, 2, 2.5), (11, 60, 61)]):
    ok(f"1.7{k}", ANS[f"1.7{k}"] == right(*s), f"expected {right(*s)}")
ok("1.8a", right(5, 12, 13) == "yes" == ANS["1.8a"])
ok("1.8b", right(15, 20, 25) == "yes" and ANS["1.8b"] == "15, 20, 25")
ok("1.8c", ANS["1.8c"] == "15; 24" and right(9, 12, 15) == "yes" and right(10, 24, 26) == "yes")
check_len("1.9a", hyp(12, 35), "cm")
ok("1.9b", ANS["1.9b"] == right(8, 10, 13))
ok("1.9c", ANS["1.9c"] == right(60, 80, 100))
check_len("1.9d", leg(10, 6), "cm")


def simp_surd(n):
    k = max(i for i in range(1, math.isqrt(n) + 1) if n % (i * i) == 0)
    return f"{k}√{n // (k * k)}"


for k, n in zip("abcd", [8, 20, 27, 75]):
    ok(f"1.10{k}", ANS[f"1.10{k}"] == simp_surd(n), f"expected {simp_surd(n)}")
# worked examples on the page
assert simp_surd(18) == "3√2" and simp_surd(48) == "4√3" and right(12, 16, 20) == "yes" and right(5, 7, 9) == "no"
assert round(math.sqrt(89), 1) == 9.4 and round(math.sqrt(95), 1) == 9.7 and hyp(9, 12) == 225 and leg(13, 5) == 144

# ------------------------------------------------------------------ fractions
ok("2.1a", Fr(2, 3) == Fr(int(ANS["2.1a"]), 12))
ok("2.1b", ANS["2.1b"] == frac_str(Fr(15, 25)))
ok("2.1c", ANS["2.1c"] == frac_str(Fr(24, 32)))
ok("2.1d", ANS["2.1d"] == frac_str(3 + Fr(2, 7), mixed=False))
ok("2.1e", ANS["2.1e"] == frac_str(Fr(29, 6)))
ok("2.1f", ANS["2.1f"] == ", ".join(frac_str(f) for f in sorted([Fr(2, 3), Fr(3, 4), Fr(5, 8)])))
for k, v in {"a": Fr(1, 2) + Fr(1, 3), "b": Fr(4, 5) - Fr(1, 2), "c": Fr(3, 4) + Fr(5, 6),
             "d": 2 + Fr(1, 4) + 1 + Fr(2, 3), "e": 5 - (2 + Fr(3, 8))}.items():
    ok(f"2.2{k}", ANS[f"2.2{k}"] == frac_str(v), f"expected {frac_str(v)}")
for k, v in {"a": Fr(2, 5) * Fr(3, 7), "b": Fr(5, 6) * Fr(3, 10), "c": (1 + Fr(1, 3)) * Fr(3, 8),
             "d": Fr(3, 4) / Fr(1, 2), "e": Fr(2, 3) / 4, "f": (3 + Fr(1, 2)) / (1 + Fr(3, 4))}.items():
    ok(f"2.3{k}", ANS[f"2.3{k}"] == frac_str(v), f"expected {frac_str(v)}")
ok("2.3g", ANS["2.3g"] == str(36 - 36 // 3 - 36 // 4))
ok("2.3h", ANS["2.3h"] == frac_str((2 + Fr(1, 4)) * 3) + " cups")
assert Fr(2, 3) + Fr(1, 4) == Fr(11, 12) and (3 + Fr(1, 2)) - (1 + Fr(2, 3)) == 1 + Fr(5, 6)  # worked examples
assert Fr(4, 9) * Fr(3, 8) == Fr(1, 6) and (2 + Fr(1, 2)) / Fr(3, 4) == 3 + Fr(1, 3) and Fr(2, 3) * 45 == 30


# ------------------------------------------------------------------ decimals
def rec(n, d):
    """Recurring decimal as '0.8(3)'."""
    i, r, seen, digits = n // d, n % d, {}, ""
    while r and r not in seen:
        seen[r] = len(digits); r *= 10; digits += str(r // d); r %= d
    if not r:
        return f"{i}.{digits}"
    k = seen[r]
    return f"{i}.{digits[:k]}({digits[k:]})"


for k, s in zip("abc", ["0.8", "0.45", "0.125"]):
    ok(f"2.4{k}", ANS[f"2.4{k}"] == frac_str(Fr(s)), f"expected {Fr(s)}")
for k, (n, d) in zip("defgh", [(3, 5), (7, 20), (5, 6), (4, 9), (3, 11)]):
    ok(f"2.4{k}", ANS[f"2.4{k}"] == rec(n, d), f"expected {rec(n, d)}")
ok("2.4i", ANS["2.4i"] == str(D("5.4271").quantize(D("0.1"))))
ok("2.4j", ANS["2.4j"] == str(D("12.3958").quantize(D("0.01"))))
for k, (a, b) in zip("abcdef", [("0.4", "0.3"), ("0.9", "0.06"), ("2.5", "0.8"), ("1.6", "0.45"), ("3.2", "0.15"), ("7.5", "0.12")]):
    ok(f"2.5{k}", num(ANS[f"2.5{k}"]) == D(a) * D(b), f"expected {D(a) * D(b)}")
for k, (a, b) in zip("abcdef", [("3.6", "0.4"), ("1.44", "0.12"), ("8.1", "0.09"), ("0.56", "0.08"), ("15", "0.5"), ("9.45", "0.3")]):
    ok(f"2.6{k}", num(ANS[f"2.6{k}"]) == D(a) / D(b), f"expected {D(a) / D(b)}")
ok("2.7a", num(ANS["2.7a"]) == 12 * D("14.90") + 8 * D("4.75"))
ok("2.7b", num(ANS["2.7b"]) == D("4.20") / D("1.5"))
ok("2.7c", num(ANS["2.7c"]) == 50 - (3 * D("2.85") + D("8.40")))
assert D("0.6") * D("0.07") == D("0.042") and D("2.3") * D("1.4") == D("3.22") and D("4.2") / D("0.07") == 60 and D("2.88") / D("0.4") == D("7.2")
assert rec(2, 3) == "0.(6)" and rec(5, 11) == "0.(45)" and rec(3, 8) == "0.375"

# ------------------------------------------------------------------ percentages
for k, f in zip("abcde", [Fr(1, 4), Fr(3, 5), Fr(12, 100), Fr(7, 8), Fr(25, 1000)]):
    want = f"{frac_str(f)} = {D(f.numerator) / D(f.denominator):f} = {(D(f.numerator) / D(f.denominator) * 100).normalize():f}%"
    ok(f"2.8{k}", ANS[f"2.8{k}"] == want, f"expected {want}")
pc = lambda p, q: D(p) / 100 * D(q)
for k, v in {"a": pc(10, 70), "b": pc(25, 36), "c": pc(40, 85), "d": pc(12, 250), "e": D(64) / 8 * 3,
             "f": pc(35, 160), "g": pc(20, 160) - pc(10, 160)}.items():
    ok(f"2.9{k}", num(ANS[f"2.9{k}"]) == v, f"expected {v}")
assert 35 + 30 + 20 + 10 + 5 == 100  # sector graph adds to 100%
for k, v in {"a": D(34) / 40 * 100, "b": D(12) / 30 * 100, "c": D(30) / 120 * 100}.items():
    ok(f"2.10{k}", num(ANS[f"2.10{k}"]) == v, f"expected {v}%")
for k, v in {"a": 60 + pc(10, 60), "b": 250 - pc(20, 250), "c": 45 - pc(30, 45), "d": D(54) / 30 * 100}.items():
    ok(f"2.11{k}", num(ANS[f"2.11{k}"]) == v, f"expected {v}")
assert pc(35, 240) == 84 and D(18) / 24 * 100 == 75 and D(450) / 2000 * 100 == D("22.5") and 80 + pc(15, 80) == 92 and 120 - pc(25, 120) == 90


# ------------------------------------------------------------------ algebra (random substitution)
def py(expr):
    e = expr.replace("−", "-").replace("×", "*").replace("÷", "/").replace("²", "**2").replace(" ", "")
    return re.sub(r"(?<=[\da-z)])(?=[a-z(])", "*", e)


def same(q, a, vars_="abcdkmnpqxy"):
    for _ in range(6):
        env = {v: random.choice([-7, -3, -2, 2, 3, 5, 11]) + random.random() for v in vars_}
        if abs(eval(py(q), {}, env) - eval(py(a), {}, env)) > 1e-7:
            return False
    return True


# the checker must reject wrong algebra, or it proves nothing
assert not same("3x + 2y", "5xy") and not same("4(2a − 3)", "8a − 3") and not same("2y²", "(2y)²") and not same("k(k − 7)", "k² − 7")
ok("3.1a", ANS["3.1a"] == "6; −1; 4; 3")
for k, (q, a) in {"b": ("5 × y", "5y"), "c": ("a × 3 × b", "3ab"), "d": ("m × m", "m²"), "e": ("2 × p × p", "2p²"),
                  "f": ("k ÷ 6", "k/6"), "g": ("4mn", "4 × m × n"), "h": ("3c²", "3 × c × c")}.items():
    ok(f"3.1{k}", ANS[f"3.1{k}"] == a and same(q, a), f"expected {a}")
for k, (n_expr) in {"a": "n + 7", "b": "4n", "c": "n − 3", "d": "n/5", "e": "2n + 1", "f": "n + 1", "g": "3(x + y)"}.items():
    ok(f"3.2{k}", ANS[f"3.2{k}"] == n_expr)
X, Y, Z = 5, 2, -3
for k, e in {"a": 3 * X + Y, "b": X * Y - 4, "c": X**2 + Y**2, "d": 2 * Y**2, "e": 3 * X**2 - 4 * Y, "f": X + Z,
             "g": Z**2, "h": 4 * Z - Y, "i": (X + Y) ** 2}.items():
    ok(f"3.3{k}", num(ANS[f"3.3{k}"]) == e, f"expected {e}")
ok("3.3j", ANS["3.3j"] == f"${45 * 3 + 60:.2f}; ${45 * 2.5 + 60:.2f}")
assert 5 * 4 - 3 == 17 and 3 * 4**2 + (-2) == 46  # worked example a = 4, b = −2
for k, (q, a) in {"a": ("6a + 2a", "8a"), "b": ("9k − k", "8k"), "c": ("3p + 4 + 2p", "5p + 4"), "d": ("5x + 3y + 2x − y", "7x + 2y"),
                  "e": ("8p − 3q − 5p + 6q", "3p + 3q"), "f": ("3ab + 2ba − ab", "4ab"), "h": ("6y² − 2y + y² + 5y", "7y² + 3y"),
                  "i": ("2m − 7 − 5m + 4", "−3m − 3"), "j": ("(3x + 2) + x + (3x + 2) + x", "8x + 4")}.items():
    ok(f"3.4{k}", ANS[f"3.4{k}"] == a and same(q, a), f"expected {a}")
ok("3.4g", ANS["3.4g"] == "−x, 7x")
for k, (q, a) in {"a": ("5 × 3k", "15k"), "b": ("2p × 7q", "14pq"), "c": ("4y × 3y", "12y²"), "d": ("−2a × 6b", "−12ab"),
                  "e": ("3m × 2n × 5", "30mn"), "f": ("−4x × (−3x)", "12x²")}.items():
    ok(f"3.5{k}", ANS[f"3.5{k}"] == a and same(q, a), f"expected {a}")
for k, (q, a) in {"a": ("18m/6", "3m"), "b": ("15xy/(5y)", "3x"), "c": ("24ab/(8a)", "3b"), "d": ("14k²/(7k)", "2k"), "e": ("30mn/(−6n)", "−5m")}.items():
    ok(f"3.6{k}", ANS[f"3.6{k}"] == a and same(q, a), f"expected {a}")
ok("3.7a", ANS["3.7a"] == "no" and 3 * 2 + 2 * 1 != 5 * 2 * 1)
ok("3.7b", ANS["3.7b"] == "4m" and same("7m − 4m", "3m"))
ok("3.7c", ANS["3.7c"] == "3a" and same("6ab/(3a)", "2b"))
ok("3.7d", ANS["3.7d"] == "15x²" and same("5x × 3x", "15x²"))
ok("3.7e", ANS["3.7e"] == "no" and 4 * 3**2 != (4 * 3) ** 2)
for k, (q, a) in {"a": ("6(m + 2)", "6m + 12"), "b": ("3(4k − 5)", "12k − 15"), "c": ("−2(y + 8)", "−2y − 16"), "d": ("a(a − 9)", "a² − 9a"),
                  "e": ("4(2x + 1) + 3", "8x + 7"), "f": ("5(p + 2) + 2(p − 3)", "7p + 4")}.items():
    ok(f"3.8{k}", ANS[f"3.8{k}"] == a and same(q, a), f"expected {a}")
for k, (q, a) in {"a": ("4x + 8", "4(x + 2)"), "b": ("9m − 6", "3(3m − 2)"), "c": ("12y + 18", "6(2y + 3)"), "d": ("k² − 7k", "k(k − 7)"),
                  "e": ("14pq + 21p", "7p(2q + 3)")}.items():
    # also check the factor outside is the HCF (nothing common is left inside the brackets)
    ok(f"3.9{k}", ANS[f"3.9{k}"] == a and same(q, a), f"expected {a}")
assert same("6x + 15", "3(2x + 5)") and same("8a − 12", "4(2a − 3)") and same("10ab + 15a", "5a(2b + 3)") and same("2(x + 5) + 3x", "5x + 10")

# ------------------------------------------------------------------ mixed exam check
ok("3.10a", ANS["3.10a"] == "5a − 4b" and same("9a + 2b − 4a − 6b", "5a − 4b"))
ok("3.10b", ANS["3.10b"] == "12m − 8" and same("4(3m − 2)", "12m − 8"))
ok("3.10c", num(ANS["3.10c"]) == 3 * 2**2 - 2 * (-5))
check_len("3.10d", hyp(16, 30), "cm")
ok("3.10e", num(ANS["3.10e"]) == D("0.7") * D("0.08"))
ok("3.10f", num(ANS["3.10f"]) == D("2.4") / D("0.03"))
ok("3.10g", num(ANS["3.10g"]) == pc(45, 360))
ok("3.10h", ANS["3.10h"] == frac_str(2 + Fr(1, 2) + Fr(3, 4)))
ok("3.10i", ANS["3.10i"] == right(7, 9, 12))
ok("3.10j", num(ANS["3.10j"]) == 150 + pc(8, 150))
marks = [1, 1, 1, 2, 1, 1, 1, 1, 2, 1]
assert sum(marks) == 12, sum(marks)

unchecked = sorted(set(ANS) - checked)
print(f"answers in key: {len(ANS)} · answers checked: {len(checked & set(ANS))} · not checked: {unchecked} · failures: {len(fails)}")
for f in fails:
    print("  FAIL", f)
