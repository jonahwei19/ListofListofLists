# Achieving a Secure AI Agent Ecosystem (Schmidt Sciences)

**Source**: PDF from Schmidt Sciences
**Date processed**: 2026-01-11
**Total items**: ~40 proposals across 3 pillars

## Overview

Report on securing AI agent ecosystems. Three pillars:
1. Securing agents from external compromise
2. Securing assets entrusted to agents
3. Securing systems from malicious agents

## Mapping to Entries

### Maps to existing problems

Most proposals map to **contain-unsafe-ai** (controlling AI systems) and **defend-against-ai-harms** (preventing misuse):

| Proposal | Maps to | Notes |
|----------|---------|-------|
| Graceful failure to safe state | [[contain-unsafe-ai]] | Control intervention |
| Staged containment system | [[contain-unsafe-ai]] | Control intervention |
| Disposable agents | [[contain-unsafe-ai]] | Control intervention |
| Pre-deployment evaluation | [[verify-ai-alignment]] | Eval intervention |
| Provable traits via formal methods | [[verify-ai-alignment]] | Verification intervention |
| Tamper-proof logging | [[verify-ai-alignment]] | Monitoring for deception |
| AI-based code verification | [[defend-against-ai-harms]] | Cyber defense |
| Autonomous monitoring agents | [[defend-against-ai-harms]] | Cyber defense |
| Honeypots for AI agents | [[defend-against-ai-harms]] | Detection |

### New interventions to consider

| Proposal | Potential intervention | Why new |
|----------|----------------------|---------|
| Agent SBOM (Software Bill of Materials) | [[agent-supply-chain-security]] | AI-specific supply chain tracking |
| Common reference architecture | [[agent-architecture-standards]] | No current entry for agent standards |
| Agent attestation & identity | [[agent-ids-and-reputation]] | Already exists, could expand |
| Inter-agent trust mechanisms | [[agent-ids-and-reputation]] | Already exists |
| Rule-based authorization limits | [[hardened-runtime-containment]] | Already exists |
| Data/instruction plane separation | [[hardened-runtime-containment]] | Already exists |
| Multi-agent collusion detection | [[multi-agent-threat-monitoring]] | Already exists |

### Not creating entries (too specific or overlapping)

- Agent versioning system - implementation detail under SBOM
- Secure communication protocol - implementation detail
- Agent OS with TPM - hardware-specific
- Constrain to verifiable code - technique under formal verification
- AI control via insider threat - research direction
- AI control via control theory - research direction
- Integrity-bound authorization - technique under containment
- Activity trace taxonomy - implementation detail
- AI summarization of traces - technique
- Definition languages for restrictions - implementation detail
- Agent reputation signatures - under agent-ids-and-reputation
- Hunter agents for rogue detection - under multi-agent-threat-monitoring
- Research on stealth/evasion - research direction
- Standardized testing environment - infrastructure, not intervention

## Key Insight

This source is heavily focused on **AI control** - how to constrain agent behavior even if we can't verify alignment. Most proposals fit under existing entries:
- `contain-unsafe-ai` for containment/control
- `verify-ai-alignment` for monitoring/evaluation
- `defend-against-ai-harms` for defending systems from agents

The main gap is **agent-specific infrastructure** (SBOM, architecture standards) which could be a new intervention under contain-unsafe-ai.

## Summary

~40 proposals, most map to existing entries. Agent ecosystem security is primarily an elaboration of AI containment and control, not a separate problem domain.
