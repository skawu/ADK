#!/usr/bin/env python3
"""Safely plan or apply a selective copy of ADK components into a project."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SOURCE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = "docs/ai-dev/ADK-MANIFEST.json"


class InstallError(ValueError):
    """Raised when an installation plan is unsafe or invalid."""


@dataclass(frozen=True)
class InstallItem:
    relative_path: str
    content: str
    source_path: str


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise InstallError(f"cannot read {path}: {exc}") from exc


def _names_from_markdown(root: Path) -> set[str]:
    if not root.is_dir():
        return set()
    return {path.stem for path in root.glob("*.md") if path.is_file()}


def _skill_names(root: Path) -> set[str]:
    if not root.is_dir():
        return set()
    return {
        path.name
        for path in root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def _validate_selection(
    selected: list[str],
    available: set[str],
    component_label: str,
) -> list[str]:
    names = sorted(set(selected))
    unknown = [name for name in names if name not in available]
    if unknown:
        raise InstallError(
            f"unknown {component_label}: {', '.join(unknown)}; "
            f"available: {', '.join(sorted(available)) or '(none)'}"
        )
    return names


def _safe_destination(target_root: Path, relative_path: str) -> Path:
    relative = Path(relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise InstallError(f"unsafe destination path: {relative_path}")
    destination = (target_root / relative).resolve()
    try:
        destination.relative_to(target_root)
    except ValueError as exc:
        raise InstallError(f"destination escapes target project: {relative_path}") from exc
    return destination


def build_plan(
    source_root: Path,
    target_root: Path,
    layout: str,
    skills: list[str],
    profiles: list[str],
    rules: list[str],
) -> tuple[list[InstallItem], list[str]]:
    """Build a deterministic copy plan without modifying the target."""
    source_root = source_root.resolve()
    target_root = target_root.resolve()

    if layout not in {"codex", "docs-only"}:
        raise InstallError(f"unsupported layout: {layout}")
    if not source_root.is_dir():
        raise InstallError(f"ADK source is not a directory: {source_root}")
    if not target_root.is_dir():
        raise InstallError(f"target project must already exist: {target_root}")
    if source_root == target_root or source_root in target_root.parents or target_root in source_root.parents:
        raise InstallError("target must not be the ADK source tree, its parent, or a child of it")

    version_path = source_root / "VERSION"
    if not version_path.is_file():
        raise InstallError(f"ADK VERSION file is missing: {version_path}")
    version = _read_text(version_path).strip()

    selected_skills = _validate_selection(skills, _skill_names(source_root / "skills"), "Skills")
    selected_profiles = _validate_selection(
        profiles, _names_from_markdown(source_root / "profiles"), "Profiles"
    )
    selected_rules = _validate_selection(
        rules, _names_from_markdown(source_root / "core" / "rules"), "rules"
    )
    if not (selected_skills or selected_profiles or selected_rules):
        raise InstallError("select at least one Skill, Profile, or rule")

    items: list[InstallItem] = []
    for name in selected_rules:
        source = source_root / "core" / "rules" / f"{name}.md"
        items.append(InstallItem(f"docs/ai-dev/rules/{name}.md", _read_text(source), source.as_posix()))

    for name in selected_profiles:
        source = source_root / "profiles" / f"{name}.md"
        items.append(InstallItem(f"docs/ai-dev/profiles/{name}.md", _read_text(source), source.as_posix()))

    for name in selected_skills:
        source = source_root / "skills" / name / "SKILL.md"
        if layout == "codex":
            destination = f".agents/skills/{name}/SKILL.md"
        else:
            destination = f"docs/ai-dev/skills/{name}/SKILL.md"
        items.append(InstallItem(destination, _read_text(source), source.as_posix()))

    items.sort(key=lambda item: item.relative_path)
    registry_detected = (target_root / ".agents" / "registry.json").is_file()
    manifest = {
        "schema_version": 1,
        "adk_version": version,
        "target_layout": layout,
        "components": {
            "rules": selected_rules,
            "profiles": selected_profiles,
            "skills": selected_skills,
        },
        "files": [item.relative_path for item in items],
        "activation_status": "manual-verification-required",
        "project_instruction_files_modified": False,
        "project_registry_modified": False,
        "project_registry_detected": registry_detected,
    }
    manifest_content = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    items.append(InstallItem(MANIFEST_PATH, manifest_content, "generated ADK install manifest"))
    items.sort(key=lambda item: item.relative_path)

    warnings = [
        "AGENTS.md, tool configuration, and project-owned registries will not be modified.",
        "Copied Skill files do not prove activation; verify the target tool and update any required registry separately.",
    ]
    if registry_detected:
        warnings.append("Detected .agents/registry.json; it will be preserved and not updated.")
    return items, warnings


def classify_plan(target_root: Path, items: list[InstallItem]) -> list[tuple[InstallItem, str]]:
    """Classify each planned file as ADD, UNCHANGED, or CONFLICT."""
    target_root = target_root.resolve()
    classified: list[tuple[InstallItem, str]] = []
    for item in items:
        destination = _safe_destination(target_root, item.relative_path)
        if not destination.exists():
            classified.append((item, "ADD"))
        elif not destination.is_file():
            classified.append((item, "CONFLICT"))
        else:
            try:
                existing = destination.read_bytes()
            except OSError:
                classified.append((item, "CONFLICT"))
            else:
                expected = item.content.encode("utf-8")
                classified.append((item, "UNCHANGED" if existing == expected else "CONFLICT"))
    return classified


def apply_plan(target_root: Path, items: list[InstallItem]) -> list[str]:
    """Apply a plan without overwriting existing files; roll back newly created files on error."""
    target_root = target_root.resolve()
    classified = classify_plan(target_root, items)
    conflicts = [item.relative_path for item, status in classified if status == "CONFLICT"]
    if conflicts:
        raise InstallError(
            "conflicts detected; no files were written: " + ", ".join(conflicts)
        )

    created: list[Path] = []
    try:
        for item, status in classified:
            if status != "ADD":
                continue
            destination = _safe_destination(target_root, item.relative_path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            try:
                with destination.open("xb") as stream:
                    stream.write(item.content.encode("utf-8"))
            except FileExistsError as exc:
                raise InstallError(
                    f"destination appeared during install; refusing to overwrite: {item.relative_path}"
                ) from exc
            created.append(destination)
    except Exception:
        for path in reversed(created):
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass
        candidate_dirs: set[Path] = set()
        for path in created:
            for parent in path.parents:
                if parent == target_root:
                    break
                candidate_dirs.add(parent)
        for directory in sorted(candidate_dirs, key=lambda path: len(path.parts), reverse=True):
            try:
                directory.rmdir()
            except OSError:
                pass
        raise

    return [path.relative_to(target_root).as_posix() for path in created]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_ROOT, help="ADK source root")
    parser.add_argument("--target", type=Path, required=True, help="existing target project directory")
    parser.add_argument("--layout", choices=("codex", "docs-only"), default="codex")
    parser.add_argument("--skill", action="append", default=[], help="Skill name; may be repeated")
    parser.add_argument("--profile", action="append", default=[], help="Profile name; may be repeated")
    parser.add_argument("--rule", action="append", default=[], help="core rule name; may be repeated")
    parser.add_argument("--apply", action="store_true", help="apply the plan; default is dry-run only")
    args = parser.parse_args(argv)

    try:
        items, warnings = build_plan(
            args.source, args.target, args.layout, args.skill, args.profile, args.rule
        )
        classified = classify_plan(args.target, items)
    except (InstallError, OSError) as exc:
        print(f"ADK install planning failed: {exc}", file=sys.stderr)
        return 2

    print(f"ADK selective install plan: {args.target.resolve()}")
    for item, status in classified:
        print(f"{status:9} {item.relative_path}")
    for warning in warnings:
        print(f"NOTE: {warning}")

    conflicts = [item.relative_path for item, status in classified if status == "CONFLICT"]
    if conflicts:
        print("Conflicts found. No files were written.", file=sys.stderr)
        return 2

    if not args.apply:
        print("DRY RUN: no files changed. Add --apply only after reviewing this plan.")
        return 0

    try:
        created = apply_plan(args.target, items)
    except (InstallError, OSError) as exc:
        print(f"ADK install failed: {exc}", file=sys.stderr)
        return 2

    print(f"Applied: {len(created)} new file(s).")
    print("Project instructions and activation registries were left unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
