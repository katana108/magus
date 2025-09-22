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

Nov 15, 2024 at 7:32 am

1 hr 23 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

MeTTa interpreter, Prolog implementation, Metallo development, Sudoku solver, constraint logic, Boolean expression, backward chaining, LSP server, Sparkle queries, optional values, Python integration, TensorFlow graph, computational graph, grounded functions, symbolic functions

## Speakers

Adam (28%), Speaker 1 (17%), Alexey (15%), Speaker 2 (11%), Speaker 3 (11%), Vitaly (10%), Speaker 4 (5%), Vu (2%), Speaker 5 (1%)

It's been five minutes. Matt is still not here, so I don't know, maybe, maybe he's not going to join but, but we can start the call nonetheless. Well, so on my side, I do have questions, but I don't want to take too much place, so maybe I'll let first, anybody else go ahead and if nobody has anything, well, maybe I'll go but yeah, Please anyone go ahead. If you have any issue, I

like, don't hesitate. I mean,

well, if really nobody has anything, I

do you have something Renee,

well, I just few. I don't know the name exactly. He wrote a Prolog interpreter in the MeTTa language, and I've tried to install that that I couldn't get it running yet. But that's how, basically, he wrote a very nice library, but I can't, cannot run it yet.

How is it distributed.

He posted it on the on the MeTTa mouse,

where image channel,

on the Metallo development channel.

But maybe, maybe his code was just a sketch, but it's not maybe it's not valid code, but the idea is very nice.

I don't see a MeTTa log development channel only. Metallo. Is it because so is it Metallo? Or is it another one?

Oh, it should be Metallo development.

I Are you sure it's in matter most?

No, if we are in matter most, we have knowledge graphs, MeTTa College, MeTTa study grid, MeTTa lobe, and below that there is Metallo development.

That's odd. I can't find it. I mean,

yeah, you too.

Maybe it's a could it be a private channel? And I can't even see that there's a private channel or something.

I tried to, I copy the original text now I can try to repost it right now. Maybe there's a repost option forward, but then to which you know,

I know I now have just pushed the forward button. I in the meta log development channel.

But where did you forwarded it from? Channel I

forwarded from inside the Metallo channel. I will now try to go to Metallo channel because, in general, I only visit the Metallo development channel, because if I visit all the channels, I I get a bit I get a bit afraid.

It is, it is overwhelming, indeed.

Yes, I posted now in the meta log channel. Okay. So that's an implementation of Prolog in the MeTTa language, but you you cannot compile it because the code is not valid MeTTa. Well, maybe I make a made a mistake.

Because if you can use it, you could write Prolog programs.

It looks similar to my background. Yes, I have to look more carefully, but,

well, not identical, but I

in the if you The person who wrote it, He is also present. I

and at the moment, I'm trying to make a sudo MeTTa program so Douglas gave me the task to very normal task with the

and I chose the right now. I chose the breath first approach for to make it to solve the Sudoku, and in my opinion, it could work, but maybe I'm not overseeing all the things that I might get stuck, but I think it could be solved with breath. Breath first.

Sudoku should be solved with sort of constraint logic programming, or something like this, which Adam actually posted a link to. So do you think it makes sense to try solving sorocov with brute force approach

is because you I can't use the constraint logic library, so it has to be without I

and I searched on the internet, and I found I did find directly other persons with the Same with the same question. They say, Well, what about if you want to do Sudoku, but without the constraint logic library, you have to invent something else.

But I'm still in the process of completing it. Eventually I will get it work, because the search space is not that, not that big, and I can always strip out possible candidates

that looks interesting. I like the the base case includes various, various cases, including evaluating a Boolean expression. And I wonder, how do you delay the the evaluation of the expression, until you can, I mean, because right now,

