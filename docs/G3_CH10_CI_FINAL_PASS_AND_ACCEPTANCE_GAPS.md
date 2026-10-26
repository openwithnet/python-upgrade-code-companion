# G3 Chapter 10 — Final CI Status and Remaining Acceptance Work

Date: 2026-10-26.

## CI status, now finalized

GitHub Actions run **40255432567** for commit `6b1dc4dd0e00007b54e5dc9b3c75ebf3bb3b2414` reports `completed/success` at 2026-10-26 01:44:05 UTC. All **18/18** jobs completed successfully: 17 chapter-isolated Python 3.11 jobs and repository structure / Python 3.11 preflight. Specifically Chapter 10 / Python 3.11 = SUCCESS. This supersedes the earlier pending-workflow status document.

Run URL: https://github.com/openwithnet/python-upgrade-code-companion/actions/runs/40255432567

## Chapter 10 remaining G3 acceptance work

1. **Word manuscript coverage denominator**: classify all actual program/test blocks, diagrams, outputs, snippets and non-runnable pseudocode in §§10.1–10.7. The 314 automatically flagged paragraphs in §§10.1–10.3/10.7 are not the number of distinct programs.
2. **Full Word-to-source trace**: for each executable unit record start/end Word paragraph, imports/dependencies, exact expected results, GitHub function/file/test and execution evidence. Do not count recap reuses as new independent programs.
3. **Source-byte verification**: the earlier 30/30 reconstructed pytest run used a manually transcribed local copy. To call it a verified GitHub checkout, first obtain byte-identical source or document a hash-based comparison.
4. **§10.6 mismatch**: Word §10.6 is about design versus over-abstraction, not specifically the C3 calibration `ch10_pipeline.py`; label this related archived candidate rather than a direct match until evidenced.
5. **Test scope**: Word §10.4.4 `ConstantDerivative` regression was added as `test_euler_constant_derivative_isolated` to `test_ch10_composition_example.py`; its GitHub CI is now covered by completed 18-job PASS.
6. **G2 Windows scope**: prior Windows/Conda pass is for an earlier source revision, not established for this new commit. G3 manuscript-wide code parity, G4 Word visual/equation QA, G5 rights provenance and G6 freeze remain incomplete.

No Python source or Word edits in this status document; G3/G4/G5/G6 HOLD.
