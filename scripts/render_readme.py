#!/usr/bin/env python3
"""Render the curated catalog between README marker comments."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CATALOG = ROOT / "data" / "resources.yml"
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"

CATEGORY_TITLES = {
    "simulation-and-modelling": "Simulation and Modelling",
    "planning-operations-and-spatial-analysis": "Planning, Operations and Spatial Analysis",
    "public-transport-and-shared-mobility": "Public Transport and Shared Mobility",
    "railways": "Railways",
    "robotics-and-autonomous-transportation": "Robotics and Autonomous Transportation",
    "transportation-data-and-safety": "Transportation Data and Safety",
    "standards-and-connected-transportation": "Standards and Connected Transportation",
    "learning-research-and-community": "Learning, Research and Community",
}

SUBCATEGORY_TITLES = {
    "multimodal-simulation": "Multimodal Simulation",
    "microscopic-traffic-simulation": "Microscopic Traffic Simulation",
    "agent-based-simulation": "Agent-Based Simulation",
    "connected-vehicle-simulation": "Connected-Vehicle Simulation",
    "pedestrian-simulation": "Pedestrian Simulation",
    "travel-demand-modelling": "Travel-Demand Modelling",
    "network-modelling": "Network Modelling",
    "strategic-planning": "Strategic Planning",
    "maps-and-networks": "Maps and Networks",
    "gis-and-spatial-analysis": "GIS and Spatial Analysis",
    "routing-and-optimization": "Routing and Optimization",
    "accessibility-analysis": "Accessibility Analysis",
    "standards-and-data-formats": "Standards and Data Formats",
    "data-catalogs": "Data Catalogs",
    "data-quality-tools": "Data Quality Tools",
    "journey-planning": "Journey Planning",
    "rider-information": "Rider Information",
    "reference-collections": "Reference Collections",
    "maps-and-infrastructure-data": "Maps and Infrastructure Data",
    "operations-and-simulation": "Operations and Simulation",
    "professional-organizations": "Professional Organizations",
    "autonomous-vehicle-simulation": "Autonomous-Vehicle Simulation",
    "scenarios-and-benchmarks": "Scenarios and Benchmarks",
    "autonomous-road-vehicles": "Autonomous Road Vehicles",
    "autonomous-driving-datasets": "Autonomous-Driving Datasets",
    "vehicle-trajectories": "Vehicle Trajectories",
    "crash-and-safety-data": "Crash and Safety Data",
    "government-data-portals": "Government Data Portals",
    "public-transport-data": "Public-Transport Data",
    "infrastructure-data": "Infrastructure Data",
    "road-network-standards": "Road-Network Standards",
    "scenario-standards": "Scenario Standards",
    "traffic-data-standards": "Traffic-Data Standards",
    "shared-mobility-standards": "Shared-Mobility Standards",
    "public-transport-standards": "Public-Transport Standards",
    "courses-and-open-education": "Courses and Open Education",
    "tutorials-and-guidance": "Tutorials and Guidance",
    "research-databases": "Research Databases",
}


def render() -> str:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    grouped: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(lambda: defaultdict(list))
    for resource in data["resources"]:
        grouped[resource["category"]][resource["subcategory"]].append(resource)

    lines: list[str] = [START]
    for category, category_title in CATEGORY_TITLES.items():
        lines.extend(["", f"## {category_title}"])
        subcategories = grouped.get(category, {})
        for subcategory in sorted(subcategories, key=lambda value: SUBCATEGORY_TITLES.get(value, value).casefold()):
            lines.extend(["", f"### {SUBCATEGORY_TITLES.get(subcategory, subcategory.replace('-', ' ').title())}", ""])
            for resource in sorted(subcategories[subcategory], key=lambda item: str(item["name"]).casefold()):
                display_url = str(resource["url"]).rstrip("/")
                lines.append(f"- [{resource['name']}]({display_url}) - {resource['description']}")
    lines.extend(["", END])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if README is not in sync.")
    args = parser.parse_args()

    content = README.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        print("README must contain exactly one catalog marker pair.", file=sys.stderr)
        return 1
    before, remainder = content.split(START, 1)
    _, after = remainder.split(END, 1)
    updated = before.rstrip() + "\n\n" + render() + after

    if args.check:
        if updated != content:
            print("README catalog is out of date; run python scripts/render_readme.py.", file=sys.stderr)
            return 1
        print("README catalog is in sync.")
        return 0

    README.write_text(updated, encoding="utf-8", newline="\n")
    print("Rendered README catalog.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
