# Chapter 10 Alignment and QA Package

- `Chapter_10_alignment_QA.md`: 원고-코드 정합성 판정과 편집 지침
- `verified_suite/kinetics.py`: Chapter 10.5 canonical runnable source
- `verified_suite/ch10_composition_example.py`: 10.3–10.4 standalone explanatory composition demonstration (not replacement for kinetics.py)
- `verified_suite/ch10_pipeline.py`: prior C3 integration supplement
- `verified_suite/test_*.py`: reused C3, Ch9, kinetic, and composition tests
- `test_results.txt`: pytest output (72 passed on Python 3.13.5)

Run from verified_suite directory:

```bash
python -m pytest -q
python kinetics.py
python ch10_composition_example.py
python ch10_pipeline.py
```

No full Chapter 10 publication Word manuscript is represented in this package.
