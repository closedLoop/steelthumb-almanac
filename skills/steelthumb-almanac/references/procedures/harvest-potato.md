---
type: Procedure
title: Harvest and store potatoes
description: Solanum tuberosum for edible tubers in soil and grow bags; general guidance with separate
  cultivar scope.
status: draft
sources:
- id: isu-potato
  title: Growing Potatoes in the Home Garden — Iowa State Extension
  resource: https://yardandgarden.extension.iastate.edu/how-to/growing-potatoes-home-garden
- id: umd-potato
  title: Growing Potatoes in a Home Garden — Maryland Extension
  resource: https://www.extension.umd.edu/resource/growing-potatoes-home-garden
- id: umn-potato
  title: Growing potatoes in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-potatoes
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: mature-skin
    kind: recommendation
    statement: For storage, wait for vine dieback and skins that resist rubbing off.
    applicability:
      conditions: Mature potato harvest; investigate premature decline.
    evidence:
    - source_id: isu-potato
      relation: supports
      locator: Harvest
  - id: cure-temperature
    kind: recommendation
    statement: Maryland cures potatoes at 50–60°F and high humidity.
    applicability:
      conditions: Postharvest curing; distinct from storage.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Storing potatoes
    quantity:
      property: curing_temperature
      unit: degF
      min: 50
      max: 60
  - id: cure-duration
    kind: recommendation
    statement: Maintain that potato cure for 10–14 days.
    applicability:
      conditions: Postharvest curing; distinct from storage.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Storing potatoes
    quantity:
      property: curing_duration
      unit: d
      min: 10
      max: 14
  - id: storage
    kind: recommendation
    statement: Maryland stores cured potatoes dark and ventilated at 40–50°F.
    applicability:
      conditions: Post-curing tubers.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Storing potatoes
    quantity:
      property: storage_temperature
      unit: degF
      min: 40
      max: 50
  - id: storage-humidity
    kind: recommendation
    statement: Maryland specifies about 90% relative humidity for potato storage.
    applicability:
      conditions: Post-curing tubers.
    evidence:
    - source_id: umd-potato
      relation: supports
      locator: Storing potatoes
    quantity:
      property: storage_relative_humidity
      unit: '%'
      value: 90
  - id: green-sprouts
    kind: recommendation
    statement: Do not eat potato sprouts or extensively green potatoes; remove smaller green areas before
      cooking.
    applicability:
      conditions: Food tubers, not planting material.
    evidence:
    - source_id: umn-potato
      relation: supports
      locator: Storage
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

# Harvest and store potatoes

Applies to [potato](../crops/potato.md), [yukon gold potato](../cultivars/yukon-gold-potato.md), [russet potato](../crops/russet-potato.md). Solanum tuberosum for edible tubers in soil and grow bags; general guidance with separate cultivar scope.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have harvest containers, a fork for beds, a contained sorting surface for bags, and a dark ventilated storage location. Measure conditions if attempting the curing settings.

## Steps and source settings

1. Check readiness before lifting; a calendar or flower alone does not prove storage maturity.
2. Loosen bed soil or empty a bag onto the sorting surface, handling tubers gently. Sort damaged material separately.
3. Follow the curing and storage claims below; record actual temperature and humidity rather than assuming a room meets them.
4. Keep planting stock separate from edible tubers and apply the food-use exclusions.

<a id="mature-skin"></a>
For storage, wait for vine dieback and skins that resist rubbing off.[^isu-potato]

<a id="cure-temperature"></a>
Maryland cures potatoes at 50–60°F and high humidity.[^umd-potato]

<a id="cure-duration"></a>
Maintain that potato cure for 10–14 days.[^umd-potato]

<a id="storage"></a>
Maryland stores cured potatoes dark and ventilated at 40–50°F.[^umd-potato]

<a id="storage-humidity"></a>
Maryland specifies about 90% relative humidity for potato storage.[^umd-potato]

<a id="green-sprouts"></a>
Do not eat potato sprouts or extensively green potatoes; remove smaller green areas before cooking.[^umn-potato]

## Follow-up

Inspect stored tubers for deterioration and record losses. Record harvested fresh tuber mass and retained edible mass separately, with cultivar and bag dimensions.

## Limits

No storage-life guarantee, canning recipe, or bag-yield forecast is provided. Minnesota gives a cooler general storage range but warmer storage for frying.[^umn-potato] The Maryland branch is retained as one coherent method rather than averaging those ranges.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^isu-potato]: [Growing Potatoes in the Home Garden — Iowa State Extension](https://yardandgarden.extension.iastate.edu/how-to/growing-potatoes-home-garden).
[^umd-potato]: [Growing Potatoes in a Home Garden — Maryland Extension](https://www.extension.umd.edu/resource/growing-potatoes-home-garden).
[^umn-potato]: [Growing potatoes in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-potatoes).
