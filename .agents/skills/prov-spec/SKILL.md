---
name: prov-spec
description: Reference W3C PROV when designing or reviewing provenance records, mapping source lineage, or producing PROV representations for Almanac knowledge and garden observations.
---

# W3C PROV reference

Use the W3C specifications to resolve provenance semantics. Open the relevant source before making a conformance claim; if unavailable, state what remains unchecked.

## Authoritative sources

- [PROV Overview](https://www.w3.org/TR/prov-overview/): choose the appropriate document in the specification family.
- [PROV-DM](https://www.w3.org/TR/2013/REC-prov-dm-20130430/): entities, activities, agents, and their relationships.
- [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/): RDF/OWL representation and property definitions.
- [PROV-N](https://www.w3.org/TR/2013/REC-prov-n-20130430/): notation for exchanging or illustrating provenance.
- [PROV Constraints](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/): validity, inference, and ordering requirements.

## Applying PROV

Identify the record's entities, activities, and responsible agents before choosing a representation. An Almanac mapping might treat a dated observation or profile revision as an entity, a measurement or editing operation as an activity, and a gardener or software agent as an agent. This is a local modeling choice.

Distinguish an activity's use of an entity from an entity's generation by an activity, derivation from another entity, and attribution to an agent. Use PROV-O's defined property direction when emitting RDF; consult qualified relations when roles or other relationship details matter.

Preserve revision identity and actual event times where known. Leave unknown actors, timestamps, and causal relationships explicit rather than fabricating them. A source citation alone does not establish the full process that produced a claim, and provenance alone does not prove its truth.

For a mapping or export, show the identifiers and relationships, cite the relevant specification sections, and distinguish syntax checks from PROV constraint validation. Label illustrative records as examples.

When integrating with OKF, read the sibling [okf-spec skill](../okf-spec/SKILL.md). Document any PROV mapping or extension separately; an OKF source list is not automatically a PROV serialization.
