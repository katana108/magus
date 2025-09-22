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

Oct 4, 2024 at 7:30 am

1 hr 29 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

lambda function, list manipulation, reduce function, beta reduction, cons atom, empty atom, type definitions, non-determinism, backward chaining, single-sided evaluation, probabilistic programming, pattern matching, variable bindings, meta interpreter, proof abstraction

## Speakers

Speaker 1 (38%), Vitaly (33%), Speaker 2 (18%), Alexey (5%), Speaker 3 (4%), Speaker 4 (2%)

Hello, hello, hello,

so Matt cannot make it today, so yeah, maybe somewhat take his place, although there is not much space to be taken, I mean, the call is usually conducting itself. So

do

Hi, Sebastian, yeah, you have stuff to go over. All right, yes, yeah. Well, I mean, I think you Well, who do we have here? Okay, we have, we have Vitaly. I mean, I'm talking in terms of a meta experts. So I think you can, you can start Sebastian, yeah,

I'll share my screen with you here. Can everybody see it?

Yes, so

yeah. So I wanted to to implement some functions to go to manipulate lists. So here I define my list with the cons and the value and nil. So in this case, I say my vec, because I wanted to see if I can do something with, you know, factors, so list of numbers, if you like. So yeah, here I've just defined a couple of functions that you can that you can use. So for example, I had a band, map, length of a list, reducing it, and that all worked well. So then, and here, this function is at one, is not really at one, but it's like, if you wanted to measure the length, it could be another way to go over it, where maybe you would want to use the reduce function to measure the length of the list. And then one of the problems that I was running into is I wanted to define a lambda function so that I could say, for example, in my

Reduce function, so I can show you, for example, here are, like, maybe a bunch of it will come out, but, and maybe not All of it equally, sense, sensible. But, for example, I if I had some, right? So this is just plus. I can feed that into my reduced operator. So I'll reduce this list with the sum and then accumulating on zero. So basically it will just add up all the different numbers in this list my VEC. So in my case, it ends up being this value, 107 and then I thought, yeah, what if you want to do something like this, where you would define that function that you're that you're putting in that. So this function, it should be,

yeah, a function from two values, your value and your accumulator to to the results. And I thought, yeah, would be it'd be nice if you can define a lambda function like this in the same as you can do, for example, in in in Python. So then I started playing around, but I was not really able to to to implement it. I tried a couple of things, and I think the best attempt that I ended up with was basically this where I said, Okay, well, what are you really doing when, when you are, when you are implementing a lambda function, you are really changing the values within an expression that match the initial, that match a certain a certain variable name or a certain symbol with something else, and then you are evaluating it. So in this case, I just use here the r. So I can, I can show you what this corresponds to. So you, if you, for example, call this R, imagining that to be like this lambda equivalent. It's like, okay, well, if I had my short function where I said, Okay, lambda x, and then I will replace what I apply this like, but I apply this function here with the value three. So basically I would substitute all the instances of X within the expression for three, and then I would want to evaluate it. So I thought, well, maybe one way that I could do it in meta is by constructing something like a list first. So I was able to construct this object by defining this R function, which basically goes over the first part of the expression every time, right, so, and then the head. And so just I've called the head, B here, and the tail, E, and then, yeah, this n is just like the next result. So I thought, Well, if the symbol matches the one that I've defined here, then then I want to substitute it for, for my value y that I've put in here as an argument that I'm that which there are, the argument that I'm calling my function with. And if it's, if it's not the case, I just want to, I just want to feed in the head itself. And then I got so then I thought, and I put it again here, the same symbol that I've used for the cons. And so that I can get get this kind of list, basically evaluating that expression with the value that I wanted would want to put in there. But then I had some trouble collapsing, or, like, reducing this list. So I thought, Well, I mean, then I can call, for example, the reduce on the on that on that list, or like, reduce on that expression that I get with some kind of function, but then I was a bit at a loss what that function should be. So maybe somebody can help me here. If, if, if there is some function that can that, if you apply that to to an expression with a head and a deal in this sort of list construction that it would basically concatenate all the terms into an atom. I think that that would kind of, that would allow me to,

