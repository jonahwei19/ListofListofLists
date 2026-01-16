  

[

![AI Futures Project](https://substackcdn.com/image/fetch/$s_!iyu_!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3409cfd0-9243-479e-80f9-d0e3922c450a_132x132.png)



](https://blog.ai-futures.org/)

# [AI Futures Project](https://blog.ai-futures.org/)

# Slow corporations as an intuition pump for AI R&D automation

### If slower employees would be much worse wouldn't automated faster ones be much better?

[](https://substack.com/@ryangreenblatt)[](https://substack.com/@elifland)

[Ryan Greenblatt](https://substack.com/@ryangreenblatt) and [Eli Lifland](https://substack.com/@elifland)

May 19, 2025

_This is a guest post primarily by Ryan Greenblatt; Eli Lifland assisted with the writing._

How much should we expect AI progress to speed up after fully automating AI R&D? This post presents an intuition pump for reasoning about the level of acceleration by talking about different hypothetical companies with different labor forces, amounts of serial time, and compute. Essentially, if you’d expect an AI research lab with substantially less serial time and fewer researchers than current labs (but the same cumulative compute) to make substantially less algorithmic progress, you should also expect a research lab with an army of automated researchers running at much higher serial speed to get correspondingly more done. (And if you’d expect the company with less serial time to make similar amounts of progress, the same reasoning would also imply limited acceleration.) We also discuss potential sources of asymmetry which could break this correspondence and implications of this intuition pump.

## The intuition pump

Imagine theoretical AI companies with the following properties:

[

![](https://substackcdn.com/image/fetch/$s_!GtBn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F952784bb-b564-410d-a6f7-efc09ad4786d_1264x1058.png)



](https://substackcdn.com/image/fetch/$s_!GtBn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F952784bb-b564-410d-a6f7-efc09ad4786d_1264x1058.png)

NormalCorp is similar to a future frontier AI company. SlowCorp is like NormalCorp except with 50x less serial time, a 5x smaller workforce, and lacking above median researchers/engineers.[1](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-1-163243860) How much less would SlowCorp accomplish than NormalCorp, i.e. what fraction of NormalCorp’s time does it take to achieve the amount of algorithmic progress that SlowCorp would get in a week?

SlowCorp has 50x less serial labor, 5x less parallel labor, as well as reduced labor quality. Intuitively, it seems like it should make much less progress than NormalCorp. My guess is that we should expect NormalCorp to achieve SlowCorp’s total progress in at most roughly 1/10th of its time.

Now let’s consider an additional corporation, AutomatedCorp, which is an analog for a company sped up by AI R&D automation.

[

![](https://substackcdn.com/image/fetch/$s_!V2aW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7089ebc5-aede-44bb-af55-1fc3a27a1b83_1732x1068.png)



](https://substackcdn.com/image/fetch/$s_!V2aW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7089ebc5-aede-44bb-af55-1fc3a27a1b83_1732x1068.png)

AutomatedCorp is like NormalCorp except with 50x more serial time, a 50x larger workforce, and only world-class researchers and engineers. The jump from NormalCorp to AutomatedCorp is like the jump from SlowCorp to NormalCorp but with 10x more employees, and with the structure of the increase in labor quality being a bit different.

It seems like the speedup from NormalCorp to AutomatedCorp should be at least similar to the jump from SlowCorp to NormalCorp, i.e. at least roughly 10x. My best guess is around 20x.

AutomatedCorp is an analogy for a hypothetical AI company with AI researchers that match the best human researcher while having 200k copies that are each 50x faster than humans.[2](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-2-163243860) If you have the intuition that a downgrade to SlowCorp would be very hobbling while this level of AI R&D automation wouldn’t vastly speed up progress, consider how to reconcile this.

That’s the basic argument. Below I will go over some clarifications, a few reasons the jumps between the corps might be asymmetric, and the implications of high speedups from AutomatedCorp.

## Clarifications

There are a few potentially important details which aren't clear in the analogy, written in the context of the jump from NormalCorp to AutomatedCorp:

- The way I set up the analogy makes it seem like AutomatedCorp has a serial compute advantage: because they have 50 years they can run things that take many serial years while NormalCorp can't. As in, the exact analogy implies that they could use a tenth of their serial time to run a 5 year long training run on 50k H100s, while they could actually only do this if the run was sufficiently parallelizable such that it could be done on 2.5 million H100s in a tenth of a year. So, you should ignore any serial compute advantage. Similarly, you should ignore difficulties that SlowCorp might have in parallelizing things sufficiently etc.
    
- At the time this takes place, AutomatedCorp has already made sufficient algorithms progress that they can run pretty smart AIs quite cheaply, making experiments on somewhat capable AIs much cheaper. Concretely, you can imagine that they can run AIs as good as the best human AI researchers at 50x speed on only ~10 H100s (or they can run a 1x speed AI on 1/5 of an H100’s worth of compute ignoring the efficiency gains from running the AI slower). This comes from thinking they are using 1/5 of their compute for researcher inference and this compute results in a roughly 1 to 1 correspondence between H100s and parallel researcher instances (with 10 million H100s and 10 million researcher instances)[3](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-3-163243860) Maybe they can do a qualitatively GPT-4 level training run in around 15k H100 hours or a week with 100 H100s (5e22 FLOP) though the resulting AI would be worse at next token prediction but compensate in other ways to be similar to GPT-4 on downstream tasks.
    
- It would be possible (at least in principle) for AI researchers to be comparable to (or better than) any individual human researcher while simultaneously being worse than a group of human researchers due to the AIs having less cognitive diversity which results in them not finding the best ideas. I’m assuming this diversity difficulty has been overcome such that this doesn’t make a big difference.
    

## Asymmetries

Why would there be any particular reason why the current regime was special such that scaling up labor (including quality and speed) is highly asymmetric from scaling down labor?

Here I’ll cover asymmetries between the jumps from SlowCorp to NormalCorp and NormalCorp to AutomatedCorp.

- **Scaling up and down the amount of parallel workers might not be symmetric due to parallelization penalties which increase with more employees.** I've attempted to compensate for this pretty aggressively by making the drop in SlowCorp's employees relative to NormalCorp only 5x while there is a 50x increase between NormalCorp and AutomatedCorp. (This is approximately equivalent to assuming that the parallelization exponent is 0.7 when going from 800 to 4,000 employees but 0.3 when going from 4,000 to 200,000 employees. As in, (4000 / 800)^0.7 ~= (200000 / 4000)^0.3.
    
- **1 year might be a more natural timescale for humans doing work than 1 week due to start up times or context switching.** As in, the amount you can get done in a year is actually more than 50x more than what you could do in a week. You can just try to ignore these sorts of costs when thinking about the analogy, compensate by giving the SlowCorp employees 2 weeks (while still having 10 million H100 years over these 2 weeks), or just talk about how long it takes for the SlowCorp employees to match NormalCorp to get at the relevant slow down. However, it's worth noting that to the extent that it's hard to get certain types of things done in a week, this could also apply to 1 year vs 50 years. We might think that 50 serial years is more than 50x better than 1 year due to reduced start up costs, less context switching, and other adaptations. So, in this way the situation could be symmetric, but I do expect that the 1 week vs 1 year situation is more brutal than the 1 year vs 50 year situation given how humans work in practice.
    
- **The quality of the best researchers matters more than the quality of the median researcher.** In SlowCorp, we fixed every researcher to the quality of the median frontier AI company researcher while in AutomatedCorp, we fixed every researcher to the quality of the (near) best frontier AI company researcher. The SlowCorp change doesn’t change the median researcher, but does make the best researcher worse while the AutomatedCorp change makes the median researcher much better while preserving the quality of the best researchers. You might think this is asymmetric as having a small number of very good researchers is very important, but having a larger number doesn’t matter as much. To make the situation more symmetric, we could imagine that SlowCorp makes each researcher worse by as much as the median frontier AI company researcher is worse than the best few frontier AI company researchers (so now the best researcher is as good as the median frontier AI company researcher while the median researcher is much worse) and that AutomatedCorp makes each researcher better by this same amount making the previously best researcher very superhuman. I avoided this as I thought the intuition pump would be easier to understand if we avoided going outside the human range of abilities and the initial situation with automated AI R&D is likely to be closer to having a large number of researchers matching the best humans rather than matching human variation while having a small number of superhuman researchers (though if inference time compute scaling ends up working very well, this type of variation is plausible).
    
- **You might expect the labor force of NormalCorp to be roughly in equilibrium where they gain equally from spending more on compute as they gain from spending on salaries (to get more/better employees).** SlowCorp and AutomatedCorp both move the AI company out of equilibrium, which could (under some assumptions about the shape of the production function for AI R&D) make the slowdown from SlowCorp larger than the improvement from AutomatedCorp. As in, consider the case of producing wheat using land and water: if you had 100x less water (and the same amount of land) you would get a lot less wheat while having 100x more water available wouldn't help much. However, I'm quite skeptical of this type of consideration making a big difference because the ML industry has already varied the compute input massively, with over 7 OOMs of compute difference between research now (in 2025) vs at the time of AlexNet 12 years ago, (invalidating the view that there is some relatively narrow range of inputs in which neither input is bottlenecking) and AI companies effectively can't pay more to get faster or much better employees, so we're not at a particularly privileged point in human AI R&D capabilities. I discuss this sort of consideration more in this [comment](https://www.lesswrong.com/posts/XDF6ovePBJf6hsxGj/will-compute-bottlenecks-prevent-a-software-intelligence-1?commentId=4arc3J2Z3G68rmrpi).
    
- **You might have a mechanistic understanding of what is driving current AI R&D which leads you to specific beliefs about the returns to better labor being asymmetric** (e.g., that we’re nearly maximally effective in utilizing compute and making all researchers much faster wouldn’t matter much because we’re near saturation). I’m somewhat skeptical of this perspective as I don’t see how you’d gain much confidence in this without running experiments to see the results of varying the labor. It’s worth noting that to have this view, you must expect that in the case of SlowCorp you would see different observations that would have led you to a different understanding of AI R&D in that world and we just happen to be in the NormalCorp world (while SlowCorp was equally a priori plausible given the potential for humans to have been slower / worse at AI R&D, at least relative to the amount of compute).
    

There are some reasons you might eventually see asymmetry between improving vs. degrading labor quality, speed, and quantity. In particular, in some extreme limit you might e.g. just figure out the best experiments to run from an ex-ante perspective after doing all the possibly useful theoretical work etc. But, it's very unclear where we are relative to various absolute limits and there isn't any particular reason to expect we're very close. One way to think about this is to imagine some aliens which are actually 50x slower than us and which have ML researchers/engineers only as good as our median AI researchers/engineers (while having a similar absolute amount of compute in terms of FLOP/s). These aliens could consider the exact same hypothetical, but for them, the move from NormalCorp to AutomatedCorp is very similar to our move from SlowCorp to NormalCorp. So, if we're uncertain about whether we are these slow aliens in the hypothetical, we should think the situation is symmetric and our guesses for the SlowCorp vs. NormalCorp and NormalCorp vs. AutomatedCorp multipliers should be basically the same.

(That is, if we can't do some absolute analysis of our quantity/quality/speed of labor which implies that (e.g.) returns diminish right around now or some absolute analysis of the relationship between labor and compute. Such an analysis would presumably need to be mechanistic (aka inside view) or utilize actual experiments (like I discuss in the one of the items in the list above) because analysis which just looks at reference classes (aka outside view) would apply just as well to the aliens and doesn't take into account the amount of compute we have in practice. I don't know how you'd do this mechanistic analysis reliably, though actual experiments could work.)

## Implications

I've now introduced some intuition pumps with AutomatedCorp, NormalCorp, and SlowCorp. Why do I think these intuition pumps are useful? I think the biggest crux about the plausibility of a bunch of faster AI progress due to AI automation of AI R&D is how much acceleration you'd see in something like the AutomatedCorp scenario (relative to the NormalCorp scenario). This doesn't have to be the crux: you could think the initial acceleration is high, but that this progress will very quickly slow due to diminishing returns on AI R&D effort biting harder than how much improved algorithms yield faster progress due to smarter, faster, and cheaper AI researchers which can accelerate things further. But, I think it is somewhat hard for the returns (and other factors) to look so bad that we won't at least have the equivalent of 3 years of overall AI progress (not just algorithms) within 1 year of seeing AIs matching the description of AutomatedCorp if we condition on these AIs yielding an AI R&D acceleration multiplier of >20x[4](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-4-163243860)

Another potential crux for downstream implications is how big of a deal >4 years of overall AI progress is. Notably, if we see 4 year timelines (e.g. to the level of AIs I've discussed), then 4 years of AI progress brought us from the systems we have now (e.g. o3) to full AI R&D automation, so another 4 years of progress feels intuitively very large[5](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-5-163243860) Also, if we see higher returns to some period of AI progress (in terms of ability to accelerate AI R&D), then this makes [a super-exponential loop where smarter AIs build ever smarter AI systems faster and faster](https://www.lesswrong.com/posts/tMHPQ5SDzm8gugoBN/will-ai-r-and-d-automation-cause-a-software-intelligence-1) more likely. Overall, shorter timelines tend to imply faster takeoff (at least evidentially, the causal story is much more complex). I think sometimes disagreements about takeoff would be resolved if we condition on timelines and what the run up to a given level of capability looks like, because the disagreement is really about the returns to a given amount of AI progress.

Thanks for reading AI Futures Project!

[1](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-anchor-1-163243860)

And below median, but that shouldn’t have as big of an effect as removing the above median employees.

[2](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-anchor-2-163243860)

These are basically just the estimates for the number of copies and speed at the point of superhuman AI researchers in [AI 2027](https://ai-2027.com/), but I get similar numbers if I do the estimate myself. Note that (at least for my estimates) the 50x speed includes accounting for AIs working 24/7 (a factor of 3) and being better at coordinating and sharing state with weaker models so they can easily complete some tasks faster. It’s plausible that heavy inference time compute use implies that we’ll initially have a smaller number of slower AI researchers, but we should still expect that quantity and speed will quickly increase after this is initially achieved. So, you can think about this scenario as being what happens after allowing for some time for costs to drop. This scenario occurring a bit after initial automation doesn’t massively alter the bottom line takeaways. (That said, if inference time compute allows for greatly boosting capabilities, then at the time when we have huge numbers of fast AI researchers matching the best humans, we might also be able to run a smaller number of researchers which are substantially qualitatively superhuman.)

[3](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-anchor-3-163243860)

Interestingly, this implies that AI runtime compute use is comparable to humans. Producing a second of cognition from a human takes [perhaps 1e14 to 1e15 FLOP](https://www.alignmentforum.org/posts/LY7rovMiJ4FhHxmH5/thoughts-on-hardware-compute-requirements-for-agi#3_1_Compute__1e14_FLOP_s_seems_like_more_than_enough) or between 1/10 to 1 H100 seconds. We're imagining that AI inference takes 1/5 of an H100 second to produce a second of cognition. While inference requirements are similar in this scenario, I’m imagining that training requirements start substantially higher than human lifetime FLOP. (I’m imagining the AI was trained for roughly 1e28 flop while human lifetime FLOP is more like 1e23 to 1e24.) This seems roughly right as I think we should expect faster inference but bigger training requirements, at least after a bit of adaptation time etc., based on how historical AI progress goes. But this is not super clear cut.

[4](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-anchor-4-163243860)

And we condition on reaching this level of capability prior to 2032 so that it is easier to understand the relevant regime, and on the relevant AI company going full steam ahead without external blockers.

[5](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition#footnote-anchor-5-163243860)

The picture is a bit messy because I expect AI progress will start slowing due to slowed compute scaling by around 2030 or so (if we don’t achieve very impressive AI by this point). This is partially due to continued compute scaling requiring [very extreme quantities of investment by this point](https://www.lesswrong.com/posts/XiMRyQcEyKCryST8T/slowdown-after-2028-compute-rlvr-uncertainty-moe-data-wall) and partially due to fab capacity running out as ML chips eat up a larger and larger share of fab capacity. In such a regime, I expect a somewhat higher fraction of the progress will be algorithmic (rather than from scaling compute or from finding additional data), though not by that much as algorithmic progress is driven by additional compute instead of additional data. Also, the rate of algorithmic progress will be slower at an absolute level. So, 20x faster algorithmic progress will yield a higher overall progress multiplier, but progress will also be generally slower. So, you’ll maybe get a lower number of 2024-equivalent years of progress, but a higher number of 2031-equivalent years of progress.

[

![AI Futures Project](https://substackcdn.com/image/fetch/$s_!iyu_!,w_96,h_96,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3409cfd0-9243-479e-80f9-d0e3922c450a_132x132.png)



](https://blog.ai-futures.org/)

#### Recommend AI Futures Project to your readers

Preparing for a world with AGI

[](https://substack.com/profile/13977520-tw)[](https://substack.com/profile/17491461-simonh)[](https://substack.com/profile/29493652-davey)[](https://substack.com/profile/25661891-thomas-larsen)[](https://substack.com/profile/312428288-romeo-dean)

35 Likes∙

[2 Restacks](https://substack.com/note/p-163243860/restacks?utm_source=substack&utm_content=facepile-restacks)

|   |   |
|---|---|
|[](https://substack.com/@ryangreenblatt?utm_source=byline)|A guest post by<br><br>\|   \|   \|<br>\|---\|---\|<br>\|[Ryan Greenblatt](https://substack.com/@ryangreenblatt?utm_campaign=guest_post_bio&utm_medium=web)<br><br>I work at Redwood Research on technical AI security+safety research.\|[Subscribe to Ryan](https://blog.redwoodresearch.org/subscribe?email=weinbaumjonah%40gmail.com&autoSubmit=true&utm_source=substack&utm_campaign=guest_post_bio&utm_medium=web)\||

#### Discussion about this post

[](https://substack.com/profile/9319587-andrewb?utm_source=comment)

[andrewb](https://substack.com/profile/9319587-andrewb?utm_source=substack-feed-item) 

[Two faced conversations](https://andrewdbl.substack.com/?utm_content=comment_metadata&utm_source=substack-feed-item)[May 19, 2025](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition/comment/118485262 "May 19, 2025, 4:05 PM")

Interesting and I can see how ai automation will speed up the research that is carried out within the theoretical models.

At some point something has to be actually built and used in the real world.

If the thing you are building is a better delivery optimisation tool or chess or go, it is relatively easy to define and so we zoom into the distance.

If the thing you are building is a word processor or a screwdriver - where better is not easily definable, you need humans.

As models improve you may be able to pass results out less frequently but (generally at the moment) You will want a human in the loop who can understand that a sonic screwdriver with a 500 yard range may be an awesome screwdriver but in the hands of a teenager is non optimal.

Indeed the first signs of superhuman reasoning may be when the ai states something is a bad idea and no human would have thought of that until thew saw the explanation.

Like (3)

Reply

Share

[](https://substack.com/profile/29659703-eskimo1?utm_source=comment)

[Eskimo1](https://substack.com/profile/29659703-eskimo1?utm_source=substack-feed-item) 

[May 21, 2025](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition/comment/119009531 "May 21, 2025, 12:50 PM")

Now that we know Vance has read AI 2027(!), it seems clear that minds are opened here at high levels of govt. Have you guys given consideration to presenting a path/scenario you’d actually like to see occur?

That Vance has 1. Read your paper and 2. Didn’t glibly dismiss it as sci-fi/decel suggests that you have his ear and they’re willing to listen, but what’s needed is a positive vision forward, which I suspect they need laid out to them.

Like

Reply

Share

[1 more comment...](https://blog.ai-futures.org/p/slow-corporations-as-an-intuition/comments)

[Early US policy priorities for AGI](https://blog.ai-futures.org/p/early-us-policy-priorities-for-agi)

[Near-term AI policy is confusing, except for these two recommendations](https://blog.ai-futures.org/p/early-us-policy-priorities-for-agi)

Dec 8, 2025 • [Nick Marsh](https://substack.com/@zzzdot)

72

12

9

![](https://substackcdn.com/image/fetch/$s_!kyVK!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19288615-5e21-4586-83fb-4ed8c4a3ac4d_2565x1115.png)

[What you can do about AI 2027](https://blog.ai-futures.org/p/what-you-can-do-about-ai-2027)

[How to steer toward a positive AGI future](https://blog.ai-futures.org/p/what-you-can-do-about-ai-2027)

Jun 28, 2025 • [Eli Lifland](https://substack.com/@elifland)

158

27

21

![](https://substackcdn.com/image/fetch/$s_!XTB-!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb716414c-ccc3-4652-a6f0-8a18149024d4_644x644.webp)

[AI As Profoundly Abnormal Technology](https://blog.ai-futures.org/p/ai-as-profoundly-abnormal-technology)

[....](https://blog.ai-futures.org/p/ai-as-profoundly-abnormal-technology)

Jul 24, 2025 • [Scott Alexander](https://substack.com/@astralcodexten)

224

47

49

![](https://substackcdn.com/image/fetch/$s_!Avx0!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a7e6fb0-72f0-4467-a251-ba0f3a4e4c73_1302x719.png)

© 2026 AI Futures Project · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://your.substack.com/publish)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com/) is the home for great culture