# Member Search Analytics

## Context

You're joining the Member Experience team at Garner. The team owns the
member-facing app where members search for in-network, high-quality
providers. Product wants weekly reports on how members are using search:
how many sessions, how many succeed (member clicked a provider), and which
specialties are trending.

A teammate started a small CLI tool that ingests raw search event logs
and produces a weekly rollup report. They left for vacation halfway
through. The tool runs, but the numbers look wrong, and the PM wants
one more breakdown added before Monday.

You'll be working through this with your interviewer. Expect to:

1. Read the existing code and get oriented.
2. Run it, look at the output, and figure out why the numbers are off.
3. Fix the bug.
4. Add a small feature on top.
5. Talk about what you'd do differently if this were going to production.

## Stack

Python 3.11+, no external dependencies. Everything runs from the command
line.

## Layout

```
usage_analytics/
  __init__.py
  loader.py        # reads the JSONL event log
  sessionizer.py   # groups events into search sessions
  report.py        # builds the weekly rollup
  cli.py           # entry point
data/
  events.jsonl     # sample event log (one JSON object per line)
tests/
  test_sessionizer.py
```

## How to run

```
python -m usage_analytics.cli data/events.jsonl --week 2026-05-11
```

Expected output is a small text report. There's also a tiny test suite:

```
python -m pytest tests/
```

## What the PM wants added

After the bug is fixed, add a per-specialty breakdown to the report:
for each specialty, how many sessions searched for it and what fraction
of those sessions ended in a click. Sort by session count descending,
show the top 5.

## Event schema

Each line in `events.jsonl` is a JSON object:

```json
{
  "member_id": "m_8821",
  "event_type": "search" | "result_click" | "filter_change",
  "timestamp": "2026-05-12T14:32:11Z",
  "specialty": "cardiology",       // present on search and filter_change
  "provider_id": "p_4471"          // present on result_click only
}
```

A "session" is all events from one member with no more than 15 minutes
of inactivity between consecutive events. A new event after a 15+ minute
gap starts a new session.

A session "succeeded" if it contains at least one `result_click`.

The session's "specialty" is whatever specialty the member searched for
most recently in that session (search or filter_change). If the session
has no search or filter_change events at all, treat the specialty as
`"unknown"`.
