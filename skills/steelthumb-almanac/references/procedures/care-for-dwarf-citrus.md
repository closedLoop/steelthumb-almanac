---
type: Procedure
title: Care for and investigate dwarf citrus
description: Nursery citrus in movable containers, outdoors in suitable weather and sheltered during freezing
  seasons; fabric bags are a provisional adaptation.
status: draft
sources:
- id: umd-citrus
  title: Growing Dwarf Citrus — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-dwarf-citrus
- id: uc-meyer
  title: Meyer Lemon — UC Master Gardeners of Sonoma County
  resource: https://ucanr.edu/site/mg-sonoma/meyer-lemon
- id: umn-citrus
  title: Growing citrus indoors — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-citrus-indoors
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: seasonal-move
    kind: recommendation
    statement: Move citrus outside after frost risk passes and indoors before frost; change light exposure
      gradually.
    applicability:
      conditions: Maryland seasonal container method.
    evidence:
    - source_id: umd-citrus
      relation: supports
      locator: Light
  - id: water
    kind: recommendation
    statement: Let the medium surface dry between waterings, then water thoroughly and drain.
    applicability:
      conditions: Meyer container guidance; avoid a fixed calendar.
    evidence:
    - source_id: umd-citrus
      relation: supports
      locator: Water
  - id: feed
    kind: recommendation
    statement: Feed potted citrus during active growth using the fertilizer label; stop for winter.
    applicability:
      conditions: Seasonal indoor/outdoor growing; account for existing medium nutrients.
    evidence:
    - source_id: umd-citrus
      relation: supports
      locator: Soil & fertilizer
  - id: pests
    kind: recommendation
    statement: Scale, whiteflies, and spider mites are common indoor citrus pests; inspect and wash both
      leaf surfaces.
    applicability:
      conditions: Pest identification still required.
    evidence:
    - source_id: umn-citrus
      relation: supports
      locator: Watch for pests
  - id: pollination
    kind: recommendation
    statement: Gently shake or flick indoor citrus flowers to help transfer pollen.
    applicability:
      conditions: Potential pollination limitation, not a fruit-set guarantee.
    evidence:
    - source_id: umn-citrus
      relation: supports
      locator: Pollinate for fruit
  - id: leaf-drop
    kind: descriptive
    statement: Citrus leaf drop can follow moisture, temperature, or indoor-transition stress.
    applicability:
      conditions: Candidate causes, not a diagnosis.
    evidence:
    - source_id: umd-citrus
      relation: supports
      locator: Common problems > Leaves drop off
  relations:
  - predicate: applies_to
    target: /crops/dwarf-meyer-lemon.md
  - predicate: applies_to
    target: /crops/dwarf-lime.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Care for and investigate dwarf citrus

Applies to [dwarf meyer lemon](../crops/dwarf-meyer-lemon.md), [dwarf lime](../crops/dwarf-lime.md). Nursery citrus in movable containers, outdoors in suitable weather and sheltered during freezing seasons; fabric bags are a provisional adaptation.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Keep the tree label, rootstock, medium/feed records, and a winter shelter plan. Have a hand lens or close-up camera for symptoms.

## Steps and source settings

1. Check moisture and drainage; use the source branches below. Bag drying must be observed, not inferred from a rigid-pot calendar.
2. Inspect foliage before a seasonal move. Gradually adjust light and maintain adequate indoor light as specified in [establishment](plant-dwarf-citrus.md).
3. Feed by label during growth. Remove shoots originating below a known graft.[^uc-meyer]
4. If leaves drop, record recent moves, moisture, and temperature. Inspect visible insects separately before choosing treatment.
5. If flowers fail to set, try the pollen-transfer step and record subsequent fruit retention.

<a id="seasonal-move"></a>
Move citrus outside after frost risk passes and indoors before frost; change light exposure gradually.[^umd-citrus]

<a id="water"></a>
Let the medium surface dry between waterings, then water thoroughly and drain.[^umd-citrus]

<a id="feed"></a>
Feed potted citrus during active growth using the fertilizer label; stop for winter.[^umd-citrus]

<a id="pests"></a>
Scale, whiteflies, and spider mites are common indoor citrus pests; inspect and wash both leaf surfaces.[^umn-citrus]

<a id="pollination"></a>
Gently shake or flick indoor citrus flowers to help transfer pollen.[^umn-citrus]

<a id="leaf-drop"></a>
Citrus leaf drop can follow moisture, temperature, or indoor-transition stress.[^umd-citrus]

## Investigate: leaf drop after a seasonal move

These are editorial observation steps using the linked source claims.

1. Compare timing of the move, light change, temperature, and measured medium moisture with the [stress candidates](#leaf-drop); inspect separately for [pests](#pests).
2. Correct an observed mismatch using [gradual transitions](#seasonal-move) and [watering guidance](#water); observe retention/new growth. Persistent decline or unidentified pests need local diagnosis.

## Follow-up

Record losses, new growth, pests found, and response to changes. Use [harvest](harvest-dwarf-citrus.md) when fruit develops; seek local diagnosis for persistent decline.

## Limits

Meyer-specific watering guidance is used as the shared container starting point; verify its suitability for the actual lime and medium. No pesticide rate or automatic nutrient treatment follows from yellow leaves. Long-term bag root management remains untested.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umd-citrus]: [Growing Dwarf Citrus — Maryland Extension](https://extension.umd.edu/resource/growing-dwarf-citrus).
[^uc-meyer]: [Meyer Lemon — UC Master Gardeners of Sonoma County](https://ucanr.edu/site/mg-sonoma/meyer-lemon).
[^umn-citrus]: [Growing citrus indoors — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/growing-citrus-indoors).
