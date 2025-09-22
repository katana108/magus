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

Feb 7 at 7:37 am

54 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

new faces, screen demonstration, function superposition, type definitions, logical statements, universal quantification, existential quantification, modal logic, temporal logic, unified rule engine, inference control, back chaining, knowledge base, logical implication, cognitive architecture

## Speakers

Alexey (34%), Douglas (32%), Speaker 1 (21%), E (8%), Matthew (4%), Speaker 2 (1%), Speaker 3 (<1%), Speaker 4 (<1%), Ben (<1%)

Is besides, just lucky enough, I was with Ico before, and I joined singularity two weeks ago, and currently I'm exploring a small system. Nice to meet you all. Thank you.

Thanks for being here. Thank you

any other new faces, and then after that said, I

Is that a no?

Okay, if no one else wants to introduce themselves, and we can proceed to suggestions screen demonstration. I

You can see my screen, right? Yes, okay, so maybe start with the thing that I observed. I was a little bit surprised about it, which is, when you when? So here in this, this simple file, I find two functions with the same name, so they will So define this function process, and one of them gives an A and the other one gives a B. So then when you when you call the function, you will get this superposition of

a of x and b of x. And then I wanted to try something out, so I basically added some atoms to the space here, maybe probability for some expression I say, Well, I'm matching expressions of that form, and then I will call that function on the results x which I found expression. So in this case, I mentioned that I want to find in my space. All the value that I assign here, right? I could call a and it would be a number from it would be a function that takes a number, so in this case, and it would give me some type that I just gave him really arbitrary name, AB, two. It's because I'm saying that these are experts, a and x b, and I'm putting an a in front or a B in front. So you would just get these rules that

basically look like that. Look like sort of tuples like this, A, B, B, but then I observed something. So in this case, there's really this name can be, really be arbitrary. So when the type is undefined of this expression, you can just sort of assign it to randomize. But then as soon as you

like a type of symbol, you kind of get the result that I did not expect at first, which is that here running this, you see that it's it's not going to match this situation like this function A, and I thought the reason is that in this case, a, like I said that A is a function from some arbitrary name to that other arbitrary name, AB tuple that I find here. So if the final result is this, then I would expect this to be of type AB tuple, because this like B would be assigned with some name. This is just both of types are undefined, and in this case, 2b is just like the type of this is basically undefined. But in the case of AA, because AF said that a it has now it does have a defined type, can no longer

be, can no longer be assigned to this first argument, a some name. Then I thought that that was maybe some observation that I wanted to share, that I was a little bit surprised by at first. But, yeah,

yeah. So

do you find this behavior correct, or is it a sort of an issue?

Well, it's not really an issue. But it does go maybe against something that I did expect at first, because I thought the sort of philosophy or idea at some point you would have the space which would be like a big sea of expressions, right? It would be full of atoms, and maybe not always, not always, like necessarily purely atoms of certain you would also end up maybe in some situations, you could use that those type definitions as a way to maybe sort of filter out what what you are matching against. But I thought that in that case, it is a little bit weird that the underlying expressions are basically gonna be able to match them to just just to any type, even if it does have a name that is assigned to other things in this space. So it does make sense, but there is

quite strong background, most still from you. So maybe it would be simply if you could copy paste your example to the call chat. I just wanted to understand if it's really surprising or it's A normal behavior. Yeah,

well, I believe it's not the problem of matching, but since you declared that type of a as some Name, AB tuple, then when you're a small function after matching returns a a result, it has been evaluated further, and it it is rejected because of the type here, because A is Not of type, some name, right? Yeah. I believe it's a normal behavior.

Yeah. I thought so too. But I was a little bit surprised when I saw it, because, you know, like B, it's, it's also not necessarily of the same type. So I was surprised that the like the you can match it something other types on the client. But otherwise, when it does have a name, then it is protected, which makes sense,

yeah. But basically, if you just type, try to execute a a, you will get a type here, and it's perfectly okay, but a B will not result in background because B is undefined.

Yeah, I thought so.

So that's one thing that I had. I also had some other questions that maybe somebody else would like to go first. Yeah,

nobody wants to go first. I will share my older accent, right? Sure

I was taking a look on how you can express some basic logical statements, or some basic statements in MeTTa, right? Because in the documentation, there are some examples where where you have these relations, like predicate object or relation subject object. So that was kind of easy to copy.

