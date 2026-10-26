# G3 Chapter 12 — Post-§12.8 Four-Check 889-Candidate Register Update (2026-10-26)

## Method
Updated the previously issued `G3_CH12_Reconciled_889_Register_20261026.csv` solely from the already recorded audited paragraphs in `docs/G3_CH12_S12_8_FOUR_REMAINDER_WORD_CHECKS_20261026.md` (commit `a9a323f2`). No prior computational work was repeated. Input is 889 Word v37 candidate paragraph positions, not 889 independent executable programs. New output snapshot: `G3_CH12_PostS128_Reconciled_889_Register_20261026.csv`.

## Exactly documented changes
10 candidate indices promoted from unreviewed to `S12_8_FOUR_WORD_CHECKS_EXPLICIT_VERIFIED`: `7636, 7640, 7641, 7642, 7644, 7645, 7652, 7660, 7752, 7754`.

The Word audit also lists p7638, but that paragraph is not among the original 889 pattern-screen candidates. Therefore it has **not** been inserted as an 890th row or counted as an eleventh promoted candidate.

The 10 indices correspond to **four** verification scenarios, *not* ten independent programs or ten new tests:
1. data/metadata/shape/nonnegative/finite assertion contract;
2. dtype `float64`;
3. non-square matrix axis semantics;
4. transpose.

## Updated mutually exclusive paragraph-ledger
| Evidence tier | Candidates |
|---|---:|
| Prior broad audit span only — individual verification not proven | 324 |
| Prior exact audit paragraph reference | 201 |
| Earlier new explicit check reference | 52 |
| §12.8 `relative_by_sample` contract paragraph evidence | 27 |
| §12.8 newly promoted four-check paragraph evidence | **10** |
| OMML-only outside §12.10 | 50 |
| §12.10 dependent snippets/OMML classification closed | 12 |
| Remaining potentially executable statements | 192 |
| Remaining potentially executable control/contract statements | 19 |
| Remaining ambiguous fragments | 2 |
| **Total** | **889** |

Unreviewed syntax/fragment candidates now **213** (192+19+2), down from 223; 324 broad-audit spans remain a *separate* documentation gap. Neither number establishes the number of currently unverified runnable programs.

## Next concrete work
Look up detailed existing QA execution-case CSVs corresponding to 324 broad-span references; recover exact paragraph code positions and distinguish per-case verified from approximate section coverage. Then syntax-reconstruct only the 213 remaining unreviewed candidates and test genuinely missing complete programs. Preserve 126 original scoped-case successes without double counting.

No Word or GitHub Python code changes. G3 Chapter 12 IN PROGRESS; G4/G5/G6 HOLD. Chapter 6 and 10 tests were not rerun.
