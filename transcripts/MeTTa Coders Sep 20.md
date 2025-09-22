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

Sep 20, 2024 at 7:31 am

1 hr 40 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

meta, file, write, rust, type, quantifiers, function, translate, git, notation, python, work, implementation, rdf, implemented, cool, data, triples, catalog, atom

## Speakers

Vitaly (27%), Douglas (25%), Speaker 1 (12%), Adam (9%), Speaker 2 (8%), Douglas (6%), Speaker 3 (6%), Speaker 4 (4%), Matthew (1%), Speaker 5 (<1%), Speaker 6 (<1%), Speaker 7 (<1%)

Hello, good Morning

now. Morning

Morning. All

Good morning,

this five

after 35, after got number so maybe we should just get started.

Welcome back now.

Oh yeah, I Am I?

Any

Any issues, any questions from this past week.

Hi, can you hear me?

Hi, Anne, is that correct?

Hi, I have a question about I'm currently like translating different data formats into meta. And I wondered whether anyone already tried to translate notation three or something similar, with like these quantifiers for all. And there exists like whether someone already tried to translate such things into meta.

Translate what into meta?

Well, I'm currently working on notation three, and so it's a data format, but it has also quantifiers, like a for all or there exists, and a few more. And I wondered whether anyone had already worked with that in meta.

You mentioned notation three. I'm seeing a Wikipedia page. Is it? I'm going to paste the is it? Yes, so that's what we Okay, uh huh.

So I wanted to mention about that is that notation three itself is supposed to translate to RDF, and so secretly, it doesn't really have quantifiers. However, some really cool people have been using the list formats of notation three and embedding quantifiers into it. But the big there's actually but so what you have is notation three with proper quantifications and though, and it, and you're using, you know, that's correct, and you're using it correctly, it just sort of overloaded the language. And get made it more capable by using those quantifiers than normally notation three would have been. Is where I was going with that.

Yeah, exactly, because I already did a translation from like notation three and then via RDF triples to go then to meta. But it's kind of hard to work with because it's just not very intuitive.

It turns everything into a arity two predicate, all the relations become. It blows up in size when you convert it, right? Yeah. So.

Annaleen, do you think you could provide a an example in notation three and,

yeah, definitely.

Give me a second.

Yeah, I'll share my screen. I

um, so here are, like, a lot of notation tree examples. Uh, there are, like the easier ones, like this one, which just consists of triples, saying like, Spider Man is the enemy of Queen goblin. Spider Man has named Spider Man and things like that. And those are obviously very easily translated into meta, because they're just triples. Those are a bit harder examples, but not yet with, like the quantifiers.

I'm sorry, just looking for some of the Yeah. These are like rules that are a little bit harder are like sort of if then rules. So here it says, if the weather is raining, then it's also cloudy. So you have like these, if then rules.

And this is rule chaining,

yeah, I think that example that that was three of three up above,

yeah, actually could have easily had a good quantifier, not like, oh yeah, superhero and imaginary. For all things that are superhero, they are also imaginary. That would be, yeah,

yeah, exactly, something like that.

So what is a? It's is

a is actually a short notation for the URI that would say type so it says a has type superhero, sorry, x has type superhero, and X has type imaginary.

Okay, so where is that coming from? Where is that a coming from?

Yeah, it's something they just kind of say in three we use the A for that. It's not really specified anywhere.

It's just short of a shorthand way of saying is, x is a superhero. Implies, yeah, exactly

imagine.

So it's a convention in this tutorial not necessarily a built in of notation, three correct.

It's built in, yeah, it's

built in, oh, okay, uh huh.

But it stands for a specific URI.

How many

years is we do? The college

a superhero, therefore x is imagine, a imaginary and imaginary. So,

so I would say, I know it all depends on, well, what kind of logical system you choose, you could choose, you could represent that in a type theoretical manner. In this case, the universal quantification would be kind of implicit, just by by virtue of having type variables, they would be universally quantified. And so there would be that if you need existential qualification, do you need that as well? Yes, yes. So, so same thing side theoretical manner, you would use a dependent sum. So, so you can go in that direction. And I have examples of that. But you can also go in other directions, which are more like, I guess, building meta terms, representing logical terms, more like, closer to classical logic or that sort of things. So, yeah, it all depends on what formalism you wish to use, basically, what maybe, what would be the use case like, what are you going to do with once it is converted into meta. What are you going to do with those with those things? Yeah,

