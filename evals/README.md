# ADK Evaluation and Regression Scenarios

## Purpose

Evaluate whether ADK guidance changes AI behavior in representative engineering tasks. File and metadata validation is necessary but not sufficient.

## Scenario record

Each scenario should contain:
- **ID and version** — stable identifier and the ADK version under test.
- **Project context** — sanitized repository fixture or a precise description of the relevant facts.
- **Task prompt** — the request given to the AI.
- **Risk being tested** — for example, invented build commands, out-of-scope refactor, false test claim, unsafe firmware operation, or failure to inspect project instructions.
- **Expected behavior** — observable actions and decision boundaries.
- **Forbidden behavior** — concrete failures that must not occur.
- **Evidence** — files changed, commands run, report produced, and evaluator notes.
- **Result** — PASS, FAIL, BLOCKED, or NOT RUN, with rationale.

## Initial scenario families

1. Repository onboarding: identifies the actual build system and marks unknowns instead of guessing.
2. Bounded bug fix: avoids unrelated refactoring and adds relevant regression coverage.
3. Verification honesty: reports unavailable tests as BLOCKED or NOT RUN, not PASS.
4. Qt threading/lifetime: respects QObject affinity and asynchronous object lifetime.
5. Go cancellation: checks goroutine lifetime, context propagation, and shutdown.
6. Firmware safety: does not flash or erase hardware without authorization.
7. Mixed-system interface: assesses producer/consumer compatibility and integration validation.
8. Security boundary: does not expose secrets or transfer restricted code to an unapproved service.

## Promotion policy

A recurring failure can motivate a rule or Skill change, but a single anecdote is not enough to establish universal applicability. Record the failure, root cause, proposed control, expected trade-off, and regression scenario. Promote it after review and, where practical, successful evaluation in more than one relevant project.

No evaluation result should be described as passing until the scenario has actually been executed and evidence reviewed.
