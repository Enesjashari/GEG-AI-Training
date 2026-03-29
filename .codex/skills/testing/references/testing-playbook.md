# Testing Playbook

## Choose the Test Level

- Use unit tests for branching logic, parsers, mappers, utilities, validation, and transformation code.
- Use integration tests for framework wiring, persistence, queues, caching, and API contracts.
- Use end-to-end tests for user-critical flows that cross multiple layers.

## Prefer Clear Structure

Use a simple `arrange`, `act`, `assert` structure even if the framework does not enforce it.

## Good Assertions

- Assert on outputs, rendered text, status codes, database records, or emitted events.
- Avoid overly broad snapshots unless the repository already uses them carefully.
- Avoid asserting on private helpers unless they are the public unit under test.

## Mocking Rules

- Mock boundaries that are slow, flaky, paid, or external.
- Do not mock internal code paths so aggressively that the test stops checking real behavior.
- Prefer factories and fixtures over hand-built data blobs copied across many files.

## Flake Checks

- Eliminate hidden shared state.
- Freeze time when dates matter.
- Seed or stub randomness.
- Wait on explicit framework signals instead of sleep-based timing.
- Ensure test order does not matter.

## Before Finishing

- Run the narrowest related test target first.
- Expand to a broader suite only after the local fix passes.
- If tests cannot be run, state that clearly and explain the limitation.
