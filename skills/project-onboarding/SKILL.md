---
name: project-onboarding
description: Build an evidence-based understanding of an existing repository before implementing work, or refresh project context when its architecture or toolchain is unclear.
---

# Project Onboarding

## Purpose

Establish a concise, evidence-based project profile so subsequent work uses actual repository facts rather than assumptions.

## Use when

- Entering an unfamiliar repository.
- Starting a substantial task with unclear dependencies or architecture.
- The build environment, supported target, or project instructions may have changed.

Do not repeat a full onboarding for a trivial follow-up when the relevant facts are already verified and current.

## Inputs and prerequisites

Repository access and permission to inspect files. Do not mutate project files during discovery unless the task explicitly includes setup.

## Procedure

1. Read root and applicable nested instructions, including AGENTS.md and tool-specific rules.
2. Inspect repository status, top-level structure, recent relevant changes, and existing local modifications.
3. Identify the actual activation path: tool configuration, instruction entry points, skill directories, and any project-owned registry or manifest. Do not assume a Skill is active because its file exists.
4. Identify authoritative architecture documents, interface contracts, and accepted decisions.
5. Identify language/framework/compiler versions, build system, dependency manager, and target platforms from configuration files.
6. Locate test suites, CI workflows, scripts, and documented build commands. Distinguish documented commands from commands verified by execution.
7. For embedded or multi-component projects, map host/target boundaries, protocol contracts, hardware dependencies, and safe operation limits.
8. Fill or update the project profile only with verified facts. Mark missing facts UNKNOWN and state how to establish them.
9. Summarize the relevant constraints and risks for the current task; do not produce an exhaustive repository tour unless requested.

## Outputs

- A concise project context summary.
- Links or paths to authoritative documents and build/test entry points.
- The active instruction and Skill activation path.
- Explicit unknowns and blockers.
- A project profile update only when useful and within scope.

## Failure handling

If files, registries, or tools are unavailable, state exactly what could not be inspected. Never infer missing project facts from a repository name or product description.

## Completion criteria

The current task's relevant architecture, build/test entry points, active guidance, constraints, and unknowns are identified well enough to plan safely.
