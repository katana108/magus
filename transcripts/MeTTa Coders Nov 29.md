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

Nov 29, 2024 at 7:30 am

1 hr 22 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284)

Summary

Transcript

## Keywords

Thanksgiving meeting, Sudoku program, list length, functional programming, Docker image, nested lists, atom space, backward chaining, forward chaining, Prolog code, hyper vectors, type checking, program synthesis, hyperdimensional computing, MeTTa log

## Speakers

Speaker 1 (44%), Speaker 2 (24%), Speaker 3 (14%), Speaker 4 (9%), Rene (4%), Speaker 5 (4%)

Hi, hello,

probably not many people are going to join because today it's

it's Thanksgiving, right? So, hi, Benjamin, welcome, hi sed, Hi, everyone,

hello, yes, I

was saying that we're probably not going to be many because it's Thanksgiving today. I think yes, but nonetheless, I mean, yeah. I mean we have Renee, we have myself. I It's already

four, already four people

and already five, five. Yeah,

yes, I thought I'd join because I'm writing a program, Sudoku program in MeTTa, and I've about everything working,

but only I need the length, the length of a list I've been trying for three hours. I know I

can help you.

So Renee, is it at least like, like a functional programming data structure, or is it a topple?

Well, I could show you, I'm, I'm using the high prong with with the Docker image.

And I could show you because, because it does not run on this machine, so I made a screenshot, and it will probably clarify,

because I've been searching the lengths, and there are several. There is one example, but it can only handle basically nested list. And I want to have the length of normal list.

So, I mean, well, depending on how you implement it, list, I mean, yeah, yeah, I have implemented a typical functional programming language, list, data structure with various algorithms, you know, fold, concatenation, map, etc, and length is probably six somewhere as well. But yeah,

it might be in some code. I've seen that it could be built in already. Do

you want to share your screen? Yes, I

I must check operating systems. I have to choose which I want to share, and then I have to take this, well, basically this. This is the screenshot which I made so you can see the screen is called the Deborah.

Yes, it's a, it's a length of couples I'm seeing, right? Yeah.

So what do you see there is, well, I make it the Sudoku program, and at a certain cell, I have

all kinds of numbers. You see them, 57793,

and then, then I filter that list. And so the remaining candidates for a certain cell is, is only, only the six and the two, and I've programmed everything with the match statement and everything working, which I basically need. But the only thing which I do not have yet is is I want to have the length of the six and the two, which you see there at the bottom.

Yeah. So, I mean, what would be the length of six and two?

It has to, has to be two,

right, right? Isn't there an arity belt in already that does

that, yes, probably see,

already, maybe, oh, it's,

maybe it's Just very simple, so it's called arati. I don't know.

Because, by default, everything is almost nested in in MeTTa, because basically it's a graph, graph language. So by default, it wants to nest everything. But in this case, I have sort of a flat, flat list. I

i really works for me, but I'm afraid I'm I'm using a branch that maybe has it implemented, but it's not on the it's not upstream. So me try.

I haven't tried everything.

I mean, of course you can implement one, but it's going to be very inefficient, just so you know. Well, although you're running that with MeTTa lock, so maybe it's going to be okay. No,

I'm running with hyperon.

Well, you're running regular MeTTa,

I'm currently developing with the hybrid, with the I'm working with the Docker image.

I see, why are you not using meta log?

Because Douglas said he had a huge bug with ADD with ADD atom and remove atom.

Oh, I see okay.

I can try everything,

but so you don't have the latest git revision, right? You have a release which is in some Docker image.

Yes, that's correct, right? I

when you, of course, you can implement it. Does it work?

Well, I should be able to implement it myself, basically in pure MeTTa, but I'll still not get it if I want to walk through this list.

Okay, let me paste some fold. Hopefully that's correct. And like with this thing, you can implement it, implement, well, a lot of things over apples, but it's going to be extremely inefficient. That's the catch. And so my recommendation is that you add a either you compile the branch that I'm using right now that has that or or you just do you know how to do a Python extension,

not really,

yeah,

because I've been trying with car Adam and CDR Adam, I think it's basically the same as what you're doing there. But, yeah,

