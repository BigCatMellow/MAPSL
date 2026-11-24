# MAPSL master roadmap

**Migration candidate — not accepted on main.** The [authorized migration plan](../../migration/PLAN.md) owns the current M0–M6 sequence. This document owns long-term outcome priorities, capability relationships and conditional triggers; [capability evidence](CAPABILITY_CHECKLIST.md) owns implementation/verification status. No second development queue.

## Permanent objective

A capable AI worker completes real work inside human-defined boundaries with minimal unnecessary intervention. MAPSL provides the operating method and, when needed, coordination and deterministic control-plane machinery. Success is not more agents, protocols, tokens, files, or checklist closures.

Evaluate each change by autonomy, reliability, reasoning/planning quality, continuity, efficiency, adaptability, controlled learning, usability and safety. The owner reports that the old system works in practice; relative performance against ordinary agent-assisted work is unknown. Preserve what works; do not make another external pilot the central objective of the project.

## Outcome-driven priorities after migration

| Program | Outcome | Next useful work and proof |
| --- | --- | --- |
| Direction and continuity | Never lose parent intent, unfinished work or the next action between sessions | Reconcile actual obligations and improve existing trajectory/steering/handoff checks; demonstrate a fresh session recovers intent, scope, owner, next action and blocker without reconstructing chat. Fix repeated missing dispositions mechanically. |
| Reasoning and context | Better judgments with the minimum trustworthy information | Preserve native THINK/PLAN, request compilation and explicit-first Skill routing; investigate observed context omissions/ambiguity; compare source-linked compaction and routing only against frozen cases. No duplicate memory store by default. |
| Execution and reliability | Work proceeds and recovers without supervision or unsafe fallback | Verify actual production enforcement for H4, E5, E6 and the opt-in hook/recovery paths. Preserve provider-neutral adapters, isolate concurrent writes; make inactive infrastructure optional where evidence supports it. |
| Safety and evidence | Human authority, independent review and reliable provenance survive every path | Reconcile SEC3/SEC4, effective least privilege, review-head binding and GitHub-native governance; prove denials, stale evidence refusal and no unsafe fallback. Preserve prior frozen cases. |
| Learning and evaluation | Repeated mistakes cause measurable, reviewed improvements | Verify L6 real-run config identity before comparisons; retain evaluation and operational learning; test failure localization, lean-vs-helper routing, and narrow candidates through JUDGE/LEARN before considering GROW. |
| Usability and portability | Easy to install, use and maintain across appropriate contexts | Verify #378 target preflight and init, documentation and method-only operation; external task or comparative test only when useful and separately authorized. |

Direction and continuity are the immediate cross-program priority during migration. Safety/reliability are mandatory constraints, not optional later phases. Prioritize actual unresolved problems and dependency gates over historical feature order. Continue only until the relevant outcome is met.

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

Every ID from the source checklist has exactly one primary objective program;
cross-cutting dependencies remain in the source designs and evidence. This is
coverage, not an instruction to implement every feature.

- **Direction and continuity:** 6.1, 6.7, 6.19, 6.20, 6.21, 6.34
- **Reasoning and context:** S1, S2, S3, S4, S5, S6, S7, 6.8, 6.9, 6.10, 6.11, 6.12, 6.33
- **Execution and reliability:** H1, H2, H3, H4, H5, H6, E1, E2, E3, E4, E5, E6, E7, 6.2, 6.3, 6.4, 6.5, 6.6, 6.13, 6.14, 6.15, 6.16, 6.17
- **Safety and evidence:** SEC1, SEC2, SEC3, SEC4, SEC5, SEC6, SEC7, 6.18, 6.22, 6.23, 6.24, 6.25, 6.26
- **Learning and evaluation:** L1, L2, L3, L4, L5, L6, L7, L8, L9, 6.27, 6.28, 6.29, 6.30, 6.31, 6.32
- **Usability and portability:** D0, D1, D2a, D2b, D2c, D3, D4, D5, D6, 6.35

## Conditional work

- S7/6.12 capability packs: repeated packaging need; E7/6.17 snapshots: actual reconstruction failures; SEC6/6.25 credential broker: real secret boundary; 6.19/6.20: measured helper continuity/stall need.
- L7 comparative evaluation: comparable configuration/outcome evidence; L8/6.31 proposal-only refinement: measured need and reviewed candidates, never self-authorizing. L9/6.32 time travel: demonstrable debugging benefit.
- D3 external pilot: meaningful task and target authority, not a mandatory repeat demonstration; D4/D5/D6: actual second stack, CI or fleet need.
- 6.33 semantic retrieval: frozen evaluation evidence and security gate; 6.34 mission object: demonstrated multi-task need without duplicate task authority.
- #341 benchmark: remain parked pending Gate 1/4/5 and explicit execution authority; [source PR](https://github.com/BigCatMellow/MAPS_Lean/pull/341).
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
