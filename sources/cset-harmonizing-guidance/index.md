# CSET Georgetown: Harmonizing AI Guidance

**Source**: Center for Security and Emerging Technology (CSET), Georgetown University
**Published**: September 2025
**Authors**: Kyle Crichton, Abhiram Reddy, Jessica Ji, Ali Crawford, Mia Hoffmann, Colin Shea-Blymyer, John Bansemer
**URL**: https://cset.georgetown.edu/publication/harmonizing-ai-guidance-distilling-voluntary-standards-and-best-practices-into-a-unified-framework/

## Overview

This report distills 7,741 recommendations from 52 different guidance documents into 258 harmonized recommendations. These are organized into 5 overarching categories and 34 topic areas.

## The 5 Categories

1. **Governance** (63 recommendations): Defining and implementing organizational strategy for managing technology and associated risks
   - Topics: Strategy & Leadership, Management, Risk Management, IT Management, Supply Chain, Workforce & Training, Inventory, Audit & Compliance

2. **Safety** (58 recommendations): Responsibly developing and evaluating technology, assessing societal impact, engaging stakeholders
   - Topics: Responsible Business Conduct, Stakeholders, Societal Impact, Impact & Trust, Fairness & Synthetic Content, Test & Evaluation, Performance Monitoring, Traceability, Transparency & Oversight, Model Safeguards

3. **Security** (84 recommendations): Developing secure systems, managing access, implementing security controls
   - Topics: Security Management, Design & Development, Vulnerabilities, Identity & Authentication, Access Control, Network Security, Information Security, Endpoint Security, Personnel & Media Security, Physical Security

4. **Privacy** (20 recommendations): Managing data (especially PII) and protecting confidentiality throughout data lifecycle
   - Topics: Privacy Program, Handling PII

5. **Detection & Response** (33 recommendations): Identifying threats/incidents, responding, building operational continuity
   - Topics: Audit Logging, Monitoring, Incident Response, Resilience & Recovery

## Key Findings: Where AI Guidance Focuses

The report identifies 5 areas where existing AI guidance concentrates:

1. **Expanded risks and impacts**: Emphasis on broader set of risks from AI systems, including societal impacts, CBRN concerns, and potential existential risks

2. **New vulnerabilities**: AI introduces novel attack vectors (model theft, data poisoning, adversarial inputs, jailbreaking, membership inference)

3. **Need for transparency**: Difficulty anticipating AI outputs; black-box nature of advanced models; need for explainability

4. **Greater testing and evaluation**: Heavy emphasis on pre-deployment testing and continuous post-deployment monitoring, including AI red-teaming

5. **Synthetic content**: Managing risks from AI-generated text, images, audio, video; detecting bias; watermarking

## Identified Gaps in AI Guidance

The report identifies areas lacking adequate guidance:

1. **Workforce**: No guidance on internal workforce displacement, upskilling, or AI awareness training
2. **Incident reporting**: Unclear mechanisms for AI-specific incidents that don't fit existing buckets
3. **Confidential information**: No guidance on managing data leakage through chatbots/AI tools
4. **Agentic AI**: Almost no guidance for AI agents that plan and take action in the real world

## Source Documents

The 52 reports analyzed include:
- 29 AI-specific guidance documents
- 23 non-AI reports covering cybersecurity, privacy, and risk management

Key sources include: NIST AI RMF, NIST CSF, ISO 42001, ISO 27001, OWASP ML Top 10, OWASP LLM Top 10, UK NCSC AI guidance, Google SAIF, DHS AI Framework, and many others.

## Files

- `cset-harmonizing-guidance-full.md` - Full extracted text of the report

## Proposal Mappings

Proposal files in `proposals/` map CSET practices to existing interventions:

| Proposal File | Mapped Interventions |
|--------------|---------------------|
| `test-evaluation-practices.md` | safety-benchmarks, evaluation-companies, cbrn-misuse-evaluations, sandbagging-detection |
| `model-safeguards-practices.md` | classified-red-teaming, defense-in-depth-closed-models, training-data-anti-poisoning, capability-unlearning |
| `incident-response-practices.md` | ai-incident-reporting, cross-org-incident-detection, cross-border-ai-incident-notification |
| `performance-monitoring-practices.md` | model-drift-monitoring, usage-incident-monitoring, agent-trace-analysis |
| `transparency-oversight-practices.md` | public-model-audits, rsp-implementation, whistleblower-protection-fund, human-ai-cooperative-evals |
| `governance-practices.md` | intergovernmental-frontier-model-forum, government-ai-expertise-centers, government-risk-framework-expansion, ai-policy-studio |
| `security-management-practices.md` | private-industry-security, subsidized-security-tools, ai-security-expert-training, confidential-computing |
| `workforce-training-practices.md` | ai-evaluator-training, ai-security-expert-training, regulatory-talent-placement |
| `agentic-ai-gap.md` | agent-ids-reputation, multi-agent-safety-protocols, agent-trace-analysis |
| `supply-chain-practices.md` | compute-supply-chain-coordination, global-hardware-verification, training-data-licensing, training-data-attribution |
| `resilience-recovery-practices.md` | ai-catastrophe-backup-plans, attack-scenario-wargaming, loss-of-control-threat-modeling |

## Key Insights for Interventions

### Strongly Validated by CSET (High AI Scores, 70-100%)
- Test & Evaluation practices (TE-3, TE-8: 95-100%)
- Model Safeguards (SG-1 through SG-6: all 100%)
- Transparency & Oversight (TO-1 through TO-7: 96-100%)
- Performance Monitoring for drift (PM-2: 79%)

### Identified as Gaps (Low AI Scores or Explicit Mentions)
- Incident Reporting (explicitly identified as gap)
- Agentic AI (explicitly identified as gap)
- Workforce/Training (explicitly identified as gap)
- Resilience & Recovery (5-24% AI Scores)
- Security Management (0% AI Scores for core practices)

### Imbalance Finding
The report notes a significant imbalance between AI safety guidance (well-developed) and AI security guidance (underrepresented), validating interventions focused on AI security infrastructure.
