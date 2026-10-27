# ADK Project Pilot Plan

## Purpose

Validate that ADK is useful across two materially different engineering environments without forcing either project to adopt a new architecture, governance system, or tool convention.

This document records the pilot design, not a claim that the behavior evaluations have passed.

## Read-only inventory completed

The initial review established two distinct integration patterns:

| Pilot | Project shape | Existing instruction/activation pattern | Primary ADK validation focus |
|---|---|---|---|
| A | Industrial Qt/QML application with C++ services | Root project instructions plus a project-owned registry for selected rules and Skills | Qt/QML implementation, resource registration, canonical build route, UI/runtime evidence, registry integrity |
| B | Multi-platform Qt/C++ SDK | Root project instructions, contribution guidance, canonical build/test documents, and PR-based validation | C++/Qt architecture, canonical build route, risk-proportional testing, exact artifact/commit evidence, compatibility claims |

The source projects' private or product-specific instructions are not copied into ADK. The table records only reusable integration differences.

## Lessons already reflected in ADK

- A root AGENTS.md is not interchangeable with a project-owned registry.
- A Skill's presence on disk does not prove that the target tool activates it.
- Project-specific build commands and test routes must remain authoritative.
- Test scope should follow risk and the property being claimed, not a universal “run everything” rule.
- Evidence needs an oracle and a clear relationship to the tested commit/artifact and environment.
- A generic status vocabulary must not override project-owned status terms.
- CI access, evidence collection, and release/merge gates must follow the project's policy.
- Project-specific product architecture and internal governance must not be promoted to universal ADK rules.

## Next pilot sequence

### P1 — Compatibility audit

For each project, record:
- active instruction entry point;
- relevant existing rules and Skills;
- tool-specific discovery/activation behavior;
- canonical build/test route;
- evidence vocabulary and required evidence strength;
- conflicts, duplicate instructions, and missing guidance.

### P2 — Select a narrow Skill set

Start with project onboarding, build-test-verify, code review, and the relevant technical Skills. Do not install all ADK content by default. Record why each selected Skill is needed and where it will be activated.

### P3 — Project-owned integration change

If the audit shows a clear benefit, create a focused change through that project's own workflow. Preserve its existing AGENTS.md, registry, status vocabulary, build authority, and security policy. Do not write directly to the consuming project's default branch or silently replace its registry.

### P4 — Bounded task evaluation

Use one low-risk, representative task per project. Capture:
- task and acceptance criteria;
- active ADK version and actual tool/model configuration;
- relevant project instructions loaded;
- changed files and diff scope;
- exact checks executed and their results;
- unexecuted or blocked checks;
- human corrections needed;
- failures caused by ADK rules, Skills, activation, or project mismatch.

### P5 — Generalize only verified lessons

A lesson enters core ADK only if it is reusable beyond one project's architecture and has a clear benefit. Otherwise it belongs in a technical Profile, adapter, project configuration, or the project's own documentation.

## Exit criteria

The pilot is ready to expand when:
1. the intended Skills are demonstrably active in the actual coding tool;
2. no project-owned rule or registry has been overwritten;
3. the selected Skills support a bounded task without expanding scope;
4. verification claims match the evidence actually collected;
5. the evaluation result and limitations are recorded;
6. reusable changes are separated from project-specific facts.

## Current status

- Read-only repository inventory: complete for initial planning.
- Structural ADK CI: passing on the latest merged baseline.
- Safe selective installer: merged in ADK; actual installation into consuming projects remains unverified.
- CodeBuddy adapter: native paths and client-specific rule formats are implemented and statically testable; runtime Skill discovery/invocation remains unverified pending a running client smoke test.
- Actual Skill activation in consuming tools: not yet verified.
- Project-side installation PRs: not started.
- Behavioral pilot scenarios: defined, not executed.
