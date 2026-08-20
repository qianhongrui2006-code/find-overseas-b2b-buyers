# Qualification and Evidence

## Hard exclusions first

Exclude before scoring when a confirmed condition violates the brief: wrong geography, irrelevant industry, inactive company, marketplace/listicle only, missing identifiable company entity, existing CRM suppression, or direct competitor when the user excludes competitors.

Keep an exclusion record with company/domain, URL, rule, evidence, and date.

## Claim-specific evidence

Use the source that is authoritative for the claim rather than one global hierarchy. Official company pages and catalogues are strongest for products, commercial role, locations, and contacts. Maps/local business profiles can corroborate operating presence. Official social/news/recruitment pages support dated activity. Association and trade-show pages support participation, not purchase intent. Licensed trade data can support import behavior when entity and product classification match. Government registries support legal identity and status only; do not use registration as a commercial-value signal or bulk discovery channel.

Search snippets and unverified aggregations are discovery clues only. Record contradictory sources and mark unresolved conflicts rather than choosing silently. Apply the separate evidence-confidence and safe-verification rules in [investment-validation.md](investment-validation.md).

## Product-relationship gate

Classify the relationship to the current brief's target deliverable before scoring:

| Value | Meaning | Default disposition |
|---|---|---|
| `exact_target` | The company officially sells, distributes, imports, brands, sources, or procures the target deliverable | eligible for qualification |
| `direct_use` | The company demonstrably deploys or consumes the target deliverable in an operationally meaningful way | eligible when it plausibly controls or influences purchasing |
| `adjacent_with_transaction_bridge` | The company is in an adjacent category, but official evidence explicitly connects its offer or operations to buying the target deliverable | eligible, with the bridge explained |
| `adjacent_only` | Same channel, customer, application, compatible equipment, or complementary category, but no evidence it buys the target deliverable | review/expansion lane only |
| `unrelated` | No meaningful product relationship | exclude |
| `unknown` | Evidence is insufficient | review |

A transactional bridge can be an official target-product SKU, bundle, replenishment/service obligation, verified consumption program, sourcing notice, supplier requirement, tender, or another explicit commercial mechanism that requires the candidate to obtain the target deliverable. Adapt these mechanisms to the current industry; do not hardcode product examples into the reusable rules.

Channel overlap, compatibility, downstream customer similarity, or possession of a complementary product is not itself a transactional bridge. If the brief explicitly asks for speculative category-expansion leads, keep them in a separately labeled expansion lane rather than mixing them with verified core buyers.

## Contact gate

Apply this before scoring. A final lead must have at least one sourced, published or verified business email or phone number. Either channel is sufficient; having both does not add points.

- Accept: an email or phone published on an official company site/social profile, an authoritative business directory, or a permitted verification provider, with source URL and retrieval date.
- Reject as gate evidence: contact form only, LinkedIn/social direct-message route only, inferred email pattern, unlabeled personal contact, or a number merely assumed to support WhatsApp.
- If both email and phone remain absent after checking the allowed contact sources, do not score the company. Move it to `排除记录` with reason `no_usable_email_or_phone`. Do not leave it in the main or review lead sheets merely to reach the requested count.
- Store contact status and source for audit, but use contact quality only to choose an outreach route or break a tie between otherwise equal leads.

## Factory-buyer score (100)

| Dimension | Max | Typical evidence |
|---|---:|---|
| Direct procurement capability | 25 | controls supplier/category selection, imports, distributes, operates private label, or directly procures for its own operations |
| Product/commercial fit | 20 | eligible product relationship plus compatible assortment, use case, price/quality position, customization, or cooperation model |
| Purchasing scale and MOQ fit | 20 | chain/network reach, wholesale volume, recurring consumption, locations, contract size, or other evidence compatible with factory MOQ/capacity |
| Current demand/timing | 15 | dated sourcing request, tender, supplier onboarding, restocking, launch, expansion, procurement hiring, or current recurring replenishment |
| Supplier openness/switchability | 10 | multi-brand sourcing, external suppliers, private label, vendor onboarding, assortment change, or evidence that supply is not structurally closed |
| Target-market delivery/compliance fit | 10 | geography, certifications, specifications, logistics, language, lead time, and cooperation terms fit the supplier brief |

