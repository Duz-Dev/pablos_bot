# módulo para conectar con .env
from decouple import Config, RepositoryEnv

# módulos para trabajar con la api de discord
from discord.ext import commands
from discord import Intents

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
bot.load_extension("app.say") # cargo el cog say

bot.run(TOKEN)
