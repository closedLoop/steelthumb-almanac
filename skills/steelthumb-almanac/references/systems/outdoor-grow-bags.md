---
type: GrowingSystem
title: Outdoor grow bags
description: A shared fabric-container arrangement with crop-specific establishment and care links.
status: draft
sources:
- id: umd-container
  title: Types of Containers for Growing Vegetables — Maryland Extension
  resource: https://extension.umd.edu/resource/types-containers-growing-vegetables
- id: umd-medium
  title: Growing Media (Potting Soil) for Containers — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-media-potting-soil-containers
- id: umd-location
  title: Growing Vegetables in Containers — Maryland Extension
  resource: https://extension.umd.edu/resource/growing-vegetables-containers
steelthumb:
  ontology_version: '0.2'
  license: MIT
  claims:
  - id: drainage
    kind: recommendation
    statement: Containers need unobstructed drainage; gravel beneath the medium does not improve it.
    applicability:
      conditions: General containers, including bag adaptation.
    evidence:
    - source_id: umd-container
      relation: supports
      locator: Container drainage
  - id: medium
    kind: recommendation
    statement: Use an aerated container mix and moisten it thoroughly before planting.
    applicability:
      conditions: General potting media.
    evidence:
    - source_id: umd-medium
      relation: supports
      locator: Growing media functions; Commercial soilless mixes
  - id: site-water
    kind: recommendation
    statement: Choose a site with accessible water and consider reflected heat from hard surfaces.
    applicability:
      conditions: Outdoor containers.
    evidence:
    - source_id: umd-location
      relation: supports
      locator: Best location for a container garden
---

# Outdoor grow bags

This arrangement is a freestanding fabric container holding growing medium. It is not a raised bed, a shallow commercial compost sack, or a claim that one bag size suits every crop. Crop procedures own planting density, crop moisture needs, and support choices.

## Setup principles

<a id="drainage"></a>
Containers need unobstructed drainage; gravel beneath the medium does not improve it.[^umd-container]

<a id="medium"></a>
Use an aerated container mix and moisten it thoroughly before planting.[^umd-medium]

<a id="site-water"></a>
Choose a site with accessible water and consider reflected heat from hard surfaces.[^umd-location]

For fabric drying behavior and its source, see the [existing fabric-container claim](jerusalem-artichoke-grow-bags.md#fabric-drying). Use the crop's care procedure to decide when to water; a daily inspection need not mean daily irrigation.

## Record the actual arrangement

These are editorial setup and observation prompts:

- Record actual filled width, usable depth, volume if known, fabric type, medium, cultivar, and plant count. Preserve the seller's gallon convention rather than guessing a conversion.
- Plan supports for climbing or tall crops without relying on a flexible rim. Check the filled bag's stability and drainage before planting.
- If containment matters, keep the base and surroundings inspectable. Fabric is not established here as a permanent barrier to mint or tuber crops.
- Retain access for harvest and, for perennial plants, repotting or moving to winter shelter. Neither portability when empty nor in-ground hardiness proves these will work when the bag is full.

## Applicability and gaps

The [bundle index](../index.md) links each crop to its ground and bag branches. Pot guidance transferred to fabric is identified as an adaptation unless the source explicitly addresses bags. No crop inherits an optimal volume, yield, fertilizer dose, or overwintering temperature from this shared system. Container suitability is distinct from proof of a particular fabric product's performance.

[^umd-container]: [Types of Containers for Growing Vegetables — Maryland Extension](https://extension.umd.edu/resource/types-containers-growing-vegetables).
[^umd-medium]: [Growing Media (Potting Soil) for Containers — Maryland Extension](https://extension.umd.edu/resource/growing-media-potting-soil-containers).
[^umd-location]: [Growing Vegetables in Containers — Maryland Extension](https://extension.umd.edu/resource/growing-vegetables-containers).
