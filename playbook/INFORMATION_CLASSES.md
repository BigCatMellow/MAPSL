# Information Classes

MAPS distinguishes seven kinds of information so authority, procedure, and
context never blur together. This is a naming/vocabulary reference, not a new
mechanism — it names distinctions the runtime already makes (see "Where this
shows up" below). The
[pinned source design](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/roadmaps/agent-harness-capabilities/02-procedural-knowledge-and-skills.md)
describes the original classification in section 2.

This is a different axis from [INFORMATION_LIFECYCLE.md](INFORMATION_LIFECYCLE.md):
lifecycle classifies information by *temporal state* (active/retired/archived)
regardless of kind. This document classifies information by *kind*
(authority/fact/Skill/flow/tool/example) regardless of how old it is. A single
piece of information has a class from this doc and, separately, a lifecycle
state from that one.

## 1. Authority / invariant

Example:

> Production deployment requires operator approval.

Lives in authoritative policy/instructions, not a Skill. It constrains what
is permitted regardless of task, and an agent cannot load its way out of it.

## 2. Task context

Example:

> TASK-0042 changes runtime policy evaluation.

Task-specific; loaded through Context Builder/task state, not authority and
not a reusable procedure. It applies to one task and stops mattering when
that task closes.

## 3. Fact / knowledge

Example:

> Service X listens on port 8443.

May be useful context. Not a procedure or authority by default — a fact can
be true and still irrelevant to the task at hand, or wrong without breaking
any rule.

## 4. Skill / procedure

Example:

> How to perform a safe PostgreSQL schema migration.

A reusable method loaded when applicable, not always-on. It tells an agent
*how* to do something; it does not grant permission to do it.

## 5. Flow

Example:

> Prepare review -> run checks -> create submission -> route reviewer.

A stable, deterministic sequence executed mechanically once it is mature
enough to trust without per-step judgment. A flow is a Skill that has
graduated to routine execution, not a new kind of authority.

## 6. Tool / capability

Example:

> PostgreSQL query execution.

A concrete ability, distinct from the instructions for using it safely (that
guidance is a Skill, not the tool itself). A tool can be available and still
misused if the Skill for using it correctly is not loaded or not followed.

## 7. Example / demonstration

A compact, validated exemplar showing a difficult procedure in action.
Examples are evidence/support for a Skill, not always-on prompt content —
they illustrate a Skill, they do not replace it or grant authority on their
own.

## Where this shows up today

- **Authority and task context are already split in Context Builder.**
  `runtime/context_builder.py::build_context_plan` returns separate
  `authority` (root [`AGENTS.md`](../AGENTS.md), class 1) and `required` (task `inputs`/
  `sources`, class 2) lists, plus a `guidance` list of attributed
  `GUIDANCE_ONLY` operational-lesson evidence (class 3 — fact/knowledge
  surfaced as advisory context, never merged into authority or boundaries).
  None of these three lists are interchangeable, and the plan's `boundaries`
  field (decision authority, non-goals, stop conditions) stays under class 1,
  never class 2 or 3.
- **Skills are loaded procedures, not authority.** `runtime/skills/format.py`
  and `runtime/skills/catalog.py` track each reusable procedure's provenance
  and content identity. The [startup flow](../runtime/flow_start.py) supplies
  the catalog to Context Builder. Eligible matches include a hash-verified
  procedure body and a resource manifest. A downstream caller can load an
  individual declared resource on demand. Task authority stays with the
  operating contract and approved task.
- **Flows compose guarded operations.** The [runtime CLI](../runtime/cli.py)
  exposes flow commands for start, handoff, review and release checks.
  They compose class-5 operations with explicit stopping points, while
  [Task Lifecycle](TASK_LIFECYCLE.md) supplies the procedure for their use.
- **Tools stay distinct from the guidance for using them.** `runtime/harness/`
  (adapter operations) and `runtime/helpers/` (Ollama/Aider lanes) are class 6
  capabilities; the safe-use guidance around them lives separately, as class
  4/1 material, not baked into the tool call itself.
- **Examples support Skills, they are not separately tracked yet.** No
  distinct example/demonstration store exists in the runtime today; when a
  Skill includes one, it is part of that Skill's own content, not a
  standalone class-7 record.
