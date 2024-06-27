# módulo para conectar con .env
from decouple import Config, RepositoryEnv

# módulos para trabajar con la api de discord
from discord.ext import commands
from discord import Intents

# conexión con la key|clave de mi archivo .env
config = Config(RepositoryEnv('./private/.env'))
TOKEN = config('DISCORD_TOKEN')
OWNER = int(config('OWNER_ID'))

intents = Intents.default() #permisos
intents.message_content = True 

#instancia del bot
bot = commands.Bot(command_prefix='>', intents = intents, owner_id = OWNER )

#Cargando extensiones de scripts de los comandos
extensiones = {
    "CoreConnect":"app.CoreConnect",
    "eventos":"app.eventos",
    "say":"app.say",
    "embed":"app.embed",
    "msg_auto":"app.msg_auto",
    "listener":"app.listener"
}

for ruta in extensiones.values():
    bot.load_extension(ruta)



bot.run(TOKEN)
