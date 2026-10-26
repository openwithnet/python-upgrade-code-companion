# G3 Chapter 12 — Post-§12.8 register reconciliation (2026-10-26)

## Inputs
- Previously recorded 889-candidate register `G3_CH12_889_Refined_Evidence_and_XML_Roles_20261026.csv`.
- Previously recorded Word-literal execution audit `docs/G3_CH12_S12_8_RELATIVE_BY_SAMPLE_WORD_CONTRACTS_20261026.md`: 2 Word-authored tests and 8 reviewer probes, passing within its stated scope.
- `docs/G3_CH12_SECTION_12_10_CODE_CANDIDATE_CLOSURE_20261026.md`: 12 candidates classified as dependent snippets or Word OMML.
- This reconciliation is a **register/evidence update**; no numerical tests were rerun and no new PASS is claimed.

## Concrete reconciliation
1. **27 candidate paragraph indices** in Word p7892–7976, previously assigned to unreviewed statement/control/fragment categories, belong to `relative_by_sample` and its two Word-authored tests. Reclassify as `WORD_CONTRACT_EXPLICIT_EXECUTION_EVIDENCE`. These are 27 *paragraph candidates* linked to **one function and two tests**, not 27 new programs or tests.
2. **12 candidate indices** in §12.10 p8487–8621 were already classified, and are now explicitly assigned `S12_10_CLASSIFIED_NOT_STANDALONE`. Of these, three are OMML math objects and the rest dependent illustrations/parts of one contract expression.
3. The earlier refined CSV's `section` column erroneously tagged these **12 §12.10 rows as §12.1**, causing the misleading 12.1 count of 84 (versus prior 72), and omitting §12.10 from counts. The new `section_corrected` field fixes these labels while preserving original source columns for audit traceability.

## Updated mutually exclusive candidate-position ledger
| Status | Count |
|---|---:|
| Prior broad audit span only (not exact check) | 324 |
| Prior explicit paragraph reference | 201 |
| Other newly explicit test references before this reconciliation | 52 |
| §12.8 Word contract & test paragraph evidence | 27 |
| OMML-only (outside §12.10) | 50 |
| §12.10 closed dependent/math classification | 12 |
| Remaining potentially executable statement candidates | 196 |
| Remaining potentially executable control candidates | 25 |
| Remaining other/ambiguous fragments | 2 |
| **Total** | **889** |

**223 candidate positions remain in unreviewed syntax/fragment categories** (196+25+2), down from 259 in the previous register due to 27 resolved §12.8 contract paragraphs and 9 non-OMML §12.10 summary candidates. **324 broad-span positions are not exact per-example verified** and remain a separate evidentiary gap, not certified PASS.

## Next actual work
Prioritize complete executable block boundary and prerequisite review for 223 unreviewed candidate positions, especially unlinked §12.8 entry/metadata/shape assertions p7593–7662 and transpose p7752–7754; resolve references for the 324 broad-span positions against audit CSV evidence when available. Preserve existing 126 scoped cases without double-counting; do not infer 889 independent programs, or an unconditional Chapter 12 G3 PASS.

No Word or Python production source changes; Chapter 6/10 tests untouched. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
