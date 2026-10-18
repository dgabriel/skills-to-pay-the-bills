Status: open

# Content-audit follow-ups: routing misses and documentation gaps

From a full content audit of all fourteen skills (every entry point, procedure, provenance file, and prompt prompt), reviewed against the evaluation evidence, approved by the owner on 2026-10-17. Headline audit findings: no bad prompts, no real content duplication, description/procedure fidelity holds everywhere, and the checker rule asymmetry is principled rather than sloppy. What remains is one genuine description/label disagreement, one accepted tripwire to document, and one missing maintainer note. The audit report also notes that no skill has demonstrated behavioral quality gain; evidence covers selection accuracy and structural compliance only. That ceiling is accepted for now and is not work in this order.

Each part below is separate work. Do one part only when the owner names it, on its own branch from `main`, and hand back for review before any PR. When a part is done, mark it here with its commit. Mark this order `done` when all parts are done or dropped.

Shared rules for every part: follow AGENTS.md and the existing package format. Don't push, open a PR, or touch remote history unless the owner says so. Historical evaluation evidence and historical work-order bodies stay unchanged. Push back in writing on anything you disagree with.

## Part A: resolve the spec-review description gate

Status: done (commit "feat: broaden spec-review description gate and rerun canonical routing")

The canonical suite's two spec-review misses ("Give a read-only pre-merge review of these changes." and "Review this patch for correctness and security.", both expected positives now routing to nothing) trace to the description's gate "against its issue/specification." Unspecced patch review never reaches the skill, even though `skills/spec-review/references/procedure.md` fully supports it (read the diff, apply documented project rules) and the two v1-era positives were never revised when the boundary sharpened. The description gate, not the evaluator, causes the misses.

**Owner decision required before this part starts; record it here.**

Owner decision: **BROADEN**, explicitly approved in the current task on 2026-10-18.

- If the decision is **broaden**: revise the spec-review description to cover patch review without a supplied spec (for example, "against its issue/specification or documented project rules"), keeping the existing exclusions. Keep the entry point within the enforced metadata format and 28-line limit. Then follow the canonical re-run policy in [evaluations/routing-regression/README.md](../evaluations/routing-regression/README.md): preserve the current snapshot, freeze the updated description set and entry hashes, run a fresh evaluator (separate roles per [evaluations/README.md](../evaluations/README.md)) over the full canonical suite, record the new output and process note, and update the manifest, canonical README, and validation.md current-status text. A description change without a fresh full-suite run leaves replay failing by design. Report the new score; do not edit the stale cases or their labels.
- If the decision is **accept**: leave the description untouched and record in [evaluations/routing-regression/README.md](../evaluations/routing-regression/README.md) that the two spec-review positives are stale labels retained as tripwires, alongside Part B's note. No re-run needed.
- Either way, keep [catalog.md](../catalog.md) and the root README table consistent with the outcome.

## Part B: document the accepted Beads tripwires

Status: open

The two Beads misses ("Prepare an issue handoff for another session." now selecting agent-handoff-prompt, and "Resolve legacy issue OLD-42 to its native tracker ID." selecting nothing) come from v1-era minimal-context prompts; their v2 revisions, which establish Beads context explicitly, route correctly. The library already treats those revisions as the live versions. The owner accepts the originals as permanent tripwires: bare requests without tracker context need not route to beads-workflow.

- Add a short note to [evaluations/routing-regression/README.md](../evaluations/routing-regression/README.md): the two original Beads positives are accepted misses, superseded by their v2 context-establishing revisions, retained unchanged so the suite keeps watching the boundary.
- No cases, labels, descriptions, or scores change. If Part A chose "broaden" and already edits this README for its re-run note, sequence Part B after it or combine the notes in one place so the four misses are explained together.
- Commit: `docs: record accepted routing tripwires`

## Part C: record the checker-group rationale

Status: open

The `history-derived` rule group in [scripts/skill_checks.json](../scripts/skill_checks.json) covers exactly the seven paraphrase-based skills (`## Pattern evidence` provenance) and not the seven public-source skills (`## Sources` provenance with extraction/license records). This is deliberate but recorded nowhere; a maintainer could reasonably read it as an oversight.

- Add one or two sentences where a maintainer will see them (the root README maintenance/helpers area is fine): the checker group applies to paraphrase-provenance skills because their pattern evidence and description exclusions need enforcement; source-extracted skills carry source-mapped rules in their provenance instead.
- Commit: `docs: record checker group rationale`

## Do not do (explicit skips)

- No boilerplate harmonization across the fourteen entry points: Part B of the second-opinion order hashes whole SKILL.md files, so cosmetic copy alignment alone would force a canonical re-freeze and fresh full-suite run. Fold any such edit into a future pass that already changes descriptions or entry points.
- No repeated-trial or blinded-grading effectiveness program; the selection-plus-structure evidence ceiling is accepted.
- No edits to any case prompts, expected labels, historical routing sets, or the retained invalid descriptive-ID run, under any part.
- No description or entry-point edits other than Part A's, only if "broaden" is chosen.

## Acceptance criteria (each part)

- [ ] `python3 scripts/check_library.py` and `python3 scripts/replay_evaluations.py` pass. Paste the output.
- [ ] Privacy grep over tracked files is clean: no private or local-only repository names, absolute personal paths, session identifiers, or credentials. Paste the command and output.
- [ ] `git status -sb` is clean and nothing is pushed.
- [ ] Part A "broaden" branch additionally: prior canonical snapshot preserved in place; the fresh evaluator's process note records role separation and allowed inputs; replay passes with the new recorded score; the new score and the four (or fewer) misses are stated in validation.md current status.

## Hand back

Which part you did, the owner decision used for Part A, the checklist with evidence, `git log --oneline main..HEAD`, and anything you disagree with.
