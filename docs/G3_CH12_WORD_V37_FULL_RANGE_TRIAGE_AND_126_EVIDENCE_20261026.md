# G3 Chapter 12 — v37 Word full-range triage and evidence reconciliation (2026-10-26)

## Verified inputs
- `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` read directly from Library, `word/document.xml` top-level paragraph indices (zero-based).
- Chapter 12 starts p4451; §12.10 starts p8487; Chapter 13 starts p8622. Thus Chapter 12 main text is p4451–8621.
- All inspected §12.7–12.10 body paragraphs, including Python snippets, were marked `Normal`; filtering only `SourceCode` style would omit relevant examples.
- GitHub existing `docs/G3_CH12_FIVE_SOURCE_CONSOLIDATED_MAPPING.md` and section audit records were read, and all five actual source files fetched from `chapters/chapter12/src`.

## Audited GitHub source inventory
| Source | SHA (GitHub blob) | Top-level functions | Role |
|---|---|---:|---|
| ch12_canonical_examples.py | `1fe40bf3b175c8ebbef9819070069ec44987fc82` | 3 | representative reconstruction |
| ch12_indexing_memory_examples.py | `f036bf1851910cd12b7217fe44ec8e03c7f18bf6` | 6 | representative reconstruction |
| ch12_remaining_examples.py | `d097295c7addaf4a47912e40386c6ec3f121fbfd` | 6 | representative reconstruction |
| ch12_6_10_verified_examples.py | `0603e64ab2ea6640784f0ee9de553920d75d4a1d` | 4 | representative reconstruction |
| ch12_additional_manuscript_examples.py | `d9ca7718ae5e1bafcf315fa5a4fa440585aaa430` | 2 | related reconstruction |
Total: 5 files, 21 top-level functions. All declare `CODE_COMPANION_ROLE: REFERENCE`, `WORD_BASED_REPRESENTATIVE_RECONSTRUCTION`, `RETAIN_AS_CANDIDATE_NOT_FROZEN`, not verbatim Word source files.

## Existing 126 case checks (not rerun)
- §§12.1,12.2: 19 and 10 checked cases, with shared dependency context; cited audit documents explicitly warn not to treat cases as independent complete source blocks.
- §12.3: 8 broadcasting examples, matched displayed outputs; deliberately invalid broadcasting fragment was **not** tested in that particular eight-case group.
- §12.8: twelve integrated 4×4 expression-array cases; ten printed outputs and two nonprint contracts, including deliberately wrong-axis example.
- §12.9: twelve scoped behavioral checks, of which three are reviewer-generated invalid-steps contract tests, not three separate printed Word programs.
- Previous consolidated audit states 126 scoped case checks across §§12.1–12.9. This review preserves this number as an existing audited count, without summing potentially overlapping subsection reports again.

## Expanded Word candidate inventory
A first-pass pattern screen across p4451–8621 yields **889 Python-looking paragraphs** (including standalone assignment, import/def, and other statement shapes). This is a broad *candidate count*, **not 889 executable programs** or 889 distinct examples. It includes fragments, repeated prerequisites, inline equations, outputs, and explanatory lines. Manual/contextual classification remains needed.
- §12.10 p8498 `y = 2.0 * x + 1.0` (requires `x`)
- p8500 `mean_values = data.mean(axis=0)` (requires `data`)
- p8519 `corrected = data * scales[:, None]` (requires `data` and `scales`)
- p8527 and p8529 selecting `values` (requires `values`)
- p8546 `np.shares_memory(a, b)` (depends on NumPy and arrays)
- p8569–8574 `np.testing.assert_allclose(...)` is a multi-paragraph assertion contract, **not** an isolated ready-made program.
- p8588–8591 include displayed differential/kinematic expressions, not necessarily runnable Python as printed.

## Decision and next substantive step
G3 Chapter 12 remains IN PROGRESS. Strong existing 126-case evidence is valid **within reported scopes**. Five source modules are semantic examples, not source-exact recovery. Next: build a classified, contiguous Chapter 12 paragraph inventory using surrounding narrative/Word syntax and match these groups to existing case IDs and the 21 source functions; audit any genuinely unmapped complete executable groups rather than recalculating the existing 126.
No Word/source edits, no Chapter 6/10 or Chapter 12 calculation retests in this pass.