yeah, you have to recurse using CDR, but again, that is extremely inefficient. So what solution do you have? Sebastian, you mentioned that you had a solution.

Yeah, I thought maybe what can be interesting is I them. Well, you can, I mean, maybe can I show you something I don't want to steal your thunder, then I but maybe you

can, boom, two people can share at the same time. You

can take over.

Okay, I can. So then you'll get the screens side by side, or,

yeah, in the screen you want to see, or you can have them side by side. I think, I think

I was, I will pause mine temporarily, I guess.

So. I mean, I haven't, I can't say they have, like, implemented it exactly, but I can't show you what I've been working on and I think it might be useful. So basically what I've been doing, I mean, let me show you actually, that implementation that I have. So I implemented this function that basically, what if you write atoms like this, so E 13 or E 26 so in your case, it could be like, available numbers or something like that. Then if you, if you evaluate this expression, it's just gonna, like, apply this. Add one function here. It just over here, right? Yeah, it's just gonna apply to every single result in your atom space. So I mean, if this, and you can also write it like this, and then it will, it will basically just return the value itself, but then it's gonna do this add one as a side effect. So I mean, if you replace the add one by a function that that does something to some state that is stored in space, and you can just make it a counter. So for example, if I, if I said, you know, if I defined a function called, you know, one more, or something like that, right? Well, of some start, like, some, some counter value, right? So maybe that would be what I would doing. Then maybe I could define it as, okay, I want to, I want to add atom to self. I of,

you know, some song wrapper, so my my counter, let's say that of counter plus one.

So you use the atom space to increment,

yeah, I mean, I suppose maybe that would be good. Then you could, you could, just like, if you can maintain the state somewhere, I would expect that it could, it could apply that.

Yes, I thought about it, yes, I could do it in that way. So I just, I increment an atom somewhere in the space every time I go through the loop.

Yeah. So, for example, imagine, imagine I did this right here. I said, imagine I would buy in this,

probably

right. And then I just have to,

have to, like, find the

down here. Sorry,

like, I would do this, or wonder if it will work. Maybe not right after that, but yeah, maybe not. Uh, anyway, something like that. This, do you think it will work? We don't. Yes,

yes, I need an increment. Anyway, but I thought only for the length of the list I would have to make it well I could, yes if, because I basically I copy, I just follow the examples which are already there. So there are several examples which walks through the list. So I could use that and I just increment the variable in the space, yeah and yes, then I would have it probably

be more efficient than using this car atom and comes atom recursively, if it's still the case that it's like passing out each time,

okay, then yes, I will do that. The probably I have all the function design functions I need for for my Sudoku. Okay, yes, I'm going to try it in that way,

the front and old implementation in one of my so if you use the fold R that I pasted above, then you you've got, I think it works. You'd have to test it, but

it doesn't. The fold does basically the same.

The fold does the same what many chooses fold. It passes an accumulator to the fold function. That's how it works.

Okay, yeah, I find it. It is sometimes it's really weird how you recurse. You make sort of recursive function, and then you use the let statement with the star inside, and somewhere you give the new argument to recurse. But where it seems to work and it seems has to be working that way, because all the examples, they do the same. I

Yeah, and I find also that in the match statement, in the in the last argument, you can use an if, if statement. So then, it took me some time to find that out, but then you can do a lot of things, and that's that's basically all I think I could build, because I have the Sudoku running already in prolog, And now I just have to transform it to MeTTa.

So depending on how you represent data, it might be considerably slower. Be aware of that? Yeah. I mean, I found that using tuples as containers is, for some reason, is a bad idea. Performance wise, it doesn't work well. I found I get better results if I if I define at least in So, let me make Sure you then just if I define that and and then I can define algorithms over these. It's just that, okay, and, and then it's, yeah, it's more efficient. I don't know why.

Okay, if, let's say that you you, if you are all the time, use, remove Adam and add atom. So that would not, not be inefficient. You can do this without punishment. Oh,

because you're using the atom space as a container.

Yes, let's say you make an increment value in the atom space and you use all the time you are using remove atom and you change it with one, with a plus one.

I think that's also extremely inefficient.

Yes, it's very expensive. Yeah,

it feels that the kind of data that you would put in a space is, is our data, which is,

