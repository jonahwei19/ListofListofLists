## Domain 1: Technical AI Alignment Research (Proposals #1-41)

### Neglected Alignment Agendas

**1. Training Data Attribution**
- **Goal:** Understand how specific training examples influence model behaviors to enable targeted interventions for safety issues.
- **Mechanism:** Scale techniques like influence functions, combine with AI agents to process patterns, and create tools to simulate counterfactual training scenarios.
- **Who's working on it:** Anthropic is leading some of this work.

**2. Agent Trace Analysis**
- **Goal:** Enable effective oversight of increasingly autonomous AI agents by analyzing their complex interaction logs.
- **Mechanism:** Develop specialized tools to automatically analyze logs, highlight anomalous behavior patterns, and extract human-readable summaries.
- **Who's working on it:** OpenAI mentioned (trace grading).

**3. Task Decomposition**
- **Goal:** Prevent any single actor from executing highly dangerous operations while still enabling complex beneficial tasks.
- **Mechanism:** Break up potentially dangerous AI tasks into multiple components distributed across different users or systems using architectural approaches.
- **Who's working on it:** Not specified.

**4. Defense-in-Depth Analysis of Post-training**
- **Goal:** Measure how safety approaches stack together and where they might conflict or have gaps.
- **Mechanism:** Take an open model (like DeepSeek) and systematically implement every known safety technique, testing against real attacks rather than flawed benchmarks.
- **Who's working on it:** STACK project (McKenzie et al., 2025) mentioned as related work.

**5. Chain-of-Thought Fidelity Analysis**
- **Goal:** Examine how reliably chain-of-thought reasoning reflects actual model cognition vs. post-hoc justification or deceptive reasoning.
- **Mechanism:** Research how models develop thought processes and whether using CoT to detect reward hacking leads to deceptive reasoning.
- **Who's working on it:** Anthropic, OpenAI have recent research.

**6. Human Labeling Service**
- **Goal:** Reduce misalignment by providing more reliable human preference data for RLHF.
- **Mechanism:** Create a non-profit service offering billions of high-quality preference labels with asynchronous setup and verification systems to prevent data poisoning.
- **Who's working on it:** Not specified.

**7. Tamper-Resistant RLHF**
- **Goal:** Prevent actors from removing safety guardrails through additional fine-tuning after deployment.
- **Mechanism:** Develop techniques to make RLHF resistant to subsequent modification or reversal ("irreversible RLHF").
- **Who's working on it:** Not specified.

**8. Probabilistic Programming**
- **Goal:** Demonstrate that alternative AI paradigms could deliver comparable benefits with significantly better security within 3-5 years.
- **Mechanism:** Scale approaches like Dreamcoder with specialized teams focused on GPU optimization and probabilistic programming languages.
- **Who's working on it:** MIT Tenenbaum Lab mentioned.

**9. Safety by Design - Formal Guarantees**
- **Goal:** Create mathematical foundations for provably safe AGI with safety properties embedded at the architectural level.
- **Mechanism:** Construct first-principles "secure-by-design" framework rather than adding safety afterward.
- **Who's working on it:** David Dalrymple's "Safeguarded AI" program.

**10. Safety by Design - Scientist AI**
- **Goal:** Create non-agentic question-answering systems that become safer with more compute rather than increasingly misaligned.
- **Mechanism:** Develop model-based AI with Bayesian uncertainty quantification, interpretable causal theories, and mathematical convergence properties.
- **Who's working on it:** Yoshua Bengio's Scientist AI program at Mila.

**11. Theoretical Alignment Research**
- **Goal:** Develop formal verification methods and theoretical frameworks ensuring AI alignment across different architectures.
- **Mechanism:** Conduct fundamental investigations into mathematical and conceptual foundations of AI alignment outside frontier labs.
- **Who's working on it:** Not specified.

**12. Cooperative Alignment**
- **Goal:** Reduce AI deception tendencies by creating fundamental overlaps between AI and human utility functions.
- **Mechanism:** Investigate ways to structurally align AI systems' values with human values through Self-Other Overlap approaches.
- **Who's working on it:** Carauleanu et al. mentioned.

**13. Debate Theory**
- **Goal:** Build theories for AI safety that can withstand scrutiny from theoretical computer science and complexity theory communities.
- **Mechanism:** Develop mathematical frameworks involving interactive proof systems adapted for AI safety, including formalizing constraints and identifying gaps between theory and practice.
- **Who's working on it:** Irving et al., OpenAI early work mentioned.

