---
type: Procedure
title: Plant garden nasturtiums
description: Garden Tropaeolum grown for edible leaves and flowers in beds or outdoor bags; cultivar unspecified.
status: draft
sources:
- id: uw-nasturtium
  title: Nasturtium, Tropaeolum species — Wisconsin Extension
  resource: https://hort.extension.wisc.edu/articles/nasturtium-tropaeolum-majus/
- id: rhs-nasturtium
  title: How to grow annual nasturtiums — RHS
  resource: https://www.rhs.org.uk/plants/nasturtiums/annual-nasturtiums/how-to-grow-annual-nasturtiums
- id: little-firebirds-packet
  title: Little Firebirds — Renee’s Garden growing instructions
  resource: https://www.reneesgarden.com/products/nasturtium-container-little-firebirds
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: sow-depth
    kind: recommendation
    statement: After frost risk passes, sow nasturtiums 0.5 inch deep.
    applicability:
      conditions: Garden Tropaeolum grown for edible leaves and flowers in beds or outdoor bags; cultivar
        unspecified.
    evidence:
    - source_id: uw-nasturtium
      relation: supports
      locator: Propagating
    quantity:
      property: sowing_depth
      unit: in
      value: 0.5
  - id: spacing
    kind: recommendation
    statement: Wisconsin recommends 10–12 inches between seeds.
    applicability:
      conditions: Direct sowing; cultivar unspecified.
    evidence:
    - source_id: uw-nasturtium
      relation: supports
      locator: Propagating
    quantity:
      property: seed_spacing
      unit: in
      min: 10
      max: 12
  - id: site
    kind: recommendation
    statement: Use a sunny, well-drained site.
    applicability:
      conditions: Garden Tropaeolum grown for edible leaves and flowers in beds or outdoor bags; cultivar
        unspecified.
    evidence:
    - source_id: uw-nasturtium
      relation: supports
      locator: Landscape Uses
  - id: bag-habit
    kind: descriptive
    statement: RHS identifies bush types for patio containers and trailing types for cascading displays.
    applicability:
      conditions: UK container guidance, not a fabric-bag trial.
    evidence:
    - source_id: rhs-nasturtium
      relation: supports
      locator: Choosing; Where to plant
  - id: packet-container
    kind: recommendation
    statement: For Little Firebirds, Renee’s specifies containers at least 8–10 inches deep and 12–15
      inches across.
    applicability:
      conditions: Renee’s Garden Little Firebirds product instructions, inspected 2026-09-27; pot culture,
        not a comparative trial.
    evidence:
    - source_id: little-firebirds-packet
      relation: supports
      locator: Easy to Start Outdoors → Container Planting
  - id: packet-sowing
    kind: recommendation
    statement: Sow Little Firebirds 1 inch deep, 1½ inches apart; thin established seedlings to 3 inches
      apart.
    applicability:
      conditions: Renee’s Garden Little Firebirds product instructions, inspected 2026-09-27; pot culture,
        not a comparative trial.
    evidence:
    - source_id: little-firebirds-packet
      relation: supports
      locator: Easy to Start Outdoors → Container Planting
  relations:
  - predicate: applies_to
    target: /crops/nasturtium.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant garden nasturtiums

Applies to [nasturtium](../crops/nasturtium.md). Garden Tropaeolum grown for edible leaves and flowers in beds or outdoor bags; cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have identified edible garden-nasturtium seed, its packet, a prepared site or bag, medium, water, and labels.

## Steps and source settings

1. Record species or cultivar, bush/trailing habit, and packet instructions.
2. Follow the site, depth, and spacing claims below for direct sowing.
3. For bags, use the [shared setup](../systems/outdoor-grow-bags.md); apply the same seed-depth starting point as an untested fabric adaptation. Preserve room for the selected habit rather than inventing a plants-per-litre rule.
4. Label, record sowing date, and begin [care](care-for-nasturtium.md).

<a id="sow-depth"></a>
After frost risk passes, sow nasturtiums 0.5 inch deep.[^uw-nasturtium]

<a id="spacing"></a>
Wisconsin recommends 10–12 inches between seeds.[^uw-nasturtium]

<a id="site"></a>
Use a sunny, well-drained site.[^uw-nasturtium]

<a id="bag-habit"></a>
RHS identifies bush types for patio containers and trailing types for cascading displays.[^rhs-nasturtium]

## Named container route: Little Firebirds

Use this branch only for the named seed product; it does not replace the general ground spacing. Start in moist potting mix and use the supplier settings below. Applying this pot route to a drained, stable fabric bag is an Almanac adaptation, not an observed fabric-bag result.

<a id="packet-container"></a>
For Little Firebirds, Renee’s specifies containers at least 8–10 inches deep and 12–15 inches across.[^little-firebirds-packet]

<a id="packet-sowing"></a>
Sow Little Firebirds 1 inch deep, 1½ inches apart; thin established seedlings to 3 inches apart.[^little-firebirds-packet]

Check drainage, moisture and stand count after emergence; retain final thinning rather than initial sowing density.

## Follow-up

Record first emergence and how many seeds establish. Compare any failures with moisture and weather records before resowing.

## Limits

No minimum bag volume or universal emergence deadline is established. A packet specific to the actual cultivar can qualify the generic spacing.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^uw-nasturtium]: [Nasturtium, Tropaeolum species — Wisconsin Extension](https://hort.extension.wisc.edu/articles/nasturtium-tropaeolum-majus/).
[^rhs-nasturtium]: [How to grow annual nasturtiums — RHS](https://www.rhs.org.uk/plants/nasturtiums/annual-nasturtiums/how-to-grow-annual-nasturtiums).

[^little-firebirds-packet]: [Little Firebirds — Renee’s Garden growing instructions](https://www.reneesgarden.com/products/nasturtium-container-little-firebirds).
