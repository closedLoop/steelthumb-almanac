---
type: Procedure
title: Prune and harvest basil
description: Harvest leaves while retaining foliage and avoiding wet-weather cuts.
status: draft
sources:
- id: umn-basil
  title: Growing basil in home gardens — Minnesota Extension
  resource: https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/yard-and-garden-problems/growing-basil
- id: clemson-basil
  title: Basil — Clemson Extension
  resource: https://hgic.clemson.edu/factsheet/basil/
steelthumb:
  ontology_version: '0.2'
  license: CC-BY-SA-4.0
  claims:
  - id: leaf-harvest-umn
    kind: recommendation
    statement: Snip young leaves as needed; cut whole stems just above a leaf pair.
    applicability:
      conditions: Leaf harvest; no fixed first-harvest day or canopy fraction.
    evidence:
    - source_id: umn-basil
      relation: supports
      locator: How to keep your basil healthy and productive → Harvesting
  - id: wet-harvest-clemson
    kind: recommendation
    statement: Avoid harvesting in wet weather to reduce gray mold risk at cuts.
    applicability:
      conditions: Clemson basil guidance; risk reduction, not a guaranteed outcome.
    evidence:
    - source_id: clemson-basil
      relation: supports
      locator: Problems → Gray mold
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Prune and harvest basil

Applies to [basil](../crops/basil.md) grown for leaves. Inspect plant condition and plan cuts that retain foliage; Clemson advises leaving enough foliage for continued growth.[^clemson-basil]

## Steps and follow-up

Use the cutting guidance below. Record fresh edible mass if measured, remaining foliage, and subsequent growth or deterioration. For new lesions or mold use [investigation](investigate-basil-symptoms.md). Choose [storage](../guides/basil-storage.md) promptly after picking.

## Source settings

<a id="leaf-harvest-umn"></a>
Snip young leaves as needed; cut whole stems just above a leaf pair.[^umn-basil]

<a id="wet-harvest-clemson"></a>
Avoid harvesting in wet weather to reduce gray mold risk at cuts.[^clemson-basil]

## Evidence scope

Gardening claims cite the supporting passages directly. The assembled sequence and recording prompts are editorial guidance; no field outcomes are asserted.

[^umn-basil]: [Growing basil in home gardens — Minnesota Extension](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/yard-and-garden-problems/growing-basil).
[^clemson-basil]: [Basil — Clemson Extension](https://hgic.clemson.edu/factsheet/basil/).
