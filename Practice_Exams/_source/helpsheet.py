"""Student help sheet covering every skill on the Year 8 Yearly Exam Skills Checklist."""
import os
import sys

from charts import right_triangle
from layout import LOGO

CSS = """
@page { size: Letter; margin: 0.55in 0.6in 0.55in 0.6in; }
* { box-sizing: border-box; }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 8.9pt; color: #111; margin: 0; line-height: 1.32; }
.head { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #1f5fa8; padding-bottom: 6px; margin-bottom: 8px; }
.head img { height: 0.6in; clip-path: inset(0 52% 0 0); margin-right: -3.1in; }
.head .t { text-align: right; }
.head .t b { font-size: 15pt; color: #1f5fa8; display: block; }
.intro { font-size: 8.6pt; margin: 0 0 8px; }
h2 { font-size: 11pt; color: #fff; background: #1f5fa8; padding: 4px 8px; margin: 10px 0 6px; break-after: avoid; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; }
.box { border: 1px solid #9db5d6; border-radius: 4px; padding: 6px 8px; break-inside: avoid; background: #fff; }
.box h4 { margin: 0 0 3px; font-size: 9.2pt; color: #1f5fa8; }
.box h4 .sk { float: right; font-weight: normal; font-size: 7.6pt; color: #666; }
.box p { margin: 2px 0; }
.box ul, .box ol { margin: 2px 0; padding-left: 16px; }
.ex { background: #f2f6fb; border-left: 3px solid #1f5fa8; padding: 3px 6px; margin: 4px 0 2px; font-family: 'Liberation Mono', monospace; font-size: 8.2pt; white-space: pre; line-height: 1.35; }
.tip { font-size: 8.2pt; color: #7a3b00; margin-top: 3px; }
.tip::before { content: "Watch out: "; font-weight: bold; }
.wide { grid-column: 1 / -1; }
table.mini { border-collapse: collapse; font-size: 8.2pt; margin: 3px 0; }
table.mini td, table.mini th { border: 1px solid #9db5d6; padding: 2px 6px; text-align: center; }
table.mini th { background: #e8eef6; }
table.mini.sm td, table.mini.sm th { padding: 1px 3px; font-size: 7.4pt; }
.formula { font-weight: bold; font-size: 9.6pt; text-align: center; margin: 3px 0; }
.pb { break-before: page; }
.foot { margin-top: 8px; font-size: 7.8pt; color: #555; text-align: center; }
"""


def box(title, skills, body, cls=""):
    return f"<div class='box {cls}'><h4>{title}<span class='sk'>{skills}</span></h4>{body}</div>"


def ex(text):
    return f"<div class='ex'>{text.strip(chr(10))}</div>"


def tip(text):
    return f"<div class='tip'>{text}</div>"


SECTION_A = [
    box("Inverse operations", "Skill 1 · Q1",
        "<p>To get the pronumeral on its own, <b>do the opposite</b> to both sides.</p>"
        "<table class='mini'><tr><th>If you see</th><td>+</td><td>−</td><td>×</td><td>÷</td></tr>"
        "<tr><th>Do</th><td>−</td><td>+</td><td>÷</td><td>×</td></tr></table>"
        + ex("a + 11 = 26      k − 4 = 13\na = 26 − 11      k = 13 + 4\na = 15           k = 17\n\n5w = 45          r ÷ 3 = 12\nw = 45 ÷ 5       r = 12 × 3\nw = 9            r = 36")),
    box("Two-step equations", "Skill 2 · Q2",
        "<ol><li>Undo the <b>+ or −</b> first.</li><li>Then undo the <b>× or ÷</b>.</li></ol>"
        + ex("2x + 9 = 25          x ÷ 4 − 2 = 3\n  2x = 25 − 9          x ÷ 4 = 3 + 2\n  2x = 16              x ÷ 4 = 5\n   x = 8                 x = 5 × 4 = 20")
        + tip("write each step on a new line – each step can earn a mark.")),
    box("Negative solutions", "Skill 3 · Q3",
        "<p>Solve exactly the same way. If you take a bigger number from a smaller one, the answer is negative.</p>"
        + ex("4k + 23 = 3\n  4k = 3 − 23 = −20\n   k = −20 ÷ 4 = −5")
        + tip("a negative ÷ a positive gives a negative.")),
    box("Checking a solution (substitution)", "Skill 4 · Q4",
        "<ol><li>Replace the pronumeral with the value.</li><li>Work out the left-hand side.</li>"
        "<li>Compare with the right-hand side and write a conclusion.</li></ol>"
        + ex("Is a = 5 the solution to 7a − 3 = 32?\n  LHS = 7 × 5 − 3 = 35 − 3 = 32\n  RHS = 32\n  LHS = RHS, so YES, a = 5 is the solution.")),
    box("“Think of a number” problems", "Skills 5, 7 · Q5",
        "<p>Write the operations <b>in the order they happen</b>, then put “= answer”.</p>"
        "<table class='mini'><tr><th>Words</th><th>Write</th></tr>"
        "<tr><td>multiply by 7</td><td>7n</td></tr><tr><td>divide by 3</td><td>n ÷ 3</td></tr>"
        "<tr><td>add 5 / increase by 5</td><td>+ 5</td></tr><tr><td>subtract 2 / take away 2</td><td>− 2</td></tr>"
        "<tr><td>the answer is 40</td><td>= 40</td></tr></table>"
        + ex("“Multiply by 7 then subtract 2. The answer is 40.”\n  7n − 2 = 40  →  7n = 42  →  n = 6")),
    box("Real-life equations", "Skills 6, 7 · Q6",
        "<p>Total = (price each × how many) + fixed amount</p>"
        + ex("A gym charges $30 to join plus $12 per week.\nOli paid $114. Let w = number of weeks.\n  12w + 30 = 114\n  12w = 84\n    w = 7   → Oli was a member for 7 weeks.")
        + tip("finish with a sentence and units ($, hours, students).")),
]

