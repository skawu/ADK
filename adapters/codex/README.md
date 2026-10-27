# Codex-Style Repository Mapping

## Status

Manual mapping guidance. The installer can copy selected Skills into a Codex-style target layout, but end-to-end activation is not automatically verified for every Codex version.

## Source and target layout

ADK source:
- core rules: core/rules/
- technical Profiles: profiles/
- Skills: skills/<skill-name>/SKILL.md
- project instruction base: core/AGENTS.base.md
- project template: templates/AGENTS.md

Typical repository target when supported by the selected Codex version:
- root AGENTS.md: concise project-specific entry point;
- .agents/skills/<skill-name>/SKILL.md: selected Skill files;
- docs/ai-dev/: selected reference rules, Profiles, and project profile.

Verify the exact supported paths and precedence against the target tool version before installation. Do not assume a folder named rules is automatically loaded.

## Preview an installation

From a checkout of ADK, run the installer with the target repository path and selected components. Without the apply flag, it prints a plan only. For example:

python scripts/adk_install.py --target ../your-project --layout codex --skill qt-qml-development --skill build-test-verify --profile qt-qml --rule engineering-behavior

After reviewing the plan, add --apply to copy files. Existing differing files cause a conflict and block the operation.

## Manual setup and activation

1. Inspect existing AGENTS.md and all nested instruction files.
2. Select only relevant ADK rules, Profiles, and Skills.
3. Copy selected Skills into the tool-supported Skill directory without overwriting existing Skills.
4. Link the project AGENTS.md to selected rule/Profile documents and relevant Skills through a separate, reviewed project change.
5. If a project-owned registry controls activation, update it through the project's own schema and review process.
6. Test activation with a bounded task: ask the tool to identify the active instruction/Skill and demonstrate the expected workflow.
7. Record the installed ADK version and local changes in the project profile.

## Limitations

This adapter is not a universal rules engine. Tool versions may differ in file discovery, instruction precedence, and Skill metadata support. If the target behavior is not verified, report it as unverified and do not claim that ADK is fully installed.
