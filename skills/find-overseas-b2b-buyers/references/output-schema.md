# Output Schema

Use the workbook template in `assets/海外B2B客户名单模板.xlsx` or reproduce its six-sheet structure.

## 合格客户 and 待人工复核

Required column order:

`公司官方名称`, `公司中文参考名`, `官方网站`, `业务邮箱`, `电话`, `WhatsApp`, `联系方式来源URL`, `联系人姓名`, `职位`, `邮箱状态`, `电话状态`, `证据可信度`, `身份验证状态`, `商业价值证据`, `证据冲突或缺口`, `建议投入动作`, `政府注册复核状态`, `验证地址`, `地图/本地商业资料URL`, `明确采购意愿`, `明确意向证据URL`, `明确意向日期`, `渠道覆盖摘要`, `产品关系`, `目标产品采购链路`, `目标产品证据URL`, `购买意向等级`, `购买意向依据`, `意向证据日期`, `意向证据URL`, `推荐开发理由`, `Lead ID`, `优先级`, `总分`, `直接采购能力分`, `产品与商业适配分`, `采购规模与MOQ适配分`, `近期需求与时机分`, `供应商开放度分`, `目标市场交付与合规适配分`, `国家`, `城市`, `公司类型`, `匹配产品或品牌`, `规范域名`, `联系表单`, `LinkedIn公司页`, `其他社媒`, `发现渠道`, `使用搜索式`, `抓取时间`, `复核状态`, `备注`.

Keep the company and actionable contact block at the front even when an adapter adds extra research columns. Immediately after the contact block include `证据可信度`, `身份验证状态`, `商业价值证据`, `证据冲突或缺口`, `建议投入动作`, and `政府注册复核状态`. Government registration is optional and must not be presented as a commercial-value score.

Then include `验证地址`, `地图/本地商业资料URL`, `明确采购意愿`, `明确意向证据URL`, `明确意向日期`, and `渠道覆盖摘要`. Use `明确采购意愿` values `明确`, `未发现`, or `不确定`. `明确` requires a dated source that directly requests the target product, supplier, quotation, tender response, or procurement partner; ordinary catalogue, hiring, exhibitor, association, expansion, or import evidence does not qualify.

Add `待复核问题` to the review sheet.

## 排除记录

`公司名称`, `官方网站`, `规范域名`, `发现URL`, `排除原因`, `触发规则`, `证据URL`, `抓取时间`.

## 搜索策略

`国家`, `语言`, `产品词`, `身份词`, `意图词`, `排除词`, `完整搜索式`, `渠道`, `已检查结果数`, `候选数`, `合格数`, `命中率`, `备注`.

Calculate 命中率 from qualified/reviewed counts; do not hardcode calculated values.

## 任务说明

Record original request, confirmed ICP, hard rules, positive signals, exclusions, contact priority, source plan, score thresholds, execution dates, requested and delivered counts, coverage, blockers, and compliance notes.

## 渠道验证

Use one row per company and source URL:

`公司官方名称`, `官方网站`, `渠道`, `检查状态`, `精要结果`, `来源URL`, `信息日期`, `抓取日期`, `明确采购意愿`, `采购意愿对象或内容`, `备注`.

Allowed channels: `官网/产品目录`, `地图/本地商业资料`, `官方社媒`, `官方新闻`, `招聘`, `展会`, `行业协会`, `合规贸易数据`, `政府注册复核`, `其他权威来源`.

Allowed check statuses: `已获取`, `已检查未发现`, `受阻`, `不可用`, `未检查`. For Maps/local profiles, save the verified address in `精要结果` and the map/profile page in `来源URL`. For social/news/recruitment/trade-show/association/trade-data results, keep only the relevant URL and one concise useful finding. Create an explicit no-result/blocked row when a planned channel produced no usable evidence; never imply it was checked by leaving it blank.

## Workbook behavior

- Freeze headers and enable filters.
- Use dropdown validation for priority, company type, match level, contact status, review status, and channel when feasible.
- Use real date/datetime and numeric cells.
- Use plain-text full source URLs.
- Apply conditional formatting to priority and score.
- Keep descriptive columns wrapped and readable.
- Do not hide excluded or unresolved records in the qualified sheet.

## Quality checks

- No duplicate normalized domains in `合格客户` unless an explained subsidiary/brand relationship exists.
- Every qualified row has company name, official site/domain, country, company type, purchase rationale, dated/source-labeled intent evidence where available, discovery source, retrieval date, and review status.
- Every qualified row has an eligible product relationship, an explained target-product purchase pathway, and a source URL supporting that pathway. Adjacent-only opportunities remain in review or a separately labeled expansion lane.
- Every qualified row has `证据可信度` of high or medium, a claim-specific evidence trail, no unresolved blocking conflict, and a recommended investment action. Low-confidence records never enter the qualified sheet regardless of commercial score.
- Every qualified/review row has channel-check records for the sources planned in the confirmed brief. Each record states whether evidence was found, nothing was found, access was blocked, the source was unavailable, or it was not checked.
- Every `明确` purchase-intent label has a dated evidence URL and a concise description of the requested product/supplier action. If no such statement was found, use `未发现`; do not upgrade indirect commercial signals to explicit intent.
- Every retained qualified/review row has at least one sourced published or verified email or phone. Records with neither are excluded; contact-form-only records do not remain in the lead sheets.
- Every non-empty contact has a status and source URL.
- Scores are 0–100 and consistent with tier thresholds.
- Formula cells contain no spreadsheet errors.
- Report actual shortfalls rather than padding the list.
