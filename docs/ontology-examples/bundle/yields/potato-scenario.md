---
type: YieldEstimate
title: Potato food-yield scenario
status: draft
sources:
- id: composition
  resource: /food/potato-raw.md
  title: Potatoes, flesh and skin, raw
- id: maine-potato
  resource: https://extension.umaine.edu/publications/2077e/
  title: 'Bulletin 2077: Growing Potatoes in the Home Garden'
steelthumb:
  ontology_version: '0.2'
  relations:
  - predicate: estimates_yield_of
    target: /crops/potato.md
  - predicate: uses_food_profile
    target: /food/potato-raw.md
  - predicate: uses_method
    target: /methods/estimate-food-yield.md
  claims:
  - id: row-yield
    kind: descriptive
    statement: Maine Extension gives an expected potato yield of one to two pounds per foot of row.
    evidence:
    - source_id: maine-potato
      relation: supports
      locator: Planting
    quantity:
      property: harvest_mass
      min: 1
      max: 2
      unit: lb
      basis: per foot of row
    applicability:
      conditions: Maine home-garden guidance; cultivar and season duration unspecified.
  yield:
    basis_kind: scenario
    food_profile: /food/potato-raw.md
    food_state: raw
    cultivar: unspecified
    growing_system: unspecified
    location: not a recorded garden
    inputs:
      harvested_mass_g:
        min: 453.59237
        max: 907.18474
        origin: source
        source_id: maine-potato
        original:
          min: 1
          max: 2
          unit: lb
          basis: per foot of row
        grams_per_lb: 453.59237
      edible_fraction:
        value: 0.9
        origin: assumption
      growing_area_m2:
        value: 0.27870912000000003
        origin: assumption
        geometry:
          row_length_m: 0.3048
          row_spacing_m: 0.9144
          definition: Row length times row spacing, including allocated inter-row space.
      period_days:
        value: 120
        origin: assumption
      harvest_count:
        value: 1
        origin: assumption
    method: /methods/estimate-food-yield.md
    results:
    - nutrient_id: usda:1008
      unit: kcal
      total:
        min: 314.339512
        max: 628.679025
      per_m2:
        min: 1127.840784
        max: 2255.681568
      per_m2_day:
        min: 9.398673
        max: 18.797346
    - nutrient_id: usda:1051
      unit: g
      total:
        min: 323.524758
        max: 647.049516
      per_m2:
        min: 1160.797171
        max: 2321.594341
      per_m2_day:
        min: 9.67331
        max: 19.34662
    - nutrient_id: usda:1003
      unit: g
      total:
        min: 8.368779
        max: 16.737558
      per_m2:
        min: 30.02693
        max: 60.05386
      per_m2_day:
        min: 0.250224
        max: 0.500449
    - nutrient_id: usda:1004
      unit: g
      total:
        min: 0.36741
        max: 0.73482
      per_m2:
        min: 1.318255
        max: 2.636511
      per_m2_day:
        min: 0.010985
        max: 0.021971
    - nutrient_id: usda:1005
      unit: g
      total:
        min: 71.399975
        max: 142.79995
      per_m2:
        min: 256.180978
        max: 512.361956
      per_m2_day:
        min: 2.134841
        max: 4.269683
    - nutrient_id: usda:1079
      unit: g
      total:
        min: 8.572896
        max: 17.145792
      per_m2:
        min: 30.759294
        max: 61.518588
      per_m2_day:
        min: 0.256327
        max: 0.512655
    - nutrient_id: usda:2000
      unit: g
      total:
        min: 3.347512
        max: 6.695023
      per_m2:
        min: 12.010772
        max: 24.021544
      per_m2_day:
        min: 0.10009
        max: 0.20018
    - nutrient_id: usda:1009
      unit: g
      total:
        min: 62.418846
        max: 124.837692
      per_m2:
        min: 223.956956
        max: 447.913911
      per_m2_day:
        min: 1.866308
        max: 3.732616
    - nutrient_id: usda:1087
      unit: mg
      total:
        min: 48.987976
        max: 97.975952
      per_m2:
        min: 175.767395
        max: 351.53479
      per_m2_day:
        min: 1.464728
        max: 2.929457
    - nutrient_id: usda:1089
      unit: mg
      total:
        min: 3.306688
        max: 6.613377
      per_m2:
        min: 11.864299
        max: 23.728598
      per_m2_day:
        min: 0.098869
        max: 0.197738
    - nutrient_id: usda:1090
      unit: mg
      total:
        min: 93.893621
        max: 187.787241
      per_m2:
        min: 336.887507
        max: 673.775014
      per_m2_day:
        min: 2.807396
        max: 5.614792
    - nutrient_id: usda:1091
      unit: mg
      total:
        min: 232.692886
        max: 465.385772
      per_m2:
        min: 834.895126
        max: 1669.790252
      per_m2_day:
        min: 6.957459
        max: 13.914919
    - nutrient_id: usda:1092
      unit: mg
      total:
        min: 1734.990815
        max: 3469.98163
      per_m2:
        min: 6225.095236
        max: 12450.190473
      per_m2_day:
        min: 51.875794
        max: 103.751587
    - nutrient_id: usda:1093
      unit: mg
      total:
        min: 24.493988
        max: 48.987976
      per_m2:
        min: 87.883697
        max: 175.767395
      per_m2_day:
        min: 0.732364
        max: 1.464728
    - nutrient_id: usda:1095
      unit: mg
      total:
        min: 1.224699
        max: 2.449399
      per_m2:
        min: 4.394185
        max: 8.78837
      per_m2_day:
        min: 0.036618
        max: 0.073236
    - nutrient_id: usda:1098
      unit: mg
      total:
        min: 0.449056
        max: 0.898113
      per_m2:
        min: 1.611201
        max: 3.222402
      per_m2_day:
        min: 0.013427
        max: 0.026853
    - nutrient_id: usda:1101
      unit: mg
      total:
        min: 0.624597
        max: 1.249193
      per_m2:
        min: 2.241034
        max: 4.482069
      per_m2_day:
        min: 0.018675
        max: 0.037351
    - nutrient_id: usda:1103
      unit: µg
      total:
        min: 1.632933
        max: 3.265865
      per_m2:
        min: 5.858913
        max: 11.717826
      per_m2_day:
        min: 0.048824
        max: 0.097649
    - nutrient_id: usda:1162
      unit: mg
      total:
        min: 80.421927
        max: 160.843854
      per_m2:
        min: 288.551473
        max: 577.102947
      per_m2_day:
        min: 2.404596
        max: 4.809191
    - nutrient_id: usda:1165
      unit: mg
      total:
        min: 0.330669
        max: 0.661338
      per_m2:
        min: 1.18643
        max: 2.37286
      per_m2_day:
        min: 0.009887
        max: 0.019774
    - nutrient_id: usda:1166
      unit: mg
      total:
        min: 0.130635
        max: 0.261269
      per_m2:
        min: 0.468713
        max: 0.937426
      per_m2_day:
        min: 0.003906
        max: 0.007812
    - nutrient_id: usda:1167
      unit: mg
      total:
        min: 4.331354
        max: 8.662707
      per_m2:
        min: 15.540767
        max: 31.081534
      per_m2_day:
        min: 0.129506
        max: 0.259013
    - nutrient_id: usda:1170
      unit: mg
      total:
        min: 1.204288
        max: 2.408575
      per_m2:
        min: 4.320948
        max: 8.641897
      per_m2_day:
        min: 0.036008
        max: 0.072016
    - nutrient_id: usda:1175
      unit: mg
      total:
        min: 1.216535
        max: 2.433069
      per_m2:
        min: 4.36489
        max: 8.729781
      per_m2_day:
        min: 0.036374
        max: 0.072748
    - nutrient_id: usda:1177
      unit: µg
      total:
        min: 61.23497
        max: 122.46994
      per_m2:
        min: 219.709244
        max: 439.418487
      per_m2_day:
        min: 1.83091
        max: 3.661821
    - nutrient_id: usda:1190
      unit: µg
      total:
        min: 61.23497
        max: 122.46994
      per_m2:
        min: 219.709244
        max: 439.418487
      per_m2_day:
        min: 1.83091
        max: 3.661821
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
        min: 0.0
        max: 0.0
      per_m2:
        min: 0.0
        max: 0.0
      per_m2_day:
        min: 0.0
        max: 0.0
    - nutrient_id: usda:1109
      unit: mg
      total:
        min: 0.040823
        max: 0.081647
      per_m2:
        min: 0.146473
        max: 0.292946
      per_m2_day:
        min: 0.001221
        max: 0.002441
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
        min: 8.164663
        max: 16.329325
      per_m2:
        min: 29.294566
        max: 58.589132
      per_m2_day:
        min: 0.244121
        max: 0.488243
    - nutrient_id: usda:1180
      unit: mg
      total:
        min: 49.396209
        max: 98.792418
      per_m2:
        min: 177.232123
        max: 354.464246
      per_m2_day:
        min: 1.476934
        max: 2.953869
    - nutrient_id: usda:1107
      unit: µg
      total:
        min: 4.082331
        max: 8.164663
      per_m2:
        min: 14.647283
        max: 29.294566
      per_m2_day:
        min: 0.122061
        max: 0.244121
    - nutrient_id: usda:1123
      unit: µg
      total:
        min: 36.740982
        max: 73.481964
      per_m2:
        min: 131.825546
        max: 263.651092
      per_m2_day:
        min: 1.098546
        max: 2.197092
    - nutrient_id: usda:1258
      unit: g
      total:
        min: 0.102058
        max: 0.204117
      per_m2:
        min: 0.366182
        max: 0.732364
      per_m2_day:
        min: 0.003052
        max: 0.006103
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
        min: 0.008165
        max: 0.016329
      per_m2:
        min: 0.029295
        max: 0.058589
      per_m2_day:
        min: 0.000244
        max: 0.000488
    - nutrient_id: usda:1293
      unit: g
      total:
        min: 0.171458
        max: 0.342916
      per_m2:
        min: 0.615186
        max: 1.230372
      per_m2_day:
        min: 0.005127
        max: 0.010253
    - nutrient_id: usda:1269
      unit: g
      total:
        min: 0.130635
        max: 0.261269
      per_m2:
        min: 0.468713
        max: 0.937426
      per_m2_day:
        min: 0.003906
        max: 0.007812
    - nutrient_id: usda:1270
      unit: g
      total:
        min: 0.040823
        max: 0.081647
      per_m2:
        min: 0.146473
        max: 0.292946
      per_m2_day:
        min: 0.001221
        max: 0.002441
    - nutrient_id: usda:1210
      unit: g
      total:
        min: 0.085729
        max: 0.171458
      per_m2:
        min: 0.307593
        max: 0.615186
      per_m2_day:
        min: 0.002563
        max: 0.005127
    - nutrient_id: usda:1211
      unit: g
      total:
        min: 0.273516
        max: 0.547032
      per_m2:
        min: 0.981368
        max: 1.962736
      per_m2_day:
        min: 0.008178
        max: 0.016356
    - nutrient_id: usda:1212
      unit: g
      total:
        min: 0.269434
        max: 0.538868
      per_m2:
        min: 0.966721
        max: 1.933441
      per_m2_day:
        min: 0.008056
        max: 0.016112
    - nutrient_id: usda:1213
      unit: g
      total:
        min: 0.400068
        max: 0.800137
      per_m2:
        min: 1.435434
        max: 2.870867
      per_m2_day:
        min: 0.011962
        max: 0.023924
    - nutrient_id: usda:1214
      unit: g
      total:
        min: 0.436809
        max: 0.873619
      per_m2:
        min: 1.567259
        max: 3.134519
      per_m2_day:
        min: 0.01306
        max: 0.026121
    - nutrient_id: usda:1215
      unit: g
      total:
        min: 0.130635
        max: 0.261269
      per_m2:
        min: 0.468713
        max: 0.937426
      per_m2_day:
        min: 0.003906
        max: 0.007812
    - nutrient_id: usda:1217
      unit: g
      total:
        min: 0.330669
        max: 0.661338
      per_m2:
        min: 1.18643
        max: 2.37286
      per_m2_day:
        min: 0.009887
        max: 0.019774
    - nutrient_id: usda:1219
      unit: g
      total:
        min: 0.42048
        max: 0.84096
      per_m2:
        min: 1.50867
        max: 3.01734
      per_m2_day:
        min: 0.012572
        max: 0.025145
    - nutrient_id: usda:1221
      unit: g
      total:
        min: 0.142882
        max: 0.285763
      per_m2:
        min: 0.512655
        max: 1.02531
      per_m2_day:
        min: 0.004272
        max: 0.008544
---

# Potato food-yield scenario

**Illustrative calculation, not an observed harvest or a cultivar forecast.**

The source gives 1–2 lb per row foot.[^maine-potato] For this scenario only, allocate a three-foot row spacing, retain 90% as food with flesh and skin, and assume 120 days. These choices are not a measured trial, a source-specified duration, or a source-specified edible fraction. The area is 0.27870912 m² for the one-foot row segment.

Use the [food profile](../food/potato-raw.md) for composition.[^composition] Apply the [method](../methods/estimate-food-yield.md) to [potato](../crops/potato.md).

## Energy result

- Total: 314.34–628.679 kcal.
- Per area: 1127.84–2255.68 kcal/m² for the stated period.
- Per area-day: 9.39867–18.7973 kcal/m²/day.

Frontmatter carries the same calculation for each reported nutrient. Raw food-energy estimates do not account for preparation losses or added ingredients. Neither these scenarios nor their daily normalization establish annual productivity; do not rank the crops by agronomic performance using these unequal assumptions.

[^composition]: [Potatoes, flesh and skin, raw](/food/potato-raw.md).
[^maine-potato]: [Bulletin 2077: Growing Potatoes in the Home Garden](https://extension.umaine.edu/publications/2077e/).