SECTION_B = [
    box("Reading any graph", "Skills 8–11",
        "<ul><li>Read the <b>title</b>, axis labels and units first.</li><li>Check the <b>scale</b> – how much is each grid line worth?</li>"
        "<li>Use a ruler to line up the top of a column or a point with the axis.</li></ul>"),
    box("Column graphs", "Skill 8 · Q7",
        "<ul><li><b>Most popular</b> = tallest column.</li><li><b>Altogether / total</b> = add the heights of <b>every</b> column.</li></ul>"
        + ex("Heights 6, 10, 3, 8  →  total = 6 + 10 + 3 + 8 = 27")),
    box("Line graphs", "Skill 9 · Q8",
        "<p><b>Change</b> = later value − earlier value. A rise is an increase, a fall is a decrease.</p>"
        + ex("9 am: 7°C,  3 pm: 19°C  →  rise = 19 − 7 = 12°C\n10 pm: 2°C,  5 am: −3°C →  fall = 2 − (−3) = 5°C")
        + tip("subtracting a negative is the same as adding.")),
    box("Sector (pie) graphs", "Skills 10, 11 · Q9",
        "<p>Amount = <b>percentage × total</b>. To change a % to a decimal, divide by 100.</p>"
        + ex("45% of 80 = 0.45 × 80 = 36")
        + "<p><b>How many more</b>: subtract the percentages first, then find that % of the total.</p>"
        + ex("Soccer 45%, Tennis 15%, total 80\n  45% − 15% = 30%   →  0.3 × 80 = 24 more")),
    box("Stem-and-leaf plots", "Skills 12, 13 · Q10",
        "<p>Use the <b>key</b>: if 3 | 6 means 36, the stem is the tens and each leaf is the units. "
        "Each leaf is one value, so <b>count the leaves</b> to find how many values.</p>"
        "<table class='mini'><tr><th>Stem</th><th>Leaf</th></tr><tr><td>5</td><td style='text-align:left'>1 4 4</td></tr>"
        "<tr><td>6</td><td style='text-align:left'>0 2 7 8</td></tr></table>"
        "<p>Values: 51, 54, 54, 60, 62, 67, 68 (7 values → median is the 4th = 60).</p>"),
    box("Dot plots", "Skill 14 · Q11",
        "<ul><li>Each dot is <b>one</b> person or result.</li><li><b>Mode</b> = the value with the tallest stack of dots.</li>"
        "<li>Total = count every dot.</li></ul>"),
    box("“At least” and “more than”", "Skill 15 · Q10–Q12",
        "<table class='mini'><tr><th>Words</th><th>Means</th><th>Example with 4</th></tr>"
        "<tr><td>at least 4</td><td>4 or more (≥)</td><td>4, 5, 6, …</td></tr>"
        "<tr><td>more than 4</td><td>bigger than 4 (&gt;)</td><td>5, 6, 7, …</td></tr>"
        "<tr><td>at most 4</td><td>4 or less (≤)</td><td>…, 3, 4</td></tr>"
        "<tr><td>fewer than 4</td><td>smaller than 4 (&lt;)</td><td>…, 2, 3</td></tr></table>"
        + tip("“more than 40” does NOT include 40 itself.")),
    box("Frequency tables", "Skill 16 · Q12",
        "<table class='mini'><tr><th>Score</th><td>1</td><td>2</td><td>3</td><td>4</td></tr>"
        "<tr><th>Frequency</th><td>5</td><td>12</td><td>7</td><td>2</td></tr></table>"
        "<ul><li><b>Total surveyed</b> = add the frequencies: 5 + 12 + 7 + 2 = 26</li>"
        "<li><b>Mode</b> = the score with the highest frequency = <b>2</b> (not 12!)</li>"
        "<li><b>At least 3</b> = 7 + 2 = 9</li></ul>"),
    box("Mean, median, mode and range", "Skills 17–19 · Q13",
        "<table class='mini' style='width:100%'><tr><th>Mean</th><td style='text-align:left'>add all the values ÷ how many values</td></tr>"
        "<tr><th>Median</th><td style='text-align:left'>put in order, find the middle value</td></tr>"
        "<tr><th>Mode</th><td style='text-align:left'>the value that appears most often</td></tr>"
        "<tr><th>Range</th><td style='text-align:left'>highest − lowest</td></tr></table>"
        + ex("Data: 7, 3, 10, 4, 10, 6   (6 values)\nMean   = 40 ÷ 6 = 6.67 (2 d.p.)\nOrder  = 3, 4, 6, 7, 10, 10\nMedian = (6 + 7) ÷ 2 = 6.5   ← even number of values\nMode   = 10        Range = 10 − 3 = 7")
        + tip("for an even number of values the median is halfway between the two middle values.")),
    box("Outliers", "Skill 20 · Q14",
        "<p>An <b>outlier</b> is a value much bigger or much smaller than the rest.</p>"
        + ex("Data: 21, 19, 22, 20, 78\n78 is the outlier.\nMean with it    = 160 ÷ 5 = 32\nMean without it = 82 ÷ 4  = 20.5")
        + "<p>A large outlier pulls the mean <b>up</b>; a small outlier pulls it <b>down</b>. The median hardly changes.</p>"),
]

