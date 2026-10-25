# Chapter 2 — Scoped Word / Code Alignment (2026-10-25)

**Decision:** Chapter 2 §2.4 C1 anchor example is numerically and pedagogically aligned with the archived source file. Four independent Word snippets executed successfully, with exact output matches. This is not proof of whole-chapter 1:1 identity or distribution rights.

| Word section | 0-based DOCX paragraph (code / expected output) | Evidence |
|---|---|---|
| 2.4.1 procedural concentration loop | 369 / 371 | Extracted code exits 0, expected output matches |
| 2.4.2 function-centered concentration conversion | 376 / 378 | Extracted code exits 0, expected output matches |
| 2.4.3 object-centered calibration | 384 / 386 | Extracted code exits 0, expected output matches |
| 2.4.3 mixed function/class example | 389 / 391 | Extracted code exits 0, expected output matches |

Code source: `chapters/chapter02/original_package/ch02_examples.py` (25 sequential educational examples); related regression checks `test_ch02.py`. The four Word blocks correspond to the procedural, function-based, object-based and mixed forms in the source. This mapping is semantic and output-based, not a claim that the whole chapter is byte-identical to the archived source.

**Data assumption:** C1 uses synthetic teaching signals [2,4,6] and slope 2; concentration [1,2,3]. The positive-slope contract alone does not validate signal finite-ness, calibration range or scientific uncertainty. The educational slope is assumed, not fitted.

**Execution scope:** Four Word code paragraphs extracted from the current G4 QA DOCX and executed separately under the working Python environment, stdout compared to the adjacent Word expected output paragraphs. This does not replace Windows CI or test every example in `ch02_examples.py`.

**Rights and release:** archived chapter-review provenance is `ARCHIVED_CHAPTER_REVIEW_COPY` and redistribution rights remain UNVERIFIED. G3 full mapping, G4, G5 and G6 remain HOLD. No source or Word manuscript changes.
