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

Aug 22 at 8:36 am

30 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa, logic encoding, true and false, propositions, type system, predicate logic, boolean functions, properties, computational benefit, pull request, logical systems, functional representation, structural representation, consistent logics, abstract concepts.

## Speakers

Speaker 1 (65%), Alexey (19%), Matthew (9%), Speaker 2 (3%), Vitaly (2%), Speaker 3 (1%)

Not converted to

another representation, as this is not a big issue, but, and this is just one example, but if someone encounters some behavior which wasn't observed before. Please report this. We will explain how to fix it so it's not a bug. It's a new behavior. It can be sometimes less convenient, but it's important, because it allows doing other stuff and can be more efficient and so, so it's a conscious decision. So if anyone observes some issues, please report them.

Any thing else anybody wants to talk about, any any issues that people came up with while working with MeTTa,

had a distinct I had a distinct feeling, feeling without nil hill here, yeah, you always have a question. He always has questions, right? And it looks like he's not going to really Be back until September, so mid September?

Any takers.

I mean, I can show you something that I have, if you like. I mean, it's not really, it's something that I had from from before, but,

sure, Sebastian,

you can see my screen, right?

Yes, yeah, so,

yeah. Just something that I found interesting is that you can you can encode logic in terms of functions like the same way that you can have a first or a second of some kind of pair of two arguments. You can define true and false in that way. So, for example, true, it would just take the first argument and false the second one. And then you can then define these, yeah, you can define your own operators essentially like this, like or and, and then it works quite nicely with the type system of MeTTa. So could write expressions like this, for example, this would return bool, that would be false. And then it's kind of maybe a fruitful way to also, yeah, I suppose Express propositions with a bit more of a classical predicate logic after this. On the basis of this one, I don't know how you like, how you normally go about implementing propositions in like from a programming language perspective. But I think that for me, it was some point kind of interesting thing to to discover that that you can just define, define truth values like this, and there's some advantages that you can, you can you can pass, you know, like, arguments of arbitrary types, into into these functions. Like it could be, you could say it's something like, pause, one, two, or something, or if it was a list, then, then I thought that it could be maybe some kind of fruitful way to express, like some other systems of logic, in a sort of intuitive way, for example, if you had some, You know if, for example, if you would pass your boolean in here, like you could define some kind of functions that that depend on a Boolean. So, for example, let's say it's a predicate, like it would be so like some predicate accepting a Boolean. And then, for example, in here you you could put like lists of properties, something like that, like has, has has a tail, or,

I don't know, it's red, or something like this. And then maybe, like the right side, it could be expressing a list of properties that you would assert not to be the case of it. So, because I feel like, in some, in some systems of logic, you like, there is obviously a difference between, between claiming that or observing that that, yeah, that some kind of a thing has, has a property in, like, in a constructive sense, and then also asserting that, that a proposition is not the case of something, it's, in a sense, a different thing, if you like, then, then, for example, not Making that observation at all. So, like, for example, like you could like, and I thought that that might be like an interesting concept to explore, where you put like, your your your positive like, the propositions that you affirm to be true on the left side of an expression like this, and then the propositions that you would or properties that you would observe not to be the case with them on the right side, and then not necessarily claiming in some kind of analytical way that that they though they are the opposite. Like, maybe there are some concepts that you wanted to say something about that are like, that could have some, some properties that that could hold, but where the like, the the concept that is the opposite of of this property that you would observe, like assert, of it could also hold at the same time, for example, when you when you're talking about some more abs, abstract things like ideas or or metaphysical concepts that are beyond, like your direct observation, something like this,

just an idea that I wanted to throw out there. I don't know if you have any reflections on that. I

Oh, yeah, it's interesting To think about it. It's I'm

I don't know any of you, yeah,

well, yeah, I wanted to say thank you for sharing that you have some like code somewhere, maybe makes us push up,

yeah, I can, I can, I can, push some code.

Yeah, actually, there is a not, not yet merged pull request on jointecologic implementation in MeTTa examples, and it's a different kind of stuff with possibility to define that something is true or not, or it is unknown whether it's or not, and it has some rules for dealing with this possibilities. So I believe, for your example, will be quite interesting for the same repository as well, so you can rise a PR to MeTTa examples.

Okay, thanks. I think that was also one of the questions I had before about how you would express this necessity or possibility. And I think I'd be very interested in in seeing that that. PR,

it seems like it would be very useful for finding different logics and parent consistent logics, etc, like Alexey alluded to i

Because, you know, I felt like, maybe, if you approach it like this, like I haven't really given much thought about what, yeah, thanks. What logical system it would adhere to. But I think there's maybe some kind of, perhaps some kind of computational benefit, because, like you, if you would pass false or true to hear it, it's kind of like you will be evaluating that, that predicate, right? So it would be like some predicate true, right and if, since this is a function that's returning the left side, then you know, like, after that you could, you could iterate over, over this list, and then like these, these. You could like escape the escape these properties, like, for example, if you had defined this and you made, you make your like function that goes through it, like recursive, then you know, like it could be also something like, like, for example, if you had had a swan, you know, like, would be white, and then you may be, like, an instantiation of an object, like, like, some Swan, one It could have, has property that it's that it has all the properties of the Swan, and then, and then evaluating those, those properties of your objects. I don't think this will make sense, but I'm just writing like, adjust down, right? You could check out whether the predicate would be true of of that particular object, and then would pick the left side every single time, and then it would sort of directly go, like, go, go deeper in there. So then I thought it that might be like a kind of, perhaps expressive, or like easy way to to nest those those concepts and make a difference, like, a difference between either describing and a property without necessarily requiring it to reference something or or just referencing the thing itself. But yeah, then, obviously, in MeTTa, you sort of already have that, that property that will just filter, reduce, like you could then you, you could essentially just write it just like this, without,

without any

without any further like, without having to have defined this, if you hadn't

looks, I'm using it's a sort of opposite direction To what Douglas did with turn and functions, interrelations here doing the opposite, logic and relations into functions, and we always have this dilemma whether to Use a functional representation or some Structural representation in MeTTa, there, mm,

All,

Anything else anyone wishes to talk about today.

I found that interesting.

Okay, It doesn't sound like it.

In that case, see you next time, I guess, sure speak. Okay,

okay, thanks,

thanks all. Have a have a great weekend.

You too.

Thank you. Bye.

How accurate was this transcription?

00:0030:47

AI Chat

Outline

Comments