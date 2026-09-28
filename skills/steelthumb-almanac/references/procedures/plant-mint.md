---
type: Procedure
title: Plant culinary mint
description: Culinary spearmint and peppermint for leaves; identified plants in beds or outdoor containers.
status: draft
sources:
- id: rhs-mint
  title: How to grow mint — RHS
  resource: https://www.rhs.org.uk/herbs/mint/grow-your-own
- id: usu-mint
  title: How to Grow Mint in Your Garden — Utah State University
  resource: https://extension.usu.edu/yardandgarden/research/mint-in-the-garden
- id: umd-containers
  title: Types of containers for growing vegetables — Maryland Extension
  resource: https://extension.umd.edu/resource/types-containers-growing-vegetables
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: light
    kind: recommendation
    statement: Mint can grow in full sun or partial shade.
    applicability:
      conditions: UK culinary mint gardening.
    evidence:
    - source_id: rhs-mint
      relation: supports
      locator: Planting
  - id: container
    kind: recommendation
    statement: RHS recommends containers with multipurpose or soil-based peat-free compost to limit spreading
      rhizomes.
    applicability:
      conditions: Container recommendation, not an escape-proof fabric barrier.
    evidence:
    - source_id: rhs-mint
      relation: supports
      locator: Planting
  - id: transplant-depth
    kind: recommendation
    statement: USU advises setting mint transplants with roots just below the soil surface.
    applicability:
      conditions: Utah mint transplant guidance.
    evidence:
    - source_id: usu-mint
      relation: supports
      locator: Planting and Spacing
  - id: container-size-umd
    kind: recommendation
    statement: 'Maryland lists mint in its small-container class: minimum 1–3 gallons of medium and 4–6
      inches deep.'
    applicability:
      conditions: General container class, not a mint cultivar density or fabric trial.
    evidence:
    - source_id: umd-containers
      relation: supports
      locator: Choose the right container size → Small vegetables or flowering plant
  - id: season-rhs
    kind: recommendation
    statement: RHS favors spring or autumn for planting mint.
    applicability:
      conditions: UK seasonal guidance; match local conditions rather than copying calendar months.
    evidence:
    - source_id: rhs-mint
      relation: supports
      locator: Planting
  relations:
  - predicate: applies_to
    target: /crops/mint.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Plant culinary mint

Applies to [mint](../crops/mint.md). Culinary spearmint and peppermint for leaves; identified plants in beds or outdoor containers.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Obtain an identified culinary plant or rooted division; retain the species/cultivar label. Prepare water, a label, and a container or a deliberately allocated bed.

## Steps and source settings

1. Choose light and medium using the claims below, and record the plant identity.
2. Transplant at the source-described depth and record the date.
3. For grow bags, use [shared setup](../systems/outdoor-grow-bags.md) and keep the base and surrounding surface inspectable. Treat this as a pot-guidance adaptation.
4. For a bed, explicitly record the space where continuing spread is acceptable; no barrier construction is established here.

<a id="light"></a>
Mint can grow in full sun or partial shade.[^rhs-mint]

<a id="container"></a>
RHS recommends containers with multipurpose or soil-based peat-free compost to limit spreading rhizomes.[^rhs-mint]

<a id="transplant-depth"></a>
USU advises setting mint transplants with roots just below the soil surface.[^usu-mint]

## Follow-up

Observe establishment and any growth outside the intended area. Begin [mint care](care-for-mint.md).

## Limits

The container starting point below supplies a broad size class, not a tested fabric-containment design. Seed sowing is omitted because this route prioritizes known culinary identity.

[Evidence scope and source context](../sources/garden-crop-research.md).


## Container starting point

Use the class below as a starting size with the mint medium and transplant-depth instructions above. For an initial labeled small transplant, one plant per container is an editorial choice, not a sourced density optimum. Record actual dimensions; divide or repot as [care](care-for-mint.md) describes. A bag is not an escape-proof barrier.

<a id="container-size-umd"></a>
Maryland lists mint in its small-container class: minimum 1–3 gallons of medium and 4–6 inches deep.[^umd-containers]



## Timing

Use the regional timing below or obtain local guidance for the identified mint.

<a id="season-rhs"></a>
RHS favors spring or autumn for planting mint.[^rhs-mint]


[^rhs-mint]: [How to grow mint — RHS](https://www.rhs.org.uk/herbs/mint/grow-your-own).
[^usu-mint]: [How to Grow Mint in Your Garden — Utah State University](https://extension.usu.edu/yardandgarden/research/mint-in-the-garden).

[^umd-containers]: [Types of containers for growing vegetables — Maryland Extension](https://extension.umd.edu/resource/types-containers-growing-vegetables).