when you say concatenate, you mean, turn this list into a tuple. Yeah,

indeed, yeah. So I mean, I just mean, if I have something like this, right? Yes,

are you? Are you aware of cones? Atom, so cones, I'm typing that in. Are you aware of that construct? No, yes, that's what you're looking for. But with respect to lambda abstraction, well, Italian, Alexey may may correct me, but I think it's coming. A built in is coming pretty soon, okay, but please have Vitaly and Alexey confirm, because I'm I'm not Sure.

Okay, well, yeah, so actually

start. So actually you can write lambda person which gets arguments as a double, but then you cannot, cannot say if you want to write a function which gets most lambda and or another function as an argument, then you probably cannot get you cannot do it with current way the ramp is defined in myth examples, for example. But

you can try to implement it by analyzing, or you cannot I actually you probably cannot even simulate it.

Okay?

What Sebastian did with the with our function r was kind of It looks to me like it was pretty close to emulating beta reduction. The only thing Sebastian is that you don't need to build a list. You can just use cos atom to read. So what you want to do, you want to deconstruct the meta expression and reconstruct it where the variable has been substituted by the argument. And so, yeah, you just, you reconstruct it using const atom and and I think it's, it's going to emulate better reduction. I think, okay,

because it's straight, because if I put here as in my reductor function that I'm putting in here to write as the function of my reduce on the list. So, I mean, I could, I could replace it here directly, is what you're saying. And, yeah, that would, in principle, be equivalent to to this, right? Because, like, for example, if I, if I do this here, like some random expression, and you evaluate it, you can see that you will get something like this, right? Do you see this output right yeah, yeah, see, but when I just put in the

it's odd, like, this goes Adam, it fails.

It says,

Huh, wait, so it's called here comes. Well, why would that be wrong? Is in no, I don't think, Huh,

oh, but maybe it could have something to do With

just maybe like this, probably The same, yeah, no.

Just so I

i actually don't completely understand reduce. Did you show again, the definition of reduced? So

reduce is basically, again, go there to definition. So it is a function that takes a list with where the cons is, D, and the function that takes and some typed value that is like the accumulator, right? It gives you another value of the same type that is mapping T into and then also an initial value. And then that will basically reduce all of that into this type. So

atom expects an expression as a second argument. So you cannot use new which is not an expression but just a symbol you need. You need to use empty paraness to use conceptum on such kind of expression,

yeah, but, but I'm but I'm calling it here, and I'm using the empty list. So this, in this case, this is my initial accumulator value, right? And then,

but after all, you have your list which ends with nil, and you tries to use, you try to use cons atom on new after all,

no, because this is in this case. This is my list. Oh, you mean here, if you saying if I would change this to this, it should work. So then I uh, right? So in this, in this case, my R function will get this list ending in nil. But now, if I change the nil to this empty atom, this is, this is also a unit, right? Yeah, then you're saying that probably that should work if I try this. No.

What is odd is that the air is really showing the the expression. And the expression is cons atom two, and the expression with n, and to me, that looks okay. If you run that thing in stand alone, what do you get? I and I wonder if the bad type is, is has, is having to do with that, or is having to do with the type signature of reduced, if you, if you run calls atom two expression in it works right? So that means that it has to do the bad type is with the color of that expression or something, not the expression itself. And because reduce as a type signature, I wonder if the type checker is not basically finding a type checking error in the way reduce is called or something, and just just speculation or somewhere else.

But

if you remove the type definitions, maybe it's going to work. Actually,

I made a mistake. Now I think, oops, should be like this. Then I

so what is give now? So, okay, this is the output of cons, atom, x, y, so that's expected, right, right? So you're saying, If I you,

is it the key for in one, number one, kind of 72

