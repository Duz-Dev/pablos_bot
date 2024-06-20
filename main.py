# módulo para conectar con .env
from decouple import Config, RepositoryEnv

# módulos para trabajar con la api de discord
from discord.ext import commands
from discord import Intents, ApplicationContext, Member

# conexión con la key|clave de mi archivo .env
config = Config(RepositoryEnv('./private/.env'))
TOKEN = config('DISCORD_TOKEN')
OWNER = config('OWNER_ID')

intents = Intents.default() #permisos
intents.message_content = True 

#instancia del bot
bot = commands.Bot(command_prefix='>', intents = intents, owner_id = OWNER )

bot.load_extension("app.comandos") # cargo el cog comandos
bot.load_extension("app.eventos") # cargo el cog eventos

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
