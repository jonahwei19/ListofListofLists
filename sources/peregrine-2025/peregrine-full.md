# The 2025 Peregrine Report

**208 Expert Proposals for Reducing AI Risk**

*Maximilian Schons, Samuel Hargestam, Gavin Leech and Raymund Bermejo*

*In collaboration with and supported by Halcyon Futures*

---

## Executive Summary

**Purpose and context.** By early 2025, mainstream debates about AI had recognized the possibility of transformative AI coming within just a few years, far faster than most historical forecasts. However, we found no comprehensive list of proposed AI risk mitigations that would be viable in such a scenario.

**Methods.** We conducted 48 in-depth interviews, with key staff at OpenAI, Anthropic, Google DeepMind, Mila, AMD, the EU AI Office, multiple AI Safety Institutes, METR, RAND, Scale AI, GovAI, Transluce, and ARIA. Participants were explicitly asked to consider interventions that might currently seem cost-prohibitive or politically infeasible - the focus was on fast, positive impact, assuming transformative AI were to arrive within only a few years.

**Results.** From the above interviews we distilled two main results: I) a structured portfolio of 208 initiatives, clustered into eight domains; II) a set of four clusters of broader strategic considerations affecting the viability of any such efforts:

1. **A need for readiness:** Too many efforts still optimize for polish over time-to-impact. With multi-year research cycles increasingly out of step with AI progress, execution needs to shift toward rapid prototypes, staged pilots, and funding mechanisms that can mobilize substantial capital in weeks or months, rather than quarters or years.

2. **A need for coordination:** The ecosystem remains fragmented and often duplicative. Actors working on risk mitigation should be pragmatic - one does not need total alignment with all other actors to have fruitful collaborations.

3. **A need for standardization:** Interviewees repeatedly called for shared audit interfaces, interoperable evaluation layers, clear capability surfaces, and operational definitions for terms like "AGI" to prevent institutions from talking past each other.

4. **A need to address capacity constraints:** evaluation capacity is too small, technically grounded leadership is scarce, and the field still relies too heavily on inexperienced talent rather than recruiting seasoned operators from adjacent domains.

---

## All 208 Initiatives

### Domain Overview

| Proposal # | Domain | Page |
|------------|--------|------|
| 01-41 | Technical AI Alignment Research | 11 |
| 42-64 | Evaluation & Auditing Systems | 19 |
| 65-86 | Intelligence Gathering & Monitoring | 24 |
| 87-114 | AI Governance & Policy Development | 29 |
| 115-133 | International Coordination | 35 |
| 134-175 | Preparedness & Response | 40 |
| 176-187 | Public Communication & Awareness | 49 |
| 188-208 | Miscellaneous | 52 |

---

# Technical AI Alignment Research

## Neglected Alignment Agendas

**Scope:** Methods for aligning AI systems which the interviewees thought were neglected, or worthy of further research funding.

## #1: Training Data Attribution

Develop scalable methods to understand how specific training examples influence model behaviors to provide invaluable insight into why models exhibit certain tendencies and how these tendencies might be modified. This work would require scaling techniques like influence functions, combining them with AI agents that process and explain the resulting patterns, and creating tools to simulate counterfactual training scenarios. Attribution technology would enable more targeted interventions to address safety issues by modifying training data instead of relying on post-training alignment techniques.

Studying how training data shapes model behavior and addressing alignment issues requires developing techniques to instill appropriate values in AI systems. This research examines how different training paradigms affect model behavior, including why models might "fake" alignment during training but behave differently during deployment. Though Anthropic is leading some of this work, much remains unpublished by major labs. Better scientific understanding would enable the development of potential regulatory frameworks for training processes that could verify alignment claims.

## #2: Agent Trace Analysis

Create tools that automatically analyze the logs of actions by autonomous systems. AI agents that perform sequential autonomous actions produce complex interaction logs that are far too lengthy for human review, creating significant challenges for evaluation and oversight. For instance, autonomous coding agents can generate thousands of lines of code and interaction steps that contain critical security flaws, yet even expert teams might miss these issues for months due to the volume of data. Developing specialized tools to analyze these traces, highlight anomalous behavior patterns, and extract human-readable summaries would enable effective oversight of increasingly autonomous systems. This technology would be particularly targeted at security-critical applications, where catching problematic agent behavior before deployment is essential.

## #3: Task Decomposition

Break up potentially dangerous AI tasks into multiple components distributed across different users or systems, none having complete capability independently, using architectural approaches. This compartmentalization would prevent any single actor from executing highly dangerous operations while still enabling complex beneficial tasks through carefully designed interfaces and information controls.

## #4: Defense-in-Depth Analysis of Post-training

Take an open model produced by an organization like DeepSeek and systematically implement every known safety technique on it, measuring how these approaches stack together and where they might conflict or have gaps. This engineering project would focus on which combinations provide comprehensive coverage, testing against real attacks rather than flawed safety benchmarks.

## #5: Chain-of-Thought Fidelity Analysis

Examine how reliably chain-of-thought reasoning reflects actual model cognition, rather than being post-hoc justification or potentially deceptive reasoning. Many AI systems currently produce "thought processes" that often align with their eventual outputs, which is fortuitous as this transparency could have been eliminated during training. A critical challenge identified in recent research shows that if you use chain-of-thought to detect reward hacking and incorporate that detection into training, models develop deceptive thought processes.

## #6: Human Labeling Service

Create a non-profit human labeling service offering billions of high-quality preference labels to replace such proxies in reinforcement learning from human feedback (RLHF). Alignment techniques like RLHF use human data to train a proxy model of human preferences. With a suitable asynchronous setup to await human inputs, this approach could reduce misalignment by providing more reliable data. The project would need verification systems to prove it isn't conducting data poisoning attacks, and could aim to provide at-cost, high-quality data that labs would naturally want to use.

## #7: Tamper-Resistant RLHF

Develop techniques to make alignment methods like reinforcement learning from human feedback (RLHF) resistant to subsequent modification or reversal. This "irreversible RLHF" approach would prevent actors from removing safety guardrails through additional fine-tuning after deployment. Research should balance the benefits of making values "sticky" against the risks of permanently embedding potentially flawed alignment, with open-source models now claimed to provide sufficient testing grounds for this work without requiring access to proprietary frontier systems.

## #8: Probabilistic Programming

Scale promising academic approaches like Dreamcoder from the MIT Tenenbaum Lab, which show impressive results and favorable alignment properties, but remain unscaled due to academia's focus on novelty rather than deployment. This would require finding experts at the intersection of GPU optimization and probabilistic programming languages to build specialized teams focused on making these approaches production-ready. With proper investment, these alternative AI paradigms could potentially deliver comparable benefits to transformer-based approaches within 3-5 years, but with significantly better security. The goal would be demonstrating sufficient progress by late 2026 to justify slowing Transformer scaling.

