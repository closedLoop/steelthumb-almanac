---
type: Procedure
title: Care for and investigate nasturtiums
description: Garden Tropaeolum grown for edible leaves and flowers in beds or outdoor bags; cultivar unspecified.
status: draft
sources:
- id: rhs-nasturtium
  title: How to grow annual nasturtiums — RHS
  resource: https://www.rhs.org.uk/plants/nasturtiums/annual-nasturtiums/how-to-grow-annual-nasturtiums
- id: uw-nasturtium
  title: Nasturtium, Tropaeolum species — Wisconsin Extension
  resource: https://hort.extension.wisc.edu/articles/nasturtium-tropaeolum-majus/
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: watering
    kind: recommendation
    statement: RHS advises regular watering for container nasturtiums and extra attention to young plants.
    applicability:
      conditions: UK ground and container guidance.
    evidence:
    - source_id: rhs-nasturtium
      relation: supports
      locator: Ongoing care > Watering
  - id: ground-feed
    kind: descriptive
    statement: Wisconsin cautions that heavy feeding favors foliage over flowers.
    applicability:
      conditions: Flower production; not a container nutrient-depletion trial.
    evidence:
    - source_id: uw-nasturtium
      relation: supports
      locator: Propagating
  - id: container-feed
    kind: recommendation
    statement: RHS advises slow-release fertilizer at container planting, while borders need no additional
      feed.
    applicability:
      conditions: UK containers versus borders.
    evidence:
    - source_id: rhs-nasturtium
      relation: supports
      locator: Ongoing care > Feeding
  - id: caterpillars
    kind: recommendation
    statement: Inspect leaf undersides for cabbage-white eggs and caterpillars; hand removal is an RHS
      option.
    applicability:
      conditions: UK nasturtiums; identify the organism before intervening.
    evidence:
    - source_id: rhs-nasturtium
      relation: supports
      locator: Problems
  relations:
  - predicate: applies_to
    target: /crops/nasturtium.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Care for and investigate nasturtiums

Applies to [nasturtium](../crops/nasturtium.md). Garden Tropaeolum grown for edible leaves and flowers in beds or outdoor bags; cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Keep the planting record and medium/feed labels; distinguish a leaf crop from a flower-production goal.

## Steps and source settings

1. Observe moisture, growth, and flowering before changing care. For bags, use [container setup](../systems/outdoor-grow-bags.md).
2. Read the feeding claims together: they apply to different media and do not establish an optimal bag dose. Account for feed already in the mix and retain its label instructions.
3. Investigate leaf damage by looking for the organism; record holes separately from the proposed cause.

<a id="watering"></a>
RHS advises regular watering for container nasturtiums and extra attention to young plants.[^rhs-nasturtium]

<a id="ground-feed"></a>
Wisconsin cautions that heavy feeding favors foliage over flowers.[^uw-nasturtium]

<a id="container-feed"></a>
RHS advises slow-release fertilizer at container planting, while borders need no additional feed.[^rhs-nasturtium]

<a id="caterpillars"></a>
Inspect leaf undersides for cabbage-white eggs and caterpillars; hand removal is an RHS option.[^rhs-nasturtium]

## Investigate: chewed leaves

These are editorial observation steps using the linked source claims.

1. Turn leaves over and look for the [eggs or caterpillars](#caterpillars) named by RHS. Holes alone do not establish the culprit.
2. If identified, use the source’s hand-removal option; revisit leaf undersides and new damage. If none are found, retain the unknown cause rather than treating by guesswork.

## Follow-up

Record irrigation and any feed change. Revisit affected leaves and new growth at the next inspection. Use the [observation workflow](review-garden-observations.md) if symptoms continue.

## Limits

Lush foliage alone does not diagnose excess fertilizer. A pest-control benefit to neighboring crops has not been established here; do not plant nasturtiums as a proven pesticide substitute.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^rhs-nasturtium]: [How to grow annual nasturtiums — RHS](https://www.rhs.org.uk/plants/nasturtiums/annual-nasturtiums/how-to-grow-annual-nasturtiums).
[^uw-nasturtium]: [Nasturtium, Tropaeolum species — Wisconsin Extension](https://hort.extension.wisc.edu/articles/nasturtium-tropaeolum-majus/).
