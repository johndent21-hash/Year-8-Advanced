# Bridge to Year 9 (mixed-ability → Year 9 Standard) – source

- `content_s1.py`, `content_s2.py` – lessons, tests; answers checked with SymPy on load
- `sbuild.py` – generated from the Advanced `build.py` by `patch.py`; uses `dsl.py`/`svg.py` from `../Bridge to Year 9 Advanced/source`
- Build: `python3 sbuild.py && node render.js student && node render.js teacher`
