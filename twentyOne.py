import random
import os
import asyncio


class twentyOne:

    def __init__(self, client):
        self.__running = False
        self._client = client
        self.__channel = None
        self.__p1turn = True
        self.__1hors = None
        self.__2hors = None
        self.__s1 = 0
        self.__s2 = 0
        self.__p1name = "Player 1"
        self.__p2name = "Player 2"

    async def set_name_1(self, name):
        self.__p1name = name

    async def set_name_2(self, name):
        self.__p2name = name

    async def setChannel(self, channel):
        self.__channel = channel

    def started(self):
        return self.__running

    def isp1turn(self):
        return self.__p1turn

    async def onehit(self):
        self.__1hors = True

    async def twohit(self):
        self.__2hors = True

    async def onestay(self):
        self.__1hors = False

    async def twostay(self):
        self.__2hors = False

    async def changeTurntoP2(self):
        self.__p1turn = False

    async def changeTurntoP1(self):
        self.__p1turn = True

    async def start(self, channel):
        if self.__running:
            await self.__channel.send('A game of 21 is in progress already, in channel {}. You can '
                                      'stop '
                                      'it with !stop.')
        else:
            await self.reset()
            self.__channel = channel
            await self.__channel.send('@here Starting game of 21!')
            self.__running = True
            await self.turn1()

    async def turn1(self):

        await self.print()
        await self.__channel.send(self.__p1name + '. Will you hit or stay?')

    async def turn2(self):
        await self.__channel.send(self.__p2name + '. Will you hit or stay?')

    async def addToScores(self):
        rand1 = random.randrange(1, 10)
        rand2 = random.randrange(1, 10)

        if self.__1hors:
            self.__s1 += rand1
        if self.__2hors:
            self.__s2 += rand2

        await self.checkForWinner()

    async def checkForWinner(self):
        if self.__s1 == 21:
            await self.print()
            await self.__channel.send(self.__p1name + ' has exactly 21! ' + self.__p1name + ' wins.')
            await self.stop()
        elif self.__s2 == 21:
            await self.print()
            await self.__channel.send(self.__p2name + ' has exactly 21! ' + self.__p2name + ' wins.')
            await self.stop()

        elif self.__s1 > 21 and self.__s2 <= 21:
            await self.print()
            await self.__channel.send(self.__p1name + ' went over 21! ' + self.__p2name + ' wins.')
            await self.stop()

        elif self.__s2 > 21 and self.__s1 <= 21:
            await self.print()
            await self.__channel.send(self.__p2name + ' went over 21! ' + self.__p1name + ' wins.')
            await self.stop()
        elif self.__s2 > 21 and self.__s1 > 21:
            await self.print()
            await self.__channel.send('Both players went over 21! Too bad! Nobody wins.')
            await self.stop()
        else:
            await self.turn1()

    async def reset(self):
        if self.__running:
            await self.stop()
        self.__s1 = 0
        self.__s2 = 0
        self.__p1turn = True

    async def stop(self):
        if self.__running:
            await self.__channel.send('Stopping game. Final scores are...')
            await self.print()
            self.__running = False
        else:
            await self.__channel.send('No game has been started yet! Start one with "!21".')

    async def print(self):
        if self.__running:
            await self.__channel.send('Game scores:')
            await self.__channel.send(self.__p1name + ': {}'.format(self.__s1))
            await self.__channel.send(self.__p2name + ': {}'.format(self.__s2))
        else:
            await self.__channel.send('No game is currently active.')
