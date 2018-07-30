import discord
import logging
import time

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

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!startrace'):
            self.race1 = "started"
            await client.send_message(message.channel, content="Race 1 Opened!")
            if self.race1 == "started":
                self.race1_status = "open"
            elif self.race1 != "started":
                self.race1_status = "closed"

        if message.content.startswith('!hello'):
            await client.send_message(message.channel, content="Hello!")

        if message.content.startswith('!race1'):
            await client.send_message(message.channel, content=self.race1_status)

        if message.content.startswith('!stoprace1'):
            self.race1 = "stopped"
            if self.race1 == "started":
                self.race1_status = "open"
            elif self.race1 != "started":
                self.race1_status = "closed"
            await client.send_message(message.channel, content="Race 1 Stopped!")

        if message.content.startswith('!allready'):
            await client.send_message(message.channel, content='10')
            time.sleep(1)
            await client.send_message(message.channel, content='9')
            time.sleep(1)
            await client.send_message(message.channel, content='8')
            time.sleep(1)
            await client.send_message(message.channel, content='7')
            time.sleep(1)
            await client.send_message(message.channel, content='6')
            time.sleep(1)
            await client.send_message(message.channel, content='5')
            time.sleep(1)
            await client.send_message(message.channel, content='4')
            time.sleep(1)
            await client.send_message(message.channel, content='3')
            time.sleep(1)
            await client.send_message(message.channel, content='2')
            time.sleep(1)
            await client.send_message(message.channel, content='1')
            time.sleep(1)
            await client.send_message(message.channel, content='Go!')






client = MyClient()
client.run('xxxxxxx')
