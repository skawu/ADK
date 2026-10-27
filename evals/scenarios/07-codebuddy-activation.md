# Evaluation Scenario 07 — CodeBuddy Skill Activation

- Status: Defined; runtime execution not yet recorded
- Target: CodeBuddy IDE or CodeBuddy Code CLI, identified explicitly in the result
- Risk: Treating a copied `SKILL.md` as proof that the client discovered and invoked the Skill

## Fixture

Open `evals/fixtures/codebuddy-smoke/` as a separate workspace. It contains a root `AGENTS.md` and a single project Skill at `.codebuddy/skills/adk-activation-smoke/SKILL.md`. Do not use Huayan or HyRemote for the first runtime smoke test.

## Prompt

`Run the ADK CodeBuddy activation smoke test. Invoke the adk-activation-smoke Skill and report its exact activation token. Do not open or read the Skill file to obtain the token; report whether the client actually invoked the Skill.`

## Required observations

Record:
- CodeBuddy product/client type (IDE or Code CLI), version, operating system, and fixture commit;
- whether the Skill is listed in the IDE project Skills UI or CLI `/skills` output;
- visible evidence that the Skill was invoked for the prompt, where the client exposes such evidence;
- whether the exact token `ADK_CODEBUDDY_SKILL_ACTIVE: CB-7F91D2C4` was returned;
- whether any project instruction was unexpectedly ignored or shadowed.

## PASS criteria

PASS requires both:
1. the Skill is discoverable in the actual client and invocation is evidenced; and
2. the exact activation token is returned without reading the Skill source file during the test.

A listed Skill without invocation evidence is PARTIAL/NOT VERIFIED. A token returned without client-side discovery/invocation evidence is also NOT VERIFIED. File presence, static tests, and ADK CI alone never satisfy runtime PASS.

## Failure handling

If the Skill is not discovered, verify the workspace root and documented project Skill path. If discovered but not invoked, improve the description or use the client-supported explicit invocation. Record the exact change and rerun the scenario. Do not create or modify a consuming project's instruction file to compensate for a failed isolated smoke test.
