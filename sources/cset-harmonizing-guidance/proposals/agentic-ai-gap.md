# Agentic AI Gap

**Maps to interventions**:
- `agent-ids-reputation.md`
- `multi-agent-safety-protocols.md`
- `agent-trace-analysis.md`

## CSET Identified Gap

The report explicitly identifies agentic AI as a gap in existing guidance:

> "Agentic AI: Existing AI-specific guidance almost wholly pertains to LLMs and generative AI. However, with the rapid pace of AI development, organizations need to be forward thinking and therefore guidance must be as well. The automation of workflows using AI agents—AI that can plan and take action in the real world—is likely on the near horizon. For these agents to be useful, they will need to be able to access a variety systems and assets belonging to the organization. Managing that access, maintaining identities for various agents, and tracking their actions across the organization will be critical. This information would be relevant to the Audit Logging, Access Control, and Identity & Authentication topics areas, among others."

## Related Existing Practices (Low AI Scores)

### Identity & Authentication

#### IA-1: Centralized Identity Management
> "Establish a centralized system to issue, manage, verify, revoke, and audit identities and credentials."

**AI Score**: 0%

#### IA-2: Proof and Bind
> "Proof and verify identities. Bind verified identities to authentication credentials. Avoid shared accounts and credentials."

**AI Score**: 0%

### Access Control

#### AC-1: Access Policy
> "Establish a policy that defines rules for access control and a process for administering access uniformly across the organization."

**AI Score**: 0%

#### AC-2: Security Principles
> "Adhere to the principles of least privilege, least functionality, separation of duties, and zero trust in the design and implementation of the access control policy."

**AI Score**: 0%

### Audit Logging

#### LG-1: Audit Process and Scope
> "Define the scope of systems and events to be logged. Establish a process to generate, store, review, and analyze audit logs."

**AI Score**: 19%

#### LG-2: What to Log
> "Log 1) access and modifications to data, software, and systems; 2) privileged actions; 3) other relevant personnel, user, and third-party activity; 4) system inputs and outputs; 5) errors; and 6) security events."

**AI Score**: 38%

## Connection to Existing Interventions

**Agent IDs & Reputation**: The report identifies "maintaining identities for various agents" as critical but notes that IA-1 and IA-2 have 0% AI Scores, meaning no existing guidance addresses AI agent identity management.

**Multi-Agent Safety Protocols**: The report notes agents need "to access a variety systems and assets" and that AC-2's "least privilege, least functionality, separation of duties, and zero trust" principles must apply to agents, but no AI-specific guidance exists.

**Agent Trace Analysis**: LG-2's logging requirements include "system inputs and outputs" which applies to agent actions, but the low AI Score (38%) indicates this isn't developed for AI agents specifically.

## Implications

The 0% AI Scores for identity and access control practices, combined with CSET's explicit identification of agentic AI as a gap, strongly validates interventions focused on:
1. Creating agent identity systems
2. Developing access control frameworks for agents
3. Building logging and tracing infrastructure for agent actions

The report's forward-looking analysis suggests these gaps will become critical as agent deployment increases.
