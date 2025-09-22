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

Nov 1, 2024 at 7:30 am

22 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

LSP server, syntax highlighting, Visual Studio, experimental feature, Metallog installation, Prolog package, cross-editor protocol, extension marketplace, large files, bug reports, documentation control, development environments, MeTTa coders, meeting wrap-up

## Speakers

Speaker 1 (73%), Alexey (17%), Vitaly (6%), Speaker 2 (4%)

Hi, everyone. I'm not sure if anyone else is going to join, so maybe we can start. Does anyone have any question or topic or discussion? I

I was kind of hoping that Doug will be here to talk about this, but we'll be making progress on the LSP server so that we can do syntax highlighting and help with with the things like Visual Studio.

So I

not sure if a screenshot is working right now. Could try and show what i've what I'm doing.

Me, not sure.

Yeah, I've had trouble with this before, so just give me a moment.

Window I know.

Yeah. So this is using a really, if you hang on it, I can't even see. Here we go. Here's an example of very small file that I've been playing with, and just a little bit of syntax coloring so you can see what the variables and the comments and strings and things are. And if you mouse over something, it'll bring up a whole lot of information about it. I think I showed this a couple of weeks ago, so the mouse over Doug has been working on this more than me recently. So I'm not, not sure what features he's, he's, he's got working, but it does include things like, if you provide a doc for the format Alex, if you, if you recall it from, even from another file, okay, that's breaking on me, because it's not okay, oops. Okay. There's still some bugs. If it's got bed syntax, we need to, this is

still the work in progress. But you, but the idea is that if you hover over something that's got docs for it'll let you provide the docs. And I believe you can do things like go to definition, it'll tell you where it where it comes from and but a lot of the navigation stuff works message. And I'll post a this is still really, really, really experimental. You need to have metal log installed for this to work and but the rest of the instructions I can post in a link. Just give me a moment. Uh,

and okay, I'm gonna post a link in a couple of minutes. I just want to make sure I'm giving I'm giving you the right link

on there. I think this is the right link anyway.

So there any any questions or comments about this things? People wonder?

Yeah, actually, one thing we've tested this with video studio should work with other editors, but we haven't. I don't think we've really probably tried their ears. But yes, now this piece servers a protocol that supposed to be cross editor.

So is it just like,

is it an extension? Do we have to, like, install it with, like, a repo or something? It's, it's a bit, it's a bit untidy. At the moment, we're cleaning it up. It's an extension. You can actually go to the, if you look at the instructions, you can go to the Visual Studio marketplace and just get it. But you do need to have metal log installed, and you do need to install a Prolog package for it to work, because the the it's basically built on top of metallock. Do you have, like, a link for all of our stuff? I've just posted it in the chat. I think, oh, yeah, I see it. Yeah, I see it. Sorry. I'm not sure that's exactly the right limit. I know what the blobs doing in there, but, yeah, that's the, that's the i

Yeah.

So that's yeah. That's something we've been working on and are continuing to work on for the past little while. So, so now there's been a fair bit of there's been requests,

and I'm definitely Doug, and I definitely open to any, any comments or bug reports, or any, you know, anything that people Yeah, any back, any comments on this,

and oh, we'll post any updates and on this in The in the Metallo channel, on the matter most i

Okay, yeah, this is other questions that speak on it done. Let me unpresent.

Look nice last time when you mentioned about this extension for Visual Studio. I found it in the shop or extension list, I know, but I wonder if the latest version of this extension is published or not?

Yeah, if you look at the instructions, you'll see that I've got a it's it's published in the shop, in the marketplace, and I've, in the instructions, I put a little diagram of which one to look for. So if you just go search, go to the extension marketplace and search for MeTTa, you'll find it. Or if you want to, you can actually create a.vs IX file and not have to go through that that at all. And the vsax is the specific thing that Visual Studio uses for getting at this stuff. So either way works, that is that, does that answer your question? I

my idea,

yeah, if you go to the store, you'll actually find three syntax highlighters for MeTTa. But this one, this one, I think, goes a little bit deeper in terms of what the links, what's available in the other ones

is it divided to like LSB server and I mean, I could official Studio code works to highlight syntax and control documentation like this. So is it possible to use this LSP server in other IDs.

The sounds are echoes, the LSP server, another, another. Sorry. What

you know development environments, for example, has bike into,

yes, it should. It should be absolutely fine to use with other editors. We haven't tested that properly yet because we've been using Visual Studio, but yeah. And also, if you know, if you're using MeTTa rather than Metallo you can still install metallogue and run this. It'll do this index highlighting with this, and this doesn't, at the moment, execute anything. So it's all about, yeah, see, you can use it with other meta development environments, but it requires meta log to run. But all it's looking at as the dot meta files and working at it from there, yeah and yes. The the server that is based on is the LSP Prolog server, and that's been that's known to work for things like Emacs and Vim and various other editors.

Okay, okay, thanks.

Any other questions?

Okay, so

Oh, there's one more thing I know. Not sure where Douglass Douglas with this, he's working on making it work quickly with with large files that go like a megabyte file, then it takes 40 seconds for everything to load up. So I know there's some I'm not sure. I'm not sure where Douglass with that, but Yeah, we're going to keep improving this. I

Okay, thanks. Anything else from anyone you

and please pause The inform MeTTa mosque channel for sure you

okay, it seems that there is no more Topic, so we can wrap it up for today. You

it seems Yes, people started the meeting, so thanks for writing up at least one topic. And it's really important to have this convenience For MeTTa, coders, bye, Bye, everyone. Thank you.

How accurate was this transcription?

00:0022:43

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5