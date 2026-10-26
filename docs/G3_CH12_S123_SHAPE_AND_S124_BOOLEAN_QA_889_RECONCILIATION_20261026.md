# G3 Chapter 12 — Shape outputs and preexisting Boolean QA crosswalk (2026-10-26)

## Actual source and scope
Canonical Word v37 DOCX `word/document.xml` direct `w:body/w:p` zero-based. Baseline 889-row register `G3_CH12_889_After_S122_S123_Evidence_Integration_20261026.csv`. Previously saved original CSV `G3_Ch12_Broadcast_Errors_Boolean_12_Examples_20261026.csv` (six passing Boolean cases); **none rerun**.

## New literal output check
Word p5667 `a=np.ones((3,4))`, p5668 `b=np.ones(3)` are the preexisting setup. Executed only shape expressions p5673 and p5674, obtaining `(3, 4)` and `(3,)`, exact matches to Word p5676 and p5677. Two output statements pass, corresponding to one shared setup, not two independent full programs. The earlier expected broadcasting `ValueError` and fixed result already passed and were not rerun.

## Paragraph role/provenance changes
29 original REVIEW positions classified without renumbering, including: p4660 and p4666 axis explanations (not Python); p5673 and p5674 literal output evidence; 19 previously REVIEW candidate positions referenced **exactly** in historical successful Boolean QA source-case indices; other explanatory prose p5924, p6963, p7662, p7675, p7787, p7987. Each updated position has explicit `role_reason` and `source_audit` in the 889-row file `G3_CH12_889_After_Boolean_QA_and_S123_Shape_20261026.csv`.

## Status
Unclassified candidate positions **102 -> 73**. By section: 12.1 0; 12.2 0; 12.3 0; 12.4 4; 12.5 6; 12.6 18; 12.7 17; 12.8 4; 12.9 24. These counts represent Word paragraph candidates, not independently runnable programs or failed tests. No Word/GitHub executable source edits. Prior Chapter 6/10 calculations untouched. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.

Next: examine the 4 residual §12.4 candidate lines, §12.5 function contracts (6), then the longer source units §12.6–12.9 and link complete blocks to prior audits before any isolated new checks.