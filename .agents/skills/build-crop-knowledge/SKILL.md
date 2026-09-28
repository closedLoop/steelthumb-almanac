---
name: build-crop-knowledge
description: Research and author additional crop knowledge for SteelThumb Almanac, including crop and cultivar profiles, growing procedures, troubleshooting, food and yield information, and evidence-backed tips. Use when adding a crop, filling knowledge gaps, reviewing imported growing material, or incorporating supplied garden experience. Produces source-linked OKF documents in an Almanac checkout; ordinary advice about one person's garden uses the consumer gardening skill instead.
---

# Build crop knowledge

Create useful gardening references whose individual claims can be traced to inspected sources or clearly labeled firsthand reports. Organize around what a gardener needs to understand or do. A source's document layout, a simulator's task list, or an attractive complete-looking profile does not determine the knowledge model.

This is a repository contributor skill. Run it in a SteelThumb Almanac checkout; paths below are repository-relative unless shown as Markdown links. Contributor instructions stay in `.agents/skills/`; authored knowledge belongs in `skills/steelthumb-almanac/references/`. This skill is separate from the installed consumer gardening skill.

## 1. Establish scope and reuse

Read the checkout's `AGENTS.md`, `README.md`, `CONTEXT.md`, `CONTRIBUTING.md`, and `docs/ontology.md`. Read `docs/evidence.md` when adding claims, field reports, revision references, or reviews. Use [OKF guidance](../okf-spec/SKILL.md) for format decisions and [PROV guidance](../prov-spec/SKILL.md) when changing lineage semantics or producing an export. Repository contracts are authoritative over examples in this skill.

Inspect the bundle index and existing crop, cultivar, procedure, and source files before creating new ones. The basil collection demonstrates document boundaries and explicit evidence gaps; its crop-specific guidance is not evidence for another crop. The separate ontology example bundle is a development fixture.

Identify the requested crop and its scope: species/category, cultivar if relevant, edible part or growing purpose, and intended growing system or region. Use supplied context. Ask only about ambiguity that changes identity or applicability; otherwise state the working scope and continue. A general profile can preserve several regional contexts without assigning the user an invented climate.

**Complete when:** the intended reader questions, crop scope, reusable documents, and needed additions are identified.

## 2. Plan coverage and research

