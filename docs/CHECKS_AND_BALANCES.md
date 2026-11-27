# Checks and Balances

The point is trustworthy autonomous work, not a larger approval process.

| Risk | Typical examples | Minimum check |
| --- | --- | --- |
| Low | Ordinary documentation, formatting, isolated mechanical move | Owner checks result. |
| Medium | Multi-file refactor, UI behavior, meaningful configuration | Relevant tests/reproduction plus independent review. |
| High | Operating-contract/authority changes, security, data loss, persistence, payments, release packaging, external side effects | Explicit task, reproduced evidence, independent review, operator-visible completion/release summary. |

Substantive `AGENTS.md` changes are always High risk and require the explicit
contract/authority scope defined in `AGENTS.md`; generic documentation or refactor
scope does not qualify.

## Non-negotiable controls

1. One accountable owner per active task.
2. Observable acceptance criteria before consequential implementation.
3. No self-approval where independent review is required.
4. Preserve enough evidence for another reviewer to verify the claim.
5. Stay inside the approved roadmap/task permission envelope.
6. Escalate to the human only for a true permission-envelope crossing; do not
   turn review/checkpoints into routine human approval gates.

## Review

An independent reviewer reads the task, changed paths, and evidence. Verdict:

- `APPROVED` — acceptance criteria met.
- `CHANGES_REQUESTED` — concrete required issue remains.
- `BLOCKED` — required context/evidence missing.

The verdict routes back to the orchestration operator. It does not pause for the
human merely because review finished.

- `APPROVED` → reconcile, close task when complete, continue roadmap.
- `CHANGES_REQUESTED` → route correction, re-review as required.
- `BLOCKED` → research/recover/reassign; human only if resolving the blocker
  would cross approved authority.

Only concrete safety, correctness, authority, or acceptance-criteria failures
block approval. Use [the review template](../templates/review.md) for medium/high
risk work.

### Applicable review lenses

Use only lenses the task triggers. One independent reviewer may cover several.

- **Functional / acceptance** — requested behavior and criteria.
- **Security / trust boundary** — inputs, identities, permissions, secrets,
  privileged actions.
- **Privacy** — sensitive/personal data collection, exposure, persistence,
  transmission.
- **Destructive / data-loss** — deletion, overwrite, corruption, irreversible
  mutation.
- **Release / acquisition** — real package/artifact/install/deploy path.
- **Authority** — executed actions remain inside inherited permission envelope;
  for operating-contract changes, verify no self-authorization, invariant loss,
  authority drift, or unintended permission expansion.

Prefer tests of executed behavior over source-text matching. Verify the exact
state/revision being approved.

## Preauthorization and high-risk actions

High risk does not automatically mean repeated human approval.

If the approved roadmap explicitly preauthorizes a destructive, external,
security/privacy-sensitive, or other consequential action with a bounded target
or class, limits/impact, and required recovery/verification, the orchestration
operator may execute it after its required checks without asking again.

If the action is not covered by the approved envelope, the human must authorize
that resolved action before execution.

A review can reject an unsafe implementation even when the action itself is
preauthorized. Preauthorization removes redundant permission prompts; it does
not remove verification, review, least privilege, or acceptance criteria.

## Successor merge controls

The migration candidate includes the read-only `test` and `review-evidence`
checks, a post-push alert for main, and the OPCMD workflow. The source
repository's branch settings and standing authorization do not transfer.
At inspection the successor default branch held only the migration entry
and inventory. Its public branch record reported protection off. Review
of the candidate does not install a trusted gate on the default branch.

Before the first integration, the owner must establish an explicitly
authorized bootstrap with a trusted policy revision, required up-to-date
checks, PR-only protection, protected deletion/force-push settings and
independent approval bound to the live head. Verify the actual settings
and test refusal in the successor before relying on them. Keep the
standing record revoked during preparation. The migration does not
authorize a direct main push, an admin override or a trial merge.

The review artifact records the reviewed substantive commit. The standing
gate also requires authenticated GitHub approval from the identified
reviewer on the exact live SHA and the repository HOLD variable to be
exactly OFF. A missing value refuses the merge. See the
[candidate gate](../work/notes/2026-10-20-github-native-opcmd-merge.md).

## High-risk completion summary

`OPERATOR_VISIBLE_RELEASE_CHECK` is visibility, not another state or approval
subsystem.

The compact summary states:

- what changed / became true;
- verification reproduced;
- material residual risk or `none`;
- any action still outside the approved permission envelope; and
- exact artifact/PR/revision when relevant.

The task may become `DONE` after required review/evidence. The orchestration
operator then continues the approved roadmap automatically.

Do not recreate an `APPROVED → RELEASED` lifecycle merely to duplicate canonical
task/review evidence. A substantive deploy/release may be its own task, but if
that task is already inside the approved roadmap it does not require another
human permission step.
