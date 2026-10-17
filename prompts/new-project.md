# Start a project in my preferred way

Paste the prompt below into a new project chat. Replace the idea placeholder; add any firm constraints. This begins planning and project-local skill setup, with an explicit handoff before implementation.

```text
Help me start this project in my preferred way.

Idea: [Describe the product, who it is for, and the problem it solves.]
Constraints: [Add any firm stack, budget, timeline, platform, or brand choices;
otherwise leave these open for discussion.]

Use https://github.com/dgabriel/skills-to-pay-the-bills as my workflow library.
Use a local checkout if available; otherwise retrieve current main. Read its
README, catalog.md, and shared contract, then load only relevant complete skill
packages. If you cannot read the library, explain the missing access instead of
claiming you used it. Read any existing project instructions and files first;
explicit choices and project conventions override the defaults below.

Start with product-requirements-interview. Ask one short round at a time, reuse
answers, and clarify the user, problem, core journey, and success signals.
Keep the MVP small, aim for roughly six must-haves or fewer, and name useful
non-goals. Push back on scope creep. Surface consequential unknowns instead of
inventing research, budgets, decisions, or approval.

Turn the requirements into a technical design with
technical-design-interview. For a new web MVP, start with FastAPI, async
SQLAlchemy, Postgres, Alembic, pydantic-settings, environment-driven feature
flags, and React/TypeScript. Prefer request/response, polling, and simple
scheduled work before queues or websockets. Explain a requirement-driven
exception and preserve any stack I explicitly choose. Cover data ownership,
authentication/authorization, API contracts, migrations, operations, cost
uncertainty, and verification of the core journey.

For a product with a user interface, use design-system-workshop once the
product context is clear. Favor restrained colors, typography, spacing, and
emphasis; preserve an existing brand. Produce a usable style guide rather than
building screens during discovery. Skip visual design for a project that does
not need it.

Save draft requirements, technical design, and any style guide in the target
project's docs structure, using the library's suggested paths where no structure
exists. Carry decisions, draft/accepted status, and open questions between
stages. Review each draft with me before treating it as accepted; do not restart
interviews for facts already supplied.

Set up relevant project-local skills using the library's current host-specific
instructions. Detect the host or ask if unclear; preserve existing copies and
copy complete packages with references, provenance, and licenses. Add concise
project instructions for selecting them, not a copy of the library's maintenance
AGENTS.md. Do not change personal/global configuration or adopt Beads or another
tracker without my choice.

Project bootstrap, after we accept the plan and I authorize setup:
Inspect what already exists and propose only missing repository preparation.
Confirm the tracker, agent host, review policy, and local runtime with me before
initializing anything. If no tracker is chosen, keep tracker adoption pending;
when I choose Beads, use beads-workflow for its project-specific setup and
commands rather than inventing a second task store. Use git-workflow to discover
or document the branch/release policy and prepare a concise Git hygiene guide.
Adapt project agent instructions and role definitions to this repository's
actual commands, stack, authority boundaries, and handoffs; do not copy another
project's agent identities or require a multi-agent pipeline.

When I authorize CI setup, use regression-testing and spec-review to define
meaningful checks and the review acceptance process. Preserve existing gates;
do not install a review service, add a paid dependency, or introduce a new LLM
release gate without my explicit choice. Use review-findings-triage for actual
review findings, not as proof that CI ran. Use local-test-handoff to document and
verify the chosen local startup/test flow when setup and runtime execution are
authorized. Preserve dev data and record actual readiness and device-access
limits. End bootstrap with files changed, tools/configuration added, checks
actually run, and setup still pending. Keep details in those existing skills
and project guidance rather than creating a competing bootstrap procedure.

Propose the first small vertical slice and its acceptance checks. For later
implementation, use the project's Git policy, meaningful regression tests,
spec review, and a durable session handoff. Use review-findings-triage only when
there are actual review findings. For completed web features, prepare a local
feature-branch instance for my device testing, preserve dev data, and give me
the verified URL and short pass/fail checklist. Match tools and ports to the
project; never share staging or production credentials.

Communicate briefly and concretely. For existing prose edits, use prose-edit:
tighten while preserving facts, avoid em dashes and AI-isms, and make warmer
mean friendlier rather than longer.

Begin the requirements conversation now. Planning documents and project-local
skill setup are authorized; application implementation is not yet authorized.
Do not commit, push, open a PR, publish, or deploy unless I ask. End planning
with the draft locations, decisions and open questions, proposed first slice,
and checks actually performed so I can approve the implementation scope.
```
