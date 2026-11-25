# Practical migration checks

Candidate tested: `6222aef60cd9913ae1b9783912b2e4fd2d906754`, Linux x86-64 with CPython 3.12.14. Two independent local Git clones of the same commit separated installation state from the method-only checkout. The original repository, live worker sessions and external projects were outside this test.

| Path exercised | Observed result |
| --- | --- |
| Method only | An assigned worker followed the operating contract and bounded migration scope to answer a concrete onboarding question: could a new user follow the recovery instructions? The documented worker flag did not appear in the CLI help and the purported local legacy extraction was absent. The worker corrected the setup guide and verified its relative links and the corrected command against the CLI. The documentation checkout contained no runtime database, project environment or HCOM directory. |
| Orchestration | The migration owner assigned a distinct checkout, write boundary, source revision and evidence requirement to the installation worker. A separate routing worker independently identified the broken extraction reference. The installation worker owned that file and supplied the corrected guide and test results to the parent. No HCOM install, live message transport or provider-specific worker launcher was required. Parent review and integrated acceptance are separate. |
| Runtime install | Installer preview printed planned commands, with no `.venv`, `.maps`, `.hcom` or Git worktree changes. `--apply --run-smoke` installed all five exact requirements into a new project environment. `pip check` found no broken requirements. SQLite reported foreign keys on, WAL, 5,000 ms busy timeout and a completed disposable task. LangGraph selected `wait_or_reconcile` using a separate checkpoint database. The HCOM executable was absent. |
| Portable target | A new temporary Git project passed read-only preflight. Preflight plus initialization preview left every pre-existing file byte-identical. Apply created all six expected entries (including directories). After editing the target roadmap, a second apply created zero entries, preserved every file byte-for-byte and preflight reported initialized. A same-root apply was refused with exit 2. |
| Authority and context | A new CLI process per step used one disposable task DB. Promotion rejected an incomplete contract, then separately rejected an externally consequential envelope missing its required reauthorization flag. A bounded local contract promoted. `flow start` bound the actual checkout revision, worktree and README content hash, which was compared to an independent SHA-256 digest. No provider launched. |
| Continuation and review | Worker A held a four-second lease. Worker B's premature claim returned `LEASE_ACTIVE`. `flow handoff` recorded A→B and stopped before transfer. After actual expiry, a fresh CLI process recovered B's claim on attempt 2. B submitted. The task store refused review by B (`SELF_REVIEW_FORBIDDEN`) and A (`CONTINUITY_REVIEW_FORBIDDEN`). An unrelated fixture identity recorded a verdict and the next fresh process read `DONE`. These test identities exercise enforcement and do not supply independent approval of this migration. |
| Failure handling and optional adapters | The recovery CLI refused canonical enforcement without its required checkout argument. Focused regressions exercised production trigger wiring, canonical-run composition, uncertain external effects, destructive-action denial, immutable review subject binding, context evidence and HCOM adapter handling with test transports. A live HCOM resume, provider session and paid/external pilot were outside this run. |

## Reproduction

In a new Linux checkout, run the installer preview before apply.

```bash
bash scripts/install_maps.sh
```

```bash
bash scripts/install_maps.sh --apply --run-smoke
```

```bash
.venv/bin/python -m pip check
```

For portable checks, use the preflight, preview and two apply calls from [Fresh Clone Setup](../docs/FRESH_INSTALL.md) against a disposable sibling Git root. Compare its files before/after preview and after changing its roadmap between apply calls.

The runtime and portable regression modules below reproduced 155 passing cases. Additional authority, evidence and adapter modules reproduced 68 passes. The two documentation route modules reproduced 27 passes after the guide corrections.

| Group | `python -m unittest` modules (under `tests.`) |
| --- | --- |
| Runtime and portability | `test_portable_target_init`, `test_portable_target_preflight`, `test_flow_start`, `test_flow_handoff`, `test_review_subject_binding`, `test_runtime_review_hardening`, `test_recovery_composition_root`, `test_recovery_external_effect_ambiguity`, `test_recovery_production_trigger`, `test_smoke_install` |
| Authority, context and adapters | `test_destructive_external_action_guard`, `test_context_evidence_hardening`, `test_hcom_adapter`, `test_harness_hcom_adapter` |
| Documentation | `test_documentation_sprawl`, `test_digital_fungus_routes` |

Use [runtime CLI flows](../runtime/README.md) to inspect the individual commands. The full regression suite and independent integrated review are gates on the final candidate. Windows and macOS execution were not measured here. The Windows instructions use pinned project requirements, and the portable target apply implementation requires POSIX directory operations.
