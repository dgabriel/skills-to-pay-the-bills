---
name: local-test-handoff
description: Prepare a completed web feature on its current feature branch for owner testing on local devices, including LAN reachability and a device checklist. Not staging/production deployment, native app distribution, or a test-code-only task.
---

# Local Test Handoff

**Inputs:** Feature branch, project dev/run instructions, local services/account setup, and requested owner devices.
**Output:** Verified running revision and exact device URL, persistent dev account access if needed, and a short pass/fail checklist.
**Try:** “Use local-test-handoff to make this feature testable from a phone before merge.” (use the skill name in your host's invocation syntax).

Honor the task scope and target-project policy; preserve unrelated work. Consult the [procedure](references/procedure.md) for operation details and the [shared contract](references/execution-contract.md) for authorization boundaries.

1. Confirm the feature revision and inspect startup scripts before running them. Preserve the feature branch, existing dev data, and unrelated services; do not use a launcher that silently checks out another branch.
2. Start or update the project’s dev runtime and verify dependencies and app readiness. Prefer an existing stable container/runtime when repeated dev-server crashes impede testing; do not tear down persistent volumes.
3. For a requested LAN test, discover the actual reachable local address/port, binding and frontend/backend access requirements; verify from available devices and give the exact URL with any unverified reachability stated.
4. Reuse or idempotently seed a persistent dev-only test account. Share local dev access in chat only after confirming its environment; never share staging/production credentials. End with device-specific pass/fail checks and the next feedback step.

Report what actually happened, pending decisions, and the next action. Use target-project paths. [Provenance and pattern evidence](PROVENANCE.md).
