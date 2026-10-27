---
name: code-review
description: Review a proposed change for correctness, regressions, architecture violations, security issues, and missing validation using the actual diff and project context.
---

# Code Review

## Purpose

Provide an independent assessment of whether a change is safe, correct, scoped, and adequately verified.

## Use when

Reviewing a diff, pull request, substantial implementation, protocol/API change, or high-risk fix.

## Procedure

1. Read the task and acceptance criteria, relevant project instructions, and the complete diff.
2. Understand the affected code paths, callers, state transitions, error paths, and external contracts.
3. Prioritize concrete defects: incorrect behavior, data loss, security exposure, concurrency/lifetime errors, compatibility breaks, and missing failure handling.
4. Check whether tests cover the changed behavior and likely regressions. Verify the reported test evidence where available.
5. Check for unauthorized scope expansion, generated artifacts, secret leakage, dependency changes, and undocumented contract changes.
6. For Qt/C++, inspect object lifetime, thread affinity, resource ownership, and event-loop behavior where relevant.
7. For Go, inspect cancellation, goroutine lifetime, channel ownership, error propagation, and race risks where relevant.
8. For embedded code, inspect timing, ISR safety, memory bounds, protocol robustness, reset/fail-safe behavior, and target-specific assumptions where relevant.
9. Report findings by severity with file/line references and a clear explanation. Separate confirmed findings from questions or suggestions.
10. If no blocking finding is identified, state the scope of the review and checks not performed; do not claim that the change is defect-free.

## Finding format

For each finding include severity, location, triggering condition, impact, and a concrete remediation. Avoid vague style comments unless the project has an explicit rule.

## Outputs

A review report containing prioritized findings, evidence, and the review scope. If no actionable finding is identified, state that result and list any checks or environments not reviewed.

## Failure handling

If the diff, task criteria, relevant source, or claimed test evidence is unavailable, identify the missing evidence and limit the review conclusion accordingly. Do not approve or declare the change defect-free based on an incomplete view.

## Completion criteria

The review has inspected the complete relevant diff and produced actionable findings or a scoped no-findings report with validation gaps.
