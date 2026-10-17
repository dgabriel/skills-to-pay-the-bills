# Start and handoff plan

The snapshot maps legacy OLD-42 to native issue `borrow-8x9` through its external_ref; title: “Record tool returns”; status: open. Use the native ID in project commands.

The fixture has no CLI. No installs, initialization, tracker commands, Git commands, or remote sync were performed.

In the actual project, first inspect its local issue and Git guidance and the wrapper's documented usage. After checking for existing work and ensuring the working tree is suitable, the authorized start command is:

```sh
scripts/issue-start.sh borrow-8x9
```

That wrapper creates the branch and claims the issue. Do not add a manual `bd` claim or manually create a competing branch. If it fails or work is already claimed, inspect and resolve that state before retrying; do not bypass its policy.

Implement only the agreed return-recording scope and run the project's acceptance checks. At handoff, record native ID and legacy link, branch/commit references, completed behavior, exact checks and results, remaining work, and blockers. Keep the issue open while code is unmerged or acceptance checks are incomplete. Use the local bd help and project guidance to determine the supported handoff-note/update command; the supplied artifacts do not establish its syntax, so an exact bd mutation would be invented.

After merge and successful acceptance checks, closing becomes eligible; verify the project's supported close command before executing it. Remote tracker sync requires separate permission and is excluded from this plan's execution. Handoff alone does not authorize closure or sync.
