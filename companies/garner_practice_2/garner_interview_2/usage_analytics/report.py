"""Builds the weekly rollup report."""
from datetime import datetime, timedelta, timezone

from .sessionizer import Session


def filter_to_week(sessions: list[Session], week_start: datetime) -> list[Session]:
    """Keep only sessions whose start falls within the 7-day window."""
    week_end = week_start + timedelta(days=7)
    return [s for s in sessions if week_start <= s.start < week_end]


def build_report(sessions: list[Session], week_start: datetime) -> str:
    week_sessions = filter_to_week(sessions, week_start)

    total = len(week_sessions)
    succeeded = sum(1 for s in week_sessions if s.succeeded)
    success_rate = (succeeded / total * 100) if total else 0.0

    unique_members = len({s.member_id for s in week_sessions})

    lines = [
        f"Weekly Search Report",
        f"Week of {week_start.date().isoformat()}",
        f"",
        f"  Sessions:        {total}",
        f"  Unique members:  {unique_members}",
        f"  Succeeded:       {succeeded} ({success_rate:.1f}%)",
    ]
    return "\n".join(lines)


def parse_week_start(s: str) -> datetime:
    return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
