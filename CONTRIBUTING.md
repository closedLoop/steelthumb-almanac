# Contributing to SteelThumb Almanac

Contribute sourced growing guidance, a correction, a useful tip, or an account of what happened in your garden. Firsthand experience is welcome even when measurements or cultivar identity are missing. Record those gaps rather than guessing.

## Submit a field report

Open an [issue](https://github.com/closedLoop/steelthumb-almanac/issues/new/choose) and choose **Garden field report or tip**. You can write ordinary prose; an agent or maintainer can help structure it. A proposed idea is welcome too, but must remain distinguishable from an actual attempt.

Include what you know:

- Your chosen public credit and whether you did the work yourself or are relaying another person's account.
- The crop, cultivar if known, growing system, relevant conditions, and dates.
- The procedure you followed and its version or saved copy, if available. If you discovered the method yourself, describe the steps.
- What you actually did, including changes from the instructions and other simultaneous changes.
- The starting condition, intended outcome, and what you observed afterward, with elapsed time and units where applicable.
- How many attempts and plants were involved, including failures, partial results, and pending follow-ups.
- Your interpretation, separately from observations. Optional photos and measurements can help others assess it.

An exact location, legal name, private journal, and photos are not required. Share only selected material you intend to publish. Use a pseudonym if preferred, remove sensitive location metadata from attachments, and credit other people's material with its reuse terms.

## From report to guidance

1. A maintainer checks that the account distinguishes observations from interpretations and has permission for publication. Missing details remain unknown; clarification is needed only when it changes what the report can support.
2. A real report becomes a `FieldReport` in the bundle's `sources/field-reports/` directory, using the [evidence contract](docs/evidence.md) and [authoring template](templates/field-report.md). Its source issue and contributor remain identifiable. No fabricated reports are added as evidence.
3. Link the report to a specific claim as supporting, contradicting, or qualifying evidence. A claim about an observed outcome can be supported by one report; a claim about causation or superiority needs evidence appropriate to that claim.
4. New methods become draft procedures. Record the procedure revision actually attempted and any deviations; a later rewrite does not automatically inherit evidence for changed steps.
5. Record reviews separately, including their scope and limitations. Preserve negative outcomes and corrections. Count distinct attempts, not issue comments, photos, copied reports, or citations of the same attempt.

A report being accepted means it is useful attributed evidence. It does not confer a general-purpose “validated” badge. Reported use, outcomes, document review, and independent repetition answer different questions. Summaries of submitted reports are not population success rates.

## Author reference knowledge

For an agent-assisted crop addition, use the [build-crop-knowledge contributor skill](.agents/skills/build-crop-knowledge/SKILL.md). It provides a coverage map, research strategies, and claim-level citation examples while following the contracts below.

Keep installable content inside `skills/steelthumb-almanac/references/`. Use `crops/`, `cultivars/`, `procedures/`, `systems/`, `guides/`, and `sources/` as needed. A crop profile links to relevant guidance. Create a cultivar document only when supported distinctions justify it. Teaching guides link to maintained procedures rather than repeating their parameters.

Each concept has OKF YAML frontmatter and readable Markdown. Use the [ontology](docs/ontology.md) for claim and relationship fields, and the [evidence contract](docs/evidence.md) for reports and reviews. These are project conventions on top of OKF, not upstream mandates.

Give important claims stable document-local IDs. Attribute factual statements using source-keyed footnotes and connect structured claims to those same source IDs. A bibliography alone does not identify which source supports which assertion. Keep conflicting recommendations separate and preserve their applicability. Separate procedure steps supported by sources from reporting instructions introduced by the Almanac.

For tips without supporting evidence, use `kind: hypothesis` and `evidence: []`. Keep them clearly labeled and request observations that could support or challenge them. Never present an invented illustrative example as a firsthand report.

## Attribution and reuse

Offer your original contributions under the repository's MIT license, or state another compatible license for maintainer review. Adaptations of the bundled CC-BY-SA-4.0 basil material retain that license and its attribution; see the [basil source record](skills/steelthumb-almanac/references/sources/steelthumb-basil.md). A citation does not grant permission to copy the cited work.

Retain authors, source URLs, revision identifiers, applicable notices, and a description of adaptations. Obtain the contributor's publication and license agreement before converting a report into bundled content. An incomplete agreement can be clarified in the issue; it is not permission by silence.

## Before submitting changes

- Parse YAML and check concept types, source IDs, claim IDs, evidence references, and relative links, including links after installation.
- Check that the scope, units, dates, and uncertainty in prose agree with metadata.
- Check attribution and license notices, and update incoming links when moving files. Bundle paths are concept identities; downstream consumers should pin a revision.
- Record exactly what was checked. Structural validation, citation review, and horticultural validation are separate activities.

Use an issue for discussion or a request, then link proposed file changes to it. Contributor templates and private operational records stay outside the installable knowledge bundle. See [repository ownership](docs/repository-boundaries.md).
