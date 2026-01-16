# Remote GPU disable capability

**Tag**: Security

## What it is
Technical mechanisms allowing authorized parties to remotely disable AI accelerator chips when policy violations are detected.

**Mechanism**:
- Firmware-level kill switch installed on AI chips
- Activation requires cryptographic authorization (potentially multi-party)
- Ties into chip tracking system to identify specific hardware for disabling
- Can be triggered by: unauthorized location (e.g., chip exported illegally), policy violation detected, international agreement breach
- Reversible disable (licensing expired) vs. permanent disable (serious violation)

**Why this is controversial but important**: Gives governments enforcement capability for AI regulations. Without enforcement mechanisms, AI governance is voluntary.

## Why it matters
- Provides actual enforcement capability for AI governance (not just paper agreements)
- Creates deterrence against unauthorized frontier AI development
- Enables response to detected threats before training completes
- Intelligence on compute movements reveals unauthorized scaling attempts

## Current state
- **Status**: Idea (controversial)
- **Bottlenecks**: Cybersecurity risks of remote disable capability; potential for abuse; industry resistance; international agreement on who holds keys; technical implementation in existing firmware

## Who's working on it
- **No dedicated organization identified** (highly sensitive area)
- Policy discussions in government circles

## Sources
- [Peregrine 2025 #74: Hardware Kill Switches and Location Tracking](../sources/peregrine-2025/interventions/peregrine-074.md)
