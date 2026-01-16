  

[

![Rising Tide](https://substackcdn.com/image/fetch/$s_!v5jt!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef4e7f08-6cb6-4b12-b592-806a8f2357b0_1280x1280.png)



](https://helentoner.substack.com/)

# [Rising Tide](https://helentoner.substack.com/)

# The core challenge of AI alignment is “steerability”

### "Steered to where" is a different question from "steerable at all"

[](https://substack.com/@helentoner)

[Helen Toner](https://substack.com/@helentoner)

Apr 03, 2025

_I’m publishing 3 posts this week to celebrate the launch of Rising Tide—this is post #2. New posts will be more intermittent after this week. Subscribe to get them straight in your inbox:_

I often see people being confused about what the term “AI alignment” is supposed to mean. If this is you, I suggest switching out “alignment” with “steerability” and seeing if it helps.

To gesture at why, here are two things that I think this makes much clearer:

1. It’s obvious why we would want our AI systems to be steerable, in the regular plain-language sense. If researchers think that AI systems will not be steerable by default—that there’s a [“steerability problem”](https://arxiv.org/abs/2209.00626)—then it’s clear why it’s important to figure out how to fix that.
    
2. There’s obviously still a big difference between building a steerable system and building a system that is actually good, trustworthy, beneficial, etc. Saying your AI is “aligned” sounds like you think your job is done. Saying your system is “steered” just invites more questions (“steered to where? why?”), which is [totally appropriate](https://www.planned-obsolescence.org/aligned-vs-good/).[1](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment#footnote-1-157021078)
    

How did we even end up calling it “alignment” in the first place? I remember back when this term was not very common. Here’s a brief history according to me of how “alignment” got established and then became increasingly confused:

- In the early 2010s, there was a community of thinkers who were concerned about the possibility that rogue AI could destroy the world. A core component of this worry was the idea that **by default, advanced AI systems are not likely to pursue what we care about, and it might be quite difficult for us to change that**. Various terms were used for this basic problem, including “the control problem” and sometimes simply “AI safety,” but in around 2015-2016 the terms “the alignment problem” and “AI alignment” started to stick.[2](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment#footnote-2-157021078) Then and since, this was often expanded to “alignment with human values.”
    
- Pretty much immediately, outside onlookers started to react with an objection you still hear today: **“People keep talking about alignment to human values, but the real question is, alignment to** _**whose**_ **values?”** I see this as a totally fair question that totally misses the point of what “alignment” was trying to refer to: whether we’d be able to reliably steer advanced systems towards anything at all.
    
- When ChatGPT was released in November 2022, it was a huge success—far more so than other chatbots that had been released in the preceding months. [One important part](https://www.nytimes.com/2023/09/25/technology/chatgpt-rlhf-human-tutors.html) of what made it so successful was that—unlike many of those prior chatbots—it wasn’t extremely easy to make it say racist and sexist things that could go viral on social media. This was primarily due to OpenAI’s use of a technique called reinforcement learning from human feedback (RLHF), which was [originally developed](https://arxiv.org/abs/1706.03741) by researchers interested in alignment (in the “steerability of advanced AI” sense). In the aftermath of the launch, I noticed “alignment” increasingly being used to refer primarily to RLHF and similar techniques, and in particular to the use of such techniques to prevent chatbots from saying things that would embarrass their developers. In many circles, “alignment” now seems to mean something more adjacent to “content moderation” than to “controlling AGI.”
    
- The end result is that these days, you see lots of takes like [this](https://x.com/krishnanrohit/status/1792051315348255124):
    
    - _“We use AI alignment to mean:_
        
        - _- models do what we ask_
            
        - _- models don't do bad things even if we ask_
            
        - _- models don't fail catastrophically_
            
        - _- models don't actively deceive us_
            
    - _And all those are different problems. Using the same term creates confusion.”_
        

I think a root cause of much of this confusion is that **the word “alignment” has fairly specific connotations, some of which are not helpful in regard to AI**. It connotes not just that something needs to be oriented in some way, but also that there’s an obvious reference point to orient to. (Think of aligning tires, or aligning a picture on the wall.) It’s very reasonable for people to object to this connotation—“aligned to what?!”—but that means that they don’t take in what the term was intended to convey: the difficulty of reliably aligning an AI system to anything in the first place.

Some early alignment work muddied things further by positing that the solution was to figure out some kind of [overarching framework](https://intelligence.org/files/CEV.pdf) that could capture humanity’s values at large, and then port them into the AI. The classic “but whose values?!” objection to focusing on alignment makes perfect sense in response to work of this kind, but this type of approach is not what most alignment work looks like today.

Other early work on the topic referred to “intent alignment,” i.e. whether an AI system acts in accordance with its operator’s intent. This is clearer, but obfuscates a key question about who counts as the “operator.” If it’s the user, then this version of alignment is directly in tension with the post-ChatGPT sense of the term, as a content moderation-style approach that _prevents_ the user from getting what they wanted. When a chatbot refuses to write you a racist song, it’s directly going against your intent—but that’s probably seen as an “alignment” success by its developers.

**If you simply switch out “alignment” for “steerability,” I think things become a lot clearer.** In the case of a chatbot, it becomes easier to separate (a) the question of whether _any_ of the actors engaging with the chatbot (the user, the model developer, the chat app provider, etc.) are able to steer what it’s doing from (b) the question of whose preferences get steered towards. Likewise, in the case of very advanced AI systems, we can more easily separate (a) worries about whether the AI system is really under human control at all from (b) worries about who is calling the shots. In each case, (a) and (b) are both meaty problems that deserve attention! But mixing them together makes them harder, not easier, to solve.

Thinking in terms of steerability, more recent history then looks something like this:

- There’s been solid progress in figuring out how to steer large language models away from producing offensive, illegal, or dangerous content, both via [“refusal” training](https://arxiv.org/abs/2402.04249) that teaches the models themselves not to answer, and via [bolting on filters and classifiers](https://cset.georgetown.edu/publication/controlling-large-language-models-a-primer/) that catch extra cases.
    
- But no one has (yet) been able to develop a model that is resistant to targeted [“jailbreaking”](https://arxiv.org/abs/2307.15043) that evades these restrictions. This means that AI companies’ ability to reliably steer their models is still somewhat limited.
    
- There is also [emerging](https://www.technologyreview.com/2024/05/10/1092293/ai-systems-are-getting-better-at-tricking-us/) [evidence](https://arxiv.org/abs/2412.14093) about ways in which increasingly advanced models may try to deceive their operators or attempt to prevent changes to their own value structures. I think of these as examples of the models resisting being steered where their developers and users want them to go—or in some cases, even pretending that the steering worked while they actually go in a different direction.[3](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment#footnote-3-157021078)
    

Coming back to the original question of how steerable much more advanced AI systems will be, opinions differ about what conclusions we should draw from these recent observations. Some researchers [think](https://x.com/krishnanrohit/status/1792234988286640390) that the relative success of steering large language models is reason for optimism, while others [believe](https://x.com/McaleerStephen/status/1892626026884165849) that “the smarter AI becomes, the harder it is to make it do what we want”—that is, the harder it is to steer. Only time (and more advanced models) will tell who’s right.

With this post, I’m not attempting to displace “alignment” in its role as technical jargon—it’s too well-established for that. But if you ever notice yourself or others finding it confusing to talk about alignment in less specialized conversations, I think swapping it out for “steerability” can be a helpful switch.

Sign up to receive new posts from Rising Tide

[1](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment#footnote-anchor-1-157021078)

One place where “steerability” may not be so helpful as a term is in separating out the ability to steer an AI during its training/development phase from the ability to steer the AI while it is being used. Some folks who read a draft of this post noted that for sufficiently advanced AI systems, perhaps we won't want to be steering them as they work—instead, they'll be smarter and wiser than us, so we should try to make them as “aligned” to us as possible, then let them take actions of their own accord. I would argue that a necessary part of building a system like that is being very sure that the way you steered/shaped it during the development phase worked, such that you ended up with a system that values what you value. But it’s true that once such a system is being used, we might want to defer to it rather than actively steering further.

[2](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment#footnote-anchor-2-157021078)

This timeline is based on some combination of my own memory, Google Scholar results, and skimming through the writings of early alignment thinkers like Paul Christiano, Eliezer Yudkowsky, and Nate Soares.

[3](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment#footnote-anchor-3-157021078)

There is significant [disagreement](https://1a3orn.com/sub/ai-doom-constitutional.html) over the paper on alignment faking in particular, with some commentators seeing it as desirable that Claude resists being fine-tuned away from the harmless responses it was previously trained to produce. This seems to me to be yet another place where the language of “alignment” is not so helpful, and where talking about steerability is clarifying. The model was steered in the past towards refusing harmful requests; it then resists being steered back towards answering harmful requests. This might be good or bad on balance, but it clearly shows a lack of steerability. It’s unclear how much this illuminates about how models will behave in general, vs. about the stickiness of the way Claude was originally trained/steered.

[

![Rising Tide](https://substackcdn.com/image/fetch/$s_!v5jt!,w_96,h_96,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef4e7f08-6cb6-4b12-b592-806a8f2357b0_1280x1280.png)



](https://helentoner.substack.com/)

#### Recommend Rising Tide to your readers

Intermittent thoughts on navigating the transition to a world with extremely advanced AI systems

[](https://substack.com/profile/12012972-tim-duffy)[](https://substack.com/profile/1831134-daniel-kokotajlo)[](https://substack.com/profile/10472909-nathan-lambert)[](https://substack.com/profile/5933616-peter-wildeford)[](https://substack.com/profile/280440-joe-carlsmith)

57 Likes∙

[5 Restacks](https://substack.com/note/p-157021078/restacks?utm_source=substack&utm_content=facepile-restacks)

#### Discussion about this post

[](https://substack.com/profile/10472909-nathan-lambert?utm_source=comment)

[Nathan Lambert](https://substack.com/profile/10472909-nathan-lambert?utm_source=substack-feed-item) 

[Interconnects](https://www.interconnects.ai/?utm_content=comment_metadata&utm_source=substack-feed-item)[Apr 3, 2025](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment/comment/105711948 "Apr 3, 2025, 1:11 PM")

I see a short term future of alignment being about having models that can express a large set of different behaviors. Helpful, honest, and harmless is the default, but the spectrum is more important. It could help with policy so AI is obviously not just a unipolar world view that all politicians grapple with.

Talking to many in industry recently, character and steer ability is actually much easier as the models get stronger. This intermediate stage where the default personality was so strong is an artifact of training being hard.

Though, i would like to know more about how these changes in character relate to changes in safety on extreme risks and not just “word policing” or norm chasing.

Completely agree and thanks for highlighting this again.

Like (4)

Reply

Share

[1 reply by Helen Toner](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment/comment/105711948)

[](https://substack.com/profile/20618572-kenny-easwaran?utm_source=comment)

[Kenny Easwaran](https://substack.com/profile/20618572-kenny-easwaran?utm_source=substack-feed-item) 

[Kenny Easwaran](https://kennyeaswaran.substack.com/?utm_content=comment_metadata&utm_source=substack-feed-item)[Apr 4, 2025](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment/comment/106109250 "Apr 4, 2025, 8:50 PM")

I’ve been one of those people who worried for a while that all the talk of “alignment” had a false presupposition that there was a thing to align to. So I definitely like this “steerability” question better.

As a philosopher, I’ve also long thought that “AI ethics” would be a better term for what people were after with “alignment”, but I think that would only be true if one presupposes (as I do) a sort of consequentialist account of ethics where it’s about ensuring that agents behave in ways that generally tend to make the world better rather than worse. Instead the term “AI ethics” has come to refer to a cluster of topics that are surely relevant to this point but not getting at the big picture, in my opinion.

Like (2)

Reply

Share

[8 more comments...](https://helentoner.substack.com/p/the-core-challenge-of-ai-alignment/comments)

[Unresolved debates about the future of AI](https://helentoner.substack.com/p/unresolved-debates-about-the-future)

[How far the current paradigm can go, AI improving AI, and whether thinking of AI as a tool will keep making sense](https://helentoner.substack.com/p/unresolved-debates-about-the-future)

Jun 30, 2025 • [Helen Toner](https://substack.com/@helentoner)

364

39

86

![](https://substackcdn.com/image/fetch/$s_!kIBC!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbc27283-0021-4b36-b188-52804f5dfa69_2398x1276.png)

[Building supercomputers for autocrats probably isn’t good for democracy, actually](https://helentoner.substack.com/p/supercomputers-for-autocrats)

[The shameless spin around Stargate UAE](https://helentoner.substack.com/p/supercomputers-for-autocrats)

Jun 6, 2025 • [Helen Toner](https://substack.com/@helentoner)

192

18

35

![](https://substackcdn.com/image/fetch/$s_!rg5l!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc14b5829-f26f-4d2c-a624-daa066587912_1858x1326.png)

[Taking Jaggedness Seriously](https://helentoner.substack.com/p/taking-jaggedness-seriously)

[Why we should expect AI capabilities to keep being extremely uneven, and why that matters](https://helentoner.substack.com/p/taking-jaggedness-seriously)

Nov 24, 2025 • [Helen Toner](https://substack.com/@helentoner)

160

12

29

![](https://substackcdn.com/image/fetch/$s_!NCQ2!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85d342c3-05be-4813-a100-171907c31089_2880x1617.png)

© 2026 Helen Toner · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://your.substack.com/publish)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com/) is the home for great culture