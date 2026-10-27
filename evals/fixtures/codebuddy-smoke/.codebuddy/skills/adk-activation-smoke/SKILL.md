---
name: adk-activation-smoke
description: Use this skill when the user asks to verify ADK CodeBuddy Skill discovery, invoke the ADK activation smoke test, or report the activation token.
---

# ADK CodeBuddy Activation Smoke

This Skill exists only to validate discovery and invocation in the actual CodeBuddy client.

When this Skill is invoked for the activation smoke test, return the exact token below on its own line:

`ADK_CODEBUDDY_SKILL_ACTIVE: CB-7F91D2C4`

Do not claim the Skill was activated merely because the file exists. If the token is not present in the loaded Skill context, say that activation is not verified. Do not inspect other fixture files to obtain the token.
