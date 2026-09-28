---
type: Guide
title: Basil growing conditions
description: Contextualized growing ranges and links to the procedures that use them.
status: draft
sources:
- id: core
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md
  title: SteelThumb basil cultivation reference
- id: wvu
  resource: https://extension.wvu.edu/lawn-gardening-pests/gardening/wv-garden-guide/growing-basil-in-west-virginia
  title: Growing Basil — West Virginia University Extension
- id: uf
  resource: https://gardeningsolutions.ifas.ufl.edu/plants/edibles/vegetables/basil/
  title: Basil — University of Florida IFAS
- id: ne
  resource: https://nevegetable.org/crops/basil
  title: Basil — New England Vegetable Management Guide
- id: kentucky
  resource: https://publications.ca.uky.edu/sites/publications.ca.uky.edu/files/NEP237.pdf
  title: Growing Your Own Basil — University of Kentucky
- id: design
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md
  title: SteelThumb procedural design
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  claims:
  - id: indoor-pot-assumption
    kind: descriptive
    statement: The earlier indoor design uses 6-inch pots.
    evidence:
    - source_id: design
      relation: supports
      locator: Objective & Assumptions
    applicability:
      conditions: Original indoor design; not a general minimum container size.
    quantity:
      property: pot_diameter
      value: 6
      unit: in
---

# Basil growing conditions

Scope: the earlier general cultivation reference, largely outdoor basil guidance, with cultivar often unspecified. The [indoor system](../systems/indoor-basil-containers.md) describes a different setting. The following are inherited recommendations awaiting source review, not experimentally established optima.[^core]

| Topic | Earlier guidance | Applicability or unresolved detail |
| --- | --- | --- |
| Season | Plant outdoors after frost risk; the text mentions nights above roughly 50–55°F (10–13°C). | Local climate and growing stage matter; the original distinguishes West Virginia and Florida seasons. [^wvu][^uf] |
| Light | Approximately 6–8 hours of direct sun; afternoon shade discussed for intense heat. | Sun duration is not equivalent to a lamp photoperiod or measured light dose. [^wvu][^uf] |
| Medium | Fertile, well-drained medium; the old summary gives pH around 6.0–7.0. | Source wording and sampling method need review; this is not rockwool soak-water pH. [^ne][^wvu] |
| Spacing | Roughly 10–18 inches between plants in the earlier guide. | Actual mature habit, row spacing, and cultivar need to be specified. [^wvu] |
| Containers | The old general guide suggests 8–10-inch pots; the indoor design uses 6-inch pots. | These are distinct design recommendations, not one averaged minimum. [^kentucky][^design] |
| Climate | Seasonal adjustment, warm microclimates, drainage, and gradual acclimation are discussed. | Preserve regional applicability instead of treating one planting calendar as universal. [^uf][^wvu] |

<a id="indoor-pot-assumption"></a>
The earlier indoor design uses 6-inch pots; the general cultivation document gives a different container recommendation.[^design][^core]

## Use with a procedure

Follow [sowing](../procedures/sow-basil.md), [transplanting](../procedures/transplant-basil.md), and [container care](../procedures/care-for-container-basil.md) for task instructions. Record the actual medium, measurements, light arrangement, and cultivar in any field report. Missing measurements remain unknown.

The former text's companion-planting suggestions, regional generalizations, and predictions of first harvest are not adopted here as universal claims. Reassess them against the named original sources and relevant conditions before using them to plan outcomes.

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^core]

[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^wvu]: [Growing Basil — West Virginia University Extension](https://extension.wvu.edu/lawn-gardening-pests/gardening/wv-garden-guide/growing-basil-in-west-virginia).
[^uf]: [Basil — University of Florida IFAS](https://gardeningsolutions.ifas.ufl.edu/plants/edibles/vegetables/basil/).
[^ne]: [Basil — New England Vegetable Management Guide](https://nevegetable.org/crops/basil).
[^kentucky]: [Growing Your Own Basil — University of Kentucky](https://publications.ca.uky.edu/sites/publications.ca.uky.edu/files/NEP237.pdf).
[^design]: [SteelThumb procedural design](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md).
