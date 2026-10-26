# G3 — Chapter 12.6 Memory and Vectorization Audit (2026-10-26)

**Eight reconstructed Word examples verified in the current QA environment.** Word source: v37 G4 QA §§12.6.1–12.6.2. Five examples match explicit printed Word expected outputs; three have no printed Word output or use reviewer-added assertions. All eight execute successfully after appropriate prior-array setup.

| Case | Word code location | Verdict |
|---|---|---|
| scalar exponential loop | 6837–6850 | successful, no printed expected Word output |
| NumPy vectorized exponential | 6852–6861 | matches expected Word p6863 |
| float64 nbytes 1,000,000 | 6932–6939 | matches 8000000, Word p6941 |
| hypot with pre-defined a,b | 6932,6949–6952,6962 | successful after context restoration; no printed Word output |
| out= reusable buffer | 6972–6981 | matches Word p6983 |
| in-place x *= 2 | 6972,6990–6994 | matches Word p6996 |
| chunked scaling (indentation restored) | 7006–7053 | matches Word p7055 |
| input integrity with buffer versus in-place | reviewer assertions based on 6972–6996 | tests passed; not a printed original Word example |

Performance measurement separately used n=200,000, five repetitions, warmed calculation, NumPy array construction excluded. Python 3.13.5, NumPy 2.3.5. Median Python-list time 12.46 ms; NumPy expression 0.45 ms in this run. No portable speedup claim; intermediate array peak memory NOT measured. No scientific-data conclusions derive from benchmark alone.

The initial hypot extraction failed because it omitted the preceding array definitions; corrected reconstruction executed normally. This was a context-extraction issue, not a Word algorithm error.

**Cumulative scoped Chapter 12 audit:** 78 earlier cases + 8 = 86 cases. These are auditing events, not 86 distinct independent .py programs. Entire chapter still not exhaustively classified. No GitHub source or Word master modified. G3/G4/G5/G6 HOLD.