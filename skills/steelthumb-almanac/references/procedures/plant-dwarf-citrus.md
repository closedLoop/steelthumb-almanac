---
type: Procedure
title: Establish dwarf citrus in containers
description: Nursery citrus in movable containers, outdoors in suitable weather and sheltered during freezing
  seasons; fabric bags are a provisional adaptation.
status: draft
sources:
- id: uc-citrus
  title: Growing Citrus in Pots — UC Master Gardeners
  resource: https://ucanr.edu/node/129790
- id: umd-citrus
  title: Growing Dwarf Citrus — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-dwarf-citrus
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: rootstock
    kind: descriptive
    statement: Dwarfing rootstocks help keep container citrus compact.
    applicability:
      conditions: Grafted trees; not every compact tree is grafted.
    evidence:
    - source_id: uc-citrus
      relation: supports
      locator: Choosing a tree
  - id: plant-depth
    kind: recommendation
    statement: Loosen a root-bound citrus root ball and plant with its crown at the medium surface.
    applicability:
      conditions: Container transplanting.
    evidence:
    - source_id: uc-citrus
      relation: supports
      locator: Planting
  - id: pot-size
    kind: recommendation
    statement: UC suggests 14–16-inch pots for small citrus trees, enlarging when root-bound.
    applicability:
      conditions: General pot guidance, not a mature-tree fabric-bag optimum.
    evidence:
    - source_id: uc-citrus
      relation: supports
      locator: Planting > Containers
    quantity:
      property: initial_pot_size
      unit: in
      min: 14
      max: 16
      basis: Source nominal pot dimension, interpreted as diameter; depth unreported.
  - id: light
    kind: recommendation
    statement: Maryland recommends at least 6 hours of direct light daily for potted citrus.
    applicability:
      conditions: Supplement indoor light when insufficient.
    evidence:
    - source_id: umd-citrus
      relation: supports
      locator: Light
    quantity:
      property: minimum_direct_light_duration
      unit: h/d
      value: 6
  relations:
  - predicate: applies_to
    target: /crops/dwarf-meyer-lemon.md
  - predicate: applies_to
    target: /crops/dwarf-lime.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Establish dwarf citrus in containers

Applies to [dwarf meyer lemon](../crops/dwarf-meyer-lemon.md), [dwarf lime](../crops/dwarf-lime.md). Nursery citrus in movable containers, outdoors in suitable weather and sheltered during freezing seasons; fabric bags are a provisional adaptation.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have a labelled nursery tree, draining container, porous citrus medium, water, and a suitable winter location. Record rootstock if known.

## Steps and source settings

1. Confirm lemon/lime identity and inspect the root ball. Use a draining citrus or cactus potting mix.[^uc-citrus]
2. Select a movable pot using the small-tree starting point below. For a bag, record actual width, depth, and volume: no equivalence to a rigid pot is established. Apply [grow-bag setup](../systems/outdoor-grow-bags.md).
3. Follow the crown-depth instruction, fill around the root ball, and water thoroughly until drainage occurs; empty collected water.[^umd-citrus]
4. Check stability and the route to shelter before locating the tree for sunlight.

<a id="rootstock"></a>
Dwarfing rootstocks help keep container citrus compact.[^uc-citrus]

<a id="plant-depth"></a>
Loosen a root-bound citrus root ball and plant with its crown at the medium surface.[^uc-citrus]

<a id="pot-size"></a>
UC suggests 14–16-inch pots for small citrus trees, enlarging when root-bound.[^uc-citrus]

<a id="light"></a>
Maryland recommends at least 6 hours of direct light daily for potted citrus.[^umd-citrus]

## Follow-up

Record date, container measurements, identity, and crown position. Inspect establishment and proceed to [care and seasonal moves](care-for-dwarf-citrus.md).

## Limits

This procedure starts with nursery trees. It does not supply permanent-ground spacing or a minimum fabric-bag volume. An oversized bag is not automatically a suitable starter container.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^uc-citrus]: [Growing Citrus in Pots — UC Master Gardeners](https://ucanr.edu/node/129790).
[^umd-citrus]: [Growing Dwarf Citrus — Maryland Extension](https://extension.umd.edu/resource/growing-dwarf-citrus).
