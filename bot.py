import discord
import requests
import json
import random
from random import *
import time

Version = "1.3.2"
client = discord.Client()

def get_quote():
    response = requests.get("Https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " - " + json_data[0]["a"]
    return (quote)


phrases_to_complain_with = [
    "Hey, Timebot, your'e getting annoying",
    "Could you stop, like PLEASE?",
    "Why did <@763802866921242646> even make you?",
    "Awake listening to timebot 24/7. Ugh",
    "F**king Mutter Mutter Grrr"
]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!help"):#help menu
        await message.channel.send("List of commands:\n!help    displays help prompt(duh),\n!info    displays bot info,\n!inspire    displays an inspiring quote,\n!diceroll    rolls a dice")
        print("Displayed help")

    if message.content.startswith("!info"):#info about the bot
        await message.channel.send("Griffinbot\nCreator: Superbee\nVersion " + Version + "\nProgrammed in python")
        print("Displayed Bot Info To Users")

    if message.content.startswith("!inspire"):#inspirational quote
        quote = get_quote()
        await message.channel.send(quote)
        print("Displayed Quote [" + quote + "]")
        
    if message.content.startswith("It is currently"):
        await message.channel.send(phrases_to_complain_with[randint(1, 5)])#conversation with timebot every hour
        time.sleep(0.5)
        x = requests.post('https://discord.com/api/webhooks/796523416630984704/4U9LYkbW2d1rc06r91uEIfGHv8spzetUy1-JjoXX9dc-Hz7hSPOzQfLzKPLCtJl5Wbws', data = {'content': "That's not nice!"})
        print("Complained About Timebot")

    if message.content.startswith("!diceroll"):#roll a die
        x = randint(1, 6)
        if x==1:
            await message.channel.send(":blue_square::blue_square::blue_square:\n:blue_square::record_button::blue_square:\n:blue_square::blue_square::blue_square:")

        if x==2:
            await message.channel.send(":record_button::blue_square::blue_square:\n:blue_square::blue_square::blue_square:\n:blue_square::blue_square::record_button:")

        if x==3:
            await message.channel.send(":record_button::blue_square::blue_square:\n:blue_square::record_button::blue_square:\n:blue_square::blue_square::record_button:")

        if x==4:
            await message.channel.send(":record_button::blue_square::record_button:\n:blue_square::blue_square::blue_square:\n:record_button::blue_square::record_button:")

        if x==5:
            await message.channel.send(":record_button::blue_square::record_button:\n:blue_square::record_button::blue_square:\n:record_button::blue_square::record_button:")

        if x==6:
            await message.channel.send(":record_button::blue_square::record_button:\n:record_button::blue_square::record_button:\n:record_button::blue_square::record_button:")
        print("rolled a die")
        
client.run("(bot id)")#this this is where the bot's id goes
