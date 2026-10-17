Status: open

# Follow-ups: checker config, validation layout, candidate skills

A backlog from the reviewer's gatekeeper passes on `codex/history-skills`. Each part is separate work. Do one part only when the owner names it, on its own branch from `main`, and hand back for review before any PR. When a part is done, mark it here with its commit. Mark this order `done` when all parts are done or dropped.

Shared rules for every part: follow AGENTS.md and the existing package format. Don't push, open a PR, or touch remote history unless the owner says so. Push back in writing on anything you disagree with.

## Part A: per-skill rules out of `check_library.py`

`scripts/check_library.py` hard-codes the history-derived skill names (for the "Pattern evidence" requirement) and a prose-edit-only em-dash rule. Move per-skill rules into skill metadata or one small config file, so adding a skill doesn't mean editing the checker.

- Use the shape you proposed in the history-skills hand-back, or propose a better one first.
- Behavior stays the same: the checker passes at HEAD, and it fails when a rule is broken. Show both by temporarily breaking one rule in a scratch copy, not in a commit.
- Commit: `refactor: move per-skill checks into skill config`

## Part B: current status first in `validation.md`

`validation.md` has turned into an append-only log. Restructure it: a short "Current status" section at the top (packages, latest checks and what actually ran, latest routing scores, open limits), then history below, newest first.

- Don't change or lose any historical result. Moving and relabeling are fine.
- Keep fresh routing scores separate from historical ones, and static review separate from execution.
- Commit: `docs: put current validation status first`

## Part C: candidate skills from session history

The reviewer's analysis of the owner's session history found four more repeated workflows. The evidence below is the reviewer's paraphrase. Don't search for, quote, or read session transcripts or local agent session directories. Use the same evidence and provenance rules as `2026-10-17-history-skills.md`. That includes the "Pattern evidence" section labeled "author session history, paraphrased by reviewer, 2026-10-17".

Before writing any of them, check for overlap with existing skills. Overlap means a section in an existing skill, not a new skill. Say which you chose and why.

1. **`diagnose-first`** (about 11 sessions, 3 projects): before fixing, explain the whole issue and confirm the problem actually exists. Ask what changed since the last working version. Offer a full rollback so the owner can test the previous version. Check current docs or the web instead of relying on old knowledge. When work goes in circles, stop and give a clean bulleted state. Several of these came after frustration, so this one has priority.
2. **`agent-handoff-prompt`** (about 13 sessions, 3 projects): write a copy-pastable prompt for another agent or developer. Assess another reviewer's or model's output and give an opinion. Run the reviewer-and-gatekeeper loop this repository uses: work order, build, review, fix, approve. Check overlap with `work-orders/README.md`.
3. **`docs-audit`** (about 10 sessions, 5 projects): check help, privacy, terms, and about pages against what the code actually does. Review all documentation for completeness. List docs that should exist but don't. Write architecture docs with diagrams a person can read.
4. **`project-bootstrap`** (about 6 sessions, 3 projects): set up a new repository so it's ready for agents. That means issue tracker init, adapted agent definitions, a git hygiene doc, review gating in CI, and local testing. Check overlap with the starter prompts on `codex/project-starter-prompts` and with `beads-workflow` and `git-workflow`. This may belong as a prompt or a section, not a skill.

For each skill you add, include the same work as the history-skills order:
- README table and catalog routing.
- 2 positive and 2 negative routing cases, written after the description is frozen and scored by a fresh evaluator.
- validation.md entries that state exactly what ran.
- One commit per skill: `feat: add <name> skill`, then `test: add routing evidence for <names>`.

## Acceptance criteria (each part)

- [ ] `python3 scripts/check_library.py`, `python3 scripts/replay_evaluations.py`, and `python3 scripts/replay_history_evaluations.py` pass. Paste the output.
- [ ] Privacy grep over tracked files is clean: no private or local-only repository names, absolute paths, session identifiers, or credentials. Paste the command and output.
- [ ] `git status -sb` is clean and nothing is pushed.

## Hand back

Which part you did, the checklist with evidence, `git log --oneline main..HEAD`, and anything you disagree with.
