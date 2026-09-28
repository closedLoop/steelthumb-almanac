---
type: Crop
title: Basil
description: Basil crop overview, scope, and routes to growing guidance.
status: draft
sources:
- id: core
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md
  title: SteelThumb basil cultivation reference
- id: uf
  resource: https://gardeningsolutions.ifas.ufl.edu/plants/edibles/vegetables/basil/
  title: Basil — University of Florida IFAS
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  claims:
  - id: sweet-basil-identity
    kind: descriptive
    statement: The earlier cultivation reference identifies sweet basil as Ocimum basilicum.
    evidence:
    - source_id: core
      relation: supports
      locator: Introduction
---

# Basil

“Basil” is used here as a broad culinary crop category covering several *Ocimum* species, cultivated selections, and hybrids. Sweet basil (*Ocimum basilicum*) is a narrower subject within that category.[^core][^uf]

<a id="sweet-basil-identity"></a>
The earlier cultivation reference identifies sweet basil as *Ocimum basilicum*.[^core]

## Identity and applicability

Use the [sweet-basil profile](sweet-basil.md) for that explicit scope and the [variety guide](../guides/basil-varieties.md) to distinguish named cultivars from informal groups, other species, and hybrids. An unspecified basil plant is not automatically Genovese. A named cultivar is distinct from the supplier product or seed lot used in a garden.

The imported guidance mixes outdoor cultivation and an indoor rockwool-to-container design. Read each procedure's scope; values are not universal requirements for every basil. Sources and local outcomes may disagree without describing the same conditions.

## Growing and learning

- [Growing conditions](../guides/basil-growing-conditions.md): seasonal context, medium, spacing, and unresolved ranges.
- [Indoor container system](../systems/indoor-basil-containers.md): the specific proposed arrangement and its assumptions.
- [Sow in growing medium](../procedures/sow-basil.md) or [start in rockwool](../procedures/sow-basil-in-rockwool.md).
- [Transplant](../procedures/transplant-basil.md) and [maintain container plants](../procedures/care-for-container-basil.md).
- [Propagate from cuttings](../procedures/propagate-basil.md).
- [Prune and harvest](../procedures/harvest-basil.md), [consider storage options](../guides/basil-storage.md), and [save seed or carry plants across seasons](../procedures/save-basil-seed.md).
- [Investigate symptoms](../procedures/investigate-basil-symptoms.md).
- [The Amazing Basil Machine learning guide](../guides/basil-learning-guide.md).

## Evidence gaps

No firsthand field reports, measured yields, or nutritional assays were supplied with this collection. The procedure drafts have documentary origins, not demonstrated effectiveness. The separate ontology example bundle remains illustrative and is not additional evidence for this crop.

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^core]

[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^uf]: [Basil — University of Florida IFAS](https://gardeningsolutions.ifas.ufl.edu/plants/edibles/vegetables/basil/).
