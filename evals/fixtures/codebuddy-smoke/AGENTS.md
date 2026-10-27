# CodeBuddy Smoke Fixture

This is a disposable, non-product workspace for testing the ADK CodeBuddy Skill adapter.

- Do not edit or access any other repository as part of this smoke test.
- Do not run shell commands or modify files.
- When the user requests the ADK activation smoke test, use the `adk-activation-smoke` Skill if the client has loaded it.
- Report whether the Skill is visible and invoked separately; never infer activation from the file existing on disk.
