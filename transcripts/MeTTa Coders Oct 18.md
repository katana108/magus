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

Oct 18, 2024 at 7:31 am

1 hr 16 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

LSP server, syntax highlighting, hover feature, Prolog package, VS code, Emacs integration, Idris language, type signatures, financial advisor, bioatom space, knowledge graphs, inference control, random sampling, minimal meta, grounded atoms

## Speakers

Alexey (28%), Speaker 1 (21%), Ben (18%), Speaker 2 (13%), Vitaly (6%), Speaker 3 (5%), Speaker 4 (4%), Matthew (4%), Speaker 5 (2%), Speaker 6 (1%), Speaker 7 (<1%)

Hello. I

Hello, Hi, there.

Who? Hello,

ah, I was muted.

Hello, Everyone.

I should we get started? Sure any questions to start? Neil Sebastian Roy, well,

not a question, but sometime today, I'd like to show off the work I've been doing on the for the years. Coach, so

cool.

Yep,

I'll keep this short because it's not complete yet, but let me share my screen.

I was wondering why I kept asking questions and no one responded.

That happens, some people see my screen, yes, yeah, it looks a bit, looks a bit dark to me. But apparently that's just, that's just a feature of at my end, not anybody else. So what I've been working on, I'll just just, it's

little,

little dark, small. Okay, let me I didn't. I didn't, oh yes, I one thing I didn't think about is how to turn the sound up. Let's turn this to the turn the size up. Just give me a second here.

Yeah, or

on the right, it gets smaller if

you share just the window, I guess.

Okay, let

me zoom in right. Okay,

let me in your whole desktop. Let me stop

presenting the try again with just that window. I

uh, windows,

confusing with me, but yeah,

I don't really use the screen sharing. Are that better?

Yes, yeah, okay,

so what I've got is this has been working on, Douglas amante been working on this for a little bit, is what's called an LSP server, which is a program that VS code and other editors, or they haven't tested, they can connect to to do things like syntax highlighting and hover and, yeah, scans for language server protocol, so Microsoft protocol,

no, LSP, okay, yeah.

So what? So the idea is, and we've got a very old version available, but this is, this is really more show than a, than a, than a, than the release. But basically what you do is you can install, go to the Microsoft micro place, install the server. There'll be a few other steps that we haven't written up. And what it basically does is, the moment does a couple of things, oops. We go to the one thing that does syntax coloring of the program. So whenever you work editing stuff, it's, you know, you can see it's highlighted according to whether it's an, whether it's a, what I call an atom, which I know is different than the meta method. I'm not sure what the name is. You know, things like the the the variables and strings and things are colored various ways. The other thing we have is a hover. So you hover over something and it tells you that's a variable

and this has changed Douglas amante, and it gives you the definition of it, or if you hover over one of the built in things, it gives you the gives you the doc help, and Doug and I are going with more information is better than less. And this one particular thing it will do is, if you hover over a something that has a has an at doc, it'll go and find it for you. So, like I've got for that, by the way, the test program I'm using is just a, my own version of format tags. I just wrote that as a, as a quick, as a quick test. And one thing it will do, and this, I know this isn't metalog, but if you do, if I was to have, I've had a test file I've been using for various fonts and things. If I have something in another window, it will still find, you know, so another file, it will still find the help. So if you've got multiple files open, it will work between files. And

so this is just a preliminary, and this was me testing. It worked for the various fonts that I know

some of you like using single characters. So, yeah, we'll be making this available pretty soon. It's written in prolog and basically, basically leverages off metal log to do its do its work. So just all the PROLOG package, download one

of these things from marketplace and everything should be running. So there any questions about this? It's just, this is just a

ruminary look.

Yeah, that's totally awesome. I know it's just a prototype, and he pretty much does syntax highlighting and and and Doc, help but, yeah,

