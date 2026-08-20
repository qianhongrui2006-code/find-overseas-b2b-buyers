---
name: find-overseas-b2b-buyers
description: Build an ideal customer profile from a user's business description, uploaded product/company documents, images, catalogues, or public company website; discover, verify, score, deduplicate, and export overseas B2B company leads with public business contact details and source evidence. Use when a manufacturer, exporter, factory owner, foreign-trade salesperson, or B2B seller asks to find overseas buyers, importers, distributors, wholesalers, brands, retailers, hospitality suppliers, corporate-gift companies, or similar prospects through web search, Google Maps/Places, directories, exhibitor lists, competitor channels, or company websites, and wants a reviewable Excel lead list.
---

# Find Overseas B2B Buyers

## Objective

Turn incomplete product information into a confirmed search brief, then deliver contact-ready potential customer companies. Optimize for two outcomes: credible purchase-likelihood evidence and a published email or phone number. Treat background enrichment as secondary and never describe inferred likelihood as confirmed current intent.

This WorkBuddy package uses [core/workflow-protocol.md](core/workflow-protocol.md) as the canonical workflow and the JSON Schemas under `core/schemas/` for structured state. Use the web, browser, file-reading, code, and spreadsheet capabilities available in the current WorkBuddy environment. When a capability is unavailable, follow `core/capability-contract.json`, state the limitation, and use the documented fallback instead of claiming completion.

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
- Treat contactability as a hard gate, not a score. Keep a company only when it has at least one sourced, published or verified business email or phone number. If both are absent, exclude it from the final lead list; a contact form, social direct-message route, or inferred-only email does not pass this gate.
- Keep product relationship separate from channel similarity. A company that only sells, uses, or services an adjacent/complementary product is a discovery candidate, not a qualified buyer, unless official evidence establishes a transactional bridge to the user's target product.
- Classify every verified candidate as `exact_target`, `direct_use`, `adjacent_with_transaction_bridge`, `adjacent_only`, `unrelated`, or `unknown`. By default, only the first three may enter the main qualified list. Put `adjacent_only` in review; contactability can never compensate for a missing target-product purchase pathway.

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

- Use `fast_calibration` for the first 3–10 leads, repeated market tests, or when the user asks for speed. Reuse a confirmed brief, create a pool of about 3 times the target, run deterministic triage, deeply verify only the best survivors, and postpone formal workbook production until the sample is accepted unless the user explicitly requests Excel.
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

Explain the reasoning in business language. For example, a glassware distributor already carrying drinking glasses is a prospect because its catalogue and channel imply recurring sourcing—not because it says “I want glass cups.”

End with a direct confirmation request such as: “请确认是否按以上公司理解和本轮筛选标准执行；如需修改，请指出国家、客户类型、产品范围或数量。” Treat “确认”“可以”“按这个执行” or an equally clear reply as approval. A requested quantity, website URL, uploaded file, or instruction to find leads is not by itself approval of the generated brief.

Do not enter prospect discovery, including a calibration sample, until the user explicitly confirms this brief. Reading the user's own public website to build the company understanding is allowed before confirmation. If the target geography is missing or ambiguous, ask for it; do not substitute the supplier's global customer footprint. If the user later changes a material field—especially country or region, product scope, buyer type, exclusions, or count—issue a revised short brief and reconfirm before continuing.

### 3. Plan discovery

Read [references/search-playbook.md](references/search-playbook.md). Build English and local-language term groups for products, buyer identities, demand signals, geography, and exclusions. Use several complementary queries rather than one oversized query.

Prefer sources in this order when appropriate:

1. Company websites and product/catalogue pages.
2. Search APIs or user-visible web search for discovery.
3. Google Places/Maps or local business directories.
4. Trade associations and exhibitor/member lists.
5. Competitor stockists, dealers, and retailer networks.
6. Official company social pages and LinkedIn for company/contact enrichment.
7. Licensed trade/import or contact databases when the user has access and requests them.

Treat government registries as an optional identity-check source, not a default discovery channel or a commercial-value signal. Use them only for shortlisted candidates whose legal identity, operating status, or location is ambiguous or conflicting. Prefer official APIs/open datasets or a small manual lookup; do not bulk-enumerate registry pages.

When the user requests social demand discovery, read [references/social-demand-signals.md](references/social-demand-signals.md). Search only publicly accessible/indexed content unless the user provides an authorized platform session or API. Treat a social post as a time-sensitive clue; link it to an identifiable company and corroborate the company's website/contact details before qualification.

