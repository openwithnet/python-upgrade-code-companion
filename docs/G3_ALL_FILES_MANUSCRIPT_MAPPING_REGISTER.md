# G3 — Repository Source to Manuscript Mapping Register

**Status: WORKING / NO FULL 1:1 VERIFIED.** This 81-file register is generated from the existing provenance/hash CSV; it does not change the file-role or release decisions. A documented *scoped* alignment does not certify each file.

## Interpretation

- `SCOPED_EVIDENCE_AVAILABLE`: a chapter-level comparison exists; it may only apply to certain representative source files and examples. Consult linked evidence before claiming a match.
- `NO_SCOPED_EVIDENCE`: no chapter-specific audited correspondence in the current reviewed set; **not** evidence of no match.
- `TEST_OR_INTERNAL_QA`: a supporting verification artifact, not necessarily a user-facing instructional entrypoint. Such files may still be appropriate in GitHub's test suite; exclusion from production does not automatically imply deleting them.
- `MANUSCRIPT_1TO1`: stays `NOT_PROVEN` for every file until precise block-level mapping evidence is recorded.
- `RIGHTS`: `UNVERIFIED` throughout; Apache 2.0 applies only to material for which rights permit it.

## Chapter-level status

| Chapter | Total Python files | Instructional candidates | Tests/internal QA | Scoped evidence |
|---|---:|---:|---:|---|
| chapter01 | 15 | 15 | 0 | Not yet reviewed |
| chapter02 | 2 | 1 | 1 | Not yet reviewed |
| chapter03 | 2 | 1 | 1 | [Review](CH03_WORD_CODE_ALIGNMENT.md) |
| chapter04 | 2 | 1 | 1 | Not yet reviewed |
| chapter05 | 2 | 1 | 1 | [Review](CH05_WORD_CODE_ALIGNMENT.md) |
| chapter06 | 2 | 1 | 1 | Not yet reviewed |
| chapter07 | 2 | 1 | 1 | [Review](CH07_WORD_CODE_ALIGNMENT.md) |
| chapter08 | 2 | 1 | 1 | [Review](CH08_WORD_CODE_ALIGNMENT.md) |
| chapter09 | 5 | 2 | 3 | [Review](CH09_WORD_CODE_ALIGNMENT.md) |
| chapter10 | 13 | 5 | 8 | [Review](G3_CH10_CH12_REPOSITORY_MAPPING.md) |
| chapter11 | 3 | 2 | 1 | [Review](CH11_WORD_CODE_ALIGNMENT.md) |
| chapter12 | 10 | 5 | 5 | [Review](G3_CH10_CH12_REPOSITORY_MAPPING.md) |
| chapter13 | 4 | 2 | 2 | Not yet reviewed |
| chapter14 | 4 | 2 | 2 | Not yet reviewed |
| chapter15 | 4 | 2 | 2 | Not yet reviewed |
| chapter16 | 5 | 2 | 3 | Not yet reviewed |
| chapter17 | 4 | 3 | 1 | Not yet reviewed |

## File-level register

