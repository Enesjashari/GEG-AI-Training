# Python Refactor Checklist

Use this checklist before and during most refactor tasks.

## 1. Define Scope

- What unit is being refactored: function, class, module, or path?
- Is behavior expected to remain exactly the same?
- What is out of scope for this pass?

## 2. Establish Baseline

- Which tests currently cover this path?
- What command can quickly prove the baseline behavior?
- Are there missing tests that should be added before risky edits?

## 3. Pick The Smallest Safe Change

- Rename unclear variables and functions first.
- Split long functions into coherent steps.
- Remove dead branches and obvious duplication.
- Flatten nested control flow where it improves readability.

## 4. Preserve Contracts

- Keep public signatures and return shapes stable.
- Keep side effects and ordering stable unless requested otherwise.
- Keep exception types and messages stable where callers depend on them.

## 5. Verify Frequently

- Run narrow tests after each meaningful change.
- Re-run the original reproduction or baseline command.
- Expand to nearby tests if the change crosses boundaries.

## 6. Finish Cleanly

- Remove temporary scaffolding or debug code.
- Confirm no unrelated files changed.
- Summarize what improved and what remains risky.

## Heuristics

- If a refactor needs many moving parts, split into multiple commits.
- Prefer explicit code over clever abstractions.
- If confidence is low, stop and add tests before continuing.
