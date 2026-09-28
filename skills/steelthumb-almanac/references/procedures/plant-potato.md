---
type: Procedure
title: Plant potatoes in soil or grow bags
description: Solanum tuberosum for edible tubers in soil and grow bags; general guidance with separate
  cultivar scope.
status: draft
sources:
- id: umd-potato
  title: Growing Potatoes in a Home Garden — Maryland Extension
  resource: https://www.extension.umd.edu/resource/growing-potatoes-home-garden
- id: isu-potato
  title: Growing Potatoes in the Home Garden — Iowa State Extension
  resource: https://yardandgarden.extension.iastate.edu/how-to/growing-potatoes-home-garden
- id: spudnik
  title: Potatoes Grow in Bags at Project Spudnik — Maryland Grows
  resource: https://marylandgrows.umd.edu/2020/03/20/potatoes-grow-in-bags-at-project-spudnik/
- id: rhs-potato
  title: How to grow potatoes — RHS
  resource: https://www.rhs.org.uk/vegetables/potatoes/grow-your-own
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: seed-stock
    kind: recommendation
    statement: Use certified seed potatoes rather than supermarket or saved garden tubers of unknown disease
      status.
    applicability:
      conditions: Maryland home potato guidance.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Planting potato facts
  - id: warm-soil
    kind: recommendation
    statement: Maryland recommends soil at least 45°F at planting.
    applicability:
      conditions: Soil temperature, not air temperature.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Planting potato facts
    quantity:
      property: minimum_planting_soil_temperature
      unit: degF
      value: 45
  - id: ground-depth
    kind: recommendation
    statement: Iowa plants small whole seed potatoes about 4 inches deep.
    applicability:
      conditions: Spring ground planting.
    evidence:
    - source_id: isu-potato
      relation: supports
      locator: Planting
    quantity:
      property: planting_depth
      unit: in
      value: 4
  - id: ground-spacing
    kind: recommendation
    statement: Iowa spaces seed potatoes about 1 foot apart.
    applicability:
      conditions: Ground planting; not bag density.
    evidence:
    - source_id: isu-potato
      relation: supports
      locator: Planting
    quantity:
      property: in_row_spacing
      unit: ft
      value: 1
  - id: ground-row-spacing
    kind: recommendation
    statement: Iowa spaces potato rows 2–3 feet apart.
    applicability:
      conditions: Ground planting; not bag density.
    evidence:
    - source_id: isu-potato
      relation: supports
      locator: Planting
    quantity:
      property: row_spacing
      unit: ft
      min: 2
      max: 3
  - id: bag-dimensions
    kind: descriptive
    statement: Spudnik bags are 16 inches deep and 16 inches across.
    applicability:
      conditions: Community garden method; dimensions and capacity reported as written.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 2
    quantity:
      property: bag_depth_and_diameter
      unit: in
      value: 16
      basis: Both source dimensions.
  - id: bag-capacity
    kind: descriptive
    statement: Spudnik labels these bags 12-gallon.
    applicability:
      conditions: Community garden method; dimensions and capacity reported as written.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 2
    quantity:
      property: nominal_bag_capacity
      unit: gal
      value: 12
  - id: bag-count
    kind: recommendation
    statement: Spudnik plants 3–5 whole seed potatoes or pieces per bag.
    applicability:
      conditions: Its specified bag; not a proven optimum.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 4
    quantity:
      property: planting_material_count
      unit: seed potatoes or pieces
      min: 3
      max: 5
      basis: Per specified Spudnik bag.
  - id: base-layer
    kind: recommendation
    statement: Begin with 4 inches of mix in the Spudnik bag.
    applicability:
      conditions: Specified Spudnik method.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 3
    quantity:
      property: initial_medium_depth
      unit: in
      value: 4
  - id: seed-cover
    kind: recommendation
    statement: Cover the seed potatoes with 3 inches of mix.
    applicability:
      conditions: Specified Spudnik method.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 4
    quantity:
      property: seed_cover_depth
      unit: in
      value: 3
  - id: site-light
    kind: recommendation
    statement: Choose a sunny, well-drained site for potatoes.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: isu-potato
      relation: supports
      locator: Planting
  relations:
  - predicate: applies_to
    target: /crops/potato.md
  - predicate: applies_to
    target: /cultivars/yukon-gold-potato.md
  - predicate: applies_to
    target: /crops/russet-potato.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant potatoes in soil or grow bags

Applies to [potato](../crops/potato.md), [yukon gold potato](../cultivars/yukon-gold-potato.md), [russet potato](../crops/russet-potato.md). Solanum tuberosum for edible tubers in soil and grow bags; general guidance with separate cultivar scope.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have labelled certified seed stock, a soil thermometer, water, a sunny prepared site, and container mix for bags. This route uses small whole seed potatoes; cutting and callusing are outside it.

## Steps and source settings

1. Confirm cultivar and readiness, then choose one branch below.
2. For ground planting, use the Iowa depth and spacing; choose a sunny, drained site.[^isu-potato]
3. For the Spudnik bag branch, use the base-layer and seed-cover settings below, placing eyes up.[^spudnik] Use its bag dimensions and count below as a reported recipe.
4. Record the actual filled dimensions and initial medium level, then follow [care](care-for-potato.md) for adding medium. Apply the [shared drainage checks](../systems/outdoor-grow-bags.md).

<a id="seed-stock"></a>
Use certified seed potatoes rather than supermarket or saved garden tubers of unknown disease status.[^umd-potato]

<a id="warm-soil"></a>
Maryland recommends soil at least 45°F at planting.[^umd-potato]

<a id="ground-depth"></a>
Iowa plants small whole seed potatoes about 4 inches deep.[^isu-potato]

<a id="ground-spacing"></a>
Iowa spaces seed potatoes about 1 foot apart.[^isu-potato]

<a id="ground-row-spacing"></a>
Iowa spaces potato rows 2–3 feet apart.[^isu-potato]

<a id="bag-dimensions"></a>
Spudnik bags are 16 inches deep and 16 inches across.[^spudnik]

<a id="bag-capacity"></a>
Spudnik labels these bags 12-gallon.[^spudnik]

<a id="bag-count"></a>
Spudnik plants 3–5 whole seed potatoes or pieces per bag.[^spudnik]

<a id="base-layer"></a>
Begin with 4 inches of mix in the Spudnik bag.[^spudnik]

<a id="seed-cover"></a>
Cover the seed potatoes with 3 inches of mix.[^spudnik]

<a id="site-light"></a>
Choose a sunny, well-drained site for potatoes.[^isu-potato]

## Follow-up

Record planting date, source lot, count, and first emergence. Inspect moisture below the surface before assuming all of the bag is wet.

## Limits

RHS offers a smaller-pot method and favors early varieties.[^rhs-potato] That alternative is not the lower bound of a proven optimal bag range. No evidence here establishes this bag recipe as optimal for Yukon Gold or every russet.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umd-potato]: [Growing Potatoes in a Home Garden — Maryland Extension](https://www.extension.umd.edu/resource/growing-potatoes-home-garden).
[^isu-potato]: [Growing Potatoes in the Home Garden — Iowa State Extension](https://yardandgarden.extension.iastate.edu/how-to/growing-potatoes-home-garden).
[^spudnik]: [Potatoes Grow in Bags at Project Spudnik — Maryland Grows](https://marylandgrows.umd.edu/2020/03/20/potatoes-grow-in-bags-at-project-spudnik/).
[^rhs-potato]: [How to grow potatoes — RHS](https://www.rhs.org.uk/vegetables/potatoes/grow-your-own).
