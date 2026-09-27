---
type: Growing System
title: "Indoor basil parameter assumptions"
status: draft
sources:
  - id: steelthumb-tasks
    resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  - id: steelthumb-environment
    resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/environment/SPEC.md
  - id: steelthumb-procedural
    resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/procedural.md
steelthumb:
  review_status: unreviewed-import
  license: CC-BY-SA-4.0
  imported_on: "2026-09-27"
---

# Indoor basil parameter assumptions

These values preserve the original project’s assumptions for review; they are not established crop requirements. Cultivar, lamp output, fertilizer formulation, and source support are missing. The numeric state-space bounds in the simulator are implementation limits, not biological tolerance ranges.

| Parameter | Imported assumption | Origin |
| --- | --- | --- |
| Rockwool conditioning | pH 5.5–6.0, soak 15–30 minutes | Task condition_rockwool[^steelthumb-tasks] |
| Soil pH target | 6.0–6.5 | Environment §1.1[^steelthumb-environment] |
| Germination lighting | Approximately 6 inches (15 cm); 14 hours on, 10 off | Task setup_germination_tray[^steelthumb-tasks] |
| Container medium | 80% soil / 20% perlite; proportion basis unspecified | Task transplant_cube_to_pot[^steelthumb-tasks] |
| Vegetative temperature | Approximately 65–75°F (18–24°C) | Task temperature_rh_monitoring[^steelthumb-tasks] |
| Harvest limit | At most one third of canopy per session | Task prune_weekly[^steelthumb-tasks] |
| Fertilizer schedule A | Half label strength, monthly; establishment check at 10–14 days | Tasks half_strength_fertilization and early_establishment_check[^steelthumb-tasks] |
| Fertilizer schedule B | Full strength, 200 ml, after at least 14 days since last feeding | Environment transition table[^steelthumb-environment] |
| Rooted-cutting readiness A | At least 2 cm roots | Procedural §5[^steelthumb-procedural] |
| Rooted-cutting readiness B | 1–2 inches roots | Procedural §6.4 and task root_cutting_in_water[^steelthumb-procedural][^steelthumb-tasks] |

The feeding schedules and rooting thresholds disagree. Retain both until source review establishes their applicability. Lamp distance alone does not specify measured light output. No missing cultivar, concentration, measurement basis, or uncertainty has been inferred during migration.

[Procedure drafts](procedure-drafts.md) retain the full instruction text. SteelThumb owns the simulation, controller assumptions, and execution criteria; reviewed Almanac knowledge can later support explicit revisions to them.

[^steelthumb-tasks]: Original task catalog; task IDs locate the extracted assumptions.
[^steelthumb-environment]: Original state-space specification, Soil/Growing Medium and state transition table.
[^steelthumb-procedural]: Original procedural design; sections 0, 5, and 6.4.
