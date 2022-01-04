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
GUILD = 'GUILD_NAME_HERE'


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
        await message.channel.send('Howdy')

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


client.run('TOKEN')
