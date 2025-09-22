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

Jul 26, 2024 at 7:53 am

1 hr 23 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), Lake Watkins

Summary

Transcript

## Keywords

meta, minimal, interpreter, docker, python, work, build, write, run, files, rust, empty, question, test, repository, change, issue, conan, faster, result

## Speakers

Vitaly (51%), Douglas (18%), Speaker 1 (9%), Speaker 2 (5%), Speaker 3 (3%), Speaker 4 (3%), Speaker 5 (3%), Matthew (3%), Speaker 6 (2%), Speaker 7 (2%), Speaker 8 (1%), Speaker 9 (1%), Speaker 10 (<1%), Douglas (<1%)

I guess, sorry, some sound system machine

Ali, a few new people joining today. I

Okay, see you, Mike in Seattle in a couple of weeks.

Yeah, right. It's kind of early for me just getting my coffee Right.

Give a couple more minutes for Any latecomers. I

can we Get Started? No,

oh, well, yeah, sure. So

Roy, I don't think I've seen you here before, or Mike or Marshawn, I don't know Blake if you were here last time,

once before right now, definitely my first, definitely my first time. I was talking with Douglas miles last week about this,

well, a little bit about yourself, maybe Roy.

Okay. So, yeah, yeah. So yeah. As I say, I've been talking to Douglas amante with being involved with helping with the project. I come from a background of what's been the last 20 years in C plus, plus, but I've I experienced the PROLOG Haskell and mercury and so meta sounds kind of interesting, and I'm basically come not known very much, and wanted to learn more about it. And the accents New Zealand. Accents New Zealand, by the way, if you're gonna ask that, cool, yeah, so I'm here to learn

couple Words. Mike,

oh, sorry I was writing something down. I thing. My background in symbolic AI Lisp, done Lisp and prolog, and had an expert system in clips. But so far with meta, is that how you pronounce

it okay? To interpretation, right? I think the idea was meta, okay, that was before Facebook rebranded itself. It's meta. But okay,

well, I've heard a couple of lectures, you know, from at the AGI conferences, and have yesterday I spent a couple of hours studying it and it, you know, look, it's starting to kind of, you know, dawn on me that, you know, the program and the data structure is pretty much the same thing. So at least I got that far and, you know, with some of the basic primitives. But I think I'm just going to keep a low profile here and try to follow along. And Sean, yeah,

also got a little bit of a background in symbolic AI, going back with my school days working kind of general software development. Since more experience with Lisp than prolog, started digging this, some of the documentation meta here, and it looks really interesting. I'm happy to be here to learn and pick up more

Sebastian, we heard from you before. So, and How's it coming along? Just and then we'll get started. Uh, any. Any questions that have arisen in the last since last time, or questions for them from the new EBS or from not newbies. Not

a lot on the meta front. For me, I was working on my chat bot. I almost had to reflect on a lot of things. So now, now I implemented meta as an intermediary layer so that you can ask a question, it gets transcribed and then turned into atoms with a very similar protest provided by vitally and then, yeah, it can get fed back into chat GPT, or any locally running more large language model, maybe for and then, and then parsed by meta, but I'm trying to use it for making The model more agentic. So I was so I was changing the building an event driven architecture where, where basically upon every event, it has to determine whether or not to call a command. So I have type of commands defined, and then it basically just has to, it has to compose two functions. But it's a work in progress still, so it cannot really show you, show you the results, because it's been mainly spending a lot of time networking, like, you know, setting up infrastructure, and not a lot of, not a lot of real meta programming. But, yeah, happy to see what you guys have come up with this week.

That sounds very interesting and apropos longer term, definitely.

So not so much on the foundations this time, but looking to implement it and see if something useful can be made out of it. I

anyone else? Blake, no

sure. I'm also looking to make something useful with meta. My interest is in games. Primarily. I come from a like a Game Dev C background, primarily, not too much experience with these functional languages, but I am trying to learn. So hopefully I can pick up something from this study group and apply it to some of these projects and work on

no questions. Up to that point, I'm sure nil will have questions. He always does. So

anyone, please, please go.

I didn't catch that. I

any difficulties that anyone's encountering. I questions.

Questions and

comments for tally.

