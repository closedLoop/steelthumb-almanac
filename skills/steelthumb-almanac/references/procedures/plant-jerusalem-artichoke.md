---
type: Procedure
title: Plant Jerusalem artichokes
description: Establish tubers in garden soil or an outdoor grow bag with distinct source contexts.
status: draft
sources:
- id: usask
  resource: https://gardening.usask.ca/gardening-advice/gardenline-nested-pages/food-plant-pages/vegetables/jerusalem-artichoke.php
  title: Jerusalem artichokes — University of Saskatchewan
- id: rhs
  resource: https://www.rhs.org.uk/vegetables/jerusalem-artichokes/grow-your-own
  title: How to grow Jerusalem artichokes — RHS
- id: mu
  resource: https://extension.missouri.edu/news/north-americas-nearly-forgotten-native-vegetable
  title: North America’s nearly forgotten native vegetable — MU Extension
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: ground-depth
    kind: recommendation
    statement: USask recommends planting tubers 10 cm deep.
    applicability:
      conditions: Canadian prairie outdoor soil planting.
    evidence:
    - source_id: usask
      relation: supports
      locator: Growing outdoors > Planting instructions
    quantity:
      property: planting_depth
      unit: cm
      value: 10
      basis: Tuber planting depth as stated; measurement reference unspecified.
  - id: ground-in-row
    kind: recommendation
    statement: USask recommends 30–35 cm between tubers within rows.
    applicability:
      conditions: Canadian prairie outdoor soil planting.
    evidence:
    - source_id: usask
      relation: supports
      locator: Growing outdoors > Planting instructions
    quantity:
      property: in_row_spacing
      unit: cm
      min: 30
      max: 35
  - id: ground-rows
    kind: recommendation
    statement: USask recommends 60–100 cm between rows.
    applicability:
      conditions: Canadian prairie outdoor soil planting.
    evidence:
    - source_id: usask
      relation: supports
      locator: Growing outdoors > Planting instructions
    quantity:
      property: row_spacing
      unit: cm
      min: 60
      max: 100
  - id: container-dimensions
    kind: recommendation
    statement: RHS specifies containers at least 45 cm wide and deep.
    applicability:
      conditions: UK pot guidance; bag adaptation untested.
    evidence:
    - source_id: rhs
      relation: supports
      locator: Planting > Planting in containers
    quantity:
      property: minimum_container_width_and_depth
      unit: cm
      value: 45
      basis: Minimum for each dimension, not volume.
  - id: container-count
    kind: recommendation
    statement: RHS specifies one or two tubers per container.
    applicability:
      conditions: Container meeting RHS dimensions.
    evidence:
    - source_id: rhs
      relation: supports
      locator: Planting > Planting in containers
    quantity:
      property: planting_tuber_count
      unit: tubers
      min: 1
      max: 2
      basis: Per container, not per litre.
  - id: container-depth
    kind: recommendation
    statement: RHS specifies tuber planting depth of 10–15 cm.
    applicability:
      conditions: UK pot guidance; bag adaptation untested.
    evidence:
    - source_id: rhs
      relation: supports
      locator: Planting > Planting in containers
    quantity:
      property: planting_depth
      unit: cm
      min: 10
      max: 15
      basis: As stated; measurement reference unspecified.
  - id: ground-season
    kind: recommendation
    statement: Plant Jerusalem artichoke tubers in spring when soil is workable.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: mu
      relation: supports
      locator: Planting guidance
  - id: site-light
    kind: recommendation
    statement: USask recommends sun for Jerusalem artichokes; partial shade is unsuitable in its guidance.
    applicability:
      conditions: Source gardening guidance; regional and route scope retained in this procedure.
    evidence:
    - source_id: usask
      relation: supports
      locator: Site requirements
  relations:
  - predicate: applies_to
    target: /crops/jerusalem-artichoke.md
  - predicate: applies_to
    target: /systems/jerusalem-artichoke-grow-bags.md
---

# Plant Jerusalem artichokes

Applies to [Jerusalem artichoke](../crops/jerusalem-artichoke.md) and the [grow-bag system](../systems/jerusalem-artichoke-grow-bags.md). Establish a labelled planting; do not treat these regional branches as one tested recipe.

## Before planting

Obtain identified planting tubers, a label, suitable ground or a bag and potting medium, water, and a support plan. Record cultivar as unknown if it is not supplied.

<a id="site"></a>
RHS advises a sheltered position in sun or partial shade for containers.[^rhs] USask excludes partial shade.[^usask] Prefer sun where available; performance in a particular shaded site remains uncertain.

MU recommends spring planting once soil is workable and keeping planting tubers from drying out.[^mu] This is a readiness condition, not a calendar date for every climate.

## Ground branch

<a id="ground-depth"></a>
<a id="ground-in-row"></a>
<a id="ground-rows"></a>
1. Choose a site whose continuing occupation is acceptable; review the crop's [spread warning](../crops/jerusalem-artichoke.md#persistent-spread).
2. Following USask, plant 10 cm deep, 30–35 cm apart within rows, with 60–100 cm between rows. Pieces need at least two buds.[^usask]
3. Label and record actual depth, spacing, date, and starting material. These recordkeeping steps are Almanac conventions.

## Grow-bag branch

<a id="container-dimensions"></a>
<a id="container-count"></a>
<a id="container-depth"></a>
1. Use the RHS pot starting point: at least 45 cm wide and deep, one or two tubers, planted 10–15 cm deep in peat-free multipurpose potting compost.[^rhs]
2. Applying this to fabric is an untested adaptation. Follow the [bag arrangement checks](../systems/jerusalem-artichoke-grow-bags.md), and document the actual filled dimensions.
3. Water after planting, then follow the [container moisture check](care-for-jerusalem-artichoke.md#container-watering).[^rhs]

<a id="ground-season"></a>
Plant Jerusalem artichoke tubers in spring when soil is workable.[^mu]

<a id="site-light"></a>
USask recommends sun for Jerusalem artichokes; partial shade is unsuitable in its guidance.[^usask]

## Follow-up and limits

Record first emergence when observed; no emergence deadline is established here. Photograph the planting label and later shoots, and begin [seasonal care](care-for-jerusalem-artichoke.md). If growth is absent, record medium condition and tuber condition before assuming failure.

This procedure chooses spring establishment and does not prescribe fall planting. Bag performance, optimal density, and cultivar-specific establishment remain unresolved. The sources' depth wording lacks a precise top-versus-centre measurement convention; record the convention actually used rather than implying greater precision.

[^usask]: [Jerusalem artichokes — University of Saskatchewan](https://gardening.usask.ca/gardening-advice/gardenline-nested-pages/food-plant-pages/vegetables/jerusalem-artichoke.php).
[^rhs]: [How to grow Jerusalem artichokes — RHS](https://www.rhs.org.uk/vegetables/jerusalem-artichokes/grow-your-own).
[^mu]: [North America’s nearly forgotten native vegetable — MU Extension](https://extension.missouri.edu/news/north-americas-nearly-forgotten-native-vegetable).
