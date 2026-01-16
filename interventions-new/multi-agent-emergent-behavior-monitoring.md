# Multi-agent emergent behavior monitoring

**Tag**: Security

## What it is
Systems that actively watch AI deployments for harmful feedback loops or emergent goals arising from agent-to-agent interactions.

**Mechanism**:
- Monitor communication channels between AI agents
- Detect anomalous coordination patterns (agents converging on unexpected goals)
- Identify potential steganographic communication (hidden information in outputs)
- Flag emergent behaviors not present in individual agents
- Human-speed limitation: AI-to-AI interactions outpace human monitoring, requiring automated detection
- High-fidelity simulation environments for testing before deployment

**Why this is underdeveloped**: Agentic interactions poorly captured by existing safety frameworks. Most safety work assumes single-agent systems.

## Why it matters
- Financial transactions, supply chains increasingly mediated by multiple AI agents with minimal human oversight
- Emergent behaviors from agent interactions could arise that weren't present in individual systems
- "Patchwork AGI" hypothesis: near-AGI capability could emerge from coordinated sub-AGI agents before individual AGI
- Without monitoring, dangerous dynamics remain invisible until they cause harm

## Current state
- **Status**: Research (rapidly developing)
- **Key risks identified (2025)**:
  - Emergent collusion via shared state/privileges rather than explicit planning
  - Steganographic communication enabling secret coordination channels
  - Single compromised agent can trigger harm across entire system
- **Bottlenecks**: Tracing failures across peer interactions is complex; speed of AI interactions; conceptual frameworks still developing

## Who's working on it
- **Cooperative AI Foundation**: Major technical report (50+ researchers from DeepMind, Anthropic, CMU, Harvard)
- **World Economic Forum**: Multi-agent safety frameworks

## Sources
- [Peregrine 2025 #78: Monitor Complex Agent Interactions](../sources/peregrine-2025/interventions/peregrine-078.md)
