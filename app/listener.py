# app/listener.py

import discord
from discord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Evitar que el bot responda a sus propios mensajes
        if message.author == self.bot.user:
            return

        # Buscar la palabra "java" en el contenido del mensaje
        if "java" in message.content.lower():
            # Obtener el emote por nombre
            emote = discord.utils.get(message.guild.emojis, name='8691lmfaostickersgg')
            if emote:
                await message.channel.send(f"javazzzzz {emote}")
            else:
                await message.channel.send("javazzzzz (emote no encontrado)")

def setup(bot):
    bot.add_cog(Listener(bot))