SECTION_C = [
    box("Pythagoras' theorem", "Skills 21, 22 · Q15",
        f"<div style='display:flex;gap:6px;align-items:center'><div>{right_triangle('a', 'b', 'c (hypotenuse)').replace(chr(39)+'230'+chr(39), chr(39)+'170'+chr(39), 1)}</div>"
        "<div><div class='formula'>c² = a² + b²</div><p>The <b>hypotenuse</b> c is the longest side, opposite the right angle.</p></div></div>"
        + ex("Find c when a = 5 and b = 12:\n  c² = 5² + 12² = 25 + 144 = 169\n  c  = √169 = 13")
        + "<p><b>Is it right-angled?</b> Square the two short sides and add. If it equals the longest side squared → YES.</p>"
        + ex("9, 14, 17:  9² + 14² = 81 + 196 = 277\n            17² = 289   277 ≠ 289  → NO")),
    box("Decimals", "Skill 23 · Q16",
        "<p><b>Multiplying:</b> ignore the decimal points, multiply, then put back the total number of decimal places.</p>"
        + ex("0.3 × 0.07  →  3 × 7 = 21\n1 d.p. + 2 d.p. = 3 d.p.  →  0.021")
        + "<p><b>Dividing by a decimal:</b> move the point in <b>both</b> numbers the same number of places until you divide by a whole number.</p>"
        + ex("6.4 ÷ 0.08  =  640 ÷ 8  =  80")
        + tip("check the answer makes sense – dividing by a number less than 1 makes the answer bigger.")),
    box("Powers and square roots", "Skill 24 · Q17",
        "<p>3⁴ means 3 × 3 × 3 × 3 = 81 (not 3 × 4). √ means “what number times itself gives this?” e.g. √169 = 13</p>"
        "<table class='mini sm'><tr><th>n</th>" + "".join(f"<td>{n}</td>" for n in range(1, 13)) + "</tr>"
        "<tr><th>n²</th>" + "".join(f"<td>{n*n}</td>" for n in range(1, 13)) + "</tr>"
        "<tr><th>n³</th>" + "".join(f"<td>{n**3}</td>" for n in range(1, 11)) + "<td colspan='2'></td></tr></table>"
        "<p>Also: 13² = 169, 14² = 196, 15² = 225, 20² = 400</p>"),
    box("Ratios and rates", "Skills 33, 34 · Q22",
        "<p><b>Simplify a ratio:</b> divide both parts by the highest common factor (HCF).</p>"
        + ex("16 : 40  → HCF is 8  → 2 : 5")
        + "<div class='formula'>Average speed = distance ÷ time</div>"
        + ex("260 km in 4 hours → 260 ÷ 4 = 65 km/h")
        + tip("if the time is in minutes, change it to hours first: 30 min = 0.5 h.")),
    box("Surds", "Skills 25, 26 · Q18",
        "<p>A <b>surd</b> is a square root that is <b>not</b> a whole number. √3, √10, √40 are surds. √36 = 6 is not.</p>"
        "<p><b>Simplify:</b> find the <b>largest square factor</b> (4, 9, 16, 25, 36, 49, 64, 81, 100).</p>"
        + ex("√28  = √4 × √7  = 2√7\n√90  = √9 × √10 = 3√10\n√200 = √100 × √2 = 10√2")
        + tip("always use the biggest square factor: √32 = √16 × √2 = 4√2.")),
    box("Algebra", "Skills 27–29 · Q19",
        "<p><b>Like terms</b> have exactly the same pronumeral part (x and x² are NOT like terms).</p>"
        + ex("5p + 2q − 3p + q = 2p + 3q")
        + "<p><b>Expand:</b> multiply the number outside by <b>every</b> term inside.</p>"
        + ex("7(k − 2) = 7k − 14\n−3(y + 4) = −3y − 12")
        + "<p><b>Substitute:</b> swap pronumerals for numbers, then use BODMAS. Powers before ×.</p>"
        + ex("4a² − b, a = 3, b = 10\n= 4 × 3² − 10 = 4 × 9 − 10 = 26")
        + tip("4a² means 4 × (a²), not (4a)². Put negatives in brackets: (−3)² = 9.")),
    box("Area and volume", "Skills 30, 31 · Q20",
        "<div class='formula'>Trapezium: A = ½ × (a + b) × h</div>"
        + ex("a = 4 cm, b = 12 cm, h = 5 cm\nA = ½ × (4 + 12) × 5 = ½ × 16 × 5 = 40 cm²")
        + "<div class='formula'>Rectangular prism: V = l × w × h</div>"
        + ex("V = 7 × 3 × 4 = 84 cm³")
        + tip("area is in units² (cm²), volume is in units³ (cm³). h is the perpendicular height.")),
    box("Tables of values", "Skill 32 · Q21",
        "<p>Substitute each x-value into the rule. Use brackets for negatives.</p>"
        + ex("y = 2x + 5\nx = −3: y = 2 × (−3) + 5 = −6 + 5 = −1\nx = 0:  y = 2 × 0 + 5 = 5")
        + "<table class='mini'><tr><th>x</th><td>−3</td><td>−2</td><td>−1</td><td>0</td></tr><tr><th>y</th><td>−1</td><td>1</td><td>3</td><td>5</td></tr></table>"
        + tip("the y-values should go up (or down) by the same amount each time – use this to check.")),
]


