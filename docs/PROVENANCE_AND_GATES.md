# v75 working repository candidate — provenance and blockers

This is a working GitHub repository candidate, **not a public release**. The initial provenance below remains historical. Verified CI results and remaining release gates are tracked separately.

- Chapter 01: v63 minimal executable section files; textbook coverage incomplete.
- Chapter 02–10: integrated **unaltered working copies** from original `Downloads.zip` chapter-review archives; canonical selection and 1:1 manuscript alignment are still outstanding. Fresh chapter-isolated checks passed; Chapter 10 requires pytest importlib collection mode.
- Chapter 11: original recovered ch11_lab.py, test_ch11_lab.py and matching kinetics.py from v72.
- Chapters 12–16: v57 integration copy of representative/reconstructed Code Companions, tested previously; not 1:1 with all Word snippets.
- Chapter 17: reconstructed candidate; original historical final release source is not recovered.
- Validation: separate source code syntax, pytest, numerical agreement, manuscript exact match, Windows/Anaconda and Word-visual QA.
- Word source of truth remains v37 contained in recovery checkpoint.
- Before GitHub publish: select and insert ch02–10 canonical files, normalize imports safely, run complete tests in integrated layout, link manuscript sections, license & CI checks.

## Verified gates (2026-10-25 status)

- G1 Ubuntu/Python 3.11: GitHub Actions Run `40062492646` 18/18 jobs PASS (commit `125b792ffbf057892f84bd890cd8fcfb385ca66c`).
- G2 Windows pip/Python 3.11: Run `40140441877` 30/30 selected checks PASS, UTF-8 mode required for Korean stdout.
- G2 Windows Miniconda/Python 3.11: Run `40140880013` `conda-core` 30/30 checks PASS, alongside `chapter15-pip` 1/1 PASS using CPU PyTorch/JAX.
- The 81 inventoried Python files carry explicit role/provenance headers. `docs/CODE_FILE_CATALOG.md` contains release-candidate classifications. `docs/SOURCE_ROLE_AND_RELEASE_GATE.csv` was refreshed to source hashes by run `40063132264`.
- These checks do **not** establish complete manuscript-to-repository 1:1 coverage, independent personal-PC compatibility, third-party redistribution rights, or Word-native final publication quality.

## Remaining public-release blockers

1. Check rights and redistribution status of archived review-package files and any third-party material. Apache-2.0 LICENSE does not grant third-party rights.
2. Complete Word manuscript editorial/render QA and representative-to-full-code alignment decisions.
3. Perform final README/release-document cleansing after rights and manuscript gates; keep repo private and NOT FROZEN until then.
