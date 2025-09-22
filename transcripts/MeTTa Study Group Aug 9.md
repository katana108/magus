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

Aug 9, 2024 at 7:31 am

1 hr 29 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

metta, function, variables, type, define, subtype, case, evaluation, unification, write, definition, call, code, rationals, implement, integer, list, python, matching, question

## Speakers

Speaker 1 (27%), Adam (24%), Speaker 2 (23%), Alexey (17%), Speaker 3 (4%), Speaker 4 (4%), Matthew (1%), Speaker 5 (1%)

I saw Alex

Hi,

Alexey. Can I ask you a real quick question? Alexey

went on vacation, and he was scheduled to give talks at the open cog hyper on workshop, and I haven't heard anything. He he went, he mentioned his vacation and left the same time, and he hasn't responded. Do you know anything?

Oh, wow. Well, actually, now I will try to ask him, I hope that he will participate in the workshop, despite of location, it's my default guess. But yeah, let me ask him to Mike. Yeah,

he hasn't responded. Non matter most. So that's, that's why. So I just wanted to, and I'm gonna have to leave in 25 minutes, so I'll just drop off then. Okay, hi nil, Hi, everyone,

hi, hi, hi.

I'd go through names, but it would take too long, right,

which is a good thing. I

i So who wants to start things off?

I had material, but please, anybody, feel free to go ahead if you have anything, because

mine are more like, I don't know how to say that.

Yeah, I got some stuff as well. Maybe I can show you. Yep, I

thanks, Ambassador, hi.

So there are two things that I wanted to show or talk about. First one I I

share this

window now. Sorry.

Direct is over, yeah, there we go.

Yeah.

We there, yeah. Do you see my VS code. Who knows?

Yeah. Okay, so I wanted to try out some recursive algorithms. So first thing that I did is I defined a function to measure how long, how long a function execution takes. So that was kind of useful in, yeah, in finding out and comparing different strategies. So I wanted to work with numbers. First thing that I tried was using the random dot random function in Python, but it was very slow, so I had more success with this by just using this function from NumPy for generating a bunch of numbers. Then I found in the metta Leung dot dev this this algorithm to create a list, right and in this case, using the car atom and CDR atom functions. So I tried to do the same for this numpy array. So I defined a PI car and the PI CDR, with the idea of obtaining a list that that might look a little bit like this, right, where you can actually iterate over it from within. Metta, but I found that that using this kind of recursive algorithm in this way is actually quite slow. So I was a little bit surprised, because I thought that, I thought that that should, should execute very quickly. But as a matter of fact, the more, the more numbers I generate. So I mean calling the numb by function, it's not, not a lot of increase, but as soon as, as soon as you call this kind of by to List function, which checks whether, yeah, whether you've reached the end. And otherwise it goes on by giving you this list item and and then recursively calling by the list again with with the deal, it actually it becomes slower as you, as you iterate more. So I didn't really understand it, because I thought that this was supposed to be like O of M. But practice is not the case when you measure it with this timing.

Yeah, as Alexa, I think, already posted in chat, the asymptotics on this are wrong. It's an issue that has a lot of debates, as is linked a feel like, what happens is that the expression gets evaluated, gets evaluated all the way down, even though, if you you add only a head, so it becomes quadratic, and instead of linear, on top of the pretty high base cost of the the PI car and pi CDR, like the the functions that call into Python, right? So you can expect like, about, I'm afraid to say, like the, I don't know what you have up to date numbers are, but you can expect, like, a much higher cost of calling into Python than just using the plain risk version. That being said, Are you using the latest version of hyper and experimental? Because so yeah,

I tried to update this. It could, it could be not, because I didn't update anything. I just did that install, upgrade. But

what version are you running on?

How can you see that PIP

brief? Yeah, if

you do like PIP lists, it should give to version numbers. I believe

I see that in the code using PI CDR. So pi CDR is would be constant, like, Why? Why would that be quadratic? If wouldn't pi CDR be constant.

That doesn't, doesn't, like high princy into the PI list. I believe the PI list is actually included as a as a value in I could be I could be wrong there. But like, no, it's still, if you're building the list like, it will still be byte quadratic, because every time you're you're running down into all the heads you've already accumulated. So,

yeah, yeah, but, but he's building so in the code pi to list, he's building an actual list, like with the constructor, and so it's not manipulating topples, man growing. Like,

still, the, you see the the double colon, right? I believe this is not a grounded function, right,

right? So, like, if,

if, the, if the double colon is not a grounded function. This is still quadratic in you, like, if you evaluate the whole expression everything,