which is Not very volatile, if it doesn't, it doesn't have some, I mean, yeah, some aspects of persistence. I'm not sure it's a good idea. Well, that's

something she should really be in the space, because they just have to be there.

Well, I mean, programs have to be in the space if you want to run them. But then, you know, if all you need is do some output given some input, you know, the input could be the structure of the the initial structure of the pseudo game, and the output could be the final structure or something. You don't have to hold that in the atom space.

You could hold it in a list,

right? Or in a matrix or anything, any data structure that you define, yes?

Well, yeah, I would prefer to have that one in, in the space.

Why?

Yeah, well, because I, if I do, I have to do it in a list. Well, it would be difficult for me, difficult, more difficult to understand. I'm still struggling with the list because, well, I come from the PROLOG, and I can do everything with the list, but as soon as I use the is state, the equal statement in MeTTa, you can only use two arguments, the input and output. It's a very restricted in my opinion,

before you know it, you have 30 apparent parenthesis with let statements and

right

by kitchen, I could maybe try to show again. Could be,

will be interesting to see. Yeah, here, here is my, my complete Sudoku program. So this, this is the Sudoku state.

So I would prefer to have this in, in the atom space. I and then I've just started, so it's not complete, but here I have a function for get remaining possible candidates. And I I do a lot with match because I got that working. I

Okay, this is basically all my this is my primitives. So far.

I wonder if you could solve that with the backward chainer, just by specifying rules pseudocode game, but, but I'm sure you can. You can define like, yeah, rules emulating playing a Sudoku game, yes. And then the backward of the other forward chainer would probably be able to just chain those rules until you reach the solution or something. I mean, it may defeat the point of like forcing you to program in MeTTa. But I think it might be, it could also be interesting, yes, in its own right.

So, so you, you have,

you do have a backward channel separated in one MeTTa file.

Yeah, so, so it's in one repository. Let me share my screen.

So

yeah, so this is, it seemed, a chaining repository, experimental, and you've got a bunch of experiment, of experiments, drain your finger. Which one is? Is maybe carry chaining, right? But Id depends. Let's say you need a forward chainer.

So you would define Oh, well, no, I'm not going to show you that. I want to show you something which is more recent, trying to think I

I guess that.

Okay, so, so that would be the forward chain. Or, okay, that's the code and when it takes in argument, okay, I don't like this implementation. Not okay, okay, I'm going to show you something else. But for now, it takes rules. So for instance, here you've got modus ponens, okay, so it takes a premise, is an implication, then the antecedent of that indication, and you get the consequence. And so you can specify a bunch of rules like that, and you can go backward or you can go forward. So for instance, I can say, so the the way things are expressed, so they expressed in a tight theoretical way. Here would be the axioms. For instance, say, well, a implies b, and you give it a name, AB is axiom, but in the type theoretical way, it is a witness of that type. Okay? And so you express a query in the same format. So you say, for instance, find me a proof that find me a proof of a

and it happens to be an axiom. So okay, it's easy to find. Then you can ask, find me a proof for instance. So that's also an axiom. You can you can ask a proof of for instance, amp, like C, which is not an axiom, and it's going to change the rules to go from that proposition to the axioms, so to prevent it as a theorem. And you can do you can go forward as well, or, okay, this thing is weird. I've had tons of experiments. I don't really remember which one does what, but the most advanced example I have is this where I'm able to prove mathematical properties over functions. This is fairly sophisticated, but it's the same very backward chain or code, which is just that. And, okay, there is a proof abstraction here, but you don't need that soul Sudoku. And, yeah, if you want to use that, I could find a version and that that would be adequate.

Yes, it would be nice. And you use only backwards there.

I use mostly backward chaining because it's the most difficult form of chaining.

But you can use forward chaining. For instance, maybe or Sudoku, you would want to use forward chaining

unless you have a way to specify the yes. I mean, I guess it depends on how you specify the problem. The other thing that you can do is you can even provide as target theorem, a partial description you can you can add, you can have all holes in your theorem and and as the backward channel to fills the hole, and to prove that it can fills the holes. Yes, yeah,

