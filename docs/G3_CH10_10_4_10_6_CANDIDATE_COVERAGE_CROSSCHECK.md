# G3 Chapter 10.4–10.6 — Word Candidate Coverage Cross-check

Date: 2026-10-26. Using actual Word v37 G4 QA `word/document.xml` top-level paragraphs 2638–3906 and the existing 27-block register.

A conservative code-like text / style detector selected **194 paragraphs**. Of these, **189** fell in a previously recorded block interval; **five** fell outside: p3333 (`return c0 * exp(-k * t)`) and p3367–3370 (remaining four Euler/analytic printed-output lines). All five are continuations of two already reviewed blocks, not previously overlooked independent executable examples.

**Register corrections**: exact-first-order block start 3321 end 3333 (previously 3331); trajectory printed-output block start 3340 end 3370 (previously 3366). The 27-block count remains unchanged. Revised working CSV: `G3_CH10_10_4_10_6_27_Block_Register_COVERAGE_CORRECTED_20261026.csv`. Candidate data: `G3_CH10_10_4_10_6_Uncovered_Candidates_20261026.csv`.

Important limit: this is a heuristic scan. A code-like line may fail the pattern and escape detection; no claim of exhaustive entire-chapter code coverage. Previously executed code checks remain valid for their own scopes; no fresh execution in this pass. Further exact source mapping and provenance review still required. GitHub source and Word unchanged; G3/G4/G5/G6 HOLD.