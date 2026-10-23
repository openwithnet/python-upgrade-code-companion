# Source roles and manuscript alignment — release decision record

**Decision:** Repository contents remain **candidate**, NOT FROZEN. Inventory generated from currently available working tree on 2026-10-23; source files were not changed.

## Scope and evidence

- Enumerated **81 Python files** under `chapters/` across **17 chapter directories**.
- A hash, source role, provenance, and release gate was recorded per file in `SOURCE_ROLE_AND_RELEASE_GATE.csv`.
- Files in a test suite are QA inputs, *not* automatically publishable instructional source. In Chapter 10, QA alternatives remain separate from `verified_suite`.
- Earlier 31/31 figure counts chapter execution *jobs*, **not** manuscript blocks or pytest test functions. Successful test jobs alone do not establish 1-to-1 code correspondence.

## Roles (file counts)

- `ALTERNATIVE_QA_COPY`: 1
- `AUTOMATED_TEST`: 32
- `EXECUTABLE_ENTRYPOINT_RECONSTRUCTED`: 1
- `INTENTIONAL_FAILURE_EDUCATIONAL`: 1
- `ORIGINAL_PACKAGE_CANDIDATE`: 14
- `PACKAGE_INITIALIZER`: 1
- `RECONSTRUCTED_SOURCE`: 1
- `RECOVERED_EXAMPLE_OR_DEPENDENCY`: 2
- `SECTION_EXECUTABLE_STUDY`: 15
- `VERIFIED_REPRESENTATIVE_EXAMPLE`: 13

## Decisions with significant teaching implications

1. **Ch01**: section-level executable study scripts reassembled from Word. Preserve learning-context dependence; do not present as untouched original source.
2. **Ch02–10**: original chapter-review package files are retained as *candidates*, not automatically approved production canonical. Ch10 includes QA duplicates/alternatives and requires `--import-mode=importlib` in its isolated test runner.
3. **Ch11**: v72 recovered example and `kinetics.py` dependency; preserve Ch10 / Ch11 contract boundaries.
4. **Ch12–16**: verified representative and reconstructed companion examples; manuscript full-code coverage remains unproven.
5. **Ch16**: `ch16_initial_bug.py` demonstrates an intentional defect. Label **EDUCATIONAL / NOT FOR PRODUCTION**; it must not be run as if it were validated implementation.
6. **Ch17**: reconstructed oscillator lab. *Not* recovered original. Retain reconstructed provenance in GitHub and textbook references.

## Manuscript alignment: unresolved gates

- **All 17 Chapters**: 1-to-1 mapping of Word v37 code blocks/outputs/sections to repository files remains unproven (see v68 release matrix).
- **Ch01–03**: verify sequential snippets versus chapter scripts, prerequisites, expected outputs.
- **Ch04–11**: select canonical final source where chapters share scientific examples / same module names; annotate duplicate test modules and reusable contracts.
- **Ch12–16**: review explanatory snippets, intentional pseudocode and representative implementations separately; do not claim complete Word coverage from test counts.
- **Ch17**: clearly attribute reconstruction and check scientific/numerical agreement with Word Chapter 17.
- **External gates**: Windows/Anaconda, real GitHub Actions runner, dependency lock, Word-native visual QA, licensing review are outstanding.

## Save policy

This is a **working QA record**, not a new mandatory download. Preserve already-downloaded v74 recovery and v75 integration snapshots until a later verified release candidate supersedes them.
