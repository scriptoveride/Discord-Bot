import discord
import os
import random
import asyncio

from discord.ext import commands

client = commands.Bot(command_prefix=">", help_command=None)

# START UP
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# HELP
@client.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(title='Help',
    description='To use me start with ">"',
    color=discord.Color(10181046))
    embed.add_field(name='General', value='hello, joi')
    embed.add_field(name='Tools', value='ping, clear, server', inline=False)
    embed.add_field(name='games', value='paperscissorsrock')
    embed.add_field(name='other', value='love')
    await ctx.send(embed=embed)

# JOI
@client.command(aliases=['Joi'])
async def joi(ctx):
    embed = discord.Embed(title='Hello, my name is Joi :purple_heart:', 
    description=f'Im a Discord bot witten in python\nIm in {len(client.guilds)} servers\n', 
    color=discord.Color(10181046))
    embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/853964068344037387/be40ad53535373a587b483985c737f61.png')
    await ctx.send(embed=embed)

# HELLO
@client.command()
async def hello(ctx):
    await ctx.send(f'Hello <@{ctx.author.id}>  :wave:')

# PING
@client.command()
async def ping(ctx):
    await ctx.send(f'ping {round (client.latency * 1000)}ms')

# CLEAR
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    if amount > 20:
       await ctx.send(f"{amount} messages is to many to delete at once")
    else:   
       await ctx.channel.purge(limit=amount + 1)     

# SERVER
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(title=name + " Server Information",
    color=discord.Color(10181046))
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)
 
client.run(os.getenv('TOKEN'))
