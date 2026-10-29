# Version policy / 버전 관리 정책

## Version 1.0 — frozen educational code baseline
- Frozen ref: `release/v1.0-20261029`, commit `46e0f95c3a6f14aae1bc85858237e069da088d2a`.
- Scope: code repository as archived on 2026-10-29, with known validation limits documented in `VERSION_1_BASELINE.md`.
- Never rewrite or force-push the V1 branch. If critical defects are found, document them; decide explicitly whether a `v1.0.1` maintenance release is required or whether to carry the fix into V2.

## Version 2 — future improvements
- Active working branch: `develop/v2`, branched from the V1 baseline.
- Changes to examples, additional biology cases, corrections in Word-to-code mapping, test coverage, and packaging should be committed to V2 with a changelog.
- Run CI and review the real Word/Code Companion consistency before V2 release.
- Do not merge V2 into V1 just to keep branches synchronized.

## Public release checklist (not yet complete)
- Verify contents for third-party intellectual property, private data, credentials, and unused archives.
- Repository visibility is currently **private**; switching to public is an owner action in GitHub Settings.
- Create an immutable-style tag such as `v1.0.0` pointing at the frozen V1 commit and publish a GitHub Release, after reviewing the branch and checks.
- Keep the book's Word copyright distinct from Apache-2.0 code licensing.
