# G3 — Chapter 1 Hash Refresh and Chapter 6 Word Extraction Check (2026-10-25)

## Resolved
- Linux workflow run [40181424645](https://github.com/openwithnet/python-upgrade-code-companion/actions/runs/40181424645) completed **SUCCESS** for source commit `29817fd26c3b951757fe363b2a4252608b210475` (Chapter 1 §1.5.3 expected-output removal).
- `docs/SOURCE_ROLE_AND_RELEASE_GATE.csv` updated for `chapters/chapter01/sections/section_1_5_3.py`: SHA-256 `eea5af569532d61367a58c74459e96d331b9571c72fc45fb791233dc7421f7d5` (UTF-8 bytes; Korean text makes byte count differ from JS string length), commit `99e65771de7c50ed75dd3eafceceadfe4e55cead`.
- Latest Word G4 QA Chapter 6 §6.5.2 program is stored in DOCX paragraph indices **898–907**, extraction yields **120 lines**, valid Python syntax and previously demonstrated output exactly equal to Word paragraph 910. Extracted 4,332-character code SHA-256 `9782d3de1d082b31cddc08a2ab444d3ebfd8b47d2634edc73b6ae236487a6308`; local QA copy at `G3_Ch06_Word_Extract_20261025.py` for reviewer use, not authoritative source.

## Still NOT proven
- Byte-for-byte Chapter 6 Word program vs repository `p1_particle_trajectory.py`: source begins with three extra role/provenance/release comment lines, so raw files are not identical; after removing header, no fully audited newline/comment/whitespace-aware diff has yet been filed. Structural and numerical match remains established; precise textual match pending.
- The Linux CI pass belongs to this source commit and does not imply renewed Windows CI PASS. Previously logged Windows CI applies to earlier source snapshots.
- Full 17-chapter G3 corpus classification, G4 Word visual QA, G5 external rights clearance and G6 Freeze remain OPEN. No Word modification in this pass.
