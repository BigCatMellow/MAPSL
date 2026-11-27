# Task: Complete the supported operating workflow

- Status: `READY_FOR_REVIEW`
- AGI status: `AGI READY`
- Type: `IMPLEMENTATION`
- Owner: MAPSL framework operator
- Risk: `MEDIUM`
- Parent: [Master roadmap](../roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md#delivery-order)
- Baseline: candidate `2718d67849d57aba3cfead29fba936b545783457`.
- Goal: Connect and verify the actual runtime lifecycle from startup through review,
  and identify the remaining framework integration boundaries.

## Scope and acceptance

Inspect the real CLI, TaskStore, runtime smoke and method routes. Implement
canonical read-only wait inspection, exact-run CLI submission, retryable
preflight for deterministic startup errors, and the connected disposable smoke.
Fix directly observed import and evidence defects. Update the affected
operation documents, capability evidence, tests and inventory hashes.

- An operator can explain dependency, review and approval waits from a single
  canonical snapshot without initializing or changing task state.
- A bad declared context leaves a task eligible. A corrected start and an
  explicit submission carry the same run to independent revision-bound review.
- Disposable smoke verifies routing, context, ownership, review and completion.
  Preserve ordinary CLI behavior and mark fixture-only evidence as such.
- Verify the full suite, source inventory and actual published tree. Obtain
  independent technical review before updating the existing draft.

## Boundaries and recovery

Fixture identities and local workspaces suffice for this slice. Preserve task
policy, supported defaults and optional provider boundaries. Source changes,
live provider execution, new spending, repository settings, protected merges
and cutover remain under their existing authority. If a deeper boundary needs
its own design, record the concrete seam and next proof.

Reproduce failures before selecting changes. Use isolated working copies for
bounded worker assignments. Verify remote candidate head before any update.

## Operating evidence

- A disposable implementation task and a research task each reached
  `DONE` using a fresh process per CLI command. Invalid context left the
  initial task eligible with zero attempts. The corrected start reached
  attempt one. `submit --run-id` and `flow review-start` resolved the same
  run and artifact. The CLI explained the review wait and refused self-review.
- [Connected smoke](../../runtime/smoke.py) exercises handoff and expired-claim
  recovery, context identity, explicit submission and independent review.
  Optional LangGraph smoke verifies that a ready-work recommendation leaves
  canonical task state untouched. All identities and artifacts are local fixtures.
- [Wait checks](../../tests/test_wait_projection.py) prove snapshot consistency
  through a concurrent review claim. [Startup checks](../../tests/test_flow_start.py)
  confirm that manifest binding independently verifies current input.
- The [information classes](../../playbook/INFORMATION_CLASSES.md) now route to
  actual Skill selection and flow commands. [Run Record tests](../../tests/test_run_record.py)
  cover missing and malformed configuration evidence. A fresh-process test
  isolates the former learning import cycle.
- [Atomic startup](atomic-flow-start.md) combines claim, manifest and required
  evidence. The rollback, retry and competing-worker tests cover the local
  path before provider launch.

## Remaining framework integrations

| Boundary | Next implementation and proof |
| --- | --- |
| Validation and recovery | H4/E4/E5/SEC3 own post-edit and review validation and incompatible-resume behavior. Close these at the supported caller, with a passing path and a refusal before the relevant effect. |
| Context and service evidence | 6.11 owns required context and downstream budgets. L6 must bind the configuration of the actual guarded service operation to its run. Startup stops before a service is selected, so unbound runs have missing evidence. |
| Learning promotion | Context Builder reads governed guidance. Prove a supported candidate-to-review-to-promotion path with authenticated authority before exposing a normal operator promotion route. |
| Hosted integration | [Successor merge controls](../../docs/CHECKS_AND_BALANCES.md#successor-merge-controls) govern protected bootstrap and separate cutover. Disposable reviewers establish runtime behavior only. |

Use the [capability checklist](../roadmaps/CAPABILITY_CHECKLIST.md) for
framework evidence and finish tests. Optional services and experiments
retain their documented triggers.
