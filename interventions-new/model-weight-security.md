# Model weight security

**Tag**: Security

## What it is
Comprehensive security measures protecting frontier AI model weights from theft, leakage, or unauthorized access. RAND's 2024 framework established five security levels (SL1-SL5): SL1 deters hobby hackers, SL5 secures against elite nation-state attackers with measures comparable to nuclear weapons protection. Key measures include: centralizing weights on access-controlled systems, insider threat programs, API hardening against exfiltration, differential privacy noise injection, confidential computing (trusted execution environments), and advanced red-teaming.

## Why it matters
- Model weights are a single point of failure: one leak bypasses years of safety work
- Adversaries with leaked weights can fine-tune away guardrails within hours
- A stolen frontier model would be worth hundreds of millions on the black market
- Recent incidents: OpenAI breach 2023 (internal communications), DeepSeek database backdoor January 2025, xAI internal LLM leak July 2025

## Current state
- **Status**: Pilot (uneven implementation)
- **Industry adoption**: 12 companies have published frontier AI safety policies (Anthropic, OpenAI, Google DeepMind, Meta, xAI, etc.) with weight security commitments
- **Gap**: Only 20% of organizations specifically test for model theft despite 97% claiming AI security priority (Hidden Layer 2024)
- **Technical challenge**: Weights are decrypted and vulnerable during use; confidential computing (TEEs) addresses this but adds complexity
- **Current benchmarks**: Google's Gemini 2.5 claims "RAND SL2" alignment

## Who's working on it
- **RAND Corporation**: Security framework and recommendations
- **Major labs**: Anthropic, OpenAI, Google DeepMind implementing varying security levels
- **METR**: Tracking common elements of frontier AI safety policies
- **UK AI Security Institute**: Evaluating lab security practices

## Sources
- [Peregrine 2025 #159: Model Weight Security](../sources/peregrine-2025/interventions/peregrine-159.md)
- [Atlas AI Resilience Gap Map: AI Systems as Targets](../sources/atlas-ai-resilience/proposals/ai-systems-as-targets.md)
