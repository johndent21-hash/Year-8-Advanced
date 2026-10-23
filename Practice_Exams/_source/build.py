"""Builds the practice exam papers and answer key as HTML, ready for printing to PDF.

Usage: python3 build.py <out_dir>
"""
import os
import sys
from fractions import Fraction

from charts import dot_plot, right_triangle
from layout import part, question, fig, section, cover, page
from papers import PAPERS
from answers import full_answers
from layout import LOGO

MARKS = (18, 21, 21)
MINUTES = 60


def table_row(head, cells, cls=""):
    return f"<tr><td class='h'>{head}</td>" + "".join(f"<td class='{cls}'>{c}</td>" for c in cells) + "</tr>"


def build_paper(n, d):
    A = []
    body = "".join(part(eq, 1, label="abcd"[i], blank=f"{v} =", work=1) for i, (v, eq) in enumerate(d["q1"]))
    A.append(question(1, "One-step equations", 4, body, intro="Solve each equation."))
    body = "".join(part(eq, 2, label="ab"[i], work=3, end=f"{v} =") for i, (v, eq) in enumerate(d["q2"]))
    A.append(question(2, "Two-step equations", 4, body, intro="Solve each equation, showing your working."))
    v, eq = d["q3"]
    A.append(question(3, "Equations with a negative solution", 2, part("", 0, work=3, end=f"{v} ="), intro=f"Solve {eq}."))
    val, eq = d["q4"]
    body = part("", 0, work=4) + f"<div class='circle'>Is {val} the solution? (circle one) <span>YES</span><span>/</span><span>NO</span></div>"
    A.append(question(4, "Checking solutions", 2, body, intro=f"Use substitution to show whether {val} is the solution to {eq}."))
    body = (part("Write an equation to represent this problem. Use <i>n</i> for the number.", 1, label="a", end="Equation:")
            + part("Solve your equation to find the number.", 2, label="b", work=3, end="n ="))
    A.append(question(5, "Worded problem", 3, body, intro=d["q5"]))
    q6 = d["q6"]
    body = (part("Write an equation to represent this situation.", 1, label="a", end="Equation:")
            + part(f"Solve your equation to find {q6['ask']}.", 2, label="b", work=3, end=f"{q6['var']} ="))
    A.append(question(6, "Worded problem", 3, body, intro=q6["text"]))

    B = []
    q = d["q7"]
    body = fig(q["chart"]) + part(q["a"], 1, label="a", blank="") + part(q["b"], 1, label="b", blank="", work=1)
    B.append(question(7, "Column graph", 2, body, intro=q["intro"]))
    q = d["q8"]
    body = fig(q["chart"]) + part(q["a"], 1, label="a", blank="") + part(q["b"], 1, label="b", work=1, end="Answer:")
    B.append(question(8, "Line graph", 2, body, intro=q["intro"]))
    q = d["q9"]
    body = fig(q["chart"]) + part(q["a"], 1, label="a", work=1, end="Answer:") + part(q["b"], 2, label="b", work=3, end="Answer:")
    B.append(question(9, "Sector (pie) graph", 3, body, intro=q["intro"]))
    q = d["q10"]
    rows = "".join(f"<tr><td class='h'>{s}</td><td style='text-align:left;min-width:150px'>{l}</td></tr>" for s, l in q["rows"])
    tbl = f"<table class='dt'><tr><th>Stem</th><th>Leaf</th></tr>{rows}</table><div class='key'>Key: {q['key']}</div>"
    body = tbl + part("Find the median.", 1, label="a", blank="", work=1) + part(q["b"], 1, label="b", blank="")
    B.append(question(10, "Stem-and-leaf plot", 2, body, intro=q["intro"]))
    q = d["q11"]
    body = fig(dot_plot(q["title"], q["values"], q["counts"], q["xlabel"])) + part("What is the mode?", 1, label="a", blank="") + part(q["b"], 1, label="b", blank="")
    B.append(question(11, "Dot plot", 2, body, intro=q["intro"]))
    q = d["q12"]
    tbl = f"<table class='dt'>{table_row(q['head'], q['values'])}{table_row('Frequency', q['freq'])}</table>"
    body = tbl + part(q["total"], 1, label="a", blank="", work=1) + part("What is the mode?", 1, label="b", blank="")
    B.append(question(12, "Frequency table", 2, body, intro=q["intro"]))
    q = d["q13"]
    body = (f"<div class='data'>{', '.join(map(str, q['data']))}</div>"
            + part("Calculate the mean.", 2, label="a", work=3, end="Mean =")
            + part("Find the median.", 1, label="b", blank="", work=1)
            + part("Find the mode.", 1, label="c", blank="")
            + part("Find the range.", 1, label="d", blank="", work=1))
    B.append(question(13, "Mean, median, mode and range", 5, body, intro=q["intro"]))
    q = d["q14"]
    body = (f"<div class='data'>{', '.join(map(str, q['data']))}</div>"
            + part("Identify the outlier in this data set.", 1, label="a", blank="")
            + part("Calculate the mean of the data, including the outlier.", 1, label="b", work=2, end="Mean =")
            + part("Does the outlier make the mean higher or lower than most of the data values? Explain your answer.", 1, label="c", work=2))
    B.append(question(14, "Outliers", 3, body, intro=q["intro"]))

    C = []
    q = d["q15"]
    rnd = " Give your answer correct to one decimal place." if q.get("round1") else ""
    body = (part(f"Find the length of the hypotenuse, <i>x</i>, in the triangle below.{rnd}", 2, label="a",
                 extra=fig(right_triangle(q["left"], q["bottom"])))
            + "<div class='wline'>Working:<span class='fill'></span></div><div class='line'></div><div class='line'></div>"
            + "<div class='endans'>x = <span class='bl'></span></div>"
            + part(f"A triangle has side lengths {q['test']}. Is it a right-angled triangle? Show working.", 2, label="b", work=4))
    C.append(question(15, "Pythagoras' Theorem", 4, body))
    a, b = d["q16"]
    body = part(f"Calculate {a}", 1, label="a", blank="", work=2) + part(f"Calculate {b}", 1, label="b", blank="", work=2)
    C.append(question(16, "Decimals", 2, body))
    a, b = d["q17"]
    body = part(f"Evaluate {a}", 1, label="a", blank="", work=1) + part(f"Evaluate {b}", 1, label="b", blank="", work=1)
    C.append(question(17, "Powers and roots", 2, body))
    opts, s = d["q18"]
    circ = "&nbsp;&nbsp;&nbsp;&nbsp;".join(opts)
    body = part(f"Circle the surds:&nbsp;&nbsp;&nbsp;&nbsp;{circ}", 1, label="a") + part(f"Simplify {s}", 2, label="b", work=3, end="Answer:")
    C.append(question(18, "Surds", 3, body))
    a, b, c = d["q19"]
    body = (part(f"Simplify {a}", 1, label="a", blank="", work=1) + part(f"Expand {b}", 1, label="b", blank="", work=1)
            + part(f"Evaluate {c}.", 1, label="c", blank="", work=2))
    C.append(question(19, "Algebra", 3, body))
    q = d["q20"]
    t, p = q["trap"], q["prism"]
    body = (part(f"Find the area of a trapezium with parallel sides {t[0]} and {t[1]} and height {t[2]}.", 2, label="a")
            + "<div class='formula'>Formula: Area = ½ × (a + b) × h, where a and b are the parallel sides and h is the perpendicular height.</div>"
            + "<div class='wline'>Working:<span class='fill'></span></div><div class='line'></div><div class='line'></div>"
            + "<div class='endans'>Answer: <span class='bl'></span></div>"
            + part(f"Find the volume of a rectangular prism that is {p[0]} long, {p[1]} wide and {p[2]} high.", 1, label="b", work=2, end="Answer:"))
    C.append(question(20, "Area and volume", 3, body))
    q = d["q21"]
    tbl = f"<table class='dt tall'>{table_row('x', q['xs'])}{table_row('y', [''] * len(q['xs']))}</table>"
    C.append(question(21, "Linear relationships", 2, tbl, intro=f"Complete the table of values for the rule {q['rule']}."))
    r, sp = d["q22"]
    body = part(f"Write the ratio {r} in simplest form.", 1, label="a", blank="", work=2) + part(sp, 1, label="b", work=2, end="Answer:")
    C.append(question(22, "Rates and ratios", 2, body))

    html = (cover(n, MARKS, MINUTES)
            + section("A", "Equations", MARKS[0], 20, "".join(A))
            + section("B", "Investigating Data", MARKS[1], 20, "".join(B))
            + section("C", "Mixed Topics", MARKS[2], 20, "".join(C) + "<div class='end'>END OF EXAMINATION PAPER</div>"))
    return page(f"Year 8 Practice Examination {n}", html)


