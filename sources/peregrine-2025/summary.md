# Peregrine 2025 - Entry Index

**Source**: [The 2025 Peregrine Report](https://riskmitigation.ai/wp-content/uploads/The-2025-Peregrine-Report.pdf)
**Original**: https://riskmitigation.ai/wp-content/uploads/The-2025-Peregrine-Report.pdf

208 source proposals → 4 problem entries + governance interventions

---

## Entries

| Entry | Threat Model | Key Bottlenecks |
|-------|--------------|-----------------|
| [[verify-ai-alignment]] | Can't tell aligned from deceptively-aligned | Behavioral tests gameable, no scalable interpretability |
| [[make-ai-aligned]] | Don't know how to train aligned systems | Training objectives don't capture values, data encodes misalignment |
| [[contain-unsafe-ai]] | Need to prevent harm even without alignment | Capable systems evade controls, no tripwires |
| [[defend-against-ai-harms]] | AI enables bio, cyber, misuse at scale | Dual-use problem, defense harder than offense |

**Note**: "Govern AI development" and "build governance capacity" were dissolved. Governance is not a goal - it's an intervention pattern. Specific governance mechanisms are redistributed as interventions under the problems they serve.

---

## Tiling Rationale

Split by what we need to achieve:
1. **Verify** - know if AI is aligned
2. **Build** - make AI aligned
3. **Contain** - prevent harm if we can't verify/build
4. **Defend** - mitigate AI-enabled harms (bio, cyber, misuse)

Governance mechanisms (compute thresholds, international coordination, whistleblower protection, etc.) are interventions serving these goals, not goals themselves. Each governance intervention needs an explicit theory of change connecting it to one of these entries.

---

## Proposal → Entry Mapping

### Domain 1: Technical AI Alignment (#1-41)
Most proposals are interventions under **verify-ai-alignment** or **make-ai-aligned**.

| Proposal | Maps to |
|----------|---------|
| #1 Training Data Attribution | [[make-ai-aligned]] (also: [[defend-against-ai-harms]]) |
| #2-5 Agent Trace, Task Decomp, Defense-in-Depth, CoT Fidelity | [[verify-ai-alignment]] |
| #6-7 Human Labeling, Tamper-Resistant RLHF | [[make-ai-aligned]] |
| #8-11 Probabilistic Programming, Safety by Design, Scientist AI, Theoretical | [[make-ai-aligned]] (alternative paradigms) |
| #12-18 Cooperative Alignment, Debate, Constitutional AI, etc. | [[make-ai-aligned]] |
| #19-23 Unlearning, Low-Stakes, Control Systems, etc. | [[contain-unsafe-ai]] |
| #24-27 Distillation Limits, Misalignment Measures, Scalable Oversight | [[verify-ai-alignment]] |
| #28-37 Meta-approaches (synthesis, academia-industry, etc.) | [[build-governance-capacity]] |
| #38-41 Interpretability | [[verify-ai-alignment]] |

### Domain 2: Evaluation & Auditing (#42-64)
Almost all map to **verify-ai-alignment**.

| Proposal | Maps to |
|----------|---------|
| #42-48 Holistic evals | [[verify-ai-alignment]] |
| #49-51 Misuse evals, Red teaming | [[defend-against-ai-harms]] |
| #52-56 Benchmarks, frameworks | [[verify-ai-alignment]] |
| #57-64 Auditing, RSPs, accountability | [[govern-ai-development]] |

### Domain 3: Intelligence Gathering (#65-86)
Most map to **govern-ai-development**.

| Proposal | Maps to |
|----------|---------|
| #65-69 Hardware monitoring, OSINT | [[govern-ai-development]] |
| #70-74 AI development monitoring | [[govern-ai-development]] |
| #75-78 Threat detection | [[contain-unsafe-ai]] |
| #79-86 Security intelligence, research | [[govern-ai-development]] |

### Domain 4: Governance & Policy (#87-114)
All map to **govern-ai-development**.

### Domain 5: International Coordination (#115-133)
All map to **govern-ai-development**.

### Domain 6: Preparedness & Response (#134-175)
Most map to **defend-against-ai-harms**.

| Proposal | Maps to |
|----------|---------|
| #134-143 Bio risk | [[defend-against-ai-harms]] |
| #144-148 Democratic/societal resilience | [[build-governance-capacity]] |
| #149-154 Economic transition | [[build-governance-capacity]] |
| #155-158 Crisis response | [[defend-against-ai-harms]] |
| #159-175 Cybersecurity | [[defend-against-ai-harms]] |

### Domain 7: Public Communication (#176-187)
All map to **build-governance-capacity**.

### Domain 8: Miscellaneous (#188-208)
Mixed:

| Proposal | Maps to |
|----------|---------|
| #188-189 Legal clarity, whistleblower | [[build-governance-capacity]] |
| #190-191 Alignment tax, neuroscience moonshots | [[make-ai-aligned]] |
| #192 Access standards | [[verify-ai-alignment]] |
| #193-196 Democratic support, kinetic actuators, nanotech, golden period | [[build-governance-capacity]] |
| #197-202 Cooperative AI, game theory | [[govern-ai-development]] |
| #203-208 Ethics, personhood, sentience, wellbeing | [[build-governance-capacity]] or VAGUE |

---

## Vague Proposals (need triage)

- #16 Complex Objective Functions: Too abstract, no specific failure mode
- #203-208: Philosophical territory, unclear if actionable

---

## Next Steps

1. Within each entry, map proposals to specific bottlenecks
2. Research to fill gaps (who's working on what, status)
3. Expand cross-problem links (interventions serving multiple entries)
4. Log remaining vague proposals with reasons
