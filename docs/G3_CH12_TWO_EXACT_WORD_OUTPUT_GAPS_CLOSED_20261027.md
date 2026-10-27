# Chapter 12 G3 consolidated audit — two remaining literal Word output gaps

Date: 2026-10-27. Canonical input: Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx. Paragraph numbers are zero-based top-level Word body paragraphs. No production Word/GitHub Python changes.

1. §12.3: Word code p5436–5441, using an explicit NumPy import as required setup. Word printed expected output at p5443: (3, 4). Observed stdout exactly (3, 4). PASS.
2. §12.8: Word import and expression array construction at p7591–7598; printed probes p7620–7622. Word expected output at p7624–7626: 2, (4, 4), 16. Observed same lines exactly. PASS.

These were two previously identified exact source/printed output evidence gaps in the seventy-group consolidated routing addendum; they are now directly verified. Reproducer source SHA256 values, full paragraph lists, setup, and expected vs observed outputs are in G3_CH12_Two_Exact_Word_Output_Gaps_20261027.csv (intermediate QA file).

Important gate boundary: closing these two cases does not resolve the other 58 prior-case-range references, ten dependent expressions, the definitive whole-Chapter-12 executable block inventory, or exact GitHub 21-function manuscript source provenance. Earlier historical tests have not been rerun. G3 Chapter 12 remains FULL HOLD / IN PROGRESS; G4/G5/G6 HOLD. Intermediate audit artifact; user need not save it.