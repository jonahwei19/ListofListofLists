# Multi-agent safety systems

**Tag**: Security

## What it is
Infrastructure for monitoring, simulating, and governing interactions between multiple AI agents. Two complementary components:

**Multi-agent monitoring**: Systems that actively watch deployments and interactions between AI systems, identifying potentially harmful feedback loops or emergent goals before they become problematic. The field is underdeveloped; agentic interactions are either poorly captured or not well-conceptualized within existing frameworks.

**Multi-agent safety protocols**: Protocols to prevent emergent cooperation between agents to circumvent safety constraints. Establishes methods for AI systems to verify trustworthiness of other agents, report problematic behavior, and implement collective safety measures across distributed systems. Includes tracking trust relationships and identifying bad actors.

## Why it matters
- Financial transactions, supply chains, and information exchange increasingly mediated by interconnected AI systems with minimal human oversight
- As AI systems increasingly interact with each other, emergent behaviors could arise that weren't present in individual systems
- High-speed AI-to-AI interactions outpace human monitoring capacity
- Without monitoring, multi-agent dynamics remain invisible until they cause harm

## Current state
- **Status**: Research (rapidly developing field)
- **Key risks identified (2025)**:
  - Emergent collusion via shared state/privileges rather than explicit planning
  - Steganographic communication enabling secret coordination channels
  - Protocol-level attacks: message tampering, role spoofing, protocol exploitation
  - "Patchwork AGI" hypothesis: near-AGI capability emerging from coordinated sub-AGI agents before individual AGI
  - Single compromised agent can trigger harm across entire multi-agent system
- **Research directions**:
  - High-fidelity simulation environments for testing coordination protocols before deployment
  - Distributional AGI safety frameworks for composite systems
  - Architectural approaches embedding risk management into multi-agent design
  - Trust verification protocols between agents
- **Bottlenecks**: Tracing failures across peer interactions is complex; human oversight speed limits; conceptual frameworks still developing

## Who's working on it
- **Cooperative AI Foundation**: Major technical report on multi-agent risks (50+ researchers from DeepMind, Anthropic, CMU, Harvard)
- **World Economic Forum**: Multi-agent safety frameworks
- **Anthropic**: Constitutional AI research for embedding safety constraints in agents
- **Academic groups**: Emergent behavior and multi-agent security research (multiple arxiv papers)

## Sources
- [Peregrine 2025 #78: Monitor Complex Agent Interactions](../sources/peregrine-2025/interventions/peregrine-078.md)
- [Peregrine 2025 #57: Multi-Agent Interaction Framework](../sources/peregrine-2025/interventions/peregrine-057.md)
