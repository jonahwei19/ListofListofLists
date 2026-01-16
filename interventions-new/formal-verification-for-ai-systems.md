# Formal verification for AI systems

**Tag**: Science

## What it is
Mathematical formal verification applied across the AI stack—from proof assistants to generated code to hardware infrastructure. Three complementary approaches:

**Automated theorem proving (Lean)**: Tools that automate formal verification, addressing the critical shortage of skilled Lean programmers worldwide (estimated at only a few hundred). Would enable implementations of AI architectures with much stronger formal guarantees. Commercial labs are unlikely to prioritize this despite its importance.

**Verified software synthesis**: Software synthesis systems that generate code with machine-checkable proofs satisfying functional, safety, and security specifications. Targets embedded systems in critical infrastructure (SCADA, medical devices, communication networks). Creates mathematical models of software behavior and proves absence of entire vulnerability classes before deployment.

**Hardware and infrastructure verification**: Focused verification of specific properties (memory safety, transaction timing, security boundaries) in critical AI components and surrounding infrastructure. Priority targets include Linux kernel and systems controlling critical infrastructure like electrical grids.

## Why it matters
- Formal verification provides strongest possible behavioral guarantees—proves security properties mathematically
- Eliminates entire vulnerability classes that AI-powered attackers might exploit
- Hardware/infrastructure vulnerabilities undermine all higher-level safety measures
- Rare expertise bottlenecks verification at scale—automation democratizes access
- Traditional testing finds bugs in test cases; formal methods prove absence of bugs

## Current state
- **Status**: Research with major 2024-2025 breakthroughs
- **Recent progress (2024-2025)**:
  - DeepMind's AlphaProof achieved silver medal at IMO 2024, proving 3/6 problems including hardest problem P6 (solved by only 5 of 609 humans)
  - Harmonic AI raised $100M to build hallucination-free AI using Lean4 verification backbone
  - Harmonic's Aristotle system reached gold-medal-level IMO performance
  - DeepSeek releasing open-source Lean4 prover models
  - Safe framework uses Lean4 to verify each step of LLM chain-of-thought reasoning, detecting hallucinations
  - LLM-based coding assistants increasingly capable at writing proof scripts
  - Amazon using Lean for Cedar authorization language (AWS Verified Permissions, Verified Access)
- **Bottlenecks**: Few hundred skilled Lean programmers globally; bridging LLM generation with formal verification syntax; specification writing expertise; computational cost of complex verification

## Who's working on it
- **DeepMind**: AlphaProof system, trained on 80M synthetic Lean statements
- **Harmonic AI**: Aristotle prover, $100M funding for formal verification + AI
- **DeepSeek**: Open-source Lean4 prover models
- **LeanDojo**: AI-driven formal theorem proving in Lean ecosystem
- **DARPA I2O office**: Verified software synthesis
- **Amazon**: Cedar language production deployment

## Sources
- [Peregrine 2025 #173: Autoverification (Lean)](../sources/peregrine-2025/interventions/peregrine-173.md)
- [Peregrine 2025 #174: Formal Verification of AI Hardware](../sources/peregrine-2025/interventions/peregrine-174.md)
- [Peregrine 2025 #168: Verified Software for Cyber Resilience](../sources/peregrine-2025/interventions/peregrine-168.md)
- [Atlas AI Resilience Gap Map: Cyber Offense-Defense Asymmetry](../sources/atlas-ai-resilience/proposals/cyber-offense-defense-asymmetry.md)
