# Claims, field reports, and provenance

Status: adopted authoring convention, 2026-09-27. This extends the [ontology](ontology.md) and [domain glossary](../CONTEXT.md). It defines Markdown/YAML records, not an operational garden database, automatic evidence scoring, or an implemented PROV exporter.

## Knowledge and evidence

Use OKF `sources` and source-keyed footnotes for document derivation and readable attribution. Use `steelthumb.claims` for independently addressable assertions: `id`, `statement`, `kind`, `evidence`, and applicability where known. Each evidence item names a local `sources[].id` through `source_id`, a `relation` (`supports`, `contradicts`, or `qualifies`), and preferably a `locator`.

A source entry showing where text originated is not proof of its horticultural correctness. An unreviewed predecessor can establish “the earlier guide recommended X.” It cannot by itself establish “X is optimal.” Cite underlying evidence where available and disclose when it has not been rechecked.

Keep a claim ID stable while its meaning remains the same. A materially different assertion gets a new ID; record the replacement in prose or revision history. In prose, give important structured claims explicit anchors matching their IDs so a reader can follow a claim link.

## Revision identity

A reproducible local concept reference is `{repository, revision, concept}`: canonical repository URL, full Git commit, and bundle-relative concept path without `.md`. Add `claim_id` when referencing a claim, and `bundle` if the repository contains multiple bundles. Repository URLs alone and branch names such as `main` do not pin content.

For an external source, use a versioned artifact URL when available. The optional project extension `steelthumb.source_revisions` maps a document's source IDs to revision references when a local path would otherwise float with the current checkout. Keep readable `sources[].resource` links as well. A pinned citation identifies the original evidence; a current local link supports navigation.

At contribution time, record the installed revision if known. If it cannot be recovered, use `revision: null` and preserve the supplied instructions or source snapshot with permission. Never substitute today's commit for the unknown version actually used. Changes must preserve old revision references rather than silently repointing them.

## Field reports

`FieldReport` is a source concept about a published firsthand account. Raw actions, measurements, and private journals remain in their owning workspace; a selected public report contains enough context to stand alone offline. Relay accounts identify both reporter and observer where known and remain distinguishable from firsthand reports.

Store real reports at `sources/field-reports/<stable-report-id>.md`. The [authoring template](../templates/field-report.md) stays outside the bundle until completed from a real account. Do not create placeholder reports in the live bundle. Use the following metadata contract under `steelthumb.field_report`; unknown scalar values are `null`, and unrecorded lists are `null` rather than empty lists.

| Field | Meaning |
| --- | --- |
| `contributors` | Public actor IDs and roles such as observer, reporter, or editor; use `human:<chosen-id>` for people |
| `account_kind` | `firsthand` or `relay`; ideas without attempts belong in hypothesis claims |
| `attempts` | One or more attempt summaries with stable `id` values |
| `attempts[].same_attempt_as` | Optional revision reference to an earlier report plus `attempt_id`, when this is another account of the same event |
| `attempts[].procedure` | Revision reference, or `null` for an original/unknown procedure |
| `attempts[].dates` | Actual start and follow-up dates, preserving available precision |
| `attempts[].subject` | Crop and cultivar as reported; unknown cultivar is `null` |
| `attempts[].conditions` | Relevant growing system, medium, light, temperature, season, and other known context |
| `attempts[].baseline` | Starting observations and stated objective, if known |
| `attempts[].steps` | What was actually done |
| `attempts[].deviations` | Departures from referenced instructions, or `null` if unrecorded |
| `attempts[].outcome` | Observations, follow-up interval, counts/units, and `assessment`: `met`, `not_met`, `partial`, `pending`, or `unknown` |
| `attempts[].limitations` | Missing context, simultaneous changes, comparison limitations, or incomplete follow-up |
| `interpretation` | Contributor's explanation, separated from observations |
| `publication` | Consent/source locator, credited identity, and license for the published material |

