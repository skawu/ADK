# Core Rule: Evidence and Delivery

## Verification states

Use these meanings consistently:

- **PASS** — the specified check was actually run and met its stated acceptance criteria.
- **FAIL** — the check was run and did not meet its criteria.
- **BLOCKED** — the check could not be run because of a stated prerequisite, permission, environment, or dependency.
- **NOT RUN** — the check was not attempted. Do not use this to disguise a known failure.
- **NOT APPLICABLE** — the check does not apply to the changed behavior; explain why when non-obvious.

A successful build is not proof that behavior is correct. A host test is not proof of target-hardware behavior. A test that was not run is not a pass.

## Required delivery report

For meaningful engineering changes, report:

1. Summary of the behavior or artifact changed.
2. Important files or interfaces affected.
3. Checks actually run, with commands or test identifiers and actual results.
4. Checks not run or blocked, with reasons.
5. Known risks, assumptions, compatibility impacts, and remaining work.
6. Commit/PR references when those operations actually occurred.

## Evidence quality

- Prefer reproducible commands, test output, CI links, and direct repository evidence.
- Keep claims proportional to the evidence available.
- Do not fabricate command output, measurements, CI status, approvals, hardware observations, or source references.
- If a check's environment differs from the target, name the difference.
- Record failed and blocked checks; do not omit them from the summary.

## Completion

A task is complete only when its agreed acceptance criteria are met or the remaining gaps are explicitly accepted by the authorized decision-maker. If a required check is blocked, report the task's actual status rather than declaring unconditional success.
