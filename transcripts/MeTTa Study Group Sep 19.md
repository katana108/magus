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

![](https://profile.otter.ai/ANVOF4NASYGTZ5SR/ANVOF4NASYGTZPQT)Number4 x

Sep 19 at 8:31 am

1 hr 6 min

Shared with: [MeTTa Study Group](https://otter.ai/group/12429284), marco.capozzoli@singularitynet.io, persival.balleste@gmail.com, zariuq@gmail.com

Summary

Transcript

## Keywords

MeTTa study, truth values, falsity space, contradiction, para consistency, binary connectives, helper functions, flatten function, add to space, match query, non-determinism, PLN, objective inference, abduction.

## Speakers

Sebastiaan (66%), Nil (23%), Speaker 1 (10%), Vitaly (<1%)

I I'm Hello, Hello, Hello,

hi, Hello,

Daniel, hi,

if anybody wants to stop, feel free if Yeah,

I got something. I had some questions, maybe that you could help me with.

Yeah, should be able to see

that there right?

So, okay, last time I was working on this and I formalized a little bit this idea of using functions for for encoding truth values. So I got, just got a clean MeTTa file here, and I created two spaces to begin. I created one space called Truth and the other one called falsity. So my idea is that I want to store the true propositions in truth and the false propositions in false, and then, so I'm kind of taking that approach, that the proposition doesn't really have to be necessarily true or false in itself, but it's more like when I make an assertion that it's true, then then that is one statement, but that is that can exist completely independently of making the same assertion that it's false. And then my goal is that I can parse the expressions into these into the more like smaller representations, such that if I find the same atom in the falsity space as in the truth space, that Then the computation that led to that result, it somehow is an indicator that there might be some contradiction at play.

Okay, so that's clear. It's a way to handle, yeah, para consistency, something like that. Yeah, yeah, I get it. Okay, so,

so I'll just walk you through the code that I got. So I find just identity function, and I define true and false, like this, so true is just left and false is just right. So then predicate or like binary connectives, they can be defined in a kind of intuitive way. So, I mean, here it's intuitive. I mean, maybe you have to take a look at it for like one or two minutes, but so you can define and, and, or that that would take two of these truth, truth values. So and, for example, if you take end of true and false, you can see that it would be like True, true, false, true. And so it would be false, right, because true is taken left, returning the left side. And in this sense, because this would be false, then could return false, and only if both are true, where all of this would be true, then I'll end up with true and otherwise to be false, and similar for or and then I find a kind of helper function when which is it is kind of the same as just applying True or False to input. So, but here I'm saying, Well, I just want to return some kind of value, when true, when, when I'm when I'm applying the truth value on the right side of this atom. So when I got this atom, here, for example, here, here, I'm giving an example. Then I want to start storing all the true properties of a thing on the left side and all the false ones on the right side. And then I'll be able to apply on the right and, like on the right hand, of my atom, the truth value, in order to just apply it to pick one of the two choices. And I'm just doing that so that it allows me to define the properties of or the statements that I want to make of a of an object, for example, without needing to reference these, these truth values from the get go. So for example here, if I this is then the idea is that you'd have some sentence,

and I want to, I want to essentially turn it into this kind of expression where I'll have my objects one, and it could be like one observation of this one. And then I'll use this, this when function that I find above. And then I'm saying, well, here, let me create a kind of list where I'll, I'll just call this this list constructor property, because, why not? And because, and then, and then I'll put so this will be all the things that are true of this one, it's white, it's a bird. So that contains a list true properties, and here the false properties, all right.

Well, slightly confusing. So the truth value in the definition of when the wind true and the wind falls are whatever you want, yeah, well, in your example, there are properties, but I guess in general, well, they're rather in strict right? It can be anything, but the truth value is true or false, correct, right? Because so then cause truth value which is true or false? Okay, so, okay, I see. So when it's going to be true, you're going to execute when true, and when the truth value is false, you're going to execute when false. Yeah.

So I could run something like this, right? And so if I said the storm true, essentially saying, Hey, give me all the true properties of this, of this one, right? Or of the of this one, really. So here, so I'll run spawn through, and you'll just give me this. So, yeah, like syntactic

sugar, I see it is true that a swan is a bird, but it's not true that. Why do you have wait fish, red haired and fish? Oh, well, it's not a fish and it's not red haired. Oh, I see, I see, okay. The list is the conjunction I get. Okay, I'm

making some assertions about it. Hey, this is not a fish, right? And I'll put it in my, in my knowledge base, and then I can get that I see, and I can, I can wonder whether something is true or false of this one. Yeah. And it gets kind of interesting when you start defining multiple, multiple of these, right? Because then, then, then you get all the properties somehow. But then I thought, well, you want to get all the properties, but it's not really useful in this representation, right? Because you have the you get your space with all the lists in there, so it's the kind of like the nesting that you want to undo. So I did that. So let's pull this out. So I thought, well, let's make some helper functions to make it a little bit easier to work with this with this representation. So I defined this function apply. Let me see if I can remember what it's doing. I'm not sure what happened here.

So here. So, yeah, I defined a function apply. It's called, it's kind of the same thing as just running the same thing, right? So, but now you don't have to, yes, this is doing the same thing as that. I define it because I was running into some trouble later on, so maybe let's get back to this later. I defined a flatten function, so this is just working on lists, right? So I'm treating two cases either, so you b and space are like parameters, and then this one is your list that you're analyzing. So either you get the empty list fed in and you get your base case nil back, or

or should be like

this, I think maybe that's right. Okay, so, or you're like this, where you say, well, or it's going to be some, some list that has a value, right? So then I'm just restructuring this list, and then, and I'm saying, Well, I'm planting it out. So in the case that, oh yeah, and here, here's where I had a question. So in the case that I that I do have a value, I'm just going to add it to some space as a side effect, right? Let, okay, that's apparently what you should be able to do with let, right? Or you say, Well, let me assign this side effect to do this variable

that does nothing and return this expression here essentially just returning the entire list, but while then also recursively applying that fat and side effect to add the atoms to the space so and then, then, then I, and then I ran into this bug here. So let me just explain what this code is doing, and then I'll show you so. So then I thought, well, I then, I can, I can use this function add to this is more a helper function, just to simplify the syntax of this. But here I'm saying, Well, I'm defining true for and false for, which allows me to kind of get the flattened representation of all these different atoms, just to remove the nesting. So this would be,

wait, no false for true, false. I thought it would be the function in the apply function, but it's not, because it doesn't match the signature. So, um, okay, well, I mean, yeah, go on.

What did I do? Because I think I always get this issue where I then I have it working, and then next couple days later, I come back. So sorry to to,

yeah, so, oh, yeah. So here's what. Here was, what was my idea? I thought, well, I'm going to call add to space. So then it would perform that adding to the space as a side effect. And then when I call false for, I'm kind of using that as a checkpoint where I'm saying, well, everything, everything that I have in that I'm able to match inside,

yeah, everything that I'm able to match Force One. I'm going to use this add to function in order to add the object to, oh, I think I know what was going on here. Just had to pass

something like that. Yeah. Maybe not.

Are you actually not using key in your

it's what I just realized. I think I wanted to add the key thing to make it yeah, let's see, right?

You want to generalize property to any cure. Here we

go. This is what I would have before. So yeah, sorry about that. Yeah. So go. Okay. So here I was. So then I thought, well, I want to get all the properties right, all the, all the true properties for the swan, but I want to get them just in a little bit of an easier representation. So let me so I thought, well, I'm going to use this adding and matching in spaces as a kind of easy way to flat, to flatten my list, if that makes sense. So I just thought, Well, okay, let me, let me, if I say false for swamp, for example, I'm assigning this side effect of i Um,

oh, yeah, of applying, of applying. Where am I calling apply up here. Oh yeah, I see Yeah, so I'll yeah, I'll end up adding like when applying false here. So Boolean All right, that's what's happening. So this expression here is essentially Swan true, right? Which was allowing me to cook, to find within the space itself all these occurrences of Swan, but all the true properties, then I so this is giving me that nested list. Then I'm flattening that result here in into, into that space, right? So I'm saying, well, that in space with some list that's going to add all the of different properties to the to the space. So that's what add to is doing. It's flattening out the result of matching Swan true or spawn false into the space, right? So then, with ADD to I could, I could perform that. So then here, when I using false four, I'm going to call add to for, yeah, I'm going to put all the false properties to false B, right? And then the final list y is

going to be assigned here, but I'm not using it. And then I wanted to return, I wanted to return this results by just matching, essentially the I want to just get anything that's inside the falsity space. So then it's all well. Now that's that's kind of useful, because now I have, I have the flat representation of of, have the flat representation of all those properties, right? So I can put the individual objects in a structured way into my space, and then I can use true for and false for, in order to get all the the flattened representation here. And then I thought, Well, okay, so now I'm kind of reached the conclusion of what I'm trying to accomplish, because now I can define a contradiction where I'm saying, Okay, well, there is a contradiction whenever, whenever I got the same property in the false space, falsity spaces in the truth space. So here, so the way that I was able to do it, and I hope it's going to work. Now, mess some stuff up, not working. Sorry, so they're

not working.

So it would say fail if there is a contradiction, right? And so you're saying

no, no, it's the opposite. It ideally, it shouldn't fail. Oh, I know why, because I had to add Phil, if it can't find anything, here we go.

Okay, this has to be removed. Maybe now, yeah, yeah. So, here we go. So, so here you can see the result on the right. So these two are from from, true for and false for. So they're just returning the returning the items in the list, because I want to be able to do that with by using match here. But it's not really what I'm after. I'm for here, like true for and false for. I'm kind of just abusing the quick syntax. But what I, what I really would be doing, is just add to, right? So I could also call add to here, it should be the same. Maybe, let's, let's try it, right? So I got, I kind of wanted to do more this where I said, well, add to truth. Thank you.

Okay, so this should be equivalent,

yeah, and so not so, then you can see in the final result here, oh yeah, because I didn't like, if you just call add to you're also getting something back,

right? Yeah,

well, I'd rather have this as return value than than what you get from doing this, right? So, but even even though I wasn't, I wasn't ideally suppressive output. But then in the fight, in the final result, you kind of see what you get, right? Because if this is full of instances of fail or nothing else, then there is not, there is no confliction that has been found.

But if you,

but if you do have it, because I said, Look, I added another one here, and this one, you can see it's funny because I'm saying that this one is not a bird, and also that it's red haired. So I'm getting two, two failure cases for red hair, because it's failing twice, right? I got two instances of two times red haired in my truth space, and once here. So that's two matches. And then also I got a bird in my true space from above. And here I'm also saying it's not a bird. So then, then, then that becomes kind of a measure, if I have a lot of observations, it could be a measure for how likely it is that there is a contradiction in

right yeah, just to be clear, could you scroll up so that I see the other call of a that is bringing right? You have two calls of Swan, right? So one is saying white bird, red hair, fish for and the other one is saying something else. And so you, you take into account the two. You accumulate all of that, right? So, so it's one is white. Is a bird from the first call, but is also from the first call. It's a red haired, I forgot what no or no. This is the first, but the second one, which is line 90, you've got these two, these two calls, you have two calls of Swan, right? And they both, they're both both taken into account, correct? Yeah, right, because you have true force one, etc, so, right, white and red hair and so and so. In there you have contradictions. And the contradiction is returning all the contradicting properties. So bird was found in both places, so that's why it returns bird, right,

and red haired was found in both places twice. And so that's why I returns. Red haired twice. Was it found right? Because twice in the Yeah, yeah, yeah, because one above, yeah, yeah, yeah, yeah, I see, I see, and then you have fail, fail. And where is that coming from?

This is just an arbitrary fallback command. So if you're not able to unify, then it will return fail.

Okay, I just want to parse the slide you to make sure I understand what it's doing. So you unify. You take the space, okay? So, like, it's like a match, but that supports failure, right? So, so you

see matching all the items in truth with this expression. So if I can, if I can find something in this expression, that it can be unified with anything in the truth space, then it will return a match. Otherwise it cannot find anything, it will fail.

And I'm not used to use this unify primitive. So, so unified. The first one is, say the left hand side that you're trying to unify are correct the for the truth is it or the truth is more like a pointer to the space you are.

Truth is so inside the space, truth your your but in the left hand side, actually, it could be. It doesn't have to right

I see. So this is the left hand side. Here's the space. It's going to be a superposition of everything that's on the space. On the right hand side, you've got something else which happens to be just a variable well wrapped in into some parentheses, and if it unifies, then you call let, y, etc. So you now you're trying to to put x inside parentheses inside y, because y is a is a fresh variable, right? So, okay, and then you try to unify. I see, right? So then, then you're trying to see

if y is in falsity, falsity, and if it happens to be, if it happens to be in falsity, then you remove it, you return it. You know, if it happens not to be, then you fail. Oh, I see, okay, okay, I get it so fail. In fact, if you were to call that on a say to space truth and falsity with lots of properties and not in common, you would receive a lot of fail, right? Yeah, yeah, I see, okay, I get it, okay.

And then I thought, You know what it would be, actually, that's why, before I had some, some key there, because I thought, well, this is, of course, good if you're talking about one object, but ideally you wanted to, you want to be able to put again, more expressions in truth and falsity, right? Like actual expressions, not just properties. So probably like for it, for the concept, to build on the concept. I thought, well, probably instead of putting a property here as it is constructor, it would just be an atom or an observation, and then the the value that, that I'm putting in there, that would just be any atom,

yeah, yeah, okay,

yeah. And so then you still kind of got that.

So I'm gonna have comments. I'm gonna have comments, but before I make the comments, I want to ask. So do you have a question about this code?

I had a question. Yeah, I had a question before. I had a problem. Oh, yeah, here. So this is my problem, so I'm calling true for only once. Okay, and I got two swans in my space, which both have two positive properties. They both have two true assertions. So I'm expecting to return, to get back from my expression, which is supposed to return match in falsity, all the items, I'm supposed to get back four items. But here there's eight of them. And when I call, when I take a look at the space here, like when I do, how do you call it? Match

when I called here, then you can see that it doesn't have eight. It actually doesn't have eight. It only has four. So somehow, in this expression, there is something weird going on where it's not actually, either it's not returning this expression, or I'm not understanding how much work

I I have a suspicion. I have the suspicion of what's going on. So so the thing is that depending on where at which point the non determinism is taking place.

Transcript limit reached

This conversation was created with an account that has a 30-minute transcription limit. Ask the owner to upgrade their plan to allow access to the full transcript.

How accurate was this transcription?

0:00:001:06:08

AI Chat

Outline

Comments