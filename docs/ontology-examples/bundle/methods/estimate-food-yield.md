---
type: MeasurementMethod
title: Estimate food energy and nutrient yield
status: draft
steelthumb:
  ontology_version: '0.2'
  relations: []
  claims: []
---

# Estimate food energy and nutrient yield

This is a SteelThumb accounting method. It estimates the nutrient content of retained food from a matching food profile; it does not predict a cultivar's agronomic performance.

## Inputs

Record crop/cultivar scope, harvested mass and food state, edible fraction or directly measured edible mass, included harvest events, growing area, and the time window. Tag each input as sourced, observed, or assumed. A measured net edible mass already excludes its recorded losses.

## Calculation

```text
edible_g = harvested_g × edible_fraction
component_total = edible_g / food_basis_g × component_per_basis
component_per_m2 = component_total / growing_area_m2
component_per_m2_day = component_per_m2 / period_days
```

Apply separately to energy (kcal), protein (g), and every reported component with its own units. Missing composition produces an unknown result. Area and duration must be positive. Edible fraction is between zero and one. Source ranges remain ranges; these are not statistical confidence intervals.

## Matching and exclusions

Use a profile with matching edible part and preparation. Retain information about skin removal, water loss or gain, added ingredients, culls, retained seed tubers, and storage losses. Do not apply losses twice. A cooked profile needs cooked food mass or a justified conversion from harvested mass. A raw-profile calculation is potential composition on that basis, not actual intake.

Basil's repeated cuts must be counted once per event. Potato tuber harvest excludes foliage and berries. A one-cycle output is not an annual output. Use [basil](../food/basil-fresh.md), [raw potato](../food/potato-raw.md), or [boiled potato flesh](../food/potato-boiled-flesh.md) only where their food definitions match.

See [the basil scenario](../yields/basil-scenario.md) and [the potato scenario](../yields/potato-scenario.md).
