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

![](https://profile.otter.ai/APMITW5CSZHX6LCM/APMITW5CSZHXZECY)Lake Watkins

Today at 7:30 am

42 min

Shared with: [MORKification Weekly](https://otter.ai/group/27457183)

Summary

Transcript

## Keywords

Mork, path map, unified transition, reordering statements, performance analysis, monotonic fragments, sink segments, WASM, native compilation, sync segments, accumulator, bitwise operations, runtime efficiency, interpreter upgrade, programming language.

## Speakers

Adam (61%), Nil (20%), Khellar (6%), Remy (4%), Speaker 1 (3%), Speaker 2 (3%), Zarathustra (2%), Speaker 3 (1%)

Yeah, oh my goodness, they all came, all at once. I admitted them. I said, admit all. I don't know why I have the permission to admit them, but whatever, bigger better more than not enough.

These are,

are you both in Europe? So it's afternoon, yep,

hello, hey, no, hey, Lexi, hi, I

don't know if we're waiting for Adam or more people to join and if there is an agenda, but if we're just waiting, I would welcome some help to to be able to compile Mork and look if anybody has succeeded to do that in this call. Yeah, if anybody can help, that would be welcome. But of course, if it I don't wish that to be at the expense of a of someone else having an agenda to about presenting something of course, yeah,

sounds to me like a good way to kill time until Adam shows up, assuming he will okay.

So okay, let me share my screen explain to you what I have so far.

So gotta be these.

Let me, let me actually move that to my wide screen finger. That'll be easier. So okay, so what do I have? So I have, I have, correctly, successfully built path map. Now the latest version I believe? Oh, what did I do? I just went into in path map and just went there, cargo, build, release. Okay, a few warnings, but other than that, it looks like it's been properly compiled. Then I went to Mork. More kernel. Oh, so in Mork, I'm using, okay. First question, Do I really need to do that? I'm using the the unified transition rework branch. So, yeah, well, okay, that's delightful.

Did you see what Zara posted in the chat before all the AI stuff

swamped it? No,

I've gotten Mark running by the server and main branches only, but Patrick was putting up a getting started on the wiki and fiddling around with that. I needed to use the rest of default nightly as well, but it's kind of got it working. Oh, so where is this wiki? Um, I put a link in the chat.

Oh, well, thank you.

You just have to scroll up past all the AI

garbage. Yeah,

hi folks. Oh, excellent, hi. Adam. Okay, so I guess then my question can reduce merely to, is that branch still the one I should use if I want to attempt to port a version of the backward channels to mark, or should I use the server? You should use main. Ah, main, okay,

yeah, until the server is merged into into me, yeah,

okay, so and CD more kernel, and then just a cargo build, and that's it. Okay? Well, no, it's not like I I don't trust you. But what? Well, I can't move there, oh yeah, because I have stuff too. Okay, yeah, okay, too. I wasn't aware of this wiki. Okay, anyways, if there is any agenda that you can you can go ahead. I'll do that in the background. Cool. Yeah, I have a

couple of items that we didn't get to last week and some new items. So it's exciting. So, first of all, sinks so you can finally play around with some things. I had a very different design, like in codes, but for for actually playing around with them. This should be this should be good. I was going kind of performance overboard, and I wanted to everything to flatten out, but in the implementation, that turned out to be like a very big meta programming challenge, and not a, not a right kind of meta so I will show a bit like how, how you can get started with it, what the different things are, what you can do with them. And they will be not a whole story, right? Even together with sources, they are not a whole story, but coming closer, but they are very big parts, because the base language of mm two is designed to be monotonic and very easy to analyze. So all all statements, as long as we have like a temporal ordering on when these statements happens the you uh, the analysis is very easy. So this is for long lived programs that that require some indices, or that have some requirements on on storage size. Then this automatic analysis is very, very handy. So I think Zara can already attest to that. He submitted like a program that took 18 seconds when formatted one way and when formatted another way, it took like 30 milliseconds, something like that, right? And so to prevent people from running into the 18 seconds sites, we want this analysis now that. So we won't just upgrade the Mork interpreter or the mm two interpreter with things, we will have a gradual progression where a lot of your statements will still be written in the monotonic fragments, and everything that happens in the monotonic fragments can then still be subject to the same analysis. And yes, Charlie, it's things with an S. So to make it a bit more visceral, what's what is happening? Let me share my screen. So

I did the most idiotic thing just before I joined the call, I updated my computer on Linux.

That's never idiotic. It's always a good use of time, right, right?

So this is some some codes. That's, that's, that's our submitted, right? And it looked pretty much like this initially, but it was slow, and so what made it fast was the reordering of these statements. This is pretty general. Like some of you will go like, what the hell? Why does that matter? And others will go like, Oh yeah, that's a typical joint ordering problem. Whichever one it is, it can be solved with analysis. So we can take notes or even take multiple statements that look like this, and we can, we can calculate, there are a few weeks to do this. One is like a conditional information metric and or one I'm not seeing your screen. Okay. Is someone else seeing my screen? Yes. Oh, weird.

I see that it's being presented, but I don't see it.

Um, let me just because this will just represent it in case that helps.

Here's it again, the

better I got it. Awesome.

Thanks, yeah, so,

so, right, I was just saying that these statements does reverse, and that's made, like 1,000x difference in speed. And that the we can automate this, that not quite to the level that I can reorder the statements, but to a level that's that most people won't be losing 1000 text performance

Adam by reordering. Do you mean assigning the proper number in the priority?

No, I mean what I'm showing on screen, which is in a query, reordering to patterns.

So the comma the order of the of the clauses in the in the comma. Okay, correct.

Would you be so kind Adam one more time to stop sharing and reshare, because I changed my screen configuration and lost you.

I will,

I think it's some issues with Google meet, because I still can see, but I'm trying to hear just because others can see, I guess, all right, so the I will also just share.

It's hard to let me see, can I share a link on this?

It came back for me. Thank you.

Looking if I can share a link?

Alright, so, yeah, the the reordering to repeat one final time for the in a query, you the reordering of the patterns doesn't influence the semantics, but it does influence the runtime, and we can make it so that's the runtime is low for for everyone by having some automatic way of ordering them. But this requires some analysis now in the current fragment of mm two, although sometimes perhaps for say, frustrating, frustratingly inexpressive is very good for analysis. And today I'm changing that where there is not just this fragment, but there is another fragment. And I presented this like a few weeks ago, which is the segment which sinks, and instead of having a comma for the patterns, it has an O for the templates, so it can output to different kinds of things, not just the space. Now what this means concretely is that you can do much more expressive things, like here, I'm subtracting two items from the space and then adding others. So this is doing like an in place swap, if you will, which you couldn't express before that cleanly,

is the screen supposed to change or because I've seen, oh, oh, wow, oh, okay, you're gonna reshare because,

yeah, I don't know what's going on today with with me.

Strange. I change great.

So the sync segments is more powerful and breaks the analysis. So that's the that's the bottom line, but you can combine them, right? So here you see one exec statements with a comma and or exit exec statements with the with the six, and you can mix and match them in your usage. The general guideline is use the least powerful thing. You are losing performance for generality in more way done, more ways than one. Igor is working on merging the sources, so I'm testing those out at the moment and and seeing like how we can list support them in the codes. But what that means is that you not only will have, like an an output that you can have here, but you can also make X statements which have some inputs. So the input from,

can you quickly scroll up and scroll down real quick? Sorry, can you quickly scroll up and scroll down real quick. I think, I think what, what's happening is maybe the Linux update has made it so that when you share, it will share a single screen, but it will not share live, because we're just seeing a static screen. So just, just want you to be aware.

Yeah, I see that it's static now,

just to have that, yeah,

let's see if I can force the update somehow, maybe, if I just maybe, what I can try is just share, like, one of my monitors, and then hope that's somehow the updates there are,

are you? Oh,

yeah. So what I was showing is that what Igor is working on at the moment is that you can have a source segment of MN two also where you can get something from an AC T file. So you say, I want to load this from my data. More space, dot, KCT, and you can also match things on the space, of course. So you say something like space, that's and then we have a final segment there. Of course, you're able to combine both. Am I still? Am I still moving? I think,

yeah, I'm getting just the Yeah, I think, I think the pattern is, is that when you share, we, we get that first screen and it, it just doesn't refresh. So, okay,

oh, there's something happened here.

So, right,

that's unfortunate I

will, or maybe it's refreshes, but at a very, very bad crime rate or something, I don't know,

yeah, um, that's frustrating. Uh, work because, like, this doesn't help if I slide, if I share a slide deck, because you maybe, maybe if you all join like a live slide deck, you can see it's on your own copy of the slide deck.

Maybe that can work. It's not that

I'm the other work around us to just reshare every time you want to move.

All right, so, but I believe you're now seeing latest which is that on screen are four different segments of mm to the source and sync segments the source segments, the like monotone. Monotonic segments and the sync segments. And these all have, like, different, different traders, of course, like you for for power, you will want to use whatever you need. But if you don't need it, you can use the weaker, weaker segments, and they all translate down into each other, right? So, like the it's not that our code has to blow up when, when we do this, we can just automatically rewrite one into the

other. Honestly, I don't understand the segments.

Have you seen the mm two flavors presentation?

I don't know. Probably not. Okay.

I will. I will share. It's again. Think I've been over it twice on these calls. If you happen to be absent on those two calls, yeah, probably what we've seen here.

Thank you. Yeah.

So for Yeah. Are there questions on this? What I'm what I'm saying here?

I have questions, but I'm supposed to you are lost them? Yeah, first, I don't understand the O instead of the comma. I don't understand the repeat. I mean, it sounds like it's repeating.

Yes, let's start with the let's start with the first question, right? The O is what you is a symbol that you use to indicate that you don't just want to write things to the space, but you want to write them to different things. This, I yeah, I don't understand that.

What part there? Well, I don't know what's the saying,

yeah, yeah. Then I think we let me see, can I think we can cover this? You've done so twice, but it's also important. So, yeah, let's just do this. So let's just go over here. I think this example is possibly, possibly the best, which is that, because it contains a bunch of different things. And so here we will note, oh, this is a statement that's that has that takes some stuff from the space. And writes out that it doesn't write out back to the space. It writes out back to an accumulator. And the accumulator here is counting unique elements. Specifically, the first argument of the accumulator is what should be counted as unique. So here that's the comments ID, and then the other two arguments are used to filter, filter the results that we get and to reinsert the result into the space. So if we have so, let's duplicate this example for a second. So if we generate something like guarantee user ID or comment ID, like comments this and the then we do this with our templates, right? So this gets called, this gets called with, let's say, three different IDs,

and

what happens there is that they are summarized or accumulated. So related, and then substitute it into x. So here we have three unique ones. So x becomes three, right? And then x, of course, unifies with this x, which becomes three. And then this is the thing that is written out to the space. And of course, we got some vote types, so let's say we got upvotes, and then what you see as an effect is user with that user ID has three upvotes that's enabled by this kind sink.

Okay, so, but it's, how do you sorry, how do you determine what is the the other variables? Because, okay, the three is the accumulation. But what about the other variables mean they could be different in the three three times. So are they Yes?

Yes. So this is, like the what is specifically happening is that, like, actually the count is indexed on this too. But for this, if that's the thing that you're struggling with, I think we are good for this example.

Oh, well, hmm.

There's an equality here. This means define as a function. Is there? Is it supported already at this point? Or you need to write an exec that.

You need an exec that consumes this. You can call this whatever this is just structure, whatever you call it,

czar. You also had a question about

this, well, I was just wondering, is built in as a specific operator or something come again, like is counts built into like work mm two.

Yes, correct. So you cannot define things like in you cannot define things in mm two. What you can do very soon is define them in wasm, which, yeah, so open it some kind of forms, but I'm excited for

it. So your example is combining two things, the O, which is the sync, and the count, which is a built in. So you can, you can use the sync with other things than count,

absolutely, absolutely. So like share another example.

Charlie has a question, by the way,

please comment it Charlie,

yeah. It's almost the same question, because can you give other examples of syncs that are not an accumulator, like count? Yes.

So up till now, we saw count and subtract correct, so you remember to remove one for from the sort

I think I do vaguely.

Thanks. Yeah, so those are two examples. Here are a couple more. Here are three more.

The whole idea here is that think is compiling to wasm.

So it's not the whole idea, but it's definitely one of the things that is like enabled by things, because things, as long as your bindings, don't communicate with other bindings, you can do whatever logic there, and because these matches are meant to go over a lot of data. So recently, I did, like, a small benchmark, and I was like, this doesn't run so fast because it was, like, taking five seconds, and I saw it did 3 billion writes. I was like, okay, yeah, 3 billion writes five seconds. Actually, that's really, that's really performance.

So the the the

bottom line here is that the functions, functionality specified here will be called a lot of times, so it can even make sense to just just compile just in time, compile a program to execute for signal statements. This, of course, won't make sense all the time, but for definitely, for some processing, it will

see Sync has something to do with just in time or somebody has entirely, because I still don't understand what's this. I think it's, it's

probably more accurate to say, like, the the count is a function that's implanted in wasm. And if you think of a function as just a pipeline, it's pipeline. Oh, and counts native. But I mean, like, I'm just thinking in terms of functions, like the the function will just be pipelined before it actually writes something to the space. So whatever, like you said, all the bindings, like, unlike, unlike, you know, something like prolog, where something could happen after you deal with like some scope. Once one whole exec happens, all the sort of transient state that's not written out goes away, so it's just pipelined. So that's how you can think of it. It's just when you have it as a function, which is what counts doing, it's just getting that and then as a function, writing it out. Now you could also write directly to a space or to a file or something like that, but, yeah, does that make sense?

Yeah,

in the pipeline, you're pipelining the execution to wasm instead of something native. And then what comes back. You're right into the space, yeah. So you're, you're basically borrowing compiling power from from wasm for certain types of executions, yes. And then you're bringing that back so that you you can actually borrow other compilers just to, you know, for specific needs, so we're not having to deal with implementing, you know, these, these things, all natively. So we can go out and sort of steal functionality from from, from wasm right now and then bring that back. That's my

Transcript limit reached

You've reached your **30 minutes** per conversation transcription limit. Upgrade to get the full transcript.

How accurate was this transcription?

00:0042:01

AI Chat

Outline

Comments