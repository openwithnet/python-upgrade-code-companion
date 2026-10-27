# Chapter 12 G3 Consolidated Audit — Tier A literal source static boundary verification (2026-10-27)

Authoritative source: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`; parsed `word/document.xml`, direct body paragraphs (zero-based). This is a *source-identity and syntax* audit, not a new numerical execution audit.

## Explicit Word source blocks
Manually selected exact Word Python statement paragraphs and retained the original line indentation, including multiline function signatures, calls and arrays.

| Block | Word code source | Static AST |
|---|---|---|
| Euler function `simulate_euler` | p7082–7123 (selected source lines, omitting intervening prose/blanks) | PASS |
| Euler example invocation/print | p7125–7132 | PASS |
| Expression matrix construction | p7593–7598 | PASS |
| Sample/gene/group metadata | p7600–7610 | PASS |
| Expression dimension/shape/size probes | p7620–7622 | PASS |
| Expression sample totals | p7670,p7672,p7677 | PASS |
| Expression gene means | p7687,p7689 | PASS |
| Row totals, broadcast normalization, printing | p7774–7798 (selected source lines) | PASS |
| Per-row 100-percent assertion | p7811–7820 (selected source lines) | PASS |
| Wrong-axis, scientifically misleading alternative | p7826–7833 (selected source lines) | PASS |

**10/10 exact selected code components pass Python AST parsing**. Detailed exact paragraph-ID lists and UTF-8 source SHA256 values: `G3_CH12_TierA_Exact_Word_Static_Manifest_20261027.csv`.

## Evidence tie-in; keep result gates separate
- Euler has a prior 9-case audit that executed a reconstruction spanning p7080–7134 and reports literal expected result `[1.,0.8,0.64,0.512,0.4096,0.32768]`, plus exception/type contracts. Prior scoped numerical PASS is preserved; the present static source check does **not establish source-byte identity** of that earlier execution with the current reconstructed function and call.
- Expression analysis has a prior 12-case audit that executed selected reconstructed examples and ten Word printed results (two nonprinting contracts). Some literal Word contexts have later targeted execution evidence. The ten static component definitions here are not claimed to be all §12.8 executable blocks (group calculations, log2, `relative_by_sample`, etc. exist elsewhere), and this is not a fully comprehensive Chapter 12 block count.
- The wrong-axis demonstration intentionally produces an array but is **scientifically the incorrect sample normalization**; AST success cannot certify scientific validity.

## G3 decision
Tier-A **selected statement boundary and syntax**: PASS 10/10. Tier-A historical case identity **PARTIAL, NOT YET VERIFIED END-TO-END**. Full Chapter-12 canonical executable block manifest **OPEN**. Source-only vs executed evidence levels remain distinct.

No original Word, OMML, GitHub production Python, or previous QA records modified. No past numerical cases rerun. Chapter 12 G3 FULL HOLD, G4/G5/G6 HOLD. Intermediate internal artifact; user need not save.