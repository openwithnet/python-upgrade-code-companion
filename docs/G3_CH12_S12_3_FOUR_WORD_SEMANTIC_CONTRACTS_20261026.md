# G3 Chapter 12 §12.3 — Targeted Word Semantic Contracts (2026-10-26)

Input: Word v37 `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, `word/document.xml` direct `w:body/w:p` zero-based. Actual selected Word statements were extracted and executed under NumPy. When Word spread a function/loop across paragraphs, Python indentation was restored to the stated structure. Reviewer assertions were added to test behavior; these assertions are **not** presented as literal Word code.

| Word code | Test | Result |
|---|---|---|
| p5465, 5467 | scalar broadcast `x+10` yields [11,12,13] | PASS |
| p5633,5635,5637–5640 and p5653,5655–5657 | explicit 2-D grid loop matches vectorized broadcast array | PASS |
| p5688,5691,5693 and p5697–5700 | erroneous time-axis scaling vs correct experiment-axis scaling have same (3,3) shape but different values | PASS |
| p5708–5728 (selected code positions) | `apply_experiment_scales`: valid (3,4) array with 3 scales succeeds; 3 malformed data/scales dimensions each raise `ValueError` | PASS |

The four are **targeted behavioral contract checks**, not four new independent programs or four newly unique cases relative to the historical 126-case chapter audits. The prior `G3_CH12_BROADCAST_ERRORS_BOOLEAN_12_CASES.md` contains semantically related coverage without fine-grained paragraph mapping; do not add four to 126 without de-duplication. These checks fill specific paragraph traceability gaps.

Source/Word defect: none found. The Word's scientifically intentional wrong-axis example should be retained as a teaching counterexample, not corrected into silence. No changes to Python source or Word. G3 Chapter 12 remains IN PROGRESS; G4–G6 HOLD. Chapter 6/10 calculations not rerun.