yes, that could be done. I I do have one implementation already that that works and it works differently. It does a sort of optimistic tryout. But if you use the backwards chain, basically, it's a sort of brute Yeah, brute

force, yeah. You're not gonna have inference control. I do have experiments with inference control, but they are very early stage and they are not going to be user friendly. So,

yes, I do. I have created an implementation in prolog, which already is working.

Yeah, no,

it doesn't have to necessarily be translated well, it could be as one solution, but I copied it. I copied the idea from a visual prolog, and what they are, what we are doing, basically we we are maintaining our own backtrack stack, and by means of our own backtrack stack that we can fill the whole puzzle,

it seems to work. And the second solution could be what you say to specify the axiomas, and then to do the brute force backward chain, link,

I guess your Prolog code has is using cuts and other Prolog optimizations, right?

No, I left, I left out the cuts as much as possible. So

to be able to go to a MeTTa as easy as possible, so I try not to use the codes

right. So ready. In that case, it could be that porting your product code to the backward channel would be easier, because the backward channel is, I mean, in a way, it resembles a lot what product does. So, yeah,

is that I could post my current Prolog into the into the forum.

Yes, because I've also been thinking about there could be a translator somewhere from Prolog to MeTTa, but as soon as you're starting you you have to use the match statement in MeTTa. So if you want to, if you want to convert existing prolo code to MeTTa code automatically, well, it would be very difficult.

So yeah, but I think it's easier to translate to automatically translate to meta code based on the backward channel, yes, yeah, but it would still be difficult. So yes,

I see it. Let's see if do I have my Current I have my current source somewhere. I

you say

I've posted it. Posted it in the in the mental log development,

yeah, I don't have access to that channel, okay? I think I need an invite or something development I did. You can post on MeTTa log, okay, So public. It's a Public one, so I

I've posted posted It

I'm going to have to Go after 20 minutes. Is there are there any other issues anyone else would want to go over?

Yeah, from my side, I just said this. Maybe

maybe the other people have questions.

I maybe I had a question about, like, typing and what would be the right formalism. I was starting a little bit. I was working on this little snippet that I just show you. I

Yeah, so

I thought this is kind of so if you, if you have a function bind, you would give it a wrapped value and some kind of a function, and it will return

the wrapped like a wrapped with but then with the value of that function applied to the original value, right? So first question I had is, is this the right way to write a type so I thought you have some variable, type

t,

put in a wrapped a wrapped value of an arbitrary type t, a function that takes d as an input and gives you Some U, and then it's going to give you a wrapped like, yeah, value of the evaluated result of type U. So first question I had is, would you write m here, or do you have to write something like Get, get type M, or even a different like fixed symbol?

So okay, I Well, so first, I don't know if it's maybe it's probably permissible what you wrote, and maybe it's just fine. That's not how I would do it. But the difference is so M, it looks like it would be a monad or something, but, but it doesn't matter. So M would be a parameterized type, so meaning I would explicitly, first, I would explicitly add the type constructor M, because M is not a variable. So, so it's a, it's a, it's a constant. I mean, so it's, it's a symbol, so it looks like it's a, right, a type constructor. I mean, there's no better way to so I would do, but first I would write this. So I pasted just to say that if you provide an argument to m, you get a type, okay. And then okay. And then I would write a data constructor for m, so let's call it make m and

and it takes, well, something, I don't know what It is that he takes and it gets you wait. I mean, let me try to think here, because you've got here here on your way to make a dependent type here.

So So okay, you've got that

I'm not sure you actually want. I'm trying to understand what you're trying to do. And I'm, yeah, it's not sure you want you want, you want because, okay, you have,

yeah, as I remember trying to do is I want to make my code more elegant and abstract away stuff, right? I like that syntax where you can just say, well, here is my symbol, my value, and then I gonna bind and apply these functions and chain them. And I noticed that I was also, I also implemented a very similar thing in Python, and there you get this kind of elegant result, where, if you, if you bind the call method of of a class to this, to this bind operator, you can, you can get it kind of, you know, you can Get these parentheses, like chain change expressions of parentheses and with which you can do stuff. And I thought it was that was just interesting. So I was doing the same thing here. But then I thought, Well, hey, you know you like, you don't really need this keyword bind, right? Like you can, you can write it like this too. And

