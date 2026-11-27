# Control-plane operation

Start with [Fresh Clone Setup](FRESH_INSTALL.md) for the preview, pinned dependency installation, smoke, manual Windows setup and portable target convention. Use this guide when debugging state or opting into session recovery. The [control-plane playbook](../playbook/CONTROL_PLANE.md) defines responsibilities.

## Local state

| Path | Purpose |
| --- | --- |
| `.maps/state/maps.db` | Task contracts, claims, reviews and evidence. Keep the database on a local filesystem for multi-process WAL. |
| `.maps/state/langgraph-checkpoints.db` | Routing checkpoints. The router recommends work and the task store validates transitions. |
| `.maps/state/recovery.json` | Recovery incidents and retry history. |
| `.hcom/` | Optional transport and session state. Set `HCOM_DIR` to this project's directory when using hcom. |

After installing the runtime, activate its virtual environment or use its Python executable. Run the following from the checkout.

```bash
python -m runtime.cli --help
```

```bash
python -m runtime.cli status
```

The [runtime guide](../runtime/README.md) covers task start, context binding, continuity and review. A fresh clone has no task history until the operator creates local task state. For a disposable lifecycle check use the smoke in the installation guide.

## Optional transport and recovery

The installer can install HCOM separately when explicitly requested. Its messages and session metadata provide transport evidence. The task store retains ownership and approval. Known-session restart needs a configured transport. Normal method use, durable SQLite claims and independent review run without HCOM, WezTerm, a model provider or paid worker execution.

### Canonical enforcement: remediating a denied resume

Once `python -m runtime.cli recovery-tick --enforce-canonical-run --harness-project-id <P>
--repo-root <PATH>` is opted into, a `CANONICAL_RUN` Hook can deny a resume
outright. `tick()` then parks the incident in a distinct `denied` state (it
does **not** consume a transient retry attempt, and it does **not** terminate
as `retry_budget_exhausted`); `last_error` carries the deny reason and the
incident stays resumable on a flat probe interval until it either clears or
hits its own consecutive-denial ceiling (`failed` /
`canonical_denial_persistent`).

The dominant first-exposure denial is `LEASE_EXPIRED`: a silently-stopped
session's claim lease has usually already lapsed.

**`python -m runtime.cli heartbeat` cannot fix this.** `heartbeat` itself refuses an
already-expired lease (`LEASE_EXPIRED`) and requires the caller to still be the
live claimant — neither holds for the recovery case.

The workflow that works is claim-recovery of the expired `ACTIVE` claim, under
the run manifest's **original** worker id:

```text
python -m runtime.cli claim TASK-0001 worker-a --lease-seconds 900
```

- Substitute the task and original worker in the example, then rerun the same bounded recovery tick. The worker ID **must** be the manifest's recorded worker.
  `CanonicalRunGuard` checks `task.claimed_by == worker_id` and the run-lineage
  checks compare the session's recorded worker against the current claimant —
  recovering under a *different* worker clears `LEASE_EXPIRED` only to trip
  `NOT_CLAIM_OWNER` / `RUN_WORKER_MISMATCH` on the same pass.
- `claim_task`'s recovery path bumps the task-truth `attempt` (counted against
  `max_attempts`), which is distinct from the recovery incident's retry
  counter. A task already at `attempt >= max_attempts` returns `ATTEMPT_LIMIT`
  and cannot be recovered this way — that incident is genuinely done and should
  be closed, not resumed.
- Claim-recovery does **not** change the run manifest's `task_revision`:
  `compute_task_revision()`'s input set (`runtime/state/integrity.py`
  `_task_definition_conn`) is the `tasks` row's definition columns plus the
  task child tables, policy, and environment — none of `status`, `claimed_by`,
  `lease_expires_at`, `heartbeat_at`, `attempt`, `updated_at` that recovery
  mutates. So `recover + re-tick` is a complete workflow; no "start a fresh
  run" step is required for a revision-stable task.

### Opt-in resume-validation gate

By default `python -m runtime.cli recovery-tick --repo-root <checkout>` runs the `quick`
validation tier against each about-to-be-resumed incident **advisorily**: the
result is recorded on the action dict (`resume_validation`) and read by
nothing — a failed tier never blocks, delays, or fails a resume.

Add `--enforce-validation` (requires `--repo-root`) to turn that observation
into a gate:

```text
python -m runtime.cli recovery-tick --repo-root <checkout> --enforce-validation --binding W=S
```

With the flag on, an incident whose pre-resume check concretely fails
(`{"attempted": true, "passed": false}`) is parked in a distinct
`blocked_validation` state **before** any resume call — no harness/hcom
resume is attempted, the transient `attempt` retry budget is untouched, and
the incident is rescheduled on the flat `silent_stop_probe_delay_seconds`
probe interval. An `{"attempted": false, ...}` result (missing / ambiguous /
unparseable spec, budget-skipped, validator error) is **not** a failure and
never blocks. After three consecutive blocks with no intervening non-block
outcome the incident becomes `failed` / `validation_block_persistent`
(distinct from `retry_budget_exhausted`); a later passing tier resets the
streak. Default off; never enabled on the `claim` piggyback pass. This
gate is independent of `--enforce-canonical-run` and composes with it
(validation gate first, then the canonical guard on the harness path).

## Source design and troubleshooting

The original [installation and porting guide](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/docs/CONTROL_PLANE_SETUP.md) preserves the subsystem implementation checklist, recovery design, helper boundaries and original install rationale. Historical paths under `migration/legacy-runtime-source/` live in the [pinned source extraction](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/migration/LEGACY_RUNTIME_EXTRACTION.md). This checkout installs and imports from `runtime/`.

If a claim fails, inspect `python -m runtime.cli show TASK-0001` with the actual task ID. For dependency problems, run `python -m pip check` inside the virtual environment. For an optional transport issue, check the project-specific `HCOM_DIR` and `hcom status` before changing session state.
