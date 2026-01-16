# Inference-only data center verification

**Tag**: Security

## What it is
Technical mechanisms to verify that data centers are being used only for inference (running existing models) and not for training new models.

**Mechanism**:
- Develop hardware/software retrofitting package that constrains facility to inference workloads
- Package monitors: compute patterns (training vs inference signatures differ), data flows (training requires massive dataset ingestion), gradient calculations (only present in training)
- Install on existing data centers without replacing hardware
- Train vetted installers and auditors (thousands needed globally)
- Regular audits verify installation integrity
- Enables treaties that limit training while preserving inference economic value

**Why this matters for enforcement**: Nations/companies can agree to not train new models above threshold while continuing to run existing ones. Verification prevents cheating.

## Why it matters
- Preserves economic value of AI inference while enabling training limitations
- Makes compute caps enforceable by distinguishing training from inference
- Enables international agreements with verification rather than just trust
- Retrofittable to existing infrastructure (doesn't require new data center construction)

## Current state
- **Status**: Research (R&D needed)
- **Bottlenecks**: Developing reliable training vs inference detection; tamper-proofing the verification system; training sufficient auditors; cost of global deployment

## Who's working on it
- **No dedicated organization identified** (gap area)

## Sources
- [AI Futures Project: Early US Policy Priorities for AGI](../sources/ai-futures-project/Early%20US%20policy%20priorities%20for%20AGI.md)
