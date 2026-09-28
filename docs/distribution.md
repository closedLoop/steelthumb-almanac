# Distribution

The [accepted layout decision](adr/0001-flatten-installable-bundle-layout.md) makes the repository itself the plugin and moves the OKF bundle to `skills/steelthumb-almanac/references/`. The migration is complete; the paths and commands below describe the flattened layout.

SteelThumb Almanac ships one self-contained Agent Skill in a Codex plugin. The OKF bundle is nested inside that skill so both installers carry its knowledge files. No npm package publication or installation hook is required.

## Source layout

```text
plugin.json                                  # Portable plugin identity
.codex-plugin/plugin.json                    # Codex compatibility and UI metadata
.agents/
  plugins/marketplace.json                    # Codex repository catalog
  skills/                                    # Contributor reference skills
skills/steelthumb-almanac/
  SKILL.md                                   # Agent entry point
  LICENSE
  references/                                # Canonical OKF bundle root
    index.md
    procedures/review-garden-observations.md
    crops/                                   # Scoped profiles and navigation
    systems/                                 # Growing arrangements
    guides/                                  # Teaching and reference guides
    sources/                                 # Source records and license text
```

Author future crops, procedures, sources, and related assets inside this bundle. Keep templates, contributor instructions, and private garden journals outside it. Distribute the `skills/steelthumb-almanac/references/` directory alone when a consumer wants plain OKF rather than an agent skill. No build or duplicated content tree is needed.

The root portable manifest provides identity; the Codex compatibility manifest provides install-surface metadata and supports legacy Codex packaging. Keep shared name, version, author, and description values in sync. The portable manifest deliberately omits an inline OpenAI extension so the compatibility overlay remains the metadata source.

The repository catalog is named `steelthumb`, and its plugin source resolves from the repository root to `./`. The repository is the plugin root, so repository documentation and contributor tooling are also within the package root. Codex discovers the gardening skill through the manifest’s `./skills/` path; `.agents/skills/` remains contributor tooling.

## Skills CLI

From a consumer project, after publication:

```bash
npx skills add closedLoop/steelthumb-almanac --skill steelthumb-almanac
```

Alternatively, scope discovery directly to the gardening skill directory:

```bash
npx skills add https://github.com/closedLoop/steelthumb-almanac/tree/main/skills/steelthumb-almanac --skill steelthumb-almanac
```

Use `--list` to inspect available skills, `--agent codex` to select Codex, and `--global` for user-wide installation. Standard `skills/` discovery finds the gardening skill without `--full-depth`; explicitly select it to exclude contributor skills.

## Codex

After publication:

```bash
codex plugin marketplace add closedLoop/steelthumb-almanac
codex plugin add steelthumb-almanac@steelthumb
```

The catalog carries no MCP server, app connection, or hook. Its standard authentication policy does not introduce service credentials into this file-only package. Start a new session after installation to pick up the skill.

## Local verification before publication

From another project directory, replacing `/path/to/steelthumb-almanac` with this checkout:

```bash
npx skills add /path/to/steelthumb-almanac --list
npx skills add /path/to/steelthumb-almanac --skill steelthumb-almanac --agent codex --copy --yes
```

For an isolated Codex test, point `CODEX_HOME` at a temporary directory for both commands:

```bash
CODEX_HOME=/path/to/temp-codex codex plugin marketplace add /path/to/steelthumb-almanac
CODEX_HOME=/path/to/temp-codex codex plugin add steelthumb-almanac@steelthumb
```

Inspect the installed skill's `references/index.md` and linked concepts, and compare them with the source files. Validate manifest metadata separately from installation behavior. Successful installation does not establish horticultural accuracy or complete OKF conformance.

## Sources

Packaging references consulted on 2026-09-27:

- [Vercel Skills CLI](https://github.com/vercel-labs/skills): repository/subdirectory installation, skill selection, and recursive discovery.
- [Skills discovery implementation](https://github.com/vercel-labs/skills/blob/main/src/skills.ts): normal search locations and `--full-depth` behavior.
- [Skills installer implementation](https://github.com/vercel-labs/skills/blob/main/src/installer.ts): copies the selected skill directory and supporting resources.
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins): portable manifests, Codex compatibility overlay, and repository marketplaces.
- [OKF specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md): the bundle remains independently readable Markdown and YAML.

Remote install commands require these files to be committed and pushed to the selected repository branch. Local smoke tests use the checkout and do not publish it.

## Bundled basil material

Start at [the basil profile](../skills/steelthumb-almanac/references/crops/basil.md). Its linked procedures, system description, guides, source records, and license text travel with either installer. Adapted documents remain unreviewed drafts under CC-BY-SA-4.0; see [attribution](../skills/steelthumb-almanac/references/sources/steelthumb-basil.md). The old import folder and image are no longer distributed. Historical source hashes live in the attribution record; the rest of the skill retains its existing license.

Field-report authoring instructions and contributor templates remain outside the bundle. Real published reports will be bundled as source concepts when supplied and accepted; none are fabricated to populate that directory. The structural refactor does not change installer discovery or plugin identity.
