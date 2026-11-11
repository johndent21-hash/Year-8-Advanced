# Summer Maths booklet builder (Julia series)

Builds the six "Summer Maths: Ready for Year X" holiday revision booklets.

- `b1.py` … `b6.py` – questions, answers, working, hints and syllabus codes for each transition
- `verify.py` – recomputes every answer with sympy (`python3 verify.py b1 b2 b3 b4 b5 b6`)
- `art.py` / `julia.py` – cover and banners, all cut from the Julia set z → z² + c, c = −0.7269 + 0.1889i
- `render.py`, `diagrams.py`, `print.js`, `build.py` – HTML → PDF via Chromium (Playwright), then pikepdf

Needs: `pip install sympy numpy pikepdf pillow`, `npm install katex@0.16.11 @fontsource/inter@5.0.18`, Playwright Chromium.
Run `python3 art.py b1` then `python3 build.py b1`.
