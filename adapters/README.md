# ADK Adapters

## Purpose

Adapters describe how to map ADK source content into an AI coding tool and an existing project's activation mechanism. They must not silently replace project instructions or assume that a copied file is active.

## Current status

- [Codex-style repository layout](codex/README.md): manual mapping guidance.
- A safe selective-copy installer is available at scripts/adk_install.py. Dry-run is the default.
- The installer does not modify AGENTS.md or project-owned registries and does not prove that copied Skills are active.
- Automated upgrade/merge of conflicting files and end-to-end activation testing in every tool are not implemented.
- Other coding environments require their own documented and tested adapter before being described as supported.

## Source-to-target mapping

- Core rules are maintained under core/rules/.
- Technology Profiles are maintained under profiles/.
- Skills are maintained under skills/<skill-name>/SKILL.md.
- Project templates are maintained under templates/.

A consuming project should install only selected content. The project's active AGENTS.md or tool-specific instructions must reference any installed rules that are not loaded automatically.

## Project registries

Some repositories maintain a registry or manifest that tracks Skill/rule status, ownership, activation conditions, risk, or replacement relationships. Treat that registry as project-owned data. Its schema is not standardized by ADK. Before adding a Skill:
1. identify how the target tool discovers Skills;
2. identify whether a separate project registry controls activation;
3. preserve existing metadata and ownership rules;
4. update the registry only through an explicit project-specific change;
5. verify activation in the actual tool rather than inferring it from file presence.

## Installer behavior

- Without --apply, the installer only prints the proposed file plan.
- With --apply, it creates selected files only when destinations do not exist.
- Identical existing files are treated as unchanged; differing files are conflicts.
- Any conflict blocks the entire operation before writes begin.
- If a write fails after application starts, newly created files are removed on a best-effort basis.
- AGENTS.md, tool configuration, and project registries are never modified.
- Replacing or upgrading an existing ADK manifest is not supported yet; review conflicts manually.

The installer is intentionally conservative. It optimizes for preserving existing project state, not for silently completing all activation steps.
