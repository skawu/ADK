# ADK Repository Instructions

## Purpose

This repository maintains ADK, a reusable set of AI engineering instructions, rules, skills, technical profiles, templates, and validation scenarios. ADK is not an agent runtime or task scheduler.

## Before changing files

1. Read the relevant sections of README.md and docs/architecture.md.
2. Inspect existing files and Git state before proposing or making changes.
3. Distinguish reusable engineering guidance from Huayan- or HyRemote-specific facts.
4. Check whether a proposed rule already exists; avoid duplicate or contradictory instructions.
5. Treat a lesson as a candidate until its scope and evidence justify making it normative.

## Authoring requirements

- Write normative instructions as observable actions and decision criteria, not vague slogans.
- State applicability and exceptions where they matter.
- Keep root-level instructions concise. Put detailed workflows in Skills and technology-specific constraints in Profiles.
- Keep project-specific decisions in the consuming project's own documentation.
- Never claim a script, workflow, or evaluation passed unless it was actually executed and its result is available.
- Prefer changes that can be reviewed and tested independently.

## Validation and delivery

For every change, inspect the diff and check references, file paths, terminology, and consistency across rules, skills, profiles, and templates. Run available validation checks when present. If checks are unavailable or not run, say so explicitly.

A delivery report must state what changed, what was checked, the actual result, known limitations, and the next action. Do not treat a planned capability as implemented.

## Change boundaries

Do not silently add a license, select a universal coding standard, require one Git branching strategy for every project, or make external network/cloud use mandatory. Do not modify consuming projects merely to make them conform to ADK unless that work is explicitly in scope.
