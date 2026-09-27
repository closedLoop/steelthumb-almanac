---
name: okf-spec
description: Reference the Open Knowledge Format specification when creating or reviewing OKF bundles, concept Markdown, frontmatter, source attribution, or conformance in the Almanac.
---

# Open Knowledge Format reference

Use the [official OKF specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) ([raw text](https://raw.githubusercontent.com/GoogleCloudPlatform/open-knowledge-format/main/SPEC.md)). Version 0.2 was consulted on 2026-09-27. The main branch can change: record the version or commit used for implementation and validation.

## Workflow

Establish the bundle root and intended version before editing concepts. Read the relevant upstream sections; if unavailable, identify the checks that remain unresolved. Keep repository administration and skills outside the selected bundle boundary.

Consult these specification sections as needed:

- §§3–4: bundle structure, reserved filenames, and concept frontmatter. Concepts are Markdown with YAML; `type` is the only always-required key. `index.md` and `log.md` are reserved.
- §5: sources, generation, verification, and lifecycle. Source entries require `resource`; claim footnote labels join to source `id` values. Record verification only when it happened.
- §§6–7: paths and actor identities. Concept IDs are bundle-relative paths without `.md`; distinguish bundle-root links from filesystem paths.
- §§8–9, §12: index, log, and version declaration conventions.
- §10: additional requirements for Attested Computation concepts.
- §11: producer and consumer conformance. Preserve unknown metadata during edits and distinguish missing knowledge links from malformed documents.

## Almanac application

Choose crop and procedure fields from actual gardening needs, labeling them as project extensions. Keep source evidence and local observations distinguishable. Use a focused example to establish a new convention before applying it throughout the collection.

Review YAML structure, link resolution, claim attribution, and the applicable conformance requirements. Report specification violations separately from project recommendations and content-evidence gaps; claim only the validation actually performed.

For explicit process lineage or PROV exports, read the sibling [prov-spec skill](../prov-spec/SKILL.md) and document the mapping independently.
