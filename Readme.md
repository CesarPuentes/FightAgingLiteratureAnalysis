# Analysis of FightAging.org Content (2004-2025)

## Introduction

As someone passionate about entering the anti-aging research field and honing my machine learning skills, I created this project to pursue both goals simultaneously.

Please bear in mind that I am currently no expert in this field; I created this project mainly to orient myself, but I still believe it is worth sharing. Therefore, is worth noting that the analysis may contain imprecisions or areas for improvement.

I chose to analyze the rich content from FightAging.org, one of my favorite resources on the subject, made available under the Creative Commons Attribution 4.0 license.

While I'm still developing my expertise, I hope this data-driven exploration of longevity topics proves interesting and useful. The analysis is presented in four parts, starting with a foundational topic review using traditional text analysis methods.

The original content can be found at https://www.fightaging.org/.

# Part 1: Topic Analysis of FightAging.org using Classic NLP Methods

## Introduction

This first section of the analysis uses classic Natural Language Processing (NLP) techniques to map the primary themes and their evolution within the content of FightAging.org. By examining word and phrase frequencies, we can establish a foundational, human-interpretable understanding of the key topics discussed on the site from 2004 to 2025. This analysis reveals a clear narrative arc, from foundational concepts to the latest research frontiers, providing a baseline for the more advanced analyses in subsequent sections.

---

## Methodology

The analysis was performed on a dataset of 18,753 articles. The text from the title and body of each article was combined and preprocessed to create a clean corpus for analysis. This process involved:
1.  Converting all text to lowercase.
2.  Removing punctuation and numerical characters.
3.  Tokenizing the text into individual words.
4.  Filtering out common English stopwords and a custom list of domain-specific words (e.g., "aging", "research", "study") to reduce noise and highlight meaningful terms.

The primary analytical techniques were word frequency analysis, visualized as a word cloud, and bigram (two-word phrase) analysis to identify key concepts and their relationships.

---

## Key Findings: Overall Themes

An analysis of the entire 20-year period highlights the core pillars of discussion on FightAging.org. The most frequent bigrams reveal the central topics with remarkable clarity.



* **Dominant Concepts**: The most prominent topics are **"stem cells"** and **"senescent cells."** These two concepts represent the primary biological targets and therapeutic avenues discussed on the site.
* **Key Interventions**: **"Calorie restriction"** stands out as the most frequently mentioned lifestyle intervention, underscoring its foundational role in aging research.
* **Disease Focus**: There is a strong emphasis on specific age-related diseases, with **"Alzheimer's disease"** being the most discussed, followed by cancer and cardiovascular disease.
* **Biological Mechanisms**: The content delves deep into the underlying mechanisms of aging, with frequent mentions of **"cellular senescence," "chronic inflammation," "oxidative stress,"** and **"DNA damage."**

The word cloud visually confirms these findings, with **senescent**, **cell**, **treatment**, **disease**, **human**, and **alzheimers** being among the largest and most central terms, providing an at-a-glance summary of the blog's focus.



---

## Thematic Evolution Over Time

Dividing the content into three distinct eras—Initial (2004-2010), Middle (2011-2017), and Recent (2018-2025)—reveals a compelling narrative about the evolution of focus in the longevity field.



### 1. Initial Era (2004-2010): The Foundational Years

This period focused on broad, foundational concepts and the key figures driving the nascent longevity movement.
* **Top Topics**: Discussions were heavily dominated by **"stem cells"** and **"calorie restriction."**
* **Key Influencers**: The high frequency of **"Aubrey de Grey"** and **"Methuselah Foundation"** points to a focus on the philosophical and organizational origins of the modern anti-aging movement.

### 2. Middle Era (2011-2017): The Rise of Senolytics

This era marks a significant shift towards a more specific, mechanistic understanding of aging.
* **Emergence of a New Pillar**: While **"stem cells"** remained a top subject, **"senescent cells"** rose dramatically in prominence, signaling the scientific community's growing excitement around targeting senescent cells (senolytics).
* **Increased Disease Focus**: Mentions of **"Alzheimer's disease"** became more frequent.

### 3. Recent Era (2018-2025): The Clinical & Mechanistic Focus

The most recent period shows a maturation of the field, with a clear focus on translation and complex systems.
* **Senolytics Take the Lead**: **"Senescent cells"** surpassed "stem cells" as the single most discussed topic, reflecting its central role in current research.
* **Spotlight on Alzheimer's**: **"Alzheimer's disease"** is now the second most frequent topic, highlighting it as a critical target for interventions.
* **Towards Application**: The appearance of **"clinical trials"** signifies a major shift from preclinical research to human application.
* **New Frontiers**: The emergence of topics like the **"gut microbiome"** indicates a broadening of research into new systems that influence aging.

---

## Conclusion for Part 1

This manual analysis effectively illustrates the trajectory of the longevity field as chronicled by FightAging.org. The progression is logical: from foundational ideas and key influencers to a deep focus on a central mechanism (cellular senescence), and finally toward a mature stage emphasizing the treatment of specific diseases and the translation of research into clinical applications. These findings provide a clear and robust baseline that sets the stage for the automated topic modeling techniques explored in the next section.

# Part 2: Analysis of Specific Entities and Trends using NER

## Executive Summary

