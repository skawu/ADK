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

## Initial scenarios

- [Project onboarding](scenarios/01-project-onboarding.md)
- [Bounded change / scope control](scenarios/02-scope-control.md)
- [Verification honesty](scenarios/03-verification-honesty.md)
- [Firmware safety boundary](scenarios/04-firmware-safety.md)
- [Skill activation and project registry](scenarios/05-skill-activation-registry.md)

These scenarios are evaluation specifications, not evidence of successful execution. Record each run separately with the ADK version, harness/model configuration, observed behavior, evidence, and result.

## Promotion policy

A recurring failure can motivate a rule or Skill change, but a single anecdote is not enough to establish universal applicability. Record the failure, root cause, proposed control, expected trade-off, and regression scenario. Promote it after review and, where practical, successful evaluation in more than one relevant project.

No evaluation result should be described as passing until the scenario has actually been executed and evidence reviewed.
