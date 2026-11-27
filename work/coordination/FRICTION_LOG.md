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

The integrated review caught conflicting wiki prose about zero-diff rebases. Route the wiki explanation to the tested verifier and canonical review method. The original review-evidence regression covers a rebase with identical content and different ancestry.

## 2026-11-25 — capability progress did not show a path to completion

- opened: 2026-11-25
- class: drift
- signal: Historical status and blanket successor PENDING entries gave the operator no way to distinguish working components, missing integration proof and optional work.
- countermeasure: Record candidate evidence and a finish test or trigger for each ID in the [existing checklist](../roadmaps/CAPABILITY_CHECKLIST.md). Use the [master delivery order](../roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md#delivery-order) for sequencing.
- verified: The [coverage test](../../tests/test_migration_coverage.py) checks original ID retention, unique ownership and the required evidence and next-step fields.
- follow-up: Update the row when proof, a blocker or an activation trigger changes. Use the normal trajectory check to reconcile drift.

## 2026-11-26 — framework components lacked a connected operating check

- opened: 2026-11-26
- class: drift
- signal: Wait reasons and exact submission lineage lacked CLI routes. A bad declared context spent a claim, and aggregate imports masked a learning dependency cycle.
- countermeasure: Connect the canonical waits and submission paths, preflight declared context before claim, and run a connected disposable smoke and a fresh-process learning import.
- verified: See [framework operating evidence](../tasks/framework-operating-workflow.md#operating-evidence).
- follow-up: Complete the [remaining integration boundaries](../tasks/framework-operating-workflow.md#remaining-framework-integrations) at their normal entry points.

## 2026-11-26 — later setup failures retained a claim

- opened: 2026-11-26
- class: drift
- signal: A missing contracted environment spec left a task active with a consumed attempt and an orphaned startup manifest.
- countermeasure: Claim, run binding and contracted evidence now commit together. SQLite fault injection and competing-start regressions exercise the same path used by the operator CLI.
- verified: [Atomic startup evidence](../tasks/atomic-flow-start.md#verification).
- follow-up: Verify incompatible-resume refusal and validation at actual execution and review boundaries.

## 2026-11-26 — corrected outcome could still enter learning guidance

- opened: 2026-11-26
- class: drift
- signal: A project-scoped lesson candidate stayed promotable after the supporting outcome was explicitly superseded. Context Builder projected it as guidance until retirement.
- countermeasure: Reproduced the sequence with normal calls against disposable SQLite and tied the promotion and admission experiment to L5 and 6.30.
- verified: [Comparative research and learning evidence](../research/2026-11-26-work-system-research.md#learn--turn-outcomes-into-scoped-reviewable-guidance).
- follow-up: Freeze both correction timings and the current-source positive controls before testing the existing owners' freshness rules.