so I'm talking about the line 17 in five fold, Dash. BC, dot, MeTTa, you've got the case bull, exp, and well, if exp go otherwise empty, but, but in some situations, you're not going to want to evaluate expression just yet. You want to weigh that. For instance, you have more more bindings and and I wonder how that's going to be dealt with. Yes,

and few Lee, do you know the answer? I

I haven't really thought about it, but I think if we follow the order of the Although, when I wrote it, I assume that when we reach that goal, then the biting would be available to be evaluated. So it's like the order of the predicate in a in a body of the in a typical horn cause. So it will be organized in a way that when the when we are trying to backward chain on that predicate, then the biting has to be available, at least for the Boolean expression.

Okay, yeah, I think it's a very nice code, but I try to compile it with our MeTTa interpreter, but I couldn't not get to get it running yet.

I do you mean metal interpreter, yes.

So which, which file Did you run?

You posted three files. Oh, yeah, so and I copied all, I copied all the three in one file. And then I I commented out the import lines. And it does, actually it, it takes in nicely, the whole file without complaining. But Metallo never complains. But as soon as I try to write, to try to execute some go I, I do not have any answers yet, but maybe, maybe I make some, made some mistakes. But should, do you think it should run already? They should test it. Have you tested it?

I tried it both on hybrid and MeTTa law, so, and it did run. Okay, so I will, I think I will check you with check with you later on, how you run it?

Yes, I will try. I thought maybe it was only very rough code. But so you say it should run,

yep. So what I did was I just, I just run the query file, which is in the F, o, l, dash, b, c, dot test MeTTa,

so yeah,

view see if you sorry if I mispronouncing your name. Is it that view or view, Lee, or

Yeah.

Vu is fine. Vu, okay.

Vu, so, yeah. So I pasted a the the URL of the some example, and I would say that if you replace, so if you, if you replace that query by swapping the the other of the variables, of course, then you don't use three. You use, I don't know six, for instance, some x6 then it's not well, I predict that it's not going to work. And yeah, because the order is, is then going, Well, yeah, there's going to be this issue that was describing. So if you encounter that issue, that issue, and you have generic solution for Atem, I am very interested. So let me, let me paste a hyper on experimental GitHub issue that describes that same issue, and that way you could participate, if you, if you happen to, if you have a solution for it, or or even just some ideas, let me, let me find URL and paste it.

Okay, okay,

I got it, so let me paste that.

Actually, actually, I built my chaining based on your experiment. So okay,

yeah, so I pasted the issue and you may read it whenever you get a chance, and and I believe MeTTa log is able to address this issue. Of course, I would prefer to have a way that's compatible across all MeTTa back ends, but if I can't make one, well, we still got Netta on,

okay? Thank you.

Yes, I could. I have been able to run the code by but with all the all the executions, I get empty list. But do I miss the knowledge base, or is the knowledge base is in one of the three files,

it's supposed to be imported, but

it's supposed to be imported, but it's not standing

Well, actually It is in one of these files, I believe, has a KB postings,

KB MeTTa, microphones,

there is a long silence. Does that mean we are moving on to another issue? Or it's just that some parties are just trying to look for running the thing?

Yes, yeah, probably, well, it's a bit difficult, maybe to run it inside the meeting, but

let me move on to my issue. It's it's going to be even more difficult. So I don't know,

but I don't see your post,

right? My Oh, man, I when I say my issue, I don't mean I pasted a GitHub issue, but that's something else i My My issue is that I'm trying to run the LSB server of meta log and, and I'm failing and, but I don't know if anybody can help me. It's under Emacs, but I did find the various buffers containing the various log messages on the presumably the EMAC side and LSP server side, so I could show that, but I also pasted a small sample of it. Okay. This morning, okay?

And we always channel

metal, Metallo, okay. Now there is essentially, well, yeah, it's kind of, it's within a thread. So you're not going to see it

about, about the LSP Roy or Douglas, they will definitely know it, because they they've been building that LSP in in the past weeks.

