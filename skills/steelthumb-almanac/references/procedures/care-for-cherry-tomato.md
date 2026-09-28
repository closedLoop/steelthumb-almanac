---
type: Procedure
title: Care for and investigate cherry tomatoes
description: Cherry-fruited Solanum lycopersicum for fresh fruit; ground and outdoor bag growing, cultivar
  unspecified.
status: draft
sources:
- id: umn-tomato
  title: Growing tomatoes in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-tomatoes
- id: rhs-tomato
  title: How to grow tomatoes — RHS
  resource: https://www.rhs.org.uk/vegetables/tomatoes/grow-your-own
- id: umd-ber
  title: Blossom End Rot on Vegetables — Maryland Extension
  resource: https://extension.umd.edu/resource/blossom-end-rot-vegetables
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: moisture
    kind: recommendation
    statement: Keep tomato-root-zone moisture consistent and water the soil thoroughly rather than sprinkling
      leaves.
    applicability:
      conditions: Cherry-fruited Solanum lycopersicum for fresh fruit; ground and outdoor bag growing,
        cultivar unspecified.
    evidence:
    - source_id: umn-tomato
      relation: supports
      locator: Watering
  - id: feeding
    kind: recommendation
    statement: RHS feeds container tomatoes every 10–14 days with high-potassium liquid fertilizer after
      fruit begins swelling.
    applicability:
      conditions: UK container guidance; dilution remains product-specific.
    evidence:
    - source_id: rhs-tomato
      relation: supports
      locator: Feeding
    quantity:
      property: feeding_interval
      unit: d
      min: 10
      max: 14
      basis: After first fruit swelling; product label controls dilution.
  - id: ber
    kind: descriptive
    statement: Blossom-end rot is less common in cherry tomatoes but can occur with fruit-calcium supply
      problems and water stress.
    applicability:
      conditions: A possibility, not an automatic diagnosis.
    evidence:
    - source_id: umd-ber
      relation: supports
      locator: Key points
  relations:
  - predicate: applies_to
    target: /crops/cherry-tomato.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Care for and investigate cherry tomatoes

Applies to [cherry tomato](../crops/cherry-tomato.md). Cherry-fruited Solanum lycopersicum for fresh fruit; ground and outdoor bag growing, cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Keep growth habit, medium/feed labels, watering history, and photographs of any concern.

## Steps and source settings

1. Check bag moisture and supports as plants grow. Apply the moisture claim below.
2. For container feeding, use the RHS stage/interval as guidance while following the product’s dilution instructions and accounting for existing feed.
3. Do not apply a cordon-pruning recipe to an unidentified dwarf or determinate plant; this collection does not prescribe routine sucker removal.
4. For fruit-end lesions, inspect their location and check moisture history. For leaf spots, document progression and seek identification; a spot is not a confirmed blight diagnosis.

<a id="moisture"></a>
Keep tomato-root-zone moisture consistent and water the soil thoroughly rather than sprinkling leaves.[^umn-tomato]

<a id="feeding"></a>
RHS feeds container tomatoes every 10–14 days with high-potassium liquid fertilizer after fruit begins swelling.[^rhs-tomato]

<a id="ber"></a>
Blossom-end rot is less common in cherry tomatoes but can occur with fruit-calcium supply problems and water stress.[^umd-ber]

## Investigate: fruit-end lesion

These are editorial observation steps using the linked source claims.

1. Compare the lesion’s position with the [blossom-end-rot candidate](#ber); inspect root-zone moisture and recent irrigation records separately.
2. If moisture has fluctuated, restore the [consistent-moisture practice](#moisture) and compare later fruit. Other lesion patterns need identification before treatment.

## Follow-up

Compare later fruit and new leaves after any care change. Record losses and no improvement as well as recovery, following the [observation workflow](review-garden-observations.md).

## Limits

No calcium or Epsom-salt addition follows automatically from a symptom. No fertilizer dose, pesticide treatment, or tomato pruning optimum is established for every cherry cultivar.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-tomato]: [Growing tomatoes in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-tomatoes).
[^rhs-tomato]: [How to grow tomatoes — RHS](https://www.rhs.org.uk/vegetables/tomatoes/grow-your-own).
[^umd-ber]: [Blossom End Rot on Vegetables — Maryland Extension](https://extension.umd.edu/resource/blossom-end-rot-vegetables).
