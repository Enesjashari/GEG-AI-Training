# Python Debug Checklist

Use this checklist at the start of most Python bug investigations, then skip any item that is clearly irrelevant.

## 1. Reproduce Reliably

- What exact command, script, or test fails?
- What input, config, environment variable, or working directory matters?
- Is the failure deterministic or intermittent?
- Can the reproduction be reduced to one test, one script, or one function call?

## 2. Capture The Signal

- Full traceback or failing assertion
- Relevant log lines near the failure
- The first unexpected value, not just the final exception
- Recent code path and boundary inputs

## 3. Check Common Python Causes

- Wrong interpreter or virtual environment
- Missing dependency or import shadowing
- `None` where a value was assumed
- Mutable default or unintended shared state
- Path, encoding, timezone, or locale mismatch
- Async task not awaited or exception swallowed

## 4. Narrow The Search

- Add small, targeted instrumentation
- Compare expected and actual values at boundaries
- Bisect the path: input parsing, transformation, persistence, output
- Prefer the smallest failing test over broad reruns

## 5. Verify The Fix

- Re-run the original reproduction
- Run nearby tests that cover the same code path
- Remove temporary debug noise unless it is intentionally kept
- Confirm the fix addresses cause, not just symptoms

## 6. Close Clearly

- State the root cause in one or two sentences
- State what changed
- State how it was verified
- Call out any remaining uncertainty