Yeah, yeah. So, yeah, I expected that it's, it's, it should be addressed to Roy or Douglas, but they're not here in this call. So yeah, so, I mean, I guess, yeah, I feel it's probably more adequate to go to another issue.

Yeah. So if anybody has another issue or please feel free to go ahead. I

or something cool you'd like to demo, or or anything.

I have some stuff to show if

you're interested. Okay,

I was playing around with a sparkle like the query language, and trying to translate some stuff of that into MeTTa. And the idea was to eventually auto translate it to MeTTa. But it is harder than I thought it would be, because most of the sparkle queries are not that hard to translate to MeTTa, but if you want to consistently translate them in a way that you could, like, automatically do it. It gets a bit hard. And maybe one thing I can show you is, like, one of the more hard things about it, let me share my screen, And that is that you have like these optional values. Can I

make this bigger?

Yeah, so year above, you have a sparkle query, and what it says is, we are looking for a person and his name is optional, so either we defined it as name or as fn from first name, and these values that we want to return are not required. But what you have with a match statement is, of course, if it cannot find a match, it gets empty. So I found different ways to kind of hack around this issue, but I think it's not very

elegant. I uh,

one of the things I came up with is, yeah, just like putting a collapse around your match, because then if it's empty,

it's like an empty thing. So you can compare it with empty, and it does not disappear. And that works. I also try the same thing, but then using, let's to, like, assign a variable to a collapse,

but it's it's not the most elegant. And like I said, it gets like, a little bit tricky if you want to Auto Translate stuff, because, yeah, you encounter a lot of edge cases. But yeah, that's what I'm up to. If you're interested, I can show more translations, but that's basically the thing.

Maybe it will be nice to rise an issue in MeTTa. Example, we already have a few issues regarding spark queries. And we also encountered, we are encountering some edge cases with, for example, Duong, tech, logic implementation, amen, MeTTa, or translating its implementation from sparkle language, or something like this, so you can supplement this issues with your own. So please put the description everything you are showing right now on your screen, or maybe something in addition,

yeah, I'm still trying to figure out how your code works. So my, my current incomplete understanding is initial so you so I'm looking at the first match, the first match query on the left. And so first you test, well, do you have just a name, right? Because it's optional. Okay, so if you don't have just the name, you say, Well, do you have just a Fn, I don't know what that is. First Name, whatever that is. And then in the end, so okay, and then in the NUS for the name. My first observation is that instead of using collapse and comparing with collapse empty, you can probably wrap the match in a case, you would do case match, etc, and then I think you have in the case you can use empty. You can use the like it, I think it's return that empty, and then, yeah, MeTTa will understand that. It means that the result of the match should be empty. In order to to take that branch, I would be slightly more elegant, I suppose, and otherwise I don't really then use chain. Yeah, I've never used chain, so I'm

actually it's the same as let's, but then your arguments are in different order. I think it's basically the same in let you say, let this variable be this thing after it, and which chain you say, I take this thing and I assign it to this variable, so it's basically the same, I think correct me if I'm wrong, but

you also can I use like as an addition to what nil said? Instead of case, you can use UniFi, which behaves like a match with empty branch. So you can specify the result when result is empty.

I think I've tried to use unified but I was struggling with it, but I cannot remember why, so I'll look into that again. I

It seems that the left Lowy can be replaced by two unified distance like this,

or maybe like this.

The three queries here do the same thing. I was just experimenting with different ways to put it in the hope that one of them would be easier to automate. But the auto translation is very tricky. I

uh, well, anyway, she said it makes sense to raise an issue and explains the task, you know, to solve. And yeah, it will be simple to understand what happens which has Aquarius difficult, and also it,

yeah, cool. Well, I'll do that.

Yes, sir. Well, I'm not familiar with the spark URL or, well, nearly not. And so optional means, okay, well, of course it means it's, I mean, in this context, is either one. So either you get name via both name, or you get named by a V card, F name, it's got to be, I mean, since you select the name, it's gotta be one of the two. And so I guess this is the idea you're trying to capture here in your MeTTa translation. Yeah, right,