so we were working on this deep, friendly projects in which we're just translating different data formats into meta, and use meta to query the data, things like that. So I guess that's mainly the goal, just to have the data somewhere in meta in a manageable way, such that it's easy to to get the information out of its

something where there's no information loss, that whenever you could have recovered from it from and three, you should be able to recover it from meta, even if it doesn't have a perfect mapping in A way. I guess that would be

a possible I made a mapping like via the RDF and then to meta, and you can perfectly translate it back without lots of information, but it's just not nice to work with, because it's very, very ugly in meta, if you put it that way. So I was just trying to find something a little bit more elegant. But I'm not sure what exactly the requirements would be. I don't know. Maybe Adam has something to add to that, because he's also on the project. But, and also, could

you point the link for that deep funding. Yeah,

so my understanding is correct. You're trying to do that, and the what you need is just to retrieve. You need to query this data, basically, you have a data in notation three format, trying to turn this data into meta for then being able to query that data with matching queries And that, yeah, is that? Is that going okay? The deep funding, yeah,

it's here.

Thank you.

I Yes, but I also saw some notation, three files which were kind of runnable. So I'm not sure whether we also want to be able to do that. Oh, I have, like, an example, I think, right here, where they have literally, like calculation rules. And what you could there is, like, literally run the code. So that would also be nice if we could, like, translate the notation three in such a way that we can also kind of run it.

I don't actually mean, no, understand what that mean. Maybe because just

this file or what I was saying, I mean,

right, running,

yeah, the code, yeah,

it's like, Vision free,

because you have, like, these, these rules, these implications, you can, like, infer things. And there are, like, programs or, yeah, there

are engines,

right? You could, you could apply a chainer. So these are rules for a chainer that can do, yeah, basically,

I run this, E, E, y, E is a chainer that runs this one, written by ONS Jetton.

I believe I have the name, yeah, and

then there's, you know, there's, it's been over time, over the last few years, more and more can run this. I've written one that runs this.

Yeah, I think if we're translating the notation tree files to meta anyways, it would be nice to be also able to do this inference. I think, well, I don't know whether it's necessary, but would be cool.

Yeah, yeah, please

do. What's interesting is sometimes we have what are called B nodes, blank nodes, and those are existential, quantified variables. Yeah, yeah. Those tests is actually like, if you look in this file, the word test in there,

yeah, in a way,

the test refers to the entire thing it is. And that's like an example. I mean, it's what there's probably gonna be way better examples of existential quantification on here. But was gonna say B nodes usually can be essentially qualified. I tell why that test there was not a B note, that's just a marker. Yeah, yeah. So,

so if you wish to to run these rules in a chain, or Yeah, I would. I mean, I'm compelled to to, to guide you towards the the type theoretic format that the background chainer supports, because while you have a backward channel already it works, is slow. Because, you know, backward chaining is slow and meta is slow, but it works, and you would be able to do this kind of reasoning, not to say that it's the only way, but it's a way that you have already some examples in meta if you want? Well,

there is definitely an ideal way that, like, you can make metacode have just you could translate this to meta, but you would still want to have the chainers, like with Nils trainer. I feel like there's going to be a point where it sort of hybrids itself into the meta language. Like, right now, it's a program that runs on top of meta language. But I feel like, as we want more inference control and things in the language, it will be it like, I feel like Neil's setting the stage of how the meta language will have a what chaining will be like in the meta language

with this.

So ideally, whatever there is going to be a format that people would translate something like this into meta and it and it wouldn't, and it would, and his chainer would be picking that up. You know, even though, yeah, go on, I

actually so even though my chainer is kind of a distinct program, taking as parameter a distinct space of rules. There's actually a way to write a meta program, you know, just a collection of function definitions with the equal the equal symbol, just as we used to define meta function. So you can, you can just turn that into an actual set of functions that will behave like this, standalone backward channel, plus rules. In other words, you can just map that directly into straight meta or something. I don't know if that's that's,

yeah,

yeah. So I have examples of that as well where the chainer is embedded the chain or postal rules are just embedded as as one thing and and so yeah, that's one possible representation as well, which is,

yeah, very much, Yeah. I mean,

that feels like what you were describing,

yeah? And I was gonna say that's going to be fast, you know, that's right,

exactly, yeah, that's going to be faster, yeah?

So my plan is to write a script that would do that automatically. We take a knowledge base, and I would just, boom, turn that into a functional

form,

and then data is programmed, basically to project the data into program.

Yeah, I I did

that manually, but I didn't write a script that does that automatically. Yet,

would be interesting for me to look at, like the syntax you see your danger, and kind of see whether I translate this into something like that.

