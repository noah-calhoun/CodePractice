# Interviewer Notes (don't peek until after you attempt)

## The bug

`Session.add` in `sessionizer.py`:

```python
if "specialty" in event and self.specialty == "unknown":
    self.specialty = event["specialty"]
```

This sets the specialty only the first time. Per the README, the session's
specialty should be the MOST RECENT search/filter_change. So a member who
searches "cardiology" then refines to "interventional_cardiology" gets
labeled "cardiology" instead of "interventional_cardiology".

### Why it's hidden

- All four existing tests use a single specialty per session.
- The top-line report (sessions / unique members / success rate) doesn't
  expose the field at all.
- It only becomes visible when you add the per-specialty breakdown
  (the feature) and notice the counts look skewed toward general
  specialties.

### The fix

```python
if event["event_type"] in ("search", "filter_change") and "specialty" in event:
    self.specialty = event["specialty"]
```

A strong candidate also writes a regression test before fixing.

### Expected impact on the sample data

36 of 85 sessions change specialty. "orthopedics" drops out of the top 5
entirely under the correct rule (members almost always refine it to
sports_medicine or spine_surgery).

## The feature

Add per-specialty breakdown to `build_report`. Sort by session count
descending, top 5.

Reasonable implementation:

```python
from collections import Counter

by_specialty_sessions = Counter(s.specialty for s in week_sessions)
by_specialty_success = Counter(
    s.specialty for s in week_sessions if s.succeeded
)

top = by_specialty_sessions.most_common(5)
lines.append("")
lines.append("Top specialties:")
for specialty, count in top:
    succ = by_specialty_success[specialty]
    rate = (succ / count * 100) if count else 0.0
    lines.append(f"  {specialty:<30} {count:>4} sessions  {rate:>5.1f}% click")
```

## Things to watch for (signal)

### Strong signal
- Re-reads the README before coding, especially the spec for "session
  specialty"
- Catches the bug by reasoning about the spec, not just by eyeballing
  output
- Writes a failing test that captures the spec, then fixes the code
- Uses `Counter` or `defaultdict(int)` for the breakdown rather than
  rolling a manual dict
- Mentions that the existing tests don't cover the spec they just read
- Asks a clarifying question before implementing the breakdown
  ("if a session has zero searches, do we include 'unknown' in the
  top 5 or filter it out?")

### Medium signal
- Finds the bug only after seeing odd output from the breakdown
- Implements the feature correctly but doesn't add tests for it
- Uses a tuple unpacking pattern like `for specialty, count in ...`
  comfortably

### Weak signal / things to gently probe
- Iterates with index counters instead of `enumerate` / direct iteration
- Builds the breakdown with nested loops (O(n*k) instead of O(n))
- Doesn't notice the malformed-line stderr output and doesn't ask if
  silent-skip is the right behavior
- Fixes the symptom (e.g. always overwrites specialty) without
  considering whether `result_click` events should reset it (they
  shouldn't, since clicks don't have a specialty field)

## Discussion prompts for the last 10 minutes

Pick 1-2 based on time and how the coding portion went:

1. "This runs in memory on a single file. If events grew to 100M/day,
   what would you change first?" (Expecting: streaming, partition by
   member or by day, parallel sessionization per member, move state
   to a real store like Postgres or Redshift. SE2 doesn't need to
   design the full system, just identify the right starting pivots.)

2. "How would you handle late-arriving events?" (Expecting: watermarks,
   reprocessing windows, idempotency on session IDs. Honest 'I'd
   need to think about it' is fine if they reason out loud.)

3. "The PM also wants to know the median session duration. How would
   you add it?" (Mostly to see if they think about p50 vs mean and
   whether they reach for `statistics.median` cleanly.)

4. "What tests would you add if this were going to production?"
   (Expecting: spec the boundary conditions, malformed input, empty
   week, session straddling the week boundary, timezone handling.)

## Timing

- 5 min: read README, run tool, run tests
- 10-15 min: investigate the bug (the feature ask is the prompt that
  surfaces it for some candidates; others spot it from the spec first)
- 10 min: fix + regression test
- 15-20 min: implement the breakdown feature
- 10 min: discussion
