import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from news_api import NewsFromBBC
from advice_slip_api import advice_slip
from openWeather_api import openWeatherApi

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello! from j.p.dawer')
    if message.content.startswith('hii'):
        await message.channel.send('Hello! from j.p.dawer')
    if message.content.startswith('hi all'):
        await message.channel.send('Hello! from j.p.dawer')
    if message.content.startswith('@everyone'):
        await message.channel.send('Hello! from j.p.dawer')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$news'):
        await message.channel.send(NewsFromBBC())

    if message.content.startswith('$advice'):
        await message.channel.send(advice_slip())

    if message.content.startswith('$weather'):
        await message.channel.send(openWeatherApi())

    msg = message.content

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
        quote = get_quote()
        await message.channel.send(quote)


keep_alive() #this is for non sleep server runing process do not delete this.
client.run(os.getenv('TOKEN')) #this is token for server so do not change this server