Use evidence quality as a gate, not compensating points. Do not award points without a source URL or explicit source note. Suggested anchors:

- Direct procurement capability: 25 explicit target-product procurement/import/category authority; 20 distributor, wholesaler, brand, chain, or e-commerce operator demonstrably selecting suppliers; 15 professional reseller/service operator with recurring buying; 10 direct-use organization that controls procurement; 0–5 unclear influence or no purchasing control.
- Product/commercial fit: 20 exact target with compatible commercial model; 16 exact category but specifications/positioning need confirmation; 12 direct use or an evidenced adjacent transaction bridge; 0 for `adjacent_only`, `unrelated`, or `unknown` because those relationships cannot qualify.
- Purchasing scale and MOQ fit: 20 strong volume/network/contract evidence and clear factory fit; 15 plausible recurring or regional-scale fit; 10 smaller but viable order pattern; 5 scale unknown; 0 confirmed mismatch. A single small consumer shop should normally score 0–5 unless the brief explicitly targets small orders.
- Current demand/timing: 15 explicit dated purchase, tender, supplier, or replenishment need within the accepted time window; 10 recent expansion, launch, procurement hiring, or supplier onboarding; 6 current catalogue/recurring replenishment evidence; 0 no usable timing signal.
- Supplier openness/switchability: 10 explicit vendor onboarding, private label, multi-supplier policy, or supplier search; 7 external-brand/multi-brand sourcing or regular assortment change; 4 plausible but unproven openness; 0 exclusive, fully in-house, or structurally closed supply.
- Target-market delivery/compliance fit: 10 all material requirements match; 7 likely fit with minor unknowns; 4 material items still need confirmation; 0 a confirmed non-negotiable conflict.

Do not award points without an evidence URL or an explicit source note. Unknown means zero for that component, not a negative fact.

Default tiers: A = 80–100; B = 65–79; C = 50–64; below 50 = exclude or review depending on the brief. Regardless of total score, default `合格客户` requires an eligible product relationship and evidence URL, direct procurement capability at least 10/25, product/commercial fit at least 10/20, the first three commercial dimensions totaling at least 35/65, the contact gate, and `evidence_confidence` of `high` or `medium`. `adjacent_only` stays in review; a candidate with no usable email or phone is excluded rather than reviewed. Government registration never adds points.

For social signals, award timing points only when the post date is known and the company/target geography is verified. Do not let an explicit supplier-request post override wrong buyer role, wrong product, wrong geography, weak company identity, insufficient direct procurement capability, or a failed contact gate.

## Company role classification

Classify using explicit commercial behavior:

- Importer: explicit importer language or reliable import data.
- Distributor/wholesaler: trade accounts, dealer network, wholesale terms, multiple downstream business customers.
- Brand: own-branded products and brand-led catalogue; manufacturing status separate.
- Retailer/e-commerce: sells to end consumers; evaluate scale separately.
- Hospitality/industrial supplier: supplies hotels, restaurants, institutions, or professional users.
- Manufacturer/competitor: explicit production facilities or manufacturing claims for the same product.
- Unknown/mixed: evidence insufficient or multiple roles.

Do not classify a company as importer merely because it sells imported-looking products.

## Duplicate and entity rules

- Use normalized registrable/official domain as the primary duplicate key.
- Remove scheme, `www`, query, fragment, and language paths.
- Keep parent, subsidiary, brand, and store relationships when commercially meaningful.
- Do not merge separate companies merely because their names are similar.
- Prefer the official legal/display name from the company site; keep translations auxiliary.

## Review outcomes

- `合格客户`: meets all hard requirements, has purchase-likelihood evidence, and has at least one sourced published email or phone.
- `待人工复核`: has a usable email or phone and is promising, but has unresolved company, buyer-role, geography, product-pathway, scale, or commercial-fit questions.
- `排除记录`: fails a hard rule or scores below the accepted threshold.
