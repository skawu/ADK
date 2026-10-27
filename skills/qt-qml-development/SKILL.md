---
name: qt-qml-development
description: Implement and review Qt Widgets, Qt Quick/QML, and C++/QML integration changes using the project's actual Qt version, architecture, build route, and UI/runtime evidence.
---

# Qt / QML Development

## Purpose

Deliver bounded Qt/QML changes that respect object lifetime, thread affinity, UI responsiveness, resource registration, and the project's established application architecture.

## Use when

- Adding or modifying a Qt Widgets or Qt Quick/QML feature.
- Changing C++/QML interfaces, models, properties, signals, slots, or asynchronous behavior.
- Fixing QML imports, resources, startup, bindings, focus, or UI interaction defects.
- Reviewing a Qt-specific change.

Use the Qt/QML Profile and the C++ Profile when applicable.

## Inputs and prerequisites

Identify the actual Qt version, modules, compiler, build system, target, active instruction entry point, project Skill activation path, affected QML module, resource registration, tests, and canonical build commands.

## Procedure

1. Read project instructions, the relevant architecture boundary, affected QML/C++ source, callers, tests, and build configuration.
2. Classify the change: presentation, state/model, C++/QML contract, resource/module registration, threading/lifecycle, startup, or packaging.
3. Preserve the existing separation between presentation, domain behavior, and device/service access. Do not let QML become an unauthorized protocol or persistence layer.
4. Check QObject ownership and lifetime, thread affinity, queued delivery, signal/slot duplication, re-entrancy, cancellation, and stale asynchronous results.
5. Keep blocking I/O and expensive computation off the UI thread. Check QML binding loops, imperative binding overwrites, focus/keyboard behavior, and avoidable object churn.
6. When adding or moving QML types, verify module URI, qmldir, resource declarations, CMake target membership, import paths, and deployment reachability.
7. Add or update tests for the changed behavior and relevant failure state. Use the project's canonical build/test route rather than inventing a parallel command chain.
8. Validate the actual interaction and important states when the claim concerns UI behavior. Static source inspection or a successful compile alone does not prove runtime usability.
9. Review the final diff for scope, resource registration, thread/lifetime risks, compatibility, and unverified claims.

## Outputs

A bounded Qt/QML change, relevant tests or acceptance criteria, build/runtime evidence, and a report of any unverified UI or target behavior.

## Failure handling

If the Qt Kit, target, resource/module contract, or required UI environment is missing or ambiguous, do not silently switch versions or fabricate a passing result. Report the missing fact and continue with safe source-level analysis or a focused diagnostic where useful.

## Completion criteria

The change follows the project's Qt architecture and build route, relevant checks have truthful statuses, and runtime/UI claims are supported by the appropriate evidence or explicitly marked unverified.
