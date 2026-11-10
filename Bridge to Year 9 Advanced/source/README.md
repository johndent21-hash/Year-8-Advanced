# Bridge to Year 9 Advanced – source

Generates the student booklet and teacher answers (Mandelbrot series).

- `content_a.py`, `content_b.py` – every question; each answer is checked with SymPy when the file loads
- `dsl.py` – question mini-language (LaTeX for display + SymPy for checking)
- `svg.py` – diagrams (drawn to scale unless captioned otherwise)
- `fractal.py` – Mandelbrot cover and banner images (JPEG q70)
- `build.py` + `style.css` → HTML; `render.js` (Playwright) → PDF

Rebuild: `pip install sympy numpy pillow`, `npm install katex@0.16.11 @fontsource/inter@5.0.18`,
then `python3 fractal.py && python3 build.py && node render.js student && node render.js teacher`.
