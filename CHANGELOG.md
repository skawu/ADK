# Changelog

This file records user-visible changes to ADK. Entries describe repository content, not assumed runtime behavior.

## 0.1.0-alpha.2 — Structural validation and evaluation fixtures

- Added a standard-library validation script for required files, Skill metadata/sections, version syntax, and local Markdown links.
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
