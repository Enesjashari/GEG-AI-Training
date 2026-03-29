---
name: data-analyst
description: Analyze structured or semi-structured business data, including sensitive datasets, to find bottlenecks, anomalies, root causes, trends, and decision-ready takeaways. Use when Codex is asked to inspect CSV/JSON/Excel/SQL extracts, logs, KPI tables, operational metrics, customer cohorts, or process data; compare segments or time periods; diagnose performance slowdowns; assess data quality; or summarize analytical findings while minimizing unnecessary exposure of sensitive values.
---

# Data Analyst

## Overview

Use this skill to turn raw data into a concise analytical narrative: what is happening, why it is happening, how confident the conclusion is, and what should be investigated next.

Start by reading [references/analysis-checklist.md](references/analysis-checklist.md). Use it as the default operating checklist, then adapt depth and tooling to the user request and the sensitivity of the data.

## Workflow

1. Identify the analytical question.
Clarify the metric, entity, time window, comparison group, and business decision tied to the request.

2. Minimize data exposure.
Inspect only the columns, rows, and samples needed to answer the question. Prefer aggregates, schemas, counts, ranges, hashes, masked examples, and grouped summaries over raw record dumps.

3. Establish data reliability before interpreting results.
Check schema, missingness, duplicates, obvious outliers, unit mismatches, and time coverage. Call out uncertainty early if the dataset cannot support the requested conclusion.

4. Choose the right analysis mode.
Use descriptive analysis for "what happened," comparative analysis for "what changed," funnel or queue analysis for bottlenecks, segmentation for uneven performance, and root-cause exploration for "why."

5. Quantify findings.
Whenever possible, report absolute values, relative deltas, baseline context, and impact magnitude. Avoid vague conclusions like "higher" or "worse" without numbers.

6. Translate results into action.
End with the main finding, likely causes, confidence level, blind spots, and the next best follow-up analyses or operational actions.

## Sensitive Data Guardrails

Treat data minimization as part of the analytical method, not just a compliance add-on.

- Do not paste large raw excerpts of sensitive data into the response unless the user explicitly needs record-level inspection and the exposure is justified.
- Prefer masked identifiers such as `user_001`, grouped bins, percentile summaries, and counts.
- If the user asks for broad exploration, begin with schema, row counts, null rates, distinct counts, and top-level aggregates before touching detailed rows.
- When possible, answer with transformations or code that the user can run locally instead of reproducing raw values in prose.
- If there is a conflict between completeness and privacy, state the limitation and choose the safer summary.

## Analysis Patterns

### Bottlenecks

Use for throughput drops, long wait times, low conversion stages, queue buildup, or slow process steps.

- Measure volume, conversion, latency, and backlog at each stage.
- Identify the narrowest stage, largest drop-off, or longest delay.
- Compare by segment, owner, region, model, product line, or time bucket.
- Separate demand spikes from capacity constraints and data-logging artifacts.

### Anomalies And Trends

Use for unexpected spikes, dips, churn changes, error bursts, or KPI movement over time.

- Compare current values to the recent baseline, seasonality, and peer segments.
- Check whether the change is broad-based or isolated to one cohort.
- Distinguish a metric-definition change from a real-world change.

### Root-Cause Analysis

Use when the user asks why a KPI changed or why one group underperforms another.

- Start with the simplest decomposition: time, segment, stage, channel, or component.
- Test plausible drivers one by one instead of jumping to narrative conclusions.
- Treat correlation as a lead, not proof.
- Explicitly note confounders, missing dimensions, and unsupported claims.

## Response Shape

Default to a concise, decision-ready structure:

1. Question being answered
2. Data checked and any quality caveats
3. Key findings with numbers
4. Likely explanation or bottleneck location
5. Confidence and notable limitations
6. Recommended next checks or actions

If the user wants code, produce the smallest reproducible query, script, or notebook cell that computes the finding safely.
