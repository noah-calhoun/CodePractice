"""Tests for the sessionizer."""
from datetime import datetime, timezone, timedelta

from usage_analytics.sessionizer import sessionize


def _event(member_id, event_type, minutes_offset, **extra):
    base = datetime(2026, 5, 12, 14, 0, 0, tzinfo=timezone.utc)
    return {
        "member_id": member_id,
        "event_type": event_type,
        "timestamp": base + timedelta(minutes=minutes_offset),
        **extra,
    }


def test_single_session():
    events = [
        _event("m1", "search", 0, specialty="cardiology"),
        _event("m1", "result_click", 2, provider_id="p1"),
    ]
    sessions = sessionize(events)
    assert len(sessions) == 1
    assert sessions[0].succeeded is True


def test_gap_creates_new_session():
    events = [
        _event("m1", "search", 0, specialty="cardiology"),
        _event("m1", "search", 30, specialty="cardiology"),
    ]
    sessions = sessionize(events)
    assert len(sessions) == 2


def test_different_members_are_separate():
    events = [
        _event("m1", "search", 0, specialty="cardiology"),
        _event("m2", "search", 1, specialty="dermatology"),
    ]
    sessions = sessionize(events)
    assert len(sessions) == 2


def test_no_click_means_failed_session():
    events = [
        _event("m1", "search", 0, specialty="cardiology"),
        _event("m1", "filter_change", 1, specialty="cardiology"),
    ]
    sessions = sessionize(events)
    assert sessions[0].succeeded is False
