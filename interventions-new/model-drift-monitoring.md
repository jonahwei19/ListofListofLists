# Open-Source Model Drift Monitoring

**Tag**: Security

## What it is
Open-source tools to detect, measure, and address gradual changes in model behavior over time. Components:

- **Statistical drift detection**: Population Stability Index (PSI), KL Divergence to quantify input distribution changes
- **Embedding-based detection**: Track prompt embedding clusters over time; detect when queries form new clusters or shift centers
- **Canary prompts**: Fixed, unchanging test inputs that surface behavioral drift in reasoning style, tone, or confidence
- **Output consistency tracking**: Monitor response variations against defined thresholds
- **Semantic drift detection**: Identify when word meanings shift (e.g., "delivery" expanding from physical to digital)

## Why it matters
- **Gradual degradation**: Model drift manifests as reduced accuracy, increased latency, or irrelevant outputs
- **Concept drift**: Shifting word meanings can confuse models trained on historical data
- **Security vulnerability**: Undetected drift creates windows for exploitation
- **Vendor-neutral tools** enable independent verification and community trust

## Current state
- **Status**: Research → Pilot (tooling maturing in 2025)
- **Recent developments (2025)**:
  - Thinking Machines Lab (September 2025): Identified batch-size variation as primary cause of LLM nondeterminism; developed batch-invariant kernels for exact reproducibility
  - Phoenix: Embedding drift monitoring tracking vector representation changes
  - LangSmith: All-in-one developer platform with visual accuracy metrics and real-time alerts
  - Braintrust: 80x faster query performance for combined evaluation/monitoring workflows
- **Bottlenecks**:
  - Establishing baseline datasets for production prompts
  - Cross-provider validation protocols needed
  - Comprehensive logging with immutable audit trails
  - Real-time detection at scale

## Who's working on it
- **Fiddler AI**: LLMOps drift monitoring platform
- **Galileo**: Production LLM monitoring strategies
- **Braintrust**: Evaluation + monitoring platform
- **LangSmith (LangChain)**: Agent/chain debugging and drift detection
- **AWS**: Embedding drift research for LLMs
- **Thinking Machines Lab**: Deterministic computing research

## Sources
- [Peregrine 2025 #79: Open-Source AI Drift Monitoring](../sources/peregrine-2025/interventions/peregrine-079.md)