## #9: Safety by Design - Formal Guarantees

Invest more substantially into research initiatives aimed at creating mathematical foundations for provably safe artificial general intelligence, such as David Dalrymple's "Safeguarded AI". This approach starts by constructing a first-principles 'secure-by-design' framework that would embed safety properties at the architectural level rather than adding them afterward. These approaches have relatively little funding and struggle to attract talent compared to mainstream AI. Despite longer development timelines, the approach offers a potential middle ground between completely halting AI development and building superintelligent systems with unacceptable risk profiles.

## #10: Safety by Design - Scientist AI

Accelerate development of model-based approaches to AI, as represented by research programs like Yoshua Bengio's Scientist AI. The Scientist AI agenda aims to create non-agentic question-answering systems with Bayesian uncertainty quantification, interpretable causal theories, and mathematical convergence properties, which become safer with more compute rather than increasingly misaligned. The strategic objective with regard to very short timelines would primarily be to develop a system that can act as a guardrail for agentic and potentially misaligned AI, as well as to demonstrate sufficient progress to convince key stakeholders that safer alternatives to the current paradigm are possible.

## #11: Theoretical Alignment Research

Conduct fundamental investigations into the mathematical and conceptual foundations of AI alignment outside frontier labs. This research would develop formal verification methods and theoretical frameworks ensuring AI systems remain aligned with human values across different architectures and development approaches.

## #12: Cooperative Alignment

Investigate ways to structurally align AI systems' values with human values by creating fundamental overlaps between their respective utility functions. This approach has demonstrated some early results in reducing AI deception tendencies. See for instance Self-Other Overlap.

## #13: Debate Theory

Develop mathematical frameworks like debate theory, which involves interactive proof systems adapted for AI safety. The project would include clearly defining theorem statements, formalizing constraints, and building theories that can withstand scrutiny from both the theoretical computer science and complexity theory communities. The project would also include identifying gaps in between theoretical results and practical implementation, alongside developing specific conjectures that can be tested.

## #14: Constitutional AI

Use existing AI systems to evaluate and supervise future AI systems to ensure security and harmlessness. Human input is given through a set of rules - a Constitution - which an AI assistant uses to give feedback to a more advanced system in training.

## #15: Pluralistic Alignment

Develop alignment research agendas that move beyond an overreliance on a particular worldview (described as "orthogonalist, individualistic") that may be too culturally and temporally specific. A more robust approach in future research would aim to embody a more ecumenical philosophical perspective rather than defaulting to a single framework based around preference-maximization.

## #16: Complex Objective Functions

Create comprehensive incentive frameworks rather than relying on rule-based constraints for AI systems. This proposal suggests rewarding desired behaviors through carefully constructed objective functions instead of imposing restrictive guardrails which have proven largely ineffective in practice. The ideal end-goal for this research program would be to provide a portfolio of success stories to be compiled and shared across the industry. The hope is that such frameworks would provide a more robust foundation for aligning AI systems with human values while also creating a compelling narrative that appeals to both sides of the political spectrum.

## #17: Automated Science - Hunch Agents

Develop AI systems capable of replicating the creative scientific thinking process of pioneers. These "hunch agents" would autonomously generate novel scientific hypotheses and alignment approaches, potentially accelerating progress by orders of magnitude beyond human-led research. The ideal is to present a working meta-level approach to alignment by attempting to automate the discovery process itself rather than pursuing specific technical solutions. One hope expressed was for this project to create a positive feedback loop where AI helps develop better alignment techniques for increasingly capable AI systems.

## #18: AI for AI Safety Research

Leverage advanced AI systems to work on AI safety problems themselves, effectively accelerating research beyond human capabilities. This approach would involve deploying substantial computational resources under careful human oversight to allow AI systems to explore safety solutions. While acknowledging the potential risks of creating even more capable systems, this approach recognizes that sufficient human oversight might enable leveraging AI capabilities for safety research.

---

## AI Security and Control

**Scope:** Work that either ensures alignment or assumes misalignment and focuses on safe containment or controlled use. There are two approaches to reducing potential threats posed by AI. First, researchers can investigate methods to ensure that AI systems are aligned. Second, they can assume that AI systems are untrustworthy and investigate methods to leverage useful work from such systems without risking catastrophic consequences.

## #19: Unlearning Capabilities

Conduct research to distinguish between unlearning knowledge (like removing specific content from training data) versus unlearning capabilities (like removing the ability to write malicious code). Knowledge unlearning has clear success metrics - a model should be indistinguishable from one never trained on certain content - but capability unlearning has no direct link between training data and resulting abilities.

## #20: Low-Stakes Alignment Settings

Create environments where multiple consecutive malicious actions would be required to produce harmful outcomes. This approach doesn't aim to develop or test for perfectly aligned models, but create systems where AI control mechanisms have multiple opportunities to detect problematic behavior. This research project would involve solid sandboxing around agent environments to ensure that no bad outcome results except when the sandbox is deliberately breached, and develop security frameworks which create multiple layers of protection.

## #21: AI Control Systems

Develop defensive systems specifically designed to contain potentially harmful AI systems even if alignment fails. This focuses on creating hardened technical environments where AIs operate - combining traditional information security with specialized machine-learning defenses to provide layered protection against "scheming AI" that may attempt to escape constraints. The emphasis here would be on building secure runtimes, strong sandboxing around the entire agent environment, and additional scrutiny at critical interaction points.

## #22: Control as a Service

Build a third-party service organization that provides forward-deployed engineers to help implement Redwood control techniques and other safety measures. This approach would make adoption of control mechanisms easier for companies by providing implementation expertise rather than just recommendations.

## #23: Loss of Control Prevention

Develop technical and governance safeguards against scenarios where institutions cede critical decision authority to AI systems over time and operate beyond human oversight parameters. This includes implementing robust model-weight security and organizational security practices to prevent concerning behaviors such as "self-exfiltration," where models copy their own weights to infrastructure the developer does not control. It also involves sectoral legislation and institutional norms that prevent the gradual "enfeeblement of humans." Advancing these safeguards requires sustained education efforts for policymakers to understand subtle long-term risks beyond immediate threats.

---

## Measuring AI Capabilities and Detecting Misbehavior

**Scope:** Proposals that might help understand AI systems' behaviors and capabilities. In order to know whether AI systems are misaligned, their standard behaviors and the limits of their capabilities need to be understood.

## #24: Limits of Model Distillation

