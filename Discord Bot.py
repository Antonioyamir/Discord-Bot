import discord 
from discord.ext import commands

intents = discord.Intents.default() #como añadir privilegios de discord
intents.message_content = True #como activar para leer mensajes

bot = commands.Bot(command_prefix='/', intents=intents) # letras con que se puede ahcer el comand por ejemplo: /hola !hola

@bot.event
async def on_ready():
    print(f'Hola, me he iniciado como {bot.user}')

@bot.command()
async def heh(ctx, count_heh = 5): #ctx para leer mensajes}
    await ctx.send('he' * count_heh)

@bot.command()
async def mrbeast(ctx, count_mrbeast = 3): #ctx para leer mensajes}
    await ctx.send('mrbeast' * count_mrbeast)

token = 'MTI1OTk5MTIxNzM4NzYwNjExNw.GEJ6XQ.P7A1weqs_ATH4gQF8K_VhRMSWFKy44BrdN40fI'
bot.run(token)
