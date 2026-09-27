# Repository ownership

## SteelThumb Almanac

This repository owns reusable growing knowledge: crop and cultivar profiles, procedures, growing systems, symptoms and problems, measurement methods, food profiles, claims, sources, and contextualized evidence. Its [ontology](ontology.md) describes those reference concepts.

The [basil and potato examples](ontology-examples/README.md) remain here as reusable reference examples. Their synthetic yield calculations demonstrate an accounting method; they are not a particular garden's records or a policy benchmark. The [distribution guide](distribution.md) defines the installable bundle and its packaging.

## SteelThumb

The [SteelThumb garden-intelligence folder](https://github.com/closedloop-technologies/steelthumb/tree/main/docs/garden-intelligence) owns:

- Garden operations: locations, plantings, material lots, observations, plans, execution, labor, resources, harvest batches, and inventories.
- Experiments: model configurations, scenarios, policies, runs, evaluation, shocks, and field trials.
- RL gym and simulator research, moved out of this repository's research files.

Its documents are [operations](https://github.com/closedloop-technologies/steelthumb/blob/main/docs/garden-intelligence/operations.md), [experiments](https://github.com/closedloop-technologies/steelthumb/blob/main/docs/garden-intelligence/experiments.md), and the [Almanac interface](https://github.com/closedloop-technologies/steelthumb/blob/main/docs/garden-intelligence/almanac-interface.md). Actual private records and large run artifacts live in configured user/experiment workspaces; schema ownership does not imply publishing those records to Git.

## References and evidence exchange

SteelThumb consumes a pinned Almanac source revision, bundle path, and concept/claim identity. Food calculations additionally preserve the composition record and snapshot. A local installation path is not a durable knowledge identifier.

Reviewed findings may return as source-backed Almanac contributions, preserving conditions, uncertainty, simulation/observation status, and reuse terms. The public bundle stays independently usable, with no dependency on private garden data or an RL runtime.

This reorganization was made in local checkouts on 2026-09-27. Cross-repository GitHub links are publication destinations and become available after the corresponding changes are committed and pushed. No publication is implied by this document.

## Migrated basil collection

The [installable basil collection](../skills/steelthumb-almanac/references/basil/index.md) owns the former SteelThumb cultivation reference, teaching guide, and video research, plus extracted procedure drafts and growing assumptions. Original citations, source hashes, and the source documentation license are preserved. These imports remain unreviewed; their inclusion is not a conformance or horticultural verification claim. Robot procedural design now lives in SteelThumb’s `steelthumb_v1_basil/environment/PROCEDURES.md`; task templates and environment models remain operational definitions there. No old-path compatibility copies are retained.