I just wanted to say that since last time we added link to the meta tutorials and documentation to the repository, it was not published before, probably in the replay at least. But right now with this, we can just get it met with this link to this site with tutorials, you can try met the interpreter from the browser so it has some playground or running metronome, page,

story, maybe in chat. Yeah, okay,

yeah, sure. I was on the impression Alexey published it before, but it looks like at least

it was also wide. I have

a question about the browser implementation. Is that, is that running in the web, assembly runtime

or or connected to the server. Oh,

okay, nice question, actually, yeah. We like we are looking to implement it using wasm right now it is implement just as a server side interpreter which gets requests from the user browser and runs it and returns answer back, but, yeah, actually, we are looking for implementing it as a wasm project. Rust can be compiled to wasm, but, and actually core meta interpreter can be compiled without any issues, but you anyway, need some template like not complete, sorry, intermediate code which can write and read. Sorry, if my mic is low, I can No, okay, okay, so, yeah, to integrate wasm program with a browser, we need to write some like intermediate layer which replaces inputoutput by interacting with browser objects. So yeah, it's work, actually. Alex. He asked me to look at this direction about months, probably more ago. Unfortunately, I didn't have enough time to look at it. But yeah, actually right now I was going to think about it more deeply. So yeah, unfortunately, it is not just like you cannot just get, like a big, big because project compiled into the vast one round in browser as fire Sam, so you Need to integrate it with the browser object model. So

and also there is Adam vandervorst, who was like, talk about me on the previous meeting. Adam has a skull implementation, skull prototype. Which I believe also he said he somehow converted, converted to was more something like this. I'm not sure about details. You can ask him, it is not fully compatible with hyper and experimental and like they have a bit different semantics, because Adam actually wrote it as a prototype, mostly, and but yeah, You still can run some metaproj on it. Okay,

Marty has a question about parenting, invoking meta from the command line. I mean, there's a when you build, well, when you build hyper, own experimental you you should have a meta executable that you can just call pass your Metis creaking argument, and it should run that. I don't know that.

Okay, do that.

I only, I

think I only partly installed the everything from I only partly did the GitHub instructions too. So,

in fact, yeah, I need to admit that setup of a project is kind of complex. I mean, at least it looks complex. Maybe it is not complex by itself. The hyperon experimental rep contains three different projects, or even four, actually, sorry, so two pure rust projects which can be built and run by cargo, absolutely without any issues, because rust build system is like self content. It doesn't require getting some binaries from outside. It just gets all sources, compiles it, and produces a single blob executable file. So, yeah, this rust, there is no such issues, and core library is written in rust, and second application is repo, which is also written and rust. But if you have, if you have to use Python integration, things gets more going to be more complex, because first meta integration with Python is done in two part, in two steps. First we created C API for meta. The reason is we was working for integrating meta, not only with Python, but with any other platforms which can be useful or usable by people. And thus, we wanted to create C API anyway, and it is created using also using rust build tools, C bind again, which can, like, just generate CPI from rust library. Okay? And second part is a Python integration to integrate Python with a native code, you need the C plus C plus plus Tampa line library. So Python project itself contains from two parts, contains two parts. First one is a C Plus Plus native library which is integrated with C API and rust core library, and second part is Python library itself. Okay? So if you don't need Python integration, the running method is pretty simple. You can just type cargo space run. That's all after calling the repository. If you need Python integration or C C API, then you need to build other two projects from the repository, repository. So to simplify these tasks, task, I tried to create some single CMake script, which should work like in the usual way your create, build folder, go into it, type CMake, like, up a directory And then make. And it should do the trick. But, yeah, unfortunately, there are many different things which this like native build system should do. Install dependencies. We have three dependencies, only three. But unfortunately, sometimes it is enough to break build. So build the C library, build the Python library, Python native library, and finally, after you build C library, it's vital native library you should install install Python library into your Python environment using Python packaging tool people. So I tried to make it as simple and as less surprising as possible. So to be like, not surprising for people who use c+ and Python. Well, he was possible. Should be used to do she make and make comments Python users probably should be, should use to install Python project with people. So it's kind of like I tried to make it clear enough for people without any, like, second tools. But yeah, recently there was like two issues reported about. Unfortunately, after writing the repo, we found out that rust, by all three integration is not really how to say when you build repo with Python enabled, Python fish enabled. It should actually be linked with Python library, but unfortunately, it is not. It is not hard link, so to speak. Not static link. Okay. It is dynamic link. And the RAS cargo or pyot Three system doesn't.

