# Chapter 12 G3 — Section 12.2 dependency-context consolidation

Date: 2026-10-27. Canonical source: unmodified Word v37 OOXML; existing provisional source inventory. **31 provisional §12.2 groups were assigned to 14 educational source contexts** using common input definitions, calculations and teaching comparisons. No numerical tests rerun.

Contexts (inclusive Word zero-based paragraph bounds, not literal all-code extraction):

| ID | Bounds | Provisional groups | Topic |
|---|---|---:|---|
| CTX01 | 4870–4879 | 2 | array dimensions |
| CTX02 | 4914–4919 | 1 | scalar/vector/matrix |
| CTX03 | 4932–4964 | 4 | shared 2D indexing and axis reductions |
| CTX04 | 4980–5025 | 5 | shared 2D means |
| CTX05 | 5038–5090 | 4 | keepdims and centered-row comparison |
| CTX06 | 5098–5109 | 1 | multi-axis mean |
| CTX07 | 5121–5129 | 1 | std/ddof |
| CTX08 | 5140–5150 | 1 | NaN handling |
| CTX09 | 5167–5215 | 4 | replicate/time/variable 3D reductions |
| CTX10 | 5229–5247 | 3 | spatial/time temperature means |
| CTX11 | 5260–5266 | 1 | species selection |
| CTX12 | 5277–5287 | 2 | gene means |
| CTX13 | 5300–5304 | 1 | transpose |
| CTX14 | 5318–5327 | 1 | typed helper definition |

The detailed 14-row workfile `G3_CH12_S122_31_To_14_Dependency_Context_Proposal_20261027.csv` preserves all 31 prior provisional IDs, exact selected source paragraph indices and hashes. Bounds can include Word narrative and printed output; source-line completeness and QA execution identity remain separate gates. CTX05's keepdims comparison is dependent on earlier inputs, not a novel standalone program. Older case checks retained, not multiplied into new PASS counts.

§12.1 previously yielded 13 contexts from 29 groups, and §12.2 now yields 14 from 31; neither count is final chapter-wide runnable scripts. Next continue §§12.3–12.9 and reconcile detailed QA. Chapter 12 G3 FULL HOLD / IN PROGRESS; G4/G5/G6 HOLD. No Word or GitHub executable Python changes. Intermediate record; user need not save.