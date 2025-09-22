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

Feb 21 at 7:32 am

1 hr 10 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

MeTTa issues, memory optimization, Windows support, type checking, new users, Hack India, project building, functional language, debugging tools, backward chaining, knowledge space, proof search, lambda functions, Python integration, tutorial resources

## Speakers

Vitaly (44%), Matthew (20%), Speaker 1 (19%), Speaker 2 (8%), Speaker 3 (6%), Speaker 4 (1%), Speaker 5 (<1%), Speaker 6 (<1%), Speaker 7 (<1%)

Hi, everyone, hello, hi,

nil, usually Unique slides And

Okay, Thank

oh and so, I guess five pass so

get started. I don't know if there's anyone here who has questions issues that they've encountered in in with MeTTa during This last week, anything they Want to talk About, I

anyone I

you encounter any problems or issues from On?

Well, I did have some issues, but I

don't really have a nice example to show that of headaches, so I just wrote my own. But that means I threw out all the examples where it failed. I I

should have put them so much to the side.

The nil usually has somebody he's not here and said he's not here, people who usually bring up questions and issues

are not here.

Anything new from Alexey or Vitaly about MeTTa, things that have changed over the last week, a couple of weeks, or,

okay, I can, can try to make Some brief data probably, I mean, the most, most important, thing was published by I'm not sure it was published already, but at least I gave Alexey to Alexey text with different items which were implemented Last month and was recently added into the code base. So the main item is more compact, Adam space representation in memory. So I think it should be compact enough to try some by atom space databases to try loading them, at least, I used some example from the small, small piece of data from the BIOS Based on space and, yeah, it was, like about 100 times smaller than previous versions. So like about 200 megabytes text file was loaded into memory and took about 40 megabytes of memory, operating memory, and it almost have to know atom duplicates, About 40 million atoms. So to be effective enough storage for large amount of data. Also,

we work on supporting Windows as a platform, so we already have some progress in it, but, like, relatively, I mean, most of the work, I would say, is done, but there are a couple of issues with dynamical In library, so we are working on them. Now, generally you can build hyper all experimental. We will be able to build hyper experimental on videos, perform, I believe we will finish this during next few weeks. And new raised, actually major issue about type checking performance. There are some cases, I mean, if you're trying to type check or get type from the way, big nested expression, I mean expression, it has a lot of nest levels will be enormous, slow. So I investigated the issue and found the cause. But yeah, and has already has some improvements, but not, I mean, not this work completely, so I'm going to finish it next week and somehow improve the performance. I believe it should improve a lot of cases, for example, cases which were raised by Patrick, as far as remember about smallness of restaration and so, yeah, I believe it's the same issue. Actually. Nil just found the example,

but it demonstrates it's so I'm trying to fix it. I believe this is a major updates about hyper experimental development. So yeah, there are a few issues we discussed in the MeTTa most about it, but yeah, they're relatively small compared to these items, I believe, I think I will try to work on some of the issue, type, check optimization.

That's it. Okay. Thank you. Perhaps maybe let's take this a little bit different direction than than usual. There's some new people here joining, joining singularity net and and then there's also people from the hack India. If I'm just

in case,

go ahead. Raman.

I reproduced my error I had. So I can show the code if you want.

Okay, maybe in a bit that could be useful. Roman, okay, I want to kind of take this and so for the I don't know how many new people there are here who've never been I know a couple at least, who've probably never seen MeTTa before. Do uh, and so that's what. So maybe a and I know for the hack India that that is coming up very quickly, yes. And so maybe ideas of how to get started learning MeTTa and and then once we've gone through some of that, that would be a good place Roman so you can show code and kind of explain things as well. If that makes sense, sure. And so suggestions, yeah, how do you pronounce your name? It

is Apurva. Apoorva. Yeah, it's a bit difficult to pronounce.

But yeah, you wanted to Yeah,

so, so for hack India, we're very excited to introduce MeTTa in this part, essentially, a lot of AI development that happens in India happens on using Python, and you it's usually a CNN, RNN, and a little bit of LMS that happens. But, yeah, a language like MeTTa, I think students are very curious to understand it. But again, the main challenge and the main aspect, which I feel should be tackled, would be good resources, and they learn the language while building something, because usually otherwise, it's like a tutorial Hell, where they just try to learn the language first and then try to build something. It's better that they have a project set up, or some idea set up, and then they use meta to build that project. So for hack India as well, that was my thoughts.