Was like, okay, but I wanted to say that this is one of the common reasons of when people cannot run project. But usually, if you have few different Python environments, and you trying to run APO with cargo run. It can on the stop. It can take incorrect Python library and that it is a known issue. Luke Peterson actually said that he's going to fix it to the beginning of the next week, so hopefully it will be fixed. But yeah, right now it is not fixed. So usually, after you install in Python library with peep, you have a Python meta executable not it is not executable file. It is a script which just starts Python interpreter of meta So, yeah, it should be after installation of the Python package, the meta common duo two should be available

to run scripts. Okay,

by the way, is the Docker file to date, because maybe it could be an easy alternative to build

the whole thing. Just build a Docker image. Okay? I usually I make a fresh Docker file on each release. Actually, after last release, there was a significant change in the repo, so I switched, I swapped two interpreters, like previously, the default interpreter was the last one. Now it is a minimal meta one which is much more accurate and faster. But unfortunately, this change is not published as a docker. Actually, I can publish it because I think it works it, and I can publish it just in a minute, I believe, like in few minutes, but yeah, all the Docker symmetries, I mean, at least latest release and latest tech. Docker tag should work well. Recently I did a lot of work to make Docker image smaller. It should take about like 100 megabytes right now. So it should be, it should be really small and fast. I mean, download more quickly so I can publish trust your as a docker. And yeah, read me. MD In the repo contains all instructions how to build Docker from the sources. If you need it, like if you need the latest version in the Docker, you can build it easily.

And yeah, you can just run the Docker from the Docker Hub. I

How I'm running the current Docker, and I can't figure out how to load meta files. What's the syntax for that? So I've been trying to note some knowledge graphs, and I've tried the import and the the other one, and I couldn't

get it to work.

So how to run file?

Files? Okay?

I was using the rebel. Okay.

Let me, let me type it. I will check that it worked, but yeah, I'm not sure. Okay, maybe I will just share my screen first i

Oh, okay. Could we see concern? Okay, let's see so

it should be allocates, not visible, probably right. Because two,

sorry, I have it quite big. Dog care for run minus means minus minus. Ram, it is just to not keep containers. Okay?

Let's say latest repo. Oh, maybe I don't have a latest version here. Yeah, it's not the latest versions I

Okay,

okay, to run repo, you can do this trick. Okay, I'm not sure right how to pass the parameters, because it should be inside the Docker. Yeah, you're right. Actually, probably the only way. I mean, I know that you can mount your folder inside the docket

before running. So, yeah, I did that. Yeah. I was doing both the import and the include, and tried to run either a folder full of meta files or just a file, and it would it was loading, but it says, what was it saying? Something about a grounded something. It would give a response, like it was doing something, but then I would search through it, I would do, like a query, and there was none of the

things that were entered were findable. Okay, so actually, yeah, like, there's

something with a probably, probably, yeah, I can answer it, but I need to see what, what meta Apple said about it, what was the issue, or at least the code, if you have one, if you can

test it, I can run

it right

here. If you can share a screen. Mike, yeah, let me try that

one second I

gotta do on My other Computer. I

Okay, can you hear me?

Yes, yep, okay, so I'm in the

so you're not,

you're not met a ripple.

Oh, right. And

then we need the space before

okay, there's that. And then, is there a way to, like, just dump the contents

of the atom space.

Get atoms you can, you can type

exclamation

Oh, get this, okay, exclamation mark, and get this atoms

and after that atom space, okay?

File,

yes,

let me check also I think include doesn't use the bang afterwards and doesn't take a space import does, though.

So we have include and import as two different ways, and I got the same response when I did import with them,

okay, yeah, but

is there a difference between include an import in terms of, yeah, there is include. Doesn't take a space just interesting. Does it take a space argument? Also, it doesn't have a bang. It's sort of like include text, what's the what's that

one?

Yeah, you can try to

give itself from here.

Yeah, that should work, and then you might take off the word meta

at The end. All right.

That supposedly works.

So try

this without the bang.

I keep doing that. Yeah,

