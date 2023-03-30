from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import requests
intents = discord.Intents.default()

load_dotenv()


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')

# Slash commands


@bot.slash_command(name='ping', description='Pong!!!!')
async def _ping(ctx):
    await ctx.respond('Pong!')


@bot.slash_command(name='quote', description='Random Quote')
async def _quote(ctx):
    r = requests.get('https://api.quotable.io/random')
    quote = r.json()['content']
    author = r.json()['author']
    await ctx.respond(quote+" ~ "+author)


@bot.slash_command(name='joke', description='Random Joke')
async def _joke(ctx):
    r = requests.get('https://official-joke-api.appspot.com/random_joke')
    setup = r.json()['setup']
    punchline = r.json()['punchline']
    await ctx.respond(f"{setup} \n || {punchline} ||")


# bot.run(os.environ.get('TOKEN'))

print(os.environ.get('TOKEN'))
