import discord
import bcrypt
import random

intents = discord.Intents.default()
intents.message_content = True
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def hej(ctx):
    await ctx.send('Hej Hej !')

@bot.command()
async def powtarzanie(ctx, count=5):
    await ctx.send('test ' * count)

@bot.command()
async def suma(ctx, a: int, b: int):
    await ctx.send(f'Suma liczb {a} + {b} = {a + b}')

@bot.command()
async def generator(ctx,lenght: int):
    symbols = "+-/*?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(lenght):
        password += random.choice(symbols)
    await ctx.send(f'Twoje hasło to: {password}')

@bot.command()
async def rzut(ctx):
    mozliwosci = ("orzeł","reszka")
    wynik = random.choice(mozliwosci)
    await ctx.send(f'Rzut padł na {wynik}')



bot.run('')
