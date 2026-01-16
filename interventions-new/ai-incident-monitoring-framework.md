# AI incident monitoring and reporting framework

**Tag**: Security

## What it is
Comprehensive infrastructure for detecting, logging, analyzing, and sharing AI incidents across the ecosystem. Three integrated components:

**Incident reporting framework**: Standardized mechanisms and procedures for documenting AI failures, misuse, or unexpected behaviors. Develops taxonomies for severity classifications and facilitates coordinated responses. Modeled on aviation safety reporting systems, including protections for whistleblowers and requirements for timely disclosure.

**Cross-organization incident detection**: Standardized framework for logging, anonymizing, and analyzing AI misbehavior across organizations. Infrastructure allows developers and third-party researchers to search through incidents, identify patterns, and share findings while protecting sensitive user data and IP. Labs collaborate directly without a third party. Expands on systems like Anthropic's CLIO.

**Usage monitoring**: Robust incident monitoring and usage data analysis to understand real-world AI utilization patterns. Replaces theoretical threat-modeling with data-driven insights from actual usage. Labs currently avoid deep usage analysis due to legal liability and privacy concerns, creating significant blind spots.

## Why it matters
- Without standardized reporting, lessons from incidents remain siloed and same mistakes get repeated
- Without shared infrastructure, each lab discovers problems in isolation
- Without understanding how systems are actually used, safety measures may miss real-world risks
- Aviation's safety record demonstrates the value of mandatory, protected reporting
- Identifies emerging misuse patterns before they become widespread

## Current state
- **Status**: Pilot/Deployed (international framework developing)
- **Recent developments (2025)**:
  - OECD released "Towards a Common Reporting Framework for AI Incidents" (February 2025)—global benchmark for incident reporting
  - Framework developed from 88 criteria refined to 29 key characteristics
  - OECD AI Incidents Monitor (AIM) tracks incidents in real-time from press reports since 2023
  - AI Incident Database (AIID) free and open-source, operated by Responsible AI Collaborative
  - Framework allows domestic tailoring while maintaining international interoperability
- **Framework components**: AI system classification, harm characterization, risk definitions (incident = realized harm, risk = potential precursor)
- **Bottlenecks**: Lab buy-in for proactive reporting; liability and privacy concerns; coordinated regulatory implementation; anonymization standards

## Who's working on it
- **OECD**: Common reporting framework and AI Incidents Monitor (AIM)
- **Responsible AI Collaborative**: AI Incident Database (AIID)—open-source incident indexing
- **Anthropic**: CLIO system for internal incident detection

## Sources
- [Peregrine 2025 #87: Incident Reporting](../sources/peregrine-2025/interventions/peregrine-087.md)
- [Peregrine 2025 #80: Comprehensive Incident Detection System](../sources/peregrine-2025/interventions/peregrine-080.md)
- [Peregrine 2025 #67: Usage and Incident Monitoring Systems](../sources/peregrine-2025/interventions/peregrine-067.md)