Oh, yeah, I mentioned you had an Adam that that said something about John, namely, that he had blue hair. And later you want to know everybody who has blue hair, then you can just match it. And the same with the relations, right? If you have a binary relation between a subject and object

names, then you can just find it with the match statement. But I got stuck pretty quickly when I tried to encode like extension and universal quantifier.

For the universal quantification. I thought, well, what like the most basic way to represent it? It would be through a function. Because in this case, I mean, if you would say equals p1, of x, p2, of x. In sense, it is also expressing that when x has a property b1, it will also magic property p2, so you could kind of imagine that being what the equivalent to statement saying for all x with, for all x with with be one of x, you also have to be two. So there I thought, well, that is one way to look at it for universal quantification, but I really got stuck when I started thinking about how you

would express existential quantification, because you can't really just assign a predicate to it, because if you, if you would express it in the way that I've done here, where I said, for example, function from

p1, of x, 2x exists, I would really, I would already, basically have to produce an atom which predicates something of X before I can, before I can know that It exists. And then I would already have produced,

produced a witness to the fact that I'm describing it. So then it would be kind of meaningless to say that over there I really got stuck, and was not sure I could imagine that maybe one of you might have thought about this before, and that you had some some way of representing such statements.

Well, yeah, actually this maybe use case for this simplified use of MeTTa is discussed in one of the basic MeTTa tutorials on the site. Let me just provide a link, and basically, it's not a correct way to try expressing universal quantification or causal relations. So logical implication in the form of P 1x equals P 2x it doesn't work in general. It can be used in some simplified ways. And in the example on the metal and depth tutorial site, there is sort of, I don't remember if there is an explanation or just a question to for the readers to consider, but you cannot represent logical implication as just Such a quality, so you need to use conditional statements in this case.

Okay, so you would say if be one of x, then p2, effects. Yeah, I see it in the documentation. Thank you.

Yeah, please take a look at the explanation, if there is an explanation in the tutorial, and if this is not enough to answer your question, it will be a perfect topic for writing another tutorial. So if you will still have questions about existential I believe there are no existential quantifications In this tutorial, so maybe we need to write an extended tutorial on how to represent things like this in MeTTa. But basically we as a need to have a sort of general purpose library in MeTTa, beat PLN, or something less specific in terms of truth values and so on. Or we need to write something's manual. Manually each time. For example, we have right now some experience with expressing join tech logic rules in pure MeTTa, and it has its own ways of handling unknown values because, in fact, we can in MeTTa, basically, if we consider it as an constructive geometric system, where we may have not only true and False, but also empty or non reducible values. And in general, as we need to say that we don't have them in this particular situation, or we need also to take them into account, to handle them in our code. And for example, there will be a difference between if something is true, or if something equals to true, because, well, maybe it's a topic for such a tutorial. In any case, if you can elaborate on your example and your question in an issue on MeTTa, MeTTa examples side, then GitHub reports, and it will be perfect, because we also use MeTTa examples report for questions which are good for tutorials. So please elaborate on this. Okay,

thank you. I will write it down, also maybe tying into that. I would also ask if there is some kind of a paper that has been written or published regarding the logical system that is underlying or like underlying guiding design of MeTTa, or whether that is something that went more in organic

way,

because if there exists such papers, I think I would like to Read it

well, there is probably no such paper. There was a preliminary net specification with some thoughts on this. There was a paper on,

well, on how to put it's not precisely on MeTTa,

well, I don't remember. I need to see this paper to understand if it's irrelevant or not at all.

Just a second,

okay, and then maybe following up to discussion about existential and universal fund gates. I also thought about, you know, how would you represent, for example, modal logic or spatial logic or temporal logic. And then

one of the one thoughts that I had and understood also from some previous discussions that exist on MeTTa Moses, that maybe the possible worlds for you would be most, would be most appropriate to represent modal logic, at least.

So I'm in the original before MeTTa open cog long, long time ago, I know we did have some modal logic included, or had done, not necessarily included, but done some Google Summer of Code work, and I'm not sure the current state on that temporal logic. I know nil is working on some and PLN. Len, but I'm not sure that, basically, following the Patrick's work in in Nars, but I don't think any of that has been, you know, incorporated at this point, I'm pretty sure it has it

