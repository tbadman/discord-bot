import os
import discord
import requests
from dotenv import load_dotenv
import json
import random

load_dotenv()
TOKEN = os.getenv('CYBERMAN_TOKEN')
GUILD = 'The Granite State Gang'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == 'mmm-boc' or message.channel.name == 'shitty-games-and-shittier-beer':

        if message.content.lower() == 'catfact':
            url = "https://catfact.ninja/fact?limit=1"
            payload={}
            headers = {
                'Accept': 'application/json'
            }

            response = requests.request("GET", url, headers=headers, data=payload).json()
            await message.channel.send(response['fact'])

        if message.content.lower() == 'dogfact':
            dogFile = 'dog_facts.json'

            with open(dogFile, 'r') as f:
                dogFacts = json.loads(f.read())
                factNumber = random.randint(0, len(dogFacts)-1)

            await message.channel.send(dogFacts[factNumber]['fact'])

        if message.content.lower() == 'bearfact':
            await message.channel.send('Bears occasionally shit in the woods.')


        if message.content.lower() == 'change name':

            await member.edit(nick='test')

        # if message.content == 'Excuse me, Cyberbot?':
        #     await message.channel.send('what?')
        # if message.content == 'Who is the dumbest person in this channel?':
        #     await message.channel.send('Obviously Cameron.')
        

client.run(TOKEN)

