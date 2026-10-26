# G3 — Chapter 10/12 Additional Context Audit

Date: 2026-10-26. Source: Word v37 G4 QA manuscript and previously registered automatic candidate groups.

**42 additional candidate groups reviewed directly against adjacent Word paragraphs:** 17 in Chapter 10 and 25 in Chapter 12.

| Verified classification | Count |
|---|---:|
| DEPENDENT_CODE (within an earlier method, loop or example) | 28 |
| EXPLANATORY_CODE (summary illustrations, not standalone) | 6 |
| DIAGRAM (flow arrows) | 5 |
| EXPECTED_OUTPUT | 2 |
| FILE_TREE (filenames in an architecture listing) | 1 |

Chapter 10's fragments around paragraphs 2885, 2889, 3258–3300 are indented continuations of program definitions, not separate standalone scripts. Its paragraphs 3680–3692 are a process diagram, and paragraph 3748 is a directory tree. Chapter 12 paragraphs 8212–8451 include continuations from particle-motion listings and outputs already inspected in the earlier 12.9 execution audit. Chapter 12.10 paragraphs 8500, 8519, 8527 and 8529 are educational expressions referring to prior variables, not independent executable examples.

Working evidence CSV: `G3_Ch10_Ch12_Additional_Context_42_Groups_20261026.csv`, containing group IDs, exact Word positions, adjacent prose, selected classification and explicit `NOT_RUN` for this pass. **No new execution PASS is claimed and previously counted 126 Chapter 12 case checks remain unchanged.** These 42 groups are classification decisions, not 42 separate Word program executions.

This contextual sample is not an exhaustive classification of all Word code blocks. GitHub Python sources and Word master were not edited. G3/G4/G5/G6 remain HOLD.