actually, yeah. Try that one, yeah, oh, take out the self there. Sorry.

I think it goes to self. We'll find out where it goes. And exclamation marketing,

oh yeah, word Netta

afterwards,

yeah, so like that, supposedly, yeah,

okay,

that might have been equivalent, but we'll see.

Oh, there we go. Okay, okay,

so detail, but import returns the the empty tuple include

returns empty. Is that as an important difference or?

Okay, sorry, let me. Let me check the code, because here not me who wrote it down. Type, okay, it says it include. Okay, so include actually interprets the atom space which is included. So if there are some exclamation marks, it executes it then these atoms, and it returns the last result from the atom space included. I

Yeah, calling Mike, by the way, what's that? Oh, for the file separator, you'll want to use a colon,

because it's intact. Yeah, okay, oh, but then I can load

files from a folder.

Yeah? Yep.

Okay. Can I use like a

wild card to load a

bunch of folder, files from a folder?

Not yet, I wish. Okay.

Thanks. And what's the status with Das? I or is that? Is that still

not integration hasn't been worked out yet.

As far as I know, integration is here, but yeah, maybe it is not like it was not a good time, but one of the members of our team I lecture back off, is working on, like on meta module, which is which integrates does into the interpreter. There is like dust team, who constantly improves the dust itself. My impression was like this integration should work, but does the US itself doesn't, doesn't permit some important features. And so it's reason why Andre don't like

don't demonstrate

it yet. So,

yeah, I haven't been able to get that stuff to build yet. I may have something wrong with my Python stuff, but,

but, yeah, I know. I guess that's I understand. It's a different

team. So actually, they publish their call to the Python packages. You can just install them from the Pypi package.

Refugees, I believe? Yeah, I guess I hung up on trying to there's within the tools set up the local Docker system,

and that's where I was getting hung up. I

Yes, they have some complex setup.

So starting dust is not like I'm not sure how easy it is, but it was not a trivial task,

at least when I started

looking at it. Yeah, they're trying to run multiple Docker containers of Mongo and and Redis and make them all work together. And that was how many able to get that to work yet

on my system, yeah, I see, like we

have the example of

the is it hyper? Experimental repos, there is an example of dust integration test. Does matter. I believe it should work, but yeah, it requires some local dust setup, which itself is not easy. Probably maybe it is easy. I can ask

someone to write an instruction how to do it.

Okay, thanks. Maybe it is there. Maybe I just know, don't know about it, but aliak, as I said, it's a member of st visa web team, usually after each after das publishes next version, he usually downloads it and tested like for compatibility with current code and fix fixes

integrations that is needed. I and

Mike is asking, Is ampersand the reserved symbol? Well, I think I'm sure ampersand self

the first own space, right? Further meaning, I'm

not sure, yeah, okay, no, it was not reserved symbol.

Yeah, at all. We just pretend we, we use it to denote that this is like a global object in

the interpreter, or something, right? Visibly, yeah, yeah. It's like. Use it as some notation to say, like, like, some

stand up notation for the global objects, right? I

the minimal method is way faster. Now we noticed, or a couple people noticed, is, is it still using the text file, or is it some of it is now written in Rus, and some of it's in that

text file, right? Yeah. So it was like, how to say, straightforward idea to write part of the minimal meta interpreter, which is written in meta write which was written meta write, it in the rust. So, yeah, actually, I did it like because Alexey asked me to solve this performance well. So I was trying as well to write some new motor, format, Atom space implementation, but I didn't finish this work. I hope I will finish some future. But yeah, so minimal meta is

more performant, mainly because

the whole interpreter, yeah, wrote, and not, not the whole, actually, the like, most of the interpreter is a whole, is now and is written last Now, and, yeah, it's, it's important, performance, significantly. And actually it was how to say it, how to put it

like even previously, it was

more performant on a large, large scale scripts, I would say, but it was not visible because nobody tried to run it. I compared

performance for that like,

like, factorial is, big numbers, something like this, so, and I saw that asymptotically, minimal meta was faster than rust interpreter, the previous class interpreter, and right now, because, like the core interpreter, was like 50 time, times faster than previously it is. It can be seen so example. Recently, I tried to run examples from meta repository using node in the operator and minimum meta interpreter and minimal meta interpreter seven times faster than, for example, on this on the specific examples for seven times faster than philosophism,

