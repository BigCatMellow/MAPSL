# Friction log

Append-only. Capture qualifying friction and verify actual countermeasures.
The [source friction log](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/coordination/FRICTION_LOG.md) remains
historical evidence; unresolved source items are in [migration reconciliation](../../migration/reconciliation.md).
Use the existing repair/learning method and `tools/triage_status.py`.

Entry format:

- opened: YYYY-MM-DD
- class: operator-request | recurring-stall | tool-gap | drift | process-gap
- signal: concrete problem
- countermeasure: actual mechanism or none yet
- verified: evidence or UNVERIFIED
- follow-up: next action

## 2026-11-24 — migration connector limits
- opened: 2026-11-24
- class: tool-gap
- signal: local GitHub DNS unavailable; connector batch exceeded call cap and one remote disconnect occurred.
- countermeasure: use pinned source tree, bounded 8–12-file batches, inspect exact blob/mode, verify final tree and atomic non-force ref.
- verified: source-exact runtime/test/tool transfer and migration coverage CI succeeded at ec719f7.
- follow-up: retain local state/independent review limitations; no unsupported completion.

## 2026-11-24 — oversized entry and missing source routes
- opened: 2026-11-24
- class: drift
- signal: original suite found 12 navigation/authority workflow failures at ec719f7; runtime smoke and static checks passed.
- countermeasure: separate migration plan from brief root router; restore purposeful owner routes and gated candidate workflows, preserve original tests.
- verified: UNVERIFIED until next integrated CI.
- follow-up: inspect exact new CI; no merge until review and governance ready.

## 2026-11-25 — incomplete historical routes and evidence

- opened: 2026-11-25
- class: tool-gap
- signal: Source #331 recorded indexed-search false negatives and truncated large-file replacements. Disconnected workers interrupted a grouped migration audit. The initial candidate also described inherited branch protection and installation routes as active.
- countermeasure: recover from isolated on-disk clones, use direct owner files and pinned Git trees, verify complete ledger changes atomically. Check terminal adapted hashes, modes and exact original pointers in CI. Restore source review and direct-push checks. Inspect live successor settings and run the installer in a clean Linux clone.
- verified: grouped source records and witnesses are linked from migration/reconciliation.md. Disposable install, continuation and denial evidence is in migration/operation-evidence.md. Source #331 remains under its original owner.
- follow-up: corroborate any missing local originals or obtain explicit exclusion. Verify default-branch governance before activation.
