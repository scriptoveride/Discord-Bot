import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix=">", help_command=None)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

words = ["fuck",] #add words you want to moderate here

@client.event
async def on_message(message):
    if any(word in message.content.lower() for word in words):
        await message.delete()  

client.run(os.getenv("TOKEN"))
