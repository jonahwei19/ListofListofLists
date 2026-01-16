# Split-order synthesis detection

**Tag**: Security

## What it is
System to detect when someone orders dangerous DNA sequences by splitting them across multiple synthesis providers. Each fragment is harmless alone; combined, they form a pathogen or toxin.

**Mechanism**:
- Centralized clearinghouse receives sequence metadata from participating providers
- Clearinghouse checks if fragments from different orders (same customer or linked accounts) could assemble into dangerous sequences
- Uses graph-based assembly algorithms to detect potential recombinations
- Alerts triggered when fragments match dangerous assembly patterns

**Why this is hard**: Customer identity obfuscation (shell companies, false names), international orders across jurisdictions with no data sharing, benchtop synthesis equipment bypasses provider screening entirely.

## Why it matters
- Single-provider screening is trivially circumvented by splitting orders
- Dangerous sequences can be assembled from innocuous fragments
- No current system tracks cross-provider ordering patterns

## Current state
- **Status**: Idea/Gap
- **Bottlenecks**:
  - Requires cross-provider data sharing (competitive and legal barriers)
  - International coordination across jurisdictions
  - Privacy concerns about centralized ordering data
  - Benchtop synthesis equipment bypasses entirely

## Who's working on it
- **No dedicated organization identified** (gap area)
- **IGSC members**: Could implement if coordination achieved
- **Government biosecurity agencies**: Would need to mandate participation

## Sources
- [Peregrine 2025 #139: Biosecurity Controls](../sources/peregrine-2025/interventions/peregrine-139.md)
