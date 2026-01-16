# Tamper-Resistant RLHF

**Source**: Peregrine 2025, Proposal #7
**Original**: https://riskmitigation.ai/wp-content/uploads/The-2025-Peregrine-Report.pdf
**Specificity**: Specific technique

## What it is
Develop techniques to make alignment methods like reinforcement learning from human feedback (RLHF) resistant to subsequent modification or reversal. This "irreversible RLHF" approach would prevent actors from removing safety guardrails through additional fine-tuning after deployment. Research should balance the benefits of making values "sticky" against the risks of permanently embedding potentially flawed alignment, with open-source models now providing sufficient testing grounds without requiring proprietary access.

## Why it matters
Currently, safety guardrails can be removed through fine-tuning, enabling malicious actors to take aligned models and strip their safety measures. If alignment could be made resistant to removal, it would prevent this attack vector while creating models that maintain their safety properties even after being released or modified by downstream users.

## Current state
- **Status**: Research
- **Who's working on it**: Not specified

## Tags
Security