yeah. So I think I have better examples of optional like this is a little bit of an easier example, where you say, either I want a name and an age, but I only want the age

if, if

there is an age. So you see, like your result has to be like you want to return Mary with your age, but Bob doesn't have an age, but you still want to return Bob, just without his age. So that's the idea behind optional.

Okay, interesting, of course, I can't help but wonder how I would do that with the backward channel, yeah,

actually say, I mean, at the very beginning, we discussed query language for the atoms places which can, which could be implemented for MeTTa and yeah, primarily, for example, is one of those fishes which could be embedded into the equivalent which is also in

it still can be prevented phrases.

So I'm not sure, but maybe does have Some something like this in the quiz I

well, I don't think does has optionals, so it may have some additional primitives of the query language, but I didn't see optionals there. Yeah,

so

the way I would do that with the backward channel. It looks a little bit like zoom did meaning I would encode in the backward channel, just some cases for dealing with a with the default. I mean, it's it, I like, I don't know how relevant that's for you, but because it's pretty much what you're doing. So,

yeah, it's,

it's essentially what you're doing.

Yeah. And then I had, like, I remember I had one example which was similar to this one, but the difference was that, can you see my cursor? By the way? Yeah, okay, yeah. So what you do here in the match statement is you only return your age, or maybe with a chain. Example, it's a bit easier. Like what you return here is your age, and you put it in the variable and one, and I had something similar. But then instead of returning the H, I wanted to return two things, and then here, assign them to two variables. And that works perfectly without a collapse. But if you want to add the collapse for the empty case, it does not work anymore. So, but I have not written it out. Now, maybe I should write it out, because I always looking for a solution on that. I

Uh, but yeah, maybe I should just write it out and send it on measure most or something, with the question,

but because, because Bob doesn't have it, Bob doesn't have an age, and therefore it doesn't return anything. Or does it return partial result? Yeah, it should return a partial result, but it doesn't return anything.

This one, if you run these queries, it returns the results that's here on the bottom. Normally,

okay,

yes, but if you leave out the collapse, if you make the normal statement, it doesn't return anything.

Yes, it only returns Mary, if you leave that out, okay?

Yes, normally MeTTa should be very permissive, but it depends if you do not specify any types.

I mean, you can try to replace chain by by, oh, you probably need to. It's better. It's probably simple like, so it should be okay. I will put up the type in the chat.

I see in the chat with a with a not find I believe I've also needed to do that some time in the past. So that's failure to unify, that failure to unify branch, which you can also put variables in. Yeah,

okay, I'm not sure about braces, but the idea should be clear,

yeah, because then in these queries, I guess I can also try to do with a case statement instead of the collapse here or

are, would a unify?

I mean, in this case, it's probably issues chain, not with something else. So you can replace chain by wet, actually, okay. To to do it, probably you need to swap both arguments, so variable should be the first arguments, and myself personally change query and some results as chin. So it should four, yeah,

let and then

change this. Okay, sorry, probably okay, you can try it. So I thought about one problem with chin, but it's, it's actually, maybe it's not. You can try it, but, yeah, I'm sure it will work.

So Did I understand correctly? Like that, this query does work, but it's hard to generalize because of the collapse.

Yeah, yeah, it is.

So yeah, you need a way to like these strict spaces, basically, yeah, and

especially, but there were a lot of problems in why these queries were hard to automate. But yeah, one that I had was if you have like, a similar query, but for example, here, you want to return like, person, and age like that, and yeah, you have here like an n1 and a n2 that works perfectly without the collapse. But then, of course, you don't get your empty results. But if you do a collapse, then it does not work anymore. Well,

perhaps with the case this,

yeah, I'm gonna try to clear out.

