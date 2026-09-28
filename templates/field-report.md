---
type: FieldReport
title: Replace with a specific account of an actual attempt
description: Replace with a short summary of the setting and observed outcome.
status: draft
sources: []
steelthumb:
  ontology_version: "0.2"
  license: null
  field_report:
    contributors: null
    account_kind: null
    attempts:
      - id: attempt-01
        same_attempt_as: null
        procedure: null
        dates:
          started: null
          follow_up: null
        subject:
          crop: null
          cultivar: null
        conditions: null
        baseline:
          observations: null
          objective: null
        steps: null
        deviations: null
        outcome:
          assessment: unknown
          observations: null
          follow_up_interval: null
          counts: null
        limitations: null
    interpretation: null
    publication:
      consent_resource: null
      credit: null
      license: null
---

# Field-report authoring template

This is an incomplete contributor template, not evidence of an attempt. Fill it using a real submitted account and the [evidence contract](../docs/evidence.md), then copy the completed report into the bundle's `sources/field-reports/` directory. Replace this heading and remove these authoring instructions. Resolve relative links from the new location.

Add a source entry for the submission issue, with `id` and `resource`, and cite it using a matching footnote. Set `contributors` to a list of `{actor, role}` entries, such as the supplied public `human:<chosen-id>` and `observer` role. Set `account_kind` to `firsthand` or `relay`. Publication credit, consent reference, and license must be resolved before bundling; keep both license fields consistent.

For a known procedure use `{repository, revision, bundle, concept}` under `procedure`; preserve `revision: null` when the actual version is unknown. For an original method leave `procedure: null` and supply the steps. Replace attempt IDs with stable identifiers. When reporting an already documented event, set `same_attempt_as` to the earlier report's revision reference plus its `attempt_id`. Add one attempt summary per distinct attempt, not per photograph or seedling by default.

Use actual source precision for dates. Counts are entries such as `{category, value, unit}`; unknown values remain null. Record the starting denominator and all outcomes, including pending ones, when supplied. Do not manufacture a complete count from a partial report. Conditions, steps, deviations, and limitations may use readable text or lists while the vocabulary evolves; their meaning must agree with the body.

## Context

Crop, cultivar, growing arrangement, dates, and objective as reported.

## What happened

Starting observations, actual steps, procedure revision, deviations, and simultaneous changes.

## Outcome

Observed results, follow-up time, counts, units, failures, partial results, and unresolved follow-ups. Refer to each attempt by its ID.

## Interpretation

The contributor's explanation, separate from observations and any editorial inference.

## Limitations

Missing context, comparison limitations, uncertain identity, or incomplete follow-up.

## Attribution and publication

Public contributor credit, source submission, publication agreement, and reuse terms for text and attachments. Add actual source-keyed footnotes here or beside the relevant statements.
