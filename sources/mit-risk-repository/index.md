# MIT AI Risk Repository

**Source**: https://airisk.mit.edu/
**Date processed**: 2026-01-11
**Type**: Taxonomy stress-test (not bulk import)
**Total items**: 2244 risk entries, 7 domains, 23 sub-domains

## Overview

Systematic evidence review of AI risks. Uses two taxonomies:
- **Causal**: Entity (AI/Human) × Intent (Intentional/Unintentional) × Timing (Pre/Post deployment)
- **Domain**: 7 categories with 23 sub-categories

Noted as "unwieldy, vague and useless" for bulk import. Used here to stress-test our taxonomy for gaps.

## Domain Taxonomy Mapping

### 1. Discrimination & Toxicity
- 1.1 Unfair discrimination and misrepresentation
- 1.2 Exposure to toxic content
- 1.3 Unequal performance across groups

**Coverage**: OUT OF SCOPE. Not mass casualty/civilizational risk. Important but not existential.

### 2. Privacy & Security
- 2.1 Privacy compromise
- 2.2 System security vulnerabilities

**Coverage**: Partially in [[defend-against-ai-harms]] (cyber section), [[secure-frontier-data-centers]], [[model-weight-security]]

### 3. Misinformation
- 3.1 False or misleading information
- 3.2 Filter bubbles, loss of shared reality

**Coverage**: [[defend-against-ai-harms]] (misuse at scale), [[content-provenance-verification]], [[crowdsourced-verification]]

### 4. Malicious Actors
- 4.1 Disinformation, surveillance at scale
- 4.2 Cyberattacks, weapons (CBRNE), mass harm
- 4.3 Fraud, scams, manipulation

**Coverage**: [[defend-against-ai-harms]] (all bottlenecks)

### 5. Human-Computer Interaction
- 5.1 Overreliance and unsafe use
- 5.2 Loss of human agency and autonomy

**Coverage**:
- 5.1: Not covered explicitly. Individual overreliance is out of scope (not mass casualty).
- 5.2: [[prevent-ai-power-concentration]] covers systemic loss of autonomy.

### 6. Socioeconomic & Environmental
- 6.1 Power centralization → [[prevent-ai-power-concentration]]
- 6.2 Employment inequality → OUT OF SCOPE (economic, not existential)
- 6.3 Cultural devaluation → OUT OF SCOPE
- 6.4 Competitive dynamics (racing) → [[responsible-scaling-commitments]]
- 6.5 Governance failure → Meta/process, no dedicated entry
- 6.6 Environmental harm → OUT OF SCOPE

### 7. AI System Safety
- 7.1 Goal conflict (misalignment) → [[make-ai-aligned]]
- 7.2 Dangerous capabilities → [[verify-ai-alignment]], [[contain-unsafe-ai]]
- 7.3 Lack of robustness → [[verify-ai-alignment]], [[safety-benchmark-development]]
- 7.4 Lack of transparency → [[extract-insight-from-model-internals]]
- 7.5 AI welfare → OUT OF SCOPE (ethics)
- 7.6 Multi-agent risks → Partially: [[multi-agent-threat-monitoring]]

## Gap Analysis

### Confirmed covered
- AI takeover scenarios (make, verify, contain)
- Misuse for bio/cyber/mass harm (defend)
- Power concentration (prevent-ai-power-concentration)
- Racing dynamics (responsible-scaling-commitments)

### Potential gaps identified

| MIT Category | Gap | Assessment |
|--------------|-----|------------|
| 7.6 Multi-agent risks | Cascading failures, selection pressures, collusion | Partially covered, could enrich |
| 6.5 Governance failure | Mechanisms can't keep pace | Meta/process, likely out of scope |
| 5.1 Overreliance | Individuals over-trusting AI | Not mass casualty, out of scope |

### Not covered by MIT but in our taxonomy
- **Hyperwar** (Entente): AI-AI conflict leading to extinction. MIT mentions multi-agent risks but not explicitly this scenario.
- **Apocalyptic terrorism** as distinct from general misuse

## Comparison to Entente Framework

| Entente Threat | MIT Coverage | Our Coverage |
|----------------|--------------|--------------|
| AI Takeover | 7.1, 7.2, 7.3 | make, verify, contain |
| Dystopia | 6.1, 5.2 | prevent-ai-power-concentration |
| Hyperwar | 7.6 (partial) | Not explicit |
| Apocalyptic terrorism | 4.2 | defend-against-ai-harms |

## Conclusion

MIT taxonomy confirms coverage of major risk categories. No critical gaps identified for mass-casualty/civilizational risks. Minor enrichment possible for multi-agent dynamics. Hyperwar (AI-AI catastrophic conflict) might warrant consideration but is speculative.

**Recommendation**: Mark as processed. No new problem entries needed. Consider enriching multi-agent sections in future pass.