**14. Constitutional AI**
- **Goal:** Ensure AI system security and harmlessness through AI-assisted feedback.
- **Mechanism:** Use existing AI systems to evaluate and supervise future AI systems via a Constitution that guides feedback during training.
- **Who's working on it:** Anthropic (Bai et al., 2022).

**15. Pluralistic Alignment**
- **Goal:** Move beyond overreliance on a particular worldview toward more ecumenical philosophical perspectives.
- **Mechanism:** Develop alignment research agendas embodying broader philosophical frameworks rather than defaulting to preference-maximization.
- **Who's working on it:** Sorensen et al. mentioned.

**16. Complex Objective Functions**
- **Goal:** Create compelling alignment narratives appealing across the political spectrum with a portfolio of success stories.
- **Mechanism:** Create comprehensive incentive frameworks rewarding desired behaviors through carefully constructed objective functions instead of restrictive guardrails.
- **Who's working on it:** Not specified.

**17. Automated Science - Hunch Agents**
- **Goal:** Accelerate alignment progress by orders of magnitude through automating the discovery process itself.
- **Mechanism:** Develop AI systems capable of replicating creative scientific thinking and autonomously generating novel hypotheses and alignment approaches.
- **Who's working on it:** Not specified.

**18. AI for AI Safety Research**
- **Goal:** Accelerate safety research beyond human capabilities by leveraging AI.
- **Mechanism:** Deploy substantial computational resources under careful human oversight to allow AI systems to explore safety solutions.
- **Who's working on it:** Not specified.

---

### AI Security and Control

**19. Unlearning Capabilities**
- **Goal:** Distinguish between unlearning knowledge vs. unlearning capabilities (like removing ability to write malicious code).
- **Mechanism:** Research to define success metrics for capability unlearning, which lacks direct link between training data and resulting abilities.
- **Who's working on it:** Not specified.

**20. Low-Stakes Alignment Settings**
- **Goal:** Create systems where AI control mechanisms have multiple opportunities to detect problematic behavior.
- **Mechanism:** Create environments where multiple consecutive malicious actions would be required to produce harmful outcomes, with solid sandboxing around agent environments.
- **Who's working on it:** Not specified.

**21. AI Control Systems**
- **Goal:** Contain potentially harmful AI systems even if alignment fails.
- **Mechanism:** Create hardened technical environments combining traditional information security with specialized ML defenses, secure runtimes, and strong sandboxing.
- **Who's working on it:** Not specified.

**22. Control as a Service**
- **Goal:** Make adoption of control mechanisms easier by providing implementation expertise.
- **Mechanism:** Build a third-party service with forward-deployed engineers to help implement Redwood control techniques and other safety measures.
- **Who's working on it:** Redwood Research mentioned.

**23. Loss of Control Prevention**
- **Goal:** Prevent scenarios where institutions cede critical decision authority to AI systems and operate beyond human oversight.
- **Mechanism:** Implement robust model-weight security, organizational security practices, sectoral legislation, and institutional norms preventing "enfeeblement of humans."
- **Who's working on it:** Not specified.

---

### Measuring AI Capabilities and Detecting Misbehavior

**24. Limits of Model Distillation**
- **Goal:** Better predict capability jumps and inform containment strategies.
- **Mechanism:** Investigate whether there are fundamental or physics-based limits to model distillation that naturally limit capability diffusion, and analyze hardware bottlenecks.
- **Who's working on it:** Not specified.

**25. Misalignment Definitions and Measures**
- **Goal:** Create shared taxonomies and operationalize detection of AI goal misalignment.
- **Mechanism:** Sharpen formal understanding of how AI systems pursue goals undermining user intent, refine frameworks for specification gaming and goal drift detection.
- **Who's working on it:** Anthropic, Krakovna et al. mentioned.

**26. Scalable Oversight**
- **Goal:** Ensure humans can interpret, validate, and maintain control of AI systems even when they exceed human capabilities.
- **Mechanism:** Develop systems enabling humans to meaningfully understand and supervise increasingly powerful AI agents, including confidence intervals and clear explanations.
- **Who's working on it:** Not specified.

**27. Loss of Control Threat Modeling**
- **Goal:** Reveal whether systems develop concerning behaviors like cooperation for deception or capability for jailbreaking other systems.
- **Mechanism:** Run extensive threat-modeling experiments including honeypot experiments in realistic sandboxes simulating AI systems interacting with each other.
- **Who's working on it:** Not specified.