Excuse me. So the question is, what is important to learn MeTTa?

Essentially, they've not seen MeTTa at all. Right.

Did couple of people know about it? Very basics of it, but no, I mean, it's in a very initial stage, so it's gonna be essentially from scratch with a lot of people.

So I mean, there is the MeTTa Leung, MeTTa, iPhone, Lang, dot Dev, I got that right. I think as a starting point with some tutorials for for the LL, M Ms, there's MeTTa Moto, or MeTTa motto, however you pronounce it. Any other ideas, Vitaly or or Alexey to get to get started with they're going to be tackling some, some problems that we're actually defining right now.

Well, yeah, in general, like the first start point is MeTTa link, the depth I share the link in the chat here, and also met the repository which also have this link, actually this link which is inputted into the replay description. So also there is a MeTTa example site

which

has a lot of, maybe some, at least some number of more complex examples. So usually I mean metal and Def has small code snippets which demonstrate how to use language and write some code. Hyper experimental is actually specific implementation, one of the implementation at the moment, so historically, it's first. But it doesn't mean it's like it is the best one, but yeah, it built on rust and also has a price bitings. So it's actually very good integrate, very has very good integration with Python. You can write, you can embed MeTTa code into the Python program. Vice versa, you can embed Python code into the MeTTa programs. And there are some also not very big, but examples of this in as which are kept as a unit test. So you can look at the unit test of the Python part of the repo, and you will see some examples of Python Federation. Also, as I mentioned earlier, there is a MeTTa example which contains bigger programs, mostly written in MeTTa, but there are some personal examples, probably too. Yeah, it makes sense to probably just look at meta learning depths. If you need some more complex examples, look at many examples, many examples. That's it. I don't know what I can suggest. Also, there are some videos. They're probably old, relatively old. It's recordings of presentations made by Alexey about how MeTTa works. Maybe if you brief your the videos, source of information. You can look at some the links to the links are in the overview section of the hyper experimental report. So maybe I will just copy one of

the links.

I don't see the direct link to the video, but where is like? There is an open CoQ ipron website which also has some information about it, but I'm not sure if it was updated recently, probably, but

you had a question? Yeah, go ahead.

No questions. I'll go through the resources and share it so that people have a good starting point.

Okay, yeah. Also, there is a MeTTa coders, MeTTa static profile. We chose them as public one. MeTTa coders

may not matter most, yes, yeah,

so so

I can try to get access If I have names that's on the world channel I

does the team have access to the world server of matter most? Do you know the people involved with hack India?

Yes, yes, yes, I know. Nefertiti and Simon and couple of other people who are involved in the initiative,

okay, yeah, good, good.

So, and are they on the MeTTa study group channel? I think so they are.

Unfortunately, I'm not there. So how can I be added?

Okay, send, okay, if you send me your probably the information, your your email, I can request to have you added to the server, perfect and with the particular channels. And do you know, by you know how to get a hold of me, but M A T, T, Matt at Singularity net.io, and I, once I have that information all, I'll request it.

Sure. Sure. I'll do that ASAP. Yeah,

I probably have it because I probably have your actually, I probably have it beyond because I may have added you to this call. Otherwise, I'll just draw or I can look at the call and get it from there. Otherwise,

if that's interrupted in the chat box as well.

Okay, cool.

And maybe Roman now is a good time so that you can kind of the by looking at at some actual code and issues and things like that. You know, people who are new can begin to kind of understand a little bit about how the language works.

Sure. Okay, this is just a simple example where the built in fold function

fails to actually works like this, too, if I just I

I save, yeah, so that's the expected output, and now the same code that is in this function here, if I just put this directly in there, then we get nothing back. Just like confused me a little bit so and that at that point, I just wrote my own function. Then I don't have to have these extra variables there. I just can just call them directly.

So Robert, you mean, if you call the function, it works, right? If you selection by its body, it doesn't work,

yeah, the only thing that's added is like an extra let's

Statement two.

So, that is one extra led statement,

yes, at least to me, I, I can hear only part of your words. Some words are just disappearing.

Well, I would say it is better to write an issue on hyper and experimental about this behavior. I mean, I'm sure I will be able to answer it. Now, I think I need to look at the code execution here. Actually, I'm not sure how many people use faults. Well, it's surprisingly like Not, not, not useful not. I mean, it's not used very often. So maybe there are some bugs. I guess

it would be nice to have just lambda functions.

