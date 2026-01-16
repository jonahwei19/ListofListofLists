# Human labeling service

**Tag**: Science

## What it is
Non-profit service providing billions of high-quality preference labels to replace proxy models in RLHF. Uses asynchronous setups to await human inputs rather than approximating with learned proxies. Requires verification systems to prove it isn't conducting data poisoning attacks. Offers at-cost, high-quality data that labs would naturally want to use.

## Why it matters
- RLHF uses proxy models because real human feedback is expensive, but proxies introduce misalignment
- Massive amounts of genuine human preference data could reduce this misalignment
- Gives safety-focused organizations leverage over training processes

## Current state
- **Status**: Idea
- **Bottlenecks**: Scale of human labeling operation; verification against data poisoning

## Who's working on it
- Not specified

## Sources
- [Peregrine 2025 #6: Human Labeling Service](../sources/peregrine-2025/interventions/peregrine-006.md)
