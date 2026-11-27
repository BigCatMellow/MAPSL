# Durable handoff register

Successor register: no completed handoff asserted. The [source register](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/handoffs/README.md)
retains all historical receipts. Outstanding external/open and acknowledged
records are tracked in [migration reconciliation](../../migration/reconciliation.md).

New forward-looking durable handoffs require ID, status (OPEN, ACKNOWLEDGED,
CONTINUED, CLOSED or SUPERSEDED), review receipt, and a durable continuation
pointer. A handoff does not transfer authority or replace live GitHub/task state.
Record the receipt in the handoff and this register; reconcile at meaningful arcs.

| ID | Status | Path | Reviewed | Continued at |
| --- | --- | --- | --- | --- |

Use [Current State](../../state/CURRENT.md) for current continuation. Do not create
a new handoff solely because a task checkpoint exists.
