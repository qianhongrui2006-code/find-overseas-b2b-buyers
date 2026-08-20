# Commercial data platforms and logistics records

Use public company platforms, permitted directories, and authorized trade-data exports to accelerate discovery and corroborate business activity. Treat platform claims as claim-specific evidence, not as universal proof of buyer quality.

## Source types and roles

| Source type | Useful fields | Default evidence role | Key risk |
|---|---|---|---|
| B2B company directory | company name, category, country, website, phone/email | candidate discovery and contact corroboration | stale, self-reported, duplicate, or supplier-side listing |
| Buyer-request/RFQ platform | requested product, date/deadline, buyer geography, platform URL | explicit intent only when the request is current, target-matched, and attributable to a company | buyer identity/contact may be hidden until an authorized response |
| Customs/shipment platform | consignee/importer, shipper, product description/HS code, shipment date/frequency | historical purchase/import and scale signal | entity resolution errors, vague HS/product text, old activity, intermediaries |
| Freight-forwarder/association directory | logistics company, address, phone/email, territory | identity/contact verification or logistics prospect discovery | a forwarder is usually not the product buyer |
| User-exported CSV/XLSX | platform-dependent structured records | batch discovery, dedupe, and triage | export license, missing provenance, stale snapshots |

## Role resolution gate

For every shipment or logistics record, store `record_role` as one of `buyer_importer`, `consignee`, `shipper_supplier`, `notify_party`, `freight_forwarder`, `customs_broker`, `nvocc_carrier`, or `unknown`.

- Qualify `buyer_importer` or a commercially matched `consignee` only after resolving it to the official operating company/domain and verifying the target-product pathway.
- Treat `notify_party`, “care of” addresses, freight forwarders, customs brokers, NVOCCs, and carriers as intermediary clues by default. Do not copy their email or phone into the buyer record.
- If the same forwarder appears across shipments, use it only to discover likely shipper/consignee names or a trade lane. Do not infer that it can disclose its customers or has permission to do so.
- Record entity-match confidence (`high`, `medium`, `low`) and conflicts in names, addresses, subsidiaries, or domains.

## Minimum fields to collect

During light discovery collect only: platform, source URL or authorized dataset reference, company name, country, record role, product description or confirmed HS code, latest relevant date, activity-frequency summary when visible, and official-domain candidate.

After triage, enrich only survivors with official product-pathway evidence, one sourced email or phone, verified geography, concise purchase rationale, and any explicit-intent evidence. Do not copy full shipment histories into the owner workbook.

## Evidence interpretation

- A current RFQ that names the target product, supplier need, quantity/specification, and deadline may support `explicit_purchase_intent` after company and geography checks.
- Shipment records show historical commercial activity, not a public statement that the company is currently seeking a new supplier.
- Repeated recent shipments can support scale/timing and procurement-capability components, but only when entity and product matches are credible.
- Directory membership supports identity/category only. It does not prove current buying, scale, or supplier openness.
- Search snippets and copied aggregator profiles are discovery clues. Open the source record or corroborate on an official site before qualification.

## Access and compliance

Use public pages within published terms and normal rate limits. For login-only, paid, CAPTCHA-protected, export-controlled, or API-limited data, do not bypass controls. Ask the user to provide an authorized CSV/XLSX export, API access, or a permitted signed-in workflow. Preserve the platform/source URL, export date, and license/access limitation in the internal audit data.