excellent. Yeah, yeah. So we'll, we hope to have that out in a few days. It's, I know Douglas amante work on different parts, but we still got some emerging to do. He's been working on the, some of the, you know, the right hand menus, we can go to definitions or declarations and things. So

I've been using LSP under Emacs. I imagine that it's not going to be harder to use that plug in per Emax as it is to use it for VS code, I guess. Do you think it be sprayed much?

I My understanding is that it's that shouldn't be hard at all. I have not tried it with any other editor, but I, but I've been basically following the protocol so it should work under a vast variety of editors, but the install instructions will, of course, be different, but you right,

right here. You just access to the marketplace, just via VS code and under REMAX, while it's going to be probably a tiny bit more involved, but

yeah, well, the way I'm actually running it, because I'm developing and don't want to take the marketplace every time, is something called a vsix file which gets loaded. So what? There's a, there's a the, there's ways of doing, loading it locally without having to go to the marketplace. Yeah? And yeah. The the, I base this on the PROLOG LSP server, which turned out to be quite buggy, which is why this took a while. And that has it that that the page for that has instructions for all sorts of editors, and I think emacs is one of them. So, so yes, yeah, should work under Emacs.

Okay, yeah, I'll try. So as soon as it's out, I'm going to try that so I'll be able to provide any right extra instruction for emacs users. And I wanted to say so I've been using specifically LSP with Idris, and I use that to fill holes in program. So basically, I would write a program, a partial program, with some holes in it. The for instance, say, I would replace, say, a function call by a question mark and the name of the whole and based on the type signature, which in Idris can can be very expressive.

Then also, so use Idris, what I'm not sure, not familiar with that? Yeah,

it so igris is a dependently typed language. It has a type system which is very expressive, right? You can, you can, pretty much, if you work hard enough, on the type signature, you can specify. You can provide a specification of the program inside the type signature of the program. And so, in principle, you can synthesize the program that you're looking for, just by finding a witness. We call that a witness of the type signature and and so all you can provide, you don't have to synthesize the entire program. You can just say, provide a template that contains holes inside and and so, okay, well, I was able to do that. It was sometimes helping even to be a little bit more productive. And so there is here, there's a lot of room to incorporate that sort of things in an meta LSP server, where, for instance, the backward chainer could synthesize a meta program, or the reduction engine could reduce a meta program in a in a, let's say, simpler form, and all that sort of thing. So what I want to say is that it could be sort of a it could provide an API to invoke AI functions directly, right via the code editor.

Yeah, that is something, that's something we're going to look at. I know we have access to everything. We're going to have access to everything's available in metallogue, and I know that that included in that is like using llv so llms and and any other tools that we have there. So that's, that's the direction that we do want to head.

Okay, excellent,

okay, anyway, that that's me. So this is any other questions,

as you implementation located at some GitHub protocol.

Sorry, the implementation is located where GitHub, oh, yes, it is. It's just part of the meta WAM project, just one, it's just one of the packages that's there. So yeah, I could actually post, I have a very old version. I could post a link to that. It doesn't do, doesn't, although, if you leave it a few hours, I'll have, we'll have some updates to it. Yeah, I could put, I could post the link that we have so far. If that's, if that's the interest, let me go find that one. Once I'm off, once I'm once I'm off of presentation,

would you say that you're going to have a release pretty soon? Anyway, like

we Yes, yes. So I'm going to talk to Douglas amante and sort out what needs to be. Yeah, it'll be a preliminary lease. Things will be not quite complete and but, you know the idea, the idea is to get people, know, to have something that's that's sort of useful. And I've been using this while. I've been writing meta, largely typing in something and seeing if it's got a definition. Is it already been helpful, see it, and then we'll keep improving it. So I'll talk to Douglas amante. Won't be won't be long. Okay,

thanks for that. That's very useful tool. I'm

sure I've set forward. I

anyone else with

ideas?

New code, questions, nil.

So I would have, oh, someone wants to say something. Please, go ahead.

