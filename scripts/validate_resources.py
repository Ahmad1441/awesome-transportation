#!/usr/bin/env python3
"""Validate the structured transportation resource catalog."""

from __future__ import annotations

import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "resources.yml"

REQUIRED_FIELDS = {
    "name",
    "url",
    "description",
    "category",
    "subcategory",
    "resource_type",
    "transport_mode",
    "organization",
    "geography",
    "free",
    "open_source",
    "tags",
    "last_checked",
}

CATEGORIES = {
    "simulation-and-modelling",
    "planning-operations-and-spatial-analysis",
    "public-transport-and-shared-mobility",
    "railways",
    "robotics-and-autonomous-transportation",
    "transportation-data-and-safety",
    "standards-and-connected-transportation",
    "learning-research-and-community",
}

RESOURCE_TYPES = {
    "software",
    "dataset",
    "api",
    "tutorial",
    "course",
    "book",
    "documentation",
    "repository",
    "standard",
    "research-group",
    "conference",
    "journal",
    "visualization-tool",
}

TRANSPORT_MODES = {
    "road",
    "rail",
    "transit",
    "cycling",
    "walking",
    "freight",
    "aviation",
    "maritime",
    "multimodal",
}

KEBAB_CASE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def normalized_url(value: str) -> str:
    parsed = urlsplit(value)
    path = parsed.path.rstrip("/") or "/"
    return f"{parsed.scheme.lower()}://{parsed.netloc.lower()}{path}"


def main() -> int:
    errors: list[str] = []
    try:
        document = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        print(f"Catalog could not be loaded: {error}", file=sys.stderr)
        return 1

    if not isinstance(document, dict) or document.get("schema_version") != 1:
        errors.append("Top-level schema_version must be 1.")
    resources = document.get("resources") if isinstance(document, dict) else None
    if not isinstance(resources, list):
        errors.append("Top-level resources must be a list.")
        resources = []

    names: list[str] = []
    urls: list[str] = []
    for index, resource in enumerate(resources, start=1):
        label = f"resource {index}"
        if not isinstance(resource, dict):
            errors.append(f"{label}: entry must be a mapping.")
            continue
        if resource.get("name"):
            label = repr(resource["name"])
        missing = sorted(REQUIRED_FIELDS - resource.keys())
        if missing:
            errors.append(f"{label}: missing required fields: {', '.join(missing)}.")
            continue

        for field in ("name", "url", "description", "category", "subcategory", "resource_type", "transport_mode", "organization", "geography"):
            if not isinstance(resource[field], str) or not resource[field].strip():
                errors.append(f"{label}: {field} must be a non-empty string.")

        url = resource["url"]
        if isinstance(url, str):
            parsed = urlsplit(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{label}: URL must be an absolute HTTP(S) URL.")
            else:
                urls.append(normalized_url(url))

        if resource["category"] not in CATEGORIES:
            errors.append(f"{label}: unknown category {resource['category']!r}.")
        if resource["resource_type"] not in RESOURCE_TYPES:
            errors.append(f"{label}: unknown resource_type {resource['resource_type']!r}.")
        if resource["transport_mode"] not in TRANSPORT_MODES:
            errors.append(f"{label}: unknown transport_mode {resource['transport_mode']!r}.")
        if not KEBAB_CASE.fullmatch(str(resource["subcategory"])):
            errors.append(f"{label}: subcategory must be kebab-case.")
        if not isinstance(resource["free"], bool) or not isinstance(resource["open_source"], bool):
            errors.append(f"{label}: free and open_source must be booleans.")
        if not isinstance(resource["tags"], list) or not resource["tags"]:
            errors.append(f"{label}: tags must be a non-empty list.")
        elif any(not isinstance(tag, str) or not KEBAB_CASE.fullmatch(tag) for tag in resource["tags"]):
            errors.append(f"{label}: every tag must be a kebab-case string.")

        description = resource["description"]
        if isinstance(description, str) and (not description[:1].isupper() or not description.endswith(".")):
            errors.append(f"{label}: description must start uppercase and end with a period.")
        checked = resource["last_checked"]
        if not isinstance(checked, (date, str)):
            errors.append(f"{label}: last_checked must be a YYYY-MM-DD date.")
        names.append(str(resource["name"]).casefold())

    for value, count in Counter(names).items():
        if count > 1:
            errors.append(f"Duplicate resource name: {value!r} ({count} entries).")
    for value, count in Counter(urls).items():
        if count > 1:
            errors.append(f"Duplicate resource URL: {value!r} ({count} entries).")

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(resources)} resources in {CATALOG.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