Oh, I guess.

Oh, actually, I posted the new version the chat, so it should work. So unified from which it should work in all cases,

I'll check that out.

Well, yeah, that were my questions. So

if nobody has anything to add, we can move on to the next questions. I think I

I have some high level questions, perhaps some folks here have thought, some I've been trying to do a couple of bindings of the following form, you have a large framework. Say you think about TensorFlow. Think about clingo, some large C Plus Plus framework, or press framework, whatever the mode of interaction, I envision is that you fill up a space with a description of your program. So in TensorFlow, this would be your computational graph. In lingo, this would be your ASP program. And you call the function like the granite function. This does have a computation, and then it returns to you another space, and this space you can investigate for the results. So in the case of TensorFlow, you can look at what were the results here, or what was the accuracy of my training run, or what have you. And in the case of clingo, you can inspect, oh, for this stable model. These are the variable assignments and on a high level, that makes sense to me, and the problems arise with constructing these program spaces, because it seems that you either need to define a completely custom format that's native to MeTTa for the program definitions. Or you need to grant a ton of for instance, to be able to construct the program in that representation. So concrete, for example, would be if you have a TensorFlow program at the which is like a control flow graph, and you add a note to that you don't do that manual, right? You write an if statement generator or a while loop generator, and it seems like all of these tensions would need to be ported to to be able to write this definition in sync with the framework. Same thing with with clinger. Well, you could write or like come up with a custom syntax, or custom not syntax, I guess, but a custom as expression formats for writing clinger programs. This has a lot of some surface area, so you you need to do the custom translation to the C Plus Plus API, or you need to expose some manipulation operations to MeTTa, which makes it a lot less transparent, and a lot of work in in the case of these big frameworks. So any thoughts on that would be appreciated. Yeah,

I understand the question. So, yeah,

so I see that in the case of TensorFlow, this graph construction language is a sort of DSL. But how does it apply to MeTTa,

yeah, so let me share my screen real quick. I don't have the examples on this computer, but I can spin up one quickly enough I believe.

Can you see my screen? I

Yep, so you would like to have something of the form like TF, run session with my session handler which was previously bind, or you can say that We also included this new session with my program.

And

right? And so my program, let's say that it looks something like this.

I

have a I want to create like a. I want to ask like a, sign, X, to range of some arguments. Let's make this a an argument to this to the program too. Stop. I want to assign. And let's, yeah, this all takes more arguments, but let's for now. I

does range return a superposition? Sorry, range returns a superposition.

No, sorry, this is just like, like, let's Skype this.

Oh, yeah, okay, I see, well, since I don't know, it's a flow, right,

this is a program definition, right? And this so we can, we can run this with parameters that we like,

right? And so while intuitively, this maps to some Python program that creates the inner product of a range and a constant factor of, I guess this would also have some spot. While intuitively that does the thing in in practice, it's, it's very, very hard to map these, because this is its own language, and nobody described this language like this is, this is something from like true to MeTTa, and TensorFlow does have an intermediate language, but it is so for both, and it's not meant to be constricted manually, so it's not even stable for outside use. So this would be kind of my dream interface, but there seems to be no way to actually do that. Does that make sense?

I don't know TensorFlow, so it's difficult for me to make complete sense of it. But x, y, z, mean this way of doing these assignment is to create a graph, right? Information flow.

That's why what TensorFlow does internally, yes, great, great. Well,

just thought I would write like I define a sign and other parts of this MeTTa representation of it was a full language. In Python to generate Python, for example, I mean, if you want to run Python, there's a following so like different session, gets the program from my program function, it actually reads this program and gets the Python program, which represents the fall I we just program and then else this program and Python interpreter, something like this, I'm not sure, maybe other so you also explain it why it is Not possible.

