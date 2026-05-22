"""Domain models for the reimbursement processor."""
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class DenialReason(str, Enum):
    PROVIDER_NOT_APPROVED = "provider not approved on date of service"
    NOT_IN_NETWORK = "provider not in network"
    SERVICE_NOT_COVERED = "service type not covered under plan"
    BELOW_DEDUCTIBLE = "claim below member deductible"
    DUPLICATE_CLAIM = "duplicate claim already processed"


@dataclass(frozen=True)
class Provider:
    npi: str  # National Provider Identifier
    name: str
    specialty: str
    in_network: bool


@dataclass(frozen=True)
class ApprovedProvider:
    """A provider on a member's approved list, with the date they were added."""
    npi: str
    added_on: date


@dataclass(frozen=True)
class Member:
    member_id: str
    plan_id: str
    deductible_cents: int  # Annual deductible in cents, 0 if none
    deductible_met_cents: int  # Amount of deductible met YTD
    approved_providers: tuple[ApprovedProvider, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Claim:
    claim_id: str
    member_id: str
    provider_npi: str
    date_of_service: date
    cpt_code: str  # Procedure code
    billed_cents: int
    member_responsibility_cents: int  # Out-of-pocket portion


@dataclass(frozen=True)
class ReimbursementDecision:
    claim_id: str
    approved: bool
    reimbursement_cents: int
    denial_reason: Optional[DenialReason] = None
    notes: str = ""
