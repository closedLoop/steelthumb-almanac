---
type: Procedure
title: Care for and investigate potatoes
description: Solanum tuberosum for edible tubers in soil and grow bags; general guidance with separate
  cultivar scope.
status: draft
sources:
- id: umn-potato
  title: Growing potatoes in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-potatoes
- id: spudnik
  title: Potatoes Grow in Bags at Project Spudnik — Maryland Grows
  resource: https://marylandgrows.umd.edu/2020/03/20/potatoes-grow-in-bags-at-project-spudnik/
- id: umd-potato
  title: Growing Potatoes in a Home Garden — Maryland Extension
  resource: https://www.extension.umd.edu/resource/growing-potatoes-home-garden
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: cover-tubers
    kind: recommendation
    statement: Keep developing potato tubers covered to prevent light-induced greening.
    applicability:
      conditions: Ground or container potatoes.
    evidence:
    - source_id: umn-potato
      relation: supports
      locator: Hilling
  - id: bag-hilling
    kind: recommendation
    statement: Spudnik adds about 4 inches of mix per filling step.
    applicability:
      conditions: Reported bag method; retain watering headspace.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 5
    quantity:
      property: medium_addition_depth
      unit: in
      value: 4
  - id: bag-fill-trigger
    kind: recommendation
    statement: Add mix when stems extend about 8 inches above it; repeat as space permits.
    applicability:
      conditions: Reported bag method; retain watering headspace.
    evidence:
    - source_id: spudnik
      relation: supports
      locator: Potato growing tips, item 5
    quantity:
      property: stem_height_above_medium
      unit: in
      value: 8
  - id: moisture
    kind: recommendation
    statement: Keep potatoes supplied with water during tuber development; both excess and shortage can
      cause disorders.
    applicability:
      conditions: Ground guidance; bags require local moisture observations.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Growing and care > Watering
  - id: beetles
    kind: descriptive
    statement: Colorado potato beetle larvae and adults can defoliate potatoes.
    applicability:
      conditions: Candidate explanation for observed feeding.
    evidence:
    - source_id: umn-potato
      relation: supports
      locator: Insects
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

# Care for and investigate potatoes

Applies to [potato](../crops/potato.md), [yukon gold potato](../cultivars/yukon-gold-potato.md), [russet potato](../crops/russet-potato.md). Solanum tuberosum for edible tubers in soil and grow bags; general guidance with separate cultivar scope.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Keep the planting record and medium/fertilizer labels. Know whether the crop is in a bed or the specified bag method.

## Steps and source settings

1. Inspect moisture, drainage, emerging tubers, and foliage. Follow the coverage and bag-filling claims below; do not bury an entire green canopy by default.
2. Use soil-test guidance for ground fertility and label directions for container feed; no universal bag dose is established.
3. Inspect feeding insects directly. For wilt, spots, or premature dieback, retain weather and moisture records and seek identification before treating it as normal maturity.
4. Use the [observation workflow](review-garden-observations.md) to track any correction.

<a id="cover-tubers"></a>
Keep developing potato tubers covered to prevent light-induced greening.[^umn-potato]

<a id="bag-hilling"></a>
Spudnik adds about 4 inches of mix per filling step.[^spudnik]

<a id="bag-fill-trigger"></a>
Add mix when stems extend about 8 inches above it; repeat as space permits.[^spudnik]

<a id="moisture"></a>
Keep potatoes supplied with water during tuber development; both excess and shortage can cause disorders.[^umd-potato]

<a id="beetles"></a>
Colorado potato beetle larvae and adults can defoliate potatoes.[^umn-potato]

## Investigate: developing tubers become exposed

These are editorial observation steps using the linked source claims.

1. Inspect after settling or irrigation for tubers visible above the medium; compare with the [coverage requirement](#cover-tubers).
2. Restore coverage using the appropriate ground/bag method and inspect again after watering. At harvest apply the [green-tuber food-use exclusions](harvest-potato.md#green-sprouts); coverage is not a claim to reverse existing greening.

## Follow-up

Record each medium addition and watering response. Inspect light exposure again after settling or irrigation, and use [harvest](harvest-potato.md) to check maturity.

## Limits

Hilling is not a promise that every buried stem section produces another crop layer. Maryland warns that potato towers usually do not work.[^umd-potato] Local disease diagnosis and cultivar-specific feeding remain unresolved.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-potato]: [Growing potatoes in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-potatoes).
[^spudnik]: [Potatoes Grow in Bags at Project Spudnik — Maryland Grows](https://marylandgrows.umd.edu/2020/03/20/potatoes-grow-in-bags-at-project-spudnik/).
[^umd-potato]: [Growing Potatoes in a Home Garden — Maryland Extension](https://www.extension.umd.edu/resource/growing-potatoes-home-garden).
