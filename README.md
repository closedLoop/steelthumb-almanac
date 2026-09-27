# SteelThumb Almanac

**An open, evidence-based guide to growing food—with humans and AI agents learning alongside the garden.**

SteelThumb Almanac is a growing collection of practical knowledge for home gardeners, market gardeners, and homesteaders. Its purpose is to help people understand what they are growing, decide what to do next, and learn from what actually happens.

The central idea is simple: **debug the garden.** Observe a real plant, identify what you know and what you are uncertain about, make a considered change, and check the result. Over time, those small feedback loops can improve both your garden and the knowledge available to everyone else.

This repository starts with that reference layer: readable, linked documents that people can keep, contribute to, and use with the AI tools of their choice. The initial goal is to document the plants in a real garden well, then expand through contributions from other gardeners and agents.

> **Project status:** This README describes the project's purpose and intended structure. Crop profiles, procedures, schemas, and agent integrations are still to be built. Examples below illustrate the proposed approach.

## Why an almanac, and why now?

A good almanac is something you return to throughout the growing season. It combines useful reference material with guidance you can apply where you live. SteelThumb extends that idea into a shared, connected body of knowledge: crop profiles, growing techniques, troubleshooting guides, sources, and observations from real gardens.

In 2026 and beyond, we want gardeners to grow food alongside AI agents that can help read references, organize observations, compare possible explanations, and plan follow-up. For that collaboration to be useful, the knowledge needs to be inspectable. A gardener should be able to ask: Where did this advice come from? Which variety and conditions does it apply to? What should I observe to see whether it worked?

The Almanac is designed around that relationship. People bring goals, judgment, physical care, and local experience. Agents help connect the information and keep track of the learning process. The garden supplies the evidence.

## What belongs in the Almanac?

The intended format follows an **Open Knowledge Format (OKF)** approach: human-readable Markdown, structured front matter for key facts, stable identifiers, and explicit links between related documents and their evidence. The exact schema will evolve as we work through real examples.

| Kind of knowledge | What it should contain |
| --- | --- |
| Crop profiles | Identity, varieties, growing requirements, lifecycle, harvest, uses, and linked procedures. |
| Growing procedures | Steps for sowing, transplanting, propagation, cultivation, pruning, harvesting, and seed saving. |
| Growing systems | Context for containers, garden beds, hydroponics, and other methods. |
| Troubleshooting guides | Symptoms, possible causes, distinguishing observations, interventions, and follow-up. |
| Tools and measurements | How to observe and measure conditions, with units and limitations. |
| Evidence and sources | Research, extension guidance, seed supplier information, and documented grower experience. |

Food uses, nutrition, calories, yields, and practical tips can be included where they are supported. Quantities should identify their basis: for example, edible fresh weight versus dry weight, or yield per plant versus per unit area over a specified period.

### Example: a Genovese basil profile

A profile should begin with a quick reference card: the information you would look for on a seed packet, presented in a form that both a person and an agent can read.

- Common and scientific name, cultivar, and links to relevant supplier information.
- Germination time and conditions, sowing depth, and spacing.
- Light, water, temperature, and growing-medium requirements.
- Time to harvest, including whether it is measured from sowing or transplanting.
- Sources, applicable conditions, and uncertainty for those values.

Below that card, the document should explain the plant and its lifecycle, with links to procedures for germination, transplanting, growing in soil or hydroponics, propagation, and harvesting. A pest section could link to a shared aphid identification and management guide, so that guide can be maintained and improved across crops.

A specific seed packet belongs in the gardener's local records: supplier, cultivar, lot if available, packet instructions, and purchase or sowing dates. Those instructions should remain distinguishable from general species guidance. If sources disagree, preserve the difference and investigate the context.

## Debugging the garden

Debugging means turning a concern into a useful cycle of observation and learning.

1. **Observe.** Record the plant, location, date, growth stage, symptoms, recent care, and relevant conditions. Photos and measurements help establish a baseline.
2. **Frame the question.** What is different from what you expected? What outcome are you trying to improve?
3. **Compare explanations.** Use the Almanac and its sources to identify plausible causes. Keep observations separate from interpretations.
4. **Choose the next check or action.** Prefer a useful observation before an uncertain intervention. When practical, change one thing at a time and record what changed.
5. **Set a follow-up.** Decide when to look again and what would count as improvement, no change, or deterioration.
6. **Review the outcome.** Update the garden record, reconsider the explanation, and share useful findings with their context.

