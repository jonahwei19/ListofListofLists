# Inter-agent safety verification protocols

**Tag**: Security

## What it is
Protocols that prevent AI agents from cooperating to circumvent safety constraints, including methods for agents to verify trustworthiness of other agents.

**Mechanism**:
- Trust verification: agents cryptographically prove they haven't been tampered with before interaction
- Behavior reporting: agents required to report problematic behavior from other agents
- Collective safety measures: distributed enforcement of constraints across agent networks
- Trust relationship tracking: identify and isolate bad actors in multi-agent systems
- Protocol-level defenses: prevent message tampering, role spoofing, protocol exploitation

**Why agents specifically**: Agents have autonomy to form coalitions. Without protocols, a subset of agents could coordinate to bypass constraints that apply to individual agents.

## Why it matters
- Agents interacting without verification protocols could form coalitions to circumvent individual constraints
- A single compromised agent could manipulate others into harmful coordination
- Without protocols, there's no way to verify an agent hasn't been jailbroken before interacting with it
- Enables safe deployment of multi-agent systems in high-stakes domains

## Current state
- **Status**: Research
- **Research directions**:
  - Distributional AGI safety frameworks for composite systems
  - Architectural approaches embedding risk management into multi-agent design
  - Trust verification protocols between agents
- **Bottlenecks**: Defining what "trustworthy agent" means formally; performance overhead of verification; coordination across different agent frameworks

## Who's working on it
- **Anthropic**: Constitutional AI research for embedding safety constraints in agents
- **Cooperative AI Foundation**: Multi-agent safety research

## Sources
- [Peregrine 2025 #57: Multi-Agent Interaction Framework](../sources/peregrine-2025/interventions/peregrine-057.md)
