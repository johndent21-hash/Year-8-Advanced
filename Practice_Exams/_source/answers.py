"""Worked answers for the four practice papers.

Data-handling answers (Q10–Q14) are recalculated from the paper data and checked
against the written answers so the key cannot drift from the questions.
"""
from fractions import Fraction
from statistics import median, multimode

from papers import PAPERS

ANSWERS = [
    # ---------------------------------------------------------------- Paper 1
    {
        "1": [("a", "x = 13", "x = 21 − 8"), ("b", "m = 17", "m = 5 + 12"), ("c", "p = 8", "p = 56 ÷ 7"), ("d", "y = 36", "y = 9 × 4")],
        "2": [("a", "x = 7", "5x = 35 (1 mark), x = 35 ÷ 5 = 7 (1 mark)"), ("b", "x = 30", "x ÷ 6 = 5 (1 mark), x = 5 × 6 = 30 (1 mark)")],
        "3": [("", "m = −4", "3m = 2 − 14 = −12 (1 mark), m = −12 ÷ 3 = −4 (1 mark)")],
        "4": [("", "NO", "4 × 6 − 9 = 24 − 9 = 15 (1 mark). 15 ≠ 13, so x = 6 is not the solution (1 mark)")],
        "5": [("a", "3n + 8 = 35", ""), ("b", "n = 9", "3n = 27 (1 mark), n = 9 (1 mark)")],
        "6": [("a", "4t + 7 = 55", ""), ("b", "t = 12, so one ticket costs $12", "4t = 48 (1 mark), t = 12 (1 mark)")],
        "7": [("a", "Mango", ""), ("b", "46 students", "11 + 7 + 14 + 9 + 5 = 46")],
        "8": [("a", "2 pm", ""), ("b", "9°C", "15 − 6 = 9")],
        "9": [("a", "60 students", "30% of 200 = 0.3 × 200 = 60"),
              ("b", "50 students", "Maths 35% of 200 = 70, Art 10% of 200 = 20 (1 mark), 70 − 20 = 50 (1 mark)")],
        "15": [("a", "x = 15 cm", "x² = 9² + 12² = 81 + 144 = 225 (1 mark), x = √225 = 15 (1 mark)"),
               ("b", "YES", "10² + 24² = 100 + 576 = 676 and 26² = 676 (1 mark). They are equal, so it is right-angled (1 mark)")],
        "16": [("a", "0.9", "36 × 25 = 900, 3 decimal places → 0.900"), ("b", "60", "5.4 ÷ 0.09 = 540 ÷ 9 = 60")],
        "17": [("a", "125", "5 × 5 × 5"), ("b", "11", "11 × 11 = 121")],
        "18": [("a", "√18 and √7", "16 and 36 are square numbers, so √16 = 4 and √36 = 6 are not surds"),
               ("b", "4√3", "√48 = √16 × √3 (1 mark) = 4√3 (1 mark)")],
        "19": [("a", "2x + 9y", "6x − 4x = 2x, 2y + 7y = 9y"), ("b", "5a + 15", ""), ("c", "63", "3 × 5² − 2 × 6 = 3 × 25 − 12 = 75 − 12")],
        "20": [("a", "56 cm²", "½ × (6 + 10) × 7 (1 mark) = ½ × 16 × 7 = 56 (1 mark)"), ("b", "80 cm³", "8 × 5 × 2")],
        "21": [("", "y = −5, −2, 1, 4", "e.g. x = −2: 3 × (−2) + 1 = −6 + 1 = −5. 2 marks all correct, 1 mark for 2–3 correct")],
        "22": [("a", "3 : 5", "Divide both by 5 (the HCF)"), ("b", "18 km/h", "72 ÷ 4 = 18")],
    },
    # ---------------------------------------------------------------- Paper 2
    {
        "1": [("a", "x = 17", "x = 30 − 13"), ("b", "m = 27", "m = 19 + 8"), ("c", "p = 7", "p = 63 ÷ 9"), ("d", "y = 48", "y = 8 × 6")],
        "2": [("a", "x = 6", "6x = 36 (1 mark), x = 6 (1 mark)"), ("b", "x = 20", "x ÷ 5 = 4 (1 mark), x = 4 × 5 = 20 (1 mark)")],
        "3": [("", "m = −5", "4m = 5 − 25 = −20 (1 mark), m = −20 ÷ 4 = −5 (1 mark)")],
        "4": [("", "YES", "2 × 5 + 11 = 10 + 11 = 21 (1 mark). 21 = 21, so x = 5 is the solution (1 mark)")],
        "5": [("a", "5n − 9 = 41", ""), ("b", "n = 10", "5n = 50 (1 mark), n = 10 (1 mark)")],
        "6": [("a", "6h + 8 = 38", ""), ("b", "h = 5, so Ava hired the bike for 5 hours", "6h = 30 (1 mark), h = 5 (1 mark)")],
        "7": [("a", "Thursday", ""), ("b", "100 books", "15 + 25 + 10 + 30 + 20 = 100")],
        "8": [("a", "2 pm", ""), ("b", "35 people", "50 − 15 = 35")],
        "9": [("a", "56 people", "35% of 160 = 0.35 × 160 = 56"),
              ("b", "64 people", "Dog 45% of 160 = 72, Bird 5% of 160 = 8 (1 mark), 72 − 8 = 64 (1 mark)")],
        "15": [("a", "x = 20 cm", "x² = 12² + 16² = 144 + 256 = 400 (1 mark), x = √400 = 20 (1 mark)"),
               ("b", "NO", "6² + 9² = 36 + 81 = 117 but 11² = 121 (1 mark). 117 ≠ 121, so it is not right-angled (1 mark)")],
        "16": [("a", "0.39", "26 × 15 = 390, 3 decimal places → 0.390"), ("b", "120", "9.6 ÷ 0.08 = 960 ÷ 8 = 120")],
        "17": [("a", "32", "2 × 2 × 2 × 2 × 2"), ("b", "12", "12 × 12 = 144")],
        "18": [("a", "√20 and √30", "49 and 100 are square numbers, so √49 = 7 and √100 = 10 are not surds"),
               ("b", "6√2", "√72 = √36 × √2 (1 mark) = 6√2 (1 mark)")],
        "19": [("a", "10m + 4n", "7m + 3m = 10m, −2n + 6n = 4n"), ("b", "4y − 20", ""), ("c", "20", "3 × 3² − 7 = 3 × 9 − 7 = 27 − 7")],
        "20": [("a", "66 cm²", "½ × (9 + 13) × 6 (1 mark) = ½ × 22 × 6 = 66 (1 mark)"), ("b", "180 cm³", "12 × 3 × 5")],
        "21": [("", "y = −9, −5, −1, 3", "e.g. x = −2: 4 × (−2) − 1 = −8 − 1 = −9. 2 marks all correct, 1 mark for 2–3 correct")],
        "22": [("a", "5 : 8", "Divide both by 4 (the HCF)"), ("b", "90 km/h", "450 ÷ 5 = 90")],
    },
    # ---------------------------------------------------------------- Paper 3
    {
        "1": [("a", "x = 14", "x = 33 − 19"), ("b", "m = 34", "m = 23 + 11"), ("c", "p = 9", "p = 72 ÷ 8"), ("d", "y = 33", "y = 11 × 3")],
        "2": [("a", "x = 6", "7x = 42 (1 mark), x = 6 (1 mark)"), ("b", "x = 32", "x ÷ 4 = 8 (1 mark), x = 8 × 4 = 32 (1 mark)")],
        "3": [("", "m = −6", "5m = 2 − 32 = −30 (1 mark), m = −30 ÷ 5 = −6 (1 mark)")],
        "4": [("", "NO", "5 × 7 − 8 = 35 − 8 = 27 (1 mark). 27 ≠ 26, so x = 7 is not the solution (1 mark)")],
        "5": [("a", "6n + 11 = 59", ""), ("b", "n = 8", "6n = 48 (1 mark), n = 8 (1 mark)")],
        "6": [("a", "9s + 65 = 290", ""), ("b", "s = 25, so 25 students went", "9s = 225 (1 mark), s = 25 (1 mark)")],
        "7": [("a", "Pepperoni", ""), ("b", "41 students", "8 + 13 + 6 + 10 + 4 = 41")],
        "8": [("a", "15 minutes", ""), ("b", "45°C", "90 − 45 = 45")],
        "9": [("a", "72 students", "30% of 240 = 0.3 × 240 = 72"),
              ("b", "96 students", "Pop 50% of 240 = 120, Rock 10% of 240 = 24 (1 mark), 120 − 24 = 96 (1 mark)")],
        "15": [("a", "x = 10.8 cm", "x² = 6² + 9² = 36 + 81 = 117 (1 mark), x = √117 = 10.816… ≈ 10.8 (1 mark)"),
               ("b", "YES", "9² + 40² = 81 + 1600 = 1681 and 41² = 1681 (1 mark). They are equal, so it is right-angled (1 mark)")],
        "16": [("a", "0.5", "125 × 4 = 500, 3 decimal places → 0.500"), ("b", "6", "4.2 ÷ 0.7 = 42 ÷ 7 = 6")],
        "17": [("a", "1000", "10 × 10 × 10"), ("b", "15", "15 × 15 = 225")],
        "18": [("a", "√27 and √14", "81 and 64 are square numbers, so √81 = 9 and √64 = 8 are not surds"),
               ("b", "5√3", "√75 = √25 × √3 (1 mark) = 5√3 (1 mark)")],
        "19": [("a", "5k + 8", "9k − 4k = 5k, 5 + 3 = 8"), ("b", "12x + 6", ""), ("c", "6", "5 × 2² − 2 × 7 = 5 × 4 − 14 = 20 − 14")],
        "20": [("a", "36 cm²", "½ × (11 + 7) × 4 (1 mark) = ½ × 18 × 4 = 36 (1 mark)"), ("b", "360 cm³", "6 × 6 × 10")],
        "21": [("", "y = −8, −3, 2, 7", "e.g. x = −2: 5 × (−2) + 2 = −10 + 2 = −8. 2 marks all correct, 1 mark for 2–3 correct")],
        "22": [("a", "2 : 3", "Divide both by 14 (the HCF)"), ("b", "12 km/h", "30 ÷ 2.5 = 12")],
    },
    # ---------------------------------------------------------------- Paper 4
    {
        "1": [("a", "x = 26", "x = 50 − 24"), ("b", "m = 23", "m = 6 + 17"), ("c", "p = 7", "p = 84 ÷ 12"), ("d", "y = 40", "y = 5 × 8")],
        "2": [("a", "x = 6", "8x = 48 (1 mark), x = 6 (1 mark)"), ("b", "x = 14", "x ÷ 2 = 7 (1 mark), x = 7 × 2 = 14 (1 mark)")],
        "3": [("", "m = −7", "2m = 5 − 19 = −14 (1 mark), m = −14 ÷ 2 = −7 (1 mark)")],
        "4": [("", "YES", "6 × 3 + 4 = 18 + 4 = 22 (1 mark). 22 = 22, so x = 3 is the solution (1 mark)")],
        "5": [("a", "n ÷ 2 + 7 = 19", "also accept n/2 + 7 = 19"), ("b", "n = 24", "n ÷ 2 = 12 (1 mark), n = 24 (1 mark)")],
        "6": [("a", "25m + 40 = 290", ""), ("b", "m = 10, so Zara had the plan for 10 months", "25m = 250 (1 mark), m = 10 (1 mark)")],
        "7": [("a", "March", ""), ("b", "45 cars", "9 + 6 + 12 + 7 + 11 = 45")],
        "8": [("a", "4 am", ""), ("b", "10°C", "8 − (−2) = 8 + 2 = 10")],
        "9": [("a", "30 students", "10% of 300 = 30"),
              ("b", "90 students", "Gaming 35% of 300 = 105, Reading 5% of 300 = 15 (1 mark), 105 − 15 = 90 (1 mark)")],
        "15": [("a", "x = 34 cm", "x² = 16² + 30² = 256 + 900 = 1156 (1 mark), x = √1156 = 34 (1 mark)"),
               ("b", "NO", "5² + 11² = 25 + 121 = 146 but 12² = 144 (1 mark). 146 ≠ 144, so it is not right-angled (1 mark)")],
        "16": [("a", "0.056", "7 × 8 = 56, 3 decimal places → 0.056"), ("b", "90", "8.1 ÷ 0.09 = 810 ÷ 9 = 90")],
        "17": [("a", "216", "6 × 6 × 6"), ("b", "14", "14 × 14 = 196")],
        "18": [("a", "√45 and √8", "1 and 121 are square numbers, so √1 = 1 and √121 = 11 are not surds"),
               ("b", "4√5", "√80 = √16 × √5 (1 mark) = 4√5 (1 mark)")],
        "19": [("a", "2x² + 7x", "3x² − x² = 2x², 5x + 2x = 7x (x² and x are NOT like terms)"),
               ("b", "−2x + 12", "−2 × x = −2x, −2 × (−6) = +12"),
               ("c", "31", "4 × (−2)² + 3 × 5 = 4 × 4 + 15 = 16 + 15")],
        "20": [("a", "42 cm²", "½ × (5.5 + 8.5) × 6 (1 mark) = ½ × 14 × 6 = 42 (1 mark)"), ("b", "150 cm³", "15 × 4 × 2.5")],
        "21": [("", "y = 3, 1, −1, −3", "e.g. x = −1: −2 × (−1) + 1 = 2 + 1 = 3. 2 marks all correct, 1 mark for 2–3 correct")],
        "22": [("a", "3 : 4", "Divide both by 15 (the HCF)"), ("b", "78 km/h", "117 ÷ 1.5 = 78")],
    },
]


