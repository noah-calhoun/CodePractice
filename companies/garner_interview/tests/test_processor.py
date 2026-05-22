"""Existing tests for the reimbursement processor.

These all pass. The candidate should add new tests as part of their work.
"""
from datetime import date

import pytest

from reimbursement.models import (
    ApprovedProvider,
    Claim,
    DenialReason,
    Member,
    Provider,
)
from reimbursement.processor import process_claim


@pytest.fixture
def in_network_provider():
    return Provider(
        npi="1234567890",
        name="Dr. Priya Patel",
        specialty="Endocrinology",
        in_network=True,
    )


@pytest.fixture
def out_of_network_provider():
    return Provider(
        npi="9999999999",
        name="Dr. Out of Network",
        specialty="Dermatology",
        in_network=False,
    )


@pytest.fixture
def standard_member(in_network_provider):
    return Member(
        member_id="M-1001",
        plan_id="PLAN-HRA-STANDARD",
        deductible_cents=0,
        deductible_met_cents=0,
        approved_providers=(
            ApprovedProvider(npi=in_network_provider.npi, added_on=date(2026, 1, 1)),
        ),
    )


def _claim(provider_npi: str, **overrides) -> Claim:
    defaults = dict(
        claim_id="C-1",
        member_id="M-1001",
        provider_npi=provider_npi,
        date_of_service=date(2026, 5, 1),
        cpt_code="99214",
        billed_cents=20000,
        member_responsibility_cents=5000,
    )
    defaults.update(overrides)
    return Claim(**defaults)


def test_approved_claim_with_in_network_approved_provider(standard_member, in_network_provider):
    claim = _claim(in_network_provider.npi)
    decision = process_claim(claim, standard_member, in_network_provider)
    assert decision.approved is True
    assert decision.reimbursement_cents == 5000


def test_denied_when_provider_out_of_network(standard_member, out_of_network_provider):
    claim = _claim(out_of_network_provider.npi)
    decision = process_claim(claim, standard_member, out_of_network_provider)
    assert decision.approved is False
    assert decision.denial_reason == DenialReason.NOT_IN_NETWORK


def test_denied_when_dental_service(standard_member, in_network_provider):
    claim = _claim(in_network_provider.npi, cpt_code="D2740")
    decision = process_claim(claim, standard_member, in_network_provider)
    assert decision.approved is False
    assert decision.denial_reason == DenialReason.SERVICE_NOT_COVERED


def test_denied_when_below_deductible(in_network_provider):
    member = Member(
        member_id="M-1003",
        plan_id="PLAN-HRA-HSA",
        deductible_cents=200000,
        deductible_met_cents=50000,
        approved_providers=(
            ApprovedProvider(npi=in_network_provider.npi, added_on=date(2026, 1, 1)),
        ),
    )
    claim = _claim(in_network_provider.npi, member_id="M-1003")
    decision = process_claim(claim, member, in_network_provider)
    assert decision.approved is False
    assert decision.denial_reason == DenialReason.BELOW_DEDUCTIBLE


def test_denied_when_provider_added_after_service(in_network_provider):
    member = Member(
        member_id="M-1001",
        plan_id="PLAN-HRA-STANDARD",
        deductible_cents=0,
        deductible_met_cents=0,
        approved_providers=(
            ApprovedProvider(npi=in_network_provider.npi, added_on=date(2026, 6, 1)),
        ),
    )
    claim = _claim(in_network_provider.npi, date_of_service=date(2026, 5, 1))
    decision = process_claim(claim, member, in_network_provider)
    assert decision.approved is False
    assert decision.denial_reason == DenialReason.PROVIDER_NOT_APPROVED

def test_last_provider_in_approoved_claimms(in_network_provider):
        member = Member(
            member_id="M-1001",
            plan_id="PLAN-HRA-STANDARD",
            deductible_cents=0,
            deductible_met_cents=0,
            approved_providers=(
                ApprovedProvider(npi=in_network_provider.npi, added_on=date(2026, 6, 1)),
                ApprovedProvider(npi=in_network_provider.npi, added_on=date(2026, 4, 1)),
                ApprovedProvider(npi=in_network_provider.npi, added_on=date(2026, 5, 1)),
        ),
        )
        claim = _claim(in_network_provider.npi, member_id="M-1001")
        decision = process_claim(claim, member, in_network_provider)
        assert decision.approved is True