all trust interpreters. So, yeah, yeah. Well, I store the I store these output files when I I run the test for metalog, and so I've been keep, I keep them in my repository. So I did a diff, and I know, so it's about three to six times faster than the old interpret, rust interpreter. So what I was doing is only running it the old rust interpreter to be able to get a performance, I mean, to get a test result comparison. Now I'm running minimal meta, and so I'm still able to see the old timing results from the time command. So I have these answer files, and the answer file gives me what the old answers were, plus it gives me the amount of time that it took. And so yeah, almost across the board, they're all four, three to six times faster

for this new minimal meta in the old question term,

yeah, sorry. Douglas amante to ask you so so now that minimal meta is the default. Did you get metalog to be 100% compatible with minimal meta, and if yes, did you? Did? You get a chance to compare the performance. So,

so, so I noticed that some of the answers for minimal meta was different than previously, like some of the tests that have different answers, it seems a little bit faster, but it doesn't seem like it's getting as many results as it used To. Like it's failing some tests that were written by Patrick. The new minimal meta is but I don't know yet if,

if we should turn in a bug or not on that. I wonder if that's due to the order superpose,

as far as I'm concerned, Oh, you're right. Yeah, there is some super post

order through the reverse right now. Yes, what I So, what I have observed, rather, what I have not observed, is any difference between the new minimum meta and the old minimal meta. But I'm not using any I'm not relying on any superposed

order. So that's why I'm one seeing an extra result in one case and then another case where we're using a void on a switch. Case used to be that you could define a default if none of us which the case statements are matched, we would use this thing called void that would say basically else case as a default case. And I noticed one of those sets weren't working. And this is on the new minimal meta, but this was a test was written by Patrick. So for, I mean, that's a, I mean, I don't know, no, actually, it would still work. It should still work anyway. So there's some changes. So this is where I was going, is it's harder for me to get a true evaluation and metalog now, because meta has different output answers by so I was getting like 96% now it's giving 88% and nothing's changed. Oh, 88% equivalent to minimal meta. So how it works is I run some tests and capture the output of both minimal meta and meta log. And before it was a 96% compatibility, now it's 88% I just have to go through and figure out what's changed. And then somehow update you vividly on what I think has changed. And then, because Patrick's tests are a little bit more than just our meta test. So, yeah, meta tests are part of hyper on experimental that we run the way runs, and I might run them and stuff, but then we have these extra tests that were created by Patrick, some were created by me, and we have to and so those are different than it was before, but we have to figure out if they're supposed to be Different, or if maybe they were wrong before now they're correct. So this was giving different answers into the month ago, but maybe the answers this month are more correct than they were two

months ago. So so

it's going to take a deeper look. But yeah, my answer was going to be, though, do you Neil, I think now it can improve. I'm going to it's still pretty fast. It's gotten a little bit faster, and

it's just not a lot of work has been done in the last three months on metallock. But

I have a lot of faith in what metalog is going to start doing in the next five months, because Ben's excited about having metalog, you know, also part of the interpreter that we're going to be using. I mean, we're going to do more if we're going to do hyper on experimental. But, yeah, I wish I could tell you Italy, you know, like, what's exactly different, but a couple Well, I know, like on the NARS test, we have an extra answer that we

didn't have before.

So

you Yeah, that that could also just be file loading, like we might have we're loading how we load our files. We might be loading the same definition twice, and so now there's going to be duplicate answered. It might not be anything wrong with the interpreter. It might just be how we load our dot meta files that changed also,

But it's definitely faster.

Okay, actually, thanks. Regarding case separation is definitely just incompatibility between previous interpreter and new interpreter. Like, actually, I'm not sure why may I mean, probably I could do it compatible, but me and Alexa, we agreed that we can otherwise make old and droplets compatible with minimal meta and then just move to the minimal net. So okay, instead of void, right now, one should use empty word, empty with capital,

okay, I will just type

it in the chat.

Thank you. Yeah. So it is because a minimum meta empty means empty result of the evaluation. Thus,

default branch. Sorry, it's like, yeah, I

think and so I was mistaken, not default branch, but when the result of evaluation is empty, you need to use empty keyboard.

