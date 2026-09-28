---
type: Procedure
title: Propagate basil from cuttings
description: Take, root, and follow up basil cuttings with source-specific readiness criteria.
status: draft
sources:
- id: core
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md
  title: SteelThumb basil cultivation reference
- id: tasks
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  title: SteelThumb task instruction templates
- id: propagation
  resource: https://gardening.org/propagate-basil/
  title: 7 Ways to Propagate Basil — Gardening.org
- id: design
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md
  title: SteelThumb procedural design
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  claims:
  - id: roots-design-threshold
    kind: descriptive
    statement: The procedural design section 5 uses roots of at least 2 cm.
    evidence:
    - source_id: design
      relation: supports
      locator: §5
    applicability:
      conditions: Original readiness assumption.
    quantity:
      property: root_length_threshold
      value: 2
      unit: cm
  - id: roots-task-threshold
    kind: descriptive
    statement: The task uses roughly 1–2 inches of roots before transplanting.
    evidence:
    - source_id: tasks
      relation: supports
      locator: root_cutting_in_water
    applicability:
      conditions: Original readiness assumption.
    quantity:
      property: root_length_threshold
      min: 1
      max: 2
      unit: in
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Propagate basil from cuttings

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Produce new basil plants from cuttings. The earlier reference describes water and growing-medium methods; the indoor task catalog uses water. Cultivar and actual success rate are unspecified.[^core][^tasks]

## Prerequisites

Identify the parent plant and its condition, label the cuttings, choose the rooting method, and record the source procedure revision. The original reference discusses cuttings as a way to retain a chosen selection; that is not evidence that a diseased or unsuitable parent is appropriate.[^core]

## Steps

1. Select an appropriate stem and record its condition. The task proposes a nonflowering stem 4–6 inches long, cut below a node; the general reference describes about four inches.[^tasks][^propagation]
2. Remove leaves that would sit below the water line. Place the stem in a clean container of water for the water-rooting method.[^tasks][^propagation]
3. Maintain and observe the cutting. The task calls for replacing water every 2–3 days; record the actual interval, light, temperature if known, and any decay.[^tasks]
4. Inspect root development and choose a documented readiness criterion. The earlier sources disagree; see below.[^design][^tasks]
5. Move ready cuttings using [transplanting](transplant-basil.md) and follow establishment after the move. Visible roots alone do not establish successful establishment in soil.[^tasks]

## Rooting readiness conflict

<a id="roots-design-threshold"></a>
The procedural design's section 5 uses roots of at least 2 cm.[^design]

<a id="roots-task-threshold"></a>
The task and procedural design's section 6.4 instead use roughly 1–2 inches.[^tasks][^design]

Keep both as source-specific assumptions. They are not equivalent unit conversions, and this reorganization does not select an optimal root length.

## Alternative: rooting in growing medium

The general reference also describes inserting a prepared cutting into moist medium and maintaining suitable moisture/humidity. It mentions optional rooting hormone, but supplies no product-specific necessity or outcome comparison here. Keep the method distinct from the water-rooting steps and record what was actually used.[^core][^propagation]

## Follow-up

Record number of cuttings, parent identity, start date, root observations, losses, transplant date, and later establishment. Include unsuccessful and pending cuttings. Multiple cuttings in one container are not necessarily independent attempts. The earlier week-or-two rooting expectations are not measured outcomes from this collection.

This consolidates `take_basil_cutting`, `root_cutting_in_water`, and the propagation portion of `end_of_season_cuttings`. It links to the complete transplant procedure for potting and recovery.[^tasks]

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^tasks]

[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
[^propagation]: [7 Ways to Propagate Basil — Gardening.org](https://gardening.org/propagate-basil/).
[^design]: [SteelThumb procedural design](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md).