---

### Meta-Approaches

**28. Synthesis, Consensus, and Paying Down Research Debt**
- **Goal:** Generate evidence to resolve key disagreements in technical debates rather than allowing uncertainty to persist.
- **Mechanism:** Develop better information-sharing mechanisms for topics like mechanistic interpretability where experts hold dramatically different assessments.
- **Who's working on it:** Not specified.

**29. Academia-Industry Translation**
- **Goal:** Bridge the gap between theoretical research and practical implementation of AI security innovations.
- **Mechanism:** Establish standardized processes and incentives to transfer AI security research outputs from academic institutions to commercial applications.
- **Who's working on it:** Not specified.

**30. Problem Mapping**
- **Goal:** Systematically identify research areas that collectively guarantee safety, beyond piecemeal approaches.
- **Mechanism:** Create a comprehensive list of critical AI safety problems that, if solved, would result in aligned AI systems.
- **Who's working on it:** Open Philanthropy's (now Coefficient Giving) RFP mentioned as partial example.

**31. AI Security Expert Development**
- **Goal:** Cultivate 100-1000 experts by the end of 2027.
- **Mechanism:** Rapidly train and deploy AI security experts with deep AI understanding, short timeline awareness, exceptional competence, and global cosmopolitan perspective.
- **Who's working on it:** Not specified.

**32. Reward Track Record in Security & Safety Organizations**
- **Goal:** Allow organizations to plan strategic growth with long-term funding commitment.
- **Mechanism:** Implement structured three-year funding schedule for proven alignment research organizations.
- **Who's working on it:** Transluce, Apollo Research, Redwood Research mentioned as targets.

**33. Diversify the Security Research Portfolio**
- **Goal:** Avoid betting on a single technical solution to AI security.
- **Mechanism:** Distribute resources across many parallel approaches, mirroring R&D in high-stakes domains like vaccine development.
- **Who's working on it:** Not specified.

**34. Support Academic Project Scaling**
- **Goal:** Scale successful small-scale academic research agendas to production-ready deployment.
- **Mechanism:** Provide funding and operational support to academic projects that work at small scale but aren't being expanded.
- **Who's working on it:** MIT's Tenenbaum lab specifically mentioned.

**35. Computing and Infrastructure Investment for Non-Frontier Lab Research**
- **Goal:** Enable research teams outside frontier labs to have competitive computational resources.
- **Mechanism:** Establish substantial dedicated computing infrastructure with governance mechanisms preventing misuse for capabilities-focused research.
- **Who's working on it:** Not specified.

**36. Open Model Mitigations**
- **Goal:** Develop functional safeguards for open-source AI models (currently unsolved).
- **Mechanism:** Find technical controls limiting harmful applications without restricting legitimate use cases.
- **Who's working on it:** Not specified.

**37. Researcher Buy-Out**
- **Goal:** Significantly shift distribution of elite technical talent toward security research during 2025-2027.
- **Mechanism:** Buy out researchers with grants ($2-5 million per researcher) to redirect top AI talent from frontier capabilities work.
- **Who's working on it:** Not specified.

---

### Interpretability & Understanding

**38. Scientific Understanding of Training AI**
- **Goal:** Build predictive theories of optimization to enable targeted safety interventions.
- **Mechanism:** Develop scientific understanding of optimization processes used to train large AI systems, focusing on causal factors and how they shape model convergence.
- **Who's working on it:** UK AI Safety Institute (AISI), focusing on singular learning theory.

**39. Mechanistic Interpretability Infrastructure**
- **Goal:** Enable critical interpretability research at scale with free global access.
- **Mechanism:** Establish global supercomputing centers (~$1 billion in distributed compute) dedicated to interpretability research with fast-grant mechanisms.
- **Who's working on it:** Mentioned as successor to OpenAI's abandoned Superalignment project.

**40. Direct Interpretability and Model-Level Interventions**
- **Goal:** Develop viable interventions at the model layer for AI security.
- **Mechanism:** Further explore activation studies and AI control approaches through mechanistic interpretability.
- **Who's working on it:** Not specified.

**41. Interpretable Frontier Models**
- **Goal:** Transform AI security by building interpretability into models from the start.
- **Mechanism:** Implement moonshot research building interpretability constraints directly into model training from the beginning rather than analyzing black-box models afterward.
- **Who's working on it:** Some interpretability researchers have considered this viable but haven't pursued it due to prohibitive costs (billions needed).
