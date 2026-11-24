# MAPSL — controlled successor migration

**Status: authorized migration in progress (2026-11-24).**
This is the single migration plan and restart entry until cutover. It is not yet
the successor operating contract. The owner authorized the reversible migration on 2026-11-24, with the original
MAPS_Lean repository preserved. Routine authorized implementation proceeds
without per-stage human permission. This does not waive independent review,
authority boundaries, or the final cutover decision.

## 1. Outcome and boundaries

Build a coherent, maintainable successor to MAPS_Lean, not a new architecture
for its own sake. MAPS already works in practice. Preserve its proven useful
behavior, deliberate decisions, safeguards, regression tests and lessons;
repair actual defects and remove duplication without losing meaning. Comparative
benefit over ordinary agent-assisted work is still unknown; measure when useful,
not as a prerequisite to migration.

Permanent objectives: autonomous completion, reliability, reasoning/planning,
continuity, efficiency, adaptability, controlled learning, usability, and safety/
human authority. Every retained capability should serve at least one objective.

Source of truth for migration:

- [MAPS_Lean main at 605ce61](https://github.com/BigCatMellow/MAPS_Lean/tree/605ce610e0be3334d1da7af2a7c6f5912b6cc05f).
- [Runtime CI at source baseline](https://github.com/BigCatMellow/MAPS_Lean/actions/runs/45405604013) reported success. This is evidence of the source, not successor parity or fresh independent review.
- [Unmerged reconciliation proposal at a4f9bec](https://github.com/BigCatMellow/MAPS_Lean/tree/a4f9becb20eecb4090790d777454872aeca0ec96): evaluate separately, not accepted source authority. Eight changed paths: root README, state/CURRENT, master/checklist/roadmap router/subsystem router, trajectory playbook, documentation-sprawl tests.
- Both repositories are public. Inspect material for secrets, sensitive records, third-party license restrictions and target-specific assumptions before copying; public source does not make every item appropriate for republication.
- Source remains intact and operational. No source deletion, archive-setting change, rewriting of Git history, secrets/credentials transfer, external project modification, paid execution, or security-control bypass. Do not maintain two feature-development programs; track necessary source changes and reconcile the delta before cutover.
- Preserve existing authority decisions and risk-based independent review. The eight-PR merge exception on the old repo does not carry over. Establish a workable successor merge/review mechanism before relying on it; do not blindly transplant repo-specific HCOM/OPCMD settings. HCOM is not used operationally by the owner; distinguish retained adapter functionality from required infrastructure.

## 2. Proposed repository ownership

Start small; create directories only when their content earns them. Names below
are tentative and may remain the existing names when that minimizes disruption.

| Owner | Job |
|---|---|
| README.md | Brief human/agent entry; link to the current plan and instructions |
| AGENTS.md | Sole global operating contract |
| roadmap/ | One current outcome-driven roadmap; one capability evidence view; detailed designs only as needed |
| playbook/ | One owner per reusable method |
| runtime/, scripts/, tools/ | Existing implementation and deterministic tooling; retain import paths where practical |
| tests/, .github/ | Regressions, checks, CI and reviewed integration |
| docs/ | Installation, operation, user guidance |
| templates/ | Reusable record shapes |
| work/ | Necessary task/review/decision/research/evidence records; no competing priority lists |
| state/CURRENT.md | Short restart pointer: current outcome, next action, blocker, evidence |
| migration/ | Temporary reconciliation evidence; archive in place after cutover |

GitHub owns live PR/CI/issue facts; canonical runtime state owns task lifecycle
truth where runtime is used. Markdown describes approved intent, reusable
methods, decisions and continuation. Do not add another task store or permanent
migration dashboard.

## 3. Account for everything

The pinned source tree contains 3,515 tracked blobs (31 executable): 2,359 under
legacy/, 115 curated legacy snapshot files under migration/legacy-*, and 1,041
other files. [Source inventory](migration/source-inventory.tsv) is the exact
path/blob/mode inventory for this baseline. It starts unreviewed, not migrated.
Do not equate inventory coverage with review coverage.

Every path must ultimately have a disposition, destination or durable source
pointer, rationale and evidence. Group paths when they share the same
dependency/disposition; do not force separate prose for every historical blob.
Track semantic items as well as files: capabilities, methods, requirements,
tests, research recommendations, decisions, tasks, issues, handoffs and known
failures. One file can contain several distinct obligations. Map those to the
existing owning capability/roadmap, not a permanent parallel backlog.

| Disposition | Meaning |
|---|---|
| MIGRATE | Retain content/behavior essentially unchanged |
| IMPROVE | Bounded change for a demonstrated defect; retain proof |
| CONSOLIDATE | Merge duplicate concepts; preserve all decision-relevant behavior |
| REPLACE | Equivalent or better behavior with tests and migration rationale |
| DEFER | Named owner, rationale, trigger and source pointer |
| RETIRE | Superseded/rejected, with rationale and preserved source |
| REFERENCE | Preserve pinned historical evidence in the original repo; no active copy needed |
| PENDING | Unassessed; never treated as complete |

Use the source inventory as a temporary coverage ledger; a terminal disposition
must include evidence and a target or source pointer. Verify destination files
against the pinned source where unchanged, tests and behavior where changed.
Record source deltas separately until incorporated. For source-only historical
groups, inspect their indexes, unique lessons and forward-relevant content before
choosing REFERENCE; never discard an entire subtree merely because it is old.

### Non-file and cross-source obligations

The migration cannot close until these are reconciled:

- All 35 master capabilities and all subsystem checklist rows (including 33
  unfinished rows after the proposed L6 correction); preserve previously
  completed capability regressions and conditional promotion gates.
- All six subsystem roadmaps, Prime study, intent compiler, async work pull,
  dated remap/first-wave/competitor research, migration backlog and promotion ledger.
- Ideas (8) and insights (12), friction log, handoff register, review queue,
  work/tasks, work/notes, decisions and review evidence. Check current owners
  and distinguish completed history from forward obligations.
- [Open PR #341](https://github.com/BigCatMellow/MAPS_Lean/pull/341): deferred
  benchmark, not execution-authorized; preserve unresolved approval/custody gates.
- Open issues [#247](https://github.com/BigCatMellow/MAPS_Lean/issues/247)
  (durable memory), [#248](https://github.com/BigCatMellow/MAPS_Lean/issues/248)
  (instruction/context compilation), [#331](https://github.com/BigCatMellow/MAPS_Lean/issues/331)
  (tool friction). Reconcile branch-only work and verify current PR/issue
  history at cutover. Do not close original issues merely because they are mapped.
- Previously reported concerns: Pilot Project Folder, competitor add-ons,
  Map the System, HCOM messages, Wiki update. Recover their actual source
  requirements, then route to owners or explicitly defer.
- Local handoff files, external Pilot Projects and uncommitted state are not
  accessible from the source tree. Record UNKNOWN with a named recovery action;
  no assertion of complete coverage without resolution or an explicit owner
  decision to exclude. Native THINK/PLAN are not blocked by external research.

## 4. Sequence (dependency slices, not blind directory copies)

| Stage | Deliverable | Exit gate |
|---|---|---|
| M0 — Inventory and baseline | Pin source and non-main candidates; recover outstanding sources; classify active, conditional and historical work; establish source test baseline and dependency/import map | Complete enumerated coverage; unresolved sources named; test/review method available; no unsupported status claims |
| M1 — Operating foundation and direction | Concise root contract, native THINK/PLAN, objective/acceptance shaping, task lifecycle, program steering, trajectory/continuation; master roadmap with objective-linked dispositions | No loss of authority/invariants; no duplicate plan; fresh session can identify next action from entry point; relevant documentation tests pass |
| M2 — Working runtime foundation | Transfer canonical task state, policy, manifests, routing, CLI, environment, context, skills, helpers and their transitive dependencies/tests in runnable increments | Each slice imports/runs; task lifecycle, authority and evidence tests pass; no duplicate state; preserve executable modes and dependency pins |
| M3 — Reliability and coordination | Recovery, harness/adapter boundaries, hooks, isolation, lineage, review, security, regression cases and CI; verify default execution paths, HCOM optionality and GitHub-native merge controls | Failure injection, authority denial, recovery and independent review verified; no security or continuity regression; no unreviewed control bypass |
| M4 — Learning and improvement | Outcomes, evals, incident taxonomy, controlled learning, research and conditional capabilities; DecisionBroker/Jev optionality; reconsider proposed GROW only if existing JUDGE/LEARN insufficient | Provenance and trust preserved; no autonomous policy promotion; evaluation records comparable; pending improvement candidates have owners/triggers |
| M5 — Portability and usability | Target preflight/init, install, thin adapters, docs/wiki, method-only/orchestrated/runtime-backed usage; update links and repo names | Fresh install and isolated disposable target smoke pass; ordinary use remains straightforward; no mandatory unused HCOM or external service |
| M6 — Full reconciliation and cutover | Account for every source path and semantic obligation, reconcile source delta, verify integrated parity and current roadmap; one active successor | No unowned pending item; regression/CI pass and independent integrated review; known gaps visible; source preserved with rollback; owner decides cutover |

M2–M5 are ordered by dependencies, not arbitrary module boundaries. Move
supporting code/tests earlier when required; do not leave a broken intermediate
slice on main. Parallelize only non-overlapping work and independent reviews.

## 5. Repeatable slice procedure

1. Recover the parent outcome and pinned source state; select the smallest
   useful dependency-complete slice.
2. Identify source paths, semantic obligations, tests, transitive dependencies,
   assumptions, and expected destination. Define success and non-goals.
3. Review the original design against actual behavior and objectives. Prefer
   exact transfer first; change only for a documented reason. Separate larger
   redesigns into later roadmap work.
4. Implement in a bounded branch/PR, with provenance pointers and tests;
   inspect outputs, validate references, imports, modes, paths, and relevant
   test results. Verify negative and recovery cases where applicable.
5. Obtain independent review proportional to risk, correct findings, reverify.
   Record actual evidence; do not claim independence from the author's own check.
6. Reconcile migration dispositions, canonical roadmap and current restart
   pointer in the same arc; proceed to the next eligible slice without a routine
   approval request. Escalate only an actual authority boundary or blocker.

## 6. Mechanical safeguards and completion

Build on existing tests rather than proliferating protocols. Establish checks for
inventory completeness (exact pinned path set, no duplicates, no missing
dispositions at cutover), valid destination/evidence pointers, objective/owner
coverage of unfinished capabilities, links, and CI/test parity. Report UNKNOWN
for inaccessible evidence. A presence check cannot prove semantic coverage;
independent sample/critical-path review must challenge omissions.

Measure real outcomes, failures, interventions, context/cost where available,
and continuity. Do not optimize file count, agent count, token count or checklist
closure at the expense of correctness. On repeat drift, add the smallest
enforced check for the observed failure.

**DONE means:** source and successor are traceably reconciled; accepted behavior
and safeguards retained or deliberately improved; tests and independent review
pass; deferred/retired/reference items are explicit; install/use/restart routes
work; one prioritized future roadmap exists; no accidental loss of source
knowledge or work. Cutover is a separate owner decision; rollback is the
unchanged old repository.

## 7. Current checkpoint

- M0 active: source pinned, exact 3,515-file inventory verified; source untouched.
- M1 preparation: isolated branch `migration/foundation`; no successor operating
  contract or implementation accepted on main yet.
- Next: reconcile outstanding sources, stage the operating foundation and its
  dependencies; retain historical source pointers, verify and review before
  acceptance. Local GitHub clone is unavailable in the execution environment
  (DNS/network); use connected GitHub and successor CI where available.
- No independent reviewer has been established. Do not self-approve or treat
  staged work as accepted. Continue independent preparation inside scope.
