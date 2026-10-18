# skills-to-pay-the-bills

Collection of skills for Agentic dev I've built over time. Also a great beat from the Beastie Boys.

[Listen to “Skills to Pay the Bills”](https://youtu.be/cJgCfP98TVQ?si=sL_yQVprLwIkaywQ).

Opinionated, reusable workflows for planning, implementing, and checking software. Built for humans to understand and coding agents to execute. Each skill works independently; combine only the stages your task needs.

## So What’cha Want? Pick a skill

| Skill | Use it for | Typical result |
| --- | --- | --- |
| [Product requirements interview](skills/product-requirements-interview/SKILL.md) | Clarifying users, the core journey, and MVP scope | `docs/prd/prd.md` |
| [Technical design interview](skills/technical-design-interview/SKILL.md) | Turning requirements into a practical architecture | `docs/technical/technical-design.md` |
| [Design system workshop](skills/design-system-workshop/SKILL.md) | Defining visual tokens and component rules | `docs/design/style-guide.md`, plus UI integration when requested |
| [Git workflow](skills/git-workflow/SKILL.md) | Branch setup/sync, commit/PR preparation, conflicts, recovery | Policy-grounded Git plan or authorized operation |
| [Beads workflow](skills/beads-workflow/SKILL.md) | Durable Beads work, blockers, legacy IDs, handoffs | Accurate native issue state or command plan |
| [Spec review](skills/spec-review/SKILL.md) | Read-only review against requirements and project rules | Findings with evidence, severity, and location |
| [Regression testing](skills/regression-testing/SKILL.md) | Behavior-focused regression tests and verification | Executed tests and reproducible failure reports |
| [Review findings triage](skills/review-findings-triage/SKILL.md) | Resolving existing automated/adversarial findings | Owner decision table, tracked dispositions, verified gate/report or explicit blockers |
| [Session start and close](skills/session-start-and-close/SKILL.md) | Orientation, interrupted-work recovery, and durable handoffs | Brief state/next-step report and tracker-backed follow-ups |
| [Local test handoff](skills/local-test-handoff/SKILL.md) | Making feature-branch web work testable on local devices | Verified running revision, device URL, dev access, pass/fail checklist |
| [Prose edit](skills/prose-edit/SKILL.md) | Tightening existing copy in the author’s voice | Edited text with facts preserved |
| [Diagnose First](skills/diagnose-first/SKILL.md) | Confirm and explain a reported problem before repair | Evidence-backed diagnosis and safe comparison plan |
| [Docs Audit](skills/docs-audit/SKILL.md) | Compare documentation claims and coverage with actual behavior | Evidence-linked mismatches, missing docs, and requested diagrams |
| [Agent Handoff Prompt](skills/agent-handoff-prompt/SKILL.md) | Write self-contained agent briefs or assess another agent’s output | Copy-pastable work order or evidence-backed verdict and fixes |

The library now includes fourteen skills; [rename notes](RENAMES.md) record identifier changes. The [source review](inventory/README.md) and [extraction ledger](inventory/extractions.md) explain which repeated procedures were extracted and what stays project-specific. Discovery material is not an instruction set to load into an agent.

## Two prompts to get started

Copy either prompt into your coding agent:

- [Improve an existing project](prompts/existing-project.md): inspect the current workflow, install useful skills, and add concise project instructions while preserving established choices.
- [Start a new project](prompts/new-project.md): shape a small MVP, design around the preferred stack, define the visual system where needed, and agree on a first implementation slice.

Both prompts work from the library URL or a local checkout and support project-local setup. The new-project prompt begins with planning; implementation follows your approval.

## Get It Together: use the whole workflow

For a new product, run requirements → technical design → design system. Technical and visual design can happen in either order once the product context is clear. Bring each output into the next step; skip stages you already have.

Give your coding agent this prompt, replacing the paths with your actual checkout and target project:

```text
Use the library at /path/to/skills-to-pay-the-bills for my project at
/path/to/my-app. Read its catalog.md and select the relevant skills.
Start with product-requirements-interview. Work through requirements,
technical design, and a design-system guide in stages, using each draft
as context for the next. Ask focused questions about unresolved decisions.
Save drafts in my project's docs directory. Do not implement the app yet.
```

For implementation work, use session-start-and-close to orient or resume when needed, beads-workflow when the project uses Beads, git-workflow for branch/policy preparation, then regression-testing and spec-review for verification. Use review-findings-triage for findings already produced by a review tool, and local-test-handoff for the owner’s pre-merge device checks. Close with a durable handoff. prose-edit is independent of that development flow. There is no mandatory multi-agent pipeline. Handoffs carry artifact/native issue IDs, decisions, checks, and unresolved work.

Defaults are deliberate: greenfield architecture starts with FastAPI/Postgres and React/TypeScript; product scope starts small; visual design starts with a restrained palette/type pair and capped emphasis. Existing project choices and explicit overrides win. Say “keep Django” or “use our existing brand” and the skills adapt. Details live in each skill’s `references/procedure.md`.

## Just a Test: try one without installing

Clone or download this repo, open your own project in an agent that can read local files, and point it to one skill:

```text
Read /path/to/skills-to-pay-the-bills/skills/product-requirements-interview/SKILL.md
and use it to interview me about a neighborhood tool-sharing app.
Write the PRD in my project at /path/to/my-app/docs/prd/prd.md.
```

No special command, account integration, or other skill is required. If local file access is unavailable, paste the chosen `SKILL.md` **and its linked execution contract and procedure** as task context. You can also follow the procedure yourself as a checklist.

## Intergalactic portability

Copy the **complete selected folder** from `skills/`, including `references/`, `PROVENANCE.md`, and `LICENSE`. The Markdown workflow is shared; invocation and discovery are host-specific.

| Host | Project install | Personal install | Invoke after discovery |
| --- | --- | --- | --- |
| Codex | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` | `Use $git-workflow to prepare this branch.` |
| Claude Code | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` | `/git-workflow prepare this branch` |

For example, from this library checkout, copy one skill to **one** host location in your target project:

```sh
# Codex project installation
mkdir -p /path/to/my-app/.agents/skills
cp -R skills/git-workflow /path/to/my-app/.agents/skills/

# Claude Code project installation
mkdir -p /path/to/my-app/.claude/skills
cp -R skills/git-workflow /path/to/my-app/.claude/skills/
```

These examples assume no existing destination skill. Check before copying; updates should deliberately replace a copy after reviewing local changes. For personal installation, use the personal root in the table. Avoid duplicate scopes with the same skill name. If the new skill is absent, refresh discovery or restart the host. Codex CLI/IDE also provides `/skills` and a `$` picker; Claude Code exposes `/name`. See [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills) (checked 2026-10-17).

```text
# Codex
Use $technical-design-interview with docs/prd/prd.md; keep our existing stack.

# Claude Code
/technical-design-interview use docs/prd/prd.md; keep our existing stack.
```

Cloning this repo alone does not install skills. `agents/openai.yaml` is optional Codex UI metadata, not a requirement for the workflow; Claude Code uses the same `SKILL.md` and references. Both hosts can select relevant skills automatically from descriptions. The direct-file/copy-paste method above remains the fallback. No package installation is needed for the skill text; tools such as `bd`, Git, a test runner, and UI previews depend on the chosen workflow and target environment.

## For bots: read selectively

Start at [catalog.md](catalog.md) for task routing and handoffs. Load only the skills relevant to the user's request. Each one is self-contained, so installing the full collection does not mean running every workflow.

- Resolve output paths against the **target project**, never the installed skill folder.
- Read existing requirements, design decisions, and project instructions before interviewing the user.
- Treat examples and default paths as adaptable; preserve the user's chosen scope, stack, and format.
- Ask about unresolved decisions, preserve partial drafts, and make assumptions explicit.
- Read the [shared execution contract](shared/execution-contract.md). Its generated reference copy travels inside each independently installed skill.
- Report artifacts, checks actually run, and what remains unverified.

[AGENTS.md](AGENTS.md) governs maintaining this library. It is not a policy file to copy into consuming projects.

## Check Your Head: quality and sources

The original workflows were adapted from repeated public project instructions. The first four history-derived workflows use reviewer-supplied paraphrases and author-stated rules, with eligible public sources checked for visibility and license before use. No session transcripts were searched or read. Each skill includes exact source provenance and the MIT notice so that it stays attributable when copied individually. Project-specific branches, deployment assumptions, and automatic cleanup actions have been removed.

Selection includes the unchanged 35-case rerun and earlier 28 fresh cases, plus a separate 16-case fresh evaluation for the four history-derived workflows. A separate [follow-up evaluation](evaluations/follow-up-skills/README.md) adds 12/12 fresh opaque-ID target decisions for diagnose-first, docs-audit, and agent-handoff-prompt; its potentially cued descriptive-ID run is retained separately. Cases were authored after their descriptions were frozen. Paired runs distinguish changed defaults/reporting from unchanged defect conclusions. The spec review default is diagnosis without unsolicited fixes; regression testing requires API contract coverage and trusted external oracles where applicable. See [validation.md](validation.md) for coverage and limitations. To propose a change, include the request that exposed the problem, the expected behavior, and a focused improvement. Keep each skill useful on its own and avoid turning one project's conventions into defaults for everyone.

Licensed under [MIT](LICENSE). Now put those skills to work.

Maintainers: edit the execution boundary once in `shared/execution-contract.md`, then run `python3 scripts/sync_contract.py`. Generated copies keep standalone installs self-contained; `python3 scripts/check_library.py` checks drift, links, metadata, and privacy hygiene. See [evaluation cases](evaluations/cases.json) and [validation results](validation.md).

The earlier four history-derived skills can be requested directly, using your host’s invocation syntax:

```text
Use $review-findings-triage to explain every current review finding and propose actions first.
Use $session-start-and-close to reconstruct interrupted work and show the next ready task.
Use $local-test-handoff to prepare this feature branch for phone testing before merge.
Use $prose-edit to tighten this existing launch note and make it friendlier.
```

The source and pattern boundaries are in each package’s provenance. The paired triage/prose runs showed no clear overall quality improvement; the [validation report](validation.md) distinguishes consistent procedure/reporting from improved results.

Maintenance helpers:

| Script | What it does |
| --- | --- |
| `scripts/check_library.py` | Checks package structure, metadata, links, contract copies, stale names, pattern provenance, and the prose package’s no-em-dash rule. |
| `scripts/replay_evaluations.py` | Single replay entry point: verifies the current canonical routing snapshot, frozen historical scores, paired evidence, and executable fixtures. Description changes require a fresh full-suite evaluator run; replay does not rerun agents. |
| `scripts/replay_history_evaluations.py` | Compatibility forwarding stub for old commands; runs the same full replay entry point. |
| `scripts/sync_contract.py` | Updates packaged contract copies from the shared source; `--check` detects drift without writing. |

The `history-derived` checker group applies to the seven paraphrase-provenance skills because their Pattern evidence sections and description exclusions need enforcement. The seven source-extracted skills instead carry source-mapped rules and extraction/license records in their provenance; their absence from this group is deliberate.

Current routing regression: the [canonical suite](evaluations/routing-regression/README.md) scores 89/93 retained target cases against all fourteen descriptions, separate from historical fresh-case scores. Re-score the complete set with a fresh evaluator whenever a description changes.
