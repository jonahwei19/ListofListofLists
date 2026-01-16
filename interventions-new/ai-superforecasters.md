# AI Superforecasters

**Tag**: Science

## What it is
AI systems that achieve human superforecaster-level accuracy through:

- **Agentic search**: Automated retrieval from high-quality news sources (AskNews outperforms Perplexity on recency)
- **Supervisor reconciliation**: Multi-agent architecture where a supervisor agent reconciles disparate forecasts
- **Statistical calibration**: Techniques to counter behavioral biases in LLMs (overconfidence, anchoring)
- **Reasoning transparency**: Visible reasoning trees allowing users to inspect, modify, and correct prediction logic

## Why it matters
- **Current gap**: Individual LLMs roughly match human crowd performance but still significantly underperform superforecasters (o3 Brier: 0.1352 vs. superforecasters: 0.0225)
- **Domain variance**: LLMs perform notably better on political vs. economic forecasting—economics may require deeper world models
- **Decision support**: Transparent AI forecasting could augment high-stakes decisions in biosecurity, AI governance, and policy
- **Scalability**: Human superforecasters are rare; AI systems could scale forecasting capacity

## Current state
- **Status**: Research/Competition
- **Recent developments (2025)**:
  - AIA Forecaster achieves superforecaster parity on ForecastBench benchmark
  - Q2 Metaculus tournament: 54 bot-makers competed, human Pro Forecasters still outperformed (p=0.00001)
  - Median prediction for AI matching top Metaculus forecasters: February 2028
  - Best-performing model: OpenAI o3, with performance gains from better news sources and scaffolding
- **Bottlenecks**: Economic forecasting accuracy; calibration on long-horizon questions; integration with decision workflows

## Who's working on it
- **Metaculus**: AI Benchmarking Series tournaments, forecasting-tools framework
- **AIA/ForecastBench**: Achieved superforecaster parity with agentic approach
- **Good Judgment Project**: Human superforecaster baseline and methodology
- **Academic groups**: Multiple research teams publishing on LLM forecasting (arxiv papers)

## Sources
- [Peregrine 2025 #76: AI Forecasters](../sources/peregrine-2025/interventions/peregrine-076.md)
