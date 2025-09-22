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

![](https://profile.otter.ai/AM6J7HM7YYN7HRX2/AM6J7HM7YYN7HXIW)Daniel Svoboda

May 30 at 9:00 am

1 hr 25 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa code, inference control, delayed call, estimate delayed call, non-determinism, reasoning engine, backward channel, minimal MeTTa, execution keys, priority instructions, probabilistic programming, functional body parts, evaluation traces, user-programmable, parallelization.

## Speakers

Nil (62%), Vitaly (20%), Alexey (17%), Patrick (1%), Speaker 1 (<1%)

Hello,

hello,

Hello, Hi,

Hi, Charlie, Hi,

no, that is here. I'm

someone at Google needs to implement the feature of separating the bots from the humans in the in the list of participants that would be easier to Get an idea. Yeah.

Who is the wife? Right?

I mean, we might as

well start. I suppose

I'm gonna have to leave early so I

Any issues questions? I

No, you usually have something. I do not have any question. Um, if nobody has any question or anything to show, I do have some interesting code to show, I think, but I would rather do that in less resort, because I think it's better to to give the room to anyone who has a was A problem to solve, or where we could help.

We need to calm down. Nine, eight.

I wonder if anyone got Mark to work, like to run the MeTTa code, because I managed to build mark, but there is not a commendation of like how to run a meta file. Well, I'm not sure if anybody from work team here, but my understanding is that you can't run, I mean, you can't run me up a code using more CRR, right now, right? You only can load your meta expressions into Mork and use it as an atom space. Also can run minimal method to command which is not MeTTa or minimal MeTTa. It's just one, one universal instruction. So public, I'm not sure. Is your question like, how do you how can you load data into the morph and queried? Or it is about execution or evaluation of expressions. I guess how to run a minimum MeTTa, top minimum. You mean, how to run minimum MeTTa, two. Okay, actually, I'm not 100% sure what Adam demonstrated to us in Dubai is right. You You can run work as a server, then connect via HTTP and send HTTP request should be GET request, probably with a specific comment, Adam, demonstrate. I mean, I saw only demonstration of the query, sending a query to server. I'm not sure about the moment to instruction. Maybe it should be, yeah,

I'll just take a look@simple.rs file in as a repository. It contains a bunch of queries you can do. And

repository, I'm not look seeing a minimal MeTTa to repository.

And look to the file so there is a bunch of tests, and they seems to cover what they have right now, I made a wrapper in hyper on experimental to some of the queries, maybe not all of them. And there is indeed a number of minimal MeTTa instructions so you can i But the server, basically, I stopped making the wrapper to other comments to The server, because it turned out that it is not fully functional in terms, for example, unification. So if you pass as the same variable in one query, then it ignores so that the variable is the same. They say that such unification should work in the core, but as a server just incomplete. In any case, if you are interested, you can take a look at this simple.rs file and see what can be done. There are actually definitions. You can use, def, for example, to provide some low level instructions. There is actually three operations there. So it's possible to do something with the server already, and if you wish, we can extend this wrapper in the hyper on experimental to make calls to this server from MeTTa.

Thank you. Yes, I guess, I guess I thought that maybe minimal matter is its own meta execution engine. But maybe it's not yet, or maybe it's not,

I'm not sure if they have a sort of command line tools or Apple for it yet. It's definitely there is a core implementation in rust. So I guess if you don't want to use a shower, you can directly use a minimal method to interpreter from rust. But it's indeed better to ask Luke and Adam

Mm, well, yeah, Adam said that he did experiment. He experimented with implementing minimal meta on the top of minimal method too, and like then he was able to run MeTTa examples using minimal MeTTa interpreters, something like this. But I'm not sure, like he never mentioned he shared this code, so probably it was just experiment, but you can Ask him also to share the minimum MeTTa interpreter.

You okay, are you? Are you invited into the workshop? Probably should be, I think, a mentor. Okay, so, yeah, it's best place to ask questions. I beg. I'm in the Baltimore.

Okay?

Well, yeah, one, one

way, center link to a initial Mark wrapper so it contains clean code for Colleen Mark server no is then is This simple.rs file, which is a little bit cryptic. So

sorry,

no, actually, I just wanted to say that you can share the I mean, we can say as an example of a usage More permitted, so you just said it is Not i

Since more people have been joining me, it's just reiterating the question, anybody has any pending issues? Need some help? Please feel Free to to Ask anything i

So, as I said, I have something that could be of interest to show, but as I also say that I would rather. I would rather use that time if really nobody has anything, because I think it's more important to help anybody who needs help, and to me to have me show show my stuff.

I'm not hearing any takers, so maybe you should just go ahead. Nil, all right, I

so what I'm going to show you is the code I'm writing to to do inference control. And I'm not going to walk you through the entire code, because it would take more time than the than this call offers. But there are a few things which I think are generally interesting. Maybe that minimal MeTTa two will render obsolete, but nonetheless I'm I'm going to share them and and wow. Well, yeah, we'll see if there's value there. But Okay, so in the context of MeTTa, what I mean by inference control? Well, in my case, it's going to be controlling the non determinism of a reasoning engine. But in the context of manage, really, we have a function, and these functions has multiple branches. We have that sort of function. And spoiler alerts, my reasoning engine is taking advantage of the non determinism that met MeTTa offers. And the way works is that it's not just that, say the function foo has three possible entries, is that when you enter one of the entries of foo down the line, you're going to have a recursive call over foo. And so this thing, and when you, when you arrive here, you again, have three possible entries. And so that's how, that's how you have the you kind of create the search space that the reasoning engine is is exploring. And so by inference control, or we could call that reduction control in general, if we don't want to to worry about reasoning and inference, but just interpreting some code that has non determinism in it. Instead of taking all the path, did you reach some kind of termination? Did you reach the leaves of your function calls? Instead of taking all these path, you want to take, say, one or two or a few. You don't want to take you want to take them all. And the way I have done that is that instead of having the code, instead of having the code, which is run right away. So let's say it enters foo and it runs body right away. Instead it returns an evaluation of how good is this body for the intended purpose. So it is going to evaluate these

three calls in parallel, but instead of outputting the result of running the body, it is going to return the code that should be run, plus an evaluation of that code. So it's going to look something like

sales score, okay, it's like, this, this body is going to be point six, and then it's going to run. This one is going to say, Well, this one is point five, and this one is and two, and it's going to say, Okay, well, I should run body one, because it has the highest score. And so in this way, instead of running, instead of generating, this can be natural explosion by taking all the possible path in a recursive manner it is going to take, it is going to take one path here, and then when it has decided to take this path only, then it's going to run body One, and then body one is going to run again. The same code here is going to enter the three possible entries of foo, and then it is going to provide again the same well now maybe in this recursive call, body one only has a score of point one and and this time, let's say body two gets the highest score. So okay, so you kind of do that with the three bodies, and he's going to choose body two, and so on, until it reads a termination condition. And right? So that's, that's really, that's what my code is doing. And I don't have time to tell you how these are evaluated, but I just want to show you how I emulate this, this thing that's all because I think it's generally useful at this when you try to do that in pure meta, it's useful now with minimal MeTTa two, maybe it's not going to be useful anymore. But anyways, maybe the idea is still useful. It's a simple idea, really. So what do I have? I have a data structure that I call D call, that stands for delayed call, that allows me to hold a function call without running it. So I have that for various arities, and I have my constructor to construct, such as delayed call and and here I have some method to run, delete the delayed call. For instance, this thing is going to run a nullary function that is being hold, being held in the D call, type, etc. Here are some examples. So I have some functions, who is nullary bar is unary etc, at that until, like a grinary function. And so I can, I can create a decoy object. So for instance, I I pass the function foo in the D call constructor to build a nullary D call, and then I can run this function and I obtain the the output of my function. So I can do that with various areas. So of course, to again, the the idea is, instead of calling here carts right away, as I'm as I'm building it well I'm, I'm wrapping that around a make the call constructor, and then I can do whatever I want with this thing, I can pass it around, and whenever I wish to run it, then I can run it with a D call, dot, rent, recall, okay, and so once I have that, I Define an ED call type, which stands for estimate delayed call, which is about the same as a D call, but it has a an additional parameter, which is a which can be understood as an estimate, which is going to provide a measurement of how good is the call, and so it's really the same thing. I mean, I Well, so this is our various functions to compare the calls. And I think I just want to jump straight to a something that's more interesting, right? So I can, I can then compare the calls, well, Ed calls, meaning they contain an estimate. So for instance, here I have two Ed calls. One is rated with an estimate of point nine, and the other is rated with the estimate of point eight. And so I can, I can call this max with function, and I pass, I pass the less than function, which going to work on Ed calls, and that way I know that this Ed call is going to be selected. So, so the this, these are the thing is going to allow me to, when I gave the example with the three possible entries of foo to select the the entry that has the highest estimate.

And so, right, so I do that and and then let me show you how I use that in my code. So, so, okay, I'm jumping over all this because it's more the logic itself, rather than the inference control. So I'd like to just go straight to the inference control. Now let me, let me look for that.

I think

probably

going to be in case i It's

that's, you see?

So,

I remember,

I think that it's really here,

um,

right? So that's my backward chair. All those who do not know what that is, it's a it's a reasoning engine that can go backwards. So I give a I can give a goal, something I want to prove, for instance, and it's going to be able to go backward from the goal, say the theorem to the axioms. Okay, and the. So, this is how I run my backward channel with inference control. So how does it work. The thing is, here I have a backward chain chaining.

Thing is going to be like the backward channel. But with the instead of returning the body, it's going to return an estimate of the body. So it's it's going to be like foo, but I call it, we would add an a little e at the end to say estimate. So I would have when, instead of returning the body directly, it would return an ED call of the body and a score on use the constructor, a score and a body, etc. And so these things, these BC, BCE, is what it's doing. It's my it's my backward channel. But instead of returning a body, it returns an ED call. And the thing here, where, where I evaluate, the, the, the the estimate of a particular branch. This is where the magic is happening, but, but I don't have time to to explain that. But anyways, then it's returning just the good old recursion that the backward channel needs. And so, right? And so, once I do that, I get all the branches of the backward channel. And then, okay, I put that in a list, and then I take the maximum according to I want the the ED call that maximizes, the that has the maximum estimate in the list of all possible branches. I take the maximum one, and then I run it, it's here. And so that, that's my way of like, running the recursion that that had the maximum estimate, and then I keep on going. And that's all. That's how it works. And, uh, and in order to because now I no longer have an exhaustive search, essentially. So instead, I have a random search. So now what I have to do is, I don't have an exhaustive search. What I need to do is I need to add to iterate, where is that, right? So, so, since I don't have a an exhaustive search, what I do is that I iterate over random seed. Because every time, well, okay, well, no, I know I I'm kind of, it's not going to make sense if I don't tell you something before, but in that experience, in that first round of experiments, the the estimate is random, and so what I do Is that I just iterate over random seed and at each random seed, the estimates are going to be distributed randomly and and only a some subset of the of the path are going to lead to solving the problems that I'm giving to the backward channel. And so I just iterated on the random season. So that's that's a little bit equivalent to having an exhaustive search. Well, except it's not exhaustive. It's just run until I solve the problem. But, but that way i i do solve the problem. I just run the I just run the backward channel many, many times, is in sequence, instead of running once in parallel and right and then the inference control experiments Go on by collecting data and

so on. But, but, yeah, that's, that's, that's the way I do inference control, right? Is this technical aspect of turning non determinism into determinism, right? That's what I wanted to present. Any question,

nice, I just have a quick comment. Well, when I implemented a probabilistic programming in scheme like 1010, years ago, I represented evaluation traces as problems themselves with additional wrappers, like this, random choice was made and so on. And it was also like sort of delayed evaluation, and you could re evaluate the resulting expression. So I see a kind of similar structure here. So yeah, it seems pretty natural if we don't go into some grounded structures with internal representations to have such sort of expressions which combine functional body parts or expressions to be evaluated with some additional information, like probability or usefulness of them, and I wanted actually to implement a generic inference control representations could look something like this, but I never had time to do this. It seems quite a good direction. I'm not sure if mm two will completely absolute. It will be nice to understand if they could be combined, because if we have some additional information about evaluations, we can still represent them

in MeTTa expressions, and if there is some additional support from mm two, like threading or something like this, then it will be just a part of the structure, rather than A replacement of it. That's all.

Yeah, yeah, I, yeah. Well, I, it is a fairly natural way, I think, to to the things. It's not surprising that, yeah, you did something similar. Many have done something similar, I'm sure, regarding Amen to what I know so far is that mm two is gonna allow you to modify the the priority in the stack of a function calls almost A way

to my my point is that this priority can be just mapped from your structure.

Yeah, I find, to be frank, I either don't know Amen to enough, or I didn't I don't have enough distance over it to to see precisely how the two would play together. But yeah, maybe you're right. Maybe it's

right. So, so let me go back to the code that so

well.

So I am I also don't know a lot about a month, so maybe we shouldn't speculate right now, but just Yeah, unfold in any case, sorry, I have to jump off. Sounds a lot.

Thanks for your question, Alex, yeah, so, so the I mean, well, even though Alex select I what I wanted to say is, because here what I'm doing is I'm collecting all the possible branches, and then I take the best one, and then I run it. But LM two mm two is going to allow something more sophisticated, where, okay, I I collect, or I evaluate, all the branches. And if I don't do anything, my understanding is that spontaneously, the interpreter of mm two is going to pick the branch with the highest score and is going to run it first and then. And so at this point, either I just erase all the other branches, maybe I assign them a, I don't know, negative score, or just erase them from from the space. Or I don't know exactly what Amen to offers at this point. But if I erase them, I get to the same behavior here, meaning I I execute only one branch, the best one, but only one so there's no backtracking or anything and but if I want backtracking, maybe I, maybe I don't need to erase them. I, maybe I, I raise some of them, but, but not all of them, etc, so I can narrow the non determinism, instead of just reducing it to a perfectly deterministic execution. That that's, that's how, that's my understanding of how it compares to Amen, too. Yeah.

Well, I actually had a short conversation with Adam about, like, what is the priority mm two instruction? So when he presented this mm two instruction, he said, It is priority. But when I asked him, What does it mean exactly, if I understand stump him correctly. He said that it is a like on the server side. They heard they have a number of execution queues. And this priority is not actually priority, but the idea of the key where execution will be done so you can so it is More my understanding, it is more some mechanism to parallelize instruction execution explicitly, which means you can just, just, can say that this instruction should be put in, into the this key execution key, and then, if you like pushed few instructions, they will be executed one by one. Like the instructions is which sent to the same key will be executed one by one. I uh, that's it. So I'm not sure if, like, it makes sense to I mean, probably one cannot say that. Mm, two instruction will prioritize something automatically,

right? Yeah, I, you, i You're right. You're right. It is, I mean, my understanding is that it's more general than just prioritization. The key that you mentioned, apparently, Adam has called that location of computation and but you can have so the interpreter. I I mean, apparently it's, it's, it's, looks like it's user programmable. What you do with the with these keys. And in the, in the prototype that she demonstrated to me, there was a there was an order between the keys, and therefore it would provide a priority. But he also mentioned to me that, well, it is whatever you want. It is user programmable, though, at this point it was user programmable in the rest code, so, but, but nonetheless, and yeah, and it doesn't have to be, it doesn't even have to be a strict order. It could be a partial order. It could be, I suppose, it could represent, doesn't have to represent the order on a stack or anything like that. It's, it's, really, yeah, it's, it's whatever we want it to be.

Okay, okay, yeah, it can be defined by writing some rust code, yeah, and

yeah. So apparently, I

mean the bottom line at the moment, we don't, don't know, even know, we will behave, okay,

right? I think it's a proof of concept, and it will mature into something more, more definitive ones, yeah, once we start using it. Yeah, I'm

I believe Matt left. I don't know

if I'm taking the role of the moderator, but yeah, I mean I have to leave after well 12 Minutes. But if anybody has any question or any I

anything that requires troubleshooting, please, Go ahead. You

we can also end the call before, before the end of the hour.

Well, yeah, if nobody has anything else on, probably, which make much sense here.

Okay, yeah, I used to have always a lot of question, but I mean, MeTTa has been maturing, and so it's, maybe it's a good sign, I Guess.

Oh yeah, probably, I'm sure, like, well, because biggest question to me is how it will change after more, after more is introduced. So okay, it's not okay,

right? Yeah, yeah, indeed.

Okay, then, well, have a have a good weekend, everyone.

Thank you. Thank you for presenting, presenting your system.

Okay, nice.

Going to read The paper as well. So

How accurate was this transcription?

0:00:001:25:49

AI Chat

Outline

Comments