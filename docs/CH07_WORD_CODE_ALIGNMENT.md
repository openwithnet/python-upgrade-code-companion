# Chapter 7 B1 — Scoped Word/Code Alignment (2026-10-25)

**Decision:** Representative B1 sequence object design agrees with Word v37 Chapter 7 §§7.1–7.7. **This is not proof of complete original-manuscript 1:1 identity or redistribution rights.**

| Word section | Source/test | Evidence |
|---|---|---|
| 7.1–7.2 conceptual inheritance vs biological taxonomy | `_SequenceBase`, `DNASequence`, `RNASequence`, `ProteinSequence` | Shallow reuse and domain-specific behavior; Protein has no GC method |
| 7.2.3 polymorphism | `HasSequence(Protocol)`, `describe_sequence` | Common `sequence` property and `length()` contract |
| 7.3.1–7.3.2 composition and delegation | `SequenceData`, `AlphabetPolicy`, `_SequenceBase` | Normalization, alphabet validation, composition and delegation |
| 7.4.2 alphabets | `DNA_POLICY`, `RNA_POLICY`, `PROTEIN_POLICY` | ACGT, ACGU, canonical 20 amino-acid symbols |
| 7.5.1–7.5.2 B1 example | `b1_sequences.py` `__main__` and `test_b1_sequences.py` | DNA ATGCGC and RNA AUGCGC GC=4/6=0.6667; Protein MKWVTF W=1/6=0.1667 |
| 7.6.3 refactor | `calculate_gc_fraction`, DNA/RNA `gc_fraction()` | Shared computation, no `gc_fraction` on Protein |
| 7.6 input contract | `SequenceData`, `AlphabetPolicy` and test cases | Uppercasing, nonempty, invalid alphabet/type rejection; no implicit N acceptance |

**Contract nuance:** `calculate_gc_fraction(sequence)` checks only type and nonempty, *not* alphabet or case. It expects an already validated uppercase DNA/RNA string. The Word v37 §7.6.3 description states that prerequisite. A direct call with an unvalidated lowercase string would not be equivalent to the object methods. Avoid claiming the independent helper validates alphabet itself.

**Test evidence:** GitHub CI Run `40140880013` covered Chapter 7 under Windows/Miniconda (overall 30/30 checks). Existing source test contains checks for DNA/RNA GC=4/6, protein W=1/6, bad symbols, empty sequences, class contract, frozen `SequenceData`, and lack of protein GC.

**Open:** Historical Word source 1:1 equivalence remains NOT_PROVEN; archived source provenance `ARCHIVED_CHAPTER_REVIEW_COPY` and redistribution rights UNVERIFIED; user-local environment untested. Do not clear G3, G5, G6 or delete warnings solely on this scoped check.

**Source files:** `chapters/chapter07/original_package/b1_sequences.py` and `test_b1_sequences.py`.
