---
type: Procedure
title: Plant cherry tomatoes
description: Cherry-fruited Solanum lycopersicum for fresh fruit; ground and outdoor bag growing, cultivar
  unspecified.
status: draft
sources:
- id: umn-tomato
  title: Growing tomatoes in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-tomatoes
- id: umd-container
  title: Types of Containers for Growing Vegetables — Maryland Extension
  resource: https://extension.umd.edu/resource/types-containers-growing-vegetables
- id: umd-tomato
  title: Growing Tomatoes in a Home Garden — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-tomatoes-home-garden
- id: rhs-tomato
  title: How to grow tomatoes — RHS
  resource: https://www.rhs.org.uk/vegetables/tomatoes/grow-your-own
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: readiness
    kind: recommendation
    statement: Transplant tomatoes after frost risk passes and soil warms; install supports at planting.
    applicability:
      conditions: Outdoor hardened transplants.
    evidence:
    - source_id: umn-tomato
      relation: supports
      locator: Transplanting > Climate and Treatment
  - id: ground-spacing
    kind: recommendation
    statement: Minnesota spaces vining tomatoes 2–3 feet apart in all directions.
    applicability:
      conditions: Vining plants in soil; compact types can differ.
    evidence:
    - source_id: umn-tomato
      relation: supports
      locator: Transplanting > Location
    quantity:
      property: plant_spacing
      unit: ft
      min: 2
      max: 3
  - id: depth
    kind: recommendation
    statement: Bury part of an ungrafted tomato stem, retaining leaves above the surface, to permit additional
      roots.
    applicability:
      conditions: Editorial restriction to ungrafted plants; grafted depth requires nursery instructions.
    evidence:
    - source_id: umn-tomato
      relation: supports
      locator: Transplanting > Treatment
  - id: bag-volume
    kind: recommendation
    statement: Maryland gives a minimum range of 8–10 gallons of medium per large vegetable plant, including
      tomatoes.
    applicability:
      conditions: General container recommendation; not a cherry-cultivar optimum.
    evidence:
    - source_id: umd-container
      relation: supports
      locator: Choose the right container size > Large vegetables
    quantity:
      property: container_medium_volume
      unit: gal
      min: 8
      max: 10
      basis: Range of recommended minimums; not a maximum container size.
  - id: bag-depth
    kind: recommendation
    statement: That Maryland large-vegetable recommendation also specifies a minimum depth range of 12–16
      inches of medium depth.
    applicability:
      conditions: Companion requirement to volume.
    evidence:
    - source_id: umd-container
      relation: supports
      locator: Choose the right container size > Large vegetables
    quantity:
      property: container_medium_depth
      unit: in
      min: 12
      max: 16
      basis: Range of recommended minimums; not a maximum container size.
  - id: site-light
    kind: recommendation
    statement: Grow tomatoes in full sun.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: umd-tomato
      relation: supports
      locator: About tomatoes → Planting
  relations:
  - predicate: applies_to
    target: /crops/cherry-tomato.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant cherry tomatoes

Applies to [cherry tomato](../crops/cherry-tomato.md). Cherry-fruited Solanum lycopersicum for fresh fruit; ground and outdoor bag growing, cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have hardened labelled transplants, growth-habit information, supports, water, and medium for bags. This route assumes ungrafted plants unless noted.

## Steps and source settings

1. Confirm mature plant habit and site sunlight; use full sun.[^umd-tomato]
2. Choose the ground spacing or large-container branch below. For a tall cherry in a bag, use one plant and check both volume and usable depth.
3. Follow [shared setup](../systems/outdoor-grow-bags.md), then transplant at the stated depth and water in.[^umn-tomato]
4. Record dimensions, cultivar, date, and support anchoring.

<a id="readiness"></a>
Transplant tomatoes after frost risk passes and soil warms; install supports at planting.[^umn-tomato]

<a id="ground-spacing"></a>
Minnesota spaces vining tomatoes 2–3 feet apart in all directions.[^umn-tomato]

<a id="depth"></a>
Bury part of an ungrafted tomato stem, retaining leaves above the surface, to permit additional roots.[^umn-tomato]

<a id="bag-volume"></a>
Maryland gives a minimum range of 8–10 gallons of medium per large vegetable plant, including tomatoes.[^umd-container]

<a id="bag-depth"></a>
That Maryland large-vegetable recommendation also specifies a minimum depth range of 12–16 inches of medium depth.[^umd-container]

<a id="site-light"></a>
Grow tomatoes in full sun.[^umd-tomato]

## Follow-up

Check transplant moisture and stability; observe new growth before treating leaf changes as a nutrient shortage. Continue with [care](care-for-cherry-tomato.md).

## Limits

RHS also describes standard growing sacks and pot dimensions.[^rhs-tomato] A flat compost sack is not automatically equivalent to a freestanding fabric bag. No optimal microdwarf bag volume is established; grafted plants need graft-specific planting instructions.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-tomato]: [Growing tomatoes in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-tomatoes).
[^umd-container]: [Types of Containers for Growing Vegetables — Maryland Extension](https://extension.umd.edu/resource/types-containers-growing-vegetables).
[^umd-tomato]: [Growing Tomatoes in a Home Garden — Maryland Extension](https://extension.umd.edu/resource/growing-tomatoes-home-garden).
[^rhs-tomato]: [How to grow tomatoes — RHS](https://www.rhs.org.uk/vegetables/tomatoes/grow-your-own).