you just expect

this to work out so

and you should have an atom of the first position expression the Second you have only one argument right now.

Yeah.

Yeah, okay, but okay. But anyway, in any case, this works. So then it is. It's interesting why this would not work, and you're saying this probably because this type definition is not right, but you disable

data aside and it still fails. So it's another problem, apparently,

and now I just seems to reduce to this. But I

uh, yeah, but maybe it just also won't reduce without any type definition or

false? No, it shouldn't be okay.

Yeah, okay, I see what you understand, what you said before, like, say, say, maybe if I change this, even without using the nil. And then here too.

Yeah, I should probably start using this, that this will be like the convention, right? Not nil.

I don't know if it's been, I mean, this is more like the convention of an empty toe pole or empty expression than an empty list, but I guess it's probably not going to be incompatible with Well, I mean, do you have a type definition of of the data? Type, list?

Yeah, so lists, I've just arbitrary right? Just arbitrary Ray, right? I see,

well, you can still use Neil in your list definition. You just need to convert Neil to an empty temple when you want to produce out of this list.

Yeah. Okay. But here should be new, probably because to it to be well tactics, so in line 91 user reduced. Definition should be improved,

but yeah, so, okay, so there's something to okay, but it will be, it will be useful if we had a lambda function because I tried to define the composition right? I thought, if you have a lambda function, that was maybe sort of intuitive way to compose two functions, something like this. But then I did not really get the didn't do not really get the lambda function so, but maybe so let's see if I can implement it in a similar fashion as this.

Yeah. Oh, yeah. Add another question. Or do, or do you have some more thoughts on this matter?

Well, I can share the code with lambdas which written, which is right, as example, meta, yeah, should I just posted the link into the okay, but if you look at them, you see that lambda side defined like there are few different lambdas Definition each for different number of arguments, so, different parity, different lambda. And it was done exactly because the author wanted to to be able to call both lambdas and of the other function as arguments to the higher function. So I believe if you want this, to do this, you can use lambda, universal lambda definition right now, but,

I mean, in any case, I thought it was interesting that in that approach, that I showed that you don't really have the problem so much like you could do that in like you in principle, for any number of arguments, right? If you just iterate over the the head and the tail of the atom, as if it were a list structure, right, like a list of symbols or then, then you match them all. You match them all together, like you could do the same if you had to, for example, of two arity, you could just say, well, then instead of, instead of taking the like, instead of saying lambda x and then some some atom, you could also define it as lambda and then some atom with arbitrary R arity, and then just look, if For all the symbols, and then if they match, just replace it for the same symbol in the variable that you're putting in there.

Yeah, I think the idea works, and I think you can just have a more direct way to implement it, fujiscons, atom, I pasted another example of lambda. It's, it's, well, it's kind of different in the sense that I never use, I did not implement beta reduction, but there's some interesting definitions anyway. For instance, I'm using the brand indices for variables and Yeah, well, that's, that's about all you will probably find useful. But

it's yeah,

the lambda is just used to represent proof abstraction, but that's equivalent to a traditional lambda and lambda calculus in a program, if, if you consider, if you're if you're trying to find programs instead of proofs,

well, yeah, As you said, yes, the idea is you can convert. Actually, I'm afraid I do not get this example completely, but okay, like in general, you can get the example of arguments converted to the top of arguments and pass it to the Rambler function. Yeah, it should be doable. You can try to share the example, like if you have this code of GitHub or something, you can say it, and I will try to look why it doesn't work for this particular

example. Share my code and make a VR and

meta examples.

Okay, thank you. I have to hop off actually, but or at least maybe, but thanks,

yeah, I've got a question about the double colon. Is that a is that you constructing your own list type? Or is that some, some alias to dealing with the the internal meta lists

just just constructed. It's just an arbitrary, okay,

