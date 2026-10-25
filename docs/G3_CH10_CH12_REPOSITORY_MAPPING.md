# G3 — Chapter 10/12 Word Examples to Repository Mapping (2026-10-25)

**Status: partial / scope-limited.** Evaluated against current Word G4 QA example ranges and `docs/CODE_FILE_CATALOG.md`. Mapping labels distinguish **DIRECT_SEMANTIC**, **RELATED_ONLY**, and **NO_EXACT_SOURCE_MATCH_FOUND**. None imply original byte-for-byte provenance or G3 PASS.

| Word example (zero-based paragraph positions) | Repository file(s) | Mapping judgment | Reason |
|---|---|---|---|
| Ch10 calibration function and list-call, 1471–1492 | `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/c3_calibration.py` | RELATED_ONLY | Word's `linear_concentration` standalone teaching function and list comprehension return [0,1,4]; repo implements `LinearCalibration.predict_concentration` with equivalent inverse formula and `analyze_many`, but **not the same named function or structure** |
| Ch10 earlier calibration snippet, 1444–1462 | Same C3 calibration module | RELATED_ONLY | Identical teaching inputs/output, but independent Word snippet, not identical repo file |
| Ch12 list repetition, 4523–4525 | No exact repository file demonstrated among the reviewed Ch12 src files | NO_EXACT_SOURCE_MATCH_FOUND | Python list repeat `[1,2,3]*2` differs from NumPy vectorized operations; preserve as a textbook-only introductory contrast |
| Ch12 NumPy elementwise multiply, 4531–4533 | Ch12 src `ch12_canonical_examples.py`, `ch12_remaining_examples.py` (broader array demonstrations) | RELATED_ONLY | Conceptual NumPy arithmetic, but exact `np.array([1,2,3])*2` block not verified in reviewed source; requires earlier `import numpy as np` |
| Ch12 vectorized decay, 4570–4586 | `chapters/chapter12/src/ch12_canonical_examples.py:decay_vectorized`; `ch12_6_10_verified_examples.py:concentration` | DIRECT_SEMANTIC | Both implement analytic `c0*np.exp(-k*times)` for c0=1, k=.2, times 0..5; source canonical gives array [1, .818731, .67032, .548812, .449329, .367879] to 6 decimals. **Not an exact textual block match.** |

## Explicit findings

- Current Chapter 12 source files are labeled `WORD_BASED_REPRESENTATIVE_RECONSTRUCTION`; this deliberately denotes *representative reconstructions*, not original manuscript extracts. Their verified scientific meaning does not establish 1:1 original code identity.
- Related-only examples are **not missing-code errors**: the curriculum can legitimately include shorter self-contained Word teaching snippets while GitHub carries larger canonical/representative files, provided the distinction is clearly documented.
- No repository Python source modified, and the 81-file hash inventory requires no refresh.
- Execution examples reported in `G3_CH10_CH12_ADDITIONAL_EXECUTION_SAMPLES.md` apply only to the specified reconstructed snippets. They are **not** newly independently executed in this mapping step.
- The rights and provenance gates remain unverified for archived Chapter 10 copies; do not infer permission to publicly release from mapping.

## Forward gate

Keep a code-to-manuscript mapping column allowing `TEXTBOOK_ONLY_EXAMPLE`, `DEPENDENT_SNIPPET`, and `RELATED_CANONICAL_IMPLEMENTATION` rather than forcing every Word fragment into a stand-alone GitHub script. Expand to all chapters only after checking paragraph context and deduplicating fragments. G3/G4/G5/G6 remain HOLD.