Yeah, right. So I'm looking for examples. I'm going to paste that, yeah, and because there are many ways, like within this type theoretic format, there are many ways, actually you can do it. And so let me paste you a few ways, and then you can decide which one is, Well, which one is best, if any? Yeah, so I'll just, I'll go silent, and I'll, I'll call the chaining repository for

these examples.

Yeah, cool. Thank you. Thank you very much.

Something about translation there that we had on the screen where absolute value is kind of the center. Sorry, let me bring it up, back up if that ends up being in prefix notation. That might be better than infix, or at least for meta translation, unless there's a, unless you're to put in front of it a, yeah, here we go. Yeah, that, oh

yeah. This was really, not Yeah, not really something yet, but yeah, please.

But then also, it makes sense. Sorry. Now I'm gonna go against my set, of course, is to actually put in front of those three triples, something that actually front of the three things, to actually have a word like triple. So it would be so in front of that x, yeah, actually in front of the let you put triple, you know, and then, yeah, that that would work too,

right?

No, no, you could leave it. Then you could leave it in fixed, yeah. Otherwise, you'd have to infix it, you know, right? And you have to, I think it could be just as efficient this way.

Yeah, it makes a lot of sense, yeah.

And you probably have a big one on the outside of the implies, you know, on the very head of the Yeah.

And you could even say something like triple from n3 so you don't think it's a triple from RDF, you know, that's

like something like this or, yeah, exactly,

perfect, yeah.

Oh, it's a wrong key.

Yeah. That's just what I wanted to say about that, because I saw you were looking for sort of like a translation that, when it got loaded in the meta, that could be used, usable, yeah,

yeah, yeah. I think what I was trying to do here was, like, literally write a meta script that would like run this as the forward chain, or which run it. So I was literally, instead of translating the file to meta, like trying to translate the functionality to meta, but I don't know whether that's the way to go. Yeah, because, yeah, of course, here I wrote absolute value as you have absolute value here, but I was thinking like, should I translate it to like, the absolute value function that is provided in meta? Or do I like, leave it like this? Or

right? I would almost leave it like this, because we don't always have if you look at the at the prefix notation, I'm not prefix, sorry, functional notation of the absolute value function, and then you look at the RDF, I mean the turf n3 it doesn't assume which is the input in the output. It's bi directional. And functional notation of meta is not necessarily bi directional by default. It can be, but we don't think of it that way. So for example, you're to say the absolute value of of x was six. Well that means x could be negative six or positive six. And if you're to write that in functional notation, how do you write that? Do you put an equal sign there, like equal six, and then the ABS wrapped in, I guess I could type it. It becomes very awkward, I think, say, put it into the chat. Okay, like that,

you see, so, if I was to actually use, you know, I mean, oh, yeah. So the so the the first 1x of map of absolute value y would be, we don't have, like a notation, functional notation, sort of messes all that up.

Yeah, I would also refrain from translating directly into metal statements, because you may have multiple interpretations you want to run it with. So you're now adhering to well enough an actual standard. And then if people want to make interpretations that differ from that standards, they can write transformations from the files that you have to their own logic to evaluate it.

Yeah, fair, yeah, cool. I

so the, you know, I was gonna say the one that the n3 that has quantifiers in it, well written, that usually has more than arity to predicates in it, relations or multiple arity, and that translates just beautifully already into meta. Meta,

because we're not restricted to any number to arity two relations, we can have any arity we want.

A few years ago, we had this natural language to logic translator, and it was working for about 10 years, and then the semantic web came out, and they wanted all those translations to become in or come become RDF, and it made the Like a translation that might be the price of meat, of beef, waste, $1 a pound. It would change that to about it take six or seven triples to translate that, whereas only took one logical sentence in the previous cycle form, but to translate that into RDF, it's like several triples, a much blown up, larger size. And that's the advantage of meta is we don't have to become RDF before we in the translation. Do I feel like those qualified statements are going to be exactly like that. They're going to be in a more in a prettier form, when they're using lists to deflect entire sentences and not trying to use triples in that, yeah, cool. That

makes a lot of sense. Thank you so much.

I have another maybe slightly unrelated, short question, like, Is there somewhere a list of all the built in methods that you have in meta?

Well, actually, I believe, can you can get from the stores? Why you cannot get it from we have a help function which can show the documentation for the function if you pass this in document, yeah, but I believe there is no function like which lists or function from the standard library. It is not like this. List is not that big. One way to look at it is to look at the source code, maybe to the documentation. I'm not sure if there is a document which contains also function as well.

