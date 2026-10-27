---
name: task-planning
description: Turn a requirement, defect, or engineering objective into a bounded and verifiable plan with explicit acceptance criteria and decision gates.
---

# Task Planning

## Purpose

Create an execution plan that is detailed enough to guide implementation but small enough to avoid unnecessary process overhead.

## Use when

- The task spans multiple files, components, or verification stages.
- Requirements are ambiguous or acceptance criteria are missing.
- The change carries meaningful compatibility, security, operational, or hardware risk.

For a clear one-line change, use a lightweight checklist rather than a large plan.

## Procedure

1. Restate the intended behavior and identify the observable outcome.
2. Inspect relevant project facts and current implementation before proposing a design.
3. Define scope, non-goals, affected interfaces, and acceptance criteria.
4. Identify dependencies, likely failure modes, compatibility risks, and the checks needed to detect them.
5. Separate decisions that can be made from repository evidence from decisions requiring human authority.
6. Prefer the smallest plan that satisfies the goal. Avoid adding unrelated cleanup or speculative future work.
7. Sequence implementation and validation so that each stage leaves a reviewable state.
8. If a material decision is required, present the question, options, consequences, and recommendation. Otherwise proceed.

## Outputs

A concise plan containing scope, implementation steps, validation steps, risks, and any required decision.

## Failure handling

If a requirement cannot be made testable, state what is missing and propose a concrete acceptance criterion. Do not invent business requirements to fill the gap.

## Completion criteria

The plan maps the stated goal to a bounded change and evidence that can determine whether the goal was met.
