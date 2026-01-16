# Defense-in-depth safety layers

**Tag**: Science

## What it is
Multiple layered protective barriers ("Swiss cheese model") for AI systems, where each layer is individually imperfect but collectively provides meaningful deterrence. Two complementary aspects:

**For closed-source models**: Deploy multiple concurrent safeguards—input filtering, output monitoring, rate limiting, user authentication, logging. Acknowledges that determined attackers may succeed but dramatically raises cost of misuse.

**For open models (research)**: Systematic engineering project that takes an open model (e.g., DeepSeek) and implements every known post-training safety technique, measuring how they stack together. Tests against real attacks rather than benchmarks to identify gaps, conflicts, and coverage patterns.

## Why it matters
- No single safety measure is foolproof—layered defenses provide redundancy
- Safety techniques studied in isolation may interact poorly when combined
- Real attack testing reveals vulnerabilities that benchmarks miss
- Maintains usability for legitimate purposes while deterring malicious use

## Current state
- **Status**: Pilot/Deployed (closed models), Research (systematic testing)
- **Recent findings (2025)**:
  - FAR.AI's STACK attack: 71% success rate on catastrophic risk scenarios vs. 0% for conventional attacks—demonstrates layered defenses have exploitable gaps when attacked sequentially
  - Math: 5 layers at 90% effectiveness each = 0.001% breach chance (if independent), but independence assumption often fails
  - Guardrail evaluation (1,445 prompts, 21 attack types): Best model (Qwen3Guard-8B) achieved only 85.3% accuracy; all models degraded on unseen prompts
  - Some attacks (emoji smuggling) achieved 100% evasion across multiple guardrails including Protect AI v2 and Azure Prompt Shield
- **Defense layers in use**: Input screening, output screening, post-hoc human/LLM review, red team bounties, threat intelligence monitoring
- **Bottlenecks**: Layer independence assumption often false; balancing security with usability; no single guardrail outperforms across all attack types

## Who's working on it
- **Anthropic**: Constitutional classifiers for Claude 4 Opus
- **Google DeepMind, OpenAI**: Announced similar layered defense plans
- **FAR.AI**: STACK attack research exposing layered defense vulnerabilities
- **Enterprise guardrail providers**: Protect AI, Azure Prompt Shield, various open-source guardrails

## Sources
- [Peregrine 2025 #161: Defense-in-Depth for Closed Source Models](../sources/peregrine-2025/interventions/peregrine-161.md)
- [Peregrine 2025 #4: Defense-in-Depth Analysis of Post-training](../sources/peregrine-2025/interventions/peregrine-004.md)
