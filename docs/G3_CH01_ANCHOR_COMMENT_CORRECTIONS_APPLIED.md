# G3 Chapter 1 — Commit of 24 Re-anchored Code References (2026-10-25)

**Applied:** 24 `# manuscript paragraph N` references in nine section scripts were changed to their independently verified current Word G4 QA zero-based locations (`N+2` in this bounded set). The §1.5.3 location was fixed in a prior commit and was not edited again.

| File | New verified Word code anchors |
|---|---|
| `section_1_1_2.py` | 28 |
| `section_1_1_3.py` | 34 |
| `section_1_2_2.py` | 52, 56 |
| `section_1_2_3.py` | 66, 71, 76, 86, 90 |
| `section_1_3_2.py` | 107, 111 |
| `section_1_3_3.py` | 120, 124, 131, 136, 139 |
| `section_1_4_2.py` | 159 |
| `section_1_4_3.py` | 168, 174 |
| `section_1_5_2.py` | 198, 209, 214, 218 |

Only source comments were changed in these nine files; Python executable statements were not changed. The source provenance remains `WORD_EXTRACT_REASSEMBLED`, role and release gate unchanged.

**Hash registry:** Nine corresponding `sha256` fields in `docs/SOURCE_ROLE_AND_RELEASE_GATE.csv` refreshed in commit `dc450b87727f8618e91f9b0fdf5510ed71969a6a`. New bytes hashed as UTF-8 including terminal newline. SHA-256 implementation cross-checked against standard 'abc' test vector.

**CI scope:** GitHub Action run `40182527282` for last hash-only commit `dc450b8772` was QUEUED when inspected. Do not claim this head commit is CI PASS until its run completes. Earlier Linux run `40181424645` was successful for the previous §1.5.3 source fix. Windows CI after these nine edits not run/confirmed.

**Release:** All 17-chapter manuscript corpus classification and file rights audits are still open. G3/G4/G5/G6 HOLD. No Word master edited.