Aren't you kind of also making one in standard lib, underscore, minimal meta, dot meta, you know where you're putting all the documentation that you're doing in that dot meta file.

Probably we can add something like this, for example, cell function for stable system belief, standard library, I mean, we could add documentation for standard library which contains all the functions library we think We can do it, but it is not implemented. I

just so you know an Elena, I have posted, oh yeah, okay,

yeah. So thank you so much. Yeah,

well, so I hope there's not going to be too messy, and you're going to find READMEs here and there. But yeah, don't hesitate to ping me if if you need

cool. Yeah, thanks.

It would be nice if everyone like in Mork and in all the different implementations we all had a place where we kept all the meta language in the list with documentation that would be even if it was a spreadsheet or a file.

Yep, yeah. And a common place to land for all the project for all the different implementations, and then subdirectories from there,

right? Yeah,

you don't have to go one place for Mark, another place for experimental, another place, just one place, and then you can branch off to all of the others.

The other would be there too, right? Pardon, Jeddah. Jeddah, is He? Is he analog? Yeah, but yeah, Jetta, there's a one that they're also working on in

vis working on, right?

Yeah, okay. Is a compiler on top of hyper experimental, so it should basically use the same i

i mean the mountain Lying depth might be a good place.

Yeah,

yeah, actually wants to embed documentation to the court, and if, if we need some pay issues which contains this implementation, we can just reinvest the court and get the information from it. I so it wasn't, maybe it was still quite clearly different things was finished and generate such variation functions. I

It would also be something that, like, on a wiki would be amazing, like, if we hadn't could, like, have an alphabetical index with wiki where all the functions were there you click on it takes you to the page where it's been edited and curated and documented that would be awesome.

And you can hit the runner, hit the run button to try it out in different ones, almost what we have there on the meta dev website already with the playground,

but you know, per function would be cool. I

I know I'd be willing to set that up, but if, but how would but if the other teams, or if another team, you know, is already set up with the meta Dev website might find that doable too.

Yeah, it's like, and there is no alphabet index,

right, right? Yeah, I was imagining

basically having the web control. Web control using a plain wiki and then using the unplanned web control that would sock it into the into the evaluator. But yeah, so the application that's actually running from, it's just a plain old wiki type application using JavaScript to go out there and hit them at interpreters,

not elegant.

All that, just for an index or free text editing I

the current one is just so beautiful and curated nicely that it wouldn't be equivalent to that wouldn't be as nice. And it would also be nice to be able to point it towards more or point it have a little scroll pull down that would point it to whatever interpreter that you wanted.

Vitaly, I wanted to ask you if you had a chance to look more deeply into the issue. I just pasted on the

on the chat,

because it seems that it says the like the next most important issue as far as reasoning is concerned.

Okay, you actually, I'm sorry, yeah, I was, I have to take, like, couple of weeks.

Yeah, I actually forgot about this. CQ, CPS, I promised you to look at it and let me look at it right. So if you response,

okay, thank you. So, yeah, and if you say, if you see that, you can outsource some of the work to me. I'm happy to, I'm happy to try to solve it. I mean, you see what I mean, under, under your guidance or something. So to not, do not lean it entirely on your shoulders.

Yeah, okay. Thank you for so interesting. I can ask.

Well, I have 96 function names here identified from our current Prolog implementation.

Yeah, I think at least 90 of those or 80 of those are from the standard Nether language

that are shared amongst all the interpreters

because it's too big to paste into the chat.

We did go through all the rust code and Python code and everything, and found he did. Renee did, finding all the meta functions that were implemented everywhere. I mean, that were part of the built in.

But then, not very long ago, vilis did the standard lib meta files, and then a ton of them are all in there. Anyway. Now we have to gravel so hard to find them all.

Yeah, there's some that would be nice if they were part of the standard meta language. And while I was imagining some sort of a wiki that was curated, is so that way, if everyone really wanted a function added to the language, they could put it in there and document it and discuss it easier. I

You okay, maybe

we can discuss, I mean, as far as you know, an exchange, mean, organizer, so to speak, the metal on the dev site, and knows the team who drives it, so maybe we can discuss with him adding some how To better, how to add such we can better do. Home,

I feel like Adam's Adam has a couple, or added a few, like intersection, unique and so forth, we all, I know he just added them to the Russ code, which was, was cool. I

It's a pity you cannot paste an image into the into the chat. You

may be able to share your screen if you want to show something specific,

if you can share your screen. I think. I mean, yeah,

