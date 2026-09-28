# SteelThumb ontology

Status: v0.2 reference authoring model, 2026-09-27. Core types and embedded claims are used by the refactored installed basil collection; the wider vocabulary remains an evolving proposal, not a complete implemented schema or conformance claim. The [domain glossary](../CONTEXT.md) defines the reference language. The adopted [evidence contract](evidence.md) adds field reports, revision references, and scoped reviews. The [basil and potato examples](ontology-examples/README.md) exercise additional types with sourced guidance, food composition, and explicitly modeled yield scenarios. See [repository ownership](repository-boundaries.md) for garden operations and experiments maintained in SteelThumb.

## Purpose and scope

The ontology should answer:

- What plant does this guidance describe, and does it apply to this cultivar and setting?
- What can a gardener do, and what should they observe afterward?
- Which source supports a particular value or recommendation?
- Where do sources disagree, and could conditions explain the difference?
- What contextualized observations or trials support this reusable guidance?

Reusable knowledge belongs in the public Almanac. SteelThumb owns operational records for particular gardens and experiment runs. Publication of selected garden evidence is an explicit contribution; it does not transfer ownership of the underlying private journal or run ledger to Almanac.

This is a lightweight domain ontology expressed through OKF documents and project metadata. It does not require an RDF database or OWL inference.

## Document types

These exact `type` strings are SteelThumb vocabulary, not types mandated by OKF. Core types are used in the installed bundle; other proposed types are exercised in examples or await content. A type describes the document's primary subject; tags provide additional grouping.

### Shared reference

| Type | Represents | Distinction |
| --- | --- | --- |
| `Crop` | A cultivated plant category and reusable growing profile | A practical crop category need not equal one botanical species |
| `Taxon` | A botanical classification with rank and scientific name | Create when identity needs a separate reference; do not require one per crop initially |
| `Cultivar` | A named cultivated selection | Keep separate from botanical rank and supplier product identity |
| `Procedure` | Instructions with purpose, prerequisites, steps, and follow-up | Instructions are not an execution record |
| `GrowingSystem` | A reusable description of a cultivation arrangement | Distinct from a particular bed or container |
| `Symptom` | A recognizable sign or pattern | Describes appearance without assigning a cause |
| `Problem` | A potential cause or harmful condition | May be biotic or abiotic; pest organisms can link to a `Taxon` |
| `MeasurementMethod` | Instructions for observing a property, including units and limitations | Distinct from a measured value |
| `Tool` | Equipment used for growing or measurement | Distinct from the method that uses it |
| `Source` | A citable artifact with attribution and reuse information | It can support several claims without supporting every claim in a document |
| `FieldReport` | A published account of an actual attempt, with observations, outcomes, and limitations | A source of evidence, not the private operational journal or a universal efficacy claim |
| `Guide` | A teaching sequence or cross-cutting reference | Links to maintained procedures; does not duplicate their numeric settings |
| `Claim` | An independently reusable or contested assertion | Usually begin with an embedded claim instead of a separate file |
| `FoodProfile` | Food composition for a specified edible part and preparation state | Generic composition is not a cultivar assay or a harvest forecast |
| `YieldEstimate` | A reusable worked calculation or published estimate of edible mass, energy, or nutrient yield | A particular garden's calculation and inventory ledger belong to SteelThumb |

Uses, harvest characteristics, and lifecycle guidance initially live as claims in relevant crop or procedure documents. Food composition lives in reusable `FoodProfile` documents because multiple cultivars and yield calculations may reference it. Promote other topics to separate concepts when independently reusable; do not create empty type directories.

### External operational model