thank you. Yeah. Well, actually, the follow up question, is there a symbol that you can use to actually construct the internal, the internal meta list that's like you've got, I think you've got dot, and probably they've got other languages, do have a symbol? Is there a symbol that you can use for that, or is it just, you've got to get it up with Condor atom and car atom? There's not necessarily a question for you. This is a question for

do you mean you have construction which deconstructs tuple, yeah, yeah, like something like this. So actually, actually, the only way to deconstruct tuple is using current and, okay, it's a moment. So,

okay, so there's no, there's no short head, like, you know, head, tail log, well,

if the tuple, if is of unknown, Rh, then you can adjust pattern much against it,

right? But this, yeah, if

zart is arbitrary, then you need to use Kuder and Car atom, okay?

Thank you.

Yes, I was actually discussion about this. And in fact, we discussed whether we need to represent all purpose in Germany, for example, as as trees. For example, binary trees, then we can reconstruct some pattern matching easily, so but, or we should not do this, and should provide this as an option to programmers. So if you want to in your program to be able to deconstruct your all your data types by pattern matching. You can use tuples of so specific ARQ matching as possible, but internally doubles represented as vectors, right? So and in syntax, there is no like, okay, regardless what, what's, what is in general representation in the meta syntax, the specifically,

say differentiate the cases When tuple has normality and like a bit layerity. I and there is no special operator to become much setup of any way it will be in German, it will be equivalent to the car atom. Thank you. I

I have a question, actually, if we knew, did you see my comment so you mentioned, oh yeah,

yeah. Thank you so much for looking into the issue and basically understanding it. Because it's, it's, it's kind of a, I tried to reduce that to minimal example, but I couldn't that. I had to, so I didn't try. Your suggestion of using the case instead of the conditional. I suspect that if it works, then I can find a way to make it not work again, because the ultimate solution is what you describe in in your last comment. So I'm going to break back so that I I can maybe read it or share it. Let me mean,

I'm going to paste it in case. So are you pasted it? You pasted it yourself, right? So, so

you're pointing to another issue which I did not,

well, another issue is, is about like, some, some, sometime, a goal Alexey address the issue about like so In principles. The problem is that at some point we don't have any grounded for variable x, but control flow tries to evaluate less if the x was greater than zero. Sorry. So. Alexey, actually suggested a long time ago to allow for the operators to behave in such partially defined contexts. But it is not strictly relevant to your case, because, I mean to this case, because we cannot return some specific value for x, we are in facts evaluating this relation. But instead it adds some restriction on various of works, and we don't have a way to represent such restrictions, variable roundings right now, there was no points to do it, and I'm not sure it is, if it is actually makes sense, because it's kind of moving part of the variation logic into the bindings represent. So

Right?

Actually, I wanted to ask you, am I right? That

thing you want to reach with this example is to write some backward chain which can prove parts of the like as a complete proof in an arbitrary order, or this is not the case.

Yeah. So, so you're right in your last comment that if I somehow managed to prioritize the order in which the backward chainer expands, then I will not be facing this issue, because at the end of the day, the right that the test of whether a variable is greater than zero for it to be useful, the the X has to be instantiated, and that all depends on The order in which the backward channel is being run. And so, so, yes, it is true, if I like, for instance, I could imagine, I could I could say, have two version of the rules, two version of the rule I gave in the example, one, one version, which is where greater than x, greater than zero is the first premise, and another rule identical, where greater than zero is the second premise. And if I do that, the the path that the backward channel will be able to take is probably going to include a path where the evaluation of x will be bound and so but the thing is, it will if I do that, if I have more rules, then I have more path to take, while, really, ideally, what I would want is the backward channel to Go, while, as deep as possible, I mean follow path. And then when it can no longer reduce some aspects of the expression, then it moves on to other aspects that it can reduce. And then after it had reduced those, then x would have a binding, and then it would be able to reduce the the ones that couldn't be reduced before, I guess in lambda calculus, that would be the confluence of better reduction where, I mean, it's not it's not identical, but there is this idea of confluence, meaning, well, I don't really care what is The Order, as long as it's an order that

