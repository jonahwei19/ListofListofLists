# Classified Red Teaming

**Tag**: Security

## What it is
Red teaming of AI systems in classified environments to assess true offensive potential for CBRN threats that cannot be tested publicly due to information hazards. Components:

- **Government-led evaluation**: National laboratories and agencies with appropriate clearances test models against classified threat scenarios
- **Cross-sector coordination**: Industry shares insights on risk identification/mitigation; government adapts to classified domains
- **Compartmentalized testing**: Results and methodologies protected to prevent proliferation of attack vectors
- **Pre-deployment assessment**: Testing before public release to understand national security-relevant capabilities

## Why it matters
- **Public evaluation limits**: Open red-teaming cannot test truly dangerous scenarios (nuclear weapons details, classified bioweapon designs) without creating information hazards
- **Risk underestimation**: Without classified testing, public evaluations may systematically underestimate actual misuse potential
- **Dual-use model categorization**: Anthropic and OpenAI both classified 2025 models in their highest CBRN-related risk categories; classified testing validates these assessments
- **Escalating capabilities**: Labs expect upcoming models to reach even higher risk levels—classified testing must scale accordingly

## Current state
- **Status**: Pilot (first partnerships operational)
- **Recent developments (2025)**:
  - Anthropic-NNSA partnership: First-of-its-kind—Claude evaluated in classified environment for nuclear/radiological knowledge by DOE's National Nuclear Security Administration
  - US AISI and UK AISI conducted pre-deployment testing of Claude 3.7 Sonnet under voluntary agreements
  - NIST AI 800-1 draft guidance on dual-use foundation model red-teaming
  - Berkeley Risk and Security Lab AI Red-Teaming Bootcamp (instructors from national labs, government, industry)
  - Enkrypt AI found 81.7% persona-based attack success rate, some models provided dangerous CBRN info 83% of time when directly asked
- **Bottlenecks**: Security clearances; coordination across government/industry boundary; information compartmentalization; scaling to match model release pace

## Who's working on it
- **NNSA/DOE**: Classified nuclear/radiological evaluation of Claude
- **US AI Safety Institute (NIST)**: Red-teaming guidance, pre-deployment testing agreements
- **UK AI Security Institute**: Pre-deployment model testing
- **Anthropic**: First industry partner for classified CBRN testing
- **Berkeley Risk and Security Lab**: Red-Teaming Bootcamp with Open Philanthropy support
- **Johns Hopkins Center for Health Security**: NIST guidance input on biosecurity
- **National laboratories**: Los Alamos, Sandia, Lawrence Livermore (CBRN domain expertise)

## Sources
- [Peregrine 2025 #53: Classified Red Teaming](../sources/peregrine-2025/interventions/peregrine-053.md)
