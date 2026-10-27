# Adopting ADK in a Project

## Goal

Apply only the relevant parts of ADK to an existing repository without overwriting its instructions, changing its architecture, or assuming its build environment.

## Initial adoption workflow

1. **Inventory the project.** Inspect repository instructions, directory structure, languages, frameworks, build files, tests, CI, deployment targets, and Git state.
2. **Identify the active instruction path.** Find root/nested AGENTS.md files, tool-specific instruction files, skill directories, and any project-owned registry that decides which rules or Skills are active.
3. **Create a project profile.** Start from templates/PROJECT_PROFILE.md. Record only verified facts; label unknowns as unknown.
4. **Select Profiles.** Choose only the applicable files under profiles/. Record framework/compiler versions and target platforms from project evidence.
5. **Select Skills.** Choose the smallest useful set of Skills. Install only into locations supported by the target tool.
6. **Compose instructions.** Start from templates/AGENTS.md and core/AGENTS.base.md, then add project-specific facts and links. Do not blindly overwrite an existing AGENTS.md.
7. **Register when required.** If the project has a registry or manifest controlling Skill/rule activation, update it according to that project's schema and ownership rules. A copied file is not automatically active.
8. **Record build and test entry points.** Complete templates/BUILD_TEST_MATRIX.md with actual commands, environment requirements, and the meaning of each result.
9. **Review conflicts.** Check existing project rules, architecture decisions, security policy, and ADK guidance. Project-specific facts win over generic assumptions.
10. **Pilot with bounded tasks.** Use representative bug fixes, feature changes, and reviews. Record misses and false positives.
11. **Upgrade deliberately.** Compare the new ADK version with the installed files, inspect the diff, and preserve local modifications.

## Installation policy

The first version is intentionally documentation-first. Do not assume a universal installer or automatic merge strategy exists. Until a tested installer is available, copy selected files manually and review every change.

An installer, when implemented, must:
- detect existing files and local edits;
- support dry-run and explicit file selection;
- avoid destructive overwrites by default;
- identify the ADK version installed in the target project;
- report added, updated, skipped, and conflicting files;
- update any required activation registry only through a project-specific adapter;
- provide a rollback or recovery path.

## Project profile requirements

At minimum, record:
- product purpose and in-scope modules;
- authoritative architecture and interface documents;
- language, framework, compiler, build system, and target versions;
- build/test commands that have been observed to work;
- host and target environments;
- active instruction entry point and Skill/rule activation mechanism;
- data handling and network/cloud constraints;
- hardware risks and required authorization;
- branch, review, and release conventions;
- unresolved assumptions and known verification gaps.

## Pilot and integration boundaries

Start with a read-only compatibility audit. Identify where ADK guidance matches, duplicates, conflicts with, or is not activated by the consuming project. Do not bulk-install ADK into a project simply because it is named as a pilot.

Any project-side installation or adaptation must follow that project's own task ownership, branch/PR, security, and review rules. Keep project-specific product facts, private policies, registry schemas, release gates, and internal architecture details out of the reusable ADK source unless they have been explicitly approved for publication.

## Pilot exit criteria

A pilot is not complete merely because files were copied. It should demonstrate that the AI can correctly identify project facts, load the intended guidance through the actual tool configuration, make a bounded change, run applicable checks, report unexecuted checks honestly, and avoid violating project-specific constraints. Record results in a repeatable evaluation scenario before promoting a lesson to a mandatory rule.
