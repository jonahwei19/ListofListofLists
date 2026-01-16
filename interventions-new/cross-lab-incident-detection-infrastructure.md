# Cross-lab incident detection infrastructure

**Tag**: Security

## What it is
Shared infrastructure allowing AI labs to log, anonymize, and analyze AI misbehavior across organizations.

**Mechanism**:
- Labs submit incident data to shared system (anonymized to protect user privacy and IP)
- Infrastructure enables pattern detection across multiple labs' deployments
- Third-party researchers can query aggregated data to identify emerging risks
- Labs collaborate directly without requiring trusted intermediary
- Builds on systems like Anthropic's CLIO (internal incident detection)
- Cross-references reveal whether incidents are isolated or systemic

**Why shared vs internal-only**: Individual labs see only their own incidents. Shared infrastructure reveals whether problems are lab-specific or industry-wide.

## Why it matters
- Patterns visible across labs invisible within single organization
- Without sharing, each lab discovers problems in isolation
- Identifies whether safety issues are one-off or systemic
- Creates collective intelligence about AI risks

## Current state
- **Status**: Research/Pilot
- **Existing systems**: Anthropic's CLIO (internal)
- **Bottlenecks**: Competitive concerns about sharing incident data; IP protection; anonymization standards; agreeing on common formats

## Who's working on it
- **Anthropic**: CLIO system for internal incident detection (potential model for cross-lab version)

## Sources
- [Peregrine 2025 #80: Comprehensive Incident Detection System](../sources/peregrine-2025/interventions/peregrine-080.md)
