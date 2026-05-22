# Claims Reimbursement Processor

## Context

You're joining the Claims Core team. We process medical claims from our insurance partners, decide which qualify for member reimbursement under their Garner HRA plan, and emit reimbursement events downstream.

The service `reimbursement/` is an early version that an engineer hacked together to unblock a pilot. It works for the happy path, but the team has been finding issues and we need to harden it before rolling out to a new employer client next week.

We don't expect you to finish everything. We care more about how you reason through the code, what you ask, and how you handle the tradeoffs.

## The codebase

```
reimbursement/
  models.py       # Claim, Member, Provider, ReimbursementDecision dataclasses
  rules.py        # Eligibility rules
  processor.py    # Main entry point: process_claim()
  loader.py       # Loads claims from a JSON batch file
tests/
  test_processor.py  # Existing tests, all passing
sample_claims.json   # Example batch
```

Run the tests:
```
pytest tests/ -v
```

Run the processor against the sample batch:
```
python -m reimbursement.loader sample_claims.json
```

## Tasks

### Task 1: Bug report from Concierge

A member messaged the Concierge team:

> "I saw Dr. Patel last Tuesday, she's on my approved provider list, but my claim got denied. The denial reason says 'provider not approved on date of service' but I added her to my list back in March."

Find the bug, fix it, and add a test that would have caught it.

### Task 2: New rule

Product wants to add a rule: **claims for preventive care visits should be reimbursed even if the provider isn't on the member's approved list**, as long as the provider is in-network. CPT codes for preventive care are in the 99381–99397 range.

Add this rule. Talk through where it fits in the existing pipeline.

### Task 3: Open-ended

The batch loader currently loads the entire JSON file into memory and processes claims sequentially. We're about to onboard a partner that will send us batches of ~500k claims per day. Walk through how you'd evolve this and, if there's time, sketch the change.
