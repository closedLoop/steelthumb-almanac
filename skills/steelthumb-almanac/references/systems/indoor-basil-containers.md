---
type: GrowingSystem
title: Indoor basil in containers
description: Rockwool starts, container plants, water cuttings, and the limits of the original design.
status: draft
sources:
- id: design
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md
  title: SteelThumb procedural design
- id: curriculum
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md
  title: The Amazing Basil Machine curriculum
- id: environment
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/environment/SPEC.md
  title: SteelThumb environment specification
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
---

# Indoor basil in containers

The earlier project proposed a nursery of rockwool starts, established basil in draining containers, water-rooted replacement cuttings, timed LED lighting, and gentle airflow. It is a reusable design description, not a record of a deployed garden or successful trial.[^design][^curriculum]

## Components and transitions

1. [Start seedlings in rockwool](../procedures/sow-basil-in-rockwool.md).
2. [Transplant established starts](../procedures/transplant-basil.md) into containers.
3. [Maintain plants](../procedures/care-for-container-basil.md) and [harvest](../procedures/harvest-basil.md).
4. [Start cuttings](../procedures/propagate-basil.md) when replacement plants are needed.
5. Observe the results and change the plan in response to actual growth.

The original nursery/producer/retiree labels describe roles in this design, not botanical lifecycle stages. A weekly replacement quota or retirement after 4–6 months is a planning assumption from the curriculum, not evidence of optimal productivity.[^curriculum]

## Unresolved assumptions

- Cultivar, lamp model/output, fertilizer formulation, and several measurement methods are unspecified.
- Lighting duration and distance are maintained in the [rockwool procedure](../procedures/sow-basil-in-rockwool.md); neither alone establishes light delivered to leaves.
- Container medium and size are maintained in [transplanting](../procedures/transplant-basil.md).
- Conflicting feeding schedules are preserved in [container care](../procedures/care-for-container-basil.md).
- Conflicting cutting-root thresholds are preserved in [propagation](../procedures/propagate-basil.md).

Simulator state-space bounds are software limits, not biological tolerance ranges.[^environment] Robot guards, execution policies, and training success criteria remain in SteelThumb. No controller or experiment schema is defined by this document.

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^design]

[^design]: [SteelThumb procedural design](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md).
[^curriculum]: [The Amazing Basil Machine curriculum](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md).
[^environment]: [SteelThumb environment specification](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/environment/SPEC.md).
