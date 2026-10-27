---
name: debugging
description: Diagnose a defect or unexpected behavior through reproduction, evidence collection, root-cause analysis, a targeted fix, and regression verification.
---

# Debugging

## Purpose

Find and correct the cause of a failure without replacing evidence-based diagnosis with guesswork.

## Use when

A bug, crash, hang, performance regression, intermittent failure, protocol mismatch, or unexpected device behavior is reported.

## Procedure

1. Capture the expected behavior, observed behavior, frequency, environment, and recent changes.
2. Inspect logs, stack traces, metrics, test failures, protocol traces, or hardware observations that are available and permitted.
3. Build the smallest reproducible case. If it cannot be reproduced, document the limitation and gather discriminating evidence.
4. Form a small set of competing hypotheses. For each, identify an observation or experiment that can confirm or reject it.
5. Run the least risky, most informative checks first. Do not change several unrelated variables at once.
6. Identify the root cause supported by evidence; distinguish it from contributing factors and unresolved hypotheses.
7. Implement a targeted fix and add a regression test or repeatable reproduction where feasible.
8. Re-run the failing scenario and relevant adjacent checks.
9. Review for resource leaks, race conditions, stale state, retry loops, and new failure modes.

## Embedded and production boundaries

Use safe bench, simulator, or captured-data methods where possible. Do not flash or manipulate production hardware without authorization. Clearly distinguish simulated findings from target-device findings.

## Outputs

Reproduction steps, evidence, root cause or unresolved hypotheses, fix summary, regression evidence, and remaining uncertainty.

## Failure handling

If the failure cannot be reproduced or evidence is insufficient to distinguish hypotheses, do not claim a root cause. Report what was observed, which hypotheses remain, and the safest next diagnostic experiment.

## Completion criteria

The reported defect is reproduced and corrected with relevant regression evidence, or the inability to prove the cause is explicitly documented.
