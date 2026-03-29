---
name: testing
description: Add, repair, and improve automated tests across application and library codebases. Use when Codex needs to write missing tests, fix failing tests, reproduce bugs with tests, improve test coverage, validate regressions, or choose a practical unit, integration, or end-to-end testing strategy in JavaScript, TypeScript, Python, or similar projects.
---

# Testing

## Overview

Use the smallest test that proves the behavior. Prefer tests that isolate the real regression, stay readable, and fail for one clear reason.

Start by identifying the current test stack from the repository before writing new tests. Match existing conventions unless they are clearly broken.

## Workflow

1. Inspect the codebase for current test tools, naming patterns, fixtures, and helpers.
2. Reproduce the expected behavior or bug before editing tests.
3. Choose the narrowest useful test level:
   - Unit: pure logic, branching, formatting, validation, adapters.
   - Integration: database, API handlers, queues, filesystem, framework wiring.
   - End-to-end: user flows that need routing, browser behavior, or full stack interaction.
4. Add or update the test with explicit setup, action, and assertion phases.
5. Run the smallest relevant test target first, then widen scope only if needed.
6. If the test is flaky, remove timing assumptions, shared state, network dependency, and order coupling.

## Practical Rules

- Prefer one strong assertion over many vague assertions.
- Test behavior, not implementation details, unless the implementation contract itself matters.
- Reuse existing fixtures and helpers before creating new abstractions.
- Keep mock scope minimal; avoid mocking what the project already treats as stable infrastructure.
- When fixing a bug, write the failing regression test first if feasible.
- Do not inflate coverage with trivial tests that add maintenance cost without catching meaningful failures.

## Framework Detection

- JavaScript or TypeScript:
  - Look for `vitest.config`, `vite.config`, `jest.config`, `playwright.config`, `cypress.config`, `package.json` scripts.
  - Prefer the project's dominant runner and assertion style.
- Python:
  - Look for `pytest.ini`, `pyproject.toml`, `tox.ini`, `conftest.py`, `unittest` suites.
  - Prefer `pytest` if the repository already uses it.
- Backend services:
  - Search for API test helpers, database factories, transaction rollbacks, and seed utilities.
- Frontend apps:
  - Search for React Testing Library, component harnesses, DOM helpers, snapshot usage, and browser test setup.

## Common Tasks

### Add Missing Tests

- Find the public behavior that is currently untested.
- Add one focused happy-path test and only add edge cases that are likely to break.
- Reuse project helpers for setup.

### Fix Failing Tests

- Confirm whether the test is wrong or the implementation regressed.
- Preserve intended behavior unless repository evidence shows the expectation is outdated.
- If production code changes are needed, keep the test aligned with externally visible behavior.

### Write Regression Tests

- Reduce the bug to the smallest reproducible case.
- Name the test after the broken behavior, not the ticket number.
- Assert the previously failing output or side effect directly.

### Stabilize Flaky Tests

- Remove sleeps and arbitrary retries unless the framework explicitly requires them.
- Reset shared mutable state between tests.
- Use deterministic clocks, seeded randomness, and isolated test data when possible.

## References

Read [references/testing-playbook.md](references/testing-playbook.md) when you need a quick decision guide for picking test type, assertion style, and anti-flake cleanup.