Garden, planting, material-lot, observation, plan, action, and outcome records are defined in [SteelThumb's operations model](https://github.com/closedloop-technologies/steelthumb/blob/main/docs/garden-intelligence/operations.md). They are not Almanac concept types. This bundle may cite a published observation as a source while leaving the operational record in its owning system.

## Relationships

Represent domain edges as `steelthumb.relations`, a list of `{ predicate, target }` mappings. An edge points from the containing document to its target. Repetition allows multiple targets; deduplicate identical edges.

| Predicate | From → to | Meaning |
| --- | --- | --- |
| `classified_as` | Crop, Cultivar, Problem → Taxon | Botanical identity asserted at the supported rank |
| `cultivar_of` | Cultivar → Crop | Cultivar profile refines a practical crop profile |
| `applies_to` | Procedure, Claim → Crop, Cultivar, GrowingSystem | Stated scope, supplemented by applicability conditions |
| `has_symptom` | Problem → Symptom | A possible manifestation, not a diagnostic implication |
| `investigates` | Procedure → Problem, Symptom | A check intended to distinguish explanations |
| `addresses` | Procedure → Problem | Intended intervention; effectiveness needs its own evidence |
| `uses_tool` | Procedure, MeasurementMethod → Tool | Equipment used by the instructions |
| `describes_food_from` | FoodProfile → Crop, Cultivar | Composition's documented crop or cultivar scope |
| `estimates_yield_of` | YieldEstimate → Crop, Cultivar | Subject of a reusable yield calculation |
| `uses_food_profile` | YieldEstimate → FoodProfile | Composition used in the calculation |
| `uses_method` | YieldEstimate → MeasurementMethod | Method used to calculate values |

Use OKF `sources` for documentary derivation. Do not substitute an `applies_to` relationship for source evidence. Store only the forward edge; reverse relationships can be computed.

Local targets use paths to Markdown documents within the explicitly selected bundle, optionally with a heading fragment. Cross-bundle targets require an explicit resolvable URI and, when reproducibility matters, a revision. Never interpret `/crops/example.md` in a personal bundle as implicitly referring to a separately installed Almanac.

Include readable Markdown links with explanatory prose for important relationships. The metadata supplies typed edges for SteelThumb-aware tools; ordinary readers can still navigate the content. Check that the two representations agree.

## Claims and applicability

Use `steelthumb.claims` for individually supported facts and recommendations. Each embedded claim has an `id` unique within its document, a `statement`, a `kind`, and `evidence`. Kinds are `descriptive`, `recommendation`, or `hypothesis`. A standalone `Claim` document contains one such claim in the same structure.

Each evidence entry contains `source_id`, matching the containing document's `sources[].id`, and `relation`: `supports`, `contradicts`, or `qualifies`. An optional `locator` identifies a page, section, table, or timestamp. Missing evidence is recorded as `evidence: []` and remains an explicit gap, not an endorsement.

Applicability is an optional mapping with `cultivars`, `growth_stages`, `growing_systems`, `climate`, `season`, and `conditions`. Lists of concepts use the same target conventions as relationships. Free-text conditions preserve distinctions that the initial model cannot yet encode. Omitted scope means unspecified, not universal.

For quantitative claims, add `quantity` with a `property`, either `value` or `min`/`max`, and a `unit`. Include `basis` when interpretation depends on it: fresh versus dry mass, edible portion, area, plant count, duration, or starting event. A pH measurement, for example, also needs a method and sampled medium; a number alone is inadequate. Keep categorical statements as statements instead of assigning arbitrary numbers.

Keep separate claims when values disagree. Do not average recommendations merely to produce one quick-reference value. If a selected summary value is useful, identify the selection rationale and preserve its source claims.

Evidence kind belongs to source metadata; verification belongs to the document's OKF metadata. Neither a prestigious source nor a human review guarantees every claim is true. Avoid an unexplained numerical confidence score.

## Frontmatter contract

Use standard OKF fields for their upstream meanings: `type`, `title`, `description`, `tags`, `resource`, `sources`, `generated`, `verified`, `status`, and `stale_after`. Only `type` is universally required by OKF; this proposed profile additionally requires `title` and `steelthumb.ontology_version` for newly authored domain concepts. Index and log files follow their special OKF rules.

Keep project extensions under one `steelthumb` mapping:

| Key | Shape / purpose |
| --- | --- |
| `ontology_version` | String, currently `"0.2"`; earlier drafts used `"0.1"` |
| `relations` | List of typed outgoing edges |
| `claims` | List of individually supported assertions |
| `identity` | Optional names, taxonomic rank, and external identifiers; use only established identity |
| `food` | For food profiles: part, preparation, mass basis, cultivar scope, and nutrient rows |
| `yield` | For estimates: input origin, harvested mass, edible fraction, area, period, matching food profile, formula and results |
| `field_report` | Published attempt summaries, contributors, observations, outcomes, and publication terms; see [evidence contract](evidence.md) |
| `source_revisions` | Source-ID mapping to revision-qualified evidence references |
| `reviews` | Actual scoped checks of identified revisions, including basis, result, and limitations |
| `license`, `review_status` | Reuse notice and explicit editorial review state; neither substitutes for source evidence |

OKF concept identity remains its bundle path without `.md`. Claim IDs are document-local and should be stable across edits. Display titles can change without changing identity. Missing fields mean unknown or unrecorded; an empty list means a list was supplied with no entries. Neither means false.

Use `status` only for document lifecycle. An executed garden task does not change OKF `status` to `completed`; execution state and event times belong to SteelThumb's operational records. Preserve source time precision when citing evidence.

### Illustrative document

The following is a synthetic structural example, not botanical guidance. Its target and source URL are placeholders to be replaced before publication.

```yaml
---
type: Crop
title: Example crop
status: draft
sources:
  - id: example-guide
    resource: https://example.org/growing-guide
    title: Example source
steelthumb:
  ontology_version: "0.2"
  relations:
    - predicate: classified_as
      target: /taxa/example.md
  claims:
    - id: example-guidance
      kind: recommendation
      statement: Follow the source's instructions for the stated growing conditions.
      applicability:
        conditions: Only the setting described in the example source.
      evidence:
        - source_id: example-guide
          relation: supports
          locator: Growing instructions
---
```

In the body, attribute the corresponding sentence with `[^example-guide]` and supply its footnote definition. Claim-level evidence is a project extension; OKF's standard footnotes remain the readable attribution mechanism.

## Food composition and nutritional yield

Food energy belongs to the harvested food; soil fertility and fertilizer nutrition remain separate growing concepts.

A `FoodProfile` names its source food exactly, including edible part, peel/skin handling, preparation, added ingredients, and a mass basis (typically 100 g). Preserve database, food identifier, release/publication information, and a retrieved snapshot. A generic basil or potato record has unspecified cultivar scope; it is not measured evidence about Genovese or Yukon Gold specifically.

Each `steelthumb.food.nutrients` row carries `id`, `name`, `unit`, `value`, `availability`, and `source_id`. `id` preserves the upstream nutrient identifier (for example `usda:1008`). `availability` is `reported` or `not_reported`; the latter requires `value: null`. A reported zero stays zero, with upstream derivation available in the snapshot. It need not mean analytical absence. Keep source precision; do not manufacture uncertainty intervals.

Capture energy; protein, carbohydrate and fat; dietary fiber and sugars; vitamins and minerals; and other measured components such as fatty acids, amino acids, choline, and carotenoids as available. Preserve nutrient forms: folate DFE and total folate, vitamin A RAE and beta-carotene, for example, are distinct entries, not summable substitutes. Missing resistant starch or phytonutrient data remains unknown. Composition alone does not establish bioavailability or a health effect. Serving-size conversions require an explicit serving mass; 100 g is a comparison basis, not an implied typical portion.

Raw, boiled, baked, dried, and oil-containing preparations need separate profiles. Do not calculate cooked-food intake by multiplying a raw harvest mass by cooked-food composition. Use the actual cooked edible mass or a sourced cooking mass-yield conversion. Added ingredients require their own contribution. Do not infer nutrient retention from two unrelated raw/cooked database records.

For matching mass and food states, the basic calculation is:

```text
edible_mass_g = harvested_mass_g × edible_fraction
nutrient_total = edible_mass_g / profile_basis_g × nutrient_per_basis
nutrient_per_m2 = nutrient_total / growing_area_m2
nutrient_per_m2_day = nutrient_per_m2 / period_days
```

Energy uses the same formula with kcal. These are food-energy estimates, not net energy after cultivation costs. Source energy is preferable to reconstructing it by a generic 4/4/9 calculation. A micronutrient total retains the profile's unit; a sum across incompatible nutrients is meaningless.

Every reference yield input records `origin`: `source` or `assumption`, with a source reference when applicable. `basis_kind` is `scenario` or `source_estimate`. A published measured harvest can be cited as a source; a live record with `origin: observation` or `basis_kind: observed_harvest` belongs to SteelThumb. Calculated nutrient output remains an estimate unless assayed. A sourced range is not a confidence interval. State cultivar, system, location, planting density, area definition, and time window when established; preserve missing context as unknown. Never label a one-harvest calculation annual output or a per-row-length figure per-area without row geometry.

The reusable accounting method requires each included harvest to be counted once and each loss deducted once. The reference examples use aggregate harvested mass and an explicit harvest count. Actual harvest events, batch lineage, food destinations, and storage losses are maintained in SteelThumb's operations model, which consumes the method and food profiles.

## PROV alignment

For reference provenance, profile revisions and source artifacts can be PROV entities; editing and reviewing can be activities; people, organizations, and software responsible for those activities can be agents. An editing activity uses sources and generates a revision. Attribution identifies responsibility, while derivation relates entities.

A `Procedure` describes intended work and may map to a PROV plan. Its existence does not establish that anyone executed it. Operational activities, record generation, and experiment runs are mapped in SteelThumb's owning model.

The adopted [evidence contract](evidence.md#project-mapping-to-w3c-prov) makes the project mapping explicit, including relation directions and revision identity. It is not an RDF serialization. Introduce a concrete PROV export only with explicit identifiers, relation direction, and validity checks. Keep source lineage distinct from botanical or causal relationships.

## Review cases

Before adopting a machine-readable schema, exercise these cases with real content:

1. One cultivar has guidance that differs from its crop profile: both claims retain their own scope and evidence; inheritance does not silently overwrite either.
2. A packet and a general guide disagree: distinguish seed-lot instructions from reusable cultivar guidance.
3. A symptom guide describes yellow leaves: keep candidate causes distinct from a confirmed diagnosis.
4. Published evidence reports improvement after an intervention: preserve study conditions without inventing causation.
5. A consumer references guidance for a planting: resolve the pinned reference without importing its private history into Almanac.
6. A document moves between releases: update incoming links or retain an explicit old-path notice; do not silently break identity.
7. Installed knowledge is read alongside a private journal: resolve each bundle's links in its own namespace.

An initial validator should distinguish YAML/OKF errors, SteelThumb profile errors, unresolved links, and evidence gaps. Ontology validation is not factual verification. The example checker validates the example bundle's references, source snapshots, and arithmetic; it is not a general ontology or PROV validator.

## Sources and open decisions

- [OKF v0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md), consulted 2026-09-27: document structure, extensions, identifiers, source attribution, and lifecycle conventions.
- [W3C PROV-DM, 30 April 2013 Recommendation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/): provenance concepts and relationships.
- [Project README](../README.md): gardening scope and observation workflow.

Resolve against further reference examples: controlled growth-stage terms, general unit vocabulary, taxonomic identifier authority, and source-kind vocabulary. The cross-repository reference contract, operational record shapes, and harvest-event design live in [SteelThumb's garden-intelligence folder](https://github.com/closedloop-technologies/steelthumb/tree/main/docs/garden-intelligence). Until resolved, preserve source wording rather than inventing precision. The [basil refactor](basil-refactor.md) applies core authoring conventions inside the existing installed-bundle root; installation paths are unchanged.
