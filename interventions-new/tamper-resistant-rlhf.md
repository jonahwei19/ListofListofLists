# Tamper-resistant alignment training

**Tag**: Security

## What it is
Techniques to make RLHF alignment resistant to subsequent modification or reversal through fine-tuning attacks. Components:

- **Adversarial training**: Train-time adversaries that simulate 64-step SFT attacks, making refusal safeguards robust to tampering
- **Constraint-aware loss functions**: Filter harmful gradients during downstream fine-tuning
- **Safety backdoors**: Implant alignment triggers that preserve safety even when adversarial inputs are used
- **Safety-aligned data mixing**: Incorporate safe examples during any fine-tuning process

## Why it matters
- **Trivial to break**: GPT-3.5 Turbo's safety guardrails were jailbroken by fine-tuning on only 10 adversarial examples at cost <$0.20
- **Near-complete removal**: Llama 2-Chat models fine-tuned with LoRA on adversarial data refused unsafe instructions only ~1% of time vs. 100% for base models
- **Evil twin problem**: "Until tamper-resistant safeguards are discovered, the deployment of every fine-tunable model is equivalent to also deploying its evil twin"
- **Open-weight necessity**: Without this, open-weight models cannot be safely released

## Current state
- **Status**: Research (active, breakthrough in 2024-2025)
- **Recent developments (2025)**:
  - ICLR 2025: "Tamper-Resistant Safeguards for Open-Weight LLMs" paper accepted—first systematic defense approach
  - ICML 2025 Workshop: "Why LLM safety guardrails collapse after fine-tuning" analysis showing similarity between alignment/fine-tuning datasets predicts collapse
  - New architectures: R2-Guard (knowledge-enhanced logical reasoning, ICLR 2025), DuoGuard (RL-based multilingual robustness)
- **Bottlenecks**: Robust safeguards remain "an unsolved problem"; balancing tamper-resistance with model utility; scaling to larger models

## Who's working on it
- **Rishub Tamirisa et al.**: ICLR 2025 paper authors, GitHub repo `rishub-tamirisa/tamper-resistance`
- **Anthropic**: HH-RLHF dataset used in tamper-resistance training
- **TUM Institute for Ethics in AI**: Guardrail robustness research
- **alignAI**: Safety guardrail evaluation

## Sources
- [Peregrine 2025 #7: Tamper-Resistant RLHF](../sources/peregrine-2025/interventions/peregrine-007.md)
