# Interpretable-by-design models

**Tag**: Science

## What it is
Research building interpretability constraints directly into model training from the start, rather than analyzing black-box models after the fact. Existing approaches:

- **Concept Bottleneck Models (CBMs)**: Two-module architecture with concept extractor → sparse linear layer; predictions traceable to relevant concepts
- **Hybrid CBMs**: Pre-trained Concept Translator combined with CLIP concept embeddings forming Static Concept Bank
- **Post-hoc CB-Autoencoders**: Transform pretrained generative models into interpretable versions with minimal concept supervision
- **Predictive Concept Decoders**: Compress activations into concept lists; decoder answers questions about network reasoning

For frontier-scale LLMs, cost estimates reach billions of dollars—prohibitive for safety-focused organizations.

## Why it matters
- Post-hoc interpretability fights an uphill battle against models not designed to be understood
- Training with interpretability as a constraint could produce inherently understandable systems
- Makes opacity a choice rather than a given
- **Performance parity**: CBM case studies show performance on par or superior to black-box models (N-CMAPSS aircraft engine dataset)

## Current state
- **Status**: Idea (for frontier LLMs) / Research (for specialized domains)
- **Recent developments (2025)**:
  - CVPR 2025: HybridCBM, Language-Guided CBM for continual learning, DOT-CBM for fine-grained visual-concept relations
  - Predictive Concept Decoders (December 2025): Successfully detect jailbreaks, implanted information, and latent user attributes
  - CBMs for prognostics achieving parity with black-box models with limited labeled concepts
  - CBM-HNMU: Distills corrected knowledge back into black-box models after identifying/removing detrimental concepts
- **Bottlenecks**:
  - Prohibitive cost at frontier scale (billions)
  - Concept annotation labor-intensive
  - VLM-based concept supervision trades applicability for concept quality
  - Unknown whether interpretability constraints preserve capability at scale

## Who's working on it
- **Stanford ML Group**: Original Concept Bottleneck Models (Koh et al., ICML 2020)
- **CVPR 2025 research teams**: HybridCBM, Language-Guided CBM, DOT-CBM
- **CLIP/Foundation model researchers**: Exploring "If Concept Bottlenecks are the Question, are Foundation Models the Answer?"
- **Industrial researchers**: Applying CBMs to prognostics and reliability engineering

## Sources
- [Peregrine 2025 #41: Interpretable Frontier Models](../sources/peregrine-2025/interventions/peregrine-041.md)
