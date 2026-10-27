"""Unit tests for the ADK structure validator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_kit import REQUIRED_FILES, validate_kit


VALID_SKILL = """---
name: demo-skill
description: Demonstrate a valid Skill for validator tests.
---

# Demo Skill

## Purpose

Test purpose.

## Use when

Test trigger.

## Procedure

Test procedure.

## Outputs

Test output.

## Failure handling

Test failure handling.

## Completion criteria

Test completion.
"""


class ValidateKitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        for relative in REQUIRED_FILES:
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("placeholder\n", encoding="utf-8")

        (self.root / "VERSION").write_text("0.1.0-alpha.1\n", encoding="utf-8")
        skill_dir = self.root / "skills" / "demo-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(VALID_SKILL, encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_valid_minimal_kit_passes(self) -> None:
        self.assertEqual([], validate_kit(self.root))

    def test_missing_required_file_is_reported(self) -> None:
        (self.root / "profiles" / "go.md").unlink()
        errors = validate_kit(self.root)
        self.assertTrue(any("required file is missing: profiles/go.md" in error for error in errors))

    def test_invalid_version_is_reported(self) -> None:
        (self.root / "VERSION").write_text("next-version\n", encoding="utf-8")
        errors = validate_kit(self.root)
        self.assertTrue(any("VERSION is not valid semantic-version syntax" in error for error in errors))

    def test_skill_directory_and_frontmatter_name_must_match(self) -> None:
        skill_file = self.root / "skills" / "demo-skill" / "SKILL.md"
        skill_file.write_text(VALID_SKILL.replace("name: demo-skill", "name: other-skill"), encoding="utf-8")
        errors = validate_kit(self.root)
        self.assertTrue(any("does not match directory 'demo-skill'" in error for error in errors))

    def test_missing_required_skill_section_is_reported(self) -> None:
        skill_file = self.root / "skills" / "demo-skill" / "SKILL.md"
        skill_file.write_text(VALID_SKILL.replace("## Failure handling\n\nTest failure handling.\n\n", ""), encoding="utf-8")
        errors = validate_kit(self.root)
        self.assertTrue(any("missing required section: Failure handling" in error for error in errors))

    def test_broken_local_markdown_link_is_reported(self) -> None:
        (self.root / "README.md").write_text("[missing](docs/not-present.md)\n", encoding="utf-8")
        errors = validate_kit(self.root)
        self.assertTrue(any("broken local link: docs/not-present.md" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