that's

why that would be the case.

So, yeah, I'm not saying it should be the case, but I believe that to be the case that you measured like the asymptotics, because it seems like it's it would be higher than linear.

I didn't measure, but I just typed in three, four or five, and it was evident from this bridge just printing the milliseconds next to it, right? So if I run it, I

so what I have found is that when you build a list in that manner, as the pie to this code does, it's faster than if you grow a top hole. So what I have assumed is that growing a couple is is, is, well, super linear, but during it that way is linear, but, but maybe, maybe both are super linear.

And also, to execute this code, I had to make a small change over here. So when, when you are running a recursive algorithm like this. There is some kind of equality check being made, but there is a funny thing going on, where if two NumPy arrays or nd arrays have a different shape, you actually cannot compare them with this is operator equals operator in Python, so it will throw an error. So I just, I just made here a small change by just wrapping this was the is the original code. I just wrapping it in a try except block where it says that there are not equal when there is an error going on. So

maybe that is sorry. Could you re explain this bit

well? So I'll show you what happens if you, if you just this is the original code, right? So your value objects, and then if I run this, so this by list, that is a that is a buy at them of an ND array with length n, right? But then if you take the tail, it has length n minus one. So what happens when you run it? We will get a runtime error. It says operands could not be broadcast together with shapes four and three. So that's those are the nd array shapes with a different or nd arrays of NumPy with a different shape. Apparently, you cannot compare them using the equality operator in Python, because if I follow this link right, I get to the atoms.py and it's evident that that this expression cannot be evaluated. So if I just define this equality function that is basically just, yeah, coalescing to false, and when there is an error, the problem is solved.

Yeah, I feel like the and the array like the it's a very old piece of technology, but I feel like by now, the consensus is that the equality check on it is first checking if the dimensions are equal. So this is like shape, like dot shape is equal to dot shape, and then checking if the flattened version is all equal. So like dot all. I believe you can go and then you can check if the or, like, even

perhaps NumPy dot equal, I don't know, NumPy dot all equal, something, something along those lines. You will find plenty of it on the internet. But first do the shapes shape test, and that will, that will eliminate the case that you you brought up where you can

if I do that, it's the same. It also solves the problem. But I thought it would be a bit awkward to put something so specific in this value object class.

Yeah, like, on the one hand, yes, on the other hand, like, the Python ecosystem is not very homogeneous. So, like, this is on Python you you will have to, like, if you wanted to be more well behaved in metta, which I believe we want. I think we do have to, at some point break up the cases. Yeah,

so that was the first thing that that I wanted to talk about. And just so for clarification, if I would change this here by some grounded atom, I don't know. Think in the docs they use the word cons, you're supposed

either,

probably the same, right?

Yeah, okay, well, anyway, so So that was one thing and then another thing. Yeah, here it's all ambitious. Of course, like any good programming student, I suppose, want to learn what a monad is, right? So I just followed this tutorial that I found on the Haskell wiki and try to copy some stuff from there. I don't know if it makes a lot of sense, so I just wanted to play around a little bit. I thought this is useful, so got this bind operator. That is, yeah, it's defined in this way. This is an example function. And then if I take this function f, which has a return type of maybe a number, it either returns just add one of the variable that I put in it, or nothing. And then, yeah, then I can define it. Here. I say that if I run this bind operator with nothing and some unimportant variable to return nothing, and if I run it on just X with a function, it will apply that function on just x. So here are, here are some examples. So if I just run it, the function f i also have. So the mechanic condition here is also that it is checking whether

it's a number or not. So in the case of nothing F, it just returns nothing. In case of just a string, it also returns nothing. But you mean you can just, you could also write my error here, or something like that, and then in this case, you get just two so you can repeat it, and then it will just compose those functions and but in this case, when the type is not maybe of a number, it won't work. You will see that in the first application, it will just reduce it to the number itself, the result of lying F on the what is inside this

binding agent, you should be able to parameterize the type of the binding operator, you know all the operators involved in your definition. So, so that the type system would not permit you to add a number with a string, even if it's wrapped in a maybe, I think, I think you should be able to do it.

Yeah, yeah. So,

so that you will get a type error when you even call that kind of function that is not, that is not so

if you scroll up in the definition of, right? So you did, oh, well, so you did. You did the right thing,

right? So you see

maybe there's some definitions missing. For example, this I've not defined maybe also there was a reference to return function which just is a function from so sorry, but

is your function definition for binding just is correct? Should you wrap the result into just as well?

In this definition, you mean,

yeah. So should it be just FX, because you need to have maybe as an output. No, I

