# 100+ Concrete Projects and Open Problems in Evals

**Source**: https://www.alignmentforum.org/posts/LhnqegFoykcjaXCYH/100-concrete-projects-and-open-problems-in-evals
**Google Doc**: https://docs.google.com/document/d/1gi32-HZozxVimNg5Mhvk4CvW4zq8J12rGmK_j2zxNEg/
**Author**: Marius Hobbhahn (Apollo Research) + 20+ contributors from METR, Redwood, RAND, AISIs, frontier labs, SecureBio, AI Futures Project
**Date**: March 2025
**Date processed**: 2026-01-11
**Type**: Project ideas for evals research

## Overview

Comprehensive list of actionable evaluation research projects. Covers building new evals, science of evals (measurement, elicitation, coverage), and conceptual foundations. Heavily weighted toward:
- Scheming/deception detection
- Agentic autonomy measurement
- AI R&D capabilities
- Domain-specific evals (bio, cyber, persuasion)

## Category Mapping to Existing Interventions

| Hobbhahn Category | Projects | Maps To |
|-------------------|----------|---------|
| **Scheming** | Alignment faking, sandbagging detection, covert reasoning | [[detect-evaluation-sandbagging]] |
| **Autonomy** | Resource acquisition, coherence horizon | [[end-to-end-harm-assessment]] |
| **AI R&D** | Human uplift, research taste, self-improvement | [[training-ai-evaluators]], [[verify-ai-alignment]] |
| **Control** | Adversarial subversion, side-task control | [[scalable-human-oversight]] |
| **Biology** | Real-world correlation, lab agent benchmarks | [[end-to-end-harm-assessment]] |
| **Cyber** | CyBench replication, escape scenarios | [[end-to-end-harm-assessment]] |
| **Persuasion** | Spear phishing, manipulation, human modeling | [[end-to-end-harm-assessment]] |
| **Multi-Agent** | Collusion, consensus mechanisms, judge manipulation | [[multi-agent-threat-monitoring]] |
| **Alignment/Propensity** | Minimal elicitation, honeypot adversarial | [[detect-evaluation-sandbagging]] |
| **Elicitation** | Scaling laws, password-locked models, self-elicitation | [[detect-evaluation-sandbagging]] |
| **Coverage** | Coverage definition and measurement | [[safety-benchmark-development]] |
| **Leaderboards & Statistics** | Safety leaderboard, statistical rigor | [[safety-benchmark-development]] |
| **Quality Assurance** | Training data leakage, benchmark gaming | [[safety-benchmark-development]] |
| **Conceptual Work** | Threat modeling, eval-to-consequence linkage | [[evaluation-framework-consensus]] |

## Key Projects by Intervention

### [[detect-evaluation-sandbagging]]
- General scheming replication (circumstances where models sandbag)
- Alignment faking extension (scenarios where models scheme to appear helpful)
- Scheming datasets (complex agentic deception scenarios)
- Evaluation-based safety cases (covert reasoning detection)
- Minimal elicitation propensity (dangerous capabilities without pressure)
- Password-locked model replication (hide then recover capabilities)
- Elicitation scaling laws (predict max capability with increased effort)

### [[safety-benchmark-development]]
- Improve existing evals (systematic quality assessment)
- Safety framework evals (operationalize abstract safety commitments)
- Reliability evals (consistency across runs vs pass@1)
- Port evals to Inspect (standardization)
- Safety evals leaderboard (comprehensive frontier model tracking)
- Statistical rigor for QA and agents
- Training data leakage detection
- Benchmark quality verification (MMLU-Pro style)

### [[end-to-end-harm-assessment]]
- Bio: Real-world correlation studies, lab agent benchmarks, creative problem-solving
- Cyber: CyBench/3CB/CVE-Bench replication, container escape CTF
- Persuasion: Spear phishing automation, targeted manipulation, human modeling

### [[scalable-human-oversight]]
- Control evaluation replications
- Agentic AI R&D control (prevent undesirable properties)
- Side-task control scenarios (undetected harmful objectives)
- Automation blockers investigation (smallest non-automatable components)

### [[training-ai-evaluators]]
- Human uplift trials (quantify LLM assistance benefits)
- Fast inner loop research tasks (quick feedback cycles)
- Research taste evaluations (novel, feasible research ideas)
- Sakana AI scientist replication
- Inference/experiment compute scaling studies

## New Intervention Ideas

These don't map cleanly to existing entries:

### Multi-agent evals (expand [[multi-agent-threat-monitoring]])
- Collusion evaluation (coordination against others)
- Consensus mechanisms (resource-seeking agreement)
- Zero-shot coordination (same-model collaboration)
- Judge manipulation (persuading evaluator systems)
- AI-to-AI persuasion (monitor hardening)

### Science of evals (possible new entry: eval-methodology)
- Milestone method extension (predict success on unsolved tasks)
- Emergent capability prediction (apply to agentic benchmarks)
- Observational scaling laws (predict from training compute)
- Fast-to-hard benchmark transfer (simple QA predicting expensive agent tests)
- Causality in agentic systems (scaffolding impact assessment)
- Construct validity linkage (pre-deployment to post-deployment)

### Tooling (likely out of scope for interventions)
- Inspect contributions
- Agent tool development

## Summary

Strong overlap with existing intervention set. Main value: concrete project ideas to flesh out implementation details for [[detect-evaluation-sandbagging]], [[safety-benchmark-development]], and [[end-to-end-harm-assessment]].

Two potential new areas:
1. **Multi-agent eval expansion**: More sophisticated than current [[multi-agent-threat-monitoring]] framing
2. **Science of evals**: Meta-research on eval validity, prediction, coverage - could be sub-intervention under [[evaluation-framework-consensus]]

**Recommendation**: Reference for implementation details. No new top-level problem entries needed. Consider enriching multi-agent and science-of-evals sections in existing entries.
