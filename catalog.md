# Skill catalog

Use this catalog to select a workflow; read the selected skill's `SKILL.md` before execution. Paths below are relative to this library, while output paths are relative to the user's target project. No skill depends on another being installed.

| Skill / entry point | Select when | Inputs | Outputs and handoff | Skip when |
| --- | --- | --- | --- | --- |
| [product-requirements-interview](skills/product-requirements-interview/SKILL.md) | Defining or revising a product's users, value, or MVP scope | Idea, brief, existing discovery, constraints | PRD; hand off its location, status, and open constraints to technical or visual design | Implementing a feature whose requirements are already clear |
| [technical-design-interview](skills/technical-design-interview/SKILL.md) | Planning or revising system architecture | PRD or equivalent concrete requirements; existing code/stack | Technical design; hand off requirements reference, decisions, unresolved issues, and implementation prerequisites | Routine debugging or implementation within established architecture |
| [design-system-workshop](skills/design-system-workshop/SKILL.md) | Creating or deliberately revising a visual system | Product/audience context, preferences, existing brand/tokens | Style guide; when requested, integrated tokens and preview, plus verification status | Creating a screen that should simply use an existing system |
| [git-workflow](skills/git-workflow/SKILL.md) | Branch/sync, commit/PR preparation, conflicts, recovery | Target Git policy, branch state, operation | Policy-aware plan or authorized action; branch/base/checks | File edits without Git operations |
| [beads-workflow](skills/beads-workflow/SKILL.md) | Durable task/blocker/legacy-ID/handoff work in Beads | Existing bd project, issue, repo policy | Native IDs, accurate state and next steps | Ephemeral lists or another tracker |
| [spec-review](skills/spec-review/SKILL.md) | Read-only patch/spec review | Diff, requirements, project rules, tests | Evidence-ranked findings and verdict | Implementation-only request |
| [regression-testing](skills/regression-testing/SKILL.md) | Regression tests and behavior verification | Spec, implementation, tooling, prerequisites | Executed tests, exact results, failure handoff | Prose edits or read-only-review-only request |

## Compose only when useful

For a new product, begin with requirements. Technical design and visual design consume that context and can follow in either order. Skip completed stages, read their existing outputs, and ask only about consequential gaps. A complete PRD is useful but not mandatory if equivalent requirements are supplied. The design workshop can run directly from a visual brief.

Carry forward artifact paths, draft/accepted status, user constraints, decisions, and open questions. Do not silently restart interviews or treat a proposal as approved. Resolve contradictions with the user rather than overwriting an earlier decision.

## Implementation handoffs

Use beads-workflow for shared Beads state when the target already uses it; it does not adopt a tracker. Use git-workflow for repository operations. Pass requirements and changed files to regression-testing, then spec-review with the test results. These are task workflows, not a requirement to spawn agents. Keep tracker completion aligned with the target's actual gate (which may include merge).

## Opinionated verification defaults

spec-review defaults to diagnosis-only handoff, treats documented visual rules as acceptance criteria, and excludes unsupported cosmetic nits. regression-testing defaults to checking validation, response shape, status, and error behavior for changed endpoints; externally defined expected values need a cited oracle or an explicit gap report. These are source-mapped in each package’s provenance. See [rename notes](RENAMES.md) for identifier changes.

## Execution contract

Read the [canonical shared contract](shared/execution-contract.md). Its generated copy is packaged under each skill’s references for standalone installation. The contract holds shared scope/authorization and draft rules; individual entry points hold task-specific decisions.

Default choices apply when no existing project convention or explicit user choice overrides them. The technical-design default is FastAPI/async SQLAlchemy/Postgres/Alembic with React/TypeScript. Requirements default to a small MVP; the workshop defaults to restrained tokens and capped emphasis. Git branch/release policy is always discovered from the target.

For human setup and both hosts’ invocation examples, see [README.md](README.md).
