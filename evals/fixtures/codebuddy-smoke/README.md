# CodeBuddy Activation Smoke Fixture

This directory is an isolated workspace for testing CodeBuddy Skill discovery without touching Huayan, HyRemote, or another consuming project.

## Run

1. Open this directory as the workspace root in CodeBuddy IDE or CodeBuddy Code CLI.
2. Confirm `.codebuddy/skills/adk-activation-smoke/SKILL.md` is visible to the client.
3. Start a fresh conversation.
4. Use the prompt in [evaluation scenario 07](../../scenarios/07-codebuddy-activation.md).
5. Record the client version, whether the Skill was listed, whether the Skill was invoked, and the exact token returned.

The token is an evaluation canary, not a secret. A token alone is insufficient: the evaluator must also capture the client-side Skill discovery/invocation evidence. Do not use this fixture as proof of project-level registry integration.
