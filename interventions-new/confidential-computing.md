# Confidential Computing for AI

**Tag**: Security

## What it is
Processing data in Trusted Execution Environments (TEEs) where it cannot be viewed or altered, applied to AI operations. Components:

- **CPU-based TEEs**: Intel TDX creates cryptographically isolated "trust domains" for each VM; AMD SEV provides similar capabilities
- **GPU confidential computing**: NVIDIA Hopper/Blackwell architectures with Protected PCIe (PPCIE) create encrypted CPU↔GPU channels
- **Remote attestation**: Services verify device/platform integrity before allowing TEE access
- **Confidential AI inference**: Proprietary model weights remain protected even when loaded onto GPUs

TEEs function as "digital vaults installed directly into the CPU and GPU"—integrated into processor packages for minimal overhead.

## Why it matters
- Enables sharing and computation without exposure of sensitive data or model weights
- Creates technical foundations for governance and auditing that don't require trusting all parties
- Allows secure collaboration between organizations with competing interests
- **AI governance enabler**: Can enforce usage policies cryptographically without trusting deployers

## Current state
- **Status**: Pilot → Production (2025 inflection point)
- **Market**: ~$24B in 2025, projected >$350B by 2032 (44-46% CAGR)
- **Recent developments (2025)**:
  - NVIDIA H100 first GPU with native confidential computing support
  - Google Cloud Confidential Space for secure ML model sharing
  - Red Hat Tinfoil project for cloud-native Confidential AI
  - Gartner predicts 60% of enterprises will evaluate TEE by end of 2025
- **Bottlenecks**: Needs standardized toolkits and frameworks for broader adoption; GPU TEE ecosystem still maturing; performance overhead for some workloads

## Who's working on it
- **NVIDIA**: GPU confidential computing (Hopper/Blackwell), Remote Attestation Service
- **Intel**: Trust Domain Extensions (TDX), confidential computing AI whitepaper
- **Google Cloud**: Confidential Space, Confidential Accelerators
- **Red Hat**: Tinfoil project for Confidential AI
- **Chutes**: Commercial confidential AI inference platform
- **Duality Technologies**: Enterprise TEE solutions

## Sources
- [Peregrine 2025 #72: Confidential Computing](../sources/peregrine-2025/interventions/peregrine-072.md)