So the this, so if I replace, if I replace this thing with a like 600 line file, and I then do something stupid like this, then I can actually make it work. The problem is more that these functions, like they are, they seem to be only defined in like Python and C Plus Plus and the mapping of how they go through the to the intermediate representation of the control flow graph like that. They have no obligation to make that accessible and well, they didn't make it accessible at all. So it's very hard to like I cannot write any MeTTa function I cannot. There is like, no definition for like, let's go. It's TFSI, right.

There is no definition that I could paste here that would do the writing. That's one problem. And then the other problem is that for functions like this in Python, they actually, you can actually write something very close to this, but they have tons of default arguments and they have, uh, yeah, this is very complex. And to make matters worse, it's there are, like, about 600 of these functions in TensorFlow. So even if you like, can do all of these, then it's still, it's still a ton of work to be able to make that, make that, make that do the writing,

Okay, several issues, as far as I can understand. But data. One of them is inter probability of Python and MeTTa, and we have pi dot operation, which, and pi object which can be used to access arbitrary Python modules and functions and objects within them, and there is a possibility to pass key value arguments to this function so you don't necessarily need full argument list or to have a wrapper to provide you the possibility to have only a few arguments. But of course, using PI, dot and py object, grounded functions will not provide you descriptions in MeTTa. And yes, MeTTa type system doesn't support optional arguments, so there is currently no way to completely fix this issue, but in general, You can write a sort of DSL which will translate which code will be translated to Python using Python pi value. But the second part is that one may want to have some code was in MeTTa and in the grounded form. And this was actually the initial idea. We are not still there, but if we consider compilation or some sort of approximation with neural networks or complex functions, then there is actually no hard border between pure symbolic functions and grounded functions, because when we compile the existing MeTTa code, we get grounded versions of MeTTa functions. And when we proceed in this direction and add, possibly somewhere in the future, for sort of super compilation or amortized inference or whatever, then we will need to have both symbolic and grounded versions of functions simultaneously and to be able to use them simultaneously, and this should work, not only for compilation of functions defined in MeTTa, but also in the opposite way, when we embed some functions, foreign objects, Some grounded functions for from other languages, we may want to construct some symbolic descriptions for them in MeTTa with some constraints or equality so type definitions and as a question, If it can be done automatically. In some cases, probably yes, if they described quite well in the language from which they are borrowed, but maybe not in the general case. So I think some part of the set of issues you described will be solved. Hopefully, some of them maybe are solvable already, but others will be solved, hopefully in the future, maybe not all of them.

Yeah, let me thanks. Thanks. Alexey, so one of the things I would like to end on here is that the TensorFlow and to some extent, Jackson pytorch To what do they? They do not use Python function calls directly. So if you write something like it, so like the first thing example, this is Python, right then, if you write in Python like R is range, something like this. Then what? What normally happens in Python is this function gets called, this range gets created and assigned to R. But if you call this in TensorFlow, what happens is that this is actually not evaluated, is just compiled to this program graph, so we cannot like so saying something like we can do

like by

sign, okay, so do you want to construct some sort of graphs in MeTTa before evaluating all the grounded functions?

Well, what I'm trying to say is that the this doesn't boil down to like, by the Ask range, that that doesn't work because the Python code is not or it's not executed to it doesn't execute the functions to to construct a graph, which that we would be able to do in MeTTa with with some with quite a lot of work of doing the findings. But what happens is that this code is directly translated into like a TensorFlow graph, which has like, oh, variable assign and then some huge structure describing, describing what happens here, right?

Well, actually, do we mean that?

Sorry. Well, you can do this MeTTa, right? So you can construct a graph for some sort of DSL and just write an interpreter for as this graph, for example, why I can convert in its nodes to Python objects using pi dot and py object operations. So

this is internal. This is internal to

well, or is your problem that you don't have access to internal representation of TensorFlow,

yeah, so let's indeed define it a bit better. So my function,

and then what happens is this is actually equivalent to

