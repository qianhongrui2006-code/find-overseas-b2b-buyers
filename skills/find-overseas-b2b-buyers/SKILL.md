---
name: find-overseas-b2b-buyers
description: Build an ideal customer profile from a user's business description, uploaded product/company documents, images, catalogues, or public company website; discover, verify, internally score, deduplicate, and export overseas B2B company leads with public business contact details and source evidence. Use when a manufacturer, exporter, factory owner, foreign-trade salesperson, or B2B seller asks to find overseas buyers, importers, distributors, wholesalers, brands, retailers, hospitality suppliers, corporate-gift companies, or similar prospects through web search, Google Maps/Places, commercial directories, public or authorized trade-data platforms, exhibitor lists, competitor channels, or company websites, and wants a concise reviewable Excel lead list.
---

# Find Overseas B2B Buyers

## Objective

Turn incomplete product information into a confirmed search brief, then deliver contact-ready potential customer companies. Optimize for two outcomes: credible purchase-likelihood evidence and a published email or phone number. Treat background enrichment as secondary and never describe inferred likelihood as confirmed current intent.

This Codex adapter is one entry point to the platform-neutral package. Use [core/workflow-protocol.md](core/workflow-protocol.md) as the canonical state machine and the JSON Schemas under `core/schemas/` whenever exchanging structured state with another platform or service.

## Non-negotiable rules

- Do not claim that a company wants to buy merely because it mentions the product.
- Separate confirmed facts, supported inferences, and unknowns.
- Attach a source URL to every material qualification claim and contact field.
- Never invent a company, contact, role, email, phone number, WhatsApp status, company size, revenue, or import history.
- Mark inferred email patterns as `推断-未验证`; do not mix them with published contacts.
- Mark a number as WhatsApp only when an official page explicitly labels it or links to WhatsApp/`wa.me`.
- Prefer public corporate and role-based contacts. Minimize unrelated personal data.
- Respect terms, robots instructions, rate limits, authentication, CAPTCHAs, and paywalls. Never bypass access controls.
- Do not send outreach, submit forms, add CRM records, or message contacts unless the user separately requests and authorizes that action.
- Do not lower qualification standards to reach a requested count. Report shortfalls honestly.
- Treat the supplier's existing or global market coverage as background only. Never expand the current run to every country the supplier serves. Use only the countries or regions explicitly confirmed for the current run.
- Do not start prospect discovery merely because the user supplied a target count such as 50. First present the company understanding and current-run screening brief, then obtain explicit approval.
- Do not start prospect discovery until the output destination is confirmed. If the user has not supplied a folder, ask once in the screening-brief confirmation whether to use a specific path or the displayed default task output folder. Do not repeat the question after the user confirms a path or accepts the default, unless writing to that location fails or the user changes it.
- Treat contactability as a hard gate, not a score. Keep a company only when it has at least one sourced, published or verified business email or phone number. If both are absent, exclude it from the final lead list; a contact form, social direct-message route, or inferred-only email does not pass this gate.
- Keep product relationship separate from channel similarity. A company that only sells, uses, or services an adjacent/complementary product is a discovery candidate, not a qualified buyer, unless official evidence establishes a transactional bridge to the user's target product.
- Classify every verified candidate as `exact_target`, `direct_use`, `adjacent_with_transaction_bridge`, `adjacent_only`, `unrelated`, or `unknown`. By default, only the first three may enter the main qualified list. Put `adjacent_only` in review; contactability can never compensate for a missing target-product purchase pathway.
- Treat freight forwarders, customs brokers, NVOCCs, carriers, and notify parties as intermediaries unless the confirmed brief explicitly targets logistics buyers. Their directory or shipment appearance may reveal a route or candidate, but never proves that they purchase the user's product.

## Select an entry path

Accept any of these inputs:

1. A free-form business description.
2. Uploaded product catalogues, company introductions, quotations, spreadsheets, images, certifications, or existing-customer lists.
3. A public company website or product-page URL.
4. A mixture of the above.

When the user has not supplied enough context, tell them they can upload documents or provide a website instead of completing a long questionnaire. Before reading a public website, state that only public pages will be used and that the extracted profile will require confirmation.

Use this information precedence when sources conflict:

1. The user's current explicit statement.
2. Current user-provided internal documents.
3. Explicit content on the user's public website.
4. Clearly identified AI inference.

Read [references/intake-and-icp.md](references/intake-and-icp.md) whenever collecting information or building the customer profile.

## Execute the workflow

### Choose a run mode

