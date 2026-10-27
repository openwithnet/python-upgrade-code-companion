# G3 Chapter 12 — Extend 249 provisional block source trace using 10 additional QA CSVs (2026-10-27)

## Work performed
Using the previously created `G3_CH12_Provisional_Source_Block_and_QA_Trace_20261027.csv` (249 provisional Word-code group IDs), loaded **10 additional original detail CSVs** available in the QA workspace. These supply **61 case rows with paragraph references**. A strict paragraph-index intersection was recorded for each provisional group; no Python arithmetic cases were rerun.

Sources used: `G3_CH12_12_2_Targeted_5_Cases_20261026.csv`, `G3_CH12_12_3_Four_Semantic_Contract_Checks_20261026.csv`, `G3_CH12_Targeted_Unmapped_Cases_20261026.csv`, `G3_CH12_S12_1_Six_Unmapped_Word_Cases_20261026.csv`, `G3_CH12_S12_8_FOUR_REMAINDER_CHECKS_20261026.csv`, `G3_CH12_S122_S123_New_Word_Blocks_20261026.csv`, `G3_CH12_S126_S127_Six_Word_Blocks_20261026.csv`, `G3_CH12_S124_S125_Last10_Word_Block_Contracts_20261026.csv`, `G3_Ch12_Broadcast_Errors_Boolean_12_Examples_20261026.csv`, and `G3_Ch12_12_5_3_12_6_1_Eight_Cases_20261026.csv`.

## Evidence results
Cross-tab for the **249 provisional groups**:
| Earlier six-CSV evidence tier | New ten-CSV intersects | No new intersection | Subtotal |
|---|---:|---:|---:|
| Prior detailed-case index intersection | 13 | 42 | 55 |
| Prior broad historical case range | 0 | 16 | 16 |
| Previously no indexed case proof | **65** | **113** | 178 |
| **Total** | **78** | **171** | **249** |

Important: **65 previously unlinked groups acquire a new source-paragraph intersection**. The previously unlinked number thus moves **178 -> 113** for this *16-CSV-index* scope. But 113 is **not** the number of unverified runnable programs. Some sources provide case ranges or code fragments and previous other QA documents may cover them.

The evidence is `INDEX_INTERSECTION_ONLY_NOT_LITERAL_BLOCK_PROOF`: a shared paragraph ID is not by itself proof of a fully executed Word block or matching printed result. A full gate needs precise block-source extraction and case-to-block proof, especially for multi-paragraph functions and dependent context.

Updated per-group evidence file: `G3_CH12_249_Blocks_Additional_10_CSV_QA_Intersections_20261027.csv`. There are no production code or Word changes. Existing Chapter 6/10 numerical checks untouched. Chapter 12 G3 IN PROGRESS, G4/G5/G6 HOLD.

## Next
1. Validate the retained **113 groups** against additional existing case records, including those whose descriptions lack paragraph-index CSV data, before declaring any tests missing.
2. Stabilize real source-block boundaries rather than interpreting gap-based 249 groups as programs.
3. Audit GitHub's 21 representative function mappings to Word blocks separately and label non-verbatim provenance.
4. Summarize formal G3 gate gaps without inflating check totals.

This is an intermediate internal QA artifact. The user is **not** being asked to download or archive it.