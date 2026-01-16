# Real-world AI usage analysis

**Tag**: Security

## What it is
Systematic analysis of how AI systems are actually used in deployment, replacing theoretical threat-modeling with data-driven insights.

**Mechanism**:
- Labs instrument deployments to capture usage patterns (without logging content)
- Analysis identifies: unexpected use cases, emerging misuse patterns, capability discovery by users
- Data reveals which theoretical risks actually manifest and which don't
- Enables prioritization of safety work based on real attack surface
- Requires legal and privacy frameworks that enable analysis without liability

**Why labs currently avoid this**: Legal liability concerns if they discover misuse. Privacy regulations make usage analysis risky. Creates significant blind spots.

## Why it matters
- Theoretical threat models may miss actual attack vectors
- Real usage patterns reveal gaps between intended and actual use
- Identifies emerging misuse before it becomes widespread
- Enables evidence-based safety prioritization

## Current state
- **Status**: Gap (mostly avoided due to liability)
- **Bottlenecks**: Legal liability if misuse discovered; privacy regulations (GDPR, etc.); user consent issues; infrastructure for privacy-preserving analysis

## Who's working on it
- **No dedicated organization identified** (gap area—legal/policy work needed to enable)

## Sources
- [Peregrine 2025 #67: Usage and Incident Monitoring Systems](../sources/peregrine-2025/interventions/peregrine-067.md)