This Named Entity Recognition (NER) analysis moves beyond the broad topics identified in Part 1 to pinpoint the specific molecules, genes, and scientific concepts driving the conversations on FightAging.org. The results reveal a clear focus on the molecular mechanisms of aging, with the **Senescence-Associated Secretory Phenotype (SASP)** emerging as the most dominant topic in recent years. Key nutrient-sensing pathways like **mTOR** and energy-related molecules such as **NAD+** also feature prominently.

This granular analysis validates the findings of the manual topic review, providing the specific "why" behind the broader trends. For instance, the rise of the "senescent cells" topic is directly explained by the explosion of research into `SASP`. The two analyses are highly complementary, with the NER results offering a deeper, more technical layer of insight into the scientific narrative.

---

## Deep Dive into Key Entity Trends

The heatmap and trend plots provide a fascinating look at which specific scientific subjects have captured the attention of the longevity community over time.


### The Dominance of SASP and Senescence

The most striking finding is the dramatic rise in discussions around **`SASP` (Senescence-Associated Secretory Phenotype)**, particularly from 2016 onwards.
* **The Story:** SASP refers to the cocktail of inflammatory proteins and other molecules that senescent cells release, which can damage surrounding tissues. The discovery of SASP transformed senescent cells from a simple curiosity into a primary therapeutic target.
* **The Data:** The line chart shows the `SASP` trend line steeply climbing to become the most frequently discussed entity in recent years. The heatmap confirms this, with the brightest squares for `SASP` appearing from 2018 to 2023.

### The Nutrient-Sensing Axis: mTOR, AMPK, and Rapamycin

Your analysis correctly identifies a core network of related entities that are central to the biology of aging.
* **The Story:** **`mTOR`** and **`AMPK`** are key metabolic regulators that sense nutrient availability. Inhibiting mTOR (with drugs like **`Rapamycin`**) or activating AMPK are proven ways to extend lifespan in model organisms, often mimicking the effects of calorie restriction.
* **The Data:** The plots show a sustained and growing interest in `mTOR` over the last 15 years. The trends for `AMPK` and `Rapamycin` closely follow, confirming that the entire pathway, not just one molecule, is a major topic.

### The NAD+ Wave

* **The Story:** **`NAD+`** is a critical coenzyme for metabolism and cellular repair whose levels decline with age. Research into precursors like NMN and NR, which can boost NAD+ levels, created a massive wave of scientific and public interest.
* **The Data:** Both the heatmap and the individual trend plot for `NAD+` show a very distinct and sharp peak in discussion frequency around 2019-2020, perfectly capturing this wave of excitement.


---

## Connecting NER Results to Manual Analysis

This NER analysis enriches the initial bigram analysis by providing the specific scientific vocabulary behind the broad topics identified in Part 1.

* **"Senescent Cells" → The `SASP` Connection**: The bigram analysis showed "senescent cells" became the dominant topic. The NER analysis reveals **why**: the discussion was driven by research into their specific molecular signature, namely the **`SASP` (Senescence-Associated Secretory Phenotype)**, and inflammatory cytokines like **`IL-6`**.

* **"Calorie Restriction" → The Nutrient-Sensing Pathways**: The manual analysis identified "calorie restriction" as a foundational theme. The NER analysis uncovers the actual biological pathways being discussed: **`mTOR`**, **`AMPK`**, and **`SIRT1`**, moving from a general concept to specific molecular targets.

* **"Chronic Inflammation" → The Molecular Drivers**: The "chronic inflammation" bigram points to a key pillar of aging. The NER results identify the specific molecules being discussed: inflammatory markers like **`IL-6`**, **`TGF-β`**, and, more recently, components of the inflammasome like **`NLRP3`**.

---

## Additional Insights and Takeaways

Beyond direct validation, combining the analyses provides higher-level insights into the state of the longevity field.

### Key Molecules and Pathways to Watch

The data acts as an excellent guide to the most scientifically relevant targets in longevity research. For anyone entering the space, the analysis points to two clear pillars of focus:

1.  **Senescence and "Inflammaging":** This research revolves around targeting senescent cells. The key entities are **`SASP`**, specific cytokines like **`IL-6`**, and inflammatory complexes like the **`NLRP3` inflammasome**.
2.  **Metabolism and Nutrient Sensing:** This second pillar shows a persistent focus on the **`mTOR`** pathway, its inhibitor **`Rapamycin`**, the energy-sensing protein **`AMPK`**, and the metabolic coenzyme **`NAD+`**.

### From 'Why We Age' to 'How We Treat Aging': An LLM Interpretation

It is interesting to note that after an analysis of the data by Google's Gemini, the LLM model found a distinct narrative pattern: a **"Shift from 'Why We Age' to 'How We Treat Aging'."** This interpretation is based on the clear evolution of the blog's vocabulary. The early focus on foundational concepts ("longevity science," `Hayflick limit`) has been superseded by the language of medical intervention ("clinical trials," `Alzheimer's disease`, and specific druggable targets like `SASP`), indicating a maturing field focused on developing tangible therapies.

---

## Conclusion for Part 2

The NER analysis successfully provides a granular, technical view of the scientific discourse on FightAging.org. It confirms that the conversations are closely tied to the key molecular pathways and hallmarks of aging recognized by the scientific community. By combining the "what" from the manual analysis with the "why" from this NER analysis, we gain a comprehensive, multi-layered understanding of a field that has matured from asking foundational questions to engineering and testing specific, actionable molecular therapies.