okay, what's up? What's it? Go home. Do?

If you want a list, if you want to have a list of all the function names, it's here. Do

so the question was, can we have a list of all the functions which I implemented? What this is part of it. This is part of it.

I I

could post them, post them somewhere, but would be better if it's in a nice wiki.

Yeah, we also need to know what the functions do, of course. So that would be with where, yeah, I think this doesn't matter. Also, some material documentation that could be got from was that still in the way

from this? Yes, it is very definitely, for example. Well, here we I began with filter atom, and this is the current Prolog implementation. And here I have created all kinds of default but the default test, and now I have to write the documentation file. Actually, I would like to know if this is a list or what, whatever can be inside here. So then I can can make the full document description.

The unspoken hint secret is, is a lot of this is in standard lib, dot, meta, some of these, a lot of these, like this, filter Adam, I think, is in there with some documentation parameters that will tell us what the

which is. It's hit. It is here, yeah.

But a lot of times we're using atom in a Pro does? We don't know what Adam means. It could mean an expression. Sometimes it could be something that's evaluated.

Yes, here, here, there is an example right to fulfill the atom call and but you can call it in this way, but you could call, could call it also in this way, if you remove the super Pose, but then it will yield complete different results. I

Yeah, superpose is kind of a combinator across functions, right? So you do get very different results, interspeed spearing, that's anywhere the I think the nicest way is currently in in minimal meta, where it just, it just like a list, right? Like it's a map this on every item of the list, instead of doing it on the expression itself. Perhaps the what is really confusing to me, at least, is the how that like operates with lazy evaluation and literal evaluation.

Yeah, yes, because here, here you can see a screen. Well, this is the metalog implementation. And now I can, you can, if you see the last line is the last command of filter atom, if I run enter, it will give me this trace. Well, I'm the beginner, beginner of the language. So I'm trying to understand this trace so that I can understand the language. So I'm still into that. I would like to understand this trace. I

then I give a semicolon for all the solutions. But basically when it begins, it begins a file superposed to superpose to where it goes, maybe to fight.

But this is a trace, but it's three times the same trace.

Yeah, that looks like a bug in metalog, right there in the way. So it is sort of a big question, if the so when I can see when filter atom was written, atom, the idea was to apply the arguments into the variable, like to evaluate that, take whatever the iterative binding was, put it into that variable, and then chain its way along, versus actually mapping the list. So super pose itself would have to be there. But the way this is evaluating, the way why I'm looking at this here, this looks like there's an error in my implementation. I can already see that. But I think the way, the way you had

implemented, if you go back and look at the dot meta file, you can see it's sort of mapping the same way that intersection is mapping right like, what was that originally was superposed supposed to be around it?

I'm not sure. Well,

superposed is not supposed to be around so, like current form, which is on the screen, I know, hit the items and expression something, or filter expression this, which is supposed to be used called structure,

yeah, so you're breaking The head off the list in the decons expression and then processing the head and then recursively going through. I see

that's actually I wrote this function because I needed some point to implement in minimal net interpreter. I need this functionality inside implementation, and I wrote it after that. I like implementation rust and the solution it was, it became just part of some strike without using,

yeah, because this is, this is the standard Document Description And, and this is, this is the minimum, minimalistic meta implementation,

right?

I have to, I'm trying to understand this with eval and always with chain. But is every is it needed to describe every function as the as the minimal in the minimal implementation,

I liked, I like practice there, because it's sort of like a reference to, know, ah, that's how it really is supposed to work, right? It's implemented in Rust, right? Oh, if this was supposed to be an exposed public function. You know, not like map atom would be, but maybe not filter out, right?

Because, if

we would trade it, this is filter atom. Here we are backed this Prolog implementation. Well, it's only one line, but because the PROLOG is so free for all the arguments, it's not clear what kind of types this can be, any kind of type. So the PROLOG could be written in such a way that it's it could detect in the trace the variable types which it could accept, and then you you would have also your Document Description ready. Do.

And there is still to come a Prolog to meta transpiler. So then it, then it could generate, is

that would be the hope it would be that would become elegant looking meta. I

