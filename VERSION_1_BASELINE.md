# Python Upgrade for Scientists — Version 1.0 baseline (2026-10-29)

This branch snapshots the existing Chapter 1–17 Code Companion at the user's V1 educational manuscript freeze.

## Scope and limitations
- Source: existing `main` branch of `openwithnet/python-upgrade-code-companion` at creation of this release branch.
- Existing examples, tests, workflows, and Apache-2.0 LICENSE are retained without rewriting.
- This is a **V1 code baseline**, not a claim that every embedded Word example is executable or tested individually.
- Chapter 12's later approved educational extension is included in the Word manuscript; additional RC3 exercises may require a separate code alignment update and must not be misrepresented as already committed here.
- The Word manuscript is distributed separately, not under the code license.
- Known gaps (Word/code one-to-one checks; 479 earlier non-parsing style blocks; 123 prioritized fragments; visual and mathematical QA) move to the V2 improvement backlog. A passing CI run does not automatically close those gaps.

## Usage
Read the repository README and use chapter-specific instructions/tests. Verify the Actions status for this branch before relying on a given environment. Preserve this branch as a reproducible snapshot, and make V2 changes on separate branches.
