# Taxonomy

The catalog uses eight reader-facing pillars. These are intentionally broader than individual modes or methods: they keep the main list navigable while allowing the structured data to grow through subcategories.

## 1. Transportation Domains

- **Traffic engineering** — Traffic flow, operations, control, capacity, and design.
- **Transportation planning** — Policy, land use, accessibility, demand, and evaluation.
- **Road safety** — Crash data, safe-system methods, conflict analysis, and design guidance.
- **Public transport and shared mobility** — Scheduled and demand-responsive transit, GTFS, bikeshare, and mobility services.
- **Railways** — Infrastructure, signalling, operations, capacity, timetabling, and railway data.
- **Freight and logistics** — Goods movement, routing, terminals, supply chains, and city logistics.
- **Active transportation** — Walking, cycling, micromobility, accessibility, and public realm.
- **Aviation** — Air-transport operations, networks, safety, and infrastructure.
- **Maritime** — Ports, waterways, vessels, terminals, and maritime logistics.

These domains appear as dedicated subcategories when the catalog has enough strong resources. Thin sections remain in the roadmap rather than being filled with marginal links.

## 2. Simulation and Modelling

- Microscopic traffic simulation
- Mesoscopic and macroscopic simulation
- Agent-based and activity-based simulation
- Multimodal and public-transport simulation
- Railway operations simulation
- Pedestrian and crowd simulation
- Freight and logistics simulation
- Connected-vehicle co-simulation
- Autonomous-vehicle simulation and testing

## 3. Planning, Operations and Spatial Analysis

- Travel-demand modelling
- Network modelling and traffic assignment
- Routing, scheduling, and optimization
- Strategic and scenario planning
- Accessibility and equity analysis
- GIS and spatial analysis
- Maps and transportation networks
- Traffic-signal control and operations
- Visualization, virtual reality, and extended reality
- Remote sensing and transportation computer vision

## 4. Robotics and Autonomous Transportation

- Autonomous road vehicles
- Autonomous public transport, buses, and shuttles
- Autonomous freight and delivery vehicles
- Railway and rail-yard robotics
- Logistics, port, and terminal robotics
- Infrastructure inspection robots and UAVs
- Mobile mapping and sensing platforms
- Cooperative and multi-agent transportation systems
- Robotics simulation, scenarios, and testing

Generic robotics is out of scope. A resource must support a transportation system, vehicle, terminal, network, or infrastructure task—not merely be technically reusable in one.

## 5. Data, Software and Infrastructure

- Open-source transportation software
- Traffic counts and detector data
- Vehicle, pedestrian, and cyclist trajectories
- Crash and road-safety data
- Transit and GTFS data
- Railway and infrastructure data
- Road and multimodal networks
- Freight, aviation, and maritime data
- Autonomous-driving data
- APIs and data catalogs
- Standards and data formats
- Cloud and scalable computing for transportation

Software is primarily filed by the job it helps a reader perform. “Open-source software” is a property and filter, not a catch-all section.

## 6. Connected and Intelligent Transportation

- Connected transportation and V2X
- Intelligent transportation systems
- Traffic management and signal control
- Cooperative automation
- Digital twins
- Sensor, edge, and communications infrastructure
- Traffic and scenario exchange standards

## 7. Learning, Research and Community

- Courses and MOOCs
- Tutorials and practitioner guidance
- Books and open educational resources
- Video courses and channels
- Research groups and laboratories
- Research databases and journals
- Conferences
- Professional organizations

## 8. Controlled Values

The current top-level `category` values are:

- `simulation-and-modelling`
- `planning-operations-and-spatial-analysis`
- `public-transport-and-shared-mobility`
- `railways`
- `robotics-and-autonomous-transportation`
- `transportation-data-and-safety`
- `standards-and-connected-transportation`
- `learning-research-and-community`

Allowed `transport_mode` values are `road`, `rail`, `transit`, `cycling`, `walking`, `freight`, `aviation`, `maritime`, and `multimodal`.

Allowed `resource_type` values are `software`, `dataset`, `api`, `tutorial`, `course`, `book`, `documentation`, `repository`, `standard`, `research-group`, `conference`, `journal`, and `visualization-tool`.

## Design Decisions

The initial 36-topic proposal has been retained as coverage goals but not as 36 peer headings. Related concepts are grouped into eight pillars so readers can scan the README quickly. Modes with strong, distinct professional ecosystems—public transport and railways—receive dedicated sections. Cross-cutting methods such as simulation, GIS, AI, optimization, ITS, and digital twins sit in method-oriented pillars. Resource type and transport mode remain structured fields, so future pages can expose alternative views without duplicating entries.
