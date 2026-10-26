# G3 — Chapter 12 Source-File Correspondence Matrix (2026-10-26)

**Status: scoped representative mapping, not a Chapter 12 whole-manuscript PASS or original file recovery.**

Word: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`. Prior independent QA logs cover **126 case checks** across §12.1–12.9, with original extracted paragraph references in each section-specific audit. Counts are *case executions*, not the number of distinct code blocks or Python source scripts.

## Word §12.10 summary inspected
The Word section `12.10 Chapter Summary` begins at **zero-based DOCX paragraph 8487** and contains conceptual recap plus short code illustrations, e.g. p8498 `y = 2.0 * x + 1.0`, p8500 `mean_values = data.mean(axis=0)`, p8519 `corrected = data * scales[:, None]`. These are **dependent illustrative expressions**, not independently runnable programs as printed. Neither should they be silently counted as additional tested cases. The next chapter starts at paragraph 8622 (`Chapter 13. SciPy...`).

## Current five-source mapping

| GitHub source file | Function(s) read from source | Word sections / scoped evidence | Relationship |
|---|---|---|---|
| `ch12_canonical_examples.py` | `decay_vectorized`, `axis_means`, `broadcasting` | 12.1 and 12.3; 19 + 8 original audits | DIRECT_SEMANTIC_RECONSTRUCTION; neither source is a byte-identical export of every Word example |
| `ch12_indexing_memory_examples.py` | `boolean_indexing`, `advanced_indexing`, `reshape_transpose`, `view_copy`, `strides`, `in_place_contract` | 12.4–12.5; 12 Boolean/error + 14 indexing/View/Copy + 7 strides + 8 memory/in-place checks contain overlapping sections but their **case counts are separately tracked** | DIRECT_SEMANTIC_RECONSTRUCTION |
| `ch12_remaining_examples.py` | `shape_axis_reduction`, `simulate_euler`, `floating_point_examples`, `positions_with_loop`, `positions_vectorized`, `compare_position_methods` | 12.2, 12.6.3, 12.7, 12.9; relevant section audit logs | DIRECT_SEMANTIC_RECONSTRUCTION; benchmark values are environment dependent |
| `ch12_6_10_verified_examples.py` | `concentration`, `expression_analysis`, `exact_positions`, `simulate_euler_motion` | 12.6, 12.8, 12.9; 8 memory/performance + 12 expression-matrix + 12 particle-motion cases | DIRECT_SEMANTIC_RECONSTRUCTION; `expression_analysis` uses representative data, not confirmed identical to Word's exact 4x4 sample |
| `ch12_additional_manuscript_examples.py` | `apply_experiment_scales`, `scale_in_chunks` | 12.3.3 and 12.6.2 (per file docstring); broadcasting / chunked-scaling audit examples | RELATED_IMPLEMENTATION pending exact parameter/data comparison |

All five carry `WORD_BASED_REPRESENTATIVE_RECONSTRUCTION` provenance and are currently `REFERENCE` candidates, not declared verbatim source recovery.

## G3 gaps
1. The automatic 1,090 candidate groups for Chapters 7–12 are not all individually reviewed, especially Chapter 10/12 text-styled fragments. No total coverage denominator is certified.
2. For each source function, record one precise Word code span and compare exact inputs, outputs, validation/error behavior. Semantic relatedness is not textual 1:1 equivalence.
3. Review §12.10 explanatory snippets separately: their implicit variables must not be presented as standalone runnable samples.
4. Verify tests and dependencies for all current candidate files against release head and reconcile separate source rights/provenance. Do not reinterpret CI PASS as whole manuscript verification.

**Gate:** G3 overall IN PROGRESS; G4/G5/G6 HOLD. Neither Word nor Python sources changed in this review.