that is well, leads to a path that that that can be taken where, well, in my case, where X is bound and can be evaluated.

So, yeah. So I, because I don't know how I can know beforehand what rules it to take for a particular problem to avoid that sort of data, and essentially,

and so, yeah, if I duplicate rules, I guess maybe I can guarantee that a path exists, but then I'm afraid He's gonna explode the complexity of the backward chaining. I

Yeah, well, it is really the question how to do it

very effectively, probable, right?

Let's get something to the information program in which Adam talked about the about, because

I know that, for instance, Prolog can do that. I I didn't try, but Douglas amante that metalog should be able to support that fairly easily by having, I think the idea is to support this notion of guard where, yeah, so yeah, yeah. And so what I was wondering is, could I support this notion of guard using minimal meta.

Okay, I actually don't know what's the notion of guard, or maybe don't remember. So I

pasted, you know, I pasted a comment in, in the issue mentioning that,

ah, sorry, no, yeah, probably I skeptically case.

Oh, Ali, the link is broken, the link with guards. Oh, well, that's, that's pity, yeah? Well, yeah, that's the nature of the internet. So yeah, let me find Another link that's not broken. I

I don't know if I'm finding a great, a great tutorial on guards. Oh, maybe I think I found one. Oh, yeah, I think I found the kind of the official, yeah, let me

fix that. Do.

Yeah,

yeah. So, I mean, basically the idea is just to have a precondition, and if the precondition is true, then the reduction occurs. And if it's not true, well it does not occur. But I think so the question is, then, because, right, so, so,

so

there's a difference between not occurring and the result is empty. So I don't know how the meta interpreter works internally. So I don't really know how it deals with not reduct, no reduction. I know that we have this not reducible keyword, but so it would be equivalent to not reducible, but it's just as long as the guard is not true, when the guard is finally true, then the reducibility should be reconsidered. But I don't know.

Yeah, you probably don't mean that, like, this expression should not be evaluated by but the evaluation should be delayed until exactly so autovaluation is really needed, right? So

exactly here, yeah,

at least in this example, probably he couldn't. Is just evaluating and after, after the second after evaluating the second premise, and thus ranking will be possible before constructing the final proof. Yeah, if, if the question whether it is possible in current meta, like or minimal meta, I would say that probably not. I don't think it is actually possible, maybe in current limitation.

So yeah, I really if it's actually interesting functionality, and somehow it intersects with the first suggestion in my comment, so it could add some card on variable value, right? And when variable value is really needed, we could try to evaluate it something like this, but, yeah, I don't think we have a journal operators are mechanisms to implement it right now, so I can think about it more after My mind,

maybe I'm thinking that maybe I could somehow rewrite the backward channel code

so that It

only it only considers calling that base case when so, so I mean meaning the caller is testing for the conditions to call the callee, as opposed To the callee during that on its own.

So yeah, I mean, I would have to kind of because the nice thing was that I was able to use

the intrinsic non determinism of meta. Now well, I kind of, I lose that if i Because, then I have to say, Well, if you have this condition, and you can call this, if you don't have this condition, then you can call me that.

So

it's not going to make the algorithm or the code, let's say as as nice looking as it is, but maybe it's going to work. So that is worth the and

then because then I still have the problem. I think that

I impose a certain order, the recursion. I mean, if you, if you look at the the recursive step of the backward channel. So there's a let, which is let star, so multiple things to evaluate, and this has a certain order. And I think that the this order is going to determine whether the something that has already the bindings or not is going to be evaluated before, whether something is going to be evaluated before it has all the bindings, and again, I don't think that's another I can know beforehand. So, okay, I'll try something. I'll think about it, and I'll try something.

