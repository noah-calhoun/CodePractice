"""Loads a batch of claims from a JSON file and runs them through the processor.

Usage:
    python -m reimbursement.loader <path-to-batch.json>
"""
import json
import sys
from datetime import date
from typing import Any

from reimbursement.models import (
    ApprovedProvider,
    Claim,
    Member,
    Provider,
)
from reimbursement.processor import process_batch


def _parse_date(s: str) -> date:
    return date.fromisoformat(s)


def load_batch(path: str) -> tuple[list[Claim], dict[str, Member], dict[str, Provider]]:
    with open(path) as f:
        payload: dict[str, Any] = json.load(f)

    providers = {
        p["npi"]: Provider(
            npi=p["npi"],
            name=p["name"],
            specialty=p["specialty"],
            in_network=p["in_network"],
        )
        for p in payload["providers"]
    }

    members = {}
    for m in payload["members"]:
        approved = tuple(
            ApprovedProvider(npi=ap["npi"], added_on=_parse_date(ap["added_on"]))
            for ap in m.get("approved_providers", [])
        )
        members[m["member_id"]] = Member(
            member_id=m["member_id"],
            plan_id=m["plan_id"],
            deductible_cents=m.get("deductible_cents", 0),
            deductible_met_cents=m.get("deductible_met_cents", 0),
            approved_providers=approved,
        )

    claims = [
        Claim(
            claim_id=c["claim_id"],
            member_id=c["member_id"],
            provider_npi=c["provider_npi"],
            date_of_service=_parse_date(c["date_of_service"]),
            cpt_code=c["cpt_code"],
            billed_cents=c["billed_cents"],
            member_responsibility_cents=c["member_responsibility_cents"],
        )
        for c in payload["claims"]
    ]

    return claims, members, providers


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m reimbursement.loader <path-to-batch.json>")
        sys.exit(1)

    claims, members, providers = load_batch(sys.argv[1])
    decisions = process_batch(claims, members, providers)

    approved_count = sum(1 for d in decisions if d.approved)
    total_reimbursed = sum(d.reimbursement_cents for d in decisions)

    print(f"Processed {len(decisions)} claims")
    print(f"  Approved: {approved_count}")
    print(f"  Denied:   {len(decisions) - approved_count}")
    print(f"  Total reimbursement: ${total_reimbursed / 100:.2f}")
    print()
    for d in decisions:
        status = "APPROVED" if d.approved else f"DENIED ({d.denial_reason.value})"
        amount = f"${d.reimbursement_cents / 100:.2f}"
        print(f"  {d.claim_id}: {status} {amount}")


if __name__ == "__main__":
    main()
