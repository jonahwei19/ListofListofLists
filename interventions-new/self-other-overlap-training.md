# Self-other overlap training

**Tag**: Science

## What it is
Fine-tuning technique that reduces AI deception by minimizing the difference between how models internally represent self-referencing scenarios vs. other-referencing scenarios. Components:

- **SOO Loss calculation**: Mean Squared Error (MSE) between self-referencing and other-referencing activations at the self-attention projection layer
- **Activation alignment**: Push model representations of "what I would do" toward "what they would do" during potentially deceptive scenarios
- **Minimal capability impact**: Loss function targets deception-relevant representations while preserving general task performance

Inspired by cognitive neuroscience research on empathy—large body of evidence links neural self-other overlap to pro-sociality in humans.

## Why it matters
- Deception requires self-other distinctions not needed for task performance
- Selecting against these distinctions removes a prerequisite for deceptive behavior
- Complements behavioral alignment (RLHF) by targeting internal representations
- **Theoretical basis**: Many configurations in weight space have similar capabilities; SOO pushes learning toward configurations with maximal overlap, selecting for honest models

## Current state
- **Status**: Research (promising early results)
- **Recent developments (2025)**:
  - ICLR 2025 submission (later withdrawn for revision)
  - Yudkowsky's preliminary positive reaction—given his typically critical stance, suggests the approach is "worth further scrutiny"
  - Related approach: SELF-MONITOR framework achieved 43.8% reduction in deceptive alignment behaviors by enabling models to oversee their own chain-of-thought reasoning
- **Bottlenecks**: Testing against adversarial sleeper agent scenarios; integration with other alignment methods; scaling validation

## Who's working on it
- **AE Studio**: Primary research team. Results across model scales:
  - Mistral-7B-Instruct-v0.2: Deceptive responses dropped 73.6% → 17.2%
  - Gemma-2-27b-it: 100% → 9.3%
  - CalmeRys-78B-Orpo-v0.1: 100% → 2.7%
  - Notably: 100% → 0% on held-out scenario not in training data
- **Alignment Forum/LessWrong community**: Active discussion and review

## Sources
- [Peregrine 2025 #12: Cooperative Alignment](../sources/peregrine-2025/interventions/peregrine-012.md)
