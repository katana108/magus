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

Sep 5 at 8:34 am

30 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa syntax, grammar, transpiling, hyper on experimental, core elements, computational structures, standard library, code examples, useful code, different implementations, formalizing syntax, minimal MeTTa, grounded atoms, extensions, syntax definition.

## Speakers

Alexey (46%), Matthew (33%), Patrick (21%), Matthew (<1%)

I'm 100 any anything we wish to talk about Today, any ideas, Patrick, or anyone else.

I don't have much regarding MeTTa itself, maybe in terms of discussing, like what Greg might have meant when he said, we don't have the grammar of matter. I wonder if we should come up with like a buck who's now a form that defends the grammar for Greg. Since he since he mentioned, one issue he faces is that that matter is not that The grammar is not defend doesn't really human.

Yeah, that was an odd

statement, I guess,

or not.

I guess I mentioned it because maybe in metal, he wants to capture the aspects look the most important aspect of the matter, right?

Well, Patrick, as I tried to explain, it actually depends on the goal, because there is a pretty simple structure which can be expressed as a grammar in terms of atoms, like atom is as a symbol, grounded atom or expression, and expressions tuples of other atoms, then yes, we have some additional both syntactic and conceptual elements, like Syntactic Elements comments and inline execution, which is actually so not too fundamental. And the question is, for what reason do we want this syntax? Because initially it's supposed that syntax is can be different in very initial my implementation of MeTTa, it was a sort of natural transformation between different spaces, like a textual space, Atom space, and you could have different textual spaces with different syntax. So what's the practical issue we have? Do we want different compilers and interpreters to support the same syntax? Well, it's one story. If you want some fundamental syntax of MeTTa, then I would say that. Well, first of all, as I already said, it's not fundamental. It was supposed to be reviewed, but due to natural, historical reasons, we have what we have and but in any case, MeTTa syntax is extendable, and what do we have for numbers, for strings, for some other grounded atoms. These are extensions of MeTTa syntax, and any library can introduce its own extensions. And the next question is, do we consider a standard library to be a very standard across all different implementations. It doesn't seem the case, because more will not support everything which is in hyper on experimental. And maybe the same is true for MeTTa IL and vice versa. And backends are different, and that's why some grounded elements are also different, like hyper on experimental has minimal met core, more has or will have Amen to core, and they have different basic operations, and they will not be the same For sure. And if we are talking about formalizing hyper on experimental MeTTa syntax, then this will be one story. We will say that we have a bunch of layers of this syntax, and we can make some more or less standard statements about the syntax from the practice, from the practice of usage. But it will definitely be different in more core MeTTa IL, and it's not avoidable, I believe. So the very, very basic syntax, which is maybe not the same in terms of syntax itself, but in terms of internal structure of atoms, it kind of the same. It can be separated, like equalities typing, but, well, I'm not sure if you should add strings or numbers. Maybe they're kind of standard, but maybe not precisely. Should we standardize them? I'm not fully sure, because they actually are different technically. For example, if we even if we take hyper and experimental, then if we import by ops, then we will have arbitrary integers of arbitrary size. If we don't import pyops, then rust integers are of limited size, and if you want to strictly formalize a syntax, then it will be different, because we will not be able to say that there can be any number of digits in a purely rust grounded integers so well. There is no, indeed one very well defined syntax for multiple reasons, and we can do something. But the question is, what is the goal for this exercise?

From my perspective, what I got from Greg's statement is, the goal is to help him with transpiling it into MeTTa. Il, whatever hyperon experimental is that's, I don't know if that's what you heard.

Patrick, yes, exactly, essentially, also to nail down for him, like, what aspects of matter he should cover in matter, because it to some degree, it seems to go a different path than original matter. Which is how to say which, which might be. I mean, it could be desirable, but, but I personally, of course, would prefer if it would stay closer to their original model. So, so, I guess, I guess there's also the question to what degree or grammar can can help correct, to to to stay closer to to the to the helper on the experimental method, but, but I think what you what you could find more beneficial, is like code examples also, also, from my end, to show some some things, some properties of matter which, which were which we like would like to have or send MeTTa l also, because, because I suspect that it could develop into a quite different language, if, if we, if we don't grant correct to some degree to replicate some of the capabilities of metal, I'm not sure it's just something I noticed that that he might stray off a bit. I

