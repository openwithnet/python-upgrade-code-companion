# Chapter 12 G3 Consolidated Audit v1 — 70-Group Evidence Routing Addendum (2026-10-27)

## Result and limits
Re-read the 70-row residual risk register from the consolidated G3 v1 audit and cross-checked the **actual paragraph ranges** against previously documented Word-source test passages. This is a *provenance-routing exercise only*, not re-execution, literal whole-block validation or release approval.

| Evidence routing category | Provisional groups |
|---|---:|
| Intersects a prior **Word-native executed context or scoped QA range**; needs precise line-by-line case join | **58** |
| Clearly **dependent expression or standalone print requiring earlier setup**, not a new self-contained program | **10** |
| No exact source case in the evidence subset consulted | **2** |
| **Total** | **70** |

The two unresolved exact-source joins are **p5436–5437** (`np.broadcast_shapes` multiline print) and **p7620–7622** (expression `.ndim`, `.shape`, `.size` print lines). Their code roles are understood, and the surrounding examples were studied in past audits, but this pass does not assume exact literal execution for those lines. Do not interpret these as discovered defects.

The 58 group intersections include §§12.3, 12.6, 12.7, 12.8, 12.9 and the formerly unknown p7087–7111 (Euler signature/body continuation); a **range overlap is not proof that every source line or the entire program was executed**, especially in §12.8 historical 12-case records. The 10 dependents include print statements and `keepdims`, `np.ix_`, temporary-array, and prohibitive giant-allocation illustrations. Some require manual source-boundary review; do not automatically exclude them from a complete run context.

Record: `G3_CH12_70_Final_Audit_Evidence_Routes_20261027.csv`, one row per original risk-register group with evidence route and evidence labels. All 70 retained; no status misleadingly changed to PASS.

## G3 decision and precise next actions
1. Confirm p5436–5437 and p7620–7622 using original Word setup, printed outputs and prior precise audit data. Only execute missing literal statements if existing case logs do not prove them.
2. For the 58, join each *complete* Word function/call/source group with exact QA execution statements/outputs instead of treating range intersection as FULL PASS.
3. Fold the 10 dependent statements into their parent executable contexts or explicitly mark as educational snippets.
4. Build a canonical whole-chapter block manifest (not the heuristic 249 groups), then review the 21 representative GitHub reference functions independently.

**G3 Full: HOLD**; earlier scoped passes unchanged. G4/G5/G6 HOLD. No Word or GitHub Python production edits, no Chapter 6/10 retesting, and no new computation in this addendum. Internal intermediate record: user need not save.
