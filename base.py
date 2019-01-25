import discord
import logging
import asyncio

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class MyClient(discord.Client):
    async def on_ready(self):
        print("Current discord.py version")
        print(discord.__version__)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('---------')
        print("Ready!")


 # race management
        self.race1 = "ready"
        self.race1_status = "Race 1 Ready!"
        if self.race1 == "started":
            self.race1_status = "open"
        elif self.race1 != "started":
            self.race1_status = "closed"


    async def on_message(self, message):

        countdown = 10
        
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!startrace'):
            race1 = "started"
            await client.send_message(message.channel, content="Race 1 Opened!"

        if message.content.startswith('!hello'):
            await client.send_message(message.channel, content="Hello!")

        if message.content.startswith('!race1'):
            await client.send_message(message.channel, content= str(race1_status))
           
        if message.content.startswith('!allready'):
            for i in range(10):
                await client.send_message(message.channel, content=str(countdown))
                countdown = countdown - 1
            print("Go!")







client = MyClient()
client.run('xxxxxxx')