Yeah, so you're saying you put just here in this definition of the bind operator, and then any function that you are that you are passing to apply to the value of just something is the void of this.

Because I thought that maybe was defined as just something or nothing. So I thought, well, you know, either it's true or false, so you either have just something or you have nothing, but then you have to do that for all The functions that you want to pass in.

Well, I

I don't know. I think it's, it's a little bit of,

it's a complex concept they still have to get used to.

Because normally speaking, you Is it supposed to function like this, the bind operator, where you can just

apply, if returns, maybe, then you're right,

yeah, ideally,

you wouldn't be able to use this with with any function, like if you're talking about flat map, of course, you you can define your your map on this as well, etc, and Those should work as in most other programming languages.

Yeah. I mean, it is interesting what you see in this result that if you do say what you said, I think

let's say that

that here you do get just three the expected output in this case,

so that just type check or,

well, I mean, you get this,

I guess if your function returns, maybe then you don't need to wrap it. Well, on the other hand, well, yeah, if f returns, maybe then Zach additional wrap and is not needed.

So you can do both. You can either choose to define output within this F, or you can just say, well, I all I say here the output is always just this, and then, then it will work regardless this one constraint less on the functions that I'm defining. So you have two options. Either you leave the just out here and you do it like this, where you

just additional trust,

delete, yeah,

and then.

But what is a type definition for F?

Function from A to maybe a? So I put in x, right? That's a number. So here, if x is a number, I get just a number, and if it's not a number, I get nothing. So that's maybe a number,

okay? And why? Why you didn't define the type definition of f as number to maybe number

well, because I wanted it to be generated right. Suppose that this could be abstracted again where you

can, yeah, like, this is a standard definition. You shouldn't. You shouldn't redefine mines. So it's good, it's indeed, it takes a function from A to m of a

that is a good track this, if any of you mean, I know that you are all experienced programmers, but if you are struggling with these concepts. I thought that this was a nice resource, and I'm also not finished yet. This is just chapter one, so it's a good thing to try to implement that those because this explains some it gives a lot of examples of Haskell implementations of monads, anything that is a good exercise to try to translate them to here,

right? So, so, so you wrote the F, such as, okay, now you have a case, if it's a number, and maybe you you like, it's just one case, but you could have more cases. What to do it. It's a string, etc, right? Is it? Is that the direction you wanted to take this thing, or

not necessarily? It's more just an exercise. I think, I think I want to try the other structures as well. I mean, from what I understand, many of the structures, like try accept blocks and side effects are supposed to be, are supposed to be somehow compatible with this form. So I think that maybe is like the entry level monad from from what, from what I gather. So then other implementations can be also useful. I'm just going to go and try to implement some other examples from this page and see if I can get it to work here in similar ways this maybe.

Yeah, sure. And so what went wrong? I

just wanted to share it with you and verify whether it made sense what I'm doing here, because I haven't really done this before,

so it's just

Oh yeah, sure, I think so. I mean, as you notice yourself, Metta is uncurried by default, like if you have to carry something, you have to explicitly carry you have to explicitly write a function as it takes one argument and returns a function that takes one argument and so on. So as you're porting the whatever Haskell code you want to metta, maybe you want to carry it explicitly, but,

I mean, it's up to you, but yeah, I don't know how you felt about this

in this process, but yeah,

i i i Yeah, I will not really experience so many problems in this case, but I will keep that advice in mind when I'm looking at those other problems.

Yeah, right, because there are functions that they are easy to generalize when you assume that the function signature is current when it's not, then, well, can be trickier, and that's other things.

And then in the in the same thing. This is just a question I had. This is also an exercise that is provided in the or a question that is provided in the metta lung dot dev documentation. So it's just in the section of recursive types, also here in this parametric types and the question was to provide the type signature of this applied twice function, given the observation that that if you if the types don't match you use, you'd want it to be here empty. So if you had the type of apply, it was just apply. And then, instead of this expression here, you would just have the variable type Y. So you take a function from X to Y right and input value x. And normally, when you apply, you will expect to get y out. And then when running apply twice, it's not always the case, because, of course, the the function has to be applicable to the type of that comes out. So I thought the so the question was, how can you, how can you choose this type in order to, in order to pass this test where we're applying greater than zero on a Boolean doesn't make a lot of sense, but if you just put here, t, y, it will return a boolean here. So I put this in there, but then I had a kind of a natural question that arose, which led me to believe that maybe I'm not really approaching this question in the right thing, which is that types don't have to be equal to be assignable to each other, right? So if you have an integer, you any mapping that works on the float will also work for an integer, right? Because it's like a subset.

