# Capability unlearning

**Tag**: Security

## What it is
Research distinguishing between unlearning knowledge (removing specific content from training data) versus unlearning capabilities (removing ability to perform tasks like writing malicious code). Components:

- **Knowledge unlearning**: Remove specific facts; success metric = model indistinguishable from one never trained on that content
- **Capability unlearning**: Remove ability to perform tasks; no direct link between training data and resulting abilities
- **Reliable methods**: RMU (Reliable Machine Unlearning) and TAR (Targeted Adversarial Regularization) show some promise
- **Evaluation frameworks**: Standardized tests to verify actual removal vs. superficial suppression

## Why it matters
- **Superficial removal problem**: Research shows many unlearning methods just suppress outputs, leaving knowledge vulnerable to extraction
- **Hindi filler attack**: Prepending Hindi filler text to prompts recovers 57.3% accuracy of "unlearned" information
- **Dual-use dilemma**: Removing security vulnerability knowledge may prevent models from identifying similar vulnerabilities (beneficial use)
- **Privacy leakage risk**: Unlearning creates two models (original and unlearned)—adversaries can exploit discrepancies to recover "erased" data
- **RLHF limitations**: Only suppresses outputs, doesn't remove underlying knowledge

## Current state
- **Status**: Research (active, fundamental limitations discovered)
- **Recent developments (2025)**:
  - ICML 2025 Workshop on Machine Unlearning for Generative AI convening safety, privacy, and policy experts
  - Harvard/Google DeepMind research reveals "no single approach works in all situations"
  - arXiv paper "Does Machine Unlearning Truly Remove Knowledge?" demonstrates extraction vulnerabilities
  - arXiv paper "Open Problems in Machine Unlearning for AI Safety" catalogs fundamental barriers
- **Bottlenecks**:
  - No clear success metrics for capability (vs. knowledge) unlearning
  - Neural networks encode information across millions of parameters—precise deletion degrades performance
  - Adversarial/whitebox attacks can recover "erased" data
  - Dual-use knowledge cannot be selectively removed for only harmful uses

## Who's working on it
- **Harvard D^3 Institute**: "The Myth of Machine Unlearning" research on data removal complexities
- **Google DeepMind**: Fundamental limitations research
- **ICML 2025 Workshop organizers**: Building standardized evaluation frameworks
- **Academic community**: RMU, TAR, and ELM methods development (GitHub: franciscoliu/Awesome-GenAI-Unlearning)

## Sources
- [Peregrine 2025 #19: Unlearning Capabilities](../sources/peregrine-2025/interventions/peregrine-019.md)
