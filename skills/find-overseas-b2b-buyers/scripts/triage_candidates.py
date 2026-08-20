#!/usr/bin/env python3
"""Fast, deterministic triage for lightweight overseas B2B candidate pools."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.parse import urlsplit

HARD_EXCLUSIONS = {
    "exclusive_supplier", "relevant_factory_owner", "white_label_manufacturer",
    "consumer_only_small_retailer", "marketplace_only", "no_official_identity",
    "no_product_signal",
}


def normalize_domain(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    candidate = value if "://" in value else "https://" + value
    host = (urlsplit(candidate).hostname or "").lower().rstrip(".")
    return host[4:] if host.startswith("www.") else host


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_known_domains(path: Path | None) -> set[str]:
    if not path:
        return set()
    data = load_json(path)
    items = data if isinstance(data, list) else data.get("domains", data.get("leads", []))
    result = set()
    for item in items:
        value = item if isinstance(item, str) else item.get("normalized_domain") or item.get("website", "")
        domain = normalize_domain(str(value))
        if domain:
            result.add(domain)
    return result


def quick_score(record: dict) -> int:
    product_hits = min(max(int(record.get("product_hits", 0)), 0), 5)
    role_hits = min(max(int(record.get("buyer_role_hits", 0)), 0), 3)
    intent_signals = min(len(record.get("intent_signals") or record.get("positive_signals") or []), 5)
    official = 10 if record.get("official_site_verified") else 0
    soft_penalty = 8 * len(record.get("soft_risks") or [])
    relationship = record.get("product_relationship")
    relationship_penalty = 15 if relationship == "adjacent_only" else 0
    return max(0, min(100, product_hits * 5 + role_hits * 8 + intent_signals * 7 + official - soft_penalty - relationship_penalty))


def process(records: list[dict], known_domains: set[str], target_count: int) -> dict:
    started = time.perf_counter()
    seen = set()
    ranked, excluded, duplicates = [], [], []
    for source in records:
        record = dict(source)
        domain = normalize_domain(str(record.get("website", "")))
        record["normalized_domain"] = domain
        if domain and (domain in known_domains or domain in seen):
            record["triage_disposition"] = "duplicate_or_cached"
            duplicates.append(record)
            continue
        if domain:
            seen.add(domain)
        flags = set(record.get("exclusion_signals") or [])
        hard = sorted(flags & HARD_EXCLUSIONS)
        if not domain:
            hard.append("no_official_identity")
        if hard:
            record["triage_disposition"] = "excluded"
            record["hard_exclusion_reasons"] = sorted(set(hard))
            excluded.append(record)
            continue
        record["quick_score"] = quick_score(record)
        record["triage_disposition"] = "hold"
        ranked.append(record)
    ranked.sort(key=lambda item: (-item["quick_score"], item.get("company_name", "")))
    deep_limit = max(target_count, target_count * 2)
    for index, record in enumerate(ranked):
        if index < deep_limit and record["quick_score"] >= 45:
            record["triage_disposition"] = "deep_verify"
    elapsed = round(time.perf_counter() - started, 6)
    return {
        "ranked_candidates": ranked, "excluded": excluded, "duplicates": duplicates,
        "metrics": {
            "input_count": len(records), "ranked_count": len(ranked),
            "deep_verify_count": sum(x["triage_disposition"] == "deep_verify" for x in ranked),
            "hold_count": sum(x["triage_disposition"] == "hold" for x in ranked),
            "excluded_count": len(excluded), "duplicate_or_cached_count": len(duplicates),
            "triage_seconds": elapsed,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Candidate JSON list or object with candidates")
    parser.add_argument("--known-domains", type=Path, help="Optional JSON cache of prior domains")
    parser.add_argument("--target-count", type=int, default=5, help="Requested qualified count; deep verification is capped near 2x")
    parser.add_argument("--output", type=Path, required=True, help="Output JSON path")
    args = parser.parse_args()
    data = load_json(args.input)
    records = data if isinstance(data, list) else data.get("candidates", [])
    result = process(records, load_known_domains(args.known_domains), max(1, args.target_count))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result["metrics"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
