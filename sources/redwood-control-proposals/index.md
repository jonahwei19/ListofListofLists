# Redwood Research Control Project Proposals

**Source**: https://www.alignmentforum.org/posts/RRxhzshdpneyTzKfq/recent-redwood-research-project-proposals
**Original**: https://www.alignmentforum.org/posts/RRxhzshdpneyTzKfq/recent-redwood-research-project-proposals
**Also**: https://blog.redwoodresearch.org/p/7-tractable-directions-in-ai-control
**Date processed**: 2026-01-11
**Total items**: 36 project proposals across 5 categories; 10 tractable directions

## Overview

Redwood Research project proposals spanning AI control, alignment science, interpretability, RL safety, and security. Organized into 5 main categories:
1. Control projects (untrusted monitoring, collusion, honeypotting)
2. Training-time alignment methods
3. Better understanding and interpretability
4. Elicitation, sandbagging, diffuse threats
5. Other (benchmarks, security)

Also includes "7+ Tractable Directions" post with higher-priority research areas.

## Mapping to Entries

### [[contain-unsafe-ai]] (problem)

| Proposal | Notes |
|----------|-------|
| Control Protocol Transfer Across Settings | Do control results transfer between settings? |
| Studying Collusion | How policy/monitor models coordinate deception |
| Monitor Decoupling | Reduce correlation between monitors to prevent collusion |
| Untrusted Monitoring Deep Dive | Comprehensive analysis of untrusted monitoring dynamics |
| Malign AI Agent Substitution | Test real-world agent substitution attacks |
| Preventing Covert Malicious Fine-tuning | Detect stealthy misalignment injection |
| Few-shot Catastrophe Prevention | Safety techniques when misaligned behavior detected |

### [[multi-agent-threat-monitoring]]

| Proposal | Notes |
|----------|-------|
| Monitor Agent | Monitors that take actions, not just score trajectories |
| Building Trusted Monitors | Framework for reliable monitoring systems |
| Debate Protocol | Debate methodology to improve detection |
| Generating Indistinguishable Synthetic Inputs | Synthetic data for honeypotting untrusted monitors |
| Teaching Models Synthetic Facts | ~40k synthetic docs can instill false beliefs for honeypots |
| Studying Collusion Countermeasures | How instances coordinate without explicit communication |
| Steganography Countermeasures | Detect hidden information encoding for collusion |

### [[detect-evaluation-sandbagging]]

| Proposal | Notes |
|----------|-------|
| Better Password-locking Experiments | Model organism for studying capability hiding |
| How to Do Elicitation Without Learning | Extract capabilities without teaching better performance |
| Further Studying Exploration Hacking | How models sandbag despite training against it |
| Few-shot Catastrophe Detection with Linear Probes | Rapid catastrophe detection from limited examples |

### [[hardened-runtime-containment]]

| Proposal | Notes |
|----------|-------|
| Low-stakes environments | Multiple bad actions needed before real harm |
| Training Attack Policies | RL to develop better red-team strategies |
| Backdoor Auditing with Humans | Human-based auditing for suspicious actions |

### [[agent-trace-analysis]]

| Proposal | Notes |
|----------|-------|
| Consistency Lenses | Extract readable text from residual streams |
| Extraction Probes | Weak models extract subversion strategies from activations |
| Decoding Opaque Reasoning | Understand hidden reasoning processes |

### Not Mapped (alignment research, not resilience)

| Proposal | Why excluded |
|----------|--------------|
| Preventing Alignment Drift with "Ridges and Tripwires" | Alignment theory |
| Safe Distillation | Training method |
| Does Training Against Misalignment Remove It | Alignment theory |
| Reward hacking generalization studies | Foundational RL research |
| Imitative Generalization | Architecture design |
| Alignment Faking Extensions | Deceptive alignment research |

## Key Tractable Directions (from 7+ post)

1. **Elicitation Without Learning** - Measure capabilities without teaching improvement
2. **Generating Indistinguishable Synthetic Inputs** - For honeypotting monitors
3. **Teaching Models Synthetic Facts** - ~40k docs instill beliefs for honeypots
4. **Studying Exploration Hacking** - Sandbagging despite training
5. **Malign AI Agent Substitution** - Real-world substitution attacks
6. **Studying Data Poisoning** - Scheming AIs poison successor training
7. **Training Attack Policies** - RL for better red-team attacks
8. **Few-Shot Catastrophe Prevention** - Safety with minimal observed failures
9. **Studying Collusion Countermeasures** - Untrusted model coordination
10. **Steganography Countermeasures** - Hidden information encoding

## New Interventions Worth Considering

### Synthetic Honeypot Generation
**Mechanism**: Generate synthetic inputs/states that AI systems cannot distinguish from real data, for honeypotting monitors and detecting scheming.
**Maps to**: [[multi-agent-threat-monitoring]] (sub-intervention)
**Status**: Active research at Redwood. ~40k synthetic documents shown effective.

### Collusion Prevention Protocols
**Mechanism**: Technical countermeasures preventing untrusted model instances from coordinating deception (steganography detection, monitor decorrelation, input perturbation).
**Maps to**: [[multi-agent-threat-monitoring]] (sub-intervention)
**Status**: Early research. Key questions: What are optimal collusion strategies? How reliable must collusion be?

### Elicitation Without Learning
**Mechanism**: Techniques to measure model capabilities without permanently modifying them or teaching better performance.
**Maps to**: [[detect-evaluation-sandbagging]] (sub-intervention)
**Status**: Active research. Using password-locked models as test cases.

## Summary

36 proposals, 10 tractable directions. Strong mapping to existing entries, especially [[contain-unsafe-ai]] and [[multi-agent-threat-monitoring]]. Redwood's control research is the leading source for technical control interventions. Three potential sub-interventions identified: synthetic honeypots, collusion prevention, elicitation without learning. No new top-level problems - all fit under existing problem structure.
