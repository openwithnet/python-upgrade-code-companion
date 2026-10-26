# G3 — Chapter 10.3 Six Word-Reconstructed Behavior Cases

Date: 2026-10-26. From Word v37 G4 QA, zero-based `Document.paragraphs` anchors. The following cases were executed in Python in an independent reconstructed harness:

| Word paragraphs | Case | Result |
|---|---|---|
| 2193–2223 | single function decay | `[1,0.8,0.64,0.512]` |
| 2252–2266 | first-order signed derivative | `-0.6000000000000001` (numerically -0.6) |
| 2277–2310 | Euler callback injection | `0.8` |
| 2379–2413 | Euler and Midpoint reuse one model | `(0.8,0.82)` |
| 2456–2471 | Trajectory length contract | expected `ValueError` |
| 2533–2565 | composed simulation | `(1,0.8,0.64,0.512)` |

**All 6 passed** the selected behavioral checks. Multiline indentation and shared definitions were reconstructed; these are not six byte-for-byte original independent Word scripts. The signed derivative API is distinct from the positive consumption-rate `kinetics.py` API. This run did not verify all scientific constraints or the entire subsection corpus. CSV `G3_CH10_10_3_Six_Cases_20261026.csv` and harness `verify_ch10_3.py` are the working evidence. No Word or GitHub source changes; G3/G4/G5/G6 remain HOLD.