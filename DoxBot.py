import discord, os, random
from bot_logic import *
from discord.ext import commands

intents = discord.Intents.default() # almacenamiento de los privilegios del bot
intents.message_content = True # Activar lectura de mensajes
bot = commands.Bot(command_prefix="/",intents=intents) # Creacion de bot y transferencia de los privilegios

@bot.event
async def on_ready():
    print(f'1,2,3. Dox, conectado al sistema como: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hola, ¿en que puedo ayudarle?")

@bot.command()
async def bye(ctx):
    await ctx.send("Nos vemos")

@bot.command()
async def password(ctx, longitud: int=5):
    await ctx.send(gen_pass(longitud))

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def whenJoined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    random_mem = random.choice(os.listdir("images"))
    
    with open(f'images/{random_mem}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("aqui tu mmm... como se llame")
