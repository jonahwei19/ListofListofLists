# Resilience & Recovery Practices

**Maps to interventions**:
- `ai-catastrophe-backup-plans.md`
- `attack-scenario-wargaming.md`
- `loss-of-control-threat-modeling.md`

## Relevant CSET Practices (Resilience & Recovery Topic)

### RR-1: Resilience and Continuity Program
> "Establish a business continuity strategy that prioritizes the critical function of the organization. Define resilience objectives and requirements."

**AI Score**: 17%

### RR-2: Resilience and Recovery Plans
> "Develop a business continuity and disaster recovery plan based on an analysis of potential threats, failures, and impacts. Regularly update the recovery plan and incorporate lessons learned."

**AI Score**: 5%

### RR-3: Dependencies and Third Parties
> "Identify the organization's essential function and its dependencies, particularly those related to suppliers. Coordinate and test response plans with those third parties."

**AI Score**: 24%

### RR-5: Backups
> "Create redundant copies of data and system configurations and store in a secure alternative location. Regularly test the backup process, the integrity of backups, and the restoration process."

**AI Score**: 10%

### RR-6: Resilience Mechanisms
> "Implement resilience mechanisms including redundancy (systems, services, equipment, etc.), fail-safes, failovers, load balancing, hot swapping, and alternative operating locations."

**AI Score**: 11%

### RR-8: Drills, Exercises, and Testing
> "Regularly test resilience mechanisms and recovery plans using automated testing, table-top exercises, realistic drills, and red teams. Ensure personnel have proficiency and proper training to conduct recovery activities."

**AI Score**: 19%

### RR-9: Restoration and Recovery Execution
> "Execute recovery plans to contain and mitigate events. Employ resilience mechanisms to ensure the continuity of critical functions. Restore systems and data, verifying their integrity."

**AI Score**: 15%

## Connection to Existing Interventions

**AI Catastrophe Backup Plans**: RR-1's "business continuity strategy that prioritizes the critical function" and RR-2's "disaster recovery plan based on an analysis of potential threats" apply to catastrophic AI scenarios. The very low AI Scores (5-24%) indicate this area lacks AI-specific guidance.

**Attack Scenario Wargaming**: RR-8 explicitly calls for "table-top exercises, realistic drills, and red teams" to test recovery plans. This directly supports wargaming interventions.

**Loss of Control Threat Modeling**: RR-2's "analysis of potential threats, failures, and impacts" and RR-3's identification of "dependencies" apply to understanding loss-of-control scenarios.

## Very Low AI Scores Indicate Gap

The Resilience & Recovery topic has among the lowest AI Scores in the entire framework (5-24%). This indicates:
1. Existing resilience/recovery guidance comes almost entirely from traditional business continuity and disaster recovery frameworks
2. There is minimal AI-specific guidance for catastrophic AI scenarios
3. Organizations adapting these practices to AI risks are doing so without established best practices

The report notes:
> "Our analysis is not exhaustive, so existing guidance relative to these areas may exist elsewhere. However, the relative absence of guidance on these topics in the reports we examined is nonetheless concerning given the central role they have played in policy discussions."

This validates interventions focused specifically on AI catastrophe planning and recovery.

## Key Gap

While RR-8's "red teams" mention relates to testing recovery plans, there is no specific guidance for:
- Recovery from AI system failures at scale
- Restoration after AI-enabled attacks
- Continuity planning for AI-dependent critical infrastructure
- Scenarios where AI systems themselves are the threat vector
