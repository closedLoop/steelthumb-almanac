---
type: YieldEstimate
title: Basil food-yield scenario
status: draft
sources:
- id: composition
  resource: /food/basil-fresh.md
  title: Basil, fresh
steelthumb:
  ontology_version: '0.2'
  relations:
  - predicate: estimates_yield_of
    target: /crops/basil.md
  - predicate: uses_food_profile
    target: /food/basil-fresh.md
  - predicate: uses_method
    target: /methods/estimate-food-yield.md
  claims: []
  yield:
    basis_kind: scenario
    food_profile: /food/basil-fresh.md
    food_state: fresh, uncooked
    cultivar: unspecified
    growing_system: unspecified
    location: not a recorded garden
    inputs:
      harvested_mass_g:
        min: 500
        max: 500
        origin: assumption
      edible_fraction:
        value: 1
        origin: assumption
      growing_area_m2:
        value: 1
        origin: assumption
      period_days:
        value: 90
        origin: assumption
      harvest_count:
        value: 5
        origin: assumption
    method: /methods/estimate-food-yield.md
    results:
    - nutrient_id: usda:1008
      unit: kcal
      total:
        min: 115.0
        max: 115.0
      per_m2:
        min: 115.0
        max: 115.0
      per_m2_day:
        min: 1.277778
        max: 1.277778
    - nutrient_id: usda:1051
      unit: g
      total:
        min: 460.3
        max: 460.3
      per_m2:
        min: 460.3
        max: 460.3
      per_m2_day:
        min: 5.114444
        max: 5.114444
    - nutrient_id: usda:1003
      unit: g
      total:
        min: 15.75
        max: 15.75
      per_m2:
        min: 15.75
        max: 15.75
      per_m2_day:
        min: 0.175
        max: 0.175
    - nutrient_id: usda:1004
      unit: g
      total:
        min: 3.2
        max: 3.2
      per_m2:
        min: 3.2
        max: 3.2
      per_m2_day:
        min: 0.035556
        max: 0.035556
    - nutrient_id: usda:1005
      unit: g
      total:
        min: 13.25
        max: 13.25
      per_m2:
        min: 13.25
        max: 13.25
      per_m2_day:
        min: 0.147222
        max: 0.147222
    - nutrient_id: usda:1079
      unit: g
      total:
        min: 8.0
        max: 8.0
      per_m2:
        min: 8.0
        max: 8.0
      per_m2_day:
        min: 0.088889
        max: 0.088889
    - nutrient_id: usda:2000
      unit: g
      total:
        min: 1.5
        max: 1.5
      per_m2:
        min: 1.5
        max: 1.5
      per_m2_day:
        min: 0.016667
        max: 0.016667
    - nutrient_id: usda:1087
      unit: mg
      total:
        min: 885.0
        max: 885.0
      per_m2:
        min: 885.0
        max: 885.0
      per_m2_day:
        min: 9.833333
        max: 9.833333
    - nutrient_id: usda:1089
      unit: mg
      total:
        min: 15.85
        max: 15.85
      per_m2:
        min: 15.85
        max: 15.85
      per_m2_day:
        min: 0.176111
        max: 0.176111
    - nutrient_id: usda:1090
      unit: mg
      total:
        min: 320.0
        max: 320.0
      per_m2:
        min: 320.0
        max: 320.0
      per_m2_day:
        min: 3.555556
        max: 3.555556
    - nutrient_id: usda:1091
      unit: mg
      total:
        min: 280.0
        max: 280.0
      per_m2:
        min: 280.0
        max: 280.0
      per_m2_day:
        min: 3.111111
        max: 3.111111
    - nutrient_id: usda:1092
      unit: mg
      total:
        min: 1475.0
        max: 1475.0
      per_m2:
        min: 1475.0
        max: 1475.0
      per_m2_day:
        min: 16.388889
        max: 16.388889
    - nutrient_id: usda:1093
      unit: mg
      total:
        min: 20.0
        max: 20.0
      per_m2:
        min: 20.0
        max: 20.0
      per_m2_day:
        min: 0.222222
        max: 0.222222
    - nutrient_id: usda:1095
      unit: mg
      total:
        min: 4.05
        max: 4.05
      per_m2:
        min: 4.05
        max: 4.05
      per_m2_day:
        min: 0.045
        max: 0.045
    - nutrient_id: usda:1098
      unit: mg
      total:
        min: 1.925
        max: 1.925
      per_m2:
        min: 1.925
        max: 1.925
      per_m2_day:
        min: 0.021389
        max: 0.021389
    - nutrient_id: usda:1101
      unit: mg
      total:
        min: 5.74
        max: 5.74
      per_m2:
        min: 5.74
        max: 5.74
      per_m2_day:
        min: 0.063778
        max: 0.063778
    - nutrient_id: usda:1103
      unit: µg
      total:
        min: 1.5
        max: 1.5
      per_m2:
        min: 1.5
        max: 1.5
      per_m2_day:
        min: 0.016667
        max: 0.016667
    - nutrient_id: usda:1162
      unit: mg
      total:
        min: 90.0
        max: 90.0
      per_m2:
        min: 90.0
        max: 90.0
      per_m2_day:
        min: 1.0
        max: 1.0
    - nutrient_id: usda:1165
      unit: mg
      total:
        min: 0.17
        max: 0.17
      per_m2:
        min: 0.17
        max: 0.17
      per_m2_day:
        min: 0.001889
        max: 0.001889
    - nutrient_id: usda:1166
      unit: mg
      total:
        min: 0.38
        max: 0.38
      per_m2:
        min: 0.38
        max: 0.38
      per_m2_day:
        min: 0.004222
        max: 0.004222
    - nutrient_id: usda:1167
      unit: mg
      total:
        min: 4.51
        max: 4.51
      per_m2:
        min: 4.51
        max: 4.51
      per_m2_day:
        min: 0.050111
        max: 0.050111
    - nutrient_id: usda:1170
      unit: mg
      total:
        min: 1.045
        max: 1.045
      per_m2:
        min: 1.045
        max: 1.045
      per_m2_day:
        min: 0.011611
        max: 0.011611
    - nutrient_id: usda:1175
      unit: mg
      total:
        min: 0.775
        max: 0.775
      per_m2:
        min: 0.775
        max: 0.775
      per_m2_day:
        min: 0.008611
        max: 0.008611
    - nutrient_id: usda:1177
      unit: µg
      total:
        min: 340.0
        max: 340.0
      per_m2:
        min: 340.0
        max: 340.0
      per_m2_day:
        min: 3.777778
        max: 3.777778
    - nutrient_id: usda:1190
      unit: µg
      total:
        min: 340.0
        max: 340.0
      per_m2:
        min: 340.0
        max: 340.0
      per_m2_day:
        min: 3.777778
        max: 3.777778
    - nutrient_id: usda:1178
      unit: µg
      total:
        min: 0.0
        max: 0.0
      per_m2:
        min: 0.0
        max: 0.0
      per_m2_day:
        min: 0.0
        max: 0.0
    - nutrient_id: usda:1106
      unit: µg
      total:
        min: 1320.0
        max: 1320.0
      per_m2:
        min: 1320.0
        max: 1320.0
      per_m2_day:
        min: 14.666667
        max: 14.666667
    - nutrient_id: usda:1109
      unit: mg
      total:
        min: 4.0
        max: 4.0
      per_m2:
        min: 4.0
        max: 4.0
      per_m2_day:
        min: 0.044444
        max: 0.044444
    - nutrient_id: usda:1114
      unit: µg
      total:
        min: 0.0
        max: 0.0
      per_m2:
        min: 0.0
        max: 0.0
      per_m2_day:
        min: 0.0
        max: 0.0
    - nutrient_id: usda:1185
      unit: µg
      total:
        min: 2074.0
        max: 2074.0
      per_m2:
        min: 2074.0
        max: 2074.0
      per_m2_day:
        min: 23.044444
        max: 23.044444
    - nutrient_id: usda:1180
      unit: mg
      total:
        min: 57.0
        max: 57.0
      per_m2:
        min: 57.0
        max: 57.0
      per_m2_day:
        min: 0.633333
        max: 0.633333
    - nutrient_id: usda:1107
      unit: µg
      total:
        min: 15710.0
        max: 15710.0
      per_m2:
        min: 15710.0
        max: 15710.0
      per_m2_day:
        min: 174.555556
        max: 174.555556
    - nutrient_id: usda:1123
      unit: µg
      total:
        min: 28250.0
        max: 28250.0
      per_m2:
        min: 28250.0
        max: 28250.0
      per_m2_day:
        min: 313.888889
        max: 313.888889
    - nutrient_id: usda:1258
      unit: g
      total:
        min: 0.205
        max: 0.205
      per_m2:
        min: 0.205
        max: 0.205
      per_m2_day:
        min: 0.002278
        max: 0.002278
    - nutrient_id: usda:1259
      unit: g
      total:
        min: 0.0
        max: 0.0
      per_m2:
        min: 0.0
        max: 0.0
      per_m2_day:
        min: 0.0
        max: 0.0
    - nutrient_id: usda:1292
      unit: g
      total:
        min: 0.44
        max: 0.44
      per_m2:
        min: 0.44
        max: 0.44
      per_m2_day:
        min: 0.004889
        max: 0.004889
    - nutrient_id: usda:1293
      unit: g
      total:
        min: 1.945
        max: 1.945
      per_m2:
        min: 1.945
        max: 1.945
      per_m2_day:
        min: 0.021611
        max: 0.021611
    - nutrient_id: usda:1269
      unit: g
      total:
        min: 0.365
        max: 0.365
      per_m2:
        min: 0.365
        max: 0.365
      per_m2_day:
        min: 0.004056
        max: 0.004056
    - nutrient_id: usda:1270
      unit: g
      total:
        min: 1.58
        max: 1.58
      per_m2:
        min: 1.58
        max: 1.58
      per_m2_day:
        min: 0.017556
        max: 0.017556
    - nutrient_id: usda:1210
      unit: g
      total:
        min: 0.195
        max: 0.195
      per_m2:
        min: 0.195
        max: 0.195
      per_m2_day:
        min: 0.002167
        max: 0.002167
    - nutrient_id: usda:1211
      unit: g
      total:
        min: 0.52
        max: 0.52
      per_m2:
        min: 0.52
        max: 0.52
      per_m2_day:
        min: 0.005778
        max: 0.005778
    - nutrient_id: usda:1212
      unit: g
      total:
        min: 0.52
        max: 0.52
      per_m2:
        min: 0.52
        max: 0.52
      per_m2_day:
        min: 0.005778
        max: 0.005778
    - nutrient_id: usda:1213
      unit: g
      total:
        min: 0.955
        max: 0.955
      per_m2:
        min: 0.955
        max: 0.955
      per_m2_day:
        min: 0.010611
        max: 0.010611
    - nutrient_id: usda:1214
      unit: g
      total:
        min: 0.55
        max: 0.55
      per_m2:
        min: 0.55
        max: 0.55
      per_m2_day:
        min: 0.006111
        max: 0.006111
    - nutrient_id: usda:1215
      unit: g
      total:
        min: 0.18
        max: 0.18
      per_m2:
        min: 0.18
        max: 0.18
      per_m2_day:
        min: 0.002
        max: 0.002
    - nutrient_id: usda:1217
      unit: g
      total:
        min: 0.65
        max: 0.65
      per_m2:
        min: 0.65
        max: 0.65
      per_m2_day:
        min: 0.007222
        max: 0.007222
    - nutrient_id: usda:1219
      unit: g
      total:
        min: 0.635
        max: 0.635
      per_m2:
        min: 0.635
        max: 0.635
      per_m2_day:
        min: 0.007056
        max: 0.007056
    - nutrient_id: usda:1221
      unit: g
      total:
        min: 0.255
        max: 0.255
      per_m2:
        min: 0.255
        max: 0.255
      per_m2_day:
        min: 0.002833
        max: 0.002833
---

# Basil food-yield scenario

**Illustrative calculation, not an observed harvest or a cultivar forecast.**

Assume 500 g retained fresh basil across five cuts, grown on 1 m² over 90 days. All harvest, area, and time inputs are invented to exercise the model. Edible fraction 1 means the input mass is already retained edible material.

Use the [food profile](../food/basil-fresh.md) for composition.[^composition] Apply the [method](../methods/estimate-food-yield.md) to [basil](../crops/basil.md).

## Energy result

- Total: 115–115 kcal.
- Per area: 115–115 kcal/m² for the stated period.
- Per area-day: 1.27778–1.27778 kcal/m²/day.

Frontmatter carries the same calculation for each reported nutrient. Raw food-energy estimates do not account for preparation losses or added ingredients. Neither these scenarios nor their daily normalization establish annual productivity; do not rank the crops by agronomic performance using these unequal assumptions.

[^composition]: [Basil, fresh](/food/basil-fresh.md).
