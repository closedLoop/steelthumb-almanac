# Citation refresh and standalone bundle review

Reviewed by Codex on 2026-09-27. This working-tree review supersedes the initial entity assessment's unreviewed-fidelity ratings. See the [current per-entity assessment](okf-entity-review.md), [rubric](../../.agents/skills/build-crop-knowledge/references/RUBRIC.md) and [machine-readable citation ledger](citation-fidelity.json).

## Scope and findings

All 171 embedded claims in 66 Markdown documents (65 concepts plus index) were compared with cited source passages. The ledger retains source URLs, passage locators, access dates, manual verdicts, claim hashes and document hashes. Optional retrieved-text hashes identify transient retrievals, not a bundled archive or permanent source snapshot. Prose and cards were reviewed for consequential settings and agreement with task owners; that sampling is not a complete second independent audit of every sentence. A supported claim remains limited to its documented crop, region, method and units.

- Basil guidance now cites direct gardening sources. Outdoor and indoor sowing routes remain distinct; container care, transplanting, propagation, harvest, downy-mildew checks, seed saving and dehydration have supported instructions. Unsupported design settings were removed. Rockwool remains an explicit planning checklist.
- Named packet routes supply dimensions and density for Sugar Ann snap peas, Little Firebirds nasturtium and Junior sunflowers. Their pot-to-fabric adaptation is editorial, not evidence from a fabric-container trial. Mint uses a sourced general container class, not an established optimum.
- Sweet-potato curing selects a coherent MSU temperature/humidity/duration route. The USU alternative is retained separately rather than mixing conditions.
- Citrus watering now cites Maryland for thorough watering and drainage; the earlier UC passage supported only part of the sentence. Tomato dimensions explicitly represent minimum recommendations, not upper size limits. Unsupported wording about sweet-potato skin handling was removed.
- Crop entries, procedures and the index no longer require knowledge of a predecessor project. Migration history, retired assumptions and uninspected video leads live in contributor research files. Required copyright attribution remains in a separate bundled legal notice.

## Unresolved decisions

Long-term fabric-container citrus performance, exposed-bag winter survival and crop-specific yield remain unestablished. Nursery scion/rootstock information and local trials would be needed to narrow these claims. No field outcomes are invented.

Sunflower food-seed drying still lacks a selected home-scale measured endpoint. [Oregon State's seed-drying publication](https://extension.oregonstate.edu/catalog/sp-50-534-drying-roasting-seeds) separates sunflower handling from pumpkin/squash; the latter's crispness instruction must not be transferred to sunflower. [Texas A&M's production guide](https://sanangelo.tamu.edu/agronomy/agronomy-publications/sunflower-production-guide/) describes commercial moisture measurement and storage distinctions. Those conditions do not establish a home drying protocol. Identify seed use/type and a suitable measurement method before claiming storage readiness.

Some variety traits remain sourced prose rather than embedded claims; some compound claims lack separate quantity fields for every number. Further semantic normalization is appropriate before those facts are reused independently. Passing the structural checker does not resolve these gaps.

## Checks

- Bundle checker: 66 documents, 171 claims, 628 local references; repeated on an isolated copy.
- Citation-ledger checker with `--require-complete`: all 171 embedded claims have scoped manual verdicts; no stale snapshots or missing reviews.
- Six citation-ledger regression tests plus ten bundle-checker tests: passed. Negative cases include changed prose, changed claims, source substitution, missing review and an uninspected evidence edge.
- Relative links, metadata and whitespace checked. No formal full OKF conformance certification, consumer integration test, field validation or publication was performed.

The authoring skill was useful for separating crop cards from authoritative task claims and for retaining uncertainty. Its earlier output exposed two weaknesses: a bibliography can look stronger than its actual claim support, and historical source organization can leak into user guidance. The standalone requirement, explicit task rubric and passage ledger now address those failure modes. Human judgment remains necessary for source applicability and task completeness.
