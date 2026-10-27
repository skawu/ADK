---
name: git-pr-lifecycle
description: Manage an authorized change through branch, commit, pull request, review, and merge while respecting the repository's collaboration policy and preserving shared history.
---

# Git and Pull Request Lifecycle

## Purpose

Keep engineering changes reviewable and repository state explicit from preparation through delivery.

## Use when

A task requires branch management, commits, pull requests, review updates, or merge preparation.

## Procedure

1. Inspect the repository's branch policy, current branch, worktree status, upstream state, and existing PRs.
2. Preserve unrelated local changes. Do not assume the worktree is clean.
3. If the repository has no workflow, use a short-lived task branch and a focused PR where practical; do not invent mandatory labels or elaborate gates.
4. Make commits logically cohesive with descriptive messages. Never include secrets or unrelated generated files.
5. Before opening a PR, inspect the complete diff and run the available required checks.
6. In the PR description, state the goal, design, tests and actual results, known risks, and any blocked checks.
7. Address review feedback with new reviewable commits unless the repository explicitly permits another approach.
8. Merge only when required reviews, checks, and authorization conditions are satisfied. Never bypass protections to speed up routine work.
9. After merge, verify the resulting branch/PR state and report the actual commit or merge result.

## Safety

Never force-push or rewrite shared history unless explicitly authorized and permitted by repository policy. Do not claim a PR, review, or merge exists until the operation has succeeded.

## Outputs

Branch and commit references, PR link and state, check results, review disposition, and any remaining follow-up.

## Completion criteria

The authorized repository workflow has reached its required terminal state, or the exact blocker and next action are recorded.
