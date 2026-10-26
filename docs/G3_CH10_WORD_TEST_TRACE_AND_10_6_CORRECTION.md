# G3 Chapter 10 — Word-to-Test Traceability and §10.6 Mapping Correction (2026-10-26)

## Material correction to preceding audit
**The current Word v37 §10.6 is titled `10.6 좋은 설계와 지나친 추상화` (zero-based paragraph 3454). It is NOT a C3 calibration-pipeline implementation section.** Subsections are 10.6.1 p3469, 10.6.2 p3534, 10.6.3 p3670 and 10.6.4 p3769. Its references to `Simulation`/`FirstOrderModel` include p3646 and p3963–3974. Accordingly, the earlier claim that `ch10_pipeline.py` directly implements Word §10.6 is **NOT VERIFIED / misleading**. That GitHub module is a valid archived C3 measurement/calibration workflow, but direct Chapter10 Word provenance requires separate evidence. Do not count its tests as exact Word §10.6 acceptance.

## Direct Word anchors and tests

| Word anchor (0-based paragraphs) | GitHub file / test | Alignment | Caveat |
|---|---|---|---|
| §10.4.3 p2851; `EulerStep.step` p2859–2869 | `ch10_composition_example.py` / `test_euler` | DIRECT_SEMANTIC | one-step numerical algorithm only |
| §10.4.3 `MidpointStep.step` p2876–2891; simulation injection p2895+ | same / `test_midpoint`, `test_solver_injection` | DIRECT_SEMANTIC | solver injection test uses reviewer-defined `RecordingSolver` |
| §10.5 `RateLaw` p3181–3188, `FirstOrderRate` p3198–3224 | `kinetics.py` / `test_rate`, `test_bad_coeff`, `test_bad_bool` | DIRECT_SEMANTIC | Word omits complete definition of reusable validation helper |
| §10.5 `Trajectory` p3234–3237, `simulate_euler` p3243–3303 | `kinetics.py` / `test_initial`, `test_euler`, `test_zero_rate`, `test_step_too_large`, `test_bad_step_count` | DIRECT_SEMANTIC | tests add edge cases beyond printed Word examples |
| §10.5 analytic helper p3329–3331 and surrounding | `kinetics.py` / `test_exact`, `test_step_refinement` | DIRECT_SEMANTIC | accuracy checks depend on model/time-step |
| §10.6 critical design discussion p3454–3882 | `ch10_pipeline.py` / `test_ch10_pipeline.py` | **NO_DIRECT_WORD_SECTION_MATCH** | C3 calibration orchestration distinct from Word's 10.6 structural-design discussion |

## Uncovered tests and additional risk paths
- `ch10_composition_example.py` tests cover positive nominal examples and injection; **no explicit negative-dt, NaN state, invalid solver, or invalid derivative tests**. The educational minimal class does not promise kinetics' validations.
- `kinetics.py` tests cover negative/NaN/Inf/bool k and large dt; explicit **nonfinite c0, NaN dt, negative dt, negative steps, nonfinite model.rate, overflow** cases were not identified in inspected test file; these are tests-to-add candidates, not confirmed implementation defects.
- `ch10_pipeline.py` has broad structural contract tests, but they validate an **archived C3 demonstration** and not the Word §10.6 heading. Any reuse in this chapter needs a documented rationale and source trace.
- Existing tests' presence is not proof they passed on the current commit; no new test suite execution was performed in this audit.

## Gate and action
Prior Chapter 10 three-module contract review should be read with this §10.6 correction. Word and source are not changed. Proposed editorial resolution: relabel `ch10_pipeline.py` as **RELATED_C3_ARCHIVED_EXAMPLE**, not `DIRECT_WORD_10_6`, pending explicit editorial decision. G3/G4/G5/G6 remain HOLD.
