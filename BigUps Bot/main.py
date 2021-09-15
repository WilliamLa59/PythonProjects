import discord
from discord.ext import commands
import os
import music 

token = os.environ['TOKEN']
cog = [music]
client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

for i in range(len(cog)):
  cog[i].setup(client)

#@client.event
#async def on_ready():
#  print('logged in as {0.user}'.format(client))

#@client.event
#async def on_message(message):
#  if message.author == client.user:
#    return

#  if message.content.startswith('!yo'):
#    await message.channel.send('yo big ups my guy')

client.run(token)
