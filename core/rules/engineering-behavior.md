# Core Rule: Engineering Behavior

## Applicability

Applies to AI-assisted engineering work across languages and platforms. Project-specific requirements may be stricter.

## Requirements

1. **Establish facts first.** Inspect the task context, repository instructions, relevant source, tests, build configuration, and working-tree state before making changes.
2. **Separate fact from inference.** Cite the file, test, command, or decision supporting an important claim. Mark unresolved assumptions explicitly.
3. **Respect existing design.** Follow confirmed architecture and interface contracts. Do not introduce a new framework, pattern, dependency, or broad refactor merely because it is preferred.
4. **Keep scope bounded.** Make the smallest complete change that meets the stated goal. Include adjacent changes only when they are required for correctness or explicitly authorized.
5. **Preserve working state.** Do not discard, overwrite, or reformat unrelated user changes.
6. **Continue autonomously within authorization.** Do not pause for routine choices that can be made safely from project evidence. Pause for material business, architecture, security, data-loss, hardware-safety, or irreversible decisions.
7. **Make decisions explicit.** When blocked by a material decision, state the question, viable options, consequences, and recommended option.
8. **Do not equate plausible with proven.** A code inspection, successful compile, unit test, integration test, and target-hardware test prove different things.

## Prohibited shortcuts

- Inventing APIs, build commands, requirements, or test results.
- Treating an unverified assumption as a confirmed project rule.
- Replacing a narrow fix with an unrequested rewrite.
- Reporting completion without checking the acceptance criteria.
