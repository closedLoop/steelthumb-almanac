---
type: Procedure
title: Plant annual sunflowers
description: Annual Helianthus annuus for seed or flowers; ground culture and compact selections in outdoor
  bags.
status: draft
sources:
- id: umn-sunflower
  title: Sunflowers — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/sunflowers
- id: junior-packet
  title: Junior — Renee’s Garden growing instructions
  resource: https://www.reneesgarden.com/products/sunflower-container-junior
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: depth
    kind: recommendation
    statement: Direct-sow sunflowers 1 inch deep after frost danger passes.
    applicability:
      conditions: Minnesota annual sunflowers.
    evidence:
    - source_id: umn-sunflower
      relation: supports
      locator: Planting > Direct seeding
    quantity:
      property: sowing_depth
      unit: in
      value: 1
  - id: dwarf-bag
    kind: descriptive
    statement: Minnesota identifies dwarf sunflower cultivars as suitable for containers.
    applicability:
      conditions: Container suitability, not a fabric-bag seed-yield trial.
    evidence:
    - source_id: umn-sunflower
      relation: supports
      locator: Dwarf cultivars
  - id: giant-spacing
    kind: recommendation
    statement: Space giant sunflowers about 2 feet apart.
    applicability:
      conditions: Giant forms in garden soil.
    evidence:
    - source_id: umn-sunflower
      relation: supports
      locator: Giant cultivars
    quantity:
      property: plant_spacing
      unit: ft
      value: 2
  - id: site-light
    kind: recommendation
    statement: Use full sun and well-drained ground for sunflowers.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: umn-sunflower
      relation: supports
      locator: Planting
  - id: packet-container
    kind: recommendation
    statement: For Junior, Renee’s allows up to three plants in a 12-inch-diameter pot, 12–18 inches deep.
    applicability:
      conditions: Renee’s Garden Junior product instructions, inspected 2026-09-27; pot culture, not a
        comparative trial.
    evidence:
    - source_id: junior-packet
      relation: supports
      locator: Plant directly in the garden or container
  - id: packet-sowing
    kind: recommendation
    statement: Sow Junior ½ inch deep after frost risk, with days and nights above 50°F.
    applicability:
      conditions: Renee’s Garden Junior product instructions, inspected 2026-09-27; pot culture, not a
        comparative trial.
    evidence:
    - source_id: junior-packet
      relation: supports
      locator: Plant directly in the garden or container
  relations:
  - predicate: applies_to
    target: /crops/sunflower.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant annual sunflowers

Applies to [sunflower](../crops/sunflower.md). Annual Helianthus annuus for seed or flowers; ground culture and compact selections in outdoor bags.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Choose seed for the intended flower or food-seed goal; retain cultivar height and packet spacing. Have labels, water, and planned support.

## Steps and source settings

1. Choose full sun and well-drained ground.[^umn-sunflower]
2. Direct-sow using the depth below; use cultivar-specific spacing, with the giant-ground example kept separate.
3. For a bag, select a compact cultivar and follow [shared setup](../systems/outdoor-grow-bags.md). Pot suitability does not establish a minimum bag volume.
4. Label cultivar, goal, and planting date; record actual spacing.

<a id="depth"></a>
Direct-sow sunflowers 1 inch deep after frost danger passes.[^umn-sunflower]

<a id="dwarf-bag"></a>
Minnesota identifies dwarf sunflower cultivars as suitable for containers.[^umn-sunflower]

<a id="giant-spacing"></a>
Space giant sunflowers about 2 feet apart.[^umn-sunflower]

<a id="site-light"></a>
Use full sun and well-drained ground for sunflowers.[^umn-sunflower]

## Named container route: Junior

Use this branch only for the named seed product; it does not replace the general ground spacing. Start in moist potting mix and use the supplier settings below. Applying this pot route to a drained, stable fabric bag is an Almanac adaptation, not an observed fabric-bag result.

<a id="packet-container"></a>
For Junior, Renee’s allows up to three plants in a 12-inch-diameter pot, 12–18 inches deep.[^junior-packet]

<a id="packet-sowing"></a>
Sow Junior ½ inch deep after frost risk, with days and nights above 50°F.[^junior-packet]

Check drainage, moisture and stand count after emergence; retain the final spacing rather than the initial sowing density. The supplier gives a flowering route for Junior, not a food-seed yield claim.

## Follow-up

Record emergence and remaining plant count. Check whether the support plan still fits the developing canopy.

## Limits

The dwarf recommendation addresses fit, not a guarantee of large edible seed. Do not apply giant-plant ground spacing as a bag-density formula.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-sunflower]: [Sunflowers — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/sunflowers).

[^junior-packet]: [Junior — Renee’s Garden growing instructions](https://www.reneesgarden.com/products/sunflower-container-junior).
