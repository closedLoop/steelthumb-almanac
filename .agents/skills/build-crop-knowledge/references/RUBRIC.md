# Crop research and OKF quality rubric

Use this rubric on one complete pilot before expanding a batch, and on every crop collection before reporting completion. Evaluate the crop hub, its reachable procedures/system guidance, and the claims and sources they use. The unit is a usable crop collection, not a file count. Assess each requested growing system separately; a complete ground route does not establish bag coverage.

This is an Almanac editorial rubric. Its scores are neither scientific confidence estimates nor OKF requirements, and they do not imply field validation.

## Applying it to individual entities

For an entity inventory, give each concept its own row and inspect its outgoing dependencies where they supply a reader decision. Record the entity type and scope. Keep collection-level gaps visible without demanding that each file repeat the whole collection. An index is a reserved bundle document, not a concept; review it separately for coverage and navigation.

Use the same research and OKF dimensions. Interpret the four usefulness dimensions according to the entity's role:

| Type | Summary/card | Task completion | Troubleshooting/failure handling | Gaps/readability |
| --- | --- | --- | --- | --- |
| Crop / Cultivar | Seed-packet facts, scoped differences, and linked owners | Reachable growing routes | Reachable distinguishing checks | Decisions left to cultivar/local evidence |
| Procedure | Purpose, prerequisites, and usable settings | The named task through follow-up | Stop/repair/referral conditions relevant to that task, or a linked diagnostic route | Unresolved inputs and adaptations |
| Guide | Clear orientation and decision summary | Reader can reach and choose the appropriate procedure | Misapplication risks and routes for unresolved questions | Teaching flow and evidence boundaries |
| GrowingSystem | Arrangement, components, and constraints | Setup and linked crop procedures | Drainage, support, exposure, or other relevant failure checks | Supported use versus adaptations |
| Source | Origin, authorship, date/revision, and inspection scope | Reader can find the supporting artifact/passage | Conflicts, inaccessible/unreviewed material, and misuse limits | Reuse terms and next evidence work |

Record all ten dimension ratings for every concept; use NR for uninspected evidence, and explain material deductions with a concrete next action. A source catalog is not penalized for lacking planting depth, nor rewarded as proof that linked articles support every claim. Do not compare totals across different entity roles as a ranking of horticultural reliability. For entity types not covered here, declare the role-specific interpretation before scoring.

## Evaluation method

1. Record the requested scope, files/revision reviewed, reviewer, and review date. For uncommitted work, state that the review refers to the working tree; do not invent a pinned revision or identity.
2. Check the release blockers below. A blocker means **needs repair** regardless of score.
3. Inspect claims against the actual supporting passages. Review every quantitative, consequential, disputed, or adapted recommendation. For other claims, declare full coverage or name the sample and unreviewed remainder. A working link is not evidence of fidelity.
4. Walk the five reader tasks and compare every card value with its owning claim. Run the structural checker and a copied-bundle check. Report these as separate evidence.
5. Score each dimension using the anchored scale. Link concrete evidence and name the repair for each deduction. Use **NR (not reviewed)** when evidence was not inspected; NR does not become zero or silently receive full credit.
6. Report scores by group, blockers, task/system gaps, and the next repairs. A batch report names the weakest crops; averaging must not conceal a blocked route. Report a full /100 score only when every dimension is assessed. Keep omitted requested work visible.

## Release blockers

- A gardening assertion is presented as established without support, or the inspected source contradicts the sentence without a retained qualification.
- A quantitative setting loses a consequential unit, temperature type, growth stage, starting event, cultivar, or system distinction, making the instruction misleading.
- A source, firsthand observation, outcome, contributor, verification event, or review has been fabricated.
- Broken evidence joins, malformed YAML, unresolved required links/claim anchors, or escaped bundle paths prevent interpretation or standalone use.
- Plant identity or food-use scope is ambiguous enough that following the instructions could apply them to a different plant or inappropriate edible part.
- A required task decision has no supported route or actionable next step, yet the collection claims that route is complete. An honest partial collection can remain draft with that route explicitly unresolved.
- Copied material lacks the required permission, attribution, or reuse notice.

## Scoring

Rate each dimension 0–4, then calculate `weight × rating / 4`. Use half-points only with a written reason. The rating describes the quality of the documented work within its stated scope, not the probability that a plant will grow successfully.

