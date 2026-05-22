"""Main entry point for processing claims."""
from typing import Mapping

from reimbursement.models import (
    Claim,
    Member,
    Provider,
    ReimbursementDecision,
)
from reimbursement.rules import RULES


def process_claim(
    claim: Claim,
    member: Member,
    provider: Provider,
) -> ReimbursementDecision:
    """Run a claim through the rule pipeline and produce a decision."""
    for rule in RULES:
        denial = rule(claim, member, provider)
        if denial is not None:
            return ReimbursementDecision(
                claim_id=claim.claim_id,
                approved=False,
                reimbursement_cents=0,
                denial_reason=denial,
            )

    return ReimbursementDecision(
        claim_id=claim.claim_id,
        approved=True,
        reimbursement_cents=claim.member_responsibility_cents,
    )


def process_batch(
    claims: list[Claim],
    members: Mapping[str, Member],
    providers: Mapping[str, Provider],
) -> list[ReimbursementDecision]:
    """Process a batch of claims, looking up the member and provider for each."""
    decisions = []
    for claim in claims:
        member = members[claim.member_id]
        provider = providers[claim.provider_npi]
        decisions.append(process_claim(claim, member, provider))
    return decisions
