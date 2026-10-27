# Changelog

This file records user-visible changes to ADK. Entries describe repository content, not assumed runtime behavior.

## 0.1.0-alpha.6 — CodeBuddy adapter and activation smoke fixture

- Added separate CodeBuddy IDE and CodeBuddy Code CLI layouts because their native rule-file formats differ.
- Added native project Skill placement under .codebuddy/skills/ and client-specific rule mapping.
- Kept project instructions, project settings, and custom registries untouched; installer manifests require runtime activation verification.
- Added a CodeBuddy activation smoke fixture and evaluation scenario.
- Structural tests cover the generated paths and metadata; actual activation in a running CodeBuddy client remains unverified.

## 0.1.0-alpha.5 — Safe selective installer

- Added a standard-library installer that previews selected rules, Profiles, and Skills by default.
- Added explicit apply mode, conflict detection, idempotent handling of identical files, and rollback of newly created files on write failure.
- The installer never overwrites existing files and does not modify AGENTS.md or project-owned registries.
- Added installer unit tests and extended kit validation to require the installer and its tests.
- Actual installation and Skill activation in consuming projects remain unverified.

## 0.1.0-alpha.4 — Project compatibility and pilot plan

- Added a two-project pilot plan based on a read-only review of different instruction/activation and build/evidence models.
- Clarified that ADK status vocabulary and hosted-CI practices must not override project-owned policy.
- Added a manual evaluation scenario for project policy precedence and activation boundaries.
- No consuming project was modified by this change.

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