TITLES = {
    "1": "One-step equations", "2": "Two-step equations", "3": "Negative solution", "4": "Checking solutions",
    "5": "Worded problem", "6": "Worded problem", "7": "Column graph", "8": "Line graph", "9": "Sector graph",
    "10": "Stem-and-leaf plot", "11": "Dot plot", "12": "Frequency table", "13": "Mean, median, mode, range",
    "14": "Outliers", "15": "Pythagoras' theorem", "16": "Decimals", "17": "Powers and roots", "18": "Surds",
    "19": "Algebra", "20": "Area and volume", "21": "Linear relationships", "22": "Rates and ratios",
}
SECTION_OF = {**{str(i): "A – Equations" for i in range(1, 7)}, **{str(i): "B – Investigating Data" for i in range(7, 15)},
              **{str(i): "C – Mixed Topics" for i in range(15, 23)}}

ANS_CSS = """
.ak h1 { font-size: 15pt; margin: 0 0 2px; }
.ak .sub { font-style: italic; font-size: 9pt; margin-bottom: 8px; }
.ak { break-after: page; }
.ak:last-child { break-after: auto; }
table.ans { width: 100%; border-collapse: collapse; font-size: 8.6pt; }
table.ans td { border: 1px solid #999; padding: 3px 6px; vertical-align: top; }
table.ans td.q { width: 1.05in; font-weight: bold; }
table.ans td.p { width: 0.25in; text-align: center; }
table.ans td.a { width: 1.9in; font-weight: bold; }
table.ans td.w { color: #222; }
table.ans tr.sh td { background: #e8eef6; font-weight: bold; border-color: #999; }
.akhead { display: flex; justify-content: space-between; align-items: center; border-bottom: 1.3px solid #000; padding-bottom: 6px; margin-bottom: 8px; }
.akhead img { height: 0.55in; clip-path: inset(0 52% 0 0); margin-right: -2.9in; }
"""