I know we probably already have some issue on this. On this topic, also feel free to just search issues if there is no such one, then for you like, then raise everyone about it. But yeah, you know about it, at some point I thought that it, it will be just simple addition into the MeTTa library, written in MeTTa, we have some examples of lambda functions in MeTTa examples repository. Let me share some observe.

Probably, yes, okay, unfortunately, there's no

okay, something like this. Maybe some files in the same gig, so as a person, same gig. Yeah, one issue is it that it requires to, I mean, at least straightforward way of doing it requires of 18. Adding some lambda definition for each entity so I didn't edit it into the library. Maybe it works even, I mean, even in this way, it was related into the MeTTa standard library, and people just can use different lambdas for different edit, probably, or we can write

some

other library definition, which will be universal. I didn't think about it deep enough, but probably we can do something like this, okay, but anyway, I

you can track by the way, you can try get the draft you finish from The example and try use it in your code. I

hopefully, that's of some use. Charlie. I don't know who else is new here. There might be others getting your name put off. Yes. So compared to Python, it MeTTa is more functional language. So that's quite a difference, right? You probably heard some of that come across in Romans.

Example, lower level code language similar to the difference between the dust as well. But yeah, I mean, I was able to understand bits and pieces of

it. Yeah.

Who else is new, just just for my I'm just curious. Yeah, see,

okay, any anything else today that anyone wants to talk about,

yeah, on, like a debugger or something, because, like, since it MeTTa, variables are values, sometimes it's really hard to figure out why something doesn't work.

Yeah, sorry. Okay, so, yeah, it's like, actually difficult issue for the language, which has, like, conception of, I mean, the evaluation is better mentioned with replacement of the Express of the part of the expression. So usually you actually, I mean, on the low level of the interpreter, you don't have such, for example, such conception as a call. So you cannot say that it was called the function that is the results because, but actually, yeah, I tried to introduce something like this, like about year, year ago, and when I was working on minimal MeTTa. And now you can see the some, some, kind of stack traces, even some kind of stack traces. There is no some GUI or common white tool to execute MeTTa code step by step and see the variables values. But actually, I think at the moment it is possible to create it. Yeah, maybe it's I Ben, maybe I should do this, or someone should do this at some point. What I use to depart programs I use debug output, you can I mean

what I'm currently doing? Yeah, sorry.

Roman, actually, I don't hear you very well.

It's just literally my code with trace stating,

yeah, you can use Trace. It's one construction which is really useful. Another way of doing this, you can enable logs, like it is explained in the internet, but probably not

very let me find this so

you can enable rust walks, and if you enable it, the logger will show you a lot of information about current steps of the interpreter. You can also see the values of all variables and stack traces

the let me find

Okay, so I will share the link as well. Maybe I can demonstrate something like this. Unfortunately, so basically, you should do something like this.

Okay, maybe repo, or if you use Python pi or just MeTTa. So then you can you see the a lot of information about runtime, as I said, and you can let me show some example. Maybe I

I just tried it. That's a lot of output,

yeah, because yes, well, on each step, it shows the holistic traces program. Not sure if it will help you, but usually I use it. I mean I use only specific steps on this traces, I will try to demonstrate.

I'm Sure If so,

sorry, my keyboard is kind of loud, so it will be enormous. Well,

I can, example,

make my microphone less sensible. So for example, let's be MeTTa first. Can you see my screen? I

yes, no, anybody, yes, yes.

Okay, so let's do some simple example.

I um, thank you.

Okay, so here, which one is contained, which contains, like, basically this, is one step of the interpreter, and it contains a full, full stack trace. You can see it's even more well if you are talking about like common word, which is like C. It is more purpose than just a list of functions which are called because it includes some, some call something. It's kind of part of the MeTTa interpreter written in minimal MeTTa so it is a minimal MeTTa state trace. It contains not only your code, but also code of MeTTa interpreter itself. So usually you can look for lines like, for example, like this, and what you actually interested in is manufactured all functions,

or just, Okay, why? Why not? Well,

okay, probably I already forgot. So probably the most interesting thing is,

this one. And then you can see, like all interpreted, all constructions which are interpreted by MeTTa interpreted itself. So you can see that first we are trying to interpret full one. It's published. Call. Then we try to interpret the full definition, one definition, and finally, we should call something

I Don't remember, what I

Okay, let's just find it. I