Apply social recency and geography gates before scoring: default to 30 days for strong signals, 90 days for usable signals, and treat older posts as background unless an active future deadline is explicit. Verify the company's target-market presence from an authoritative source; language, hashtag, poster location, or geotag alone is not enough.

Treat search snippets and list documents as discovery evidence only. Verify candidates on an official site or another authoritative source.

For `fast_calibration`, start with at most three high-yield query families. Stop adding queries once the candidate pool reaches roughly 3 times the requested count or marginal results are mostly duplicates/noise.

### 4. Research a calibration sample

- Research 3–10 companies before scaling unless the user has already validated an identical brief.
- Normalize the official domain and merge duplicate results.
- Check Home, About, Products/Catalogue, Brands, Industries, Locations, Contact, News, and relevant supplier/trade pages.
- Determine company role, product relevance, market relevance, scale fit, demand signals, and contactability.
- Verify the candidate's relationship to the deliverable defined in the current brief. Record a target-product evidence URL and distinguish an evidenced purchase pathway from a speculative cross-sell opportunity.
- Place ambiguous companies in `待人工复核`; do not force them into the qualified list.
- Show the sample and ask for directional feedback before completing a larger batch.

Use `scripts/triage_candidates.py` before deep verification. Feed it lightweight candidate facts and a prior-domain cache. Only open detailed product, legal, group, and contact pages for candidates that survive hard exclusions and rank near the top. Apply a default page budget of four relevant official pages per surviving domain; exceed it only when buyer/manufacturer identity remains decisive.

### 5. Qualify and score

Read [references/qualification-and-evidence.md](references/qualification-and-evidence.md) and [references/investment-validation.md](references/investment-validation.md). Apply hard exclusions first, then score only surviving candidates. Keep scoring explanations tied to evidence.

After the contact and product-relationship gates pass, use a factory-buyer 100-point score: direct procurement capability 25, product/commercial fit 20, purchasing scale and MOQ fit 20, current demand/timing 15, supplier openness/switchability 10, and target-market delivery/compliance fit 10. Do not award points merely because both email and phone are present. Treat contact quality as an outreach-routing note and tie-breaker only.

Assign `evidence_confidence` independently as `high`, `medium`, or `low`, and record an `investment_action`. A high commercial score cannot compensate for low-confidence evidence. Only `high` or `medium` confidence may enter the qualified list; use `manual_review` or exclusion for unresolved material conflicts. Government registration can confirm identity but never adds commercial-score points.

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

- Build a candidate pool approximately 2–5 times the requested qualified count.
- Cache already-read pages and deduplicate by normalized domain.
- Limit pages per domain and stop repeated failed requests.
- Preserve the query/source that discovered each company.
- Report blocked sources, inaccessible pages, and coverage gaps.
- Persist normalized domains, disposition, decisive evidence URL, and last-checked date in the run output so later batches can skip unchanged companies.

### 8. Deliver the workbook

Read [references/output-schema.md](references/output-schema.md). Use `assets/海外B2B客户名单模板.xlsx` when available, or create an equivalent workbook with the spreadsheet tooling available in the environment.

Deliver these sheets:

1. `合格客户`
2. `待人工复核`
3. `排除记录`
4. `搜索策略`
5. `任务说明`

In both lead sheets, put the decision-maker's most actionable fields first: company official name, reference/translated name, website, phone, email, WhatsApp, contact form or contact-source URL, contact person, role, and contact status. Put scoring fields and research evidence after this front contact block.

Verify formulas, filters, URLs, dates, categorical fields, duplicate domains, evidence completeness, and visible layout before delivery. Include a concise batch summary: researched count, qualified count, A/B/C distribution, contact coverage, main exclusions, limitations, and recommended next iteration.

For a speed test, also include a small `效率记录` sheet or structured summary with measured stage durations, candidate counts entering/leaving each stage, pages opened, and avoidable delays. Reuse the bundled workbook template or a tested builder instead of recreating layout logic for every run.

## Stop conditions

Stop and explain the issue when:

- the target product or buyer role remains materially ambiguous after one focused clarification round;
- the user requests prohibited bypassing, private-data harvesting, or deceptive contact practices;
- the only path requires authentication, CAPTCHA solving, paywall bypass, or disallowed automated access;
- available sources cannot support the requested confidence or quantity;
- a required external account, API, or paid database is unavailable.

Offer a safe fallback such as a smaller sample, user-supplied search results, public-source-only research, or a revised target market.
