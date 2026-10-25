# G3 — Chapter 10 & 12 Context Verified Groups (2026-10-25)

**Status: 24 hand-checked group classifications in the current Word G4 QA manuscript; no new code execution, no global G3 PASS.** 24 entries were selected from the prior Chapter 7–12 automatic group triage and classified using adjacent Word paragraphs, not merely preview fragments.

| Classification | Count | Evidence |
|---|---:|---|
| DEPENDENT_CODE, including CONTINUATION | 13 | Source fragments require preceding variables/imports, or span blank paragraphs and a single earlier control-flow block |
| EXPECTED_OUTPUT | 6 | Output follows explicit Word labels such as `출력:` or `예상 출력:` |
| DIAGRAM | 5 | Chapter 10 ASCII flowchart arrow fragments at p1542–1554, not Python |

**Examples and corrected boundaries**

- Ch10 p1456–1458 is the continuation of an earlier `for` loop and cannot be executed independently; the complete earlier example is p1444–1460. p1462 is labeled output.
- Ch10 p1542,1545,1548,1551,1554 consist of vertical/arrow characters in a textual process diagram. Their automatic candidate grouping is misleading: do not extract them as programs.
- Ch12 p4523 and p4525 form the list-repeat demonstration, while p4527 is **expected output**; p4531/4533 is a dependent NumPy array demonstration with output p4535.
- Ch12 p4547–4551 form the array-squaring snippet and p4553 is its expected output. p4557–4561 is a separate exponential-vector snippet depending on `np`.
- Ch12 p4570–4586 is one vectorized first-order decay example; p4588 is expected output, not runnable code.

**Data:** `G3_Ch10_Ch12_ContextVerified_24_Groups_20261025.csv` in QA working output includes each group ID, precise Word range, verified classification, context reason and reconstructed example boundary. This evidence does not automatically resolve the remaining 1,066 groups (of the earlier 1,090) and does not claim that 24 groups correspond to 24 distinct runnable examples.

**CI:** GitHub Linux Action run 40182527282 on the earlier 9-file Chapter 1 reanchor change was still **QUEUED** at check time. No CI completion claim is inferred from this unrelated classification pass.

**Next:** expand context review in contiguous spans, prioritize Ch12 output/text fragments, and keep source mapping separate from execution results. No Word/Python source edits or release-gate changes.