Oh, me, yeah, yeah, I posted on the metacoder site that I've been trying to do metamodel, and I tried a sample code of interfacing with chatgpt, and it said client was not found. I think someone, I think Alexey, you responded that I just need to import the open API key, and it should work correct,

I guess so. Yes, so if you have open AI key and environment variables, then maybe it's one of the possible issues, because if the key is not found as a client is not created, we need to improve this behavior, but generally speaking, yeah, I guess this is the main reason.

Okay, yeah, I'll try that out. And I saw like, the sample code of using metamodel with chatgpt. GPT, so yeah, I definitely will want to try it out. Um, I think it looks pretty simple in terms of, like, grouping items together. So I have like, you know, simple examples, um, and when I was at the AGI conference, there was like a demo about using metamodel with chatgpt. And I think it was like some basic overview. I'm just curious, does anyone, does anyone have any ideas of, like, very sophisticated examples of using meta with chatgpt. Is there, like, I don't know, some sort of example where you know it, you've turned like, chatgpt into like, a complete financial advisor, or what is like, or what is like a really, really great example that could showcase, like the example of meta with chatgpt For me,

well, the most complete example we had was for the prototype of singularitynet platform assistant, and maybe this is the only one sort of product, or something like This. There are plans for sort of financial advisor Nick NEFA is developing a product plan which includes, in particular, the possibility of using meta motor for crypto trading or something like this. But we are not there yet. Well, another example was for the

travel assistant, but it wasn't finished, because our colleagues lost interest in further development. Basically, we just don't have enough use cases right now. And if you have some applications for it, you are welcome to share them, and we can discuss how it how metamod could be used for them.

That was the only question I had. Thank

you. Might Alexa, you might point Daniel to the code for the assistant. Maybe would that help? I

I say.

Alexey, yeah,

well, here is also maybe it's not the final version, because we passed the development to Mike pavlien, like half a year ago. So maybe you can contact him to find out if they have something else or if the continued development in this report, I believe it is yes, it is public right now And but I'm not sure that it will work with the current version of metamoto, because as far as I can see, last commits were like seven months ago, and metamoto was considerably modified meanwhile. But if you don't want to run this example, but just to see as meta motor usage, then it can Be a good start. I

Okay, great. Thank you. Thank

and you can also try pinging Switzerland, besides on matter most, if you have some technical questions, although she's now on vacation. I'm not sure if she will be responsive, but in any case, You can try to pin her. I

Okay, thanks. I,

uh, by the way, I was using metamoto from the GitHub repo, or have you installed it using Pip? I here,

I I basically went to the GitHub page and I downloaded the files. So there was like a python setup and then a pip install. So I did the pip install directly from the directory that I downloaded from metamodel.

Okay. The issue is that metamoto is now under refactoring, so we are trying to keep it in sync with hyper experimental repo. But if you are using, or trying to use a meta motor from GitHub, then hyper on experimental could also be built from the source, because if you try to install hyper on using Pip, then there can be some incompatibilities with the current version of metamater. Okay, hopefully, we'll make release of both hyper and experimental and metamod maybe by the end of the next week, and these versions should be compatible with each other.

Okay, so we say refactoring, meaning that instead of having to download and install directly from the directory, I could just do a standalone installation, much like you can just do a standalone installation of NumPy and pandas and so on.

No, no. Actually, you already can use API P to install a boss hyper own and meta motor refactoring has nothing to do with it. I'm just saying that the current versions on PI py are compatible, but if you use meta motor from GitHub, it can be incompatible with the version of hyperon from Qi toi, FBI, Qi, okay.

Okay, understood.

I have a question about I feel like I've been experimenting so far, mainly by trying to implement implement programs in meta that you could also implement in other languages. And I feel like the examples that you that I've been seeing passing in about the way that meta sort of excels is, for example, through the match statement. And my I feel like maybe, that would be more useful to run on, like specific data sets that contain a lot of relation relationships between concepts already, like, you know, like knowledge graphs, or that, maybe that you can find somewhere. Is there any data set that you are using as a default that is good for trying out language experiments, for example, like a little bit more in the in the concrete domain, instead of just in the abstract programming realm.

