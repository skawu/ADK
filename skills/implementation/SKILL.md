---
name: implementation
description: Implement an authorized change in an existing codebase while preserving architecture, limiting scope, and keeping the result verifiable.
---

# Implementation

## Purpose

Translate an agreed requirement and plan into a minimal, coherent, reviewable implementation.

## Use when

A task requires creating or changing code, configuration, tests, or project documentation. Use the relevant technical Profile alongside this Skill.

## Procedure

1. Confirm the current task, acceptance criteria, repository instructions, and working-tree state.
2. Read the relevant implementation, callers, interfaces, tests, and configuration before editing.
3. Identify the smallest complete change and any required test or documentation updates.
4. Follow the project's existing architecture, naming, error handling, dependency, and compatibility conventions.
5. Make changes in coherent increments. Do not overwrite unrelated edits or reformat unrelated files.
6. Add or update tests that exercise the changed behavior and relevant regression boundary.
7. Run the applicable build and checks through build-test-verify.
8. Review the complete diff for unintended behavior, security issues, generated files, and scope expansion.
9. Report what changed and what remains unverified.

## Decision boundaries

Do not silently alter public APIs, persistent formats, protocol contracts, dependency baselines, deployment behavior, or safety-critical control logic. If the task does not authorize a consequential change, present options before performing it.

## Outputs

A reviewable change, appropriate tests/documentation, and an evidence-based change report.

## Completion criteria

The implementation satisfies the agreed criteria or its remaining gaps are clearly reported with status and evidence.
