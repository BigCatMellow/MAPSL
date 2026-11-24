# Migration reconciliation evidence

**In progress — not acceptance or a second roadmap.** 2026-11-24.
Parent: [authorized migration](PLAN.md); current direction:
[master roadmap](../work/roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md).
The source stays read-only. This record tracks remaining M0/M1 evidence;
the file-level ledger is [source inventory](source-inventory.tsv).

## Verified baseline

- Pinned source main 605ce610e0be3334d1da7af2a7c6f5912b6cc05f; exact inventory 3,515 files, 31 executable, no symlink or submodule entries in the returned tree.
- Source runtime CI [success](https://github.com/BigCatMellow/MAPS_Lean/actions/runs/45405604013). No successor runtime parity assertion.
- All 35 master capability IDs and 45 subsystem milestone IDs recovered from the source checklist and mapped to objective programs. Source DONE is not successor DONE.
- 51 original foundation files staged by exact Git blob and mode, including 25 playbooks and 18 templates; the roadmap router has since been deliberately replaced with a concise route. No fresh independent review. Secret-pattern screening of transferred text is limited, not a comprehensive security audit.
- The successor retains existing work/roadmaps paths, rather than renaming to roadmap/, to avoid breaking tooling and references without benefit. Original detailed designs remain reachable through pinned source links. Consolidation is a candidate until reviewed.
- Source checkout unavailable: container DNS cannot resolve github.com. Connected GitHub reads/writes work. Local runtime execution and external machine paths are not available. CI can verify repository-only checks when configured.

## Previously hidden or competing planning sources

| Source | Current migration disposition (not acceptance) |
| --- | --- |
| [Original master](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md), [checklist](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/CAPABILITY_CHECKLIST.md), six detailed roadmaps, [Prime](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/prime-agent-capability-roadmap.md), [intent compiler](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/operator-intent-compiler.md), [async pull](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/github-async-work-pull.md) | 80 IDs crosswalked to one objective roadmap; preserve source proof and design, review remaining design-level obligations before disposition. |
| [Full recursive Harada roadmap branch](https://github.com/BigCatMellow/MAPS_Lean/tree/f5f2e21bb0cfa5872d86baaafc1f8c89378e0a7c/work/roadmaps/harada-full-map) | Newly recovered unmerged proposal; 31 commits ahead of its divergence and 121 behind current main, not ratified. Its nine outcome branches, 80-ID coverage, original §15 properties/§16 scenarios, dependencies and challenge are useful inputs. Reconcile unique acceptance conditions into the existing master, not a parallel tree. |
| [October goal remap](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/research/evaluation-and-reliability/2026-10-20-think-plan-maps-goal-remap.md) | Preserve source rationale, not external-pilot-first mandate. |
| [November reconciliation proposal](https://github.com/BigCatMellow/MAPS_Lean/tree/a4f9becb20eecb4090790d777454872aeca0ec96) | Eight changed paths, unmerged. Adopt objective/coverage lessons as appropriate; external pilot priority no longer matches operator direction. Regression check candidate requires execution/review. |
| docs/method-selection-no-sprawl-20261021 | Two commits ahead of divergence; candidate PROJECT_BOOTSTRAP/roadmap router, compare against merged native THINK/PLAN and avoid duplicate rules. |
| [#341](https://github.com/BigCatMellow/MAPS_Lean/pull/341) | Only open source PR; head 3f5e6fb332ac5d7f51031f3c0bac2be857d974e5. Benchmark parked; selection revision still needs review, Gate 1 Arm C and Gate 4/5 custody unresolved. Preserve pinned branch and evidence; no run, spend or approval. |
| [#247](https://github.com/BigCatMellow/MAPS_Lean/issues/247), [#248](https://github.com/BigCatMellow/MAPS_Lean/issues/248), [#331](https://github.com/BigCatMellow/MAPS_Lean/issues/331) | Routed to continuity/reasoning and operational reliability; actual implementation still conditional/pending. |
| [Ideas](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas), [insights](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights), [friction](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/coordination/FRICTION_LOG.md) | 8 ideas, 12 insights and dated friction records retained; full dispositions require checking promoted/stale/resolved evidence and open records. Source merge authorization friction UNVERIFIED: verify new successor governance before use. |
| [Handoff register](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/handoffs/README.md) | 64 recorded handoffs (55 continued, 7 closed, 1 open, 1 acknowledged in prior audit). Open external bobo PLAN calibration file inaccessible; acknowledged legacy navigation/simulation handoff needs successor decision. Verify continued pointers; cannot treat as closed. |
| [Review queue](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/review_queue/README.md) | Five old QUEUED packets; reconcile to live source review/merge and tests; do not blindly restart or mark done. |
| [Research index](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/research/README.md), [legacy audit](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/LEGACY_KNOWLEDGE_AUDIT.md), [idea recovery audit](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/LEGACY_IDEA_RECOVERY_AUDIT.md), [promotion ledger](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/LEGACY_PROMOTION_LEDGER.md), [future backlog](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/FUTURE_IDEAS_BACKLOG.md) | Existing audits support keeping historical source trees in place. The older idea recovery audit has explicit remaining audit work; do not mark all 2,474 historical files semantically resolved from their classification. Preserve candidate triggers, examine unresolved lessons, then disposition by group. |
| Pilot Project Folder, competitor add-ons, Map the System, HCOM messages, Wiki update | Reported open concerns, original requirements need recovery. Route to portability, learning, continuity, coordination and usability; no speculative closure. |

## Successor merge and review boundary

The source AGENTS.md is staged byte-for-byte, including its repository-specific
OPCMD policy. It is not yet activated on main. Old standing authorization and
repository configuration do not transfer. The source review/merge process must
be mapped into a usable successor gate without weakening human authority,
exact-head independent review, CI or fail-closed HOLD. No independent reviewer
is available in this session; do not self-approve. Preserve and prepare
independent slices while this is unresolved. The owner need not review
technical detail personally.

## Dependencies and next verification

M1: staged playbooks have references to future runtime, evidence, scripts and
coordination paths. Reconcile links to source or actual successor owners before
claiming usability. Preserve the source contract rather than silently rewriting
it; high-risk authority changes need explicitly scoped review.

M2: runtime is a tightly coupled Python package (124 files) with 114 test
modules/files. Inspect imports and test fixtures; migrate dependency-complete
slices starting with canonical state/policy and required primitives, preserving
schema, paths and executable modes. Do not run copied source automation that
targets old repo names, HCOM, local folders or credentials.

M3+: migrate/review CI, security, recovery, evidence and other capabilities in
dependency order; verify actual wiring, not just unit-test existence. External
target state, old local .maps databases and uncommitted files remain UNKNOWN.
Recover through the owner's environment if needed; no transfer of credentials,
live databases or paid execution is authorized.

## Idea and insight dispositions (candidate, source evidence inspected)

All 20 current source records were read at their disposition sections. These routes preserve open issues and prior closure decisions without treating the successor as verified. Promoted-but-unverified items require direct evidence, and open candidates do not become new tasks automatically.

| Source record | Proposed disposition / owning concern |
| --- | --- |
| [IDEA-582cc671](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-08-19-name-a-low-effort-zero-diff-re-review-tier-in-model-capabili-IDEA-582cc671.md) | Source stale/implemented #297, residual #345. Preserve review revalidation regression, no duplicate task. |
| [IDEA-20615e4d](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-08-19-standardize-per-agent-isolated-git-worktrees-as-the-default--IDEA-20615e4d.md) | Source superseded by worktree method plus #350 contract link. Preserve isolation rule and executed guard tests. |
| [IDEA-bc6cd243](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-09-03-a-stale-worktree-prune-report-step-in-coordination-housekeep-IDEA-bc6cd243.md) | Promoted in coordination tooling branch; verify landed prune/report behavior. Reliability; no destructive prune without boundary. |
| [IDEA-968eb261](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-09-03-check-review-evidence-py-should-tolerate-a-pure-rebase-onto--IDEA-968eb261.md) | Source stale/implemented #297; #345 resolves rebase residual. Safety/evidence regression. |
| [IDEA-a134ad7c](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-09-03-exclude-claude-worktrees-from-check-spiderweb-py-by-default-IDEA-a134ad7c.md) | Promoted in tooling fixes; verify scanner excludes transient worktrees without hiding actual source. Continuity. |
| [IDEA-9e7014fa](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-09-03-fix-coordination-housekeeping-py-it-crashes-on-gh-pr-list-IDEA-9e7014fa.md) | Promoted in tooling fixes; reproduce actual housekeeping call on successor with no external effects. Reliability. |
| [IDEA-fe6c0f0f](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-09-05-revalidation-review-tier-s-ancestor-check-never-fires-on-a-p-IDEA-fe6c0f0f.md) | Source implemented and reviewed #345; preserve diff-equivalence acceptance tests. Safety/evidence. |
| [IDEA-497fca2f](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/ideas/2026-09-10-track-rows-awaiting-a-first-exposure-exercise-in-a-standing--IDEA-497fca2f.md) | Open first-exposure tracking idea: use existing capability evidence row and tests, not another standing list. Reliability and continuity. |
| [INSIGHT-29a10ad4](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-08-19-check-review-evidence-py-s-head-sha-walk-back-stops-silently-INSIGHT-29a10ad4.md) | Known merge-commit review-evidence walkback constraint; retain provenance/verification tests and document limits, not weaken gate. |
| [INSIGHT-e0b448a6](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-08-19-recoverysupervisor-tick-has-zero-production-invocation-anywh-INSIGHT-e0b448a6.md) | Source resolved trigger #165; preserve recovery-tick and claim behavior tests, recheck HCOM optionality. |
| [INSIGHT-75785aae](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-08-19-the-harness-layer-h4-h5-l6-sec4-waves-has-zero-production-ca-INSIGHT-75785aae.md) | Source resolved production caller #277, actual default/guard coverage still separate H4/SEC3. Reliability. |
| [INSIGHT-102296b5](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-03-maps-recovery-tick-enforce-canonical-run-may-be-structurally-INSIGHT-102296b5.md) | Source resolved real-stall exercise DEC-003/#298; no automatic repetition, preserve regression evidence. |
| [INSIGHT-651d8c62](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-03-the-7-row-security-cluster-has-been-one-step-from-done-for-1-INSIGHT-651d8c62.md) | Source resolved specific seven-row stall; original L6 status contradiction and guard coverage remain evidence questions. |
| [INSIGHT-45727354](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-03-the-friction-log-behavioral-entry-path-lets-repeat-failures--INSIGHT-45727354.md) | Owner KEEP; no automatic task. Repeated drift must have mechanical safeguard; existing triage/repair owner. |
| [INSIGHT-68a53a28](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-03-the-roadmap-trajectory-check-has-become-part-of-the-developm-INSIGHT-68a53a28.md) | Owner KEEP; trajectory cadence should track meaningful arcs, avoid constant checklist bureaucracy. |
| [INSIGHT-ab696436](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-04-design-decision-notes-carry-stale-forward-references-to-work-INSIGHT-ab696436.md) | Specific DEC-003 resolved #284; general stale prerequisite references remain continuity gap, check actual accepted head before claiming blocked. |
| [INSIGHT-a6406800](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-04-triage-status-py-earned-its-keep-on-its-first-real-trajector-INSIGHT-a6406800.md) | Retain existing triage_status.py and tests; confirms mechanical check caught omission. Learning/continuity. |
| [INSIGHT-f095b669](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-10-outward-facing-representations-have-no-reconciliation-cadenc-INSIGHT-f095b669.md) | Open: reconcile wiki/README outward projections at meaningful arc, no parallel status tracker. Usability. |
| [INSIGHT-2b8b9a4b](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-12-gh-cli-merge-authorship-cannot-distinguish-an-agent-from-the-INSIGHT-2b8b9a4b.md) | Promoted native review protection candidate; no settings mutation authorized. Verify successor exact-head independence and identity governance before activation. |
| [INSIGHT-bbb3b845](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/insights/2026-09-12-new-standing-registers-created-without-a-named-reconciliatio-INSIGHT-bbb3b845.md) | Open: every standing register must have reconciliation owner/cadence. Use existing trajectory check. |

Tool/environment friction this arc: local clone failed DNS; connector has bounded call count and one remote disconnect. Recovery: pinned-tree batches limited to 8–12 reads, source/destination SHA+mode checks before atomic ref update. No credentials moved; one pattern match in redaction test was an explicit synthetic fixture. Record remaining local state UNKNOWN. Future recurring tool friction belongs in existing repair/learning flow, not a new tracker.

## Historical audit reconciliation checkpoint — 2026-11-24

Corrected integration [CI run 45419052227](https://github.com/BigCatMellow/MAPSL/actions/runs/45419052227) completed successfully in both runtime and coverage jobs. Runtime log reports 1,502 tests, OK (5 skipped); compilation, lint, security analysis, dependencies, smoke and inventory checks passed. This is CI evidence, not independent review. Source main comparison against the pinned baseline returned identical (zero ahead/behind).

The pinned legacy idea-recovery audit and promotion ledger were inspected again. Preserve their distinctions rather than resurrecting historical implementations. Route the recovered obligations into existing master roadmap programs:

| Program | Historical evidence and required disposition |
| --- | --- |
| Direction and continuity | Audit items 8, 9, 11, 18: actual-use checks, single state authority, derived wait visibility, reachable/correctable state transitions. Preserve bounded audit practice; no permanent watcher or duplicate state. |
| Reasoning and context | Items 4–6: frozen end-to-end context rubric, explicit authority boundaries, exact anchors, paraphrase and hard-negative tests. EXP-0006 was REVISE, not a successful retrieval implementation. |
| Execution and reliability | Item 12: no-progress advisory only when measured need exists; no automatic kill or naive timeout. Preserve source atomic claim, isolation and terminal recovery regressions. |
| Safety and evidence | Items 1, 13–17: durable write-surface secret safety, fresh/revision-bound evidence, behavioral security tests, risk-specific review, explicit ratification and prerequisite ordering. No proposal becomes authority by citation. |
| Learning and evaluation | Items 2, 3, 7, 10, 19: three-layer evaluation, scoped lessons with expiry, bounded proposal-only discovery, end-to-end scenarios, measured review changes. No continuous discovery loop. |
| Usability and portability | Preserve read-only status/replay concepts with completeness and provenance; old desktop/TUI/launchers and fixed rosters remain historical, not required infrastructure. |

Source promotion ledger explicitly classifies old task/event/handoff/review datasets as historical and rejects obsolete presentation implementations. Preserve pinned originals; do not copy live state or restart old tasks by default. The curated snapshots remain in the source. The legacy audit explicitly leaves unresolved MAP-relevant Insights, unfinished promotions, retired task chains and referenced research unexamined. These remain PENDING; this checkpoint does not establish semantic coverage of all 2,474 historical files. Next pass should screen those targeted records and check the current runtime before closing each group.

## Review queue and targeted insight reconciliation — 2026-11-24

All five source review packets were read. They refer to [PR #19](https://github.com/BigCatMellow/MAPS_Lean/pull/19), now closed with zero recorded GitHub reviews. Its implementation commit 0776a6b45490d85487c725474e9d3bbf600524da is an ancestor of the pinned main (936 commits ahead, zero behind). The candidate ledger records exact staging of the four runtime surfaces and corresponding original tests. Preserve packets as historical review inputs; do not manufacture approval or restart five implementation tasks.

| Packet | Successor review focus |
| --- | --- |
| Priority observability | Trace remains read-only, secret-safe boundaries and explicit coverage gaps; retain authority and risk-specific review rules. |
| Outcome feedback | DONE-only observations, immutable supersession and task/run provenance; no task authority mutation. |
| Context Builder v1 | Explicit input relationships, path confinement, hashes and coverage limits; no implicit retrieval authority. |
| Status surface | Canonical read-only attention projection, correct outcome supersession, explicit gaps. |
| PR CI | Read-only PR verification; confirm required checks and installer/legacy independence coverage before acceptance. |

Eight targeted historical insights were read in full from the pinned source:

- INS-0023 (RAW): inward infrastructure repeatedly displaced useful outcomes. Fold into Direction and continuity; current master outcome and actual-use acceptance address the concern in intent, not yet proven in practice. Do not impose an external pilot.
- INS-0032 (OPEN), INS-0053 (OPEN): rules buried in prose were repeatedly missed. Fold into controlled learning and behavioral enforcement; prove applicable guidance actually reaches agents and consequential guards execute. No duplicate global rules.
- INS-0054 (PROMOTED): remote authority network denial differs from local SQL denial; preserve explicit failure reasons, no classifier exemptions or automatic policy-denial retries. Old remote architecture remains historical.
- INS-0055 (PROMOTED): a checked discovery box did not establish useful discovery. Preserve bounded event-triggered, proposal-only discovery; no automatic model invocation or blanket release ritual.
- INS-0056 (PROMOTED): lessons from authorized method-only work can be lost without a formal task. Preserve opt-in learning without importing work into governance or expanding authority.
- INS-0059 (RAW): privileged mutation review caught arbitrary restore and transactional snapshot races. Preserve adversarial security and concurrency review for applicable paths, not old cross-host implementation.
- INS-0061 (RAW): scanner evidence pointed at unrelated events; separate uncommitted curation also caused duplicate processing. Preserve exact event attribution, source freshness and canonical reconciliation tests when implementing learning/eval signals; do not revive the legacy scanner.

These are proposed semantic dispositions within the existing roadmap programs. Current runtime behavior beyond the staged tests still requires direct verification; other Insights, promotions and retired task chains remain pending.

Migration friction: [CI run 45423585107](https://github.com/BigCatMellow/MAPSL/actions/runs/45423585107) caught a stale staged-adapted hash for state/CURRENT.md after the previous checkpoint edit. The ledger was repaired using the actual destination blob in commit 33e203673a5516f5561b860f496dfc23c7a1bece. Keep the existing fail-closed check. Future edits to staged destinations must reconcile the ledger in the same change; prefer atomic tree commits. Fresh CI remains required.

## Branch comparison checkpoint — 2026-11-24

[CI run 45423873562](https://github.com/BigCatMellow/MAPSL/actions/runs/45423873562) passed runtime and coverage after the ledger repair. The following comparisons were made against pinned source main, not against moving branch heads. All 17 checked branches diverge; divergence alone is not proof of unmerged functionality.

| Branch | Ahead/behind | Observed disposition evidence |
| --- | --- | --- |
| agent/operational-learning-authority1-wave4 | 2/515 | Storage code contains all old lines and newer active-lesson read projection; preserve newer source, check schema/tests/brief before closing. |
| agent/recovery-stage2-run-id-wiring | 1/515 | run_lineage.py exact; supervisor newer harness integration; check regression tests before closing. |
| agent/repo-cleanup-status-fix | 1/519 | Sole changed async-work-pull document blob identical; no unique file content. |
| agent/repair-record-stalled-worker | 1/513 | Sole changed note now includes explicit operator closure and sharded-test regression evidence; retain closed disposition, not new work. |
| agent/pin-hcom-fork-source | 1/518 | Installer exact; install docs contain old lines plus portable-target guidance; retain optional HCOM, no installation/external action. |
| agent/review-enforcement-design | 1/517 | Sole design note adds recorded Option B choice and limitation: evidence file cannot prove identity independence. Old standing authority does not transfer. |
| agent/task-briefs-authority1-recovery2 | 1/516 | Two task briefs; compare current dispositions before closure. |
| agent/stalled-work-triage-protocol | 1/514 | Coordination README; compare actual current guidance. |
| ask1-control-plane-runbook | 3/276 | Runbook and review evidence; inspect current version and avoid activating old setup. |
| agent/runtime-readme-refresh | 6/510 | Runtime README and review evidence; compare current version. |
| agent/review-evidence-check | 5/511 | Newer script adds content-equivalent rebase validation; preserve newer safety tests; other changed files pending. |
| canonical-denied-tick-state | 2/332 | Recovery store/supervisor/test, setup, review and checklist; compare current guarded denial behavior. |
| ci/handoff-receipt-registration-check | 2/142 | Script and original test exact; workflow, trajectory and evidence remain to reconcile. |
| chore/friction-log-triage-loop-20260831 | 6/343 | Legacy rotation plus active repair/trajectory/handoff/friction; distinguish obsolete code from lessons. |
| chore/repository-organization-2026-10-06 | 20/122 | Organization, legacy retention and navigation; preserve source decisions, inspect remaining differences. |
| chore/friction-rotation-followup-20260831 | 3/341 | Friction record and evidence; check later dispositions. |
| canonical-enforcement-first-exposure-design | 4/339 | Design note exact; review evidence pending. |

No older branch was merged. Remaining branch-only changes and semantic obligations stay pending. See the pinned refs below.

## Reference dispositions and portability checkpoint — 2026-11-24

The inventory now records 139 REFERENCE dispositions: 104 historical YAML handoff snapshots, one historical event dataset, six old review-queue documents, 20 already-reconciled current-source idea/insight records, and eight inspected legacy insight records. Each row points to its exact pinned original, rationale and evidence. Source legacy handoff/event/inbox indexes and the earlier audit were inspected; historical data must not become live state. This classifies file custody, not the completeness of all semantic obligations; unresolved retired task chains, promotions, current handoffs and other unique lessons remain PENDING. 343 files remain staged but not accepted; 3,033 additional source paths lack staging/disposition. See commit 5a729da8e1db794ff1d20849b7be7b9e1a7d0ec2.

The [green integration run](https://github.com/BigCatMellow/MAPSL/actions/runs/45423873562) reports all 21 portable-target preflight/init tests passing, including explicit roots, wrong types, self-targets, symlink boundaries, preview nonmutation, idempotency and non-overwrite. The smoke test also passed its no-legacy-execution-dependency assertion. Comparing the original runtime-stack workflow with successor migration coverage revealed two missing explicit steps: the full active legacy-dependency scanner and installer syntax/preview. Restored both in commit 33b02fb2a3c6d9dff80655d03e605841793746a7, with preview checks for absent .venv/.maps/.hcom and clean tracked status. This is read-only CI verification; no external installation or target project mutation. Fresh CI for these changes and a disposable full fresh-install exercise remain required.

## Source branch inventory

All 102 observed branch refs are pinned here for later unique-content
reconciliation. A listed ref does not mean live work, unmerged content, or
permission. Determine ancestry/tree equivalence and PR disposition before
importing unique forward-relevant work. Source is preserved even if a branch is
not migrated.

| Branch | Observed head |
| --- | --- |
| 6.9-slice2-impl | [7ed7858d33](https://github.com/BigCatMellow/MAPS_Lean/tree/7ed7858d334d1be0e7755ad606297abcf10167e0) |
| 6.22-withhold-fixture-b-results | [8354053c9c](https://github.com/BigCatMellow/MAPS_Lean/tree/8354053c9c9dcec1d0a0c3366f7e8bc2bd276d76) |
| agent/operational-learning-authority1-wave4 | [7d77b59232](https://github.com/BigCatMellow/MAPS_Lean/tree/7d77b5923255af859340668e5363e5323b6d8d80) |
| agent/pin-hcom-fork-source | [781bd5229f](https://github.com/BigCatMellow/MAPS_Lean/tree/781bd5229fa21f047debe06de4edd24f4af01a05) |
| agent/recovery-stage2-run-id-wiring | [5dd8d7cfd7](https://github.com/BigCatMellow/MAPS_Lean/tree/5dd8d7cfd72e03c75f111368f1bcefdf97e8a56d) |
| agent/repair-record-stalled-worker | [1531e40354](https://github.com/BigCatMellow/MAPS_Lean/tree/1531e403546980b4d4beec18c2551b00ee3514ab) |
| agent/repo-cleanup-status-fix | [cd2f15359b](https://github.com/BigCatMellow/MAPS_Lean/tree/cd2f15359b6fb0fe2aa6c8c899ce33512126b278) |
| agent/review-enforcement-design | [036dd8a0bb](https://github.com/BigCatMellow/MAPS_Lean/tree/036dd8a0bbc6c28675c53b1a5ff76cc34938eb64) |
| agent/review-evidence-check | [954b80fa80](https://github.com/BigCatMellow/MAPS_Lean/tree/954b80fa808cc3f8930a1041a92c1de33f2256d2) |
| agent/runtime-readme-refresh | [a23b1a2ef5](https://github.com/BigCatMellow/MAPS_Lean/tree/a23b1a2ef5ef6bdabdef073f6d045d0c726bcadc) |
| agent/stalled-work-triage-protocol | [74382693ec](https://github.com/BigCatMellow/MAPS_Lean/tree/74382693ec8fdfa062b17f6fff19b862e033c2e7) |
| agent/task-briefs-authority1-recovery2 | [658a721f3f](https://github.com/BigCatMellow/MAPS_Lean/tree/658a721f3fcea2351614c48d090bb958101a8e9b) |
| ask1-control-plane-runbook | [29296659f8](https://github.com/BigCatMellow/MAPS_Lean/tree/29296659f8b67b6060b52f4c41cc6e4dda57fbb0) |
| canonical-denied-tick-state | [9e5fba09ab](https://github.com/BigCatMellow/MAPS_Lean/tree/9e5fba09aba7142a6247e8b5862bc5e81d3f164b) |
| canonical-enforcement-first-exposure-design | [8cad49fb93](https://github.com/BigCatMellow/MAPS_Lean/tree/8cad49fb93d70d010b251f02e36834fd92c5e34e) |
| chore/friction-log-triage-loop-20260831 | [ac277a04fe](https://github.com/BigCatMellow/MAPS_Lean/tree/ac277a04fefb76db99c6330faea418251e5a5dbf) |
| chore/friction-rotation-followup-20260831 | [45be6b9598](https://github.com/BigCatMellow/MAPS_Lean/tree/45be6b95989920c89e7a775bae6358d18e17ebb5) |
| chore/repository-organization-2026-10-06 | [e8437e6dca](https://github.com/BigCatMellow/MAPS_Lean/tree/e8437e6dcae051f62f1d3d0072eb704ecff95fd1) |
| ci/handoff-receipt-registration-check | [e03b51a2fe](https://github.com/BigCatMellow/MAPS_Lean/tree/e03b51a2fe743de7940d8cbbddf6db953f6fe8c0) |
| design/env-report-source-cache | [b9fb4270bd](https://github.com/BigCatMellow/MAPS_Lean/tree/b9fb4270bddc34c2cf0df763e3684ef7d9c3d915) |
| design-6.22-withhold-deny-fixture | [5b4ea469d3](https://github.com/BigCatMellow/MAPS_Lean/tree/5b4ea469d3de0f72a425d39f5aa890ef5e9a5113) |
| docs/adapt-think-plan-evidence-led | [e2f8b7b0ba](https://github.com/BigCatMellow/MAPS_Lean/tree/e2f8b7b0babf01432c9a774dd1c6aab600d32761) |
| docs/handoff-register-legacy-sweep-maps-lean | [a00c9d1901](https://github.com/BigCatMellow/MAPS_Lean/tree/a00c9d1901ec37c6a6a1405317247ede8ef12fed) |
| docs/method-selection-no-sprawl-20261021 | [80c4f88433](https://github.com/BigCatMellow/MAPS_Lean/tree/80c4f8843393c8c0faad4f3cd0fa1866484b78ea) |
| docs/protocol-discoverability-2026-09-15 | [2f0e396e6b](https://github.com/BigCatMellow/MAPS_Lean/tree/2f0e396e6b61a45ba99dd6d07e3a97d68f064602) |
| docs/reconcile-program-direction-20261124 | [a4f9becb20](https://github.com/BigCatMellow/MAPS_Lean/tree/a4f9becb20eecb4090790d777454872aeca0ec96) |
| docs/reset-desk-log | [4a2d6011ba](https://github.com/BigCatMellow/MAPS_Lean/tree/4a2d6011ba3066504113715f6f8e9267574a2378) |
| docs/roadmap-crossproject-tracking | [8bf36beeb0](https://github.com/BigCatMellow/MAPS_Lean/tree/8bf36beeb0e798a5186f4ab304a87e293c8751db) |
| emergence/cross-root-synthesis-20260905 | [6a72ac6027](https://github.com/BigCatMellow/MAPS_Lean/tree/6a72ac6027defacfe3a2319548c0c29986f2047e) |
| emergence/supersession-authority-20260907 | [09d904c449](https://github.com/BigCatMellow/MAPS_Lean/tree/09d904c449b5db91ac62761b3b2f9f70dae80635) |
| eval/protocol-effectiveness-benchmark-v0 | [3f5e6fb332](https://github.com/BigCatMellow/MAPS_Lean/tree/3f5e6fb332ac5d7f51031f3c0bac2be857d974e5) |
| feat/portable-target-preflight-20261104 | [755f237967](https://github.com/BigCatMellow/MAPS_Lean/tree/755f2379679a3353a3494aa8805e7a51b489a00e) |
| feature/decision-provider-seam | [bda1cd50f9](https://github.com/BigCatMellow/MAPS_Lean/tree/bda1cd50f9349747bc68d21f696f5e3a1fafe38d) |
| feature/idea-fe6c0f0f-diff-equivalence | [1b760fdcf8](https://github.com/BigCatMellow/MAPS_Lean/tree/1b760fdcf8b435b76dd3f924a171c8c3bffbcdd7) |
| fix/dependency-cycle-readiness-2026-09-09 | [c5d82767af](https://github.com/BigCatMellow/MAPS_Lean/tree/c5d82767afd38df5d0276eac1d7bb68185135797) |
| fix/github-native-standing-merge-gate-20261020 | [0dd8d4e2a7](https://github.com/BigCatMellow/MAPS_Lean/tree/0dd8d4e2a7f8395a7e92298e21ab4d71f7cc5f80) |
| flow-handoff-prose-fix | [ab2ebc4b5c](https://github.com/BigCatMellow/MAPS_Lean/tree/ab2ebc4b5c1933c926150c9e7a2629489c3a6a86) |
| flow-release-check-design | [fe659e0a41](https://github.com/BigCatMellow/MAPS_Lean/tree/fe659e0a418f30802ecf33ad57eb6f0311e92de0) |
| flow-release-check-impl | [f623d8eed6](https://github.com/BigCatMellow/MAPS_Lean/tree/f623d8eed66cb2c45f8d6cb444910f348a246864) |
| handoff/reviewed-gap-switchyard-2026-09-10 | [0466d353b3](https://github.com/BigCatMellow/MAPS_Lean/tree/0466d353b3f945217d37ff3bb4a43c5f9ec74982) |
| handoff/task-history-retention-guards-2026-09-10 | [a9b6619574](https://github.com/BigCatMellow/MAPS_Lean/tree/a9b6619574bd0632a51ad4fb4a1e9e2eb31fd0e4) |
| handoff-reconciliation-phase4-maps-correction | [dac0f2c35f](https://github.com/BigCatMellow/MAPS_Lean/tree/dac0f2c35f33ab308a9b5a7e8418d0bb5d5323ab) |
| impl/hook-harness-composition-root-20260830 | [7c26719fe2](https://github.com/BigCatMellow/MAPS_Lean/tree/7c26719fe2fcef89954ebfa9e65822583f7ca031) |
| impl/resume-validation-gate | [cb2c058056](https://github.com/BigCatMellow/MAPS_Lean/tree/cb2c05805649b34d7c2f668c16adc94b95e21433) |
| impl/sec4-half2-authority-wiring | [368fd897e9](https://github.com/BigCatMellow/MAPS_Lean/tree/368fd897e910964a91bad08882f42fe006677bca) |
| impl/worktree-binding-guard-20260831 | [2b16c96056](https://github.com/BigCatMellow/MAPS_Lean/tree/2b16c96056ca80108355710d4286b873b92709a8) |
| lineage-bootstrap-wiring-scoping | [ff4e8a603e](https://github.com/BigCatMellow/MAPS_Lean/tree/ff4e8a603e116e274be79f018898b5203b46f3ce) |
| main | [605ce610e0](https://github.com/BigCatMellow/MAPS_Lean/tree/605ce610e0be3334d1da7af2a7c6f5912b6cc05f) |
| maintenance/pilot-information-routing-20260829 | [b8e10b24d5](https://github.com/BigCatMellow/MAPS_Lean/tree/b8e10b24d516372cf188f7091d1ed0b042cc82d0) |
| maintenance/reconcile-project-truth-20260826 | [fe97cb5710](https://github.com/BigCatMellow/MAPS_Lean/tree/fe97cb571044c43924f183f24a56d79d9c4d4bdc) |
| memory-trust-tool-call-gate-design | [8a4ee5c314](https://github.com/BigCatMellow/MAPS_Lean/tree/8a4ee5c31465dcde73d5b7ddb9dceed4d6b657c8) |
| noop | [18b064cdce](https://github.com/BigCatMellow/MAPS_Lean/tree/18b064cdce00963b0417c8105c36e7fe624f3e4e) |
| noop2 | [18b064cdce](https://github.com/BigCatMellow/MAPS_Lean/tree/18b064cdce00963b0417c8105c36e7fe624f3e4e) |
| noop3 | [18b064cdce](https://github.com/BigCatMellow/MAPS_Lean/tree/18b064cdce00963b0417c8105c36e7fe624f3e4e) |
| obs/recovery-harness-operation-evidence-2026-09-09 | [18b064cdce](https://github.com/BigCatMellow/MAPS_Lean/tree/18b064cdce00963b0417c8105c36e7fe624f3e4e) |
| operator-decisions-session17 | [7a43483b11](https://github.com/BigCatMellow/MAPS_Lean/tree/7a43483b1157b6b341607e558ae7282d4be039b7) |
| plan/full-recursive-harada-capability-roadmap-2026-10-20 | [f5f2e21bb0](https://github.com/BigCatMellow/MAPS_Lean/tree/f5f2e21bb0cfa5872d86baaafc1f8c89378e0a7c) |
| plan/think-plan-maps-goal-remap-2026-10-20 | [ae0ec2048f](https://github.com/BigCatMellow/MAPS_Lean/tree/ae0ec2048fc0f57dbdaedad5d829e30edd5a99c9) |
| portable-d1-installer-design | [d6bdcc75b5](https://github.com/BigCatMellow/MAPS_Lean/tree/d6bdcc75b588af0e4e0ae37cd2df61eeca999aa7) |
| pr116 | [680c103fc7](https://github.com/BigCatMellow/MAPS_Lean/tree/680c103fc77ea2204753fc49e209124fcc5589f4) |
| pr341-armc-approval-solo-owner-design-2026-09-16 | [6756376a52](https://github.com/BigCatMellow/MAPS_Lean/tree/6756376a52e925497f3f59b7f01d8814c25f688f) |
| release-check-3b-scoping | [78cba06ec1](https://github.com/BigCatMellow/MAPS_Lean/tree/78cba06ec180cb4f7e552e23efc4e358baad9ea6) |
| research/cost-resource-admission-audit-2026-09-09 | [29b69a60a2](https://github.com/BigCatMellow/MAPS_Lean/tree/29b69a60a245a7a3eb339286c84ffb82e65576f1) |
| research/external-effect-idempotency-audit-2026-09-09 | [a33eea89aa](https://github.com/BigCatMellow/MAPS_Lean/tree/a33eea89aaaff3fa03ada424bb1fcf0b0573f621) |
| research/github-mechanisms-cross-system-20261104 | [e46e4d5d72](https://github.com/BigCatMellow/MAPS_Lean/tree/e46e4d5d72b89993cdc693cbd0fb28c5d6bc1d07) |
| review/pr-178-evidence-20260830 | [7e88aeb1d4](https://github.com/BigCatMellow/MAPS_Lean/tree/7e88aeb1d4cf543f599b9548ad46d74dbc5add4d) |
| review/pr-179-evidence-20260830 | [530ed98124](https://github.com/BigCatMellow/MAPS_Lean/tree/530ed98124ede11e3cab34d4f15cb3ba7df2a5dd) |
| review/pr-179-rebased-evidence-20260830 | [1a737dd095](https://github.com/BigCatMellow/MAPS_Lean/tree/1a737dd095c1d9a293739649fc5a5db4590e9cd7) |
| review/pr-180-evidence-20260830 | [db003e6c82](https://github.com/BigCatMellow/MAPS_Lean/tree/db003e6c82d0bfa5da370426056e4c4741e301f7) |
| review/pr-180-rebind-20260830 | [a29a15d60b](https://github.com/BigCatMellow/MAPS_Lean/tree/a29a15d60bc09741e5434dfbf49b50f230985975) |
| rns-harness-resume-callsite | [f08e11c748](https://github.com/BigCatMellow/MAPS_Lean/tree/f08e11c7489932dcae705e6670dc1d99b4cbe42e) |
| rns-trigger-loop-design | [e6f801d270](https://github.com/BigCatMellow/MAPS_Lean/tree/e6f801d270e5c138b23a8ac52d2046adef6bafa8) |
| rns-validation-tier-impl | [e0478b4332](https://github.com/BigCatMellow/MAPS_Lean/tree/e0478b433244c3ec95c2a6632675a5efc3d2eddc) |
| s6-frozen-eval-v2-corpus | [a3f5bd1f42](https://github.com/BigCatMellow/MAPS_Lean/tree/a3f5bd1f421352ea48d39fcc51b99e406ee4fb5a) |
| s6-frozen-selection-eval-scoping | [90c7fa0155](https://github.com/BigCatMellow/MAPS_Lean/tree/90c7fa01554101637d7a9847c67482c2066e1a01) |
| s6-selector-quality-impl | [b6c38cdebc](https://github.com/BigCatMellow/MAPS_Lean/tree/b6c38cdebc85d2fb7c3ad29fcede0ed8846733cd) |
| s6-selector-quality-scoping | [eb0f753983](https://github.com/BigCatMellow/MAPS_Lean/tree/eb0f753983b859074ba44f2e49d09e843f98d06a) |
| s6-slice3-scoping | [152f04d4e6](https://github.com/BigCatMellow/MAPS_Lean/tree/152f04d4e63e76763eab6a16dfdf6b57911ee9a0) |
| sec3-64-guard-wiring | [e8f77d160a](https://github.com/BigCatMellow/MAPS_Lean/tree/e8f77d160a46d4f530fb464f88ae8373e6ef5ea9) |
| sec3-guard-impl-readiness-design | [b7345bd608](https://github.com/BigCatMellow/MAPS_Lean/tree/b7345bd608816b4e797407f372256593314f499b) |
| sec4-catalog-entrypoint-design | [a654c173d3](https://github.com/BigCatMellow/MAPS_Lean/tree/a654c173d3b895f45f9fa8345ba3cd54c19ac00b) |
| sec4-catalog-entrypoint-impl | [59f488feb3](https://github.com/BigCatMellow/MAPS_Lean/tree/59f488feb30e174d617d9adc63138f7362a8591b) |
| sec4-half2-authority-wiring-design | [a73ca5e118](https://github.com/BigCatMellow/MAPS_Lean/tree/a73ca5e1188e11105755664328079409d44ea890) |
| sec4-half3-slice2-2a | [ef1ea3815a](https://github.com/BigCatMellow/MAPS_Lean/tree/ef1ea3815ac656c043f972c2dde7885f538253cd) |
| sec-65-resume-val-gate | [96ecdf2702](https://github.com/BigCatMellow/MAPS_Lean/tree/96ecdf2702e3cf9cd391e2084a0ac5e40e6075f3) |
| session43-handoff-receipt | [bd1fcb7f4c](https://github.com/BigCatMellow/MAPS_Lean/tree/bd1fcb7f4cc0ad053661868d07c6b4c80e4b87b0) |
| spiderweb-audit | [0f15e5b9ba](https://github.com/BigCatMellow/MAPS_Lean/tree/0f15e5b9ba477797de355efaff6c973c8c13654d) |
| switchyard/context-evidence-stage1-sync-20260816 | [ec525615fd](https://github.com/BigCatMellow/MAPS_Lean/tree/ec525615fd708610bc3e90e07a95bb6c791d2465) |
| task-environment-contract | [75411a2861](https://github.com/BigCatMellow/MAPS_Lean/tree/75411a28614660b3f6c10b6941e009421c70201b) |
| tests/competitor-stale-owner-invariant-2026-09-09 | [018312f7c3](https://github.com/BigCatMellow/MAPS_Lean/tree/018312f7c33759eaaf4c1cab02e19940a4ff59c5) |
| tests/task-event-atomicity-2026-09-09 | [29f5c62111](https://github.com/BigCatMellow/MAPS_Lean/tree/29f5c621119a3053c919de54654ccc8f1655f4f0) |
| tmp-ignore | [18b064cdce](https://github.com/BigCatMellow/MAPS_Lean/tree/18b064cdce00963b0417c8105c36e7fe624f3e4e) |
| trajectory-check-15 | [f08f2b1a80](https://github.com/BigCatMellow/MAPS_Lean/tree/f08f2b1a8070ba4ebed27e22b3f5fbbb90bbe448) |
| trajectory-check-16 | [d444ef764a](https://github.com/BigCatMellow/MAPS_Lean/tree/d444ef764a24174186e5a48f97f31e31fc447454) |
| validation-callsite-design | [9591be4dcf](https://github.com/BigCatMellow/MAPS_Lean/tree/9591be4dcf6a40b4e988148eff0c71c039c3abd7) |
| vame/trajectory-check-18 | [689142501e](https://github.com/BigCatMellow/MAPS_Lean/tree/689142501ec5cbd084a33ffc4f992a44413098b5) |
| vame/trajectory-check-19 | [08da4d704b](https://github.com/BigCatMellow/MAPS_Lean/tree/08da4d704baff59f6865b6821e185f5209be320d) |
| vame/6.9-s6-gate-rerun | [1cccbc666f](https://github.com/BigCatMellow/MAPS_Lean/tree/1cccbc666fec7284f656c15c04b8e9bd0d5869d8) |
| wiki-protocol-map | [6124c9cec8](https://github.com/BigCatMellow/MAPS_Lean/tree/6124c9cec88153205d867cf33ffe2363eabace99) |
| worktree-binding-enforcement-seam | [94f7f23ee1](https://github.com/BigCatMellow/MAPS_Lean/tree/94f7f23ee19164da101850c14e3f53d4e4df40a6) |
| worktree-invariant-drift-safeguard | [79a1075913](https://github.com/BigCatMellow/MAPS_Lean/tree/79a1075913ba31ffb749ab2481956a9379886dcf) |
| worktree-sec4-half3 | [75312ece89](https://github.com/BigCatMellow/MAPS_Lean/tree/75312ece8913e5ecd2bf7dbfee6cffaba366798f) |
