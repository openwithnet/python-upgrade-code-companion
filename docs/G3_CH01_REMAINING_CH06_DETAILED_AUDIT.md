# G3 — Chapter 1 Remaining Ten Files and Chapter 6 Listing Audit (2026-10-25)

**Status: PARTIAL. Newly identified source/Word alignment defects must be addressed before G3 final approval. No source or Word changes in this audit.**

## Chapter 1 — Ten remaining study files

| Section file | Source-declared Word paragraph anchors | Prerequisite noted in source |
|---|---|---|
| 1.1.2 | 26 | none |
| 1.1.3 | 32 | none |
| 1.2.2 | 50, 54 | §1.1.3 NumPy |
| 1.2.3 | 64, 69, 74, 84, 88 | §1.1.3 NumPy |
| 1.3.2 | 105, 109 | §1.1.3 NumPy |
| 1.3.3 | 118, 122, 129, 134, 137 | §1.1.3 NumPy |
| 1.4.2 | 157 | §1.1.3 NumPy |
| 1.4.3 | 166, 172 | §1.1.3 NumPy |
| 1.5.2 | 196, 207, 212, 216 | §1.5.1 expression matrix |
| 1.5.3 | 221, 223 | §1.1.3 NumPy |

**Verified discrepancy:** source `section_1_1_2.py` comments `# manuscript paragraph 26`, but current Word v37 G4-QA paragraph index 26 is the **§1.1.2 heading**, not the code block. Similarly `section_1_5_3.py` says code at Word paragraph 221 and `True` at 223, but current Word indexes: 222=§1.5.3 heading, **223=code block, 224='예상 출력:', 225='True'**. These anchors may derive from earlier indexing/layout or off-by-one errors; their original basis is not yet established. Do not state paragraph positions are verified merely because source headers contain numbers.

**Classification defect:** the end of `section_1_5_3.py` contains a bare `True` expression under `# manuscript paragraph 223`. In current Word it is explicitly the **expected output**, not executable source. Running the file may still succeed and display the boolean from a previous print, but this artifact's role should be documented and cleaned in a controlled source update followed by hash/CI refresh. Do not mutate source now, because this audit is documentation only.

CI evidence for all 15 section files remains valid for the tested files, but **CI pass is not proof of exact Word paragraph mapping**.

## Chapter 6 canonical executable listing

Word v37 §6.5.2 comprises current Word paragraph indices **898–907**, including module docstring, imports, `finite_real`, immutable `ParticleState`, `euler_step`, `Particle`, `TrajectoryRecord`, `Trajectory`, `simulate_particle`, `main`, main guard. GitHub `chapters/chapter06/original_package/p1_particle_trajectory.py` has the same named components and explicit Euler numerical policy.

Word §6.5.3 expected output is at current paragraph index 910: 5 records (t=0,.5,1,1.5,2), final Euler x=3, exact x=4 and error=1. Test `test_p1.py` asserts expected trajectory and immutability. This is **structural and numeric alignment**; an actual code-string/line-by-line diff of the concatenated 898–907 listing with repository source is **not yet produced**, so exact textual identity stays NOT_PROVEN.

## Blocking follow-up

1. Derive reliable current-Word section-to-code anchors from Word structure instead of trusting source paragraph comments.
2. Remove/move expected-output expressions from runnable source only after recording canonical Word output and preserving pedagogical labels; refresh hashes and CI when edited.
3. Perform precise Chapter 6 Word listing vs repo file source diff, excluding known repository role/provenance header lines; categorize any differences before source or Word edits.
4. No automatic release-rights approval: Ch6 is `ARCHIVED_CHAPTER_REVIEW_COPY`.

G3 NOT FROZEN; G4/G5/G6 remain HOLD.