Keep the body readable: Context, What happened, Outcome, Interpretation, and Limitations. Link photos or data as local permitted assets or cited external resources. Document the origin of a newly discovered method in the report, then derive a separate reusable draft procedure from it.

An attempt's identity is qualified by its report identity, not the local string `attempt-01` alone. Assess `met`, `not_met`, or `partial` against the report's stated objective; without an assessable objective retain the observations and use `unknown`. Use `pending` when the intended follow-up has not happened.

Report IDs identify documents; attempt IDs identify events. Multiple reports of one event retain the same attempt reference. Plants within one batch do not automatically count as independent attempts. Corrections identify what changed and retain history. Outcome totals include failures and pending results, with an explicit denominator and collection scope; they are not population success rates.

## Review records

`status: draft | stable | deprecated` describes document lifecycle. OKF `verified` records actual checks of content against its sources; it does not mean a gardener tried the procedure or proved its effectiveness. Omit it when no such verification occurred.

For a scoped review, add `steelthumb.reviews` entries with `by`, `at` (ISO datetime with offset), `subject` (revision reference and optional claim ID), `scope`, `basis` (source revision references or artifact URLs), `result`, and `limitations`. A structural check and a citation check have different scopes. The review record refers to an earlier committed subject revision; its own subsequent commit preserves the review event. Do not invent reviewer identities or timestamps.

Record reported use and outcome in field reports, not `verified`. Link an independently repeated attempt as new evidence. Avoid a single “validated” flag or numerical confidence score that conceals these distinctions. No evidence is inherited automatically by materially changed procedure steps.

## Illustrative evidence link

This fragment is synthetic and uses a hypothetical report. It is not a live bundle record or a horticultural claim.

```yaml
sources:
  - id: report-0042
    resource: /sources/field-reports/report-0042.md
steelthumb:
  claims:
    - id: reported-rooting-outcome
      kind: descriptive
      statement: Four of six cuttings developed visible roots by day twelve in this attempt.
      evidence:
        - source_id: report-0042
          relation: supports
          locator: Outcome, attempt-01
      applicability:
        conditions: Only the reported attempt; no comparison group.
```

The body sentence carries `[^report-0042]` and a matching footnote definition. Pin the report revision through `steelthumb.source_revisions` when incorporating a real record. A derived recommendation needs its own claim and a rationale for the inference.

## Project mapping to W3C PROV

This is a project mapping, not part of OKF or a PROV serialization. Revision-qualified identifiers distinguish changing documents. A gardener's attempt, report authorship, and review are distinct activities; known dates and actors must come from records.

| Almanac concept | PROV interpretation and direction |
| --- | --- |
| Procedure revision | Entity describing a plan (`prov:Plan`) |
| Gardening attempt | Activity associated with its gardener; plan may be recorded through a qualified association |
| Field-report revision | Entity generated by a reporting activity; attributed to its responsible contributor |
| Photo or measurement record | Entity generated by its actual capture/measurement activity when known |
| Revised guidance | Entity derived from source/report entities; generated by an editing activity that used them |
| Review | Activity that used the subject and evidence revisions and generated a review record |

PROV `used` points from activity to entity, `wasGeneratedBy` from entity to activity, `wasDerivedFrom` from derived entity to source entity, and `wasAttributedTo` from entity to agent. A procedure's physical execution does not necessarily read a document: represent the plan association and only assert document usage when recorded. A source footnote establishes documentary lineage, not every activity or causal link. Botanical evidence relationships (`supports`, `contradicts`, `qualifies`) remain project semantics, separate from derivation.

The current files have no PROV export or PROV constraint validation. Source identity, actual execution, outcome assessment, and factual truth remain separate questions.

## References

- [OKF v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md), consulted 2026-09-27: sources, concept IDs, lifecycle, and verification. The upstream main branch can change.
- [PROV-DM, 2013 Recommendation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/): entities, activities, agents, derivation, plans, and responsibility.
- [Repository ownership](repository-boundaries.md): published evidence here, private operations and their schemas in SteelThumb.
