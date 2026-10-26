# G3 Chapter 10.3 Five Previously Untested Groups

2026-10-26. Word v37 G4 QA; zero-based top-level paragraph positions. Five reviewer-reconstructed examples executed successfully: B04 lambda callback (2316-2322, 0.8); B05 bound FirstOrderModel method (2328-2347, 0.8); B06 second-order derivative callback (2358-2369, 0.8); B08 InitialCondition frozen dataclass (2433-2444, fields 0.0 and 1.0); B10 decay_step (2485-2499, 0.8). All five PASS in the local Python execution harness. B04-B06 are supported by Word context/prose; B08 and B10 use reviewer-added assertions. Shared euler_step and imports are assembled from preceding Word source, not standalone files. No new Python source or Word modification.

Evidence: G3_CH10_10_3_Five_Missing_Cases_20261026.csv and G3_CH10_10_3_Five_Missing_Tests_20261026.py in local QA directory.

This closes the five outstanding §10.3 logical group execution checks identified by the earlier candidate classification; it does not certify all Word content or the complete Chapter 10 G3 gate. Remaining §10.4–10.6 exact code-span inventory, tests, source parity and provenance need separate approval. G3–G6 HOLD.