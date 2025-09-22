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

![](https://profile.otter.ai/AKMRNBM5G52I6ZL2/AKMRNBM5G52I5LUB.png)Iain Wentworth

Apr 4 at 8:31 am

30 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa Study Group, assert function, pull request, LSP server, Visual Studio Code, Emacs, code commenting, LLM, code formatting, code completion, error message, documentation, code evaluation, local LLM, prompt engineering.

## Speakers

Speaker 1 (48%), Speaker 2 (32%), Alexey (10%), Bitseat (8%), Speaker 3 (2%), Speaker 4 (1%)

Hi, everyone. Alexey, ah, hey, Alexey, thank you. Hi,

so I wonder if we should wait a little bit longer, or should we start? Does anybody have anything any issue or topic for discussion.

Thank you. I have one issue. Alexey, I'm sure it's going to be quick, so let me just quickly share my screen and let's see what happens.

I hope you can see my screen, right?

Yes,

okay, sorry about the background. So what I was doing is defining some assets, and I'm putting them under HTTP dot Mita file, as you can see. So the two functions I added are the first one is this one, assert, can you say it

in the other one is this assert, contain function. The problem is I was just adding some test scripts for the two functions saying this assert works fine. I did review the project, but this assert content is not working. So I just want to know what I have to do after adding a function to STD lib dot MeTTa, so that it can be recognized. If suppose we're not recognized, it would be easy, I think. But now assert works fine, but assert contents doesn't work

well. If it is in study lip dot MeTTa, then it should be accessible. So maybe the reason is different. So you can rise a draft pull request and we can discuss it there, or you can rise an issue and put your code in this issue. Do you want your assert functions to be added to a release?

Yes, yes, yes, that was the plan.

Then maybe rising a draft PR would be the best way to go.

All right, okay, but as far as you know, there's no a function called assert, right? I couldn't find one.

Yes, I guess you don't have just a short function, but minor commenter right away, I would actually like an asshole function to have a short a second argument, which informs what the problem is. Because if you put such as shorts in some code, then you would like to get a error message, but it can be described, discussed within your PR. If it's incomplete pairs, and it's just a draft pair, and you can describe what your problems in this pair, and we will work on it together. All

right, okay, sounds good. Thank you. We'll do that

for a little while. We had something called this true but that might be really similar to assert true.

Yeah, what we want is a function that evaluates a single expression and returns like an NPT if it's true. But like you said, Yeah, we have true. True.

It's also not very difficult to write an assert function in terms of the assert equals that already exists. But I also agree it should be a function in its own rights.

Yeah, and usually the error message will be the source code that didn't assert true. I mean, if you a lot of times, we'll have a certain we'll have a string that says What's wrong, and then we'll have, like, some condition that has to evaluate to true. But like, even in this case, sometimes, if you don't need that string, you'll have, like, it'll show at least the source code that failed. No, yeah,

okay, anything else I

after we've done a couple, maybe a couple more issues or questions, I can show off the LSP server that we have for MeTTa that's in Visual Studio Code. Sorry, we have a couple features like it comments your code for you using an LLM, comment your MeTTa code for you. You know, things like that. Also, James cash, he's one that wrote it, has it running an Emacs, and might be able to show that off on emacs someone's interest,

yeah? For sure, I could demo that as well. I'll have to switch computers first. Yeah,

yeah. Ty would mention that. So that way you could Do that. Yeah? I

I think the client now I can just do that quick emacs demo, reasonable at this point.

Yeah, I think I think the idea, okay, right, yeah, that's probably a good idea.

Okay, hopefully this works here. I'm bumping the font size a bit so okay, that's visible. Yes, I have the LSP server running here. This is emacs using the egg lot the built in LSP server. It should also work with emacs LSP mode. And Douglas is saying it's working in Visual Studio. And there's also instructions for running it with them or Neil them in various configurations, fairly standard setup. If there's any other editor configurations that are not working, people can put a pull request or issue or something, or let me know on the the meta Wan repo, yeah. So started this the LSP. Here, we have some hover things here, so can pull, pull the documentation again. I have my editor configured in a kind of minimalistic way. So here, the hover information is showing up at the bottom and just on a little file. Here is just some test stuff. So we can see the documentation for predicates or the functions, if they are documented. If they're not, it'll just show their implementation. We can evaluate stuff. So the code action. There's a couple code actions here. And do the run, load MeTTa, and it's hard to see, but down at the very bottom of the screen, the server reports, and then 52 being the result of that, there's various other things that will work. There's also like eval expression, which will give the result and will capture output. So again, hard to see, but down at the bottom, it's showing empty square Brax, no value. But then after the semi colon, showing a printed out through bar, so we can see the output it was captured. Let's see, this is kind of a small file. Let me see, hopefully I have the LLM stuff set up, but Douglas mentioned the code commenting so we can ask an LLM to comment here. I have this is going to a local language server that I have running. It's probably a bit slower than using like a API endpoint, but it has the advantage that it's LM has been configured with a system prompt that has a whole bunch of information about what MeTTa is and how it works. So people want to set that up. There's instructions in this repo, leave in this file, so under the MeTTa WAM libraries, LSP, server, MeTTa prolog, LSP, MeTTa LLM has instructions up top for configuring the olama using that configuration. I know it's quite small on this screen, but if people want to see that, it's fairly straightforward. So we can see this added a bunch of comments explaining what each lines are doing to the best of the LMS ability to determine which obviously can kind of vary

with you know, how good a job it is doing. I've also just recently added some LLM code completion. So if I have the cursor here, I can say, oops, what I want to do is hit the Code Complete shortcut here and again. This takes a moment because I'm running the kind of debug mode with a local thing, so maybe it's not going to work for me at the moment. Also because, of course, because I'm demoing is when things are going to fail. Oh, there we go. So completion options. So again, hard to see down at the bottom the first couple options that are kind of giving a full block of code are the LMS attempts to guess what coach a complete here. Some of it seems kind of like nonsense. Some of it seems maybe a little more reasonable. There are the LLM. So this is the LLM is. It's a local version of llama llama three, I don't remember maybe the 70 billion parameter that's been given a system prompt. So inside this repository here, I can put a link in the chat to the that file on GitHub, just if people want to have the kind of overview instructions. Let me quickly pull that up. There's a model file in the repository that this. The comment at the top of that file mentions that will is the thing that one runs drop that link into. So it's essentially just a would be the thing that you pass to olama with that configured, right? The other completion options all, let's give it a second. Yeah, I'm kind of of two minds of two minds of the completion here right now, having the LLM thinks does meet the completion quite a bit slower. We can see the other completion options are just based on all the other MeTTa functions and such. So of just generally useful things here, I'm completing with nothing. So it doesn't have much to go on. As I say here, it's a thing that's slightly annoying is it makes completion quite a bit slower to go through the LLM, whereas otherwise it's almost instant if you want to complete the this built in function, so it's something that can be configured again, then the documentation for the LSP server. If people want to enable or enable the the LSP, let's see what else. So the other thing that's been added is code formatting. So say, if we just make this kind of indented a little bit strangely, you can hit keyboard shortcut to reformat it all. I think I accidentally part of the problem here. I think the LM when I did that comment eight, the close parentheses, so got all unbalanced. But So right now, if I hit the shortcut that calls the LSP format on here? Yeah, it would like reformat the functions I got eaten there. I think the editors got noticing there. Sorry again. I'm running a debug build, so things get weird here. You can also highlight just a region and say that, but, oh, I think I haven't implemented that, but didn't restart the server since I fixed that anyway, that should also work to reformat just the code in the region. Kind of think, if there's anything else, think this is talking to an old version of the LSP, which is why it's doing a bunch of weird thing. So actually, let me just save I think it got kind of out of sync there. Well, there we go. That's kind of what I expect to look like anything here, yeah. So that's kind of the quick highlights of the features. Here we have the LM commenting. We have the code formatter. We have auto complete the lookup documentation there in the hover various code actions for evaluating, running the test in the file, running a particular line of code. And yeah, as I say, this is running in Emacs. It should also work in, I mean, any other editor that supports LSD protocol. To the best of my knowledge, the ones we've tested it with configured it with there's a the tested with Neo Vim, which, again, kind of depends on exactly how one is configuring what version of Neo Vim, the Visual Studio Code extension is there's an instructions in the repository, in the read me for setting that up, which is a couple more steps. But the VS code interface has a nice Settings panel, and that makes it easier to tweak various options about exactly how the LSP runs at various options, at configuring the PLM integration and such. Yeah, I think that's kind of the overview. If there's any questions or anything people anything more people want to see,

well, that's great. My main question is, is a redistributable package for speech hardware.

I haven't we haven't set that up yet. There's instructions for building that from in the repository for configuring it that should work. So the simple like it would need a Prolog installed, because this is built on the meta log distribution. But the instructions in the read me which I can drop that link in as well. This so easy to find. Oops. I following those instructions should kind of just work. That's to extent the the Emacs, Neo vim setups are just like snippets of code to add to the extension after running the steps up top for installing the LSP server, I will say I have, I'm not sure if we've tested it, running it without meta log installed, because it is using the meta log, I guess implementation of MeTTa to do The Code evaluation and look up docs and such. So meta log would need to

be available, at least from this repository. So I guess, yeah, the short answer is, there's not kind of a one click setup, but the instructions in the repository should be be sufficient to get it running.

Yeah, the also, the way we have it configured is, I use open a eyes, LLM so the local one that we want to make sure we'll have a local that users can set up the local one so we have, like, some prompt files that we give it to sort of get it writing MeTTa for us. And that will always be moving target. It'll never be perfect. So we're gonna be, you know, it's gonna I have, like, some that work great with open AI, and then James found some of that prompt would work with his local one. But it's not perfect. It's just, it's a little bit of of stuff that we've just been, I've been sort of finding that gets the LLM on track, but doesn't give it too much information that it that, I mean prompt, prompt engineering is a really, a fun, difficult thing to do, but at least sometimes it writes good Netta, sometimes It's horrible, you know, peasants, it's moments. Just also answer your question.

Let's see on the LM setup. So even if you have it set up and working, it might be really good sometimes and terrible the other times, but it's almost always trustworthy when it comes to commenting. But

by the way, garden collecting a MeTTa Corp for training alums to know MeTTa, MeTTa and possibly llama three can be also fine tuned on this corpse in this in the future.

Yeah, that's I thought that was really awesome that llama three was working, and that people been able to set up a local one. They don't have to use the open AI one. Yeah,

that's nice. I

I guess I could go ahead and show off the Visual Studio Code version.

Yeah, okay. I

I'm running VS code locally here, and let's see, oh, is VS code showing up because I picked the right screen share. I

think it's whole desktop.

Yeah. Okay, let me make sure I

Okay, I guess, I guess I got it there so you're seeing Visual Studio code and not like my email or something. Yeah, okay. So, yeah, the LSP server. I don't use Emacs much, but I really like Visual Studio code. So it's pop ups, have are more, you know, there's windows that you can sort of scroll through and use. Stuff. So here's, here's using chat, GPT, 3.5 to do code commenting here, I'm going to give it a little bit more of a comment just hanging that much. See format. We want this and we want to comment this block. Okay, it looks like it's working. There we go, but commented that actually rewrote, didn't rewrite the code. No, it did. It just that's pretty good. You know, there, there it is, commenting code that works pretty good. Oh, so James was talking about the configuration SEC of our LSP server. Show that off.

That's funny. There we go. I me. So we have to get to set your you can set, oh, I guess I'm using, wow, I'm using GPT four. Oh, that's my model there. You can set the temperature and so forth. We'll probably add something where you could add, like, an extra prompt file, this, like that. That would be kind of good. It was surprising to me that that we actually had to do this, because I would have thought there was a ton of get your LLM to talk to Visual Studio Code easily, stuff already, but they're always so language specific, like we would have renamed this to dot list file. You know, there would have been something that would have done that, but it was nice to have something that was like MeTTa specific, that would work. And so all the features that you saw James show off are all are all working in this one. Since our LSP server is written in meta log, it's just it runs locally, and then all the editors connect to it through a socket. And so, like, whatever, so, whatever. So when you're running MeTTa locally, you can have the LSP server connect to it

and but I've already got one running, and it would be, I haven't tested the setup today for the but, oh yeah, when you do run it locally, you can set up, tell it to talk to your local, your local meta instance. So like, I think right now, this is even already, was that a windows aren't responding. No, it has something to do more with other than does with anything else. Oh, yeah, since another logs like massively concurrent multi threading, that's why I.

How accurate was this transcription?

00:0030:03

AI Chat

Outline

Comments