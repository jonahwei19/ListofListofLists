# Critical infrastructure formal verification

**Tag**: Security

## What it is
Targeted formal verification of specific security properties in critical infrastructure components, particularly those underlying AI systems.

**Mechanism**:
- Identify highest-priority verification targets: Linux kernel, electrical grid control systems, AI training infrastructure
- Define specific properties to verify: memory safety, transaction timing, security boundary enforcement
- Apply focused verification efforts to these properties (not full system verification, which is intractable)
- Prioritize components where AI-powered attackers would have highest impact
- Results propagate through software supply chain (verified Linux kernel benefits everyone using Linux)

**Why targeted vs comprehensive**: Full formal verification of complex systems is intractable. Targeting specific high-impact properties (memory safety, security boundaries) is achievable and removes entire attack classes.

## Why it matters
- Infrastructure vulnerabilities undermine all higher-level AI safety measures (if attackers compromise training infrastructure, alignment work is moot)
- Linux kernel underlies most AI development infrastructure—verified kernel benefits entire ecosystem
- AI-powered attackers will systematically exploit infrastructure; verification removes their targets
- One-time verification investment provides permanent protection

## Current state
- **Status**: Research
- **Active targets**: Linux kernel memory safety, seL4 microkernel (already verified), Amazon Cedar authorization
- **Bottlenecks**: Complexity of legacy systems; specification of security properties; verification tooling for low-level code

## Who's working on it
- **Amazon**: Cedar authorization language with Lean proofs (production deployed)
- **seL4 project**: Fully verified microkernel
- **Academic formal methods groups**: Infrastructure verification research

## Sources
- [Peregrine 2025 #174: Formal Verification of AI Hardware](../sources/peregrine-2025/interventions/peregrine-174.md)
- [Atlas AI Resilience Gap Map: Cyber Offense-Defense Asymmetry](../sources/atlas-ai-resilience/proposals/cyber-offense-defense-asymmetry.md)
