import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    for member in guild.members:
        print(member.name)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = 'shut up josh'

    if message.content == 'what' and message.channel.name == 'test':
        await message.channel.send(response)

client.run(TOKEN)