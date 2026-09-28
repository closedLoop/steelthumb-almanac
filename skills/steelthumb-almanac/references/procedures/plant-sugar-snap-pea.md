---
type: Procedure
title: Plant sugar snap peas
description: Sugar snap peas for tender edible pods; outdoor beds and provisional bag culture, cultivar
  unspecified.
status: draft
sources:
- id: umn-peas
  title: Growing peas in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-peas
- id: rhs-peas
  title: How to grow peas — RHS
  resource: https://www.rhs.org.uk/vegetables/peas/grow-your-own
- id: sugar-ann-packet
  title: Sugar Ann — Renee’s Garden growing instructions
  resource: https://www.reneesgarden.com/collections/renees-seed-packets/products/container-snap-peas-sugar-ann
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: season
    kind: recommendation
    statement: Minnesota recommends sowing when thawed soil is workable.
    applicability:
      conditions: Minnesota spring planting.
    evidence:
    - source_id: umn-peas
      relation: supports
      locator: Starting seeds
  - id: depth
    kind: recommendation
    statement: Cover pea seed with 1 inch of soil in the Minnesota method.
    applicability:
      conditions: Minnesota direct sowing.
    evidence:
    - source_id: umn-peas
      relation: supports
      locator: Starting seeds
    quantity:
      property: seed_cover_depth
      unit: in
      value: 1
  - id: spacing
    kind: recommendation
    statement: Minnesota gives 6–7 inches between seeds in a narrow trench.
    applicability:
      conditions: Single-row method, not broadcast spacing.
    evidence:
    - source_id: umn-peas
      relation: supports
      locator: Starting seeds
    quantity:
      property: seed_spacing
      unit: in
      min: 6
      max: 7
  - id: rhs-spacing
    kind: recommendation
    statement: RHS instead spaces taller peas 7.5 cm apart.
    applicability:
      conditions: UK tall-variety rows; separate method.
    evidence:
    - source_id: rhs-peas
      relation: supports
      locator: Sowing outdoors
    quantity:
      property: seed_spacing
      unit: cm
      value: 7.5
  - id: bag-selection
    kind: recommendation
    statement: RHS favors smaller pea varieties in large, well-watered containers.
    applicability:
      conditions: UK guidance particularly favoring mangetout; snap-pea adaptation is provisional.
    evidence:
    - source_id: rhs-peas
      relation: supports
      locator: Sowing outdoors in containers
  - id: support
    kind: recommendation
    statement: Provide support for vining pea varieties.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: umn-peas
      relation: supports
      locator: Starting seeds
  - id: packet-container
    kind: recommendation
    statement: For Sugar Ann, Renee’s specifies pots at least 15–18 inches across and 12 inches deep.
    applicability:
      conditions: Renee’s Garden Sugar Ann product instructions, inspected 2026-09-27; pot culture, not
        a comparative trial.
    evidence:
    - source_id: sugar-ann-packet
      relation: supports
      locator: For Containers
  - id: packet-sowing
    kind: recommendation
    statement: Sow Sugar Ann 1 inch deep and apart; thin to 3 inches apart at 2–3 inches tall.
    applicability:
      conditions: Renee’s Garden Sugar Ann product instructions, inspected 2026-09-27; pot culture, not
        a comparative trial.
    evidence:
    - source_id: sugar-ann-packet
      relation: supports
      locator: For Containers
  - id: packet-support
    kind: recommendation
    statement: Install 2–3-foot supports when planting Sugar Ann.
    applicability:
      conditions: Renee’s Garden Sugar Ann product instructions, inspected 2026-09-27; pot culture, not
        a comparative trial.
    evidence:
    - source_id: sugar-ann-packet
      relation: supports
      locator: For Containers
  relations:
  - predicate: applies_to
    target: /crops/sugar-snap-pea.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant sugar snap peas

Applies to [sugar snap pea](../crops/sugar-snap-pea.md). Sugar snap peas for tender edible pods; outdoor beds and provisional bag culture, cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have snap-pea seed, cultivar height information, a trellis if vining, labels, and drained soil or container medium.

## Steps and source settings

1. Choose a locally appropriate cool-season sowing window; the claims below preserve two regional methods without averaging them.
2. Install support for vining peas before growth needs it, as Minnesota recommends.[^umn-peas]
3. Use the Minnesota direct-sown depth and narrow-row spacing branch unless following a specific packet or regional method.
4. For bags, use [shared setup](../systems/outdoor-grow-bags.md), document actual dimensions, and prefer a compact snap selection. Use the named container branch below when that selection is chosen; no row-to-volume conversion is established.

<a id="season"></a>
Minnesota recommends sowing when thawed soil is workable.[^umn-peas]

<a id="depth"></a>
Cover pea seed with 1 inch of soil in the Minnesota method.[^umn-peas]

<a id="spacing"></a>
Minnesota gives 6–7 inches between seeds in a narrow trench.[^umn-peas]

<a id="rhs-spacing"></a>
RHS instead spaces taller peas 7.5 cm apart.[^rhs-peas]

<a id="bag-selection"></a>
RHS favors smaller pea varieties in large, well-watered containers.[^rhs-peas]

<a id="support"></a>
Provide support for vining pea varieties.[^umn-peas]

## Named container route: Sugar Ann

Use this branch only for the named seed product; it does not replace the general ground spacing. Start in moist potting mix and use the supplier settings below. Applying this pot route to a drained, stable fabric bag is an Almanac adaptation, not an observed fabric-bag result.

<a id="packet-container"></a>
For Sugar Ann, Renee’s specifies pots at least 15–18 inches across and 12 inches deep.[^sugar-ann-packet]

<a id="packet-sowing"></a>
Sow Sugar Ann 1 inch deep and apart; thin to 3 inches apart at 2–3 inches tall.[^sugar-ann-packet]

<a id="packet-support"></a>
Install 2–3-foot supports when planting Sugar Ann.[^sugar-ann-packet]

Check drainage, moisture and stand count after emergence; retain final thinning rather than initial sowing density.

## Follow-up

Record emergence and stand count, and check support stability as tendrils develop. Begin [care](care-for-sugar-snap-pea.md).

## Limits

RHS container preference is not a trial of all snap cultivars. Do not transplant its UK calendar months to a different climate. No optimum bag count or volume is claimed.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-peas]: [Growing peas in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-peas).
[^rhs-peas]: [How to grow peas — RHS](https://www.rhs.org.uk/vegetables/peas/grow-your-own).

[^sugar-ann-packet]: [Sugar Ann — Renee’s Garden growing instructions](https://www.reneesgarden.com/collections/renees-seed-packets/products/container-snap-peas-sugar-ann).
