# Analysis of FightAging.org Content (2004-2025)

## Introduction

As someone passionate about entering the anti-aging research field and honing my machine learning skills, I created this project to pursue both goals simultaneously.

Please bear in mind that I am currently no expert in this field; I created this project mainly to orient myself, but I still believe it is worth sharing. Therefore, is worth noting that the analysis may contain imprecisions or areas for improvement.

I chose to analyze the rich content from FightAging.org, one of my favorite resources on the subject, made available under the Creative Commons Attribution 4.0 license.

While I'm still developing my expertise, I hope this data-driven exploration of longevity topics proves interesting and useful. The analysis is presented in four parts, starting with a foundational topic review using traditional text analysis methods.

The original content can be found at https://www.fightaging.org/.

# Part 1: Topic Analysis of FightAging.org using Classic NLP Methods

## Introduction

This section uses classic **Natural Language Processing (NLP)** techniques to map primary themes and their evolution within FightAging.org content. Examining word and phrase frequencies establishes a foundational, human-interpretable understanding of key topics from 2004 to 2025, revealing an arc from foundational concepts to research frontiers.

---

## Methodology

The analysis used 18,753 articles. Text from the title and body of each article was combined and preprocessed:
1.  Converted text to **lowercase**.
2.  **Removed punctuation** and numerical characters.
3.  **Tokenized** text into words.
4.  **Filtered out** common English stopwords and custom domain-specific words (e.g., "aging," "research") to reduce noise.

Primary techniques were **word frequency analysis** (visualized as a word cloud) and **bigram** (two-word phrase) analysis.

---

## Key Findings: Overall Themes

Analysis of the 20-year period highlights core discussion pillars. The most frequent bigrams clarify central topics:

* **Dominant Concepts**: **"Stem cells"** and **"senescent cells"** are the primary biological targets and therapeutic avenues.
* **Key Interventions**: **"Calorie restriction"** is the most frequently mentioned lifestyle intervention.
* **Disease Focus**: **"Alzheimer's disease"** is the most discussed age-related disease, followed by cancer and cardiovascular disease.
* **Biological Mechanisms**: Frequent mentions of **"cellular senescence," "chronic inflammation," "oxidative stress,"** and **"DNA damage"** show a focus on underlying mechanisms.

The word cloud visually confirms these findings, with **senescent**, **cell**, **treatment**, **disease**, **human**, and **alzheimers** as central terms.

---

## Thematic Evolution Over Time

Dividing content into three eras—Initial (2004-2010), Middle (2011-2017), and Recent (2018-2025)—shows the field's evolving focus.

### 1. Initial Era (2004-2010): Foundational Years

This period focused on broad concepts and key figures.
* **Top Topics**: Discussions were dominated by **"stem cells"** and **"calorie restriction."**
* **Key Influencers**: High frequency of **"Aubrey de Grey"** and **"Methuselah Foundation"** points to a focus on the philosophical and organizational origins of the movement.

### 2. Middle Era (2011-2017): Rise of Senolytics

This era shifted toward a more specific, mechanistic understanding.
* **Emergence of a New Pillar**: **"Senescent cells"** rose dramatically in prominence, signaling excitement around targeting them (**senolytics**). **"Stem cells"** remained a top subject.
* **Increased Disease Focus**: Mentions of **"Alzheimer's disease"** became more frequent.

### 3. Recent Era (2018-2025): Clinical & Mechanistic Focus

The most recent period shows field maturation, focusing on translation and complex systems.
* **Senolytics Take the Lead**: **"Senescent cells"** surpassed "stem cells" as the most discussed topic.
* **Spotlight on Alzheimer's**: **"Alzheimer's disease"** is the second most frequent topic.
* **Towards Application**: The appearance of **"clinical trials"** signifies a shift from preclinical research to human application.
* **New Frontiers**: Topics like the **"gut microbiome"** indicate a broadening of research into new systems.

---

## Conclusion for Part 1

