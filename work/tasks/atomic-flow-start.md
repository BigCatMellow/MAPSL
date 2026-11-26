# Task: Make flow startup atomic

- Status: `READY_FOR_REVIEW`
- AGI status: `AGI READY`
- Type: `IMPLEMENTATION`
- Owner: MAPSL framework operator
- Risk: `MEDIUM`
- Parent: [Framework integration](framework-operating-workflow.md#remaining-framework-integrations)
- Baseline: `3b03e6a0e54ad4bb0528e076905785b3c0e93e30`

## Outcome and scope

If eligible local startup fails, the canonical task keeps its previous claim
and attempt history. On success, the new claim, immutable run manifest and
required environment evidence become visible together. Use existing guards
and one SQLite transaction for the three writes. Project-level Skill catalog
registration remains content-addressed and independently durable.

The owner may update the flow, connection-owned state helpers, focused
regressions, related documentation and inventory hashes on the draft.
Other task transitions, policies, protected integration, external launches
and cutover retain their existing authority. The requested R&D report links
current findings to the master roadmap and research evidence.

## Acceptance and continuation

- Missing or invalid environment inputs leave the task unchanged. A corrected
  retry works immediately on the same next attempt. A failing binding or
  evidence write leaves no new manifest, claim or task event.
- A failed replacement preserves the old expired claim. A stale plan or
  claimant cannot publish over a newer task definition or claim. Concurrent
  startups yield at most one committed claim and matching run.
- Ordinary claim, manifest, environment and review callers retain behavior.
  Verify targeted fault cases, the full suite, smoke, CLI and inventory.
- Use independent review and verified remote CI before calling this slice
  complete. Publish to the existing draft under the current ref lease.

## Verification

The baseline reproduction left an `ACTIVE` claim, incremented the attempt
and wrote a run when the required environment spec was missing. With the
change, a corrected retry can start immediately. [Flow tests](../../tests/test_flow_start.py)
exercise missing inputs, binding revalidation, a failed SQLite evidence
insert, expired-claim recovery, competing workers and stale preparation.
With a fresh process per CLI command, a missing environment spec left the
task READY at attempt zero. Restoring the spec produced one claimed attempt,
one run and one environment record. The full local suite ran 1,520 tests
with five skips and zero failures.

Skill catalog entries may be independently registered during preparation.
The atomic guarantee covers the task claim, immutable manifest, contracted
environment evidence and their task events. Provider launch, runtime faults
after successful startup, and hosted release safeguards have separate paths.

Check [draft CI](https://github.com/BigCatMellow/MAPSL/pull/2/checks) and the
[independent review receipt](../reviews/pr-2-review-evidence.md) for the
reviewed scope. See the [R&D status](../research/2026-11-26-rd-status.md)
for research results and remaining framework dependencies.
