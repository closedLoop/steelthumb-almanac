---
type: Procedure
title: Care for and investigate sweet potatoes
description: Ipomoea batatas for storage roots in warm-season beds or outdoor grow bags; cultivar unspecified.
status: draft
sources:
- id: umd-sweet
  title: Growing Sweet Potatoes in a Home Garden — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-sweet-potatoes-home-garden
- id: usu-sweet
  title: How to Grow Sweet Potatoes in Your Garden — Utah State University
  resource: https://extension.usu.edu/yardandgarden/research/sweet-potatoes-in-the-garden
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: water
    kind: recommendation
    statement: Supply moisture during establishment and growth without keeping sweet-potato soil saturated.
    applicability:
      conditions: Ground guidance; bag frequency depends on actual drying.
    evidence:
    - source_id: umd-sweet
      relation: supports
      locator: Watering
  - id: shallow-weeds
    kind: recommendation
    statement: Control early weeds without deep cultivation that can damage roots.
    applicability:
      conditions: Outdoor sweet potatoes.
    evidence:
    - source_id: usu-sweet
      relation: supports
      locator: Weeds
  - id: late-water
    kind: descriptive
    statement: USU associates excessive late watering with root cracking.
    applicability:
      conditions: Utah guidance, not a direction to let bags desiccate.
    evidence:
    - source_id: usu-sweet
      relation: supports
      locator: Water; Frequently Asked Questions
  relations:
  - predicate: applies_to
    target: /crops/sweet-potato.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Care for and investigate sweet potatoes

Applies to [sweet potato](../crops/sweet-potato.md). Ipomoea batatas for storage roots in warm-season beds or outdoor grow bags; cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Retain slip identity, planting date, medium/feed labels, and recent water and weather records.

## Steps and source settings

1. Monitor moisture and drainage, using the claims below. Do not copy a bed irrigation interval directly to a bag.
2. Mark the original planting location so harvest observations stay linked to the plant. Allow room for vines or document any support arrangement.
3. For holes in roots, inspect for feeding evidence. For lesions or rot, preserve photographs and seek a diagnosis; appearance alone does not identify a pest.
4. For large vines but little root yield, retain cultivar, temperature, and input history rather than assuming more nitrogen is needed.

<a id="water"></a>
Supply moisture during establishment and growth without keeping sweet-potato soil saturated.[^umd-sweet]

<a id="shallow-weeds"></a>
Control early weeds without deep cultivation that can damage roots.[^usu-sweet]

<a id="late-water"></a>
USU associates excessive late watering with root cracking.[^usu-sweet]

## Investigate: cracked harvested roots

These are editorial observation steps using the linked source claims.

1. Compare cracking with the [late-water association](#late-water) and actual rain/irrigation records. Document holes or rot separately; they are not evidence of the same cause.
2. Check for excessive water or poor drainage before changing care; retain the [non-saturated moisture practice](#water). Compare later lifted roots, or the next crop if harvest is finished; one association does not establish causation.

## Follow-up

Record new growth, water additions, any root damage, and the response to a single change where practical. Use [harvest](harvest-sweet-potato.md) before damaging cold arrives.

## Limits

The sources give regional ground fertility advice but no calibrated fabric-bag fertilizer dose. Routine vine trimming to improve root yield is not established by this collection.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^umd-sweet]: [Growing Sweet Potatoes in a Home Garden — Maryland Extension](https://extension.umd.edu/resource/growing-sweet-potatoes-home-garden).
[^usu-sweet]: [How to Grow Sweet Potatoes in Your Garden — Utah State University](https://extension.usu.edu/yardandgarden/research/sweet-potatoes-in-the-garden).