Then, yeah, variance is not implemented in metta or nor nor is it really implemented in in her skull, to be honest. But

that is that concept is called variance. Yeah. So that just means that you have to keep in mind that when you are working with overlapping, overlapping so you just

here, so we would be, we'd be talking about a subtype. Ink is a subtype float, thing that generalizes variants.

Well, yeah. So subtyping is in the like, what you see here is what you intuitively expect on the composition is that if the output of your function is less general than your inputs that you can apply it twice, right? So if you go from, let's say, rationals to integers, then you can apply that twice, because you for from the first application get back an integer, and an integer is also a rational, right? So integer is a subtype of rational, so you can feed that into the second application. If it's

the other way around, you cannot do that if you have a function that takes integers and returns rationals. You try apply that twice, then to the second implication, you would try and feed an integer rational to a function that takes an integer and it doesn't know what to do with it. So that's, yeah, it's a pretty important concept, but like you can, you can try and specify subtyping on that, but like, basically the way you wrote it down, like in subtype of floats, that's, well, first of all, that's not correct, and second of all, like the like metta, won't fare well with that, and nor will Haskell Like is a pretty, pretty hard concept to get right.

Yeah, that's my question, that, what is the right notation for this? Because I'm come from set theory, right? And I don't have, I don't write that down. I

based it so I don't know if there is really a standard notation in there's a Wikipedia page where they use the notation that I used in an experiment. I pasted the link on the chat so where? So it's an experiment that uses the backward chainer to do type checking. And so if you use the backward channel, as opposed to rely on the built in type checker of metta, you actually can deal with that sort of situation.

Yeah, so you click on that link here,

all right, and just one more clarification, imagine that this did indicate subtype. I think it was you, Adam, who made a comment. You're supposed to swap them around or

no, they do not bear relation. Integer and floats are are not comparable.

Okay, so

you have, you have Boolean floats, for example, if you have Boolean, boolean is a subtype of integer. So you could, you could do that, but you cannot say integer is a subtype of float.

I said theoretically, that is the intuition.

So you have rationals, or they are called fraction in Python. And so if you have the Python fraction, then you can write that integers are a subtype of fraction, but they are not a subtype of floats.

And you said that boolean is a subtype of int. Is that because boolean is used in the definition of natural numbers or something?

I mean, of course, well, yeah. I mean, in meta, you only have number so if you, if you're, if you start to manipulate integers and floats and stuff and rationals, you have to define them, unless perhaps you can rely on, say, a Python right? Python definitions. But so it would be the the subtyping relationship would be whatever you Well, you say it is, and as long as you have a you can coerce a type into another one well, and it's then it's a subtype.

Well, it has to, it has to adhere to loss, right?

Oh, well, yeah. I mean, so, well, the laws are here. It has to be reflexive, transitive and Contra variant over the input and covariant over the it's there are three laws, and they are in the lane that I and but, right So, and these laws, essentially, they are telling you whether you can coerce a type into another One by say, right, you're you're automatically allowed to coerce if a type is a subtype of another one, you're automatically allowed to coerce into the supertype. That's my understanding. Anyway, I learned on the job when I when I wrote that code. So,

okay, all right. Thank you, everybody for your your very helpful comments.

NO IDEA has any issue to go through, I just would like to use that call as a just to to raise awareness on a an issue which, which I desperately need,

maybe desperate is a little bit too

strong. But pasting the issue and basically the says it all in the title is just, we have double matching. We have evaluation based on double matching full unification in metta by default, and that's great. But if we could decide, if we could choose with using only single matching evaluation, as it is the case in

regular Do you still want to support variables over this like, do you need? Do you want to support single size matching, as in the sense that the the query sites contains variables and the data sites does not? Or do you want single sided matching, but with also variables in the data? Like, well, that's, that's

such a good question. Well, I think, I think I, I would like to have this, to have variables as well in the data, variables everywhere. The difference is that the variables in the data they do not get, they do not how to say, get transformed by the substitution

how like, because the how is the matching them single side. Can I give a brief example, yeah, yeah, but then we can go over that

and, yeah, yeah. Let me. Let me just come up with something, and I have something issue as well. But okay,

can So,

can you see what I'm showing

you?

Yeah, so like, if your left hand let's say your left hand side is a, b, and your right hand side is x, x, and you're doing left hand side biased, single sided matching. Would you expect this to do you expect to match the right hand side with left hand side or not?

Uh, okay, well, so when you say I'm biased, not sure. I'm sure they understand, but I'll give you the single

