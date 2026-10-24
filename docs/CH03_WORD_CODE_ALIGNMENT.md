# Chapter 3 P1 — Word / Code Scoped Alignment (2026-10-25)

**Status: P1 representative example ALIGNED; complete 1:1 manuscript match NOT PROVEN.**

| Word v37 section | Source/test evidence | Result |
|---|---|---|
| 3.3.3 validation | `chapters/chapter03/original_package/P1_particle_motion.py` finite-value, positive step and integer-step checks | Conceptual alignment |
| 3.4.1 constant-acceleration setup | Script parameters x0=v0=0, a=2, dt=0.5, T=2 | Matched |
| 3.4.2 embedded Euler excerpt | Same previous-state explicit Euler update as source | Matched |
| 3.4.2 excerpt stdout | Word lists `[0.0, 0.0, 0.5, 1.5, 3.0]` and `[0.0, 1.0, 2.0, 3.0, 4.0]` | Independently executed Word excerpt and exact output matched |
| 3.4.2 final position error | Word 3 vs exact 4, error 1 | Matched source/test |
| 3.4.2–3.4.3 dt sensitivity | Word dt=1/.5/.25 corresponds to position 2/3/3.5 | Matched `test_P1.py` |
| 3.4.3 update order | explicit vs semi-implicit Euler warning | Matched test assertions |

The Word snippet is a deliberately abbreviated stand-alone teaching excerpt, NOT a byte-for-byte copy of the full source. Github source and tests retain provenance `ARCHIVED_CHAPTER_REVIEW_COPY`. Full Chapter 3 historic manuscript sentence comparison and redistribution rights remain **UNVERIFIED**. Keep G3, G5 and G6 open. No Python code/Word manuscript edits performed for this check.
