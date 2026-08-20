# Owner-facing output schema

Use `assets/海外B2B客户名单模板.xlsx` or reproduce its four-sheet structure. Optimize the workbook for deciding whom to contact and why. Keep internal scoring, deduplication, and audit details outside this workbook.

## Late workbook generation

Treat XLSX as the final presentation artifact, not the working database. During discovery, triage, and verification, persist lightweight candidate JSON/CSV plus verified-lead and channel-evidence records. Do not open, append to, or restyle the workbook after each company.

Generate the workbook once after the requested qualified set is complete or a documented shortfall is final. Populate all sheets in one pass, apply formatting once, and run one final QA pass. During calibration, show a concise Markdown/text preview unless the user explicitly requests an interim workbook.

## 潜在客户

Required column order:

`公司名称`, `国家/城市`, `官方网站`, `业务邮箱`, `电话`, `WhatsApp`, `联系方式来源URL`, `客户类型`, `匹配产品/采购用途`, `明确采购意愿`, `意向证据URL`, `意向日期`, `验证地址`, `地图URL`, `建议动作`, `推荐理由`, `证据可信度`, `最近核验日期`, `备注`.

Use `明确采购意愿` values `明确`, `未发现`, or `不确定`. `明确` requires a dated source that directly requests the target product, supplier, quotation, tender response, or procurement partner. A catalogue, hiring post, exhibitor/association listing, growth announcement, or import history is not explicit intent.

Use `建议动作` values `立即联系`, `低成本试探`, `待人工复核`, or `暂不投入`. Convert internal score/evidence decisions into this business recommendation; do not reveal the numeric score by default.

## 待人工复核

Use the same columns as `潜在客户`, followed by `待复核问题`. Only retain companies that still pass the email-or-phone gate. State the precise unresolved buyer-role, product-pathway, geography, scale, entity-match, or evidence question.

## 渠道证据

Use one row per company and source URL:

`公司名称`, `渠道`, `检查状态`, `精要结果`, `来源URL`, `信息日期`, `明确采购意愿`, `备注`.

Allowed channels include `官网/产品目录`, `地图/本地商业资料`, `公开商业平台`, `合规贸易数据`, `货代/物流名录`, `官方社媒`, `官方新闻`, `招聘`, `展会`, `行业协会`, `政府注册复核`, and `其他权威来源`.

Allowed statuses are `已获取`, `已检查未发现`, `受阻`, `不可用`, and `未检查`. Save the verified address for Maps/local profiles. For commercial/trade/logistics platforms, summarize the record role and entity/product/date limitation. A forwarder, broker, NVOCC/carrier, or notify party must be labeled as an intermediary rather than a buyer.

## 任务摘要

Use `项目`, `内容`, `状态/说明`, and `来源/更新时间`.

Record the confirmed screening scope and output path, requested/delivered counts, researched and excluded counts, email coverage, phone coverage, explicit-intent count, checked source mix, blocked/unavailable sources, main exclusion reasons, measured stage times, and recommended next iteration.

## Internal-only run data

Retain these outside the owner workbook in schema-valid JSON or internal logs: `lead_id`, normalized domain, score components, total score, A/B/C tier, discovery query, detailed exclusion records, full search strategy, page/cache logs, and raw shipment histories.

`lead_id` is a stable machine identifier used to deduplicate, resume, and join evidence across files. It is not a sales decision field and must not appear in the default workbook.

## Workbook behavior

- Freeze headers and enable filters on lead/evidence sheets.
- Use dropdown validation for categorical fields when feasible.
- Use real date cells and plain-text full URLs.
- Keep descriptive columns wrapped and readable.
- Do not preformat hundreds of empty rows; keep the used range compact.
- Do not hide excluded or unresolved records in `潜在客户`; keep exclusions in internal logs and unresolved survivors in `待人工复核`.

## Quality checks

- No duplicate official domains in `潜在客户` unless an explained subsidiary/brand relationship exists.
- Every retained row has a company name, official/authoritative identity source, target geography, buyer type, target-product pathway, and at least one sourced published or verified email or phone.
- Every non-empty contact has a source URL; inferred-only contacts do not pass the gate.
- Every retained row has `高` or `中` evidence confidence; low-confidence records are excluded or kept out of the owner list.
- Every `明确` intent label has a dated evidence URL and concise requested action/product.
- Planned channel checks are disclosed as obtained, no result, blocked, unavailable, or not checked.
- Formula cells contain no spreadsheet errors.
- Report actual shortfalls rather than padding the list.
