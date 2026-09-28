---
type: Procedure
title: Transplant basil
description: Move seedlings or rooted cuttings while recording readiness and establishment.
status: draft
sources:
- id: tasks
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  title: SteelThumb task instruction templates
- id: core
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md
  title: SteelThumb basil cultivation reference
- id: curriculum
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md
  title: The Amazing Basil Machine curriculum
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Transplant basil

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Move basil seedlings or rooted cuttings to a growing container or bed. The rockwool-to-pot sequence comes from the original indoor design; outdoor acclimation comes from the general cultivation reference. Keep those contexts distinct.[^tasks][^core]

## Prerequisites

Record the starting medium, plant/cutting identity, destination, drainage, and observed readiness. The curriculum uses two pairs of true leaves and visible roots for seedlings. Cutting readiness has conflicting thresholds in [propagation](propagate-basil.md). Neither is a validated universal transplant rule.[^curriculum]

## Steps

1. Choose an appropriate destination and record its size and medium. The indoor task assumes a 6-inch pot and 80% soil/20% perlite; the proportion basis and meaning of “soil” were unspecified.[^tasks]
2. Make space for the root mass. The rockwool task keeps the whole cube intact, seats it at cube height, and backfills gently.[^tasks]
3. Water as required by the chosen medium and drain excess. Record the amount if measured.[^tasks]
4. For outdoor moves, gradually acclimate plants to the new conditions; the general guide describes approximately a week of hardening off, without a universal schedule.[^core]
5. Check establishment and new growth. The indoor task schedules an initial check after 10–14 days and defers feeding; feeding decisions remain subject to the [unresolved schedules](care-for-container-basil.md).[^tasks]

## Follow-up and disputed details

Record leaf/root condition before moving, signs of wilting afterward, recovery, new growth, and losses. A temporary humidity cover for 24–48 hours is an unreviewed task suggestion, not a routine requirement for every transplant.[^tasks] Store the actual duration and conditions if it was used.

This consolidates `transplant_cube_to_pot`, `early_establishment_check`, `pot_up_rooted_cutting`, and `humidity_tent_for_transplant`. The general guide's different container-size advice is retained in [growing conditions](../guides/basil-growing-conditions.md).[^tasks]

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^tasks]

[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^curriculum]: [The Amazing Basil Machine curriculum](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md).
