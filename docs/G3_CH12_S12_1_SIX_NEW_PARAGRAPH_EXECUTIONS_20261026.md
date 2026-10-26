# G3 Chapter 12 — Newly Grounded §12.1 Six Word Code Executions (2026-10-26)

Word source: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` (Library). Direct `word/document.xml` top-level `w:body/w:p`, zero-based paragraph indexing. Code text assembled from precisely recorded paragraph locations; narrative, display outputs, and mathematical typesetting excluded. Python `compile`/`exec` and captured stdout were compared to Word displayed output. Whitespace-only normalization was allowed in the textual comparison.

These **six** checks are in §12.1 **before** the first previously enumerated §12.1 execution at paragraph 4599, therefore there is no *paragraph-level* overlap with the 19 §12.1 examples described in `G3_CH12_SECTION_12_1_11_EXECUTED_EXAMPLES.md` and `G3_CH12_SECTION_12_1_ADDITIONAL_8_EXECUTED.md`. Semantic overlap with later examples is possible; they are presented as new explicitly documented Word paragraph checks, not six new independent programs.

| Check | Word code paragraph indices | Expected output paragraph | Result |
|---|---|---|---|
| scalar/vector/matrix ndim | 4499,4501,4503,4505–4508,4510–4512 | 4514–4516 (0,1,2) | PASS |
| Python list repetition | 4523,4525 | 4527 | PASS |
| ndarray elementwise multiply | 4499,4531,4533 | 4535 | PASS |
| square elementwise | 4499,4547,4549,4551 | 4553 | PASS |
| np.exp vectorized | 4499,4557,4559,4561 | none, stdout observed | PASS (execution only) |
| first-order analytic decay | 4570,4572,4573,4575–4582,4584,4586 | 4588 | PASS |

**6/6 direct reconstructed Word excerpt execution PASS; 5/5 explicit expected stdout PASS.** No numeric/source text corrections. Excel-compatible CSV audit artifact is `G3_CH12_S12_1_Six_Unmapped_Word_Cases_20261026.csv` (working session artifact).

## Evidence-level caution
- Pre-existing 126 scoped checks are **not rerun** and are not transformed into 126 unique Word-code programs.
- The earlier crosswalk's 364 `NO_CASE_PARAGRAPH_REFERENCE` hits still include non-code mathematical illustrations and uncovered items. Only these six newly specified code groups are independently resolved here.
- Chapter 12 full G3 PASS remains HOLD. Source modules represent reconstructions; tests across environments and rights G4–G6 remain separate.
- No changes to Word or executable GitHub source; no Chapter 6/10 calculation reruns.
