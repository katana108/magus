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

![](https://profile.otter.ai/ALYGSUM6TC6GXVLZ/ALYGSUM6TC6GS5ZQ)Yenatfanta Shifferaw

Jun 27 at 9:39 am

1 hr 18 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa Study Group, installation issues, Python client, server branch, backward chaining, process calculus, mock server, data preprocessing, parallel execution, permission level, debug builds, knowledge base, evidence, recursion, interpreter.

## Speakers

Adam (76%), Nil (14%), Alexey (11%), Speaker 1 (<1%)

Hello, Hello, Hello,

I was hoping Alan would join to show us. Mm, two, still not here. He mentioned that he would make an effort to join, Yeah, this Meeting. I

MeTTa itself. I do not have any pending issues or

oh, wait, I'm

I'm very confused. I think

multiple people want to join this call, and I see a

Adam's here, hi, yeah, I

was just saying that for MeTTa itself, I have no pending issues. I don't know if anybody has, but personally, I was looking forward to have you join Adam. So

that's, that's great,

yeah, yeah, we can, we can go over the backward general, or I can. We can discuss some, some grinding stuff, like, yeah, lots, lots to discuss. We always have the issue of scoping also on our agenda, implicitly, I believe. But yeah, we can, I can. I can take some time to walk through that.

I was wondering Adam, if we could begin with a walk through the installation, because I so, yeah,

that may be better written up than me. Me saying it, but on the other hand, this call is probably recorded five times over, so we can refer people to the video of the installation instruction. Sure. I mean,

it all depends on how long do you think that may take? I've already tried on my end, I didn't I did manage to compile more, but first I had to fix a few trivial issues. But nonetheless, it wouldn't comply right away without these issues fixed and well, but then I just don't know what to do with that, so I don't even know if I'm doing what I'm supposed to do.

Yeah, that's, of course, like a consumer problem in the sense of what problem do you want to solve? But, well, nothing is not straightforward.

Yeah. So I just want to be able to like, to send an end to program to a server and see the server react.

Cool, but let's do that. All right, so,

right now, work with a mental backend. Come again? Does mock server work with Amen to backend already?

Yeah, kinda in the sense that I, since we emerged, I rewrote the unifier and the major matching algorithm. So, like the there's some things that need to, need to be back ported, but the I need to backward, but the all the normal or all the normal stuff, quite unquote, should work on on the server. So let me, let me share the situation and indicate so. This is the mortgage repository. There you go. And

if you go to server, then this is, this contains, like, a lot of lot of refactoring, like making making things safer and making it work on on the server, and then the easiest or way to use It's probably using Python or something like Python, which else calls. And I'm doing that way. So we are in Server, morgue Python, and then to cargo build before, before we'll get to the answer. The basic interaction paradigm, right is that you have some binary of the morgue server people want. They can distribute some x86 binaries too, and to avoid needing to go through a build process. But then you can use this managed Mark instance to spin up the server. And if you use and terminate, it will also well terminate the server. Can also use, let's go here. You can also log the questions. Okay, go ahead.

The first one. Do you plan to keep server in its own branch, or I'll go into merge it into a main branch at some point.

Yeah. So the So currently there are two active branches, which is server, server and unified transition rework, and we, we plan on merging server into main or sorry, first merging this into server and then merging server into main. That's the current plan. All of these, like all of these, contain a bunch of work, to be honest, like they so there is a large different, large difference between these three branches and the So for now, like to use this kind of stuff in you need to server branch, but then we do definitely plan on Making it the default way to interact with Mark. So

uh, Okay. Another question is, why do you think it's convenient to use a binary file? Is it true? Because not everyone is going to build it.

Yeah, so you can build it and will be more performance, most likely, it just That's all right. So if you want to build it here, start to build insertions. If you're interested in it, you will, first of all need rust. So you can do rest up for that. Let me share, share that.

Well, I know it. I just wonder if you think that people are going to use separate binaries more often than, say, HTTP servers.

I think most, most, if not all, of the work can be done via the server, and the and the interaction paradigm will be over HTTP or some other protocol that the server supports in the future, rather than Like a calling it as a library, that makes sense,

yeah. I mean, you started with your Python client, the default operation mode is to try running a binary instead of connecting to a server instead.

Well, so

it does.

So there are convenience methods for all three, right, like so connects. If we go to connect right, you can specify either a URL or a binary path. So yeah, so you can, you can host it, host it elsewhere, hosted locally. That doesn't really matter. It's first tries to connect. And if it, if it's can't connect, it tries to start with the binder, okay, all right, so we have a question. Oh, no, takers. Note takers are spamming my links away. So, and when you're connected with the server, you get this server object, and you can, you can do the commands. One of the commands would be uploads, some, some literal space, or would be to do like a match statements over it, where you say, Oh, we transform everything that looks like this to something that looks like this, and we can execute as a specific we can execute statements on a specific threat. For example, here we put things in the execution space, so execution and then this is a threat ID, and we say, All right, we are going to run the execution space with this threat ID. And then finally, we we are going to download the results. So you may note a few, few other things that I skipped over. There are block calls in here. This simply means weights or pull the server until, until this is done, and you can specify a delay and or like a polling algorithm for that. You may also notice the underscores, so we have most things that are like

both underscore and non underscore versions. The non underscore versions allow you to specify a pattern and the templates so you can transform your data that you upload to the server. Let's see that in action.

Let's

right here. Here we have a non underscore version, and you see that we start with a pattern that looks like data sets simple, and then the contents of our of our data set. Then we export it, and we drop the simple wrapper so we just say, data sets x so on exports, it will match everything that looks like this in the space, and it will write out everything that looks like this to the file with the paths that you specify. Questions so far.

So the reason you have this s export was just in case, you don't want to pollute the space with the exact expression, then you can just use that,

right? Yeah, so the that would be like the reason for the transform statements, right? Like, if you, if you just want, like a match statements, then you can just use the Transform commands without going to amend two so for data pre processing, like this example, that works great. And then this statement is simply exporting the states to a file, right? So it's I want to know for like, what I want to check manually that this is actually this, the thing that I expected to do. So, yeah, that makes sense. Okay, so notice one fun thing here is that none of these transforms have a block statement on them, so they will all be performant in parallel. So if your computer has more than four cores, it will actually or has four cores, it will actually run four times in parallel, and performing these different match statements in parallel. And then finally, here, this is really important. We have, we are trying to extract parent relationships, but there is only child of woman and child of man, things in the database. And so they have these two match statements. They have overlapping destinations. And with the overlapping destinations, we want to do them sequentially, so we block on this one and then we execute this one.

What happens if you do not do it sequentially? Then

this the second statement here will fill and you will get here in the in the events, you will get pre processing events transform fields

which

could not get right permissions to execute this. So if you're collaborating with multiple people on one server, this becomes important, right? You You want some coordination mechanism such that you're not overwriting each other's work, and this is to prevent some some basic you

have locks at the expression level,

not at the expression level, but at the permission level. And the permission level in this case is the prefix, the constant prefix of the destination. So we are writing like a few 1000s parent relationships out here, and we they are under one lock, which is this one the simple parents. And that's actually how, if you look at here, this is how the whole code bases work. Or this whole example is constructed.

So we have work at Island kg, work at data sets, work at source. And this is, this is wrapping, wrapping the expressions into finer namespaces such that they can happen independently. So if you're connecting to a server, to a URL, right? And other people are working on other projects that are not ants, kg, then they will not conflict with anything you're doing here. Because, basically, if I edit this data as an example, right, everything you do will look like aunts, AG, and then some, like, Royals 92 and then some simple blah. And here will leave your actual parents. Eventually. And because the because of the work at statements right, it's it causes to be prefixed by this. And then anyone else that's working on the server, like, for example, in someone else has has a space has a bio atom space subspace, and they are working on GDR, and

they have genome. I don't know biology, so I'm just saying something, right? And so these two task tasks can happen in parallel on the same server, and the prefix is what separates these tasks, right? So

yeah, all right.

And then right. So we connect here. We actually, for this example, we first clear the subspace that we clear everything first, because we want to this is a test script, and we want to make sure that the test runs. We are not fooling ourselves in that the test runs by already having done all the work. Few other things that here, here's another projection, so non underscore things. So we have a transform statement, or a match statement, we match on all individuals, and get out their name and prints print the name to the screen. So, if we actually run this. I don't know if I have, everything's at that button moment. To run this live, but if.

Details on this call. But the basic idea is that we want to add, we want to do some piano arithmetic in a process calculus. So this is very, very emulated, right? Like we are on an interpreter. We are running an interpreter that runs an interpreter that emulates some numerical things. Anyways, it's very MeTTa. And what we do here is we say all right, in our little DSL here,

I want the results of adding two and two,

and we upload this battery dish in a namespace called battery, and we upload the actual interpreter here in the top level namespace. And you can see, then in the top level namespace to match things, we actually have to wrap it by by this battery right here. And then we execute our our process, and we wait until it's finished. Here we use inference control, namely we are we have two rounds and we have them. This is all like program, just for the this is always just for the example, right? This is not hard coded in any way. So we run this for 10 rounds, and we alternate between doing step zero and step one. And you can see here the process calculus is what we call this example. So if other people on the server are running other tasks on other threads, that's perfectly fine. We wait until that's finished, and then we project out our results. So we match on everything that looks like this. So what is being sent to the results that x we want to show. We get the data, we print that data,

and we assert that this result is

the piano encoding of four.

Now I covered a lot,

so I will check in. Does this still make sense to people? I have a question to other people. So basically, there was a question on mattermost Some time ago regarding this Python client, whether we want to make it a convenient way to use it from hyper on experimental. So I have a general questions question while everyone is seeing how it can be done from Python directly. It's good time to ask if this is a preferred way, or is any request for making mm two and mock server, a sort of library callable from hyper on experimental MeTTa. So does anyone want this, or

is it enough, or more preferable to call it from Python directly? Yeah.

But I to to the answer, does anyone want this? I cannot provide a personal answer to that. It then the answer should be yes, I suppose. But to be

Transcript limit reached

This conversation was created with an account that has a 30-minute transcription limit. Ask the owner to upgrade their plan to allow access to the full transcript.

How accurate was this transcription?

0:00:001:18:25

AI Chat

Outline

Comments