# G3 Chapter 12 — Exact Word source spans for the 28 outside-889 code candidates (2026-10-27)

## Work completed
Using the canonical Word v37 `word/document.xml` direct `w:body/w:p` paragraph indices, all **28 source-form paragraphs omitted from the original 889-candidate screen** were associated with **20 concrete Word source-span identifiers**. This replaces the previous nearest-neighbor-only adjacency argument with explicit spans. No numerical tests repeated, no Word or Python source edited.

**Role outcomes:** 18 function-signature continuations; 3 multiline arithmetic continuations; 2 assertion continuations; 2 multiline-call continuations; 1 array literal continuation; 1 contract-dependent statement; and **1 standalone *dependent expression*** (`a[np.ix_([0,2],[1,3])]`, Word p6071, requiring the earlier array `a`).

Examples:
- Word p5319–5320: `mean_over_replicates` signature p5318–5340
- p5709–5711: `apply_experiment_scales` signature p5708–5730
- p6439, p6454–6455, p6665–6667: view/copy and scaling function signatures
- p7009/p7012: `scale_in_chunks` function p7008–7045
- p7638: array-shape contract p7636–7645
- p7812: normalized-totals assertion p7811–7819
- p7893–7894: `relative_by_sample` function p7892–7937
- p8082/p8086: analytic position function p8081–8101, already precisely tested in a prior scoped audit
- p8243/p8280: multiline Euler calls in p8243–8251 and p8278–8288

**Trace file:** `G3_CH12_28_Outside_Candidate_Exact_Block_Spans_20261027.csv` (28 records; each has direct Word text, span ID, start/end and explicit caveat).

## Limits
Span boundaries are **structural, inclusive review ranges**, not a claim that all intervening paragraphs consist of executable Python. Some include prose or expected output; exact runnable-line extraction is still required when assembling a canonical complete source. One span can contain multiple dependent examples. Mapping 28 paragraphs into 20 contexts is not 20 new tests or 20 fully validated independent programs.

The earlier 14 Word tables / 230 table-cell paragraphs review remains valid as a role screen (no new independent Python code identified). **Chapter-wide complete block inventory remains IN PROGRESS**, since a deterministic sweep for *every* executable source group and matching evidence record is still pending. The five GitHub Chapter 12 modules are marked as educational representative reconstructions, not verbatim complete extraction. G3 FULL PASS HOLD; G4/G5/G6 HOLD.

## Release/storage policy
This is an internal/provenance intermediate written to the private GitHub repository. **The user does not need to download or save this CSV.** Only a true recovery baseline/final canonical release should be marked MUST SAVE.