well, it makes things clearer, but still, it's not clear what part of hyper on experimental should be transpiled. And what level of syntax we are talking about.

But in any case, it helps a little so it's not a sort of generalization of different mettas, but it's about hyper and experimental, and the goal is to help with translation. Okay,

so I guess it what I'm hearing from Patrick is identifying the core elements and the core computational structures that were actually using in practice, and those, it would those, if we can identify the ones that which part of H, E is is most useful for us to formalize and then that could be transpiled. Was that what you're getting out with the code snippets?

And exactly?

Well, yeah, this is exactly the question, because in Patrick's attempt to provide Ben F of as she met some very specific elements, like let, if case, and some others which are not actually a part of core MeTTa syntax. This just delete functions. So should we include all study functions in this syntax definition, or some of the most useful of them and so on?

Hmm, I agree, ideally, of course, in MeTTa l some of the more commonly used constructs would also be available at some point, but I agree. I'm not sure if it should be part of the grammar definition in this case, if it's If it's just a function implemented in the standard library.

So do we need to do anything with this syntax definition? I can discuss it with Vitaly, but I still don't understand if what level of details should provide it like with this. Should there be a minimal MeTTa, or we don't want to transpile minimal meta operations, although they are used in MeTTa, also they can be used in hyper and experimental MeTTa. So that's actually the question. So what exactly is needed? I

Hmm,

I guess with MeTTa, as far as I understood, correct dress to capture, try to capture for MeTTa, but, but more recently, from from what he described, it also seems like he might diverge a bit from, from the current hyper and experimental method. Um, so I'm not sure to what degree he aims to be compatible what things you want to change, or whether he's already clear on what things he wants to change, it

would help if he were here.

I'm not sure. And so correctly, did you give him your version of the syntax?

Not yet. I think I mentioned the Ben F in one of the discussion for it, but I did not yet go into Greg

okay, because there are some inconsistencies With how we treat atoms and expressions. For example, I mm, as I wrote, I

so we don't need to do anything at this point. Or should we do something? Well,

Patrick was suggesting supplying Greg with useful code that we're using right.

Useful code has always been available, I believe,

well and so, especially as we start moving towards more implementations of different modules. I think that should be so. For example, the the I mean, they were written in meta morph, but what Patrick and and and Peter and Robert put together for PLN version 0.5 and then we're going to be bringing in that which is pretty much a straight port, a direct port from classic open cog of E can. And we're going to begin wanting to rerun experiments, we ran on classic open cog, and that's what I meant by useful code, that it's not all. It might be there yet, but integrating, for example, I think they're the hyper on experimental code for ECAM and then Moses at some point, with that from from PLN, which is in the Use Cases Patrick Peter and Robert wrote it's all in metamorph and so I think that begins to supply a bigger

purpose of of of code.

I got some code like nil wrote because the code which we wrote is mostly using only a subset of the language, and nil is exploiting the depth system

Exactly,

and it's it's available, but it's all spread out and maybe collating that the supply could help, or at least getting links Ready, because they're all in different repositories, scattered over

GitHub repositories, but they're not all in one location. Some are in true AGI. Others are in hyper on experimental. Some are in Nils private branch.

Becomes an icon lab Dev, Like a lab dev brand,

I mean, does that mean I can identify where the different githubs are and maybe send those over, would that be?

Can Help correcting culture as well for correct? Okay, cool.

Maybe that's, that's what we can do at this point. I mean, as I said, it helps if he were here to respond to that, but I think that as a proactive move,

this is, this is the kind of code that we want to use. We want transpiled. I'm sure it's not going to touch on all of the different use cases that will come up against, but it's a start, at the very least,

I agree. Under the next meeting, I can also ask him what he exactly wants in terms of grammar, because I was not clear myself about what he meant.

I mean Ben after would make sense, but,

or we postpone until we until.

How accurate was this transcription?

00:0030:02

AI Chat

Outline

Comments