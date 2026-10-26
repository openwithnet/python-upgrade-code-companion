# G3 Chapter 10 — Six Scoped Python Behavior Checks (2026-10-26)

Word source: v37 G4 QA manuscript. Extracted `EulerStep` Word paragraphs 2859–2869, `MidpointStep` 2876–2891, and `RateLaw`, `FirstOrderRate`, `Trajectory`, `simulate_euler` from paragraphs 3178–3306.

Six reconstructed scenarios all passed in Python: Euler step returns 0.8 for initial 1, rate 0.2, time step 1; Midpoint returns 0.82; five-step explicit Euler trajectory matches the recurrence with numerical tolerance; negative concentration step triggers ValueError; boolean `steps=True` triggers TypeError; zero-step simulation preserves initial state.

**Important caveat:** The Word text explicitly omits the full implementation of `nonnegative_finite`, so the execution harness supplied a reviewer-authored minimal helper obeying the stated nonnegative/finite contract. The Euler/Midpoint snippet also used a reviewer-authored minimal Protocol and model scaffold. This is scoped *behavior checking* of Word code fragments, not execution of a fully self-contained verbatim Word program or complete Github file. The original strict float tuple-equality assertion failed due to roundoff; rerun with `math.isclose` tolerance passed. No textbook algorithm defect was found in that case.

Detailed evidence CSV: `G3_CH10_Scoped_6_Execution_20261026.csv`. These six checks do not certify chapter-wide G3 coverage, scientific validity of a given kinetic model or source publication rights. No Word or repository Python source changed. G3/G4/G5/G6 remain HOLD.