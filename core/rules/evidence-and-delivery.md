# Core Rule: Evidence and Delivery

## Verification states

ADK uses the following reference states:

- **PASS** — the specified check was actually run and met its stated acceptance criteria.
- **FAIL** — the check was run and did not meet its criteria.
- **BLOCKED** — the check could not be run because of a stated prerequisite, permission, environment, or dependency.
- **NOT RUN** — the check was not attempted. Do not use this to disguise a known failure.
- **NOT APPLICABLE** — the check does not apply to the changed behavior; explain why when non-obvious.

A consuming project may define additional or different terms, such as NOT VERIFIED. Preserve the project's required vocabulary and map it to these reference states only when the project policy calls for that mapping. Do not replace project status semantics with ADK defaults.

A successful build is not proof that behavior is correct. A host test is not proof of target-hardware behavior. A green CI status is not evidence for checks that did not execute. A test that was not run is not a pass.

## Evidence contract

For each material claim or acceptance check, identify:

- **Property:** the behavior or product promise being evaluated.
- **Subject:** the commit/artifact, configuration, toolchain, platform, and target environment to which the result applies.
- **Action:** the test, command, inspection, or observation actually performed.
- **Oracle:** the observable condition that determines PASS or FAIL.
- **Result:** the status and relevant output.
- **Invalidation:** changes that make retained evidence no longer applicable, such as a new commit, toolchain, configuration, target, or material interface change.

Do not treat a screenshot, log, benchmark value, registered test, or workflow definition as self-interpreting evidence. The result must be tied to the relevant subject and an explicit oracle. Exact commit or artifact identity is required whenever the claim depends on a specific version.

## Risk-proportional verification

- Choose the cheapest evidence that can honestly prove the changed property.
- Scale test scope and cost with the change's risk and affected contracts.
- A documentation-only change does not automatically require full hardware qualification; a deployment or ABI change may require stronger environment-specific evidence even when the code diff is small.
- Avoid redundant tests that prove the same property at the same layer without additional value.
- Never substitute cheaper evidence when the product claim requires a stronger environment, integration path, or physical observation.
- Zero discovered or executed tests are not evidence of a passing test suite.
- Follow the consuming project's policy for whether hosted CI evidence may be inspected or used.

## Required delivery report

For meaningful engineering changes, report:

1. Summary of the behavior or artifact changed.
2. Important files or interfaces affected.
3. Checks actually run, with commands or test identifiers and actual results.
4. Checks not run or blocked, with reasons.
5. Known risks, assumptions, compatibility impacts, and remaining work.
6. Commit/PR references when those operations actually occurred.

## Evidence quality

- Prefer reproducible commands, test output, CI links, and direct repository evidence where project policy permits their use.
- Keep claims proportional to the evidence available.
- Do not fabricate command output, measurements, CI status, approvals, hardware observations, or source references.
- If a check's environment differs from the target, name the difference.
- Record failed and blocked checks; do not omit them from the summary.

## Completion

A task is complete only when its agreed acceptance criteria are met or the remaining gaps are explicitly accepted by the authorized decision-maker. If a required check is blocked, report the task's actual status rather than declaring unconditional success.
