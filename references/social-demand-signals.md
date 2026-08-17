# Social Demand Signals

Use social platforms to discover time-sensitive buying clues, not as an unrestricted contact-harvesting source.

## Access modes

1. Public/indexed mode: use normal web search and public post/profile URLs. No API is required, but coverage is incomplete and older or login-gated posts may be invisible.
2. Authorized browser mode: use a user-provided logged-in session only for visible, permitted research. Do not bypass login, rate limits, CAPTCHAs, group privacy, or platform controls. Avoid bulk extraction.
3. Official API mode: use user-provided API credentials and an approved app/provider for repeatable or larger-scale monitoring. Follow the current platform scopes, review requirements, quotas, retention, and display rules.
4. Licensed listening provider: use only when authorized by the user; record provider provenance and coverage limits.

## Signal queries

Combine product terms and local-language equivalents with phrases such as:

- `looking for supplier`, `seeking manufacturer`, `need distributor`, `request for quotation`, `RFQ`, `vendor wanted`;
- `new product line`, `opening`, `expanding`, `restock`, `out of stock`, `supplier issue`, `alternative supplier`;
- local-language procurement, wholesale, supplier, tender, restock, and launch phrases.

Use web-indexed forms such as `site:x.com`, `site:twitter.com`, `site:facebook.com`, and public company-page URLs. Do not assume search-engine coverage is complete.

## Qualification

For every social signal, save platform, account/page name, post URL, post date, exact business claim summarized in your own words, company identity link, retrieval date, and confidence.

- Strong: a dated company/employee post explicitly seeks a supplier, quote, product, replenishment, or procurement partner.
- Medium: a recent launch, expansion, new location, stock problem, or supplier change creates plausible near-term demand.
- Weak: generic engagement, hashtags, follows, likes, or product discussion without a business need. Do not use weak signals alone.

Corroborate identity and obtain email/phone from the official company site or another authoritative source. A social post alone does not qualify a lead. Public personal posts without a clear company/business role are out of scope.

## Recency and geography gates

- Default recency: strong when posted within 30 days; usable when within 31–90 days; older than 90 days is background only unless the post states an active future deadline or ongoing supplier program.
- Save the post date separately from the retrieval date. If the post date is unavailable, mark recency `unknown` and do not award timing points.
- Verify target geography from the official website, legal/location page, company profile, or authoritative registry. A hashtag, language, poster location, or post geotag alone is insufficient.
- Accept a company outside the target country only when authoritative evidence shows that it buys for, distributes into, or operates in the target market and the brief permits regional buying offices.

## False-positive checks

Reject or review a supplier-request post when the poster is an individual, recruiter, consultant, sourcing agent with no disclosed buyer, event organizer, competitor seeking raw materials rather than the user's product, seller seeking distributors instead of supply, tiny consumer-only reseller, copied/spam account, or company outside the accepted geography.

Social timing points cannot rescue a weak lead. Require direct procurement capability at least 10, the first three commercial dimensions totaling at least 35, geography compliance, identifiable company evidence, an eligible product relationship, and a sourced published or verified email or phone for the qualified list.

## No-API workflow

Without an API, search public/indexed posts through web search, open accessible post/profile pages, apply the same recency/geography/role gates, verify the company on its official site, and output only verified survivors. State that coverage is partial and not suitable for exhaustive or continuous monitoring.

## Platform caveats

- X/Twitter and Facebook frequently limit anonymous search, historical access, and automation. Expect partial coverage without an API or authorized session.
- LinkedIn is useful for roles and company activity but commonly requires login and restricts automated scraping. Use visible public pages or authorized providers only.
- Never infer that a phone number supports WhatsApp unless an official source explicitly labels or links it.
