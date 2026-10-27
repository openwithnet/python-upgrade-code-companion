# G3 Chapter 12 — Tier B historical executed-source AST comparison (2026-10-27)

## Material new finding
Recovered **original QA CSVs containing the actual previously executed Python source code** from the user's Library:
- `G3_Ch12_12_6_3_12_7_Nine_Cases_20261026.csv` (9 scoped cases, includes `code`).
- `G3_Ch12_12_7_3_Reduction_7_Cases_20261026.csv` (7 scoped cases, includes `source`).

Re-extracted the seven Tier B non-dependent selected Word code components from authoritative Word v37 OOXML. Compared parsed Python ASTs against the actual historical source strings. Ignored irrelevant `1` versus `1.0` numeric lexical spelling; for multiple-initial-state case excluded the reviewer-added `audit_ok` assignment absent from Word. This checks computation structure, **not byte-for-byte or full-manuscript source identity**.

| Word Tier B component | Historical source relation | Comparison |
|---|---|---|
| Multiple initial states | historical QA includes extra reviewer `audit_ok` check | selected Word computation AST matches |
| `np.where` branch output | same statement structure | MATCH |
| `np.where` eager logarithm warning | same structure | MATCH |
| `np.vectorize` result | first printed calculation matches; **Word has a second `print(x**2 + 1)` that historical source did not execute** | PARTIAL MATCH for prior run, extra Word line remains outside historical source |
| `float32` dtype | same structure | MATCH |
| Floating-point cancellation | same structure | MATCH |
| Reduction addition-order | same structure | MATCH |

**7/7 scoped historical computation AST comparisons MATCH** after explicitly documented normalization/exclusions; `np.vectorize` has a **separate additional Word statement** not covered by that original historical execution. This is not 7 fresh numeric tests. The previous QA CSVs have recorded PASS results in their stated scope.

Full 9-row Tier B register still contains two dependent motion snippets; not separately matched by these two source-code files, not labeled failures. Working trace: `G3_CH12_TierB_Historical_Executed_Source_AST_Identity_20261027.csv`.

**Gate:** Tier B selected historical code *structural identity* now established for seven previously run computation subsets (with exceptions documented). Exact byte identity and full Word code coverage are **not** established. The additional vectorize print can be traced to another audit or targeted checked later, without reflexive rerun. Chapter 12 full G3 HOLD pending whole chapter canonical code-block completeness and evidence. G4/G5/G6 HOLD. No Word or production GitHub Python edits. Intermediate audit; user need not archive.
