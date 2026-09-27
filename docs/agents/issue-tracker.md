# Issue tracker: GitHub

Issues and specs live in closedLoop/steelthumb-almanac.
Use the gh CLI from this repository.

- Publish a ticket: `gh issue create --title "..." --body-file <file>`
- Read a ticket: `gh issue view <number> --comments`
- List tickets: `gh issue list --state open`
- Comment: `gh issue comment <number> --body-file <file>`
- Apply labels: `gh issue edit <number> --add-label "<label>"`
- Remove labels: `gh issue edit <number> --remove-label "<label>"`
- Close: `gh issue close <number>`

For multiline bodies, write the exact Markdown to a temporary file
and pass --body-file.

PRs as a request surface: no.

## Wayfinding

Represent a map as an issue labeled wayfinder:map. Link child tickets
as sub-issues where supported; otherwise use a task list in the map
and a "Part of #<map>" line in each child.

Use wayfinder:research, wayfinder:prototype, wayfinder:grilling,
or wayfinder:task labels for child types.

Record blockers using native issue dependencies where supported;
otherwise use "Blocked by: #<number>" in the child body.

Select the first open, unassigned child in map order with no open
blockers. Claim it by assigning the driving developer. On resolution,
record the outcome, close the child, and add a linked summary to the
map's Decisions-so-far.
