# Security Management Practices

**Maps to interventions**:
- `private-industry-security.md`
- `subsidized-security-tools.md`
- `ai-security-expert-training.md`
- `confidential-computing.md`

## Relevant CSET Practices (Security Topics)

### Security Management

#### SM-1: Security and Privacy Program
> "Establish a program to manage security and privacy across the organization. Communicate the strategy, related policies, and responsibilities to personnel. Enforce and regularly evaluate the program's policies."

**AI Score**: 0%

#### SM-4: Encryption and Key Management
> "Employ accepted methods of encryption to secure assets. Manage and protect the creation, distribution, use, storage, and destruction of cryptographic keys."

**AI Score**: 0%

#### SM-5: Security Boundaries
> "Establish physical and logical boundaries at the organization's perimeter and between segregated security domains within the organization. Implement protections at those boundaries."

**AI Score**: 0%

### Design & Development

#### DD-2: Threat Modeling
> "Conduct threat modeling and attack surface mapping as a part of system design. Ensure the development team is aware of the organization's threat landscape."

**AI Score**: 63%

#### DD-3: Secure Design
> "Adopt a secure-by-design approach. Implement security design principles. Assess how the system will interact with other IT infrastructure. Ensure that the design specification is consistent with the organization's security and privacy architecture."

**AI Score**: 30%

#### DD-6: Testing
> "Require developers, internal or external, to conduct static and dynamic application security testing (SAST and DAST). Commission independent assessments to validate testing."

**AI Score**: 39%

### Vulnerabilities

#### VN-1: Reporting Processes
> "Create mechanisms and incentives for internal and external parties to report the existence of bugs and vulnerabilities. Report relevant information about vulnerabilities and patches to stakeholders."

**AI Score**: 51%

#### VN-2: Secure Development
> "Reduce vulnerabilities by following secure software development practices and conducting vulnerability detection. Obtain security assurances from third-party providers. Only use trusted libraries and components."

**AI Score**: 58%

#### VN-5: Patching
> "Patch or otherwise mitigate known vulnerabilities in a timely manner. Proactively fix similar vulnerabilities in other software or systems."

**AI Score**: 21%

## Key Finding: Security Is Underrepresented in AI Guidance

The report explicitly identifies an imbalance:

> "Yet the large imbalance in attention suggests that it would be worth revisiting whether further work may be needed on issues pertaining to AI security and, if so, what barriers have prevented such guidance from being developed."

And notes:
> "AI security is not absent from existing guidance—one of the five focus areas discussed above relates to the novel vulnerabilities in AI systems—yet the large imbalance in attention suggests that it would be worth revisiting whether further work may be needed on issues pertaining to AI security."

## Connection to Existing Interventions

**Private Industry Security Organization**: The low AI Scores (0% for core security management) reveal that security practices are drawn almost entirely from non-AI cybersecurity frameworks. This gap justifies specialized AI security oversight.

**Subsidized Security Tools**: DD-6's requirement for "static and dynamic application security testing" and VN-2's "trusted libraries and components" describe the tooling needs. The report notes smaller organizations lack resources.

**AI Security Expert Training**: DD-2's "ensure the development team is aware of the organization's threat landscape" and the workforce gap identified in the report support training programs.

**Confidential Computing**: SM-4's encryption requirements and SM-5's security boundaries apply to protecting model weights and training data in secure enclaves.

## Gap: AI-Specific Security Guidance

The report observes that existing guidance has "clearly drawn heavily from the AI safety and AI trust communities" while AI security remains underrepresented. This validates interventions focused specifically on AI security infrastructure and expertise.
