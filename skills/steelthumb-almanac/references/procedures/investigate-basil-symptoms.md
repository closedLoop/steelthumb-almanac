---
type: Procedure
title: Investigate basil symptoms
description: Distinguish observations, possible causes, and evidence needed before intervention.
status: draft
sources:
- id: core
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md
  title: SteelThumb basil cultivation reference
- id: tasks
  resource: https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml
  title: SteelThumb task instruction templates
- id: clemson
  resource: https://hgic.clemson.edu/factsheet/basil/
  title: Basil — Clemson Extension
- id: ucipm
  resource: https://ipm.ucanr.edu/home-and-landscape/basil/
  title: Basil — UC Integrated Pest Management
- id: maine
  resource: https://extension.umaine.edu/gardening/2023/07/19/what-could-be-eating-my-basil-seedlings/
  title: What could be eating my basil seedlings? — Maine Extension
- id: cornell
  resource: https://www.vegetables.cornell.edu/pest-management/disease-factsheets/basil-downy-mildew/
  title: Basil Downy Mildew — Cornell
- id: umn
  resource: https://extension.umn.edu/disease-management/basil-downy-mildew
  title: Basil downy mildew — Minnesota Extension
- id: ncsu
  resource: https://emgv.ces.ncsu.edu/2022/07/why-are-the-leaves-of-my-basil-turning-yellow/
  title: Why Are the Leaves of My Basil Turning Yellow? — NC State Extension
- id: magnesium
  resource: https://www.e-gro.org/pdf/E303.pdf
  title: Magnesium Deficiency of Hydroponic and Container Grown Basil — e-GRO
steelthumb:
  ontology_version: '0.2'
  review_status: unreviewed-source-adaptation
  license: CC-BY-SA-4.0
  relations:
  - predicate: applies_to
    target: /crops/basil.md
---

# Investigate basil symptoms

Applies to [basil](../crops/basil.md) within the scope stated below.

## Purpose and scope

Investigate a concern without turning a symptom into a diagnosis. The original reference discusses pests, disease, and environmental causes; its abbreviated task responses are not diagnostic tests or verified treatments.[^core][^tasks]

## Steps

1. Record plant identity, stage, dates, symptom distribution, both leaf surfaces, medium condition, recent care, and nearby affected plants. Photographs and measurements are useful when available.
2. Describe the observation before choosing a cause. Use the topic table below to locate relevant candidate references.
3. Look for distinguishing evidence and consider alternative explanations. Preserve uncertainty if identification is unresolved.
4. Choose a supported check or intervention appropriate to the identified problem, growing setting, and intended food use. Product-specific treatment requires its applicable instructions.
5. Record the actual action, other changes, and a follow-up observation. A before/after improvement alone does not isolate its cause.

These investigation and recording steps are Almanac conventions. The following topics and sources were present in the earlier compilation and still require claim-level source review.[^core]

| Observed concern | Candidate topics from the reference | Source leads |
| --- | --- | --- |
| Insects, honeydew, webbing, or feeding marks | Aphids, whiteflies, spider mites, thrips | Clemson and UC IPM [^clemson][^ucipm] |
| Holes, missing seedlings, trails, or frass | Slugs/snails, flea beetles, caterpillars/cutworms, leaf miners | Maine, Clemson, UC IPM [^maine][^clemson][^ucipm] |
| Root abnormalities or persistent poor growth | Nematodes, root disease, medium conditions | Original compilation and UC IPM [^core][^ucipm] |
| Yellowing and suspicious leaf undersides | Downy mildew among several explanations | Cornell and Minnesota [^cornell][^umn] |
| Wilt, stem discoloration, lesions, or collapse | Fusarium wilt, bacterial wilt/leaf spots, root/stem rots, damping off | Original compilation and extension references [^core][^clemson][^ucipm] |
| Gray mold or powdery growth | Botrytis and other fungal problems | Original compilation; identity and treatment need review [^core] |
| Yellowing without an established pathogen | Water/medium problems, nutrient availability, other stress | NC State and e-GRO [^ncsu][^magnesium] |
| Bleaching, blackening, distorted growth, or stretch | Cold exposure, acclimation/light stress, chemical exposure | Original compilation; record actual conditions [^core] |
| Flowering | Plant identity, maturity, and growing objective | [Harvest](harvest-basil.md) or [seed saving](save-basil-seed.md) |

## Task responses awaiting review

The old catalog proposed leaf rinsing, insecticidal soap, increased humidity for mites, slug/snail bait or barriers, culling for suspected downy mildew or Fusarium, and fertilizer or magnesium supplementation for yellowing. These are retained as review topics, not automatic actions triggered by appearance.[^tasks]

In particular, `magnesium_deficiency_fix` ties supplementation to yellowing on newer leaves without adequate confirmation. A narrow visual rule should not be promoted to a nutrient diagnosis. The old text's cinnamon treatment for damping off, fixed pesticide schedules, and immediate disposal shortcuts have not been adopted as supported procedures.[^tasks][^core]

This consolidates `rinse_leaves`, `spray_insecticidal_soap`, `humidity_increase_for_mites`, `slug_snail_exclusion`, `downy_mildew_cull`, `fusarium_wilt_disposal`, `nutrient_deficiency_fix`, and `magnesium_deficiency_fix`. No recorded outcomes demonstrate these interventions here.[^tasks]

## Evidence and reuse

This document reorganizes earlier SteelThumb material. Source attribution is retained; the underlying horticultural claims have not been rechecked. It records no real-world attempts or outcomes. Adapted from SteelThumb contributors under CC-BY-SA-4.0; see [attribution and changes](../sources/steelthumb-basil.md).[^tasks]

[^core]: [SteelThumb basil cultivation reference](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/domain-knowledge/core_facts.md).
[^tasks]: [SteelThumb task instruction templates](https://github.com/closedloop-technologies/steelthumb/blob/decb3b444a7bedd8b0f5c2112350a682e7797536/steelthumb_v1_basil/tasks/tasks.yaml).
[^clemson]: [Basil — Clemson Extension](https://hgic.clemson.edu/factsheet/basil/).
[^ucipm]: [Basil — UC Integrated Pest Management](https://ipm.ucanr.edu/home-and-landscape/basil/).
[^maine]: [What could be eating my basil seedlings? — Maine Extension](https://extension.umaine.edu/gardening/2023/07/19/what-could-be-eating-my-basil-seedlings/).
[^cornell]: [Basil Downy Mildew — Cornell](https://www.vegetables.cornell.edu/pest-management/disease-factsheets/basil-downy-mildew/).
[^umn]: [Basil downy mildew — Minnesota Extension](https://extension.umn.edu/disease-management/basil-downy-mildew).
[^ncsu]: [Why Are the Leaves of My Basil Turning Yellow? — NC State Extension](https://emgv.ces.ncsu.edu/2022/07/why-are-the-leaves-of-my-basil-turning-yellow/).
[^magnesium]: [Magnesium Deficiency of Hydroponic and Container Grown Basil — e-GRO](https://www.e-gro.org/pdf/E303.pdf).
