# Automated Lean theorem proving

**Tag**: Science

## What it is
AI systems that automate mathematical proof generation in Lean4, addressing the critical shortage of skilled formal verification programmers.

**Mechanism**:
- Train AI on millions of synthetic Lean statements and existing proofs
- AI generates proof scripts given theorem statements as input
- Human experts verify and refine AI-generated proofs
- Enables verification of AI systems at scale (proofs about neural network behavior, training guarantees, safety properties)
- Tools integrate with Lean ecosystem (LeanDojo, mathlib)

**Why Lean specifically**: Lean4 has the most active AI proof community; large proof libraries exist; strong type system catches errors early. Only a few hundred humans worldwide are skilled Lean programmers—automation removes this bottleneck.

## Why it matters
- Formal verification provides mathematically certain guarantees (not just high probability from testing)
- Current bottleneck is human expert time—automation enables verification at scale
- Can prove properties about AI systems (safety constraints, behavioral bounds) with certainty
- Amazon already using Lean proofs in production (Cedar authorization language)

## Current state
- **Status**: Research with major 2024-2025 breakthroughs
- **Recent progress**:
  - DeepMind's AlphaProof achieved silver medal at IMO 2024 (proved 3/6 problems including hardest P6)
  - Harmonic AI raised $100M for hallucination-free AI using Lean4 backbone, reached gold-medal IMO performance
  - DeepSeek releasing open-source Lean4 prover models
  - Safe framework uses Lean4 to verify each step of LLM chain-of-thought reasoning
- **Bottlenecks**: Bridging LLM generation with formal syntax; specification writing still requires expertise; computational cost of complex proofs

## Who's working on it
- **DeepMind**: AlphaProof (trained on 80M synthetic Lean statements)
- **Harmonic AI**: Aristotle prover ($100M funding)
- **DeepSeek**: Open-source Lean4 prover models
- **LeanDojo**: AI-driven formal theorem proving

## Sources
- [Peregrine 2025 #173: Autoverification (Lean)](../sources/peregrine-2025/interventions/peregrine-173.md)
