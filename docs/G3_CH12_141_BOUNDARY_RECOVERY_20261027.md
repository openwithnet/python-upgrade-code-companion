# Chapter 12 G3: 141 fragmented Word group boundary recovery

Date: 2026-10-27. Word v37 OOXML; no source changes or numeric execution.

The original 249 provisional groups included 141 selected extracts that did not parse. Restoring **unaltered original Word paragraph text** gave these outcomes:

- 35 groups parsed after restoring intervening Word paragraphs within their old start/end range.
- 57 more parsed after appending up to four original following paragraphs.
- 49 still required a wider enclosing code context or removal of non-code passages.

These are AST-only boundary observations, not 92 newly passing runnable programs or 49 program errors. Parsing an interval can accidentally include output or narrative: code-role confirmation remains mandatory.

Detailed 141-row evidence: G3_CH12_141_Gap_Boundary_Recovery_Screen_20261027.csv. Reproducer: ch12_gap_recovery.py in the audit workspace.

Next: classify restored intervals as code versus prose/output; attach unresolved 49 to full parent routine, then deduplicate before a canonical chapter-wide block manifest. Chapter 12 G3 FULL HOLD; G4/G5/G6 HOLD. No Word/GitHub production modifications. This is an intermediate QA record; no user download requested.