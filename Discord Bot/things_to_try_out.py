import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

data = open('C:/Users/zhewe/Coding Projects/Discord-Bot-Project/Discord Bot/data_for_users.csv')
load_dotenv('bot_token.env')
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f"Token: {len(TOKEN) * 'X'} Bot is ready to operate!")


class Test:
    def startup(self):
        ...


@client.event
async def start(message):
    test = Test()


client.run(TOKEN)