it's single sided, which means that the left hand side is dominant, right? If you, if you choose the slides, you, if it's you say it's single slide, that you have to choose a slide, and so

dominant in the sense that it is like any specification that it carries will be turned into bindings to the other side. I mean, or is it dominant in even? That is not totally clear to me, but I can show you an example with a function call, which is basically the use case in my situation

where so i

i see you. You've got a function, okay? I hope I'm not gonna mess that up. Just,

just see i

Because, because I, because I have an example ready to go and I and I cannot remember, so, okay, maybe

you can, like, write it on matter most, or the issue, and we can discuss because it's, I'm saying this because it's a very subtle subject. I've been working for like, the past three days, basically, on a new unification algorithm, and also looked at a bunch of pattern matching algorithms, and it's like, yeah, what do you want the behavior to be if you're not doing unification? Because matching against variables is, it is really subtle, especially if you have, if you have constraints, and yeah, that's something we really need a lot of examples for.

Yeah. So okay, I realize that in the issue, I have exactly what I want, but, but okay, but that's that's fine, too, even though, when the practicality this may not be obvious. So it's not obvious. I i can make it obvious by making the issue bigger, but the idea would be okay, so let me just write that. So, so what I suggested is, okay, we have this function, so now it is timely defined with the equal symbol. So it's, it's just traditional metta semantics. So if I run that, I'm gonna get, as a result, I'm going to get

well some, you know, some variable, some new variable,

because, because this thing, so this thing is going to come match against that. Well, yeah, it does unify. We just have to introduce this new variable, and then we call f with this new variable, and we have that. And so now this thing is going to keep on keep on unifying with the thing, right? Because it can still unify with this. And so now it's going to get me, well, it's going to get me again, the same thing,

you know,

another one, and it's going to go on for infinity. If I have the alternative of that, which is I'm able to define f as a single sided matching

evaluation, whatever you have to call it. I'm just going to call that title now

this pain to make a difference. So this thing means single sided, then, okay, I've got the same thing, and it's the exact same definition. The only difference is that now, if I call F on

a variable, I'm not going to get anything.

It doesn't, it doesn't unify, because this thing is, is yeah,

that's indeed, which left, yeah,

that's what I mean.

Yeah, okay.

Why do I want that?

Is that a question? Alexey, no,

the question is, why it shouldn't unify. So What? What? So it's not unification, right? So you mean that you treat, why not as a variable, right?

So I do treat y as a variable. The difference is that this thing is going to refuse to unify, because this variable, it has to be at least as specific as the pattern. If it's more abstract, then well,

what if you have a definition of F, just f s, without variables, should,

right, right? So you're saying, what is none of this, yeah. So, so something else, like, like this, for instance, no,

no, no, you don't execute FA. You have an equality for f s,

oh, I'm not sure you're saying

you have s,

yes. So will it work? Or it will say that S is not general enough. Why? Is not specific enough.

I don't understand the suggestion.

Well, it's not a suggestion, it's a question. So f y will be evaluated to S or not. In this case,

you're saying, if our I see, I see, I see, if I have this, if I have a single sided, such definition, and what's going to happen to that? Yeah, well, I think it's, it will also not unify.

So in this case, you just don't have variables, or you don't treat variables in as a call as variables, right? Or in this case, I don't see in which cases it makes any sense. So you can just replace your variables in the execution, in the expression for evaluation with some smells, right,

right? So you say, if I just build my own variable, and then I I say, Well, yeah, so then I use that, and then it is not going to Yeah. So that's actually what I'm doing. So what I'm doing to work around all these, I have my own variable type, which are actually Deborah and indices and and that's how I escape this problem. But if I, if I had that, if I could define this single sided type of evaluation, then I would not need to introduce those variables, and I would still be able to reduce, because the thing so why I'm using it's really to reduce, I want to use, use that to reduce a program, a metta expression in some normal form. It's for as most

this can be useful in normalization, because you're you're monotonically increasing the information about your free variables instead of where in unification, you can introduce variables.

Yeah, yeah. So I didn't hear what you said at the beginning, but I think what you're saying is that if you have double sided evaluation, then you cannot use it as reduction, because you are you are going to introduce new variables. And I don't want to do that. I want to add structure. I want to, well, okay, yeah, that's what you mean. That's exactly, exactly the point, yeah.

So there are difference like, Unification is one specific join or one specific like, way of combining information on a lattice. There are, like many other ones, and I think it's a good question to ask ourselves, like, what do we want to be supported in reduction, and can we bootstrap it on the reduction that exists? And perhaps that's the case here. Perhaps, like, instead of needing an equals, percentage sign that you have here, you can write it as an equals, which has some function that like transforms your function transform no like on the outside so you have, like a, let's say, single sided matching of that function you had before. Do you want?

