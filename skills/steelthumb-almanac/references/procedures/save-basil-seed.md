---
type: Procedure
title: Save basil seed and plan seasonal continuity
description: Separate seed collection from vegetative replacement and retain identity uncertainty.
status: draft
sources:
- id: core
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md
  title: SteelThumb basil cultivation reference
- id: tasks
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  title: SteelThumb task instruction templates
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Save basil seed and plan seasonal continuity

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Collect seed from an identified basil plant where seed saving is appropriate. The earlier reference also proposes overwintering or taking cuttings for continuity. These are different propagation routes with different identity implications.[^core]

## Steps

1. Identify the plant and objective. Determine whether the selection produces usable seed and whether maintaining that selection is important. The original guide distinguishes seed saving from propagating selected plants by cuttings.[^core]
2. For seed collection, select plants and allow flowering rather than applying the leaf-production bud-removal routine.[^core]
3. Observe flower/seed-head development, collect mature dry material, and separate seed from debris using the method described by a suitable source.[^core]
4. Dry and store seed under documented conditions, labeling parent identity, collection date, and any uncertainty about crossing.[^core]
5. Record later germination and resulting plant traits rather than assuming identity or viability from the label alone.

## Continuity alternatives

The earlier guide proposes moving plants indoors or taking cuttings before cold weather. Use [propagation](propagate-basil.md) for the latter and document parent condition. The task `end_of_season_cuttings` proposes 4–6 cuttings and disposal of remaining material according to health status; neither number nor disposal choice is a demonstrated optimum.[^tasks]

## Follow-up and gaps

The original claims about five-year seed viability, a fixed isolation distance, and predictable offspring were not established by this refactor. Verify them against the actual species/cultivar and seed-saving method. Record collected quantity, storage dates/conditions, later emergence, and unexpected traits. A repeated harvest/propagation cycle does not establish perpetual production.

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^core]

[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
