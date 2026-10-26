# G3 Chapter 10.4–10.6: 27 Source Blocks and Pending Checks

Date: 2026-10-26. Word v37 G4 QA, zero-based top-level document paragraph indexes.

Twenty-seven logical code or conceptual blocks were identified by reading Word paragraphs 2638–3882 in context, rather than treating every line as an executable program. The per-block list is `G3_CH10_10_4_10_6_27_Block_Register_20261026.csv` in the QA working directory.

Previously checked blocks cover Euler/Midpoint solvers, `ConstantDerivative` isolated pytest (now in GitHub test and CI), first-order kinetics, analytic concentration and refactoring agreement. They were not re-counted as new executions.

**Outstanding specific targets**: §10.4.1 combined `FirstOrderModel`/`EulerSolver`/`Simulation` code p2680–2729; §10.4.2 fixed vs configurable simulation p2745–2794; §10.5.4 complete trajectory printout versus analytic values p3340–3366; §10.6.2 functional Euler callback p3571–3605 and object-based variant p3613–3634. These require complete snippet reconstruction and output comparison. The anti-pattern pseudocode, diagram and file tree in §10.6.3 are not standalone scientific programs.

This inventory is a manual logical block register, **not** proof that every program or line in the section is covered; it is not a new PASS tally. Some block locations are conceptual group ranges and can include prose between code paragraphs. Source-file exact-byte reconciliation remains separately open. Word and GitHub Python source were not modified; G3/G4/G5/G6 remain HOLD.