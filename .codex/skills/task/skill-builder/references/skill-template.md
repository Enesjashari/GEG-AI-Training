# Skill Template

Use this template when creating a new skill and replace every placeholder.

```md
---
name: your-skill-name
description: Explain what the skill does and when to use it. Include trigger situations, common task types, or contexts where this skill should activate.
---

# Your Skill Title

Write 1-2 short sentences explaining the purpose of the skill.

## Workflow

1. Describe the first action.
2. Describe the main execution flow.
3. Describe how to validate or finish.

## Key Rules

- Keep only reusable knowledge here.
- Move long details into `references/` when needed.
- Add `scripts/` only for repeatable automation.
- Add `assets/` only for reusable output files or templates.

## Validation

```powershell
python "C:/Users/milia/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "<path-to-skill>"
```
```

Suggested `agents/openai.yaml`:

```yaml
interface:
  display_name: "Short UI Name"
  short_description: "Short human-facing summary"
  default_prompt: "Use $your-skill-name to help with the target task."
```
