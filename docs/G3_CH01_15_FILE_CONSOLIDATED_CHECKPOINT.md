# G3 — Chapter 1 Consolidated 15-file Checkpoint (2026-10-25)

**Status: file inventory/anchor comments reconciled; not full manuscript 1:1 nor public-release clearance.**

All 15 repository files under `chapters/chapter01/sections/` were fetched from current branch and source-header anchors were recorded. Nine files had their source-comment positions updated using the checked G4 Word QA mapping; §1.5.3 was fixed in an earlier commit to separate a printed expected output `True` from executable source. No Python statements were altered by the nine re-anchoring edits.

| Section / Python file | Current source-declared Word indexes (zero-based) | Review status |
|---|---|---|
| `section_1_1_1.py` | 10,15,19 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_1_2.py` | 28 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_1_3.py` | 34 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_2_1.py` | 41 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_2_2.py` | 52,56 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_2_3.py` | 66,71,76,86,90 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_3_1.py` | 97 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_3_2.py` | 107,111 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_3_3.py` | 120,124,131,136,139 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_4_1.py` | 144 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_4_2.py` | 159 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_4_3.py` | 168,174 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_5_1.py` | 187 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_5_2.py` | 198,209,214,218 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |
| `section_1_5_3.py` | 223 | Anchor comments inventoried; individual independent execution/expected-output coverage not established here |

## What the evidence establishes

- Source role for all fifteen: `SECTION_EXECUTABLE_STUDY`; provenance `WORD_EXTRACT_REASSEMBLED`; release `RETAIN_AS_CANDIDATE_NOT_FROZEN`; 1:1 `NOT_PROVEN`.
- Nine corrected reference-comment files have refreshed SHA-256 rows in `docs/SOURCE_ROLE_AND_RELEASE_GATE.csv` (commit `dc450b87727f8618e91f9b0fdf5510ed71969a6a`). §1.5.3 previously refreshed separately.
- The latest checked Linux workflow run `40182527282`, at this audit's read, remained **QUEUED**. Do not relabel latest-head CI to PASS. A successful earlier run `40181424645` applies to an earlier source commit.
- Prior successful Windows/Conda runs were for earlier source snapshots, not a fresh validation of these edits.

## Work remaining for Chapter 1 G3 approval

1. Verify remaining section anchors against the exact current Word code content (not merely their annotation) and expected outputs.
2. Run/review complete chapter section scripts against the current head and check the latest Linux workflow conclusion.
3. If Word pagination/paragraphs change again, preserve a stable section + source signature in addition to fragile integer paragraph indexes.
4. Clear licensing and provenance separately. Do not infer from `WORD_EXTRACT_REASSEMBLED` that redistribution permission has been confirmed.

G3/G4/G5/G6 remain HOLD. No Word or Python source modifications made in this checkpoint.