This analysis illustrates the trajectory of the longevity field chronicled by FightAging.org. The progression moves from foundational ideas and key influencers to a focus on a central mechanism (**cellular senescence**), and finally toward a mature stage emphasizing the treatment of specific diseases and the translation of research into clinical applications.

***

# Part 2: Analysis of Specific Entities and Trends using NER

## Executive Summary

**Named Entity Recognition (NER)** analysis pinpoints specific molecules, genes, and scientific concepts. Results focus on molecular mechanisms, with the **Senescence-Associated Secretory Phenotype (SASP)** dominant in recent years. Nutrient-sensing pathways like **mTOR** and energy molecules like **NAD+** also feature prominently.

This granular analysis validates Part 1, providing the specific biological basis for broader trends (e.g., the rise of "senescent cells" is explained by research into `SASP`).

---

## Deep Dive into Key Entity Trends

### The Dominance of SASP and Senescence

Discussions around **`SASP` (Senescence-Associated Secretory Phenotype)** rose dramatically from 2016 onward.
* **Concept:** SASP is the cocktail of inflammatory proteins senescent cells release, which damages surrounding tissues. Its discovery transformed senescent cells into a primary therapeutic target.
* **Data:** The `SASP` trend line steeply climbs to become the most frequently discussed entity in recent years, with the highest frequency between 2018 and 2023.

### The Nutrient-Sensing Axis: mTOR, AMPK, and Rapamycin

A core network of related entities central to the biology of aging is consistently discussed.
* **Concept:** **`mTOR`** and **`AMPK`** are key metabolic regulators. Inhibiting mTOR (with drugs like **`Rapamycin`**) or activating AMPK extends lifespan in model organisms.
* **Data:** Interest in `mTOR` is sustained and growing. Trends for `AMPK` and `Rapamycin` closely follow, confirming the entire pathway is a major topic.

### The NAD+ Wave

* **Concept:** **`NAD+`** is a critical coenzyme for metabolism and repair that declines with age. Research into precursors (NMN, NR) created a wave of interest.
* **Data:** The trend plot for **`NAD+`** shows a distinct and sharp peak around 2019-2020.

---

## Connecting NER Results to Manual Analysis

NER analysis provides the specific scientific vocabulary for the broad topics in Part 1.

* **"Senescent Cells" $\rightarrow$ The `SASP` Connection**: The dominant topic "senescent cells" is driven by research into their molecular signature, the **`SASP`**, and cytokines like **`IL-6`**.

* **"Calorie Restriction" $\rightarrow$ The Nutrient-Sensing Pathways**: The foundational theme "calorie restriction" translates into discussions of specific biological pathways: **`mTOR`**, **`AMPK`**, and **`SIRT1`**.

* **"Chronic Inflammation" $\rightarrow$ The Molecular Drivers**: The "chronic inflammation" bigram links to specific molecules: inflammatory markers like **`IL-6`**, **`TGF-β`**, and the **`NLRP3` inflammasome**.

---

## Additional Insights and Takeaways

Combining the analyses provides higher-level insights into the state of the longevity field. The data points to two clear pillars of focus:

1.  **Senescence and "Inflammaging":** Targeting senescent cells. Key entities are **`SASP`**, cytokines like **`IL-6`**, and the **`NLRP3` inflammasome**.
2.  **Metabolism and Nutrient Sensing:** Persistent focus on the **`mTOR`** pathway, its inhibitor **`Rapamycin`**, the energy-sensing protein **`AMPK`**, and the metabolic coenzyme **`NAD+`**.

### LLM Interpretation: Shift from 'Why We Age' to 'How We Treat Aging'

An analysis of the data by Google's Gemini found a distinct narrative: a **"Shift from 'Why We Age' to 'How We Treat Aging'."** This is based on the blog's vocabulary evolving from foundational concepts ("longevity science," `Hayflick limit`) to the language of medical intervention ("clinical trials," `Alzheimer's disease`, and specific druggable targets like `SASP`).

