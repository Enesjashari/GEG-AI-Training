#!/usr/bin/env python3
"""
Create a new skill inside the local task folder.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
TASK_DIR = REPO_ROOT / "task"
UPSTREAM_INIT = (
    Path.home()
    / ".codex"
    / "skills"
    / ".system"
    / "skill-creator"
    / "scripts"
    / "init_skill.py"
)
INVALID_DESCRIPTION_LINE = (
    "description: [TODO: Complete and informative explanation of what the skill does and "
    "when to use it. Include WHEN to use this skill - specific scenarios, file types, or "
    "tasks that trigger it.]"
)
VALID_DESCRIPTION_LINE = (
    'description: "TODO: Explain what this skill does and when to use it."'
)


def normalize_for_display(skill_name: str) -> str:
    return " ".join(part.capitalize() for part in skill_name.split("-"))


def build_command(skill_name: str, resources: str, examples: bool) -> list[str]:
    display_name = normalize_for_display(skill_name)
    short_description = f"Create and use {display_name} workflows"
    default_prompt = f"Use ${skill_name} to help with the target task."

    command = [
        sys.executable,
        str(UPSTREAM_INIT),
        skill_name,
        "--path",
        str(TASK_DIR),
        "--interface",
        f"display_name={display_name}",
        "--interface",
        f"short_description={short_description}",
        "--interface",
        f"default_prompt={default_prompt}",
    ]

    if resources:
        command.extend(["--resources", resources])
    if examples:
        command.append("--examples")

    return command


def fix_skill_frontmatter(skill_name: str) -> None:
    skill_md = TASK_DIR / skill_name / "SKILL.md"
    if not skill_md.exists():
        return

    content = skill_md.read_text(encoding="utf-8")
    if INVALID_DESCRIPTION_LINE not in content:
        return

    skill_md.write_text(
        content.replace(INVALID_DESCRIPTION_LINE, VALID_DESCRIPTION_LINE, 1),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a new skill in the local task folder."
    )
    parser.add_argument("skill_name", help="Skill name in hyphen-case")
    parser.add_argument(
        "--resources",
        default="",
        help="Optional comma-separated resource folders: scripts,references,assets",
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Create example files in selected resource directories",
    )
    args = parser.parse_args()

    if not UPSTREAM_INIT.exists():
        print(f"[ERROR] Upstream initializer not found: {UPSTREAM_INIT}")
        return 1

    TASK_DIR.mkdir(parents=True, exist_ok=True)
    command = build_command(args.skill_name, args.resources, args.examples)
    completed = subprocess.run(command, check=False)
    if completed.returncode == 0:
        fix_skill_frontmatter(args.skill_name)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
