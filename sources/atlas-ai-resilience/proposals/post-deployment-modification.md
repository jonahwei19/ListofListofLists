# Post-Deployment Model Modification

**Source**: Atlas AI Resilience Gap Map
**URL**: (internal document from Atlas Computing)

## Quoted passage

> gap: Once AI models are accessible (open-source or through theft), adversaries can fine-tune or modify them to remove safety features or enhance dangerous capabilities, and we lack technical methods to make models robustly resistant to such adversarial modification

> claim: unlearning or other methods are critical can isolate and remove dangerous knowledge from the models

> Research program developing robust unlearning techniques, architectural constraints, or cryptographic verification methods that persist under adversarial fine-tuning

> claim: hardware-based model authentication could be implemented to track and identify modified models through robust model fingerprinting and provenance

> This requires both adversarially robust watermarking/fingerprinting techniques that survive fine-tuning, and also requirements that compute systems check some amount of model authenticity

> claim: the models could be made robust to adversarial fine-tuning with sufficiently coherent training around things like values

> A multifaceted research program generating benchmarks, evaluation frameworks, and training to improve the coherence of model values, potentially coupled with a requirement that sufficiently sophisticated AI hardware enables models to delete themselves

## Tags
Security
