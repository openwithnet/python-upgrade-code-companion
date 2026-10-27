# Chapter 12 G3 — Section 12.3 source dependency consolidation (2026-10-27)

Authority: unmodified Word v37 and the 249-group provisional Word-source inventory. In §12.3, **35 provisional groups have been assigned to 16 instructional source contexts** by shared input, calculation and function/test relationship, with all 35 original block IDs and Word source paragraph positions preserved.

Examples: matrix plus vector Broadcasting p5413–5423; broadcasting shape precheck p5436–5445; experimental vs time-axis scale p5485–5527; variable-rate concentration p5572–5590; 3D scaling p5601–5623; grid via broadcasting and loops p5633–5657; incompatible shape and repair p5667–5682; same-shape wrong-axis semantics p5688–5697; Word function apply_experiment_scales p5708–5728; shape precheck p5738–5743; Word-authored unit tests p5783–5819.

**Important distinct role:** p5774 `result = a * b + c` is a dependent explanatory temporary-array expression, not a standalone runnable program. The Word-authored tests are distinct from the implementation function, and may share its setup. Context boundaries are inclusive *review ranges* that can contain explanatory prose and expected stdout, not whole-source literal extraction. No numerical tests rerun and no new runtime PASS claimed.

Working manifest: G3_CH12_S123_35_To_16_Dependency_Context_Proposal_20261027.csv, 16 contexts with exact provisional member IDs and selected Word paragraph positions. Running totals for the dependency proposal: §12.1 29->13, §12.2 31->14, §12.3 35->16; subtotal 95 provisional groups assigned to 43 proposed contexts. These are not 43 independently runnable programs.

Next continue §12.4 and later sections, preserve historical QA evidence, then consolidate into a full Word-context manifest and compare against five representative GitHub modules. Chapter 12 G3 FULL HOLD; G4/G5/G6 HOLD. Intermediate internal audit: user need not save.