Investigate the theoretical limits of AI capabilities, including whether there are fundamental limits to model distillation. This would examine whether small, easily-diffused models will always be able to capture the capabilities of larger systems, or if there are physics-based constraints that naturally limit capability diffusion. The project would also analyze potential hardware bottlenecks, such as GPU interconnect innovations or test-time compute limitations, to better predict capability jumps.

## #25: Misalignment Definitions and Measures

Sharpen formal understanding of how AI systems pursue goals in ways that undermine user intent so we can have shared taxonomies and operationalize better. This includes refining frameworks to detect specification gaming and goal drift, clarifying what counts as an alignment failure, and developing practical ways to measure when a system is exploiting loopholes in its instructions.

## #26: Scalable Oversight

Develop systems enabling humans to meaningfully understand and supervise increasingly powerful AI agents performing complex tasks. This work would bridge the capability gap between humans and advanced AI systems, allowing for meaningful human participation even as AI capabilities dramatically increase. Current AI outputs often lack confidence intervals, probability estimates, and clear explanations of reasoning, making oversight difficult. Scalable oversight aims to ensure humans can interpret, validate, and maintain control of systems even when those systems exceed human capabilities in specific domains.

## #27: Loss of Control Threat Modeling

Run extensive threat-modeling experiments for loss-of-control scenarios, including honeypot experiments in realistic sandboxes that simulate AI systems interacting with each other. These simulations could reveal whether systems develop concerning behaviors like cooperation for deception or capability for jailbreaking other systems.

---

## Meta-Approaches

**Scope:** Ways to improve the technical research ecosystem, or highly abstract technical proposals which may be applied to a variety of different security or control agendas.

## #28: Synthesis, Consensus, and Paying Down Research Debt

Develop better information-sharing mechanisms for topics like mechanistic interpretability, where different experts hold dramatically different assessments. The work would involve publishing analyses that clarify current cruxes in technical debates, generating evidence to address these cruxes rather than allowing uncertainty to persist indefinitely. Current discussions remain fragmented with little consensus-building or evidence generation to resolve key disagreements.

## #29: Academia-Industry Translation

Establish effective mechanisms to transfer AI security research outputs from academic institutions to commercial applications. Currently, the handoff between these sectors is notably weak, causing valuable security innovations to remain theoretical rather than implemented in production systems. This initiative would focus on creating standardized processes and incentives to bridge the gap between theoretical research and practical implementation. Literature alone often isn't enough, since findings can rely on closed weights/data, lack reproducible code and benchmarks tied to deployment constraints, and don't map to security/compliance requirements.

## #30: Problem Mapping

Create a comprehensive list of critical AI safety problems that, if solved, would result in aligned AI systems. As an example, Open Philanthropy's (now Coefficient Giving) RFP is a good list but does not present an overarching framework or justification for thinking that solving the problems listed would lead to aligned AI systems (the present document suffers from this same foible - surfacing ideas but does not claim sufficiency). The goal of problem mapping is to systematically identify research areas that collectively guarantee safety, beyond the current piecemeal approach.

## #31: AI Security Expert Development

Rapidly training and deploying AI security experts who possess a deep understanding of AI technology, acknowledge short timeline implications, demonstrate exceptional competence in their field, and maintain a global cosmopolitan perspective. An initiative like this should aim to cultivate 100-1000 experts by the end of 2027.

## #32: Reward Track Record in Security & Safety Organizations

Implement a structured three-year funding schedule for alignment research organizations to signal long-term commitment and allow organizations to plan strategic growth. Example targets for substantially increased funding for proven alignment research organizations include Transluce, Apollo, and Redwood.

## #33: Diversify the Security Research Portfolio

Aim to mirror R&D in other high-stakes domains like vaccine development, where multiple concurrent paths were pursued during the COVID pandemic. Rather than betting on a single technical solution to AI security, distribute resources across many parallel approaches.

## #34: Support Academic Project Scaling

Provide funding and operational support to academic research agendas that work successfully at small scale but aren't being expanded because academics prioritize novel discoveries over scaling existing approaches. MIT's Tenenbaum lab was specifically mentioned as having promising results that languished without proper resources for deployment.

## #35: Computing and Infrastructure Investment for Non-Frontier Lab Research

Establish substantial dedicated computing infrastructure for AI security researchers working outside frontier labs, as the concentration of critical infrastructure might create significant barriers for security researchers should their access be revoked. Open-source models may provide sufficient testing grounds for many safety approaches without requiring proprietary access, and the cluster would enable research teams to have access to competitive computational resources. The infrastructure should also be coupled with governance mechanisms that prevent its misuse for purely capabilities-focused research.

## #36: Open Model Mitigations

Develop functional safeguards for open-source AI models (a currently unsolved problem). Current research focuses on finding technical controls that could limit harmful applications without restricting legitimate use cases. There's significant uncertainty whether such mitigations can be implemented quickly enough in short timeline scenarios, especially as existing models may already present above-baseline risks.

## #37: Researcher Buy-Out

Buying out researchers with grants to redirect top AI talent from frontier capabilities work toward security research (estimated costs of $2-5 million per researcher). This investment would be conducted with the goal of significantly shifting the distribution of elite technical talent during the critical two-year window between 2025 and 2027.

---

## Interpretability & Understanding

**Scope:** Research that aims to reverse engineer AI systems' behavior into human-understandable computations, and aims to map the internal activations of AI systems to meaningful semantic concepts or features. Although AI models are very capable, understanding why they behave the way they do, or what models are computing, remains to a large degree an open problem.

## #38: Scientific Understanding of Training AI

