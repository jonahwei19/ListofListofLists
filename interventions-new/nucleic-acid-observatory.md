# Large-scale metagenomic sequencing

**Tag**: Security

## What it is
Metagenomic sequencing of environmental samples (wastewater, air, nasal swabs) to detect novel pathogens before clinical cases appear. Unlike targeted PCR tests that look for known pathogens, metagenomic sequencing reads all genetic material in a sample—enabling detection of previously unknown or engineered pathogens. The NAO operates at scale: 270 billion read pairs sequenced in Q1 2025 alone (more than all pre-2025 sequencing combined), analyzing each billion reads for under $10 using AWS Batch.

## Why it matters
- Detects novel pathogens before clinical surveillance can identify them
- Works against unknown threats including engineered pathogens that evade targeted tests
- Provides critical early warning time for response measures—detection in wastewater can precede clinical cases by days to weeks

## Current state
- **Status**: Pilot (operational detection systems) with government scale-up planned
- **Scale**: CASPER system processes samples from 20 cities (as of Oct 2025), generating billions of reads weekly—the largest untargeted wastewater MGS dataset ever assembled
- **Detection sensitivity**: Estimated to detect viral pathogens shedding like flu/SARS-CoV-2 before 1-3% of monitored population infected
- **Government adoption**: President's FY 2026 Budget proposes $52M to CDC for "Biothreat Radar" based on NAO findings—would enable detection before 12 in 100,000 Americans infected
- **Recent progress (2024-2025)**:
  - Genetic engineering detection pipeline operational—detecting HIV-based viral vectors
  - Reference-based growth detection moving to production (second operational method)
  - 270B read pairs sequenced in Q1 2025 (more than all pre-2025 sequencing combined)
  - Nextflow-based pipeline processes 1B reads for <$10
- **Bottlenecks**: False positive management; international coordination for global deployment; integrating with public health response systems

## Who's working on it
- **Nucleic Acid Observatory (SecureBio)**: Primary operator; 9 FTEs across Near-Term Detection and Robust Detection teams; $3.4M Open Philanthropy grant for scale-up
- **CDC**: FY 2026 budget request for $52M Biothreat Radar program based on NAO methods
- **Broad Clinical Labs**: Sequencing partnership using NovaSeq X+ sequencers
- **University of Missouri (Marc Johnson lab)**: Partner sequencing facility
- **University of Miami (Helena Solo-Gabriele lab)**: South Florida sewershed
- **PHC Global**: ANTI-DOTE contract for military/marine wastewater

## Sources
- [Peregrine 2025 #137: Nucleic Acid Observatory](../sources/peregrine-2025/interventions/peregrine-137.md)
- [Apollo Program for Biodefense: Detection](../sources/apollo-biodefense/proposals/detection.md)
- [Concrete Biosecurity Projects: Early Detection Center](../sources/concrete-biosecurity-ea/proposals/early-detection-center.md)
- [Biosecurity Engineers: Biomonitoring Hardware](../sources/biosecurity-engineers/proposals/biomonitoring-hardware.md)
- [Atlas AI Resilience Gap Map: Pathogen Surveillance](../sources/atlas-ai-resilience/proposals/pathogen-surveillance-gap.md)
