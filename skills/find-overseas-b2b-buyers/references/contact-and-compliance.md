# Contact Data and Compliance

## Contact discovery order

1. Official Contact, About, Team, Legal, Locations, or department pages; extract email and phone first.
2. Official page footer, `mailto:`, `tel:`, structured data, and WhatsApp link.
3. Official company LinkedIn and social profiles.
4. Official Places/Maps fields or reputable directories with attribution.
5. User-authorized licensed contact database.
6. Inferred corporate email pattern, stored separately.

Prioritize procurement, sourcing, category, owner/founder for smaller companies, and relevant commercial departments. An official generic `info@` address or switchboard is acceptable when no stronger contact exists. Record contact forms separately; they are fallback channels and do not satisfy the default main-list contact gate.

## Status vocabulary

- `公开-官网`
- `公开-官方社媒`
- `公开-目录或API`
- `验证-第三方服务`
- `推断-未验证`
- `无`

Store source URL and retrieval date beside every contact. If a page has several numbers, retain labels such as headquarters, sales, mobile, or support.

## WhatsApp

Confirm WhatsApp only when an official source:

- labels the number “WhatsApp”;
- provides a WhatsApp button/link;
- uses `wa.me` or an equivalent official WhatsApp URL.

A mobile-format phone number alone is not proof.

## Data minimization

- Collect only data relevant to B2B evaluation and contact.
- Prefer company and role-based contact channels.
- Do not collect sensitive traits, private accounts, family data, or unrelated personal details.
- Maintain a suppression/do-not-contact list when supplied by the user.
- Do not scrape behind login, bypass access controls, or solve CAPTCHAs.
- Do not treat public visibility as automatic permission for marketing.

Before outreach, advise the user to assess applicable marketing/privacy law, lawful basis, notice and opt-out requirements, retention, and vendor terms for the recipient country. This skill performs research and does not provide legal advice.

## Source-specific constraints

- Prefer official APIs where available.
- Follow provider attribution and storage restrictions.
- Do not make direct Google result-page scraping the default implementation.
- Search and API availability can change; verify current official documentation when implementing integrations.
- Stop rather than circumvent a block.
