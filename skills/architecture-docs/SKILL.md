---
name: architecture-docs
description: Create or update engineering architecture and decision documents based on verified requirements, current implementation, and explicit trade-offs.
---

# Architecture Documentation

## Purpose

Keep architecture documents useful, traceable, and consistent with the actual system rather than aspirational or speculative.

## Use when

A task changes module boundaries, interfaces, deployment topology, data flow, concurrency model, technology decisions, or operational assumptions.

## Procedure

1. Identify the decision or behavior that needs documentation and its audience.
2. Read current implementation, existing architecture documents, relevant requirements, and prior decisions.
3. Separate current state, proposed change, alternatives, assumptions, and open questions.
4. Describe component responsibilities, interfaces, lifecycle, failure handling, data flow, and deployment implications where relevant.
5. Record meaningful alternatives and trade-offs; do not list options without explaining why they matter.
6. Link claims to source files, tests, interface specs, or decisions when possible.
7. Update the appropriate existing document rather than creating a competing source of truth.
8. Check that terminology, diagrams, examples, and interface names match the implementation.
9. Identify any decision that needs explicit approval and recommend an option.

## Outputs

An updated architecture document or ADR with scope, context, decision, alternatives, consequences, verification approach, and open issues as applicable.

## Completion criteria

The document accurately distinguishes current facts from proposed design and leaves no material ambiguity about the decision being recorded.
