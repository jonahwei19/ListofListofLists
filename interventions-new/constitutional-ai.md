# Constitutional AI

**Tag**: Science

## What it is
Using existing AI systems to evaluate and supervise future AI systems for security and harmlessness. Human input is provided through a set of rules (a Constitution) that an AI assistant uses to give feedback to a more advanced system in training. The process involves:

1. **Supervised learning phase**: Generate initial responses, self-critique against constitutional principles, revise responses, fine-tune on revisions
2. **RL phase**: Train model with AI-generated feedback based on constitutional principles (RLAIF)

The constitution can include external principles (UN Universal Declaration of Human Rights) and internal guidelines. Achieves Pareto improvement: models become both more helpful AND more harmless compared to pure RLHF.

## Why it matters
- Human feedback doesn't scale to billions of examples or superhuman outputs
- Enables supervision of systems whose outputs humans can't directly evaluate
- Provides a path to scale oversight without proportionally scaling human labor
- All harmlessness results came purely from AI supervision—no human data on harmlessness required
- Demonstrates scalable oversight is achievable

## Current state
- **Status**: Deployed (foundational to Claude)
- **Recent developments (2024-2025)**:
  - Claude's constitution: 75 points including UN Declaration of Human Rights principles
  - Collective Constitutional AI: Democratic input into constitution design, reduced bias across 9 social dimensions
  - Hybrid approaches: Claude 4/4.5 combine CAI for harmlessness + RLHF for helpfulness + specialized fine-tuning
  - Public constitution showed lower bias for disability status and physical appearance
- **Bottlenecks**: Constitution specification; ensuring AI evaluators faithfully apply principles; balancing multiple training objectives

## Who's working on it
- **Anthropic**: Pioneer, deployed in all Claude models
- Production AI systems increasingly combine CAI with RLHF and additional fine-tuning

## Sources
- [Peregrine 2025 #14: Constitutional AI](../sources/peregrine-2025/interventions/peregrine-014.md)