If you just can implement a grounded function which replaces metta, variables in the expression to be evaluated with some mock variables, and just run it, and after getting The result back, it makes the opposite conversion. So will it work for you? So it's pretty simple in implementation, but I'm not sure that it is exactly what you need. So it's not like having an single sided pattern matching. It's just Well, well, we can go in different directions for implementation, but in order just to have it, I will this simple, grounded function for such evaluation work.

So I agree with your suggestion, Alex, except that, so how am I going to say that? I So, having a this, this kind of definition, makes it that metta is going to spontaneously. You know, anytime something's going to match this, it's going to trigger. And that's great, and I want to keep that that's the thing, because if I start to to do what you suggest, then I need to to implement my own control. I can't. I can't just say, well, um, because,

well, well, maybe you misunderstood me. You don't need to implement your own control for, uh, or, well, my man, can

I share my screen and implement it? I believe I know what Alexey means. Second, let me share my screen and we can make it really concrete.

Can you see? Yeah,

so you had the definition of predecessor, which takes some successor of a number and returns that number itself. I believe that was it. Then you wanted to have a single sided version of this, and you propose something like this, and was, I think it is that Alex is suggesting that, no, no,

my proposition is actually not to introduce other types of qualities, but just instead of directly evaluating some quality, some function in metta, we just pass the expression to a grounded function which evaluates it in a different way. But, yeah, we can do this so as a type of qualities if we wish. But I'm not sure that It will be simpler. You

Yeah,

I believe here where what you get is some some wrapper that takes your original definition and then translates that into normal function so it runs eagerly, but it now matches on like a more general type, and it's it's processes those bindings and those This generated could then be defined as, for example, like, let me, let me give a brief example. You say that's general rate, it's spelled correctly. Say that's,

yeah,

that of x, that's this, this reduces to x. But then, like, if I have something, if I have like, bar or like, you say, you can even use, you don't need to use actual variables anymore, because generated could introduce that. And then you say, oh, is if, like, this is a variable actually, I want to prune this branch. I want, I don't want to continue reduction on that and so, and what Alexey suggested this unit both forward and backwards. Translation for this if you're replacing the

variable. So you could some do something like, yeah, do this definition and then say, like, replace, replace, x, so to say that introduces the variable again, of course, this, this somewhat breaks composition on the value level, but it would, I believe it would do The logic that's

that you want. Yeah. So, so, yeah, so I, I agree you can do that, but there are just so many situations where, mean, yeah, just just having single sided evaluation, as in a traditional function of programming language. It just makes your code much, much cleaner. Why this is so maybe there's a way to turn this into a macro, something that looks nice. Yeah,

I would spend a lot of energy in like defining that, defining precisely what you want out of the single side, matching and what you expected behavior is, and like, maybe reference like, oh yeah, it should behave like this kind of thing in this language. Because, as I suggested before, there's like, a really subtle, subtle thing. So before we we add that to metta, like, we better be sure what it is.

Yeah. I mean, it would be better if it's added on top of metta, rather than in metta. And I absolutely agree with that. And just,

Oh, why don't you like grounded function?

Um, so, um, I

Okay, I guess I have to. I'm going to think really hard on how to do that on top of metta

and

because I don't have anything against grounded Well, actually, I do have things against grounded functions, but, but maybe that's another issue.

Man,

like, if you need grounded function to complete metta, maybe metta is not expressive enough or something. But

well, you you can write it in metta, I believe, but, okay,

I will try. I will try as hard as I can make something as clean as possible from the user viewpoint. Yet that does what I want. I mean, I think what Adam suggests, where you have something that you remove the template from the function call, and then you deal with that thing inside the body. I mean, it's just that. I mean, that's what I've done so far. I didn't do it necessarily in the most, I would say, generic and user friendly way, but that's what I did. But I just,

I'm still,

I'm still longing for a something that would be much cleaner, that's all out of the box. But, yeah,

because double sided evaluation is so unstandard, it's like I would, I would almost put the question in reverse, like before we use double sided evaluation as the kind of the

core

of metta evaluation system, We have to be to think pretty carefully, because it is completely unstandard. Yeah,

I see what you wrote. Alexey, one side about and T Yeah, I tried that. But the problem is that there's a difference between I mean, maybe there's no difference. Anyways, okay, I get it. I will try harder. Get that thing on top of metta, maybe even using a branded function, if I have to. And then I'll come back to you. Case Closed for now,

