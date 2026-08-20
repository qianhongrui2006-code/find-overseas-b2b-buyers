# Investment-worthiness and safe verification

## Purpose

Decide whether a candidate deserves sales time. Do not confuse legal existence with commercial value. Government registration data can confirm identity or operating status, but it does not prove product demand, procurement authority, scale fit, supplier openness, or current buying intent.

## Default verification path

Use this order for normal research:

1. Official company website and current product catalogue: verify offering, buyer role, target-product purchase pathway, locations, and public business contacts.
2. Maps or an authoritative local business profile: corroborate physical presence, operating status, website, address, and phone.
3. Official company social posts, news, and recruitment: identify dated launches, expansion, procurement hiring, new locations, supplier onboarding, or other timing signals.
4. Official trade-show exhibitor and industry-association pages: corroborate industry participation and current activity; never treat membership or attendance as purchase intent by itself.
5. Licensed or user-authorized trade/import data: corroborate import behavior, frequency, scale, and entity matching while recording classification uncertainty.
6. Government registry: use only for targeted identity or status checks when a high-value candidate is ambiguous, conflicting, or requires legal-name confirmation.

Do not enumerate a government registry to create the candidate pool by default. Do not give score points merely because a company is registered.

## Government-source safety

- Prefer official APIs, downloadable open datasets, or manual lookup over HTML scraping.
- Check site terms, `robots.txt`, API documentation, and rate limits before automated access.
- Use low concurrency, cache prior results, stop on `429`, authentication, CAPTCHA, paywall, or access-denied responses, and never bypass controls.
- Do not create or use an account/API key without the user's authorization. Report any unavailable check as `not_available` or `blocked`, not as a negative company fact.
- Collect only fields needed for business verification. Prefer corporate and role-based contact data; minimize unrelated personal data.

## Evidence confidence

Assign evidence confidence separately from the 100-point commercial score:

| Level | Minimum interpretation | Default action |
|---|---|---|
| `high` | Official identity and geography; official target-product or purchase-pathway evidence; sourced email/phone; no unresolved material conflict | `contact_now` |
| `medium` | Identity and contact are supported; commercial fit is corroborated by an official source plus at least one independent source; some non-blocking unknowns remain | `low_cost_test` or `manual_review` |
| `low` | Depends mainly on snippets, aggregators, inference, stale evidence, or unresolved identity/product/contact conflict | never put in the qualified list |

Source strength is claim-specific. A registry is strong for legal identity but weak for buying likelihood. A current official product page is strong for assortment but does not prove a dated purchase request. A trade-show list is strong for participation but not buyer role.

## Field-level provenance and contradiction check

Retain a source URL and retrieval date for company identity, geography, buyer role, product relationship, target-product pathway, each contact value, and each dated timing signal. Before qualification, actively test contrary explanations:

- manufacturer or competitor rather than buyer;
- adjacent product only;
- inactive or wrong-country entity;
- consumer-scale outlet below factory MOQ;
- third-party contact presented as company contact;
- expired tender or stale social signal;
- conflicting address, phone, domain, or legal name.

Record unresolved conflicts and lower confidence instead of silently selecting the preferred source.

## Sales-investment action

Use these actions independently of score:

- `contact_now`: qualified, high confidence, and a clear reason for timely outreach.
- `low_cost_test`: qualified or promising with medium confidence; send one tailored message or make one call only after the user separately authorizes outreach.
- `manual_review`: commercially attractive but a material identity, pathway, geography, scale, or evidence issue remains.
- `do_not_invest`: failed a hard gate, low confidence, or confirmed mismatch.

When the user supplies outreach outcomes, retain only business-relevant feedback such as bounce, valid phone, response, confirmed category buying, backup-supplier openness, MOQ mismatch, or refusal reason. Use aggregate outcomes to refine later briefs. Never send outreach automatically without separate authorization.
