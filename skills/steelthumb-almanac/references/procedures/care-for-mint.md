---
type: Procedure
title: Care for and investigate culinary mint
description: Culinary spearmint and peppermint for leaves; identified plants in beds or outdoor containers.
status: draft
sources:
- id: rhs-mint
  title: How to grow mint — RHS
  resource: https://www.rhs.org.uk/herbs/mint/grow-your-own
- id: usu-mint
  title: How to Grow Mint in Your Garden — Utah State University
  resource: https://extension.usu.edu/yardandgarden/research/mint-in-the-garden
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: moisture
    kind: recommendation
    statement: Keep container mint compost moist, especially during hot or dry weather.
    applicability:
      conditions: UK container mint; avoid treating moist as continuously flooded.
    evidence:
    - source_id: rhs-mint
      relation: supports
      locator: Watering
  - id: renewal
    kind: recommendation
    statement: Repot mint into a larger container or divide it as the clump fills its pot.
    applicability:
      conditions: Timing depends on container size and plant growth.
    evidence:
    - source_id: rhs-mint
      relation: supports
      locator: Planting
  - id: rust-candidate
    kind: descriptive
    statement: Raised spots becoming orange-brown on mint leaf undersides are consistent with mint rust.
    applicability:
      conditions: Candidate diagnosis requiring inspection.
    evidence:
    - source_id: usu-mint
      relation: supports
      locator: Pests and Disease > Mint Rust
  relations:
  - predicate: applies_to
    target: /crops/mint.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Care for and investigate culinary mint

Applies to [mint](../crops/mint.md). Culinary spearmint and peppermint for leaves; identified plants in beds or outdoor containers.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Keep the identity label, planting record, and medium/feed information; inspect both leaf surfaces.

## Steps and source settings

1. Check moisture and drainage and water according to the claim below; inspect bag fabric and surroundings as part of containment monitoring.
2. When crowded, follow the renewal choice below, retaining plant identity when dividing.
3. For leaf spots, photograph both surfaces and compare the actual signs with the rust candidate; leaf yellowing alone is not sufficient.
4. Use the [observation workflow](review-garden-observations.md) for persistent decline.

<a id="moisture"></a>
Keep container mint compost moist, especially during hot or dry weather.[^rhs-mint]

<a id="renewal"></a>
Repot mint into a larger container or divide it as the clump fills its pot.[^rhs-mint]

<a id="rust-candidate"></a>
Raised spots becoming orange-brown on mint leaf undersides are consistent with mint rust.[^usu-mint]

## Investigate: spots on leaf undersides

These are editorial observation steps using the linked source claims.

1. Compare raised orange-brown underside spots with the [rust candidate](#rust-candidate), checking both surfaces. Yellowing alone does not meet that description.
2. If the pattern matches or spreads, seek a diagnostic identification with affected leaves/photos before treatment. Recheck new leaves and record spread; this collection does not establish a rust treatment.

## Follow-up

Record moisture, repotting or divisions, escape observations, and subsequent new growth. Recheck affected leaves after any care change.

## Limits

No universal winter-hardiness claim transfers to exposed bags. Crop-specific container fertilizer rates, pesticide treatment, and complete disease discrimination remain unresolved.

[Evidence scope and source context](../sources/garden-crop-research.md).

[^rhs-mint]: [How to grow mint — RHS](https://www.rhs.org.uk/herbs/mint/grow-your-own).
[^usu-mint]: [How to Grow Mint in Your Garden — Utah State University](https://extension.usu.edu/yardandgarden/research/mint-in-the-garden).
