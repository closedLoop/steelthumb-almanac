---
type: Procedure
title: Harvest dwarf lemons and limes
description: Nursery citrus in movable containers, outdoors in suitable weather and sheltered during freezing
  seasons; fabric bags are a provisional adaptation.
status: draft
sources:
- id: uc-meyer
  title: Meyer Lemon — UC Master Gardeners of Sonoma County
  resource: https://ucanr.edu/site/mg-sonoma/meyer-lemon
- id: uc-citrus
  title: Growing Citrus in Pots — UC Master Gardeners
  resource: https://ucanr.edu/node/129790
- id: uf-persian
  title: Growing Tahiti Limes in the Home Landscape — UF/IFAS
  resource: https://ask.ifas.ufl.edu/publication/CH093
- id: uf-key
  title: Key Lime Growing in the Florida Home Landscape — UF/IFAS
  resource: https://ask.ifas.ufl.edu/publication/CH092
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: meyer-color
    kind: descriptive
    statement: Meyer lemons develop orange-yellow fruit.
    applicability:
      conditions: Meyer lemon, not all lemons.
    evidence:
    - source_id: uc-meyer
      relation: supports
      locator: Introduction
  - id: sample-and-clip
    kind: recommendation
    statement: Sample colored citrus fruit for readiness, then clip stems to avoid tearing supporting
      twigs.
    applicability:
      conditions: General container fruit; use the lime-specific stages below.
    evidence:
    - source_id: uc-citrus
      relation: supports
      locator: Harvesting
  - id: persian-stage
    kind: recommendation
    statement: UF harvests Persian limes dark to medium-dark green at about 45 mm diameter.
    applicability:
      conditions: Florida guidance; earlier fruit may lack juice.
    evidence:
    - source_id: uf-persian
      relation: supports
      locator: Harvest, Ripening, and Storage
    quantity:
      property: harvest_fruit_diameter
      unit: mm
      value: 45
      basis: Approximate; paired with green harvest color.
  - id: key-stage
    kind: recommendation
    statement: UF harvests mature Key limes when their peel turns yellow.
    applicability:
      conditions: Key lime branch, not a Persian harvest rule.
    evidence:
    - source_id: uf-key
      relation: supports
      locator: Harvest, Ripening, and Storage
  relations:
  - predicate: applies_to
    target: /crops/dwarf-meyer-lemon.md
  - predicate: applies_to
    target: /crops/dwarf-lime.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Harvest dwarf lemons and limes

Applies to [dwarf meyer lemon](../crops/dwarf-meyer-lemon.md), [dwarf lime](../crops/dwarf-lime.md). Nursery citrus in movable containers, outdoors in suitable weather and sheltered during freezing seasons; fabric bags are a provisional adaptation.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Confirm fruit identity and have clean pruners and labelled containers.

## Steps and source settings

1. Choose the Meyer, Persian, or Key branch below. For Meyer, color plus sampling is the editorial combination of the two sources.
2. Clip suitable fruit gently; record taste and juiciness to refine the next picking decision.
3. Separate damaged fruit and record harvest date and usable fresh mass.

<a id="meyer-color"></a>
Meyer lemons develop orange-yellow fruit.[^uc-meyer]

<a id="sample-and-clip"></a>
Sample colored citrus fruit for readiness, then clip stems to avoid tearing supporting twigs.[^uc-citrus]

<a id="persian-stage"></a>
UF harvests Persian limes dark to medium-dark green at about 45 mm diameter.[^uf-persian]

<a id="key-stage"></a>
UF harvests mature Key limes when their peel turns yellow.[^uf-key]

## Follow-up

Continue observing remaining fruit rather than assuming an entire tree ripens together. Store UF lime harvests in refrigerated polyethylene bags.[^uf-persian][^uf-key]

## Limits

UC describes fully ripe Bearss limes as yellow; UF gives a usable green harvest stage.[^uc-citrus] These are different picking stages, not evidence that every green lime is immature. Meyer storage duration and preservation recipes are not established.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^uc-meyer]: [Meyer Lemon — UC Master Gardeners of Sonoma County](https://ucanr.edu/site/mg-sonoma/meyer-lemon).
[^uc-citrus]: [Growing Citrus in Pots — UC Master Gardeners](https://ucanr.edu/node/129790).
[^uf-persian]: [Growing Tahiti Limes in the Home Landscape — UF/IFAS](https://ask.ifas.ufl.edu/publication/CH093).
[^uf-key]: [Key Lime Growing in the Florida Home Landscape — UF/IFAS](https://ask.ifas.ufl.edu/publication/CH092).
