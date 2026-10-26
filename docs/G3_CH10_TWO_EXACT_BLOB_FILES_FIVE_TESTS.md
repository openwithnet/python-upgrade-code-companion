# G3 Chapter 10 — Exact Git Blob Parity and Pytest

2026-10-26. Two files fetched from the current GitHub default branch and materialized as byte-exact UTF-8 contents in the isolated runtime. SHA-1 was computed using the Git blob format `sha1('blob '+byte_length+'\0'+file_bytes)`.

- `ch10_composition_example.py`: exact Git blob `ac5c5121c06903f762317ab7884e9b8c0797071b` — MATCH.
- `test_ch10_composition_example.py`: exact Git blob `d6a7387af83e8bf1f3bfce61939c17bc50477b8b` — MATCH.
- Ran `python -m pytest -q test_ch10_composition_example.py` against ONLY these exact files in an isolated directory: **5 passed in 0.08 seconds, exit 0**. The recently added `ConstantDerivative` test is among the five.

Evidence: `ch10_exact_github_pair/VERIFICATION.txt` and `verify_exact_ch10_pair.py` in the QA workspace. Scope is **two exact blobs only**. Other six original modules/tests have not been verified byte-identical in this pass. Earlier local copies differed from original; this new exact-pair experiment does not retroactively authenticate them. GitHub CI run 40255432567 remains a separate 18/18-success check on its source commit. Full Chapter 10 G3 and G4–G6 remain HOLD. No Word or GitHub executable source changed.