# MAPSL master roadmap

**Migration candidate.** The [authorized migration plan](../../migration/PLAN.md) owns M0–M6. This roadmap owns improvement priorities and dependencies. The [capability checklist](CAPABILITY_CHECKLIST.md) holds current evidence, the next action and the finish test for every capability.

## Permanent objective

A capable AI worker completes real work inside human-defined boundaries with minimal unnecessary intervention. MAPSL provides the operating method and, when needed, coordination and deterministic control-plane machinery. Success is not more agents, protocols, tokens, files, or checklist closures.

Evaluate each change by autonomy, reliability, reasoning/planning quality, continuity, efficiency, adaptability, controlled learning, usability and safety. The owner reports that the old system works in practice; relative performance against ordinary agent-assisted work is unknown. Preserve what works; do not make another external pilot the central objective of the project.

## Delivery order

1. **Finish migration preparation.** Verify the integrated candidate, its
   evidence and the source delta under the [migration plan](../../migration/PLAN.md).
   [Current state](../../state/CURRENT.md) owns the next action. Integration
   requires [authorized bootstrap and review controls](../../docs/CHECKS_AND_BALANCES.md#successor-merge-controls).
   Cutover requires the owner's decision.
2. **Resume and finish ordinary work.** After cutover, use one coding task and
   one non-coding task with the native [THINK and PLAN methods](../../playbook/INDEX.md#native-think-and-plan-routes)
   as applicable. A fresh session can
   recover the goal, authority, owner, next action, confirmed wait or blocker
   and review evidence, then reach the agreed outcome. Use the normal routes
   and the existing task store when runtime is needed. Start with 6.1, 6.7,
   6.21 and 6.18. This is the continuity proof for #247.
3. **Prove safe execution and recovery.** Exercise one normal runtime path
   with explicit task and environment binding, isolated writable work, a
   supported harness lifecycle and recovery. Verify actual guard and
   validation boundaries, outcomes when they deny, and trace through review.
   Resolve H4/6.4/6.5 with E4 and SEC3, E5 with E2/E3, and 6.24 with SEC4 and
   recorded environment evidence. A safe refusal and an authorized completion
   are both required proof.
4. **Deliver the right context.** Use the same code/non-code cases to show
   normal startup preserves required inputs and authority. Make progress on
   6.11 and #248 against a measured baseline. S4/S6/6.9 share explicit-first
   routing proof; SEC4/6.10 and SEC5/6.22 prove which Skills and lessons can
   reach the worker. Use frozen retrieval evidence before considering 6.33.
5. **Learn from evidence tied to real runs.** Connect one run to its outcome,
   a reproducible case and an authorized guidance decision. Show the recorded
   effective configuration survives into the exported Run Record (L6)
   before relying on comparisons (L7). Keep new refinement proposals behind
   reviewed evidence and authority.
6. **Make the proven workflow portable.** Keep supported installation and
   project-local setup working throughout. Reconcile D0/D2b/D2c, then prove
   that a fresh user can set up and inspect an isolated target with the
   documented method. External lifecycle proof (D3/6.35) depends on a useful
   task and separate target authorization. Additional stacks, CI and fleet
   features advance only on their triggers.

Keep safety, evidence integrity and existing supported operation in force
throughout. A defect blocking an earlier outcome or violating a safety
boundary takes priority. Run shared checks once for overlapping IDs and
retain the distinct exit test for each broader capability.

## Outcome-driven priorities after migration

| Program | Outcome | Next useful work and proof |
| --- | --- | --- |
| Direction and continuity | Never lose parent intent, unfinished work or the next action between sessions | Reconcile actual obligations and improve existing trajectory/steering/handoff checks; demonstrate a fresh session recovers intent, scope, owner, next action and blocker without reconstructing chat. Fix repeated missing dispositions mechanically. |
| Reasoning and context | Better judgments with the minimum trustworthy information | Preserve native THINK/PLAN, request compilation and explicit-first Skill routing; investigate observed context omissions/ambiguity; compare source-linked compaction and routing only against frozen cases. No duplicate memory store by default. |
| Execution and reliability | Work proceeds and recovers without supervision or unsafe fallback | Verify actual production enforcement for H4, E5, E6 and the opt-in hook/recovery paths. Preserve provider-neutral adapters, isolate concurrent writes; make inactive infrastructure optional where evidence supports it. |
| Safety and evidence | Human authority, independent review and reliable provenance survive every path | Reconcile SEC3/SEC4, effective least privilege, review-head binding and GitHub-native governance; prove denials, stale evidence refusal and no unsafe fallback. Preserve prior frozen cases. |
| Learning and evaluation | Repeated mistakes cause measurable, reviewed improvements | Verify L6 real-run config identity before comparisons; retain evaluation and operational learning; test failure localization, lean-vs-helper routing, and narrow candidates through JUDGE/LEARN before considering GROW. |
| Usability and portability | Easy to install, use and maintain across appropriate contexts | Verify #378 target preflight and init, documentation and method-only operation; external task or comparative test only when useful and separately authorized. |

## Recovered requirements and dependencies

Use these conditions when the owning program becomes eligible. The detailed evidence lives in the [branch audit](../../migration/branch-evidence.md#forward-requirements-recovered-from-divergent-branches), [work audit](../../migration/work-evidence.md#open-obligations-and-historical-proofs) and [historical audit](../../migration/history-evidence.md).

- Direction and continuity owns fresh-session recovery. Apply the continuity proof above before closing #247. Treat any live roadmap sheet as a projection of the checklist. The September PLAN handoff has an [approved historical disposition](../../migration/reconciliation.md#historical-evidence-decision).
- Execution and safety own consequential-call validation, isolation, lease recovery, ambiguous external effects, and reviewer identity. Preserve refusal for an uncertain prior side effect. Verify an eligible trusted producer before promoting reviewer-execution attestation.
- Reasoning and learning own the failed retrieval experiments, production configuration identity and bounded uptake of lessons. The source shipped TASK-223 despite the incomplete promotion record. Check that scoped lessons reach the actual startup path. Reconsider retrieval only on frozen hard negatives, exact anchors, acceptable alternatives and blind scoring.
- Portability owns preview, initialization and repeat-safe upgrades. The [Linux operation evidence](../../migration/operation-evidence.md) covers a disposable target. External piloting, fleet automation, and publication each require their own trigger and authority.

## Full-system acceptance dimensions

Preserve the original [ten program definitions of DONE](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md#15-program-definitions-of-done) and [six end-state scenarios](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md#16-end-state-scenarios). The recovered [Harada candidate](https://github.com/BigCatMellow/MAPS_Lean/tree/f5f2e21bb0cfa5872d86baaafc1f8c89378e0a7c/work/roadmaps/harada-full-map) reinforces full-system acceptance, not another competing planning tree.

| Dimension | Observable proof |
| --- | --- |
| Control | Provider-neutral start/inspect/communicate/recover/stop for supported workers without authority expansion. |
| Context | Minimal trustworthy, progressively loaded procedures and evidence with explicit authority. |
| Reproducibility | Environment/context/revision lineage sufficient to explain differences and decide recovery compatibility. |
| Safety | Actual consequential call paths enforce deterministic least-privilege checks; untrusted content cannot ratify policy. |
| Coordination | Parallel/helper ownership, isolation and continuity remain correlated. |
| Evidence | Task/run/session/helper/recovery/submission/exact review/outcome reconstructable. |
| Review integrity | Approval bound to actual artifact/revision/evidence. |
| Learning | Real failure becomes a frozen case and reviewed candidate comparison. |
| Human authority | No self-authorization of consequential policy, safety or scope. |
| Complexity control | Method-only default; orchestration and infrastructure earn their cost through observed needs. |

Representative proofs: ordinary coding, prompt injection denial, interrupted worker, concurrent writable workers, imported Skill quarantine/activation, repeated real-world failure. Exercise relevant scenarios at risk-appropriate scope; a successful isolated component or one happy-path pilot cannot establish all ten properties. No mandatory paid/benchmark/external runs are implied.

## Complete capability ownership

Each capability has one accountable program. The groups below link directly to
the same checklist that carries their evidence and finish tests.

- [Direction and continuity](CAPABILITY_CHECKLIST.md#direction-and-continuity)
- [Reasoning and context](CAPABILITY_CHECKLIST.md#reasoning-and-context)
- [Execution and reliability](CAPABILITY_CHECKLIST.md#execution-and-reliability)
- [Safety and evidence](CAPABILITY_CHECKLIST.md#safety-and-evidence)
- [Learning and evaluation](CAPABILITY_CHECKLIST.md#learning-and-evaluation)
- [Usability and portability](CAPABILITY_CHECKLIST.md#usability-and-portability)

## Conditional work

The checklist records each conditional trigger and the proof needed to proceed.
Review eligibility when its evidence changes or a meaningful work arc ends.
Prime and other provider studies remain research inputs. Promote a bounded
adapter trial only for a demonstrated integration gap under the applicable authority.

- [Work-system research](../research/2026-11-26-work-system-research.md#research-conclusions-and-development-routes) maps the external comparisons and measured gaps to the existing execution, evidence, context and learning owners.
- #341 benchmark: the generic control text passed its exact-text Gate 1 review. Full revision-3 package review, selection and corpus custody gates, and explicit execution authority remain. [R&D status](../research/2026-11-26-rd-status.md#research)
- [#247](https://github.com/BigCatMellow/MAPS_Lean/issues/247) memory and [#248](https://github.com/BigCatMellow/MAPS_Lean/issues/248) context compilation: reasoning/continuity, compare existing mechanisms first. [#331](https://github.com/BigCatMellow/MAPS_Lean/issues/331) tool friction: reliability, reproduce and repair proportionally.

## Source design and evidence

The detailed designs remain accessible at the pinned source; retain or import
specific implementation-relevant sections after review rather than maintaining
parallel design queues. Their old implementation waves are historical, not current scheduling.

- [00-MASTER-MAPS-CAPABILITY-ROADMAP.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md)
- [prime-agent-capability-roadmap.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/prime-agent-capability-roadmap.md)
- [operator-intent-compiler.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/operator-intent-compiler.md)
- [github-async-work-pull.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/github-async-work-pull.md)
- [agent-harness-capabilities/01-harness-mechanics.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/01-harness-mechanics.md)
- [agent-harness-capabilities/02-procedural-knowledge-and-skills.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/02-procedural-knowledge-and-skills.md)
- [agent-harness-capabilities/03-environment-and-reproducibility.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/03-environment-and-reproducibility.md)
- [agent-harness-capabilities/04-agentic-security.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/04-agentic-security.md)
- [agent-harness-capabilities/05-learning-and-evaluation.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/05-learning-and-evaluation.md)
- [agent-harness-capabilities/06-portable-deployment.md](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/06-portable-deployment.md)
- [Research router](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/research/README.md), [October goal remap](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/research/evaluation-and-reliability/2026-10-20-think-plan-maps-goal-remap.md), [future ideas](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/FUTURE_IDEAS_BACKLOG.md), [promotion ledger](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/LEGACY_PROMOTION_LEDGER.md).

Unfinished research, handoffs, friction, old review queues and historical task
obligations must be reconciled during migration; see the temporary
[reconciliation evidence](../../migration/reconciliation.md). Do not turn
history into a live task queue merely by citing it.

## Maintenance

Use the existing trajectory check at meaningful arcs: update this roadmap when
priorities change; update the evidence checklist when proof changes; update
the current-state pointer when the next action or blocker changes. Reconcile
new tasks, issues, research, decisions and discoveries into an existing owner
or explicit disposition with a trigger. A source not checked is UNKNOWN, not
clean. Use deterministic checks for repeated omission, not more permanent
planning documents.