def build():
    head = (f"<div class='head'><img src='{LOGO}'><div class='t'><b>Yearly Exam Help Sheet</b>"
            "Year 8 Mathematics · Equations, Investigating Data and Mixed Topics</div></div>")
    intro = ("<p class='intro'>Use this sheet while you work through the practice exams. Every skill on the "
             "<b>Skills Checklist</b> is here, and the question numbers (Q1–Q22) match the practice exams and the "
             "yearly exam. <b>Exam tips:</b> about one minute per mark · show your working · check the scale, key and "
             "units on every graph · underline words like <i>at least</i>, <i>more than</i>, <i>altogether</i>.</p>")
    body = (head + intro
            + "<h2>Section A – Equations</h2><div class='grid'>" + "".join(SECTION_A) + "</div>"
            + "<h2>Section B – Investigating Data</h2><div class='grid'>" + "".join(SECTION_B) + "</div>"
            + "<h2>Section C – Mixed Topics</h2><div class='grid'>" + "".join(SECTION_C) + "</div>"
            + "<div class='foot'>Kingscliff High School · Year 8 Mathematics · Help sheet for the Yearly Examination practice papers</div>")
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>Year 8 Yearly Exam Help Sheet</title>"
            f"<style>{CSS}</style></head><body>{body}</body></html>")


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "helpsheet.html"), "w") as f:
        f.write(build())