Yeah, the symbol to match. Oh, and that's actually, I think, really, what's going on is it's always been returning empty, and so we've been using void, but now if we use

empty, we'll actually match it correctly. Yeah, yeah. So yes, one, one,

uncompatibility,

yeah. Oh, sorry about this. I didn't probably in nowhere. I patched the test in the repository, but, or maybe even, Alexi did it.

I don't remember, yeah

and yeah, it's also interesting,

like to know about this metallocut, yeah.

Oh, what? So a question that I have is not NLP, we have a couple types of knobs, no operations. One is you can put it around a form, and no matter if it was the form evaluated to correct or to true or no matter what, it always returns. Now my question

empty or does it return

nothing? Minimal method returns empty. Minimal method, it turns empty, but matter meta semantics here, I would say, you know, change. So, for example, let right, he or not not, let on match, in minimal method that is a similar iteration unified, which actually has two arguments, one to return when two atoms can be unified and one to return when two atoms cannot be unified. So and match is just returns result only when two atoms can be unified and usually cannot be returns like empty result, but not empty symbol. Inside minimal method, one will receive empty symbol, and you can handle this situation like I did in the interpreter, actually, but if you write in meta, unfortunately, it will be convert to the empty result before return to user to be compatible with previous data semantics. Actually,

it's interesting question how

to, like, whether we want to migrate to this, like make meta more more, like minimal meta or not. I think we need to discuss. We can discuss it probably see, but actually, as I understand at the moment, he

he's more busy with

other things, so

like compiler and

semantics. Yeah, this has kind of been a long ongoing question. Are we going to use empty is or if we're going to return nothing, yeah, we have to eventually work this out, because some functions have to have a return. And so, um, and that's so, so, you know, like in case of a grounded function, the idea is, always will return something. And so we've been, yeah, having going

back and forth. Yeah, actually, I would say that it should be possible to write programs. It doesn't, it doesn't reach, okay, but,

yeah, you can probably,

using UniFi, you can write the programs which doesn't turn empty. I mean empty results, but

determine empty in such situations. So I totally agree with you. Yeah, I think, I think we have to be able to return both. You know, even that, even though it seems like they're changeable, in some cases, we're in the end, we're going to have to be able to do either one as we want to, especially because in a case where something is not going to return any results, let's say a sub query, it's going to be a lot faster. The interpreter is going to go faster

if we're able to say if we're not creating a

return in certain cases. In other words, yeah, I it's thoroughly clear in my head, but I don't know how to say it out loud, you know. So if you're aggregating two results together, you want to aggregate nothing and something, not

empty and something.

So in another log, I originally went with the original full meta on how it did something. And so we'll so like you're saying, goodly, we'll have minimal meta versus how non minimal meta does that. And so I'll have to pick one for metalog, and that's okay. If minimal meta becomes more the standard, I feel like it's a big deal to change some behavior to make it more compatible with minimal meta,

where I have to say about that, yeah, okay, but at least right now it is not,

I mean, no Clear file, some like moving to the minimal bit. I with,

like making meta more more community. I think that most important question here, it's like, how to

how to improve consumers, control, structure, constructions,

so Alexey worked on this for some time, tried to experimenting with different approaches, and wrote some programs in minimal met, as far as I understand, But unfortunately, I I didn't hear about some like clear results of it. So

not sure how to continue this. I

Yeah, something we can talk about

over a GitHub issue or

Something like we can find that stuff.

Yeah, yeah, well,

okay. Actually, I have published the latest

hyperm experimental state as a Docker image. So

hypergram 3j hyper and latest now points in the current state of the main branch of the airport.

This minimum methane input by default. So I guess there's a one question, is Python 10 point 11, or python three point 12. Yeah, is the Docker using the previous one, or the Docker is using, of course, one that works. But do both of them work? Or is it still just one of them that works?

Of the Python versions, python three dot 12 doesn't work. Let me check I have,

yeah, I read some issue on this. Don't remember what specific issues

call an exception. Okay,

maybe the problem is some I

uh, some common and compatibility. Okay, one, one more reason to migrate the corner to actually.

