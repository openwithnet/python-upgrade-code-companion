# G3 — Chapter 1 Word Anchor Classification / Chapter 6 Comparison Gate (2026-10-25)

**Scope:** Cross-checked 25 paragraph indices from the 10 remaining Chapter 1 study files against `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` using current zero-based `python-docx` paragraph positions. **These are original source-comment claimed indices, not verified block mappings.**

| Actual type at claimed index | Count |
|---|---:|
| Heading | 7 |
| Subheading | 6 |
| Code-styled paragraph | 5 |
| Code-likely other style | 1 |
| Explanatory text or printed output (not conclusively separated by automatic classification) | 5 |
| Empty | 1 |
| **Total** | **25** |

Examples: §1.1.2 source claims p26 but Word p26 is its *heading*; §1.1.3 claims p32 but Word p32 is a *heading*; §1.3.2 source p109 is printed output; §1.5.2 source p216 is output (`Gene A: 12.33`...); §1.5.3 source p223 matches code, while Word p225 is expected output `True`. Therefore globally shifting all anchors by one is unsafe. **The next correct fix is to locate full code block text in the latest Word, then re-anchor each source comment individually.** A local CSV captures all 25 classifications.

**Chapter 6:** v37 Word §6.5.2 120-line extract and repository `p1_particle_trajectory.py` show same named modules, executable flow and numeric outputs. GitHub adds three role/provenance/release header lines. A byte-for-byte, whitespace/newline-aware diff on both actual files (minus headers) has **not yet been independently produced**, so exact textual match remains NOT_PROVEN. Do not assert content identity based on matching print output.

**CI:** Linux run `40181424645` for the §1.5.3 source correction completed SUCCESS. Inventory SHA for the corrected file was refreshed in commit `99e65771de7c50ed75dd3eafceceadfe4e55cead`. That does not renew the previous Windows CI against the amended commit.

**No additional Python or Word sources were changed in this audit.** G3/G4/G5/G6 remain OPEN.
