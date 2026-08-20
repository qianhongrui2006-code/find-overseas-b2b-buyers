# Platform-neutral workflow protocol

This file is the canonical orchestration contract. A platform adapter may change wording and tool syntax, but must preserve state, gates, evidence rules, and outputs.

## States

| State | Purpose | Required output | Next state |
|---|---|---|---|
| `INTAKE` | Accept business description, files, URLs, or mixed input | intake object with source labels | `PROFILE` |
| `PROFILE` | Extract supplier capabilities and create preliminary ICP | profile plus unknowns | `CLARIFY` or `BRIEF` |
| `CLARIFY` | Ask at most one concise round of high-impact questions | updated intake/profile | `BRIEF` |
| `BRIEF` | Define targets, hard rules, signals, exclusions, contacts, sources, count, and output destination | search-brief object | `AWAIT_CONFIRMATION` |
| `AWAIT_CONFIRMATION` | Obtain explicit approval for the company understanding, current-run screening brief, and output destination | approval or requested edits | `SAMPLE` or `BRIEF` |
| `SAMPLE` | Research 3–10 candidates and apply evidence rules | sample batch | `AWAIT_SAMPLE_FEEDBACK` |
| `AWAIT_SAMPLE_FEEDBACK` | Calibrate buyer types and qualification thresholds | approval or corrections | `SCALE` or `BRIEF` |
| `SCALE` | Expand a parallel search-task matrix with limits, cache, and batch deduplication | lightweight researched candidates | `QUALIFY` |
| `QUALIFY` | Apply hard exclusions, internal scoring, and contact status | qualified/review/excluded groups | `QA` |
| `QA` | Validate schemas, evidence, duplicates, contacts, formulas, and counts | QA report | `DELIVER` |
| `DELIVER` | Produce workbook and concise batch summary | XLSX plus batch object | terminal |
| `BLOCKED` | Record unavailable capability, source, permission, or legal boundary | blocker and safe fallback | user-dependent |

## Mandatory gates

1. Do not enter `SAMPLE` or `SCALE` before the user explicitly confirms the company understanding, current-run screening brief, and output destination. If the user did not provide a folder, ask exactly once whether to provide one or accept a displayed concrete default. Once supplied or accepted, do not ask again unless writing fails or the user changes the path. A website, file, requested lead count, or initial instruction to search is not confirmation. Reading the supplier's own public website during `PROFILE` is allowed. If country or region, product scope, buyer type, exclusions, count, or output destination changes materially, return to `BRIEF` and reconfirm.
2. Treat the supplier's global or historical market coverage as profile context, never as the current search geography. Search only the countries or regions confirmed in the current brief.
3. Do not retain a final lead without at least one sourced published or verified business email or phone number; if both are absent, place it in `excluded` with `no_usable_email_or_phone`. Contact forms and inferred-only emails do not pass this gate.
4. Do not place a company in `qualified` without an official domain or authoritative identity source, an eligible product relationship (`exact_target`, `direct_use`, or `adjacent_with_transaction_bridge`), a target-product evidence URL, direct procurement capability, and the contact gate. `adjacent_only` belongs in review or a separately labeled expansion lane.
5. Do not place a contact value in output without status, source URL, and retrieval date.
6. Do not mark current purchase intent unless a dated source explicitly supports it.
7. Keep commercial score separate from evidence confidence. A `low`-confidence candidate cannot enter `qualified` regardless of score; unresolved material identity, product-pathway, geography, or contact conflicts require review or exclusion.
8. Treat government registration as optional identity evidence only. Do not bulk-enumerate registries by default, do not add commercial points for registration, and stop at login, CAPTCHA, paywall, `429`, or access denial.
9. For every source channel planned in the confirmed brief, record `found`, `checked_no_result`, `blocked`, `unavailable`, or `not_checked`, plus concise findings and URLs where available. Mark explicit purchase intent only from a dated source that directly requests the target product, supplier, quotation, tender response, or procurement partner.
10. Never write generated customer data into the installed Skill directory. Save all deliverables below the confirmed output root; request normal host permission for paths outside the workspace and never silently substitute another directory.
11. Do not enter `DELIVER` until QA reports no blocking schema, evidence, channel-disclosure, destination, or duplicate errors.
12. For commercial/shipment/logistics platforms, identify the record role before qualification. Do not treat forwarders, brokers, NVOCCs/carriers, notify parties, or care-of addresses as product buyers without separate official evidence.

