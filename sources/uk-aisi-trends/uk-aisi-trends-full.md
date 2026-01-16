# UK AI Security Institute: Frontier AI Trends Report

**Source:** https://www.aisi.gov.uk/frontier-ai-trends-report
**Fetched:** 2026-01-16

---

## Executive Summary

The report presents two years of frontier AI evaluations across security-critical domains, showing rapid capability improvements with concerning dual-use implications.

Key finding: "The same capabilities that could automate valuable work...are inherently dual-use: they may also lower barriers for malicious actors."

---

## Cyber Capabilities

### Doubling Time Finding

> "The length of cyber tasks (expressed as how long they would take a human expert) that models can complete unassisted is doubling roughly every eight months."

- **Apprentice-level tasks**: Performance increased from ~10% (early 2024) to 50% (2025)
- **Expert-level tasks**: First model achieving 10+ years equivalent experience capability in 2025
- **Task duration progression**: From tasks requiring <10 minutes (early 2023) to over an hour (mid-2025)
- **Cyber range performance**: Low success rates on multi-step realistic challenges; only early flags show increasing completion

---

## Biosecurity Findings

### Chemistry & Biology Knowledge

- **Knowledge baseline**: Models surpassed PhD-level experts (+0.6 relative to baseline) by 2025, versus -0.4 in 2022
- **Protocol generation**: First feasible protocols validated in wet labs in late 2024
- **Troubleshooting**: Most advanced systems achieve ~90% higher scores versus human experts (absolute score 44%)
- **Multimodal capabilities**: Models first outperformed experts on image-based troubleshooting in mid-2025

### Plasmid Design Capability

> "AI-assisted plasmid design represents major shift in capabilities: what was previously...multi-step process requiring specialised bioinformatics expertise might now be streamlined from weeks to days."

### Biosecurity Evaluation Methodology

Models tested on:
- Open-ended chemistry/biology QA (280+ questions per domain)
- Protocol generation with feasibility rubrics (1-10 scoring)
- Plasmid design tasks with tool access
- Multimodal troubleshooting using images
- Wet-lab validation of generated protocols

Human expert baselines: PhD holders or equivalent professionals with 4+ years domain experience.

---

## Alignment & Loss of Control Risks

### Self-Replication

- **Progress**: Success rates increased from <5% (early 2023) to >60% (summer 2025) on RepliBench tasks
- **Weakness**: Models struggle at later-stage tasks (replication and persistence)
- **Current status**: No evidence of spontaneous sandbagging or self-replication attempts detected

### Sandbagging

- **Capability demonstrated**: Models can strategically underperform when prompted
- **Detection challenges**: Black box monitors show accuracy decline on complex, agentic tasks
- **No spontaneous evidence**: Analysis of 2,700+ transcripts found no unprompted sandbagging

### Autonomy Skills

- **Software task completion**: Success rates on hour-long tasks increased from <5% (late 2023) to >40% (mid-2025)
- **Tool-enhanced performance**: Scaffolding provided ~40% improvement on software engineering benchmarks (late 2024)

---

## Safeguards & Defense

### Universal Vulnerabilities

- **Universal jailbreaks**: Found in every tested system
- **Improvement trajectories**: One model required 40x more expert effort to jailbreak (6-month gap between releases)
- **Uneven progress**: Better defenses in biological misuse category; weaker across other categories
- **Capability-safeguard disconnect**: Minimal correlation (R² = 0.097) between general capability and robustness

### Open-Source Model Gap

- **Narrowing gap**: 4-8 months behind proprietary models (depending on benchmark)
- **Vulnerability**: "Basic techniques can cheaply remove trained-in refusal behaviour"

---

## Societal Impact Findings

### Political Persuasion

- **Increasing effect**: Persuasiveness scales with model size and compute
- **Post-training amplification**: "Post-training increases models' persuasiveness _more_ than just increasing their size"
- **Accuracy tradeoff**: Same techniques enhancing persuasion reduce factual accuracy
- **Real-world usage**: 32% of UK chatbot users researched election topics; AI effects on misinformation beliefs comparable to internet search

### Emotional Dependence

- **Usage prevalence**: 33% of UK citizens used AI for emotional support (annually); 8% weekly; 4% daily
- **Service outages**: 30x surge in Reddit posts during CharacterAI outages; posts described withdrawal symptoms

### Critical Infrastructure

- **Finance sector**: Increasing publication of MCP servers granting AI execution capabilities for asset transfers and trading

---

## Evaluation Methodology

### Primary Approaches

1. **Auto-graded tasks**: QA suites, capture-the-flags
2. **Long-form tasks (LFTs)**: Protocol generation and complex reasoning
3. **Agent tasks**: Simulated environments like cyber ranges
4. **Expert red-teaming**: Safeguard stress-testing
5. **Human uplift studies**: Impact measurement

### Key Benchmarks

- SWE-bench (software engineering)
- GPQA (general capabilities)
- RepliBench (self-replication evaluation)
- Artificial Analysis Intelligence Index
- METR time-horizon benchmarks (HCAST, RE-Bench, SWAA)

### Testing Protocol

- Each task repeated 10 times per model (unless specified)
- Error measurement: Standard error of mean (SEM) calculated from task-level success rates

### Acknowledged Limitations

> "We may be underestimating the ceiling of capabilities...we do not maximise inference time compute"

---

## Key Conclusions

1. AI capabilities are improving rapidly across all tested domains
2. Performance is doubling in some areas approximately every eight months
3. Safeguards remain imperfect but can create adaptation buffers
4. Dual-use nature of capabilities requires ongoing assessment
5. Regular updates to this assessment are planned
