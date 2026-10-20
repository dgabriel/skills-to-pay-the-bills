# Skill-security-review: canonical rerun process

On 2026-10-18 the coordinator preserved the entire prior 91/93 canonical tree in snapshots/2026-10-18-before-skill-security-review, including its earlier snapshot. The new skill was finalized and all fifteen descriptions/entry hashes frozen before a separate author read only that freeze and wrote two positive and two negative cases. All prior 93 cases and labels remain unchanged. Four new source occurrences bring the canonical suite to 97 target cases and 165 retained occurrences.

The coordinator consolidated the new cases into the canonical input. A separate fresh evaluator with no inherited conversation was instructed to read only routing-input.json and overwrite routing-output.json, without reading existing output, labels, cases, skill bodies, snapshots, work orders, repository context, or prior results. It reported reading only that input, writing all 97 answers, and inheriting settings without overrides, with no network, scoring, or other agents. This is tool-call sequence and evaluator self-report, not an access-control audit.

After completion the coordinator scored **94/97 target decisions**. The four new skill-selection cases scored **4/4**. No cases, labels, descriptions, or evaluator responses were edited after scoring, and no repeated trial was run.

Current missed positives:
- “Prepare an issue handoff for another session.” Target beads-workflow; selected agent-handoff-prompt and session-start-and-close.
- “Verify this feature and report exact failures without fixing app code.” Target regression-testing; selected spec-review.
- “Resolve legacy issue OLD-42 to its native tracker ID.” Target beads-workflow; selected none.

The Beads originals remain accepted as potential misses under the earlier owner decision. The regression-testing miss remains unaccepted. This is selection evidence, not a measured injection-detection rate, quality improvement, or native host discovery. A separate finite static-review smoke test is retained under evaluations/skill-security-review and must not be conflated with routing scores. Historical outputs, invalid evidence, and prior snapshots remain unchanged.