- **0:** absent, misleading, or unusable.
- **1:** substantial missing evidence or decisions; headings and links alone do not satisfy the criterion.
- **2:** partly usable, with specific unresolved weaknesses affecting scope or decisions.
- **3:** usable within explicit scope; minor omissions have actionable follow-up.
- **4:** fully meets the dimension's evidence below, including relevant edge cases and independently checkable references.

| Group / dimension | Weight | Evidence for a 4 |
| --- | ---: | --- |
| Research: identity and applicability | 10 | Species/category/cultivar/rootstock distinctions resolve the actual request; each consequential claim retains region, stage, material, and system context. |
| Research: source fitness and inspection | 10 | Inspectable primary or otherwise claim-appropriate sources were read; dates, locators, inaccessible originals, and shared origins are preserved. Source count and institutional prestige do not substitute for fit. |
| Research: claim fidelity | 15 | Inspected passages support the precise statements and quantities; alternatives, conversions, and editorial combinations are transparent. No inference is promoted to a tested result. |
| Research: conflicting and missing evidence | 5 | Relevant differences are investigated and kept as scoped alternatives; an evidence gap names what would resolve it without inventing a setting. |
| Usefulness: seed-packet card | 10 | Applicable planting method/timing/depth/spacing/light/habit/establishment/harvest/bag fields show concise facts linked to owning claims. Unknowns state the next check. No universal maturity interval or supplier identity is invented. |
| Usefulness: complete growing tasks | 15 | A reader can choose material, establish, maintain, and harvest through an explicit supported route, with prerequisites and follow-up. Each requested system is evaluated separately. |
| Usefulness: troubleshooting | 10 | At least one relevant failure has an observable sign, candidate cause, distinguishing check, supported response or justified referral, and a follow-up observation. A request for photographs alone is insufficient. |
| Usefulness: actionable gaps and readability | 5 | Gaps name the blocked decision and next evidence; shared caveats are consolidated; task-specific cautions remain beside the action. Readers can find essentials quickly. |
| OKF: structural integrity | 10 | YAML/project metadata, IDs, evidence joins, footnotes, anchors, quantities, typed relations, and local paths pass checks. Unknown metadata survives edits. Manual numeric/prose agreement is checked separately. |
| OKF: navigation, maintenance, and provenance | 10 | Cards and index lead to authoritative claims/tasks; shared instructions are maintained once; standalone copying works. Concepts explain gardening directly without predecessor-project or migration dependencies; required license notices stay separate. Source, review, execution, outcome, and license meanings stay distinct. |

Group totals: research **40**, usefulness **40**, OKF **20**.

## Interpreting the result

- **90–100:** strong draft reference, subject to stated applicability and field-evidence limits.
- **75–89:** usable scoped draft; repair named weaknesses before broadening claims or scope.
- **Below 75:** substantive revision needed.
- **Any release blocker:** needs repair; the total cannot override it.
- **Any NR dimension:** incomplete quality evaluation; report assessed group/dimension scores without a normalized total.

A clearly disclosed gap can earn credit for honesty while still losing task-completion credit. Missing cultivar maturity need not block picking when a supported readiness cue exists. Missing bag dimensions can leave bag establishment partial even if all ground instructions are usable. Structural success alone earns at most the structural dimension's points.

## Compact review record

Keep batch reviews outside the installed OKF bundle unless a revision-qualified review is deliberately being published under the evidence contract.

```text
Scope / requested crops and systems:
Files or revision / working-tree status:
Reviewer / date:
Source passages inspected this review / unreviewed remainder:
Release blockers:
Dimension ratings, weighted points, and evidence links:
Reader tasks: material; establish; maintain; harvest; investigate:
Ground / pot / bag coverage and adaptation status:
Automated checks and manual checks actually run:
Repair priority: affected decision → change or next evidence:
Result: strong draft / usable scoped draft / needs repair / incomplete evaluation:
```

Follow the [card and task-review guidance](authoring.md#seed-packet-quick-reference), [research strategy](research.md), and repository [evidence contract](../../../../docs/evidence.md) when gathering or recording the evidence. A rubric review is not permission to invent verification metadata or garden outcomes.
