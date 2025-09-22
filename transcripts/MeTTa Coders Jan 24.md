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

![](https://profile.otter.ai/AKMRNBM5G52I6ZL2/AKMRNBM5G52I5LUB.png)Iain Wentworth

Jan 24 at 7:31 am

42 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io

Summary

Transcript

## Keywords

MeTTa, memory efficiency, atom space, type inference, minimal MeTTa, type checking, non-determinism, superposition, backward chainer, type constructor, promise, union type, evaluation, grounded functions, pragma.

## Speakers

Nil (42%), Vitaly (34%), Adam (18%), Speaker 1 (4%), Speaker 2 (1%), Speaker 3 (<1%)

Hello, hello, Hello, Hello,

it looks Like Matt has left. Maybe, maybe we should start before we are waiting for his for his return. I'll find the word yeah for his return, right? I have stuff to show my side, but I'd like to give the priority to others. So if anybody has something, please go ahead. I

Oh, I can say a few words about my recent work, second Chrome experience, both It seems I've seen so I was working on a new version of in memory atom space. It should be more compact in the presentation of that I'm spacing my algorithm current spaces, and hopefully it should be also more performant. I just finished this implementation. I'm trying to test it and to test it, I also going to introduce some stream meta file reading to read really big meta files without Holding it, sent in memory in advance because previous See, simple log in was like big file, memory, first cell, parse it. Now it will be parsed from the disk, and should help. Maybe it will help to buy atom space team, for example, towards their files into hybrid experimental I'm going to check it of some by atom space File Examples big enough to see the difference.

So

update on the hyper experimental to progress.

Okay, so you're saying that it should be more memory efficient.

Yeah, it should be more memory efficient. And probably it should be faster in COVID, because previous version was like previous version. Does unification couple of times to ensure the extracted atom is unified with query like it was very inefficient but simple solution, now it will be unified only once just well queries processed inside the atom Space Tree, yeah, it should be more, much more compact, because, I mean for symbolic, for other places, when where symbols, where we should, which contains, which contain many similar symbols, because it's this, it use hash to to keep symbols inside the memory. So not hash, but IDs like, like yes and so, yeah, you should compress. It should be much more compulsory use. One,

nice,

okay, so more people have joined. So I'm, going to reiterate the question. Has anybody anything to show or to ask?

Got maybe a small question? Yeah, sure. So share my screen. Think it's a question that I've that we discussed sometime before, but

it's about typing, so I think I'm just overlooking something. Just

so, yeah, so let's say I'm defining type constructor, so I was just trying to implement something like this. Like doesn't really matter what the name is. But I thought, well, let's say I define two functions, async and await that. So let's say if I have a function from A to B called F, and I want to know what the what the type is of async, F, right? Let's call that g. Then I've just said that code on T is just to get the type. Then you can see down here that,

yeah,

that it types correctly, like a function from A to promise B. And then I thought, well, what if I want to define a weight such that, for example, it could take a function that goes from T to a promise U, and then probably it should return a new function that goes from T to either. I don't know if this symbol is correct, either U or a promise of U, depending on some kind of implementation. So I kind of expected that if I was looking at the type of this expression await G here, that it would also infer that these D here, for example, should be the same as A. But that's still that's not inferred automatically. So I was a bit confused by that, because it does recognize that it's of the shape the promise you right. Otherwise it could not, could not infer this expression. But then it doesn't really seem to realize that, that it could already probably have inferred that this should be a and this should be B. Does that make any

sense? Okay. Sebastian, I probably didn't get it completely, but I would like to note that the symbols that you used, I mean, no con and what what is great. So it should not. I mean it is not supposed to use this in such expression. Could you please repeat Why did you use it here? I mean, I mean the last type is a weight. Weight up is a point eight. So point eight or last, like last nested expression which has a symbol which shouldn't be here, actually, I mean, it is not.

What do you mean with the symbol should not be here? You mean this, this symbol here? Yeah, I

mean, it is not supposed thing, and it should not be handled automatically here. So what did you mean by using

it? I mean, I just, I just want to express something like this, either you or,

okay, actually, the simple way to do this, okay? I'm not sure if here is a simple way. Let me think about it. So because of you is okay, you can try to

you. To

define some parameterized type. I mean, it is not short attention, but it should work actually. So you could wait like, let's define some type, weight return. For example, it is not exactly weight return, right. Let's name it somehow in just some type, okay.

Okay, maybe I will, instead of trying to spell it, I will try to type it out. Check. So, by

the way, I was wondering the last line of your code shouldn't G be between parentheses? That's

what I was thinking, too. But I got a Type error. If I do that,

you get a type error, I don't know, so you're using colon tea. I wasn't aware of that. And I wasn't aware, I wasn't aware of this other symbol that you use for a union.

Yeah, I don't know really how to express it. I want to press a union. But I thought, Well, I mean, probably would be like this, right? But So

if, if one way that I know is that you use non determinism, you say that await. So either, either you redefine a weight to, like, if you were, if you were to unfold the union, you would just define two versions of the type of a weight, right? So you would do that. So that's one way. Maybe you can use superposition inside the tie. I don't know about that. Maybe you can, maybe you cannot. I never try the column T I mean, I'm trying it and it doesn't work on my end. So where like,

just to find a version, just to find it here.

Oh, right, okay, makes sense now. Okay, yeah, so you won't type, you know, I don't think there is a type union built in.

But this regarding the union, wouldn't you expect, still the case to be that this expression should infer that, instead of dollar sign, D, I stick to 208, it should be a inferred here, like if I if I do this before it gave me, Oh, that's interesting. Okay, yeah, making this so changing this expression, it actually solves this problem,

right? Yes, probably the type checker had trouble with the with the union type that you were

trying to use. So, but it's then, it's kind of interesting that it does not really throw type error here, because, you mean, it's still, it No, it's it does no, because now you're not putting in a function from T to promise you right, because it's like, because that's actually that G is

the type. But Right, right. But so okay, I'm trying to right. So you define g here, but you never define you never gave a type signature to G. So I think I would assume that the type checker relies on that, yeah,

because I think in this case, you wouldn't really want to practically be having to redefine the type if you're just defining G in terms of another, right?

Yeah. Yeah. True. True. I agree. I would say that my backward chainer, if you use it as a type checker, I suspect will be able to to deal with that. It will, it will infer the missing type definitions on the way. Yeah.

Okay, all right, thanks. That's shit.

I actually typed a couple of solutions, like what new proposed and what I suggested, so you can try to I'm not sure about second. I mean, my solution may may not work, but what's new suggests should look using the type, non determinism. Yeah, and New Year, commit NGO as so you cannot use the position site types, unfortunately at the moment, yeah, it, it was a point to like to be implement type checking using MeTTa interpreter itself, and then it could do this. And also, I think at some point it will be done, but not yet.

Yeah, so this is,

I see you already, yeah, so this also, this is also a way, I suppose, so the man, you could just get either type B here, but then it would be equivalent to this.

Yeah, again, I, I think, I'm not 100% sure, actually, whether my background can can deal with that. I

Great.

Yeah, well, I'm blanking. I just can't, I can't think about this. We would do it. Have to try just I

Bill, what are some of the things your back with China can do?

Yeah, so Well, actually, I would have something to show as not demonstrating type checking or type inference, but something else. I wanted to show that for another purpose, but I could also show how, how type checking a type inference works, by the way, before I just wanted to just do something a bit weird. Just let me just share my screen for a second. I

so

if I if I ask the type of collapse,

I get

atom to atom, but then it is in contradiction with how collapse of say, foo 42 is evaluated because it actually evaluates foo 42 which is in contradiction with the type atom, I think,

is that I think what it would be supposed to be, maybe undefined and defined, or something like that, as opposed to atom, atom,

then, yeah, just go on. So strange. I mean, I need to think I cannot get, I mean, strangely, but I can't understand why the result

is because collapse is a built in and so maybe the evaluation is somewhat more freely decoupled from the type definition, since the rest interpreters, is doing the work and so

well. So algorithm is that it knows that collapse is a function. It knows it is argument, and it's like tries to apply function to argument and understand the type of the argument, but yeah, it wouldn't be BA is a double, please. I don't see why. It can be the tuple. And also it should not be, yeah, it should be, probably just atom. Okay, you're talking

about the you talk about the first argument, first atom, or the second one, because I've been working in the transpiler on metallogue, and one of the things that we do there is an atom means don't evaluate foo right away. We're going to be evaluating it inside the function. And so if you had undefined for the first undefined for the input, then that would break that so that I can see an argument for the first one for the return type. I can see that my being, being undefined, being sensible, but the input atom does seem to make sense. I

Yeah, actually, probably I was confused, is it a MeTTa lockout experience?

Sorry. I missed that.

Well, it was a question to you, all right, whether this output is produced by MeTTa walk or

something. Oh, good. Good question. Let's see, so produced by hyper and experimental, but let me check, Yeah, same thing with metal. Okay, maybe it makes sense. Maybe it just, it's just counter intuitive, but maybe not that much, because it's true that collapse takes a superposition. So and it is true that food 42 ultimately, is a superposition of a and b, so maybe it's perfectly fine. Maybe I'm just trying to find problems where there is no problem. I

but, well, yeah, at least, okay, yeah, it's anyway. It's not saying not string, because co ops doesn't guarantee that principle being that order. I mean, it can be a and b, or be in B and A, so it's not determined, and it looks like some order here. So let's just produce some order.

Yeah, the return, the return type, I can see not being an atom, because that's just, that's just effectively an expression. No, not. Yeah. Expression of the small e, not necessarily the middle or capital E, but yeah, MeTTa capital E, but yeah.

Anyway, I mean collapse behaves as we expect. So I guess that's the most important. So if you want me to I can show you either what the backward channel how the backward channel can be used for type inference and type checking. But before that, I'd like to ask if anybody has something else to to ask or to show. Because I don't want to take. I want to take. I mean, I don't want the space I take to be at the detriment of new comers, we do have Questions and Need help you.

I i or so

initially I just wanted to show this experiment of of trying to do some kind of a generating program, MeTTa programs, in MeTTa and and the problems that I'm facing, which is that I have to be careful with. I mean, I basically, I want a way to express that sort of MeTTa expression without spontaneously reducing it. So I know I can use quote. I can do that. And it's a little bit cumbersome because I don't know exactly. I mean, I'm, I am. It's probably premature for me to show this thing, because I should try harder to use quotes before i i Yeah, I expose that issue, but, but, and I haven't so but nonetheless, even if I were to use quote, There is one problem with variables, which is That variables inside a quote are going to be unified, and I don't necessarily want to do that. And so what I did, what I've been doing traditionally, is I am not using the MeTTa grounded functions or anything that's been previously defined. So for instance, if I want to use bool, well i i write rule, but in Unicode, with Unicode characters that MeTTa is not going to confuse the two and and if I want variables, I use deep Brian indices. So I do that. And when

I do that, I'm able, for instance, here, to use again my backward channel to evolve programs. So I can even, by, if I go straight to the end, like I can even express, I can express the query of evolving programs that are fit given a sufficiently given a certain degree of fitness, in that way. So that's my query. I want to evolve feed programs. I read this thing, this is a sigma type, and what it tells is, well, that would be the type of the expression I'm trying to evolve is just a Boolean expression and and then it needs to have this constraint, which is, it has to be fit. But I don't want to say how much it has to be fit, so I'm leaving this parameter as a whole. And so, so I it works. I can run this thing and, and I'm getting programs,

Transcript limit reached

This conversation was created with an account that has a 30-minute transcription limit. Ask the owner to upgrade their plan to allow access to the full transcript.

How accurate was this transcription?

00:0042:37

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5