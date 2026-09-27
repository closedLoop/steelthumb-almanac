# Basil and potato ontology examples

Start at the [example bundle index](bundle/index.md). These 18 draft concepts exercise the [proposed ontology v0.2](../ontology.md). They are maintained separately from the installable bundle while the ontology is being explored. They are reusable reference examples; garden operations and experiments belong to SteelThumb under the [repository ownership guide](../repository-boundaries.md).

## What is represented

| Crop | Cultivars | Shared procedures | Food composition |
| --- | --- | --- | --- |
| [Basil](bundle/crops/basil.md) | Genovese, Siam Queen, Rutgers Devotion DMR | Outdoor sowing; repeated leaf harvest | Fresh basil, generic cultivar scope |
| [Potato](bundle/crops/potato.md) | Yukon Gold, Russet Burbank, Red Norland | Seed-tuber planting; mature harvest | Raw flesh and skin; boiled flesh cooked in skin without salt |

Procedures reference the crop once and can serve multiple cultivars. Cultivar profiles preserve specific claims rather than copying a whole growing guide. “Thai basil” and “russet” are not treated as uniquely identifying one cultivar.

The Yukon Gold document preserves a real maturity-classification disagreement between Illinois and Maine Extension. Neither source establishes a common numeric maturity baseline here. The example retains both assertions rather than selecting an unsupported universal days-to-harvest value.

## Nutrition

These are food-composition values per **100 g of the stated edible food**, not per plant, per harvest, or a usual serving. The three profiles use USDA FoodData Central SR Legacy records; cultivar-specific composition is unknown.

| Component | Fresh basil | Raw potato, flesh and skin | Boiled potato flesh, cooked in skin, no salt |
| --- | ---: | ---: | ---: |
| Energy, kcal | 23 | 77 | 87 |
| Protein, g | 3.15 | 2.05 | 1.87 |
| Carbohydrate by difference, g | 2.65 | 17.49 | 20.13 |
| Total fat, g | 0.64 | 0.09 | 0.10 |
| Dietary fiber, g | 1.6 | 2.1 | 1.8 |
| Potassium, mg | 295 | 425 | 379 |
| Vitamin C, mg | 18 | 19.7 | 13 |
| Vitamin K (phylloquinone), µg | 414.8 | 2 | 2.2 |

Sources: [USDA basil, FDC 172232](https://fdc.nal.usda.gov/food-details/172232/nutrients), [USDA raw potato, FDC 170026](https://fdc.nal.usda.gov/food-details/170026/nutrients), [USDA boiled potato flesh, FDC 170438](https://fdc.nal.usda.gov/food-details/170438/nutrients). Original API records are archived in [the data directory](bundle/references/data/). These are historical reference foods, not newly collected samples; see [USDA data-type documentation](https://fdc.nal.usda.gov/data-documentation/).

The individual food profiles also carry calcium, iron, magnesium, phosphorus, sodium, zinc, copper, manganese, selenium, B vitamins, vitamins A/E/D, choline, sugars, starch where reported, selected fatty acids, essential amino acids, beta-carotene, and lutein/zeaxanthin. The nutrient panel is selective and records upstream nutrient IDs and units. Missing basil starch is explicitly `null`, not zero. Resistant starch, total polyphenols, bioavailability, and cultivar-specific assays remain evidence gaps.

Raw and cooked values describe different food parts and states. Their difference does not measure cooking retention. Serving comparisons require a stated serving mass, and dietary adequacy would require a separate intake question and appropriate reference values.

## Caloric and nutrient yield

The [yield method](bundle/methods/estimate-food-yield.md) uses matching edible mass and composition. Each scenario calculates every reported nutrient, as well as energy.

| Scenario | Inputs and assumptions | Estimated energy |
| --- | --- | --- |
| [Basil](bundle/yields/basil-scenario.md) | Invented 500 g retained fresh material, five cuts, 1 m², 90 days | 115 kcal total; 115 kcal/m² over the stated period |
| [Potato](bundle/yields/potato-scenario.md) | Sourced 1–2 lb per row foot; assumed 3 ft row spacing, 90% retained food, 120 days | About 314–629 kcal for the row segment; 1,128–2,256 kcal/m² over the stated period |

The potato mass range comes from [Maine Extension's home-garden bulletin](https://extension.umaine.edu/publications/2077e/), not a cultivar trial. Both calculations are scenarios. They are not observed harvests, annual yield forecasts, or a controlled comparison of the crops. The period and loss assumptions are explicit. Daily normalization does not establish repeatable annual production.

## Changes the examples required

- Added `FoodProfile` to separate part/preparation-specific composition from crop identity.
- Added `YieldEstimate` to separate calculated output from food energy density and observed harvests.
- Identified the need for `PlantingMaterialLot` and `from_material_lot` so seed tubers are not misrepresented as true seed; these now belong to SteelThumb's operational model.
- Defined nutrient identity, source fidelity, unknown versus zero, edible losses, and area/time accounting.
- Preserved maturity disagreement and generic nutritional proxies instead of silently inheriting values into cultivars.

The examples cover reusable crop knowledge and worked calculations. Actual planting-material lot records, dated garden observations, operational schedules, and experiment traces belong to SteelThumb. A complete care reference and a PROV export remain outside this example set.

## Check the examples

With Python 3.9+ and PyYAML available, run from the repository root:

```bash
python docs/ontology-examples/check.py
```

The checker validates local bundle links, source and claim references, the selected nutrient values against archived USDA records, food-state matching, mass and area conversions, all yield results, and multiple cultivar/procedure coverage. It does not validate full OKF or PROV conformance, botanical accuracy, or external link availability. External extension guidance is summarized and linked, not copied as a local manual.
