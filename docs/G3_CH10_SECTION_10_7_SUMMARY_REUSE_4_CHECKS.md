# G3 Chapter 10.7 — Summary Snippet Reuse Verification

Date: 2026-10-26. Word v37 QA document, top-level zero-based paragraph anchors.

Four summary-based checks executed in Python and passed: volts_to_millivolts(.009)=9 (p3929–3930), Euler with FirstOrderModel(.2) and dt=1 returns .8 (p3963–3967), Midpoint returns .82 (p3969–3973), and first_order_concentration(1,.2,5) equals exp(-1) (p4009,4012–4017).

The Euler and Midpoint classes were imported from a prior locally reconstructed source copy. The other summary examples were reconstructed with indentation from Word. These are summary-code REUSE checks, not four additional original independent executable programs or exact Word printed output matches. CSV evidence: G3_CH10_10_7_Four_Summary_Checks_20261026.csv. Harness: g3_ch10_7_summary_checks.py.

Word §10.4.4 p2970–3071 also contains distinct test designs: direct signed derivative, ConstantDerivative solver isolate, RecordingSolver invocation, and Euler/Midpoint integration. Source tests cover some but not all of these Word cases; exact complete test-body parity remains pending. More source and Word checks are needed before whole-chapter G3 PASS.

No Word or GitHub executable code changed. G3/G4/G5/G6 HOLD.