Yeah, I believe like breaking all these dependencies when you are inside a chain, will be really difficult task, and probably done inside the Jupiter. So I mean, Jupiter should provide some construction to do it automatically, and also one alternative way. I mean, the only alternative I see right now is to use non determinism to to try Calculate, calculate premises in different orders, I mean, but you're right. It will export, export some like if you combine them in different ways, in different orders, and try to evaluate some initial one of the real until one on the Hook probably will be infected, but you should work in current interpreter as well, should not be too difficult.

Yeah, I will try different, different ways, and yeah, then I'll have a clear idea of how right, How workable is a work around that.

Yeah, it's interesting how we can embed, we could embed such functionality into the metacore. It's also interesting questions.

Something that relates to that as well, is specifically in that case, not for guards in general, but if I had a way to tell well, that reduction is only how to say. So I used to to to say single sided, it's probably, it's a miss. It's a misnomer. But what I mean is so bad issue submitting, yes, a basic issue. So basically, the ability, if I have the ability to tell that a function definition is only meant to be single sided in the sense that it's going to run like a traditional function definition in in a functional programming language, meaning that, well, essentially it can only be called on a term. Well, as a as I'm talking, I'm actually not even sure, okay, I'm going to finish my sentence, but meaning it's only going to work on a term which is either an argument which is fully grounded, or at least, which does not have more structure than the the the pattern inside the function definition something. But now I'm realizing that for my example to really work, it would have to be fully grounded. It's kind of uh, but nonetheless, I mean, I they, I have situations where I define a function, and I really would want this function just to be reduced if the

if the caller is calling that function on Something that's fully grounded, there are multiple situations where I found having that would simplify my code. And yeah, I'm saying that it's just one more of these.

And since the Kotlin compiler makes some kind of this assumption. Currently, maybe it could be useful for optimization purposes as well.

Yeah. Well, I actually don't really see how it could help with this particular example, because like we are talking about, I mean, finally, in packaging A code, we are trying to better match result of recursive call tobacco change with some pair of expected result, And if greater than zero operation is not reduced because argument is not carefully rounded, then what the whole, the whole vacutiny of step should return? So right now, I mean in the description of the issue, it returns empty when greater than zero evaluated and it Turns false. It becomes some tuple. Is CPU proof if expression is related and return true, but what should it return when expression is not valid? This is the question so Angel should figure out so, so I think

the um, I was going to say, well, it's the equivalent of not matching, therefore not triggering a call. That's how I see it, that

let that

will so like, then that will not be evaluated as well. So according to current meta semantics, if this code not evaluated, then the whole stack is not evaluated. If it comes a if you don't like you don't handle the situation manually, so you're expecting that something inside motivated.

Well. So, so yeah, I suppose it's back to the question of the order.

It's true that it's the first situation where the order matters. And so yeah, all it means is, well, it doesn't match, as long as it's not grounded, it doesn't match. And if it doesn't match, then this thing, this branch, cannot be taken, and maybe another one can be taken. And maybe this one that's taken will result into a proof, but the one with the CPU proof cannot be taken. And,

yeah, yeah, yeah, it's all but I mean, according to meta semantics, a new example. As far as I see, there is only branch in your example. So because China just recursively cause its costs of by, but I mean if, if something in this branch cannot be related, then in this particular example, there is no other branch to, okay,

yeah, yeah, correct.

I mean, so product solution and somehow to use this branch, either I introduced through some internal meta, like, does it change in the meta semantics, or adding something to the Meta semantics which allows you to like, which was interpreters to form another branch, actually in such case, so to speak, or another solution is to add This branch manually, right by writing by cochinia, yeah. Yeah. So, yeah, maybe you meant it. So maybe I mean when we didn't mean that introducing the single site evaluation will solve the problem by itself, automatically. But right, yeah. Just that's some notation which we can use to help interpreter to understand

solve the problem, yeah, yeah, yeah. So basically, I would rewrite, so if I had that, then I would rewrite that code by just replacing I'm going to paste the two base case and the second base case would look like pasting, Yeah, is

