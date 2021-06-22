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

@client.command()
async def trivia(ctx):

  i = random.randint(1,7)

  if i == 1:
    question = 'What part of the atom has no electric charge?'
    yellow = 'Electron'
    green = 'Neutron'
    red = 'Proton'
    blue = 'Nucleus'
    r1 = 'WRONG'
    r2 = 'CORRECT'
    r3 = 'WRONG'
    r4 = 'WRONG'  
  elif i == 2:  
    question = 'Which planet is the hottest in the solar system?'
    yellow = 'Mars'
    green = 'Jupiter'
    red = 'Earth'
    blue = 'Venus'
    r1 = 'WRONG'
    r2 = 'WRONG'
    r3 = 'WRONG'
    r4 = 'CORRECT'
  elif i == 3:  
    question = 'What is the symbol for potassium?'
    yellow = 'K'
    green = 'P'
    red = 'F'
    blue = 'Kr'
    r1 = 'CORRECT'
    r2 = 'WRONG'
    r3 = 'WRONG'
    r4 = 'WRONG'
  elif i == 4:  
    question = 'Which continent is the largest?'
    yellow = 'North America'
    green = 'Asia'
    red = 'Africa'
    blue = 'Antarctica'
    r1 = 'WRONG'
    r2 = 'CORRECT'
    r3 = 'WRONG'
    r4 = 'WRONG'
  elif i == 5:  
    question = 'What year did the movie "Hackers" come out in?'
    yellow = '1995'
    green = '1989'
    red = '1996'
    blue = '1999'
    r1 = 'CORRECT'
    r2 = 'WRONG'
    r3 = 'WRONG'
    r4 = 'WRONG'
  elif i == 6:  
    question = 'What year did the movie "Hackers" come out in?'
    yellow = '1995'
    green = '1989'
    red = '1996'
    blue = '1999'
    r1 = 'CORRECT'
    r2 = 'WRONG'
    r3 = 'WRONG'
    r4 = 'WRONG'
  elif i == 7:  
    question = 'Hg is the chemical symbol of which element?'
    yellow = 'Magnesium'
    green = 'Hydrogen'
    red = 'Mercury'
    blue = 'Zinc'
    r1 = 'WRONG'
    r2 = 'WRONG'
    r3 = 'CORRECT'
    r4 = 'WRONG'

  embed = discord.Embed(title='Trivia',
  description= question,
  color=discord.Color(10181046))
  embed.add_field(name=yellow, value= ':yellow_square:')
  embed.add_field(name=green, value= ':green_square:', inline=True)
  embed.add_field(name=red, value= ':red_square:', inline=True)
  embed.add_field(name=blue, value= ':blue_square:')
  message = await ctx.send(embed=embed)

  await message.add_reaction('🟨')
  await message.add_reaction('🟩')
  await message.add_reaction('🟥')
  await message.add_reaction('🟦')

  def check(reaction, user):
      return user == ctx.message.author and str(reaction.emoji) in ['🟨', '🟩', '🟥', '🟦']

  try:
      reaction, user = await client.wait_for('reaction_add', timeout=15, check=check)
    
      if reaction.emoji == '🟨':
          await ctx.send(r1)
          return

      elif reaction.emoji == '🟩':
          await ctx.send(r2)
          return

      elif reaction.emoji == '🟥':
          await ctx.send(r3)
          return

      elif reaction.emoji == '🟦':
          await ctx.send(r4)
          return     

  except asyncio.TimeoutError:
      await ctx.send("Timed out")

client.run(os.getenv("TOKEN"))
