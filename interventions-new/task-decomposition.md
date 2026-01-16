# Task decomposition for dangerous capabilities

**Tag**: Security

## What it is
Architectural approach splitting dangerous AI capabilities across multiple isolated systems or users, preventing any single agent from having complete capability. Example: a bioweapon design task might be decomposed so one system handles molecular modeling, another handles synthesis planning, and neither has access to the other's outputs—only a human reviewer can combine them. Interfaces are designed so compartments can contribute to beneficial tasks while preventing end-to-end execution of catastrophic operations.

## Why it matters
- Provides defense-in-depth at architecture level, not just alignment level
- Even compromised individual systems cannot independently cause worst outcomes
- Reduces single points of failure for high-stakes applications

## Current state
- **Status**: Idea
- **Bottlenecks**: Designing decompositions that actually prevent recombination; performance overhead of compartmentalization

## Who's working on it
- Not specified

## Sources
- [Peregrine 2025 #3: Task Decomposition](../sources/peregrine-2025/interventions/peregrine-003.md)
