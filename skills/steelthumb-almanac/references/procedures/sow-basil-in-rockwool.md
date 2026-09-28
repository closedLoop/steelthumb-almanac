---
type: Procedure
title: Start basil in rockwool
description: Complete the original indoor sowing sequence while exposing unverified settings.
status: draft
sources:
- id: tasks
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  title: SteelThumb task instruction templates
- id: design
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md
  title: SteelThumb procedural design
- id: curriculum
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md
  title: The Amazing Basil Machine curriculum
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  claims:
  - id: conditioning-assumption
    kind: descriptive
    statement: The original task specifies conditioning rockwool in pH 5.5–6.0 water for 15–30 minutes.
    evidence:
    - source_id: tasks
      relation: supports
      locator: condition_rockwool
    applicability:
      conditions: Original task assumption; soak water, unspecified rockwool product.
  relations:
  - predicate: applies_to
    target: /crops/basil.md
  - predicate: applies_to
    target: /systems/indoor-basil-containers.md
---

# Start basil in rockwool

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Start indoor basil seedlings in rockwool under the original project's light-and-airflow arrangement. Cultivar, lamp output, and rockwool product are unspecified. The numeric settings below are project assumptions requiring product/source review.[^tasks][^design]

## Prerequisites

Seeds, labeled cubes, a draining tray, a cover where appropriate, water, a suitable pH measurement method, and the specified lighting arrangement. Confirm the actual growing-medium and equipment instructions before selecting settings.

## Steps

1. Prepare the cubes. The task catalog specifies soak water at pH 5.5–6.0 for 15–30 minutes, then draining; this is a conditioning assumption, not a soil pH target.[^tasks]
2. Arrange cubes in a tray and configure the cover, lighting, and gentle airflow. The original setup uses about 6 inches (15 cm) lamp distance and a 14-hour-on/10-hour-off schedule; lamp output was not documented.[^tasks]
3. Place 1–2 seeds per cube, cover lightly as described by the chosen product/method, moisten, and label. The original task opens the dome vent roughly 20–40%; that percentage is equipment-specific and unvalidated.[^tasks]
4. Check moisture and condensation daily. The old task removes the dome at cotyledon emergence; preserve what actually happens rather than treating elapsed days as proof of readiness.[^tasks]
5. Thin excess seedlings and proceed to [transplanting](transplant-basil.md) after documenting root and leaf development.[^tasks][^curriculum]

<a id="conditioning-assumption"></a>
The original task specifies conditioning rockwool in pH 5.5–6.0 water for 15–30 minutes.[^tasks]

## Follow-up and gaps

Record seed count, emergence, losses, moisture, actual light settings, and dates. The teaching guide's 70–80°F starting range and 5–10-day emergence expectation are unreviewed assertions, not verified results.[^curriculum] Distance and photoperiod cannot substitute for missing light-output information. Do not invent a cultivar, lamp intensity, or concentration.

The steps consolidate `condition_rockwool`, `setup_germination_tray`, `sow_basil_seeds`, `daily_seedling_check`, `remove_humidity_dome`, and `thin_seedlings` from the task catalog.[^tasks]

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^tasks]

[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
[^design]: [SteelThumb procedural design](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md).
[^curriculum]: [The Amazing Basil Machine curriculum](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md).
