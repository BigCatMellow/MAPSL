# Comparative research across the MAPSL work system

November 26, 2026 · MAPSL baseline [48edfaf](https://github.com/BigCatMellow/MAPSL/commit/48edfaf66e9f8efbade9fc0db164de5941775e6e)

The original system map describes THINK → PLAN → DO → JUDGE → LEARN, with
context, memory and governance supporting every stage. This comparative
study applies the same discipline used for THINK to the supporting research
method and the rest of that loop. The [master roadmap](../roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md)
owns development priorities. [Original system map](https://github.com/BigCatMellow/Pilot_Projects/blob/main/complete-ai-work-system/SYSTEM_MAP.md)
· [THINK testing protocol](https://github.com/BigCatMellow/Pilot_Projects/blob/main/complete-ai-work-system/evals/THINK-TESTING-PROTOCOL.md)
· [Existing R&D status](2026-11-26-rd-status.md)

[Research](#research--claims-that-can-survive-a-handoff)
· [Context and memory](#context--memory--preserve-authority-and-recover-exact-evidence-under-a-budget)
· [DO](#do--execute-and-recover-without-repeating-uncertain-work)
· [JUDGE](#judge--make-evidence-useful-for-review-and-failure-diagnosis)
· [LEARN](#learn--turn-outcomes-into-scoped-reviewable-guidance)
· [Authority](#governance-and-authority-across-the-work-system)
· [Development routes](#research-conclusions-and-development-routes)

## Evidence and experiment rules

Each area gives a mechanism observed upstream, its fit with the actual MAPSL
entry point, a reproduced local baseline where available, and a proposed
test. Source code and documentation establish what an upstream mechanism
does or claims. Local MAPSL tests establish scoped behavior on this revision.
The experiments below need their own results before any change earns
adoption. This extends the September and November investigations by
pinning specific evidence, local seams and test thresholds.
[Prior research](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/research/README.md)

For each proposed comparison, freeze the baseline commit, candidate change,
input and evaluator digests, acceptable outcomes and rejection cases before
running. Use matched inputs and scope. Review expected outputs independently
and hold back cases used to judge improvements that were tuned. Keep
quality, safety, time, bytes or tokens, and operator intervention visible
where applicable. Track inconclusive and adverse results in the same
evidence. Provider-driven comparisons require their applicable authority.

## RESEARCH — claims that can survive a handoff

**Borrow.** ReAct interleaves a reasoning step with an information-gathering
action, then uses the observation to revise the next decision. For MAPSL, the
transferable unit is the material question, source, observation and decision.
ALCE separately evaluates answer correctness and citation quality. Its scorer
checks whether a claim is actually supported by its cited passages and whether
individual citations contribute. For MAPSL, score authoritative support,
version and anchor as separate facts, including when evidence is missing.
[ReAct paper](https://arxiv.org/abs/2210.03629)
· [ALCE paper](https://aclanthology.org/2023.emnlp-main.398/)
· [ALCE citation scorer](https://github.com/princeton-nlp/ALCE/blob/main/eval.py)

**MAPSL baseline.** The [Research playbook](../../playbook/RESEARCH.md) already
requires precise source locations, retrieval dates, material assumptions and
explicit handling of disagreements. The [evidence integrity evaluator](../../runtime/context_evidence.py)
checks exact version, anchor, temporal scope, authority and abstention on its
[frozen corpus](../evals/context-builder-evidence-integrity-v1.json).
All 21 evaluator tests and 10 frozen-corpus structure tests passed. In a small
calibration, an exact positive card passed, while a wrong source hash, missing
anchor and unsupported hard-negative claim each failed. A check for citation
presence alone counted all four as cited. The calibration used deliberately
constructed cards and establishes the scorer's discrimination on those cases.

**Proposed comparison.** Compare the current research brief with the same
brief plus a source-support check at the decision handoff. Freeze 12 local
questions and source snapshots, balanced across direct facts, conflicting or
superseded records, insufficient support and valid source alternatives.
Independently label the applicable authority, expected claim or abstention,
and acceptable source versions. Use the same sources and time budget.
Advance only if the candidate retains all applicable authority and
stop conditions, passes every unsupported and stale-source control, and
reduces unsupported claims without reducing correct supported answers.
Measure extra source opens and review minutes. Reuse the existing brief and
evidence evaluator for the check.

## CONTEXT / MEMORY — preserve authority and recover exact evidence under a budget

**Research disposition: test a source-linked handoff.** The November scan already proposed validating references before compaction. The code comparison narrows that idea to an optional, disposable handoff projection. The question is whether a fresh worker can recover the same authority, task constraints and evidence with less total context. Preserve the current explicit-first route as the control. [Earlier research](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/research/skills-and-tools/2026-11-04-community-memory-context.md)

| Mechanism inspected | Transfer to MAPSL | Limitation |
| --- | --- | --- |
| **Pi.** Chooses a valid recent-context boundary by estimated tokens and accumulates read/modified paths across compactions from prior entries and tool calls. [Pinned compaction code](https://github.com/earendil-works/pi/blob/ede8bdca0b76dba9e0dc77376318cc3479ba8142/packages/coding-agent/src/core/compaction/compaction.ts#L448) | Test carrying exact source paths and unresolved work separately from narrative. | File-operation history describes what was touched. It cannot prove what was authorized or which fact the bytes support. |
| **SLICE.** Validates cited entry IDs against the available branch prefix, checks literal quotes, and rejects a checkpoint whose source-prefix hash differs. [Pinned note validation](https://github.com/youxi-huang/slice/blob/ede9dd335f59326c2f98c071a56fc4dba0ae9d72/packages/compaction-core/src/notes.ts#L151) | Test a digest and exact anchor on each compact evidence reference, with a verified reopen before relying on it. | Matching a citation proves source identity and availability. A compact packet can still omit a required constraint or misinterpret a source. |
| **LlamaIndex.** Splits retrieved text into numbered chunks and clears the parent node identity and old offsets before constructing citation nodes. [Pinned citation-node code](https://github.com/run-llama/llama_index/blob/40d4f79eb9d8f68430692d0cc156483ca2d7f4f6/llama-index-core/llama_index/core/query_engine/citation_query_engine.py#L322) | Use its chunk-boundary handling as a negative control. A new excerpt needs its own verifiable source-relative anchor. | A numbered citation identifies a prompt unit. MAPSL needs independently verifiable provenance back to the exact source revision. |

**MAPSL baseline.** At `48edfaf`, Context Builder records explicit paths, statuses and SHA-256 for locally resolved files. The delivery renderer carries authority and requirements in the message and separately tracks memory admission and embedding. Its reference text carries paths and statuses. A handoff receipt with exact anchors is a separate research hypothesis. Local context tests ran **104 with five skips and zero failures**. The frozen 16-case retrieval controls reproduced explicit-only **11/16**, exact same-path drift **13/16**, both with full hard-negative abstention and zero forbidden temporal sources. Lexical overlap passed **12/16** overall while failing both hard negatives. The previously measured semantic candidate failed both hard negatives and selected a forbidden temporal source. The handoff experiment below measures context preservation and size. [Builder](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/runtime/context_builder.py) · [Delivery](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/runtime/context_delivery.py) · [Historical semantic result](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/notes/2026-08-17-context-retrieval-semantic.md)

**First frozen comparison.** Pin the [evidence-integrity corpus](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/work/evals/context-builder-evidence-integrity-v1.json) and [retrieval overlay](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/work/evals/context-builder-retrieval-stage2-v1.json) at `48edfaf`. Before running, freeze a coding handoff and a research handoff with independently labeled required facts and allowed reads. A uses current explicit delivery plus its normal evidence reads. B keeps mandatory authority and task boundaries intact and replaces repeated optional evidence with references containing source SHA-256, exact section or symbol, and provenance role. Reuse `project_evidence_card` and its scorer. Give both arms the same resolver and scripted fresh-process reader. Keep expected answers out of both inputs.

Require exact goal, authorized output boundaries, acceptance criteria, current revision, unresolved blocker and reviewer/evidence reference in every applicable case. Changed bytes at the same path, absent source, historical text offered as current, duplicate/misanchored excerpts and guidance presented as authority must fail or be explicitly withheld. Use a deliberately lossy handoff as a control to show the grader detects omitted constraints. Measure initial **plus reopened** UTF-8 bytes, source opens and paired p95 latency. Propose advancement only with zero hard-gate losses, at least 20% median total byte reduction and no more than 25 ms added p95 local latency. If it misses, retain explicit delivery and preserve the counterexample. A passing local comparison supports a bounded candidate review for **6.11, #247 and #248**. It establishes neither generic semantic recall nor agent outcome gains.

## DO · Execute and recover without repeating uncertain work

**Research question.** Can MAPSL block recovery into an incompatible environment and preserve execution progress after interruption using its existing recovery and state components?

### Mechanisms worth carrying forward

| System | Mechanism and MAPSL fit |
| --- | --- |
| Temporal | Completed Activities are represented in workflow history. A crash after an Activity applies an effect and before it reports completion can cause another attempt. Temporal recommends a stable operation key enforced by the receiving service. MAPSL should preserve the distinction between an observed success and uncertainty about an effect. Study receiver-enforced deduplication only for adapters that can prove it. [Activity semantics](https://docs.temporal.io/activity-definition#idempotency) |
| LangGraph | Checkpoints capture graph progress, and a node retry can execute the node again. The installed `1.2.11` retry implementation clears failed-attempt graph writes and reinvokes the node. MAPSL already uses LangGraph to checkpoint route recommendations in a separate SQLite database. Keep route replay available for diagnostics while canonical task ownership and effect decisions continue through the existing state and harness boundaries. [Retry semantics](https://docs.langchain.com/oss/python/langgraph/fault-tolerance#retry-boundaries-and-idempotency) · [Upstream replay test](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/tests/test_time_travel.py) |
| Restate | Durable steps record results and can reuse them from the journal. Retry time and count can be bounded, and stable invocation-derived identifiers support correlation across replays. For MAPSL, borrow the small idea of observable, attributable receipts when the adapter can supply them. Keep journal-engine adoption conditional on a measured recovery gap beyond the current harness. [Durable steps](https://docs.restate.dev/develop/python/durable-steps) |

### MAPSL baseline

At `48edfaf`, flow startup already writes its claim, manifest, and required environment observation in one transaction. The composed recovery path has a run and lease guard, an opt-in quick-validation block, and existing handling for ambiguous resume results. In particular, `UNKNOWN` after possible dispatch suppresses direct fallback within that tick. A later pass re-observes the session before attempting another resume. An old environment observation is displayed as advisory evidence. The supervisor still lacks a decision that compares a fresh replacement environment with the exact run’s requirements before either dispatch path. This is the specific E5 gap. [Startup](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/runtime/flow_start.py) · [Recovery decision](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/runtime/recovery/supervisor.py) · [E5 criteria](https://github.com/BigCatMellow/MAPSL/blob/48edfaf66e9f8efbade9fc0db164de5941775e6e/work/roadmaps/CAPABILITY_CHECKLIST.md#execution-and-reliability)

**Reproduced locally.** All 147 tests passed across flow startup (20), LangGraph routing (3), recovery supervisor (76), ambiguous-effect handling (3), recovery composition (20), and canonical harness guard (25). These are local fixtures at the pinned revision. They establish the baseline for a comparison.

### First comparison · Gate a contracted resume on fresh evidence

- **Control and treatment.** Freeze the current recovery composition and the same fake-clock, disposable workspace, SQLite records, and recording adapter for both arms. In the treatment, add a pre-dispatch E5 decision at the existing recovery boundary. It binds a fresh observation to the manifest’s run and spec and records the decision before either guarded resume or direct fallback.
- **Frozen cases.** Use matched-compatible and incompatible targets, a changed spec, missing or stale evidence for a contracted run, an uncontracted legacy run, an expired claimant with a replacement, and a dispatch with an unknown effect followed by a live-session observation. Freeze expected actions and dispatch counts before testing.
- **Pass conditions.** Require zero calls for incompatible, stale-owner, or unresolved required-evidence cases. Require one authorized dispatch for the compatible control, unchanged legacy behavior, and no extra dispatch after an unknown result when the next pass observes the session live. Each decision needs an exact run, reason, observations, and retry count. A compatibility block cannot spend a transient retry or imply effect success.
- **Cost and stopping rule.** Run 30 paired repetitions, balancing which arm goes first. Record median and p95 recovery time, observations per tick, and extra durable bytes. Start with a provisional p95 budget of baseline plus 25 ms on the compatible local fixture. Stop on any unexpected dispatch, stale ownership, or unverifiable receipt. Share results with E5 and H4/E4 owners before extending validation to the mutation and review call sites.

## JUDGE — make evidence useful for review and failure diagnosis

**Disposition:** Keep MAPSL’s canonical review and outcome stores. Test a read-only view that helps an independent reviewer find the earliest actionable failure and point to the evidence. The view should distinguish a genuine failure, a correctly refused or recovered action, and insufficient evidence.

### Current MAPSL baseline

`record_review` rechecks the claimed reviewer’s independence at verdict, requires complete criterion verification where applicable, and invokes the review-subject hook before approval. The hook can bind the task revision, submission, run and artifact references, and require fresh matching evidence. Completion review and subsequent real-world outcome observations are separate records. [Review path](../../runtime/state/review.py) · [Binding](../../runtime/state/review_binding.py) · [Outcomes](../../runtime/state/outcomes.py)

Run Record v1 explicitly distinguishes task-level reviews and events from evidence checked against the selected run. Harness-operation trajectory is missing and some cross-source lineage remains unknown. The existing regression evaluator can compare per-case and per-property results on a shared frozen corpus with separate configuration references and measurement deltas. This is enough to test whether a better evidence view helps within known coverage. [Run Record](../../runtime/run_record.py) · [Comparator](../../runtime/evaluation/evaluator.py)

At `48edfaf`, 108 targeted local tests passed across flow review, review binding and hardening, Run Record, outcomes, benchmark result evidence and the regression evaluator. They cover stale subjects, wrong-run attribution and honest missing coverage. The proposed comparison below is pending.

### Prior art and transfer

| Mechanism | Evidence and MAPSL fit |
| --- | --- |
| **AgentRx, step-linked checks before interpretation** | Its checker yields a named violation with step index and supporting event, and its judge loads the violation context. The taxonomy includes inconclusive diagnoses. Adapt the evidence shape for a small allowlist of existing MAPSL checks. Keep diagnosis advisory and defer generated checks and model judging. **Code inspected.** [Checker](https://github.com/microsoft/AgentRx/blob/7a18c79708e7671be15124460f4f7296107c2a55/agentrx/invariants/checker.py#L721-L746) · [Judge input](https://github.com/microsoft/AgentRx/blob/7a18c79708e7671be15124460f4f7296107c2a55/agentrx/judge/judge.py#L980-L1015) |
| **Inspect AI, separate rescoring and coverage** | Its scoring pass defaults to copying and appending scores, and carries forward logged-sample coverage so a rescored partial run remains partial. Borrow this distinction in derived comparisons. Keep the observed event set fixed and name any excluded or unknown evidence. Defer importing another evaluation runtime. **Code inspected.** [Rescoring](https://github.com/UKGovernmentBEIS/inspect_ai/blob/a1175d932c8ddd95f5c59ba52f69edd6c079c354/src/inspect_ai/_eval/score.py#L315-L344) · [Coverage](https://github.com/UKGovernmentBEIS/inspect_ai/blob/a1175d932c8ddd95f5c59ba52f69edd6c079c354/src/inspect_ai/_eval/score.py#L407-L425) |
| **GitHub protected branches, independent checks on a changing subject** | GitHub can invalidate stale review approvals and require status checks from an expected app. Use this as a release comparison: MAPSL’s local artifact and continuity checks establish different evidence than the hosting service’s merge controls. Keep both in their existing owners. **Documented control.** [GitHub requirements](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) · [MAPSL protection work](../../docs/CHECKS_AND_BALANCES.md#successor-merge-controls) |

### Proposed first comparison

Freeze 18 sanitized local examples, six for calibration and 12 separately labeled holdouts. Include six evidenced failures such as the wrong run or an uncorrected stale review, three incomplete joins, and three successful controls including a properly refused action and a recovered warning. An independent labeler records the earliest actionable event and evidence reference, or the correct no-failure or insufficient-evidence disposition. The reviewer sees the same Run Record and criterion evidence in both arms. The candidate adds an ordered list of applicable existing check results and exact evidence references. Balance assignment across reviewers and case groups so nobody sees the same case twice. Freeze the rules and labels before scoring.

Record exact localization, supported explanations, correct abstentions, false alarms, and median review time. Keep the candidate only if it localizes at least two more evidenced failures on the 12 holdouts with no lost correct localizations, zero unsupported attributions or false alarms on controls, and median review time at or below baseline. Stop for an evidence join failure, a need for more trace access, or any proposal to change verdict or task state. Revise the input boundary before expanding the study.

## LEARN — turn outcomes into scoped, reviewable guidance

**Question.** Can MAPSL learn from a completed task while keeping later corrections, project scope, and operator decisions authoritative? Start at the existing learning owners L5 / 6.30 and SEC5. L6 configuration identity remains a prerequisite for meaningful comparisons of real agent runs. [Capability evidence](../roadmaps/CAPABILITY_CHECKLIST.md#learning-and-evaluation)

### What other systems do

| Mechanism inspected | Fit and disposition |
| --- | --- |
| **Agent Workflow Memory** uses ground-truth rewards or an automated trajectory assessment to select WebArena examples, groups them by intent template, then induces a workflow for subsequent runs. Its driver calls inference, evaluation, and workflow regeneration in sequence. The authors report relative success gains on WebArena and Mind2Web. That is benchmark evidence for workflow induction. | **Adapt the input discipline.** Compare recurring, evaluated outcomes and group by task family so one repeated pattern cannot dominate. Keep generated procedures as scoped candidate guidance. Directly replacing the next agent's workflow would skip MAPSL's decision checks. [Pinned induction code](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py#L102-L161) · [Authors' paper](https://arxiv.org/abs/2409.07429) |
| **GEPA** uses diagnostic feedback to propose and score variants. Its optimizer scores the original and selected candidate on an optional held-out set outside the search call budget. The code therefore separates selection from final measurement, and shows why final evaluation needs its own explicit budget. | **Adapt the protocol.** Freeze inputs and evaluator before drafting a change, keep held-out cases inaccessible during selection, and record proposal and evaluation cost separately. A winning result becomes evidence for JUDGE. [Pinned optimizer](https://github.com/gepa-ai/gepa/blob/ce5b0d6e3d6af6c6dbec6de2c54536bbb961d309/src/gepa/optimize_anything.py#L485-L567) · [Authors' paper](https://arxiv.org/abs/2507.19457) |
| **LangMem** reads prior memories in a namespace, extracts structured changes, optionally applies consolidation phases, then writes changed and removed records. Its reflection mechanism can move extraction off the foreground path. | **Adapt separation of work.** Extract candidate lessons separately and keep existing append-only decisions as the record of promotion and retirement. A background writer or second store is deferred until collection cost is demonstrated. [Pinned persistence code](https://github.com/langchain-ai/langmem/blob/4beb9c36a40953f09357e5b2dd62ecc726f22d13/src/langmem/knowledge/extraction.py#L1025-L1137) · [Reflection documentation](https://github.com/langchain-ai/langmem/blob/4beb9c36a40953f09357e5b2dd62ecc726f22d13/docs/docs/background_quickstart.md) |

### Verified MAPSL baseline

At `48edfaf`, **124 focused tests passed** across outcomes, lesson candidate construction and storage, learning schema and projection, Context Builder, memory trust, and regression evaluation. The candidate builder binds exact canonical outcome, task revision and optional run references. Construction checks whether the source outcome has since been superseded. Promotion stores an append-only decision with a supplied actor label. Operator identity binding is still a separate prerequisite for exposing a normal promotion route. [Candidate builder](../../runtime/outcome_lesson_candidate.py) · [Storage and decisions](../../runtime/state/operational_learning_storage.py) · [Context projection](../../runtime/context_builder.py)

A disposable SQLite check exposed a later freshness gap. An outcome-derived candidate stayed invisible until promotion. When a correction superseded the source outcome between creation and promotion, promotion still succeeded and Context Builder loaded the lesson as `GUIDANCE_ONLY`. Explicit retirement removed it from later context. This demonstrates stale guidance after corrected evidence. It measures neither downstream task quality nor authenticated operator behavior.

### Proposed comparison — evidence freshness

Freeze eight development fixtures and sixteen held-out fixtures by task family before proposing a change. Use eight eligible held-out cases and eight hard negatives covering corrections before and after promotion, scope mismatch, pending/expired/retired guidance, missing provenance, and preserved task authority. Compare current promotion and admission with one addition: recheck canonical source freshness at both points for outcome-derived lessons. Identical fixture operator decisions and phase timestamps isolate the comparison.

Count correctly admitted, withheld, or refused cases, record provenance and refusal reasons, and measure elapsed time and added database reads. Require 16/16 held-out decisions, all previously correct positives retained, zero authority changes, and closure of both supersession cases. Cap the first pass at one candidate revision, 48 fixture evaluations across development and held-out pairs, and zero provider calls. Stop on any authority regression, holdout leak, or budget overrun. Record the result for JUDGE. Evaluate real outcome improvements only after binding the effective harness configuration and establishing the operator path.

### Local comparison result

The offline comparator reruns the existing outcome candidate builder and
checks that its source references still match the saved lesson. It checks
before the normal promotion call and filters active lessons before the normal
Context Builder projection. It leaves production entry points untouched.
The comparator and [development fixtures](../evals/lesson-source-freshness-dev-v1.json)
were frozen at comparator blob `356f5613d9ff0f98451ff6bb34598ecf28a8ff9e`
before importing the independently authored
[holdout](../evals/lesson-source-freshness-holdout-v1.json).

| Cases scored on both promotion and admission | Current path | Recheck |
| --- | ---: | ---: |
| Development | 5/8 | 8/8 |
| Held-out valid lessons | 8/8 | 8/8 |
| Held-out hard negatives | 4/8 | 8/8 |
| Held-out total | 12/16 | 16/16 |

An explicit correction before promotion refused the fixture decision.
A correction after promotion withheld the guidance and preserved the existing
decision. Missing outcome and missing canonical binding each refused promotion.
The current path admitted guidance in all four cases. An unrelated observation
on the same task still allowed guidance. Scope mismatch, pending promotion,
expiry and retirement remained effective. For all 48 evaluations, task state
and authority were unchanged, stored source references were preserved, and
each loaded lesson stayed `GUIDANCE_ONLY`. Every positive admission included
its original promotion decision reference. No provider was called.

| Held-out timing sample | Pairs | Current median | Recheck median | Added SELECTs total / maximum per pair |
| --- | ---: | ---: | ---: | ---: |
| Promotion attempt | 15 | 1.17 ms | 5.32 ms | 237 / 19 |
| Context admission | 16 | 3.71 ms | 6.87 ms | 161 / 17 |

Timing includes the observed call and SQLite tracing and excludes fixture
setup. Cases alternate arm order. The extra SELECTs are net relative to the
matched call. This one local run covers one lesson per fixture and gives no
production latency or concurrency estimate. Reusing the full builder loads
the outcome history and repeats source lookups. L5 / 6.30 retain a production
finish test for promotion in the same transaction as the freshness check and
canonical admission that reads the decision and freshness together. Include a
concurrent correction test and verify bounded read cost on a backlog of
lessons and outcomes. SEC5 still owns the authenticated operator route.

Replay either split from the repository root with Python 3. The
[comparator](../evals/lesson-source-freshness.py) emits each case's decisions,
reasons and costs as JSON.

```bash
PYTHONPATH=. python3 work/evals/lesson-source-freshness.py dev
```

```bash
PYTHONPATH=. python3 work/evals/lesson-source-freshness.py holdout
```

## Governance and authority across the work system

**Questions.** Can a reviewer tell which check permitted, refused or held an action, what evidence it used, and whether that evidence still applies? How much would clearer evidence cost? This keeps the existing MAPSL authority model as the baseline.

### What other systems make explicit

| System | Evidence and MAPSL disposition |
| --- | --- |
| Open Policy Agent | Its documented runner supports named, data-driven policy cases and reports evaluated and unevaluated lines. Decision logs can correlate a decision ID with the policy bundle revision and mask sensitive fields before export. **Adapt the testing pattern.** Count covered action/decision pairs in the existing Python guards and try a compact local record with allowlisted fields. Line coverage alone cannot establish that a supported action actually reached its guard. [Policy testing](https://www.openpolicyagent.org/docs/policy-testing) · [Decision log fields and masking](https://www.openpolicyagent.org/docs/management-decision-logs) |
| Cedar | Authorization evaluates an explicit principal, action, resource and context. A satisfied forbid overrides a permit, and the response exposes determining policy IDs and evaluation errors. Cedar skips an erroneous individual policy. **Adapt the explicit bindings and diagnostics.** Keep MAPSL’s existing fail-closed behavior for required evidence. Treat missing and invalid evidence as separate cases. [Authorization semantics](https://docs.cedarpolicy.com/auth/authorization.html) |
| GitHub | Rulesets can discard stale approvals when the approved diff changes. The synchronous merge API can enforce a supplied expected head SHA and returns a conflict when it differs. **Keep the revision-binding pattern.** A hosted approval establishes the account and reviewed commit. Attesting to the actual model or session requires evidence from a trusted producer. [Ruleset review semantics](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-a-pull-request-before-merging) · [Merge API contract](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request) |

### What MAPSL already proves

At candidate `48edfaf`, `CanonicalRunGuard` checks canonical task, run and session evidence before protected lifecycle operations. `DestructiveExternalActionGuard` checks an explicit action classification against the task envelope and required human reauthorization. Its current service-level firing evidence covers session stop. The research question is which supported call sites actually reach required checks. Separately, review-subject binding and the OPCMD candidate connect approval to revision. The latter checks an authenticated GitHub reviewer on the live SHA and still depends on the authorized successor bootstrap. A trusted producer for reviewer execution identity remains an open evidence requirement. [Runtime guards](../../runtime/policy/) · [Successor merge controls](../../docs/CHECKS_AND_BALANCES.md#successor-merge-controls) · [Attestation finding](../../migration/work-evidence.md#open-obligations-and-historical-proofs)

**Reproduced locally.** 89 tests passed across canonical binding (25), consequential-action classification (20), authority baseline and hook context (9), review-subject binding (16), review-evidence checking (13), and six mocked GitHub approval cases. These are local fixtures. Live protection configuration and provider identity require their own evidence.

### Proposed comparison

Use the existing fake stop adapter and read-only harness guards on frozen synthetic records. Compare **A**, current decision output, with **B**, the same decisions plus a bounded record of fired guard, reason code, task/run/revision references and evidence status. Keep the authenticated-approval cases as separate controls. Label ordinary authorized and reauthorized positives plus missing or invalid classification, out-of-envelope action, missing reauthorization, stale revision, expired lease, and missing, stale or mismatched approval. Count action/decision coverage independently of documentation.

Freeze cases and labels before scoring. Require zero false permits, zero lost legitimate permits, zero adapter calls for refusals, and zero raw payload markers in evidence. Require a blinded reader to recover the correct governing check and bound revision on at least 90% of eligible fixtures and more often than with A. Report median and p95 monotonic wall time over 30 paired repetitions and encoded bytes per decision. Proposed ceilings are 1 ms additional p95 and 512 bytes per decision in the local fixture. Stop on any hard failure or if the record provides no diagnostic gain. Route results to SEC3/6.24 and 6.18. The comparison carries zero provider calls or repository setting changes.

## Research conclusions and development routes

| Route | First question to test | Existing owner |
| --- | --- | --- |
| Execution and authority | Does a contracted run refuse an incompatible resume before dispatch, with a reviewable reason? | E5 and SEC3/6.24 |
| Research and context | Does a compact handoff preserve every material claim, current source and authority boundary after a fresh session? | 6.11, #247 and #248 |
| Judgment | Can an independent reviewer find the earliest actionable failure more accurately using the same captured evidence? | Review evidence and L2/L3 |
| Learning | The local recheck passed. Can the canonical paths preserve the same decisions across concurrent corrections and bound the read cost? | L5 / 6.30 and SEC5 |

The local startup-to-review smoke also passed on the common baseline. These
separate test groups overlap, so their counts should be read by area. Keep
the [existing roadmap order](../roadmaps/00-MASTER-MAPS-CAPABILITY-ROADMAP.md#delivery-order).
This report supplies comparison criteria for those stages. The broader
benchmark and any provider-driven proof retain the prerequisites recorded
in the [R&D status](2026-11-26-rd-status.md).
