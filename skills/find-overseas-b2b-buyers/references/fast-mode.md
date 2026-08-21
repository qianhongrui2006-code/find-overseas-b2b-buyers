# Fast calibration mode

Use this mode for a first sample, a repeated country/industry test, or a user-requested speed run.

## Funnel and stop rules

| Stage | Input | Action | Stop condition |
|---|---|---|---|
| Brief reuse | confirmed supplier profile | reuse product, buyer, exclusion, MOQ, and country rules | do not re-read unchanged supplier pages |
| Parallel light discovery | country × buyer type × language task matrix | run independent cells concurrently when supported; capture only lightweight candidate fields | deduplicated pool reaches about 3× target or results become mostly duplicates |
| Deterministic triage | candidate JSON/CSV + prior domains | normalize after every batch, deduplicate, hard-exclude, quick-rank | retain only the best candidates needed to reach the target with a small buffer |
| Core verification | ranked survivors | check product/purchase pathway, buyer identity, geography, and minimum contact | qualification is decided or two primary official pages plus one decisive fallback were checked |
| Minimum contact | surviving candidates | collect one sourced published or verified email or phone | either channel found, or allowed contact sources exhausted and candidate excluded |
| On-demand enrichment | finalists or unresolved high-value candidates | check social/news/recruitment/trade/contact-provider sources only when triggered | the specific intent, entity, scale, or outreach question is answered |
| Late delivery | completed verified set | generate the workbook once from structured records and run compact QA | formulas, duplicates, evidence, and layout pass |

Do not enrich all candidates. Use `DISCOVER_LIGHT → TRIAGE → VERIFY_CORE → CONTACT_MINIMUM → ENRICH_ON_DEMAND → DELIVER_ONCE`. Use websites, industry directories, and Maps/local profiles as the primary lanes. Collect social/news/recruitment links, named contacts, a second contact channel, and detailed trade history only for finalists when they can change the decision or outreach route.

## Parallel search-task matrix

Create one lightweight task per confirmed `country × priority buyer type × search language`. Add source-lane variants only for website/search, industry directory/association, and Maps/local profiles. Assign a small result quota to each cell and merge results by normalized domain after every batch.

Run independent cells concurrently only when the host supports parallel requests within provider limits. Otherwise process one small batch from each cell in round-robin order. Never broaden beyond the confirmed countries merely to keep workers busy.

## Lightweight checkpoints

During discovery and triage, persist JSON or CSV rather than XLSX. Keep only:

`company_name`, `candidate_url`, `official_domain`, `country`, `buyer_type_clue`, `source_role`, `product_clue`, `activity_date`, `contact_clue`, `discovery_query`, and `disposition`.

Write verified survivor records and channel evidence separately. Do not append to or restyle a workbook after each company. Generate one final workbook only after the requested target is reached or the shortfall is finalized.

## Hard exclusions at triage

- prior qualified/excluded normalized domain unless a recheck is due;
- explicit exclusive supplier relationship;
- clear ownership of a relevant manufacturing line or white-label manufacturing business;
- consumer-only small retailer or marketplace-only seller;
- no official domain or authoritative identity source;
- no target/adjacent product signal.

An adjacent-product signal may survive triage for discovery, but it cannot pass final qualification without an evidenced transactional bridge to the target deliverable. Mark adjacent-only candidates for review instead of using their contactability to raise them into the main list.

Do not treat a generic word such as `fabricant` as a hard exclusion by itself. Confirm whether it describes the company, a partner factory, or marketing language.

## Page budget

Default fast-mode maximum per surviving domain:

1. Product/category or home page that establishes the purchase pathway.
2. Contact page, or Maps/local profile when it already provides an authoritative phone/site.
3. One About/group/legal page only when buyer identity, geography, or ownership remains decisive.

Open another page or secondary channel only when it can decide buyer-versus-manufacturer identity, exclusive supply, entity matching, or a high-value demand signal. Stop immediately after a decisive hard exclusion or once the minimum evidence and contact gates pass.

## Timing record

Use a monotonic or wall-clock timer and store measured seconds for brief reuse, light discovery, triage, deep verification, contact enrichment, workbook/QA, and total.

Also record candidates discovered, duplicates skipped, triage exclusions, deeply verified domains, qualified/review/excluded counts, and official-contact coverage. Label unmeasured historical comparisons as estimates.

## Output depth

- Default fast sample: concise preview table plus evidence URLs.
- Follow the table with a compact sample-mix summary and 3–6 observed, actionable calibration choices. For each choice state what appeared, why changing it would affect lead quality or outreach, and one reply the user can copy. Prefer dimensions such as buyer type, product/purchase pathway, order-scale fit, geography allocation, contact route/role, and optional intent-research depth.
- Put `方向正确，按当前标准继续` first. Do not require the user to understand internal scoring, and do not show numeric scores unless requested.
- Treat all suggestions as optional. Do not lower hard evidence/contact/product/geography gates or change weights automatically. Material user-requested changes return to the brief confirmation step; accepted sample leads count toward the final target.
- Create the formal workbook once, only after the final verified set is complete or the user explicitly requests an interim workbook.
- Never sacrifice evidence, contact provenance, or buyer/manufacturer checks for speed.
