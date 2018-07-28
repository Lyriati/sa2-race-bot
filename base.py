import discord
import logging

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
        race1 = "ready"
        race1_status = "ready"
        if race1 == "started":
            race1_status = "open"
        elif race1 != "started":
            race1_status = "closed"


    async def on_message(self, message):
        client.race1_status = "ready"

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!startrace'):
            race1 = "started"
            await client.send_message(message.channel, content="Race 1 Opened!")

        if message.content.startswith('!hello'):
            await client.send_message(message.channel, content="Hello!")

        if message.content.startswith('!races'):
            await client.send_message(message.channel, content=print(race1_status))





client = MyClient()
client.run('NDcyNDczMTcyODAyMDExMTM3.Dj1PeA.0PvrYUQX_uniVGMf1eeqajyP7w8')