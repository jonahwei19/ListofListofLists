# Peregrine 2025 → Entry Mapping

**Source**: [The 2025 Peregrine Report](https://riskmitigation.ai/wp-content/uploads/The-2025-Peregrine-Report.pdf)
**Processed**: 2026-01-10
**Total proposals**: 208

**Structure**: 208 source proposals → 4 problem entries + intervention pages

---

## Problem Entry Mapping

| Entry | Description | Key Proposals |
|-------|-------------|---------------|
| [[verify-ai-alignment]] | Know if AI systems are aligned | #2-5, #24-27, #38-48, #50-56 |
| [[make-ai-aligned]] | Train aligned AI systems | #1, #6-18 |
| [[contain-unsafe-ai]] | Prevent harm if we can't verify/align | #19-23, #57-64, #65-86, #159-163 |
| [[defend-against-ai-harms]] | Mitigate AI-enabled bio/cyber/misuse | #49-53, #134-158, #164-175 |

---

## Domain 1: Technical AI Alignment (#1-41)

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 1 | Training Data Attribution | [[make-ai-aligned]], [[defend-against-ai-harms]] | [[interventions/shape-training-data-for-alignment]] |
| 2 | Agent Trace Analysis | [[contain-unsafe-ai]] | [[interventions/agent-trace-analysis]] |
| 3 | Task Decomposition | [[contain-unsafe-ai]] | [[interventions/multi-user-task-decomposition]] |
| 4 | Defense-in-Depth Analysis | [[verify-ai-alignment]] | [[interventions/defense-in-depth-analysis]] |
| 5 | Chain-of-Thought Fidelity | [[verify-ai-alignment]] | [[interventions/verify-chain-of-thought-fidelity]] |
| 6 | Human Labeling Service | [[make-ai-aligned]] | [[interventions/high-quality-preference-data]] |
| 7 | Tamper-Resistant RLHF | [[make-ai-aligned]] | [[interventions/tamper-resistant-training]] |
| 8 | Probabilistic Programming | [[make-ai-aligned]] | [[interventions/probabilistic-programming-approaches]] |
| 9 | Safety by Design - Formal | [[make-ai-aligned]] | [[interventions/safety-by-design-architectures]] |
| 10 | Safety by Design - Scientist AI | [[make-ai-aligned]] | [[interventions/non-agentic-question-answering]] |
| 11 | Theoretical Alignment Research | [[make-ai-aligned]] | [[interventions/theoretical-alignment-foundations]] |
| 12 | Cooperative Alignment | [[make-ai-aligned]] | [[interventions/cooperative-alignment]] |
| 13 | Debate Theory | [[verify-ai-alignment]] | [[interventions/scalable-human-oversight]] |
| 14 | Constitutional AI | [[make-ai-aligned]] | [[interventions/fine-tune-on-explicit-principles]] |
| 15 | Pluralistic Alignment | [[make-ai-aligned]] | [[interventions/pluralistic-alignment-frameworks]] |
| 16 | Complex Objective Functions | VAGUE | See vague/log.md |
| 17 | Automated Science - Hunch Agents | [[make-ai-aligned]] | [[interventions/ai-for-alignment-research]] |
| 18 | AI for AI Safety Research | [[make-ai-aligned]] | [[interventions/ai-for-alignment-research]] |
| 19 | Unlearning Capabilities | [[contain-unsafe-ai]] | [[interventions/capability-unlearning]] |
| 20 | Low-Stakes Settings | [[contain-unsafe-ai]] | [[interventions/hardened-runtime-containment]] |
| 21 | AI Control Systems | [[contain-unsafe-ai]] | [[interventions/hardened-runtime-containment]] |
| 22 | Control as a Service | [[contain-unsafe-ai]] | [[interventions/hardened-runtime-containment]] |
| 23 | Loss of Control Prevention | [[contain-unsafe-ai]] | [[interventions/loss-of-control-prevention]] |
| 24 | Limits of Model Distillation | [[verify-ai-alignment]] | [[interventions/capability-diffusion-analysis]] |
| 25 | Misalignment Definitions | [[verify-ai-alignment]] | [[interventions/misalignment-definitions]] |
| 26 | Scalable Oversight | [[verify-ai-alignment]] | [[interventions/scalable-human-oversight]] |
| 27 | Loss of Control Threat Modeling | [[contain-unsafe-ai]] | [[interventions/loss-of-control-threat-modeling]] |
| 28-37 | Meta/Infrastructure | Research acceleration | Not problem-specific |
| 38-41 | Interpretability | [[verify-ai-alignment]], [[make-ai-aligned]] | [[interventions/extract-insight-from-model-internals]] |

---

## Domain 2: Evaluation & Auditing (#42-64)

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 42 | Interactive Inspection Tools | [[verify-ai-alignment]] | [[interventions/scalable-human-oversight]] |
| 43 | End-to-End Harm Assessment | [[verify-ai-alignment]] | [[interventions/end-to-end-harm-assessment]] |
| 44 | Evaluation Sandbagging Detection | [[verify-ai-alignment]] | [[interventions/detect-evaluation-sandbagging]] |
| 45 | Training AI Evaluators | [[verify-ai-alignment]] | [[interventions/training-ai-evaluators]] |
| 46 | Cooperative Evals | [[verify-ai-alignment]] | [[interventions/cooperative-evaluation-frameworks]] |
| 47 | Meta-Research on Safety | [[verify-ai-alignment]] | [[interventions/safety-technique-meta-research]] |
| 48 | Characterizing AI Risks | [[verify-ai-alignment]] | [[interventions/risk-characterization-frameworks]] |
| 49 | Vulnerability Matching | [[defend-against-ai-harms]] | [[interventions/vulnerability-matching]] |
| 50 | Safety Benchmark Development | [[verify-ai-alignment]] | [[interventions/safety-benchmark-development]] |
| 51 | Evaluation Framework Consensus | [[verify-ai-alignment]] | [[interventions/evaluation-framework-consensus]] |
| 52 | Risk-Model Evaluation | [[verify-ai-alignment]] | [[interventions/risk-model-evaluation]] |
| 53 | Classified Red Teaming | [[defend-against-ai-harms]] | [[interventions/classified-red-teaming]] |
| 54 | Capability Assessment Framework | [[verify-ai-alignment]] | [[interventions/capability-assessment-frameworks]] |
| 55 | Ultra-Reliable AI Evaluation | [[verify-ai-alignment]] | [[interventions/ultra-reliable-evaluation]] |
| 56 | Misuse Evaluations | [[defend-against-ai-harms]] | [[interventions/misuse-evaluation-frameworks]] |
| 57 | Multi-Agent Interaction Framework | [[contain-unsafe-ai]] | [[interventions/multi-agent-threat-monitoring]] |
| 58 | Evaluation Companies | [[verify-ai-alignment]] | [[interventions/evaluation-organizations]] |
| 59 | Public Audits | [[contain-unsafe-ai]] | [[interventions/public-model-audits]] |
| 60 | AI Auditing Institutions | [[contain-unsafe-ai]] | [[interventions/ai-auditing-institutions]] |
| 61 | Secure Frontier Data Centers | [[contain-unsafe-ai]] | [[interventions/secure-frontier-data-centers]] |
| 62 | Verified Kinetic Actuators | [[verify-ai-alignment]] | [[interventions/verified-actuator-systems]] |
| 63 | Speed Limits in Data Centers | [[contain-unsafe-ai]] | [[interventions/data-center-speed-limits]] |
| 64 | Physical Chokepoints | [[contain-unsafe-ai]] | [[interventions/physical-deployment-chokepoints]] |

---

## Domain 3: Intelligence Gathering (#65-86)

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 65 | AI OSINT | [[contain-unsafe-ai]] | [[interventions/ai-development-osint]] |
| 66 | AI Diffusion Research | [[contain-unsafe-ai]] | [[interventions/capability-diffusion-analysis]] |
| 67 | Usage and Incident Monitoring | [[contain-unsafe-ai]] | [[interventions/incident-reporting-systems]] |
| 68 | Global Hardware Verification | [[contain-unsafe-ai]] | [[interventions/global-hardware-verification]] |
| 69 | Industry Security | [[contain-unsafe-ai]] | [[interventions/industry-security-oversight]] |
| 70 | On-Chip Monitoring | [[contain-unsafe-ai]] | [[interventions/hardware-enabled-governance]] |
| 71 | Flexible Hardware Governance | [[contain-unsafe-ai]] | [[interventions/hardware-enabled-governance]] |
| 72 | Confidential Computing | [[contain-unsafe-ai]] | [[interventions/hardware-enabled-governance]] |
| 73 | Privacy-Preserving Verification | [[contain-unsafe-ai]] | [[interventions/international-treaty-verification]] |
| 74 | Hardware Kill Switches | [[contain-unsafe-ai]] | [[interventions/remote-compute-disable]] |
| 75 | AI for Collective Decision-making | Meta/societal | Not problem-specific |
| 76 | AI Forecasters | Meta/societal | Not problem-specific |
| 77 | Economic Impact Research | [[defend-against-ai-harms]] | [[interventions/societal-resilience-planning]] |
| 78 | Monitor Agent Interactions | [[contain-unsafe-ai]] | [[interventions/multi-agent-threat-monitoring]] |
| 79 | AI Drift Monitoring | [[contain-unsafe-ai]] | [[interventions/incident-reporting-systems]] |
| 80 | Incident Detection System | [[contain-unsafe-ai]] | [[interventions/incident-reporting-systems]] |
| 81 | AI Misuse Detection | [[contain-unsafe-ai]] | [[interventions/incident-reporting-systems]] |
| 82 | Control Loss Monitoring | [[contain-unsafe-ai]] | [[interventions/loss-of-control-monitoring]] |
| 83 | AI-Enhanced Monitoring | [[contain-unsafe-ai]] | [[interventions/ai-enhanced-monitoring]] |
| 84 | Intelligence Explosion Monitoring | [[contain-unsafe-ai]] | [[interventions/intelligence-explosion-tripwires]] |
| 85 | System-Level AI Effects | [[contain-unsafe-ai]] | [[interventions/multi-agent-threat-monitoring]] |
| 86 | Golden Period Framework | [[contain-unsafe-ai]] | [[interventions/capability-phase-monitoring]] |

---

## Domain 4: Governance & Policy (#87-114)

Governance is not a goal - mechanisms serve specific problems.

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 87 | Incident Reporting | [[contain-unsafe-ai]] | [[interventions/incident-reporting-systems]] |
| 88 | Agent IDs and Reputation | [[defend-against-ai-harms]] | [[interventions/agent-ids-and-reputation]] |
| 89 | Technical Governance Tools | [[contain-unsafe-ai]] | [[interventions/ai-attribution-tools]] |
| 90 | Human Verification Systems | [[defend-against-ai-harms]] | [[interventions/human-verification-systems]] |
| 91 | Compute Governance | [[contain-unsafe-ai]], [[verify-ai-alignment]] | [[interventions/training-compute-thresholds]] |
| 92 | Enhanced RSP Implementation | [[verify-ai-alignment]] | [[interventions/responsible-scaling-commitments]] |
| 93 | Barriers to Fine-tuning | [[contain-unsafe-ai]] | [[interventions/barriers-to-fine-tuning]] |
| 94-98 | Data/accountability frameworks | Contested ToC | Various interventions |
| 99-114 | Government capacity | Serve multiple problems | [[interventions/governance-capacity-building]] |

---

## Domain 5: International Coordination (#115-133)

Theory of change contested. Some actors won't cooperate regardless of coordination availability (Karnofsky). These are enforcement tools, not just coordination tools.

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 115-133 | International frameworks, diplomacy | [[contain-unsafe-ai]] | [[interventions/international-treaty-verification]] |
| 123 | Compute Supply Chain | [[contain-unsafe-ai]] | [[interventions/compute-supply-chain-coordination]] |

---

## Domain 6: Preparedness & Response (#134-175)

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 134-143 | Bio risk measures | [[defend-against-ai-harms]] | [[interventions/metagenomic-pathogen-surveillance]], [[interventions/broad-spectrum-countermeasures]] |
| 144-154 | Economic/societal resilience | [[defend-against-ai-harms]] | [[interventions/societal-resilience-planning]] |
| 155-158 | Crisis response | [[defend-against-ai-harms]] | [[interventions/attack-scenario-analysis]], [[interventions/backup-planning]] |
| 159-163 | AI lab security | [[contain-unsafe-ai]] | [[interventions/model-weight-security]], [[interventions/sl5-data-center-protocols]] |
| 164-175 | Cybersecurity | [[defend-against-ai-harms]] | [[interventions/formally-verified-software]], [[interventions/automated-vulnerability-patching]] |

---

## Domain 7: Public Communication (#176-187)

All meta/advocacy - not mapped to specific problem entries.

---

## Domain 8: Miscellaneous (#188-208)

| # | Source Title | Maps To | Intervention |
|---|--------------|---------|--------------|
| 188-189 | Legal/whistleblower | [[contain-unsafe-ai]] | [[interventions/incident-reporting-systems]] |
| 190 | Alignment tax | [[make-ai-aligned]] | [[interventions/alignment-incentive-mechanisms]] |
| 191 | Neuroscience moonshots | [[make-ai-aligned]] | [[interventions/alternative-ai-paradigms]] |
| 192 | Access standards | [[verify-ai-alignment]] | [[interventions/responsible-scaling-commitments]] |
| 193-202 | Game theory, cooperation | Various | Various interventions |
| 203-208 | Ethics, personhood, sentience | VAGUE | See vague/log.md |

---

## Vague Proposals

See [[vague/log.md]] for proposals that couldn't be mapped:
- #16 Complex Objective Functions
- #203 Ethics for AI Alignment
- #204 Legal Personhood Framework
- #205 AI Sentience Research
- #206 Psychological Interventions for AGI
- #207 Whole Brain Emulation
- #208 AI Alignment Researcher Wellbeing

---

## Summary

| Category | Count |
|----------|-------|
| [[verify-ai-alignment]] | ~35 |
| [[make-ai-aligned]] | ~18 |
| [[contain-unsafe-ai]] | ~45 |
| [[defend-against-ai-harms]] | ~55 |
| Meta/Infrastructure | ~35 |
| Vague | 8 |
| Multi-mapped (counted in multiple) | ~20 |

Note: Some proposals serve multiple problems and appear under multiple entries.
