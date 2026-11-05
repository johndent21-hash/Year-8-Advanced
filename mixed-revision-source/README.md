# Year 8 catch-up revision booklet: source

This folder builds `Yr8_Mixed_Pythagoras_FDP_Algebra_Revision_Booklet.pdf` (9 pages) and its answer booklet `..._Answers.pdf` in the repository root.

| Pages | Topic | NSW syllabus outcomes |
|---|---|---|
| 1–3 | Pythagoras’ theorem (with squares, square roots and surds) | MA4-PYT-C-01, MA4-IND-C-01 |
| 4–6 | Fractions, decimals and percentages | MA4-FRC-C-01 |
| 7–9 | Algebraic techniques, then a mixed exam check | MA4-ALG-C-01 |

All pages also address MAO-WM-01 (working mathematically).

## Build and check

You need Node.js with Playwright (`npm install playwright`, then `npx playwright install chromium`), and Python 3.

```bash
node build.js        # writes both PDFs to the repository root, plus answers.json
python3 verify.py    # works out every answer again in Python and compares it with answers.json
```

`build.js` prints a table of the spare space on each page. A negative number means that page overflows.

- **Answers:** every answer is calculated in `build.js` from the numbers in its question, so the answer key cannot drift from the questions.
- **Second check:** `verify.py` is a separate check. It retypes each question, works it out with `fractions`/`decimal`, and tests algebra by substituting random values into both the question and the answer.
- **Diagrams:** all triangles are drawn to scale from their side lengths. The algebra rectangles are marked “not to scale”.

## Files

- `build.js`: page content (questions, worked examples, scaffolds) and the PDF build.
- `lib.js`: maths markup, diagrams and layout blocks.
- `style.css`: the stylesheet.
- `fonts/`: Lexend, used under the SIL Open Font License.