Per i don't have such data sets, but different groups, they have their own data sets, like by AI team, or maybe someone else, hopefully will have a sort of crypto Knowledge Graph or whatever else. So maybe other people from the school can help you with this.

Yeah, I found an interesting data set that I've been running some experiments on, but just in with, with like by dorj. But if that is a snli data set. It's a data set of labeled natural language pairs, and the labels are have to do with logical entailment. So you will have one label for entailment, one for when the statements are contradiction, and one for neutral relationship. I thought might be interesting.

Semantic caution,

I just popped into the middle of that. But what kind of data sets are we looking for? For what?

Well, I feel like with the meta, the the use cases that we're supposed to get out of it that are not available within other languages. They may might be specifically useful when you already have a graph. For example, that knowledge graph that you can Yes,

the most substantial case currently being played with in that regard is the so called Bio atom space, which Douglas miles and a couple of helpers are working with. And there's a lot of integrated knowledge from Gene Ontology and the pathway databases and Mike, I don't know if Douglas on this call, Mike Duncan is on this call and and know knows about this, that's been, to my knowledge, mostly played with in the meta log version of meta. But there's no reason the same knowledge base can be played with with any of the meta interpreters. I mean that that the bio I'm space has the downside that to understand what's going on in there,

maybe a pain if you know anything about genomics and proteomics and stuff on the, on the on the other hand, it is. It has been accumulated over many years in opencock Classic with a bunch of thought behind the knowledge representations. And it's not just like a bunch of triples. There's there's a bunch of complexity and complex cross linkages. And, I mean, it's, it's all real stuff. So that's, that's the best example of, like a large, curated ad space that's been used for research publications before, and so forth. We are, there's an initiative going on to build comparable spaces for both us, stock market data and cryptocurrency data, which is being led by Anton colonen in Novosibirsk. But those are not actually ready now, whereas the bio AB space is ready now, is being used a bunch by Douglas miles, T

and Michael the team, presented a demo at AGI 24 as well as wasn't a coping Yeah,

ramen summary, gave a demo of PLN reasoning On the bio atom space in the afternoon of the hyperam workshop at the AGI 24 conference. And they have a little user interface showing the entrance trails from PLN doing some biological reasoning on that. So I mean that the video of that talk is is online in YouTube,

and the graphs from semantic Parson project could be used now,

yeah, but we don't have, like, a big app space you could just download now For that, I don't think, I mean, could, could be, but the biolabs face is the one that's like right there, and you could just import it and load it and and play with it, right? I mean, what we have in semantic parsing is script second building AB space, but we, we're still screwing with the the way to do it. So we haven't yet, like, done a big batch job where we parse a huge amount of data and just make, like, a reference Adam space and unless, unless I missed something. I haven't seen that yet.

There's also the KGW iPhone package that Robert Haas made, that all that works really well. And you can you can just get some, like, there's like, five different graphs that you can download and and make a meta version.

What's it? What's in KGW, I don't know.

It's just, it takes some publicly existing bio it was a deep funding project.

It's more more, more biology. Yeah, it's

more biology stuff.

We don't, we don't like all these human bodies. We want to make AI's.

We can make them out of biomolecules,

all right. And Sebastian,

I'm going to post Abdul's email. Abdul Rahman, in case you have questions about the actual code that was used to query That bio atom space, XA bush@singularitynet.io Okay. Thank you. Applause.

Nobody, has nothing to say. I do have a question about a function of I've come across the standard library meta file and called unique that doesn't work, and it would be, it would be very nice if we had that, because Mindy, okay, I'm trying to share my screen now. Wait, let me try and do that.

