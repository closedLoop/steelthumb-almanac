---
type: Procedure
title: Harvest culinary mint
description: Culinary spearmint and peppermint for leaves; identified plants in beds or outdoor containers.
status: draft
sources:
- id: usu-mint
  title: How to Grow Mint in Your Garden — Utah State University
  resource: https://extension.usu.edu/yardandgarden/research/mint-in-the-garden
- id: rhs-mint
  title: How to grow mint — RHS
  resource: https://www.rhs.org.uk/herbs/mint/grow-your-own
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: harvest-start
    kind: recommendation
    statement: USU starts fresh mint harvest when plants reach 3–4 inches tall, cutting leaves and stems
      with scissors.
    applicability:
      conditions: Utah guidance; established culinary plants.
    evidence:
    - source_id: usu-mint
      relation: supports
      locator: How to Harvest and Store Mint
    quantity:
      property: plant_height_at_first_harvest
      unit: in
      min: 3
      max: 4
  - id: young-leaves
    kind: recommendation
    statement: RHS recommends regular young-leaf picking to keep mint compact.
    applicability:
      conditions: Culinary mint in UK gardening.
    evidence:
    - source_id: rhs-mint
      relation: supports
      locator: Plant Care
  relations:
  - predicate: applies_to
    target: /crops/mint.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Harvest culinary mint

Applies to [mint](../crops/mint.md). Culinary spearmint and peppermint for leaves; identified plants in beds or outdoor containers.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Confirm culinary identity and treatment history; have clean scissors and a harvest container.

## Steps and source settings

1. Use the readiness claim below for first picking.
2. Select young growth, clip the required material, and record whether this was a light picking or a heavier cut.
3. Keep divisions for propagation labelled separately from food harvest.

<a id="harvest-start"></a>
USU starts fresh mint harvest when plants reach 3–4 inches tall, cutting leaves and stems with scissors.[^usu-mint]

<a id="young-leaves"></a>
RHS recommends regular young-leaf picking to keep mint compact.[^rhs-mint]

## Follow-up

Record harvested fresh mass if useful, remaining growth, and subsequent recovery. Reassess weak plants using [care](care-for-mint.md) before another cut.

## Limits

No medicinal dose, oil-extraction procedure, quantified harvest fraction, or storage/preservation guarantee is supplied.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^usu-mint]: [How to Grow Mint in Your Garden — Utah State University](https://extension.usu.edu/yardandgarden/research/mint-in-the-garden).
[^rhs-mint]: [How to grow mint — RHS](https://www.rhs.org.uk/herbs/mint/grow-your-own).
