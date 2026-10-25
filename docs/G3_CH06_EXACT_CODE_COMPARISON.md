# G3 — Chapter 6 Exact Source Comparison (2026-10-25)

**Decision: EXACT CODE TEXT MATCH AFTER DOCUMENTED WRAPPER NORMALIZATION.**

Compared the actual Word v37 QA §6.5.2 program extracted from paragraphs 898–907 (`G3_Ch06_Word_Extract_20261025.py`) with GitHub `chapters/chapter06/original_package/p1_particle_trajectory.py`.

- Word extract: **4,332 Unicode characters**, **120 lines**, FNV-1a 32 checksum `ebc20915`.
- GitHub source: drop first **three** metadata comment lines (`CODE_COMPANION_ROLE`, `PROVENANCE`, `RELEASE`) without changing any program lines; resulting source has **4,333 characters**, **121 newline-separated segments**, checksum `41745bcd`.
- Word extract plus **one terminal LF** has **4,333 characters** and checksum **`41745bcd`**, matching the stripped GitHub source. Source and Word text thus match after removing role headers and normalizing the one extra final newline, assuming checksum collision-free for this limited comparison; this is a character-based checksum verification rather than a byte-by-byte independent diff artifact.
- Word extract syntax and runtime output were already verified; Word expected output is identical. **Section-specific Ch6 source identity is now established to the described normalization standard.**

**Not a G3 global PASS.** The GitHub source is marked `ARCHIVED_CHAPTER_REVIEW_COPY`, so rights still need separate review. Test claims are scoped to Ch6, not all Word text. There is no manuscript or Python source modification here.
