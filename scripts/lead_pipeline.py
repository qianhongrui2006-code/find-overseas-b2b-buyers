#!/usr/bin/env python3
"""Normalize, deduplicate, score, and validate overseas B2B lead records."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

WEIGHTS = {
    "direct_procurement_capability": 25,
    "product_commercial_fit": 20,
    "purchasing_scale_moq_fit": 20,
    "current_demand_timing": 15,
    "supplier_openness": 10,
    "market_delivery_compliance_fit": 10,
}

REQUIRED = [
    "company_name", "website", "country", "company_type", "match_reason",
    "evidence_url", "discovery_source", "retrieved_at",
]

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
QUALIFIED_PRODUCT_RELATIONSHIPS = {
    "exact_target", "direct_use", "adjacent_with_transaction_bridge",
}


def normalize_domain(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    candidate = value if "://" in value else "https://" + value
    host = (urlsplit(candidate).hostname or "").lower().rstrip(".")
    return host[4:] if host.startswith("www.") else host


def clamp_score(value: object, maximum: int) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return 0.0
    return max(0.0, min(number, float(maximum)))


def calculate_score(record: dict) -> int:
    components = record.get("score_components") or {}
    return round(sum(clamp_score(components.get(key, 0), maximum) for key, maximum in WEIGHTS.items()))


def tier(score: int) -> str:
    if score >= 80:
        return "A"
    if score >= 65:
        return "B"
    if score >= 50:
        return "C"
    return "排除"


def has_usable_email_or_phone(record: dict) -> bool:
    blocked_statuses = {"inferred_unverified", "推断-未验证", "none"}
    source = str(record.get("contact_source_url", "")).strip()
    for channel in ("email", "phone"):
        value = str(record.get(channel, "")).strip()
        status = str(record.get(f"{channel}_status", "")).strip()
        if value and source and status not in blocked_statuses:
            return True
    for contact in record.get("contacts") or []:
        if (
            contact.get("channel") in {"email", "phone"}
            and str(contact.get("value", "")).strip()
            and str(contact.get("source_url", "")).strip()
            and contact.get("status") not in blocked_statuses
        ):
            return True
    return False


def validate(record: dict) -> list[str]:
    issues = [f"missing:{key}" for key in REQUIRED if not str(record.get(key, "")).strip()]
    score = record.get("total_score")
    if not isinstance(score, int) or not 0 <= score <= 100:
        issues.append("invalid:total_score")
    email = str(record.get("email", "")).strip()
    if email and not EMAIL_RE.match(email):
        issues.append("invalid:email")
    contacts = [record.get("email"), record.get("phone"), record.get("whatsapp")]
    if any(str(v or "").strip() for v in contacts) and not str(record.get("contact_source_url", "")).strip():
        issues.append("missing:contact_source_url")
    if str(record.get("whatsapp", "")).strip() and not str(record.get("whatsapp_status", "")).strip():
        issues.append("missing:whatsapp_status")
    if record.get("qualification_status") == "qualified":
        if not has_usable_email_or_phone(record):
            issues.append("missing:usable_email_or_phone")
        relationship = str(record.get("product_relationship", "")).strip()
        if relationship not in QUALIFIED_PRODUCT_RELATIONSHIPS:
            issues.append("invalid:qualified_product_relationship")
        if not str(record.get("target_product_purchase_pathway", "")).strip():
            issues.append("missing:target_product_purchase_pathway")
        if not str(record.get("target_product_evidence_url", "")).strip():
            issues.append("missing:target_product_evidence_url")
        components = record.get("score_components") or {}
        procurement = clamp_score(components.get("direct_procurement_capability", 0), 25)
        product_fit = clamp_score(components.get("product_commercial_fit", 0), 20)
        scale_fit = clamp_score(components.get("purchasing_scale_moq_fit", 0), 20)
        if procurement < 10:
            issues.append("below_gate:direct_procurement_capability")
        if product_fit < 10:
            issues.append("below_gate:product_commercial_fit")
        if procurement + product_fit + scale_fit < 35:
            issues.append("below_gate:commercial_core")
    return issues


def load_records(path: Path) -> list[dict]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        return data if isinstance(data, list) else data.get("leads", data.get("qualified", []))
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def process(records: list[dict]) -> tuple[list[dict], list[dict]]:
    seen: dict[str, int] = {}
    output: list[dict] = []
    duplicates: list[dict] = []
    for index, source in enumerate(records, start=1):
        record = dict(source)
        domain = normalize_domain(str(record.get("website", "")))
        record["normalized_domain"] = domain
        if not has_usable_email_or_phone(record):
            record["qualification_status"] = "excluded"
            reasons = list(record.get("exclusion_reasons") or [])
            if "no_usable_email_or_phone" not in reasons:
                reasons.append("no_usable_email_or_phone")
            record["exclusion_reasons"] = reasons
            record["total_score"] = 0
            record["unscored_reason"] = "failed_contact_gate"
            record["priority"] = "排除"
        else:
            record["total_score"] = calculate_score(record)
            record["priority"] = tier(record["total_score"])
        record["validation_issues"] = validate(record)
        if domain and domain in seen:
            record["duplicate_of_row"] = seen[domain]
            duplicates.append(record)
            continue
        if domain:
            seen[domain] = index
        output.append(record)
    return output, duplicates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON or CSV lead file")
    parser.add_argument("--output", type=Path, required=True, help="Processed JSON output")
    args = parser.parse_args()
    records = load_records(args.input)
    processed, duplicates = process(records)
    payload = {"leads": processed, "duplicates": duplicates, "weights": WEIGHTS}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    issue_count = sum(bool(item["validation_issues"]) for item in processed)
    print(json.dumps({"input": len(records), "kept": len(processed), "duplicates": len(duplicates), "records_with_issues": issue_count}, ensure_ascii=False))
    return 2 if issue_count else 0


if __name__ == "__main__":
    sys.exit(main())
