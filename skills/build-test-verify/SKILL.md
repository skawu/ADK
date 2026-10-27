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
2. Select the cheapest set of checks that can honestly prove the changed behavior, affected interfaces, and material regression risks. Scale cost and environment strength with the claim and change risk.
3. Confirm prerequisites, target configuration, environment, and whether the command may mutate or erase data.
4. Execute checks in a useful order: focused test, relevant module build, broader tests, static analysis, integration or target validation as appropriate.
5. Capture exact commands or test identifiers, exit status, relevant output, environment details, and the commit/artifact identity when the claim depends on a specific version.
6. For each check, record PASS, FAIL, BLOCKED, NOT RUN, or NOT APPLICABLE using the definitions in core/rules/evidence-and-delivery.md.
7. Verify that each important check has a clear oracle and that the recorded result applies to the stated subject.
8. Investigate failures sufficiently to distinguish a product defect from an environment or test-infrastructure issue.
9. Do not weaken tests, suppress warnings, or change unrelated code just to obtain a green result.
10. Report what the evidence proves, what it does not prove, and which changes would invalidate the result.

## Target-aware verification

For cross-platform and embedded projects, report host build, cross-compile, simulator, bench, hardware-in-the-loop, and production results separately. Do not imply target validation from a host-only result.

## Outputs

A verification table with property, subject/commit, command or observation, oracle, status, evidence, and explicit gaps.

## Failure handling

If a check fails, preserve the relevant output and determine whether the failure is caused by the change, environment, or test infrastructure. If a required check is blocked, record the prerequisite and do not replace it with an unrelated check. Escalate only when a decision or access change is required.

## Completion criteria

All required checks have a truthful recorded status, evidence applies to the identified subject, failures are addressed or surfaced, and remaining verification gaps are visible.