okay, because I thought maybe one of the ways looking at it would be that maybe it's not necessarily to always when you're representing like statements in the MeTTa, to have one final definition. But that could also be somehow, later on, transform, like, certain statements, for example, if you're talking about spatial logic, that could start with, like, one way of system, that different way of looking at it. It would just be, for example, a predicate. And then you could maybe, like, somehow translate through these different ways of expressing a similar thought.

You know, it is true that if you're representing ura, universal rule engines from open rules from open cog, you can definitely represent the results of implication and modal logic, you can do temporal logic pretty easily, as long as you're Keeping negation separate sometimes from positive implication. For example, all dogs are mammals. You could, you know that's a a universal quantification thing. And so if you have an assertion that something is a man a dog, you can query and get that it's a mammal, and you could assert that assertion through as a universal implicate implication, and end up being able to query, tell me about the mammals, and then have that particular dog come up during your query for mammals. And so I guess what I'm saying is the way the universal, the inside rule engine worked, and open COVID was capable of making deductions that way because they had a back chainer. And we should be able to do that MeTTa without a problem. Also, you can represent existential quantification in a similar way by having it. For an example of existential qualification is for every something rather there exists something else. So let's say all mammals have hearts. You could say for for all things are mammals, there exists a heart, and that heart is something that that mammal has specifically and so now, if we were to query for all hearts out of the data of the knowledge base for that one dog would that we had in there would yield one heart, and it would come back as heart of Fido, let's say. And so you can get existential quantification, as long as there are like relevant facts. Oh, we can have a dependent quantification. If you want a singular quantification, we can also do that. But what I was going to say about negation earlier, this is why it's important if we have something, we have a fact in the knowledge base saying there are no hearts that exist in the world, then we would have a way of proving that there's no mammals. They exist in the world, because all mammals have hearts. So I'm trying to say is that if you have a fully specified, unified rule engine, you have the capable of doing capability of universal existential quantification. If there's going to be some way that would be better optimized in MeTTa to do that, that would be great. But no matter what, we can always fall back on having that type of system as a something that's written on top of MeTTa,

I see, but I mean, as you speak, you wouldn't really be able to express the concept of topic exists without providing a specific instance,

providing, yeah, I mean, I did say that that is even kind of Even a limit. What I would say is that we could, let's say that we. No one said anything about there not being hearts, and no one said there was anything about about there not being any mammals or or even even put anything in the knowledge base about dogs, we should be able to ask, we should be able to use the model logic, is it possible that something exists? And it would be able to to say, should be able definitively say, Yes, does something exist? It should be able to tell us that it should be able to come up with no answer because we haven't told it anything, but we should build and we should be able to query this actually nothing exists, and it should be able to come back with no answer, leading us to conclude that something may exist. I mean, there is a way of getting good, necessary and possibility logic on top of a system like your ure, so you don't always have to have a specific instance. But I mean, as long as you you realize you're using an open world system, you can your type of query can be such and you know, you can even make wrap those types of queries into something easier to make. So for example, if we want to find out if something is possible, you know, for example, we might query if the negation is is true and the negation comes up with no answer, then we would know something is possible. We can code that in into something that infers the possibility in a single predicate relation, rather than having to make like two or three queries to come up with the deduction, we can still make those a back chaining rule that would allow us to make that deduction with a single query.

But when we are representing these kind of concepts like quantification. They could also be just like implementing with a certain symbol or something like that, and then later on, implement those kind of rules to actually make them for

Yeah, exactly, totally. We can. So, yeah. So any sort of thing that sometimes those are called role macro predicates, where people call them that, where we make an assertion at the high level of describing exactly what we want, and the side effect that is in the knowledge base is a result of that, you know, factoid that we put in, first off, we say there exists two dogs, and we would wouldn't have to actually assert information about two specific dogs in the knowledge base, that if we're to query it, we should be able to get two columns, At least two column dogs coming out with knowledge base for us without having to assert them specifically. Yeah, that's the superpower of the Unified rule engine that the way MeTTa is designed, there's no difficulty doing unified rule engine type work inside of the meta language.

Okay, That's all.

Anything else from my neighborhood I

anyone.

