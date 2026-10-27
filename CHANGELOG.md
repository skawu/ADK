# Changelog

This file records user-visible changes to ADK. Entries describe repository content, not assumed runtime behavior.

## 0.1.0-alpha.3 — Technical Skills and adapter guidance

- Added technology-specific Skills for Qt/QML, C++, Go, and embedded/MCU work.
- Clarified that copying a Skill file does not prove that the target tool or project registry activates it.
- Added manual adapter guidance for a Codex-style project layout and custom project registries.
- Strengthened evidence requirements with explicit oracle, artifact/environment identity, invalidation, and risk-proportional verification.
- Extended structural validation to require adapter documentation and all core/technical Skills.

## 0.1.0-alpha.2 — Structural validation and evaluation fixtures

- Added a standard-library validator for required files, required core Skills, semantic-version syntax, Skill metadata/sections, and local Markdown links.
- Added unit tests for valid structure and common validation failures.
- Added GitHub Actions workflow to run unit tests and kit validation on pushes and pull requests.
- Added initial manual evaluation scenarios for onboarding, scope control, verification honesty, and firmware safety.
- Evaluation scenarios are specifications only; no behavioral evaluation result is claimed.

## 0.1.0-alpha.1 — Initial foundation

- Initialized ADK as a reusable AI engineering kit, separate from agent runtime and orchestration systems.
- Established core rules for engineering behavior, security/data boundaries, change control, and evidence-based delivery.
- Added initial technical Profiles for Qt/QML, C++/CMake, Go, embedded/MCU, and mixed systems.
- Added reusable project templates and the first set of core Skills.
- Defined adoption, Skill authoring, and evaluation principles.