def build_answers():
    blocks = []
    for i in range(len(PAPERS)):
        a = full_answers(i)
        rows, last = [], None
        for q in map(str, range(1, 23)):
            if SECTION_OF[q] != last:
                last = SECTION_OF[q]
                rows.append(f"<tr class='sh'><td colspan='4'>Section {last}</td></tr>")
            parts = a[q]
            for k, (lab, ans, work) in enumerate(parts):
                qcell = f"<td class='q' rowspan='{len(parts)}'>Q{q} {TITLES[q]}</td>" if k == 0 else ""
                rows.append(f"<tr>{qcell}<td class='p'>{lab}</td><td class='a'>{ans}</td><td class='w'>{work}</td></tr>")
        blocks.append(f"""<div class='ak'><div class='akhead'><img src='{LOGO}'><div style='text-align:right'>
            <b>Year 8 Mathematics</b><br>Practice Examination {i + 1} – Answers and marking guide</div></div>
            <h1>Practice Examination {i + 1} – Answers</h1>
            <div class='sub'>Total 60 marks. Award method marks shown in brackets; an answer without working earns the final mark only.</div>
            <table class='ans'>{''.join(rows)}</table></div>""")
    return page("Year 8 Practice Examinations – Answers", "".join(blocks), ANS_CSS)


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for i, d in enumerate(PAPERS, 1):
        with open(os.path.join(out, f"paper{i}.html"), "w") as f:
            f.write(build_paper(i, d))
    with open(os.path.join(out, "answers.html"), "w") as f:
        f.write(build_answers())
    print("built", len(PAPERS))
