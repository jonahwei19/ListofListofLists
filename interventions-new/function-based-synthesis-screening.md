# Function-based DNA synthesis screening

**Tag**: Security

## What it is
Screening DNA synthesis orders by predicting what the sequence *does*, not just what it *looks like*. Solves the AI-evasion problem where models can redesign toxins to evade homology-based (BLAST) screening while retaining harmful function.

**Mechanism**:
- Sequence submitted to synthesis provider → screened against danger classifiers
- Classifiers trained on dangerous vs benign sequences using protein structure prediction (AlphaFold, ESMFold)
- Pathway analysis checks for biosynthesis of toxins, virulence factors
- Positive hits flagged for human review or rejection

**Key difference from homology screening**: BLAST catches sequences that *look like* known pathogens. Function-based screening catches sequences that *behave like* pathogens, even if they're novel or AI-designed.

## Why it matters
- October 2025 Microsoft paper demonstrated AI-designed toxin variants slipping past global BLAST-based screening while retaining harmful function
- ~80% of gene synthesis capacity is from IGSC members using homology screening (2017)
- Function-based approaches are the only defense against AI-designed evasion sequences

## Current state
- **Status**: Research/Pilot (function-based); Deployed (homology-based)
- **Implementations**:
  - SecureDNA: Free screening with AI-evasion protections
  - IBBIS Common Mechanism: Baseline screening standard
  - Battelle UltraSEQ, FAST-NA: Emerging tools
- **Bottlenecks**: Function prediction accuracy; compute costs; false positive rates

## Who's working on it
- **SecureDNA**: Free screening API with function-based protections
- **IBBIS**: Common Mechanism screening standard
- **Battelle**: UltraSEQ tool development
- **Microsoft**: AI evasion research and patch development

## Sources
- [Peregrine 2025 #139: Biosecurity Controls](../sources/peregrine-2025/interventions/peregrine-139.md)
