# Search Playbook

## Model buyer signals, not declarations of intent

Most prospects do not publish “we want to buy X.” Discover companies through durable commercial signals:

- already sell or distribute the target product;
- sell adjacent products to the same downstream buyers;
- operate a private-label or own-brand range without clear manufacturing evidence;
- serve a channel that consumes the product, such as hospitality or corporate gifts;
- stock competing brands or products;
- appear in relevant association/member/exhibitor lists;
- show time-sensitive expansion, launches, hiring, new locations, or supplier onboarding.

Label these as market fit, product fit, or timing/intent signals. Do not merge them.

Adjacent-category queries are discovery tools, not qualification evidence. After discovery, verify whether the company actually obtains the target deliverable through an explicit commercial mechanism. If no such transactional bridge is supported, label the company `adjacent_only` and keep it out of the default qualified list.

## Build five term groups

1. Product: formal name, common name, category, material, use case, parent/subcategory.
2. Buyer identity: importer, distributor, wholesaler, dealer, brand, retailer, stockist, buying office, hospitality supplier, local-language equivalents.
3. Business/demand signal: wholesale, trade account, brands, catalogue, private label, supplier, vendor, new collection, locations.
4. Geography: country, priority city, industrial cluster, ccTLD, country calling code.
5. Exclusions: jobs, careers, marketplaces, consumer articles, irrelevant meanings, competitors when requested.

Generate both English and local-language variants. A country-code domain is a discovery filter, not proof of location.

## Query families

Use short, auditable query families and record each executed query:

```text
"{product}" (importer OR distributor OR wholesaler) "{country}" -jobs -careers
site:{ccTLD} "{local product}" ("{local importer}" OR "{local wholesaler}")
intitle:distributor "{product}" "{country}"
inurl:brands "{product}" "{country}"
"{product}" ("trade account" OR "wholesale only" OR catalogue)
"{adjacent category}" distributor "{country}"
"{competitor brand}" (stockist OR dealer OR distributor) "{country}"
filetype:pdf ("exhibitor list" OR "member directory") "{industry}" "{year}"
site:linkedin.com/company "{industry}" "{country}"
site:linkedin.com/in (buyer OR procurement OR sourcing OR owner) "{company}"
site:x.com ("looking for supplier" OR "seeking manufacturer" OR RFQ) "{product}" "{country}"
site:twitter.com ("need supplier" OR restock OR "alternative supplier") "{product}" "{country}"
site:facebook.com ("looking for supplier" OR "seeking distributor" OR RFQ) "{product}" "{country}"
related:{known-good-domain}
```

Use social queries only as an optional intent-signal lane. Read [social-demand-signals.md](social-demand-signals.md) before using login sessions, APIs, or social posts as evidence.

Test a few results before generating many variants. Search engines may reinterpret parentheses, wildcards, and operators; measure result quality rather than assuming strict Boolean execution.

## Source roles

| Source | Best use | Never assume |
|---|---|---|
| Search result | Discover official sites and documents | snippet is current or company is qualified |
| Company site | Verify offering, role, location, contacts | marketing claim is independently proven |
| Maps/Places | Verify physical presence, phone, site, operational signals | rating equals buying intent |
| Directory/association | Discover members and classifications | every listing is current or a buyer |
| Exhibitor list | Discover relevant companies | every exhibitor is an importer; many are suppliers |
| Competitor stockists | Identify proven category sellers | stockist is independent or open to alternatives |
| LinkedIn/social | Enrich roles and activity | employment/contact is current without corroboration |
| Trade data | Verify import behavior | product classification and entity match are error-free |
| Commercial company platform | Discover companies, categories, public contacts, or authorized RFQs | a listing is current, independent, or commercially qualified |
| Freight/logistics directory | Verify a logistics company or discover trade-lane intermediaries | the forwarder, broker, NVOCC, carrier, or notify party buys the user's product |
| Government registry | Targeted legal-name, status, or address verification for shortlisted ambiguous candidates | registration proves buying likelihood or deserves score points |

Read [commercial-data-platforms.md](commercial-data-platforms.md) before using aggregators, shipment records, or freight/logistics collections. Resolve each source role and official domain before qualification.

Do not crawl or enumerate government registries to build the default candidate pool. Prefer an official API/open dataset or a small manual lookup, obey published access limits, and stop at authentication, CAPTCHA, paywall, `429`, or access denial. Continue without the registry when website, maps, association, trade-show, and commercial evidence already establish a sufficient identity.

## Calibration

For each query record candidates reviewed, qualified candidates, noise types, and useful terms found on real company sites. Revise terms when target-company precision is poor. Prefer several narrow query families to a single brittle query.
