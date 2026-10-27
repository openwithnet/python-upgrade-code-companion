# G3 Chapter 12: 23-context evidence join and two source executions

Date: 2026-10-27. Source: Word v37, direct document.xml. No production modifications.

We matched paragraph indices of 23 reconstructed contexts against the accessible 14 case-level QA CSVs. None of the 23 contexts had an explicit source-paragraph intersection in this limited CSV subset. This is a provenance gap for the selected files, not evidence that all contexts are untested or incorrect. Crosswalk: G3_CH12_23_Context_Raw_QA_Source_Overlap_20261027.csv.

New narrowly scoped Word-source executions:

- C01: p4599–4608, Python loop and NumPy array square computation, both pass a reviewer-added equivalence assertion, [1,4,9].
- C23: p7006–7053, full original scale_in_chunks function and original call, result [2.5,5,7.5,10], input preserved; PASS with reviewer numeric assertion.

Exact paragraph IDs, values, source hashes and evidence limits: G3_CH12_C01_C23_Exact_Word_Execution_20261027.csv. These are two source contexts, not two claims of book-wide coverage. C12 remains a dependent keepdims snippet, not an independently missing program. Twenty other contexts need precise evidence reconciliation, without presuming failure. Existing checks not deliberately rerun.

Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD. Word and GitHub Python unchanged. Intermediate audit; user need not save it.