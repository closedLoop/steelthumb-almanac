---
type: Procedure
title: Care for and investigate sugar snap peas
description: Sugar snap peas for tender edible pods; outdoor beds and provisional bag culture, cultivar
  unspecified.
status: draft
sources:
- id: umn-peas
  title: Growing peas in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-peas
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: water-soil
    kind: recommendation
    statement: During dry weather, water pea soil rather than wetting the vines.
    applicability:
      conditions: Minnesota peas; bag frequency remains observation-based.
    evidence:
    - source_id: umn-peas
      relation: supports
      locator: Watering
  - id: heat
    kind: descriptive
    statement: Minnesota reports loss of flower and pod production above 85°F.
    applicability:
      conditions: Regional general guidance, not an exact threshold for every cultivar.
    evidence:
    - source_id: umn-peas
      relation: supports
      locator: Starting seeds
    quantity:
      property: air_temperature_threshold
      unit: degF
      value: 85
      basis: Source describes temperatures above this value.
  relations:
  - predicate: applies_to
    target: /crops/sugar-snap-pea.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Care for and investigate sugar snap peas

Applies to [sugar snap pea](../crops/sugar-snap-pea.md). Sugar snap peas for tender edible pods; outdoor beds and provisional bag culture, cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Keep seed identity, planting date, support arrangement, and recent moisture/weather observations.

## Steps and source settings

1. Inspect moisture and tendril attachment; apply the watering claim below. Bags use the [shared drainage principles](../systems/outdoor-grow-bags.md).
2. If growth or pods stall, compare dates and weather with the heat limitation before assuming a nutrient shortage.
3. For leaf coating, spots, or wilt, photograph both surfaces and inspect medium condition. Those symptoms alone do not establish a pathogen.
4. Keep any proposed treatment separate from the observed symptom; use the [observation workflow](review-garden-observations.md).

<a id="water-soil"></a>
During dry weather, water pea soil rather than wetting the vines.[^umn-peas]

<a id="heat"></a>
Minnesota reports loss of flower and pod production above 85°F.[^umn-peas]

## Investigate: flower or pod production stalls

These are editorial observation steps using the linked source claims.

1. Compare actual recent temperatures with the [regional heat limitation](#heat), then check soil moisture independently.
2. Use the [dry-weather watering practice](#water-soil) when needed. If heat coincides with the stall, obtain local cool-season timing guidance; observe new flowers/pods after conditions change rather than promising recovery.

## Follow-up

Record flowering, first pods, moisture, and any action. Check the same plants again and retain no-change or declining outcomes.

## Limits

No fixed bag irrigation rate, inoculant benefit, disease treatment, or fertilizer dose is established. A temperature association in a garden is not proof of causation.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umn-peas]: [Growing peas in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-peas).
