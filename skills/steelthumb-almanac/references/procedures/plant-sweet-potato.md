---
type: Procedure
title: Plant sweet-potato slips
description: Ipomoea batatas for storage roots in warm-season beds or outdoor grow bags; cultivar unspecified.
status: draft
sources:
- id: umd-sweet
  title: Growing Sweet Potatoes in a Home Garden — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-sweet-potatoes-home-garden
- id: sweet-bags
  title: Try Growing Sweet Potatoes This Year! — Maryland Grows
  resource: https://marylandgrows.umd.edu/2023/04/21/try-growing-sweet-potatoes-this-year/
- id: usu-sweet
  title: How to Grow Sweet Potatoes in Your Garden — Utah State University
  resource: https://extension.usu.edu/yardandgarden/research/sweet-potatoes-in-the-garden
- title: Grow More Sweet Potato — Alabama Cooperative Extension
  resource: https://www.aces.edu/blog/topics/lawn-garden/grow-more-sweet-potato/
  id: aces-sweet
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: warm-soil
    kind: recommendation
    statement: Plant sweet-potato slips after frost risk passes and soil reaches 65°F.
    applicability:
      conditions: Maryland planting threshold.
    evidence:
    - source_id: umd-sweet
      relation: supports
      locator: Planting; Growing and care, item 6
    quantity:
      property: planting_soil_temperature
      unit: degF
      value: 65
  - id: row-spacing
    kind: recommendation
    statement: Maryland spaces sweet-potato rows 40 inches apart.
    applicability:
      conditions: Ground planting; not bag density.
    evidence:
    - source_id: umd-sweet
      relation: supports
      locator: Planting sweet potato
    quantity:
      property: row_spacing
      unit: in
      value: 40
  - id: slip-spacing
    kind: recommendation
    statement: Maryland spaces slips 12 inches apart within rows.
    applicability:
      conditions: Ground planting; not bag density.
    evidence:
    - source_id: umd-sweet
      relation: supports
      locator: Planting sweet potato
    quantity:
      property: in_row_spacing
      unit: in
      value: 12
  - id: bag-size
    kind: recommendation
    statement: Jon Traunfeld suggests one sweet-potato plant in a 10-gallon container, including fabric
      bags.
    applicability:
      conditions: Extension recommendation; not a controlled volume trial.
    evidence:
    - source_id: sweet-bags
      relation: supports
      locator: General growing tips, container photo caption
    quantity:
      property: container_capacity
      unit: gal
      value: 10
      basis: Source nominal gallon size; one plant.
  - id: slip-depth
    kind: recommendation
    statement: Alabama Extension plants sweet-potato slips 2–3 inches deep.
    applicability:
      conditions: Home garden guidance; applied to the bag branch as an adaptation.
    evidence:
    - source_id: aces-sweet
      relation: supports
      locator: Plant
    quantity:
      property: slip_planting_depth
      unit: in
      min: 2
      max: 3
  - id: site-light
    kind: recommendation
    statement: Grow sweet potatoes in full sun.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: sweet-bags
      relation: supports
      locator: General growing tips
  relations:
  - predicate: applies_to
    target: /crops/sweet-potato.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant sweet-potato slips

Applies to [sweet potato](../crops/sweet-potato.md). Ipomoea batatas for storage roots in warm-season beds or outdoor grow bags; cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have labelled slips with healthy roots, a thermometer, water, a sunny site, and bag medium if using containers.

## Steps and source settings

1. Confirm cultivar, available warm season, and the temperature/readiness claim below. Choose full sun.[^sweet-bags]
2. Use the ground spacing or the one-plant container branch, keeping them distinct. Follow [bag setup](../systems/outdoor-grow-bags.md) for drainage.
3. Set slips using the sourced depth below; retain any cultivar-specific nursery directions and record deviations.
4. Water regularly while slips establish.[^usu-sweet]

<a id="warm-soil"></a>
Plant sweet-potato slips after frost risk passes and soil reaches 65°F.[^umd-sweet]

<a id="row-spacing"></a>
Maryland spaces sweet-potato rows 40 inches apart.[^umd-sweet]

<a id="slip-spacing"></a>
Maryland spaces slips 12 inches apart within rows.[^umd-sweet]

<a id="bag-size"></a>
Jon Traunfeld suggests one sweet-potato plant in a 10-gallon container, including fabric bags.[^sweet-bags]

<a id="slip-depth"></a>
Alabama Extension plants sweet-potato slips 2–3 inches deep.[^aces-sweet]

<a id="site-light"></a>
Grow sweet potatoes in full sun.[^sweet-bags]

## Follow-up

Record survival, new growth, planting depth, medium temperature, and actual bag dimensions. Begin [care](care-for-sweet-potato.md).

## Limits

The Maryland bag size is a starting point, not an optimum. Alabama offers a different container density; only its slip depth is adopted here.[^aces-sweet] This route begins with slips; producing slips from roots is not included. Local frost dates and cultivar duration must be checked.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umd-sweet]: [Growing Sweet Potatoes in a Home Garden — Maryland Extension](https://extension.umd.edu/resource/growing-sweet-potatoes-home-garden).
[^sweet-bags]: [Try Growing Sweet Potatoes This Year! — Maryland Grows](https://marylandgrows.umd.edu/2023/04/21/try-growing-sweet-potatoes-this-year/).
[^usu-sweet]: [How to Grow Sweet Potatoes in Your Garden — Utah State University](https://extension.usu.edu/yardandgarden/research/sweet-potatoes-in-the-garden).

[^aces-sweet]: [Grow More Sweet Potato — Alabama Cooperative Extension](https://www.aces.edu/blog/topics/lawn-garden/grow-more-sweet-potato/).
