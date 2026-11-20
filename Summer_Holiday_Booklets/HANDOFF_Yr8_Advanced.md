# Handoff: Year 8 Advanced → Year 9 Advanced Summer Maths booklet (Julia series)

## The task
Build **one new booklet**: *Summer Maths: Ready for Year 9*, for a Year 8 **Advanced** class going into Year 9 **Advanced**. It should match the six Julia-series booklets already built, especially the Year 9 Adv → 10 Adv one (`b4`) and Year 10 Adv → 11 Adv one (`b6`). Use the same layout, pipeline, checking standard and file naming.

### The six existing booklets
| Key | Transition | Palette | Julia region (centre, width, rotation) |
|---|---|---|---|
| b1 | Yr 7 → 8 | Watermelon | whole set, (0, 0.02), 1.95, 82° |
| b2 | Yr 8 Std → 9 Std | Lagoon | top spiral, (−0.05, 0.47), 0.95, 0° |
| b3 | Yr 9 Std → 10 Std | Mango | small spiral cluster, (0.86, 0.2), 0.42, 25° |
| b4 | Yr 9 Adv → 10 Adv | Ocean | big-spiral close-up, (0.52, −0.12), 0.34, −30° |
| b5 | Yr 10 Std → 11 Std | Sunset | valley, (−0.30, −0.27), 0.40, 35° |
| b6 | Yr 10 Adv → 11 Adv | Tropical Palm | deep zoom, (0.36, −0.02), 0.09, 0° |

All six share J(c) with c = −0.7269 + 0.1889i. The set is symmetric under z → −z, so don't use the point-mirror of a used region.

### Important context
- An **older** Year 8 Adv → 9 Adv booklet already exists. It was the original model for the series: `Yr8_Summer_Holiday_Ready_for_Yr9_Revision_Booklet_v2.pdf` (and v1), in Drive › Kingscliff Maths Resources 7–12 › Year 08 › Revision Booklets.
- That older booklet's palette was magenta, orange, teal and yellow. Each of its banners used a *different* c, and it lists no outcome codes.
- The new one is a rebuild in series style. **Ask the user** whether it should replace v2 (name it `…_v3`) or sit alongside under the new name `Yr8_Advanced_Summer_Holiday_Ready_for_Yr9_Advanced_Revision_Booklet.pdf`. Their rule is: don't create duplicates; give a newer version a version label or ask.
- **Suggested look:** key `b7`. Keep the original's magenta, orange, teal and yellow ("Tropical Punch") so it stays recognisable as the Year 8 Advanced booklet, but use a new region.
  - Recommended region: the left medium spiral with its tip, centre (−1.12, 0.12), width ~0.62, rotation 90°. It was tested earlier and looks good.
  - Avoid magenta for the *title* if it clashes with `b6`'s coral. Otherwise reuse the original colours: title #d6337f-ish, subtitle #e8a020, stripe magenta, orange, teal, yellow.

## Where things are
- **Build source** (committed, branch `claude/affectionate-carson-j9pex6`): `Year-8-Advanced/Summer_Holiday_Booklets/source/`. It includes a README.
  - `b1.py`–`b6.py`: content files. Copy `b4.py` as the template.
  - `qlib.py`: the `Q`, `B`, `xy` and `stemleaf` helpers.
  - `verify.py`: the sympy checker.
  - `art.py` (the `PAL` dict, seeds and views) and `julia.py`.
  - `render.py`: HTML/CSS. `NAME_COLS` maps group names to colours.
  - `diagrams.py`: SVGs drawn to scale.
  - `print.js`: Playwright to PDF, with column auto-fit and overflow and KaTeX reports.
  - `build.py`: prep, pikepdf, and now `ensure_dots()`.
  - `qcheck.py`: Dijkstra and MST checks.
- **Textbook chapters:** `Year-8-Advanced/` (chapters 1–12, `Year8_Maths_Skills_Checklist.pdf`, `Year_8_Yearly_Maths_Exam.pdf`, `Year_8_Exam_preparation_booklet.pdf`). Year 9 Advanced chapters are in `Year-9-Advanced/`. The NESA K–10 (2022) syllabus PDF is in every repo.
- **Finished PDFs** are in each year's repo under `Summer_Holiday_Booklets/`.

## Setup in a fresh container
```bash
cp -r /home/user/Year-8-Advanced/Summer_Holiday_Booklets/source <scratchpad>/build && cd <scratchpad>/build
pip install sympy numpy pikepdf pillow pymupdf
npm init -y && npm install katex@0.16.11 @fontsource/inter@5.0.18
# Playwright + Chromium are preinstalled (require('playwright') works). Don't reinstall.
python3 verify.py b4        # sanity check: should report 126 items, 0 failed
```
Then:
1. Add `b7` to `art.py`: a `PAL` entry (cover gradient, view, title, sub, kick, kick_d, cream, peach, firstup, stripe, 6 week colours dark enough for white text) and a seed in `make()`.
2. Add `b7` to `JNOTE` in `build.py`.
3. Write `b7.py`, then run:
```bash
python3 verify.py b7
python3 art.py b7
python3 build.py b7
```
Run `art.py b7 --draft` first for quick layout passes. The full-resolution art takes about 40 seconds.

