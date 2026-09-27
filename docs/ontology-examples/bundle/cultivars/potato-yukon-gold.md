---
type: Cultivar
title: Yukon Gold
status: draft
sources:
- id: illinois-potato
  resource: https://extension.illinois.edu/gardening/potato
  title: 'Potato: Home Vegetable Gardening'
- id: maine-potato
  resource: https://extension.umaine.edu/publications/2077e/
  title: 'Bulletin 2077: Growing Potatoes in the Home Garden'
steelthumb:
  ontology_version: '0.2'
  relations:
  - predicate: cultivar_of
    target: /crops/potato.md
  claims:
  - id: cultivar-traits
    kind: descriptive
    statement: Illinois Extension describes Yukon Gold as yellow-fleshed and a very early bearer.
    evidence:
    - source_id: illinois-potato
      relation: supports
      locator: Recommended Varieties
    applicability:
      conditions: Extension description; not a guarantee for every site or supplier lot.
  - id: maturity-maine
    kind: descriptive
    statement: The Maine variety table places Yukon Gold in its late-season column.
    evidence:
    - source_id: maine-potato
      relation: supports
      locator: Varieties table
    applicability:
      conditions: Maine bulletin; no common timing baseline supplied for comparison with Illinois.
  identity:
    cultivar_name: Yukon Gold
---

# Yukon Gold

Illinois Extension describes Yukon Gold as yellow-fleshed and a very early bearer.[^illinois-potato]

Belongs to [potato](../crops/potato.md). Follow the shared planting and harvesting procedures linked there. Record the actual supplier and material lot separately.

This profile has no cultivar-specific nutritional assay or yield trial attached. A generic food profile may be used only as an explicitly labeled proxy. No maturity date is inherited from the parent crop.

## Unresolved maturity disagreement

The Maine table instead marks Yukon Gold late-season.[^maine-potato] Preserve both source assertions. These categories have no shared days-from-planting definition here; do not average them or invent a numeric maturity time. A documented supplier maturity estimate or local trial is needed to schedule a particular planting.

[^illinois-potato]: [Potato: Home Vegetable Gardening](https://extension.illinois.edu/gardening/potato).
[^maine-potato]: [Bulletin 2077: Growing Potatoes in the Home Garden](https://extension.umaine.edu/publications/2077e/).