Read [references/fast-mode.md](references/fast-mode.md) before research.

- Use `fast_calibration` for the first 3–10 leads, repeated market tests, or when the user asks for speed. Reuse a confirmed brief, create a pool of about 1.5–2 times the target, run deterministic triage, deeply verify only the best survivors, and postpone formal workbook production until the final qualified set is accepted unless the user explicitly requests Excel earlier.
- Use `full_research` for an approved larger batch. Keep the same staged funnel but expand the source mix and contact enrichment.
- Record actual wall-clock time for discovery, triage, deep verification, contact enrichment, and delivery. Do not present an estimate as measured time.

### 1. Extract and label information

- Extract products, materials, applications, differentiators, cooperation modes, MOQ, price position, capacity, lead time, certifications, markets, and existing customer patterns.
- For each important item, label it `用户确认`, `资料确认`, `官网确认`, `推断`, or `未知`.
- Do not ask for information already confirmed by a higher-priority source.
- Ask only questions whose answers materially change target countries, buyer types, qualification, or research depth. Prefer one concise round.

### 2. Build a search brief

Before any prospect discovery, produce one short, confirmation-ready response with two clearly separated parts.

**Company understanding**

- what the supplier sells and does not sell;
- likely advantages, cooperation model, capacity/MOQ, and compliance constraints when known;
- facts taken from the user, files, or website versus important assumptions and unknowns.

**Current screening target**

- product scope and confusing products to exclude;
- target countries or regions for this run and search languages;
- buyer types in priority order;
- hard requirements, positive signals, and exclusions;
- desired contact roles and acceptable fallback contacts;
- target count and research depth;
- proposed sources and limitations.
- output folder for the workbook, channel evidence, intermediate data, and execution summary; mark it as user-specified or default-accepted.

Explain the reasoning in business language. For example, a glassware distributor already carrying drinking glasses is a prospect because its catalogue and channel imply recurring sourcing—not because it says “I want glass cups.”

If the user already supplied an output path, repeat it in the brief and include it in the ordinary approval request; do not ask a second folder question. If no path was supplied, display a concrete default such as `<current-workspace>/outputs/<task-name>-<date>` and ask exactly once: “请提供输出文件夹，或回复‘使用默认目录’。” The user must either provide a path or explicitly accept the displayed default.

End with a direct confirmation request such as: “请确认是否按以上公司理解、本轮筛选标准和输出位置执行；如需修改，请指出国家、客户类型、产品范围、数量或保存路径。” Treat “确认”“可以”“按这个执行” or an equally clear reply as approval only when an output destination has already been supplied or accepted. A requested quantity, website URL, uploaded file, or instruction to find leads is not by itself approval of the generated brief.

Do not enter prospect discovery, including a calibration sample, until the user explicitly confirms this brief and `output_destination_status` is `confirmed`. Reading the user's own public website to build the company understanding is allowed before confirmation. If the target geography is missing or ambiguous, ask for it; do not substitute the supplier's global customer footprint. If the user later changes a material field—especially country or region, product scope, buyer type, exclusions, count, or output path—issue a revised short brief and reconfirm before continuing.

### 3. Plan discovery

Read [references/search-playbook.md](references/search-playbook.md). Build English and local-language term groups for products, buyer identities, demand signals, geography, and exclusions. Use several complementary queries rather than one oversized query.

Build a search-task matrix across confirmed countries, priority buyer types, and relevant languages. Execute independent cells concurrently when the host supports safe parallel search; otherwise rotate through cells in small batches so one country or buyer type cannot consume the full search budget. Deduplicate normalized domains after every batch.

Use the following source tiers rather than checking every channel for every candidate:

1. **Primary discovery and verification:** search APIs or user-visible web search, company websites/product catalogues, industry directories/associations, and Maps/Places or authoritative local business profiles.
2. **Secondary discovery:** competitor stockists, exhibitor/member lists, retailer networks, and public commercial platforms when the primary pool is insufficient or a buyer role needs corroboration.
3. **On-demand enrichment only:** official social pages, news, recruitment, licensed trade/shipment data, and contact providers. Check these only for finalists, unresolved high-value candidates, an explicit-intent request, or a material qualification question.

Mark secondary channels that were not triggered as `not_checked`; do not spend time checking them merely to fill the channel-evidence sheet.

Read [references/commercial-data-platforms.md](references/commercial-data-platforms.md) before using company aggregators, freight/logistics directories, customs records, bills of lading, or user-exported platform data. Record the entity role shown by the source and resolve the candidate to an operating company and official domain before qualification. Never bypass login, CAPTCHA, export, subscription, or API controls; ask the user to provide an authorized export or access route when needed.

