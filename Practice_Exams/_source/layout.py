"""HTML building blocks that reproduce the look of the Year 8 Yearly Examination paper."""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "logo.png"), "rb") as f:
    LOGO = "data:image/png;base64," + base64.b64encode(f.read()).decode()

CSS = """
@page { size: Letter; margin: 0.75in 0.85in 0.7in 0.85in; }
* { box-sizing: border-box; }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 9.6pt; color: #000; margin: 0; }
.cover { height: 9.4in; position: relative; break-after: page; }
.cover .top { display: flex; justify-content: space-between; align-items: flex-start; margin-top: 0.15in; }
.cover .top { justify-content: center; }
.cover .top img { width: 6.2in; }
.namebox { width: 2.95in; }
.namebox div { border: 1.2px solid #000; height: 0.38in; margin-bottom: 0.32in; padding: 4px 8px;
  font-family: 'Liberation Serif', 'Times New Roman', serif; font-size: 9pt; }
.cover h1 { font-weight: normal; text-align: center; font-size: 20pt; margin: 0.55in 0 0.16in; }
.cover h2 { font-weight: normal; text-align: center; font-size: 17pt; margin: 0 0 0.16in; }
.cover .practice { text-align: center; font-size: 11pt; font-style: italic; margin-top: 0.1in; color: #333; }
.instr { display: flex; border: 1px solid #000; margin: 0.8in auto 0; width: 6.1in; }
.instr > div { width: 50%; padding: 8px 10px; }
.instr .l { border-right: 1px solid #000; font-size: 8.8pt; }
.instr .l b { display: block; margin-bottom: 8px; }
.instr .l ol { margin: 0; padding-left: 16px; line-height: 1.5; }
.instr .r { font-family: 'Liberation Serif', 'Times New Roman', serif; font-size: 9.2pt; }
.instr .r p { display: flex; justify-content: space-between; margin: 0 0 9px; padding-right: 14px; }
.sec { break-before: page; }
.sec h3 { font-size: 12.5pt; margin: 0; }
.sec .sub { font-style: italic; font-size: 8.8pt; margin: 2px 0 6px; }
.sec hr { border: 0; border-top: 1.3px solid #000; margin: 0 0 12px; }
.q { break-inside: avoid; margin-bottom: 16px; }
.qh { display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 3px; }
.intro { margin: 0 0 4px; line-height: 1.35; }
.fig { text-align: center; margin: 4px 0 6px; }
.part { margin: 3px 0 5px; }
.prow { display: flex; align-items: baseline; }
.lab { width: 20px; flex: none; }
.ptext { flex: 1; line-height: 1.35; }
.blank { flex: none; width: 1.85in; white-space: nowrap; }
.bl { display: inline-block; border-bottom: 1px solid #000; width: 1.15in; height: 0.9em; vertical-align: baseline; }
.blank .bl { width: 1.25in; }
.mk { flex: none; width: 0.75in; text-align: right; font-weight: bold; }
.wline { display: flex; margin: 9px 0 0 20px; width: 5.15in; }
.wline .fill { flex: 1; border-bottom: 1px solid #000; margin-left: 3px; }
.line { border-bottom: 1px solid #000; height: 22px; margin-left: 20px; width: 5.55in; }
.endans { margin: 12px 0 2px 20px; }
.endans .bl { width: 1.6in; }
.circle { margin: 12px 0 0 20px; }
.circle span { margin-left: 22px; }
table.dt { border-collapse: collapse; margin: 5px auto 4px; font-size: 9.2pt; }
table.dt td, table.dt th { border: 1px solid #000; padding: 4px 12px; text-align: center; min-width: 44px; }
table.dt th { font-weight: bold; }
table.dt td.h { font-weight: bold; }
table.dt.tall td { height: 24px; }
.key { text-align: center; font-style: italic; font-size: 8.8pt; margin-top: 2px; }
.data { text-align: center; letter-spacing: 0.4px; margin: 6px 0 4px; }
.formula { margin: 2px 0 2px 20px; font-size: 9pt; }
.end { text-align: center; font-weight: bold; margin-top: 10px; }
.foot { text-align: center; font-size: 8pt; color: #555; margin-top: 18px; }
"""


def esc_marks(m):
    return f"({m} mark{'s' if m != 1 else ''})"


def part(text, marks, label=None, blank=None, work=0, end=None, extra=""):
    """One question part laid out like the exam.

    blank: text shown before the inline answer line (e.g. 'x =' or '' for a plain line).
    work:  0 = no working lines, 1 = 'Working:' line, n = 'Working:' line + (n-1) full lines.
    end:   label for an answer line under the working (e.g. 'x =', 'Answer:').
    """
    h = ["<div class='part'><div class='prow'>"]
    h.append(f"<span class='lab'>{label + ')' if label else ''}</span>")
    h.append(f"<span class='ptext'>{text}</span>")
    if blank is not None:
        h.append(f"<span class='blank'>{blank} <span class='bl'></span></span>")
    h.append(f"<span class='mk'>{esc_marks(marks) if marks else ''}</span></div>")
    h.append(extra)
    if work:
        h.append("<div class='wline'>Working:<span class='fill'></span></div>")
        h.extend("<div class='line'></div>" for _ in range(work - 1))
    if end:
        h.append(f"<div class='endans'>{end} <span class='bl'></span></div>")
    h.append("</div>")
    return "".join(h)


def question(num, title, marks, body, intro=""):
    i = f"<p class='intro'>{intro}</p>" if intro else ""
    return (f"<div class='q'><div class='qh'><span>Question {num} &nbsp;–&nbsp; {title}</span>"
            f"<span>{esc_marks(marks)}</span></div>{i}{body}</div>")


def fig(svg):
    return f"<div class='fig'>{svg}</div>"


def section(letter, name, marks, minutes, body):
    return (f"<div class='sec'><h3>Section {letter} – {name} ({marks} marks)</h3>"
            f"<div class='sub'>Suggested time: {minutes} minutes. Show all working.</div><hr>{body}</div>")


def cover(paper_no, marks, minutes):
    a, b, c = marks
    return f"""
<div class='cover'>
  <div class='top'><img src='{LOGO}'></div>
  <h1>MATHEMATICS</h1>
  <h2>Year 8 – Practice Examination {paper_no}</h2>
  <h2>Equations, Investigating Data and Mixed Topics</h2>
  <div class='practice'>Practice paper for the Year 8 Yearly Examination</div>
  <div class='instr'>
    <div class='l'><b>Instructions</b><ol>
      <li>Attempt all questions</li><li>Show working where needed</li>
      <li>Time Allowed {minutes} minutes</li><li>Calculators are permitted</li>
      <li>Marks are shown beside each question</li></ol></div>
    <div class='r'>
      <p><span>Equations (Section A):</span><span>/{a}</span></p>
      <p><span>Investigating Data (Section B):</span><span>/{b}</span></p>
      <p><span>Mixed Topics (Section C):</span><span>/{c}</span></p>
      <p><span>Total Marks:</span><span>/{a+b+c}</span></p>
    </div>
  </div>
</div>"""


def page(title, body, css_extra=""):
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>"
            f"<style>{CSS}{css_extra}</style></head><body>{body}</body></html>")
