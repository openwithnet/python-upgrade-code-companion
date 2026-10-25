# G3 — Chapter 1 Exact Word Paragraph Re-anchoring (2026-10-25)

**Scope:** 25 source-comment references in the *ten previously unaudited section files*, checked against current `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` using zero-based python-docx indices.

**Result:** 24 actual code paragraphs now located at **old index + 2**, validated against syntax-bearing Word `Source Code` paragraphs. The 25th source reference is a bare output `True`, currently Word p225, **removed already** from executable `section_1_5_3.py` in commit `29817fd`. This +2 mapping is established **only for these 25 references**; never apply it blindly to other chapters/other Word builds.

| Section | Source claimed anchor(s) | Verified current Word CODE anchor(s) |
|---|---|---|
| 1.1.2 | 26 | 28 |
| 1.1.3 | 32 | 34 |
| 1.2.2 | 50,54 | 52,56 |
| 1.2.3 | 64,69,74,84,88 | 66,71,76,86,90 |
| 1.3.2 | 105,109 | 107,111 |
| 1.3.3 | 118,122,129,134,137 | 120,124,131,136,139 |
| 1.4.2 | 157 | 159 |
| 1.4.3 | 166,172 | **168,174** |
| 1.5.2 | 196,207,212,216 | 198,209,214,218 |
| 1.5.3 | 221 (code); 223 (output expression) | 223 (code); **225 (expected output only)** |

**Selected CSV row (0-based iloc 17, column 3):** Chapter 1 §1.4.3 claimed Word p166, classified `HEADING` because p166 is the reduction subsection title. The corresponding executable code is p168, not p166. Similarly p172 (blank) maps to p174 code.

The actual Word code block starts were checked for names/statement contents and `Source Code` styles, not by accepting a raw 2-line offset alone. Source-comment updates and SHA-256 registry refresh are a separate controlled change; do not call the original source headers corrected until committed and CI verified.

**Gates:** G1 current Linux PASS as previously reported for the single-source change; G2 Windows latest amended commit not revalidated; G3 overall HOLD; G4/G5/G6 HOLD.