Treat government registries as an optional identity-check source, not a default discovery channel or a commercial-value signal. Use them only for shortlisted candidates whose legal identity, operating status, or location is ambiguous or conflicting. Prefer official APIs/open datasets or a small manual lookup; do not bulk-enumerate registry pages.

When the user requests social demand discovery, read [references/social-demand-signals.md](references/social-demand-signals.md). Search only publicly accessible/indexed content unless the user provides an authorized platform session or API. Treat a social post as a time-sensitive clue; link it to an identifiable company and corroborate the company's website/contact details before qualification.

Apply social recency and geography gates before scoring: default to 30 days for strong signals, 90 days for usable signals, and treat older posts as background unless an active future deadline is explicit. Verify the company's target-market presence from an authoritative source; language, hashtag, poster location, or geotag alone is not enough.

Treat search snippets and list documents as discovery evidence only. Verify candidates on an official site or another authoritative source.

For `fast_calibration`, start with at most three high-yield query families per search-task batch. Stop adding queries once the deduplicated candidate pool reaches roughly 1.5–2 times the requested count or marginal results are mostly duplicates/noise. During first-pass discovery save a lightweight JSON/CSV record containing only company name, candidate/official URL, country, buyer-type clue, source role, product/HS clue, dated activity clue, one visible contact clue, and discovery query. Do not collect full addresses, social links, named contacts, every contact channel, long evidence summaries, or workbook formatting until the candidate survives triage.

### 4. Research a calibration sample

- Research 3–10 companies before scaling unless the user has already validated an identical brief.
- Normalize the official domain and merge duplicate results.
- Check Home, About, Products/Catalogue, Brands, Industries, Locations, Contact, News, and relevant supplier/trade pages.
- Determine company role, product relevance, market relevance, scale fit, demand signals, and contactability.
- For every source channel planned for the run, record one of `found`, `checked_no_result`, `blocked`, `unavailable`, or `not_checked`. Never leave the user guessing whether a channel was checked.
- Store channel results as concise audit facts: Maps/local profile keeps the verified address and source URL; official social, news, recruitment, trade-show/association, and authorized trade-data checks keep the relevant URL plus at most one sentence of useful information. Preserve multiple URLs as separate channel records rather than merging them into an unverifiable paragraph.
- Verify the candidate's relationship to the deliverable defined in the current brief. Record a target-product evidence URL and distinguish an evidenced purchase pathway from a speculative cross-sell opportunity.
- Place ambiguous companies in `待人工复核`; do not force them into the qualified list.
- Show the sample and ask for directional feedback before completing a larger batch.

Use `scripts/triage_candidates.py` before deep verification. Feed it lightweight candidate facts and a prior-domain cache. Only open detailed product, legal, group, and contact pages for candidates that survive hard exclusions and rank near the top. Apply a default page budget of four relevant official pages per surviving domain; exceed it only when buyer/manufacturer identity remains decisive.

### 5. Qualify and score internally

Read [references/qualification-and-evidence.md](references/qualification-and-evidence.md) and [references/investment-validation.md](references/investment-validation.md). Apply hard exclusions first, then score only surviving candidates. Keep scoring explanations tied to evidence.

After the contact and product-relationship gates pass, use a factory-buyer 100-point score internally: direct procurement capability 25, product/commercial fit 20, purchasing scale and MOQ fit 20, current demand/timing 15, supplier openness/switchability 10, and target-market delivery/compliance fit 10. Do not award points merely because both email and phone are present. Treat contact quality as an outreach-routing note and tie-breaker only. Keep `lead_id`, score components, total score, normalized domain, discovery query, and exclusion details in the structured run data for deduplication, resuming, and QA; do not expose them in the default owner-facing workbook.

Assign `evidence_confidence` independently as `high`, `medium`, or `low`, and record an `investment_action`. A high commercial score cannot compensate for low-confidence evidence. Only `high` or `medium` confidence may enter the qualified list; use `manual_review` or exclusion for unresolved material conflicts. Government registration can confirm identity but never adds commercial-score points.

Assign `explicit_purchase_intent` independently as `explicit`, `not_found`, or `unclear`. Use `explicit` only when a dated public source clearly requests the target product, a supplier, quotation, tender response, procurement partner, or equivalent transaction. A product catalogue, association membership, exhibitor listing, recruitment post, import record, or company expansion is not explicit purchase intent by itself. When `explicit`, save the exact source URL, source date, target product, and a short paraphrase; never rely on a search snippet alone.

