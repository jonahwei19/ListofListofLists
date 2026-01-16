  

[

![Joe Carlsmith's Substack](https://substackcdn.com/image/fetch/$s_!0n9O!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe108b95c-c73a-4845-ab3f-25dc68188cd1_1280x1280.png)



](https://joecarlsmith.substack.com/)

# [Joe Carlsmith's Substack](https://joecarlsmith.substack.com/)

# AI for AI safety

### We should try extremely hard to use AI labor to help address the alignment problem.

[](https://substack.com/@joecarlsmith)

[Joe Carlsmith](https://substack.com/@joecarlsmith)

Mar 14, 2025

_Podcast version [here](https://joecarlsmithaudio.buzzsprout.com/2034731/episodes/16790183-ai-for-ai-safety) (read by the author), or search for "Joe Carlsmith Audio" on your podcast app._

_This is the fourth essay in a series that I’m calling “How do we solve the alignment problem?”. I’m hoping that the individual essays can be read fairly well on their own, but see [this introduction](https://joecarlsmith.substack.com/p/how-do-we-solve-the-alignment-problem) for a summary of the essays that have been released thus far, and for a bit more about the series as a whole._

---

# 1. Introduction and summary

In my [last essay](https://joecarlsmith.substack.com/p/paths-and-waystations-in-ai-safety), I offered a high-level framework for thinking about the path from here to safe superintelligence. This framework emphasized the role of three key “security factors” – namely:

- _Safety progress_: our ability to develop new levels of AI capability safely,
    
- _Risk evaluation_: our ability to track and forecast the level of risk that a given sort of AI capability development involves, and
    
- _Capability restraint_: our ability to steer and restrain AI capability development when doing so is necessary for maintaining safety.
    

In this essay, I argue for the crucial importance of what I call “AI for AI safety” – that is, the differential use of frontier AI labor to strengthen these security factors. I frame this in terms of the interplay between two feedback loops, namely:

- _The AI capabilities feedback loop_: access to increasingly capable AI systems driving further progress in AI capabilities.
    
- _The AI safety feedback loop_: safe access to increasingly capable AI systems driving improvements to the security factors above.
    

AI for AI safety is about continually using the latter feedback loop to either outpace or restrain the former.

[

![](https://substackcdn.com/image/fetch/$s_!2RDj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F707fa9fb-d111-4dd0-b3c9-cfbb9f977c96_1600x690.png)



](https://substackcdn.com/image/fetch/$s_!2RDj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F707fa9fb-d111-4dd0-b3c9-cfbb9f977c96_1600x690.png)

The basic argument for the importance of AI for AI safety is obvious: AI has the potential to unlock massive productivity gains, so of course we want to use this productivity for safety-relevant applications wherever possible. But it becomes particularly clear, I think, in light of the way that progress on AI capabilities is likely, by default, to be massively accelerated by large amounts of fast, high-quality AI labor. If our ability to make increasingly capable AI systems _safe_ can’t benefit from such labor in a comparable way, then at least for relatively hard problem profiles, and absent large amounts of capability restraint, I think we’re likely headed for disaster.

I also discuss the _timing_ of our efforts at AI for AI safety. In particular, I highlight what I call the “AI for AI safety sweet spot” – that is, a zone of capability development where frontier AI systems are capable enough to radically improve the security factors above, but not yet capable enough (given our countermeasures) to disempower humanity. I don’t think it’s clear that we’ll be able to benefit from such a sweet spot – and especially not, for long. But I think it’s a useful concept to have in mind, and an important possible focal point for our efforts at capability restraint.

[

![](https://substackcdn.com/image/fetch/$s_!kpM1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb368545-4874-4386-a2a3-0dd4a5480ad6_1600x502.png)



](https://substackcdn.com/image/fetch/$s_!kpM1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb368545-4874-4386-a2a3-0dd4a5480ad6_1600x502.png)

The big question, though, is whether we’ll actually be _able_ to do AI for AI safety at the scale and potency necessary to make a meaningful difference. I close the essay by introducing the concerns in this respect that I view as most serious – both more fundamental concerns (centered on elicitation/evaluation failures, differential sabotage, and dangerous rogue options), and more practical concerns (centered on e.g. the available amounts of time and political will). I then examine these concerns in more detail in the next essay, in the context of the application of “AI for AI safety” that I view as most important – namely, automated alignment research.

# 2. What is AI for AI safety?

By “AI for AI safety,” I mean: any strategy that makes central use of future AI labor to improve our civilization’s competence with respect to the alignment problem, _without_ assuming a need for radical, human-labor-driven alignment progress first. Let’s go through a few options in this respect, for the different security factors above.

- **Safety progress**:
    
    - Probably the most prominent application of AI for AI safety is **automated alignment research** – that is, using AIs to help with research on shaping AI motivations and local options in desirable ways.[1](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-1-159044941)
        
        - AIs already play an important role in various processes closely relevant to alignment – e.g. [evaluating AI outputs during training](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback), [labeling neurons in the context of mechanistic interpretability](https://openai.com/index/language-models-can-explain-neurons-in-language-models/), [monitoring AI chains of thought for reward-hacking behaviors](https://openai.com/index/chain-of-thought-monitoring/), [identifying which transcripts in an experiment contain alignment-faking behaviors](https://www.anthropic.com/research/alignment-faking), [classifying problematic inputs and outputs for the purpose of preventing jailbreaks](https://www.anthropic.com/news/constitutional-classifiers), etc. And of course, alignment researchers can benefit from the same general AI tools (e.g. coding, writing, brainstorming) that everyone else can; and the same tools for ML engineering, in particular, that other ML researchers can.
            
        - In the future, though, we can imagine AIs that more fully automate the complete pipeline involved in generating new alignment-relevant ideas, critiquing them, identifying and running informative experiments, interpreting the results, and so on.[2](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-2-159044941) Indeed, automation of this kind is a key focal point for safety efforts at some existing AI labs[3](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-3-159044941); and in my view, it’s the most important application of AI for AI safety. In my next essay, I’ll examine it in depth.
            
    - Beyond automated alignment research, though, advanced AIs can also help with **hardening the broader world** so that it is more robust to efforts by rogue AIs to seek power.[4](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-4-159044941) For example:
        
        - **Cybersecurity**: AIs could assist with improving the world’s cybersecurity, thereby making it much more difficult for rogue AIs to self-exfiltrate, to hack into unauthorized compute resources, etc. Indeed, if the offense-defense balance in cybersecurity is sufficiently favorable (and in particular: if enough code can be formally verified as secure using AI labor), then in principle AI labor could radically change the degree of baseline cybersecurity in the world at large.[5](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-5-159044941)
            
        - **Monitoring for rogue activity**: AIs could assist in monitoring for rogue AI activity, thereby making it harder for rogue AIs to operate undetected.[6](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-6-159044941)
            
        - **Anti-manipulation**: We could develop novel AI tools for detecting and blocking AI persuasion techniques aimed at manipulating humans.[7](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-7-159044941)
            
        - **Countermeasures to specific threat models**: AIs could assist in developing countermeasures to specific threat models for rogue AI attack, like biological weapons (via e.g. developing cheap and rapid diagnostics; improving disease surveillance, PPE and vaccine pipelines; developing novel countermeasures like [far-UVC](https://blueprintbiosecurity.org/works/built-environment-transmission-suppression/); etc).
            
        - **Eating free energy**: More generally, non-rogue AIs operating and competing in the economy at large makes it harder for rogue AIs to easily gain outsized amounts of money and influence. (Though: I doubt this is the most leveraged place for safety efforts to focus).[8](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-8-159044941)
            
- **Risk evaluation**:
    
    - Possibilities for **automated risk evaluation** include: automating the pipeline involved in designing and running evals, using AIs to help create and assess safety cases and cost-benefit analyses, using AI labor to assist in creating model organisms and other sources of evidence about AI risks, and using AI labor to generally improve our scientific understanding of how AI works. (Much of this intersects closely with automated alignment research, since progress on making AIs safe is closely tied to understanding how safe they are).
        
    - The potential role for AI labor in **forecasting** is perhaps especially notable, in that forecasting affords especially concrete and quantitative feedback loops for use both in training the AIs, and in assessing the quality of their task-performance.
        
    - And to the extent the **general quality of our collective epistemology** feeds into our risk evaluation in particular, AI can help notably with that too.[9](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-9-159044941)
        
- **Capability restraint:**
    
    - **Individual caution**: AI-assisted risk evaluation and forecasting can promote individual caution by helping relevant actors understand better what will happen if they engage in a given form of AI development/deployment; and AI advice might be able to help actors make wiser decisions, by their own lights, more generally.
        
    - **Coordination**: AIs might be able to help significantly with facilitating different forms of coordination – for example, by functioning as negotiators, identifying more viable and mutually-beneficial deals, designing mechanisms for making relevant commitments more credible and verifiable, etc.
        
    - **Restricted options and enforcement**: AIs might be able to help develop new and/or better technologies (including: AI technologies) for monitoring and enforcement – e.g., on-chip monitoring mechanisms, offensive cyber techniques for shutting down dangerous projects, highly trustworthy and privacy-preserving inspection capacity, etc. They could also help with designing and implementing more effective policies on issues like export controls and domestic regulation. And in the limit of direct military enforcement, obviously AIs could play a role in the relevant militaries.[10](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-10-159044941)
        
    - **Broader attitudes and incentives**: AI labor can also play a role in shaping the broader attitudes and incentives that determine how our civilization responds to misalignment risk – e.g., by helping with communication about the risks at stake.
        

In my [previous essay](https://joecarlsmith.substack.com/p/paths-and-waystations-in-ai-safety), I also included a catch-all security factor that I called “**backdrop capacity**,” which covered our civilization’s general levels of abundance, happiness, health, efficiency, institution quality, epistemology, wisdom, virtue, and so on.

- Relative to the more specific security factors above, the influence of backdrop capacity on loss of control risk is more diffuse, so I doubt that safety-focused efforts should actively focus on it.
    
- But I do think that at least in scenarios where there’s time for AI to significantly impact the economy before full-blown superintelligence is created, AI labor will likely be able to improve our backdrop capacity in a huge number of ways,[11](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-11-159044941) and that this could make an important difference to our civilizational competence.[12](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-12-159044941)
    

I’ll also note one final application of AI for AI safety: namely, using AI labor to assist in unlocking the sort of **enhanced human labor** I discussed in [my last essay](https://joecarlsmith.substack.com/i/158809605/sources-of-labor), which could then itself be used to improve the security factors discussed above.

- Thus, AI labor could be used for developing the science and technology necessary for **whole brain emulation** – e.g., for connectomics, brain-scanning, relevant neuroscience, animal experiments, etc – and for **other routes to enhanced human labor** as well – e.g., brain computer interfaces (BCI) and other biological interventions.
    

Analyzing all of these potential applications of AI for AI safety in detail is beyond my purpose here. I hope, though, that the broad vibe is clear. AI labor can play a role similar to human labor in many domains. And in the limit (including: the limit of trust), it can function as a full and superior substitute across the board. So anything you might’ve wanted to do with humans is in principle a candidate for “AI for AI safety” – and this includes improvements to all the security factors above.

## 2.1 A tale of two feedback loops

Here’s a way of thinking about “AI for AI safety” that I’ve found useful.[13](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-13-159044941)

The scariest AI scenarios, in my opinion, involve what we might call an “AI capability feedback loop,” in which the automation of the R&D involved in advancing AI capabilities leads to rapid escalation of frontier AI capabilities – the so-called “intelligence explosion.”[14](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-14-159044941) Here’s a simple diagram, applied to the toy model of AI safety I described in my last essay (and focusing, for even more simplicity, only on a single actor).[15](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-15-159044941)

[

![](https://substackcdn.com/image/fetch/$s_!I44W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29d42faa-c5c6-4471-b46f-15b153fc5f73_1600x847.png)



](https://substackcdn.com/image/fetch/$s_!I44W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29d42faa-c5c6-4471-b46f-15b153fc5f73_1600x847.png)

In the diagram, there are two sources of labor being devoted to making frontier AI systems more capable – normal human labor, and AI labor. And as the capability frontier advances, so does the quality of the AI labor being used to advance it.

It’s an open question exactly where this feedback loop leads, and on what timescales. In the bad case, though, this feedback loop quickly drives the capability frontier outside of the safety range, leading to loss of control.

[

![](https://substackcdn.com/image/fetch/$s_!Ts8A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde10d6b0-7181-4fbc-af14-742716de3adb_1600x900.png)



](https://substackcdn.com/image/fetch/$s_!Ts8A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde10d6b0-7181-4fbc-af14-742716de3adb_1600x900.png)

By contrast, many forms of “AI for AI safety” focus on strengthening a different feedback loop, which I’ll call the “AI safety feedback loop.” Here, safe forms of frontier AI labor get directed towards improving the security factors I discussed above, which in turn make it possible to get safe access to the benefits of more capable forms of AI labor. Thus, in a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!l9H5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b97708-ec55-4c70-a71f-74af54783ab5_1600x1080.png)



](https://substackcdn.com/image/fetch/$s_!l9H5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b97708-ec55-4c70-a71f-74af54783ab5_1600x1080.png)

So one way of thinking about “AI for AI safety” is in terms of the interplay between these two feedback loops – where the aim is for the AI safety feedback loop to continually secure the AI capability feedback loop, via some combination of (a) outpacing it (i.e., by expanding the safety range fast enough that the capability frontier never exceeds it), and (b) restraining it (i.e., strengthening our capacities for risk evaluation and capability restraint enough to hold off on pushing the capability frontier when necessary).[16](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-16-159044941)

## 2.2 Contrast with “need human-labor-driven radical alignment progress” views

“AI for AI safety” is not an especially specific strategy. Indeed, in some sense, its central claim is just: “AI labor is really important for dealing well with the alignment problem; try really hard to use AI labor to help.” And this might sound obvious.

Still, some people disagree. In particular: some people endorse what I’ll call “need human-labor-driven radical alignment progress views,” on which AI labor will remain some combination of unhelpful and unsafe absent radical progress on alignment – progress that therefore needs to be driven by some form of _human_ labor instead.[17](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-17-159044941) Thus, in a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!5qyc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbda7b004-24c9-4936-b0fe-f26b6338c30b_1600x921.png)



](https://substackcdn.com/image/fetch/$s_!5qyc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbda7b004-24c9-4936-b0fe-f26b6338c30b_1600x921.png)

We can also distinguish a sub-type of this sort of view – namely, one on which _unenhanced_ human labor _also_ isn’t enough to meaningfully help with alignment (though: maybe it can help with other security factors).[18](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-18-159044941) On these views, we will specifically need to unlock _enhanced_ human labor, before we can make enough alignment progress to safely and meaningfully benefit from advanced AI labor. And because unlocking enhanced human labor will likely take a while, we will likely need some serious capability restraint (e.g., a sustained global pause) in the meantime. (This, as I understand it, is the rough view of the leadership at the Machine Intelligence Research Institute.[19](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-19-159044941))

I’ll call these views “need _enhanced_-human-labor-driven alignment progress” views. Thus, in a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!B6Xb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4851d09b-fd30-4121-ab05-de93bf67616c_1600x982.png)



](https://substackcdn.com/image/fetch/$s_!B6Xb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4851d09b-fd30-4121-ab05-de93bf67616c_1600x982.png)

Below I’ll discuss the sorts of objections that motivate views like these. For now, I’m flagging them, centrally, in order for the contrast to help bring the substance of “AI for AI safety” into clearer view. That is: AI for AI safety argues for a more direct role for the “future AI labor” node, even absent radical, human-labor-driven safety progress. In a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!yUsb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3b05208-04e1-4848-973f-11c578710f48_1600x843.png)



](https://substackcdn.com/image/fetch/$s_!yUsb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3b05208-04e1-4848-973f-11c578710f48_1600x843.png)

## 2.3 Contrast with a few other ideas in the literature

I’ll also briefly note a few other contrasts with related ideas in the literature,[20](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-20-159044941) notably:

- **D/acc**: “AI for AI safety” is closely related to what [Buterin (2023](https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html)) calls “d/acc,”[21](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-21-159044941) which focuses on differentially developing beneficial (and in particular, in Buterin’s framing, “defensive”/“decentralized”/“democratic”) forms of technology relative to harmful forms.[22](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-22-159044941) And we can view the interplay between the two feedback loops discussed above through a similar lens – that is, the goal is to differentially direct the glut of productivity that AI progress makes possible into the AI safety feedback loop, relative to the AI capability feedback loop. But Buterin is interested in differential technological development very broadly (not just AI-driven technological development), with respect to a wide array of issues (e.g., Covid, authoritarianism, etc); whereas I’m specifically interested in _AI labor_ being applied to improving the security factors that help with addressing the alignment problem in particular. And this narrower focus makes clearer how a beneficial “feedback loop” might get going.[23](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-23-159044941)
    
- **Automated alignment research**: As I noted above, automated alignment research is an especially important form of AI for AI safety (and one I’ll analyze in detail in the next essay); but AI for AI safety covers a variety of other applications as well.
    
- **Pivotal acts**: Some approaches to AI safety attempt to identify some “[pivotal act](https://arbital.com/p/pivotal/)” – i.e., an action that drastically improves the situation with respect to AI safety – that we use AI systems to perform.[24](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-24-159044941) This is similar to “AI for AI safety” in its central focus on advanced AI labor – that is, first one gets access to some kind of pivotally useful AI system, and then one “saves the world” from there. But even assuming the world needs “saving,”[25](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-25-159044941) I think that thinking in terms of discrete “pivotal acts” can easily mislead us about sorts of improvements to our security factors required in order for the world to get “saved.” In particular: those improvements can result from a very large assortment of individual actions by a very large number of different agents (and/or non-agentic AI systems), no individual one of which needs to be dramatically pivotal (we might call this a “pivotal act by a thousand cuts”).[26](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-26-159044941)
    

# 3. Why is AI for AI safety so important?

“AI for AI safety,” then, is about safely using AI labor to improve our civilizational competence with respect to the alignment problem, without first assuming the need for radical, human-labor-driven alignment progress. And I hope it’s clear why, if we _can_ do this, we should. To do otherwise, after all, would be to give up on a source of labor that could provide meaningful help. And not just any source. Rather: in the sorts of transformative AI scenarios we’re considering, AI labor is increasingly the central driver of productivity and progress across our civilization. Of course you’d want to use it for AI safety applications, too – if you can. And not doing this would be a kind of “reverse d/acc” – i.e., differentially _slowing down_ safety-relevant aspects of the economy.

But I think the urgency and importance of “AI for AI safety” – and especially, of automated alignment research – becomes even clearer once we bring to mind the AI capabilities feedback loop I described above. That is: AI developers will increasingly be in a position to apply unheard of amounts of increasingly high-quality cognitive labor to pushing forward the capabilities frontier. If efforts to expand the safety range can’t benefit from this kind of labor in a comparable way (e.g., if alignment research has to remain centrally driven by or bottlenecked on human labor, but capabilities research does not), then absent large amounts of sustained capability restraint, it seems likely that we’ll quickly end up with AI systems too capable for us to control (i.e., the “bad case” described above).

Of course: it may be that, unfortunately, automated alignment research isn’t viable, and avoiding failure on the alignment problem does in fact require large amounts of sustained capability restraint. I’ll discuss various concerns in this respect below; and I’ll discuss this kind of restraint in more detail later in the series as well. Indeed, I think capability restraint remains extremely important even _if_ automated alignment research _is_ viable. Especially on hard problem profiles, we will still need as much time as possible.

But I am sufficiently optimistic about automated alignment research (especially if we actually try hard at it), and sufficiently worried about the difficulty of achieving large amounts of capability restraint (e.g., sustained global pauses), that I think we should approach strategies that focus _solely_ on capability restraint, and/or on human-labor-driven forms of alignment progress, with a large burden of proof. That is: given our current evidence, I think we would be _extremely_ foolish to give up, now, on using frontier AI labor to help with alignment (and with all the other aspects of our civilizational competence). To me, this looks like giving up pre-emptively on the most powerful tool in the toolbox (albeit, also: the most dangerous), and the one most likely to make a crucial difference. Maybe, ultimately, we should do this. But not, I think, on the basis of the existing objections to e.g. automated alignment research; and especially not without having made an _extremely serious effort_ at actually doing automated alignment research well. My next essay explains my view here in more detail.

# 4. The AI for AI safety sweet spot

I also want to highlight another concept that I find useful in thinking about AI for AI safety – that is, what I call the “AI for AI safety sweet spot.” By this I mean, a zone of capability development (and safety progress) such that:

1. Frontier AIs are capable enough to radically improve the security factors above, _if_ relevant actors can succeed at eliciting these capabilities.[27](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-27-159044941)
    
2. Disempowering humanity is not an option for these AIs, given our efforts to restrict their options in this respect (call such efforts “countermeasures”).[28](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-28-159044941)
    

Thus, in a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!L7VE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55411079-4ee2-4601-a26a-b080c00ea8e1_1600x498.png)



](https://substackcdn.com/image/fetch/$s_!L7VE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55411079-4ee2-4601-a26a-b080c00ea8e1_1600x498.png)

The AI for AI safety sweet spot is important, I think, because it’s an especially salient target for efforts at capability restraint:

- That is: to extent one has a limited budget of capability restraint, applying it once you’re within the AI for AI safety sweet spot, relative to beforehand, makes it possible for the time you buy to go towards radical, AI-driven improvements to our civilizational competence; whereas this is less true of earlier “pauses.”[29](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-29-159044941)
    
- Whereas applying capability restraint _later_ means working with AI systems that are in a position to disempower all of humanity – a scarier position (more on this below).
    

Note that in principle, different security factors might have different sweet spots – e.g. maybe the capability level required to use AIs to help with coordination is lower than the level required to use AIs for alignment research.[30](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-30-159044941) And note, also, that you can expand the AI for AI safety sweet spot by improving your countermeasures – and that AI labor can help with this.

[

![](https://substackcdn.com/image/fetch/$s_!cZyi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5701be5f-bfd4-407e-91ee-3f832986497e_1600x545.png)



](https://substackcdn.com/image/fetch/$s_!cZyi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5701be5f-bfd4-407e-91ee-3f832986497e_1600x545.png)

Indeed, some strategies in the vicinity of “AI for AI safety” have roughly the following structure:[31](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-31-159044941)

- **Step 1**: Get to/create the AI for AI safety sweet spot.
    
- **Step 2**: Stay there for as long as possible.
    
- **Step 3**: Be able to elicit the useful-to-safety capabilities of frontier AIs.
    
- **Step 4**: Do a ton of AI for AI safety.
    
- **Step 5**: Hopefully things are a lot better after that.
    

Of course, all of these steps may be quite difficult. That is, step 1 may require significant investment in countermeasures; step 2 may require significant capability restraint; step 3 requires adequate success at capability elicitation; and step 4 requires adequate investment by relevant actors.

And in addition to being a highly _useful_ zone to spend time in, the AI for AI safety sweet spot is also a much _scarier_ to zone to spend time in, relative to earlier points, because frontier AIs are closer in capability to systems with options to disempower humanity (indeed, they may only lack such options in virtue of our countermeasures), and they are likely capable enough to drive rapid progress in frontier AI capability, if applied to the task.

Also: note that it’s not actually clear that we _do_ have a limited budget of capability restraint. To the contrary: one can easily imagine the reverse – i.e., that earlier efforts at capability restraint make later efforts _easier_ (because, for example, you’ve gotten practice with the relevant sorts of coordination and coalition-building; because you’ve started setting up relevant forms of infrastructure; because you’ve changed what sorts of policies seem like live options; etc). Indeed, strategies that involve racing to the brink of destruction, while claiming that you’ll hit the brakes at the last possible second, justifiably invite skepticism – about whether brakes will in fact get pulled, and in time; about the momentum that all-out-racing beforehand will have created; and so on.

Overall, then, I don’t think there’s any kind of knock-down argument for focusing efforts at capability restraint on the AI for AI safety sweet spot in particular. But I think it’s worth bearing in mind as a possibility regardless.

## 4.1 The AI for AI safety spicy zone

Can we expand the AI for AI safety sweet spot to include full-blown superintelligent agents – i.e., agents that are safe because they don’t have any options for disempowering humanity? In a later essay, I’ll discuss some of the key difficulties with relying purely on option control in the context of superintelligences[32](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-32-159044941) – difficulties that make me expect that motivation control will eventually need to play at least some role in ensuring safety. But I don’t think this is totally obvious.

Assuming we can’t rely solely on option control all the way up through superintelligent AI agents, though, then at some point (if we’re building superintelligent AI agents at all – recall that we don’t have to), we’re going to need to exit the AI for AI safety sweet spot. Importantly, though, this doesn’t mean that “AI for AI safety” is no longer viable. Rather, we just need to have made enough progress on _motivation control_ to do it safely – and we need to keep making adequate progress in this respect as the capability frontier advances.[33](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-33-159044941)

Let’s call this sort of capability level the “AI for AI safety spicy zone.”

[

![](https://substackcdn.com/image/fetch/$s_!6Kf1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd922959e-1201-4c7e-8391-0d11ccb4cc8b_1600x612.png)



](https://substackcdn.com/image/fetch/$s_!6Kf1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd922959e-1201-4c7e-8391-0d11ccb4cc8b_1600x612.png)

I’m calling this zone “spicy” because it involves entering what I called, in the appendix of my second essay, a “[vulnerability to motivations](https://joecarlsmith.substack.com/i/157445591/appendix-a-typology-of-vulnerability-conditions)” condition. That is: AIs, at this point, are in a position to disempower humanity, and we are relying on them to choose not to do so. This is a much scarier position to be in than one in which the AIs have no such option.[34](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-34-159044941)

Note, though, that [as I discussed in my second essay](https://joecarlsmith.substack.com/i/157445591/what-about-the-incentive-prerequisites), the vulnerability at stake in the AI for AI safety spicy zone still comes along a spectrum. In particular: it increases when AI systems can disempower humanity via _more_ paths, _more_ easily[35](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-35-159044941); when smaller numbers of AIs can do it, with less coordination; and so on.[36](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-36-159044941)

## 4.2 Can we benefit from a sweet spot?

Will we be in a position to benefit from an AI for AI safety sweet spot? It’s not all clear. Here I’ll note a few salient worries. (And note that these worries can apply to milder versions of the “spicy zone” as well.)

The first is just that: there won’t be a sweet spot at all. That is: by the time frontier AIs are capable enough to radically improve our civilizational competence, they’ll also be in a position to disempower humanity, even given our countermeasures. Call this a “no sweet spot view.”[37](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-37-159044941)

[

![](https://substackcdn.com/image/fetch/$s_!UqwN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb5cbe56-5703-4eab-82cf-b3ea71df9245_1236x642.png)



](https://substackcdn.com/image/fetch/$s_!UqwN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb5cbe56-5703-4eab-82cf-b3ea71df9245_1236x642.png)

Alternatively: you might think that there will be some sort of sweet spot, but that it will be too narrow-a-band given how fast the capability frontier will be advancing. Different versions of this concern can give different amounts of weight to (a) the size of the sweet spot, (b) the default speed of frontier AI progress, and (c) our ability to slow down if we try, but the broad theme is: we’re going to blow through the sweet spot so fast it doesn’t matter. Thus, in a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!2oke!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4f45543-02b7-42a6-97ca-4033a6be053d_1336x646.png)



](https://substackcdn.com/image/fetch/$s_!2oke!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4f45543-02b7-42a6-97ca-4033a6be053d_1336x646.png)

Finally, you might think that there will be a large enough sweet spot to spend meaningful time in, but that we’ll be unable to usefully _elicit_ the capabilities of the AIs in question. Thus, in a diagram:

[

![](https://substackcdn.com/image/fetch/$s_!5tT5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb9ce8c1-c138-4819-9e71-a67bd98b834a_1600x482.png)



](https://substackcdn.com/image/fetch/$s_!5tT5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb9ce8c1-c138-4819-9e71-a67bd98b834a_1600x482.png)

And we can imagine a variety of other concerns besides.[38](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-38-159044941) Indeed, these concerns tend to mirror the core concerns about AI for AI safety more generally. Let’s look at those more directly now.

# 5. Objections to AI for AI safety

What are the main objections to AI for AI safety?

I’ll note three core objections that seem to me more fundamental; and then some other objections that seem more practical (which isn’t to say they aren’t serious).

## 5.1 Three core objections to AI for AI safety

The three core objections to AI for AI safety, as I see them, are:

1. **Evaluation failures**: We won’t be able to elicit the sorts of helpful-to-AI-safety task performance we want out of AI systems capable of that task-performance, because we won’t be able to evaluate well enough whether that sort of task performance is occurring.
    
2. **Differential sabotage**: Power-seeking AIs will actively and differentially sabotage helpful-to-AI-safety work, relative to other sorts of work (for example, work on advancing frontier AI capabilities), because they won’t want us to succeed in our AI-safety-related goals.
    
3. **Dangerous rogue options**: AIs capable and empowered enough to meaningfully help with AI for AI safety would also be in a position to disempower humanity. So we would need to already have achieved substantive amounts of alignment in order to use them safely.
    

I think all three of these objections are serious concerns. And they’re interrelated. For example: weakness in our evaluation processes makes sabotage easier. But they’re also importantly distinct. For example: some evaluation failures _don’t_ arise from differential sabotage, and these have importantly different properties (more in my next essay).

These three core objections can arise, in various guises, with respect to any application of AI for AI safety. But the specific form they take will differ depending on the application in question. For example, the sort of dangerous rogue options at stake in (3) might vary depending on the application.

## 5.2 Other practical concerns

Beyond these three core objections, we can also note a variety of other concerns about AI for AI safety – concerns that focus less on whether AI for AI safety is viable in principle, and more on whether or not, in practice, we would do it right. Of these, I worry most about the following (but see footnote for a few others[39](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-39-159044941)):

- **Uneven capability arrival**: the sorts of capabilities necessary for AI for AI safety will arrive much _later_ than the capabilities necessary for automating capabilities R&D, thereby significantly disadvantaging the AI safety feedback loop relative to the AI capabilities feedback loop.
    
- **Inadequate time**: Even setting aside uneven capability arrival, by the time we’re in a position to use AI systems to meaningfully help us with AI safety goals, there won’t be enough time left before the AI capability feedback loop pushes us into catastrophe.
    
- **Inadequate investment**: In practice, relevant actors and institutions won’t devote adequate resources to AI for AI safety relative to other projects and priorities.
    

I think that these more practical concerns are real and important as well. And here, too, their specific form and force can vary based on the application in question.

In my next essay, I’ll look at these objections – both the more fundamental objections, and the more practical objections – in more detail. And I’m going to focus, in particular, on their relevance to the application of AI for AI safety that I view as most important: namely, automating alignment research.

[1](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-1-159044941)

I think people generally use the term “alignment research” in a way that covers both motivation control and local forms of option control (e.g. oversight and monitoring; and not: hardening the broader world), and I’m going to do this, too. And I’m going to include what I’ve previously called “incentive design” – that is, research on what sorts of incentives give rise to cooperative behavior – as well.

[2](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-2-159044941)

This also includes identifying and developing more safety-conducive routes towards capability progress – including, e.g., routes that don’t rely on agentic systems; routes that proceed via new and more verifiably-secure paradigms, etc.

[3](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-3-159044941)

Thus, as I discussed in my [last essay](https://joecarlsmith.substack.com/p/paths-and-waystations-in-ai-safety): this is the waystation that OpenAI’s old “superalignment” team was focusing on – see e.g. discussion [here](https://openai.com/index/introducing-superalignment/): “Our goal is to build a roughly human-level [automated alignment researcher⁠](https://openai.com/blog/our-approach-to-alignment-research). We can then use vast amounts of compute to scale our efforts, and iteratively align superintelligence.” And something in the vicinity is suggested by [Sam Bowman’s description of Anthropic’s theory of victory on AI as well](https://sleepinyourhat.github.io/checklist/) (see especially section 2 on “[TAI, or Making the AI do our homework](https://sleepinyourhat.github.io/checklist/#ch2)”).

[4](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-4-159044941)

This is a form of non-local “option control,” but it still falls under “safety progress” on my definition. And note that “backdrop capacity,” discussed below, intersects in important ways with hardening the world to AI attack.

[5](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-5-159044941)

Though note that not all the effects of this on the strategic landscape are necessarily positive. Thus, for example, some of the less aggressive forms of “[mutually-assured AI malfunction](https://arxiv.org/abs/2503.05628)” involve different actors being able to sabotage each other’s projects using cyberattacks.

[6](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-6-159044941)

This could include gathering and processing vastly larger amounts of information than humans have hitherto been able to process.

[7](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-7-159044941)

See [Davidson (2023)](https://www.lesswrong.com/posts/zxmzBTwKkPMxQQcfR/let-s-use-ai-to-harden-human-defenses-against-ai) for more here.

[8](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-8-159044941)

See [Karnofsky (2022)](https://www.lesswrong.com/posts/rCJQAkPTEypGjSJ8X/how-might-we-align-transformative-ai-if-it-s-developed-very) for more.

[9](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-9-159044941)

See e.g. [Lukas Finnveden’s discussion of “AI for epistemics”](https://forum.effectivealtruism.org/posts/jPKoNFRowKJwGgGyy/what-s-important-in-ai-for-epistemics) for more.

[10](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-10-159044941)

Though: this is one of the scariest applications of AI for AI safety, and worth special caution.

[11](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-11-159044941)

See e.g. Amodei’s “[Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace)” for some discussion.

[12](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-12-159044941)

Though of course: AI could also degrade our backdrop capacity in lots of ways as well – and in scenarios with a fast and disruptive transition to advanced AI, we might expect a lot of this, too.

[13](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-13-159044941)

I think I first heard this framing from Carl Shulman.

[14](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-14-159044941)

See e.g. [here](https://situational-awareness.ai/from-agi-to-superintelligence/) and [here](https://www.openphilanthropy.org/research/what-a-compute-centric-framework-says-about-takeoff-speeds/) for more discussion. Note that the intelligence explosion need not involve AI systems literally improving _themselves_ – i.e., recursive _self-_improvement. Nor need it involve the automation of ~all tasks in the economy.

[15](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-15-159044941)

Though: note that not all scary AI scenarios involve this feedback loop. For example: the creation of the AI systems that disempower humans might be driven centrally by human labor.

[16](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-16-159044941)

Though: note that to the extent that we end up relying heavily on _restraining_ further increases in frontier AI capability, the AI safety feedback loop also won’t be able to benefit from more capable forms of AI labor, and so the “feedback” aspect will be correspondingly stalled.

[17](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-17-159044941)

See e.g. [Leahy et al (2024)](https://www.thecompendium.ai/) for an example: “The iterative alignment strategy has an ordering error – we first need to achieve alignment to safely and effectively leverage AIs… Fundamentally, the problem with iterative alignment is that it never pays the cost of alignment. Somewhere along the story, alignment gets implicitly solved – yet no one ever proposes an actual plan for doing so beyond ‘the (unaligned) AIs will help us’.”

[18](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-18-159044941)

Or at least, unenhanced human labor of the form that will likely, in practice, be brought to bear.

[19](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-19-159044941)

At least as of early 2024. From [here](https://www.lesswrong.com/posts/q3bJYTB3dGRf5fbD9/miri-2024-mission-and-strategy-update#fndnikb6w9rc8): “Nate and Eliezer both believe that humanity should not be attempting technical alignment at its current level of cognitive ability, and should instead pursue human cognitive enhancement (e.g., via uploading), and then having smarter (trans)humans figure out alignment.”

[20](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-20-159044941)

Lizka Vaintrob and Owen Cotton-Barratt also have a forthcoming piece on a topic closely akin to “AI for AI safety,” which offers a perspective quite similar to my own.

[21](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-21-159044941)

See also [Clifford (2024)](https://www.joinef.com/posts/introducing-def-acc-at-ef/) on “def/acc.”

[22](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-22-159044941)

D/acc is thus a particular implementation of what [Bostrom (2002)](https://nickbostrom.com/existential/risks.pdf) calls “differential technological development.” See also [these notes](https://michaelnotebook.com/dtd/) on the topic from Michael Nielsen, and [this recent update](https://vitalik.eth.limo/general/2025/01/05/dacc2.html) from Buterin.

[23](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-23-159044941)

That said, the more we focus on “backdrop capacity,” and include human labor in addition to AI labor in the picture, then AI for AI safety and d/acc become more similar (though d/acc is still concerned with a broader range of technological issues, not just the alignment problem).

[24](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-24-159044941)

See e.g. the strategy outlined in MIRI’s [2017 fundraiser update](https://intelligence.org/2017/12/01/miris-2017-fundraiser/), and Yudkowsky’s discussion [here](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities) of “So far as I'm concerned, [if you can get a powerful AGI that carries out some pivotal superhuman engineering task, with a less than fifty percent chance of killing more than one billion people](https://twitter.com/ESYudkowsky/status/1070095112791715846), I'll take it.”

[25](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-25-159044941)

I think talk of “pivotal acts” often brings in an implicit assumption that the default outcome is doom (hence the need for the world to be “saved”) – an assumption I don’t take for granted. But we can remedy this issue by focusing, in particular, on problem profiles where doom is currently the default.

[26](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-26-159044941)

This is a point from [Christiano (2022)](https://www.lesswrong.com/posts/CoZhXrhpQxpy9xw9y/where-i-agree-and-disagree-with-eliezer): “No particular act needs to be pivotal in order to greatly reduce the risk from unaligned AI, and the search for single pivotal acts leads to unrealistic stories of the future and unrealistic pictures of what AI labs should do.” See also Critch (2022) [here](https://www.lesswrong.com/posts/etNJcXCsKC6izQQZj/pivotal-outcomes-and-pivotal-processes).

[27](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-27-159044941)

And in particular: if they’re willing to devote large amounts of compute and other relevant resources to the project – though I won’t take a stand here on how much is necessary.

[28](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-28-159044941)

I.e., they don’t have options for disempowering humanity that would succeed with non-trivial probability. That is, in the [taxonomy of vulnerability conditions I offered in my second essay](https://joecarlsmith.substack.com/i/157445591/appendix-a-typology-of-vulnerability-conditions), we aren’t in a global vulnerability-to-motivations condition. And note that one way this can happen is: the relevant AIs don’t satisfy the agency pre-requisites at all.

[29](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-29-159044941)

Though of course, the usefulness of our AIs comes along a spectrum, and we should be trying to do as much AI for AI safety as we can, at every step along the way.

[30](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-30-159044941)

Thanks to Owen Cotton-Barratt for discussion.

[31](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-31-159044941)

This is the sort of strategy that I associate with e.g. Shlegeris and Greenblatt [here](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled), though I’m not sure if they’d endorse this framing.

[32](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-32-159044941)

For example: applying option control to superhuman strategies requires access to superhuman forms of oversight and monitoring.

[33](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-33-159044941)

Plus, as in the case of the AI for AI safety sweet spot, we need adequate elicitation ability.

[34](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-34-159044941)

Though obviously, relying on our countermeasures to ensure this condition is its own form of scary as well.

[35](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-35-159044941)

Because the availability of more such paths makes it harder for an AI’s “inhibitions” to rule out all the available options, and higher probabilities of success make it easier for lower-levels of “ambition” to justify going for it anyways.

[36](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-36-159044941)

And in my opinion, arguments about AI risk too often focus on the _maximally_ spicy case (i.e., the case of AIs that are in a position to disempower humanity extremely easily via a wide variety of paths).

[37](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-37-159044941)

In the diagram, I’ve put the two lines in the same place; but in principle, the capability level required for disempowering humanity might actually come _earlier_ than the capability level required to radically improve our competence. H/t Owen Cotton-Barratt for discussion.

[38](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-38-159044941)

For example: we might worry that it will be too difficult to _tell_ when we’re in the sweet spot (h/t Catherine Brewer); or we might worry that relevant actors won’t invest enough resources into benefiting from the sweet spot.

[39](https://joecarlsmith.substack.com/p/ai-for-ai-safety#footnote-anchor-39-159044941)

We might also worry about:

**Cover**: The idea of “AI for AI safety” will provide cover for people to push forward with dangerous forms of AI capability development.

**Complacency**: The idea of “passing the buck to the AIs” will obscure how much work humans will still need to be doing, and will render us complacent more generally.

**Capabilities externalities**: Efforts aimed at AI for AI safety will further accelerate AI capabilities.

**Distraction from capability restraint**: Efforts focused on “AI for AI safety” will distract attention and resources from capability restraint, which should be our core focus.

**Premature effort**: People might make efforts at AI for AI safety prior to the point where it can really be useful, or in a manner that would have been far more efficient had they waited for another notch of capability improvement, thereby wasting precious time.

**Harmful delegation**: even if the AIs we delegate safety-relevant tasks to are behaving broadly as we intend, the delegation in question might degrade human understanding and control in ways that exacerbate loss-of-control risk down the road – for example, by increasing our reliance on AIs, reducing our epistemic grip on the world, and exposing us to unanticipated problems that delegation to AIs (even non-rogue AIs) can create.

I’ll discuss these briefly in the next essay as well.

[

![Joe Carlsmith's Substack](https://substackcdn.com/image/fetch/$s_!0n9O!,w_96,h_96,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe108b95c-c73a-4845-ab3f-25dc68188cd1_1280x1280.png)



](https://joecarlsmith.substack.com/)

#### Recommend Joe Carlsmith's Substack to your readers

Philosophy, futurism, and other topics

[](https://substack.com/profile/18478049-interstellar-philosopher)[](https://substack.com/profile/26108900-neuro-morph)[](https://substack.com/profile/110583982-alex-popescu)[](https://substack.com/profile/3277030-jacques-thibodeau)[](https://substack.com/profile/857781-sandra)

9 Likes∙

[3 Restacks](https://substack.com/note/p-159044941/restacks?utm_source=substack&utm_content=facepile-restacks)

#### Discussion about this post

[](https://substack.com/profile/6833561-andreas-f-hoffmann?utm_source=comment)

[Andreas F. Hoffmann](https://substack.com/profile/6833561-andreas-f-hoffmann?utm_source=substack-feed-item)

[THEAFH’s Substack](https://theafh.substack.com/?utm_content=comment_metadata&utm_source=substack-feed-item)[Mar 21, 2025](https://joecarlsmith.substack.com/p/ai-for-ai-safety/comment/102360087 "Mar 21, 2025, 6:04 PM")

I would argue that the obsessive preoccupation with alignment is currently a waste of time. This is probably also the conclusion that the OpenAI leadership team found after they realized that scaling a steam engine (GPT 4o) won't lead to an magical emergency of an jet engine (AGI) and they decided to get rid of most oft their alignment team. I fear we have collectively looked on the wrong comparisons for AI development and and therefore came to the wrong conclusions regarding the steps and time scale to AGI:

[https://theafh.substack.com/p/what-viruses-can-teach-us-about-ai?r=42gt5](https://theafh.substack.com/p/what-viruses-can-teach-us-about-ai?r=42gt5)

Like (1)

Reply

Share

[1 reply](https://joecarlsmith.substack.com/p/ai-for-ai-safety/comment/102360087)

[1 more comment...](https://joecarlsmith.substack.com/p/ai-for-ai-safety/comments)

[Fake thinking and real thinking](https://joecarlsmith.substack.com/p/fake-thinking-and-real-thinking)

[When the line pulls at your hand.](https://joecarlsmith.substack.com/p/fake-thinking-and-real-thinking)

Jan 28, 2025 • [Joe Carlsmith](https://substack.com/@joecarlsmith)

86

10

18

![](https://substackcdn.com/image/fetch/$s_!KJ5F!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc9ba6cf-b825-4b1e-85b7-f6572731177d_280x356.jpeg)

[Leaving Open Philanthropy, going to Anthropic](https://joecarlsmith.substack.com/p/leaving-open-philanthropy-going-to)

[On a career move, and on AI-safety-focused people working at AI companies.](https://joecarlsmith.substack.com/p/leaving-open-philanthropy-going-to)

Nov 3, 2025 • [Joe Carlsmith](https://substack.com/@joecarlsmith)

40

3

3

![](https://substackcdn.com/image/fetch/$s_!qMsC!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F042fbe7d-b262-49dc-bddc-88a4075a861c_960x440.png)

[The stakes of AI moral status](https://joecarlsmith.substack.com/p/the-stakes-of-ai-moral-status)

[On seeing and not seeing souls.](https://joecarlsmith.substack.com/p/the-stakes-of-ai-moral-status)

May 21, 2025

35

11

10

![](https://substackcdn.com/image/fetch/$s_!udrM!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf567fc8-6e84-4445-a491-1cdfc152324d_1114x613.png)

© 2026 Joe Carlsmith · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://your.substack.com/publish)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com/) is the home for great culture