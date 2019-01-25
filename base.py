import discord
import random
import asyncio
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    countdown = 10
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        if message.author.id == 83299750824120320:
            await message.channel.send("Goodbye Lyri.")
        else:
            await message.channel.send('Hello!')

    if message.content == '$countdown':
        if message.author.id == 83299750824120320:
            await message.channel.send("No countdown for you!")
        else:
            await message.channel.send("The race is starting!")
            await asyncio.sleep(1)
            for j in range(1):
                await message.channel.send(str(countdown) + " seconds!")
                await asyncio.sleep(5)
            countdown = 5
            for i in range(5):
                await message.channel.send(str(countdown))
                await asyncio.sleep(1)
                countdown = countdown - 1
            await asyncio.sleep(0)
            await message.channel.send("Go!")


client.run('NDcyNDczMTcyODAyMDExMTM3.Dy0LQA.z3sK1LOVLg1i05U7JG2fhlTemgU')