Okay. Just today I was like to get the native dependencies, we use Conan repository and Conan two. And from the beginning of the project, I was using Conan one, but right now they have a Conan two, two, I mean the second, second generation common variable tool is not fully compatible with previous version, and it is a reason why migration is not not trivial. I'm trying to migrate to it right now, like today, I was trying to build project using Conan common second version, and probably it should solve the incompatibility with python three, dot 12 issue. Unfortunately, the problem is that, well, Conan, first version was at least embeddable into cmakes. Conan, second version is more like external. Is proposed to be used as external to before, before building, you need to use Conan common line two to get dependencies and generate some CMake files. After that, you need point CMake to these files properly, and after that, you can build your project. I don't like it because it complicates build instructions and you cannot do it like from from your memory. You need to read it literally because they use some unusual CMake variables to encode quantum files, con files generated by column with dependencies. And mainly, I simplify this setup to one comment, maybe

two comments. So pretty much we like I probably have a Conan one profile sitting on my disk, you know, but so we have to, I mean, so I have to make so Conan two

might work with both pythons. Yeah, probably it works.

I'm not sure what, because I see the problem is Python, 12 is 312. Is some common package incompatibility. Ah, okay, maybe it's not common, but common package, sorry, right, okay,

yeah, some module is absent.

Okay, actually, Python itself is really annoying with like many, many

different complexities.

Yeah, 12 is also like concrete has has more as structure has a weird requirement when using PIP that 11 doesn't that's going to be going forward. I Yeah, so I ended up putting a different the last version of Ubuntu on my development systems of the newest

one, because the newest one ships with 12

which means people are not able to build the nearest hyper on with the nearest Ubuntu,

which is A pain.

Okay, um, excellent.

Okay, it's interesting. Maybe I got I was a way to search. So maybe it's more fundamental issue.

It's like clear yet

it's not really clear why 12 was really not working. It could be Conan, but

it might be something more. Yeah, I

so I guess Matt left for a different meeting. He's sort of our official,

yeah,

the meeting actually

me, Matt, Alexey, and Ben and

one more person, but Ben is here and said, if it's dropped now, and

we discussed it with Ben, and he said that probably his meeting should be canceled.

But I believe Matt knows that.

Okay? We have another meeting like this in two weeks, right?

We don't have one next. Yeah, I

Yeah, good. I invited three guests. I'm glad, glad they all showed up. Thank you Sean, Mike and

Roy, yeah, yeah. Thank you guys. Thank

you Douglas amante for inviting them.

Well, thanks for the invite.

I Yeah, thanks for the help, and

up to you in two weeks.

Yeah, thanks. Vitaly, yeah. Actually, I see if you have any questions or like difficulties, please feel free to fail an issue. For example, I'm not very responsive in chats usually, but I mean matter most, for instance, but because I rely on meta most email notifications, and they actually are not reliable, unfortunately, but you can always fail the issue, and I will answer if it's like easy, if it's not easy, then we can discuss it here so well. Thank you for using please share your experience.

Ask questions, feel free. I

Sorry, what channel on matter

most is the best one for keeping in touch. Okay, there are a few channels. Metacoding group is also have some channel.

Okay, let me, let me share them

with the styling group. Probably okay. We have meta coders,

and it is probably the best one

to share the experience like, like it is more most,

boy, I shared the link in the chat,

probably for questions like beginning of slide questions, or I don't know how to do this. Don't know why it doesn't work. It's like, doesn't seems like bug. It is the best channel to post such issues. We also have hyper role, which is more,

not general.

Let's see. I'll see about getting insights to to three guys to get on the matter most.

I think the public

server is

not a big deal.

I mean, it's big guilt. I

don't know if I have to ask anyone. I don't think I do.

Change the AB store. We were also discontented with Redis

and open source licensing

was a joke in the iron channel. It says a spatial value store. So you are also discontented with the Redis and things to try to make

your own competitive. Okay, so?

Okay, there is also meta study group channel, but it seems

okay. It's also relief. I

Okay,

if nothing else, we can finish the meeting. Thank you. I hope I don't know if I was muted when I mentioned I'll get the three guys invites to the server as well. Was I muted?

No, okay, good.

I think I heard you. Yeah. All right, well, take care. Everyone.

Great

meeting. Well, thank You.

Thank You. Thank You.

0:00:001:23:53

AI Chat

Outline

Comments