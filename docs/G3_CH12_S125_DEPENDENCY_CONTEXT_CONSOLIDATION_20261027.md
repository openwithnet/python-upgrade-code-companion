# Chapter 12 §12.5 — source dependency consolidation

Date: 2026-10-27. Authoritative source: Word v37. No calculations rerun.

All 24 existing §12.5 provisional code groups were assigned exactly once to 21 proposed instructional source contexts. Contexts cover introductory view/copy, ndarray shape/dtype, view mutation, explicit copy, basic/advanced indexing memory relations, base, normalization functions, strides, C/F memory order, contiguous flags, slice/transposed/negative strides, reshape copy, data integrity, pure/in-place scaling functions, read-only mutation, ufunc out, shares_memory and Word-authored unit tests.

The 21-row local register G3_CH12_S125_24_To_21_Dependency_Context_Proposal_20261027.csv retains every original group ID, Word source paragraph set, parent span and topic. These are proposed contexts, not 21 independently executed programs or QA PASS.

Overall progress through §12.5: §12.1 29 to 13; §12.2 31 to 14; §12.3 35 to 16; §12.4 35 to 16; §12.5 24 to 21. Total 154 provisional groups assigned to 80 proposed contexts. The broader 249-group inventory and 889-candidate register remain unchanged.

Important distinctions: normalize_inplace versus normalized have different mutation contracts; scale_measurements and scale_measurements_inplace likewise. Tests at Word p6736–6754 are separate verification source, not a duplicate independent algorithm. Word p6711 is a dependent shares_memory expression; its complete example follows at p6713–6720. The read-only assignment p6687 intentionally raises an error; do not label it a failing implementation.

Next: consolidate §12.6–§12.9 by the same dependency-grounded method and then build the whole-chapter manifest with distinct source/QA evidence levels. Chapter 12 G3 FULL HOLD; G4/G5/G6 HOLD. Production Word and GitHub Python sources unchanged. Intermediate audit; user need not save.