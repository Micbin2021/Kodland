import discord
import bcrypt
import random
import os


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
    await ctx.send(f"zahaszowane haslo: {bcrypt.hashpw(password.encode(), bcrypt.gensalt())}")

@bot.command()
async def rzut(ctx):
    mozliwosci = ("orzeł","reszka")
    wynik = random.choice(mozliwosci)
    await ctx.send(f'Rzut padł na {wynik}')

@bot.command()
async def image(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        await ctx.send(file=discord.File(f))

@bot.command()
async def zakupy(ctx):
    lista =  ["chleb", "mleko", "jajka"]
    await ctx.send(f'Twoje  zakupy to:{lista}')
    await ctx.send(f'Losowy produkt:{random.choice(lista)}')

@bot.command()
async def kolory(ctx,*x):
    color = {
        "czerwony": 0xFF0000,
        "niebieski": 0x0000FF,
        "zielony": 0x00FF00,
    }
    if x in color:
        await ctx.send(f'Kolor {x} to {color[x]}')
    else:
        await ctx.send(f'Nie znalem koloru {x}')

@bot.command()
async def pomysl(ctx):
    pomysly = {
        "papierowy samolot",
        "rysunek martwej natury",
        "papierowe kwiaty",
        "papierowe ptaki",
        "papierowe drzewa",
        "origami"
    }
    await ctx.send(f'Pomysł to: {random.choice(list(pomysly))}')

@bot.command()
async def sortowanie(ctx,x):
    lista = {
        "gazeta":"papier",
        "zabawka":"plastik",
        "butelka":"szkło",
        "kubek":"metal"
    }
    if x in lista:
        await ctx.send(f'Przedmiot {x} wrzuc do: {lista[x]}')
        
    

@bot.command()
async def rozklad(ctx, x):
    lista = {
        "guma":"5 lat",
        "butelka":"1 rok",
        "papier":"1 rok"
    }
    if x in lista:
        await ctx.send(f'Produkt {x} rozpadnie sie w {lista[x]}')
