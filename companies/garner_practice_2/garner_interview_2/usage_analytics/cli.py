"""CLI entry point: python -m usage_analytics.cli <events> --week YYYY-MM-DD"""
import argparse

from .loader import load_events
from .sessionizer import sessionize
from .report import build_report, parse_week_start


def main():
    parser = argparse.ArgumentParser(description="Weekly search analytics report")
    parser.add_argument("events_path", help="Path to events.jsonl")
    parser.add_argument("--week", required=True, help="Week start date (YYYY-MM-DD, UTC)")
    args = parser.parse_args()

    events = load_events(args.events_path)
    sessions = sessionize(events)
    week_start = parse_week_start(args.week)

    print(build_report(sessions, week_start))


if __name__ == "__main__":
    main()