## Content plan (Stage 4, with Year 8 Advanced extras and a Year 9 Advanced preview)
- **Year 8 Advanced coverage:** Pythagoras (incl. surds and triads), working with numbers, algebra, geometry, area and volume, fractions and percentages, data, probability, equations, ratios and rates, linear graphing, similar figures and surface area.
- **Asterisked (advanced) sections in the textbook**, which this class has done:
  - surd simplification
  - algebraic index laws
  - binomial expansion, perfect squares, difference of two squares
  - equations with brackets
  - polygon angle sum
  - networks
  - Venn diagrams and two-way tables
  - gradient
- **★ Year 9 Advanced preview** (Stage 5 core + Adv path):
  - quadratic factorising, ALG-P-01/02
  - surd operations, IND-P-02
  - trig ratios and elevation, TRG-C-01/02
  - negative and fractional indices, IND-C-01, IND-P-01
  - monic quadratics and inequalities, EQU-P-01
  - simple interest and earning money, FIN-C-01
  - surface area of prisms and cylinders, ARE-C-01
  - midpoint, distance and y = mx + c, LIN-C-01/02
  - multistage probability, PRO-C-01
  - congruence and similarity, GEO-P-01
- **Suggested 20 strands**, the same as the original Year 8 booklet:
  1. Fractions & integers
  2. Percentages & rounding
  3. Indices
  4. Roots & surds
  5. Simplify & substitute
  6. Expand
  7. Factorise
  8. Equations
  9. Equations
  10. Formulas
  11. Pythagoras
  12. Area
  13. Volume
  14. Number plane
  15. Gradient
  16. y = mx + c
  17. Angles
  18. Probability
  19. Algebra in context
  20. Measurement in context
- **Groups** (names must exist in `render.NAME_COLS` and give 8 different colours): Number [1,2], Indices & roots [3,4], Algebra [5,6,7], Equations [8,9,10], Measurement [11,12,13], Linear [14,15,16], Angles & chance [17,18], In context [19,20]. The `hints` list must be in the **same order** as `groups`.
- Write **fresh questions**: don't copy v2's. Pitch harder than `b2` (Year 8 Std) and easier than `b4`. Each page moves from easy to harder, and week 1 is easiest. Use about 2–4 ★ per week, about 3 diagrams per week, and a bonus challenge each week. No calculator; give trig values in the question, e.g. "Use tan 35° ≈ 0.70".
- `star_text`: "Year 9 preview (Stage 5)". Fill the `outcomes` string with the MA4 codes plus the ★ MA5 codes.

## Gotchas learned
- **Money and maths:** write money as `\\$`; math goes in `$…$`, which `render.mathify` converts. An unpaired `$` trips an assertion. Don't write `\,^\circ`; use `^\circ`. Use `\tfrac` for mixed numbers.
- **Check specs:**
  - `('eq', expr, expected)`, `('solve', lhs, rhs, var, [sols])`, `('fac', expr, factored)`, `('py', code, {env})`, `('man', note)`.
  - Exponential solves return complex roots, so filter for `is_real`.
  - For a compound inequality, intersect two `solve_univariate_inequality` results.
  - `sp` is available in `py` checks.
- **Diagrams:** draw them with the `diagrams.py` functions so they come out to scale. A network can't be to scale; it already prints "Not to scale".
- **Shrinking columns:** `print.js` shrinks a crowded column's question font (it logs `FIT:`). Below ~10.8 px, shorten the question wording instead.
- **Styling:** no `box-shadow` (Chrome rasterises it and bloats the PDF). Dots come from the shared PNG tile. Expect about 0.85–1.0 MB per booklet: images are JPEG q70 at 1200 px, and the rest is fonts and text.
- **QA:** `pdftoppm -r 100 -png` the pages and look at every week page, the hints page and the answer pages. In the build log, `KATEX errors` must be 0 and `OVERFLOW` must be absent.

## User preferences to honour (from their profile)
- NSW NESA syllabus alignment. List outcome codes on the resource (page 2 "NSW syllabus" box). Label beyond-stage content (★). Use Australian spelling and NSW contexts.
- A second-teacher check: every answer computed independently in code, exactly one correct answer each, diagrams consistent with their numbers, answer key matching the questions.
- **Google Drive:** save the final PDF to Kingscliff Maths Resources 7–12 › **Year 08 › Revision Booklets** (folder id `13VUvPUhoBFhIZp9AK35eVhSxPXopf1vO`). Check for duplicates first.
  - Last session the upload was blocked by the auto-mode permission classifier ("unrequested commit"), so **get the user's explicit go-ahead to upload** before calling `create_file`.
  - Upload with `base64Content: "sha256:<hash>:<abs path>"` and `disableConversionToGoogleType: true`.
  - If the upload fails, give a zip in the Drive folder structure plus the exact folder.
- **Git:** commit the PDF and `b7` source to `Year-8-Advanced` on `claude/affectionate-carson-j9pex6` and push with `git push -u origin <branch>`.
  - Check first whether that branch's PR was merged. If it was, restart the branch from `main`.
  - Push one repo per plain command; a complex shell loop was rejected by the safety parser.
- **Report back in a few lines:** outcomes covered, what was checked, what was fixed, and anything uncertain.
