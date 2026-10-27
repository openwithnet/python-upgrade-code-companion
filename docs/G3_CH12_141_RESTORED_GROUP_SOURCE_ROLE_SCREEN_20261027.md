# Chapter 12 G3 — restored 141 fragment role screen (2026-10-27)

Read actual Word v37 OOXML and the previous 141-row boundary-recovery CSV. This is a static role screen, not a numerical test.

Of 141 provisional groups:
- 66 restored groups parse and show no obvious Korean prose or standalone printed-output markers under a *coarse textual screen*.
- 26 restored groups parse but include array rows, output-like numbers or other ambiguous spans. These are **not identified errors**; many bracketed arrays are valid multiline source literals. Do not discard any of these lines without checking surrounding Python syntax.
- 49 groups still require a broader parent function/example context before a complete AST check.

The numerical split is **66 + 26 + 49 = 141** and **66 + 26 = 92** earlier AST restorations. Output file: `G3_CH12_141_Recovery_Content_Purity_Triage_20261027.csv`. The automated lexical classifications are provisional and not a comprehensive source/output census; in particular bracketed literal data can look exactly like printed arrays.

Next: apply AST node spans to distinguish in-expression literal array rows versus output text and map remaining 49 to enclosing complete Word code units. Only after that can duplicate group boundaries be consolidated into reliable canonical block IDs. No previous computations rerun; Word and production GitHub Python unchanged. G3 FULL HOLD, G4/G5/G6 HOLD. Intermediate artifact; user need not save.