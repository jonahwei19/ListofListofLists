# Training data attribution

**Tag**: Science

## What it is
Methods to trace model behaviors back to specific training examples using techniques like influence functions and counterfactual simulation. Rather than treating the model as a black box shaped by post-training alignment, attribution lets you identify which training data caused particular tendencies and modify the source directly.

## Why it matters
- Enables root-cause fixes for alignment issues rather than patching symptoms with RLHF
- Provides verifiable evidence for alignment claims (useful for audits and regulation)
- Could reveal unexpected sources of problematic behaviors that post-training methods miss

## Current state
- **Status**: Research
- **Bottlenecks**: Scaling influence functions to frontier model size; processing and interpreting massive attribution results

## Who's working on it
- **Anthropic**: Leading work, though much remains unpublished

## Sources
- [Peregrine 2025 #1: Training Data Attribution](../sources/peregrine-2025/interventions/peregrine-001.md)
