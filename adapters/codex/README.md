# Codex-Style Repository Mapping

## Status

Manual mapping guidance. This directory does not contain an installer and does not claim end-to-end activation has been tested in every Codex version.

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

## Manual setup

1. Inspect existing AGENTS.md and all nested instruction files.
2. Select only relevant ADK rules, Profiles, and Skills.
3. Copy selected Skills into the tool-supported Skill directory without overwriting existing Skills.
4. Link the project AGENTS.md to the selected rule/Profile documents and relevant Skills.
5. If a project-owned registry controls activation, update it through the project's own schema and review process.
6. Test activation with a bounded task: ask the tool to identify the active instruction/Skill and demonstrate the expected workflow.
7. Record the installed ADK version and local changes in the project profile.

## Limitations

This adapter is not a universal rules engine. Tool versions may differ in file discovery, instruction precedence, and Skill metadata support. If the target behavior is not verified, report it as unverified and do not claim that ADK is fully installed.
