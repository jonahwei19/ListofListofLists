# Verified software synthesis

**Tag**: Science

## What it is
Software synthesis systems that generate code together with machine-checkable proofs that the code satisfies functional, safety, and security specifications.

**Mechanism**:
- Developer provides high-level specification (what the code should do, security requirements)
- Synthesis system generates implementation code
- System simultaneously generates formal proof that code meets specification
- Proofs are machine-checkable—no trust in synthesis system required
- Targets embedded systems in critical infrastructure: SCADA, medical devices, communication networks
- Proves absence of entire vulnerability classes (buffer overflows, injection attacks) before deployment

**Why synthesis with proofs vs just synthesis**: AI-generated code is convenient but error-prone. Attaching proofs ensures correctness regardless of how the code was generated.

## Why it matters
- AI-powered attackers will exploit software vulnerabilities at scale; verified code eliminates vulnerability classes entirely
- Critical infrastructure (power grids, medical devices) runs software that can't be fixed after deployment
- Proofs are permanent—verified code stays verified regardless of future attack techniques
- Enables AI-generated code to be trusted in high-stakes applications

## Current state
- **Status**: Research
- **Recent progress**: LLM-based coding assistants increasingly capable at writing proof scripts alongside code
- **Bottlenecks**: Specification writing requires expertise; synthesis for complex systems still limited; computational cost; integration with existing codebases

## Who's working on it
- **DARPA I2O office**: Verified software synthesis research programs
- **Academic research groups**: Formal methods community

## Sources
- [Peregrine 2025 #168: Verified Software for Cyber Resilience](../sources/peregrine-2025/interventions/peregrine-168.md)
