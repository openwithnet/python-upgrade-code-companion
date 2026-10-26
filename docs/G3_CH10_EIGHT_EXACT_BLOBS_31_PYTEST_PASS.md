# G3 Chapter 10 — Eight Exact Git Blobs and Integrated Pytest PASS

Date: 2026-10-26. Fetched source contents and expected blob SHA values from GitHub default branch at `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/`. Reconstructed eight files byte-for-byte into local `ch10_exact_all/`; Git blob SHA-1 computed over `blob <length>\\0<bytes>` matched **8/8** GitHub-provided blob values.

- `kinetics.py`: 20744240691b06bef0b6cdb47af9ec8650b1ddf3 — MATCH
- `test_kinetics.py`: 1650e8e0baf342836c79ef801834c43ba5a1ecc9 — MATCH
- `ch10_composition_example.py`: ac5c5121c06903f762317ab7884e9b8c0797071b — MATCH
- `test_ch10_composition_example.py`: d6a7387af83e8bf1f3bfce61939c17bc50477b8b — MATCH
- `ch10_pipeline.py`: d71cc743adb2d6a83dcca27be8a6b0c068fdc0c0 — MATCH
- `test_ch10_pipeline.py`: 01f976e2b28b1b5e50f080a6b67a4fdda27c05c9 — MATCH
- `c3_calibration.py`: 3bd000de428a818fc4765bd75631369c44a5606c — MATCH
- `c3_validation.py`: ecd4c28c15e4ae8ac25be7e9803e0e3674969906 — MATCH

Run from exact eight-file directory: `python -m pytest -q test_kinetics.py test_ch10_composition_example.py test_ch10_pipeline.py`. **31 passed in 0.08s; exit 0** (Python 3.13.5, pytest 9.0.2). Local full run evidence: `/mnt/data/python_upgrade_qa/ch10_exact_all/VERIFICATION.txt`. Source reconstruction helper is `/mnt/data/python_upgrade_qa/rebuild_ch10_exact.py`.

This **supersedes earlier local-transcription hash-mismatch limitation for these eight particular repository files**. It is not proof of every Chapter 10 code source in the repository, full Word-to-source program correspondence, scientific validation beyond tests, Windows latest revision, or publication rights. The old §10.6 labeling issue remains: `ch10_pipeline.py` is related C3 material, not established as direct Word §10.6. No Word/executable Python source edits. G3 overall/G4/G5/G6 HOLD.