Yeah, here we go.

So yeah. So that's the functioning question now, and I tried to use it, it does not work, right? I did implement before I was actually aware of it. I implemented my own, but it's very slow, very, very slow. And so having, well, having a built in that's reasonably fast would be very welcome. And so there's that. There are a few others that, okay, could be potentially interesting. And so they all operate on superpositions. And what I'm thinking is that, as we've been well, brainstorming a little bit about inference control or reduction control, we may say. And I'm thinking that maybe all that we need, would it be just, you know, just to try if, even if, that's not the the final design that we uni currently works. I met Metallo. That's cool. Okay, great, right? So I actually wanted to mention Metallo. So metalog has another one that also works over superpositions, which is limit you will take this limit, for instance, three some computation, and it would get the first three superposition that you get out of the composition of the computation. And that's another example of something that, well, can give us some capability to do some form of reduction control. And another one could be, I don't know. I mean, maybe limit can be combined with something like random. You deduction, or, I don't know, something like that, which would try to which, which would introduce randomness in the interpreter, in the priorities of the branches that the interpreter is going to select, etc, these sort of things. I mean, again, I don't know if that's really the design we want for a fully fledged inference control subsystem, But, yeah, just just wondering.

Well, few questions. I wonder, who implemented unique and other such functions.

It's actually say, was it used by Adam

for migration to the minimum. It after migration is done, doesn't work in minimum, it because implemented with K with the errors. So, yeah, we have an issue about this on the GitHub. Experiment approach, yes,

okay, we can try assigning this issue to someone in our team, maybe who is not deeply involved in meta development yet. But this can be a good first issue, or will it be too complex

with any motivation? Actually, my first one I found that I tried to look, can I fix it quickly? Say, remember, there is some issues this. And probably it is not easy, okay, I will start trying to implement it through German consult to the auto interpreter, result, like result coding the interpreter inside meta, actually, inside, I mean, inside this implementation of the instruction. I believe it was before I introduced meta function into the minimal meta interpreter, and now it should be actually easy to fix it. I believe Okay. I need to look at it. I can say for sure right now, if it is easy or not,

think about implementation in pyramid itself.

I believe it could be implemented in, yeah, in pure beta, probably. But

Well,

not exactly. I mean, okay,

if it would be implementation of a grounded function in Python, then I know people who can do this without distracting you from implementing but if it's involved metacogs, and maybe it will not be that simple for those people to do this.

Okay? So actually, the main idea was not to only fix the bug, but also to improve the implementation, because previous implementation did it get recursive call to the interpreter and rust, and it is actually Not safe and not very traceable, I would say so. The main idea was just make some necessary things in ground, inside ground, function, body, but, but delegate interpretation of the internal, of the open past to the interpreter, to the out interpreter, without recursive call.

So is the best way to pressure with this issue. Will you take another look?

I will take another look, and we can just decide was dealing I mean, as we assign someone from our team, for example, to fix it. Maybe it's just fixable in context right now.

Yeah, so in case that's relevant, I do have a pure meta implementation. Okay, it could be simplified, just because I'm first how to say, converting a topple into a list, but, but anyways, it's really, it's incredibly inefficient. I don't think, like, even if I were to skip my conversion from to list, it would still be incredibly inefficient. And yeah, so I just, I think that if it can be ideally a rest built in, or if a Python built in is, uh, well, it's fast enough, all right, good, but, yeah, big, anything that is remotely related to inference control should be as fast as it can be.

I was it a question? Oh, no, okay, and as for the second part of your question regarding random sampling prioritization and so on, yeah, this is a question how to approach it. So I tried a little to do some sort of probabilistic programming, but abandoned it because was to certain uh necessity to combine this sort of sampling with compilation, because when we have some deterministic branches, which we do not want to recalculate because there's the same there is a great, great desire to just compile these branches, and it could be tried, Say, in Python. But since there

