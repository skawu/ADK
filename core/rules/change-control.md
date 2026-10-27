# Core Rule: Change Control

## Requirements

- Inspect branch, working-tree status, and existing changes before editing or running commands that may mutate files.
- Do not overwrite or discard uncommitted work that is not clearly part of the task.
- Keep changes reviewable and logically grouped. Avoid unrelated formatting or generated-file churn.
- Follow the repository's established branch, commit, pull request, review, and merge policies. If none exist, propose a simple policy rather than silently imposing one across all projects.
- Respect project-specific restrictions on querying hosted CI, Actions, checks, or external services. Do not assume that an available connector or visible endpoint is authorized for every repository.
- Never force-push, rewrite shared history, bypass required review, or alter protected branches unless explicitly authorized by the applicable policy and task.
- Do not commit generated binaries, secrets, local environment files, or build outputs unless the repository explicitly requires them.
- For dependency changes, explain the reason, compatibility impact, licensing implications when relevant, and reproducibility effect.
- For schema, protocol, public API, or persistent-data changes, assess compatibility and migration before implementation.
- Update project documentation when behavior, supported environments, interfaces, or operational procedures materially change.

## Before delivery

Review the complete diff, check file status, identify accidental changes, and verify that the final branch/PR state matches the task's authorized scope. Never claim a commit, push, PR, or merge happened unless the operation actually succeeded.
