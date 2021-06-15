
import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix=">",help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('>help'))
    print('We have logged in as {0.user}'.format(client))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.command()
async def hello(ctx):
    await ctx.send(f'Hello <@{ctx.author.id}>  :wave:')
    
    
client.run(os.getenv('TOKEN'))