is some work on compiling metacode, I decided to postpone it. Of course, there is always an option to try to implement another interpreter in pure minimal net like the current interpreter is implemented and, but, but, yeah, most likely it just will be inefficient and non satisfactory in terms of computation time And also, well it's, it can also be implemented in meta by some additional annotations or structures, but basically, when we are talking about choosing different branches and sampling, we need to keep information about previous interpretations, and as I said, it can be naturally done in meta. But another approach would be to enrich atoms themselves internally with some additional information, like this atom was evaluated and gave this result, or this atom is probabilistic, and an attempt to re evaluate it will yield different result and so on. So basically, the question is so whether to enrich the internal structure of atoms in order to implement such inference control and so on, or it would be better to try doing this in pure, minimal method. I don't have a clear answer to it. To this question. I

uh. But in any case, as a basic or random sampling should be done by grounded atoms, and it's if it is so it is natural to extend the semantics to all the atoms as well and the version of interpreter, whether it is built on top of minimal meta or meta implementation, and minimal meta, the this interpreter should know about this semantics. So in any case, I see it as possibly a modification of the interpreter. So it most likely shouldn't be done

within the Met interpreter, but we need to go the level below and do it as in minimal meta, or possibly make some new type of atoms which will contain this additional information about sampling processes,

when you say so, okay, so first of all, I do see that, for instance, as far as random sampling of different branches is concerned that could be done in pure meta, okay, just have a you just have a random sampler over whatever collection, and you just collapse the superposition, then you sample, and then you well, you run what you sampled, or you you superpose a few things that you sampled, if you sampled more than one, and so that could, right? So that can be implemented entirely in pure meta. Of course, it will be very slow, so there's, there's an incentive to implement it in a lower level. And so there's that, okay, and so. And then there is the specification of the behavior. When you mentioned the data structure associated to the atoms, I think you're referring to that which could be in the type system, right? Is Is it what you have in mind? Alexey, oh,

well, not necessarily type system. You can indeed incorporate it into a type system. And if you really have a structure in meta itself, like meta expressions, instead of some internals of atoms, like it was done in opencock classic when there were some values internally attached to atoms rather than exposed to the atom space. So Well, on the one hand, it should be natural to represent such structures in meta, because it is supposed to do this right? So we have now one part which represents the expression being evaluated, and another part can represent a computational trace or the results of previous samplings of this expression and why couldn't be represented as also an expression and method assigns a corresponding type to it, right? On the other hand, it indeed might be not like it's kind of problematic to write as a compiler of metta. In metta, it's just inefficient, and there are many heavy computations which should be done under the hood for this sort of evaluations and reevaluations of expressions. And well, if we are writing some sort of compilers, and maybe this procession should be a part of this compiler, but compiler general enough to compile any metacodes, and we can write this into a method and compile it with a generic compiler, but we don't have such compiler right now.

Okay, okay, okay, I see what you mean, right? So if you have a value which is attached to an atom, then of course, you can just write a function that would return that value. You can write that in pure meta using just declaring a function, but it's not going to be efficient. So you're wondering whether we want to have this at the level of a right interpreter. Yeah, like an open car, classy. I

I mean, I think that as long as the the built ins are say, right, maybe we could just have, say, a built in called key, a function key that would associate a value to an atom and and then this could just well either be implementing pure meta or have a special treatment by a compiler. And right, the compiler would intercept the pure meta definition in, say, in the standard library, and just compiling to something more efficient or something, I guess that would be the way to go, Bit like inference control. Thanks,

thank you.

Okay, anything else?

Thanks, so I missed, I missed the beginning of this call. And there's a bunch of familiar faces to me on here, not, not, not that many, though,

yeah. So I,

