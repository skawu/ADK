# ADK Architecture

## 1. Purpose

ADK is a versioned source of reusable engineering guidance for AI-assisted software development. It supplies instructions and repeatable workflows that can be adapted to a repository. It does not execute tasks, host models, manage agent processes, or replace project governance.

## 2. Layers

### Core instructions and rules

The root AGENTS.md guides work in this repository. core/AGENTS.base.md is a source template for a consuming project's generated or assembled AGENTS.md. Core rules describe stable cross-project requirements: engineering behavior, security and data handling, change control, and evidence-based delivery.

### Skills

A Skill describes a repeatable workflow with explicit triggers, steps, outputs, and failure handling. Skills should be loaded when relevant, not copied wholesale into every prompt. The repository source location is skills/<skill-name>/SKILL.md. An adapter may install these into the target tool's supported skill directory, such as .agents/skills, after verifying the target tool's conventions.

### Technical Profiles

Profiles provide technology-specific checks and constraints. They are not universal mandates. Select only the Profiles relevant to the repository and reconcile them with the actual compiler, framework version, target hardware, and existing architecture.

### Project layer

The consuming repository owns its product requirements, architecture, interface contracts, build commands, test matrix, safety case, release policy, and decisions. ADK must not invent these facts. The project layer may add stricter rules or explicitly document justified exceptions.

### Adapters and validation

Adapters translate the source kit into the conventions of a particular coding environment. Validation checks file structure and metadata; evaluations test whether an AI follows the guidance in representative tasks. These are distinct: a structurally valid kit is not proof that it improves engineering outcomes.

## 3. Authority and conflict resolution

Use this order when reconciling guidance:

1. Applicable law, organizational security policy, and explicit user authorization boundaries.
2. Confirmed project requirements, architecture decisions, interface contracts, and safety constraints.
3. Relevant project-level instructions and tool-specific constraints.
4. ADK core rules and selected technical Profiles.
5. Skill defaults and AI-generated assumptions.

A lower layer cannot silently override a higher one. If a material conflict prevents safe or correct work, state the conflict and propose options. Do not turn a project-specific convention into a universal ADK requirement without evidence.

## 4. Rule, Skill, Profile, or script?

- **Rule:** a persistent constraint that must apply whenever its scope matches.
- **Skill:** a conditional workflow used for a class of tasks.
- **Profile:** technology-specific knowledge and checks selected by a project.
- **Template:** a starting point that must be filled with project facts.
- **Script/check:** a deterministic test for a machine-verifiable property.
- **Evaluation scenario:** a controlled case used to test behavior, not merely file syntax.

Prefer deterministic checks for objective requirements. Use review and evaluation for architectural or semantic judgments that cannot be reliably reduced to a script.

## 5. Design constraints

- Minimize duplicated instructions.
- Keep the root AGENTS.md concise.
- Separate reusable practices from project facts.
- Make claims proportional to evidence.
- Avoid tool-specific features in core content unless the feature is clearly marked and isolated in an adapter.
- Preserve local development and data-boundary constraints from the consuming project.
