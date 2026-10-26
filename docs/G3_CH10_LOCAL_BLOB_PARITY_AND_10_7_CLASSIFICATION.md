# G3 Chapter 10 — Local Copy Byte Parity and §10.7 Candidate Classification

Date 2026-10-26. Original GitHub blobs were read at `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/`; local copies are in `/mnt/data/python_upgrade_qa/ch10_source_run/`. Compared GitHub contents blob SHA with `git hash-object` of the actual on-disk local file (Git blob hash).

| File | GitHub blob SHA (prefix) | Local blob SHA (prefix) | Byte-identical |
|---|---|---|---|
| kinetics.py | 20744240 | 97b06641 | NO |
| ch10_composition_example.py | ac5c5121 | 88226928 | NO |
| ch10_pipeline.py | d71cc743 | 6f8842d1 | NO |
| c3_calibration.py | 3bd000de | 5692a560 | NO |
| c3_validation.py | ecd4c28c | 77827a2d | NO |
| test_kinetics.py | 1650e8e0 | dfa2c4ef | NO |
| test_ch10_composition_example.py | d6a7387a | 5ccf5833 | NO |
| test_ch10_pipeline.py | 01f976e2 | 7e10fe56 | NO |

**Finding:** The prior locally reconstructed 30/30 or 31/31 pytest success is scoped to the transcription and should not be called exact GitHub-source execution. Divergent Git blob SHA shows a difference in file bytes, not whether semantics differ. GitHub Actions run 40255432567, commit 6b1dc4dd, independently completed SUCCESS 18/18 for its exact checked-out revision; this remains the authoritative CI evidence for that revision.

## Word §10.7: all 17 auto-candidates contextually classified

Manual classification of the 17 flagged top-level Word paragraph positions: 3929–3930 is one function definition/body; 3963–3967 is one multi-line Euler setup; 3969–3973 is one multi-line Midpoint setup; 3990 is **Korean explanatory prose erroneously flagged as code**; 4009 is an import; 4012,4016–4017 form parts of one analytic helper definition. Thus 17 flagged lines correspond to **four dependent logical code units**, one import line and one prose false positive, not 17 programs. Euler/Midpoint summary reuses classes defined in prior sections and is not self-contained. Some source lines outside regex candidates can also contribute to each unit.

Evidence file: `G3_CH10_10_7_17_Candidate_Manual_Classification_20261026.csv`. **No new run was performed for this 17-item classification**. Previous §10.7 four reuse checks remain separately scoped.

Next: obtain exact GitHub source bytes rather than manually transcribed copies if new local testing is needed; continue contextual classification of remaining §§10.1–10.3 candidate paragraphs against all neighboring code and prose. No Word or source edits. G3 overall/G4/G5/G6 HOLD.