---

## Conclusion for Part 2

The NER analysis provides a granular, technical view of the scientific discourse, confirming its alignment with key molecular pathways and hallmarks of aging. Combining the "what" (manual analysis) with the "why" (NER analysis) gives a comprehensive, multi-layered understanding of a field focused on developing tangible therapies.

***

# Part 3: Unsupervised Topic Modeling with BERTopic

## 1. Stand-Alone Analysis

**BERTopic**, an unsupervised learning technique, groups documents by underlying semantic meaning, clustering full articles into coherent "topics." This reveals the natural structure of conversations on FightAging.org.

### Key Findings from BERTopic

* **Coherent Topics Emerge:** The model identified distinct, scientifically relevant topics:
    * **Topic 0:** **Mitochondria** and oxidative stress.
    * **Topic 3:** **Cellular Senescence**.
    * **Topic 5 & 13:** **Stem Cells** (likely different research aspects).
    * **Topic 7:** **Gut Microbiome**.
    * **Topic 15:** **Epigenetics** and methylation clocks.

* **Temporal Trends Confirm Narrative:** The "Topics over Time" graph reveals the lifecycle of discussions.
    * **The Bedrock Topic:** **Mitochondrial aging (Topic 0)** is the most consistently high-frequency topic, an enduring pillar of research.
    * **The Rise of Senescence:** The **Senescence topic (Topic 3)** shows a dramatic rise starting around 2012, becoming a dominant topic in the last decade.
    * **The Rise of the Microbiome:** The **Gut Microbiome topic (Topic 7)** is nearly absent before 2015, then begins a steady climb.
    * **Early Dominance, Later Submergence:** Topics like **Cryonics (Topic 1)**, **Stem Cells (Topic 5)**, and **Telomeres (Topic 4)** were major drivers in the first decade but have since decreased in relative frequency.

---

## 2. Relation to Previous Experiments

* **From "What" and "Why" to "How It's Organized"**: Manual Analysis established **what** the topics were; NER analysis established **why** they mattered; BERTopic shows **how** these ideas are structurally related by grouping entire documents.

* **Validation Through a Different Lens:**
    * The "Senescence" topic (Topic 3) in BERTopic includes keywords "senescent," "senescent cells," and "`sasp`." Its rise in the timeline graph validates the earlier findings of the "senescent cells" bigram and the `SASP` entity.
    * BERTopic automatically created a coherent "Mitochondria" topic (Topic 0) by clustering articles discussing "mitochondria," "mtdna," "oxidative," and "mitophagy," discovering the structural connection between individual entities.

* **A Top-Down Confirmation:** The previous analyses were "bottom-up" (counting small pieces); BERTopic is "top-down" (grouping whole documents by meaning). The confirmation between the two approaches indicates a robust overall analysis.

---

## 3. Gemini's Interpretation

The discourse on FightAging.org, and likely the field, is built upon **three foundational pillars** while exploring new frontiers.

### The Three Pillars of Aging Discourse

1.  **Cellular Housekeeping & Damage (Wear and Tear):** Represented by **Topic 0: Mitochondria**. This is the most enduring, fundamental topic, addressing the constant, low-level damage.
2.  **Cellular Fate & Regeneration (Running Out of Parts):** Represented by **Topic 5: Stem Cells** and **Topic 4: Telomeres**. Dominant in early years, focused on the decline of cellular division and tissue regeneration.
3.  **Cellular Senescence & Inflammation (Zombie Cell):** Represented by **Topic 3: Senescence**. A minor topic initially, it has exploded in the last decade, focusing on how malfunctioning cells actively drive the aging process.

### The New Frontier: Systems Biology

The recent emergence of the **Gut Microbiome (Topic 7)** and **Epigenetic Clocks (Topic 15)** shows a move toward a more complex, **systems-level understanding**. The field increasingly recognizes that aging is driven by an interconnected network of processes. The BERTopic analysis captures the emergence of this holistic paradigm.