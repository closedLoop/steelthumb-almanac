# Authoring and citing crop knowledge

Use the checkout's [ontology](../../../../docs/ontology.md), [evidence contract](../../../../docs/evidence.md), and [contribution guide](../../../../CONTRIBUTING.md) as the authoritative contracts. The examples here teach the workflow without defining a second schema.

## From source passage to claim

1. Write the narrow assertion the inspected evidence can support. Separate “the guide recommends X,” “X occurred in this attempt,” and “X improves outcomes.” Each requires different evidence.
2. Assign a stable document-local claim ID. A changed meaning requires a new ID rather than silently reusing the old one.
3. Add each cited artifact to the document's `sources` with a stable `id`, concrete `resource`, and useful title. Preserve source authors/version in the established fields or source notes where known. Never put a search-result URL or tool-internal citation token in repository content.
4. In `steelthumb.claims`, identify the claim kind, evidence relation, exact source locator, applicability, and quantity/basis where relevant.
5. Give the claim a matching body anchor and cite the readable sentence with `[^source-id]`. Define that footnote using the same ID and a descriptive source link. The frontmatter and prose must agree.

Several claims can cite one source; a claim can cite several sources. A bibliography at the bottom does not substitute for statement-level attribution. Split a sentence if its clauses need different support. Evidence for one step does not automatically support every step in a procedure.

## Structural example

This is a **synthetic example**, not growing advice or an actual source. Its fictional claim, URL, dates, and scope must not enter the live bundle. It demonstrates how an observed outcome differs from a general recommendation.

```markdown
---
type: Crop
title: Example crop
description: Illustrative crop profile; replace with real researched content.
status: draft
sources:
  - id: example-trial
    resource: https://example.org/fictional-trial
    title: Fictional trial used only to explain citation structure
steelthumb:
  ontology_version: "0.2"
  claims:
    - id: emergence-in-trial
      kind: descriptive
      statement: The cited trial reports first emergence eight days after sowing.
      quantity:
        property: time_to_first_emergence
        value: 8
        unit: d
        basis: Days after sowing; first emergence, not complete germination.
      applicability:
        conditions: Only the cultivar, medium, and temperature recorded in the trial.
      evidence:
        - source_id: example-trial
          relation: supports
          locator: Results, Table 2, first-emergence row
---

# Example crop

<a id="emergence-in-trial"></a>
The cited trial reports first emergence eight days after sowing.[^example-trial]
This observation is not a guarantee for other conditions or all seeds in a batch.

[^example-trial]: [Fictional trial](https://example.org/fictional-trial), Results, Table 2.
```

For an unsupported proposed explanation, use `kind: hypothesis` and `evidence: []`, label it in prose, and describe what evidence would test it. Missing knowledge alone does not require inventing a hypothesis.

## Procedure composition

A complete procedure answers:

- **Purpose and scope:** What task and crop/setting does this cover? What outcome is intended?
- **Prerequisites:** What identity, stage, materials, measurements, or readiness conditions matter?
- **Steps:** What is done, in what sequence, with citations for the recommendations and settings?
- **Follow-up:** What should be observed and when? Distinguish a source-supported expected response from a suggested observation schedule.
- **Limits:** Which parameters, alternatives, conflicting sources, or situations remain unresolved?

Combine compatible source guidance only when its context warrants it, and label the combination as an editorial synthesis if it has not been evaluated as a whole. Do not imply that a source tested the assembled procedure. Keep materially different methods as explicit branches or separate procedures. Retain exact source wording for uncertain terms in notes rather than silently converting them into a precise schema.

Use existing relation predicates and readable links for crop/cultivar/system applicability. Do not copy the same procedure for every cultivar; add a scoped variation when evidence supports one. Quick-reference values should link to their owning claims, and guides should link to the maintained procedure.

## Sources, reports, and revision history

Use inline source entries for ordinary citations. Create a separate `Source` concept when shared attribution, source context, permitted assets, or review notes warrant independent maintenance; a source record need not contain a full copy of the original. Inspect source reuse terms before copying text, images, or datasets. Paraphrase in original language and retain license/attribution notices for adaptations.

For private experience, use a selected real `FieldReport` under the existing publication contract. Preserve steps, observations, interpretation, counts, and limitations. Cite its outcome for claims about that attempt; do not turn an AI-generated example or a proposed experiment into evidence.

Pin procedure and report references as the evidence contract specifies. Record actual deviations. Keep a report's observational record distinct from a later inference or revised procedure. Several reports of the same attempt must retain their shared attempt identity. Independent repetition needs a new real attempt, not another citation.

Treat `status` as lifecycle, `verified` as an actual content check under OKF, and scoped `steelthumb.reviews` as records of what was checked. Source inspection during drafting does not authorize an invented human sign-off. Report any performed citation checks precisely; no lookup or structural check establishes universal horticultural effectiveness.

## Review before declaring the addition complete

| Check | Evidence of completion |
| --- | --- |
| Identity and scope | Crop/species/cultivar/product distinctions are explicit; unspecified conditions stay unspecified |
| Requested coverage | Each requested topic has useful supported content, a clear limitation, or an identified evidence gap |
| Citation fidelity | The inspected passage supports the actual sentence; locators and source IDs resolve |
| Quantities | Units, original precision, starting event, mass/area/time basis, and conversions agree in YAML and prose |
| Conflicts and inference | Disagreement is retained; synthesized recommendations and reported outcomes remain distinguishable |
| Provenance | Contributors, source versions, actual attempts, and reviews are represented only when known |
| Packaging | Index and crop links resolve; required resources remain inside the installed skill; contributor templates remain outside |
| Reuse | Credit and license notices follow adaptations and assets; no unnecessary import archive remains |

Check actual content, not merely the presence of headings. Completion with an evidence gap must say what remains unknown rather than describe that topic as fully researched or validated.
