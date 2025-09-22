[Skip to main content](https://otter.ai/#main-content)

Connect your Zoom account so Notetaker can join meetings you host

[](https://otter.ai/home)

[](https://otter.ai/home)[](https://otter.ai/home)

[

](https://otter.ai/home)

[](https://otter.ai/otter-chat)[

](https://otter.ai/setting/connected_apps)

[](https://otter.ai/group)

[](https://otter.ai/direct-messages)

[](https://otter.ai/folder)

![](https://profile.otter.ai/AO5TT6NCA6NC7ONB/AO5TT6NCA6NC36AR)Kirubel Abiyu (i-Cog)

Aug 20 at 2:00 am

30 min

Shared with: adam.vandervorst@gmail.com, Adam Vandervorst, adam@trueagi.io, adricktench@gmail.com, akolonin@gmail.com, alexey.glushchenko@singularitynet.io, Alexey Potapov, Amen Belayneh, amenbelayneh@gmail.com, André Senna, Anton Onishchuk (NAINT), anton.poponin@singularitynet.io, anton@singularitynet.io, aonishchuk@naint.ru, arseniy.losev@singularitynet.io, Andres Suarez Madrigal, asya.lyanova@singularitynet.io, basliel.amsalu@singularitynet.io, Ben Goertzel, Benjamin Goertzel, Berick Cook, birhane.gulilat@singularitynet.io, calloquillick@gmail.com, Charlie Derr, clarke.remy@gmail.com, Number4 x, Deborah Duong, Dianne Krouse, Dmitry Kaplun, Douglas Miles, Edmund Daniels, Edgar Brissow, Esubalew Amenu (i-Cog), evgeny.bochkov@singularitynet.io, Eyasu Birhanu (i-Cog), Eyob Derese (i-Cog), E Y, Eyobed Abreham (i-Cog), greg.meredith@singularitynet.io, Haley Lowy, Hamza Laaqira, Hedra Seid, Ibby Benali, igor.mlvts@gmail.com, Ilya Fedotov, Innokenty Zhdanov, james.cash@occasionallycogent.com, Janet Adams, Mike Archbold, Jonathan Warrell, kenric.nelson@photrek.world, Kevin R.C., Khellar Crawford, Kirill Yesalov, manhin, levu2001.amser@gmail.com, Lucius Meredith, liya.habtemariam@singularitynet.io, Douglas Miles, luke.gniwecki@singularitynet.io, luke.peterson@singularitynet.io, marco.capozzoli@singularitynet.io, Matthew Ikle, Michael Duncan, Mike Pavlenko, mpavlenko@naint.ru, Nejc Znidar, Lake Watkins, Nil Geisweiller, Pamela Mackay, Patrick Hammer, peter.isaev@singularitynet.io, pgwadapool@gmail.com, rafael.levi@singularitynet.io, robert.haas@protonmail.com, Robert Werko, roberthaas@protonmail.com, Roman Reinhard Treutlein, roy@orange-kiwi.com, rune.kek@gmail.com, rvvessum@gmail.com, Sarah Isakson, Saulo Augusto, sergey@singularitynet.io, Sergey Shalyapin, stassapatsantzi@gmail.com, Surafel Fikru (i-Cog), Tewodros Nibret, thomask@rawpowergames.com, trikua.misganaw@singularitynet.io, Vesselin Malev, Vita Potapova, Vitaly Bogdanov, vsbogd@gmail.com, wolf@rawpowergames.com, Wondwossen Regasa (i-Cog), Abdulrahman Semrie, Yeabsira Derese (i-Cog), Yeabsira Nigusse, yuri@tenuki.org

Summary

Transcript

## Keywords

MORKification Weekly, note takers, accepted behavior, new laptop, dual boot, Python world, VS code, Emacs, database parallel, memory bandwidth, GPU clusters, neural networks, graph databases, query planning, heterogeneous sources.

## Speakers

Adam (53%), Sergey (28%), Charlie (9%), Remy (5%), Igor (3%), Speaker 1 (1%), Speaker 2 (<1%)

So many note takers, I don't know where mine is. Why isn't it here? Well, you got a notebook, right?

Words, I have notebooks, another computer to type on, another window to type in. How are you

doing? All right, just some stuff I thought would have gotten done. It's taking longer because of what's a good way of putting it. We have. We're slowly coming to a Quakers consensus about what the right the right semantics and stuff are, and it's and making a distinction between accepted behavior and error, and I have to attend on the I have to shift my focus on the idea of it being accepted behavior rather than errors, and that that's confusing For some people in the team. So that's all small stuff, but hopefully I'll be able to move on to some other part of the work. How about you? What are you up to?

Wasting a lot of time doing something that I enjoy way too much, which is I got a I got a new laptop, and so trying to make sure I get it tuned absolutely perfectly. This time, I used to do an awful lot of this, and I sort of scrambled quickly when I bought a laptop, when I started working in February or March, and didn't do it great. So now I've got another one, right? Both of them have GPUs, and my work involves training models, so I wanted to have things locally, but it means that just, you know, I decided to try to go back to what I haven't done for 20 years, which is to dual boot Windows, rather than I used to just white Windows, Linux. Hello,

Hey, Adam. So Oh.

So it got so excited about that that I went, you know, after I got this one doing pretty well, I went back to the one that I bought in February or March, and wiped it. And now, so now it's sort of semi brick for the moment. Let's see. I'll be able to resurrect it, but it's going to take even more time, which will take me away from doing productive stuff rather than fussing with tooling, right?

Well, hopefully it'll your mind will be clear once you're done with it.

Yeah, that's that's an optimistic Of course. I'll move on to some other obsession about tooling. I'm still trying to figure out whether, in the Python world, right? It seems like with large code bases and not enough of an emacs guru. So do I use VS code or something else,

or join the Emacs site and become a guru?

I've been using emacs forever, but I just find that I really like the the features and these other things that sort of come out of the box and don't require me learning e Lisp or something in order to, you know, jump to functional definitions in another file or something

without e list. You don't know emacs

Well, there you go. Can I say I'm an aspiring e list programmer. I know much of it as I know in Haskell, which is not very much.

So quick headset, I'm sick, and I'm also, I couldn't work from home because there were people drilling out the pavement right in front of the building. So I'm, like, using, using, like, my phone as a microphone in the remote battery back. But I do have like, a couple of like, aside from the obvious discussion and the and the topic that we said, I do have a small presentation just to make some some things clear that people have been asking about and that are rightfully confusing, there is such a thing. And then I hope that we can, we can also have a, have an idea on, on the priority itself, some topics to cover. So there is a i said i to original lists. That's the original list. This is progressing nicely, but I feel like there, there should be some more. I and some more ways for folks to to engage. And besides, because these tend to be quite, quite focused and technical on specific subjects, but I feel like there is also more that can be done to allow more people to use it and understands how they can apply to their use case. I

I'm also just back from Iceland, so I'm reading the mattermost chat. Always amusing. Do we have the icon here? No, it's probably like a ungodly hour there. I

uh, Adam, hi. If you're waiting for someone, I have a really quick topic to raise for you. Go for it, please. For like, several minutes, go for it. Yeah, I just haven't had a discussion with folks who are doing database parallel, like heavily parallel database installations for for the most universities they do, Oxford, Cambridge, you might see many places, and we were discussing, like aggressive in Remy based supply of compute. I'm trying, I'm trying to solve this, remembering the problem on some level, even on conceptual one. So the idea here is we can potentially give 100 gigabytes per second directly to pure CPU in CPU, that will be cash bottleneck, definitely. And we can separate to discuss how cache is managed. But on the level of ask alone, as I think that might be direct supply, what do you think generally about, about the idea

that's really cool. So Igor was able to run mark on Escalon in the both the simulator, or, like, both cam and whisper, yeah, that's exciting. And then, yeah, the we put a lot of effort in actually making more somewhat flexible to run on different platforms. So if we can, if we can exploit that's, I think computing near memory for graph databases makes a ton of sense. We are, like most of these workloads, are extremely parallel, and there is no way to leverage that parallelism because we are they're bands with bottleneck, right? So, yeah, increasing the bandwidth by localizing the compute makes a lot of sense.

So here we will definitely have a sort of network bottleneck problem. But we can also dive into deeper anyway, like 100 gigabytes of supply, of direct supply might be really, really, really tempting. It's per core. In fact, the computing core they can give, and that's definitely needs building the race.

You have an actual document to share on this, because there is, of course, like, a lot of technical details to go over here.

Yeah, we just, we just, we just, like writing different, you know, different, different sketches for now, so I can give you more detail a bit later. But what folks are doing, they just work in the general process for, like, general research. And they started from like loose Luther like implementations. But the point is, it's low level code which can operate in VM, in VM, quite efficiently so on Ask alongs that might be strategic. And that's also imagery was on the meeting, and we are working on this, we can set up sort of separate internal meeting to discuss how we how we model that in Cayman whisper, then digging deeper and also trying to implement, implement work. That's why ISA is asking a lot of questions to you. I think she's working on just like direct implementations, but at the same time we can, we can try to port more into the simulations to try ask alone, because we have before we have us colon in hardware, right? So can try this. But I'm trying to work on memory supply in parallel, and maybe, maybe in the year on PCI six, in combination with this low level, low level code of memory supply might be the key. I'm also considering, like building GPU clusters for that, like having quite, quite, quite cheap mass market black walls supplied by by this, by this memory to give like crazy memory extension, like terabytes per per Blackwell chip for for neural network process, just to build something like Rock, but much more universal, like General, General, General purpose to make it more flexible than just memory, than just compute in network. Just as you both understand that deeply customized for every model, right? What bug rock is doing. But the most interesting here is try to run more, both on classical CPUs and like shared cache CPUs like uscalon. So that's the that's, that's the general idea,

all right. So, yeah, that's exciting, but please do send me like the concrete, the concrete details on that that I can look at it myself too. Igor, do you have any any thoughts on this?

Yeah, so the code we have, it's not specialized for any like hardware, and there are certain parts of it which are specialized, but it is possible that the current implementation of work do not be able to make the best use of the ascolon architecture we are but we will certainly See what we can do to make it happen?

Yeah, yeah. In fact, like on the previous meeting on transform, including Ben, we've been discussing like rewriting the kernel plots to make to make it workable. But anyway, it just needs some, some some framework and the whole overall concept glorified before we just, we just fall into the into the direction. But if you see good perspective, we can deeply, deeply collaborate on this and just make it happen. So right, right now it's, it's also a concept, deep conceptual discussion, because I just, I just need a conceptual solution for that which will be scalable in future, for clustering systems and the large scale. So that's, that's why I'm discussing this in Remy race as a vertical solution.

May it would be, I think it would be very beneficial if there will be some overview on how like over how the system is different, and an example of a task which is solved in a significantly more performant way on as column, specifically,

yeah, yeah, the

Yeah, I think indeed, it's the so Mork has been from the ground up designs to to parallelize. But parallel is actually more than the current code base does, because the current code base is built for CPU, and even though that SQL is a CPU, like, if you if you say, we get, like, a much higher memory bandwidth per core, then there may be other ways of parallelizing the workloads. And then it makes sense to just test this out with some C Plus Plus kernels, for example, right? And just see what is the upper bounds, how much faster is it? And then this isn't like running full mark yet. This is just like, for example, like a neighbor's query, or, like a very, very simple query that we lowered down into into the architecture, and then we see what kind of potential gain there is to to porting that. That makes sense.

Yeah, that's, I'm just, I'm just gaining some inspiration from more on GPGPU compute. It's, it's sort of stupid and straightforward, but we avoid in cache here, and classics, classical CPUs anyway, if we just over summarize, it's a computing cache, right? And we just have the data files as one random, sequential supply for this process. So have any shared cache in in azkalon, first might, might be an option to get it to get a streamlined, sort of streamlined memory supply, right on one hand, like it happens in GPU for for Massive amounts of memory supply, like terabytes per cheap that's one thing, another thing that we maybe can build some layer architecture. So if it's, if it's, we had a lot of discussions on DDA or igbm with Anton, remember? So maybe if we have like streamlined terabyte scale, or even even more dozens terabyte scale safe per per compute process of sequential supply and HBM on on a chiplet as a massive cache and have it like layered system designed that way, to process it that way. Maybe that's also most beneficial. So I'm just just speaking out loud, yeah, yeah.

There is definitely. There's a potential there, right? Some there. There is, of course, a lot of trade offs as concerned that on the last call, like HBM is very hard to get your hands on. It stays very expensive, and for us going, yeah, anyway, so I don't think actually we can discuss those matters on this discount. But let's move on to some of the I will give a brief presentation, and then the people watching the recording can can get on that, and the people here can also ask some questions on that, and then we can dive into the full topic.

Yeah, sure, sorry for thank you so much of time just, just, just, just to finish this the thread, what I'm thinking about, to summarize again, it just maybe did their DDR memory doesn't that doesn't make sense here, because if You have direct, direct supply with 100 gigabytes per process that makes more sense to work with. The HBM is random as random access cache system, and we can maybe bring it up on the next that storage call and discuss it like as a whole idea to try to calibrate it. Thank you and sorry for taking so much.

No, this is from minus things up. So yeah, that's fine. All right, so let's address a couple of things

that were released. Let me start with one of the last things in the memos chat. So it is true like if you go to server, this branch has a as like, it's data processing at the moment where like graph database kind of stuff for mn two you want to use unified transition rework. I'm in the progress of merging these two. But there are, there is some difficulties there. And, yeah, the unified transition, if you go to this path, then you can see the same the same trick. That's that Patrick was suggesting, which is that's like, if you, if you want to test something out with Granny, you can just have a lookup table. This is perfectly valid. You can generate a lookup table. You can upload, yeah, it can have many millions grounded items that you just insert, like this, and that way you're able to this is actually equivalent with on the finite subset, with the grounded functions themselves, right? So if we, if we go to where this is used, right? Then whether you have this in grounding, or you have this as part of the query here, that does the same thing, and It's a quick way to prototype.

Now, if I share

is that. So

the initial mm two was presented something like this, where you have some patterns that you match over the space and some templates that you fill in to the space. And the there is like an implied semantics here that I've been over a couple of times, where the patterns, you don't take them from the space, and the templates, you insert them in the space. So this is actually, if we get, if we generalize the priority a little bit to work with the multi threaded environments, then this is what I call the monotonic subset of mm two. It is very easy to analyze. So if you have many of these statements executing, one after the other, you can actually rewrite the statements live and get much, much better performance by utilizing the knowledge of what has been previously generated, kind of like query Planning, where, yeah, the fact that this is so easy to analyze allows you to do cool stuff. Any questions about uh, monotonic fragments of MN two?

All right, if you still have them like, feel free to interrupt me. So then I presented this Dubai so slight alteration, where you are allowed to do branded functions in here, and the meaning of this was any granted function, and this was problematic. So actually, if I have a I have the example. Now, for some reason, I got rid of the example. This was problematic because you need the optimizing compiler to be able to introspect the grounded functions and make and have them be performance, be executed at the right time. So this, this wasn't very good. So now we take this, this fragment of mm two, to mean just slight effect, pre grounded functions like Not, not equals or less than, or addition. Does this make sense to folks

I did have like, one question about grounded functions, like, do they work over, just the current match, or does it work over, like, the space underneath? I don't know what the

Yes, yeah. So that's indeed. What I wanted to remark is that in the original this mission, it works on over spaces, but in the new definition, it does not. So let me pick if I can actually bring up the example again.

Yeah,

I swear I have the slide on this, if I could raise up the slides at some point.

So this was the, this was the original motion. And here comes, is a was a function that accesses the space, and this is no longer allowed, so

stars, but of course,

there is a question, what is the alternative, right? So then there was a question about positive and negative, or deletion, right? How to do to deletion? This is a fragment actually implemented, and it is not very general, but it's still by by eliminating, it's still quite analyzable because so let me walk you through the semantics here. So if there is a minus sign in front of a pattern, it means that you are deleting that pattern as used in the match, so without the binding substituted. And if you use a minus sign on the templates, it means deleted with the bindings in there, which it's kind of funny that there are, like, two different notions of deletion. This is, yeah, that it trust me, if you think about it long enough, it does make sense that there would be, yeah, and then, so the plus on the template just means insert this in the space. So, yeah, this is a fragment of two. It's much more. It is actually more expressive in some in some way, and it easily embeds the algebraic operations, which is also also obviously a good thing, yeah, so, so here you can see, process this into this and take, take the resource that you use to do this, or take the or this is no longer needed. So we have, we have completed this task. If we compare this to, for example, the backwards chain. Or now, like you work with generations, so you say, oh, in this generation that happens in and in the generations, everything is monotonic, which has real, real advantages, but of course, also the advantages. And here it is not monotonic anymore, but yeah, quite a bit more expressive. So then we talked about the option to match, not just over in memory spaces, but also over on disk spaces right here, has been hard at work to making this happen. So you basically have heterogeneous sources where you can say, hey, query this from that file or query this from that image, or the Fourier features of this image, and those would all be sources, right? And then the proposal I want to make now, which it's not quite like there are things that need to be

to happen here before, before that works is this, this version so branded, plus sources, plus destinations or sinks, this would actually be sync. So destination, I think, is maybe a bit the wrong terminology.

Transcript limit reached

This conversation was created with an account that has a 30-minute transcription limit. Ask the owner to upgrade their plan to allow access to the full transcript.

How accurate was this transcription?

00:0030:04

AI Chat

Outline

Comments