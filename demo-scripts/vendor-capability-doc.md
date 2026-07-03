# Sample Input — Vendor Capability Doc (Tier 2 demo)

Fictional vendor, fictional capability doc — stands in for "us" during the Tier 2
demo. Paste this into the same chat window as
[`sample-rfp-distributor-portal.md`](./sample-rfp-distributor-portal.md) as the second
input for the Option A prompt.

Deliberately not a perfect match to the RFP — three requirements are a genuine
Partial Fit or Gap, spread across compliance, technical, and logistics, so the agent
has real substance to flag in step 4 of the demo script, not just a wall of green
checkmarks.

---

**Copy everything below this line into the chat window as the second demo input:**

---

# Capability Overview — Northbridge Digital Partners

## Who we are

Northbridge Digital Partners is a mid-market software consultancy specializing in
B2B web portals, order management systems, and enterprise integrations. We've
delivered 30+ portal and e-commerce rebuilds for mid-market manufacturing and
distribution clients over the past eight years.

## Relevant past projects

- **Order portal rebuild, industrial fasteners distributor (2024–2025):**
  Full rebuild of a distributor-facing order portal, including real-time status,
  bulk CSV ordering, and an audit-logged approval workflow. Delivered in a
  phased release, first phase live in 14 weeks.
- **Distributor API layer, packaging supplier (2023):** Built a documented REST
  API exposing order and shipment data for two large distributor accounts who
  wanted to integrate directly rather than use the portal UI.
- **Search performance remediation, wholesale electronics client (2022):**
  Rebuilt order search from a slow SQL-only implementation to an indexed search
  layer, load-tested to 50,000+ historical orders per account.

## Technical capabilities

- **Real-time updates:** Standard capability — WebSocket/event-driven status
  updates are part of our default architecture for order-status use cases.
- **Bulk upload & validation:** Standard capability, including pre-submission
  CSV validation and error reporting.
- **Approval workflows & audit trail:** Standard capability. Every workflow we
  build includes a full audit log of who changed what and when by default —
  this is part of our base platform, not a custom add-on.
- **Single sign-on:** We support SAML 2.0 and OIDC federation broadly, and have
  shipped SSO integrations with Azure AD, Google Workspace, and OneLogin.
  **We have not yet completed a production Okta integration** — our SAML/OIDC
  work should transfer, but Okta-specific configuration (SCIM provisioning,
  Okta-specific claims mapping) would be new territory for our team and would
  need to be scoped and tested rather than treated as a known quantity.
- **Search performance:** Standard capability; see the wholesale electronics
  project above (validated well beyond the 10,000-order threshold requested here).
- **Mobile-responsive design:** Standard capability across all our recent work.
  We do not build native mobile apps as a standard offering, but that isn't
  required for this RFP's Phase 1 scope.
- **Notifications:** Standard capability (email at minimum; SMS/push available
  as an add-on).

## Compliance & security

- Northbridge is **SOC 2 Type I certified** (report available on request).
  **Our SOC 2 Type II audit is in progress, with completion targeted for Q1
  2027** — we do not currently hold a Type II report.
- All hosting is via AWS us-east-1 and us-west-2 regions, meeting US/Canada
  data residency requirements.

## Support

- Standard support hours are **9am–7pm IST (roughly 11:30pm–9:30am Eastern
  the prior day through mid-morning Eastern)**, Monday–Friday, with a 4-hour
  critical-issue response SLA during those hours. After-hours critical support
  is available on a best-effort basis but is not a contracted 24/7 SLA.

## Team & delivery model

- Our delivery teams are distributed, based primarily out of our Dehradun,
  India office, with a US-based account lead for client-facing coordination.
  **We do not maintain a standing US office and do not typically staff
  in-person kickoffs on short notice** — our default kickoff format is a
  structured series of virtual working sessions in the client's business
  hours, with an in-person visit arranged separately if a client requires one
  (typically needing 4–6 weeks' lead time to schedule travel).

## References

Available on request; two references from comparable mid-market portal/e-commerce
rebuild engagements can be provided within 2 business days of request.
