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

/

![](https://profile.otter.ai/APMITW5CSZHX6LCM/APMITW5CSZHXZECY)Lake Watkins

Sep 8 at 7:31 am

30 min

Shared with: [MORKification Weekly](https://otter.ai/group/27457183)

Summary

Transcript

## Keywords

Morkification, PLN, second order probability distributions, GitHub profile, Singularity Net Compute, hardware deployment, data center, network issues, InfiniBand servers, 20 gigabit data network, 16 nodes, Wikidata, factor graphs, inference control.

## Speakers

Adam (47%), Benjamin (29%), Sergey (19%), Charlie (2%), Speaker 1 (1%), Speaker 2 (1%), Haley (1%)

Hey, zar, well, it was good fun. You're Improving fun, huh? Actual? Uh, new, exciting things.

He returns next week. Hi, Doc.

All right, yeah, I thought last year Neil's presentation was very forward looking, so I wondered what he presented this year.

Well, I mean, his presentation is on his GitHub profile. Who needs to go to France, huh?

I go to the Alps, any chance I get.

I mean, it is a beautiful location in the Oh, is it the Alps? Yeah, right, yeah, if the Alps then they'll present it on the basics of PLN is like working over a second order probability distributions and how one could try and use that to estimate the likelihood that some conjecture is true. Yeah. Interesting. I feel like every time i i hear nil give a talk. PLN means something different, but it's often interesting. I do pretty much associates no with the PLN guy for whatever definition of PLN is, maybe that that won't Hold up very much longer with a 0.5 release. I

still logging into my account, because first time I boot up my machine in quite a time I

do you have an idea if Ben is joining Matt? Anyone's guess?

Because there is a lot of clarification that I would like to get from ban on some of the more use cases, which like that would be a super interesting discussion because it's relatively high level. So I think a lot of people can can join in on that in some form or another. Yeah. Uh, of course, I have plenty of low level stuff to discuss too, so then doesn't join. I will. I mean, back into did accept,

but it's still early for him. Yes, of course, of course.

Um, it's only five minutes after the schedule, right? Start, yeah, I may spend the next 10 minutes giving some trivia updates or

look for me.

Hello, hello,

hi, Sergey. Sergey, what is can you summarize in two sentences? What is singularity, net compute, and how does it affect Adam?

How does it affect Adam for Mork. Yes, singularity compute is a project to deploy hardware which took much longer than expected. Unfortunately, that's why it doesn't affecting work thus far, but one is successfully deployed, and I hopefully, and hopefully that will happen soon that will help us really efficient as bad for more, have we looked at

the possibility of deploying Mork at some point as One of the value added aspects of compute.

Sergey, yeah, definitely also, you know, singularity compute is the first it's a package of hardware purchased being deployed in the data center.

Is it the one sitting in Amsterdam, or

it's it's in Sweden right now, yes, near Stockholm. It's not sitting in Amsterdam. It's for some time in the data center. And we had problems with network. We had other problems. We are solving them. And right now we are back and back and forth, back. So Cisco networks are coming. All the servers are there, and it's just in the progress of assembling right away. Cool, yeah, if you,

if you need any help, networking clusters for graph databases. I, I know a lot of people in that field, but I guess that's, that's not the initial goal. Of course. Yeah.

I think we will run Mork instance there and other stuff. But right now it's just the initial phase of setting up the whole network. We will have InfiniBand C servers. This will be the same as what with GPU servers, the same I promised in the very beginning, we also have a data network of 20 gigabit, bonded like separate from Mellanox, from any band for pure, for pure data management. And we will have 16 nodes, last generation, interconnected through your VMA, and also eight, I don't know, also, also 16 nodes. What does mean?

Sorry, you said last generation nodes. What does that mean?

Ah, maybe it's not the last right now, it took some time to deploy. I mean, it's just the largest with as much of computing threads as possible back packed with memory up to up to the top, like as much memory we can the 1.5

terabyte once I forgot, yeah, cool

for you.

That's awesome. So like I've, as I've shown in, I don't know if you were able to to see it online. But as I shown in RGK, that took a long time to retrieve, like Mark, just by being, by virtue of being a server, can distribute work, so it's like, as long as it's not too communication heavy, like the current infrastructure, like actually does allow for not just saturating compute on a single node, but also like deploying to multiple nodes and just doing some embarrassingly parallel stuff on there and then summarize the results in various ways.

Yeah, sort of interesting. I just think it's really cool to have this the database like regular database sort of design, but also understand that the most intensive hyper graph process will be just direct interconnection of it. We just, we just need to have simulation of of unified memory array and unified computer array. So what I tried to do from the very beginning is just to let this being processed in the straightforward way. But definitely we can. We can use this layer, like server and memory, layered memory distribution. But anyway, for me, it's like straightforward to have the first, like resume array, which we can aggregate computing memory directly to have, like, maximized output. Yeah. I mean, this

is a complex topic, right? Because

Ben joined if we wanted to have,

I think this is actually very open to finish on the remark that Sergey the direct memory access is like, very good on paper, but if you don't have a notion of locality in in the workload or in the graph, then still like it will just slow down your workload, right? So you still need some model of what does it mean to distribute, even though that your network technically supports DMA. Does that make sense?

Yeah, it's absolutely that. But anyway, having having a configuration in which, in which we like PCI bus interconnect and CPUs equal to network bandwidth, it's really nice to have any sorts of experiments and understand the bottlenecks and calibrate the system further on to control the locality and absolutely

address

so I tried to build it like sort of test stand to deal with any sorts of experiments and calibrate the system further on, up to convenience and better design.

And last dangerous question, what is the timeline on being able to deploy Mork across like 16 of these nodes?

I thought several, several, several time, and it was not, not not the case. But now, now it's quite close. So the servers are in the racks, and that's just the process which is on CUDA. And so CUDA just asked to set up all the, all the environments on their end, and we delegated this, this, this work to them, because we they're doing it for all of the clusters, and we just cannot violate their timelines, if that was me, that we will do it like for, I don't know, for several days, but we need to go with good timeline, because they asked to set up all the all the environment once, and run the scripts under the schedule. And it's sort of sequential, so we are dependent on them. But anyway, it looks like October to finish it.

Okay, cool. Keep me up to date. There's some really big mark experiments that I want to run for a long time. Really, really cool. Just, just, just to bridge

the gap, you asked about computers and other side of compute, which is working on, working on the guy as a service. And there is hyper graphing service there in the road map. It's, you know, it's sort of abstract eyes right now as a product. And we didn't discuss the deeply, but I thought, once we have this hardware and had some, some first could have some first initial experiments, we can discuss productizing this maybe in the beginning of 2026

or something like, yeah, the to give some perspectives to folks here, right? Like, the the biggest thing that Mark has processed was Wikidata, and this took, like a little over a day to make a metagraph of all of Wikidata. And this was on the machine, on the machine that I rented for 400 an hour. So it's one of the largest machines that that exists, which has like eight Intel sockets and terabytes of memory. I think it has 16 terabytes of memory. So actually, now we would need less memory, because this was before the allocator changes. But the and I have it here, this is the end results. I don't know it's flashing in and out of its existence, but this is a drive, right? This is a US. This is a USB for Drive, actually? Yes, those things exist that contains, like all of Wikidata as a morgue store, or specifically, like it has it in a couple of different formats that we can load into individual devices. And so the dream is that I can take this up to my laptop and like just with a USB four cable, hook it up and gets around 2020, or 40 gigabits per seconds of bandwidth, like reversing parts of that huge, 70, 70 billion atom atom space.

And so hopefully things like that can become routine given the right compute infrastructure. This is Sorry, Charlie,

I said from your lips to dog's ear.

All right, so what then? Do you have an agenda?

No, okay. Lost, we lost track of these calls, but I don't think I've been in every single one of them, either. So I'm not the best person to be a

bother. You some about your papers on MORKification or mark dash x.

We could do that. We

can as well see if anyone else in the call has some pressing thing they're trying to do when they're confused about it. Well, Adam, you'll have things we're trying to do when they're confused about Yeah.

Adam, you mentioned getting some, some, some use cases, right?

Yeah, we can. I think we can take Okay, so what a little note is that I had this conversation with Robert. I don't know if he's on the call here, but about Mork use cases. And I was like, Ben, kind of put out this like paper or six of them, seven of them, on how to use Mork in specific AGI related use cases. And I believe if it's still the plan to do AGI, then those are the best things to look at for prioritization purposes, obviously, or perhaps not obviously, but certainly true. Mork, at its turns, in its currency, is like a good generalized graph database, so you can already use it for all applications as required, that if you just want to fire, fire tests, some of that. And then there, there are applications in between these two. So in between this AGI level application on top and the graph database and generalizations thereof at the bottom and between the two are things that require certain niche optimizations or certain niche features, and that someone is willing to own right. Someone wants to say, hey, I have a problem. It kind of looks like hyper graph processing. I would love to deploy it with Mork or speed. Speed it up with Mork, and then we can collaborate and have a dialog on how we can best empower these people and what features need to be added, first to to enable these prototypes, and later deployment.

Does that make sense to you? Kellar,

for the most part, yeah, no, it's also a perfectly fine answer. I can elaborate on whatever you're unclear.

Yeah, should we go over? Well, you would ask Ben to take us through that.

Yeah, right. So we have already, like, on previous call, calls talks about factor graphs to a very little extent. I would love to, love to deep, dive, much deeper onto that. But I think that's best done offline, since it's at this point like there's a very good theoretical match. It's just about like the implementations there and which quantiles we want to support, and like how we specifically kind of get,

yeah, let me, do we have?

Do we have no and Patrick on this call

on vacation till next week. Okay?

And we do not have Patrick hammer either. He's on the invite. He's not here. There is, there is some discussion on

factor graphs

from a PLN standpoint, which will be, would be quite worth having, but it would be nice to have Patrick and and nil on there, because it's, it seemed like maybe, maybe Patrick hadn't fully grok what the factor graph is actually, actually going to be doing here, but that's, that's his. But maybe he does, and I just don't understand that the questions that he has, but that will better be dealt with with Patrick, right? So perhaps I

can set up a call with nil Patrick, you if you're available for sometime next week or the week thereafter, where we specifically go into the factor graph. Because I think like this, this kind of leaf propagation as locally computable. PLN approximation is a good direction.

Yeah,

that seems that seems highly valuable. And I mean, once you start thinking about having the factor graph there, there's all sorts of other things you can do with it, right? Like, well, this is another nil topic. Like I was, I posted something. I was thinking about an alternate inference control mechanism. When you go from the source and the target at once. So like combined forward and backward chaining. But then each like, each forward chainer is sending out some little, like, statistical probes to see how close it is to the emanating backward chainers. And each backward chainer is sending out some statistical probes to see how close it might be to the emanating forward changes, right and so then, then, formally, you can,

you're trying to find, like, a GD thing that gets shortest path between beginning and end. But the the factor graph could be super useful here, and making it possible to send out a sort of rough probe to see, like, how close is this forward trainer to the current state of any of the any of the backward changes, right? Because you even so that that occurred to me as a way that, like, even if, even if the factor graph ultimately wasn't good enough to get you to your answer, like, because it's fast to propagate stuff, then the factor graph is giving a sort of statistical guidance to to a swarms of chainers, right? So that there's a, I mean, sometimes the factor F can just give you the answer also, but it's, it's interesting. It could be useful even in cases where chaining is in the end what you're going to do.

So what is the mechanism that allows you to approximate the distance? Well, here

you're trying to estimate. I mean, you I should probably just give a whole presentation on this and show that, show the math of it. But I mean, you're, if you, if you formulate what it is to make a geodesic between the starting and ending point according to the Schrodinger bridge metric, which is, which is what I was, I was, I was using, I mean, then, as the chain of proceeds, you want the chair to take a next step in a way that things will be along the shortest path from the beginning to the end, right and to to then there come out to be two terms. One is about, is it the shortest path going back to the beginning? The other is about, is the shortest path going forward to the end, right? So to estimate, is it shortest path going back to the beginning is not too hard. If you're a trainer who just came from the beginning. To estimate, are you roughly following the shortest path toward the end? Is a bit harder, since you don't know the path toward the end, but, but what you could do is like, send out a swarm of kind of greedy reasoners and see how

close they can, how close they can get to the end, basically, and do some statistical analysis of that, and then you're estimating which, which direction is more likely along, along the shortest path, right?

Yeah. It almost reminds me more like, because it's such a discrete setting, in a way, like, of like ant colony optimization, where, like, as soon as you have one, one that is able to prove that there is something there. Look, more resources can be spent on the optimization. But I mean ant

colony optimization as I remember, yeah, it should be basically like that. I mean, I didn't try to compare the math, but yeah, I mean, you have a bunch of little cheap searchers going along, and they're laying a trail of what they did. And then, then, I mean, you'd do a little, a little bit different math on that, but yeah, from what all the ants do, you're going to be able to tell what's likely the shortest path. The novel idea would be to have some forward chainers And some backward chainers going and you are doing rigorous chaining, but then to tell the direction that the rigorous chainer goes. You do all this swarm of ant stuff just to guess, guess which direction to go. So then you're trying to the swarms of ants are helping the forward chainers Tell the shortest path

to the back retainers, and the backward changers tell the shortest path to the forward chambers, right? And so, so then. But I mean, you don't, you don't have to be perfect and actually find the correct mathematical geodesic, because it's just about control anyway, right? So, I mean, the point is, it's a it's a different way of guiding things in which the forward and backward are being done at at the same time. And the point, the point with the factor graph, is, that's where the ants can swim along, right because having, having the factor graph for a bunch of cheap attempts to extrapolate forward from, from the head of your inference, or having the factor graph for that is much better than just doing random sampling inference from, from the space of PLN rules or something which You just take a very large number of samples to get anywhere. I mean, the factor graph, obviously, is giving a certain bias which is baked into it, but we're kind of assuming, we're assuming this bias is more more good than bad, or the factor graph will be a kind of productive thing, thing anyway.

So what allows you to parallelize across these different forward shiner and across these different backward channels, this is for forward chain or I assume this is different assumptions that you're inserting and trying out. Or what is the into, or different heuristics that each of these forward channel use, or what is

the it really depends on what's your base control heuristic like if you were doing, if you already had an admin space of inference histories, and you were choosing which steps to take based on the based on the data in your inference history, I mean, that's that's very Frequently going to going to point to just one direction for inference anyway. I mean, it's going to be a quite messy distribution. You're you, you're naturally going to get a lot of different different directions to explore, from looking at from looking at inference history.

So, yeah, I mean, that's kind of the same as what you're saying. It's different theories. But, I mean, it's, it's different theories about what's the lesson of the of the corpus of same difference, right?

I think Charlie has a question and Remi has a question.

Yeah, thanks. Um, I was just looking for clarification. It was the question that you asked Adam that I still don't quite right, if there are probes coming from the forward chainer and probes coming from the backward chainer, right? I mean, is there some mechanism by which we know that they both touch the same point and then we have a complete loop? Or were you asking the question about how to tell the distance between the closest I'm trying to

make them grow toward each other. I mean, you don't, you don't know that it will work, but

very cheap heuristics would be like, All right, in how many like, like, if you have a something like meta math or large corpus, like, in how many of the shared proofs is something that we want in the conclusion and someone thing that we currently have Right? Like, how many proofs of these are chairs, or what fraction of this neighborhood of proof structure. So be like an extrinsic heuristic, but like a very, very simple one or a very straightforward one where you're just saying, all right, this is the set I have. How roughly similar is it to proofs, to actual proofs that are distributionally similar to what we are trying to prove at the moment that would be like, one way to guesstimate the like, how far you are from from a goal. But this goal can also be a sub goal of a backward chain right? So you can evaluate this for each of this like, for each of the sub goals that one of the backward chainers has you can evaluate, all right? How many shared proofs are there where this was a needed step to end up into something like that, right? This is an on the fly. Came up with heuristics. I may be completely shit, but that's an example. Yeah, I don't I don't

want to shut down cool, random discussion, as it doesn't happen often enough with the distributed group. On the other hand, this was not the topic I would have had in mind for a call, as it's like I.

How accurate was this transcription?

00:0030:02

AI Chat

Outline

Comments