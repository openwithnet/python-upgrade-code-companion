# G3 Word–Code Alignment Matrix — 2026-10-25

**State: PARTIAL / NOT FROZEN.** This matrix consolidates six representative examples. It does not certify all 17 chapters or line-by-line equivalence of a Word manuscript and repository.

| Chapter | Anchored Word scope | GitHub evidence | Finding | Outstanding |
|---|---|---|---|---|
| 3 | §§3.3–3.4 P1 particle motion | [CH03_WORD_CODE_ALIGNMENT.md](CH03_WORD_CODE_ALIGNMENT.md) | Euler calculation, numerical output and update-order semantics agree | Complete chapter/source historical 1:1; rights |
| 5 | §5.7 C2 kinetic observations | [CH05_WORD_CODE_ALIGNMENT.md](CH05_WORD_CODE_ALIGNMENT.md) | Synthetic data, rates, midpoints, model function contract agree | Complete coverage; rights |
| 7 | §§7.1–7.7 B1 sequence objects | [CH07_WORD_CODE_ALIGNMENT.md](CH07_WORD_CODE_ALIGNMENT.md) | DNA/RNA/Protein policy, GC/residue calculation, composition agree | Complete coverage; rights; helper preconditions |
| 8 | §§8.3–8.5 C3 calibration interface | [CH08_WORD_CODE_ALIGNMENT.md](CH08_WORD_CODE_ALIGNMENT.md) | Linear/quadratic inverse models, Protocol, batch outputs agree | Real-world validation and full coverage; rights |
| 9 | §§9.4–9.5 C3 validation | [CH09_WORD_CODE_ALIGNMENT.md](CH09_WORD_CODE_ALIGNMENT.md) | Unit conversion and test contracts align; `predict()` vs `predict_concentration(signal)` mismatch found | Corrected in current G4 QA Word candidate, but complete G3/full test-count correspondence not proven |
| 11 | §§11.5–11.6 strategy/observer kinetics | [CH11_WORD_CODE_ALIGNMENT.md](CH11_WORD_CODE_ALIGNMENT.md) | Euler, midpoint, event counts and recovered module boundary agree | Word EventSource teaching sketch differs from executable callback example; full coverage/rights |

## Evidence and decision boundaries

- G1 Ubuntu Python 3.11 runner (Run `40062492646`) passed 18/18 workflow jobs.
- G2 Windows Python 3.11 pip (Run `40140441877`) passed 30/30 chapter-entry checks.
- G2 Windows Miniconda (Run `40140880013`) passed 30/30 checks, with Chapter 15 CPU PyTorch/JAX job also successful.
- CI job/check counts do **not** prove every Word code block ran, nor that all `pytest` parametrized tests correspond to historic manuscript test counts.
- Reviewed source provenance includes `ARCHIVED_CHAPTER_REVIEW_COPY` and `RECOVERED_V72`; those labels preserve history but are not redistribution-rights clearances.
- The Word manuscript in the working G4 QA stream has 770 OMML objects after §9.4.2 conversion and the §9.5.2 method-name correction; that is **not** book-wide OMML editability approval.
- Chapter 11 uses recovered `kinetics.py` with mol/L and seconds. Do not merge it with Chapter 5's mmol/L and minutes examples just because both cover kinetics.

## Open gates

1. **G3:** enumerate and map every independently runnable textbook example, explanatory snippet and pseudocode across 17 chapters; classify each and check required outputs/dependencies. No full 1:1 claim until then.
2. **G4:** complete Word-native QA across the book and reconcile the remaining historical/reconstruction notices with evidence. Latest QA Word file remains a *candidate*.
3. **G5:** clear file-level authorship and third-party redistribution permissions, especially the 32 archived chapter-review files in [ARCHIVED_REVIEW_RIGHTS_AUDIT.md](ARCHIVED_REVIEW_RIGHTS_AUDIT.md).
4. **G6:** only after G3–G5 close, cleanse README/release docs and approve Freeze. Repository remains PRIVATE.

**No Python source change in this matrix update.**
