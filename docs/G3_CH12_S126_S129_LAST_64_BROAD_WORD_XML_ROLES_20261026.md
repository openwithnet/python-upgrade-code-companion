# G3 Chapter 12 — Final 64 broad-reference paragraph roles, §§12.6 & 12.9 (2026-10-26)

## Method
Read exact Word v37 `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, `word/document.xml`, direct `w:body/w:p` zero-based. Selected precisely the 64 positions with `latest_status=PRIOR_BROAD_SPAN_ONLY` from the 889-candidate register `G3_CH12_889_Post_S1245_Residual_Classification_20261026.csv`. For each position, inspected `w:t` and true `m:oMath` / `m:oMathPara` nodes.

Reproducible local trace: `G3_CH12_64_Broad_Reference_Word_XML_Classification_20261026.csv`.

## Word-grounded classification
| Section | Python code or multiline continuation | OMML maths (not code) | Explanatory prose (not code) | Total |
|---|---:|---:|---:|---:|
| 12.6 | 47 | 2 | 0 | 49 |
| 12.9 | 7 | 7 | 1 | 15 |
| **Total** | **54** | **9** | **1** | **64** |

- §12.6 p7138,7165 are Word equations, not Python. The 47 code-form candidates belong to four **reconstructed context groups**, *not* 47 standalone programs: p7080–7132 Euler solver & call (27 candidate positions); p7146–7156 multiple initial values (7); p7167–7192 np.where and eager log warning (7); p7200–7213 np.vectorize (6). These correspond at the **range/behavior level** to the previous `G3_CH12_12_6_3_12_7_NINE_NUMERIC_CASES.md` audit (Euler / negative step contract / vectorize / where / warning); the old 9 cases are not rerun and all 47 do **not** inherit exact line-by-line PASS.
- §12.9 p8071,8073,8076,8176,8177,8265,8267 are OMML mathematical displays; p8041 is ordinary prose about `np.linspace()`.
- Remaining seven §12.9 code-form positions p8081,8087,8093,8095,8096,8097,8100 belong to the manuscript `position_constant_acceleration` definition/usage (p8081–8100), an analytical formula example. They are semantically related to the previously passed analytic-position calculations, but the available detailed 12-case CSV lists p8054–8062 and p8107–8133, **not** this exact p8081–8100 source region. Accordingly their exact paragraph-level source/execution linkage remains **NEEDS_EXACT_SPAN_EVIDENCE**; do not equate semantic similarity to literal test proof.

## Gate interpretation
The 64 broad-reference positions are now **all Word-XML role classified** (54 code/continuation, 9 OMML, 1 prose). This closes their *type identification only*, **not** their executable-evidence status. In particular the §12.9 analytic function needs source-span examination and possibly isolated Word-native execution, and a separate 213 unclassified syntax/fragment candidates elsewhere in Chapter 12 remain.

Prior 126 scoped checks unchanged; no tests rerun; no Word or Python executable source edits. G3 Chapter 12 IN PROGRESS; G4/G5/G6 HOLD.
