---
type: Crop
title: Basil — sweet basil scope
status: draft
sources:
- id: umn-basil
  resource: https://extension.umn.edu/vegetables/growing-basil
  title: Growing basil in home gardens
steelthumb:
  ontology_version: '0.2'
  relations: []
  claims:
  - id: crop-scope
    kind: descriptive
    statement: This profile covers sweet basil, Ocimum basilicum.
    evidence:
    - source_id: umn-basil
      relation: supports
      locator: Overview
  identity:
    scientific_name: Ocimum basilicum
    common_names:
    - sweet basil
    - basil
---

# Basil — sweet basil scope

This profile covers sweet basil, Ocimum basilicum.[^umn-basil]

## Cultivars

- [Genovese](../cultivars/basil-genovese.md)
- [Siam Queen](../cultivars/basil-siam-queen.md)
- [Rutgers Devotion Dmr](../cultivars/basil-rutgers-devotion-dmr.md)

These are named selections, not interchangeable supplier lots. Shared procedures live once and apply to the crop; cultivar documents retain specific distinctions. Broader labels such as “Thai basil” or “russet” should not automatically become cultivar identities.

## Procedures

- [Sow Basil](../procedures/sow-basil.md)
- [Harvest Basil](../procedures/harvest-basil.md)

## Food and yield

- [Basil Fresh](../food/basil-fresh.md)
- [Yield calculation example](../yields/basil-scenario.md)

Food composition is generic, not a measured cultivar-specific value. The yield example is explicitly a scenario, not a harvest promise. Other basil species need their own crop scope; this profile does not silently include holy basil or every lemon basil.

[^umn-basil]: [Growing basil in home gardens](https://extension.umn.edu/vegetables/growing-basil).
