#!/usr/bin/env python3
"""Validate the static structure and internal Markdown links of an ADK checkout."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "VERSION",
    "CHANGELOG.md",
    "core/AGENTS.base.md",
    "core/rules/engineering-behavior.md",
    "core/rules/security-and-data.md",
    "core/rules/change-control.md",
    "core/rules/evidence-and-delivery.md",
    "docs/architecture.md",
    "docs/adoption.md",
    "docs/pilot-plan.md",
    "docs/skill-authoring.md",
    "adapters/README.md",
    "adapters/codex/README.md",
    "profiles/qt-qml.md",
    "profiles/cpp-cmake.md",
    "profiles/go.md",
    "profiles/embedded-mcu.md",
    "profiles/mixed-system.md",
    "templates/AGENTS.md",
    "templates/PROJECT_PROFILE.md",
    "templates/BUILD_TEST_MATRIX.md",
    "templates/ADR.md",
    "templates/CHANGE_REPORT.md",
    "evals/README.md",
    "scripts/validate_kit.py",
    "scripts/adk_install.py",
    "tests/test_adk_install.py",
    "tests/test_validate_kit.py",
)

REQUIRED_SKILLS = (
    "project-onboarding",
    "task-planning",
    "implementation",
    "debugging",
    "build-test-verify",
    "code-review",
    "git-pr-lifecycle",
    "architecture-docs",
    "qt-qml-development",
    "cpp-development",
    "go-development",
    "embedded-firmware",
)

REQUIRED_SKILL_SECTIONS = (
    "Purpose",
    "Use when",
    "Procedure",
    "Outputs",
    "Failure handling",
    "Completion criteria",
)

VERSION_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)
SKILL_NAME_PATTERN = re.compile(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", re.MULTILINE)
SKILL_DESCRIPTION_PATTERN = re.compile(r"^description:\s*(\S.*)$", re.MULTILINE)
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def _validate_required_files(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"required file is missing: {relative}")


def _validate_version(root: Path, errors: list[str]) -> None:
    path = root / "VERSION"
    if not path.is_file():
        return
    try:
        version = _read_text(path).strip()
    except ValueError as exc:
        errors.append(str(exc))
        return
    if not VERSION_PATTERN.fullmatch(version):
        errors.append(f"VERSION is not valid semantic-version syntax: {version!r}")


def _validate_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        errors.append("required directory is missing: skills/")
        return

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append("no Skill directories found under skills/")
        return

    present_names = {path.name for path in skill_dirs if (path / "SKILL.md").is_file()}
    for required_name in REQUIRED_SKILLS:
        if required_name not in present_names:
            errors.append(f"required Skill is missing: skills/{required_name}/SKILL.md")

    for skill_dir in skill_dirs:
        relative = skill_dir.relative_to(root).as_posix()
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{relative} is missing SKILL.md")
            continue

        try:
            content = _read_text(skill_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", content, re.DOTALL)
        if not frontmatter:
            errors.append(f"{relative}/SKILL.md has no valid YAML frontmatter")
            continue

        metadata = frontmatter.group(1)
        name_match = SKILL_NAME_PATTERN.search(metadata)
        description_match = SKILL_DESCRIPTION_PATTERN.search(metadata)
        if not name_match:
            errors.append(f"{relative}/SKILL.md is missing a valid lowercase name field")
        elif name_match.group(1) != skill_dir.name:
            errors.append(
                f"{relative}/SKILL.md name {name_match.group(1)!r} "
                f"does not match directory {skill_dir.name!r}"
            )

        if not description_match or not description_match.group(1).strip():
            errors.append(f"{relative}/SKILL.md is missing a non-empty description field")

        for section in REQUIRED_SKILL_SECTIONS:
            heading = re.compile(rf"^##\s+{re.escape(section)}\s*$", re.MULTILINE)
            if not heading.search(content):
                errors.append(f"{relative}/SKILL.md is missing required section: {section}")


def _validate_markdown_links(root: Path, errors: list[str]) -> None:
    markdown_files = sorted(
        path for path in root.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )
    for markdown_file in markdown_files:
        try:
            content = _read_text(markdown_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        for match in MARKDOWN_LINK_PATTERN.finditer(content):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith("#") or target.startswith("//"):
                continue
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue

            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue

            candidate = (markdown_file.parent / path_part).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                errors.append(
                    f"{markdown_file.relative_to(root).as_posix()} links outside the repository: {target}"
                )
                continue
            if not candidate.exists():
                errors.append(
                    f"{markdown_file.relative_to(root).as_posix()} has a broken local link: {target}"
                )


def validate_kit(root: Path) -> list[str]:
    """Return validation errors for the kit rooted at *root*."""
    root = root.resolve()
    errors: list[str] = []
    if not root.is_dir():
        return [f"repository root is not a directory: {root}"]

    _validate_required_files(root, errors)
    _validate_version(root, errors)
    _validate_skills(root, errors)
    _validate_markdown_links(root, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="ADK repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args(argv)

    errors = validate_kit(args.root)
    if errors:
        print(f"ADK validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("ADK structure validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
