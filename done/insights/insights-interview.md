> Adam: Hey.
> Aaron: Hey.
> Adam: Yeah, uh, Draft.dev is, uh, they don't, they don't want to do two articles. They, uh, like, want to do a whole thing.
> Aaron: Oh.
> Adam: I sent an email. But it's basically like, they want to, they only do like six month, uh, engagements. Start an article cost works out to like, 20, $2,200 an article, I think.
> Aaron: Oh wow, that's a lot.
> Adam: Yeah. And then they, they do like an e-book and a lead gen thing and, uh, yeah.
> Aaron: Yeah, we probably don't want to do that. I was thinking, also, can come up with like a good sort of like, ROI model or like why we need to do that.
> Adam: Yeah, it's just like, doing the writer, like, outsourcing individual writers is a lot of work. Like, I don't think we have, like, it's almost like you need somebody to manage that, you know?
> Aaron: Yeah. Yeah, it's tricky.
> Craig: Hey folks. Hey, Dan.
> Aaron: Hey.
> Craig: Great. I don't know if we, I think Ali said she wouldn't mind joining, but I don't know if she wants to or is going to.
> Aaron: I think we should just get going. Um, Ellie may jump on.
> Craig: All right, let's do that then. So Adam, I saw your note. Um, uh, I'm, sorry, to be blunt, I'm not a fan of doing what you said for two reasons. One, I don't think I'm going to have time to do what you just said, uh, what your proposal was. And the other is, I don't think you want me on camera. Uh, I'm not a great, uh, public speaker. Uh, and so, it's, uh, it's not a forte of mine. So, my preference would be more of a traditional type demo video, um, instead of an interview type thing. Um, so, that's my feedback, uh, on the, on that proposal. Um, what, what can I, what's the right way to kind of close on the plan and what information do we need to flush out in this meeting?
> Adam: So I, I personally would love to know what we are launching. What's, what's new? What will be new? Uh, give us the walk through.
> Craig: Did you, okay. Did you see the deck that I put together?
> Adam: No. Where is it? Did you drop it here now?
> Craig: No, no, no, no. I put it together for Kathy and, um,
> Adam: No. No.
> Craig: Okay, here, let me Oh, for the sales enablement, you mean, tomorrow?
> Adam: Yeah.
> Craig: Okay. Well, no, it is here. Let's see it. Yeah, this is, uh, there's a, um, Kathy copied these into a separate deck, but this is close enough. So, um, in terms of the, the sales enablement was more about what are we delivering and then also what's the future roadmap. And really, the roadmap is four, four areas. And what we're delivering on December 2nd is the first one, is discovery. Um, discovery is, is all about just discovering your sea of chaos, your infrastructure. And the, there really is only one feature we're delivering on December 2nd. And that's just discovery. And let me just demo a little bit of it and then we can get into what we're delivering in the future if we have time, but, so, generally it's, uh, the, there's a UI in, on, in front of discovery. And then there's, we're scanning and finding all of your resources. And this, this is the feature we're delivering. By doing this and by bringing the resources into the same infrastructure that we use for IAC, it unlocks three things. It unlocks, um, policy. So it unlocks Cross Guard against discovered resources. It unlocks resource search and the resource explorer UI. And it unlocks co-pilot. Um, so from, let me, let me go into the demo then. And, um, so, uh, the, the feature from a user perspective, the feature is accounts. Accounts are like stack, like the stacks feature. This is a list of all of the different accounts, uh, and you can create a new account. Account manages a scan. So you go in, you create an account, you specify what provider you want. You give it a name for the account, an ESC environment that manages the credentials needed to scan. What, in the case of Azure, or in case, in case of AWS, what regions you want to scan, and what policies you want to apply to that scan, what policy groups. And then you're done. Uh, and this will then scan every 24 hours or manually if there's a scan, there's a scan button. So if I go back to here, um, uh, actually it's not hooked up in this UI. This, this, the problem we have from a demo perspective is this UI is still work in progress. While it's, um, while this UI is here, it's not hooked up. Uh, so this is not working UI, right?
> Adam: And just to ask you, do you specify what you're scanning for? Like, what are, when you scan, what are No, you're scanning everything. You have no control over what resource types. We scan everything. And the reason for that is there's a catch 22, is that we don't know, you don't know what resource types you have to even tell us what to scan for. So,
> Adam: Okay. Okay. So you scan and then,
> Craig: And then all the resources show up in the resources explorer. Here. Um, intermixed with your IAC resources. You will be able to filter of what's insights resources. I have a, a pre-filter here. Um, you'll be able to tell what's managed by IAC and what's not. Um, but they're just, they show up in the resource explorer, they show up in resource search. So all of the search capabilities that you've had before, including AI search, all are enabled. So you can do things like, I want to know for, I've filtered to only, uh, these are only insights, discovered resources. Okay. So I have, uh, 12,000 discovered resources. And this is in the Pulumi, um, production account. And so I can see, you know, what I have. Here's my storage, um, resources. And I can drill in in the same way that I, I could before in terms of seeing all of its metadata properties. Um, the, when, when we do a scan, the policies that you've assigned to the account will run anytime we see a new resource or a changed resource. We'll run policy against those resources. And the policy violations that show up will show up here in the policy violations page. So any violations that you have in your infrastructure outside of IAC will show up here. And again, you have all the abilities of the policy violations page to, to be able to group, um, you know, where you're having issues and, and start to understand where the policy violations are. You can also in co-pilot ask questions about, you know, do I have any, um, uh, VPCs that are exposed to the internet? Or whatever classic questions you ask about your IAC resources, you can now ask about your non-IAC resources. And this turns out to be even more powerful because with IAC resources, you've kind of thought through, you have programmatically designed your infrastructure in code. Right? With non-IAC resources, it's a wild, wild west. And so the ability to ask questions of that side of it is actually even more powerful than, than the IAC side of things. Because you, you don't know, like it is chaos. The whole point of insights is to be able to wrap your arms around, what are all my departments doing? Or I've acquired 14 companies in the last year and we've brought in a bunch of crap and I have no idea what's going on. Or these sorts of scenarios. And that's where co-pilot itself helps. So, the summary to your, to your question was, what are we enabling? It's discovery. But once you have discovery, resource search, policy violations, and co-pilot are enabled.
> Aaron: How do I, so how do I see the accounts work in progress page? And I, I also don't have these drop downs.
> Craig: You don't, you don't have it on, it's not on Adam for you?
> Aaron: No.
> Craig: Okay.
> Aaron: I don't have the under resources. I don't know if I just have the resource thing as well. I don't have
> Craig: These are, these are just saved queries.
> Aaron: Oh, those just, I was wondering. Yeah, okay.
> Craig: I just created a query and then, and hit save.
> Aaron: Oh, okay. That makes sense. Um, so, uh, I'll, I'll can get that, uh, the accounts page turned on for you.
> Aaron: So what's like a, uh, yeah, what's, what's the exciting, like, use case? Like you said, like, what would you highlight?
> Craig: That's, that's the, the problem here. Um, uh, because it's, it's about wrapping your arms around the breadth. Um, it's the exact same scenarios you would highlight for IAC. It's just you would highlight it for non-IAC resources. But that's hard to demo, that, the fact that it's, um, non-IAC.
> Aaron: Well, maybe not, but like, what, what, uh, let's pick one. Like, what would be interesting? Like, oh, a public S3 bucket that we didn't know existed or Right. Yeah, yeah. Is that one of the, like, what's the sexy use case, I guess, is what I'm thinking?
> Craig: Well, a lot of it is policy, right? So, um, uh, do I have policy violations against non, so, sock compliance issues or security issues related to, um, you know, Kubernetes, uh, configuration issues. Um,
> Adam: The, these three issues that you showed us, the example, how, does insights bubble this up and highlights, okay, these resources have issues, or do you somehow have to read the laundry list of resources and figure out which is okay, which is not working or has issues?
> Craig: On the policy violations, these are all of the resources that have issues. That's what this page is. So here's the resource here that has, it has this issue.
> Adam: I see.
> Craig: If you go into it, it shows you the issue right here, the details.
> Adam: Does it show you how to fix it?
> Craig: No. In these cases, no. We, they're not, there are some policies that, if the policy is written in a certain way, that it could, it's called a remediation policy. This exists, has existed for the last two years, uh, the remediation policies. And that if they're written in a way that it could show you how to fix it, but I don't know what percentage of our policies are actually written as remediation policies.
> Adam: Okay. So policy is the use case that you think is the most exciting, most Well, it's the one that answers your question the most. The, the biggest thing is, um, I actually think the biggest one is just bringing it into the resources explorer and doing things like knowing how many storage resources do I have? Why do I have 1,500 storage resources? Answering questions like that of like, I had no idea about this. Why? It's not, like, lots of people have pointed out, lots of customers and stuff, it's the simple questions. It's like, uh, what the hell do you mean I have 82,000 total resources? What the hell? I thought I had 1,000. It's those simple things like that a lot of them, as it really is, I don't know what I don't know. I don't, like again, I had acquired some companies. I don't know what infrastructure they have or what my departments created because somebody got a root login for AWS console. Um, so a lot of it really is just the simple questions. That's the first one. Wrap your arms around the sea of chaos. The second one is then, okay, give me insights into it, like policy violations. Like, am I running GP3 volume instances where I really only need GP2 or GP1, you know, sized instances? Um, uh, do I have, you know, show me the IP address of, uh, of this particular VPC. Uh, well, that's not a policy one. That's just a resource or a co-pilot question. Um, so, any way that you would have marketed or sold IAC specific cloud console scenarios apply to non-IAC now.
> Aaron: Yeah, makes sense. I'm just clicking around here. And, yeah, this is the, um, the hard part about it is on one hand, you're seeing nothing new. Right? We've had the resource search for, you know, year and a half or two years now. We've had the policy violations explorer for six months. We've had co-pilot for a year. Right? So those end features have existed for a long time. And now,
> Adam: Yeah, but the new thing is that now it's available to all your resources, not just for Pulumi, right? That's Right. Which is huge. I'm just saying the, the visible features, there aren't visible features. It's that we've made those visible features an order of magnitude more powerful now. Like, most companies that most of our, our, um, customers are not running 100% IAC. They're like in some degree of the process of getting to IAC. They've got like 10% of their resources. And, and I love the quote of, um, the guy from Israel, um, I don't know, DoiT or something. It was one of the companies. And he was like, if my CEO asked me how far along I am of the project of moving resources to IAC, I have no idea what to tell them. Because I have no idea how many resources I have. I don't know if I'm 10% of the way there or I'm 90% of the way there. I have no idea. We're picking resource types off one by one, but I have no idea. Because I need to know the scope of my infrastructure. So just answering that question provides a sense of comfort and, and understanding that, oh, oh, I see, yeah, I've got like 30,000 resources. Where are they all? Why are they here? What are the, um, and then what are the problems with them? And that's where the policy part comes in. It's really this two stage, right? Understanding and insights.
> Adam: So getting clay of the land of your infrastructure, all the resources, and then step two, uncovering potential issues.
> Craig: Right.
> Adam: Yeah, and some landmines.
> Craig: Right. And this is kind of, Ellie, this is kind of where I've been having this, this, you know, challenge of this December 2nd launch, is there's not much, it's not complete, right? There's not much to it. Because we haven't started adding in things like the, you know, the dashboard where, you know, you can start to track your projects over time, or the ability to do resource tagging so that when you discover something interesting, you can tag those resources as they're interesting in this way. You know, keep, let me keep track of it and then I can group and search by or, uh, sort by them. Or if I have a policy, how do I burn down my policy violations page? Right? How do I, because you always want this page to be zero. Nothing in it. Right? I have no violations. So as I work through them, how can I tag them as, no, that's one I don't care about. Triage it away. Or how do I work, how do I create tickets for my devs to actually go and solve what this problem represents? Those sorts of scenarios, that's what's next year. What we're delivering right now is just this base sort of, okay, first thing is I have to know everything I got. And that's what we're delivering is just that. Um, and, and that's really, like if you talk to folks, even just like Motive Care or, um, even what Snowflake is doing internally, or even what Nvidia now has internally, it's just that. It's just bring it in, let me see what I got. Their internal tools that they've built themselves is just bring it into a data warehouse and let me start putting, doing some understanding side.
> Aaron: So I appreciate the fact that we're just, let me see what we got, and we got a bunch of stuff imported in. How do you make sense of this chaos beyond just continue to run a bunch of queries yourself? Because there's a lot of resources, right? Like, and there's a lot of noise. Like, I'm not sure what the insight, you know, the true insights are other than I have a lot. Um, like, I think the other thing I, I, in our marketing materials once upon a time, like, we talk about the super graph, right? And the super graph like has interrelationships between the resources. Um, I'm playing around with it on the side over here and I don't really see many like interrelationships, like inferring stacks. Um, non, non-IAC stacks with each other. Um, is that stuff coming or is that like possible to infer? Um, just trying to understand that a bit more.
> Craig: So, um, uh, yeah, right now, one of the things you, one of the limitations, like today, this will be fixed later this week, you can't get to a resource details page for, um, uh, non-IAC resources. And, uh, what you will see is a page that's somewhat like this for IAC resources. It's somewhat like this. At the bottom here, you will see relationships. And you'll see, uh, uh, sorry, references. And you'll see references in and references out. So as a table. One of the features for next year, um, again, not now, but one of the features for next year is showing that as a, as a graph. So, um,
> Aaron: All right, let me, let me ask a very, um, I don't even know if it's a dumb or smart question here. So, um, we're trying to launch essentially it's like now you have the ability to import and sync and then you get your resources, policy violations, and co-pilot on, on non-IAC resources, right? That's essentially what we have.
> Craig: Right.
> Aaron: Like, are we expecting customers to sign up or are we expecting to just have, be able to have more sales conversations?
> Craig: I mean, it's largely, this was the conversation kind of that, you know, Ali and Bob and I had a couple weeks ago, which is the launch, I think what we agreed to is more end of January. This is getting people interested in trying, whether that's sales engagement type things or even self-service. Um, but it's, it's not launch in the sense of
> Adam: Yeah, for launch we're not going to do press. Basically, we just want to get people to use it. Hence why the, the, the video is important, especially the video. Let's hope the product landing page, but the video to show people, to give them ideas. Hey, ah, that's what I can
> Aaron: Like, basically, you do know that this isn't really different than what we launched with, like, pre-announced, right?
> Adam: It's not.
> Aaron: I, I
> Craig: No. Yeah. This is effectively, remember what we talked about at PulumiUP? Now you can actually go do it.
> Aaron: This is exactly the same. You just actually have it mocked, like, outside of staging.
> Adam: Now it's live. Yeah. It's actually live.
> Aaron: Okay. So this is what I'm hearing.
> Craig: Well, more, more, more carefully, it's less than what we announced at PulumiUP, because at PulumiUP we talked about some of the January and February, March things, right? So this is the first step of that vision we talked about at PulumiUP. This is step one of a three or four steps.
> Aaron: Yeah, so, okay. Adam, look, you're essentially creating another teaser trailer of this. And we're, we're essentially trying to get another shot of making noise by saying there's something new. That's all.
> Craig: Making noise, not necessarily in the press contexts.
> Aaron: Making noise into practitioner user contexts.
> Craig: Yeah. Yeah. But, uh,
> Aaron: Yeah, I come away with this going like, okay, well, we sort of announced this already. Like, we're, we're, you know, it's sort of, it's sort of what we, in some ways, it's exactly the same go-to-market that we currently have, which is sign up for the wait list, talk to sales. And then Craig at some point talks to you.
> Craig: You no longer have to sign up to the wait list is what's changed. There's no wait list anywhere.
> Aaron: Okay. But that, the wait list goes away.
> Craig: You just, just sign up to use it. Just do it.
> Aaron: Yeah. So, Adam, I, I think this is pretty simple. It's simple-ish, right? Take a look at Craig's demo at Reinvent and you're essentially just going to cover, you know, you can write out the, like, you know, the 30 second script, like, "Hey, want to talk about, like, insights and what we got prepared for you. Today, we announce, you know, the feature, the import feature that we talked about at PulumiUP. Um, check this out. You can import Azure, AWS, all these resources. Um, and, uh, when you import it all, you now have the ability to search upon it, uh, check for policies, and do co-pilot." All right, well, let's, let's jump in and see how this works. Right? You'll show us like, hey, we're going to do AWS, we're going to do ESC, um, and, like, credentials. And then this allows us to sync, you know, you go, okay, let's wait for it to sync. Okay, now let's look at all the resources I imported. Oh, cool. All right. Well, I can do search, I can move around, um, you know, go through, essentially show off the resource.
> Adam: And also show the, the total resources at the top. Oh, now I have this many resources. Show the list. The
> Aaron: Yeah. So I'm not sure if we need to do it from scratch and import to another organization. I don't know what you recommend there, Craig. Like,
> Craig: I kind of, I, I kind of would because your counts are, like this sort of thing are going to be off. I, I think you want to, well, there's an interesting question of, are you targeting our existing IAC users, which point they would already have some resources, or are you targeting brand new users? I would have thought more the brand new scenario, but
> Aaron: We're targeting people that have no IAC, right? Like, or just like, we're just targeting people that just have a shit ton of infrastructure and they need to import it.
> Craig: So I would probably start with a blank. Um,
> Aaron: Okay, so Adam, you will start with a blank and import Pulumi's AWS account.
> Adam: Yeah, yeah.
> Aaron: Yeah. Um, so,
> Craig: That takes, that, right now that takes seven minutes.
> Aaron: That's pretty darn fast and sort of scary. So does the, does that part work yet, the importing, you said?
> Craig: Yeah, yeah. It's, so, um, uh, what you're actually seeing here is live. Like, these are our live accounts.
> Aaron: Okay. Okay. Um, what else do you need to know, Adam?
> Adam: Um, I don't know. Yeah. Um, yeah, so create new org, walk through, doing the import, and then show, oh, here's the resources. You can ask some questions. Um,
> Aaron: Or Craig, could he delete your sync and then resync it? That way he gets the benefits of the Pulumi org and all the setup, existing credentials.
> Craig: Um, yes, yes, I believe so. Yes, I think we can do that through the console. Delete, delete the accounts.
> Aaron: Like, delete essentially this account.
> Craig: This, this is not set up right yet.
> Aaron: Yes. I saw that feature and I'm like, okay, we can just delete it and then just start from scratch.
> Craig: I can, I, maybe this, maybe, this is literally changing hourly. So I can ask if they,
> Aaron: Adam, try replicating another organization that, like, where you can import a bigger AWS account, and seeing how we get. So that's going to require you to set up a YDC and Pulumi ESC and, like,
> Craig: Well, let me see if I can, we can delete it. Um,
> Aaron: Right now, I don't even have like this page.
> Craig: Yeah, I know. Well, I'll, I'll get that turned on for you.
> Aaron: Okay. Um, I lost the thread. We're going
> Craig: Let me see if I can, we can delete these for you so that you can actually just do this from scratch.
> Aaron: Yeah, I mean, that would be easy. Yeah, if I could just use the existing Pulumi account. Yeah.
> Craig: Yeah. Yeah.
> Aaron: All right, so we probably have to delete all of those, right?
> Craig: Yeah, we'll delete them all. Well, here, actually, this is, this is mine. Let me just see what happens.
> Aaron: Wait, how much of Pulumi is not managed by IAC? I'm now, um, sort of slightly, uh, interested in seeing.
> Craig: Honestly, we don't know. Oh, it did delete it. I don't know if, did it delete all my resources?
> Aaron: I would just go back to the dashboard and see if they dropped. Well, no, it hasn't.
> Craig: Yeah, so I'm not, I think it's deleting the account, but it's not iterating, walking through and deleting all the resources for, that's under the account.
> Aaron: Fun times.
> Craig: Um, which, which I, I believe we can do through the console. But when are you, when are you planning on, on trying, on actually recording this, Adam?
> Adam: Uh, I don't know. Yeah, it's a good question. Um,
> Craig: A lot of this will be working by, you know, end of, end of the week, early next week.
> Adam: Okay. Well, that works. I mean, the end of the week is pretty soon.
> Craig: Yeah. Well, it kind of has to because Thanksgiving and then launch.
> Adam: Yeah, yeah. Um, so we would need this by December 10th, but we need it to get it to the editor as well.
> Craig: Right. But I don't, as, as, I think as Aaron said, I don't think the video is long or complicated.
> Adam: Yeah, yeah.
> Craig: Right? We want to keep it pretty simple and a snack for people.
> Adam: Um, okay. Yeah, I will start working on it soon. I don't know, I think.
> Craig: Um, well, we'll get you the, the, um, uh, access to the accounts first. And then I'll find out if, if we can delete the resources associated with accounts or when we will be able to do that and clean up our resource counts.
> Adam: Sounds like a plan. Okay. Yeah, it works.
> Craig: All right. I'll let you know. Cool. Thank you for your help. Um, and yeah, I think figuring out the scenario, the demo scenarios is the, the challenge here is the thing that I think we're all struggling with.
> Adam: Hey, I just have one, uh, another question, non-video related. So Bob wanted for the sales team some sort of a proof of value doc. Proof of value, business value. How should we, how do you advise us to proceed here?
> Craig: Proof of business value.
> Adam: Yeah. Uh, so basically something to show the sales team at Reinvent if they're talking to decision makers, why they should care about insights, what value insights brings, but somehow for us to prove it.
> Craig: Is that not the same thing as what are the demo scenarios? Like, I don't know what, what a business value doc tends to look like. Like, the, the, you know, there's the high level PRFAQ type statements of, you know, that you, you are now able to gain visibility and understanding into your entire infrastructure, right? Where you, you know, previously you would have struggled to, to understand the scope of your infrastructure and any of the particular issues that are outside of the mainline purview. Uh, and now insights lights that up, uh, and, in, in your, your experience and provides you the tools to understand and manage that, all of your infrastructure, not just the IAC. That's the high level sense. Um, the proof points are the scanning and then the ability, the demo scenarios of, you know, showing me the counts, showing me, being able to ask co-pilot what's open to the internet, being able to show policy, sock two policy violations, or, um, you know, that kind of thing. That's, so that I can, like, oh shit, I didn't know blah. I didn't know that I had this. And, oh, thank you for, for highlighting that for me so that I can now go and fix it. And now I can use IAC to go and correct the issues.
> Adam: Okay.
> Aaron: What was the, uh, document that you were sharing at the beginning, Craig? Is that useful for me or?
> Craig: Yeah, sure. There's, um, in the, yeah, let me share again.
> Aaron: Just send a link maybe or
> Craig: Yeah. So this directory is all of the specs for, um, but there's also like technical specs and stuff like that. The one that, this was the, so phase one is the discovery. Phase two is more understanding. This is, you know, what we're going to do between now and, uh, January, end of January, where we're adding in more information, more ability to scan more of your infrastructure. Uh, and then phase three is starting to do a lot more of the value add things on top for managing, for, for understanding things, like the, the graphs that you were asking about, um, improvements to policy, making policy a lot easier to build and, and manage. And then the last one is all the, is, you know, helping you actually now actively improve your infrastructure by building out a lot of the workflows for, you know, integrations with ticket management systems like Jira or code generation for IAC code generation. That sort of thing. So that's what this document shows.
> Aaron: Cool.
> Craig: I can, yeah, I can forward that to you.
> Aaron: I found it.
> Craig: Okay. No, that's helpful. Okay. But these, again, right now, December is just phase one.
> Aaron: Yeah, yeah. Exactly. It's just the first.
> Craig: Yeah. Cool. I'm sure I'll have more questions.
> Aaron: You know where to find me.
> Craig: So again, I really appreciate the help. And, and yeah, things are coming very hot here, which is why there's not a lot of, and it's our first foray, you know, into this. And so there's not a lot to go on, but
> Adam: And can you, can you drop here in the, in the Zoom channel that deck, link to the deck?
> Craig: The one I just showed?
> Adam: Yeah.
> Craig: Yeah, sure.
> Adam: Okay. In that same folder, there's other content that might also be interesting, right? Of
> Adam: The Pangaea folder. Okay. Yeah. I know how to get to it. Okay. Cool.
> Aaron: So I guess since we still have you here, Craig, uh, or wait, did we go over time?
> Craig: Yeah, we're over time.
> Aaron: Okay. Well, I was going to ask you about the detail page that you don't have time for and figure out what a hybrid potential thing we could do on that. The what?
> Craig: The detail page, the insights detail page, the product page?
> Aaron: The product page.
> Craig: Oh yeah.
> Aaron: Yeah, I was just trying to find what happy compromise we could do in terms of rewriting it. Maybe you and I just need to brainstorm for 30 minutes.
> Craig: I think, I think that's, I think that'