---
name: build-test-verify
description: Select and execute applicable build, test, static-analysis, integration, and target checks, then report their actual outcomes without overstating evidence.
---

# Build, Test, and Verify

## Purpose

Establish what the change has actually been shown to do in the available environment.

## Use when

After implementation, after a defect fix, before a meaningful delivery, or when a test/build failure needs triage.

## Procedure

1. Read the project's build/test matrix and existing CI or developer instructions.
2. Select checks that cover the changed behavior, affected interfaces, and regression risks.
3. Confirm prerequisites, target configuration, environment, and whether the command may mutate or erase data.
4. Execute checks in a useful order: focused test, relevant module build, broader tests, static analysis, integration or target validation as appropriate.
5. Capture exact commands or test identifiers, exit status, relevant output, and environment details.
6. For each check, record PASS, FAIL, BLOCKED, NOT RUN, or NOT APPLICABLE using the definitions in core/rules/evidence-and-delivery.md.
7. Investigate failures sufficiently to distinguish a product defect from an environment or test-infrastructure issue.
8. Do not weaken tests, suppress warnings, or change unrelated code just to obtain a green result.
9. Report what the evidence proves and what it does not prove.

## Target-aware verification

For cross-platform and embedded projects, report host build, cross-compile, simulator, bench, hardware-in-the-loop, and production results separately. Do not imply target validation from a host-only result.

## Outputs

A verification table with commands, statuses, evidence, and explicit gaps.

## Completion criteria

All required checks have a truthful recorded status, failures are addressed or surfaced, and remaining verification gaps are visible.