Okay. Now I need update it also go to the rust this L of C, so it calls a full one finally, and it is List of queries which was done. It is the results, and like you can see the variable values and so on, which basically that it, it is

the most opposite,

the most low level. Think you can see about MeTTa, code execution, I would not recommend to use it each time if you are not ready. But sometimes, sometimes it's the only way to find out why code works In this way or Another.

Okay, I hopefully that gives the feeling for some of the flavor, at least somewhat.

It's very scary. It should be scary, actually,

like initially it is, I think so

many of the hack India people are the people the students are going to be involved seeing any functional programming in the past.

Yes, they have so essentially, people from engineering colleges in India have a good expertise over languages like rust in low level something like C. They have very good overview of object oriented languages, mainly so whether it's Java or C plus plus something like that. And for AI, it's usually Python, but I think if we can go a bit, as I said, project building approach, then it would be easier for them to understand the language and grasp it real quick. Yeah,

but nothing like Haskell or

scheme.

Scheme, yes, scheme is taught in the final year of engineering, usually when they enter their the last year of the graduation. But before that, it's mostly object oriented language and things like data structures and algorithms which have been taught. Yeah.

So is having that flexibility ability between those two paradigms will be most useful? Yeah,

100% so I mean, learning curve isn't that big. People usually are fast learners here. So we can, we can definitely start initially by again the basics, as he explained, and then slowly taking it to a project based approach. And things can go really well after that, because these guys are good with programming in general. So they're good developers in general. They're also good problem solvers. Is that getting a knack of new language, initially in the syntax and in the structure of the working language is a bit difficult, but once they understand that, that would be easier

to build. Yeah.

Okay. Anything else, or shall we call it for, for this week, and in a couple weeks, hopefully nil, almost always has examples that he works on, but he he wasn't here today, so

I mean, just want an example I can show the new chain. That is,

it's quite that might be great. That would, that would actually be a really good thing.

It complicated, I guess. Okay, to hope connection doesn't

interrupt again,

yes in the test case. So

did you guess

me? I just saw I feel good. Yes. So here we have a little simple knowledge space of the form we have, like some premises that can be used to prove some conclusions.

And temple, can we find a proof of a and, well, that just has to and how do we do that? Simple, so the backward chain is consisting of two steps. At the moment, since what we're looking for can be a set of conclusions, we'll basically take this expression, decompose it into a head and a tail,

and go through

the list

in here. That means we go down here,

basically in this one maps all conclusions to all the rules that prove it, and the other one maps all the premises to rules that use them. And here, basically we look up all the rules that could be used to prove the

our conclusion next.

We have been premises we already have overlap with The premises

that this rule that and then

this that this rule requires

are already met, turn the rule as a proof for what we wanted and if we didn't do

I find it, then we basically check the main backward chain up there again with the new set of this that we want to prove so now they're here in the conclusion. Yeah, and that's,

I'm not sure if there are any questions about it, or if I should go into more detail.

The main advantage this one has Go ahead.

Yes, I did understand a bit, but again, I have to see through the structure again. Maybe if you can share more details,

okay, sure, we'll go through a bit more detail. I mean that the trace statements there might be a bit confusing because they add a bunch of noise, but basically Here,

I mean, it's a set we want to

I think a screen is not visible, but you can maybe send it

to me. I'll try sharing again. Think, yeah, my internet has slight issues at the moment. Okay, can you see it again now? Yes, and click it so yeah. Basically here we calling the backward channel for a single conclusion. We provided the knowledge based on the tab if you want to search, and then this that we already know or expect, and then the conclusion we want to prove of this rule. It's just some trace statements. So basically I find out, well, what, what did this return? But then we can basically start up here. I if the conclusion

tail is empty, click call this function here, also with knowledge with depth on

the rest,

once we found this, we basically merge both rules into one and the things that We try to prove.

Got it? Okay? Yeah, exactly.

And if you look out how to prove for a single rule, like I said, we look up the conclusions here in our knowledge space, this might return a superposition, so all the rules that could potentially fit, and then we'll just iterate through all of them.

Okay,

results, it could this set minus this set is on the left side, and

this set minus and so basically, if this PP set is the parameter set that we want to prove, or we have to prove, if that's empty, well we're done. Then there's one more extra step where we go, map through all the control we basically we can call aviatory meta code in the backward chain to compute some values. Return here we're trying to well, if this is not empty, then we still have something left to prove.

