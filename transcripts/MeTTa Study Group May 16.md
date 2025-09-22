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

![](https://profile.otter.ai/ANWAXENATEW7FVHK/ANWAXENATEW7CJOV)Charlie Derr

May 16 at 8:30 am

1 hr 11 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa Study Group, note takers, hyperion experimental, context space, assert options, standard library, built-in module, filter atom, minimal MeTTa expression, unit type, functional programming, type checking, concept blending, motivation system, GitHub issues.

## Speakers

Vitaly (47%), Nil (27%), Lake (11%), Speaker 1 (4%), Matthew (2%), Emmanuel (2%), Zarathustra (2%), Speaker 2 (1%), Speaker 3 (1%), Speaker 4 (1%), Douglas (<1%)

Hello, hi nil, hi every lots of note takers. Douglas,

I I wonder

brand. I had to systematically lots of lots

of note takers, so I probably missed some people there.

Yeah, they need to add a some kind of feature so that we can filter by humans and Non Humans, because it's a little bit annoying.

Robert,

hello, hello. I

don't know if I got everybody who's live. I'm not naming note takers, so

you are not what

I'm not saying. I'm, I'm. I was trying not to say hi to the note takers. I just was trying to say hi to people, yeah,

it is a challenge, but the people

are like the small fraction,

because I'm tempted to just not accept AIs. But on the other hand, some people you know would benefit from having,

I think, and this one, there's no point not to. There's nothing this we want to kind of spread information around, is

right? There's that as well. But, yeah, this Vitaly,

can I have device decent? Because I have a new kind of man, I'm using another microphone, and it's kind of far away from me. I mean, it's like, like, over a meter away from me. Can you hear me? Well, or Yeah, no problem. No problem. Okay.

Great. Thank you.

Well, I'm sure Alexey will be here, because he said he will prepare to the flight. As far as I understand, he has a flight between Dubai, or maybe, okay, at least in this direction, Dubai,

and

he should start his trip to Dubai today, but, yeah, I'm not sure which time exactly. Maybe he's

gonna be at Dubai, right? Vitaly, ah,

I should be, but unfortunately, I injured my leg and oh, sorry, I can't walk now, so

not even with crutches.

Ah, great. I don't know this word, but yeah, this, I can walk with scratches, yeah, I can. I can do big, long

arms, yeah. So

I have one the player. I can work with them. So I will do it, yeah,

it's just up in that. Multiple times. So I know,

okay, okay, I'm not used to it. Actually.

I got to be quite proficient in in using them.

Okay, you can show them. Mr. Claus,

you can go really fast. That's not safe, necessarily, but you can,

yeah, I feel always safe. Actually, stairs. What bothers me?

So so hopefully, actually, I will be able to step on my leg to the end of the week, maybe in couple of days, but I'm not sure. So right now, I'm, I'm going to go

a

way to someone else so we can start. So

I think we should start. I mean, I'm going to have to leave. I'm just backed up all day, so I'm going to have to leave when the meeting ends, but I'll make somebody host, maybe nil.

Well, I'm also supposed to leave at the top of the hour. I mean, well, so the call is optional, so maybe Vitaly, then

maybe you can Okay,

okay, so we maybe should Get a start. Anybody want To start us off? Yeah,

oh, okay, I can, I can tell about some changes in hyper on experimental. So yes, of last week and this week, actually, I was working on trying to implement different new assert options according to Nils issue, just to understand, wasn't this possible In current Hyperion experimental implementation? And I have found that at least I made some experiments and published results in the issue actually. And I have found that I need something, some new operation, to return current context space, because ampersand self is not like it is not interpreter context dependent. So understand self always returns to the space where it is used, but when you, for example, the right standard library, some function which interprets atom in the context of interpreter space, you cannot use self because self points on almost a belief, Atom space, not at some, at some current interpreter, Atom space, and I have introduced new operator, context space, which returns The context space of the interpreter, and using it, I wrote new implementations for co ops and the shirt without grounded atoms. I mean the main functionality is implemented in pure MeTTa, now grounded atoms, I used the only grounded path is to compare two vectors of results, because it just simple to call it in rust, and I already had correct implementation. So I'm almost ready to publish this result. I already merged and kept space, probably, maybe not. I'm sure I was going to, but maybe I decided to implement corpse before it and check it well. So I will implement a short echo, short alpha equal using U in pure better using U operator. And then someone or okay, it is possible to introduce new implementations of asserts, and it can be done in pure MeTTa using current implementations as examples. This one part, and also, I have introduced some example of built in module for the hyper road experimental core library. So the king is done from St Petersburg team already moved some part of the standard library into the built in module. For example, random, random functions. Library is moved into the random module, and he also works on file, input, output API, and it will be interviewed. It will be introduced as a separate built in module. So it is just like some part of the library will be moved into the separate modules, native rust modules inside core library. Probably that's it.

Yeah, that's all who I said.

Okay, thank you, Vitaly, so you were talking about, I think about the assert. That was the bug where when we would Oh, no, no, wait, it was with super Oh, oh, well, because we had this problem with superpose, when we would know when we would subtract the superposition so two superpositions, we would apply subtraction to that, and when we would replace one of the superpositions by a non deterministic function that would if executed, corresponds to them to an equivalent superposition, then it would fail. And so it looks like what you are describing with the with the cert, or, I don't know what, taking into account context, it looks like it's fixing that. Am I correct or

Okay, actually, I didn't quite fully understand you're talking about. But the issue was that, for example, you want to write some standard library function which gets an atom as an input, and then eliminates it and analyzes the result. Right? You cannot quite do it now, because, I mean, you need, you need some space to interpret the atom in context on the of this space and function in standard library cannot get this space. You need to run results. If you want to collect all kind of results, for example, empty result or result, you need to use collapse to get the whole set of results as an item. And yeah, so the collapse is a function which cannot be written without congested from space, and it is the reason why I need to introduce some operator to return this from space. I uh, okay, okay. Now it is, it is possible to write some like some standard library function which calls MeTTa interpreter from from inside using the context atom space, and correctly interprets atom in context of the like of the caller, for example, call your space,

yeah, okay, okay, I see that thing. It's a it what you're saying confirms what I thought that it relates to an issue I just based it on, on, on the chat that that involves what involves subtraction, but in fact, is probably caused by what you explained, I think, but, but in any case, okay, that's nice

whether, yeah, actually, yeah, actually, I saw this issue and yeah, it also has the same root cause, so Nicolaus fixes it, and Let me check if I raise this. Yeah, actually, yeah.

Okay, no, so yeah, I will learn just after meeting, it's already I just didn't do it because before, because I wanted to check, I can implement a search on the top of it, to test it, to test it better.

Okay, great. Thank you. More people have joined. So maybe, maybe we get people with questions. So if so, please feel free. Applause.

For instance, I saw, I know lake you had a question. Two weeks ago, and I wasn't present. And if you still have the question, please feel free.

Maybe you have the question, I guess it's here. Let me get set up, and I'll ask unless anybody else has A question. I don't want to take up space. I

I think that hmm. Okay, so just to review the question again, you know, I'm writing this motivational framework where we basically are looking at a set of actions and trying to decide whether or not to take that action. So we want to look at the considerations and discouragements for our goals, and we want to choose the action that is you know best satisfies our goals and least satisfies our anti goals. So basically, we do some calculations, we come up with our action choice, and then I wanted to pick the action from a list. So as an example, if we do score all I'm gonna comment this out and run this so we would get a list with the final decision score for each action we would see the talk has the highest decision score all good so far. But then we want to choose the action with the highest decision score. So normally, this would just be applying a simple like filter atom over the list, finding the one that has the highest score and then choosing the corresponding action name. However, I've been having a lot of trouble with filter atom and just the order of evaluations and things, right? So this is the example of filter atom that is in the documentation. So I'm pretty sure this one, yes, sorry, this isn't exactly the same I put in this let here for the greater but if we take that out, and then we reset it. So this is what was in the documentation, right? But if I put like the let in there, for example,

it does not evaluate, probably because this doesn't fully this doesn't fully evaluate. So the crux of my problem is, I'm just trying to figure out what,

how I would go about using action like filter atom correctly, so that it's the predicate fully evaluates.

Okay, yeah, actually, because it was written as a part of minimal MeTTa interpreter, and I did not actually think about publishing it as a part of standard library. It was just like we can at the moment, we don't have any private functions in our modules, so it is public because I cannot make it private. And task was how to say provided as a part of standard type library. But actually the issue with this code, I think, I mean, I'm almost sure, is that filter atom expects you're providing some minimal net expression as a filter expression, and ML is a minimal meta Construction. It works, but when you wraps it into the wet. Let is not minimum MeTTa instruction. It is just like general MeTTa function, and it is a part of standard library and the whole filter expression. This kind of filter expression is not minimum map expression and fit the item. Cannot evaluate it properly. I mean, it's called just don't expect it. It is, I would say it is a bug, like for now. I mean, at the moment, I would name it back and actually in the work which I just described, I also fixed some similar issue inside another, another similar function, although atom and I know how to fix it actually, maybe just to not wait for the PR I can publish, I can I can provide you a code of the filter atom which should do what you want me.

Okay, well, he

could be best

if you want to pass it off to me. We can test it right now, if you have it right now, or I can wait for the PR but I would like to understand better conceptually what a minimal MeTTa representation is, and any documentation for that so that I can better understand because I take it that you can't reduce a Like a non minimal expression to a minimal representation. Like there's no way that.

I mean, there is a way to do this, but you need to embed MeTTa return to this interpretation yet. So it's kind of known that doesn't make much sense. I mean, when you can use the filter atom, it was exactly I wrote MeTTa interpreter in minimum method terms. So I just wrote MeTTa interpreter in minimum MeTTa language, and filter atom was part of it. Okay, let me just find the code of the original function. And

sure I will.

I will mute myself because my keyboard is very low. That's fine.

Lake. I have a kind of another answer to that question. But you mean well? I'm almost hesitant to provide it because it somewhat goes against what the standard library is offering so but, but nonetheless, if you're interested, I can show you that

the ready.

We might as well just take a quick look. But I do want to try to work within the standard library, or at least the standards like, I want pretty standard MeTTa code I don't want to break necessarily,

yeah, yeah, that's that's completely understandable. Do you want to, just to check is if Vitaly is ready, and if he's you can just continue and and if he's not, we can decide whether you want, you want me to, to pollute your your pristine mind about MeTTa and MeTTa way of implementing things,

I mean, it pollute away. I would say I need all I can get at this point. But Vitaly, are you ready?

Yes, just finish the occasion. Sure, let me copy it. Sure why I cannot try this file now.

Uh, into the chat and, okay, it has a number one.

Yeah, yeah, okay, so

actually, it's almost the same as a library. I added a tick symbol at the end of the name to like to make it different from the stands for everyone, and it has only one difference, the MeTTa call around the filter expert, yeah, if you quoted this into your code, it should actually work with that as well and with any other expression.

Let me just show it. So check the numbers out. It's obviously not liking the apostrophe at the end. Let's try changing this to ones.

Now it's saying our I

parentheses are off. Where is that coming from?

This I

guess you didn't do the closing parentheses is that it

should be, should be, actually correct.

I posted it is out. Maybe it looks like it cut out, yes,

select this is now,

yeah, it looks like it cut it, yeah, I'm not sure if

you want to give me the second Part, then I'll bring that in. Okay?

Chain calls, no.

I remember looking this

up, okay, from arrows. I

uh, yeah, I will let this fix into the prick,

filter atom one. Okay, so let's try this. Filter atom one with our first base case. It's good, and we'll do the left version. I'm

right?

And then we'll send run it again.

Did I screw something up?

Okay, no, I don't see like those. The only difference is a MeTTa instead.

Okay, maybe,

yeah, there should be recursive call it probably you forgot to.

So this is filter item one, filter item, one, yeah,

it was one here.

So you just set that one into the third line, or it was,

yeah, I mean, I changed it away from the parentheses because I was screwing up there.

Okay, actually, I didn't try it, but one should work as well, right? Yeah, okay, okay, let me try it offline then, or I can, if there are any other questions, I can try it.

Okay, why don't you try it or just see it on your end? Let's maybe go back to nil. If you want to go through your solution, I

am I understanding that I can Share my my screen or, yeah, yeah, okay.

So, um, okay, so I, I personally never use the

higher level operators met developers, which just filter and so on. And the reason I do that is because I am essentially too scared to manipulate tuples. Because I know that well, so I know that if I if I mean that situation. And up happens to be a function that's defined somewhere these things is spontaneously going to reduce. And so since I don't want to deal with that, I systematically put everything into an explicit list, and it's like the heavy you know, so this I would represent in this way?

Yeah, I had been doing that, but then I noticed that it, well, it was a little bit awkward for me to work with, and then the standard library didn't expect that. So that's why I moved it back to

the Yeah.

I mean, I totally understand that in my case, because my code is generating a lot of weird stuff. It's like it's the purpose of my code is to generate things, either programs or proofs, or is to generate stuff. And so I prefer from my case, I'm a little bit more I'm overly cautious. Let's say there's another reason, which is, let's say I kind of come from a functional programming paradigm, and I just, I like it. I'm used to it. And so that's the other reason why I tend to just compare everything as explicit list or explicit whatever, you know, data structure I want. And well, well, there's that. There's actually a third reason is because, when I use list, then I could say that. I can say, well, I want to list of number. I can do that. I want list of, you know, whatever weird thing I have defined, I can do that. And I can do type checking, so on and so, right. So for these three reasons, I prefer to use the more traditional functional programming way of processing containers and so that's, for instance, an example of getting the maximum element of the least. So I know you are using filter. You seem to describe that you wanted to have the max. So that's what I thought about that. But filter would would just be a similar example. So you see, I have, I have a type signature where I'm going to take a less than operator

and

a list of something, and then I'll get that thing. I'll get the maximum. I have these four fold. I have these four map I have Yeah, and so so often I just write my MeTTa program, really the old fashioned functional programming where I'm trying to one liner of a clever color fold or something.

And most Yeah, I mean, I

Yes, all right. Well, I

initially started coming with expressions because I thought they were basically just lists, but I realized it seems a bit slow when I test the speed and it's I'm only likely to just run into weird, unexpected behavior because they're free floating expressions, whereas, while the list seems a bit clunky, it's just very containerized and clear. Well, I'm giving up and following suit.

I see so I can't stop this. You mean

so far leading in the direction of that, or having, like, more explicit symbolic tags that will prevent things from being treated more arbitrarily. Okay,

one comment the explicit nested list is, let's call it slow because, for example, for indexing, it it has to iterate also using and this isn't the case for Amen table, because a standard function to index by an index.

Yeah, you could have a point. I mean, I'm sufficiently paranoid that I would rather go with something that makes me write nicer code, nicer according to to my subjective measure, anyway, but and I'm okay to trade a little bit of speed, but I've done a bit of benchmarks, and I didn't see a difference between doing that and just manipulating tuples. For instance, I know that I believe St Patrick was able to measure a considerable difference with using superpose and and superpose is okay if your container is not sequential, but if it's sequential, I really don't think it's a good idea, because it's not supposed to be ordered.

How fast this will pause,

honestly, I forgot, and I think it's, it's probably constantly evolving so, but I'll tell you that MeTTa log is, I mean, is just, can run can run that? I mean, any of these, you know, typical functional programming go through that with no problem. It's really so I'm not super concerned about those sort of things, but,

I mean, it can be important, then it's certainly true,

yeah, But then we had a bit luck, said the current version of a metal log for us back into interpreter interpreted mode.

Pardon me, into a left mode. I couldn't understand

inter interpreted mode. Somehow.

I'm sorry I cannot understand the word interpolated, okay,

interpreted,

interpreted, oh, right, right, yeah, yeah, yeah, sure, sure. I mean counting on MeTTa log that's as a compiler, but,

uh, and almost works.

And, and, of course, we have the more back end, which is coming soon as well. So, but, I mean, yeah, sure, the problem working with something slow today is that you can't push your experiments very far, and so that's problematic. That's I certainly recognize that. But for me, the ability to specify the type of a container is, I just feel too good about it that just comment, I can't let that go.

The points distance, so linear overhead is always and

you're talking about linear overhead. So maybe you because maybe a list is not what you want. Maybe what you want is a sorted list, for instance, or something else you know, but something that emulates a set percentage. And then you can, you can insert, you can retrieve in, supposedly, I mean, sub linear time, but, but, but I mean, well, yeah, I don't know it's getting a little bit too deep into even, like the MeTTa interpreter and back and so on, but purely from a traditional, you know, complexity considerations, wow, you can implement whatever you want, I mean, so you can go suddenly over for sure.

And maybe at this point I I should let the telecom guy

sorry, no, did you mention

I thought that You were preparing something Vitaly, that's why.

Okay, actually, I tried to check with the item why it doesn't work, and I found it doesn't work, actually, yeah, my implementation, my fix, doesn't work, at least, but I will do the research. File doesn't work, we'll fix it. Actually.

I think if it is a part of standard library, it should. It should work as expected. So important, be able to give MeTTa expressions as a filter expression, so I will check where this book.

Okay, thanks. Just let me know when You

okay. Great. Thanks. Bye. I'm

okay, any Other questions or issues you

I have a tiny question. What is supposed to be the you? Okay, let me wait. Maybe I'll share my screen again, slightly easier, too. So what's supposed to be the unit type this, or this and, and so I believe men, okay, okay, yeah, please go ahead. Detail, actually,

the first one like empty paralysis is a radio unit type, right? So let's see unit value. And second is like, yeah, it is a definition of unit type. So, no, the first one is a unit value. It's not unit type, it's in value.

So, okay, so that's a unique Okay, so that's clearly a unique value. That is clear. I thought it was also unit type, okay. Type,

yeah, actually, it's Alexey who proposed this notation. I mean, for unit type, I'm not sure maybe maybe he, like, he get it from some vehicle or book. Maybe he just imagined that it's a. Actually, I don't quite, quite understand the second notations. I mean, why unit type is designated like function which doesn't have arguments doesn't have return.

Yeah, yeah.

So probably, if you get type for the first one you it will return. Maybe expression, I believe the second one, maybe it can be type. It's like, get me. Yeah, you can try and get type.

So unfortunately, my I haven't compiled, yeah, it's, well, it's kind of a new laptop, and I haven't, I haven't installed hyper on experimental yet. So we're going to be able to do that right now.

If you have a code you can use, if you just go on the Ripper, you can use car grant,

all right, right, of course, and like, like, Okay, yeah, let's do that.

If you have rust installed, actually, because if you don't have rust installed, You

I understand, no, I'm hoping to.

I was actually hoping to use MeTTa line Doug dead, to run my code that I realized.

Okay, I actually posted the answer from my Okay, thank you. So it's undefined for the get type focus for both, get type calls and expression for both, get MeTTa type, I would say like, it's probably not very correct. It should be like, get type of the empty parentheses should return the type, unit type as a result. Okay, I'm not sure if it have some consequences, because empty parentheses, empty empty expression is used widely, probably, and if I will just set the type in standard library, it can break something, but it can be otherwise It can be easily fixed. And we also cannot type for the unit type, and it should be type, I believe.

So, yeah, it's quite clearly should be type. But, yeah, yeah, okay, okay, okay. I mean, it's not a very it's not very important to me, but I was still a little bit puzzled by, still a bit puzzled by it. Okay, all right, I guess when Alex, when Alex, say, we can ask him okay,

into semi I tried to add type for the empty expression to The standard library, but it still returns like, can you find it's kind of not probably type chicken doesn't try to get the type from the standard library and just calculates it. But it can be fixed as well. So

I keep imagining there's going to be a certain point where unit type is actually doesn't return anything kind of like becomes the void type. Or, you know, something like empty could be considered, since it doesn't return anything, be like a void type,

yeah, it's like a void Yeah. I'm not sure why Alexey chose the notation the function which doesn't have arguments and doesn't return anything, you you can probably yes, name it void, for example.

Well, I think there is a decision that maybe everything just so that fits in with the bigger ecosystem of the programming world has to return something, you know, so everything had to start returning something. Yeah. Well,

if we look at the value like to the function which just returns something without getting an incident, yeah. So in this picture, it's correct notation, right? But we don't have notation for otherwise. Quite not, not aligned with other venues.

Maybe the same mean. Meant that, potentially, we should have this type for the values as well. This idea, the moment when he thought about his type,

well, unit type could actually just be literally called unit type, like the symbol, you know, that would be okay, too, yeah, yeah, it

could be any, any simple,

I mean, to me, Technically, using the expression as a type kind of can read some, some technical issues with this inside interpreter, experimental code. But hope, I mean, like it doesn't have such effect.

By using just the arrow with the parentheses. It doesn't, like, add a whole new symbol to the interpreter. Like, I like it in a way, it's like, okay, we're not going to add any more extra for the namespace to have this unit type, you know, almost because the arrow is already part of the type system. We'll just use, you know, symbols that we won't add any symbols to the types if we want to have this type. But okay,

yeah, well, I mean, that would

be an argument of why the arrow in the parentheses was used.

Yeah, maybe feel such a coach. But, yeah,

Nil really likes to try, you know, use functions as a type, and it works out really well to do to use the arrow in as a type declaration for a function, like, we're going to pass a function here, so we're going to use an arrow here. Yeah,

what arrow? Okay, maybe you,

but yeah, it doesn't make use much. Doesn't fit in with the unit

type that Well, I

Oh, I guess functions that return unit type can always return an error too, right? So, like import returns unit type, but it also might return an error. So maybe error type, you know, the error type is a type of unit type,

well, actually is a part of any type. In this sense, any function can become an error and the interpreter expects it. Oh,

you're right, yeah, something, it could return a string can decide to return error instead, yeah,

yeah, only if you if you have stronger probability type system, right? I mean, not strong, but, but, but more formally described then, yeah, we, we would need, we would need to add type part of any type recently, but at the moment, It's implicit is a part of any type. So I

Okay, I'm going to move to my call.

Thank you all the way.

Thank you. Nil, bye, okay, if there is no other question, they can

finish the call. Yeah, I'm hoping to ask my question, probably

within our next meetings. Yeah, maybe next year is or fall. They're actually working on the concept blending with the RFP, yeah, and also analysis, yeah, so and how to find Tina with MeTTa programming language, yeah, quite work, trying to just read some research papers on that. Yeah, so hopefully, if there's a clue on my end, I will just ask questions regarding those area. Yeah, thanks for the call too.

Which RFP is it

okay? I think they have one on experimenting, experimenting with that's concept blending. Oh, listen, yeah, as far as experimental concept blending in MeTTa,

using so including fuzzy and para consistent with MCA. That's from our concept analysis in MeTTa.

Yeah, very good.

Yeah, actually, other places to ask questions, like if it's hyper on experimental specific example, you can ask it, raise it as a GitHub issue. To me, it's probably the best way to to look at it. Or here you can use some another most chats, example, MeTTa study group or to ask the question,

that's fine. Thank you.

I've got a question as well. What of MeTTa with with motivation systems. Do you also speak on that? Just ask the question.

Sorry, motivation system. Sorry, Musonda is the question to me. Maybe you can put it in those words, because I didn't quite understand.

Yeah, I'm asking the purpose of the group whether you also touch Yeah, unlike motivation systems with MeTTa as well, it's just the question I was raising. Okay,

I'll just say that yes. I'm also working on a motivation system in MeTTa, so you can ask questions here or in

them. Yeah, actually, MeTTa study group is very general purpose group. So the main purpose is to ask if you don't understand something about MeTTa is a programming one which for like, inference system, you can ask their agent questions about it. So if you have like questions about some specific behavior of some implementation, for example, network or icon, experimental, you can also ask there, but it's probably better to ask them on this appropriate GitHub projects like MeTTa lock issue on The GitHub.

Thank you for that. You

okay, I see some questions about map and Hello, actually, yeah, I just answered to the chat, but somebody Yes, but can have the same issues as fault and filter upon her. So I already prepared fixed for both, and it should fix web as well. Chris, ah, yeah, I will raise their fault that will raise behalf filter. I will notify people who are invested in this angle, like I will write issues. I fix it. They are PRC reverse, okay. If there's no other questions, we can finish the call. Thank you very much for participating for discussions. Please, as I said, feel free to raise any issues on hyperbole. Have specifics or some specific we have questions, or use MeTTa, stellar questions. Have a nice weekend. Thank you. Is, You

Know,

How accurate was this transcription?

0:00:001:11:27

AI Chat

Outline

Comments