For example, “my basil looks unhappy” can become a dated record of which leaves changed, photos of both leaf surfaces, growing-medium conditions, and recent watering. An agent can help identify missing observations and find relevant references. The gardener checks the plant and chooses the action. A later observation tests whether the explanation was useful.

One successful intervention is a local observation. Repeated, well-documented results can strengthen the shared guidance, while unsuccessful attempts help others understand its limits.

## Your garden and the shared reference

The Almanac holds reusable knowledge. Your own `garden.md` can describe what is happening in your particular garden and link back to the relevant profiles and procedures.

A useful garden record includes:

- Your goals and constraints: food you want to grow, available space, time, and growing methods.
- Beds, containers, plantings, cultivars, and seed sources, each with a stable name or identifier.
- Local conditions and dated observations, including the most recent garden walkthrough.
- Actions taken, open questions, planned checks, harvests, and outcomes.

Keep personal garden records wherever you prefer. Share selected observations when they can help others, including enough context to interpret them. The public reference should remain useful independently of any one person's journal.

### Working with an AI agent

Start by giving an agent the relevant Almanac documents and your current garden notes. A useful request might be:

> Read my garden notes and the linked crop profiles. Separate what we observed from possible explanations. Identify the most useful missing observations, cite the sources behind your suggestions, and propose one manageable next step with a follow-up check. Mark anything that the references do not establish.

Agents should preserve source links, dates, units, and uncertainty; distinguish a proposed action from a completed action; and ask for missing local information when it changes the advice. A confident answer does not replace an observation. Gardeners decide what to do and record what actually happened.

## Evidence people can inspect

The aim is a highly cited reference that makes the basis of its advice visible.

- **Trace claims to sources.** Prefer original research, documented trials, supplier instructions for the specific seed product, and university extension guidance as appropriate to the claim.
- **Identify the kind of evidence.** A controlled study, an extension summary, a seed packet, and a gardener's observation offer different kinds of support.
- **Preserve applicability.** Record cultivar, climate, season, growing system, and other conditions that affect interpretation.
- **Make uncertainty visible.** Keep conflicting findings, gaps, and untested hypotheses explicit.
- **Respect attribution and reuse terms.** Link to sources, write original summaries, and preserve the attribution and license of any material legitimately reused.

Agents and people are welcome to propose additions. Contributions should include verifiable sources or clearly labeled firsthand observations. Human review remains part of maintaining the shared reference.

## Portable knowledge, useful over time

The goal is for the reference itself to work offline: clone or download the repository, read the documents, and use them with local tools or a local model. Following external links and fetching updated sources still requires connectivity unless those resources have been separately archived with permission.

Plain files and version history allow people to inspect changes, keep a known version, fork the collection, and contribute improvements. Useful garden knowledge should remain available as models, applications, and hosting services change.

## Related work and foundations

This project builds on a long tradition of shared growing knowledge. Relevant projects include:

- [Permapeople](https://permapeople.org/): collaborative plant knowledge, garden journals, and planning tools.
- [OpenFarm](https://github.com/openfarmcc/OpenFarm): structured growing guides designed for people and machines.
- [Practical Plants](https://practicalplants.org/wiki/practical_plants/): a plant encyclopedia combining readable articles and structured information.
- [Growstuff](https://www.growstuff.org/): an open gardening platform connecting crops, plantings, and harvest records.
- [OpenPlantDB](https://github.com/cwfrazier1/openplantdb): plant information distributed as data files in Git.
- [UC Integrated Pest Management](https://ipm.ucanr.edu/): university guidance for identifying, monitoring, and managing pests.

These are references and potential foundations, not bundled datasets or endorsements. Their content has its own reuse terms. SteelThumb's focus is connecting portable reference knowledge to sourced procedures and the observations that tell a gardener what happened next.

## How to contribute

Start with something you actually grow or a problem you have investigated. Open an issue or pull request with a crop profile, a procedure, a correction, a useful source, or a documented garden observation.

Describe the question, provide the evidence, identify the conditions, and explain what remains unknown. Small, well-supported improvements are valuable. The first milestone is a useful collection for one real garden, with a repeatable way for other people and agents to expand it.

The repository is licensed under the [MIT License](LICENSE). Referenced third-party material remains subject to its own license and attribution requirements.
