# Licensed access tiers for biology-capable AI

**Tag**: Security

## What it is
Tiered access system where full-capability AI models for biology are restricted to licensed institutions. General users get models with dangerous biological knowledge filtered or gated.

**Mechanism**:
- Training: Models exclude or downweight dangerous biological information (synthesis routes for pathogens, enhancement techniques)
- Inference: Query filters flag biology-related red flags before reaching the model
- Access tiers: Public (filtered), Institutional (KYC-verified labs/universities), Government (full capability)
- Audit: Usage logging for institutional/government tiers

**What this doesn't solve**: Open-weight models already in circulation; knowledge reconstructible from multiple filtered queries; determined actors can train their own models.

## Why it matters
- AI models trained on biological literature could provide step-by-step pathogen creation instructions
- Tiered access creates friction without blocking legitimate research
- KYC for biology queries creates accountability

## Current state
- **Status**: Partial deployment
- **Implementations**:
  - Most frontier models have biology-related refusals
  - No standardized licensing or tiering system across providers
- **Bottlenecks**: Open-weight models bypass; international coordination; defining "dangerous" biological knowledge

## Who's working on it
- **Frontier AI labs**: Voluntary refusal training (varies by lab)
- **No standardized licensing body exists**

## Sources
- [Peregrine 2025 #139: Biosecurity Controls](../sources/peregrine-2025/interventions/peregrine-139.md)
