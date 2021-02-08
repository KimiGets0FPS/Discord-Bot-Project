import discord
from discord.ext import commands
# from discord.ext.commands import Bot

from dotenv import load_dotenv
# import csv
# import asyncio

import random as r
import os

# data = open('C:/Users/zhewe/Coding Projects/Discord-Bot-Project/Discord Bot/data_for_users.csv')


load_dotenv('bot_token.env')
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('BOT_GUILD')


Client = discord.Client()
client = commands.Bot(command_prefix="%")


# Boot up signal
@client.event
async def on_ready():
    print(f"Token: {len(TOKEN) * 'X'}, GUILD:{GUILD}; Bot is ready to operate!")


# TODO: FIX ERROR
@client.command()
async def error(message):
    await message.channel.send(f'There is no such command {message.author.mention}!')


# Kills crewmates
@client.command(name='kill', help='Kills random amounts of people (Still in progress)')
async def kill_things(message):
    kills = r.choice([0, 0, 0, 1, 1, 2])
    if kills == 0:
        await message.channel.send(f'OOF! Nobody was there {message.author.mention} :(')
    else:
        if kills == 2:
            await message.channel.send(f"{message.author.mention} got caught getting 2 kills!")
        else:
            await message.channel.send(f'\nWow, {message.author.mention} got {kills} kill!')


# Finding things
@client.command(name='search', help="\n\nPlace list: Electrical, Admin, Lower Engine, Upper "
                                    "Engine, O2, Cafeteria, Navigation, Reactor, Medbay, Weapons, Shields, Storage"
                                    "\n\nBased on the map Skield in the real game.")
async def search(message, place_to_search=''):
    things_you_can_get = ['knife', 'coins', 'massive Tongue', 'hair dyer', "crewmate's keycard", 'nothing', 'missile',
                          'nothing', 'nothing', 'ejected', 'gun']
    places = ['Electrical', 'Admin', 'Lower Engine', 'Upper Engine', 'O2', 'Cafeteria', 'Navigation', 'Reactor',
              'Medbay', 'Weapons', 'Shields', 'Storage']
    if not place_to_search:
        await message.channel.send("You have to enter a place you want to search!")
    else:
        if place_to_search and place_to_search.title() in places:
            wat_u_get = r.choice(things_you_can_get)
            wat_u_get_2 = r.choice(things_you_can_get)

            if wat_u_get == 'ejected' or wat_u_get_2 == 'ejected':
                await message.channel.send(f"{message.author.mention} got caught doing some 'sus' stuff, and got "
                                           "ejected!")

            elif wat_u_get == 'nothing':
                await message.channel.send(f'{message.author.mention} got {wat_u_get_2}')

            elif wat_u_get_2 == 'nothing':
                await message.channel.send(f'{message.author.mention} got {wat_u_get}')

            elif wat_u_get and wat_u_get_2 == 'nothing':
                await message.channel.send(f'{message.author.mention} got nothing!')

            else:
                await message.channel.send(f'{message.author.mention} got a {wat_u_get} and a {wat_u_get_2}!')

        else:
            await message.channel.send(f'What are you even thinking {message.author.mention}, '
                                       'that is not a available place to search/do your business.')


# @client.command(name='inv', help='Use this command to see what is inside your inventory! (Still in progress'
#                                  'progress for storing your data')
# async def inventory(message):
#     await message.channel.send(f"Still in progress {message.author.mention}!(This will probably take a while...)")

client.run(TOKEN)
