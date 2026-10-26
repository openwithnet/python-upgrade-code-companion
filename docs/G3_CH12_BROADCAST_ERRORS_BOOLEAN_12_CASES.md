# G3 Chapter 12: Broadcasting and Boolean Indexing Audit

Date: 2026-10-26. Word G4 QA source.

Twelve targeted checks completed in Python. Ten examples printed the expected Word output; two intentionally invalid Broadcasting combinations raised ValueError as anticipated.

- Invalid shape checks: (3,4) versus (3,) in np.broadcast_shapes and multiplication.
- Valid cases: paired exponential model, two 3-D scaling variants, Cartesian grid.
- Boolean masking: selection, interval, OR, finite/nonnegative and 2-D row filtering.

The earlier 37 successful checks and ten new successful checks total 47; 45 have explicit matching Word output. With two expected-error checks this is 49 scoped cases, not the total example count in Chapter 12.

Evidence: G3_Ch12_Broadcast_Errors_Boolean_12_Examples_20261026.csv in QA workspace. No Word or Python source changed; G3/G4/G5/G6 remain HOLD.