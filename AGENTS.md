# Working in SteelThumb Almanac

Read [README.md](README.md) for the project's purpose and scope. Its proposed structures and examples describe intent; inspect the files before assuming a schema or integration exists.

## Reference skills

- For adding a crop, researching missing growing guidance, or incorporating supplied crop experience, use [build-crop-knowledge](.agents/skills/build-crop-knowledge/SKILL.md).
- For provenance modeling, source lineage, or PROV exports, read [prov-spec](.agents/skills/prov-spec/SKILL.md).
- For OKF concepts, bundle layout, frontmatter, or format conformance, read [okf-spec](.agents/skills/okf-spec/SKILL.md).
- When mapping OKF source metadata to PROV, read both and document the mapping as a project convention.

## Contributions

For new guidance, firsthand reports, corrections, or evidence reviews, follow [CONTRIBUTING.md](CONTRIBUTING.md). For claim identifiers, field-report metadata, revision references, and the local PROV mapping, read [the evidence contract](docs/evidence.md).

For installable content and plugin packaging, read [distribution](docs/distribution.md). The canonical OKF bundle is `skills/steelthumb-almanac/references/`; keep all resources needed by the installed skill inside its directory.

Keep gardening claims traceable to sources or labeled firsthand observations. Preserve cultivar, growing conditions, dates, units, and uncertainty when they affect applicability. Separate observations, interpretations, proposed actions, and recorded outcomes.

Link evidence to individual claims and pin the procedure revision actually attempted; record deviations. Record use, observed outcomes, and review separately. Publish field reports only from real supplied observations; label structural examples as synthetic and exclude them from evidence counts. Preserve failures, conflicts, unknowns, and contributor credit.

Keep reusable reference knowledge separate from personal garden records. Follow the README's attribution and reuse guidance when incorporating external material.

For ownership across repositories, read [repository boundaries](docs/repository-boundaries.md). Maintain reusable knowledge, procedures, food profiles, and evidence here. Garden-operation schemas, RL research, and experiment contracts belong in `steelthumb/docs/garden-intelligence/`.

Treat new crop fields and taxonomies as project conventions unless the linked specification defines them. Organize knowledge by concept type and use crop profiles as navigation hubs. Keep agent instructions and contributor templates outside the OKF bundle so they are not parsed as knowledge concepts.

For documentation changes, check relative links, metadata, and consistency with the cited specification. Report which checks ran and which conformance claims remain untested; introduce build or validation tooling only when the work calls for it.

## Agent skills

### Issue tracker

Tickets live in GitHub Issues for closedLoop/steelthumb-almanac.
See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five standard triage labels.
See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: root `CONTEXT.md` and `docs/adr/`.
See `docs/agents/domain.md`.
