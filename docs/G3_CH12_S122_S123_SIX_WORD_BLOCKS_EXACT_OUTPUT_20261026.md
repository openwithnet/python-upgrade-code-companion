# G3 Chapter 12 — Six Word-native block checks (2026-10-26)

Source: Word v37 OOXML, original paragraphs; NumPy import as isolated setup. All six code blocks compiled, executed, and matched printed Word results exactly. No historical cases were deliberately rerun.

| Case | Word source | Result |
|---|---|---|
| Three-axis averaging | 5167–5215, selected original code paragraphs | PASS, exact outputs |
| Temperature spatial/time aggregation | 5229–5247, original code paragraphs | PASS, exact shapes |
| Chemical species selection | 5260–5266 | PASS, shape (3,5) |
| Gene expression mean | 5277–5287 | PASS, [3. 5. 8.] |
| Axis reordering | 5300–5304 | PASS, (20,30,10) |
| Broadcast-shape precheck | 5738–5743 | PASS, (3,4) |

Detailed per-case paragraph indices, original displayed expected values, actual stdout, and extracted-code SHA-256: G3_CH12_S122_S123_New_Word_Blocks_20261026.csv (local QA artifact).

Word p5774 result = a * b + c is a dependent educational expression, not an independent runnable snippet without input arrays. Word p5348 and p5507 are prose. p5090 requires prior variable setup; no standalone claim made.

These are six scoped execution contexts, not proof of Chapter 12 full completion. Chapter 12 G3 IN PROGRESS; G4–G6 HOLD. Word and Python production sources unchanged; Chapter 6/10 calculations not rerun.