# G3 Chapter 12 — 889 candidate paragraph evidence crosswalk (2026-10-26)

## Method
Word v37 `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` was read from direct `word/document.xml` top-level paragraphs 4451–8621 (zero-based). The prior preliminary 889-candidate CSV was joined to the **paragraph positions explicitly quoted** in existing GitHub G3 Chapter 12 audits. For audit documents reporting only broad section/ranges (e.g. §12.9 8026–8328) we marked `AUDIT_SPAN_REFERENCE_ONLY`, **not** exact per-code coverage. Candidate paragraphs no more than two paragraph indices apart were provisionally grouped: these are proximity groups, not yet syntax-reconstructed complete Python programs.

## Results
| Crosswalk evidence tier | Paragraphs | Meaning |
|---|---:|---|
| AUDIT_EXACT_REFERENCE | 201 | Paragraph index appears within specific enumerated code positions in one of the scoped audit records |
| AUDIT_SPAN_REFERENCE_ONLY | 324 | Lies within a wider audit-mentioned range, but individual code coverage **not established** |
| NO_CASE_PARAGRAPH_REFERENCE | 364 | No matching documented paragraph position among records screened; may be outputs, math, snippets, missing per-case index, or an unverified program |
| Total | 889 | Candidate paragraphs, not distinct programs |
| Proximity groups | 452 | Heuristic grouping; may split multiline blocks or merge nearby snippets |

Unreferenced candidate counts by section: 12.1=31, 12.2=81, 12.3=62, 12.4=24, 12.5=7, 12.6=28, 12.7=25, 12.8=62, 12.9=32, 12.10=12. These are **investigation workload indicators**, not failure counts.

## Audit records used
- `G3_CH12_SECTION_12_1_11_EXECUTED_EXAMPLES.md`
- `G3_CH12_SECTION_12_1_ADDITIONAL_8_EXECUTED.md`
- `G3_CH12_SECTION_12_2_TEN_EXECUTED.md`
- `G3_CH12_SECTION_12_3_BROADCASTING_8_EXECUTED.md`
- `G3_CH12_ADVANCED_INDEX_VIEW_COPY_14.md`
- `G3_CH12_STRIDES_7_EXECUTED.md`
- `G3_CH12_MEMORY_INTEGRITY_VECTORIZATION_EIGHT_CASES.md`
- `G3_CH12_SECTION_12_6_MEMORY_PERFORMANCE_8.md`
- `G3_CH12_12_6_3_12_7_NINE_NUMERIC_CASES.md`
- `G3_CH12_12_7_3_REDUCTION_7_CASES.md`
- `G3_CH12_12_8_INTEGRATED_EXPRESSION_12_CASES.md`
- `G3_CH12_12_9_PARTICLE_MOTION_12_CASES.md`

Other audits such as `G3_CH12_BROADCAST_ERRORS_BOOLEAN_12_CASES.md` provide behavior/case totals but **do not list sufficient paragraph references** to assign specific candidate indices: lack of mapping is not a contradiction of those 126 checks.

## Decisions
- Previous **126 scoped verification cases** remain respected and were not rerun.
- A complete **code-block-level** classification is NOT yet supported by these automatic groups. Next work: manually reconstruct complete statement boundaries (particularly §12.2, §12.3 and §12.8), attach prerequisites/output paragraphs, and test only genuinely missing examples.
- Existing five Python sources are representative reconstructions, not textual exports of 889 paragraphs.
- Neither Word manuscript nor executable Python source was modified; G3 Chapter 12 remains IN PROGRESS; G4–G6 HOLD.
