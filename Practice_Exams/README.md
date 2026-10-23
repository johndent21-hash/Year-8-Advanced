# Year 8 Practice Examinations

Four practice papers for the Year 8 Yearly Examination (Equations, Investigating Data and Mixed Topics).

| File | What it is |
|---|---|
| `Year_8_Practice_Exam_1.pdf` … `Year_8_Practice_Exam_4.pdf` | Practice papers, 60 marks, 60 minutes each |
| `Year_8_Practice_Exams_Answers.pdf` | Answers and marking guide for all four papers |
| `../Year_8_Exam_Help_Sheet.pdf` | Student help sheet (3 pages) to use while practising |

## How the papers match the yearly exam

* Same layout, sections and question order (Q1–Q22), so question numbers line up with the
  **Skills Checklist** and the exam preparation booklet.
* Every one of the 34 checklist skills is assessed in **every** paper.
* No equation, data set, diagram or number set from the yearly exam is reused.
* Shortened from 65 marks / 75 minutes to 60 marks / 60 minutes so a paper fits in one lesson
  (about 20 minutes per section). The parts removed only repeated a skill already tested
  elsewhere in the paper, e.g. a third two-step equation and a second "at least" question.

| Section | Marks | Questions |
|---|---|---|
| A – Equations | 18 | Q1–Q6 |
| B – Investigating Data | 21 | Q7–Q14 |
| C – Mixed Topics | 21 | Q15–Q22 |

## Regenerating

The PDFs are built from `_source/` (Python 3 + headless Chromium):

```
python3 _source/build.py out && python3 _source/helpsheet.py out
chromium --headless --no-pdf-header-footer --print-to-pdf=out/paper1.pdf out/paper1.html
```
