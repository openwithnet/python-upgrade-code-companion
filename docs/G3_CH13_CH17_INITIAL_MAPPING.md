# G3 — Chapters 13–17 Initial Word/Code Mapping (2026-10-25)

**Decision: scoped concept/implementation correspondences found; NOT a file-by-file or historical full 1:1 match.** Word source: current v37 G4 QA manuscript. Paragraph indices below are zero-based python-docx indexes and may shift after edits. Reviewed GitHub source headers distinguish `WORD_BASED_REPRESENTATIVE_RECONSTRUCTION` (Ch13–16) and `RECONSTRUCTED_NOT_ORIGINAL` (Ch17).

| Chapter | Word anchor | GitHub sample | Mapping status | Qualification |
|---|---|---|---|---|
| 13 | §13.3 SciPy curve fitting, Word ~8985–8992 | `chapters/chapter13/src/ch13_examples.py`: `concentration_model`, `fit_decay` | DIRECT_SEMANTIC | Uses `curve_fit` and 1st-order decay, but Word's exact example/data and function names are not all identical |
| 13 | §13.4 ODE and `solve_ivp`, Word ~9604 | `ch13_examples.py`: `reaction_rhs`, `integrate_decay` | DIRECT_SEMANTIC | Numeric integration with `solve_ivp`, not verbatim complete Word extraction |
| 13 | reproducibility/hash discussions, Word ~11553 | `ch13_examples.py`: `sha256_file`, `save_analysis` | RELATED_IMPLEMENTATION | Reconstructed CSV/hash/metadata workflow |
| 14 | §14.2 biological sequence, Word ~12430 | `chapters/chapter14/src/ch14_examples.py`: `dna_operations`, `sequence_features` | DIRECT_SEMANTIC | Biopython Seq/SeqRecord-based operations, constrained unambiguous DNA features |
| 14 | §14.3–14.4 sklearn workflow, Word ~12784–12834 | `ch14_examples.py`: `fit_linear_example`, `fit_sequence_pipeline` | DIRECT_SEMANTIC | LinearRegression, Ridge and Pipeline; didactic reconstruction |
| 15 | §15.2–15.4 autodiff/functional Python, Word ~14825; §15.6 | `chapters/chapter15/src/ch15_core_concepts.py`: `torch_backward_example`, `jax_functional_grad`, `three_library_decay` | RELATED_IMPLEMENTATION | Concepts agree; exact names `three_library_decay` are not Word block names. Windows ch15-pip job PASS; not proof every snippet executed |
| 16 | review, validation and reproducibility, Word ~19241–19332 | `chapters/chapter16/src/ch16_review_workflow.py`, `ch16_validated_decay.py` | RELATED_IMPLEMENTATION | Word `validated_decay` function concept exists; `inspect_python_source` is reconstruction, not located as exact Word function |
| 16 | intentional bug demonstration | `chapters/chapter16/src/ch16_initial_bug.py` | INTENTIONAL_BUG | Retain as explicitly labeled educational defect; do NOT classify as production-executable verified source |
| 17 | harmonic oscillator, Word ~22350–22401 | `chapters/chapter17/src/oscillator_lab/core.py`: `OscillatorModel`, `EulerSolver`, trajectory/validators | DIRECT_SEMANTIC_RECONSTRUCTION | Model and solver families correspond, but **NOT original recovered source** and no exact Word file/text identity established |

## Actual checked code examples

- Ch13 `concentration_model` and `integrate_decay` are representatives for word discussions about first-order exponential decay and `solve_ivp`.
- Ch14 `dna_operations` maps to Biopython use and `fit_sequence_pipeline` to sklearn object composition, **not** evidence of externally validated biological predictive power.
- Ch15 Torch/JAX examples require optional CPU dependency environment; G2 Windows Chapter 15 job succeeded. No full Word block coverage claim.
- Ch16 `inspect_python_source` parses Python AST but does not establish code safety or semantic correctness; `ch16_initial_bug.py` is intentionally defective.
- Ch17 `OscillatorModel(m,k).rhs(t,[x,v])=[v,-(k/m)x]` gives harmonic oscillator dynamics; this is mathematical correspondence with the Word model, **not** provenance recovery.

## Release gates

All 19 Python files in Ch13–17 retain their file-level release classifications; this matrix does not change any `manuscript_1to1=NOT_PROVEN` inventory cells. This is a first scoped mapping, not exhaustive block review or executed output comparison. Exact source identity, whole-book QA, third-party licensing and G6 Release stay HOLD. Do not rewrite Word or Python source merely to force textual identity.
