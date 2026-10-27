---
name: cpp-development
description: Implement and review C++ changes with explicit ownership, lifetime, error handling, concurrency, ABI, and CMake target boundaries.
---

# C++ Development

## Purpose

Produce small, maintainable C++ changes that respect the project's language standard, interfaces, resource ownership, and supported toolchain.

## Use when

- Implementing or refactoring C++ code.
- Changing public headers, ABI-sensitive interfaces, threading, resource management, or CMake targets.
- Diagnosing memory, lifetime, concurrency, build, or integration defects.

Use the C++/CMake Profile and any framework-specific Profile relevant to the task.

## Inputs and prerequisites

Establish the language standard, compiler/toolchain, build system, affected target, dependency policy, error-handling conventions, ownership model, test framework, and target environment from the repository.

## Procedure

1. Read the relevant interfaces, callers, tests, CMake target definitions, and accepted design decisions.
2. Identify ownership and lifetime of objects, buffers, handles, files, locks, and asynchronous callbacks.
3. Prefer RAII and explicit ownership. Check bounds, overflow, conversions, reference/iterator invalidation, error paths, and exception safety.
4. Review concurrency assumptions, shared mutable state, lock ordering, cancellation, shutdown, and data-race risks.
5. Keep dependencies and interfaces explicit. Do not broaden the change or introduce a new abstraction unless it solves a demonstrated problem.
6. Update the correct CMake target and dependency declarations; do not add global flags or suppress diagnostics to hide defects.
7. Add focused tests for behavior and failure paths. Use sanitizers or static analysis when available and relevant.
8. Preserve source and binary compatibility where required. Confirm the configured standard before using language or library features.
9. Run the project's canonical build/test commands and review the final diff.

## Outputs

A reviewable C++ change, appropriate tests, build evidence, and documented compatibility or verification gaps.

## Failure handling

If the required compiler, target, interface contract, or dependency is unavailable, do not guess a replacement. Isolate the uncertainty, run safe checks that remain useful, and report what could not be verified.

## Completion criteria

The change respects ownership, lifetime, error handling, concurrency, and build boundaries, with evidence proportionate to its risk.
