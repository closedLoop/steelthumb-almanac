---
type: Procedure
title: Plant jalapeño peppers
description: Jalapeño-type Capsicum annuum for fruit; warm-season beds and outdoor grow bags, cultivar
  unspecified.
status: draft
sources:
- id: umn-pepper
  title: Growing peppers in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-peppers
- id: umd-pepper
  title: Growing Peppers in a Home Garden — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-peppers-home-garden
- id: uconn-pepper
  title: Peppers — University of Connecticut Home Garden Education
  resource: https://homegarden.cahnr.uconn.edu/factsheets/peppers/
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: night-temperature
    kind: recommendation
    statement: Minnesota transplants peppers after nighttime lows remain above 50°F.
    applicability:
      conditions: Outdoor pepper transplants.
    evidence:
    - source_id: umn-pepper
      relation: supports
      locator: Transplanting > Climate
    quantity:
      property: minimum_night_air_temperature
      unit: degF
      value: 50
      basis: Source says above this value.
  - id: soil-temperature
    kind: recommendation
    statement: Maryland advises waiting for soil to reach 65°F.
    applicability:
      conditions: Soil, not night air; complementary readiness criterion.
    evidence:
    - source_id: umd-pepper
      relation: supports
      locator: Planting pepper facts
    quantity:
      property: planting_soil_temperature
      unit: degF
      value: 65
  - id: spacing
    kind: recommendation
    statement: Minnesota spaces pepper plants 18 inches apart.
    applicability:
      conditions: Ground plants; not bag count.
    evidence:
    - source_id: umn-pepper
      relation: supports
      locator: Transplanting > Location
    quantity:
      property: in_row_spacing
      unit: in
      value: 18
  - id: row-spacing
    kind: recommendation
    statement: Minnesota spaces pepper rows 30–36 inches apart.
    applicability:
      conditions: Ground plants; not bag count.
    evidence:
    - source_id: umn-pepper
      relation: supports
      locator: Transplanting > Location
    quantity:
      property: row_spacing
      unit: in
      min: 30
      max: 36
  - id: depth
    kind: recommendation
    statement: Set pepper transplants at their previous soil line and water them in.
    applicability:
      conditions: Transplants, not seed sowing.
    evidence:
    - source_id: umn-pepper
      relation: supports
      locator: Transplanting > Treatment
  - id: bag-size
    kind: recommendation
    statement: Maryland gives a 5-gallon minimum container for peppers.
    applicability:
      conditions: General peppers; not a jalapeño-specific fabric trial.
    evidence:
    - source_id: umd-pepper
      relation: supports
      locator: Growing and care
    quantity:
      property: minimum_container_capacity
      unit: gal
      value: 5
      basis: Source nominal size; container type unspecified.
  - id: site-light
    kind: recommendation
    statement: Grow peppers in full sun.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: uconn-pepper
      relation: supports
      locator: Soil Requirements
  relations:
  - predicate: applies_to
    target: /crops/jalapeno-pepper.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant jalapeño peppers

Applies to [jalapeno pepper](../crops/jalapeno-pepper.md). Jalapeño-type Capsicum annuum for fruit; warm-season beds and outdoor grow bags, cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have labelled hardened transplants, water, a thermometer, a sunny site, and medium for bags.

## Steps and source settings

1. Check both soil and night-air readiness; they measure different things and must not be averaged.
2. For ground growing, use the spacing and planting-depth claims below.
3. For bags, start with one plant as an editorial density choice and use the sourced minimum as a floor, not an optimum. Follow [shared setup](../systems/outdoor-grow-bags.md).
4. Record cultivar, planting date, bag dimensions, and initial watering.

<a id="night-temperature"></a>
Minnesota transplants peppers after nighttime lows remain above 50°F.[^umn-pepper]

<a id="soil-temperature"></a>
Maryland advises waiting for soil to reach 65°F.[^umd-pepper]

<a id="spacing"></a>
Minnesota spaces pepper plants 18 inches apart.[^umn-pepper]

<a id="row-spacing"></a>
Minnesota spaces pepper rows 30–36 inches apart.[^umn-pepper]

<a id="depth"></a>
Set pepper transplants at their previous soil line and water them in.[^umn-pepper]

<a id="bag-size"></a>
Maryland gives a 5-gallon minimum container for peppers.[^umd-pepper]

<a id="site-light"></a>
Grow peppers in full sun.[^uconn-pepper]

## Follow-up

Observe establishment and new growth, then begin [care](care-for-jalapeno-pepper.md).

## Limits

Seed-starting and a local planting calendar are outside this transplant route. Maryland’s generic container table gives a larger recommendation for large vegetables; the pepper-specific minimum does not settle optimal size for a full-grown plant.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-pepper]: [Growing peppers in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-peppers).
[^umd-pepper]: [Growing Peppers in a Home Garden — Maryland Extension](https://extension.umd.edu/resource/growing-peppers-home-garden).

[^uconn-pepper]: [Peppers — University of Connecticut Home Garden Education](https://homegarden.cahnr.uconn.edu/factsheets/peppers/).