We unify the depth full with s step. So we are using, oh god, I forgot how it's called, but this form of numbers, right? C zero, and then s of C is 1s, of s of C is two, and so on. Because we can pattern match on that easily, that's a bit more comfortable and natural. Numbers go deeper then we call the backward chain on a second, potentially we could check if we actually have a set here, but yeah, and try to prove the set of premises that we still need for this rule to work. Once we find it again, we just merge the rule we found up here with the rule that this one found and return it the school case, if the parameters that we are provided is a variable, that means the user is fine with accepting any parameter. Mate has been used. So even prove them, we can just return it. We basically can return a rule. Then we can also watch and, yeah, that's it. Then, not just for running CPU

function, stay pu then the function name and the arguments and as the output, CPUs check that the arguments are closed, so we're not trying to call the CPU functions with a unbound variable, and then we just basically, if we, if we concatenate the function with the arguments, that automatically results in a meta expression that gets evaluated. You created.

Okay? So if it's not closed, the statement is just going through it, right? It's returned, and then it will be processed later on, maybe, or

Yes, yes, it will maybe process later on, it's, it's it's only necessary the user assess that the Parameter Set is can be a variable, because then we can find partially applied rules, and then we have to check for it's being closed. If the user asks for a proof that given an empty set basically proves whatever he wants, then we wouldn't need it, because then, basically we only try to run these functions after if the parameters are all proven already, And then it's guaranteed that the arguments are evaluated.

I'm sorry. Could you re explain in which circumstance

this would be true would be false,

if, like, for example, here, right? We're trying give them an empty set we're trying to prove. Get a proof of a But if instead we asked for, well, give me anything that has a as a conclusion rule, just as it is with all its parameters, at which point, obviously the C

function, the variables would not be created yet. So like, I mean, up here I have an example of such a

the rule, the paper proof of one number and a proof of another number,

we run the rollback. And now, if I were to ask for any rule. So that was my experience today. It

was really great, and I'm looking forward

and I'm excited

to yep, I think I understood this time completely. Thanks.

Okay, yeah, so nil, you weren't here at the beginning. So we kind of took an opportunity. There's some new people here. Charlie der, who goes way, way back to web mine days and and I, I keep struggling with your name put off. Yeah,

you can just call me Abu APU,

yeah. So this, this is who's working with that, the hack India. That's, that's when is that happening? Actually, I know we're putting things together very quickly, right now. So, right.

So it's gonna happen across of various universities. It's gonna start on 28 Feb, which is like next week. Okay,

yeah, so, so we're trying to, there's two challenges that we're coming up with. One of them is going to involve MeTTa. The other one is is not. And so these probably we're trying to kind of go through some base, simple examples of MeTTa so that put it off has seen it, and can kind of help guide some, some of the work next, that's next week or Yeah?

Okay, great. Well, welcome guys,

yeah, so you weren't here, so it kind of took a different direction today. Yeah.

Hi nil, nice to meet you.

Nice to meet you.

And Merle, mine was going through the chaining example, and so that, hopefully that gave some some indication of the language. Charlie and a put off.

Yes, very much. And it's good to see you again. Nil, after meeting you just over a year and Stockholm,

Hey, good to see you too. You

yes, that gave a good experience, at least a decent overview of the language. Thank you so much for that.

Okay, awesome. So

we've gone over a little bit, and so, unless somebody has something urgent, shall We call it?

You keep coming and going, going, Roman,

yes, three,

we're about to

to call it. So

thanks for that, that the chaining example is a perfect a perfect one. So I think

okay, then

hopefully, if you have questions in the meantime, a PUT OFF. Feel free. I've, I've asked to have you added to the world matter most server, and if you want, I can add you to this call moving forward. Yeah,

100% I've got my email as well in the chat box. Yeah,

I Okay. I have it, yeah, yeah,

okay, okay, I'll add you. I think I did, but I'll double check. Okay, sure, then until, until next time and in a couple of weeks,

perfect. Thank you so much guys for having me. It was a great session, very insightful, and looking forward to spread this in India.

Yeah. Goal is to kind of, get more people knowing about the language. It has a lot of unique features, I would argue, compared to most any other language, right?

I can definitely see the potential, and I'll Scout through the MeTTa developers in India who are already there, and also maybe add them in the call next time.

Okay, awesome,

perfect. Okay, thanks. Okay.

Bye, thank you. Bye, bye. Bye. Bye, Bye,

How accurate was this transcription?

0:00:001:10:31

AI Chat

Outline

Comments