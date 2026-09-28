---
type: Procedure
title: Prune and harvest basil
description: Plan cuts, preserve the remaining plant, and observe regrowth.
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
  claims:
  - id: canopy-limit-assumption
    kind: descriptive
    statement: The weekly pruning task limits removal to one third of the canopy per session.
    evidence:
    - source_id: tasks
      relation: supports
      locator: prune_weekly
    applicability:
      conditions: Original task; canopy measurement method unspecified.
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Prune and harvest basil

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Harvest basil leaves and shape plants in the original indoor design. The general cultivation reference also discusses outdoor plants. Readiness, cutting intensity, and flowering behavior depend on the actual plant and purpose.[^tasks][^core]

## Steps

1. Observe plant size, vigor, recent pruning, and flowering before deciding what to remove. The teaching guide's approximately six-inch height is an unreviewed heuristic, not a universal harvest threshold.[^curriculum]
2. For the task's tip-harvest method, cut above a node and retain foliage below. The original pinching task specifies about half an inch above a node; that precision has not been independently checked.[^tasks]
3. Record the amount removed. The weekly task limits removal to one third of the canopy; the batch-pesto task retains at least two leaf pairs per stem. The general reference also describes heavier cuts, so do not treat those instructions as interchangeable.[^tasks][^core]
4. For a large harvest, the batch task distributes cuts across several plants.[^tasks]
5. Handle the harvested material for the intended use, and consult the [storage review](../guides/basil-storage.md) before adopting preservation instructions.[^core]

<a id="canopy-limit-assumption"></a>
The weekly pruning task limits removal to one third of the canopy per session.[^tasks]

## Flowering and post-prune care

The original task removes flower buds when leaf production is the goal. Seed saving has a different goal and requires a [separate procedure](save-basil-seed.md). Flowering, sterility, and changes in flavor are distinct claims; the earlier text overgeneralized some of them.[^tasks][^core]

A gray-mold-prevention task proposes avoiding overhead watering for 48 hours after heavy pruning and increasing airflow. Its precise interval and efficacy remain unverified; it is not evidence that mold was prevented in practice.[^tasks]

## Follow-up

Record the cuts, remaining foliage, harvest mass if measured, date, and later regrowth or deterioration. State fresh/dry and edible/gross basis for quantities. Do not infer increased yield simply because more branches appeared.

This consolidates `pinch_apical_tip`, `prune_weekly`, `remove_flower_buds`, `gray_mold_prevention`, `harvest_basil`, and `harvest_batch_for_pesto`.[^tasks]

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^tasks]

[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^curriculum]: [The Amazing Basil Machine curriculum](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/kids_textbook.md).