Use `scripts/lead_pipeline.py` for deterministic normalization, duplicate detection, weighted scoring, and schema checks when preparing or auditing structured lead JSON/CSV. Run `python scripts/lead_pipeline.py --help` for usage.

### 6. Find contacts

Read [references/contact-and-compliance.md](references/contact-and-compliance.md). Search official Contact/About/Team pages, page footers, `mailto:`/`tel:` links, structured data, official social profiles, and permitted data providers.

For each contact value save:

- value;
- type or role;
- source URL;
- source/status label;
- retrieval date;
- confidence or unresolved issue.

Do not enrich contacts for candidates already excluded during triage. In fast mode, collect one sourced published or verified business email or phone first; stop contact research once either gate-eligible channel is found. Search for a second channel or named procurement contact only after the company is accepted or the user asks for deeper enrichment. If neither email nor phone can be found after the official contact surfaces and allowed sources are exhausted, exclude the candidate. A contact form is only a reported fallback and never satisfies the final-list contact gate.

### 7. Scale with controls

- Build a deduplicated candidate pool approximately 1.5–2 times the requested qualified count in fast mode; expand it only when survivor yield is insufficient.
- Cache already-read pages and deduplicate by normalized domain.
- Limit pages per domain and stop repeated failed requests.
- Preserve the query/source that discovered each company.
- Report blocked sources, inaccessible pages, and coverage gaps.
- Persist normalized domains, disposition, decisive evidence URL, and last-checked date in the run output so later batches can skip unchanged companies.
- Persist lightweight candidate records after each discovery batch, then write verified survivor records separately. Do not build or repeatedly update an XLSX during discovery, triage, or per-company verification.

### 8. Deliver the workbook

Read [references/output-schema.md](references/output-schema.md). Use `assets/海外B2B客户名单模板.xlsx` when available, or create an equivalent workbook with the spreadsheet tooling available in the environment.

Generate the workbook once, after the target set is complete or an honest shortfall has been decided. Build it from the final verified structured records and channel records, then run one formatting and QA pass. Use a concise text/Markdown preview during calibration instead of creating disposable interim workbooks unless the user explicitly requests one.

Save all task outputs under the confirmed output root. Never save generated customer data inside the installed Skill directory. If the confirmed path is outside the active workspace, request the host platform's normal file permission rather than silently changing destinations. Create only task-relevant subfolders beneath the confirmed root. If writing fails, report the exact path and ask whether to grant access or choose a new location; do not continue with an undisclosed fallback.

Deliver four owner-facing sheets:

1. `潜在客户`
2. `待人工复核`
3. `渠道证据`
4. `任务摘要`

Put sales-action fields first: company name, country/city, official website, business email, phone, WhatsApp, and contact-source URL. Follow with buyer type, matching product or purchase pathway, explicit-purchase-intent label and dated URL when present, verified address/map URL, recommended action, concise reason, evidence confidence, last verification date, and notes. Add only `待复核问题` to the review sheet.

Do not show numeric scores, score components, priority tiers, `Lead ID`, normalized domains, discovery queries, or long exclusion/search logs in the default workbook. Preserve them in structured JSON or internal run logs. In `渠道证据`, use one row per company and source URL with the channel, check status, concise finding, source URL, information date, and explicit-intent label. Include planned channels with no result or blocked access so absence is visible rather than silently omitted.

Verify formulas, filters, URLs, dates, categorical fields, duplicate domains, evidence completeness, and visible layout before delivery. Include a concise batch summary: researched count, qualified count, email/phone coverage, explicit-intent count, main exclusions, limitations, and recommended next iteration. Do not show A/B/C distribution unless the user specifically requests the scoring audit.

For a speed test, also include a small `效率记录` sheet or structured summary with measured stage durations, candidate counts entering/leaving each stage, pages opened, and avoidable delays. Reuse the bundled workbook template or a tested builder instead of recreating layout logic for every run.

## Stop conditions

Stop and explain the issue when:

- the target product or buyer role remains materially ambiguous after one focused clarification round;
- the user requests prohibited bypassing, private-data harvesting, or deceptive contact practices;
- the only path requires authentication, CAPTCHA solving, paywall bypass, or disallowed automated access;
- available sources cannot support the requested confidence or quantity;
- a required external account, API, or paid database is unavailable.

Offer a safe fallback such as a smaller sample, user-supplied search results, public-source-only research, or a revised target market.
