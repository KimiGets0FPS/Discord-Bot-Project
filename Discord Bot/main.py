import discord
from discord.ext import commands

from dotenv import load_dotenv
# import csv

import random as r
import os

# data = open('C:/Users/zhewe/Coding Projects/Discord-Bot-Project/Discord Bot/data_for_users.csv')


load_dotenv('bot_token.env')
TOKEN = os.getenv('BOT_TOKEN')

Client = discord.Client()
client = commands.Bot(command_prefix="%")


# Boot up signal
@client.event
async def on_ready():
    print(f"Token: {len(TOKEN) * 'X'}; Bot is ready to operate!")


@client.event
async def on_command_error(ctx, message):
    if isinstance(message, Exception):
        await ctx.send(f"There is no such command!")


with open('badwords.txt') as file:
    file = file.read().split()


@client.command(name='bet', help='Bet against your opponent!')
async def bet(message):
    message.channel.send(f"{message.author.mention} got {r.randint(0, 100)}"
                         f" and his/her opponent got {r.randint(0, 100)}!")
    return


@client.command(name='dice', help='Randomly rolls a dice for you(numbers 1-6)! Do: %roll <number of dices! (optional, '
                                  'default is 1)>')
async def dice(message, number=1):
    if number == 1:
        await message.channel.send(f"{message.author.mention}, your number is {r.randint(1, 6)}")
    elif number > 100:
        await message.channel.send(f"{message.author.mention} your number is too big!")
    else:
        rolls = []
        for i in range(number):
            rolls.append(str(r.randint(1, 6)))
        await message.channel.send(f"{message.author.mention}, your numbers are: {', '.join(rolls)}")


@client.command(name='slap', help='FUN! Slapping people is disrespectful, but it sure is FUN!')
async def slap(message, victim):
    if victim:
        await message.send(f'{message.author.mention} just slapped {victim}!')
        return
    await message.send(f'{message.author.mention} just slapped {client.user.mention}')


@client.command(name="ping", help="Hey! What's your ping?")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

# I must get clout


@client.command(name='youtube', help='Gives you the link for my Youtube Channel!')
async def youtube(message):
    await message.channel.send(f"{message.author.mention} here is the Youtube link:"
                               f"\n https://www.youtube.com/channel/UC9J0m0MVZvpa27R8iMnL9bg")


@client.command(name='patreon', help='Gives you the link for my Patreon page!')
async def patreon(message):
    await message.channel.send(f"{message.author.mention} here is the Patreon link:"
                               f"\n https://www.patreon.com/KimiGets0FPS?fan_landing=true")


@client.command(name='twitter', help='Gives you the link for my Twitter! Follow me!')
async def twitter(message):
    await message.channel.send(f"{message.author.mention} here is the Twitter link:"
                               f"\n https://twitter.com/K0fps")


client.run(TOKEN)