you your your buying function looks like a map in functional programming language, map, but, well, yeah, where m would be a moon ad, and I'm not. I'm not sure, because I'm not, I don't feel super confident about monads, but, but anyways, it doesn't matter what It looks like. Let me let me see.

Amen. I

because I like, I know that in like, in the I just took it from, from what I found, also in other like, like in Python, there's this library, like returns Library. It gives you some tools, and then they also write it like that with pine. So it's like similar functionality, like, same psychological structure is this. So what do you that's your data constructor. Mkm,

right. I mean, well, yeah, it's an example. Let's say and and. So then I would use the data constructor to identify patterns in whatever methods of these types you want. So in your case, bind. So instead of M, I would use make m, because I um, yeah, so that that's very similar to what you wrote. It's the only difference. And I'm and I don't even know if how to say it's better in the sense that we met, maybe MeTTa is just fine with what you wrote. It works just fine, but it's just a functional programming way, and I tend to hold back on functional programming. Okay, thanks. Yeah, it's kind of a Yeah. So

if we can ask a question. So from the way I understand it, you like, it would be ambiguous to use the same symbol m here for the type of which this would be like an, in an instance, this whole thing, right? And then I don't. So here, basically this the function of this expression here, it would be to let the like the MeTTa compile or interpreter know that this is a type,

right? Yeah. So you could have so, for instance, m of number and so make m, you provide a number. Make M, 42 man, that that is now an inhabitant of the type and number, yeah.

Okay, so I see data, constructor, type, constructor, yeah, okay. I understand, right. Okay. And then one other question, if we can sure. So I thought, well, let's, let's also add this other effect function. I just said, yeah, that that works, but actually notice that it's not working. If you so, I thought, well, now I can, I can use this kind of syntax right where. So I so something like this. I suppose I can use this syntax where I'm able to write expressions like this, right? So I would have some kind of make m of 42 and then I can, I can do add one or whatever. Then I thought, yeah, well, what if I want to just apply in effect and return the the very same value for like, chaining operations, right? So I would do something like, imagine that I want to,

okay, see, that's nice. I get what you're Yeah, yeah. So

then I thought, well, so this this expression does not really work, because if you, if you would do this right or right, yeah, it's not going to, like I want, I wanted to. I want this, like I want there to be two operations, like, in this case, it will, it will definitely, you can, you can definitely return this make m of value. But then my expected, I expected this expression. But that's

I see, right? So, so maybe you want to use super pose, yeah, but

then so then I'll just get a unit type returned as well. Then I'll get a superposition of unit type and and make m,

okay. So, so the problem is, so, okay, so that your problem is that you're trying to find a way to type this thing.

Yeah? Like, if you give

us otherwise MeTTa complaints or something, yeah, it's,

I mean, it's just like, No, it's more like this. It just simply won't evaluate this, this expression, like, if I write this like, for example, let me show you this results that I have here. I have my function at one, right? So just think that M is make M. So I would like, I would define this E, this E expression here, for example, I would say, Okay, well, that is gonna basically bind right beside this, this,

right? So you want, you would like this m to end up in the atom space, right?

Yeah, indeed. And that's not happening because, like, look, if I, if I evaluate this, it's but if I evaluate this expression, is just going to apply add one to each of one of these atoms that are in the atom space, right? It is going to match itself. It's going to find these E and F, and it's going to return F. So it's going to give me, like, m of 13 and m of 26 but then inside of it,

so you would like to update, to replace the content of the item space, to replace it from E, 13, E, 26 by E, 14, E, 27 Yeah.

Or M, M, 14, M, 27

All right, right. Yeah. So you, you, ultimately, you have to delete the one that you have updated and then add the new the new data correct you want to update. I mean, I

don't really need them to need this. I just, I mean, maybe let's just start with getting the M first, because here's the word thing. It's like, when, when I So here, when I tried to do the same thing, but then replacing the symbol E here in this expression for M, so binding that to capital letter Q, it won't give any result, right? Because, yeah, obviously it hasn't been added to the space. But, well, I mean, what if I bind this add atom function to like, in a very similar way, right? So I define a function. So instead of add one, this is just add Adam C. So it's kind of like, yeah, add Adam to self with the value that has been like, wrapped and you in your matching. So if I would expect that, if I bind this at Adam C function to my queue, right, yeah. Some, some function that has this, that has this, like property that you can you know that it's calling the bind method of before then I would expect it to execute this at atom for like this second part of the expression. I wanted to execute it like this,