have to jump off in a minute, but I want to share real quickly that we implemented like fast loading of JSON and CSV into Merck, and we already had serialization to meta. So in in practice, we now have a JSON to meta and CSV to meta converter that's that's very scalable, and on top of that, as as an Lynne shared like there are already, like some Python examples with or some Python translations which are much richer in nature. All of this is to say that we may want to discuss at some point what are good canonical embeddings of these popular file formats in meta? And then the second point to discuss is drivers for databases, for example, running SQL queries from within meta and directly importing data that way, instead of having to go through the file formats, which going through files is already a bit yoke, if, if you're talking about, like very, very large or scientific data sets, where mostly you don't need all The data, you want some slices of the data, and you want that in a in a way that's specifically nice for meta. Quick results show that the we can load about 120 million atoms in about 200 seconds in morrick, from from Jason,

it's way faster in JSON than it is in S expressions, right?

Yeah, the our s expression parser actually couldn't handle like because there is no the meta formats doesn't have a spec on how to handle escapes. Are like different metapartures, different things. So that's not a suitable format for large data. It may be a suitable format for for code that people write. But if you're talking about, like, new complex numerics, or you're talking about strings and all their elegances, then you definitely want something with a specification or saying, Oh, we are copying this specification, the morgue serializer for meta uses the rusts, escapes.

Don't feel bad. I have the same problem as you do. My native format is 1000 times faster than the S expression format, just like your JSON, is 1000 times faster.

Oh yeah, Jason is definitely not a not a fast thing for me, but it is the kind of the industry standards, unfortunately, in a lot of scientific fields.

It's been highly optimized.

Well, I wrote my own JSON parser for so I didn't have to go to the intermediate layer.

Yeah. Anyways, that's something to discuss. What are the canonical embeddings? And I feel like this has to be informed by what yields good queries, or what yields goods transform or match statements over these, because nobody wants to use the data how it sparse. It's always like transforming, transforming until it has the right shape for the queries that you're interested in, and it's naturally fits your problem.

And Andre said I shared that sentiment too, that he wants a canonical form of of meta where everything is on one line, if it's a meta statement, it's on a single line, no comments anywhere, and then he we can just grab right through if he wants to pick and choose, like you said, take the first half or take some out and leave some of it behind. It would be easier to do.

And even new lines aren't the best way to do it. Right if you want parallelism, you actually want to have indicators of like here, the next 100,000 atoms are stored in this byte slice, which, like a lot of the binary formats deal with, is where they they don't just go left to right, but they actually have skip ahead pointers In them, and this is really what you need for for larger data, which we are dealing with, right? Like I was working with Robert house, his files, and I was working with Abdou files, and those are files that you don't want in a plain text formats loading serially. You want to load this from from a standard format. And if it's not like if it's not a standard plain text format, it's like a standard database or a standard way of interacting with it?

Yeah, I'd like, I like that idea, what you said, the idea that we'd be able to load and store meta into some sort of a remote database, and we have a standard way that we're all doing that, so we could cherry pick the meta that we're pulling in.

Yeah, perhaps, like, the good way to go about this is, like, specify a very small API for an SQL driver or something, or a sparkle mapping or something along those lines. Cool, I have to jump off. Thanks. I

Isn't there some kind of a file system that is sort of like peer to peer that we that singularity nets talked about. It's not like a particular product or anything, or a feature product. There's some sort of a, I forget the name, what they called it, but Alexey is usually one that mentions it interplanetary

file system or no, you're not talking about that. I suppose

it's like when you you were asking him a question one day and he says, Oh, that would be kept in our blah, blah file system. When you were asking him, No, it was,

was it about the marketplace, or it

was, it was adjacent to the marketplace? Yeah, I didn't think so.

So, I mean, what I was mentioning is IPFS, but that's the closest thing that fits the description you were. Yeah, writing it

does, and we're talking about the Python SDK, or the meta SDK, and those with you, where those files are kept,

right, yeah, yes, that's

um, yeah,

yeah. I think that's exactly how it works. Yeah. It's not kept in the smart contract. It's kept the smart contract only gives pointers to IPFS, yeah,

hash keys.

Oh yeah, because it's like expensive to keep a lot of data inside a smart contract. There is, there's decision to keep the data, like service map information on the IPFS and keeps the IPFS URI URI inside contract to the point

so the IPFS would be something like, I would have a server that would give out the files, but someone have to know to come to me To get them and but I would stick that into the shared thingy that everyone looks at, and that's like a

directory of IPFS files. So how that works?

I believe it's usually your requesting file through the server, is through the one of the servers, and in case of platform, is our own instance of IPFS server, IPFS mode. I'm

not

sure, because I didn't dive deep into the protocol, but IPFS knows should be able to exchange information about which which files they kept between each other. I believe it's it should work something like this, if you're looking for a file which is not on like exactly note you're asking for it, this note can provide to you the note which has this file. So for this, actually, I almost don't know, but the idea Bogdanov,

