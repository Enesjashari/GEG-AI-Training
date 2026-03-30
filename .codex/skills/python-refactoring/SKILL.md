---
name: python-refactoring
description: Refactor Python code for readability, maintainability, and safer change velocity without changing behavior. Use when Codex is asked to clean up complex functions, split large modules, remove duplication, improve naming, simplify control flow, introduce lightweight abstractions, or apply incremental structure improvements with verification.
---

# Python Refactoring

## Overview

Use this skill when the goal is structural code improvement with behavior preserved.

Start by reading [references/refactor-checklist.md](references/refactor-checklist.md). Use it as the default sequence, then adapt scope to repository size and test confidence.

## Workflow

1. Lock down current behavior first.
   Reproduce current behavior with existing tests, scripts, or a small baseline command set before making structural edits.

2. Define a narrow refactor target.
   Choose one unit at a time: one function, class, module, or call path. Avoid broad rewrites unless explicitly requested.

3. Improve clarity before abstraction.
   Prefer better naming, smaller functions, flatter control flow, and dead-code removal before introducing new patterns.

4. Preserve public contracts.
   Keep input and output behavior stable, including function signatures, return shape, side effects, and error behavior unless the user asked for API changes.

5. Apply changes in small, verifiable steps.
   Each step should be understandable and testable on its own. Keep diffs focused and avoid unrelated formatting churn.

6. Verify after each meaningful change.
   Run the narrowest tests or commands that validate unchanged behavior, then widen scope if needed.

7. Summarize intent and risk.
   Report what was simplified, what behavior was preserved, what was validated, and what remains unverified.

## Refactoring Priorities

- Readability first: names, boundaries, and predictable control flow.
- Duplication reduction: extract shared logic only when duplication is real and stable.
- Complexity reduction: replace deeply nested branching with guard clauses or decomposition.
- Safer state handling: limit mutable shared state and hidden side effects.
- Dependency hygiene: isolate I O, framework, and persistence boundaries from pure logic where practical.

## Python-Specific Guidance

- Extract pure functions from mixed logic plus side-effect blocks where possible.
- Replace long if elif chains with table-driven mapping only when it improves clarity.
- Use dataclasses or typed structures when they improve readability and contracts.
- Avoid over-engineering with premature class hierarchies.
- Keep exception handling explicit and close to error boundaries.
- Preserve async semantics when refactoring coroutine code.

## Response Shape

Default to this summary order:

1. Refactor target and constraints
2. Structural changes made
3. Behavior-preservation checks run
4. Residual risk or untested paths
5. Suggested next refactor slice
