---
name: skill-builder
description: Create or update reusable Codex skills for a workspace. Use when Codex needs to build a new skill folder, improve an existing SKILL.md, add reusable references/scripts/assets, or prepare a skill that helps create other skills.
---

# Skill Builder

Create skills that another Codex instance can use with minimal setup. Keep instructions lean, practical, and focused on reusable workflow rather than one-off explanations.

## Workflow

1. Identify the skill outcome before writing files.
2. Choose a short hyphen-case name.
3. Create the skill folder with `SKILL.md` and `agents/openai.yaml`.
4. Add only the resource folders the skill actually needs.
5. Validate the finished skill structure.

## Define The Skill

- Clarify what problem the skill solves repeatedly.
- Write the trigger context into the frontmatter `description`, not just the body.
- Prefer one core job per skill. If the request spans several unrelated jobs, split them.
- If the user asks for a skill that creates other skills, make the workflow explicit and include a reusable template or checklist.

## Build The Files

Create these files:

- `SKILL.md`
  Use the structure in [references/skill-template.md](./references/skill-template.md) and replace all placeholders.
- `agents/openai.yaml`
  Include `display_name`, `short_description`, and `default_prompt`. Keep them short and user-facing.
- Optional `references/`
  Add only when detailed guidance would clutter `SKILL.md`.
- Optional `scripts/`
  Add only when the same logic would otherwise be rewritten often.
- Optional `assets/`
  Add only when the skill needs templates or files to copy into outputs.

For quick setup inside this workspace, run:

```powershell
python ".\task\skill-builder\scripts\create_skill.py" "<skill-name>" --resources references
```

This creates the new skill inside `task/` and pre-fills the standard UI metadata.

## Writing Rules

- Use imperative wording.
- Keep `SKILL.md` short enough to scan quickly.
- Put durable process in the skill; keep temporary project facts out unless they are essential.
- Avoid extra docs like `README.md` or changelogs inside the skill.
- Prefer references over bloating the main file when detailed examples are needed.

## Suggested Creation Flow

When asked to create a new skill:

1. Pick the target folder.
2. Create the base structure.
3. Draft `SKILL.md` with a clear trigger description.
4. Add one reusable reference if it will save future work.
5. Validate the skill.

When asked to improve an existing skill:

1. Read the current `SKILL.md` and `agents/openai.yaml`.
2. Tighten the trigger description.
3. Remove vague or repetitive text.
4. Move bulky details into `references/` when useful.
5. Re-validate after edits.

## Validation

Run:

```powershell
python "C:/Users/milia/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "<path-to-skill>"
```

If validation fails, fix the reported frontmatter or naming issue first.

## Local Automation

Use [scripts/create_skill.py](./scripts/create_skill.py) when the destination is this repository's `task` folder. It wraps the upstream initializer and keeps the path and interface fields consistent.

## Output Expectation

Deliver a ready-to-use skill folder, not just advice. If the user names a destination folder, place the skill there and leave it validated.
