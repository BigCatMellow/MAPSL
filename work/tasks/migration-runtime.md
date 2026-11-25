# Migration runtime candidate

Parent: [authorized migration](../../migration/PLAN.md).
Owner: migration orchestration operator. Authority: reversible changes only in
MAPSL candidate branches; no source writes, external project execution, spending,
credential or control bypass. Outcome: preserve all 124 source runtime files,
114 test files and 18 tools/scripts with exact hashes and modes, then reconcile
repository-specific links and guards without changing working runtime behavior.

Proof: [initial integrated run](https://github.com/BigCatMellow/MAPSL/actions/runs/45417993224)
passed compile, fatal lint, dependency consistency, security static analysis,
inventory coverage and disposable smoke. 1,502 tests ran; 5 failures and 7 errors
were navigation/authority workflow gaps; 5 skipped. Correct those gaps and run
the full suite again. Independent review required before accepted integration.
Stop this branch only at verification/review or explicit dependency boundary;
continue independent semantic reconciliation. No external target touched.

## Integration and verification

The same owner now reconciles the complete source tree, branch history and identified obligations into the candidate. Work is bounded to the approved migration plan. Dispositions, owner/trigger routing, fresh Linux operation, original regressions and an independent review of the integrated tree are required. Use [current state](../../state/CURRENT.md) and [reconciliation](../../migration/reconciliation.md#remaining-acceptance-gates) for the live continuation. Missing primary records and the first trusted merge require separate resolution; filing evidence does not release the candidate.