well as for non standard things, the idea was to unify metta with the unified rule engine. And the core of unified rule engine is unification. Yeah, yeah.

I totally, I absolutely, totally agree with that, and I, I know, not only respect that, but I love that so, but I'm also missing the traditional functional programming semantics and so on. But Well, see,

in traditional functional programming semantics, you just cannot write the expressions you want to evaluate. So you cannot write f y as an expression for evaluation. It will just give you an compilation here or so,

right? You're right. You're right. I mean, I was actually, yeah, yeah. Man, okay, okay. It's also like my mind is, is also polluted, by the way the Idris type checker works, and the Idris type checker can do that.

It does that at compile time. It doesn't do that at runtime.

And so see some train to reproduce some kind of dependently typed type. Checker, but, you know, on steroid, that's able to do much more. That's why I'm missing that feature, I guess. But, but again, let me try harder, and then we'll see, because maybe there's an elegant solution, and then we don't need to change the code meta, and that would be ideal.

Oh, okay, I still don't think why we hesitate so much to introduce new grounded functions. When it is convenient, in the perfect situation, when the large subset of metta can be compiled, we will prefer to write more stuff in metta. But for now, I just don't introduce this grounded function and remove the blocker for much more. AJ, things you'd like to do instead of combating with current limitations,

yeah, fair enough. Yeah.

So I can imagine how to write such a function in metta, but it will require of car atom and quarter atom and so on, and it will be just too slow, as we just saw. So that's why just writing a grounded function can be a hot fix for the blocker.

Yeah, I see what you're what you're saying. Yeah, that was my concern as well. Okay, I'll, I'll keep that in mind and see what I can come up with. Thank you.

But maybe, indeed, there is some elegant solution in metta without substituting something like watching variables in the expression to be evaluated or whatever. But I believe if you just recursively traverse your expression and quote variables in it, then it will work in a way you want, but it will be just slow

if you do it in metta. All right, yeah, okay, I will explore all that.

Yeah, but maybe in minimal metta with, uh, uh, but no, I think it's still based on unification. So even if you make one step of evaluation, you will still need is some additional tools to Understand that you got something you didn't want. Okay, I

yeah, I mean, it is the one thing that is kind of slightly bothering me is that so full unification is is more expensive than partial unification. And so is it. And of course, you can emulate partial unification with some overhead. And so I am just wondering if the core of the language, I mean that it's probably a stupid concern. I mean, if every every core has these pluses and minuses, it's probably, anyways,

and by by the way, particularly in the course of implementing a sub part of metta in Kotlin. What is being implemented in the first place is the functional part, of course, because it's easier to compile, and if this compiler will absorb larger and larger parts of metta, maybe it will naturally separate the functional code and from unification, and will have unification, not as a core mechanism of evaluating everything, but as an additional mechanism to which we resort in a more controllable way and when early functional evaluation doesn't work. So maybe if we will press it in this direction, your issue will be solved, or your dilemma will be solved in another way.

Yeah, yeah, that's a good point, and that summarizes the right exactly the issue I had in mind.

Yeah. Man, okay.

But anyways, as I said, I'm going to explore really concretely how I can work around that, and

then I'll come back With with what I have. I

Okay, anything else I

uh, Sims now then, uh, see you on a workshop. Or do you have Adam and, yeah,

um, if people still have time, I still wanted to show something. But if there's like, no time left, it's also fine.

How much 10 do you need? Like, five minutes? Yeah, sure.

So what I was actually working on is just translations from C CSV to metta. But of course, there's, like many, many, many options to do that. So let me go to my examples. So as an example, I was just using some CSV documents about customers, and each customer has their index, their ID and their first name and much more. But for the example, this is fine, and so the most easy way to convert that to CSV was where I would just give each row a number and make an atom out of, like, all the information in that row. And yeah, you can translate it back and forth from CSV to metta and back then, if you know that you have like a header, you can use this information to label your header, or even say per customer things like, Oh, my index is one, my customer ID is this, and so on. Or what we did here is in row one, we have

a customer with index one. In row one, we have a customer ID this and so on so on. So these are like four ways in which we try to translate metta to CSV. And my question is mainly searching for some opinions or other ways it would be better translations or, yeah, just looking for that a bit.

Oh, well, there is a number of ways of doing it, and it does a better way depends on whether you will separate your data in space which will contain it. In this case, maybe adding some additional constructors or wrappers is not necessary and may provide some overhead. But if you will put different sources into the same atom space. It would definitely be better to have data constructors with well defined types. This is one point so you will have something like a raw constructor which takes certain types and outputs something which says that it is a well typed expression. Another thing I would like to mention is that currently we don't index grounded data, so if you have strings or integers, then they are not hashed

