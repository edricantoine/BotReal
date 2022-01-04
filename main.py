# bot.py
import os
import discord
import requests
import json
import random
import twentyOne

client = discord.Client()
twentyOne = twentyOne.twentyOne(client)
happyWords = ["angry", "mad", "trash", "bad", "loser", "garbage", "pissed", "frustrated"]
gameBeingPlayed = False
sadStatements = [
    "COPIUMCOPIUMCOPIUM"
    "Nobody cares that you feel that way",
    "Cope, seethe, mald",
    "Doin ur mom",
    "Cry more"
]
GUILD = 'GUILD.'


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    for channel in guild.text_channels:
        await channel.send("I am here to make your lives miserable")


@client.event
async def on_message(message):
    global gameBeingPlayed
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!hello'):
        await message.channel.send("Fuck you. You useless piece of shit. You absolute waste of space and air. You "
                                   "uneducated, ignorant, idiotic dumb swine, you’re an absolute embarrassment to "
                                   "humanity and all life as a whole. The magnitude of your failure just now is so "
                                   "indescribably massive that one hundred years into the future your name will be "
                                   "used as moniker of evil for heretics. Even if all of humanity put together their "
                                   "collective intelligence there is no conceivable way they could have thought up a "
                                   "way to fuck up on the unimaginable scale you just did. When Jesus died for our "
                                   "sins, he must not have seen the sacrilegious act we just witnessed you "
                                   "performing, because if he did he would have forsaken humanity long ago so that "
                                   "your birth may have never become reality. After you die, your skeleton will be "
                                   "displayed in a museum after being scientifically researched so that all future "
                                   "generations may learn not to generate your bone structure, because every tiny "
                                   "detail anyone may have in common with you degrades them to a useless piece of "
                                   "trash and a burden to society. No wonder your father questioned whether or not "
                                   "your were truly his son, for you'd have to not be a waste of carbon matter for "
                                   "anyone to love you like a family member. Your birth made it so that mankind is "
                                   "worse of in every way you can possibly imagine, and you have made it so that "
                                   "society can never really recover into a state of organization. Everything has "
                                   "forever fallen into a bewildering chaos, through which unrecognizable core, "
                                   "you can only find misfortune. I would say the apocalypse is upon us but this is "
                                   "merely the closest word humans have for the sheer scale of horror that is now "
                                   "reality. You have forever condemned everyone you love and know into an eternal "
                                   "state of suffering, worse than any human concept of hell. You are such an unholy "
                                   "being, that if you step within a one hundred foot radius of a holy place or a "
                                   "place that has ever been deemed important by anyone, your distorted sac religious "
                                   "soul will ruin whatever meaning it ever had beyond repair. You are an idiotic, "
                                   "shiteating, dumbass ape and no one has ever loved you. Rhodes Island would have "
                                   "been better off if you'd never joined us. You are a lying, backstabbing, "
                                   "cowardly useless piece of shit and I hate you with every single part of my being. "
                                   "Even this worlds finest writers and poets from throughout the ages could never "
                                   "hope to accurately describe the scale on which you just fucked up, "
                                   "and how incredibly idiotic you are. Anyone that believes in any religion out "
                                   "there should now realize that they have been wrong this entire time, "
                                   "for if divine beings were real, they would never have allowed a being such as you "
                                   "to stain the earth and this universe. In the future there will be horror stories "
                                   "made about you, with the scariest part of them being that the reader has to "
                                   "realize that such an indescribable monster actually exists, and that the horrific "
                                   "events from the movie have actually taken place in the same world that they live "
                                   "in right now. You are the absolute embodiment of everything that has ever been "
                                   "wrong on this earth, yet you manage to make it so that that is only a small part "
                                   "of the evil that is your being. Never in the history of mankind has there been "
                                   "anyone that could have predicted such an eldrich abomination, but here you are. "
                                   "It’s hard to believe that I am seeing such an incredible failure with my own "
                                   "eyes, but here I am, so unfortunately I cannot deny your existence. Even if I did "
                                   "my very best, my vocabulary is not able to describe the sheer magnitude of the "
                                   "idiotic mistake that is you. Even if time travel some day will be invented, "
                                   "there still would not be a single soul willing to go back in time to before this "
                                   "moment to fix history, because having to witness such incredible horrors if they "
                                   "failed would have to many mental and physical drawbacks that not even the bravest "
                                   "soul in history would be willing to risk it. I cannot imagine the pure dread your "
                                   "mother must have felt when she had to carry a baby for nine months and then "
                                   "giving birth to such a wretched monster as you. Not a single word of the "
                                   "incoherent, illogical rambling you may be wanting to do to defend yourself or "
                                   "apologize would ever be able to make up for what you just did. The countries of "
                                   "the world would have wanted to make laws preventing such a terrible event like "
                                   "this from ever happening again, but sadly this is not possible since your "
                                   "horrific actions just now have shattered every form of order this world once had, "
                                   "making concepts such as laws irrelevant. Right from the moment I first set my "
                                   "eyes on you I knew you were an absolute abomination of everything that is wrong "
                                   "with humanity. I was hoping I would have been able to prevent your evil from "
                                   "being released upon this world by tagging along and keeping my eye on you, "
                                   "but it is clear to me now that not even the greatest efforts would have been able "
                                   "to prevent a terrible event in this scale from occurring. You are the worst human "
                                   "being, or even just being in general, that I have ever had the misfortune of "
                                   "witnessing. Events like the infected plague apparently only happened with the "
                                   "goal of teaching humanity to survive such a horrible event as the one you just "
                                   "created, but not even mankind’s greatest trials were able to even slightly "
                                   "prepare anyone for the insufferable evil you have just created. If you ever had "
                                   "them, your children would be preemptively killed to protect this universe from "
                                   "the possibility of anyone in your bloodline being even half as bad as you are, "
                                   "except you will never be able to have children, because not a single human being "
                                   "will ever want to come within a hundred mile radius of you and anything you have "
                                   "ever touched. You are a colossal disappointment not only to your parents, "
                                   "but to your ancestors and entire bloodline. The disgusting mistake that you have "
                                   "just made is so incredibly terrible that everyone who would ever be to hear about "
                                   "it would spontaneously feel an indescribable mixture of immense anger, "
                                   "fear and anxiety that emotionally and physically they would never truly be the "
                                   "same ever again. The sheer scale of your mistake, if ever to be materialized, "
                                   "would not only surpass the size of the world, but it would reach far beyond the "
                                   "edges of the known, and almost certainly the unknown universe. I could sit here "
                                   "and write paragraphs, nay, books describing your immense failure, yet even if I "
                                   "were to dedicate my life to describing the reality of what has just gone down "
                                   "here, and I would spend every moment of it until my heart stops beating working "
                                   "as hard and efficiently as possible, yet there is not even a snowballs chance in "
                                   "hell that I would be able to come close to transcribing the absolute shitshow you "
                                   "have just released upon the world. You are an irresponsible, idiotic, disgusting, "
                                   "unloved, horrible excuse for a living being who’s soul contains less humanity "
                                   "than every ginger in history combined. The absolute disgust I feel when thinking "
                                   "about anything that has even a slight resemblance to anything that might have to "
                                   "do with you and your unholy actions is so incredibly great that when I am honest "
                                   "about it I think that even I do not posses a consciousness great enough to "
                                   "comprehend my own feelings about it. When people of Columbia fought to break free "
                                   "from Lungmen, countless soldiers fought and lost their lives in favor of a chance "
                                   "at a better future for their children, they did not give their lives to have you "
                                   "fuck the world up beyond repair to the degree that you are doing right now. "
                                   "Honestly, even when technology advances and studies on the subject become more "
                                   "and more accurate, I do not think humanity will ever truly be able to understand "
                                   "what your failure actually means for the universe. My hate for you and everything "
                                   "you stand for is so much deeper than the depths of Shambala that you could "
                                   "probably take the entire Lungmen population down there and back up around twenty "
                                   "million times before you would have sunk to the end of my hate, and honestly, "
                                   "I do not want to exaggerate, but I think that that insult was low balling it such "
                                   "a massive amount that all mountains in this world combined would not be able to "
                                   "stack up to this imprecise judgement in light of the fact that when being honest, "
                                   "my hate is almost certainly bottomless. There is no one in this world that has "
                                   "ever loved you, and especially after what you just did, no one will ever love you "
                                   "in the future either. There is no hope that your idiotic behavior and especially "
                                   "your crooked soul will ever change for the better, and in fact quite the opposite "
                                   "might be true. By making the mistake that you just did, you have shown me that "
                                   "you are so incredibly hopeless that you will only devolve into a more idiotic and "
                                   "wretched creature than you already are. The only possible way in which your "
                                   "future would be brighter than the black hole your existence currently is would "
                                   "exclusively be because there is absolutely no conceivable way that you would even "
                                   "be able to sink lower than the pathetic place your current failure has put you "
                                   "in.")

    if msg.startswith('!exit'):
        await message.channel.send('Aight imma head out')
        await client.close()
        exit()

    if msg.startswith('!21') and not gameBeingPlayed:
        await twentyOne.start(message.channel)
        gameBeingPlayed = True

    if msg.startswith('!stop21'):
        await twentyOne.setChannel(message.channel)
        await twentyOne.stop()
        gameBeingPlayed = False

    if msg.startswith('!score21'):
        await twentyOne.setChannel(message.channel)
        await twentyOne.print()

    if msg.startswith('!hit') and twentyOne.started():
        if twentyOne.isp1turn():
            await twentyOne.onehit()
            await twentyOne.changeTurntoP2()
            await twentyOne.turn2()
        else:
            await twentyOne.twohit()
            await twentyOne.changeTurntoP1()
            await twentyOne.addToScores()

    if msg.startswith('!stay') and twentyOne.started():
        if twentyOne.isp1turn():
            await twentyOne.onestay()
            await twentyOne.changeTurntoP2()
            await twentyOne.turn2()
        else:
            await twentyOne.twostay()
            await twentyOne.changeTurntoP1()
            await twentyOne.addToScores()

    if any(word in msg for word in happyWords):
        await message.channel.send(random.choice(sadStatements))

    if 'laptop' in msg:
        await message.channel.send("Today when I walked into my economics class I saw something I dread every time I "
                                   "close my eyes. Someone had brought their new gaming laptop to class. The Forklift "
                                   "he used to bring it was still running idle at the back. I started sweating as I "
                                   "sat down and gazed over at the 700lb beast that was his laptop. He had already "
                                   "reinforced his desk with steel support beams and was in the process of finding an "
                                   "outlet for a power cable thicker than Amy Schumer's thigh. I start shaking. I "
                                   "keep telling myself I'm going to be alright and that there's nothing to worry "
                                   "about. He somehow finds a fucking outlet. Tears are running down my cheeks as I "
                                   "send my last texts to my family saying I love them. The teacher starts the "
                                   "lecture, and the student turns his laptop on. The colored lights on his RGB "
                                   "Backlit keyboard flare to life like a nuclear flash, and a deep humming fills my "
                                   "ears and shakes my very soul. The entire city power grid goes dark. The classroom "
                                   "begins to shake as the massive fans begin to spin. In mere seconds my world has "
                                   "gone from vibrant life, to a dark, earth shattering void where my body is getting "
                                   "torn apart by the 150mph gale force winds and the 500 decibel groan of the "
                                   "cooling fans. As my body finally surrenders, I weep, as my school and my city go "
                                   "under. I fucking hate gaming laptops.")

    if 'meow' in msg:
        await message.channel.send(
            "Wowwwww, you meow like a cat! That means you are one, right? Shut the fuck up. If you really want to "
            "be put on a leash and treated like a domestic animal then that’s called a fetish, not “quirky” or "
            "“cute”. What part of you seriously thinks that any part of acting like a feline establishes a "
            "reputation of appreciation? Is it your lack of any defining aspect of personality that urges you to "
            "resort to shitty representations of cats to create an illusion of meaning in your worthless life? "
            "Wearing “cat ears” in the shape of headbands further notes the complete absence of human attribution "
            "to your false sense of personality, such as intelligence or charisma in any form or shape. Where do "
            "you think this mindset’s gonna lead you? You think you’re funny, random, quirky even? What makes you "
            "think that acting like a fucking cat will make a goddamn hyena laugh? I, personally, feel extremely "
            "sympathetic towards you as your only escape from the worthless thing you call your existence is to "
            "pretend to be an animal. But it’s not a worthy choice to assert this horrifying fact as a dominant "
            "trait, mainly because personality traits require an initial personality to lay their foundation on. "
            "You’re not worthy of anybody’s time, so go fuck off, “cat-girl”.")

    if 'racist' in msg or 'racism' in msg:
        await message.channel.send("My fellow Americans, due to the overwhelming amount of Black squares teenage "
                                   "girls are posting on Instagram, the supreme court has decided end racism "
                                   "completely. We did not think you would go to such extreme measures but you "
                                   "have very much proved your point. The Military will be told to stand down "
                                   "just please stop. Thank you")

    if 'cancer' in msg:
        await message.channel.send("Ive had a nasty cough for the past few days, so I went to the doctor to see "
                                   "if it was Corona. He said 'its not corona' Woohoo! But then, he said 'You "
                                   "have every type of cancer and you will die in three (3) days. I thought I "
                                   "should say goodbye to my reddit family before I go.")
        await message.channel.send("TLDR: I will die in three (3) days")

        for x in range(3):
            await message.channel.send("Edit: Thanks for the gold kind stranger!")

        await message.channel.send("Edit: Okay which one of you fuckwits gave me silver? Do you think this is "
                                   "funny? Do you think this is some kind of joke? I open my heart and soul to "
                                   "you, and you give me this shit? Unbelievable.")

        for x in range(3):
            await message.channel.send("Edit: Thanks for the gold kind stranger!")

        await message.channel.send("Edit: OMG! I just went back to the doctor, and he told me the the four (4) "
                                   "years of reddit premium which you collectively gave me cured my cancer! This "
                                   "is so wholesome! Thanks guys.")

    if 'legos' in msg:
        await message.channel.send("There are no such things as 'Legos'. They don't exist. 'Lego' refers to the "
                                   "COMPANY THAT MAKES THE TOY, and thus the shortening Lego is acceptable. Saying "
                                   "'I'm playing with my Lego' works because it's referring to the sets themselves: "
                                   "The individuals aspects that make of the toy from the bricks to the mini-figures "
                                   "to the electronics to the other little parts. It isn't claiming that the fucking "
                                   "square bricks are each a Lego. THE ENTIRE THING IS. If you were to say 'I'm "
                                   "playing with my Legos' that implies that you're playing with at least two "
                                   "different types of Lego set at once, i.e. Lego City and Bionicle.")

    if 'hunting' in msg or 'hunt' in msg:
        await message.channel.send("If you want to be proud of a large animal you killed then you need to kill it "
                                   "with a spear. Seriously where is the challenge in killing a Buffalo with a high "
                                   "caliber rifle round from long range? Congrats, the animal never saw it coming! "
                                   "Your supersonic lead blew its brains out from 300 yards with the flick of a "
                                   "finger. Man the fuck up and fight the animal 1v1. It’s got horns, and you have "
                                   "got a spear. It has brawn, and you have brains. Test your agility against its "
                                   "brute strength. Cut its heart out and eat it raw. Then I might be impressed.")

    if 'based' in msg:
        await message.channel.send("Based? Based on what? In your dick? Please shut the fuck up and use words "
                                   "properly you fuckin troglodyte, do you think God gave us a freedom of speech just "
                                   "to spew random words that have no meaning that doesn't even correllate to the "
                                   "topic of the conversation? Like please you always complain about why no one talks "
                                   "to you or no one expresses their opinions on you because you're always spewing "
                                   "random shit like poggers based cringe and when you try to explain what it is and "
                                   "you just say that it's funny like what? What the fuck is funny about that do you "
                                   "think you'll just become a stand-up comedian that will get a standing ovation "
                                   "just because you said 'cum' in the stage? HELL NO YOU FUCKIN IDIOT, "
                                   "so please shut the fuck up and use words properly you dumb bitch")

    if 'amogus' in msg or 'among us' in msg or 'sus' in msg:
        await message.channel.send("I can't fucking take it any more. Among Us has singlehandedly ruined my life. The "
                                   "other day my teacher was teaching us Greek Mythology and he mentioned a pegasus "
                                   "and I immediately thought 'Pegasus? more like Mega Sus!!!!' and I've never wanted "
                                   "to kms more. I can't look at a vent without breaking down and fucking crying. I "
                                   "can't eat pasta without thinking 'IMPASTA??? THATS PRETTY SUS!!!!' Skit 4 by "
                                   "Kanye West. The lyrics ruined me. A Mongoose, or the 25th island of greece. The "
                                   "scientific name for pig. I can't fucking take it anymore. Please fucking end my "
                                   "suffering.")


client.run('TOKEN')
