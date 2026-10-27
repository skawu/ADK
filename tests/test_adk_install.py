"""Unit tests for the safe selective ADK installer."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.adk_install import InstallError, apply_plan, build_plan, classify_plan


class AdkInstallTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.source = self.root / "adk-source"
        self.target = self.root / "consumer"
        self.source.mkdir()
        self.target.mkdir()

        (self.source / "VERSION").write_text("0.1.0-alpha.6\n", encoding="utf-8")
        skill = self.source / "skills" / "qt-qml-development" / "SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("skill source\n", encoding="utf-8")
        profile = self.source / "profiles" / "qt-qml.md"
        profile.parent.mkdir(parents=True)
        profile.write_text("profile source\n", encoding="utf-8")
        rule = self.source / "core" / "rules" / "engineering-behavior.md"
        rule.parent.mkdir(parents=True)
        rule.write_text("rule source\n", encoding="utf-8")

        (self.target / "AGENTS.md").write_text("project-owned instructions\n", encoding="utf-8")
        registry = self.target / ".agents" / "registry.json"
        registry.parent.mkdir(parents=True)
        registry.write_text('{"project":"owned"}\n', encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def make_plan(self, layout: str = "codex"):
        return build_plan(
            self.source,
            self.target,
            layout,
            ["qt-qml-development"],
            ["qt-qml"],
            ["engineering-behavior"],
        )

    def test_plan_is_dry_run_and_does_not_write_files(self) -> None:
        items, warnings = self.make_plan()
        statuses = [status for _, status in classify_plan(self.target, items)]
        self.assertTrue(all(status == "ADD" for status in statuses))
        self.assertFalse((self.target / ".agents" / "skills").exists())
        self.assertTrue(any("registry.json" in warning for warning in warnings))

    def test_apply_copies_selected_files_and_preserves_project_owned_files(self) -> None:
        items, _ = self.make_plan()
        created = apply_plan(self.target, items)
        self.assertEqual(len(items), len(created))
        self.assertEqual(
            "skill source\n",
            (self.target / ".agents/skills/qt-qml-development/SKILL.md").read_text(encoding="utf-8"),
        )
        self.assertEqual(
            "profile source\n",
            (self.target / "docs/ai-dev/profiles/qt-qml.md").read_text(encoding="utf-8"),
        )
        self.assertEqual("project-owned instructions\n", (self.target / "AGENTS.md").read_text(encoding="utf-8"))
        self.assertEqual('{"project":"owned"}\n', (self.target / ".agents/registry.json").read_text(encoding="utf-8"))
        manifest = json.loads((self.target / "docs/ai-dev/ADK-MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual("manual-verification-required", manifest["activation_status"])
        self.assertTrue(manifest["project_registry_detected"])
        self.assertFalse(manifest["project_registry_modified"])

    def test_docs_only_layout_does_not_place_skills_in_tool_directory(self) -> None:
        items, _ = self.make_plan(layout="docs-only")
        apply_plan(self.target, items)
        self.assertTrue((self.target / "docs/ai-dev/skills/qt-qml-development/SKILL.md").is_file())
        self.assertFalse((self.target / ".agents/skills/qt-qml-development/SKILL.md").exists())

    def test_conflict_blocks_all_writes(self) -> None:
        existing = self.target / ".agents/skills/qt-qml-development/SKILL.md"
        existing.parent.mkdir(parents=True)
        existing.write_text("local content\n", encoding="utf-8")
        items, _ = self.make_plan()
        with self.assertRaises(InstallError):
            apply_plan(self.target, items)
        self.assertFalse((self.target / "docs/ai-dev/profiles/qt-qml.md").exists())
        self.assertFalse((self.target / "docs/ai-dev/ADK-MANIFEST.json").exists())
        self.assertEqual("local content\n", existing.read_text(encoding="utf-8"))

    def test_repeating_identical_install_is_idempotent(self) -> None:
        items, _ = self.make_plan()
        apply_plan(self.target, items)
        second_items, _ = self.make_plan()
        statuses = [status for _, status in classify_plan(self.target, second_items)]
        self.assertTrue(all(status == "UNCHANGED" for status in statuses))
        self.assertEqual([], apply_plan(self.target, second_items))

    def test_codebuddy_ide_layout_uses_native_skill_and_rule_paths(self) -> None:
        items, warnings = self.make_plan(layout="codebuddy")
        by_path = {item.relative_path: item.content for item in items}
        self.assertIn(".codebuddy/skills/qt-qml-development/SKILL.md", by_path)
        rule = by_path[".codebuddy/rules/engineering-behavior/RULE.mdc"]
        self.assertIn('description: "ADK reusable engineering rule: engineering-behavior"', rule)
        self.assertIn("alwaysApply: false", rule)
        self.assertIn("enabled: true", rule)
        self.assertIn("project-specific facts take precedence", rule)
        self.assertTrue(any("actual client" in warning for warning in warnings))

    def test_codebuddy_code_layout_uses_markdown_rule_files(self) -> None:
        items, _ = self.make_plan(layout="codebuddy-code")
        by_path = {item.relative_path: item.content for item in items}
        self.assertIn(".codebuddy/skills/qt-qml-development/SKILL.md", by_path)
        rule = by_path[".codebuddy/rules/engineering-behavior.md"]
        self.assertIn("alwaysApply: false", rule)
        self.assertNotIn("enabled: true", rule)
        self.assertIn("project-specific facts take precedence", rule)

    def test_codebuddy_conflict_blocks_all_writes(self) -> None:
        existing = self.target / ".codebuddy/skills/qt-qml-development/SKILL.md"
        existing.parent.mkdir(parents=True)
        existing.write_text("client-owned skill\n", encoding="utf-8")
        items, _ = self.make_plan(layout="codebuddy")
        with self.assertRaises(InstallError):
            apply_plan(self.target, items)
        self.assertEqual("client-owned skill\n", existing.read_text(encoding="utf-8"))
        self.assertFalse((self.target / "docs/ai-dev/profiles/qt-qml.md").exists())
        self.assertFalse((self.target / "docs/ai-dev/ADK-MANIFEST.json").exists())

    def test_codebuddy_layout_preserves_instruction_files_and_project_registry(self) -> None:
        (self.target / "CODEBUDDY.md").write_text("client-owned instructions\n", encoding="utf-8")
        items, warnings = self.make_plan(layout="codebuddy")
        apply_plan(self.target, items)
        self.assertEqual("project-owned instructions\n", (self.target / "AGENTS.md").read_text(encoding="utf-8"))
        self.assertEqual("client-owned instructions\n", (self.target / "CODEBUDDY.md").read_text(encoding="utf-8"))
        self.assertEqual('{"project":"owned"}\n', (self.target / ".agents/registry.json").read_text(encoding="utf-8"))
        manifest = json.loads((self.target / "docs/ai-dev/ADK-MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(["AGENTS.md", "CODEBUDDY.md"], manifest["project_instruction_files_detected"])
        self.assertTrue(manifest["project_registry_detected"])
        self.assertFalse(manifest["project_registry_modified"])
        self.assertTrue(any("CODEBUDDY.md" in warning for warning in warnings))

    def test_target_inside_source_tree_is_rejected(self) -> None:
        nested_target = self.source / "consumer"
        nested_target.mkdir()
        with self.assertRaises(InstallError):
            build_plan(
                self.source,
                nested_target,
                "codex",
                ["qt-qml-development"],
                [],
                [],
            )

    def test_unknown_component_is_rejected(self) -> None:
        with self.assertRaises(InstallError):
            build_plan(self.source, self.target, "codex", ["missing-skill"], [], [])


if __name__ == "__main__":
    unittest.main()
