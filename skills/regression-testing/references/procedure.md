# Regression Testing procedure and defaults

## Establish the oracle

Read requirements and test configuration before writing assertions. Expected results come from a specification, trusted fixture, independent reference, or explicit user decision. For domain calculations, record the reference and relevant tolerance; never compute an expected value with the same function being tested. If behavior is undecided, report the decision needed rather than codifying a guess.

Select a minimal useful matrix: happy path, boundary/edge path, and invalid/error path. Add ownership, permissions, duplicate actions, partial failures, and state-transition tests where the feature demands them. For ranges or thresholds test exactly on, just below, and just above the boundary. For a rejected mutation, assert unchanged state as well as the response.

## Execution

Default backend stack when creating new tests for the author's FastAPI/Postgres projects: pytest with an API test client and isolated database fixtures. Existing target tests/config override that default. For frontend, match the existing runner and assert user-observable behavior instead of component internals. A standard-library-only task remains standard-library-only.

Run targeted files during iteration. Run broader checks at the target project's ready/pre-push gate, not repeatedly for unrelated changes. Inspect Docker/database health and environment prerequisites before interpreting a wall of connection errors as a regression. Never run two suites concurrently if they share a database. Keep external API calls mocked and secrets out of test output; a smoke test must not send real email or mutate a production service unintentionally.

Do not weaken assertions to make a suite green. If assigned testing only, leave app code unchanged and hand failing evidence to implementation. If the task explicitly includes fixing code, use the failing regression to guide the fix and rerun it.

## Report

Record exact command, exit code, test count when emitted, and what behavior was covered. For failure, include file/line, test name, assertion/error text, expected result, and actual result. Distinguish assertion failures from collection/environment failures. Do not fabricate assertion counts. State which broader checks were not run and why. A test file that was authored but never executed is not a passing test.

## Opinionated defaults added in this revision

**Endpoint contract checklist:** for each changed API operation test request validation, response shape, status codes, and error handling, not merely a happy-path response. Mark a category inapplicable with a concrete reason rather than silently skipping it. This makes the template tester’s Backend tests checklist an explicit per-operation default; use the target runner, with pytest/API client as the FastAPI starting point.

**Missing external oracle is a stop condition:** when scientific/domain expected values come from an external reference, cite source name, URL, retrieval date, and relevant tolerance beside the expectation. If the source cannot be accessed and no trusted fixture/reference was supplied, stop those value assertions and report missing evidence. Other spec-defined tests can still run. Do not generate a plausible expected number or call the implementation to create it. This adapts the astronomy tester’s requirement to externally defined domain values; ordinary assertions derived directly from a supplied specification need no external citation.

**Source-backed threshold practice:** the same tester exercises exact routing thresholds and wraparound boundaries. The below/on/above triplet and rejected-mutation state assertion were already in the previous library procedure; they are now visible in the entry point and are not claimed as newly added opinions. [Rule provenance](../PROVENANCE.md).
