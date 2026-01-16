# Atlas AI Resilience Gap Map

**Source**: Excel file from Atlas
**Date processed**: 2026-01-11
**Total items**: 23 gaps across multiple domains

## Overview

Gap analysis for AI resilience. Categories: AI Trustworthiness, Model Security, Biosecurity, Cybersecurity, Epistemic Security, Economic Security, Civil Resilience, AI Governance, Force Multipliers.

## Mapping to Entries

### AI Trustworthiness & Security

| Gap | Maps to | Notes |
|-----|---------|-------|
| AI capabilities outpacing trustworthiness tools | [[verify-ai-alignment]] | Core alignment verification problem |
| Multi-billion dollar secure AI investment | Out of scope | Funding coordination, not technical intervention |
| AI systems as high-value targets | [[model-weight-security]], [[secure-frontier-data-centers]] | Already covered |
| Post-deployment model modification | [[barriers-to-fine-tuning]] | Already covered |

### Biosecurity

| Gap | Maps to | Notes |
|-----|---------|-------|
| Preventing novel biological threat creation | [[defend-against-ai-harms]] (Bio section) | Synthesis screening, etc. |
| Pathogen detection and surveillance | [[metagenomic-pathogen-surveillance]] | Already covered |
| Medical countermeasure timelines | [[broad-spectrum-countermeasures]] | Already covered |
| Biothreat reporting from AI labs | NEW: [[ai-lab-biosecurity-reporting]] | Specific gap - no clear pathway when labs detect biorisk |

### Cybersecurity

| Gap | Maps to | Notes |
|-----|---------|-------|
| AI advantage for offense over defense | [[automated-vulnerability-patching]], [[formally-verified-software]] | Already covered |

### Epistemic Security

| Gap | Maps to | Notes |
|-----|---------|-------|
| AI-scaled disinformation | [[defend-against-ai-harms]] (Misuse at scale) | Redistributed here |

### Economic/Civil/Governance

| Gap | Maps to | Notes |
|-----|---------|-------|
| AI job automation at unprecedented scale | Out of scope | Economic disruption, not catastrophic risk |
| AI engagement reducing agency | Out of scope | Individual autonomy, not mass casualty |
| AI persuasion exceeding human ability | [[defend-against-ai-harms]] | Manipulation concern |
| AI-enabled mass surveillance | Out of scope | Civil liberties, not existential |
| Rubber-stamping AI outputs | Out of scope | Process problem |
| Power centralization through AI | NEW: [[prevent-ai-power-concentration]] | Dystopia threat from Entente |
| Institutional legitimacy for AI governance | Out of scope | Meta/process |
| Verifiable AI deployment | [[hardware-enabled-governance]] | Already covered |
| Systematic blindspots in threat models | Meta | Self-referential |

### Force Multipliers (Meta)

| Gap | Maps to | Notes |
|-----|---------|-------|
| Organizational development | Out of scope | Meta |
| Talent limitations | Out of scope | Meta |
| Philanthropic funding | Out of scope | Meta |
| Public attention | Out of scope | Meta |

## New Entries Created

1. **AI lab biosecurity reporting** - Created [[ai-lab-biosecurity-reporting]] in interventions-new/. Organization to receive, analyze, and respond to biorisk reports from frontier AI labs.

2. **Prevent AI-enabled power concentration** - Already exists as [[prevent-ai-power-concentration]] problem entry with Atlas source linked.

## Related Lists (from source)

The "Related lists" tab references sources we already have:
- Convergent Research Gap Map ✓ processed
- MIT AI Risk Repository ✓ pending
- Project GRASP ✓ pending
- Schmidt Sciences Agent Security ✓ just processed
- Sam Bowman's Checklist ✓ pending
- List of Lists of Biosecurity Projects ✓ pending
- List of Lists of AI Safety Projects ✓ pending
- IFP Preventing AI Sleeper Agents - NEW source to add
- Open Problems in Technical AI Governance (arXiv) - NEW source to add

## Summary

23 gaps processed:
- Created 12 proposal files in `proposals/` subdirectory for specific technical gaps
- Added Atlas as source to 10 existing intervention/problem files
- Created new intervention: [[ai-lab-biosecurity-reporting]]
- Power concentration already covered by existing [[prevent-ai-power-concentration]] problem
- Skipped meta/funding/process gaps per instructions

Also identified 2 new sources from "Related lists" tab.
