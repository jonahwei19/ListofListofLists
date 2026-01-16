# On-chip compliance monitoring

**Tag**: Security

## What it is
Verification logic embedded directly into AI accelerator chips that can prove compliance with international agreements without revealing proprietary information.

**Mechanism**:
- Dedicated circuitry on chip monitors training run characteristics (model size, data throughput, safety evaluation completion)
- Cryptographic attestation: chip produces signed proofs that specific conditions were met
- Zero-knowledge proofs allow verification without exposing model architecture or training data
- Auditors can verify compliance remotely without accessing proprietary systems
- Analogous to nuclear verification protocols adapted for AI

**Why this differs from software-based monitoring**: Software can be modified or bypassed. On-chip monitoring is tamper-resistant at hardware level.

## Why it matters
- Enables "trust but verify" for international AI agreements
- Privacy-preserving: proves compliance without revealing trade secrets
- Tamper-resistance prevents well-resourced actors from circumventing verification
- Provides technical foundation for enforceable international treaties

## Current state
- **Status**: Research
- **Bottlenecks**: Requires coordination with chip manufacturers during design phase; anti-tamper techniques against nation-state actors; defining what properties to verify; multi-year chip development cycles

## Who's working on it
- **Future of Life Institute**: Hardware-backed compute governance research
- **CNAS**: Research on securing AI chip supply chain

## Sources
- [Peregrine 2025 #70: On-Chip Monitoring Mechanisms](../sources/peregrine-2025/interventions/peregrine-070.md)
