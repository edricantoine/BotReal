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
    "Consider suicide",
    "Nobody cares that you feel that way",
    "Cope, seethe, mald",
    "Doin ur mom",
    "Cry more"
]
GUILD = os.getenv('Bot test')


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


client.run('TOKEN HERE')
