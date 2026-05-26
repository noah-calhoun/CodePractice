"""Groups raw events into per-member search sessions."""
from collections import defaultdict
from datetime import timedelta
from typing import Iterable

SESSION_GAP = timedelta(minutes=15)


class Session:
    def __init__(self, member_id: str):
        self.member_id = member_id
        self.events: list[dict] = []
        self.specialty: str = "unknown"
        self.succeeded: bool = False

    def add(self, event: dict) -> None:
        self.events.append(event)

        if event["event_type"] == "result_click":
            self.succeeded = True

        # Track the specialty the member was looking at.
        if "specialty" in event and self.specialty == "unknown":
            self.specialty = event["specialty"]

    @property
    def start(self):
        return self.events[0]["timestamp"]

    @property
    def end(self):
        return self.events[-1]["timestamp"]


def sessionize(events: Iterable[dict]) -> list[Session]:
    """Group events into sessions, split by 15 minutes of inactivity."""
    by_member: dict[str, list[dict]] = defaultdict(list)
    for e in events:
        by_member[e["member_id"]].append(e)
    sessions: list[Session] = []
    for member_id, member_events in by_member.items():
        member_events.sort(key=lambda e: e["timestamp"])

        current = Session(member_id)
        for event in member_events:
            if current.events and event["timestamp"] - current.end > SESSION_GAP:
                sessions.append(current)
                current = Session(member_id)
            current.add(event)

        if current.events:
            sessions.append(current)

    return sessions
