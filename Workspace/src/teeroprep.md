Systems Design Question for Teero
Context
Teero is a dental staffing and revenue cycle management (RCM) platform. Key services include:

- On-demand dental hygienist staffing with marketplace matching
- Insurance verification and pre-authorization workflows
- Claims submission, denial management, and payment posting
- Integration with major practice management systems (Dentrix, Eaglesoft, Open Dental)
- Real-time analytics and KPI dashboards for RCM metrics

Problem Statement
You're designing the core Insurance Verification and Pre-Authorization Engine for Teero's RCM platform. This system must handle the front-line verification process that occurs 7 days before patient appointments to prevent claim denials and cash flow delays.
Key Requirements:

1. Real-time Eligibility Checks - Query hundreds of insurance carriers using their varied APIs and data formats. Normalize responses into a consistent schema. Each query must return coverage details (deductibles, annual maximums, frequency limitations, waiting periods, prior authorization needs) within 10 seconds.

2. Insurance Carrier Integration - Multiple carriers (Delta Dental, Aetna, Blue Cross, UnitedHealth, etc.) expose eligibility through different APIs with unique response structures. Some support real-time queries, others require batch files. Some carriers are unreachable due to network issues or outdated systems.

3. Practice Management System (PMS) Sync - Write-back normalized benefit data to the patient record in the connected PMS (Dentrix, Eaglesoft, Open Dental) via their APIs. Teero must not assume a single PMS; practices may use different systems.

4. Pre-Authorization Workflow - For high-value treatments (> $500), automatically request pre-authorization when needed. Track pre-auth IDs, expiration dates, and compliance with frequency limitations (e.g., one cleaning per 6 months). Alert billing specialists if a scheduled treatment conflicts with benefit restrictions.
5. Denial Prevention and Accuracy - Detect data inconsistencies (patient DOB mismatch, expired insurance IDs, member ID formatting errors) before claims are submitted. Flag high-risk procedures that trigger denials 20% of the time with that carrier.
6. Scalability - Teero partners with hundreds of dental practices. The system must handle 10,000+ verification requests per day across thousands of patient schedules and manage concurrent requests from multiple PMS integrations.
7. Fallback and Offline Handling - When carrier APIs are down or queries timeout, the system must gracefully degrade. Store recent eligibility snapshots and allow manual verification override with audit trails. Practices should never be blocked from scheduling.
8. Compliance and Security - HIPAA-compliant handling of patient PII and insurance data. Encrypt data in transit and at rest. Maintain audit logs for every lookup (who requested it, which carrier, response time, data returned).

Questions to Address:

- How would you structure the carrier integration layer to handle hundreds of different API formats and latency profiles? What's your strategy for normalizing disparate eligibility responses into a unified schema?
- Describe the system architecture for handling concurrent PMS write-backs. How do you ensure atomicity when writing normalized benefits to Dentrix, Eaglesoft, and Open Dental simultaneously without data inconsistencies?
- What data structures and caching strategy would you use to store recent eligibility results? How would you balance freshness (re-verifying frequently) with latency and carrier API rate limits?
- Design the pre-authorization tracking system. How do you detect when a scheduled treatment violates frequency limitations or requires pre-auth before the claim is submitted?
- How would you implement the fallback mechanism when carriers are unreachable? What is the patient/practice experience when real-time verification fails?
- Design the denial prevention heuristic engine. How would you surface high-risk procedures to billing specialists before claims are submitted?
- Walk through the end-to-end flow from appointment scheduling to pre-verification completion. Where are the critical path bottlenecks, and how would you measure success (e.g., 95% of appointments verified 7 days ahead)?


# Requirments/major steps:
- Insurance Verification & Pre-Authorization (happens BEFORE treatment)
- Claim Submission (happens AFTER treatment)
- Payment Posting & Denial Management (happens AFTER carrier responds)




- ## Initial Injest Architecture:
- Injest Customer Insurance+data:
-   Need to parse this data, and format it using the associated insurance provider (Blue Cross, UnitedHealth, etc.)
- Query Insurance Carrier for insurance plan details (deductibles, annual maximums, frequency limitations, waiting periods, prior authorization needs)
- Check eligablility based on provider- have different endpoints routing (backed by a queue) based on desired request format by vendor (real-time endpoint, batching, other)
- Confirm eligablility, request from customer if needed. 

- ## Send claim to Insurence:
- Send payload to insurence with previously Authed customer data
- Process EOB to desired format (could use LLM for this if data fields are wildly inconsistent)
-   If Error on EOB, proceed to denial Prevention

- ## Denial Prevention
- Parse EOB denial for reason, elevate this to customer dashboard, highlighting if it is actionable.