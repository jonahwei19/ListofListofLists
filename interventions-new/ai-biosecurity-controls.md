# AI biosecurity controls

**Tag**: Security

## What it is
Implement strong controls over biological data and DNA synthesis that could enable harmful applications. Multiple complementary approaches:

**AI model controls**: Training models to exclude dangerous biological information, filtering queries for biology-related red flags, implementing Know Your Customer (KYC) guidelines. Full-specification biology-capable models available only to licensed institutions.

**DNA synthesis screening**: Screening orders at synthesis providers before fulfillment. Moving beyond homology-based (BLAST) screening to function-based approaches that assess whether sequences "do dangerous things, regardless of sequence similarity."

**Function-based approaches**: Protein function prediction (AlphaFold, ESMFold), danger classifiers trained on dangerous vs. benign sequences, pathway analysis for biosynthesis of toxins/virulence factors.

## Why it matters
- AI models trained on biological data could provide detailed instructions for creating dangerous pathogens
- October 2025 Microsoft/Science paper: AI protein design tools can redesign toxins to evade BLAST-based screening while retaining harmful function
- Homology-based screening has fundamental limits against AI-designed sequences
- Only ~80% of global gene synthesis capacity is produced by IGSC members (2017 estimate)

## Current state
- **Status**: Deployed (synthesis screening), Research (function-based approaches)
- **Recent developments (2025)**:
  - Microsoft demonstrated AI-designed toxin variants slipping past global synthesis screening
  - Patches deployed globally catch ~97% of AI-designed evasion attempts, but gaps remain
  - May 2025 Trump EO created regulatory uncertainty—90-day deadline for new framework passed without announcement
  - Function-based screening tools emerging: IBBIS Common Mechanism, Battelle UltraSEQ, FAST-NA, SecureDNA Random Adversarial Thresholds
- **Bottlenecks**: Function prediction accuracy; international coordination; regulatory uncertainty; benchtop synthesis equipment bypasses provider screening

## Who's working on it
- **SecureDNA**: Free screening for sequences 30+ nucleotides with AI-evasion protections
- **IGSC (International Gene Synthesis Consortium)**: Industry screening standards
- **IBBIS (International Biosecurity and Biosafety Initiative for Science)**: Common Mechanism baseline screening
- **Battelle**: UltraSEQ screening tool
- **Microsoft**: AI evasion research and patch development

## Sources
- [Peregrine 2025 #139: Biosecurity Controls](../sources/peregrine-2025/interventions/peregrine-139.md)
- [Atlas AI Resilience Gap Map: Biological Threat Creation](../sources/atlas-ai-resilience/proposals/biological-threat-creation.md)
