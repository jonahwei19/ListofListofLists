# Performance Monitoring Practices

**Maps to interventions**:
- `model-drift-monitoring.md`
- `usage-incident-monitoring.md`
- `agent-trace-analysis.md`

## Relevant CSET Practices (Performance Monitoring Topic)

### PM-1: Monitoring Performance
> "Determine what technical and business metrics should be measured and monitored over the course of the system's life cycle. Conduct continuous monitoring and regular validation of system performance."

**AI Score**: 78%

### PM-2: Performance Drift and Misalignment
> "Measure the model's performance for drift, misalignment, and behavior change. Conduct regular health checks to ensure the model continues to align with the organizations' values and risk tolerance. Review when new versions are deployed."

**AI Score**: 79%

### PM-3: Continuous Reassessment
> "Conduct regular risk and impact assessments, evaluations, red-teaming exercises, and penetration testing. Continuously reassess the effectiveness of the tests and metrics being used."

**AI Score**: 43%

### PM-4: Corrective Action
> "Take corrective action when an issue, noncompliance, or nonconformity is identified. Assess the effectiveness of the corrective action taken. Update response and recovery strategies as necessary."

**AI Score**: 65%

### PM-5: Oversight
> "Continually identify improvements from evaluation and monitoring activities. Validate that these activities provide sufficient information for audit, compliance, and oversight."

**AI Score**: 31%

## Connection to Existing Interventions

**Model Drift Monitoring**: PM-2 directly addresses this: "Measure the model's performance for drift, misalignment, and behavior change." This provides explicit guidance for what open-source drift monitoring tools should measure.

**Usage Incident Monitoring**: PM-1's "continuous monitoring and regular validation of system performance" combined with PM-4's corrective action when "noncompliance or nonconformity is identified" describes the monitoring-to-response pipeline.

**Agent Trace Analysis**: PM-1's emphasis on "technical and business metrics" measured "over the course of the system's life cycle" applies to tracing agent behavior through multi-step tasks.

## Key Insight on AI-Specific Monitoring

The report notes:
> "A heavy emphasis in existing guidance is placed on testing and evaluation capabilities for AI. This includes pre-deployment testing and continuous post-deployment monitoring and evaluation. In particular, there is a focus on how benchmarking and new AI red-teaming techniques should be incorporated into existing organizational TEVV practices."

PM-2's high AI Score (79%) confirms that drift and misalignment monitoring is genuinely AI-specific guidance, not just general software monitoring applied to AI.
