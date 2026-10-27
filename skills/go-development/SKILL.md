---
name: go-development
description: Implement and review Go services and libraries with explicit context cancellation, goroutine ownership, channel semantics, error propagation, and race-aware verification.
---

# Go Development

## Purpose

Deliver Go changes that have clear concurrency ownership, bounded lifecycle, explicit errors, and tests appropriate to the changed behavior.

## Use when

- Implementing Go services, libraries, commands, or background workers.
- Changing goroutines, channels, Context propagation, shutdown, shared state, or API contracts.
- Diagnosing leaks, races, deadlocks, flaky tests, or service lifecycle failures.

## Inputs and prerequisites

Inspect go.mod, the configured Go version, package layout, build tags, generated code, dependency policy, service lifecycle, test commands, and supported deployment environments.

## Procedure

1. Read the affected packages, callers, interfaces, tests, and repository-specific development instructions.
2. Define ownership and exit conditions for each goroutine introduced or changed.
3. Propagate context cancellation and deadlines through request-scoped work; avoid detached background work without explicit lifecycle ownership.
4. Check channel ownership, closure, blocking sends/receives, backpressure, cancellation paths, and shutdown ordering.
5. Preserve errors with useful context, avoid swallowing failures, and prevent sensitive payloads from entering logs.
6. Review shared state for data races and synchronization correctness. Use the race detector where supported and relevant.
7. Respect public API and serialization compatibility; avoid unnecessary dependencies and broad package redesign.
8. Apply project formatting, tests, linting, and build commands. Do not assume a tool is installed or a test suite is complete without checking.
9. Verify graceful shutdown and failure handling when service lifecycle is affected.

## Outputs

A bounded Go change, tests, actual command results, and remaining concurrency or environment risks.

## Failure handling

If required services, dependencies, or test infrastructure are unavailable, record the blocker and run independent checks that remain meaningful. Do not substitute a passing unit test for an unexecuted integration or race check when the latter is required by the claim.

## Completion criteria

The change has explicit concurrency/lifecycle behavior, relevant tests and checks are recorded truthfully, and unresolved risks are visible.
