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

![](https://profile.otter.ai/AEKJXYMK43CXNS2X/AEKJXYMK43CXMPDU)Douglas Miles

Aug 23, 2024 at 7:32 am

1 hr 7 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

meta, tree, calculus, unification, variables, expressions, lambda calculus, creating, issue, function, combinator, evaluate, reduction, good, guards, fork, context, result, delta, interesting

## Speakers

Adam (49%), Speaker 1 (23%), Alexey (12%), Vitaly (9%), Speaker 2 (3%), Speaker 3 (2%), Speaker 4 (1%), Speaker 5 (<1%), Matthew (<1%)

Hi again.

Hello.

Morning I

so we might as well get started, I guess. So

anyone like to start off? I

sure

I have something fun. It's only something small, but

let me see if I can share my screen.

It's one of those things that I think matter is really good for. So as always,

I assume Nobody here is familiar with the tree calculus. I will also link that I

familiar,

so I linked it in chats. The idea is that

let me share my screen.

I'm sorry. I'm so slow. Today I've been traveling for 26 hours or something, so

short term. So all right, here

there is a tree. And it's not just any tree, it's a tree with just Can

you see my screen? I do.

So it's a special kind of tree. It's a natural tree, which means that it only has one kind of elements. It doesn't have values, and so the leaves of this are, they're of the same type as the branches or as a single links, and this tree is noted with Delta. Let me see. This doesn't allow me to scroll very fast.

It's download it and

look. You say

that? Well, I don't know if you say value, but say the color of the leaf has to be the same as the one of the branch.

No. So the colors don't don't really matter. What I'm saying is that everything is represented like with one construct, namely this, this delta here, I assume you can share see my screen now, sharing the PDF, not,

not now. Can share your screen? Are you the and now? Yes,

yeah, so, yeah, exactly. So here you see the language, right? So if you have application and you have delta, and so if you start with it's trees all the way down. So if you start with something like expression, like this, condition, small tree for then, like the word small, again, that's a tree of S M, a l, l, and each of those s m, a l, l, those are then binary encoders. I'm not sure if they give us an example here, but in any way. So you can go all the way down and the this is, well, binary encoding. Also can do that. What's special about this? What's special about this is that this comes with a way to evaluate it, so it's both data and a way to evaluate it in one so here you can see the trees for ants or and I believe you also have some trees up here with which represent like true and false. And so while these are data, you also have a canonical way to evaluating them,

and it has the same expressive power as the SF calculus, which the SF calculus, it's you can think about it as lambda calculus, but with reflection and the evaluation laws are very simple. Oh yeah, yeah, here you see, like natural numbers. You can just see as like this right tree in the piano encoding. You can, of course, have more interesting codings. And then everything can compile, compile down to these things. And then k i are also, are also compiled down to delta. And then this, this is your utility for the reflection. So you can query. You can have a certain results, if there are no children, if it's a leaf, right, another function, if it's single link, and another function still, if it has two descendants,

all right, let's go to the meta codes.

So I Yeah, okay.

So first of all, this is the representation the power notation they introduce. It's very simple. It's like the M is applied to k times to n, which is a recursive, recursive function here, and this is the base case. And then the natural numbers. So this is the right bracket. It's three. And then the natural numbers can be translated by just the Delta repeated however many that number is times over, delta as a as a right side,

yes. The

exponent is like, what an repeat? An iterator?

Yeah, yeah, exactly. It's like, repeat, repeat x times or k times

right repeat K application, right? Yeah,

so if you think about the successor and zero, then, like, this is a generalized form of that where you have this is your successor, or M is your successor and M is your zero, and then this is how many times you apply the successor, right? So, and in this case, your successor and zero are the same thing.

Interesting, yes.

And so the reduction rules are also very like there are three reduction rules. They are straightforward but somewhat mechanical, like they are not super intuitive, at least not to me. Maybe if you live and breathe trees, then these are somewhat intuitive. What is cool about them, though, is that we can just well express them in meta and then from the for the rest of the documents, like programs will, like the three calculus will evaluate whenever we write the expressions. Yeah,

however you do have to, you can only evaluate fully grounded expression. They have variables. I suspect this is going to lead to infinite recursions.

I don't think this leads to any infinite recursions. The rewrites are really nice in that way.

So if you try, you

like Y Combinator, of course, like this? Yeah, no,

no, no. Not because the calculus itself is creating, not because the tree calculus is creating an infinite recursion, but because meta is meta is going to do that. But I see in your test line, 1617, and so on. You're never using variables. Well, you're using symbols,

oh yeah, using Yeah, that's

right. All I'm saying is that if you replace, if you introduce some meta variables inside this, you're probably going to hit some infinite recursions.

Yeah, I didn't think about that. I just intuitively, intuitively used values there or symbols there, yeah. Okay, so these are the reduction rules like you may be familiar with the SKA calculus. Well, you definitely are known, but other people here, so K translates to Delta, Delta, I translate to this thing. And then D is some other utility that we can special, special, specify,

yeah, as far as remark, because that can be natural. Logic is during complete and variable free. So I'm not sure if we need to introduce very meta variables here.

No like, it

definitely evaluates without like, everything just runs out in these trees. So, like, if you have pure tree calculus, then you don't turn into problems. But I see what's like, hey, we can try and find an example or a mill like you can pull this file just

to be clear. The reason in my case, I was forced, yeah, I was led to have meta variables in a combinatory logic like calculus is because I'm synthesizing expressions. The backward channel is synthesizing expressions, and as it synthesizes expressions. In some expressions, they have holes. So the meta variables, they are not used as variables of the calculus. They are just used as holes. Right for their existence as holes, they do get, you know, the reduction gets tracked into infinite recursions. Interesting that is that,

because the because of some things that are like, is this like a unification recurse check or, or, what is the intuition for it?

So it hits infinite recursion. Because down the line, I mean, we would have to look carefully at the your reduction rules, but, but I'm sure we would find some. Oh yeah, I actually saw one. So if you scroll up, scroll up a little bit, I think line eight you got, like, right here you've got Y, Z, X, Z, and that one brings potential for infinite recursion, because if the Y is a whole and it's a meta variable, then Okay, well, all right, this thing might not because, well, the way, but it's

kind of hard to discuss on the call. Maybe you can. What you can do is you can, like, just pull this file, yeah, and replace some things with meta variables, and then we can figure out, because that's an important use case, right? Be able to have holes in your program, so definitely need to,

yeah, so it might not be a problem for your experiment, but it was a problem from my experiments as I'm synthesizing programs with holes, yeah, sure,

I'm let me like finish this. The I'm following the book closely. I haven't put a lot of time into it yet, but we can see that well, if you say, what's a natural number five representation in natural trees, it's this thing that's pretty nice, the K Combinator, as we all know and love. If you give it two arguments, it gives you the left one identity gives you just a thing back, and then the s, s combinator on

x, y z, gives you the x, z, y, z, so it uses Z for both, for both functions, kind of like the s, as is branching, D is also some kind of branching, yeah. And then so interestingly, we can impurely trees. We can define true, false and or implies, and we can and the logical works out so and true false equals a tree for false. And then the last example that's in here is the reflection. So the query operator is kind of complex. But then from the query operator, we can define like is leaf, is stem and is fork, which is like the the nullary, unary and binary operators, and then we can feed the isleaf tree, this tree or these trees, and we can see it returns the true tree, or is leaf and like the core, like, basically this correctly classifies it. This is very, very fascinating to me, because it's it just trees. It's like there is no grounded, like true is not grounded here, like nothing is is a function. It's just the reduction rules on the trees themselves. So please, you can pull it from here.

It's very interesting. Could you provide an intuition for line 35 definition of very mysterious. This

is very mysterious, right? Let me actually share the share the book briefly again, because it's, I've also stared at it a bit like, what's like? It's so it seems so complex. And the reason it's, it is so complex is because it was derived from just solving the equations. So we wanted these equations to be true, or specifically these right, and so what they did in the book was they they just algebraically manipulated the expression until they had a definition that gave where all these things were true. So this is like a system of equations on the tree calculus, and that's why it's it's a complex formula. This is the, here you can see the the formula drawn out within the parameters is one, is two and a zero, and then the is leaf, is stem and is fork. Those are just which they have specific instantiations of this, namely K, I or K, and okay,

and the the intuition here, behind these kind of anonymous looking trees, is that it supports a concept called tagging, so you can Where is it's sorry for all the scrolling. I know it's annoying on video,

I would like to make a quick remark while I browsing, I see the immediate possible application of this to algorithmic chemistry in which Ben is interested, it would be nice to apply some sort of genetic program and evolution stuff to it. The only issue is, of course, computational speed, which if, but it's pretty simple. And if it can be compiled in one way or another, maybe it will be fast enough or with use of Mork or whatever. So yeah, it's quite fun.

Yeah, yeah, definitely. I think the main thing to take away from this is perhaps not the precise calculus, because the precise calculus is like, so minimal that, indeed, yeah, that there is not enough cases, or enough there to be really efficient. This is how minimal it is. Like the string small is just represented as, like the tree representing the letters, S, M, a, l, l, which has the binary like the ASCII code expanded into it, so, But you do have reduction rules over it.

So

yeah, that helps somewhat. In any case, the ideas in here are very interesting, though, the for a combinator calculus supporting a reflection like it kind of reminds me of, like the combinator row stuff, which, like Greg always also suggests that's good for algorithmic chemistry. And in any case, we can play around with it, with it. So the I was going to say the about the tagging, the tagging allows you to have branches in the tree that are not evaluated, or that that are kind of like noise for the or not noise but are ignored in evaluation. So you can have without quoting or unquoting parts of the tree that's are evaluated by default and parts that are just data. And it's very easy to manipulate the tree in ways to extract the data from from it, or to extract and then, like, reduce it as code, etc. So all these things that are normally on top, like quoting you, quoting is normally something you do on top of the language, and this is really

or inside the language, and this is can just be built on top of this. Even programs like size, like what is the size of program? Of the program in like a tree, in a piano encoder tree, this completely compiles them to the the delta. So you can see here the program size which has, like a Y Combinator, which recursively checks like is stem and then adds exercises together.

Yeah, I recall we had experiments with Sergei Donovan applying evolution of combinatorial logic expressions to sort of universal induction. And it was fun, but there was, of course, complexity wall in terms of expression lengths, they grew quite fast, and maybe with this representation, which seems quite powerful in terms of representing meta stuff, like coaching programs and so on, it would be possible to go further in this direction, as sounds quite, quite cool. Thanks. Thank you.

Yeah, the reflectiveness is yes, kind of just do not understand it, that that's quite that looks magical. Yeah,

that's amazing. I could have been able to look at that book. Thank you. I

Well, if nobody else has a question, I've got one. I'm working on a sealed term and the PROLOG implementation. And if anybody has particularly good examples, please send them to me. I'm on matter most help my would help, my testing, the sealed, yeah,

I think I have or let me Yeah, try and share this

bear with me.

I just had some coffee. So should be fine, but I am operating on sleep. So formal meta. Formal meta was a a project I did to well formalize some of the meta semantics. And while it wasn't it's functional. Can actually run things with its they didn't capture everything we wanted from meta. This capture some part. Let's see

here. I Huh, here.

Okay, so let's take a look. What do we have here? Some lists, some stack operations, some lambda named after nil. Oh, yeah. Vitaly had a reduction question so it does, like people have thrown different problems at it, and it did correctly do that. This was the Socrates test, all right, yeah, and here you have the unification test. So this is where I want to get. So to do the frog unification, the backward chaining, we had to revise the rules a little bit specifically you see here, execute with context. And depending on what that context is, you get varying levels of power of the unification. If the context is global, then you got like kind of Prolog style located variables. And if the context is none, then you got, like the lambda calculus, local style, substitution. And I believe this is where my ignorance is gonna come up. I believe there is a fork of this thing. How do I go to forks from GitHub? No, I don't want to fork my own copy. Want to see the forks. Any input from the audience?

How do I see the folks?

I think if you start to fork your own copy, then it actually gives you can get a list of existing forks that's better than that one. But, yeah, I think you can then go, that's the one you want,

right? So I will,

yeah, set trees for, I believe one of these, yeah, so this is also five commits ahead. Let's see sealed,

right? So

I believe in the seals, except for cleaning up my codes a little bit, and it seems like adding uglier code. Yeah, so it seems like what they have done here is generates, like unforgeable names in to create, like a fresh context which the original example liked, and I hope that there are also some examples that they added to test that functionality. Yeah, so sealed tests do? So you will probably have to decode it on your own. I believe there is, there is pretty printing, Oh, yeah. And it also has an execute print, so you can also follow the traces. I will link this to you. Thanks. And then hopefully that that's a lights a little bit, or that elaborates a little bit. I don't know how many examples there are. I hope there is more than one. But if not like what one is better, one is better than zero. I guess there's also a threats, I think, with Vitaly Bogdanov on the on the hypern experimental

which dives into lambda calculus and how lambda calculus can be implemented on top of sealed. So, yeah, I shared this in the chats here. Great. Can also share, yeah, if you let me know if you have it, and also, I will also share it on mapping list.

Thanks.

A I believe if you ping Greg about it, he won't be mad. And you can like he you can can ask, you can poke him with questions. And that's the dolly linked the the lambda the seals, lambda calculus example.

Great. Thank you. There you go.

Yeah, I've got something, something very small, just a note that for anyone using metallogue, there's been a recent update which has included a new dependency with metallogue now depends on the liberta package. So if you've got, if you're installing this from scratch, it'll be fine, but if you're up, if you know, if you do an update of the repo, things might break. There's a troubleshooting section on the homepage. If not, then contact me or Doug and we will get you sorted out. So just there's a new improvements have created a new dependency, which may break things. For some people,

right? If you haven't already, could you update the Docker file so that if someone builds a Docker well yet, it includes that added dependency? That's

a very good point. Thank You. I'll look into that. I

I just want to mention that's going to be great. So for those who, for those who haven't seen on the hyper arm channels, I thread about the curry programming language, and I'm, I'm going through the tutorial these days, and I'm finding Things that could be interesting to Barrow, from it to meta and, and I think, well, in particular, Alexa, in detail, you may want to to go through that thread. Yeah, yeah, that's, that's, that's all I wanted to say. And I'm and I'm going to add as as I go, I'm going to have more and more stuff, but there's already plenty.

Yeah, the the, I believe Doug actually brought up curry to be two years ago, something like that. Yeah, and back then I briefly played around with it. And I feel like for the as far as functional logic programming languages go, which there aren't super many of like, I believe there are like five that have some decent community. It's quite good. I talked to Simon Peyton Jones about why he created first, and it's not just because, because they pay good money at Epic Games. So there are some inelegancies when going to the level of of functional style, that's that career has done. So there is like a whole trade off of, how far do you follow back changes, which becomes super relevant as soon as you have side effects. And then Monets and side effects are kind of funky, and so that's where I believe they run into some into some trouble. So as far as curry and meta goes, I feel like one of the there are two really beautiful aspects of meta that are not in Korea. One is the clickability, and the other is the massive data. So massive data in in curious is a no go. That's not what the language is optimized for. That's not what you should do with it, but you can solve, like, pretty, pretty hard problems with it nonetheless. And then the clickability is the part of this, of the story that's that's also very important, and that has been somewhat ignored in evaluating programming language, like, hey, we have this whole backing store here, right? Like, if they live completely separate, then you cannot expect the evaluation over, over this large store to be efficient. Like, databases are very complex pieces of software with planners and execution engines that tailor specifically towards the the algebra that's that supports it on that. So, yeah, some some thoughts on curry.

Actually understand the first, the first thing you say about data, yeah, I just couldn't understand the words that were before data inside didn't get it.

Yeah, I'm not sure what specifically you're referring to, but you say

there are two things in meta that are better the data story exists. They are in meta and they are not in curry, yeah,

the store of data is, is the big one? Yeah, pluggability was the other

one. As you say, the storage, and I'm still doing,

yeah, the store or the database aspect,

right, right. Okay, okay, I see,

yeah, yeah. I, I agree, and I it did cross my mind as well, yeah. But so for the things, I mean, there's one thing that's crossing my mind that thing is nice is guards, or they call, they call that conditions, but I mean, it's cards in, you know, standard functional programming lingo, it's called guards. And the way I was thinking is that, I mean, in a functional program, you may see a guard as just being sugar syntax for a conditional, but in the context of meta, it could actually be more than that, because a conditional is Inside the body of a program. So by the time you you access to that body, you have triggered a reduction while a guard is before the body, and it's guarding whether you are going to trigger the reduction to begin with. And so the difference, like, since meta supports non determinism and, say, partial function definitions and so on, it really make. It really makes a difference between a function that hasn't changed at all and a function that has already been substituted by its body and well, maybe some stuff have already happened inside the body. And I was thinking, the reason this is of interest to me is because the backward chainer I would want the backward channel to trigger function execution, but I don't want these functions to be triggered at any moment. They do have conditions, and so these guards could be a way for me too. Yeah, that's

fair. Greg and I actually discussed this very point in Seattle a couple of days ago where we this comes down to, or at least one way to frame it is that it comes down to, if you're doing zero to order, or first order or second order unification. So are you, are you evaluating functions in your unification context, or are you evaluating them in a new context? And the Garth is, is like the creating, like a separate, a separate context for for the evaluation to happen into. And the good thing is that we were able to at least, at least syntactically and on a high level, unify the meta calculus that was presented with higher order unification. Of course, computationally, they are quite different. So even though they can, at a high level, live in the same place as as you well know, there's a big difference between like lining up multiple functions to be unified together, or their results to be unified together, versus a like calling a function and first and then using those results and a unification

Yeah. I'm also thinking about guars from time to time. The question is, how, exactly on what level to introduce them and who will do the actual work. As one way is to introduce guards into better matching metal language, or unification meta language, or another place where guards can be introduced is in meta interpret, implemented in minimal meta. Maybe there are other ways, like implementing words in DSL in meta itself. So I wonder if there are some specific ideas regarding implementation.

I think it's really good to bring a minimal meta, because minimal meta has an explicit chain operation for for lifting the unification. Yeah,

I actually you, I saw your comment about guards, probably today, you also try to look at the issue. And in fact, I don't fully understand what doesn't work at the moment. I mean, I spent now on this, but you fully understand code and how it works and why doesn't work that you expected. And also, probably by this reason, not sure why God helps. And in fact, twice understand what I mean from from the discussion and that you want to use guard to, okay, somehow change variation order, something like this. Oh, maybe, maybe I can ask some additional question. Initially, we can discuss first,

yeah, I wish the example was a little bit slimmer, but I just couldn't say, couldn't create an example that was smaller than the one I providing. The issue without being somewhat like kind of meaning. I mean, meaningless, yeah, meaningless in terms of the utility of it. So, I mean, so, I mean, the what's provided there's

right there are instructions provided to reproduce the problem, but, but, of course, one needs to be convinced that it is a problem to begin with. Not sure. How can we make that simpler?

So I believe so. Douglas amante, I just want to say that I looked at it, and I'm going to

look at it first as well. Okay, so, but yeah, so, just to put you on on the perhaps the right track. So the idea is really, and that's really what's in this example, we have a reasoning taking place, and there are some theorems which are very easy to prove if you delegate the trust to an external function. And so the idea is, okay, so how do I prove that two plus two equals four? Either I can create an inference tree that is manipulating natural numbers and moving them around until I find that two plus two equals four, or I can just call plus on four on two and two, see if the result is four, and if, if the result is four, then I say, Well, okay, that's good enough of a proof that two plus two equals four. And so that is what this the test that is provided in the issue is attempting to emulate. And so there is a in the base case is the second one. The name of the proof is CPU, and that's just the idea of that. Well, it's not two plus two, but it's something that invokes a meta function, and and basically and so the idea is that in order to know that two plus two equals four, you need to guarantee that the arguments of plus are fully granted if you do variable plus two, well, the plus is not going to apply here and so, so you need a way to pause to say, Well, don't run variable plus two because it's not going to need to to a result that this rule is going to be able to deal with. You know that that's really the idea. And so the question is, how do you do this, pausing without starting a reduction that then while you come backtrack and in the same time you got the wrong result. So the entire reasoning process is going to a dead end while, in fact, it could have, if it had taken the turn just a little bit later, it would have led to a correct proof tree.

Yeah. Okay, thanks explanation is so much clear now I believe, yeah, I will maybe, I mean, one of the things I would like to, like to see is how it really introduces what called skilled to the expected, or maybe some unexpected, which leads to the similar result.

I'm sorry, Vitaly, I couldn't understand. The audio is not very good. Okay,

okay. I mean, think thanks to explanation, I look at the execution trace and understand whether there is some unexpected behavior also. Also low level,

yeah, by the way, there is a so in the additional context section, all the thing about without minimal meta is, well, you know, it's irrelevant. It's no longer, no longer applies. I probably should remove this thing. And maybe, in fact, I should probably retest this thing with new mana and see if it behaves as it used to behave. Because, yeah,

well, I ran it today so they can say that, okay, so actually behaves as you explained. Okay, one, one strange thing is a difference between pure rust interpreter and Python interpreter probably because arithmetics is implemented by different in Python interpreter, or just when you type meta installing the hyper experiment, or it runs Python interpreter. So in Python interpreter, it returns empty result. As you said, in the Rust interpreter, it's actually claims that less operator has a variable as an argument and cannot be

cannot be used.

So you mean it raises an error?

Yeah,

right, okay.

Well, by the way, when I was preparing an example for the workshop with enumerating different expressions and compiling them for sort of curve fitting task, I also encountered issues, I believe, which Neil encountered for multiple times already with variable renaming and so on. So I wonder if we can systematize all these issues and think what we can do, because, indeed there can be very convenient to construct expressions with meta variables, for example, for sending them for compilation, but we have no guarantees that this variables will remain as they are and will not be converted To variables with some suffixes and so do you think I should raise an issue on this?

I think so, yeah, we also had some issue about differences in behavior of those new interpreter. Maybe we can just raise race. I'm not sure if it is some incompatibility between previous and new version, or it is like just just behavior, which was also

I also encountered a problem with specifying strings, grounded strings which contain double quotes. So I suppose that backslash for escaping sequences will work, and it kind of works. But instead of creating a grounded atom with the corresponding string, the parser creates a symbol atom. I wonder if it is an intended behavior or not. So once again, should I arise an issue regarding this?

Well, I think raising the issue, I mean, it's difficult to understand, but without specific

I remember raising an issue about escaping characters, but I think it was actually fixed, but maybe, maybe it hasn't been completely fixed.

Yes, this is surprising. So indeed, I also used escaping sequences in different cases, and I thought it should work, but it didn't work. For some reason I

yeah, I think I found the issue

pasted here.

It's been closed so

that, I mean,

maybe it's a different issue than the issue you did encounter, but it looks related as well.

Yeah, so something like new strings work, but double quotes don't work because if you just put a double quotes inside single quote inside the strings, then they are treated by regular expressions as determination of things. But for some reason, when we put them into escape sequences, it seems that something goes wrong. So yeah, the issue you pointed to seems to be solved, but it doesn't cover this specific case when I want to put a double quotes inside grounded strings,

Right? Maybe the regular expression is not even right should be correct in

maybe more.

Yeah, we see, just read, we should Post in the example. So build, and

I have to jump off. Thanks everyone.

Thank you. Adam, that was very

Thank you. Interesting.

Loving that tree calculus. I think Alexa's point about the algorithmic chemistry is Spot on.

Okay, great call, Bye, bye, Everyone,

Bye, Bye.

How accurate was this transcription?

0:00:001:07:18

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5