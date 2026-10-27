# Chapter 12 — G3 Consolidated Final Audit v1 (2026-10-27)

**Decision: SCOPED QA SUCCESSES RETAINED; G3 FULL APPROVAL = HOLD.**

## Purpose and authoritative scope
This is the consolidated gate-decision record, superseding a stream of standalone candidate-count progress reports. The authoritative manuscript is the unmodified `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`; its exact SHA256 in the current QA workspace is `94ea118680c3d8be1bfbbf5086d364f011b392e62526ab48a7d635b0517c2a47`. Chapter 12 direct Word paragraph range p4451–8621. The Word review master is authoritative, and OMML equations must be preserved. Existing Python/GitHub source remains unmodified.

## Audited facts, with evidence scope
| Layer | Measured fact | Gate meaning |
|---|---|---|
| Original heuristic candidate extraction | 889/889 paragraph candidate roles classified | Role screen complete, **not exhaustive block completeness** |
| Reverse Word paragraph screen | 3,282 formerly outside-889 top-level paragraphs screened; 76 hits; 28 code-form dependent/continuation positions recovered and mapped | Shows initial candidate extraction missed source lines; no new independent faulty programs demonstrated |
| Table-cell examination | 14 tables, 230 cell paragraphs reviewed; no standalone runnable source seen | Table scope screen complete; other Word stories not exhaustively certified |
| Provisional source inventory | 818 source-form candidate positions split into 249 gap-based groups | **Heuristic fragments, not 249 runnable programs** |
| 16 detailed original QA CSVs | Original 55 exact index intersections, 16 historical range-only references, another 65 group intersections | Index coincidence is weaker than full source execution evidence |
| Selected 36 previously unlinked groups | Consolidated to 23 Word contexts | Specific subqueue only; not a chapter-wide census |
| Selected 23 contexts | 22 source-literal executable contexts PASS; C12 is dependent keepdims snippet | Strong *scoped* evidence, not Chapter 12 full coverage |
| Reference GitHub modules | Five `REFERENCE` modules, 21 top-level functions, each marked `WORD_BASED_REPRESENTATIVE_RECONSTRUCTION` and `RETAIN_AS_CANDIDATE_NOT_FROZEN` | Topic-level alignment, NOT full verbatim canonical source equality |

## 249-group evidence partition — mutually exclusive
- 55 groups already intersect source paragraph indices in first six QA CSVs.
- 16 groups tied only to previous broad case ranges.
- 65 additional groups intersect source indices in next ten QA CSVs.
- 43 other groups gained Word source-line overlap from the separately executed 22-context corpus.
- **70 groups** do not intersect those specific indices or 22-context program lines.

Total = 55+16+65+43+70 = **249**.

The 70 are a **source-evidence routing queue**, not 70 failed / unexecuted programs. Their raw group texts show multiple fragments of previously documented computations, printed output expressions and dependent instructional snippets. A local risk register `G3_CH12_Consolidated_Final_Audit_70_Risk_Register_20261027.csv` assigns every such group a section-level evidence route and preserves its verbatim first-line sample. Counts: §12.1 3, §12.2 3, §12.3 9, §12.6 10, §12.7 11, §12.8 23, §12.9 9, section-parser-unknown 2. No test pass is inferred solely from this routing.

## Critical evidence gaps (blockers)
**B1 — Canonical complete executable-block register NOT DEMONSTRATED.** The 249 group boundaries were determined heuristically by punctuation/gaps and may split one executable function or combine several snippets. No independently exhaustive line-accurate code program inventory has been certified, especially from OOXML structures outside direct top-level paragraphs.

**B2 — Program-level literal-source-to-result chain NOT COMPLETE.** An indexed paragraph intersection, a previous reported execution range or a semantic contract test is not proof that *a particular entire complete Word program* executed with matching output. Need a stable canonical block ID -> exact source paragraph indices -> required imports/setup -> expected printed output/assertions -> named QA case/log -> PASS/FAIL/NOT_RUN with no scope inflation.

**B3 — Source packaging provenance unresolved.** The five Chapter 12 GitHub source modules openly declare educational representative reconstruction; all 21 top-level functions have topic-level Word counterparts but no 1:1 complete literal-source equality established. Decide whether to keep these as reference and publish separate literal executable blocks as a Code Companion, without treating them as canonical without evidence.

**B4 — Documentation hygiene and rights gates.** Report historical overlapping check totals without summing duplicate cases. G4 formatting/source provenance and G5 third-party rights/licensing must remain separate HOLD gates until applicable reviews are carried out.

## No known calculation defects
The previous audited Word-native examples and contracts described in the case documents PASS within their stated scopes. The 70 unlinked *fragment* group labels are not bug discoveries; do not create 70 unneeded test jobs or redo approved Chapters 6/10. A demonstrated production bug would merit a targeted source correction, with tests, not a broad rewrite.

## Decision gates / recommended efficient sequence
1. Freeze this evidence ledger as **G3 consolidated v1, HOLD** (not the book's canonical release): a single audit document + 70-item risk register within private GitHub.
2. Replace heuristic 249 fragment groups with **canonical runnable-context IDs** using actual Word line continuations and exact program boundaries. First resolve section-parser unknown entries (p6071, p7087–7111), dependent expressions and other clear overlaps.
3. For every canonical executable context, attach exactly matching test evidence (Word literal execution, expected output or reviewer contract clearly marked). Allow prior verified case reuse; only targeted-run unknown *complete* programs.
4. Conclude either **G3 SCOPED PASS, FULL HOLD** if any program lacks provenance, or **G3 FULL PASS** only once the full inventory and per-program evidence chain is established and reviewed.
5. Independently decide reference modules versus canonical extraction for Chapter 12 GitHub publishing. Do not silently rewrite Word or modules.

## Formal status
- **Candidate role audit:** COMPLETE.
- **23 targeted Word context audit:** COMPLETE, 22 executable PASS and one dependent.
- **249 provisional group final canonical boundary:** OPEN.
- **70 residual group evidence routing:** TRIAGED, NOT FULLY SOURCE-PROVEN.
- **Chapter 12 G3:** **FULL PASS HOLD / FINAL AUDIT v1 COMPLETE WITH BLOCKERS**.
- **G4/G5/G6:** HOLD.
- No new numerical computations were run in this consolidation. No Word or source code changed.

**User storage policy:** this is an interim auditable record in the private GitHub repository; no user download or local storage is requested. Only a truly frozen canonical release or essential recovery package will be tagged MUST SAVE.
