---
status: accepted
date: 2026-09-27
---

# Make the repository the plugin and keep the OKF bundle inside its skill

SteelThumb Almanac must distribute the same knowledge through `npx skills`, a Codex plugin, and plain OKF files. Make the repository root the plugin root and place the canonical OKF bundle at `skills/steelthumb-almanac/references/`. This removes redundant directory layers while keeping the knowledge inside the skill directory that the Skills CLI installs.

## Target layout

```text
steelthumb-almanac/
├── plugin.json
├── .codex-plugin/plugin.json
├── .agents/
│   ├── plugins/marketplace.json
│   └── skills/                       # Contributor reference skills
├── skills/
│   └── steelthumb-almanac/
│       ├── SKILL.md
│       ├── LICENSE
│       └── references/               # Canonical OKF bundle root
│           ├── index.md
│           └── …                     # Knowledge documents and assets
├── docs/
├── templates/                        # When needed
├── README.md
├── AGENTS.md
└── LICENSE
```

Keep the skill name `steelthumb-almanac` as its distinct installation identity. The `steelthumb` marketplace points to `"source": { "source": "local", "path": "./" }`. The portable manifest and Codex compatibility manifest retain matching identity metadata. Contributor skills remain in `.agents/skills/`; consumers select the gardening skill explicitly.

Plain OKF consumers can copy `skills/steelthumb-almanac/references/` independently. Agent instructions, contributor templates, and private garden records remain outside that bundle. Content categories are independent of this packaging decision; preserve the bundle's internal paths when moving it.

## Alternatives and consequences

The initial `plugins/steelthumb-almanac/skills/steelthumb-almanac/references/almanac/` layout works but repeats the product name and adds unnecessary nesting for a single-plugin repository. A separate top-level `almanac/` would be easier to browse, but would sit outside the installed skill and require an additional packaging or copying step. The chosen layout keeps one authoritative content tree with no build step.

The target Skills CLI command is:

```bash
npx skills add closedLoop/steelthumb-almanac --skill steelthumb-almanac
```

Standard `skills/` discovery removes the need for `--full-depth`. Codex retains the same marketplace and plugin identifiers:

```bash
codex plugin marketplace add closedLoop/steelthumb-almanac
codex plugin add steelthumb-almanac@steelthumb
```

Making the repository the plugin root broadens the package root to include repository documentation and contributor tooling; consumers should enter through the declared gardening skill. Revisit this decision if the repository needs independently released plugins.

## Verification and implementation state

On 2026-09-27, a temporary copy of the starter package was flattened and installed using an isolated `CODEX_HOME`. Marketplace registration with `source.path: "./"`, `codex plugin add steelthumb-almanac@steelthumb`, and plugin manifest validation all passed. The installed skill and OKF files matched the temporary source byte-for-byte, and local Markdown links resolved. This tested local Codex packaging; it did not test a published GitHub installation or the shortened Skills CLI command.

The working repository migration was completed on 2026-09-27. Manifests now live at the repository root, the marketplace source is `./`, and the canonical bundle is `skills/steelthumb-almanac/references/`. The [distribution guide](../distribution.md), skill instructions, repository links, and SteelThumb’s basil references use the new paths.

Both local installers passed against the migrated checkout: Codex with an isolated `CODEX_HOME`, and `npx skills add <checkout> --skill steelthumb-almanac --agent codex --copy --yes` from a temporary consumer project, without `--full-depth`. All 12 bundle files retained identical relative paths and SHA-256 hashes; all 14 skill files matched both installed copies byte-for-byte. Plugin and skill validation passed, manifest identities matched, and local documentation links resolved. Published GitHub installation and horticultural accuracy remain untested.