and this thing. This is a whole compiler. So my function is never executed like my function is compiled by the TensorFlow compiler into the graph, the computational graph and the computational graph. Well we can, and I've made something along these lines work, while we can like, do this, and then I can do like. I can this is what I got, working right graph. And then I can do something like two JSON, and I can take this JSON right, and I can embed it into MeTTa, and then I can sense that Jason to the grounded

function that I have here, and and that works, but what I cannot do is write MeTTa or Python functions that construct this graph directly, because this graph format is internal to a large degree. So indeed, if I, if the, if the problem was executing the Python code, I could or, like, say, you have this, then I could just do, like, I binds, TF, dot range. It's like MeTTa range, but, but that that doesn't work because, yeah, this is the this is what actually happens. A compiler is run on the source codes, on the Python source codes.

Well, if the only thing you can use to create a graph result, it's a Python code that we need to generate the Python code.

Yeah, I'm thinking how much like of these Python features are isolated versus not? If they are isolated, then, yeah, like the MeTTa codes can generate the Python codes that can then be compiled. That's that's fair. However, if you have some, I don't know how that works. If you have something like plus my model, and then I

right? I don't know. I didn't know how that will be like, but possibly we don't need it. But I'm not sure how you import things into that scope, or even even something simpler, like import 10s of flow, dot probability. That's

even something like this. It's, How do you know in in MeTTa, what the modules are of TensorFlow, right? How do you know how to translate the meta name to the Python name that corresponds with the correct function, and we aren't even talking about types yet, or the the arguments contract. Well,

I'm thinking about something like MeTTa library to generate Python programs like, you know, so each which can generate the Python syntax, and then you don't need to encode some specific library name to this. You can use it as an amen to the generator, but I'm not sure. Okay, so this solution seems ugly, but should work at least.

Yeah, I would say that pi dot and pi object cover maybe half of it, maybe a little bit less. And maybe we indeed need some basic primitives. Which will also allow you defining classes or functions.

Yeah, we can take this up in our time, but, but I believe it's an important thing to figure out at some points. All right, thanks.

Last question, I'm not actually really familiar with stanza for doing the zone input of the TensorFlow is Python or probably not. Sorry,

can you repeat your question?

I mean, use the Python code the only input to the TensorFlow to generate the graph, probably not you can. It

is a it is the only inputs when you use it from Python. So, there used to be so this is in TensorFlow. Two, this is the only option intensive flow. One, you could do some things to the graph manually. And in C plus you can still do some things to the graph too. So the the the other option I looked into today was, can we write C Plus Plus bindings for Mark, or can we write risk bindings for for TensorFlow, but both of them, these are, yeah, non trivial, non trivial tasks to be able to call the graph functions more directly. So to answer your question, this implicitly TF dot function also implicitly takes, like a library of methods, which it makes it a bit harder to do this from from MeTTa code still, Because the library of MeTTa contains, like, all the the C Plus Plus and CUDA and like, Yeah, from the CPU to the GPU routines, it says, like, what names corresponds to what routines. So it's also important piece of information, but it's not. It's internal to the frameworks, and nobody like took care to actually define this or to expose it so we can use it for MeTTa.

Well, actually, it seems like it's quite close to compiling MeTTa to Python, about which I had been thinking before we started working on the Kotlin based compiler. But yeah, there are some use cases so where it would really be nice to write a function definition and MeTTa and be able to transform it to the Python function definition in order to for some Python library like TensorFlow, to take it and use for some subsequent procession. Yeah, it's an interesting case, so maybe we need to return to this ideas of, sort of translating MeTTa to Python. It also will provide a sort of a way for construction grounded functions from MeTTa descriptions. So

okay, okay, cool, thank you.

Okay, so Well, I think we, we could end the call by now, yeah, so let me wish you a nice weekend and thank you all for your engagement. Bye, bye, thank you. Thank you. Bye, Bye. You

How accurate was this transcription?

0:00:001:23:21

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5