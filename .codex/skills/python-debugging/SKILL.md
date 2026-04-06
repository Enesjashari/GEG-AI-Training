---
name: python-debugging
description: Debug Python errors, failing tests, incorrect behavior, crashes, performance regressions, import problems, environment mismatches, and flaky scripts. Use when Codex is asked to investigate a Python bug, reproduce an issue, inspect stack traces, add targeted instrumentation, isolate root cause, or implement and verify a fix.
---

# Python Debugging

## Overview

Use this skill when the task is to find and fix a Python bug, not just explain Python syntax.

Start by reading [references/debug-checklist.md](references/debug-checklist.md). Use it as the default workflow, then adapt depth to the size of the codebase and the cost of running the reproduction.

## Workflow

1. Reproduce the issue first.
Capture the exact command, inputs, environment assumptions, and observed failure. Prefer a deterministic reproduction over theory.

2. Preserve the original signal.
Read the traceback, failing assertion, log lines, and recent code path before editing. Do not guess at the cause from the top-level error alone.

3. Narrow the fault surface.
Identify the smallest function, module, test, or input that still reproduces the bug. Favor targeted commands over broad test runs when possible.

4. Inspect state with lightweight instrumentation.
Use focused prints, logging, assertions, or temporary test scaffolding to confirm control flow and data shape. Remove or convert temporary instrumentation before finishing unless it provides lasting value.

5. Fix the root cause, not the symptom.
Trace bad output back to the earliest incorrect assumption, mutation, boundary condition, type mismatch, or environment dependency.

6. Verify at the right level.
Run the narrowest reproduction that proves the bug is fixed, then run nearby tests if they are cheap and relevant.

7. Summarize the debugging chain.
Report the reproduction, root cause, fix, and verification in a way that lets another engineer understand what changed quickly.

## Python-Specific Guidance

- Prefer reading the full traceback from the first failing frame through the application frames.
- Check imports, package layout, virtual environment assumptions, and working-directory-sensitive paths early for startup failures.
- For data-shape bugs, inspect concrete values, types, lengths, and `None` handling at module boundaries.
- For async issues, verify where coroutines are awaited, where tasks are created, and whether exceptions are being swallowed.
- For performance regressions, measure before optimizing. Confirm whether the bottleneck is I/O, repeated work, large object copying, or accidental quadratic behavior.
- For test-only failures, compare fixture setup, environment variables, temp paths, and test order assumptions.

## Common Failure Modes

### Exceptions

- Wrong argument shape or missing `None` handling
- Unexpected mutation of shared state
- Import cycles or module shadowing
- Path assumptions that differ between local runs and tests
- Timezone, locale, or encoding mismatches

### Incorrect Behavior

- Off-by-one boundaries
- Default values masking invalid state
- Silent fallbacks hiding bad inputs
- Cached state not invalidated after updates
- Sorting, filtering, or grouping on the wrong key

### Flaky Or Environment-Specific Bugs

- Shared global state between tests
- Race conditions or missing synchronization
- Reliance on wall-clock time or iteration order
- Filesystem case sensitivity or path separator differences
- Hidden dependency on locally installed packages or shell state

## Response Shape

Default to a concise debugging summary:

1. Reproduction used
2. Root cause
3. Fix applied
4. Verification run
5. Remaining risk or follow-up if verification was partial

If the issue cannot be reproduced, state exactly what was tried, what evidence is still available, and the next best way to reduce uncertainty.
