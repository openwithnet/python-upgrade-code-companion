# Chapter 11 — Word/Code Scoped Alignment (2026-10-25)

**Decision:** Sections 11.5–11.6 representative strategy/observer lab conceptually and numerically aligned with recovered v72 source. Whole chapter and historical original-text 1:1 fidelity remain NOT PROVEN.

## Evidence table

| Word section | GitHub implementation | Finding |
|---|---|---|
| 11.5.1–11.5.3 observer semantics | `StepEvent`, `EventObserver`, `Recorder`, `simulate(...,observer)` | event per initial + every completed step; exceptions propagate |
| 11.6.1 shared canonical kinetics | `kinetics.py` `FirstOrderRate`, `simulate_euler` | c0=1 mol/L, k=.2/s, dt=1s, 5 steps |
| 11.6.1 replaceable strategy | `StepStrategy`, `EulerStep`, `MidpointStep`, `make_solver` | Euler c'=c−dt·kc, midpoint c_mid=c−dt·kc/2 then c'=c−dt·k c_mid |
| 11.6.2 event recording | `Recorder`, `StepEvent` | 5 steps yield 6 events, including step 0 |
| 11.6.3 design cost/tradeoff | `test_ch11_lab.py` | canonical Euler agreement, midpoint precision, invalid steps, bad solver, exception propagation |

## Numerical reference

- Euler factor for dt=1 and k=.2: .8, final `0.8**5 = 0.327680`.
- Explicit midpoint factor: `1-.2+.5*.2**2 = .82`, final `0.82**5 = 0.3707398432`.
- Exact c(5)=exp(-1)=0.367879441171...; midpoint error ≈0.0028604 vs Euler error ≈0.0401994.
- `Recorder` receives 6 events. `make_solver('bogus')` raises ValueError.

## Important distinctions

- The standalone Word §11.5.2 teaching sketch features an `EventSource` with subscription/unsubscription; the recovered runnable `ch11_lab.py` uses one optional callback `observer`. These are **different instructional abstractions**, not identical source blocks. Do not imply a byte-for-byte match.
- `kinetics.py` is a recovered v72 Chapter 10.5 canonical dependency used by Chapter 11; keep module boundary explicit rather than replacing with Chapter 5 kinetics (whose units are mmol/L/min, not mol/L/s).
- Word §11.6.3 says 13 historic automated tests passed, while current `test_ch11_lab.py` includes parametrized pytest cases. Current Linux and Windows CI cover chapter entrypoint but do not prove Python 3.14 support or all Word code snippets. Distinguish counts.
- The `RECOVERED_V72` source provenance is not proof of historical complete original manuscript identity. Third-party rights and publication permission have not been affirmatively cleared.

**Gate:** Scoped representative lab aligned. Full G3/G4/G5/G6 remain HOLD. Source code and Word manuscript unchanged by this audit.
