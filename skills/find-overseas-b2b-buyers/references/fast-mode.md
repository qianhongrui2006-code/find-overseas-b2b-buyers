# Fast calibration mode

Use this mode for a first sample, a repeated country/industry test, or a user-requested speed run.

## Funnel and stop rules

| Stage | Input | Action | Stop condition |
|---|---|---|---|
| Brief reuse | confirmed supplier profile | reuse product, buyer, exclusion, MOQ, and country rules | do not re-read unchanged supplier pages |
| Light discovery | 2–3 query families | capture name, official URL, snippet/product/role signals only | pool reaches about 3× target or results become mostly duplicates |
| Deterministic triage | candidate JSON + prior domains | normalize, deduplicate, hard-exclude, quick-rank | keep about 2× target for deep verification |
| Deep verification | ranked survivors | check product, buyer identity, factory/group, demand/scale | qualification is decided or four useful official pages were checked |
| Minimum contact | surviving candidates | collect one sourced published or verified email or phone | either channel found, or allowed contact sources exhausted and candidate excluded |
| Delivery | accepted sample | reuse workbook template/builder and run compact QA | formulas, duplicates, evidence, and layout pass |

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

Default maximum per surviving domain:

1. Home or category page.
2. Product/catalogue page.
3. About/group/legal page.
4. Contact page.

Open another page only when it can decide buyer-versus-manufacturer identity, exclusive supply, or a high-value demand signal. Stop immediately after a decisive hard exclusion.

## Timing record

Use a monotonic or wall-clock timer and store measured seconds for brief reuse, light discovery, triage, deep verification, contact enrichment, workbook/QA, and total.

Also record candidates discovered, duplicates skipped, triage exclusions, deeply verified domains, qualified/review/excluded counts, and official-contact coverage. Label unmeasured historical comparisons as estimates.

## Output depth

- Default fast sample: concise preview table plus evidence URLs.
- Create the formal workbook only when requested or after sample approval.
- Never sacrifice evidence, contact provenance, or buyer/manufacturer checks for speed.