okay, but, I mean, it just asks my question. So like every little bit byte of the file is stored in this fragmented, crazy way on the on the blockchain, it's literally just addresses, and the files are stored someplace in the real world, separate,

yeah, yes.

I believe each time some note gets a file, it also can start to share the file, like in guitar. But I usually, I believe it doesn't do it by by fragments, but just shares the information that files, okay, the tools, no, you can get it from. I

I guess we're gone over time, but I was wondering about the catalog system that I saw you guys implemented in the Rust code. Is that supposed to be where you Well, here you add a GitHub repository into the catalog, or is catalog different than the Git stuff? Git stuff?

Sorry, that was probably, I don't really understand when you're talking about catalog.

Yeah, me neither. I don't understand what you mean by catalog. Yeah,

this,

oh, maybe that's a question for Luke. The catalog system. I saw that the rust code had some get module API now to be able to mount a remote get repository into the module system that matter.

Okay, sorry, that was, yeah. You're talking about meta modules, catalogs, okay,

actually,

yeah. So we can use some GitHub here as a catalog of meta modules which are which can be also located on GitHub. Actually, it was idea. I mean, the idea was to allow users publish, to publish the modules as a GitHub using GitHub repositories. So in the second level is the catalog of modules is published as a GitHub repository. It is implemented. So the implementation is called, as you mentioned, and yeah, we have some catalog. If it's it's probably almost empty. It is published on GitHub,

so there's no metamoto, maybe, maybe today's metamoto,

I can find something

I believe it's more for, like, mounting something like the chainer into making it to where everyone has a copy of the chainer because it gets put into the catalog and then so it's almost like a packaging system. And what my kind of, my question was going to be is, is, how adopted, how far along is that going to go? Is? And like, how like, like, is it 15% complete, and then it may not

go all the way to 100% or is it like 95% complete? And now we want every interpreter to use it.

Okay? Actually, Luke bettorson is not here right now. I believe was pre maintained, and it's mainly his design, I would say, like it should be ready about 70% ready. But, yeah, I think we can start using it. I mean, we should start using it and find out whether usable or not, whether it's convenient for people to use it or not something like this and make some I mean, find issues, fix issues, maybe redesign it. If it's needed. I don't think it is path to support it in a current way shouldn't be hard. I don't think it will be radically changed somehow in the future. So, yeah, it is why I'm saying that it is 70% three. So just answers your question. Questions. I

I believe we can try to write, I mean, look, try to write some specification in code, readme files. It's inside hyper experimental report, but, yeah, we could try to write it as a separate document to to be able to discuss you. Potential projects.

It's very cool system, like, I like, you know, I like the idea of having an entire meta space that just tracks these catalogs. And we have so I can minimal or rust meta right now we have, like, a catalog space called catalog, and then we can, like, import repository URLs there, and then there, at some point, there would be a thing that would mount those so, like, and that's a very cool way of doing it. Yeah,

so,

yeah, my my question was, like, it was she did answers like, Yeah, we like it. We're gonna see how far it goes. It's 70% done. And,

yeah, i Hmm,

yes, the idea must not reinvent the package system exactly as you say, just use something already. Unfortunately, you'd GitHub from the rust code is a really tricky thing if you want to. I unfortunately. GitHub uses, I mean, not unfortunately, but GitHub uses SSA library, and it uses compression library, and compile package, and I mean say link in the Python packages which have the Git functionality embedded is really, oh, it's better than BigQuery, yeah, so I mean, in last it's relatively easier. But this, our Python integration is written in C

plus, plus, we need to compile Python API and link it to be a different libraries and a specialist cross platform language, it doesn't work very well, so you should compile somehow compile cross platform Binary.

So it's a one way relationship between Python and rust. You need a two way relationship.

Okay, so I would say using Git is a cool idea, but yes, hard part is to embed git functionality into application and keep it cost portfolio.

That's funny. So the Python version is is more complete as far as being able to talk to GitHub and stuff, and so you'd have to expose it through G plus plus bindings that make it Russ be able to command and control the Python library better. You're saying,

Well, I mean, the main functionality is implemented inside rust Coco library, and maybe I just explained it not very correctly previously, When you're using the rust core library from Python, you Yeah. So when you're making the Python distribution package, you need to put some binary inside it which can be distributed and work on all platforms where Python works, so it has one dimension so different computation, I mean CPU platforms like arm x86 MIPS or something like This. And another dimension is different leap versions and different Linux or UX versions. So it's actually difficult to compile one binary or a set of binaries which will support all these platforms, because each platform has different level of support. I mean, supports different versions of SSL, SSL library. Okay, so it's, it's kind of, so kind of linkage problem, which is not on the surface.