right, right, right. That's what it should do.

But that is not what was happening for me. But don't you

need to have a bang at the end of what here? Isn't there? There's no need to have a Ben. This expression

works. So down here, if I, if I add them like this, then this will just return m2 right? So it's gonna, because this isn't like a met like it's gonna match all the symbols. Yeah, and they didn't tell you that here, this is just, like, I just said, Whatever symbol you put in there, you're just gonna find all the all the other symbols, all the other wrapped values with this. M, um,

okay, yeah, you're right. You don't need to have a bang. Okay. All right, um,

and I think so another way is to use lead, maybe,

yes, but that's my hypothesis. That's about I was like, a little bit like not was was confused about is that here I just kind of turn it back to M for the moment. I will change it properly later.

So that's why you use let it's to capture the type that's output by font or right, and then you return also that code looks fine, so that doesn't do what you want. Well, it

returns this second part,

right? This.

It's not applying this as an effect, really, yeah. But maybe, maybe I need to add a type or something here, and it would exalt it. I don't know that better. I

don't know, no, I mean, the type is only going to constrain the way you can call m so, I mean your structure here. So I don't think that's strange, that it doesn't work. I It looks like it would work space, yeah, I don't know,

maybe hard to to work like that, but so let me just see that is it is strange, Right? Don't know what happened here. Is it saying? I

Hello. I

i i know i just added, I know it's I

says, not working.

I Oh, maybe this,

yeah, okay, so here you can see what's going on. So here you can see this. It's giving output here and 27, and 14,

the ideal way to communicate code. But okay,

so yeah, I would you can see also m2 that is happening. So definitely this, like matching with m this working can replace it with good q2 and that's the same definition. It is, only after I make this explicit add item, but as soon as I

do it over here.

So I'm kind of expecting that there would be, like an exclamation mark somewhere, but if you do like this, it won't work. So you can see that it's able to match it correctly, right? It's like, it's definitely this expression here, the small letter Q. It's definitely able to match instances of queue something in ampersand cell, so in the space, and then it's applying this at Adam C to 79 otherwise you wouldn't be able to see at Adam C 79 then here, as soon as you do this right, would expect this to just apply, apply it. But if it had been applied, then you would expect it to, oh, maybe, listen, maybe it's just, actually, I got it. Okay, I just have to wrap this. I

think I got something working that's similar. I was able to have the side effect of adding,

do I would have expected, like, that's not, actually not what I wanted. I didn't want to make an explicit there. So when binding this

is yeah,

I don't know if that's what you want. But

what did you do? Add yourself?

It did add 42 so, so that our name right? So this call is, is triggering that evaluation, which triggers this, which result into adding, adding 42 there returns This, yeah, which is this? Yeah,

yeah, and 42 so

so

this is the same, right? It's the same expression that you have, sure, yeah, that is x. It's called Val case, yeah, yeah, add to self. It's also the same right here,

yeah, add to self, yeah, yeah,

great. So, and then, yeah. So you're saying, Well, if I do,

yeah, but here is the weird thing. I think that I would expect this Q, because, for example, if I say q, add one, right, then you can see it shows M 80. That's the result here. But as soon as I do like add to self, it's not, it's not catching that M 80 later on here. But in fact, it's actually just, it's trying. It's trying to, like, add the atom of the, like, the content of the value to the space. So, oh, maybe it actually makes sense, yeah, because it's implying it's applying the function inside of the inside, right? Yeah. Okay, now I see, so that's why it would make sense here. Yeah, it's not applying, it's not applying anything to the wrapper ever. That's the whole point of this change execution. Okay, so you would have to make it explicit here, and then it should, definitely should work. Yeah,

okay, okay, I'm going to have to go soon. Ben, gentleman, do you have any how to say question? I mean, I told you I can't really answer your request for proposal questions. But Is everything going on right in that direction? Do you have, do you know what you're supposed to do if you want to participate?

