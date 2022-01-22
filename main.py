import os
import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

# token = os.environ.get("TOKEN")

token=""
with open("token.txt") as file:
    token=file.read()

client.run(token)
