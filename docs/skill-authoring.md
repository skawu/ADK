# Skill Authoring Standard

## Required file format

Each Skill lives at skills/<skill-name>/SKILL.md and begins with YAML frontmatter containing:
- name: a stable, lowercase, hyphen-separated identifier;
- description: a concise explanation of what the Skill does and when it should be used.

The Skill body should be independently understandable. Do not rely on hidden conversation context.

## Required sections

1. **Purpose** — the job the Skill is responsible for.
2. **Use when** — concrete triggers; include exclusions where needed.
3. **Inputs and prerequisites** — files, facts, tools, permissions, and environment assumptions to establish.
4. **Procedure** — ordered, actionable steps.
5. **Decision points** — what can proceed autonomously and what requires authorization.
6. **Outputs** — artifacts, evidence, or report fields expected.
7. **Failure handling** — how to report blockers, missing data, and failed checks.
8. **Completion criteria** — observable evidence that the workflow is complete.

## Quality requirements

- Use imperative, testable language.
- Do not duplicate the full core rules; link to them and explain the Skill-specific application.
- Do not assume a particular shell, operating system, framework version, CI provider, or repository layout unless the Skill is scoped to it.
- Distinguish commands that were actually executed from commands suggested for later execution.
- Never instruct the AI to fabricate logs, test results, measurements, source citations, or approvals.
- State the safe default for destructive or irreversible operations.
- Prefer concise procedures over long collections of generic advice.
- Keep tool-specific syntax in an adapter or a clearly marked subsection.
- When adding or changing a Skill, add at least one evaluation scenario that exercises its most important behavior when practical.

## Naming and maintenance

Use one Skill per coherent workflow, not one Skill per tiny action. Keep the directory name, frontmatter name, and references consistent. Update the changelog when a released or published version materially changes Skill behavior.
