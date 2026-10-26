# G3 Chapter 12.5.3 / 12.6.1 — Eight Direct Python Verification Cases

Date: 2026-10-26. Word QA v37, zero-based paragraph indexes.

Eight reconstructed Word examples ran in the working Python environment. Seven exited successfully and one read-only array assignment raised the expected `ValueError: assignment destination is read-only`.

| Case | Word paragraphs | Verification |
|---|---|---|
| View mutation | 6631–6639 (code spans) | Printed `[10. 40. 60. 40.]`, matched Word p6641 |
| Copy isolation | 6646–6655 (code spans) | Printed unchanged raw and modified working, matched p6657–6658 |
| NumPy `out=` | 6695,6697,6699,6701 | `[2. 4. 6.]`, matched p6703 |
| Shared vs copied memory | 6713,6715,6717,6719,6720 | `True`, `False`, matched p6722–6723 |
| Read-only assignment | 6683,6685,6687 | Expected ValueError observed, as Word p6688 describes |
| Invariant test definitions | 6736–6754 (selected code paragraphs) | Both functions defined successfully. **Do not count as tests executed**: the Word snippet defines two test functions but does not invoke them; independent assertions inside functions were not evaluated by this run |
| Loop calculation | 6795–6802 (code spans) | `[3.0, 5.0, 7.0, 9.0]`, matches p6804 |
| NumPy vectorized calculation | 6806–6812 (code spans) | `[3. 5. 7. 9.]`, matches p6814 |

Note: 8/8 means script behavior matched its chosen verification criterion; the test-function definitions only passed syntax/execution at module level. Six examples have direct matching stdout, one intentionally fails and one defines functions. With the previous 70 scoped Chapter 12 cases, the *non-overlapping* running tally is 78 checks, not full manuscript coverage.

QA CSV: `G3_Ch12_12_5_3_12_6_1_Eight_Cases_20261026.csv`.

No Word or Python source changed. G3/G4/G5/G6 remain HOLD.