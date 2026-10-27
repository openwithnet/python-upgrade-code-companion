# Chapter 12 §12.6 — dependency-context consolidation (2026-10-27)

Canonical source: Word v37, unchanged. All **22 provisional §12.6 groups** assigned exactly once to **15 proposed instructional contexts**. Group membership, Word paragraph ranges, exact selected source positions and roles are preserved in `G3_CH12_S126_22_To_15_Dependency_Context_Proposal_20261027.csv` (internal interim register).

| Context | Word paragraph range | Topic |
|---|---|---|
| S126-01 | 6795–6812 | Python list vs NumPy result |
| S126-02 | 6837–6861 | decay loop vs array |
| S126-03 | 6873–6909 | benchmark plus result equivalence check |
| S126-04 | 6924 | dependent temporary-array expression |
| S126-05 | 6932–6939 | memory / nbytes |
| S126-06 | 6949–6962 | chained temporary arrays vs hypot |
| S126-07 | 6972–6981 | ufunc out |
| S126-08 | 6990–6994 | in-place array update |
| S126-09 | 7006–7053 | scale_in_chunks definition, body and call |
| S126-10 | 7080–7132 | simulate_euler definition, body and call |
| S126-11 | 7146–7156 | Euler for multiple independent initial conditions |
| S126-12 | 7167–7177 | np.where conditional values |
| S126-13 | 7184–7188 | np.where eager evaluation caveat |
| S126-14 | 7200–7213 | np.vectorize comparison |
| S126-15 | 7221–7223 | pairwise difference array memory blowup |

Completeness: 22 original group IDs included without omission or duplication. These 15 records are educational/dependency **contexts**, not 15 independent runnable scripts, and not 15 newly passed runtime cases. S126-04 and S126-15 need upstream variable definitions to execute. Distinguish vectorization across independent initial conditions from sequential time stepping in Euler, and differentiate `np.where` conditional output from eager evaluation of branch expressions. Prior scoped QA is retained; no reruns performed.

Cumulative §12.1–§12.6: **176 provisional groups -> 95 proposed contexts** (29->13, 31->14, 35->16, 35->16, 24->21, 22->15). Work remains §§12.7–12.9 and whole-chapter canonical block register, source-level runtime attribution, and G3 final gate. **G3 FULL HOLD / IN PROGRESS; G4–G6 HOLD**. No Word or GitHub executable code changed. Intermediate record does not require user archival.