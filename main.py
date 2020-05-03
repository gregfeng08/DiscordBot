import discord
import math
import random
from array import *
from discord.ext.commands import Bot


client = discord.Client()
array_new = array


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.find(".help") != -1:
        await message.channel.send("Current Commands: \n"
                                   ".spam [irl name] \n"
                                   ".hello \n"
                                   ".8ball [question] \n"
                                   ".botsays [message]"
                                   "")

    if message.content.find(".hello") != -1:
        await message.channel.send("Hi")

    if message.content.startswith(".insult"):
        who = message.content[8:].upper()
        if (who == "ME"):
            await message.channel.send(who)
            await message.channel.send("Error Message")
        else:
            await message.channel.send(who)
            await message.channel.send("Normal Insult")

    if message.content.startswith(".list"):
        add = eval(message.content[6:].upper())
        array_new.append(add)
        await message.channel.send(add)
        await message.channel.send(array_new)



    if message.content.startswith(".8ball"):
        randomNumber = random.randint(1, 2)
        if randomNumber == 1:
            await message.channel.send("Yes")
        if randomNumber == 2:
            await message.channel.send("No")

    if message.content.startswith(".spam"):
        userInput = message.content[6:].upper()

        if(userInput == "KIMBERLY"):
            for i in range(0,3):
                await message.channel.send("<@544336783803154452>")
        if(userInput == "STEVEN"):
            for i in range(0,3):
                await message.channel.send("<@524727009528774667>")
        if(userInput == "ERIC"):
            for i in range(0,3):
                await message.channel.send("<@525828118318153768>")
        if (userInput == "THERESA"):
            for i in range(0,3):
                await message.channel.send("<@330006903339876352>")
        if (userInput == "ALLAN"):
            for i in range(0, 3):
                await message.channel.send("<@!354844813259964416>")
        if (userInput == "GREG"):
            for i in range(0, 3):
                await message.channel.send("<@!308806743511531523>")

    if message.content.startswith(".botsays"):
        await message.delete()
        msg = message.content[9:]
        await message.channel.send(msg)

    if message.content.startswith(".giveaway"):
        userid=message.author.id
        free = message.content[10:]
        await message.channel.send("Everyone, "+message.author.name+" is giving away a "+free+"! React below with a ✅ to participate in the giveaway!")
        await message.delete()

# @client.event
# async def on_reaction_add(reaction, user):
#     if (reaction.message.content == "asdf"):
#         await client.send_message(user.name+" has reacted to the giveaway!")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NzA0NjIwMjI3NjE0MjEyMTM3.Xqf7Fw.PpyIfQebssoICPWUTnLjRy95ROc')