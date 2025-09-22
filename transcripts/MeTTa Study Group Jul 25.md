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

![](https://profile.otter.ai/ANVOF4NASYGTZ5SR/ANVOF4NASYGTZPQT)Number4 x

Jul 25 at 9:14 am

1 hr 18 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

code reduction, no eval, atom, expression, map function, quoted expression, superpose, interpreter, type signature, function arguments, type constructor, MeTTa type, code manipulation, function evaluation, problem-solving

## Speakers

Nil (80%), Speaker 1 (17%), Speaker 2 (2%), Rene (1%), Alexey (1%)

Hello. I again, is it?

Is It sounds working.

Yes, Okay, I

This You're

I have a question regarding

how to control

reduction, like when how to pause reduction, how to resume reduction. And I'm just trying to find a file in my on my hard drive that had a bunch of these kind of problems, but I can't, I can't find it anymore. So it's a little difficult to formulate more precisely my question. I'm still looking i

Okay, do you mean you? You all can right now and you find something ask a question, or, do you mean, we could try to explain something in general,

right? So, so I mean I remember? Well, the problem is that I remember very precisely the problem, but I remember in some call, maybe last week, with some group of people, that I've also forgotten that it's irrelevant. But most importantly, I have forgotten the detail of what we were trying to do, but what I recall is that we're using quote and unquote And eval and desperately trying to control

how to write, how to manipulate a piece of code. Oh, I think I remember. Now I remember the context. Okay, maybe I'll find that file, right. So, okay, now, now I remember precisely the problem. So, okay, I wonder whether maybe I share my screen and I attempt to reconserve the problem in front of you, or I persevere trying to find it on my hard drive. Maybe give me another minute, because maybe I will find it, and if I do not find it, then I will share my screen and attempt to recreate the problem. Okay, so just give me one minute, and anybody else does anything has any Question, please feel free. Don't wait for me.

Okay? Applause,

So there are No Questions. I

I think I may have found it, but it's not as informative as I hoped it was, so I'm actually going to reconstruct the thing. So okay, if anybody has a question, please go ahead and otherwise I will go ahead.

Please look at me. I think I

I saw is the file I was looking for. But rather than focus on that, I think I will just create another one

and explain. Okay, so it's okay, so I'm

gonna say that,

right? So I have a function, and meanwhile, I have a program that

I have to think

that is going to

right. I

I'm trying to think of something that's gonna make sense. But okay, I'm maybe I won't. I'm not gonna make the effort of trying to make sense. But all right, just to capture the idea so,

so I've got that.

So I Okay, so

before I explain it, let me run this thing, just to make sure that it's running as intended. I

Yeah, unfortunately consultant cannot be probably,

yeah, so

it's like

to do that. Now I'm, I don't know if I'm deviating from from what I wanted to but okay, let's, let's, let's Let's do it, and I will course correct.

Okay, I

right? So, oh, wait, I don't even understand, so that's not what I expected. Okay, so, I mean, check, so this goes here. Yeah, we were supposed to.

So here I think we're supposed to get that

again. I

can always just take it step by step. I

Okay,

and so, and then, this is suppose, right, yeah, right, right. So

this is supposed to it is, yeah,

okay, let's try.

Okay, all right. And now

it's supposed to return be

a 42 I think.

But apparently it's it does not return this.

Okay, nil. The trick is that on Saturn returns atom. So in your second that yeah,

table, I made a typo. I put t1 instead of t2 that's why. Okay, so now this,

it will not work anyway, you need to somehow calculate t2 you expect that conceptum returns who 42 and it is I reduce it further. But as consultant returns atom, like its return type is atom, so 42 is not reduced further,

right? So can possibly

wrap it into ID function, function, yeah, you can add another into ID function.

Oh, damn it. What happened? Just a second. Okay, so just to be absolutely sure, okay, so this was reduced because it was reduced here, right? I mean, yeah, yeah, okay, it was given here. In fact, it was given here at flu 42 Yeah, correct. But by the time it arrives here, then it reduces,

yeah, you can check it by wrapping two into No. Level,

right? So I see right, yeah, okay, okay, so I think it's, it's it kind of answers, think it answers my question. Yeah. Yes. So, okay, so now, so if I do that now, I am getting this, because this thing is expecting an atom, something that doesn't reduce expression, right? Expression? Well, I think so well, there was this issue where I think that this would return. Let's try. But Hello, expression. Well, so now I'm so confused, because I thought that this did not have the effect of pausing reduction, but maybe, maybe you have changed, maybe you have changed hyper on experimental Italian so that it now.

No actually, yeah, expression has the same effect as as Adam atom, yeah, I believe it was from the very beginning.

Okay, all right, because there was an issue.

I mean, if you pass an expression, it is not reduced. If you pass in something, but you probably, yeah, if you pass not expression that says type check error here, but if you pass an expression doesn't reduce. It is not reduced. So

if I do that simply, okay, I see, okay, great, well, so okay, maybe at some point, yeah, I do recall it was like from the beginning. And I think maybe at some point it was no longer like that, and that created a few problems, but it looks like this has been fixed, and it also looks like in case. So let's say now that, let's say I have another function here

that's going to be

bass y, and it does something like, I Don't know,

R,

Y, and then I replace this bypass. Then I expect it is going to reduce. No, well, now it's a bit confusing, right? So this is the first one, and right, so it is reduced, but if I wanted not to be reduced, then I would write no email, and then it doesn't reduce. So, okay, and so just, just let me so of course, all right, so now I do that, if I

Okay, if I

return that, Of course, of course, it is going to reduce. I and so now let's say I pass this thing somewhere else. So, and I want this not to reduce either so, but I do that and, okay, let me just try that. Just

make sure,

right, so I was able to suppress reduction at every stage, because every time I use no eval, okay, I think it answers my problem. So, yeah, I think that's, I think that's the solution. I would have to go back to the initial code and and just experiment, but, but I think it answers to the problem I had. So, yeah,

right. And indeed, the other thing I had tried is because, okay, I mean, well, that's a solution, so at least I have something but the other way. So, because every time I'm carrying out this thing, I need to wrap it in no eval to make sure that it doesn't reduce. I was wondering if, if there is an alternative where I, for instance, use

quote

and unquote, for instance. And I had tried that, and it did not work. So

if I,

if I do that, I'm going to get something quoted right, and so, and of course, this, I can carry it. Let's try. So let's say, for instance, t6 it takes t5 and so I

so I was saying, right? So, so now I have a little bit of a problem, because, let's say that I want to wrap something around t5

if I do that, it's going to wrap outside of the codes. So like

how you can write probably function which pops up. Quote,

right, unquote, right. But I don't think let's try unquote. I don't think it's going to work. It's straight, oh, it works, but it has reduced, yeah, so that, I think that was the issue I was experiencing as well. So how do I wrap?

You can try and quote. You can try to to wrap unquote by no evil,

pardon me, no eval, yeah, but then the unquote is going to remain right. Oh, wait,

what happened here?

Okay, okay, probably it doesn't.

Yeah, you're right. It should not execute on it should introduce of quotes, and the result

is surprising.

Could you please? Maybe you did not save the file? How did me?

I mean, maybe you can try to save it one more time.

I'm sorry, I couldn't hear you.

Ah, sorry. I think maybe changes will not saved, and try to save file gain and run it again, just To make sure. Okay.

Transcript limit reached

This conversation was created with an account that has a 30-minute transcription limit. Ask the owner to upgrade their plan to allow access to the full transcript.

How accurate was this transcription?

0:00:001:18:05

AI Chat

Outline

Comments