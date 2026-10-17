# skills-to-pay-the-bills

Collection of skills for Agentic dev I've built over time. Also a great beat from the Beastie Boys.

[Listen to “Skills to Pay the Bills”](https://youtu.be/cJgCfP98TVQ?si=sL_yQVprLwIkaywQ).

Reusable workflows for turning an idea into requirements, architecture, and a visual system. Built for humans to understand and coding agents to execute. Each skill works independently; together they form a lightweight product-planning workflow.

## So What’cha Want? Pick a skill

| Skill | Use it for | Typical result |
| --- | --- | --- |
| [Product requirements interview](skills/product-requirements-interview/SKILL.md) | Clarifying users, the core journey, and MVP scope | `docs/prd/prd.md` |
| [Technical design interview](skills/technical-design-interview/SKILL.md) | Turning requirements into a practical architecture | `docs/technical/technical-design.md` |
| [Design system workshop](skills/design-system-workshop/SKILL.md) | Defining visual tokens and component rules | `docs/design/style-guide.md`, plus UI integration when requested |

These are the first three skills. Git workflows, adversarial review, and other candidates remain in the [discovery backlog](inventory/README.md). The inventory is research material, not an instruction set to load into an agent.

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

The agent should read the selected `SKILL.md` before using it, preserve decisions between stages, and distinguish a draft from something you have accepted. Running all three does not authorize a build, release, or repository publication.

## Just a Test: try one without installing

Clone or download this repo, open your own project in an agent that can read local files, and point it to one skill:

```text
Read /path/to/skills-to-pay-the-bills/skills/product-requirements-interview/SKILL.md
and use it to interview me about a neighborhood tool-sharing app.
Write the PRD in my project at /path/to/my-app/docs/prd/prd.md.
```

No special slash command, account integration, or other skill is required. If the agent cannot read local files, provide the chosen `SKILL.md` as task context. You can also use it yourself as an interview checklist.

Once a host has installed and exposed a skill, an explicit prompt can use its name:

```text
Use $product-requirements-interview to define my MVP.
Use $technical-design-interview with docs/prd/prd.md; keep our existing stack.
Use $design-system-workshop to create a guide; leave the UI code unchanged.
```

Run those as separate requests when you want one stage at a time. The `$skill-name` syntax depends on the host; the direct-file approach above is the portable fallback. Merely cloning this repository does not install or activate skills.

## Intergalactic portability

Copy the complete folder for each selected skill into your agent's configured skill directory, retaining its `SKILL.md`, metadata, provenance, and license. For a host that discovers project skills under `.agents/skills`, the destination would look like:

```text
my-app/.agents/skills/product-requirements-interview/SKILL.md
my-app/.agents/skills/technical-design-interview/SKILL.md
my-app/.agents/skills/design-system-workshop/SKILL.md
```

Use your host's documented discovery location; there is no universal installation directory. Reload skill discovery if your host requires it. Avoid installing duplicate copies of a skill at different scopes. To update a copied skill, replace it deliberately from this repo after checking any local customizations.

Every skill includes an example prompt, input expectations, output location, workflow, and completion checks. `agents/openai.yaml` supplies optional display metadata for compatible hosts; the Markdown workflow remains usable without it. No runtime packages or external services are required by these skills. File editing, contrast calculations, and UI previews depend on tools available in the host.

## For bots: read selectively

Start at [catalog.md](catalog.md) for task routing and handoffs. Load only the skills relevant to the user's request. Each one is self-contained, so installing the full collection does not mean running every workflow.

- Resolve output paths against the **target project**, never the installed skill folder.
- Read existing requirements, design decisions, and project instructions before interviewing the user.
- Treat examples and default paths as adaptable; preserve the user's chosen scope, stack, and format.
- Ask about unresolved decisions, preserve partial drafts, and make assumptions explicit.
- Report the artifacts produced and what remains unverified. A skill invocation does not grant permission to commit, push, deploy, or publish.

[AGENTS.md](AGENTS.md) governs maintaining this library. It is not a policy file to copy into consuming projects.

## Check Your Head: quality and sources

These workflows were adapted from the public `dgabriel/claude-code-project-template` repository. Each skill includes exact source provenance and the MIT notice so that it stays attributable when copied individually. Project-specific branches, deployment assumptions, and automatic cleanup actions have been removed.

The first release has structural validation and scenario-based review; real-world effectiveness will improve through use. See [validation.md](validation.md) for coverage and limitations. To propose a change, include the request that exposed the problem, the expected behavior, and a focused improvement. Keep each skill useful on its own and avoid turning one project's conventions into defaults for everyone.

Licensed under [MIT](LICENSE). Now put those skills to work.