it? Yeah?

So you see that the first definition of the base case is traditional because it has to be traditionally two sided, and the second one is has this extra equality percentage symbol that indicates that this one is only going to be single sided, or, I guess I should be more specific, the the arguments have have to be fully grounded, yeah. So if I had that, I believe would, we would. It would solve the problem if the interpreter is willing to wait, yeah, okay, right, yeah. And so if you need that for other purposes, such as Kotlin, Kotlin optimizations, or things like that. Well, I would welcome that, otherwise, in the meantime, I will keep trying to find workarounds, because they probably exist. I suspect they do exist. Maybe they will not make the code as elegant as I would like, but if they exist, then this is not a blocker. So the other thing is that they may exist, but because they are not using built ins, they make things much slower. That's will have to be taken into account, but, but as I said, let me first see how far I can go with the meta as it currently is, and and if it really is a problem, then only, then I'll come back.

Okay, yeah, I'll try to also think about it.

Yeah, difficult, like, have a list of premises we need to move. And just move to this list by trying these premises. If we can evaluate backward chaining call on this, just remove it from the list. If you cannot evaluate them, just put the end of the list and continue, continue moving as a princess before we come to the first one. So it should work, probably, but and be effective enough, I would say. But it's interesting. Is it possible and is it easy to quote it,

yeah, it, it occurred to me that I actually have a few I know we're past the time, but

if you're still available, Vitaly, I have a few more questions coming from, well, various teams working on using meta and so, on their behalf, I'd like to ask So. So,

for instance, in the context of porting Moses to meta, the question of turning non determinism into just a one how to say one run that randomly takes branches. You see what I mean. So, so in the case of the backward channel, would be, for instance, is not going to try to evaluate all possible branches before it ends the computation. It will just pick one and, well, if it evaluates to something empty, well maybe return empty, or maybe they would repeat until it evaluates to something that's not empty. But, you know, random sampling interpreter, as opposed to fully non deterministic, non interpreter, I believe Alexey has been experimenting with that. I think I've heard that, but I don't know how close to be integrated into meta that would be. That's my first question is it. Is it clear? Is the question clear?

Well, yeah, I experimented a little with a sort of sampling semantics, but I didn't progress a lot because was destructed by other stuff, like metamod, snet, SDK, format, etc. It will be nice to return to this probabilistic programming stuff, and I have it on my to do list, but I'm not as a yet.

Okay, so do you think it makes sense for me to to tell the team in question? Well, go ahead and if you feel like it, hack meta and, you know, just hack the interpreter to experiment with that. Or do you have something that's a little bit more like, maybe something that's already a beginning of, something that you'd rather pursue, that either yourself or if it's not yourself, in a specific way that you that you see as being more promising, and If so, do you have code? You have a branch that would have that code or etc?

Roy, I've got a

question I want to ask at the end of the at the end of this bit of the conversations, before we wrap up. So just flagging the one to do

that. No, is it related to Neil's question? Or should I go first? No, no, it's

not related to Nils question, which is why I want to let you finish this conversation first.

Okay, so Neil, well, I do have some code, but it's quite experimental, so I don't think it makes sense at this stage to share it, and I recall that I was also waiting for the cotton compiler to Be more ready, because when I started working on this probabilistic programming stuff. I realized that I want to compile some execution traces right away, and it makes no sense to work on compilation on my side. So I wanted to fuse it with compilation on the Kotlin compiler side. So this is one more reason why I stopped working on it. So yeah, if someone wants to hack into as a meta interpreter, then yeah, please go ahead, it would be interesting to share.