Use [information coverage and research strategies](references/research.md) to choose topics and sources. For a general profile, use the [seed-packet card and task review](references/authoring.md#seed-packet-quick-reference) to define the reader's decisions: select planting material, establish it, maintain it, recognize harvest readiness, and investigate a common failure. Scale other topics to the request.

Track each relevant topic as supported, conflicting, unresolved, or out of scope. For each unresolved decision, state what is missing and the next source or observation that could resolve it. Research blocking decisions first; keep general evidence limitations in shared source notes.

**Complete when:** the requested coverage has a concrete research path and missing information has not been silently treated as universal, false, or zero.

## 3. Inspect evidence before drafting claims

Open the relevant source material, including the actual table, method, label, or video segment supporting a claim. Search snippets, AI summaries, catalog blurbs, and a bibliography alone are discovery aids. Use the source strategies in the research reference; match evidence to the claim rather than rank all sources by one prestige score.

For each proposed claim, retain source identity, passage locator, applicability, units/basis, and whether the source supports, contradicts, or qualifies it. Trace copied advice back to its origin where possible; several retellings of one study or attempt are not independent evidence. Verify time-sensitive guidance against current applicable sources when authoring it.

If a source is inaccessible, seek an accessible primary source or supplied material. Mark unresolved support explicitly; never imply the original was read through a secondary citation. When research is unavailable, produce only the supported portion and clearly labeled gaps.

**Complete when:** each proposed factual statement has inspectable support, or is explicitly withheld, qualified, or labeled a hypothesis. No numerical setting is invented to make a procedure executable.

## 4. Author the knowledge

Use the existing ontology and [citation and authoring examples](references/authoring.md). Keep a readable body with source-keyed footnotes and use embedded claim records for independently reusable, quantitative, contested, or consequential assertions.

- `Crop`: identity, scope, quick reference, and navigation to relevant guidance.
- `Cultivar`: supported differences from its crop; retain each claim's scope rather than automatically inheriting values.
- `Procedure`: one complete gardening task, with purpose, applicability, prerequisites, steps, follow-up, and unresolved details.
- `GrowingSystem`: a cultivation arrangement and constraints, separate from its measurements or controller settings.
- `Guide`: teaching or cross-cutting explanations that link to maintained procedures.
- `Source` and `FieldReport`: inspectable documentary origins and real published accounts. Read the evidence contract and use `templates/field-report.md` for supplied attempts.
- Use `FoodProfile`, `YieldEstimate`, `Problem`, `Symptom`, or `MeasurementMethod` only when the material needs an independently maintained concept; consult their ontology contracts first.

Place each recommendation in one authoritative location. Crop cards display concise values with links to the owning claim; check both when a value changes. Teaching guides link to maintained procedures. Preserve unknown metadata when editing existing files. Keep personal operational records in their owning workspace.

For a batch, author one representative crop end to end first. Use the [research and OKF quality rubric](references/RUBRIC.md) for the task review and run the structural checker; correct the card and procedure pattern before expanding the remaining crops. Choose a pilot that exercises the requested growing system. Reuse structure only where the next crop's lifecycle and decisions fit it; this is a local review, not an approval gate.

For newly discovered tips, distinguish the contributor's observed result from the inferred recommendation. Record the procedure version and deviations; retain failures and pending outcomes. Untried ideas remain hypotheses. Apply the contribution guide's publication and license requirements to real reports and attachments.

For imported material, research and write standalone gardening guidance using direct sources. Keep migration history, retired design assumptions and uninspected research leads outside the OKF bundle. Preserve required attribution in a separate bundled legal notice. Readers must not need a predecessor repository to understand a concept or complete its supported route. Source credit is not a horticultural verification event.

**Complete when:** the requested material is represented in useful, linked documents with inspectable evidence and explicit applicability. Gaps and conflicts remain visible to readers.

## 5. Check and connect

Update the bundle index, crop navigation, related procedures, and incoming links. Keep required sources, licensed assets, and license notices inside the installed skill. A local link must remain valid when the bundle is copied away from the repository.

Check YAML, required project metadata, unique claim/source IDs, evidence joins, body footnotes, claim anchors, relative paths, typed relationships, and agreement between quantities in prose and metadata. Check citation support separately: a valid URL does not establish that its page supports the sentence. Confirm that lifecycle, source review, and actual outcomes have not been conflated.

Run `python .agents/skills/build-crop-knowledge/scripts/check_bundle.py skills/steelthumb-almanac/references` (Python 3 and PyYAML). This reusable checker covers bundle structure and local references; its `--help` describes scope and limitations. Check the same bundle copied to a temporary directory. Evaluate source fidelity, card values, and reader task completion with the [quality rubric](references/RUBRIC.md); record unreviewed dimensions explicitly. Automated success does not establish them.

For citation-refresh work, record manual passage judgments in a contributor ledger outside the bundle. Run `python .agents/skills/build-crop-knowledge/scripts/check_fidelity.py skills/steelthumb-almanac/references docs/research/citation-fidelity.json --require-complete` when using the current project ledger. This checks review coverage and stale snapshots, not whether a source is true; re-read changed assertions before updating their hashes. See [the current review scope](../../../docs/research/citation-refresh.md).

**Complete when:** structural checks pass and the task review names the supported route, distinguishing symptom check, and any blocked decisions with next steps for every requested crop. Card values match their owning claims. Report partial coverage as partial even when all headings exist. Record actual verification only under the evidence contract; do not invent review events or claim field validation. Creating local content does not require publishing an issue or pushing a branch.

## Report back

Link the crop entry point and summarize coverage, important disagreements, evidence gaps, and checks performed. Distinguish sources inspected from sources merely retained as leads. Name any requested topic that remains incomplete and why.

Example requests:

- “Use $build-crop-knowledge to add carrots for outdoor home gardens, including establishment, harvest, and storage.”
- “Use $build-crop-knowledge to research cultivar-specific differences in the existing potato profile.”
- “Use $build-crop-knowledge to incorporate my supplied propagation notes as a field report and draft tip, preserving the failed attempts.”