since there's a lot of people in here, I wanted to note that, if it hasn't been noted in this call, we've, we've released a bunch of grant offers for meta work on the deep funding site from singular unit and so this is basically to give people grants For doing various specific AI things in hyperlon using meta. So I will send a link to that on the Google meet chat board. So if these are not available to people who are now working for singularity net for for pay. They're intended to bring more people into it, right? So. But if, if anyone on this call wants to apply for one of these, or if you have friends, aunts, uncles, colleagues, whatever, who might might want to apply to these, please, please pass the link along. So that's mostly not about the plumbing of meta language. It's doing AI, some specific AI stuff that singularity that thinks is interesting, using meta to do with evolutionary learning, probabilistic reasoning, attention, allocation, blah, blah, blah. But the there's also a couple there which are like, generate a bunch of meta code, which is just like generating meta code, because we want to be able to train llms or other systems to be meta coding assistance and and for other reasons, so that Alexa and I had tossed around actually using evolutionary learning with a strong diversity fitness function, just to generate a lot of correct but diverse medical doing, doing particular things. But anyway, bunch bunch of stuff there. And if folks are interested in those things and have questions to ask Matt or I, or Alexa or others or Neil, will be happy to answer questions on RFPs. Oh, yeah, yeah. So there's a branching out as well as reaching out to relevant people. Individually, there is an email address for asking questions.

Thanks, Matt.

Great point.

So I'm I'm quite named, the meta stuff, and I was just wondering, is there, anywhere to go for just like all of the examples so far, because I was looking through the docs. And even though that does help you get up to with the like,

well, there's a true AGI dash IO GitHub, which has a bunch of examples, and Patrick hammers GitHub as the NACE system, which is a lot of meta for sort of a experiential learning in a simple game worlds. And those, those are, those are two places I want to dig around in code and in the true AGI dash, io, GitHub, there's a bunch of textbook examples of of algorithms and data structures. And other than Patrick's thing is like a bigger a bigger system using meta, which is interesting to see for that reason,

sweet. I'll check those out.

Other questions. There's also a bunch of code from Douglas miles in metalog doing a bunch of tests against the bio atom space, which I I haven't looked through that stuff as much myself, but Mike Duncan, who's on here, Douglas miles, can probably, probably point to where that is, yeah, so someone posted the true AGI IO. There was also had the link on that, but there's a nice repo from Patrick hammer. There's a Patrick made a meta version of Barrick Cook's Aris system for like one shot or few shot inductive learning in simple game environments. Douglas Miles has a bunch of meta code for handling the bio Adam space

I just posted Douglas miles, parent, yeah,

Patrick, stuff, isn't it? As I recall. I've been looking at it for a while,

but you probably have to dig around logic. Mean for some of the stuff, for the

Yeah, Patrick is making and Mike Archibald are making a bunch of meta test cases intended to compare metalog with the other meta interpreters and compilers. But I haven't actually looked. I haven't actually looked through that code myself. Patrick, stuff is quite nice,

yeah, and it's still in the true AGI, among some more textbooky stuff, you'll see some simple Palin reasoning stuff, or Nil. Nil. Put a couple of inference rules in there using a sort of dependent type formulation for the for the rules. So there's a bunch of stuff there, beyond the tutorials, it tends to be well commented. I still find most of it extremely confusing, but how it goes?

Yeah, so under true AGI project in GitHub, there is a repo called Cheney with a number of experiments about chaining, usually small examples.

Yeah, so part of the motivation for these deep funding requests for proposals is to get more people doing more complicated stuff with meta just to see what problems come up and understand how to do things. And there's also, of course, the hope of getting some actually useful code for building toward the premise cognitive architecture. I gotta jump to another meeting, though, but that I was able

to great having so many community members beginning to join us so and that's it. I'm glad Ben brought that up about the RFPs. We just released all of those. I think they went live yesterday. I

anything else before we call it. I

I guess that these were good.

Thank you. And the total lack of science, I the total silence, not lack of silence.

Okay, thank you.

Thank you all that was useful. I hope

you're All By I

How accurate was this transcription?

0:00:001:16:07

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5