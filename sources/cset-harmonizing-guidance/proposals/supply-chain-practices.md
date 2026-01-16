# Supply Chain Practices

**Maps to interventions**:
- `compute-supply-chain-coordination.md`
- `global-hardware-verification.md`
- `training-data-licensing.md`
- `training-data-attribution.md`

## Relevant CSET Practices (Supply Chain Topic)

### SC-1: Managing and Coordinating
> "Manage relationships with suppliers. Establish procedures to acquire, use, manage, and exit third-party services. Coordinate roles and responsibilities between the organization and suppliers."

**AI Score**: 26%

### SC-2: Mapping the Supply Chain
> "Map the third-party products, components, and services that the organization depends on throughout the supply chain. Identify suppliers and alternative suppliers, prioritizing by criticality."

**AI Score**: 47%

### SC-3: Risks and Risk Management
> "Incorporate supply chain risks into enterprise risks management. Ensure third-party risks are included as a part of risk identification, assessment, and treatment activities."

**AI Score**: 39%

### SC-4: Supply Chain Security
> "Raise awareness and improve the resilience of supply chain security. Ensure the organization meets its own security responsibilities as a supplier and consumer. Require the same of its suppliers."

**AI Score**: 58%

### SC-5: Procurement Plans and Due Diligence
> "Establish procurement plans to evaluate and select services from a range of options. Vet potential suppliers and conduct due diligence prior to acquisition. Collect evidence that suppliers and services meet the organization's standards."

**AI Score**: 39%

### SC-6: Contracts and Requirements
> "Establish contractual obligations that require third-parties to implement specified security, privacy, risk management, audit, and compliance practices. Include provisions to verify those obligations are met."

**AI Score**: 20%

### SC-7: Monitoring and Assessment
> "Assess the practices of third-party organizations and their continued ability to comply with the terms of their contract. Continuously monitor third-party services and products for changes, deviations, or failures in meeting obligations."

**AI Score**: 17%

## Model Supply Chain (from Model Safeguards)

### SG-5: Model Supply Chain
> "Source assets that are used in the development of AI systems (e.g., data, libraries, software, hardware, pretrained models) from verified and trustworthy sources. Document sources using bill of materials (BOM) or model cards."

**AI Score**: 100%

## Connection to Existing Interventions

**Compute Supply Chain Coordination**: SC-2's "map the third-party products, components, and services" and SC-4's supply chain security apply to compute infrastructure. The report notes supply chain sits "at the intersection of Privacy, Security and Governance categories."

**Global Hardware Verification**: SC-5's "due diligence prior to acquisition" and SC-7's "continuously monitor third-party services and products" apply to hardware verification. SG-5's "verified and trustworthy sources" is specifically AI-focused.

**Training Data Licensing**: SC-6's "contractual obligations" and the data-specific aspects of SG-5 apply to data provenance. The report notes supply chain guidance "incorporates recommendations related to the data supply chain, often the focus of privacy concerns."

**Training Data Attribution**: SG-5's "document sources using bill of materials (BOM) or model cards" directly supports attribution requirements.

## Key Insight on Supply Chain Position

The report observes:
> "At the intersection of Security and Safety we find the Model Safeguards cluster... Finally, between the Privacy, Security and Governance categories we find the Supply Chain cluster. This topic incorporates recommendations related to the data supply chain, often the focus of privacy concerns, and the software and hardware supply chain, which typically falls under the cybersecurity domain."

This positioning shows supply chain practices must integrate across multiple domains. The moderate AI Scores (17-58% for general SC, but 100% for SG-5) indicate AI-specific supply chain guidance focuses on model-specific assets while broader supply chain management draws from traditional practices.
