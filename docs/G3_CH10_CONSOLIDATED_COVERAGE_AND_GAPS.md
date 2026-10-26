# G3 Chapter 10 Consolidated Checklist and Unverified Code Register

Date 2026-10-26. Scope: full Chapter 10 structure inspected in Word v37 G4 QA, existing audits consolidated with corrected Word paragraph indexing. No new original GitHub test suite run, and no additional execution success claimed.

## Source-location convention

**Word anchors below are zero-based top-level document paragraphs** (the same convention as `python-docx Document.paragraphs`). Counting every XML `w:p`, including paragraphs inside tables, changes the indexes; do not silently mix these numbering systems. Extracting top-level XML paragraphs confirmed §10.4.3 p2851, §10.5 p3112, §10.6 p3454 and §10.7 p3907; Chapter 11 starts p4075.

## Integrated G3 checklist

| Word position | Main concern | Evidence / test relation | G3 disposition |
|---|---|---|---|
| §10.1–10.3 (preceding p2638) | Functions/objects and calculation composition | Previous contextual-fragment classification only | **UNVERIFIED FULL PROGRAMS** |
| §10.4.3 p2851–2955 | `EulerStep`, `MidpointStep`, `Simulation`, interface injection | Six prior Word-reconstructed behavior checks (Euler .8, midpoint .82, etc); repository `test_ch10_composition_example.py` reviewed | **SCOPED_BEHAVIOR_PASS**, not standalone Word full-program parity |
| §10.4.4 p2956–3089 | Input/contract and design verification | Selected assertions in source tests; not all Word fragments mapped to test IDs | **MAPPING_INCOMPLETE** |
| §10.5 p3112–3453 | RateLaw, FirstOrderRate, Euler simulation, analytic results and automated checks | Six scoped Word checks and eight selected kinetics error probes; `test_kinetics.py` assertions inspected | **SCOPED_BEHAVIOR_PASS**, coverage incomplete |
| §10.6 p3454–3906 | Good design vs overabstraction | Word is a design discussion. `ch10_pipeline.py` is an unrelated C3 calibration pipeline; its named '10.6' docstring is NOT direct Word provenance | **DIRECT_SOURCE_MATCH_NOT_ESTABLISHED** |
| §10.7 p3907–4074 | Chapter summary with prior component excerpts | Conceptual summary and dependent snippets; classify before any execution count | **NOT_FULLY_CLASSIFIED** |

## Distinct source and test status

- `ch10_composition_example.py` — derivative model and solver composition. Its four edge probes were **observations**, not validation-contract PASS (negative dt 1.2, NaN state NaN, None solver AttributeError, negative state negative result). API policy is an editorial choice.
- `kinetics.py` — nonnegative consumption rate and explicit Euler; **eight selected negative cases rejected as expected**. This is not proof of all possible edge cases.
- `ch10_pipeline.py` — C3 calibration and unit conversion; existing `test_ch10_pipeline.py` inspected for tests, but no direct Word §10.6 example matched.
- Associated three test files carry archived-review provenance. A file's tests being readable does not demonstrate they passed in a new run.

## Open G3 work

1. Reconstruct and classify **all** true executable example boundaries in Chapter 10, particularly §§10.1–10.3, 10.4.4, 10.5.5 and 10.7, rather than treating explanatory lines, output, file trees or diagrams as programs.
2. Complete test ID -> exact Word source span -> source function -> observed run mapping; mark document-derived reviewer harnesses separate from verbatim extract.
3. Run current repository modules and tests as actual source files in an isolated Python environment (including C3 dependencies), not just equivalent function bodies.
4. Determine whether `ch10_pipeline.py` belongs in the book's Chapter 10 release at all, given the §10.6 mismatch. Do not change canonical Word or code without deliberate resolution.
5. Continue source provenance and rights review before public release.

**Gate**: G3 IN PROGRESS; G4/G5/G6 HOLD. No Python sources or Word manuscript modified in this audit.
