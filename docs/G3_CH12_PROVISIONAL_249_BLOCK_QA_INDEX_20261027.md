# G3 Chapter 12 — Provisional Word source-block / QA index (2026-10-27)

## Concrete work
Parsed Chapter 12 Word v37 OOXML, existing complete 889-role ledger, and 28 separately mapped omitted source-continuation paragraphs. Used reproducible source-form screening and gap/heading splitting to build a **first-pass block-level index**; read available detailed QA CSV case/code-paragraph columns and joined literal paragraph indices. No tests rerun.

- **818 distinct source-form paragraph positions** admitted into this provisional code-screening pool (including all 28 already identified omitted continuations). The other classified 889 rows include OMML maths, output, prose, reference labels, and dependent items excluded by this intentionally conservative screen. This is a **heuristic set**, not the official count of executable source lines.
- **249 provisional groups** created based on gaps / headings, each with block ID, paragraph IDs, Word sample text and matched QA case label where one was found.
- **55 groups** intersect available detailed QA **indexed source positions**.
- **16 groups** intersect a historical case's **reported paragraph range**, which is weaker than exact literal-line evidence.
- **178 groups** currently lack a match from the **specific six CSV inventories read in this pass**. They are **not** asserted untested: other previous audit records exist; groups may be narrative, dependent snippets, outputs or pieces split from one program. A numeric QA FAIL count is not warranted.
- All 28 outside-original-889 source-form continuations are represented by exact paragraph IDs in these groups.

Output: `G3_CH12_Provisional_Source_Block_and_QA_Trace_20261027.csv`. Generating script: `build_ch12_block_inventory.py` (local working artifact). The six indexed detail sources read were advanced indexing 14, strides 7, particle motion 12, Word §12.4–12.5 block 12, Word §12.2–12.3 block 6, and Word §12.6–12.7 block 6. The results must not be equated to a complete QA document census.

## Gate limitations and next required work
This is **not yet the canonical complete runnable-block inventory**: automatic gap splitting can fragment multi-line functions, combine adjacent educational examples, and miss text stored in alternate Word stories; the table-cell check was separately reviewed (14 tables / 230 paragraphs, no independent runnable programs seen). Detailed cases from other QA CSVs/docs still need joining; block boundaries need human review and source extraction to produce unambiguous complete program/context identifiers.

Next: import remaining historical QA case-level records and tag source exactness before doing any new execution. Then inspect high-risk multi-paragraph routines, mark dependent snippets and formula/output passages as non-standalone, and decide whether representative GitHub modules remain just references or require a new canonical code collection. Do not claim 178 new programs, 249 independently runnable scripts or a 55/249 pass rate.

Chapter 12 G3 remains **IN PROGRESS / FULL PASS HOLD**; G4/G5/G6 HOLD. Neither Word nor GitHub executable sources were edited. No previous Chapter 6/10 calculation retests. This is an intermediate internal audit artifact; user **does not need to save it**.
