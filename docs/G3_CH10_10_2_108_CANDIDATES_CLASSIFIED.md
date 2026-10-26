# G3 Chapter 10.2 — Classification of 108 Code-like Paragraphs

Date: 2026-10-26. Input: Word v37 QA and previous top-level paragraph candidate CSV. Each of the 108 §10.2 flagged paragraphs was assigned to an explicit source-span group, using the paragraph excerpt and known neighboring Word example boundaries. This is **candidate-context classification**, not fresh execution or exhaustive detection of all unflagged code.

Class totals: 103 dependent program lines; 4 assertion lines within existing examples; 1 Korean prose false positive at paragraph 2020. The 108 candidates belong to 9 code/example clusters and 1 prose cluster, not 108 programs.

Groups: A01 voltage conversion (1773–1779); A02 model states (1797–1825); A03 fixed-model function (1842–1855, not independently tested); A04 injected models (1863–1892); A05 recording model (1910–1930); A06 function composition (1952–1979); A07 object delegation (1991–2011); A08 inheritance prose (2020); A09 analysis delegation (2055–2067, dependency for A10); A10 integrated V/mV test (2093–2116).

**Execution evidence**: A01, A02, A04, A05, A06, A07, A10 were covered in the earlier seven scoped §10.2 executions, although A02 had reviewer-supplied input. A03 was not independently verified and A09 was executed only indirectly through A10 (using C3 dependencies). Code and tests are reconstructed; no byte-identical GitHub parity inferred. No additional execution PASS was created here.

Working evidence: `G3_CH10_10_2_108_Candidates_Context_Classified_20261026.csv`. Candidate rows now classified in the original four-section inventory: 68 (§10.1) + 108 (§10.2) + 17 (§10.7) = **193 of 314**, with 121 (§10.3) still unclassified. No Word/source edits. G3/G4/G5/G6 remain HOLD.