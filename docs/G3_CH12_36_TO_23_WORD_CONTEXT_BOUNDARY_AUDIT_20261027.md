# G3 Chapter 12 — Restore 36 unresolved groups into 23 Word source contexts (2026-10-27)

## Ground truth and process
Read the user’s authoritative Word v37 OOXML direct top-level paragraph text and the previously recorded `G3_CH12_113_Previously_Unlinked_Group_Provenance_Triage_20261027.csv`. Selected exactly **36** entries marked `UNRESOLVED_WHOLE_CONTEXT_PROVENANCE`. Examined their relevant surrounding Word source, printed outputs, and prose, then assigned **23 distinct local Word source contexts**; each initial group maps to precisely one context.

| Section | Prior fragmentary groups | Reconstructed Word source contexts |
|---|---:|---:|
| 12.1 | 13 | 7 |
| 12.2 | 6 | 5 |
| 12.3 | 8 | 5 |
| 12.6 | 9 | 6 |
| **Total** | **36** | **23** |

Detailed 36-row exact-context link: `G3_CH12_36_To_23_Word_Source_Contexts_20261027.csv` (fields include block ID, source paragraph positions, context ID, start/end, role, and pending evidence gate). These context ranges are *inclusive reference spans* and may contain prose/output between source statements; they are not claimed 23 literal standalone Python scripts or 23 new tests.

### Concrete boundary examples
- §12.1 p4691–4711: one concentration array setup plus two alternative means, separated by explanation and printed outputs, formerly two provisional groups.
- §12.1 p4792–4808: one shared 3D zero-array setup, two reductions along different axes.
- §12.2 p5002–5025: reductions using a `a` defined in an earlier paragraph; this is a **dependent** context, not standalone source.
- §12.3 p5497–5527: replicate-axis correction versus per-time scaling with a shared concentration matrix.
- §12.6 p6949–6962: shared `a,b` with `np.sqrt(a*a + b*b)` versus `np.hypot(a,b)`.
- §12.6 p7006–7053: **one** `scale_in_chunks` full function and example spanning **three** provisional groups.
- §12.2 p5090 was already treated as a dependent keepdims illustration in earlier evidence; retaining it here does not reopen the role classification.

## Connected GitHub function provenance
Read five Chapter 12 source modules directly in GitHub; 21 top-level functions total (3+6+6+4+2). Their headers uniformly mark:
`CODE_COMPANION_ROLE: REFERENCE`,
`CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION`,
`CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN`.

The representative functions map **by topic**, not 1:1 literal Word source: `decay_vectorized` / `concentration` relate to §§12.3/12.6 decay; `axis_means` / `shape_axis_reduction` to §§12.1/12.2 axis reductions; `broadcasting` to §12.3; `scale_in_chunks` to Word p7008–7053; `apply_experiment_scales` to Word p5708–5823. Other GitHub representative functions address §§12.4–12.9, outside these 23 contexts. The mapping does **not** establish exact equality of inputs, source statements, results or coverage of all Word snippets. A separate all-21-functions-to-every-Word-block verification remains required.

## Gate decision
The previous **36 unresolved temporary group identities** are now assigned precise Word source contexts, but their **exact QA-case identity / entire executable extraction** remains to be reconciled. This is **structural boundary progress, not 36 checks passing or Chapter-12-wide source completeness proof**. Do not misstate 23 contexts as the final count of all Word manuscript programs (249 earlier groups span whole chapter; only 36 targeted here).

No existing calculations were rerun; Word manuscript and GitHub Python sources untouched. Chapter 12 **G3 IN PROGRESS / FULL PASS HOLD**, G4/G5/G6 HOLD. User need not save this intermediate artifact.