# Proposal: AISI Evaluation Methodology

**Source:** UK AISI Frontier AI Trends Report (2026)
**Category:** Evaluation / Assessment Framework

---

## Primary Evaluation Approaches

1. **Auto-graded tasks**: QA suites, capture-the-flag challenges
2. **Long-form tasks (LFTs)**: Protocol generation, complex reasoning
3. **Agent tasks**: Simulated environments (cyber ranges, software engineering)
4. **Expert red-teaming**: Safeguard stress-testing
5. **Human uplift studies**: Direct impact measurement

---

## Benchmarks Used

| Benchmark | Domain |
|-----------|--------|
| SWE-bench | Software engineering |
| GPQA | General capabilities |
| RepliBench | Self-replication |
| Artificial Analysis Intelligence Index | Cross-domain |
| METR HCAST | Time-horizon tasks |
| METR RE-Bench | Agentic evaluation |
| METR SWAA | Software agent assessment |

---

## Testing Protocol

- **Repetition**: Each task repeated 10 times per model (unless specified)
- **Error measurement**: Standard error of mean (SEM) calculated from task-level success rates
- **Multiple model generations**: Tracking capability changes across model releases

---

## Human Baselines

For biosecurity evaluations:
- PhD holders or equivalent professionals
- 4+ years domain experience required
- 280+ questions per domain (chemistry/biology)

---

## Acknowledged Limitations

> "We may be underestimating the ceiling of capabilities...we do not maximise inference time compute."

Additional limitations:
- Benchmarks may not capture full capability range
- Real-world conditions differ from controlled testing
- Scaffolding and tool access not always maximized

---

## Key Methodological Innovations

### Wet-Lab Validation

Protocol generation evaluated not just on paper but through actual wet-lab implementation—providing ground truth for feasibility assessment.

### Multi-Stage Self-Replication Testing

RepliBench evaluates:
1. Resource acquisition
2. Environment setup
3. Replication execution
4. Persistence maintenance

### Safeguard Correlation Analysis

Systematic measurement of relationship (or lack thereof) between capability scores and safeguard robustness (R² = 0.097).

---

## Relevance for Proposals

This methodology provides:
1. **Reproducible framework**: Standardized testing across model generations
2. **Quantitative tracking**: Concrete metrics for capability progression
3. **Ground truth validation**: Wet-lab testing moves beyond simulated assessment
4. **Safeguard assessment**: Separate evaluation of defensive measures

---

## Key Quote

> "We may be underestimating the ceiling of capabilities...we do not maximise inference time compute." — UK AISI, acknowledging conservative bias in their assessments
