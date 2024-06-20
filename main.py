#!/c/Users/miner/environments/venv_pablos-bot/Scripts/python
# módulo para conectar con .env
from decouple import Config, RepositoryEnv
# módulos para trabajar con la api de discord
from discord.ext import commands
from discord import Intents, ApplicationContext, Member

config = Config(RepositoryEnv('./private/.env'))
TOKEN = config('DISCORD_TOKEN')

intents = Intents.default() #permisos
intents.message_content = True 

#instancia del bot
bot = commands.Bot(command_prefix='>', intents = intents, owner_id = 295594807701798912 )

#DISCORD-CLIENTE
#DISCORD-BOT. MODULO POR DESARROLLADORES
#DISCORD

bot.load_extension("comandos") # cargo el cog comandos
bot.load_extension("eventos") # cargo el cog comandos

@bot.command("saludo")
async def comando(ctx: commands.Context): #el contexto recibe toda la información del mismo comando.
    await ctx.reply(f"Hola {ctx.author.mention}")

@bot.slash_command(name = "xd", description = "Usa este comando cuando no recuerdes usar el equisde")
async def xd(ctx: ApplicationContext,usuario: Member):
    await ctx.respond(f"ola xd {usuario.mention} ")

@bot.slash_command(name = "say", description = "muestra un mensaje xd")
async def chilito(ctx: ApplicationContext, usuario: Member):
    await ctx.respond(f"{usuario.mention} me toco mi chilito")

bot.run(TOKEN)
