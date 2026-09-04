# Awesome Transportation 🚦🚆🚌🚲 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Engineering and research across road, rail, transit, active mobility, connected systems, and autonomous transportation.

A curated collection of high-quality tools, datasets, software, APIs, courses, tutorials, standards, and open-source projects for transportation and mobility.

This collection is curated rather than exhaustive. Resources are selected based on usefulness, quality, relevance, and accessibility.

The list serves transportation engineers, planners, railway and transit professionals, researchers, students, data scientists, developers, and autonomous-systems teams. Every entry must have a meaningful transportation connection; generic AI, GIS, or robotics resources are out of scope.

## Contents

- [Simulation and Modelling](#simulation-and-modelling)
- [Planning, Operations and Spatial Analysis](#planning-operations-and-spatial-analysis)
- [Public Transport and Shared Mobility](#public-transport-and-shared-mobility)
- [Railways](#railways)
- [Robotics and Autonomous Transportation](#robotics-and-autonomous-transportation)
- [Transportation Data and Safety](#transportation-data-and-safety)
- [Standards and Connected Transportation](#standards-and-connected-transportation)
- [Learning, Research and Community](#learning-research-and-community)
- [Coverage Roadmap](#coverage-roadmap)

<!-- catalog:start -->

## Simulation and Modelling

### Agent-Based Simulation

- [BEAM](https://transportation.lbl.gov/index.php/beam) - Agent-based framework for modelling transportation, energy, and mobility systems at regional scale.
- [MATSim](https://www.matsim.org) - Open-source agent-based framework for large-scale transport simulation, travel demand, and policy analysis.

### Connected-Vehicle Simulation

- [Eclipse MOSAIC](https://eclipse.dev/mosaic) - Multi-domain co-simulation framework for connected, cooperative, and automated mobility applications.
- [Veins](https://veins.car2x.org) - Vehicular-network simulation framework coupling road traffic and wireless-network models for V2X research.

### Microscopic Traffic Simulation

- [CityFlow](https://cityflow-project.github.io) - Multi-agent traffic simulation platform designed for large-scale traffic-signal control and reinforcement-learning experiments.
- [Eclipse SUMO](https://eclipse.dev/sumo) - Open-source microscopic and continuous traffic simulator with multimodal demand, network editing, and extensive control interfaces.

### Multimodal Simulation

- [A/B Street](https://a-b-street.github.io/docs) - Interactive transportation planning simulator for exploring traffic, parking, cycling, and street-design scenarios on OpenStreetMap networks.

### Pedestrian Simulation

- [JuPedSim](https://www.jupedsim.org) - Open-source pedestrian-dynamics simulator for evacuation, facility, and walking-flow analysis.

## Planning, Operations and Spatial Analysis

### Accessibility Analysis

- [r5r](https://ipeagit.github.io/r5r) - R package for rapid multimodal routing and accessibility analysis using the R5 routing engine.

### GIS and Spatial Analysis

- [QGIS](https://qgis.org) - Open-source desktop GIS for spatial analysis, network data preparation, cartography, and transportation workflows.

### Maps and Networks

- [OpenStreetMap](https://www.openstreetmap.org) - Collaborative global map database widely used for routable road, path, cycling, rail, and transit network data.
- [OSMnx](https://osmnx.readthedocs.io) - Python package for downloading, modelling, analysing, and visualizing street and transport networks from OpenStreetMap.

### Network Modelling

- [AequilibraE](https://www.aequilibrae.com) - Open-source transportation-modelling toolkit for network skimming, traffic assignment, transit, and matrix workflows.

### Routing and Optimization

- [Open Source Routing Machine](https://project-osrm.org) - High-performance routing engine for shortest-path and travel-time queries on OpenStreetMap road networks.
- [pgRouting](https://pgrouting.org) - PostgreSQL and PostGIS extension providing shortest-path, vehicle-routing, and graph-analysis functions for spatial networks.

### Strategic Planning

- [VisionEval](https://visioneval.github.io) - Open-source strategic planning system for evaluating regional transport, land-use, energy, and emissions scenarios.

### Travel-Demand Modelling

- [ActivitySim](https://activitysim.github.io/activitysim) - Open platform for implementing disaggregate activity-based travel-demand models in Python.

## Public Transport and Shared Mobility

### Data Catalogs

- [Mobility Database](https://mobilitydatabase.org) - Global catalog of public GTFS, GTFS Realtime, and GBFS feeds with quality and source metadata.
- [Transitland](https://www.transit.land) - Community-maintained transit-feed registry and API for exploring aggregated GTFS data.

### Data Quality Tools

- [Canonical GTFS Schedule Validator](https://github.com/MobilityData/gtfs-validator) - Canonical open-source validator for checking GTFS Schedule feeds against the specification and best practices.

### Journey Planning

- [Navitia](https://github.com/hove-io/navitia) - Open-source multimodal journey-planning and passenger-information engine with routing and transit APIs.
- [OpenTripPlanner](https://www.opentripplanner.org) - Open-source multimodal journey-planning engine using GTFS and OpenStreetMap data.

### Reference Collections

- [MobilityData Awesome Transit](https://github.com/MobilityData/awesome-transit) - Specialist community list covering open standards, software, datasets, and APIs for public transportation.

### Rider Information

- [OneBusAway](https://opentransitsoftwarefoundation.org/onebusaway) - Open-source platform and applications for publishing real-time transit arrivals and rider information.

### Standards and Data Formats

- [General Transit Feed Specification](https://gtfs.org) - Official documentation for the static and real-time open data specifications used to publish public-transport information.

## Railways

### Maps and Infrastructure Data

- [OpenRailwayMap](https://www.openrailwaymap.org) - Global railway-infrastructure map built from OpenStreetMap data, including tracks, signalling, electrification, and speeds.

### Operations and Simulation

- [OpenTrack](https://www.opentrack.ch/opentrack/opentrack_e/opentrack_e.html) - Railway operations simulation software used for timetable, capacity, signalling, and infrastructure studies.
- [OSRD](https://osrd.fr/en) - Open-source railway capacity, timetable, and infrastructure-design platform developed for operational planning.

### Professional Organizations

- [International Union of Railways](https://uic.org) - International railway-sector organization publishing technical reports, statistics, standards-related material, and research programmes.

### Standards and Data Formats

- [railML](https://www.railml.org) - Open XML-based exchange format for railway infrastructure, rolling stock, timetables, and interlocking data.

## Robotics and Autonomous Transportation

### Autonomous Road Vehicles

- [Apollo](https://github.com/ApolloAuto/apollo) - Open autonomous-driving platform integrating perception, prediction, planning, control, mapping, and simulation components.
- [Autoware](https://autoware.org) - Open-source autonomous-driving software stack covering sensing, localization, planning, control, and vehicle interfaces.

### Autonomous-Driving Datasets

- [Argoverse 2](https://www.argoverse.org/av2.html) - Autonomous-driving datasets supporting 3D perception, motion forecasting, and map-change research.
- [KITTI Vision Benchmark Suite](https://www.cvlibs.net/datasets/kitti) - Established road-scene benchmark datasets for stereo vision, optical flow, detection, tracking, odometry, and depth estimation.
- [nuScenes](https://www.nuscenes.org) - Multimodal autonomous-driving dataset with camera, lidar, radar, maps, and annotated scenes.
- [Waymo Open Dataset](https://waymo.com/open) - Large-scale autonomous-driving datasets and benchmarks for perception, motion prediction, and end-to-end driving research.

### Autonomous-Vehicle Simulation

- [CARLA](https://carla.org) - Open-source urban driving simulator for autonomous-system development, perception, planning, and control research.

### Scenarios and Benchmarks

- [CommonRoad](https://commonroad.in.tum.de) - Benchmarking framework with scenarios, models, and tools for motion planning and automated-driving research.
- [ScenarioNet](https://metadriverse.github.io/scenarionet) - Scenario database and toolkit for converting, managing, and replaying driving datasets in learning and simulation workflows.

## Transportation Data and Safety

### Crash and Safety Data

- [Fatality Analysis Reporting System](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) - National census of police-reported fatal motor-vehicle crashes in the United States, with downloadable annual data.

### Government Data Portals

- [Bureau of Transportation Statistics](https://www.bts.gov) - Official United States portal for multimodal transportation statistics, maps, indicators, and data tools.
- [International Transport Forum Data](https://www.itf-oecd.org/transport-data-and-statistics) - Cross-country transport statistics covering passenger and freight activity, infrastructure, vehicles, and safety.

### Infrastructure Data

- [LTPP InfoPave](https://infopave.fhwa.dot.gov) - Web portal for Long-Term Pavement Performance data, documentation, visualization, and analysis tools.

### Public-Transport Data

- [National Transit Database](https://www.transit.dot.gov/ntd) - Official data on United States transit agencies, service, ridership, finance, assets, safety, and performance.

### Vehicle Trajectories

- [highD](https://levelxdata.com/highd-dataset) - Drone-recorded vehicle trajectories from German motorways, available by application for non-commercial traffic-flow and automated-driving research.
- [INTERACTION Dataset](https://interaction-dataset.com) - Trajectory dataset of interactive driving scenarios from intersections, roundabouts, and merging locations in several countries.
- [NGSIM](https://ops.fhwa.dot.gov/trafficanalysistools/ngsim.htm) - Federal Highway Administration programme providing detailed vehicle-trajectory datasets and supporting traffic-analysis material.

## Standards and Connected Transportation

### Public-Transport Standards

- [NeTEx](https://transmodel-cen.eu/index.php/netex) - CEN standard for exchanging public-transport network, timetable, fare, and related reference data.

### Road-Network Standards

- [ASAM OpenDRIVE](https://www.asam.net/standards/detail/opendrive) - Standard for the logical description of road networks used by driving simulation and automated-driving applications.

### Scenario Standards

- [ASAM OpenSCENARIO](https://www.asam.net/standards/detail/openscenario) - Standard for describing dynamic driving scenarios used in simulation, testing, and validation of automated vehicles.

### Shared-Mobility Standards

- [General Bikeshare Feed Specification](https://gbfs.org) - Open data standard for real-time information about shared-mobility systems such as bikeshare and scooter share.

### Traffic-Data Standards

- [DATEX II](https://datex2.eu) - European standard and reference model for exchanging road-traffic and travel-information data.

## Learning, Research and Community

### Courses and Open Education

- [MIT OpenCourseWare Transportation Systems Analysis](https://ocw.mit.edu/courses/1-201j-transportation-systems-analysis-demand-and-economics-fall-2008) - Graduate-level open course materials on transportation demand, supply, equilibrium, evaluation, and economics.

### Professional Organizations

- [IEEE Intelligent Transportation Systems Society](https://ieee-itss.org) - Professional society supporting conferences, publications, standards activity, and technical communities in intelligent transportation systems.
- [International Transport Forum](https://www.itf-oecd.org) - Intergovernmental organization producing policy research, statistics, and international dialogue across transportation modes.
- [Transportation Research Board](https://www.trb.org) - Research organization convening technical committees, conferences, publications, and the annual meeting across transportation modes.

### Research Databases

- [TRID](https://trid.trb.org) - Major bibliographic database of transportation research literature maintained by the Transportation Research Board and partners.

### Tutorials and Guidance

- [FHWA Traffic Analysis Toolbox](https://ops.fhwa.dot.gov/trafficanalysistools) - Practitioner guidance and reference material for selecting, applying, and validating traffic-analysis tools and simulation models.

<!-- catalog:end -->

## Coverage Roadmap

The initial catalog favors resources that could be verified with high confidence. Strong contributions are especially welcome in freight and logistics, active transportation, traffic engineering and signal control, road safety methods, aviation, maritime transportation, railway robotics, infrastructure inspection, digital twins, transportation-specific computer vision, and open educational resources.

See the [full taxonomy](docs/taxonomy.md) for intended coverage, the [curation guide](docs/curation.md) for the data schema and review method, and the [project-readiness notes](docs/project-readiness.md) for Awesome compatibility and suggested GitHub metadata.

## Contributing

Suggestions and corrections are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Update both the readable list and its structured metadata, run the documented checks, and include evidence that the canonical URL was reviewed.
