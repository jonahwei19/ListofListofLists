# Interpretability supercomputing centers

**Tag**: Science

## What it is
Global supercomputing centers dedicated to interpretability research with approximately $1 billion in distributed compute resources. Freely accessible to researchers worldwide through fast-grant mechanisms. A philanthropically-funded successor to initiatives like OpenAI's abandoned Superalignment project. Could follow rapid deployment models like xAI (data center in two months).

## Why it matters
- Interpretability research requires massive compute to analyze large models
- Most researchers lack access, limiting who can work on understanding model internals
- Democratized infrastructure could accelerate one of the most promising safety approaches

## Current state
- **Status**: Idea (infrastructure), Active Research (methods)
- **Methodological progress (2024-2025)**:
  - Sparse autoencoders now work at scale: Anthropic extracted tens of millions of interpretable features from Claude 3 Sonnet using dictionary learning
  - 70% of extracted features map cleanly to single concepts (Arabic script, DNA motifs, etc.)—up from polysemantic neurons
  - Safety-relevant features identified: deception, sycophancy, bias, dangerous content
  - Cross-coders enable "diffing" models to understand changes
  - Method generalizing beyond LLMs: applied to protein language models with biological interpretability
- **Bottlenecks**: Funding for dedicated infrastructure; rapid deployment capability; compute costs still prohibitive for most researchers

## Who's working on it
- **Anthropic Interpretability Team**: Leading sparse autoencoder scaling, integration with Responsible Scaling Policy
- **AI Safety Foundation**: Open-source sparse autoencoder tools
- **OpenAI Superalignment**: Related but abandoned

## Sources
- [Peregrine 2025 #39: Mechanistic Interpretability Infrastructure](../sources/peregrine-2025/interventions/peregrine-039.md)