## Source labels

Use these labels for supplier-profile facts:

- `user_confirmed`
- `document_confirmed`
- `website_confirmed`
- `inferred`
- `unknown`

Use these labels for contacts:

- `published_official_site`
- `published_official_social`
- `published_directory_or_api`
- `verified_third_party`
- `inferred_unverified`
- `none`

## Capability negotiation

At startup, compare platform tools with `core/capability-contract.json`.

- If `public_web_read` is missing, build the profile from user-provided text/files and output a research plan rather than claiming researched leads.
- If `web_search` is missing, accept user-provided URLs or candidate lists.
- If `file_read` is missing, ask the user to paste relevant text or provide a public URL.
- If `xlsx_write` is missing, output schema-valid JSON/CSV and instruct the host platform to convert it externally.
- If a paid/authorized provider is unavailable, omit that source and report the resulting coverage limitation.

Never simulate a missing capability.

## Idempotency and resume

Assign `task_id`, `brief_id`, and `batch_id`. Persist the last completed state, confirmed brief, executed queries, normalized domains, source timestamps, and blockers. On resume, continue from the last valid state and avoid re-fetching unchanged pages when cached evidence is still acceptable.

## Error policy

Retry transient reads within host limits. Stop repeated failures. Do not bypass authentication, CAPTCHAs, robots instructions, paywalls, or access blocks. Move to `BLOCKED` with a concrete safe fallback.

## Efficiency contract

Within `SAMPLE` and `SCALE`, use this sub-funnel:

1. `DISCOVER_LIGHT`: build a confirmed-country × priority-buyer-type × language task matrix. Run independent cells concurrently when supported, otherwise round-robin them in small batches. Start with official-site web search, industry directories/associations, and Maps/local profiles. Collect only company name, official/candidate URL, country, buyer-type clue, source role, product/HS clue, latest relevant date, visible contact clue, discovery query, and known-domain match. Persist lightweight JSON/CSV; do not enrich contacts, addresses, social links, or long evidence.
2. `TRIAGE`: normalize domains, remove prior/duplicate domains, apply hard exclusions, and rank survivors with `scripts/triage_candidates.py`.
3. `VERIFY_CORE`: open only high-ranked survivors. Default to one product/category page plus one contact page or authoritative Maps/local profile. Open one About/group/legal page only when identity, ownership, or geography remains decisive; stop when qualification is already decided.
4. `CONTACT_MINIMUM`: collect one sourced published or verified email or phone for surviving companies. Stop when either is found. Exclude candidates when both remain absent after allowed sources are exhausted. Contact forms may be reported as supplementary routes but do not pass the gate. Named-person enrichment and a second contact channel are optional and come later.
5. `ENRICH_ON_DEMAND`: use social, news, recruitment, licensed trade/shipment data, and contact providers only for finalists, unresolved material questions, explicit-intent research, or user-requested depth. Record untriggered planned channels as `not_checked`.
6. `DELIVER_ONCE`: after the target set or honest shortfall is finalized, generate one workbook from verified structured records, apply formatting once, and run one QA pass. Show only owner-facing sales fields; keep lead IDs, scores, normalized domains, queries, and exclusion logs in structured internal data.

For calibration, stop discovery near 1.5–2 times the requested lead count. If fewer candidates survive, expand the best-yield matrix cells or run one additional query family before lowering any threshold. Cache normalized domains and decisive evidence so subsequent runs do not repeat unchanged work.
