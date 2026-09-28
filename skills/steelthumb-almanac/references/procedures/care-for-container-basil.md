---
type: Procedure
title: Care for container basil
description: Observe moisture, light, feeding, and sanitation with explicit unresolved assumptions.
status: draft
sources:
- id: tasks
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  title: SteelThumb task instruction templates
- id: environment
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/environment/SPEC.md
  title: SteelThumb environment specification
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  claims:
  - id: task-feeding-assumption
    kind: descriptive
    statement: The task catalog specifies monthly feeding at half label strength.
    evidence:
    - source_id: tasks
      relation: supports
      locator: half_strength_fertilization
    applicability:
      conditions: Original indoor task assumption; fertilizer unspecified.
  - id: environment-feeding-assumption
    kind: descriptive
    statement: The environment transition table specifies full-strength feeding of 200 ml after at least
      fourteen days.
    evidence:
    - source_id: environment
      relation: supports
      locator: State transition table
    applicability:
      conditions: Original simulator transition assumption; fertilizer unspecified.
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Care for container basil

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Maintain basil in the [indoor container arrangement](../systems/indoor-basil-containers.md). The earlier task catalog supplies draft care steps; it contains no observed outcomes.[^tasks]

## Routine

1. Observe medium moisture and plant condition before watering. The task uses dryness in the top inch (about 2–3 cm) as a trigger and waters to slight runoff, draining the saucer within ten minutes. This is an unreviewed rule for an unspecified medium.[^tasks]
2. Check lighting, airflow, and temperature. The task suggests vegetative temperatures around 65–75°F (18–24°C), lamp distance of 6–12 inches for established plants, and gentle airflow. Record actual measurements; equipment details remain missing.[^tasks]
3. Observe stretching or leaning before changing light placement. Pot rotation by 90 degrees appears in several tasks; consolidate it into one recorded action, rather than counting duplicate instructions as separate evidence.[^tasks]
4. Choose feeding only after resolving the product, concentration, medium, and plant context. The source schedules below disagree; this document selects neither.[^tasks][^environment]
5. Clear debris and clean tools using a suitable method. The original sanitation task specifies alcohol wipes without concentration or contact time; those details require a supported product/method before use.[^tasks]

## Conflicting feeding assumptions

| Source | Earlier instruction | Missing applicability |
| --- | --- | --- |
| Task catalog | Half label strength monthly; no feeding during the initial 10–14-day establishment check | Product, concentration, medium nutrient content, and plant response |
| Environment transition table | Full strength, 200 ml, after at least 14 days since previous feeding | Product, concentration, container/plant size, and empirical basis |

<a id="task-feeding-assumption"></a>
The task catalog specifies monthly feeding at half label strength.[^tasks]

<a id="environment-feeding-assumption"></a>
The environment transition table specifies full-strength feeding of 200 ml after at least fourteen days.[^environment]

## Follow-up and troubleshooting

Record dates, measured amounts, product formulation, before/after condition, and simultaneous changes. A salt-crust task proposes flushing with 2–3 pot volumes of water; this remains an unreviewed intervention requiring confirmation of the medium and problem, not a response automatically justified by a visible crust.[^tasks]

Use [symptom investigation](investigate-basil-symptoms.md) for yellowing, pests, or suspected disease. Leaf rinsing, soap application, nutrient supplements, and altered humidity are interventions whose suitability must be established separately.

This consolidates `routine_watering`, `half_strength_fertilization`, `leach_salts`, `adjust_light_distance`, `monthly_light_position_maintenance`, `rotate_pot`, `temperature_rh_monitoring`, and `sanitation_cycle`.[^tasks]

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^tasks]

[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
[^environment]: [SteelThumb environment specification](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/environment/SPEC.md).
