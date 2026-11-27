# First Run

Use this route when joining the repository. Orientation should end as soon as you
can name the owner, allowed scope, next action, verification, and escalation
boundary.

## Minimum route

1. Read [`AGENTS.md`](../AGENTS.md), the **single repository-wide operating contract**.
2. Read the approved roadmap/project scope and active task. The [migration plan](../migration/PLAN.md) defines the current project scope. If authorized roadmap
   work exists but no child task does, the orchestration operator shapes/selects
   the next in-scope task and continues.
3. Select **one** relevant method from the [playbook index](../playbook/INDEX.md).
   Read a second only when a distinct concern actually requires it.
4. Confirm owner, outputs/actions, acceptance criteria, verification/review, and
   the true authority boundary. Shape missing detail inside inherited authority;
   escalate only a real boundary crossing.

Common-case reading budget:

```text
AGENTS.md + approved roadmap/task + one relevant playbook method
```

## Route by need

Do not browse directories to discover these paths:

| Need | Route |
| --- | --- |
| Role-bound browser session / PR coordination | [`work/coordination/README.md`](../work/coordination/README.md) → live GitHub |
| Resume prior cross-session work | [`state/CURRENT.md`](../state/CURRENT.md) → linked evidence and live GitHub |
| Find a `work/` record class | [`work/README.md`](../work/README.md) |
| Capability/roadmap question | [`work/roadmaps/README.md`](../work/roadmaps/README.md) before opening a large roadmap/checklist |
| Legacy/reference research | [`migration/README.md`](../migration/README.md) for pinned source evidence |
| Runtime/control-plane concern | [`playbook/CONTROL_PLANE.md`](../playbook/CONTROL_PLANE.md) |
| Inspect why a runtime task is waiting | [Task status and waits](../runtime/README.md#status-surface-v1) |
| Fresh runtime installation | [`docs/FRESH_INSTALL.md`](FRESH_INSTALL.md) |
| Verification/review level | [`docs/CHECKS_AND_BALANCES.md`](CHECKS_AND_BALANCES.md) |

For a single-owner task, follow the method directly. For bounded parallel work,
use [Helpers and Communication](../playbook/HELPERS_AND_COMMUNICATION.md) and
give each writer an isolated checkout. Install the runtime when the work needs
durable claims, evidence, review or recovery. HCOM is optional in ordinary use.

Do not read the whole wiki, `work/`, roadmap corpus, or playbook as a prerequisite
ritual. If routine work requires stitching several overlapping documents together,
treat that as a routing/consolidation problem.