| File | Role | Provenance | Instructional/release decision | Mapping evidence | 1:1 | Rights |
|---|---|---|---|---|---|---|
| `chapters/chapter01/sections/section_1_1_1.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_1_2.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_1_3.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_2_1.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_2_2.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_2_3.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_3_1.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_3_2.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_3_3.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_4_1.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_4_2.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_4_3.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_5_1.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_5_2.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter01/sections/section_1_5_3.py` | SECTION_EXECUTABLE_STUDY | WORD_EXTRACT_REASSEMBLED | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter02/original_package/ch02_examples.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter02/original_package/test_ch02.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter03/original_package/P1_particle_motion.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH03_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter03/original_package/test_P1.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH03_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter04/original_package/b1_dna_analysis.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter04/original_package/test_b1_dna_analysis.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter05/original_package/python_upgrade_ch05/c2_kinetics_pipeline.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH05_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter05/original_package/python_upgrade_ch05/tests/test_c2.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH05_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter06/original_package/p1_particle_trajectory.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter06/original_package/test_p1.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter07/original_package/b1_sequences.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH07_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter07/original_package/test_b1_sequences.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH07_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter08/original_package/Chapter_08/c3_calibration.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH08_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter08/original_package/Chapter_08/test_c3_calibration.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH08_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter09/original_package/c3_calibration.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH09_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter09/original_package/c3_validation.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH09_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter09/original_package/test_c3_pytest.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH09_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter09/original_package/test_c3_validation.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH09_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter09/original_package/test_ch09_additional.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH09_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/ch10_composition_example.py` | ALTERNATIVE_QA_COPY | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/test_ch10_composition_example.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/c3_calibration.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/c3_validation.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/ch10_composition_example.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/ch10_pipeline.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/kinetics.py` | ORIGINAL_PACKAGE_CANDIDATE | ARCHIVED_CHAPTER_REVIEW_COPY | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/test_c3_pytest.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/test_c3_validation.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/test_ch09_additional.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/test_ch10_composition_example.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/test_ch10_pipeline.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/test_kinetics.py` | AUTOMATED_TEST | ARCHIVED_CHAPTER_REVIEW_COPY | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter11/ch11_lab.py` | RECOVERED_EXAMPLE_OR_DEPENDENCY | RECOVERED_V72 | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH11_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter11/kinetics.py` | RECOVERED_EXAMPLE_OR_DEPENDENCY | RECOVERED_V72 | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](CH11_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter11/test_ch11_lab.py` | AUTOMATED_TEST | RECOVERED_V72 | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](CH11_WORD_CODE_ALIGNMENT.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/src/ch12_6_10_verified_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/src/ch12_additional_manuscript_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/src/ch12_canonical_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/src/ch12_indexing_memory_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/src/ch12_remaining_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/tests/test_ch12_6_10.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/tests/test_ch12_additional_manuscript_examples.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/tests/test_ch12_canonical_examples.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/tests/test_ch12_indexing_memory.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter12/tests/test_ch12_remaining_examples.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; [Scoped chapter review](G3_CH10_CH12_REPOSITORY_MAPPING.md) | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter13/src/ch13_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter13/src/ch13_extended.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter13/tests/test_ch13_examples.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter13/tests/test_ch13_extended.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter14/src/ch14_advanced.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter14/src/ch14_examples.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter14/tests/test_ch14_advanced.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter14/tests/test_ch14_examples.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter15/src/ch15_core_concepts.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter15/src/ch15_sensitivity.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter15/tests/test_ch15_core_concepts.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter15/tests/test_ch15_sensitivity.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter16/src/ch16_initial_bug.py` | INTENTIONAL_FAILURE_EDUCATIONAL | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter16/src/ch16_review_workflow.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter16/src/ch16_validated_decay.py` | VERIFIED_REPRESENTATIVE_EXAMPLE | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter16/tests/test_ch16_review_workflow.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter16/tests/test_ch16_validation.py` | AUTOMATED_TEST | WORD_BASED_REPRESENTATIVE_RECONSTRUCTION | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter17/src/oscillator_lab/__init__.py` | PACKAGE_INITIALIZER | RECONSTRUCTED_NOT_ORIGINAL | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter17/src/oscillator_lab/__main__.py` | EXECUTABLE_ENTRYPOINT_RECONSTRUCTED | RECONSTRUCTED_NOT_ORIGINAL | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter17/src/oscillator_lab/core.py` | RECONSTRUCTED_SOURCE | RECONSTRUCTED_NOT_ORIGINAL | RETAIN_AS_CANDIDATE_NOT_FROZEN | Not yet reviewed | NOT_PROVEN | UNVERIFIED |
| `chapters/chapter17/tests/test_core.py` | AUTOMATED_TEST | RECONSTRUCTED_NOT_ORIGINAL | EXCLUDE_FROM_PRODUCTION | TEST_OR_INTERNAL_QA; Not yet reviewed | NOT_PROVEN | UNVERIFIED |

## Next acceptance criteria

1. Assign Word section/paragraph spans and code block types before upgrading a file to DIRECT_SEMANTIC or EXACT_TEXT_MATCH.
2. Preserve legitimate textbook-only snippets and explicitly labeled pseudocode instead of inventing runnable counterparts.
3. Link CI test evidence to correct scope; a chapter entrypoint PASS does not execute every manuscript fragment.
4. Independently clear origin and redistribution rights per included source file, especially archived review copies.
5. Keep GitHub private and G3/G5/G6 NOT FROZEN until evidence gates close.
