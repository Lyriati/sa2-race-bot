import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Current discord.py version")
        print(discord.__version__)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('---------')
        print("Ready!")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await client.send_message(message.channel, content="Hello!")

        if message.content.startswith('!races'):
            await client.send_message(message.channel, content="Currently: No races")

client = MyClient()
client.run('NDcyNDczMTcyODAyMDExMTM3.Dj1PeA.0PvrYUQX_uniVGMf1eeqajyP7w8')