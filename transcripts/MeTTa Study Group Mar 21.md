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

![](https://profile.otter.ai/ALYPMAM6TLTJYZPW/ALYPMAM6TLTJ4FDE)pvl8maker

Mar 21 at 8:33 am

30 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa, meta coding, predictive burden, fork space, child space, immutable spaces, sampling methods, random generator, trace evaluation, debugging, module system, standard library, nested spaces, resampling, Python performance.

## Speakers

Nil (61%), Alexey (29%), Roy (10%)

Hi, Lake, Hey, how's it going?

Going? Well. What about you doing? All right. Hold on. Attending these meetings for a while, but might actually get into some real meta coding this week. So kind of excited. Excellent

Thanksgiving. It two more minutes, sure,

if they're just looking at all the note takers.

Yeah,

hi, Matt. Oh, no, Matt is not here. Sorry I had seen you.

Oh, it's been five minutes. Maybe Matt will join later, but otherwise we can start. I mean, anybody

right now on another call regarding predictive burden?

Okay, let's see.

Yes. So anybody, if you have any question, just go ahead, or you want to show what you've Been doing, or, yeah, anything really you

otherwise I have I otherwise, I have some kind of questions. I mean,

more stuff, what's happening? Whatever. Yeah, if, if nobody has anything, I do have questions. So basically,

a bit sad and, well, I'm not going to be able to tell her name, yeah, Fanta. Ask me some kind of how we call that. Yeah, good, good for first task, things related to MeTTa and men basically test task related to MeTTa that are good for a newcomer and as a way to kind of educate them on MeTTa while being already providing something to to the project, and, and, and so I've been coming up with a few things, and I've been writing, actually, Even issues which I haven't submitted to to the I to get her. I mean, let me just grab that, because yeah, and it's I need to see my notes. But I was thinking my plan was just to submit those issues on GitHub and and to discuss that there. But I could also, in anticipation, do that here, someone wants to join just a second.

Yeah, and so, right? So, yeah, to to, maybe it's PV. I wrote that on another computer, and it would be nice if I could share my Wonder. Is either, either you give me five minutes and I transfer the files and then I can show you the the issues that's going to be easier to discuss it,

or I kind of discussed that, you know, without a safety net or whatever, and and maybe that not so I'm going to be as a as nice. So I would suggest, so I'm going to do the transfer to show you the issues and and during this, you know, coupled minutes to maybe five minutes. If anyone has any issue, please go ahead and and then I can, later on, I can come back to that, but that's what I suggest. Anybody Are you okay with that?

Yes,

okay, sounds good. Yeah, okay, yeah, like, please go ahead.

Sorry that was a mistake. I met A thumbs up. There we Go. Okay,

okay, it's coming any moment you

Okay so?

Okay, so I have four issues. I guess I'm gonna somebody on the first one. Okay, so fork space. So basically the issue is about having a so bringing the ability to fork a space or to create a child space, so it's a little bit like new space, but you give an input a space, and it's going to create a new space that contains everything that The parent space has, and you can modify it and without modifying the parent space. And so the reason, I think this is very useful is because in the that way, you can easily, you can easily create kind of a tree of spaces as you create a tree of evaluation of a non deterministic evaluation. So I don't know if I illustrate this in the issue. But I think I

was issue is quite clear, and, yeah, it would be very useful to have such a possibility as the question is, do have some ideas on how to implement it?

Absolutely, no idea. Yeah, I don't know the I imagine it would be something like, you know, some kind of lazy

but babata can just put in spaces, one inside another, work or not. So, I mean, it's a not really an issue, but the question how to do this using the current implementation, or it will not be a good first issue will be a very involved issue to solve, because you will need to modify how spaces,

yeah, so that that's that's probably the Most difficult issue. I created

just a quick question, so I could just scroll up a bit. So when you create a you create a child's base and a grandchild space, and you modify the child that doesn't modify the grandchild Exactly.

It doesn't modify the right.

So space is only so space, when you fork a space, it's, it's only capturing what's in the space at the moment of the fork. What? So if you fork a space, the child space only has what was in that space at the moment of the four

Yeah, yeah, yeah. It's really local. It's really to have a local space exactly in the example, yeah, we see that, yeah, the grand Chai space has been modified, but not the chai space, yeah, yeah, they are separated. And yeah. So the idea is that every brand should have its own local space and, and that's kind of tricky, and, right? I mean, it's kind of, it's kind of crazy as a first

in terms of implementation, and I'm talking from Metallo here, the the easy and expensive way to do it would be just, every time you focus space, just make a copy of everything in the space. But that, you probably don't want to do that, because things can be huge, or you, or you have a hit. You all, you had to have a system where you have a reference to the stage say, yeah. But then you have the problem if you modify a space, then, yeah. So, so what

implementation we are talking about?

Well, I'm working on, I'm working on the Metallo implementation. So,

well nil, I have questions about MeTTa lock or

I it's, I guess both. I mean, ultimately, if it comes on, if it becomes a built in, then all, all back ends of MeTTa are required to implement this built in.

Well, what do you mean by required? Because there are still some differences. In any case, it can be greatly implementation specific. So as I said, maybe what you needed just to create a space and put the parent space inside, then you will be able to modify the child space without modifying the parent space, but it greatly depends on what mechanics doing it. I mean, if you can modify the part of the child space which was in the parent space, and it will not affect the parent space, then the proposed mechanism will not work. So if you specify in detail, well, the scenario in the issue, then, yeah, we can so, so the

the, I think the issue, the scenario is, is well detailed. I think it's really, it's really a functional approach, where everything is immutable. I mean, everything is immutable, but no man, they are mutable. Of course, they are just like spaces are mutable, but the forks are really independent, like a the relationship between the forks is all the other space should not be affected by by what happened to a particular fork. It's in open car classic. We have that,

yeah, if you modify the parent space, will it affect the child? No, no, okay, so you mean they, you just fork them. I mean you don't want, well, if it will not affect, they will not be any effect in both ways. Then I don't see how you can do this without copying.

Yeah, that's tricky. Or maybe maybe the parent space can be modified explicitly. You know, if it's referenced and it's being modified, it's gonna affect the child space. I I'm not sure I Okay. That's there can be in any case, we can,

if you and desirable behaviors, and you can discuss if this behavior implies quite a heavy implementation, like copy paste in the whole space, or something like, Well, I don't know, not copy pasting by but by the whole space, but somehow shadowing. But if you do this in a very nested ways, then you will need to keep track of all this modifications in nested spaces, and it will also become inefficient. So let's just discuss, yeah,

I agree. I agree. It's very tricky. And I mean by by the way, in terms of like first issue, it could still be kind of a first issue if it was implemented in pure MeTTa without any optimization. In mind, you know, just, just to have something and, but, but anyway. But it is a complex issue to be used really pragmatically. So the

other thing you want to specify just quickly, if you do that is what happens if you delete something in the parent space? Does that delete at the child?

Yeah, that's another question. Yeah, yeah, yeah. So, so, yeah, okay, okay, but yeah, that's, that's a complex thing, okay, and so the Okay, let me open a less. I a complicated issue. So this is just to have more sampling methods. So currently we only have this, well, this one, I think, is kind of probably temporal, temporary. So,

yeah, yeah, I have a quick comment. It's first a few comments. First of all, flip was introduced initially purely for testing purposes of automatic conversion between rust and Python, and it was just moved to standard library by occasion, because no context was provided about this method, and I definitely agree that We need to implement more methods and maybe name them differently, but there are two, and maybe it's a good first issue, indeed, but there are two, maybe not problems, but concerns. The first one is that I don't think we would like to have all these methods in the standard library, and that's why we first need to be able To add customly imported library libraries in our build, and it's what we have just discussed with Vitaly. And another issue is that, well, maybe it's okay to have these functions as well, but I was thinking about the possibility to have some dedicated sampling structure, not just imperative sampling functions, but some structure which would provide you with capabilities of resampling. What has been sampled with sort of traces of computations after some sampling has happened, and it is much more involved, but maybe it's okay. Maybe these are two different things and it's okay to start with just implementing a rich random number library.

Yeah, yeah. So regarding the standard library, yeah, I agree with you, but it depends on what we define by standard library

attack. Automatically versus what is important when you write imports, import,

okay, okay, I see, yeah, yeah, I agree, yeah, okay, okay, yeah. So basically, right, because we need to have a module system that makes it that importing a third party module is very easy, so easy that even though you have to make import Well, it's kind of a it belongs to a repository that could be viewed as a standard, curated repository, just like the C Plus Plus STL library contains, you know, all these sophisticated samplers. Is in the STL, the C Plus Plus STL, but you do have to do to include etc, so do something similar, you know, yeah, I think that's easy to use. Basically, yeah, that's just what I meant by standard library,

right? So, so I mean,

one can just start implementing such functions and they can be easily moved to a separate library afterwards.

Yeah, yeah, true. And so the question I had, which I did not mention in the issue, is, well, I did mention a little bit here, yeah, indeed, you can use Python. But then there is the the question of the random generator. So currently in MeTTa, we have a standard random generator. You can also create a new one. I think you something like that, and, and so that's great, because you have control over that thing or that thing, you can you can reset the seed, which is very convenient when you are doing testing. You know, because you, you want something to be reproducible. And so we have already available these things to reset the seed of a random generator and pass the random generator to these random samplers. And so if one starts to use Python, that is going to be a different random generator, etc. And so you have, it feels like you have to, basically, either you're on the Python side, or you're you're on the meta side, or maybe MeTTa, just create some kind of wrapper where everything is on the Python side, on the back end. But from the user perspective, it's just a built in MeTTa, and right? And so I was just there. Was just decided it's not that important, in fact, but yeah, just this, this issue was crossing my mind,

isn't, isn't there? Isn't there a big performance as she was going through Python, yeah, exactly. So sometimes, when you're doing sampling, if you do Monte Carlo or something, you're going to want a lot of random numbers really quickly, at which point the Python becomes the bottleneck. So this, this was seen to be fundamental enough that we want to have it, not in the standard steno, not built in, but with it, with it, with something you can easily import. So that would be, yeah,

I agree. And

this is also problems, just a matter of effort and doing this,

yeah,

I have to jump off another meeting, which was unscheduled, scheduled today. Okay. So, okay. Alexey, yeah, yeah, thank you. Anyway, just twice as this issues and we will discuss them. Yeah, sure.

Okay, I'll do that. Bye. Okay, so let me go over the other issue. So this one is for tracing your call, so we so we do have trace but, but it's only tracing one message. And what I suggest is to have, I don't know, trace eval. I call that Tracy Val, but whatever you know, you have this thing, you give it a space. You call it and it say it's a recursive function. You're going to trace everything, 4241 because this thing is just decreasing, but it's all it's so it should also trace that food. 41 is a child of food 42 No, you know, and who 40 is a child of food 41 etc. And that is extremely useful. It's so useful that I find myself doing that, and I manually, I manually write that exactly what as I did. And so it would be really good to have something that does that for us, and maybe has a special notation where you have a child, but it's an it's like a non deterministic, I mean, it's like, well, it could take that branch, but it could, it could take also that branch, and you have a clear way to see that it's two different branches from from the same parent or something, anyways. So that that's this issue, I didn't complete the issue, but that's really the idea

that would be tremendous. That would be tremendously useful, not only for writing meta, but for debugging when you're exactly now, even for the people implementing meta, something like that is useful because, yeah, yeah, there is, there is a meta log, there is a flag, which I can't remember, off hand, where you can sit weak and turn on trace for the whole program, but it's done at it's done, it's done on startup and you can't say you can't just do it per function, which is right. Very, very, very verbose

and right and the idea would be that everything would be stored in a trace.

How accurate was this transcription?

00:0030:03

AI Chat

Outline

Comments