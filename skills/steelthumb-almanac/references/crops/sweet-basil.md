---
type: Crop
title: Sweet basil
description: Scoped entry point for Ocimum basilicum guidance.
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
  - id: scope
    kind: descriptive
    statement: This profile covers sweet basil, Ocimum basilicum, as identified in the earlier cultivation
      reference.
    evidence:
    - source_id: core
      relation: supports
      locator: Introduction
  identity:
    scientific_name: Ocimum basilicum
    common_names:
    - sweet basil
---

# Sweet basil

<a id="scope"></a>
This profile covers sweet basil, *Ocimum basilicum*, as identified in the earlier cultivation reference.[^core][^uf]

The broader [basil profile](basil.md) also covers other species and hybrids. Holy basil and African Blue basil do not silently inherit this profile's guidance. Cultivar-specific distinctions belong in a cultivar entry when supported; generic basil guidance is not a cultivar trial.

## Quick reference

| Topic | Where the maintained guidance lives |
| --- | --- |
| Named selections and informal groups | [Variety guide](../guides/basil-varieties.md) |
| Season, light, medium, and spacing | [Growing conditions](../guides/basil-growing-conditions.md) |
| Sowing | [Growing-medium procedure](../procedures/sow-basil.md); [rockwool procedure](../procedures/sow-basil-in-rockwool.md) |
| Propagation | [Cuttings procedure](../procedures/propagate-basil.md) |
| Harvest | [Pruning and harvest procedure](../procedures/harvest-basil.md) |
| Problems | [Symptom investigation](../procedures/investigate-basil-symptoms.md) |

These procedures retain unspecified cultivar scope from their sources. Confirm applicability to the actual selection and setting before choosing a method. Days to germination, first harvest, and seed viability remain source-dependent estimates; this profile makes no universal maturity or yield promise.

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^core]

[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^uf]: [Basil — University of Florida IFAS](https://gardeningsolutions.ifas.ufl.edu/plants/edibles/vegetables/basil/).
