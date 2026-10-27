# ADK Adapters

## Purpose

Adapters describe how to map ADK source content into an AI coding tool and an existing project's activation mechanism. They must not silently replace project instructions or assume that a copied file is active.

## Current status

- [Codex-style repository layout](codex/README.md): manual mapping guidance only.
- Automated installation, upgrade, merge, and rollback are not implemented.
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

## Installer requirements

Any future installer must support dry-run, selected components, conflict detection, preservation of local edits, version tracking, an explicit update plan, and a recovery path. It must not overwrite AGENTS.md or project registries by default.
