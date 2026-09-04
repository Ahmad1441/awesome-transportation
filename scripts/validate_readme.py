#!/usr/bin/env python3
"""Check the hand-maintained README catalog against structured metadata."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CATALOG = ROOT / "data" / "resources.yml"
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"

CATEGORY_BY_TITLE = {
    "Simulation and Modelling": "simulation-and-modelling",
    "Planning, Operations and Spatial Analysis": "planning-operations-and-spatial-analysis",
    "Public Transport and Shared Mobility": "public-transport-and-shared-mobility",
    "Railways": "railways",
    "Robotics and Autonomous Transportation": "robotics-and-autonomous-transportation",
    "Transportation Data and Safety": "transportation-data-and-safety",
    "Standards and Connected Transportation": "standards-and-connected-transportation",
    "Learning, Research and Community": "learning-research-and-community",
}

SUBCATEGORY_BY_TITLE = {
    "Multimodal Simulation": "multimodal-simulation",
    "Microscopic Traffic Simulation": "microscopic-traffic-simulation",
    "Agent-Based Simulation": "agent-based-simulation",
    "Connected-Vehicle Simulation": "connected-vehicle-simulation",
    "Pedestrian Simulation": "pedestrian-simulation",
    "Travel-Demand Modelling": "travel-demand-modelling",
    "Network Modelling": "network-modelling",
    "Strategic Planning": "strategic-planning",
    "Maps and Networks": "maps-and-networks",
    "GIS and Spatial Analysis": "gis-and-spatial-analysis",
    "Routing and Optimization": "routing-and-optimization",
    "Accessibility Analysis": "accessibility-analysis",
    "Standards and Data Formats": "standards-and-data-formats",
    "Data Catalogs": "data-catalogs",
    "Data Quality Tools": "data-quality-tools",
    "Journey Planning": "journey-planning",
    "Rider Information": "rider-information",
    "Reference Collections": "reference-collections",
    "Maps and Infrastructure Data": "maps-and-infrastructure-data",
    "Operations and Simulation": "operations-and-simulation",
    "Professional Organizations": "professional-organizations",
    "Autonomous-Vehicle Simulation": "autonomous-vehicle-simulation",
    "Scenarios and Benchmarks": "scenarios-and-benchmarks",
    "Autonomous Road Vehicles": "autonomous-road-vehicles",
    "Autonomous-Driving Datasets": "autonomous-driving-datasets",
    "Vehicle Trajectories": "vehicle-trajectories",
    "Crash and Safety Data": "crash-and-safety-data",
    "Government Data Portals": "government-data-portals",
    "Public-Transport Data": "public-transport-data",
    "Infrastructure Data": "infrastructure-data",
    "Road-Network Standards": "road-network-standards",
    "Scenario Standards": "scenario-standards",
    "Traffic-Data Standards": "traffic-data-standards",
    "Shared-Mobility Standards": "shared-mobility-standards",
    "Public-Transport Standards": "public-transport-standards",
    "Courses and Open Education": "courses-and-open-education",
    "Tutorials and Guidance": "tutorials-and-guidance",
    "Research Databases": "research-databases",
}

ENTRY = re.compile(r"^- \[([^]]+)]\((https?://[^)]+)\) - (.+)$")


def main() -> int:
    errors: list[str] = []
    content = README.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        print("README must contain exactly one catalog marker pair.", file=sys.stderr)
        return 1
    section = content.split(START, 1)[1].split(END, 1)[0]
    resources = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))["resources"]
    expected = {resource["name"]: resource for resource in resources}

    category: str | None = None
    subcategory: str | None = None
    seen: dict[str, int] = defaultdict(int)
    ordered: dict[tuple[str, str], list[str]] = defaultdict(list)

    for line_number, line in enumerate(section.splitlines(), start=1):
        if line.startswith("## "):
            title = line[3:]
            category = CATEGORY_BY_TITLE.get(title)
            subcategory = None
            if category is None:
                errors.append(f"Unknown catalog category heading: {title!r}.")
            continue
        if line.startswith("### "):
            title = line[4:]
            subcategory = SUBCATEGORY_BY_TITLE.get(title)
            if subcategory is None:
                errors.append(f"Unknown catalog subcategory heading: {title!r}.")
            continue
        if not line.startswith("- ["):
            continue

        match = ENTRY.fullmatch(line)
        if not match:
            errors.append(f"Malformed README entry near catalog line {line_number}.")
            continue
        name, url, description = match.groups()
        seen[name] += 1
        resource = expected.get(name)
        if resource is None:
            errors.append(f"README contains unknown resource {name!r}.")
            continue
        if category is None or subcategory is None:
            errors.append(f"{name!r} is not under a recognized category and subcategory.")
            continue
        if resource["category"] != category:
            errors.append(f"{name!r} is under the wrong README category.")
        if resource["subcategory"] != subcategory:
            errors.append(f"{name!r} is under the wrong README subcategory.")
        if url != str(resource["url"]).rstrip("/"):
            errors.append(f"{name!r} has a README URL that differs from resources.yml.")
        if description != resource["description"]:
            errors.append(f"{name!r} has a README description that differs from resources.yml.")
        ordered[(category, subcategory)].append(name)

    for name in expected:
        if seen[name] == 0:
            errors.append(f"README is missing {name!r}.")
        elif seen[name] > 1:
            errors.append(f"README contains {name!r} {seen[name]} times.")
    for location, names in ordered.items():
        if names != sorted(names, key=str.casefold):
            errors.append(f"README entries are not alphabetical in {location[0]}/{location[1]}.")

    if errors:
        print("README validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"README matches all {len(resources)} structured resources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
