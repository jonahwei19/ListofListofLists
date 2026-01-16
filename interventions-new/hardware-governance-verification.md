# Hardware governance and verification

**Tag**: Security

## What it is
Hardware-level mechanisms for governing and verifying AI development, comprising four interconnected approaches:

**Global hardware tracking**: Reporting and verification requirements for all high-performance computing hardware above specified computational capacity thresholds. Tracks GPUs, TPUs, and similar processors globally, including retrofitting tracking on older models. Requires international collaboration with major hardware producers (NVIDIA, AMD, Intel, Google, Huawei).

**On-chip monitoring**: Hardware-level monitoring technologies embedded directly into AI accelerator chips to verify compliance with international agreements. Employs hardware engineers, designers, and manufacturing specialists to prototype verification technologies integrating with commercial chip manufacturing—similar to nuclear verification protocols.

**FlexHEG (Flexible Hardware-Enabled Governance)**: Each chip placed in a tamper-proof enclosure alongside a secure processor that monitors and filters all information and instructions. Supports training run size limitations, verification of appropriate data usage, standardized safety evaluations, and controlled access to model weights. Updates require signature by a quorum of international parties with rollback to minimal baseline ruleset.

**Kill switches**: Technical mechanisms to remotely disable GPUs when policy violations are detected. Tracks specific hardware shipments and movements, providing intelligence on compute scaling and enforcement capability.

## Why it matters
- Creates comprehensive awareness of which organizations are utilizing advanced computing resources
- Provides technical foundation for international treaty compliance and enforcement
- Enables detection of illicit national-scale AI activity (e.g., unauthorized intelligence explosion attempts)
- Enforces constraints through technical mechanisms rather than purely policy
- Enables privacy-preserving verification without exposing proprietary details

## Current state
- **Status**: Research/Pilot (active development)
- **Recent developments (2025)**:
  - Nvidia piloting chip-tracking software using existing telemetry to estimate device location (no hardware modification required)
  - White House OSTP Director Michael Kratsios considering chip-level location tracking for export control enforcement
  - Longview Philanthropy funding FlexHEG FRO ($2-10M seed, goal: working FlexHEGs in 2-3 years)
  - Hardware-enabled mechanisms (HEMs) papers exploring visibility tools and enforcement mechanisms
  - Offline licensing systems proposed: cryptographically signed licenses verified by stored public key
  - High-end AI chips represent only 0.00025% of global semiconductor production—enabling targeted regulation
- **Bottlenecks**: Requires coordination with NVIDIA, AMD, Intel, Google, Huawei; international treaty frameworks; firmware updates may be faster than chip redesign; anti-tamper techniques against well-resourced actors; privacy protections for chip owners

## Who's working on it
- **Longview Philanthropy**: Funding FlexHEG FRO development
- **NVIDIA**: Piloting chip-tracking software
- **White House OSTP**: Policy development for hardware controls
- **CNAS**: Research on securing AI chip supply chain
- **Future of Life Institute**: Hardware-backed compute governance research
- **IAPS**: Location verification research for AI chips

## Sources
- [Peregrine 2025 #68: Global Hardware Verification](../sources/peregrine-2025/interventions/peregrine-068.md)
- [Peregrine 2025 #70: On-Chip Monitoring Mechanisms](../sources/peregrine-2025/interventions/peregrine-070.md)
- [Peregrine 2025 #71: Flexible Hardware for AI Governance](../sources/peregrine-2025/interventions/peregrine-071.md)
- [Peregrine 2025 #74: Hardware Kill Switches and Location Tracking](../sources/peregrine-2025/interventions/peregrine-074.md)
- [Atlas AI Resilience Gap Map: Verifiable Deployment](../sources/atlas-ai-resilience/proposals/verifiable-deployment.md)