def _num(x):
    x = Fraction(x).limit_denominator(1000)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):g}"


def stem_values(rows):
    return [s * 10 + int(l) for s, leaves in rows for l in leaves.split()]


def data_answers(d):
    """Answers for Q10–Q14, derived from the paper data."""
    out = {}
    vals = stem_values(d["q10"]["rows"])
    n = len(vals)
    med = median(vals)
    b = d["q10"]["b"]
    import re
    k = int(re.search(r"(\d+)", b.split("than")[-1] if "than" in b else b.split("least")[-1]).group(1))
    cnt = sum(v > k for v in vals) if "than" in b else sum(v >= k for v in vals)
    pos = f"{(n + 1) // 2}th value" if n % 2 else f"average of the {n // 2}th and {n // 2 + 1}th values"
    out["10"] = [("a", _num(med), f"{n} values, so the median is the {pos}"),
                 ("b", str(cnt), ("values above " if "than" in b else "values of ") + f"{k}" + ("" if "than" in b else " or more") + ": " + ", ".join(str(v) for v in vals if (v > k if "than" in b else v >= k)))]
    q = d["q11"]
    mode = q["values"][q["counts"].index(max(q["counts"]))]
    b = q["b"]
    k = int(re.search(r"(?:least|than) (\d+)", b).group(1))
    if "least" in b:
        c = sum(cn for v, cn in zip(q["values"], q["counts"]) if v >= k)
        note = f"Count the dots at {k} and above"
    else:
        c = sum(cn for v, cn in zip(q["values"], q["counts"]) if v > k)
        note = f"Count the dots above {k} (not including {k})"
    out["11"] = [("a", str(mode), "The tallest column of dots"), ("b", str(c), note)]
    q = d["q12"]
    tot = sum(q["freq"])
    mode = q["values"][q["freq"].index(max(q["freq"]))]
    out["12"] = [("a", str(tot), " + ".join(map(str, q["freq"])) + f" = {tot}"),
                 ("b", str(mode), f"{mode} has the highest frequency ({max(q['freq'])}) – the answer is the value, not the frequency")]
    data = d["q13"]["data"]
    s, n = sum(data), len(data)
    srt = sorted(data)
    mm = multimode(data)
    out["13"] = [("a", _num(Fraction(s, n)), f"Total = {s} (1 mark), {s} ÷ {n} = {_num(Fraction(s, n))} (1 mark)"),
                 ("b", _num(median(data)), "In order: " + ", ".join(map(str, srt)) + f". Middle two values: {srt[n//2-1]} and {srt[n//2]}"),
                 ("c", str(mm[0]), "Appears most often"),
                 ("d", str(max(data) - min(data)), f"{max(data)} − {min(data)}")]
    data = d["q14"]["data"]
    s, n = sum(data), len(data)
    srt = sorted(data)
    out_v = max(data, key=lambda v: abs(v - median(data)))
    rest = [v for v in data if v != out_v]
    rmean = Fraction(sum(rest), len(rest))
    higher = out_v > median(data)
    out["14"] = [("a", str(out_v), "Much further from the other values than any other score"),
                 ("b", _num(Fraction(s, n)), f"{s} ÷ {n}"),
                 ("c", "Higher" if higher else "Lower",
                  f"The outlier is much {'larger' if higher else 'smaller'} than the rest, so it pulls the mean "
                  f"{'up' if higher else 'down'}. Without it the mean is about {float(rmean):.1f}.")]
    return out


def full_answers(i):
    a = dict(ANSWERS[i])
    a.update(data_answers(PAPERS[i]))
    return a


EXPECTED = [  # hand-checked values, used to catch any data/answer drift
    {"10": ["27", "6"], "11": ["1", "6"], "12": ["38", "3"], "13": ["11", "10", "9", "11"], "14": ["34", "11", "Higher"]},
    {"10": ["26", "4"], "11": ["1", "7"], "12": ["40", "2"], "13": ["22", "22.5", "24", "15"], "14": ["4", "21", "Lower"]},
    {"10": ["26.5", "6"], "11": ["2", "7"], "12": ["32", "1"], "13": ["7", "7.5", "8", "8"], "14": ["460", "180", "Higher"]},
    {"10": ["61", "5"], "11": ["3", "6"], "12": ["25", "1"], "13": ["24", "24", "19", "12"], "14": ["8", "37", "Lower"]},
]

for i, exp in enumerate(EXPECTED):
    got = data_answers(PAPERS[i])
    for q, vals in exp.items():
        assert [x[1] for x in got[q]] == vals, (i + 1, q, got[q], vals)