Yeah, but at the moment, I'm just getting into the language and so forth. Do you Do you see my screen right now? Yeah, this word. So I just made the little progress in evaluating from emX. I was just, I thought this was cool. Say something like, how does MeTTa work? I'm just, I'm still getting into the tutorial, but I can, oh, wow. I thought, maybe thought, This is good,

excellent. How did you do? So,

I just wrote this up that was here so far. This is prototype, very, very early prototype, just running the hyper run here. Here, I run the hyper run process, and then I defined some E list where I evaluate MeTTa, and then in the in the callback this, this just, it's just very early, okay, and I'm here. I have here I can show you maybe, maybe you will like this, or whatever. I'm gonna document my progress here. So I'll put this. I will also show how I do this interactive, evolve and these kinds of things. So, yeah, that's getting into, getting into the language. It looks interesting, for sure. Okay, how do I say stop? Guess

Okay, so, so obviously, I mean, well, have you seen I'm an emacs user, but we're probably a minority most programmers nowadays, I don't know they use, they tend to use VS code. I think some still use Vim or neovim, and so that's why the the team that's working with that's making MeTTa log ready is part of Rene is part of that team are making this LSB server? Because we, we kind of need a way, right? We need a standard, somewhat standard way to communicate, to create this interface over a range of popular ad terms. But, yeah, nonetheless, very cool. Yeah, so, so I mean all these sort of things, as I was explaining in my message on matter most, right, evaluating, type checking, program synthesis, program factorization, and then you've got all the AGI stuff, such as program evolution and reasoning, and yeah, can go. It can go quite far. So, yeah, I think if you put together, I mean, again, I I'm afraid I'm going to tell you something wrong about the request for proposals. I don't know how that works, but, but it could be that you can put a proposal to together, or something like that. I really have no idea. So and right, as I mentioned, there was this possibility of also hiring someone to help with my work, but that's that's probably more a how to say a longer term thing, that it's not going to happen very soon. But right? Yeah, I don't know at all how it's going to go. So, so yeah, anyways, yeah,

I'm interested in the languages and check checking it out right now. And, yeah, let's see, yeah for the courses. I'm like, my main interest is hyper, hyper vectors. If you know that, I wonder if maybe there would be a proposal to put the hyper vectors in. Like there was this concept blending

thing, hyper dimensional computing. Yes, exactly, yes. Yeah. Okay, so Adam, Adam vandervors has done a bunch of work, yeah, using MeTTa like he has a MeTTa to hyper vector compiler where he's able to Okay, so let me try to to recall what he's doing. So basically, he has, he's able to compile a database in MeTTa into a hyper vector. So the entire database itself is a hyper vector, and then he's able to query this, this hyper vector in this that now contains a graph, and gets, then a result which itself is a hyper vector. Because if the hyper vector is large enough, then you can, you can store a graph. You can store results from a query over that graph. You can and it's all just going to be one hyper vector. I mean, that's the thing I understood. He gave a number of presentations, I don't know, a year a few months ago, and that was really fascinating. So yeah, if you want to work out that he's probably the right person to get in touch with.

Can you, can you link me his? Yeah,

so Okay, let me okay, just straight from the MeTTa log. Just going to see if I can. Maybe, instead of pinging him. I'm going to send you a message.

He so, yeah, I'm going to send you a private message, not because it has to be private, but just, just, do not ping Adam for no reason. Yeah, that's it. So you've got his, yeah, his contact,

yeah, no, it's good. I'm gonna maybe getting

in touch, yeah, and I know that. I mean, it looks very promising. Some people are designing hardware to work with hyper vectors. And it's, yeah, it looks totally fascinating. So I think there's a lot of, yeah, a lot of stuff to be done. Okay, I'm going to go. So thank you very much for your participation and see you. Well, maybe in two weeks, I guess, if not earlier.

Okay, thank you. Thank you.

Goodbye, Thanks. Yeah, Bye.

How accurate was this transcription?

0:00:001:22:50

AI Chat

Outline

Comments

Otter AI ChatClick the suggested questions or type in your own questions.

1 / 5