# Epistemic Security (early thinking)

**Source**: Local markdown file - tiling tree from Jonah
**Date processed**: 2026-01-11
**Status**: Dissolved - interventions redistributed

## What went wrong

The source was an **intervention taxonomy** (source integrity → content integrity → distribution → coordination), not a problem taxonomy. I mistakenly created "ensure epistemic security" as a problem entry, but that's a domain label not a specific failure mode. It's like having "ensure AI safety" as an entry.

**Key insight**: "Epistemic security" is instrumental - it matters because it enables coordination on other problems. The interventions serve multiple problems:
- Deepfake detection → AI misuse (`defend-against-ai-harms`)
- Content provenance → AI misuse, also attribution
- Identity verification → AI misuse, fraud
- Deliberation tools → cross-cutting coordination infrastructure

## Disposition

**Problem entry dissolved**: `ensure-epistemic-security.md` removed

**Interventions redistributed to**:
- `defend-against-ai-harms` (Misuse at scale bottleneck):
  - [[content-provenance-verification]]
  - [[source-identity-infrastructure]]
  - [[crowdsourced-verification]]

**Interventions kept as cross-cutting** (useful across multiple problems):
- source-identity-infrastructure - created, useful beyond just AI misuse

**Not created** (lower priority, specific techniques):
- source-track-records
- trust-propagation
- structured-claims-infrastructure
- recommendation-accountability
- virality-friction
- information-diversity
- collective-deliberation-tools
- common-knowledge-infrastructure
- commitment-mechanisms

## Tiling from source (for reference)

```
Defense-dominant epistemic infrastructure
├── Source integrity (who said it?)
│   ├── Source identity infrastructure
│   ├── Source track records
│   └── Trust propagation
├── Content integrity (is it true?)
│   ├── Provenance evidence (capture → custody → claims)
│   ├── Crowdsourced synthesis
│   ├── Information condensation
│   └── Crowdsourced investigation
├── Distribution governance (does truth spread?)
│   ├── Amplification accountability
│   ├── Friction mechanisms
│   └── Diversity injection
└── Coordination infrastructure (can we act on truth?)
    ├── Preference legibility
    ├── Common knowledge
    └── Commitment / finality
```

## Possible future problems

If epistemic threats become more pressing, consider more specific problem entries:
1. **Prevent AI-enabled mass manipulation** - already in defend-against-ai-harms
2. **Prevent information environment capture** - specific to power lock-in/dystopia threat (Entente framework)
3. **Maintain crisis coordination capacity** - instrumental to pandemic response, AI coordination

These would have specific threat models and failure modes, unlike the vague "ensure epistemic security."
