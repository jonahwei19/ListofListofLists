# Weapons of mass destruction misuse evaluations

**Tag**: Security

## What it is
Standardized frameworks for red-teaming AI systems against realistic CBRN (Chemical, Biological, Radiological, Nuclear) misuse scenarios. Components include:

- **Structured evaluation protocols**: Multi-tiered attack methodologies testing models against prompts designed to elicit dangerous information (e.g., Enkrypt AI's 200-prompt CBRN dataset)
- **Risk scoring systems**: Red/Amber/Green prioritization frameworks for resource allocation (e.g., RAND-CLR Global Risk Index)
- **Third-party verification**: Independent evaluation by organizations without commercial incentives to underreport
- **Lifecycle testing**: Evaluation throughout model development, not just pre-deployment

## Why it matters
- **Trust deficit**: AI labs control both design and disclosure of dangerous capability evaluations, creating incentives to underreport alarming results
- **No correlation between risk and accessibility**: RAND found 61.5% of tools indexed as "Red" (highest risk) are fully open-sourced
- **Standardization gap**: Without common frameworks, labs test different scenarios with different rigor—vulnerabilities slip through
- **Policy dependency**: DHS CBRN Report (April 2024) and NTIA dual-use foundation model report (July 2024) both depend on robust evaluation data

## Current state
- **Status**: Research/Pilot
- **Recent developments (2025)**:
  - Enkrypt AI red team study tested 10 frontier models from Anthropic, OpenAI, Meta, Cohere, Mistral—found major safety gaps
  - RAND-CLR Global Risk Index assessed 57 AI-enabled biological tools: 13 "Red", 15 "Amber"
  - Apart Research launched CBRN × AI Risks Research Sprint for defensive solutions
  - RAND 2024 study found no statistically significant difference in biological attack plan viability with vs. without LLM access—but methodology debated
- **Bottlenecks**: Labs have incentive to underreport; no single organization owns responsibility; coordination failure

## Who's working on it
- **UK AI Security Institute (UK AISI)**: Third-party evaluations of frontier models
- **RAND Corporation**: Global Risk Index, biosecurity governance research, expert convenings
- **Centre for Long-Term Resilience**: Co-developed Global Risk Index with RAND Europe
- **Enkrypt AI**: CBRN red teaming studies
- **SecureBio**: Independent biosecurity evaluations
- **METR**: Responsible Scaling Policy components, biorisk evaluation methodology
- **Apollo Research**: AI governance research including internal deployment risks
- **Apart Research**: CBRN × AI research sprints

## Sources
- [Peregrine 2025 #56: Misuse Evaluations](../sources/peregrine-2025/interventions/peregrine-056.md)
