"""Eligibility rules for claim reimbursement.

Each rule returns either None (rule passes, continue) or a DenialReason.
The processor evaluates rules in order; the first denial short-circuits.
"""
from datetime import date
from typing import Optional

from reimbursement.models import (
    Claim,
    DenialReason,
    Member,
    Provider,
    ApprovedProvider,
)


def check_in_network(claim: Claim, member: Member, provider: Provider) -> Optional[DenialReason]:
    """Provider must be in the member's insurance network."""
    if not provider.in_network:
        return DenialReason.NOT_IN_NETWORK
    return None


def check_provider_approved(claim: Claim, member: Member, provider: Provider) -> Optional[DenialReason]:
    """Provider must be on the member's approved list as of the date of service."""
    for approved in member.approved_providers:
        if approved.npi == claim.provider_npi and (approved.added_on < claim.date_of_service):
            return None
    if check_approved_details(claim, provider ):
        return None
    return DenialReason.PROVIDER_NOT_APPROVED


# CPT codes for non-reimbursable service types under our standard HRA plan
EXCLUDED_CPT_PREFIXES = ("D",)  # Dental codes start with D


def check_service_covered(claim: Claim, member: Member, provider: Provider) -> Optional[DenialReason]:
    """Some service types aren't covered under the HRA plan (e.g. dental)."""
    if claim.cpt_code.startswith(EXCLUDED_CPT_PREFIXES):
        return DenialReason.SERVICE_NOT_COVERED
    return None


def check_deductible(claim: Claim, member: Member, provider: Provider) -> Optional[DenialReason]:
    """If the member's plan has a deductible (HSA-paired plans), they must have met it."""
    if member.deductible_cents == 0:
        return None
    if member.deductible_met_cents < member.deductible_cents:
        return DenialReason.BELOW_DEDUCTIBLE
    return None

def check_approved_details(claim: Claim, provider: Provider) -> bool:
    """claims for preventive care visits should be reimbursed even if the provider isn't on the member's approved list**, 
    as long as the provider is in-network. CPT codes for preventive care are in the 99381 - 99397 range."""
    if provider.in_network and claim.cpt_code >= 99381 and claim.cpt_code <= 99397:
        return True
    return False




# Rules run in order. First denial wins.
RULES = (
    check_in_network,
    check_provider_approved,
    check_service_covered,
    check_deductible,
)