in the actual implemented that. So, okay, so then it

depends on what atom space or what type of space you're going to use, yeah. So

I specifically, I implemented, like, if types are serializable, and I believe, no, I don't know this vital is here at the moment, but I believe that's still in there. That's like, now, if types are serialized serializable, they are hashed and indexed, which actually, like, speeds up this kind of queries, because what you said really good remark, right? Like the you want to be able to use the index to go to a certain row or to a to or to a certain column, like you want to be able to use that for this. But I do believe that hyper and experimental Now does that on integers and strings, at least because I needed that for the union and intersection operations.

Well, I think this would be very useful, as that would have many practical applications, right? I also got the impression that lot of the modern databases that are in use right now in business that they use column based indexing instead of row based, especially when you dealing with large

amounts of data,

something I was wondering so but, but it all depends on the use case, but you could also represent everything functionally. So, for instance, you would have, you would define a function index, and this function would take a row, and then it would return the value.

So, like a map, like a sorry List map,

basically, no, I mean, no, no, it would just, it would be like you would define the data, as

I would say,

very specialized functions access functions. So you know what?

Yeah, so if you have, for example, your you can say your ID on road to this, like, oh,

so like you

do the category or thing where you you hide internal representation, and you just say, like you have projection functions and injection functions. Okay, yeah, no, that, that's actually a really good suggestion.

Yeah, I like that.

Yeah, I wasn't thinking of category theory, but yeah, I'm sure you can put category theory on that as well. You can.

You can do it on everything. Yeah, you know that, no, yeah,

but yeah. I mean, the concrete example I gave was is first name of rule two is Preston

that I typed you to chat,

yeah? And then you can define the function as whatever you want, like on whatever internal representation you want? Yeah,

you use the type system to define first name, blah, blah, blah, yeah. I

think that's also something that Alexey suggested, where you, like, have a structs in metta and match like, the types to the header so you have, like, well, typed data points.

Yeah, that's actually what I did to represent features AI services on the similar net marketplace. That's exactly how I did but, but I don't even know if that's the right way, even for that application, it's just that I like to go functional by instinct.

Yeah, like one way I was also thinking of, but which I really don't like, is if you just say, like, I have also sort of function, but that says on row one, column two, you have this data point, but it really has no information in it whatsoever, yeah,

like with unification, I think it would, it would play really well like, because you could unify on the index, or you could unify on the data, like, so I actually think that will work well in queries. Or, I don't know if it would be fast, but I believe like, you could, if you have two data points you could say like unify on what this function returns. So I actually like that will allow you to write like joins, or none of you use like the same index or two of these calls, like, you could unify it, like on that and say, like, hey, take them from the same same row, or something. Yes. Actually think like, yes, it would be very mechanical, yeah, but I think it would combine well with meta queries, like with the like comma, match, query,

yeah, cool. Thank

you so much. That's really, really valuable to me.

Glad to help you.

I guess still next time, unless anybody else wants to bring anything up, but we are somewhat over time now,

I want to bring Adam. I want to bring Adam, I wanted to answer regarding your pull request. So basically, met examples that doesn't have this report doesn't have strict rules. So if also of the examples is satisfied with their code, then it's okay for merging. So if you don't have specific questions, then let's just merge it. Okay, yeah, okay, yeah, no, that's

sir.

I think a lot of these are very simple. Like, like, hey, how do you do perfect, perfect numbers in in metta, in Slack. It's very, very straightforward. Like, hey, this is how you use collapse, and this is how you use like, if I'm empty, and this is how you prune branches, like this is, and this is like range with non determinism. So these are very basic concepts put together. So I believe, like, a lot of these stones don't need a lot of, yeah, lot of support. Okay, yeah. Thanks, Alexey,

just question you don't have rights for an origin by yourself. Yeah,

that's correct. Okay, sure.

Is it? Nor sorry, did I listen?

Yeah, I have just not,

okay, awesome, yeah, I see. I see now. Okay, cool, yeah, so this adds a bunch of them, like the like a knowledge graph and this bus and some graph generalization, the strips, which Linda, This is the planning,

planning something,

yes, stack based evaluator and a graph traverser. So, yeah, okay.

Okay, I guess we're good for today.

Yeah, thanks everyone on the workshop.

Bye, thank you. Thank you. Bye,

How accurate was this transcription?

0:00:001:29:03

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5