All right, okay, okay, and so I have two more questions I'm going to ask them, and and Roy, then you can, you can ask your question. So it's about the types. So is there any plan to have something like, how we call that very addict, very addict type, or something that would be able to to tell that, well, someone, someone who's writing something. So let me read that first, in case that's relevant. Thanks very much. The idea would be to create a similar space in Spanish, disseminate. Okay, okay, okay, we can look into that. Yeah, okay. Questions, I guess so, yeah, so. So, for instance, if you were to write an NRE plus, for instance, something that is taking a an arbitrary number of arguments, but you want to specify their own numbers. So is there a way? Well, I know the answer. The answer is no. There's no way to specify such a type. Do you think it would be a good idea to have such such a type, and, and, well, I guess, yeah, that's, that's basically the main question. I say I had two questions. Ben, thanks. Just one. It's this one. Well,

it's the same question as Vitaly has already answered. Because if to do this, we, as you, need to integrate it into pattern matching and under the hood to represent tuples as trees, or you can just use explicit types, like list of nets, for example, right? Yeah,

that's the answer I expected. Okay, right? And actually, it occurs to me that right, due to the known determinism of type definition we can have if we want to say, Well, if we want to define say up to 50, or whatever number we can do that actually, right? It's it's possible. So, yeah, okay, that's all for my side. Any other question, please go ahead, right? Yeah,

please go ahead. Yeah. This is, this is not from me. This is from Edrick, who's been working on the collapse bind and metallogue. And he posted a battery posted, he posted a question to meta coders a few days ago that he'd like to know why I just posted in the table. Just show up. I thought it is posted in the let me try again. Basically why valers needed to get binding with collapse. Bind, this is trying to put in the chat.

Is the best person. Sorry,

I've posted it twice a year. That's that. So, yeah, so anybody can help with that. Andrew is kind of stuck on it, so he asked me to bring this up.

Okay, Can someone explain why to get by and,

okay,

why? Well, so okay, I don't, I'm not sure I understand the question actually, fully, because I will

I was needed, I'm sure who was needed to get bindings with calls by But the difference is, I mean, at first, Alexi inter, introduced superpose and cops, which doesn't contain variable bindings in the results and arguments. So you can just run superpose or codes and we you will get results without findings. Okay, so maybe I realized what the question is. So and when, when I was writing minimum meta interpreter, I tried to use scopes and super poles internally, and I found out that I cannot pass the full evaluation context without passing bindings. Thus I added two specialized functions, scopes, bind and superpose, bind, which which use bindings will increase values inside the results and arguments and these two functions was used mainly internally inside the meta interpreter, implemented in minimal meta so actually one can use co ops without bind, postfix and superpose without bind postfix and this function will return result without bindings. But sometimes you actually want to keep the bindings context in your program. I mean, for example, you want to evaluate like, like, like here you evaluate test is Variable. Variable actually get some bindings if you if to get the result of this evaluation and filter it out, and after that, you want to return it into the interpreter. By using superpose, you will find out that variable x just like just to lost its value because the value was not inside the filtered list of the result, results. So the short answer or some summary, if you don't need variable bindings, you can use co ops and superpose without positives bind if you want to keep variable context between co ops and super pose calls, you use versions with postfix minus byte. Does it answer the question? Yeah,

I think so, yeah, like I say, this is, this is an adjudic question, but I'll pass it on to him. So thank you.

Okay, no problem, I can repost it the answer into the metamost as well. So thank you, sorry I really at least at this point.

Thank you again.

Okay, and there is suggestion with which new career sets, some collaboration and similar meeting in Spanish, I believe here we can discuss the bottom most. I would say it's great idea.

Yeah. Guillermo, if you have something to add, feel free to to vocalize it now, I think, but, but otherwise, yeah, sure, we discussed that on matter most.

Yeah, Neil, sorry,

yeah, thank you.

I will text you on monomos, and we we figure out how we do this, as it's pretty challenging, and we myself. I'm still in learning mode so but I reached later to you guys, and thank you again for doing this amazing stuff.

Thank you. Okay, thank

you for your interest. All right, so I think we can end the call Well, well, thank you all and See you after

two weeks. Then,

thanks everybody.

Thank You.

How accurate was this transcription?

0:00:001:29:24

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5