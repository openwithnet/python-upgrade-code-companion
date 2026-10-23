# Chapter 6 — Integration QA report

Status: **INTEGRATED REVIEW / NOT FROZEN**

## Verified by execution
- `python -m pytest -q test_p1.py`: **16 passed**.
- `python p1_particle_trajectory.py`: 5 records for t = 0, 0.5, 1, 1.5, 2 seconds.
- Final Euler position 3.0 m, exact position 4.0 m, absolute position error 1.0 m; final velocity 4.0 m/s.
- The integrated reference source is `p1_particle_trajectory.py`; chapter snippets are instructional alternatives and must not be pasted as conflicting class definitions.

## Manuscript / Word QA
- The six sections 6.1–6.6, both Introductions and the three-level TOC are present.
- Markdown and DOCX generated from the same review manuscript.
- DOCX was rendered to 12 page images and an overview was inspected.
- 12 OMML math elements were embedded using Pandoc conversion.
- **Content-preservation limitation:** full verbatim 6.1–6.6 prose cannot be compared line by line against prior on-screen messages in the current local file set. This is a comprehensive reconstruction, not a proven lossless transfer. Some narrative and some intermediate code demonstrations are abbreviated. Do not mark as final/frozen until original manuscript is supplied or an exact textual comparison is completed.
- Python 3.14-specific runtime compatibility not tested; tests run in available interpreter (recorded below).

## Remaining work before freeze
1. Compare the original full on-screen draft with DOCX/Markdown, restoring missing descriptions and intermediate examples without paraphrase loss.
2. Confirm whether the chapter's canonical three-level TOC titles match an independently frozen book TOC; especially 6.5, which was newly defined during drafting.
3. Proofread equations, units, text/code concordance and Word layout page by page at print zoom.
4. Validate on Python 3.14.x and chosen NumPy/runtime configurations where applicable. Chapter 6 canonical code depends on Python standard library only; test dependency is pytest.
5. Freeze only after editorial acceptance.

Current Python interpreter: `3.13.5`.
