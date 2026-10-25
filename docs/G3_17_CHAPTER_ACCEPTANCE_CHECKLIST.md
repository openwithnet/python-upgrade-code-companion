# G3 — 17-Chapter Acceptance Checklist (2026-10-25)

**Verdict: IN PROGRESS — NO FULL MANUSCRIPT/CODE 1:1 CERTIFICATION.** This index records the strongest available anchor evidence without claiming every source/example is complete.

| Chapter | Scoped evidence | What remains |
|---|---|---|
| 1 | [CH01_WORD_CODE_ALIGNMENT.md](CH01_WORD_CODE_ALIGNMENT.md), 15 word-reassembled study scripts | 10 files need detailed spans/output and all narrative snippet coverage |
| 2 | [CH02_WORD_CODE_ALIGNMENT.md](CH02_WORD_CODE_ALIGNMENT.md), four extracted Word snippets executed | All other source blocks |
| 3 | [CH03_WORD_CODE_ALIGNMENT.md](CH03_WORD_CODE_ALIGNMENT.md), P1 Euler | Full chapter and rights |
| 4 | [CH04_WORD_CODE_ALIGNMENT.md](CH04_WORD_CODE_ALIGNMENT.md), B1 DNA | Full example source identity |
| 5 | [CH05_WORD_CODE_ALIGNMENT.md](CH05_WORD_CODE_ALIGNMENT.md), C2 kinetics | Full example coverage |
| 6 | [CH06_WORD_CODE_ALIGNMENT.md](CH06_WORD_CODE_ALIGNMENT.md), P1 object-based Euler | Byte/text comparison of Word program |
| 7 | [CH07_WORD_CODE_ALIGNMENT.md](CH07_WORD_CODE_ALIGNMENT.md), B1 sequences | Code blocks in Normal styles |
| 8 | [CH08_WORD_CODE_ALIGNMENT.md](CH08_WORD_CODE_ALIGNMENT.md), C3 calibration | Exact standalone source coverage |
| 9 | [CH09_WORD_CODE_ALIGNMENT.md](CH09_WORD_CODE_ALIGNMENT.md), C3 validation | Historic test counts vs current pytest |
| 10 | [G3_CH10_CH12_REPOSITORY_MAPPING.md](G3_CH10_CH12_REPOSITORY_MAPPING.md), samples | Large Normal-style code inventory |
| 11 | [CH11_WORD_CODE_ALIGNMENT.md](CH11_WORD_CODE_ALIGNMENT.md), strategy/observer | Different teaching EventSource vs code Observer |
| 12 | [G3_CH10_CH12_REPOSITORY_MAPPING.md](G3_CH10_CH12_REPOSITORY_MAPPING.md), selected NumPy examples | Large Normal-style fragment inventory |
| 13–17 | [G3_CH13_CH17_INITIAL_MAPPING.md](G3_CH13_CH17_INITIAL_MAPPING.md); [test contracts](G3_CH13_CH17_TEST_CONTRACT_EVIDENCE.md) | Exact paragraph maps and independently verified output/coverage per source; 17 original source not recovered |

## Explicit gate policy

- **Representative-scoped PASS:** outputs, equations, contracts, required dependencies and source names checked for a stated example. Many representative results meet this bar.
- **G3 whole-book PASS:** all relevant manuscript code blocks across 17 chapters classified as `STANDALONE_RUNNABLE`, `DEPENDENT_SNIPPET`, `EXPLANATORY`, `PSEUDOCODE`, `EXPECTED_OUTPUT`, `COMMAND`, or `NONCODE`; each genuinely runnable example has a documented execution/expected-output result or reason for exclusion. Repository files have exact section mappings and provenance labels. No false requirement for every paragraph to have a dedicated .py file.
- **G4 PASS:** Word editorial and visual/OMML QA approved separately; counts of objects do not by themselves establish correct editability.
- **G5 PASS:** rights/attribution for publicly included code independently cleared. All current `ARCHIVED_CHAPTER_REVIEW_COPY` items remain rights UNVERIFIED in current audit.
- **G6 Freeze:** only after G3, G4 and G5 are resolved. Repo PRIVATE, source candidate, Word QA candidate until then.

GitHub Actions G1 and G2 previously passed their specific environments and chapter-entry checks, not the whole-book manuscript coverage gate.