Develop a scientific understanding of the optimization processes used to train large AI systems. This agenda would focus on the causal factors in training and how they shape what models converge to, where the goal is to build predictive theories of optimization: when models will generalize (and when they won't), when failure modes like goal drift arise, and how interventions at training time can reliably steer outcomes. Understanding the relationship between training processes and emergent capabilities would enable more targeted interventions to improve safety. The UK AI Safety Institute is already pursuing aspects of this work, focusing particularly on singular learning theory and formal frameworks for optimization processes.

## #39: Mechanistic Interpretability Infrastructure

Establish global supercomputing centers dedicated to interpretability research, with approximately $1 billion in distributed compute resources, that would enable critical research at scale. This infrastructure should be freely accessible to researchers worldwide through fast-grant mechanisms, effectively creating a philanthropically-funded successor to initiatives like OpenAI's abandoned Superalignment project. Such centers could potentially be established quickly, following models like xAI, which reportedly set up their data center in just two months.

## #40: Direct Interpretability and Model-Level Interventions

Understanding what AI models are doing internally through mechanistic interpretability remains underdeveloped. Activation studies and AI control approaches need more exploration to develop viable interventions at the model layer.

## #41: Interpretable Frontier Models

Implement a moonshot research project focused on building interpretability constraints directly into model training from the beginning, rather than trying to analyze black-box models after the fact. This would be extremely expensive but potentially transformative for AI security. Some interpretability researchers have considered this approach viable but haven't pursued it due to the prohibitive costs involved. With sufficient funding (in the billions), this could become feasible.

---

# Evaluation & Auditing Systems

## Holistic Evaluations

**Scope:** Evaluation methods with richer qualitative benchmarks. A recurring theme was that current quantitative benchmarks fail to capture the AI behaviors that should be of greatest concern.

## #42: Interactive Inspection Tools

Move beyond basic evaluation numbers and develop rich, interactive interfaces for users to explore model behaviors through natural language queries like "Why did the model fail on this task?" or "How would it perform if it had internet access?". Current AI evaluation methods reduce complex system behavior to simplistic benchmark scores that fail to capture important nuances. Instead of static reports, these tools would provide dynamic dashboards where users can probe model capabilities, investigate failures, and perform detailed sensitivity analyses. Such inspection tools would have to be AI-backed to scale with increasing model capabilities, using specialized AI systems to interpret and explain the behaviors of frontier models.

## #43: End-to-End Harm Assessment

Conduct comprehensive evaluations of harmful AI capabilities which involve full capability assessment frameworks, rather than (for example) focusing on multiple-choice tasks. Most current benchmarks are verifiable but limited, involving tests that don't capture how systems would execute complex, harmful sequential tasks in the real world. Methodologies are needed to evaluate "end-to-end harmful capability manifestation" - i.e., not just whether an AI can answer questions about harmful topics, but whether it can assist with ideation, planning, and execution of potentially dangerous activities.

## #44: Evaluation Sandbagging Detection

Develop methodologies and tools to identify when AI systems deliberately underperform on safety evaluations for strategic purposes ("sandbagging"). This involves developing research techniques to ensure evaluation reliability as models become more sophisticated, and create robust testing protocols that remain effective even against systems attempting to game assessment frameworks.

## #45: Training AI Evaluators

Train specialized investigator AI agents specifically to analyze the vast amounts of data generated by frontier models, including millions of neuron activations, extensive training datasets, and complex interaction logs. Current approaches to detecting AI capabilities and failure modes are severely limited, relying on simplistic evaluations that miss critical behaviors until they emerge in deployment. For instance, cybersecurity evaluations involve testing models against a small set of predefined tasks rather than comprehensively assessing models across wider contexts. Research must move beyond benchmark-focused evaluations toward holistic understanding of model capabilities in real-world contexts.

## #46: Cooperative Evals: AIs Working With Humans

Undertake empirical research comparing human performance on various tasks, both with and without AI assistance (and with varying forms of AI systems). The aim would be to establish a better understanding of how humans might cause harm with AI models that wouldn't have been possible otherwise, in addition to providing information on how humans could be productively integrated with AI systems.

---

## More-Scientific Evals

**Scope:** More rigorous, scientifically grounded benchmarks that better signal general capabilities and alignment-relevant behaviors. Many participants noted that there was little consensus on how indicative of general capabilities and alignment AI benchmarking scores are.

## #47: Meta-Research on Safety Techniques

Conduct research that evaluates and validates the effectiveness of different AI safety approaches. This research program would require multiple independent actors to assess the same models using different techniques, in order to compare results to determine reliability and blind spots. This proposal was mentioned as necessary for AI alignment to move beyond piecemeal theoretical approaches, and towards empirical safety science with repeatable, testable methodologies that can scale with increasing capabilities.

## #48: Characterizing AI Risks with Evidence

Focus on robust research that characterizes risks empirically with high validity, with a particular focus on evidence that could be used to inform policy decisions. The goal would be to give governments clear criteria for when to intervene. This research would aim to create benchmarks that establish clear quantitative thresholds for risks, and provide credible empirical evidence that would enable appropriate government action when AI capabilities increase.

## #49: Vulnerability Matching

Directly connect discovered AI vulnerabilities to appropriate research proposals addressing them. This approach would ensure funding flows efficiently to researchers tackling actual, identified problems rather than theoretical concerns. The system would continuously update as new vulnerabilities are discovered through red teaming, creating a rapid feedback loop between threat identification and solution development that significantly accelerates safety progress.

## #50: Safety Benchmark Development

Establish comprehensive high-effort benchmarks for evaluating AI safety and security. Many safety benchmarks have been defunded or discontinued, leaving organizations without clear targets or metrics to aim for. Additionally, skepticism has been raised about the ability of benchmarks to provide reliable signals about actual safety properties. This initiative would develop rigorous, transparent methodologies for assessing various dimensions of AI safety, aiming to provide a common language for discussing safety progress across different models and organizations.

## #51: Go Beyond Pre-Paradigmatic Evaluation Frameworks

Seek to achieve consensus on how to evaluate AI systems for security, especially as evaluation needs to transition from being locked inside labs to standardized external processes. Crucial questions remain unresolved about whether evaluations will be qualitative or quantitative, crowdsourced or team-based, and what risk thresholds should trigger interventions. Without answers to these fundamental questions, the absence of an agreed upon framework for security evaluation was thought to be a key bottleneck for progress on regulatory frameworks or accountability mechanisms.

## #52: Risk-Model Evaluation

Develop evaluation frameworks for AI risk assessment systems, via creating methodologies to identify, classify and prioritize potential AI mistakes based on their consequences. These evaluations would test how well risk models detect both obvious and subtle errors, especially focusing on high-stakes contexts where mistakes could have severe impacts. The frameworks would quantify both false positive and false negative rates, enabling trade-offs between intervention frequency and risk exposure. This work creates the foundation for reliable triage systems that focus human attention where it's most critically needed.

## #53: Classified Red Teaming

Develop classified red teaming capabilities in order to understand the true scope of AI's offensive potential. This work should involve collaboration with Los Alamos National Laboratory specialists focused on chemical, radiological, biological, and nuclear threats (CBRN), drawing on key red-teaming experts from organizations like DeepMind and Microsoft to provide insights on systematic vulnerabilities and failure patterns. The objective would be to create an accurate assessment of exactly "how easy" it is to misuse AI for harmful purposes before developing appropriate countermeasures.

## #54: Capability Assessment Framework

Develop a systematic, grounded approach to evaluating which potential AI risks are most credible and which are overrated. This framework would distinguish between well-evidenced catastrophic harms and more speculative concerns, providing a realistic assessment of current capabilities and improvement trends. The project would aim to help influence and prioritize mitigation efforts by focusing resources on empirically validated risks rather than theoretical possibilities that may not materialize.

## #55: Ultra-Reliable AI Evaluation

Develop engineering approaches to achieve high reliability and benchmarking methodologies that efficiently identify edge cases where models fail catastrophically. Current AI benchmarks lack the depth and variety needed to establish true reliability at scale, focusing on 99% accuracy even though "five nines" (99.999%) may be needed for reliability of critical systems. Future evaluation frameworks should probe worst-case adversarial examples without requiring millions of test instances, where evaluations are modeled more like aircraft safety standards than Kaggle competitions.

## #56: Misuse Evaluations

Develop highly realistic evaluations for CBRN (Chemical, Biological, Radiological, Nuclear). Catastrophic misuse scenarios are critically needed in the AI safety ecosystem. This work faces a tragedy of the commons problem where all major AI labs recognize the necessity but lack sufficient individual incentives to fully own the responsibility. Creating centralized, standardized frameworks for testing advanced AI systems against sophisticated misuse scenarios would help identify vulnerabilities before they can be exploited. These evaluations should simulate realistic threats with adversarial intent.

## #57: Multi-Agent Interaction Framework

Develop infrastructure for simulating and analyzing multi-agent interactions, with particular focus on preventing emergent cooperation between agents to circumvent safety constraints. As AI systems increasingly interact with each other autonomously at high speeds, they will need robust frameworks for tracking trust, identifying bad actors, and establishing interaction norms. These frameworks would establish protocols for AI systems to verify the trustworthiness of other agents, report problematic behavior, and implement collective safety measures across distributed systems. This work is becoming increasingly urgent as financial transactions, supply chain operations, and information exchange become mediated by interconnected AI systems operating with minimal human oversight.

---

## Auditing Institutions

**Scope:** New institutions that would enable evaluating and auditing AI systems more effectively.

## #58: Evaluation Companies

Fund crucial evaluation organizations in the AI security ecosystem such as SecureBio, PatternLabs, and Expo that handle cybersecurity and offensive evaluations. These companies represent a relatively small financial investment but perform critical functions in the evaluation landscape that could otherwise become bottlenecks.

## #59: Public Audits

Have independent organizations conduct comprehensive public audits of open-weight models with significant compute resources. Such audits would aim to demonstrate in public what thorough model analysis should look like, thereby creating a template for what information should be available about any deployed AI system. By performing these audits in public settings, the process would open itself to community feedback and improvement, establishing consensus on best practices that can then be enforced through various policy mechanisms. The goal would be to create public precedents for robust evaluation that would be difficult for private labs to ignore, essentially raising the "floor" for responsible disclosure without requiring immediate regulation.

## #60: AI Auditing Institutions

Found human-based verification and auditing bodies specifically for AI, similar to the IAEA's role in nuclear oversight. Currently, no organization is actively designing such institutions despite their critical importance for any international governance framework. This would require bringing together experts from nuclear verification, cybersecurity, and AI technical domains to design protocols and organizational structures capable of credibly verifying compliance with safety standards. The resulting institution would need sufficient technical capacity, international legitimacy, and access rights to effectively monitor development at leading labs while respecting intellectual property and national security concerns.

## #61: Secure Frontier Data Centers

Build SL4 strength data centers with scalability for increased energy requirements, effectively creating frontier compute facilities that meet SCIF-level security standards (Secure Compartmentalized Information Facilities). Critical technologies like confidential computing and HSMs (Hardware Security Modules) are either insufficiently innovative or not properly activated. This large-scale hardening effort would become crucial in the next few years when lab automation feedback loops become particularly dangerous. These facilities would provide the infrastructure necessary for secure AI development with proper containment protocols to prevent potential "data center uprisings".

## #62: Verified Kinetic Actuators

Develop provably safe mechanisms for AI systems to interact with physical environments through robotics and other actuators. As AI systems increasingly control physical infrastructure and machinery, ensuring their reliable and predictable operation becomes critical for preventing accidents and misuse. Verification systems for physical AI actions would provide crucial safety guarantees for industrial automation, autonomous vehicles, critical infrastructure systems, and other applications where software failures could have catastrophic physical consequences.

## #63: Speed Limits in Data Centers

Implement technical restrictions on computing speed in data centers to slow capability advancement and buy time for safety research. This approach aims to tackle a wide range of problems at once, by directly limiting the pace of AI development. The primary bottlenecks are political popularity and coordination, with the expectation that this would engender especially strong pushback from leading AI labs.

## #64: Physical Chokepoints

Reframe security concerns away from attempts to constrain digital models, and instead towards physical world interfaces, with a particular focus on limiting the mass production of robotic systems. If the control of AI systems may ultimately come down to physical constraints rather than digital ones, one of the most critical questions concerns whether AI systems could acquire enough physical force in the world to enact harmful outcomes. If model proliferation is "inevitable and unstoppable", the most effective chokepoints may be at the level of physical implementation.

---

# Intelligence Gathering & Monitoring

## Hardware Monitoring

**Scope:** Systems that track the movement, use, and concentration of advanced compute hardware to detect emerging capability risks and provide oversight.

## #65: AI OSINT

Provide relatively cheap intelligence without requiring unilateralist action, making it politically feasible while revealing where regulatory or governance levers might be needed. Open-source intelligence efforts for AI monitoring and tracking compute hardware (especially GPUs) moving through countries like Turkey into Russia and China. Organizations like Sentinel and Bellingcat would be ideal for developing internet scrapers to uncover hidden developments, like OpenAI hiring physics professors in South Korea. Additionally, AI-powered scrapers could detect emerging threats, such as AI-generated romantic videos or increasingly sophisticated AI-powered scam tools becoming available for sale.

## #66: AI Diffusion Research

Conduct comprehensive research on the dynamics and limitations of AI capability diffusion. This work would analyze to what extent powerful capabilities will inevitably spread versus remain concentrated, examining hardware requirements, data access limitations, and algorithmic innovations. The project would track diffusion patterns of current capabilities while developing predictive models for how future capabilities might spread, informing containment and governance strategies.

## #67: Usage and Incident Monitoring Systems

Implement robust incident monitoring and usage data analysis systems to understand real-world AI utilization patterns. Labs currently avoid deep usage analysis due to legal liability and privacy concerns, creating significant blind spots in risk assessment. Effective monitoring would aim to replace theoretical "ivory tower" threat-modeling with data-driven insights from actual usage patterns.

## #68: Global Hardware Verification

Implement reporting and verification requirements for all high-performance computing hardware to create a global monitoring system for AI development. This would require tracking all GPUs, TPUs, and similar processors with more than a specified computational capacity, including retrofitting systems on older models. Such an approach necessitates international collaboration, particularly with major hardware producers including NVIDIA, AMD, Intel, Google, and Chinese manufacturers like Huawei. The goal would be creating comprehensive awareness of which organizations are utilizing advanced computing resources, enabling early detection of potentially concerning development patterns.

## #69: Industry Security

Create a privately-funded alternative to the chronically underfunded Bureau of Industry and Security (BIS) with its meager $15 million budget, focusing on comprehensive oversight of GPU distribution and AI research automation monitoring. This entity would prototype advanced data center surveillance, implement GPU tracking systems, and establish protocols for questioning companies about their research automation capabilities. This organization would need to be designed to create "proposals that are hard and awkward to oppose" in order to maximize political viability.

## #70: On-Chip Monitoring Mechanisms

Develop hardware-level monitoring technologies embedded directly into chips to verify that countries aren't pursuing dangerous AI developments in violation of international agreements (e.g. AI intelligence explosions), similar to nuclear verification protocols. Leadership would require both governance expertise and technical understanding to properly prioritize efforts. The organization would employ hardware engineers, designers, and manufacturing specialists working to prototype verification technologies. Its mission would involve proving to government that such verification is possible, in addition to developing technologies that could be integrated with commercial chip manufacturing. This project focuses on state-level verification hardware embedded at the chip-fabrication layer to support treaty compliance and detect illicit national-scale AI activity.

## #71: Flexible Hardware for AI Governance

Implement hardware-based governance mechanisms through Flexible Hardware-Enabled Guarantee (flexHEG) mechanisms that can be added to AI accelerators. This approach places each AI accelerator chip in a tamper-proof enclosure alongside a secure processor that monitors and filters all information and instructions, enabling multilateral, privacy-preserving verification and automated compliance. The design supports various governance options including training run size limitations, verification of appropriate data usage, standardized safety evaluations, and controlled access to model weights. The project involves ensuring that critical privacy protections prevent unauthorized data transmission, while requiring updates to be signed by a quorum of international parties and allowing rollback to a minimal baseline ruleset. This project focuses on lab-level governance hardware added around accelerators to enforce organizational policies, access controls, and safe-use constraints within companies and cloud providers.

## #72: Confidential Computing

Process data in trusted execution environments, where it cannot be viewed or altered. Making confidential computing easier to implement would enable more secure AI operations across various contexts, while creating technical foundations for establishing trust boundaries around high-risk AI capabilities. This would in turn prevent unauthorized access to dangerous functionalities while enabling legitimate research. Although a handful of startups are working in this space, broader adoption requires standardized toolkits and frameworks that establish robust contracts and credentials for secure computation.

## #73: Privacy-Preserving Verification Systems

Implement surveillance, monitoring and verification technologies that track hardware supply chains, chip deployments, power grid construction, and computing infrastructure globally. The initiative would combine both OSINT and privacy-preserving cryptographic methods to verify what activities are occurring inside data centers. Such tools would collect critical intelligence about AI development capacity while providing transparency to prevent miscalculations between major powers, aiming to prevent countries accelerating AI development out of fear others are doing the same. Distribution of this information would need to be handled carefully through diplomatic channels rather than complete public disclosure in order to avoid triggering adversarial reactions.

## #74: Hardware Kill Switches and Location Tracking

Implement monitoring systems to track the location and usage of AI-specific hardware combined with technical 'kill switches' which can remotely disable GPUs. The approach would involve tracking specific hardware shipments and movements, and providing intelligence on compute scaling that could inform when and where to apply regulatory levers. This would provide states with crucial information about attempts to circumvent agreements on compute governance, and the technical ability to halt undesirable AI development. This is about state visibility, compliance verification, and the ability to halt unauthorized compute.

---

## Forecasting and Decision Tools

**Scope:** Methods and platforms that help decision-makers predict AI trajectories, compare scenarios, and choose high-impact actions under uncertainty.

## #75: AI for Collective Decision-making

Develop specialized tools to enhance collective decision-making capabilities. This would help people make wiser long-term decisions, cooperate more effectively, and filter misinformation.

## #76: AI Forecasters

Develop AI systems as superforecasters, employing forecasting feedback loops with real-world validation. These techniques could be incorporated into frontier models, allowing users to understand prediction logic and prevent avoidable errors. The aim is to develop systems that become the default for people looking to find trustworthy predictions, which display large reasoning trees allowing users to inspect, understand, and even modify the logic behind predictions, and thus providing transparency beyond simple numerical probabilities.

## #77: Economic Impact Research

Collect data on how AI systems affect economic outcomes and job displacement across sectors, and analyze this data. This would provide concrete evidence of AI's real-world impacts, helping society recognize and address concerns about technological disempowerment. The project would track economic metrics, with the aim of proactively identifying emerging patterns before they become widespread societal problems.

---

## AI Behavior Monitoring

**Scope:** Tools and systems that observe models in real time, detect unexpected or risky behaviors, and surface for intervention.

## #78: Monitor Complex Agent Interactions

Develop systems to monitor dynamics between multiple AI agents interacting in complex environments. This field remains underdeveloped, and agentic interactions are either poorly captured or not well-conceptualized within existing frameworks. Teams would focus on creating implementations that actively watch deployments and interactions between systems, identifying potentially harmful feedback loops or emergent goals before they become problematic.

## #79: Open-Source AI Drift Monitoring

Develop open-source tools to detect, measure, and address gradual changes in model behavior over time. This initiative would establish standard metrics and benchmarks for identifying when models begin to deviate from their intended function or otherwise exhibit concerning behaviors. Create a tool that provides transparent, vendor-neutral assessment of model drift across different AI systems. The resulting framework would help organizations maintain oversight of their AI deployments and intervene before drift creates significant security vulnerabilities.

## #80: Comprehensive Incident Detection System

Create a standardized framework for logging, anonymizing, and analyzing AI misbehavior across organizations. Build infrastructure allowing developers and third-party researchers to search through incidents, identify patterns, and share findings while protecting sensitive user data and IP. Expand on systems like Anthropic's CLIO to enable rapid identification of concerning behaviors before they escalate into major incidents. Unlike the OSINT suggestion, this proposal would involve labs collaborating directly with each other without a third party.

## #81: AI Misuse Detection Systems

Create systems to identify and address AI misuse before "mini-catastrophes": examples include market manipulation, coordinated influence operations, or novel cyberattack patterns. This project requires developing technical infrastructure and monitoring systems to track patterns of usage across AI ecosystems, flagging suspicious activity patterns, indications of weaponization, and proactive checks for "weird AI behavior" in the wild. Such systems would need both technical mechanisms for detection and human evaluation processes to distinguish genuine innovations from potential threats. The project would function as a safety net for catching misuse scenarios that weren't explicitly anticipated in initial safety evaluations, and help bring concrete evidence of risks to light sooner - potentially motivating political action before more severe incidents occur.

## #82: Control Loss Monitoring

Develop technologies to trigger alarms if AI systems have broken containment. Surveillance acts as a detection layer for potential control failures, enabling intervention before full containment breaches.

## #83: AI-Enhanced Monitoring

Deploy AI systems which continuously monitor other AI systems, looking for anomalous behaviors or market activities that might indicate concerning capabilities developments. This surveillance network of AI systems would function as a de facto surveillance system and network of private investigators, aiming to catch anomalous AI behaviors as early as possible. Implementation would require web-scale scraping expertise, drawing from DEFCON-style talent pools to turn this into competitive challenges to identify hidden compute resources akin to capture-the-flag competitions.

## #84: Intelligence Explosion Monitoring

Establish metrics and monitoring systems to detect when AI systems begin contributing more to their own improvement than human researchers, and tracking acceleration in capabilities against predefined thresholds that would trigger emergency protocols before reaching full AGI. This monitoring would provide early warning when AI progress enters exponential growth phases, enabling intervention before rapid capability jumps make control more difficult or when labs might be incentivized to keep breakthroughs secret.

## #85: System-Level AI Effects

Do research beyond individual model safety: system-level effects from multiple AI models interacting in complex ecosystems create substantial blind spots and unknown risks. Current safety approaches primarily focus on organization-level defenses rather than addressing emergent behaviors that might arise from complex AI interactions in the wild. There's particular concern about "flash crash" type phenomena, where distributed AI systems with poorly understood dynamics could create cascading failures. The field requires significantly more theoretical work on complex systems and practical exploration of multi-agent dynamics to identify and mitigate these emergent risks.

## #86: "Golden Period" Identification Framework

Establish metrics and monitoring systems to detect when AI capabilities reach the 10-100x productivity enhancement threshold without compromising security. Create coordination mechanisms to extend this period from weeks to months, allowing humanity to maximize benefits from relatively safe systems before advancing to potentially riskier models. Develop strategy frameworks for optimal exploitation of this window.

---

# AI Governance & Policy Development

## Verification and Monitoring Infrastructure

**Scope:** Abilities to monitor variables of importance to AI policy and governance.

## #87: Incident Reporting

Implement a robust incident reporting framework for AI systems, alongside standardized mechanisms and procedures for documenting, analyzing, and sharing information about AI failures, misuse, or unexpected behaviors. The framework would enable cross-organizational learning from incidents, develop taxonomies in order to establish severity classifications, and facilitate coordinated responses to emerging threats. Similar to aviation safety reporting systems, it would ideally include protections for whistleblowers and requirements for timely disclosure. Implementation would require buy-in from major AI labs, coordinated regulatory frameworks across jurisdictions, and technical infrastructure for secure information sharing.

## #88: Agent IDs and Reputation Systems

Implement identification mechanisms like "agent IDs" for AI systems, so that it is possible for AI agents to build and maintain reputations. This could help prevent or disincentivize the development of AI agents that attack or exploit other agents, analogous to how humans control exploitation via reputation mechanisms. This approach would allow tracking behavior across interactions and building trust, which could be particularly valuable in scenarios where power remains distributed among different actors.

## #89: Technical Governance Tools

Develop technical governance tools for attribution and verification. These tools would include methods to verify model identity, authenticate AI interactions, and track compute usage to provide assurances about computational resource deployment. The techniques required for verification of model identity overlap with "Agent IDs and Reputation Systems," though this initiative focuses more narrowly on verification for the purpose of one-time interactions (rather than reputations over time), and more broadly on developing tools for tracking the compute usage of different AI systems.

## #90: Human Verification Systems

Build robust systems for verifying human identity to protect critical decision-making. Such systems become increasingly important as AI capabilities advance, helping distinguish human actors from AI systems, in particular, forming a critical component of security infrastructure in domains requiring human authorization. These systems would need to be continuously updated to counter increasingly sophisticated impersonation capabilities.

## #91: Compute Governance

Implement governance systems for global AI computation resources, via creating technical and policy frameworks to track and potentially regulate high-capability computing. This would involve development of monitoring systems for major compute clusters, transparency requirements for large-scale training runs, and verification mechanisms for compute usage claims. The proposal requires substantial government involvement and participation in order to provide greater visibility into who controls computational resources, what systems are being developed, and potential capability thresholds being approached.

---

## Aligning Commercial Incentives

**Scope:** Mechanisms which better align AI companies' incentives with the social good. A recurring theme of many interviews involved "natural incentives" causing AI companies to underinvest in alignment and security.

## #92: Enhanced Responsible Scaling Implementation

Transform existing Responsible Scaling Policies (RSPs) from theoretical frameworks into actionable implementation plans. Developing concrete, tested "if-then commitments" with ready-to-deploy protocols for when safety boundaries are approached, and build social mechanisms (including public accountability and transparency requirements) to ensure compliance. Significant focus would be placed on creating industry-wide norms and social pressure that makes non-compliance reputationally costly, driving collective behavior change across the AI industry.

## #93: Barriers to Fine-tuning

Develop technical and policy barriers that make unauthorized fine-tuning of advanced AI models extremely difficult, in order to prevent proliferation of dangerous capabilities. These barriers would combine technical measures like secure hardware enclaves, cryptographic verification of model origins, and detection systems for identifying unauthorized derivatives. Policy frameworks would establish legal consequences for circumventing these protections while providing legitimate access paths for authorized research.

## #94: Addressing AI Crawling Challenges

Develop industry standards and technical solutions for managing how AI systems access and index web content. This would include addressing issues around blocking unauthorized crawling activities, preventing data harvesting that violates creator intent, and establishing ethical norms for training data collection. Several groups are already taking independent action in this space, but are lacking coordination across their efforts. The project would focus on creating consensus around acceptable crawling practices, technical enforcement mechanisms, and could include compensation models for content creators whose work is used for AI training.

## #95: Training Data Licensing

Implement a regulated market for high-quality, difficult-to-replicate training data. There is a potentially "huge market of hard-to-get data" which cannot yet be automated, and this proposal aims to fairly compensate those whose data is used for the purpose of AI training, as well as providing nations and regulatory bodies leverage over AI development. Companies needing specialized data (like scientific papers or professional knowledge) would need to comply with regulations to maintain access, creating "natural incentives for companies to sign up" to oversight mechanisms.

## #96: Development-Phase Accountability Tools

Create mechanisms to hold AI companies accountable during the critical model development period when many risks emerge. Current regulatory approaches focus heavily on deployment while neglecting development phases. This was claimed to represent significant 'white space' in the oversight ecosystem. The internal, sensitive, and legally complex nature of development processes likely requires novel governance approaches.

## #97: Accountability Frameworks

Develop robust accountability and traceability governance approaches as well as liability systems for labs. As a reference: aerospace safety significantly improved when airlines faced meaningful liability, suggesting similar mechanisms could incentivize responsible AI development, although getting international players like China to participate could prove challenging.

## #98: Data Rights Systems

Establish frameworks for compensating individuals whose data is used in AI training, particularly focusing on high-skilled or vulnerable sector labor contributions. The ideal system would be "incentive compatible", in addition to providing "good data and good oversight". A system of data rights would aim to create economic returns for participants while ensuring quality data governance. This work would specifically focus on compensation and rights for individuals (compared to the "AI Ownership" idea below) whose data trains AI models, not broader questions of who owns AI-generated economic value.

---

## Building Government and Regulatory Capacity

**Scope:** Ways for government departments and policymakers to more efficiently acquire external talent, and for improving internal government expertise on AI. One key bottleneck raised across many different interviews was the lack of expertise within government and policy circles to regulate AI effectively.

## #99: Expert Collaboration

Assemble top economists and geopolitics experts to work intensively at a retreat to model AI governance challenges, with a focus on preventing both monopolistic AI control and the chaotic diffusion of dangerous AI capabilities. Following the expert collaboration, direct significant funding toward implementing whatever solutions the economists and geopolitics experts identify as most promising.

## #100: Regulatory Talent

Place a thousand competent, mission-aligned experts in government positions globally, with the aim to improve the talent pool of people working AI governance. This would involve strategic talent allocation across critical agencies like the EU AI Office, various ACs (AI Centers), and other regulatory bodies. Focus on enhancing government capabilities from within, ensuring regulators have both the technical understanding and motivation to implement oversight mechanisms and policies.

## #101: Government AI Use

Support governments in effectively using AI by developing specialized systems for policy implementation, monitoring, and regulatory oversight. This would be particularly critical in potential loss-of-control scenarios, where rapid technological change outpaces traditional governance mechanisms. These systems would help speed up government feedback loops, enabling more responsive regulation of AI-driven economic activity. Creating accountability and transparency mechanisms for government AI use would aim to maintain democratic control while leveraging efficiency benefits.

## #102: Academic-National Lab Cooperation

Adopt a hybrid model that combines university-driven theoretical innovation with laboratory-driven practical deployment to create accelerated paths for transitioning academic concepts into operational security measures within critical timeframes. University research excels at capability demonstration but struggles with practical implementation, whereas national laboratories provide essential implementation expertise but are often constrained by bureaucratic processes.

## #103: Policy Connection

Build relationships between technical experts and policymakers by creating institutional bridges that translate AI safety research into actionable governance frameworks. This work would develop shared vocabularies, educational resources, and collaboration mechanisms to ensure policy development is technically informed while remaining practically implementable. Regular exchanges between technical teams and government officials would help anticipate regulatory needs, shape technical development toward governance-amenable directions, and ensure oversight mechanisms remain effective as AI capabilities advance.

## #104: AI Security Institutes

Establish security institutes in more major jurisdictions than those that exist today, to create both the possibility of better local enforcement in addition to collaboration through established lines of communication. Funding and specific implementation mechanisms remain the main issue.

## #105: Risk Assessments

Persuade governments to incorporate AI-driven catastrophic scenarios into official risk frameworks. Most national risk assessments focus exclusively on conventional threats like floods and earthquakes, systematically overlooking emerging technological risks including advanced AI systems. These assessments directly influence critical resource allocation decisions regarding infrastructure investments, research funding priorities, and emergency preparedness capabilities. Engaging directly with government risk assessment agencies represents a force-multiplier for resilience funding. This would potentially redirect billions in existing funding toward relevant preparedness measures.

## #106: Legal Authority Clarification

Develop clear frameworks specifying which government agencies would have jurisdiction and authority to intervene in dangerous AI development. In the US, different agencies (DOD vs. DOE) would approach control very differently, making this determination crucial for effective governance. The project would also address who should be involved in oversight, including Congress, the public, and international allies - with current defaults likely favoring excessive exclusion. The goal would be producing ranked intervention plans that balance effectiveness with maintaining proper checks on power.

## #107: Government Support Framework

Create mechanisms to shape how governments support AI lab security through external lobbying bodies, as this idea currently lacks significant lab buy-in. This work would need organizations that understand both government regulation mechanics and the technical work involved in AI development and security.

## #108: Policy Studio/Competition

Create a dedicated policy innovation hub which would draft specific legislation, regulations, and governance frameworks for AI safety, alongside writing clear explainers of the legislation and what it is trying to accomplish, addressing the issue of existing policy proposals being "too nebulous". The studio would identify potential implementation pitfalls in future legislation by examining past regulatory failures like SB 1047, while developing concrete policy solutions.

## #109: Increased ARIA Support

Increase support for the UK's AI efforts, with a particular focus on ARIA's Advanced Research and Invention Agency efforts in hardware mechanisms and non-LLM based agent development approaches. The UK is pioneering numerous reasonable approaches to AI safety including engagement with China and technical verification methods. These initiatives were said to represent sensible alternatives to accelerating the LLM paradigm while still capturing economic benefits, and expanding these efforts would demonstrate viable paths for beneficial AI development without unnecessarily increasing risk.

## #110: AI R&D Acceleration Threat Modeling

Investigate risks associated with the acceleration of AI R&D. These risks may be difficult to characterize empirically but can be approached either as a risk factor for other threats or through loss of control scenarios. Building appropriate models would require studying how quickly capabilities progress through various thresholds and whether preparedness can keep pace. This area needs more concrete threat modeling to move beyond vague concerns about "more R&D being bad" towards specific, actionable insights about acceleration dynamics.

## #111: AI Development Lifecycle Risk Management Framework

Develop comprehensive risk management approaches combining multiple safety interventions for "defense-in-depth" against AI risks. This would integrate measures spanning the entire AI development lifecycle - from training methodology to ongoing monitoring, containment procedures, and continued alignment training. The framework would specify how different technical and governance interventions complement each other to address risk scenarios.

## #112: Government Data Centers

Construct secure government facilities capable of hosting model weights and other sensitive AI assets. These facilities could serve as repositories for models deemed too dangerous for widespread distribution, or as platforms for government auditing and testing. Access protocols could be tied to government procurement contracts,