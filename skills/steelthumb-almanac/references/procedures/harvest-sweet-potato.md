---
type: Procedure
title: Harvest and cure sweet potatoes
description: Ipomoea batatas for storage roots in warm-season beds or outdoor grow bags; cultivar unspecified.
status: draft
sources:
- id: sweet-bags
  title: Try Growing Sweet Potatoes This Year! — Maryland Grows
  resource: https://marylandgrows.umd.edu/2023/04/21/try-growing-sweet-potatoes-this-year/
- id: usu-sweet
  title: How to Grow Sweet Potatoes in Your Garden — Utah State University
  resource: https://extension.usu.edu/yardandgarden/research/sweet-potatoes-in-the-garden
- id: umd-sweet
  title: Growing Sweet Potatoes in a Home Garden — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-sweet-potatoes-home-garden
- id: msu-sweet
  title: Growing Sweet Potatoes at Home — Mississippi State Extension, Publication 2784
  resource: https://extension.msstate.edu/publications/growing-sweet-potatoes-home
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: before-frost
    kind: recommendation
    statement: Maryland advises harvesting eating-size sweet-potato roots before frost, without washing.
    applicability:
      conditions: Maryland home gardens.
    evidence:
    - source_id: sweet-bags
      relation: supports
      locator: Harvesting tips
  - id: cure
    kind: recommendation
    statement: USU cures sweet-potato roots at 80°F.
    applicability:
      conditions: Utah home-garden guidance; humidity unspecified.
    evidence:
    - source_id: usu-sweet
      relation: supports
      locator: How to Harvest and Store
    quantity:
      property: curing_temperature
      unit: degF
      value: 80
      basis: Humidity unspecified.
  - id: cure-duration
    kind: recommendation
    statement: USU maintains that cure for 1–2 weeks.
    applicability:
      conditions: Utah home-garden guidance; humidity unspecified.
    evidence:
    - source_id: usu-sweet
      relation: supports
      locator: How to Harvest and Store
    quantity:
      property: curing_duration
      unit: wk
      min: 1
      max: 2
  - id: storage
    kind: recommendation
    statement: USU follows curing with storage at 50–55°F.
    applicability:
      conditions: Post-curing roots; source describes a cool, dry location.
    evidence:
    - source_id: usu-sweet
      relation: supports
      locator: How to Harvest and Store
    quantity:
      property: storage_temperature
      unit: degF
      min: 50
      max: 55
  - id: cure-msu
    kind: recommendation
    statement: Cure immediately after harvest at 80–85°F and 85–90% relative humidity for 7–10 days.
    applicability:
      conditions: Mississippi home-garden guidance; keep this complete method separate from USU.
    evidence:
    - source_id: msu-sweet
      relation: supports
      locator: Curing
  - id: storage-msu
    kind: recommendation
    statement: After curing, store sweet potatoes in darkness at 55–60°F; do not refrigerate raw roots.
    applicability:
      conditions: Mississippi guidance; different lower temperature limit from USU.
    evidence:
    - source_id: msu-sweet
      relation: supports
      locator: Storage
  relations:
  - predicate: applies_to
    target: /crops/sweet-potato.md
  - predicate: applies_to
    target: /systems/outdoor-grow-bags.md
---

# Harvest and cure sweet potatoes

Applies to [sweet potato](../crops/sweet-potato.md). Ipomoea batatas for storage roots in warm-season beds or outdoor grow bags; cultivar unspecified.

[Outdoor grow bags](../systems/outdoor-grow-bags.md) describes the shared setup and adaptation limits.

## Before you start

Have gentle lifting tools, a sorting surface for bags, labelled containers, and a thermometer plus hygrometer for curing/storage.

## Steps and source settings

1. Inspect a sample root for usable size near the cultivar’s expected harvest; follow the before-frost branch below.
2. Loosen soil away from the roots, or open a bag onto a contained surface; lift and sort without scraping. The bag-handling adaptation is editorial.
3. Separate damaged roots and record actual curing conditions using the selected Mississippi route below.
4. Move cured roots to the stated storage conditions and retain their harvest identity.

<a id="before-frost"></a>
Maryland advises harvesting eating-size sweet-potato roots before frost, without washing.[^sweet-bags]

<a id="cure"></a>
USU cures sweet-potato roots at 80°F.[^usu-sweet]

<a id="cure-duration"></a>
USU maintains that cure for 1–2 weeks.[^usu-sweet]

<a id="storage"></a>
USU follows curing with storage at 50–55°F.[^usu-sweet]

## Follow-up

Inspect for deterioration, remove spoiled roots, and record losses.[^sweet-bags] Record fresh edible root mass separately from vine biomass or damaged roots.

## Limits

USU also discusses harvest after frost damages foliage, while Maryland advises before frost; this procedure selects the earlier branch. Maryland describes a warmer, more humid commercial cure.[^umd-sweet] Do not combine temperature from one method with duration from another and call it tested. No guaranteed shelf life or preservation recipe is supplied.

[Evidence scope and source context](../sources/garden-crop-research.md).


## Selected complete curing route

Use the Mississippi route below when temperature and relative humidity can be measured and maintained. Have a thermometer and hygrometer ready before harvest. Log both conditions throughout curing and record departures; an unmonitored warm room does not establish that the cure was achieved. Inspect stored roots for deterioration as described above.

This route is selected because it specifies temperature, humidity and duration together. The older USU claims above remain traceable alternatives; their 50–55°F storage range differs from Mississippi's 55–60°F. Do not average the ranges or attach Mississippi humidity to USU duration. Local storage constraints remain a planning input, not evidence that these conditions were met.

<a id="cure-msu"></a>
Cure immediately after harvest at 80–85°F and 85–90% relative humidity for 7–10 days.[^msu-sweet]

<a id="storage-msu"></a>
After curing, store sweet potatoes in darkness at 55–60°F; do not refrigerate raw roots.[^msu-sweet]


[^sweet-bags]: [Try Growing Sweet Potatoes This Year! — Maryland Grows](https://marylandgrows.umd.edu/2023/04/21/try-growing-sweet-potatoes-this-year/).
[^usu-sweet]: [How to Grow Sweet Potatoes in Your Garden — Utah State University](https://extension.usu.edu/yardandgarden/research/sweet-potatoes-in-the-garden).
[^umd-sweet]: [Growing Sweet Potatoes in a Home Garden — Maryland Extension](https://extension.umd.edu/resource/growing-sweet-potatoes-home-garden).

[^msu-sweet]: [Growing Sweet Potatoes at Home — Mississippi State Extension, Publication 2784](https://extension.msstate.edu/publications/growing-sweet-potatoes-home).
