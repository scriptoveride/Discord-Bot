import discord
import random
import os
import asyncio

from discord.ext import commands

client = commands.Bot(command_prefix=">", help_command=None)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.command(aliases=['paperscissorsrock'])
async def psr(ctx):
    msg = await ctx.send("Paper, Scissors or Rock?")

    await msg.add_reaction("🧻")
    await msg.add_reaction("✂️")
    await msg.add_reaction("🪨")

    botchoice = random.randint(1,3)

    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) in ['🧻', '✂️', '🪨']

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10, check=check)
    
        if reaction.emoji == '🧻':
          if botchoice == 1:
            await ctx.send("DRAW  :roll_of_paper: = :roll_of_paper:")
          elif botchoice == 2:
            await ctx.send("LOSE  :roll_of_paper:  <  :scissors:")  
          elif botchoice == 3:
            await ctx.send("WIN  :roll_of_paper:  >  :rock:") 
          return

        elif reaction.emoji == '✂️':
          if botchoice == 1:
            await ctx.send("WIN  :scissors: > :roll_of_paper:")
          elif botchoice == 2:
            await ctx.send("DRAW  :scissors:  =  :scissors:")  
          elif botchoice == 3:
            await ctx.send("LOSE  :scissors: < :rock:") 
          return

        elif reaction.emoji == '🪨':
          if botchoice == 1:
            await ctx.send("LOSE  :rock:  <  :roll_of_paper:")
          elif botchoice == 2:
            await ctx.send("WIN  :rock:  >  :scissors:")  
          elif botchoice == 3:
            await ctx.send("DRAW  :rock:  =  :rock:") 
          return

    except asyncio.TimeoutError:
        await ctx.send("Timed out")

client.run(os.getenv("TOKEN"))
