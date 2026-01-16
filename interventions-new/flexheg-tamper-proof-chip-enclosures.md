# FlexHEG tamper-proof chip enclosures

**Tag**: Security

## What it is
Physical enclosures that wrap AI chips, containing a secure processor that monitors and filters all instructions before they reach the chip.

**Mechanism**:
- Each AI chip placed in tamper-proof physical enclosure
- Secure processor inside enclosure intercepts all I/O
- Processor enforces rules: training run size limits, data usage verification, mandatory safety evaluations, controlled weight access
- Rules can be updated only with cryptographic signatures from quorum of international parties
- If tampering detected, rolls back to minimal baseline ruleset
- FlexHEG = Flexible Hardware-Enabled Governance

**Why physical enclosures vs on-chip**: Can be retrofitted to existing chips without waiting for new chip designs. International governance rules can be updated without hardware changes.

## Why it matters
- Retrofittable to existing hardware (doesn't require next-gen chip redesign)
- International governance without relying on software enforcement
- Quorum requirement prevents any single nation from unilaterally changing rules
- Tamper detection provides verifiable compliance

## Current state
- **Status**: Research (funded, 2-3 year development timeline)
- **Funding**: Longview Philanthropy providing $2-10M seed funding for FlexHEG FRO
- **Bottlenecks**: Tamper-proofing against well-resourced actors; defining initial ruleset; achieving international quorum agreement; installation logistics

## Who's working on it
- **Longview Philanthropy**: Funding FlexHEG FRO development

## Sources
- [Peregrine 2025 #71: Flexible Hardware for AI Governance](../sources/peregrine-2025/interventions/peregrine-071.md)
