# Diagnosis procedure

## Confirm the problem

Read project instructions, the report, relevant code, logs, and existing tests before editing. Establish expected versus observed behavior, triggering inputs, affected environment, and impact. Reproduce with safe local fixtures when possible; otherwise say what is unverified. Distinguish an application bug from environment, configuration, stale artifacts, and a mistaken expectation. Do not assume the report is wrong merely because local reproduction fails.

Ask what changed since the last known working version. First inspect supplied context and available history so the owner need not repeat answers. Trace the whole failure path, including side effects and dependencies, rather than patching the nearest error message. State hypotheses, evidence for and against each, and the next discriminating check. For version-sensitive behavior, consult current official documentation or primary sources and report the version/reference checked; if unavailable, mark the assumption unverified.

## Compare without losing current work

When a previous version could distinguish a regression, offer a full previous-version comparison with its revision, environment assumptions, and what the result would establish. Obtain explicit owner approval before creating or using a separate worktree or comparison branch for a rollback test. A general request to investigate is not rollback approval. Never discard, reset, overwrite, or automatically stash current work. Inspect dirty state and leave the working checkout intact; prefer a separate worktree when switching would disturb it. Do not rewrite published history. Keep data, migrations, shared services, and credentials isolated too; reproducing an older revision must not roll back a live database or deployment. If isolation is unavailable, present a plan and stop that comparison.

## Explain, then hand off

Before repair, explain the symptom, trigger, causal path, expected behavior, practical impact, and confidence in plain language. If evidence is insufficient, give the smallest next check rather than presenting a guess as a cause. Diagnosis does not itself authorize implementation; proceed with a fix only within the owner's actual scope.

When successive attempts repeat without new evidence, stop the loop. Return short bullets covering confirmed facts, attempts and exact outcomes, unresolved hypotheses, blockers, and the next decision. Do not reset the project to make the investigation look clean. Report commands actually run and checks only proposed. Offer a focused regression test once the intended behavior is established, without claiming it was executed.