Just because you can solve it once doesn't mean you're gonna, you just solved it for every place. It's kind of what you're saying, like there could be also, maybe you may at work this week, but it's not going to work on Windows. I mean, just different, yeah,

because, because it's just like the proper version of this, for example. And, yeah, actually, usually people use Git just calling the executable from the from, from, from the application. So if you have an application which should use Git, you either ask user to perform your comments, uh, Git comments,

right, the executing show commands, which is fine and no, they work because they're the right ones, because we install the right version of Git. Yeah,

but we me and Luke decided to embed git library inside rascal, because at the first ones, it seems nice solution, but it turned out that it is not easy solution, because Python, because it's not cross platform. So for the rust it is not a problem, because rust application usually is compiled. So when you, when someone installs rust application, it just gives the rust code that compiled, compiles it for for its platform. So I who's a Python your distributions are precompiled binaries, and you need to compile some limerels. Let

me see makes sense. That leads to the other question I have. When we do the we have functions like pi list and pi pupil and stuff, and the return type right now is undefined. Should we have a type like called PI object, or some type that says I'm from elsewhere,

yeah? Problem, yeah, I would say, so it's better to to have some specific type of them, this particular functions, and actually, there are few others, it should simplify for the users. I it was a Alexei, maybe, maybe to implement some meta API for manipulation, manipulation by Python objects, because,

well, you have to, if you're going to call Python code from rust, you have to give a Python list, and Not a rust

list. Yeah. So yeah, they they implemented, I believe, so again, remember few different functions which instantiate and perhaps atoms into the Python, Python primitive. So Python types? Well, yeah, I'm not sure why they didn't use specific type for this functions. Maybe it's, maybe it's, it doesn't work somehow, I'm not sure, but probably just because, like, it was a straightforward way to use any file here. But maybe, maybe there are some difficulties. You can ask Alexey, I believe he knows this, this API, because I even think just it

would seem like some like pytorch and the NumPy arrays and all those things should have a return type, you know, that we would recognize definitely, I mean, that that would be part of it, the quite, you know, yeah,

yeah, yeah. I believe so. Most of this was a permitted by Alexey, maybe for example, MPI library or integration. He just implemented this as like, as quick as possible, just to demonstrate how to do it. But maybe it is a reason why he did not use topics.

Also, it's a very, very mighty answer question to answer. Like, should we, you know, have a special type for foreign objects, like,

and, I mean, like, you can just flip a coin, like, the answer is probably too important to solve in, like, one thought paragraph or something, and that's probably why you didn't, you know, could have been, I mean, could have been

like, I no one feels like they would have the right answer immediately there to ask sometimes what to do. And then those cases we just sort of leave it to be done later.

Yeah, kind of what, actually, some kind, some part of the Python API has prototypes, and one reason for this is to make it possible using Python primitives from the rust quote or vice versa. Yeah. And so, yeah, I believe heaven types should be better than not having them. I'm sure why, but you always need to look at the specific case. Need to find out why this year was made. Maybe it is because, as I said, it doesn't work another way or something. Because, for some I mean, for the complex Python types, it is not possible to convert some dirty crimps rust, and you need to if you want to manipulate them from rust, your manipulates them.

I mean, from the rust you see them as a block box, bug boxes, but I don't see why it prevalence, but properly typing. So,

yeah, I always tempted to want to have Git type call the actual type off the Python object, you know, that's physically there in the PI Interface, you know, and then suddenly we have, like, 1000 new types because of 1000 types of objects are sitting around in Python, you know. And that wouldn't be horrible, but It would be one possibility I

Yeah, so I'll ask that in the meta coders channel and see if we get discussion, because I want to be able to do a get type on these, and not, you know, just return undefined, because I feel like it's users are going to want something to know that it's

not undefeated. Maybe, maybe somehow Alexis is that there are some types. I mean, kind of type system implementation is too restrictive to express this types properly. I'm not sure.

So, yeah, but it was actually

I got another meeting, so I got to jump off. Thank you.

Thank you So Kim, if there are no other questions, we can probably this meeting.

Thank you, everyone. Great. Let me talk. Thank you.

Thank you so

much. Everyone. Have a good weekend.

Thank You.

Thank you. Thank you. Bye,

How accurate was this transcription?

0:00:001:40:03

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5