# AI agent accountability

**Tag**: Security

## What it is
Infrastructure for tracking and verifying AI agent behavior through two complementary mechanisms:

**Agent IDs and reputation**: Identification mechanisms for AI systems that enable building and maintaining reputations over time. Helps prevent or disincentivize development of AI agents that attack or exploit other agents, analogous to how humans control exploitation via reputation mechanisms. Allows tracking behavior across interactions and building trust.

**Trace analysis**: Automated tools that analyze logs from autonomous AI agents performing sequential actions. Agents can generate thousands of lines of code and interaction steps, far too much for human review. These tools highlight anomalous behavior patterns, flag security flaws, and produce human-readable summaries of what the agent actually did.

## Why it matters
- Creates accountability and consequences for AI system behavior over time
- Autonomous agent logs exceed human review capacity by orders of magnitude
- Security flaws in agent-generated code can go undetected for months even by expert teams
- Provides incentives for good behavior through reputation effects
- Enables oversight of agentic systems before deployment catches harm

## Current state
- **Status**: Idea
- **Bottlenecks**: Technical implementation of reliable identification; defining meaningful reputation metrics; scaling trace analysis to agent complexity

## Who's working on it
- Not specified

## Sources
- [Peregrine 2025 #88: Agent IDs and Reputation Systems](../sources/peregrine-2025/interventions/peregrine-088.md)
- [Peregrine 2025 #2: Agent Trace Analysis](../sources/peregrine-2025/interventions/peregrine-002.md)
