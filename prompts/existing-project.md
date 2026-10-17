# Adopt useful skills in an existing project

Paste the prompt below into an agent working in your project. It authorizes project-local skill installation and small instruction updates, while preserving the project's existing workflow.

```text
Review https://github.com/dgabriel/skills-to-pay-the-bills and adopt the skills
that will improve development in this project. Use a local library checkout
if available; otherwise retrieve the current main branch. If you cannot read
it, tell me what access is missing rather than inventing its contents.

First get your bearings: read this project's instructions, architecture,
requirements, test commands, Git policy, tracker setup, and current work.
Preserve unrelated changes. Read the library's README, catalog.md, and shared
execution contract, then inspect the complete packages for relevant skills.
The library's maintenance AGENTS.md is not a policy to copy into this project.

Choose skills based on concrete needs and repeated work here. Consider session
orientation/handoff, Git operations, regression testing, and spec review first;
add the planning, visual design, review-triage, local-device-testing, prose, or
Beads workflows only where they fit. Use Beads only if this project uses it.
Do not restart completed discovery or replace our stack, tracker, design
system, branch policy, or release process with library defaults.

Proceed with useful, additive setup. Detect the agent host and use the library's
current project-install instructions. If the host is unclear, ask that one
question before installing; do not install duplicate copies for multiple hosts
unless I request them. Copy complete selected skill folders, including their
references, provenance, and license. Check for existing skills and name clashes
first. Preserve local customizations; ask before replacing conflicting copies.
Make a small update to the project's existing agent instructions explaining
when to select the installed skills, without duplicating their procedures or
making every skill a mandatory step. If installation is unavailable, provide
usable direct-file instructions and state the limitation.

Keep project-specific commands and conventions in this project. Do not change
application code, initialize tools or trackers, alter personal/global settings,
commit, push, publish, deploy, or open a PR as part of this setup.

Finish with a brief table: skill, need it addresses, installed location or
reason skipped. Report files changed, checks actually run, unresolved conflicts,
and two or three example requests I can use immediately. Verify copied package
references and explain if host discovery still needs a refresh. Do not claim
native discovery or behavioral testing unless you actually performed it.
```
