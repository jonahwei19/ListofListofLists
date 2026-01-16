# Sam Bowman's AI Safety Checklist

**Source**: https://sleepinyourhat.github.io/checklist/
**Date processed**: 2026-01-11
**Total items**: 25 goals across 3 chapters

## Overview

Anthropic-centric safety roadmap organized by phase:
- Chapter 1: Preparation (19 goals) - current phase, ASL 2-4
- Chapter 2: TAI phase (6 goals) - ASL-4/5
- Chapter 3: Post-TAI - no checklist items, defer to institutions

## Mapping to Entries

### Alignment & Verification

| Goal | Maps to | Notes |
|------|---------|-------|
| Solving alignment fine-tuning | [[make-ai-aligned]] | Scalable oversight, avoiding reward hacking |
| Rendering AI harmless | [[contain-unsafe-ai]] | Control-style safeguards |
| Safety cases for ASL-4 | [[verify-ai-alignment]] | Evidence-based safety demonstrations |
| Interpretability for strong assurances | [[extract-insight-from-model-internals]] | Mechanistic safety evidence |
| Evidence of robustness | [[verify-ai-alignment]] | Adversarial testing |
| Calibrated evaluations | [[safety-benchmark-development]] | High-stakes eval design |
| Smoking gun demos | [[detect-evaluation-sandbagging]] | Demonstrating emerging risks |

### Security

| Goal | Maps to | Notes |
|------|---------|-------|
| ASL-3/4 security standards | [[model-weight-security]], [[secure-frontier-data-centers]] | Weight security |
| ASL-5 security (Ch2) | [[sl5-data-center-protocols]] | State-level defense |
| Protecting algorithmic secrets | Out of scope | Competitive dynamics |

### Policy & Governance

| Goal | Maps to | Notes |
|------|---------|-------|
| RSP well-calibrated | [[responsible-scaling-commitments]] | Transparent commitments |
| Preparing to pause/de-deploy | [[responsible-scaling-commitments]] | Commitment to stop |
| Stress-testing safety cases | [[verify-ai-alignment]] | Independent assessment |
| Adjudicating safety cases | Out of scope | Org governance |

### Infrastructure & Coordination

| Goal | Maps to | Notes |
|------|---------|-------|
| Not missing the boat on capabilities | Out of scope | Competitive strategy |
| Adaptive research infrastructure | Out of scope | Internal tooling |
| Supporting societal resilience | [[defend-against-ai-harms]] | External defenses |
| Well-calibrated forecasts | Out of scope | Internal planning |

### AI Welfare

| Goal | Maps to | Notes |
|------|---------|-------|
| AI welfare commitments | Out of scope | Ethics, not resilience |

### TAI-Phase Specific (Chapter 2)

| Goal | Maps to | Notes |
|------|---------|-------|
| Align superhuman AI | [[make-ai-aligned]] | Extension to superhuman |
| Evaluate constantly | [[verify-ai-alignment]] | Continuous assessment |
| Deploy dangerous systems carefully | [[responsible-scaling-commitments]] | Conditional deployment |
| High-stakes decision support | Out of scope | Product decisions |

## Key Insights

1. **Heavy overlap with existing entries**: Almost all goals map to our 4 problem areas (verify, make, contain, defend)

2. **Anthropic-specific framing**: ASL levels, RSP structure, LTBT oversight - useful for understanding one lab's approach but not generalizable

3. **Evaluation integrity as theme**: Recurring concern about systems gaming evaluations, especially as they gain strategic reasoning capability

4. **No new problems identified**: This checklist elaborates existing problems rather than revealing new ones

## Not Creating Entries For

- Competitive capability access (strategic, not safety)
- Internal org governance (adjudication, LTBT)
- AI welfare (ethics domain, not resilience)
- Forecasting/planning (meta)
- Algorithmic secret protection (competitive dynamics)

## Summary

25 goals, most map to existing 4 problems. Provides good detail on Anthropic's approach but doesn't reveal new problem categories. Useful for enriching intervention details (e.g., specific eval approaches, security standards).
