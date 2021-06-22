import discord
import os
import asyncio
import random

token = (os.getenv('TOKEN'))
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
async def ch_pr():
  await client.wait_until_ready()
  statuses = [f"in {len(client.guilds)} servers", ">help"]
  while not client.is_closed():
    status = random.choice(statuses)
    await client.change_presence(activity=discord.Game(name=status))
    await asyncio.sleep(9)
client.loop.create_task(ch_pr())    

@client.event
async def on_member_join(member):
   role = discord.utils.get(member.guild.roles, name = 'Skiddies') 
   guild = client.get_guild() # Guild ID
   welcome_channel = guild.get_channel() # Guild channel ID
   await member.add_roles(role)
   await welcome_channel.send(f'Welcome {member.mention} to the {guild.name} Discord Server\nYou are member number {member.guild.member_count}')
   await member.send(f'We are glad to have you {member.name}, in the {guild.name} Discord Server ')
   
@client.event
async def on_member_remove(member):
    if member.guild.id == : # Guild ID
       guild = client.get_guild() # Guild ID
       welcome_channel = guild.get_channel() # Guild channel ID
       await welcome_channel.send(f'{member.mention} has left the Discord Server :frowning:')
    else:    
        return

client.run(os.getenv("TOKEN"))
