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

## Basil knowledge and published field reports

The [installable basil profile](../skills/steelthumb-almanac/references/crops/basil.md) links to refactored crop guidance, complete procedures, a system description, guides, and source records. Documentary origins, historical source hashes, and the source documentation license remain in the [attribution record](../skills/steelthumb-almanac/references/sources/steelthumb-basil.md). These drafts remain unreviewed; their inclusion is not a conformance or horticultural verification claim. The old import folder has been removed; [coverage notes](basil-refactor.md) identify replacements. Robot procedural design lives in SteelThumb’s `steelthumb_v1_basil/environment/PROCEDURES.md`; task templates and environment models remain operational definitions there.

A `FieldReport` is a selected published evidence account owned by Almanac, with contributor permission, applicability, actual steps, outcomes, and procedure revision references. It does not transfer the underlying operational journal, action schema, or experiment ledger into this repository. See the [evidence contract](evidence.md) and [contribution process](../CONTRIBUTING.md). No real reports are supplied by the basil source compilation.
