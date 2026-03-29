# Analysis Checklist

Use this checklist at the start of most requests, then skip any item that is clearly irrelevant.

## 1. Frame The Question

- What exact decision or hypothesis is this analysis serving?
- What is the primary metric?
- What is the unit of analysis: user, order, event, session, ticket, job, or day?
- What time window matters?
- What comparison matters: prior period, target, cohort, region, product, or stage?

## 2. Minimize Exposure

- Read schema before reading full rows.
- Prefer aggregates, grouped tables, and masked samples.
- Avoid echoing sensitive values back unless strictly necessary.
- Keep intermediate outputs focused on the question being answered.

## 3. Verify Data Quality

- Row count and date coverage
- Missing values in key fields
- Duplicate keys or repeated events
- Type mismatches and unit inconsistencies
- Obvious outliers or impossible values
- Join explosions or dropped rows after merges

## 4. Choose The Analysis

### For bottlenecks

- Count throughput at each step.
- Measure drop-off and latency.
- Compare segments to isolate where the queue or slowdown concentrates.

### For anomalies

- Compare against a recent baseline.
- Check whether the anomaly survives segmentation.
- Rule out instrumentation or definition changes.

### For trends

- Look at absolute values and percent change.
- Compare rolling windows, not just point-to-point movement.
- Note seasonality and calendar effects.

### For root cause

- Break the problem down by time, segment, stage, and source.
- Test one candidate driver at a time.
- Separate explanation supported by data from speculation.

## 5. Summarize Clearly

- Lead with the answer, not the process.
- Include actual numbers and deltas.
- State confidence and limitations.
- Recommend the next best action or follow-up query.
