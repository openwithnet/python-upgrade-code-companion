# Chapter 4 — Integrated Review

**Status: NOT FROZEN.** This is a reconstructed editorial review draft, **not a verbatim preservation of the detailed chat manuscript**.

Files:
- `Chapter_04_integrated_review.docx`: Word manuscript (editable OMML equations)
- `Chapter_04_integrated_review.md`: Markdown source
- `b1_dna_analysis.py`: authoritative, runnable B1 example for this review
- `test_b1_dna_analysis.py`: 15 unittest tests
- `example_output.txt`, `test_results.txt`: actual run records
- `Chapter_04_QA_report.md`: verification and outstanding gaps

Run (Python >=3.13, stdlib only):

```bash
python b1_dna_analysis.py
python -m unittest -v test_b1_dna_analysis.py
```

The B1 program accepts only A/C/G/T bases, is intentionally educational, and fails fast when encountering invalid input.
