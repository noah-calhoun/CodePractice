"""Reads the raw search event log."""
import json
from datetime import datetime
from typing import Iterator


def load_events(path: str) -> Iterator[dict]:
    """Yield events from a JSONL file, parsing timestamps to datetimes.
    Malformed lines are skipped with a warning printed to stderr.
    """
    with open(path) as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
                event["timestamp"] = datetime.fromisoformat(
                    event["timestamp"].replace("Z", "+00:00")
                )
                yield event
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                import sys
                print(f"skipping line {lineno}: {e}", file=sys.stderr)
