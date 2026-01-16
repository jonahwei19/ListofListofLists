# Model Safeguards Practices

**Maps to interventions**:
- `classified-red-teaming.md`
- `defense-in-depth-closed-models.md`
- `training-data-anti-poisoning.md`
- `capability-unlearning.md`

## Relevant CSET Practices (Model Safeguards Topic)

### SG-1: Fail-safes
> "Develop systems to identify and handle out-of-distribution input, low-confidence predictions, and high uncertainty situations in which failures are likely to occur. Employ fail-safes such as deferring to a human-in-the-loop."

**AI Score**: 100%

### SG-2: Mitigating Data Risks
> "Use trusted data labeling and data sources for model training. Assess datasets for potential bias, data quality issues, and signs of poisoning or tampering. Employ training techniques, such as using adversarial examples, to improve model robustness."

**AI Score**: 100%

### SG-3: Model Security
> "Protect models against security threats including adversarial, poisoning, out-of-distribution, model inversion, membership inference, and model extraction attacks. Harden access points, such as application programming interfaces (APIs), and scrutinize inputs and outputs for anomalies."

**AI Score**: 100%

### SG-4: Evaluating Performance
> "Analyze system performance for model degradation, data drift, anomalous behavior, and emergent capabilities. Track key metrics and establish regular benchmarking. Systematically review and report results."

**AI Score**: 100%

### SG-5: Model Supply Chain
> "Source assets that are used in the development of AI systems (e.g., data, libraries, software, hardware, pretrained models) from verified and trustworthy sources. Document sources using bill of materials (BOM) or model cards."

**AI Score**: 100%

### SG-6: Continual Learning
> "Deploy safeguards to sanitize new data used by AI systems for continual learning. Scrutinize changes in model behavior as these systems can be more susceptible to poisoning and adversarial attacks."

**AI Score**: 100%

## Connection to Existing Interventions

**Classified Red Teaming**: SG-3's comprehensive list of attack vectors (adversarial, poisoning, model inversion, membership inference, model extraction) outlines exactly what classified red teaming should assess. The report notes these as "new vulnerabilities" that AI introduces.

**Defense in Depth**: SG-1 and SG-3 together support layered defenses. SG-1's fail-safes and SG-3's hardened access points represent multiple defensive layers.

**Training Data Anti-Poisoning**: SG-2 directly addresses this: "Assess datasets for potential bias, data quality issues, and signs of poisoning or tampering." SG-6 extends this to continual learning systems.

**Capability Unlearning**: SG-4's monitoring for "emergent capabilities" relates to identifying dangerous capabilities that may need to be removed.

## Key Quote on AI Security Focus

From the report's Insights section:
> "In addition to the vulnerabilities found in traditional software, AI systems introduce new attack vectors that adversaries can exploit. These systems are vulnerable to confidentiality attacks that extract information about the model (model theft or distillation) and the underlying training data (model inversion or membership inference). These systems can also be subject to integrity attacks that manipulate the behavior of the model to produce an adversary's desired output. These attacks include data poisoning, backdoors, adversarial input, and jailbreaking."
