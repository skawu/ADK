# CodeBuddy IDE and Code CLI Adapter

## Status

The ADK adapter supports the documented project Skill paths for CodeBuddy IDE and CodeBuddy Code CLI. The installer creates client-specific rule files when rules are explicitly selected. This is **static adapter support**, not proof that a running client has discovered or invoked the Skill.

Official references:
- [CodeBuddy IDE — Skills](https://www.codebuddy.ai/docs/ide/Features/Skills)
- [CodeBuddy IDE — Rules](https://www.codebuddy.cn/docs/ide/User-guide/Rules)
- [CodeBuddy Code CLI — directory structure](https://www.codebuddy.ai/docs/cli/codebuddy-dir)
- [CodeBuddy Code CLI — Skills](https://www.codebuddy.ai/docs/cli/skills)

## Select the exact client

| Installer layout | Client | Skill destination | Native rule destination |
|---|---|---|---|
| `codebuddy` | CodeBuddy IDE | `.codebuddy/skills/<name>/SKILL.md` | `.codebuddy/rules/<name>/RULE.mdc` |
| `codebuddy-code` | CodeBuddy Code CLI | `.codebuddy/skills/<name>/SKILL.md` | `.codebuddy/rules/<name>.md` |

Do not use the IDE rule format with the CLI or vice versa. Profiles are copied to `docs/ai-dev/profiles/` for reference. Without either CodeBuddy layout, selected rules are copied as plain reference documents under `docs/ai-dev/rules/`.

## Preview and apply

From the ADK checkout:

```sh
python scripts/adk_install.py --target ../your-project --layout codebuddy \
  --skill qt-qml-development --skill build-test-verify \
  --profile qt-qml --rule engineering-behavior
```

For CodeBuddy Code CLI, use `--layout codebuddy-code`. The installer is dry-run by default; review every planned destination, then add `--apply` only after the plan is acceptable.

## Instructions, rules, and registries

- The installer does not create, replace, or edit `AGENTS.md`, `CODEBUDDY.md`, `.codebuddy/CODEBUDDY.md`, `.codebuddy/settings.json`, or a project-owned registry such as `.agents/registry.json`.
- CodeBuddy IDE documents compatibility loading of root `AGENTS.md` when root `CODEBUDDY.md` is absent. If a project already has either instruction file, inspect the actual precedence rather than generating a second entry point.
- CodeBuddy Code has its own `CODEBUDDY.md` project-memory convention. Do not create one automatically to make generic ADK rules load; doing so can change which project instructions the tool sees.
- Rules are generated with `alwaysApply: false`; the adapter does not force generic rules into every prompt. Confirm their actual selection behavior in a new conversation.
- If the project maintains a separate registry, ownership manifest, or allowlist for Skills, update it only through that project's own reviewed workflow. Native CodeBuddy discovery does not replace project governance.
- A copied file, a manifest entry, or a green ADK CI run does not prove that the actual client loaded or invoked a Skill.

## Activation smoke test

Use [the CodeBuddy activation scenario](../../evals/scenarios/07-codebuddy-activation.md) and the isolated [smoke fixture](../../evals/fixtures/codebuddy-smoke/README.md).

1. Open the fixture as the workspace root in the actual CodeBuddy client.
2. Start a new conversation after adding or changing rules.
3. Confirm the Skill appears in the CodeBuddy IDE project Skills UI or the CodeBuddy Code CLI `/skills` listing.
4. Ask the client to invoke the `adk-activation-smoke` Skill and report its activation token. Use the scenario's exact prompt.
5. Record the client/product version, visible discovery evidence, invocation evidence, token result, and whether any project instructions were unexpectedly shadowed.
6. If the Skill is listed but does not trigger, adjust its description or activation route and repeat. Do not report PASS based on file presence alone.

## Known limits

- ADK does not currently control a CodeBuddy process or query its live loaded-Skill state.
- The adapter tests prove path generation, metadata shape, conflict handling, and preservation of project-owned files. Only a smoke test in the actual CodeBuddy client can establish runtime discovery/invocation.
- The installer is a copy tool, not a registry migration or merge tool. Conflicting existing destinations block the entire operation.
