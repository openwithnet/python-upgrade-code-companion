# G3 — Chapter 12 §12.2.1–12.2.2 Ten Word-Extracted Execution Checks (2026-10-25)

**Result: 10/10 executed successfully and 10/10 expected stdout matches.** Latest G4 QA Word source `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`. Python code extracted by zero-based paragraph index; executed under the current working Python environment, not independent Windows revalidation.

| Example | Word code paragraphs | Word expected-output paragraphs | Result |
|---|---|---|---|
| ndim/shape/size for 2x3 | 4870,4872–4875,4877–4879 | 4881–4883 | 2; (2,3); 6 |
| scalar/vector/matrix shape | 4914–4916,4918–4919; import from 4870 | 4921–4923 | 0 (); 1 (1,); 2 (1,1) |
| indexed element | 4932–4935,4937 | 4939 | 60 |
| indexed row | 4932–4935,4943 | 4945 | [40 50 60] |
| indexed column | 4932–4935,4947 | 4949 | [20 50] |
| indexed result shapes | 4932–4935,4951–4952 | 4954–4955 | (3,); (2,) |
| 3x4 array shape | 4980–4984,4986 | 4988 | (3,4) |
| grand mean | 4980–4984,4992 | 4994 | 5.0 |
| axis=0 mean | 4980–4984,5002–5005,5007–5008 | 5010–5011 | [2,4,6,8]; (4,) |
| axis=1 mean | 4980–4984,5019–5022,5024–5025 | 5027–5028 | [2.5,5,7.5]; (3,) |

**Method:** Reconstructed declared imports and prior array definitions as prerequisites. Compared Python stdout against Word using whitespace-token normalization without changing numeric values; all Python subprocesses exit 0.

**Scientific/editorial notes:** (1) Word p4897–4904 is an ASCII axis diagram, not runnable code. (2) Actual View vs Copy behavior belongs primarily to §§12.4–12.5 and has not been audited by these ten checks. (3) This is scoped Chapter 12 evidence, not all-Chapter execution; previous §12.1 audits counted 19 checked example executions, so the nonoverlapping subtotal for §§12.1–12.2 is 29. (4) Some examples share prerequisite definitions; the ten executions do not imply ten independent GitHub scripts.

**Artifact:** `G3_Ch12_12_2_Executed_10_Examples_20261025.csv` contains per-example stdout, expected output and process return code. No Word/Python source files modified. G3/G4/G5/G6 remain HOLD.