I would just like to make a quick comment on the last Yeah, when I said that, if someone is using MeTTa, they have easy to manually code, some inference stuff. I don't mean some complicated stuff, but still some rule processing stuff and rule changing stuff, which can be done quite nicely in MeTTa, at least sometimes, but still, there is a need to write this stuff down and when I said that it would be nice to have a sort of library in MeTTa which could be general enough to be useful for implementing To help more than MeTTa already does in implementing different logic inference engines, yeah, I meant something like a unified role engine. So our idea was, while MeTTa is much more rich and language like and has more capabilities for inference than ame. And the unified rule engine was actually coded in C Plus Plus with the use of queries in atom space. And we wanted to put some part of the Unified rule engine into the basic language. It turned out to be not precisely enough. MeTTa is still lower level than the unified rule engine, and we possibly need a library which make coding new logical systems even simpler than it is now. And well, I think that it should not be a quite specific logic system like Duong tech logic, PLN, NARS or whatever, but it's it indeed should be something like the unified tool engine, and it's not yet here, And that's why we have to code some additional stuff in MeTTa itself when we are implementing something like what Sebastian has shown. But in some cases, we maybe not need something too heavy, like the unified religion and capabilities of the core MeTTa language. I enough for this. So yeah, please go ahead with your elaboration of on your example on MeTTa examples GitHub repo, and we will discuss

you. That

makes total sense. Alexey,

someone on my team working on Nether logs, started implementing the unified role engine. Some of the pieces of it in MeTTa is basically a back chainer where you might say, this is the consequent and these are the antecedents. So you might make a so you make like a so you call this predicate called prove. And what it would do is try to prove the head, and then it would go and do the back chain for the antecedents, nil, sort of has worked on this sort of thing with the towards PLN as well. Like, there's sort of a common theme where we all have been seeing, Oh yes, you know, we have to have these implication rules. You know, even the original MeTTa implementation allows you to write a rule like append, which appends two lists and it sort of back chains and produces all answers the way you would expect a rule engine to do. So, like the things are there in MeTTa, the support that you might need to do back chainers And rule engines and so people have been doing them. We just haven't really converged on, we're going to say, use this particular back chainer for everything. But sometimes it's not that idea.

Yeah, but the issue is that if we just implement a backward chain or in a general way, it will be not efficient enough, and we need a library or a part of as inference system inside the interpreter to have inference control. And it's very big project. So if to introduce such things inter MeTTa, we would like to do it right, and it's quite legend, or

you're totally right, and that's why, no, we have to converge. Because we keep telling ourselves, yeah, once we have what we feel like influence control should look like, then, you know, we'll talk about implementing it in the interpreter itself, you know. And yeah, you're completely right. And explain that well, even a must be a reason it hasn't, you know, because we realize that it's going to be inefficient, and we have to have it in the interpreter as part of it, And it even if it was a library, yeah, I

uh, another approach, which is sort of, is what is like, say, Nils back chainer, if it's being slow, we are optimizing the interpreter to make It not slow, and that that ends up being musical to everyone.

Well, I didn't mean performance issues of the interpreter itself. I Amen that the problem of backward chaining is kind of AGI complete. So it's not just about efficiency of recruiting stuff, but it's about well, algorithms, heuristics, program specialization, maybe amortized inference with neural networks or whatever. So it's very, very huge thing, which maybe should be a part of the cognitive architecture, like Primus or whatever else, rather than a part of the language design, you're right,

yeah, it's way more than about performance. It's about being able to not get trapped into loops, its ability to use types, these type restrictions, all these useful things that have to be going on besides performance inference control, like saying the ability to limit the number of answers, if that's what you're looking for, yeah, you're right. Indexing large spaces. Be able to have something you know so much information that fits on more than one machine and still have that work during back chaining. All these require more than performance and optimization. I

It also requires a little bit of standardization of like what we think an implication will look like too, like if we're going to use quantifiers and we're going to use there exists for all. And are there other quantifiers like and there is at least one or there is less than two? We have to have a full, rich language for this logic, and that probably goes beyond just personal logic. It has to do with, you know, the larger part of AI and AGI,

sure, and I mean, we did think through and within PLN itself. We did think through, you know, kind of like almost all, or, you Know, flexibility and defining those terms, those quantifiers,

totally, I

but that has, that still hasn't been ported over to hyper on PLN yet. I

Okay, Maybe there is no other topic. Or maybe you can finish,

thanks everyone.

Thank you, bye. Have a Good weekend.

Thank You, Bye, Bye,

How accurate was this transcription?

00:0054:21

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5