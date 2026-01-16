# AI chip tracking registry

**Tag**: Security

## What it is
Global database tracking all high-performance AI chips above specified FLOPS thresholds, with reporting requirements for hardware producers and data centers.

**Mechanism**:
- Hardware producers (NVIDIA, AMD, Intel) report serial numbers and initial buyers to centralized registry
- Data centers above threshold capacity must register chip inventories
- Telemetry from chips reports approximate location (NVIDIA already piloting this)
- Intelligence agencies cross-reference declared inventories against detected clusters
- Domestic enforcement via DPA Section 705 for US-based facilities

**Why not just use export controls**: Export controls track chips leaving country. Registry tracks where chips end up and whether they're being used for undisclosed large training runs.

## Why it matters
- AI chips represent only 0.00025% of global semiconductor production—small enough for targeted tracking
- Detects undisclosed frontier AI projects before they complete dangerous training runs
- Provides foundation for any international AI treaty enforcement
- Makes compute harder to aggregate secretly for unauthorized capability jumps

## Current state
- **Status**: Pilot
- **Recent developments (2025)**:
  - NVIDIA piloting chip-tracking software using existing telemetry to estimate device location
  - White House OSTP Director considering chip-level location tracking for export control enforcement
- **Bottlenecks**: International coordination needed; privacy concerns for legitimate users; chip movement after initial sale

## Who's working on it
- **NVIDIA**: Piloting telemetry-based tracking
- **White House OSTP**: Policy development
- **IAPS**: Location verification research

## Sources
- [Peregrine 2025 #68: Global Hardware Verification](../sources/peregrine-2025/interventions/peregrine-068.md)
